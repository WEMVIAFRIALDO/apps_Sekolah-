<?php

namespace App\Services;

use App\Models\User;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use RuntimeException;
use Throwable;

/**
 * Pengirim push notification lewat Firebase Cloud Messaging HTTP v1.
 *
 * Tidak pernah melempar exception: kegagalan notifikasi hanya dicatat di log
 * agar proses utama, seperti perubahan status kelulusan, tetap berjalan.
 */
class FcmService
{
    private const SCOPE = 'https://www.googleapis.com/auth/firebase.messaging';

    /**
     * @param  array<int, string|null>  $tokens
     * @return int Jumlah notifikasi yang diterima FCM.
     */
    public function send(array $tokens, string $title, string $body): int
    {
        $tokens = array_values(array_unique(array_filter($tokens)));
        if ($tokens === []) {
            return 0;
        }

        try {
            $credentials = $this->credentials();
            if ($credentials === null) {
                Log::warning('[FCM] Kredensial Firebase belum dipasang, notifikasi dilewati.', ['tujuan' => count($tokens)]);
                return 0;
            }
            $accessToken = $this->accessToken($credentials);
        } catch (Throwable $e) {
            Log::error('[FCM] Gagal mengautentikasi ke Firebase: '.$e->getMessage());
            return 0;
        }

        $url = "https://fcm.googleapis.com/v1/projects/{$credentials['project_id']}/messages:send";
        $sent = 0;

        foreach ($tokens as $token) {
            try {
                $response = Http::withToken($accessToken)->timeout(10)->post($url, [
                    'message' => [
                        'token' => $token,
                        'notification' => ['title' => $title, 'body' => $body],
                    ],
                ]);

                if ($response->successful()) {
                    $sent++;
                } elseif ($response->status() === 404) {
                    // Token sudah tidak terdaftar, misalnya aplikasi telah dihapus.
                    User::where('fcm_token', $token)->update(['fcm_token' => null]);
                } else {
                    Log::warning('[FCM] Pengiriman ditolak.', ['status' => $response->status()]);
                }
            } catch (Throwable $e) {
                Log::error('[FCM] Gagal mengirim notifikasi: '.$e->getMessage());
            }
        }

        return $sent;
    }

    /** @return array{project_id: string, client_email: string, private_key: string, token_uri: string}|null */
    private function credentials(): ?array
    {
        $path = config('services.fcm.credentials');
        if (! $path) {
            return null;
        }
        if (! is_file($path)) {
            throw new RuntimeException('File FIREBASE_CREDENTIALS tidak ditemukan.');
        }

        $data = json_decode((string) file_get_contents($path), true);
        foreach (['project_id', 'client_email', 'private_key', 'token_uri'] as $key) {
            if (empty($data[$key])) {
                throw new RuntimeException("File FIREBASE_CREDENTIALS tidak memiliki kolom {$key}.");
            }
        }

        return $data;
    }

    private function accessToken(array $credentials): string
    {
        $now = time();
        $unsigned = $this->base64Url(json_encode(['alg' => 'RS256', 'typ' => 'JWT']))
            .'.'.$this->base64Url(json_encode([
                'iss' => $credentials['client_email'],
                'scope' => self::SCOPE,
                'aud' => $credentials['token_uri'],
                'iat' => $now,
                'exp' => $now + 3600,
            ]));

        if (! openssl_sign($unsigned, $signature, $credentials['private_key'], OPENSSL_ALGO_SHA256)) {
            throw new RuntimeException('Kunci privat Firebase tidak valid.');
        }

        $response = Http::asForm()->timeout(10)->post($credentials['token_uri'], [
            'grant_type' => 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'assertion' => $unsigned.'.'.$this->base64Url($signature),
        ]);

        $token = $response->json('access_token');
        if (! $response->successful() || ! $token) {
            throw new RuntimeException('Firebase menolak permintaan token (HTTP '.$response->status().').');
        }

        return $token;
    }

    private function base64Url(string $value): string
    {
        return rtrim(strtr(base64_encode($value), '+/', '-_'), '=');
    }
}
