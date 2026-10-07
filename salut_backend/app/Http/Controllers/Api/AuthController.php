<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\ValidationException;
use Tymon\JWTAuth\Facades\JWTAuth;
use Tymon\JWTAuth\Exceptions\JWTException;

/**
 * REQ-F-01: Login dengan NISN + Password → JWT Bearer Token.
 * REQ-NF-01: Keamanan JWT untuk seluruh akses API.
 */
class AuthController extends Controller
{
    /**
     * POST /api/login
     * Response: { token, user }
     */
    public function login(Request $request): JsonResponse
    {
        $request->validate([
            'nisn'     => 'required|string|digits:10',
            'password' => 'required|string|min:6',
        ]);

        $user = User::where('nisn', $request->nisn)->first();

        if (!$user || !Hash::check($request->password, $user->password)) {
            return response()->json([
                'success' => false,
                'message' => 'NISN atau password salah.',
            ], 401);
        }

        if (!$user->is_active) {
            return response()->json([
                'success' => false,
                'message' => 'Akun Anda tidak aktif. Hubungi Admin sekolah.',
            ], 403);
        }

        try {
            if ($request->has('fcm_token')) {
                $user->update(['fcm_token' => $request->fcm_token]);
            }
            $token = JWTAuth::fromUser($user);
        } catch (JWTException $e) {
            return response()->json([
                'success' => false,
                'message' => 'Gagal membuat token. Coba lagi.',
            ], 500);
        }

        return response()->json([
            'success' => true,
            'token'   => $token,
            'user'    => $this->formatUser($user),
        ]);
    }

    /**
     * POST /api/logout — Invalidate JWT token.
     */
    public function logout(Request $request): JsonResponse
    {
        try {
            JWTAuth::invalidate(JWTAuth::getToken());
            return response()->json(['success' => true, 'message' => 'Berhasil logout.']);
        } catch (JWTException $e) {
            return response()->json(['success' => false, 'message' => 'Gagal logout.'], 500);
        }
    }

    /**
     * POST /api/refresh — Refresh JWT token yang hampir expired.
     */
    public function refresh(): JsonResponse
    {
        try {
            $newToken = JWTAuth::refresh(JWTAuth::getToken());
            return response()->json(['token' => $newToken]);
        } catch (JWTException $e) {
            return response()->json(['message' => 'Token tidak bisa diperbarui.'], 401);
        }
    }

    /** Format user data untuk response (tanpa field sensitif) */
    private function formatUser(User $user): array
    {
        return [
            'id'              => $user->id,
            'name'            => $user->name,
            'nisn'            => $user->nisn,
            'email'           => $user->email,
            'phone'           => $user->phone,
            'role'            => $user->role,
            'school'          => $user->school,
            'class'           => $user->class_name,
            'angkatan'        => $user->angkatan,
            'graduation_date' => $user->graduation_date?->format('Y-m-d'),
            'joined_at'       => $user->created_at->format('Y-m-d'),
        ];
    }
}