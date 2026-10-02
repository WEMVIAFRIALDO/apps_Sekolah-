<?php
namespace Database\Seeders;

use App\Models\User;
use App\Models\Achievement;
use App\Models\GraduationDoc;
use App\Models\TracerStudy;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

/** Seeder data dummy untuk testing lokal SALUT */
class UserSeeder extends Seeder
{
    public function run(): void
    {
        // 1. Admin
        $admin = User::create([
            'name'     => 'Administrator SALUT',
            'nisn'     => '0000000001',
            'email'    => 'admin@salut.sch.id',
            'password' => Hash::make('admin123'),
            'role'     => 'admin',
            'school'   => 'SMA Negeri 1 Teladan',
            'is_active'=> true,
        ]);

        // 2. Guru
        $guru = User::create([
            'name'     => 'Drs. Suharto, M.Pd',
            'nisn'     => '0000000002',
            'email'    => 'guru@salut.sch.id',
            'password' => Hash::make('guru123'),
            'role'     => 'guru',
            'school'   => 'SMA Negeri 1 Teladan',
            'is_active'=> true,
        ]);

        // 3. Siswa Aktif
        $siswa = User::create([
            'name'       => 'Budi Santoso',
            'nisn'       => '0054321987',
            'email'      => 'budi@siswa.sch.id',
            'password'   => Hash::make('siswa123'),
            'role'       => 'siswa',
            'phone'      => '+6281234567890',
            'school'     => 'SMA Negeri 1 Teladan',
            'class_name' => 'XII IPA 3',
            'angkatan'   => 2026,
            'is_active'  => true,
        ]);

        // Prestasi dummy siswa
        Achievement::create([
            'user_id'        => $siswa->id,
            'nama_kegiatan'  => 'Olimpiade Fisika Provinsi',
            'penyelenggara'  => 'Dinas Pendidikan Jawa Barat',
            'tingkat'        => 'Provinsi',
            'peringkat'      => 'Juara 1',
            'tahun'          => 2025,
            'deskripsi'      => 'Mewakili sekolah dalam olimpiade fisika tingkat provinsi.',
            'status_validasi'=> 'Approved',
            'validated_by'   => $guru->id,
            'validated_at'   => now(),
        ]);

        Achievement::create([
            'user_id'        => $siswa->id,
            'nama_kegiatan'  => 'Lomba Karya Ilmiah Nasional',
            'penyelenggara'  => 'Kemendikbudristek',
            'tingkat'        => 'Nasional',
            'peringkat'      => 'Finalis',
            'tahun'          => 2025,
            'deskripsi'      => 'Penelitian bidang energi terbarukan.',
            'status_validasi'=> 'Pending',
        ]);

        // 4. Alumni
        $alumni = User::create([
            'name'            => 'Siti Rahayu',
            'nisn'            => '0067890123',
            'email'           => 'siti@alumni.sch.id',
            'password'        => Hash::make('alumni123'),
            'role'            => 'alumni',
            'phone'           => '+6285678901234',
            'school'          => 'SMA Negeri 1 Teladan',
            'class_name'      => 'XII IPS 2',
            'angkatan'        => 2024,
            'graduation_date' => '2024-06-15',
            'is_active'       => true,
        ]);

        // Arsip dokumen alumni (path dummy — file tidak ada, hanya untuk testing struktur)
        GraduationDoc::create([
            'user_id'     => $alumni->id,
            'doc_type'    => 'ijazah',
            'title'       => 'Ijazah SMA',
            'file_path'   => "angkatan_2024/nisn_0067890123/ijazah.pdf",
            'file_size'   => '1.2 MB',
            'is_verified' => true,
            'uploaded_by' => $admin->id,
        ]);

        GraduationDoc::create([
            'user_id'     => $alumni->id,
            'doc_type'    => 'skl',
            'title'       => 'Surat Keterangan Lulus',
            'file_path'   => "angkatan_2024/nisn_0067890123/skl.pdf",
            'file_size'   => '0.5 MB',
            'is_verified' => true,
            'uploaded_by' => $admin->id,
        ]);

        // Tracer Study alumni
        TracerStudy::create([
            'user_id'      => $alumni->id,
            'status'       => 'Kuliah / Melanjutkan Studi',
            'nama_instansi'=> 'Universitas Indonesia',
            'kota'         => 'Depok',
            'tahun_masuk'  => '2024',
            'prodi'        => 'Teknik Informatika',
        ]);

        $this->command->info('✅ Seeder SALUT selesai! Data dummy berhasil dibuat.');
        $this->command->info('');
        $this->command->info('   🔑 Login credentials:');
        $this->command->info('   Admin   → NISN: 0000000001 | Password: admin123');
        $this->command->info('   Guru    → NISN: 0000000002 | Password: guru123');
        $this->command->info('   Siswa   → NISN: 0054321987 | Password: siswa123');
        $this->command->info('   Alumni  → NISN: 0067890123 | Password: alumni123');
    }
}