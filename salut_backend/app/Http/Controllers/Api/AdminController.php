<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Achievement;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Tymon\JWTAuth\Facades\JWTAuth;

/** Endpoint khusus Admin dan Guru */
class AdminController extends Controller
{
    /** GET /api/admin/achievements — Semua prestasi (untuk validasi Guru) */
    public function listAchievements(Request $request): JsonResponse
    {
        $user = JWTAuth::user();
        if (!$user->isGuru() && !$user->isAdmin()) {
            return response()->json(['message' => 'Tidak diizinkan.'], 403);
        }

        $query = Achievement::with('user:id,name,nisn,class_name,angkatan')
            ->orderBy('created_at', 'desc');

        if ($request->has('status')) {
            $query->where('status_validasi', $request->status);
        }

        return response()->json(['success' => true, 'data' => $query->paginate(20)]);
    }

    /**
     * PATCH /api/admin/achievements/{id}/validate
     * REQ-NF-03: Guru memvalidasi prestasi siswa.
     */
    public function validateAchievement(Request $request, Achievement $achievement): JsonResponse
    {
        $guru = JWTAuth::user();
        if (!$guru->isGuru() && !$guru->isAdmin()) {
            return response()->json(['message' => 'Tidak diizinkan.'], 403);
        }

        $request->validate([
            'status'  => 'required|in:Approved,Rejected',
            'catatan' => 'nullable|string',
        ]);

        $achievement->update([
            'status_validasi' => $request->status,
            'catatan'         => $request->catatan,
            'validated_by'    => $guru->id,
            'validated_at'    => now(),
        ]);

        return response()->json([
            'success' => true,
            'message' => "Prestasi berhasil di-{$request->status}.",
        ]);
    }

    /**
     * POST /api/admin/users — Tambah siswa baru (Admin only)
     */
    public function createUser(Request $request): JsonResponse
    {
        $admin = JWTAuth::user();
        if (!$admin->isAdmin()) {
            return response()->json(['message' => 'Hanya Admin.'], 403);
        }

        $validated = $request->validate([
            'name'       => 'required|string|max:100',
            'nisn'       => 'required|digits:10|unique:users,nisn',
            'email'      => 'nullable|email|unique:users,email',
            'password'   => 'required|min:6',
            'role'       => 'required|in:siswa,alumni,guru,admin',
            'class_name' => 'nullable|string|max:20',
            'angkatan'   => 'nullable|digits:4',
            'phone'      => 'nullable|string|max:20',
        ]);

        $user = User::create([
            ...$validated,
            'password' => Hash::make($validated['password']),
            'school'   => 'SMA Negeri 1 Teladan',
        ]);

        return response()->json([
            'success' => true,
            'message' => "Akun {$validated['role']} berhasil dibuat.",
            'data'    => ['id' => $user->id, 'name' => $user->name, 'nisn' => $user->nisn],
        ], 201);
    }

    /**
     * PATCH /api/admin/users/{id}/promote
     * REQ-F-07: Transisi manual Siswa → Alumni oleh Admin.
     * (Otomatis dijalankan via cron job saat jadwal pengumuman tiba)
     */
    public function promoteToAlumni(User $user): JsonResponse
    {
        $admin = JWTAuth::user();
        if (!$admin->isAdmin()) {
            return response()->json(['message' => 'Hanya Admin.'], 403);
        }

        if (!$user->isSiswa()) {
            return response()->json(['message' => 'User bukan Siswa Aktif.'], 422);
        }

        $user->update(['role' => 'alumni', 'graduation_date' => now()]);

        return response()->json([
            'success' => true,
            'message' => "{$user->name} berhasil dipromosikan menjadi Alumni.",
        ]);
    }

    /** GET /api/admin/stats — Dashboard statistik untuk web admin */
    public function stats(): JsonResponse
    {
        $admin = JWTAuth::user();
        if (!$admin->isAdmin() && !$admin->isGuru()) {
            return response()->json(['message' => 'Tidak diizinkan.'], 403);
        }

        return response()->json([
            'success' => true,
            'data' => [
                'total_siswa'         => User::where('role','siswa')->count(),
                'total_alumni'        => User::where('role','alumni')->count(),
                'total_guru'          => User::where('role','guru')->count(),
                'prestasi_pending'    => Achievement::where('status_validasi','Pending')->count(),
                'prestasi_approved'   => Achievement::where('status_validasi','Approved')->count(),
                'tracer_filled'       => \App\Models\TracerStudy::count(),
            ],
        ]);
    }
}