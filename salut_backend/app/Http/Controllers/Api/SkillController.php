<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\SkillCompetency;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

/**
 * Controller untuk fitur Skill Raport / Portofolio Kompetensi SMK.
 * - Guru input kompetensi per siswa
 * - Siswa/Alumni lihat kompetensi milik sendiri (SKPI)
 * - Admin bisa lihat kompetensi semua siswa
 */
class SkillController extends Controller
{
    /**
     * GET /api/guru/skills/students
     * Daftar siswa untuk guru pilih (dengan filter jurusan)
     */
    public function getStudents(Request $request): JsonResponse
    {
        if ($denied = $this->denyNonGuru()) return $denied;

        $query = User::whereIn('role', ['siswa', 'alumni']);

        if ($request->has('jurusan')) {
            $query->where('jurusan', $request->jurusan);
        }
        if ($request->has('search')) {
            $term = $request->search;
            $query->where(function($q) use ($term) {
                $q->where('name', 'like', "%$term%")
                  ->orWhere('nisn', 'like', "%$term%");
            });
        }

        $students = $query->select('id','name','nisn','jurusan','class_name','angkatan','role')
                          ->orderBy('name')->get();

        return response()->json(['success' => true, 'data' => $students]);
    }

    /**
     * GET /api/guru/skills/{userId}
     * Daftar semua kompetensi milik seorang siswa
     */
    public function getByStudent(int $userId): JsonResponse
    {
        if ($denied = $this->denyNonGuru()) return $denied;

        $siswa = User::findOrFail($userId);
        $skills = SkillCompetency::where('user_id', $userId)
            ->with('guru:id,name')
            ->orderBy('created_at', 'desc')
            ->get();

        return response()->json([
            'success' => true,
            'siswa'   => [
                'id'       => $siswa->id,
                'name'     => $siswa->name,
                'nisn'     => $siswa->nisn,
                'jurusan'  => $siswa->jurusan,
                'angkatan' => $siswa->angkatan,
            ],
            'data' => $skills,
        ]);
    }

    /**
     * GET /api/skills/my
     * Kompetensi milik pengguna yang sedang login (Siswa/Alumni)
     */
    public function mySkills(): JsonResponse
    {
        $user   = Auth::user();
        $skills = SkillCompetency::where('user_id', $user->id)
            ->with('guru:id,name')
            ->orderBy('kategori')
            ->get();

        return response()->json([
            'success' => true,
            'jurusan' => $user->jurusan,
            'data'    => $skills,
        ]);
    }

    /**
     * POST /api/guru/skills
     * Guru menginput kompetensi untuk seorang siswa
     */
    public function store(Request $request): JsonResponse
    {
        if ($denied = $this->denyNonGuru()) return $denied;

        $validated = $request->validate([
            'user_id'         => 'required|exists:users,id',
            'nama_kompetensi' => 'required|string|max:255',
            'kategori'        => 'nullable|string|max:100',
            'level'           => 'nullable|in:Dasar,Terampil,Mahir',
            'keterangan'      => 'nullable|string',
            'semester'        => 'nullable|string|max:10',
            'tahun_pelajaran' => 'nullable|string|max:10',
        ]);

        $validated['guru_id'] = Auth::id();

        $skill = SkillCompetency::create($validated);
        $skill->load('guru:id,name', 'siswa:id,name,nisn');

        return response()->json([
            'success' => true,
            'message' => 'Kompetensi berhasil ditambahkan.',
            'data'    => $skill,
        ], 201);
    }

    /**
     * DELETE /api/guru/skills/{id}
     * Guru hapus entri kompetensi
     */
    public function destroy(int $id): JsonResponse
    {
        if ($denied = $this->denyNonGuru()) return $denied;

        $skill = SkillCompetency::findOrFail($id);
        $skill->delete();

        return response()->json(['success' => true, 'message' => 'Kompetensi dihapus.']);
    }

    /**
     * GET /api/admin/skills/stats
     * Statistik distribusi kompetensi per jurusan untuk Dashboard Admin
     */
    public function stats(): JsonResponse
    {
        // Jumlah siswa per jurusan
        $perJurusan = User::whereIn('role', ['siswa','alumni'])
            ->selectRaw('jurusan, COUNT(*) as total')
            ->groupBy('jurusan')
            ->orderBy('total', 'desc')
            ->get();

        // Distribusi skill per jurusan (top 5 kompetensi terbanyak per jurusan)
        $topSkills = SkillCompetency::selectRaw('nama_kompetensi, kategori, COUNT(*) as total')
            ->groupBy('nama_kompetensi', 'kategori')
            ->orderBy('total', 'desc')
            ->limit(10)
            ->get();

        return response()->json([
            'success'     => true,
            'per_jurusan' => $perJurusan,
            'top_skills'  => $topSkills,
        ]);
    }

    /** Endpoint /guru/skills/* hanya untuk Guru dan Admin */
    private function denyNonGuru(): ?JsonResponse
    {
        $user = Auth::user();
        if ($user->role !== 'guru' && $user->role !== 'admin') {
            return response()->json(['message' => 'Akses ditolak.'], 403);
        }
        return null;
    }
}
