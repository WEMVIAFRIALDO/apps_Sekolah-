<?php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;
use Tymon\JWTAuth\Facades\JWTAuth;
use Tymon\JWTAuth\Exceptions\JWTException;
use Tymon\JWTAuth\Exceptions\TokenExpiredException;
use Tymon\JWTAuth\Exceptions\TokenInvalidException;

/** REQ-NF-01: Semua endpoint protected wajib melewati middleware JWT ini */
class JwtMiddleware
{
    public function handle(Request $request, Closure $next): Response
    {
        try {
            $user = JWTAuth::parseToken()->authenticate();
            if (!$user) {
                return response()->json(['message' => 'User tidak ditemukan.'], 401);
            }
        } catch (TokenExpiredException $e) {
            return response()->json(['message' => 'Token sudah expired. Silakan login ulang.'], 401);
        } catch (TokenInvalidException $e) {
            return response()->json(['message' => 'Token tidak valid.'], 401);
        } catch (JWTException $e) {
            return response()->json(['message' => 'Token tidak disertakan.'], 401);
        }
        return $next($request);
    }
}