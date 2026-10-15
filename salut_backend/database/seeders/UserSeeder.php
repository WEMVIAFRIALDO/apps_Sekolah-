<?php
namespace Database\Seeders;

use App\Models\User;
use App\Models\Achievement;
use App\Models\GraduationDoc;
use App\Models\TracerStudy;
use App\Models\SkillCompetency;
use App\Models\AcademicRecord;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Schema;

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
        'Universitas Diponegoro','Politeknik Negeri Bandung','Politeknik Elektronika Negeri Surabaya',
        'Universitas Hasanuddin',
    ];
    private array $perusahaan = [
        'PT Astra International','PT Telkom Indonesia','PT Bank Mandiri','PT BCA',
        'PT Pertamina','CV Solusi Digital','Gojek Indonesia','Tokopedia','PT Infomedia','CV NetWork Pro',
    ];
    private array $jabatan = ['Staff IT','Teknisi Jaringan','Web Developer','Admin Sistem','Desainer Grafis','Operator','Teknisi Hardware'];
    private array $prodi = [
        'Teknik Informatika','Sistem Informasi','Manajemen Informatika','Teknik Komputer Jaringan',
        'Rekayasa Perangkat Lunak','Desain Komunikasi Visual','Akuntansi','Teknik Elektro',
    ];
    // ── Jurusan SMK ──────────────────────────────────────────────────────────
    private array $jurusanList = ['TKJ', 'RPL', 'Multimedia', 'Akuntansi', 'Pemasaran'];
    // Bidang industri sesuai jurusan SMK
    private array $bidangIndustri = [
        'TKJ'       => ['Jaringan & Telekomunikasi', 'IT Support', 'Infrastruktur IT'],
        'RPL'       => ['Pengembangan Software', 'Web Developer', 'Mobile Developer'],
        'Multimedia'=> ['Desain Grafis', 'Periklanan', 'Videografi & Animasi'],
        'Akuntansi' => ['Perbankan', 'Keuangan', 'Perpajakan'],
        'Pemasaran' => ['Retail', 'E-Commerce', 'Digital Marketing'],
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
        Schema::disableForeignKeyConstraints();
        SkillCompetency::truncate();
        Achievement::truncate();
        TracerStudy::truncate();
        GraduationDoc::truncate();
        AcademicRecord::truncate();
        User::truncate();
        Schema::enableForeignKeyConstraints();

        // ─────────────────────────────────────────────────────────────────────
        // 1. ADMIN
        // ─────────────────────────────────────────────────────────────────────
        $admin = User::create([
            'name'      => 'Administrator SALUT',
            'nisn'      => '0000000001',
            'email'     => 'admin@salut.sch.id',
            'password'  => Hash::make('admin123'),
            'role'      => 'admin',
            'school'    => 'SMK Negeri 1 Teladan',
            'is_active' => true,
        ]);

        // ─────────────────────────────────────────────────────────────────────
        // 2. GURU (4 orang) — masing-masing wali jurusan
        // ─────────────────────────────────────────────────────────────────────
        $guruData = [
            ['Drs. Suharto, M.Pd',      '0000000002', 'guru@salut.sch.id',     'guru123', 'TKJ'],
            ['Ibu Ratna Dewi, S.Pd',    '0000000003', 'ratna@salut.sch.id',    'guru123', 'RPL'],
            ['Bpk. Arif Budiman, M.Pd', '0000000004', 'arif@salut.sch.id',     'guru123', 'Multimedia'],
            ['Ibu Sri Wahyuni, S.Pd',   '0000000005', 'sriwahyuni@salut.sch.id','guru123','Akuntansi'],
        ];
        $guru = null;
        $gurusByJurusan = [];
        foreach ($guruData as $i => $g) {
            $created = User::create([
                'name'      => $g[0],
                'nisn'      => $g[1],
                'email'     => $g[2],
                'password'  => Hash::make($g[3]),
                'role'      => 'guru',
                'jurusan'   => $g[4],
                'school'    => 'SMK Negeri 1 Teladan',
                'is_active' => true,
            ]);
            $gurusByJurusan[$g[4]] = $created;
            if ($i === 0) $guru = $created; // guru pertama untuk validasi
        }

        // ─────────────────────────────────────────────────────────────────────
        // 3. SISWA — 190 total (63 Kelas X + 63 Kelas XI + 64 Kelas XII)
        //    Tiap kelas: L dulu, P kemudian
        // ─────────────────────────────────────────────────────────────────────
        // SMK: kelas berdasarkan jurusan bukan IPA/IPS
        $kelasList = [
            'X'   => ['X TKJ 1','X TKJ 2','X RPL 1','X Multimedia 1'],
            'XI'  => ['XI TKJ 1','XI TKJ 2','XI RPL 1','XI Multimedia 1'],
            'XII' => ['XII TKJ 1','XII TKJ 2','XII RPL 1','XII Multimedia 1'],
        ];
        // Mapping kelas → jurusan SMK
        $jurusanByKelas = [
            'TKJ 1' => 'TKJ', 'TKJ 2' => 'TKJ',
            'RPL 1' => 'RPL', 'Multimedia 1' => 'Multimedia',
        ];
        $angkatanMap = ['X' => 2028, 'XI' => 2027, 'XII' => 2026];
        $countMap    = ['X' => 63,  'XI' => 63,   'XII' => 64];
        // Gender split: 32 L + 31 P per kelas (64: 33 L + 31 P)
        $lCountMap  = ['X' => 32, 'XI' => 32, 'XII' => 33];

        $nisnCounter = 10; // mulai dari 0000000011
        $idxL = 0; $idxP = 0;
        $siswaSatu = null; // simpan 1 siswa untuk contoh prestasi
        $allStudents = [];

        // Siswa Demo Utama (Budi Santoso - sesuai LOGIN_SALUT.txt)
        $budi = User::create([
            'name'       => 'Budi Santoso',
            'nisn'       => '0054321987',
            'email'      => '0054321987@salut.sch.id',
            'password'   => Hash::make('siswa123'),
            'role'       => 'siswa',
            'school'     => 'SMK Negeri 1 Teladan',
            'class_name' => 'XII RPL 1',
            'jurusan'    => 'RPL',
            'angkatan'   => 2026,
            'is_active'  => true,
        ]);
        $siswaSatu = $budi;
        $allStudents[] = $budi;

        foreach (['X', 'XI', 'XII'] as $tingkat) {
            $total  = $countMap[$tingkat];
            $lCount = $lCountMap[$tingkat];
            $pCount = $total - $lCount;
            $kelasPilihan = $kelasList[$tingkat];
            $angkatan = $angkatanMap[$tingkat];

            for ($i = 0; $i < $lCount; $i++) {
                $kelas = $kelasPilihan[$i % count($kelasPilihan)];
                // Ekstrak jurusan dari nama kelas (misal: "X TKJ 1" → ambil setelah tingkat)
                $kelasKey = trim(str_replace($tingkat, '', $kelas));
                $jurusan  = $jurusanByKelas[$kelasKey] ?? 'TKJ';
                $s = User::create([
                    'name'       => $this->nama(true, $idxL++),
                    'nisn'       => $this->nisn($nisnCounter++),
                    'email'      => $this->nisn($nisnCounter - 1) . '@salut.sch.id',
                    'password'   => Hash::make('siswa123'),
                    'role'       => 'siswa',
                    'school'     => 'SMK Negeri 1 Teladan',
                    'class_name' => $kelas,
                    'jurusan'    => $jurusan,
                    'angkatan'   => $angkatan,
                    'is_active'  => true,
                ]);
                $allStudents[] = $s;
                if ($siswaSatu === null) $siswaSatu = $s;
            }

            for ($i = 0; $i < $pCount; $i++) {
                $kelas = $kelasPilihan[$i % count($kelasPilihan)];
                $kelasKey = trim(str_replace($tingkat, '', $kelas));
                $jurusan  = $jurusanByKelas[$kelasKey] ?? 'TKJ';
                $s = User::create([
                    'name'       => $this->nama(false, $idxP++),
                    'nisn'       => $this->nisn($nisnCounter++),
                    'email'      => $this->nisn($nisnCounter - 1) . '@salut.sch.id',
                    'password'   => Hash::make('siswa123'),
                    'role'       => 'siswa',
                    'school'     => 'SMK Negeri 1 Teladan',
                    'class_name' => $kelas,
                    'jurusan'    => $jurusan,
                    'angkatan'   => $angkatan,
                    'is_active'  => true,
                ]);
                $allStudents[] = $s;
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

        // Alumni Demo Utama (Siti Rahayu - sesuai LOGIN_SALUT.txt)
        $siti = User::create([
            'name'            => 'Siti Rahayu',
            'nisn'            => '0067890123',
            'email'           => '0067890123@salut.sch.id',
            'password'        => Hash::make('alumni123'),
            'role'            => 'alumni',
            'school'          => 'SMK Negeri 1 Teladan',
            'class_name'      => 'XII TKJ 1',
            'jurusan'         => 'TKJ',
            'angkatan'        => 2024,
            'graduation_date' => '2024-06-15',
            'is_active'       => true,
        ]);
        GraduationDoc::create([
            'user_id'     => $siti->id,
            'doc_type'    => 'ijazah',
            'title'       => 'Ijazah Asli Digital',
            'file_path'   => "angkatan_2024/nisn_0067890123/ijazah.pdf",
            'file_size'   => '2.4 MB',
            'is_verified' => true,
            'uploaded_by' => $admin->id,
        ]);
        GraduationDoc::create([
            'user_id'     => $siti->id,
            'doc_type'    => 'skhun',
            'title'       => 'SKHUN',
            'file_path'   => "angkatan_2024/nisn_0067890123/skhun.pdf",
            'file_size'   => '1.8 MB',
            'is_verified' => true,
            'uploaded_by' => $admin->id,
        ]);
        TracerStudy::create([
            'user_id'         => $siti->id,
            'status'          => 'Bekerja',
            'kota'            => 'Bandung',
            'tahun_masuk'     => '2024',
            'nama_instansi'   => 'PT Telkom Indonesia',
            'jabatan'         => 'Teknisi Jaringan',
            'bidang_industri' => 'Jaringan & Telekomunikasi',
        ]);
        $alumniList[] = $siti;

        for ($i = 0; $i < 10; $i++) {
            $isLaki = $i < 5;
            $angkatan = $alumniAngkatan[$i];
            $nisn = $this->nisn($nisnCounter++);
            $namaAlumni = $this->nama($isLaki, $i + 20);

            $jurusanAlumni = $this->jurusanList[$i % count($this->jurusanList)];
            $al = User::create([
                'name'            => $namaAlumni,
                'nisn'            => $nisn,
                'email'           => $nisn . '@salut.sch.id',
                'password'        => Hash::make('alumni123'),
                'role'            => 'alumni',
                'school'          => 'SMK Negeri 1 Teladan',
                'class_name'      => 'XII ' . $jurusanAlumni . ' 1',
                'jurusan'         => $jurusanAlumni,
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
                $namaKampus = $this->kampus[$i % count($this->kampus)];
                $namaProdi  = $this->prodi[$i % count($this->prodi)];
                $tracerData['nama_instansi'] = $namaKampus;
                $tracerData['nama_kampus']   = $namaKampus;
                $tracerData['prodi']         = $namaProdi;
                $tracerData['nama_prodi']    = $namaProdi;
            } elseif ($status === 'Bekerja') {
                $bidangArr   = $this->bidangIndustri[$jurusanAlumni] ?? ['IT'];
                $bidang      = $bidangArr[$i % count($bidangArr)];
                $namaPerush  = $this->perusahaan[$i % count($this->perusahaan)];
                $tracerData['nama_instansi']  = $namaPerush;
                $tracerData['jabatan']        = $this->jabatan[$i % count($this->jabatan)];
                $tracerData['bidang_industri']= $bidang;
            } else {
                $tracerData['nama_instansi']  = 'Usaha Mandiri';
                $tracerData['jabatan']        = 'Pemilik Usaha';
                $tracerData['bidang_industri']= 'Wirausaha';
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
                'nama_kegiatan'  => 'LKS (Lomba Kompetensi Siswa) Tingkat Kota',
                'penyelenggara'  => 'Dinas Pendidikan Kota',
                'tingkat'        => 'Kecamatan / Kabupaten',
                'peringkat'      => 'Juara 1',
                'tahun'          => 2025,
                'deskripsi'      => 'Mewakili sekolah dalam Lomba Kompetensi Siswa bidang IT tingkat kota.',
                'status_validasi'=> 'Approved',
                'validated_by'   => $guru->id,
                'validated_at'   => now(),
            ]);
            Achievement::create([
                'user_id'        => $siswaSatu->id,
                'nama_kegiatan'  => 'Hackathon Pelajar SMK Tingkat Provinsi',
                'penyelenggara'  => 'Kemendikbudristek',
                'tingkat'        => 'Provinsi',
                'peringkat'      => 'Finalis Top 10',
                'tahun'          => 2025,
                'deskripsi'      => 'Membuat aplikasi solusi digital untuk UMKM lokal.',
                'status_validasi'=> 'Pending',
            ]);
        }

        // ─────────────────────────────────────────────────────────────────────
        // 6. SKILL RAPORT / PORTOFOLIO KOMPETENSI SISWA SMK
        // ─────────────────────────────────────────────────────────────────────
        $skillCatalog = [
            'TKJ' => [
                ['Administrasi Server Linux (Debian/Ubuntu)', 'Sistem Operasi Jaringan', 'Mahir', 'Instalasi & konfigurasi DNS, Web Server, DHCP, FTP'],
                ['Routing MikroTik Fundamental (MTCNA)', 'Jaringan Komputer', 'Mahir', 'Static & Dynamic Routing (OSPF), Bandwidth Management'],
                ['Instalasi & Troubleshooting Fiber Optic', 'Infrastruktur Jaringan', 'Terampil', 'Penyambungan FO Splicer, Pengujian OTDR & OPM'],
                ['Keamanan Jaringan & Firewall Filtering', 'Cyber Security', 'Terampil', 'Konfigurasi IPTables, Port Knocking, VPN Wireguard'],
            ],
            'RPL' => [
                ['Pengembangan RESTful API dengan Laravel', 'Web Development', 'Mahir', 'Arsitektur MVC, Autentikasi JWT, Relasi Eloquent ORM'],
                ['Pemrograman Mobile Multiplatform (Flutter & Dart)', 'Mobile Development', 'Mahir', 'State Management GetX/Provider, Integrasi REST API'],
                ['Manajemen Basis Data Relasional (MySQL)', 'Database Engineering', 'Mahir', 'Normalisasi DB, Stored Procedures, Indexing & Query Optimization'],
                ['Frontend Web Modern (Tailwind CSS & JavaScript)', 'Web Development', 'Terampil', 'Responsive Design, DOM Manipulation, Async/Await'],
            ],
            'Multimedia' => [
                ['Desain Antarmuka Pengguna / UI/UX (Figma)', 'Desain Grafis', 'Mahir', 'Wireframing, High-Fidelity Prototyping, Design System'],
                ['Video Editing & Audio Mixing (Adobe Premiere)', 'Audio-Visual', 'Mahir', 'Cut-to-beat, Multi-camera Editing, Audio Mastering'],
                ['Motion Graphics & Visual Effects (After Effects)', 'Animasi', 'Terampil', 'Kinetic Typography, Shape Layers, 2D Character Rigging'],
                ['Desain Vektor & Corporate Branding (Illustrator)', 'Desain Grafis', 'Mahir', 'Pembuatan Logo Vektor, Buku Pedoman Brand (GSM)'],
            ],
            'Akuntansi' => [
                ['Komputerisasi Akuntansi (MYOB & Accurate)', 'Akuntansi Keuangan', 'Mahir', 'Setup Data Awal, Jurnal Khusus, Buku Besar, Neraca'],
                ['Penyusunan Laporan Keuangan Standar PSAK', 'Akuntansi Keuangan', 'Mahir', 'Laporan Laba Rugi, Perubahan Modal, Arus Kas'],
                ['Perhitungan & Pelaporan Pajak Terapan (e-SPT)', 'Perpajakan', 'Terampil', 'PPh Pasal 21, PPh Badan, dan PPN Faktur Pajak'],
            ],
            'Pemasaran' => [
                ['Digital Marketing Campaign & Social Media Ads', 'Pemasaran Digital', 'Mahir', 'Meta Ads Manager, Content Planning, Copywriting'],
                ['Pengelolaan Toko Online E-Commerce & Marketplace', 'E-Commerce', 'Mahir', 'Optimalisasi SEO Toko, Live Streaming Sales, Analisis GMV'],
                ['Teknik Negosiasi & Manajemen Hubungan Pelanggan', 'Penjualan', 'Terampil', 'Handling Objections, CRM Software, Closing Deals'],
            ],
        ];

        // Seed skill untuk alumni
        foreach ($alumniList as $al) {
            $j = $al->jurusan ?? 'TKJ';
            $pool = $skillCatalog[$j] ?? $skillCatalog['TKJ'];
            $guruPenguji = $gurusByJurusan[$j] ?? $guru;
            foreach ($pool as $item) {
                SkillCompetency::create([
                    'user_id'         => $al->id,
                    'guru_id'         => $guruPenguji->id,
                    'nama_kompetensi' => $item[0],
                    'kategori'        => $item[1],
                    'level'           => $item[2],
                    'keterangan'      => $item[3],
                    'semester'        => 'Genap',
                    'tahun_pelajaran' => '2023/2024',
                ]);
            }
        }

        // Seed skill untuk siswa (misal 50 siswa)
        $sampleStudents = array_slice($allStudents, 0, 50);
        foreach ($sampleStudents as $s) {
            $j = $s->jurusan ?? 'TKJ';
            $pool = $skillCatalog[$j] ?? $skillCatalog['TKJ'];
            $guruPenguji = $gurusByJurusan[$j] ?? $guru;
            for ($k = 0; $k < min(2, count($pool)); $k++) {
                $item = $pool[$k];
                SkillCompetency::create([
                    'user_id'         => $s->id,
                    'guru_id'         => $guruPenguji->id,
                    'nama_kompetensi' => $item[0],
                    'kategori'        => $item[1],
                    'level'           => $item[2],
                    'keterangan'      => $item[3],
                    'semester'        => 'Ganjil',
                    'tahun_pelajaran' => '2025/2026',
                ]);
            }
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