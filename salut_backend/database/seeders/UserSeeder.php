<?php
namespace Database\Seeders;

use App\Models\User;
use App\Models\Achievement;
use App\Models\GraduationDoc;
use App\Models\TracerStudy;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

/**
 * Seeder SALUT v2.0
 * Total data: 210 pengguna
 *   - 1  Admin
 *   - 1  Guru (+ 3 guru tambahan = 4 guru)
 *   - 63 Siswa Kelas X   (32 L + 31 P)
 *   - 63 Siswa Kelas XI  (32 L + 31 P)
 *   - 64 Siswa Kelas XII (33 L + 31 P)  → total siswa = 190
 *   - 10 Alumni (5 L + 5 P)
 *   = 205 + 5 (admin+guru) = 210 total
 */
class UserSeeder extends Seeder
{
    // ── Nama depan & belakang pool ─────────────────────────────────────────────
    private array $namaDepanL = [
        'Ahmad','Budi','Dani','Eko','Fajar','Galih','Hendra','Irfan','Joko','Kurniawan',
        'Lukman','Maulana','Nanda','Omar','Pandu','Rama','Sandi','Teguh','Umar','Vino',
        'Wahyu','Xander','Yusuf','Zaki','Andri','Bagas','Cahyo','Dimas','Erwin','Faisal',
        'Gilang','Hafiz','Ivan','Julyan','Krisna',
    ];
    private array $namaDepanP = [
        'Ayu','Bella','Citra','Dewi','Eka','Fitri','Gita','Hani','Indah','Julia',
        'Karina','Lina','Maya','Nila','Okta','Putri','Ratna','Sari','Tika','Umi',
        'Vera','Wulan','Xena','Yuni','Zahra','Anis','Bunga','Cahyani','Desi','Elsa',
        'Farah','Grace','Hesti','Intan','Jasmine',
    ];
    private array $namaBelakang = [
        'Santoso','Rahayu','Susanto','Wibowo','Pratama','Kurniawan','Hidayat','Nugroho',
        'Saputra','Lestari','Wijaya','Purnama','Setiawan','Ardian','Firmansyah',
        'Mulyadi','Cahyani','Permatasari','Handayani','Kusuma','Maulana','Febrianti',
        'Prasetyo','Anggraeni','Yulianto','Safitri','Ramadhan','Khoirunnisa','Utama',
        'Hakim','Septiani','Surya','Puspita','Ismail','Nuraini',
    ];
    private array $kota = [
        'Bandung','Jakarta','Surabaya','Yogyakarta','Medan','Semarang','Palembang',
        'Makassar','Denpasar','Malang','Depok','Tangerang','Bekasi','Bogor','Solo',
    ];
    private array $kampus = [
        'Universitas Indonesia','Institut Teknologi Bandung','Universitas Gadjah Mada',
        'Universitas Airlangga','Universitas Padjadjaran','Institut Teknologi Sepuluh Nopember',
        'Universitas Diponegoro','Universitas Lampung','Universitas Sriwijaya',
        'Universitas Hasanuddin',
    ];
    private array $perusahaan = [
        'PT Astra International','PT Telkom Indonesia','PT Bank Mandiri','PT BCA',
        'PT Pertamina','PT PLN','Gojek Indonesia','Tokopedia','Bukalapak','PT Unilever',
    ];
    private array $jabatan = ['Staff IT','Analis Data','Marketing','Finance','HRD','Operator','Teknisi'];
    private array $prodi = [
        'Teknik Informatika','Sistem Informasi','Manajemen','Akuntansi',
        'Teknik Elektro','Ekonomi','Ilmu Komunikasi','Pendidikan','Hukum','Kedokteran',
    ];

    /** Generate NISN unik: awalan digit + padding */
    private function nisn(int $n): string
    {
        return str_pad((string)($n + 1000000), 10, '0', STR_PAD_LEFT);
    }

    /** Pilih nama acak dari pool berdasarkan gender */
    private function nama(bool $isLaki, int $index): string
    {
        $pool  = $isLaki ? $this->namaDepanL : $this->namaDepanP;
        $depan = $pool[$index % count($pool)];
        $belakang = $this->namaBelakang[($index * 3 + ($isLaki ? 1 : 7)) % count($this->namaBelakang)];
        return "$depan $belakang";
    }

    public function run(): void
    {
        // ─────────────────────────────────────────────────────────────────────
        // 1. ADMIN
        // ─────────────────────────────────────────────────────────────────────
        $admin = User::create([
            'name'      => 'Administrator SALUT',
            'nisn'      => '0000000001',
            'email'     => 'admin@salut.sch.id',
            'password'  => Hash::make('admin123'),
            'role'      => 'admin',
            'school'    => 'SMA Negeri 1 Teladan',
            'is_active' => true,
        ]);

        // ─────────────────────────────────────────────────────────────────────
        // 2. GURU (4 orang)
        // ─────────────────────────────────────────────────────────────────────
        $guruData = [
            ['Drs. Suharto, M.Pd',      '0000000002', 'guru@salut.sch.id',     'guru123'],
            ['Ibu Ratna Dewi, S.Pd',    '0000000003', 'ratna@salut.sch.id',    'guru123'],
            ['Bpk. Arif Budiman, M.Pd', '0000000004', 'arif@salut.sch.id',     'guru123'],
            ['Ibu Sri Wahyuni, S.Pd',   '0000000005', 'sriwahyuni@salut.sch.id','guru123'],
        ];
        $guru = null;
        foreach ($guruData as $i => $g) {
            $created = User::create([
                'name'      => $g[0],
                'nisn'      => $g[1],
                'email'     => $g[2],
                'password'  => Hash::make($g[3]),
                'role'      => 'guru',
                'school'    => 'SMA Negeri 1 Teladan',
                'is_active' => true,
            ]);
            if ($i === 0) $guru = $created; // guru pertama untuk validasi
        }

        // ─────────────────────────────────────────────────────────────────────
        // 3. SISWA — 190 total (63 Kelas X + 63 Kelas XI + 64 Kelas XII)
        //    Tiap kelas: L dulu, P kemudian
        // ─────────────────────────────────────────────────────────────────────
        $kelasList = [
            'X'   => ['X IPA 1','X IPA 2','X IPS 1','X IPS 2'],
            'XI'  => ['XI IPA 1','XI IPA 2','XI IPS 1','XI IPS 2'],
            'XII' => ['XII IPA 1','XII IPA 2','XII IPS 1','XII IPS 2'],
        ];
        $angkatanMap = ['X' => 2028, 'XI' => 2027, 'XII' => 2026];
        $countMap    = ['X' => 63,  'XI' => 63,   'XII' => 64];
        // Gender split: 32 L + 31 P per kelas (64: 33 L + 31 P)
        $lCountMap  = ['X' => 32, 'XI' => 32, 'XII' => 33];

        $nisnCounter = 10; // mulai dari 0000000011
        $idxL = 0; $idxP = 0;
        $siswaSatu = null; // simpan 1 siswa untuk contoh prestasi

        foreach (['X', 'XI', 'XII'] as $tingkat) {
            $total  = $countMap[$tingkat];
            $lCount = $lCountMap[$tingkat];
            $pCount = $total - $lCount;
            $kelasPilihan = $kelasList[$tingkat];
            $angkatan = $angkatanMap[$tingkat];

            for ($i = 0; $i < $lCount; $i++) {
                $kelas = $kelasPilihan[$i % count($kelasPilihan)];
                $s = User::create([
                    'name'       => $this->nama(true, $idxL++),
                    'nisn'       => $this->nisn($nisnCounter++),
                    'email'      => $this->nisn($nisnCounter - 1) . '@salut.sch.id',
                    'password'   => Hash::make('siswa123'),
                    'role'       => 'siswa',
                    'school'     => 'SMA Negeri 1 Teladan',
                    'class_name' => $kelas,
                    'angkatan'   => $angkatan,
                    'is_active'  => true,
                ]);
                if ($siswaSatu === null) $siswaSatu = $s;
            }

            for ($i = 0; $i < $pCount; $i++) {
                $kelas = $kelasPilihan[$i % count($kelasPilihan)];
                $s = User::create([
                    'name'       => $this->nama(false, $idxP++),
                    'nisn'       => $this->nisn($nisnCounter++),
                    'email'      => $this->nisn($nisnCounter - 1) . '@salut.sch.id',
                    'password'   => Hash::make('siswa123'),
                    'role'       => 'siswa',
                    'school'     => 'SMA Negeri 1 Teladan',
                    'class_name' => $kelas,
                    'angkatan'   => $angkatan,
                    'is_active'  => true,
                ]);
            }
        }

        // ─────────────────────────────────────────────────────────────────────
        // 4. ALUMNI — 10 orang (5 L + 5 P), angkatan 2024-2025
        // ─────────────────────────────────────────────────────────────────────
        $alumniAngkatan = [2024, 2024, 2024, 2025, 2025, 2024, 2025, 2025, 2024, 2025];
        $alumniKelulusan = [
            '2024-06-15','2024-06-15','2024-06-15','2025-06-14','2025-06-14',
            '2024-06-15','2025-06-14','2025-06-14','2024-06-15','2025-06-14',
        ];
        $statusTracer = [
            'Kuliah / Melanjutkan Studi','Bekerja','Bekerja','Kuliah / Melanjutkan Studi',
            'Wirausaha','Bekerja','Kuliah / Melanjutkan Studi','Bekerja','Wirausaha','Kuliah / Melanjutkan Studi',
        ];

        $alumniList = [];
        for ($i = 0; $i < 10; $i++) {
            $isLaki = $i < 5;
            $angkatan = $alumniAngkatan[$i];
            $nisn = $this->nisn($nisnCounter++);
            $namaAlumni = $this->nama($isLaki, $i + 20);

            $al = User::create([
                'name'            => $namaAlumni,
                'nisn'            => $nisn,
                'email'           => $nisn . '@salut.sch.id',
                'password'        => Hash::make('alumni123'),
                'role'            => 'alumni',
                'school'          => 'SMA Negeri 1 Teladan',
                'class_name'      => $isLaki ? 'XII IPA 1' : 'XII IPS 2',
                'angkatan'        => $angkatan,
                'graduation_date' => $alumniKelulusan[$i],
                'is_active'       => true,
            ]);

            // Arsip dokumen untuk setiap alumni
            GraduationDoc::create([
                'user_id'     => $al->id,
                'doc_type'    => 'ijazah',
                'title'       => 'Ijazah SMA Negeri 1 Teladan',
                'file_path'   => "angkatan_{$angkatan}/nisn_{$nisn}/ijazah.pdf",
                'file_size'   => '1.' . ($i + 1) . ' MB',
                'is_verified' => true,
                'uploaded_by' => $admin->id,
            ]);
            GraduationDoc::create([
                'user_id'     => $al->id,
                'doc_type'    => 'skl',
                'title'       => 'Surat Keterangan Lulus',
                'file_path'   => "angkatan_{$angkatan}/nisn_{$nisn}/skl.pdf",
                'file_size'   => '0.' . (5 + $i % 4) . ' MB',
                'is_verified' => true,
                'uploaded_by' => $admin->id,
            ]);
            GraduationDoc::create([
                'user_id'     => $al->id,
                'doc_type'    => 'skhun',
                'title'       => 'SKHUN',
                'file_path'   => "angkatan_{$angkatan}/nisn_{$nisn}/skhun.pdf",
                'file_size'   => '0.' . (3 + $i % 3) . ' MB',
                'is_verified' => true,
                'uploaded_by' => $admin->id,
            ]);

            // Tracer Study
            $status = $statusTracer[$i];
            $tracerData = [
                'user_id'  => $al->id,
                'status'   => $status,
                'kota'     => $this->kota[$i % count($this->kota)],
                'tahun_masuk' => (string)($angkatan),
            ];
            if ($status === 'Kuliah / Melanjutkan Studi') {
                $tracerData['nama_instansi'] = $this->kampus[$i % count($this->kampus)];
                $tracerData['prodi']         = $this->prodi[$i % count($this->prodi)];
            } elseif ($status === 'Bekerja') {
                $tracerData['nama_instansi'] = $this->perusahaan[$i % count($this->perusahaan)];
                $tracerData['jabatan']       = $this->jabatan[$i % count($this->jabatan)];
            } else {
                $tracerData['nama_instansi'] = 'Usaha Mandiri';
                $tracerData['jabatan']       = 'Pemilik Usaha';
            }
            TracerStudy::create($tracerData);

            $alumniList[] = $al;
        }

        // ─────────────────────────────────────────────────────────────────────
        // 5. PRESTASI contoh (untuk siswa pertama & beberapa alumni)
        // ─────────────────────────────────────────────────────────────────────
        if ($siswaSatu) {
            Achievement::create([
                'user_id'        => $siswaSatu->id,
                'nama_kegiatan'  => 'Olimpiade Fisika Provinsi',
                'penyelenggara'  => 'Dinas Pendidikan Provinsi',
                'tingkat'        => 'Provinsi',
                'peringkat'      => 'Juara 1',
                'tahun'          => 2025,
                'deskripsi'      => 'Mewakili sekolah dalam olimpiade fisika tingkat provinsi.',
                'status_validasi'=> 'Approved',
                'validated_by'   => $guru->id,
                'validated_at'   => now(),
            ]);
            Achievement::create([
                'user_id'        => $siswaSatu->id,
                'nama_kegiatan'  => 'Lomba Karya Ilmiah Nasional',
                'penyelenggara'  => 'Kemendikbudristek',
                'tingkat'        => 'Nasional',
                'peringkat'      => 'Finalis',
                'tahun'          => 2025,
                'deskripsi'      => 'Penelitian bidang energi terbarukan.',
                'status_validasi'=> 'Pending',
            ]);
        }

        // ─────────────────────────────────────────────────────────────────────
        // Output summary
        // ─────────────────────────────────────────────────────────────────────
        $totalSiswa = User::where('role', 'siswa')->count();
        $totalAlumni = User::where('role', 'alumni')->count();
        $totalGuru = User::where('role', 'guru')->count();

        $this->command->info('');
        $this->command->info('╔════════════════════════════════════════╗');
        $this->command->info('║   ✅  SEEDER SALUT v2.0 SELESAI        ║');
        $this->command->info('╠════════════════════════════════════════╣');
        $this->command->info("║  👨‍💼 Admin   : 1                       ║");
        $this->command->info("║  👩‍🏫 Guru    : {$totalGuru}                       ║");
        $this->command->info("║  👨‍🎓 Siswa   : {$totalSiswa} (63 X + 63 XI + 64 XII)");
        $this->command->info("║  🎓 Alumni  : {$totalAlumni} (5L + 5P)              ║");
        $this->command->info('╠════════════════════════════════════════╣');
        $this->command->info('║  🔑 LOGIN CREDENTIALS:                 ║');
        $this->command->info('║  Admin   → 0000000001 | admin123       ║');
        $this->command->info('║  Guru    → 0000000002 | guru123        ║');
        $this->command->info('║  Siswa   → 0000000011 | siswa123       ║');
        $this->command->info('║  Alumni  → (lihat DB) | alumni123      ║');
        $this->command->info('╚════════════════════════════════════════╝');
        $this->command->info('');
    }
}