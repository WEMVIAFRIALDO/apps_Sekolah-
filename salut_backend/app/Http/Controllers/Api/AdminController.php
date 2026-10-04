<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Achievement;
use App\Models\TracerStudy;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Hash;
use Tymon\JWTAuth\Facades\JWTAuth;

/** Endpoint khusus Admin dan Guru */
class AdminController extends Controller
{
    /**
     * GET /api/admin/users — Daftar semua pengguna dengan filter role, kelas, angkatan, search
     * Digunakan oleh students.html
     */
    public function listUsers(Request $request): JsonResponse
    {
        $caller = JWTAuth::user();
        if (!$caller->isAdmin() && !$caller->isGuru()) {
            return response()->json(['message' => 'Tidak diizinkan.'], 403);
        }

        $query = User::query()->orderBy('name');

        // Filter role
        if ($request->filled('role')) {
            $query->where('role', $request->role);
        } else {
            // Default: tampilkan siswa, alumni, guru (bukan admin)
            $query->whereIn('role', ['siswa', 'alumni', 'guru']);
        }

        // Filter kelas
        if ($request->filled('class_name')) {
            $query->where('class_name', $request->class_name);
        }

        // Filter angkatan
        if ($request->filled('angkatan')) {
            $query->where('angkatan', $request->angkatan);
        }

        // Search nama / NISN
        if ($request->filled('search')) {
            $q = $request->search;
            $query->where(function ($sub) use ($q) {
                $sub->where('name', 'like', "%{$q}%")
                    ->orWhere('nisn', 'like', "%{$q}%");
            });
        }

        $perPage = (int) $request->get('per_page', 50);
        $paginated = $query->select(
            'id','name','nisn','role','phone','class_name','angkatan','graduation_date','is_active','created_at'
        )->paginate($perPage);

        return response()->json(['success' => true, 'data' => $paginated]);
    }

    /**
     * GET /api/admin/tracer-studies — Rekapitulasi Tracer Study semua alumni
     * REQ-F-10
     */
    public function listTracerStudies(Request $request): JsonResponse
    {
        $caller = JWTAuth::user();
        if (!$caller->isAdmin() && !$caller->isGuru()) {
            return response()->json(['message' => 'Tidak diizinkan.'], 403);
        }

        $query = TracerStudy::with('user:id,name,nisn,angkatan,class_name,graduation_date')
            ->orderBy('created_at', 'desc');

        // Filter angkatan
        if ($request->filled('angkatan')) {
            $query->whereHas('user', fn($u) => $u->where('angkatan', $request->angkatan));
        }

        // Filter status
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $perPage = (int) $request->get('per_page', 50);
        $paginated = $query->paginate($perPage);

        // Hitung ringkasan
        $summary = [
            'total'        => TracerStudy::count(),
            'kuliah'       => TracerStudy::where('status', 'like', 'Kuliah%')->count(),
            'bekerja'      => TracerStudy::where('status', 'Bekerja')->count(),
            'wirausaha'    => TracerStudy::where('status', 'Wirausaha')->count(),
            'lainnya'      => TracerStudy::whereNotIn('status', ['Bekerja', 'Wirausaha'])
                                         ->where('status', 'not like', 'Kuliah%')->count(),
        ];

        return response()->json([
            'success' => true,
            'summary' => $summary,
            'data'    => $paginated,
        ]);
    }

    /**
     * GET /api/admin/tracer-studies/export-csv — Export CSV Tracer Study
     * REQ-F-10
     */
    public function exportTracerCsv(Request $request): Response
    {
        $caller = JWTAuth::user();
        if (!$caller->isAdmin()) {
            abort(403, 'Hanya Admin.');
        }

        $query = TracerStudy::with('user:id,name,nisn,angkatan,class_name,graduation_date')
            ->orderBy('created_at', 'desc');

        if ($request->filled('angkatan')) {
            $query->whereHas('user', fn($u) => $u->where('angkatan', $request->angkatan));
        }

        $rows = $query->get();
        $csv  = "No,Nama,NISN,Angkatan,Kelas,Status Pasca-Lulus,Instansi,Kota,Jabatan/Prodi,Tahun Masuk\n";

        foreach ($rows as $i => $r) {
            $u = $r->user;
            $detail = $r->jabatan ?? $r->prodi ?? '-';
            $csv .= implode(',', [
                $i + 1,
                '"' . ($u->name ?? '-') . '"',
                $u->nisn ?? '-',
                $u->angkatan ?? '-',
                '"' . ($u->class_name ?? '-') . '"',
                '"' . $r->status . '"',
                '"' . ($r->nama_instansi ?? '-') . '"',
                '"' . ($r->kota ?? '-') . '"',
                '"' . $detail . '"',
                $r->tahun_masuk ?? '-',
            ]) . "\n";
        }

        $filename = 'Tracer_Study_SALUT_' . date('Y-m-d') . '.csv';
        return response($csv, 200, [
            'Content-Type'        => 'text/csv; charset=UTF-8',
            'Content-Disposition' => "attachment; filename={$filename}",
        ]);
    }

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
    /**
     * GET /api/admin/schedules — Lihat jadwal kelulusan
     */
    public function listSchedules(): JsonResponse
    {
        $admin = JWTAuth::user();
        if (!$admin->isAdmin()) {
            return response()->json(['message' => 'Hanya Admin.'], 403);
        }

        $schedules = \App\Models\GraduationSchedule::orderBy('angkatan', 'desc')->get();
        return response()->json(['success' => true, 'data' => $schedules]);
    }

    /**
     * POST /api/admin/schedules — Set jadwal kelulusan baru
     */
    public function createSchedule(Request $request): JsonResponse
    {
        $admin = JWTAuth::user();
        if (!$admin->isAdmin()) {
            return response()->json(['message' => 'Hanya Admin.'], 403);
        }

        $validated = $request->validate([
            'angkatan' => 'required|integer',
            'graduation_date' => 'required|date'
        ]);

        $schedule = \App\Models\GraduationSchedule::updateOrCreate(
            ['angkatan' => $validated['angkatan']],
            ['graduation_date' => $validated['graduation_date'], 'status' => 'pending']
        );

        return response()->json([
            'success' => true,
            'message' => 'Jadwal kelulusan berhasil disimpan.',
            'data' => $schedule
        ]);
    }
}