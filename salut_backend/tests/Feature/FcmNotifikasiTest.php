<?php

namespace Tests\Feature;

use App\Models\GraduationSchedule;
use App\Models\User;
use App\Services\FcmService;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Tests\TestCase;
use Tymon\JWTAuth\Facades\JWTAuth;

class FcmNotifikasiTest extends TestCase
{
    private ?string $credentialsPath = null;

    protected function setUp(): void
    {
        parent::setUp();

        if (DB::connection()->getDriverName() !== 'sqlite' || DB::connection()->getDatabaseName() !== ':memory:') {
            $this->fail('Tes dibatalkan: koneksi bukan SQLite in-memory.');
        }

        $this->artisan('migrate');
        Http::preventStrayRequests();
    }

    protected function tearDown(): void
    {
        if ($this->credentialsPath) {
            @unlink($this->credentialsPath);
        }
        parent::tearDown();
    }

    private function pasangKredensial(): void
    {
        $key = openssl_pkey_new(['private_key_bits' => 2048, 'config' => 'C:/xampp/php/extras/ssl/openssl.cnf'])
            ?: openssl_pkey_new(['private_key_bits' => 2048]);
        if (! $key) {
            $this->markTestSkipped('OpenSSL tidak bisa membuat kunci uji.');
        }
        openssl_pkey_export($key, $pem, null, ['config' => 'C:/xampp/php/extras/ssl/openssl.cnf']);

        $this->credentialsPath = tempnam(sys_get_temp_dir(), 'fcm');
        file_put_contents($this->credentialsPath, json_encode([
            'project_id' => 'proyek-uji',
            'client_email' => 'uji@proyek-uji.iam.gserviceaccount.com',
            'private_key' => $pem,
            'token_uri' => 'https://oauth2.example.test/token',
        ]));
        config(['services.fcm.credentials' => $this->credentialsPath]);
    }

    private function buatSiswa(string $nisn, ?string $token): User
    {
        return User::create([
            'name' => 'Siswa', 'email' => "$nisn@uji.test", 'password' => 'rahasia123', 'nisn' => $nisn,
            'role' => 'siswa', 'class_name' => 'XII RPL 1', 'angkatan' => 2026, 'is_active' => true, 'fcm_token' => $token,
        ]);
    }

    public function test_tanpa_kredensial_tidak_crash_dan_dicatat_di_log(): void
    {
        config(['services.fcm.credentials' => null]);
        Log::spy();

        $this->assertSame(0, app(FcmService::class)->send(['token-a'], 'Judul', 'Isi'));

        Log::shouldHaveReceived('warning')->once();
    }

    public function test_file_kredensial_hilang_tidak_crash(): void
    {
        config(['services.fcm.credentials' => 'D:/tidak/ada/firebase.json']);

        $this->assertSame(0, app(FcmService::class)->send(['token-a'], 'Judul', 'Isi'));
    }

    public function test_mengirim_notifikasi_dan_membersihkan_token_tidak_terdaftar(): void
    {
        $this->pasangKredensial();
        $this->buatSiswa('0000000011', 'token-hidup');
        $mati = $this->buatSiswa('0000000012', 'token-mati');

        Http::fake([
            'oauth2.example.test/*' => Http::response(['access_token' => 'akses-uji']),
            'fcm.googleapis.com/*' => function ($request) {
                return Http::response([], $request['message']['token'] === 'token-mati' ? 404 : 200);
            },
        ]);

        $this->assertSame(1, app(FcmService::class)->send(['token-hidup', 'token-mati', 'token-hidup', null], 'Judul', 'Isi'));

        Http::assertSent(fn ($r) => str_contains($r->url(), '/v1/projects/proyek-uji/messages:send')
            && $r->hasHeader('Authorization', 'Bearer akses-uji'));
        $this->assertNull($mati->fresh()->fcm_token);
    }

    public function test_jadwal_kelulusan_tetap_memproses_siswa_walau_firebase_menolak(): void
    {
        $this->pasangKredensial();
        $siswa = $this->buatSiswa('0000000011', 'token-hidup');
        GraduationSchedule::create(['angkatan' => 2026, 'graduation_date' => now()->subDay(), 'status' => 'pending']);

        Http::fake(['oauth2.example.test/*' => Http::response([], 500)]);

        $this->artisan('salut:promote-alumni')->assertSuccessful();

        $this->assertSame('alumni', $siswa->fresh()->role);
    }

    public function test_jadwal_kelulusan_mengirim_notifikasi_ke_siswa_yang_lulus(): void
    {
        $this->pasangKredensial();
        $this->buatSiswa('0000000011', 'token-hidup');
        GraduationSchedule::create(['angkatan' => 2026, 'graduation_date' => now()->subDay(), 'status' => 'pending']);

        Http::fake([
            'oauth2.example.test/*' => Http::response(['access_token' => 'akses-uji']),
            'fcm.googleapis.com/*' => Http::response(['name' => 'ok']),
        ]);

        $this->artisan('salut:promote-alumni')->assertSuccessful();

        Http::assertSent(fn ($r) => str_contains($r->url(), 'messages:send') && $r['message']['token'] === 'token-hidup');
    }

    public function test_token_perangkat_pindah_ke_akun_yang_terakhir_login(): void
    {
        $lama = $this->buatSiswa('0000000011', 'token-hp');
        $baru = $this->buatSiswa('0000000012', null);

        $this->withHeader('Authorization', 'Bearer '.JWTAuth::fromUser($baru))
            ->patchJson('/api/profile/fcm-token', ['fcm_token' => 'token-hp'])
            ->assertOk();

        $this->assertNull($lama->fresh()->fcm_token);
        $this->assertSame('token-hp', $baru->fresh()->fcm_token);
    }

    public function test_token_dihapus_saat_logout(): void
    {
        $siswa = $this->buatSiswa('0000000011', 'token-hp');

        $this->withHeader('Authorization', 'Bearer '.JWTAuth::fromUser($siswa))
            ->postJson('/api/logout')
            ->assertOk();

        $this->assertNull($siswa->fresh()->fcm_token);
    }
}
