<?php

namespace Tests\Feature;

use App\Models\GraduationDoc;
use App\Models\User;
use Database\Seeders\DatabaseSeeder;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Storage;
use Tests\TestCase;
use Tymon\JWTAuth\Facades\JWTAuth;

class DokumenRahasiaTest extends TestCase
{
    protected function setUp(): void
    {
        parent::setUp();

        // Seeder mengosongkan tabel: tes ini hanya boleh berjalan di SQLite in-memory.
        if (DB::connection()->getDriverName() !== 'sqlite' || DB::connection()->getDatabaseName() !== ':memory:') {
            $this->fail('Tes dibatalkan: koneksi bukan SQLite in-memory.');
        }

        $this->artisan('migrate');
        Storage::fake('local');
        Storage::fake('public');
    }

    private function buatUser(string $role, array $data = []): User
    {
        return User::create(array_merge([
            'name' => "Uji $role",
            'email' => uniqid($role).'@uji.test',
            'password' => 'rahasia123',
            'role' => $role,
            'is_active' => true,
        ], $data));
    }

    private function sebagai(User $user): self
    {
        return $this->withHeader('Authorization', 'Bearer '.JWTAuth::fromUser($user));
    }

    public function test_upload_arsip_memakai_path_hierarkis_di_disk_privat(): void
    {
        $admin = $this->buatUser('admin', ['nisn' => '0000000001']);
        $alumni = $this->buatUser('alumni', ['nisn' => '0012345678', 'angkatan' => 2026]);

        $this->sebagai($admin)->postJson('/api/arsip', [
            'user_id' => $alumni->id,
            'doc_type' => 'ijazah',
            'title' => 'Ijazah',
            'file' => UploadedFile::fake()->create('apa_saja.pdf', 10, 'application/pdf'),
        ])->assertCreated();

        Storage::disk('local')->assertExists('angkatan_2026/nisn_0012345678/ijazah.pdf');
        $this->assertSame([], Storage::disk('public')->allFiles());
    }

    public function test_upload_arsip_ditolak_jika_nisn_tujuan_tidak_valid(): void
    {
        $admin = $this->buatUser('admin', ['nisn' => '0000000001']);
        $tujuan = $this->buatUser('alumni', ['nisn' => '../../evil', 'angkatan' => 2026]);

        $this->sebagai($admin)->postJson('/api/arsip', [
            'user_id' => $tujuan->id,
            'doc_type' => 'ijazah',
            'title' => 'Ijazah',
            'file' => UploadedFile::fake()->create('a.pdf', 10, 'application/pdf'),
        ])->assertStatus(422);

        $this->assertSame([], Storage::disk('local')->allFiles());
    }

    public function test_sertifikat_prestasi_memakai_path_hierarkis_dan_nama_acak(): void
    {
        $siswa = $this->buatUser('siswa', ['nisn' => '0054321987', 'angkatan' => 2026]);

        $this->sebagai($siswa)->postJson('/api/prestasi', [
            'nama_kegiatan' => 'Lomba',
            'penyelenggara' => 'Dinas',
            'tingkat' => 'Provinsi',
            'peringkat' => 'Juara 1',
            'tahun' => (int) date('Y'),
            'sertifikat' => UploadedFile::fake()->create('nama_asli.pdf', 10, 'application/pdf'),
        ])->assertCreated();

        $files = Storage::disk('local')->allFiles();
        $this->assertCount(1, $files);
        $this->assertMatchesRegularExpression('#^angkatan_2026/nisn_0054321987/sertifikat/[^/]+\.pdf$#', $files[0]);
        $this->assertStringNotContainsString('nama_asli', $files[0]);
    }

    public function test_download_dokumen_wajib_jwt_dan_hanya_untuk_pemilik_atau_admin(): void
    {
        $pemilik = $this->buatUser('alumni', ['nisn' => '0012345678', 'angkatan' => 2026]);
        $lain = $this->buatUser('alumni', ['nisn' => '0012345679', 'angkatan' => 2026]);
        $admin = $this->buatUser('admin', ['nisn' => '0000000001']);

        $path = 'angkatan_2026/nisn_0012345678/ijazah.pdf';
        Storage::disk('local')->put($path, '%PDF-1.4');
        $doc = GraduationDoc::create([
            'user_id' => $pemilik->id, 'doc_type' => 'ijazah', 'title' => 'Ijazah',
            'file_path' => $path, 'is_verified' => true,
        ]);
        $url = "/api/arsip/{$doc->id}/download";

        $this->getJson($url)->assertUnauthorized();
        $this->sebagai($lain)->getJson($url)->assertForbidden();
        $this->sebagai($pemilik)->get($url)->assertOk();
        $this->sebagai($admin)->get($url)->assertOk();
    }

    public function test_disk_privat_tidak_punya_rute_publik(): void
    {
        $this->assertFalse(Route::has('storage.local'));
    }

    public function test_seeder_menyediakan_akun_uji_dan_path_arsip_sesuai_struktur(): void
    {
        $this->seed(DatabaseSeeder::class);

        foreach ([
            ['0000000001', 'admin123', 'admin'],
            ['0000000002', 'guru123', 'guru'],
            ['0054321987', 'siswa123', 'siswa'],
            ['0067890123', 'alumni123', 'alumni'],
        ] as [$nisn, $password, $role]) {
            $this->postJson('/api/login', ['nisn' => $nisn, 'password' => $password])
                ->assertOk()
                ->assertJsonPath('user.role', $role);
        }

        $docs = GraduationDoc::with('user')->get();
        $this->assertNotEmpty($docs);
        foreach ($docs as $doc) {
            $this->assertStringStartsWith("angkatan_{$doc->user->angkatan}/nisn_{$doc->user->nisn}/", $doc->file_path);
            Storage::disk('local')->assertExists($doc->file_path);
        }
    }
}
