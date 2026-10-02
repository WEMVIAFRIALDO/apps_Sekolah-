<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Achievement;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Tymon\JWTAuth\Facades\JWTAuth;

/**
 * REQ-F-03: Input prestasi siswa.
 * REQ-NF-03: Status validasi Pending → Approved/Rejected oleh Guru.
 * File sertifikat disimpan di private storage dengan path hierarkis.
 */
class PrestasiController extends Controller
{
    /** GET /api/prestasi — List prestasi milik siswa yang login */
    public function index(): JsonResponse
    {
        $user = JWTAuth::user();
        $achievements = Achievement::where('user_id', $user->id)
            ->orderBy('created_at', 'desc')
            ->get()
            ->map(fn($a) => $this->formatAchievement($a));

        return response()->json(['success' => true, 'data' => $achievements]);
    }

    /** POST /api/prestasi — Upload prestasi + sertifikat (multipart/form-data) */
    public function store(Request $request): JsonResponse
    {
        $user = JWTAuth::user();

        $validated = $request->validate([
            'nama_kegiatan'  => 'required|string|max:255',
            'penyelenggara'  => 'required|string|max:255',
            'tingkat'        => 'required|in:Kecamatan / Kabupaten,Kota / Madya,Provinsi,Nasional,Internasional',
            'peringkat'      => 'required|string|max:100',
            'tahun'          => 'required|digits:4|integer|min:2000|max:' . date('Y'),
            'deskripsi'      => 'nullable|string',
            'sertifikat'     => 'required|file|mimes:pdf,jpg,jpeg,png|max:5120', // maks 5MB
        ]);

        // Simpan sertifikat ke private storage: achievements/{user_id}/{timestamp}_{filename}
        $path = $request->file('sertifikat')->storeAs(
            "achievements/{$user->id}",
            time() . '_' . $request->file('sertifikat')->getClientOriginalName(),
            'local'  // private, tidak bisa diakses langsung
        );

        $achievement = Achievement::create([
            'user_id'         => $user->id,
            'nama_kegiatan'   => $validated['nama_kegiatan'],
            'penyelenggara'   => $validated['penyelenggara'],
            'tingkat'         => $validated['tingkat'],
            'peringkat'       => $validated['peringkat'],
            'tahun'           => $validated['tahun'],
            'deskripsi'       => $validated['deskripsi'] ?? '',
            'status_validasi' => 'Pending',
            'sertifikat_path' => $path,
        ]);

        return response()->json([
            'success' => true,
            'message' => 'Prestasi berhasil dikirim. Menunggu validasi guru.',
            'data'    => $this->formatAchievement($achievement),
        ], 201);
    }

    /** GET /api/prestasi/{id}/sertifikat — Download sertifikat (JWT required) */
    public function downloadSertifikat(Achievement $achievement): mixed
    {
        $user = JWTAuth::user();

        // Hanya pemilik atau guru/admin yang bisa download
        if ($achievement->user_id !== $user->id && !in_array($user->role, ['guru','admin'])) {
            return response()->json(['message' => 'Tidak diizinkan.'], 403);
        }

        if (!Storage::disk('local')->exists($achievement->sertifikat_path)) {
            return response()->json(['message' => 'File tidak ditemukan.'], 404);
        }

        return Storage::disk('local')->download($achievement->sertifikat_path);
    }

    private function formatAchievement(Achievement $a): array {
        return [
            'id'              => $a->id,
            'nama_kegiatan'   => $a->nama_kegiatan,
            'penyelenggara'   => $a->penyelenggara,
            'tingkat'         => $a->tingkat,
            'peringkat'       => $a->peringkat,
            'tahun'           => $a->tahun,
            'deskripsi'       => $a->deskripsi,
            'status_validasi' => $a->status_validasi,
            'catatan'         => $a->catatan,
            'created_at'      => $a->created_at->format('Y-m-d'),
        ];
    }
}