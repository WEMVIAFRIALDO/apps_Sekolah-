<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Tests\TestCase;
use Tymon\JWTAuth\Facades\JWTAuth;

class AuthLogoutTest extends TestCase
{
    protected function setUp(): void
    {
        parent::setUp();

        if (DB::connection()->getDriverName() !== 'sqlite' || DB::connection()->getDatabaseName() !== ':memory:') {
            $this->fail('Tes dibatalkan: koneksi bukan SQLite in-memory.');
        }

        $this->artisan('migrate');
    }

    private function buatSiswa(): User
    {
        return User::create([
            'name' => 'Siswa', 'email' => '0000000021@uji.test', 'password' => Hash::make('rahasia123'), 'nisn' => '0000000021',
            'role' => 'siswa', 'class_name' => 'XII RPL 1', 'angkatan' => 2026, 'is_active' => true,
        ]);
    }

    public function test_token_dicabut_di_server_setelah_logout(): void
    {
        $token = JWTAuth::fromUser($this->buatSiswa());

        $this->withHeader('Authorization', "Bearer $token")->getJson('/api/profile')->assertOk();

        $this->withHeader('Authorization', "Bearer $token")
            ->postJson('/api/logout')
            ->assertOk()
            ->assertJson(['success' => true]);

        // Token yang sama tidak boleh dipakai lagi (masuk blacklist).
        $this->withHeader('Authorization', "Bearer $token")->getJson('/api/profile')->assertUnauthorized();
    }

    public function test_logout_tanpa_token_ditolak(): void
    {
        $this->postJson('/api/logout')->assertUnauthorized();
    }

    public function test_logout_dua_kali_dengan_token_sama_ditolak(): void
    {
        $token = JWTAuth::fromUser($this->buatSiswa());

        $this->withHeader('Authorization', "Bearer $token")->postJson('/api/logout')->assertOk();
        $this->withHeader('Authorization', "Bearer $token")->postJson('/api/logout')->assertUnauthorized();
    }

    public function test_token_baru_dari_login_tetap_valid_setelah_logout_sesi_lama(): void
    {
        $siswa = $this->buatSiswa();
        $lama = JWTAuth::fromUser($siswa);

        $this->withHeader('Authorization', "Bearer $lama")->postJson('/api/logout')->assertOk();

        $baru = $this->postJson('/api/login', ['nisn' => '0000000021', 'password' => 'rahasia123'])
            ->assertOk()
            ->json('token');

        $this->withHeader('Authorization', "Bearer $baru")->getJson('/api/profile')->assertOk();
    }
}
