<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\TracerStudy;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Tymon\JWTAuth\Facades\JWTAuth;

/** REQ-F-08: Form dinamis Tracer Study untuk Alumni pasca-lulus */
class TracerStudyController extends Controller
{
    /** GET /api/tracer-study — Cek apakah alumni sudah mengisi */
    public function show(): JsonResponse
    {
        $user   = JWTAuth::user();
        $tracer = TracerStudy::where('user_id', $user->id)->first();

        return response()->json([
            'success'      => true,
            'has_filled'   => !is_null($tracer),
            'data'         => $tracer,
        ]);
    }

    /** POST /api/tracer-study — Simpan atau update data tracer study */
    public function store(Request $request): JsonResponse
    {
        $user = JWTAuth::user();

        $validated = $request->validate([
            'status'       => 'required|string|max:100',
            'nama_instansi'=> 'nullable|string|max:255',
            'kota'         => 'nullable|string|max:100',
            'tahun_masuk'  => 'nullable|digits:4',
            'jabatan'      => 'nullable|string|max:100',
            'prodi'        => 'nullable|string|max:100',
            'keterangan'   => 'nullable|string',
        ]);

        $tracer = TracerStudy::updateOrCreate(
            ['user_id' => $user->id],
            array_merge($validated, ['user_id' => $user->id])
        );

        return response()->json([
            'success' => true,
            'message' => 'Terima kasih! Data Tracer Study berhasil disimpan.',
            'data'    => $tracer,
        ], 201);
    }
}