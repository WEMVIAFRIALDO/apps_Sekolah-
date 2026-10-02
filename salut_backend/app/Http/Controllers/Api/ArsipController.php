<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\GraduationDoc;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Tymon\JWTAuth\Facades\JWTAuth;

/**
 * REQ-F-06: Arsip digital kelulusan (Ijazah, SKHUN, SKL, Rapor).
 * REQ-NF-01: Semua file PRIVATE — wajib JWT Bearer Token untuk download.
 */
class ArsipController extends Controller
{
    /** GET /api/arsip — List semua arsip milik alumni yang login */
    public function index(): JsonResponse
    {
        $user = JWTAuth::user();

        $docs = GraduationDoc::where('user_id', $user->id)
            ->orderBy('doc_type')
            ->get()
            ->map(fn($d) => [
                'id'          => $d->id,
                'title'       => $d->title,
                'type'        => 'PDF',
                'doc_type'    => $d->doc_type,
                'file_size'   => $d->file_size ?? '-',
                'is_verified' => $d->is_verified,
                'created_at'  => $d->created_at->format('Y-m-d'),
            ]);

        return response()->json(['success' => true, 'data' => $docs]);
    }

    /**
     * GET /api/arsip/{id}/download
     * REQ-NF-01: File hanya bisa diakses oleh pemilik yang sudah autentikasi JWT.
     * Storage path hierarkis: angkatan_{year}/nisn_{nisn}/{doc_type}.pdf
     */
    public function download(GraduationDoc $graduationDoc): mixed
    {
        $user = JWTAuth::user();

        // Hanya pemilik atau admin yang bisa download
        if ($graduationDoc->user_id !== $user->id && !$user->isAdmin()) {
            return response()->json(['message' => 'Akses ditolak.'], 403);
        }

        if (!Storage::disk('local')->exists($graduationDoc->file_path)) {
            return response()->json(['message' => 'File tidak ditemukan di server.'], 404);
        }

        return Storage::disk('local')->download(
            $graduationDoc->file_path,
            $graduationDoc->title . '.pdf'
        );
    }

    /** POST /api/arsip — Upload arsip (Admin only) */
    public function store(Request $request): JsonResponse
    {
        $uploader = JWTAuth::user();
        if (!$uploader->isAdmin() && !$uploader->isGuru()) {
            return response()->json(['message' => 'Hanya Admin yang bisa upload arsip.'], 403);
        }

        $validated = $request->validate([
            'user_id'  => 'required|exists:users,id',
            'doc_type' => 'required|in:ijazah,skhun,skl,rapor,portofolio',
            'title'    => 'required|string|max:255',
            'file'     => 'required|file|mimes:pdf|max:20480', // maks 20MB
        ]);

        $targetUser = \App\Models\User::findOrFail($validated['user_id']);

        // Simpan ke path hierarkis: angkatan_{year}/nisn_{nisn}/{doc_type}.pdf
        $path = $request->file('file')->storeAs(
            "angkatan_{$targetUser->angkatan}/nisn_{$targetUser->nisn}",
            $validated['doc_type'] . '.pdf',
            'local'
        );

        $doc = GraduationDoc::updateOrCreate(
            ['user_id' => $validated['user_id'], 'doc_type' => $validated['doc_type']],
            [
                'title'       => $validated['title'],
                'file_path'   => $path,
                'file_size'   => round($request->file('file')->getSize() / 1024) . ' KB',
                'is_verified' => true,
                'uploaded_by' => $uploader->id,
            ]
        );

        return response()->json([
            'success' => true,
            'message' => "Arsip {$validated['doc_type']} berhasil diupload.",
            'data'    => ['id' => $doc->id, 'title' => $doc->title],
        ], 201);
    }
}