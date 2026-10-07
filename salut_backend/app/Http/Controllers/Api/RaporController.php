<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use App\Models\AcademicRecord;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;
use Tymon\JWTAuth\Facades\JWTAuth;

class RaporController extends Controller
{
    /**
     * GET /api/guru/rapor/students
     */
    public function getSiswaList(Request $request): JsonResponse
    {
        $guru = JWTAuth::user();
        if ($guru->role !== 'guru' && $guru->role !== 'admin') {
            return response()->json(['message' => 'Akses ditolak.'], 403);
        }

        // Get all students. Can add filters later
        $query = User::where('role', 'siswa');
        
        if ($request->has('class')) {
            $query->where('class_name', $request->class);
        }
        
        $students = $query->orderBy('name')->get(['id', 'name', 'nisn', 'class_name']);

        return response()->json(['success' => true, 'data' => $students]);
    }

    /**
     * GET /api/guru/rapor/students/{id}
     */
    public function getStudentRapor($id): JsonResponse
    {
        $guru = JWTAuth::user();
        if ($guru->role !== 'guru' && $guru->role !== 'admin') {
            return response()->json(['message' => 'Akses ditolak.'], 403);
        }

        $student = User::where('role', 'siswa')->findOrFail($id);
        $records = AcademicRecord::where('user_id', $id)->orderBy('semester')->get();

        return response()->json([
            'success' => true,
            'student' => ['id' => $student->id, 'name' => $student->name, 'nisn' => $student->nisn, 'class_name' => $student->class_name],
            'records' => $records
        ]);
    }

    /**
     * POST /api/guru/rapor/students/{id}
     */
    public function storeRapor(Request $request, $id): JsonResponse
    {
        $guru = JWTAuth::user();
        if ($guru->role !== 'guru' && $guru->role !== 'admin') {
            return response()->json(['message' => 'Akses ditolak.'], 403);
        }

        $validated = $request->validate([
            'semester'      => 'required|integer|min:1|max:6',
            'average_score' => 'required|numeric|min:0|max:100',
            'rank'          => 'nullable|integer|min:1',
            'academic_year' => 'required|integer',
        ]);

        $record = AcademicRecord::updateOrCreate(
            ['user_id' => $id, 'semester' => $validated['semester']],
            [
                'average_score' => $validated['average_score'],
                'rank'          => $validated['rank'],
                'academic_year' => $validated['academic_year'],
                'status'        => 'Tervalidasi',
                'input_by'      => $guru->id,
            ]
        );

        return response()->json([
            'success' => true,
            'message' => 'Nilai rapor berhasil disimpan.',
            'data'    => $record
        ]);
    }
}
