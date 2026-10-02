<?php
namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use Tymon\JWTAuth\Facades\JWTAuth;

/** GET /api/profile — Data profil dari JWT token */
class ProfileController extends Controller
{
    public function show(): JsonResponse
    {
        $user = JWTAuth::user();
        return response()->json([
            'success' => true,
            'data' => [
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
            ],
        ]);
    }

    public function update(Request $request): JsonResponse
    {
        $user = JWTAuth::user();
        $request->validate([
            'phone' => 'nullable|string|max:20',
            'email' => 'nullable|email|unique:users,email,' . $user->id,
        ]);
        $user->update($request->only(['phone','email']));
        return response()->json(['success' => true, 'message' => 'Profil diperbarui.']);
    }

    public function changePassword(Request $request): JsonResponse
    {
        $user = JWTAuth::user();
        $request->validate([
            'current_password' => 'required',
            'new_password'     => 'required|min:6|confirmed',
        ]);
        if (!Hash::check($request->current_password, $user->password)) {
            return response()->json(['success' => false, 'message' => 'Password lama salah.'], 422);
        }
        $user->update(['password' => Hash::make($request->new_password)]);
        return response()->json(['success' => true, 'message' => 'Password berhasil diubah.']);
    }
}