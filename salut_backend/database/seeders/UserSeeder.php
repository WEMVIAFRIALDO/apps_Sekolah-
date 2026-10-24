<?php
namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Schema;

/**
 * Seeder SALUT v3.0 — 200 pengguna dummy untuk statistik dashboard.
 *   - 2   Admin
 *   - 8   Guru (wali/penguji per jurusan)
 *   - 130 Siswa aktif, 3 jurusan (TKJ, RPL, Multimedia), kelas X–XII
 *   - 60  Alumni angkatan 2024–2026, lengkap dengan tracer study
 *         (kuliah di mana, kerja di mana, wirausaha apa)
 *
 * Akun demo tetap sama dengan LOGIN_SALUT.txt:
 *   Admin 0000000001 / admin123 · Guru 0000000002 / guru123
 *   Siswa 0054321987 / siswa123 · Alumni 0067890123 / alumni123
 *
 * Insert memakai DB::table (bulk) supaya cepat.
 */
class UserSeeder extends Seeder
{
    private const SEKOLAH = 'SMK Negeri 1 Teladan';
    private const JURUSAN = ['TKJ', 'RPL', 'Multimedia'];

    // ── Pool nama ────────────────────────────────────────────────────────────
    private array $depanL = [
        'Ahmad','Budi','Dani','Eko','Fajar','Galih','Hendra','Irfan','Joko','Lukman',
        'Maulana','Nanda','Pandu','Rama','Sandi','Teguh','Umar','Vino','Wahyu','Yusuf',
        'Zaki','Andri','Bagas','Cahyo','Dimas','Erwin','Faisal','Gilang','Hafiz','Ivan',
        'Krisna','Rizky','Arya','Bayu','Reza','Aldi','Fikri','Yoga','Ilham','Agung',
    ];
    private array $depanP = [
        'Ayu','Bella','Citra','Dewi','Eka','Fitri','Gita','Hani','Indah','Julia',
        'Karina','Lina','Maya','Nila','Okta','Putri','Ratna','Sari','Tika','Umi',
        'Vera','Wulan','Yuni','Zahra','Anis','Bunga','Desi','Elsa','Farah','Hesti',
        'Intan','Jasmine','Nadia','Salsa','Tiara','Aulia','Dinda','Kirana','Laras','Nabila',
    ];
    private array $belakang = [
        'Santoso','Rahayu','Susanto','Wibowo','Pratama','Kurniawan','Hidayat','Nugroho',
        'Saputra','Lestari','Wijaya','Purnama','Setiawan','Ardian','Firmansyah','Mulyadi',
        'Permatasari','Handayani','Kusuma','Febrianti','Prasetyo','Anggraeni','Yulianto',
        'Safitri','Ramadhan','Utama','Hakim','Septiani','Surya','Puspita','Ismail','Nuraini',
    ];

    // ── Tujuan alumni setelah lulus ─────────────────────────────────────────
    /** Index 0–5 kampus di Lampung, 6–9 luar Lampung */
    private array $kampus = [
        'Universitas Lampung', 'Institut Teknologi Sumatera', 'Politeknik Negeri Lampung',
        'Universitas Teknokrat Indonesia', 'IIB Darmajaya', 'UIN Raden Intan Lampung',
        'Universitas Gadjah Mada', 'Institut Teknologi Bandung', 'Universitas Indonesia',
        'Politeknik Negeri Jakarta',
    ];
    private array $kotaKampus = [
        'Bandar Lampung', 'Lampung Selatan', 'Bandar Lampung', 'Bandar Lampung', 'Bandar Lampung',
        'Bandar Lampung', 'Yogyakarta', 'Bandung', 'Depok', 'Depok',
    ];
    private array $prodiPerJurusan = [
        'TKJ'        => ['Teknik Informatika', 'Teknik Komputer', 'Teknik Elektro', 'Teknologi Rekayasa Jaringan'],
        'RPL'        => ['Teknik Informatika', 'Sistem Informasi', 'Ilmu Komputer', 'Rekayasa Perangkat Lunak'],
        'Multimedia' => ['Desain Komunikasi Visual', 'Ilmu Komunikasi', 'Teknologi Rekayasa Multimedia', 'Film dan Televisi'],
    ];

    /** Tempat kerja per jurusan: [perusahaan, jabatan, bidang industri, kota] */
    private array $kerjaPerJurusan = [
        'TKJ' => [
            ['PT Telkom Indonesia', 'Teknisi Jaringan', 'Jaringan & Telekomunikasi', 'Bandar Lampung'],
            ['PT Indosat Ooredoo Hutchison', 'Network Engineer', 'Jaringan & Telekomunikasi', 'Jakarta'],
            ['PT Biznet Networks', 'Teknisi Fiber Optic', 'Jaringan & Telekomunikasi', 'Bandar Lampung'],
            ['PT Bank Lampung', 'IT Support', 'IT Support & Infrastruktur', 'Bandar Lampung'],
            ['PT Astra International', 'Admin Sistem', 'IT Support & Infrastruktur', 'Jakarta'],
        ],
        'RPL' => [
            ['Gojek Indonesia', 'Junior Mobile Developer', 'Pengembangan Software', 'Jakarta'],
            ['Tokopedia', 'Web Developer', 'Pengembangan Software', 'Jakarta'],
            ['CV Solusi Digital Lampung', 'Programmer', 'Pengembangan Software', 'Bandar Lampung'],
            ['PT Infomedia Nusantara', 'Quality Assurance', 'Pengembangan Software', 'Bandung'],
            ['PT Bank Mandiri', 'Staff IT', 'IT Support & Infrastruktur', 'Bandar Lampung'],
        ],
        'Multimedia' => [
            ['Lampung Post', 'Desainer Grafis', 'Desain & Kreatif', 'Bandar Lampung'],
            ['TVRI Lampung', 'Editor Video', 'Media & Penyiaran', 'Bandar Lampung'],
            ['PT Kreasi Media Nusantara', 'Motion Designer', 'Desain & Kreatif', 'Jakarta'],
            ['CV Visual Kreatif', 'Fotografer', 'Desain & Kreatif', 'Metro'],
            ['PT Shopee International', 'Content Creator', 'Digital Marketing', 'Jakarta'],
        ],
    ];

    /** Usaha alumni per jurusan: [nama usaha, bidang] */
    private array $usahaPerJurusan = [
        'TKJ'        => [['Servis Komputer & Jaringan', 'Jasa Teknologi'], ['Penyedia Internet RT/RW Net', 'Jaringan & Telekomunikasi']],
        'RPL'        => [['Jasa Pembuatan Website', 'Pengembangan Software'], ['Toko Online Aksesoris HP', 'E-Commerce']],
        'Multimedia' => [['Studio Foto & Video', 'Desain & Kreatif'], ['Jasa Desain & Sablon', 'Desain & Kreatif']],
    ];

    private array $gaji = ['< Rp 3 juta', 'Rp 3–5 juta', 'Rp 5–8 juta', '> Rp 8 juta'];

    private int $nisnSeq = 100;
    private string $now;

    private function nisn(): string
    {
        return str_pad((string) (1000000 + $this->nisnSeq++), 10, '0', STR_PAD_LEFT);
    }

    private function nama(bool $laki, int $i): string
    {
        $pool = $laki ? $this->depanL : $this->depanP;
        return $pool[$i % count($pool)] . ' ' . $this->belakang[($i * 7 + ($laki ? 3 : 11)) % count($this->belakang)];
    }

    private function user(array $data): int
    {
        return DB::table('users')->insertGetId($data + [
            'school' => self::SEKOLAH, 'is_active' => true,
            'created_at' => $this->now, 'updated_at' => $this->now,
        ]);
    }

    private function stamp(array $row): array
    {
        return $row + ['created_at' => $this->now, 'updated_at' => $this->now];
    }

    public function run(): void
    {
        mt_srand(2026); // data acak tapi selalu sama setiap seeding
        $this->now = now()->toDateTimeString();
        $hash = [
            'admin'  => Hash::make('admin123'),
            'guru'   => Hash::make('guru123'),
            'siswa'  => Hash::make('siswa123'),
            'alumni' => Hash::make('alumni123'),
        ];

        Schema::disableForeignKeyConstraints();
        foreach (['skill_competencies', 'achievements', 'tracer_studies', 'graduation_docs', 'academic_records', 'users'] as $t) {
            DB::table($t)->truncate();
        }
        Schema::enableForeignKeyConstraints();

        // ─────────────────────────────────────────────────────────────────────
        // 1. ADMIN (2)
        // ─────────────────────────────────────────────────────────────────────
        $adminId = $this->user(['name' => 'Administrator SALUT', 'nisn' => '0000000001', 'email' => 'admin@salut.sch.id', 'password' => $hash['admin'], 'role' => 'admin']);
        $this->user(['name' => 'Staf TU Kurikulum', 'nisn' => '0000000006', 'email' => 'tu@salut.sch.id', 'password' => $hash['admin'], 'role' => 'admin']);

        // ─────────────────────────────────────────────────────────────────────
        // 2. GURU (8) — penguji/validator per jurusan
        // ─────────────────────────────────────────────────────────────────────
        $guruData = [
            ['Drs. Suharto, M.Pd',         '0000000002', 'guru@salut.sch.id',       'TKJ'],
            ['Ibu Ratna Dewi, S.Pd',       '0000000003', 'ratna@salut.sch.id',      'RPL'],
            ['Bpk. Arif Budiman, M.Pd',    '0000000004', 'arif@salut.sch.id',       'Multimedia'],
            ['Ibu Sri Wahyuni, S.Pd',      '0000000005', 'sriwahyuni@salut.sch.id', 'TKJ'],
            ['Bpk. Hendra Gunawan, S.Kom', '0000000007', 'hendra@salut.sch.id',     'RPL'],
            ['Ibu Maya Sari, S.Ds',        '0000000008', 'maya@salut.sch.id',       'Multimedia'],
            ['Bpk. Doni Saputra, S.T',     '0000000009', 'doni@salut.sch.id',       'TKJ'],
            ['Ibu Lestari Putri, M.Kom',   '0000000010', 'lestari@salut.sch.id',    'RPL'],
        ];
        $guruByJurusan = [];
        foreach ($guruData as $g) {
            $id = $this->user(['name' => $g[0], 'nisn' => $g[1], 'email' => $g[2], 'password' => $hash['guru'], 'role' => 'guru', 'jurusan' => $g[3]]);
            $guruByJurusan[$g[3]][] = $id;
        }
        $guruUtama = $guruByJurusan['TKJ'][0];

        // ─────────────────────────────────────────────────────────────────────
        // 3. SISWA AKTIF (130) — tingkat X/XI/XII × jurusan TKJ/RPL/Multimedia
        //    Tahun ajaran 2026/2027 → angkatan = tahun lulus (XII lulus 2027)
        // ─────────────────────────────────────────────────────────────────────
        $sebaranSiswa = [ // [tingkat, jurusan, jumlah] → 129 + 1 siswa demo = 130
            ['X', 'TKJ', 16], ['X', 'RPL', 15], ['X', 'Multimedia', 13],
            ['XI', 'TKJ', 15], ['XI', 'RPL', 15], ['XI', 'Multimedia', 13],
            ['XII', 'TKJ', 15], ['XII', 'RPL', 15], ['XII', 'Multimedia', 12],
        ];
        $angkatanSiswa   = ['X' => 2029, 'XI' => 2028, 'XII' => 2027];
        $semesterSelesai = ['X' => 0, 'XI' => 2, 'XII' => 4];

        $siswa = []; // [id, tingkat, jurusan]
        $budiId = $this->user([
            'name' => 'Budi Santoso', 'nisn' => '0054321987', 'email' => '0054321987@salut.sch.id',
            'password' => $hash['siswa'], 'role' => 'siswa', 'class_name' => 'XII RPL 1',
            'jurusan' => 'RPL', 'angkatan' => 2027,
        ]);
        $siswa[] = [$budiId, 'XII', 'RPL'];

        $idx = 0;
        foreach ($sebaranSiswa as [$tingkat, $jurusan, $jumlah]) {
            for ($i = 0; $i < $jumlah; $i++, $idx++) {
                $rombel = $jurusan === 'TKJ' ? ($i % 2) + 1 : 1; // TKJ punya 2 rombel
                $nisn = $this->nisn();
                $id = $this->user([
                    'name' => $this->nama($i % 2 === 0, $idx), 'nisn' => $nisn, 'email' => "$nisn@salut.sch.id",
                    'password' => $hash['siswa'], 'role' => 'siswa', 'class_name' => "$tingkat $jurusan $rombel",
                    'jurusan' => $jurusan, 'angkatan' => $angkatanSiswa[$tingkat],
                ]);
                $siswa[] = [$id, $tingkat, $jurusan];
            }
        }

        // Nilai rapor per semester yang sudah dilewati
        $rapor = [];
        foreach ($siswa as [$id, $tingkat]) {
            $base = mt_rand(780, 920) / 10;
            for ($s = 1; $s <= $semesterSelesai[$tingkat]; $s++) {
                $rapor[] = $this->stamp([
                    'user_id' => $id, 'semester' => $s,
                    'average_score' => min(98, round($base + mt_rand(-20, 30) / 10, 2)),
                    'rank' => mt_rand(1, 32), 'academic_year' => $angkatanSiswa[$tingkat] - 3 + intdiv($s - 1, 2),
                    'status' => 'Tervalidasi', 'input_by' => $guruUtama,
                ]);
            }
        }
        foreach (array_chunk($rapor, 200) as $chunk) DB::table('academic_records')->insert($chunk);

        // ─────────────────────────────────────────────────────────────────────
        // 4. ALUMNI (60) — angkatan 2024, 2025, 2026 × 3 jurusan
        // ─────────────────────────────────────────────────────────────────────
        // Komposisi status per 20 alumni/angkatan; null = belum mengisi tracer
        $polaStatus = array_merge(
            array_fill(0, 7, 'Bekerja'),
            array_fill(0, 6, 'Kuliah / Melanjutkan Studi'),
            array_fill(0, 3, 'Wirausaha'),
            array_fill(0, 2, 'Mencari Kerja'),
            ['Belum Memutuskan', null]
        );

        $alumni = []; // [id, jurusan, angkatan, status]
        $sitiId = $this->user([
            'name' => 'Siti Rahayu', 'nisn' => '0067890123', 'email' => '0067890123@salut.sch.id',
            'password' => $hash['alumni'], 'role' => 'alumni', 'class_name' => 'XII TKJ 1',
            'jurusan' => 'TKJ', 'angkatan' => 2024, 'graduation_date' => '2024-06-15',
        ]);
        $alumni[] = [$sitiId, 'TKJ', 2024, 'Bekerja'];

        $idx = 0;
        foreach ([2024, 2025, 2026] as $angkatan) {
            $pola = $polaStatus;
            if ($angkatan === 2024) array_shift($pola); // satu slot "Bekerja" sudah dipakai Siti
            shuffle($pola);
            foreach ($pola as $i => $status) {
                $jurusan = self::JURUSAN[$i % 3];
                $nisn = $this->nisn();
                $id = $this->user([
                    'name' => $this->nama(mt_rand(0, 1) === 1, 60 + $idx++), 'nisn' => $nisn, 'email' => "$nisn@salut.sch.id",
                    'password' => $hash['alumni'], 'role' => 'alumni', 'class_name' => "XII $jurusan 1",
                    'jurusan' => $jurusan, 'angkatan' => $angkatan, 'graduation_date' => "$angkatan-06-15",
                ]);
                $alumni[] = [$id, $jurusan, $angkatan, $status];
            }
        }

        // Arsip dokumen + tracer study: ke mana alumni setelah lulus
        $tracer = [];
        $docs = [];
        foreach ($alumni as [$id, $jurusan, $angkatan, $status]) {
            foreach (['ijazah' => 'Ijazah Digital', 'skl' => 'Surat Keterangan Lulus', 'skhun' => 'SKHUN'] as $type => $title) {
                $docs[] = $this->stamp([
                    'user_id' => $id, 'doc_type' => $type, 'title' => $title,
                    'file_path' => "angkatan_$angkatan/user_$id/$type.pdf",
                    'file_size' => (mt_rand(5, 30) / 10) . ' MB', 'is_verified' => true, 'uploaded_by' => $adminId,
                ]);
            }
            if ($status === null) continue;

            $row = [
                'user_id' => $id, 'status' => $status, 'tahun_masuk' => (string) $angkatan,
                'nama_instansi' => null, 'kota' => null, 'jabatan' => null, 'bidang_industri' => null,
                'nama_kampus' => null, 'nama_prodi' => null, 'prodi' => null, 'rentang_gaji' => null, 'keterangan' => null,
            ];
            switch ($status) {
                case 'Bekerja':
                    $pilihan = $this->kerjaPerJurusan[$jurusan];
                    $kerja = $id === $sitiId ? $pilihan[0] : $pilihan[mt_rand(0, count($pilihan) - 1)];
                    $row = array_merge($row, [
                        'nama_instansi' => $kerja[0], 'jabatan' => $kerja[1], 'bidang_industri' => $kerja[2],
                        'kota' => $kerja[3], 'rentang_gaji' => $this->gaji[mt_rand(0, 3)],
                    ]);
                    break;
                case 'Kuliah / Melanjutkan Studi':
                    // ±60% kuliah di Lampung, sisanya ke luar daerah
                    $k = mt_rand(1, 10) <= 6 ? mt_rand(0, 5) : mt_rand(6, 9);
                    $prodi = $this->prodiPerJurusan[$jurusan][mt_rand(0, 3)];
                    $row = array_merge($row, [
                        'nama_instansi' => $this->kampus[$k], 'nama_kampus' => $this->kampus[$k],
                        'prodi' => $prodi, 'nama_prodi' => $prodi, 'kota' => $this->kotaKampus[$k],
                    ]);
                    break;
                case 'Wirausaha':
                    $u = $this->usahaPerJurusan[$jurusan][mt_rand(0, 1)];
                    $row = array_merge($row, [
                        'nama_instansi' => $u[0], 'jabatan' => 'Pemilik Usaha', 'bidang_industri' => $u[1],
                        'kota' => ['Bandar Lampung', 'Metro', 'Pringsewu', 'Kalianda'][mt_rand(0, 3)],
                    ]);
                    break;
                case 'Mencari Kerja':
                    $row['keterangan'] = "Sedang melamar kerja di bidang $jurusan";
                    $row['kota'] = 'Bandar Lampung';
                    break;
                default:
                    $row['keterangan'] = 'Masih mempertimbangkan kuliah atau kerja';
            }
            $tracer[] = $this->stamp($row);
        }
        DB::table('tracer_studies')->insert($tracer);
        foreach (array_chunk($docs, 200) as $chunk) DB::table('graduation_docs')->insert($chunk);

        // ─────────────────────────────────────────────────────────────────────
        // 5. PRESTASI (45) — campuran Approved / Pending / Rejected
        // ─────────────────────────────────────────────────────────────────────
        $lomba = [
            'TKJ'        => ['LKS IT Network Systems Administration', 'Lomba Konfigurasi MikroTik', 'Cyber Security Competition Pelajar'],
            'RPL'        => ['LKS Software Application Development', 'Hackathon Pelajar SMK', 'Lomba Aplikasi Mobile Inovatif'],
            'Multimedia' => ['LKS Graphic Design Technology', 'Festival Film Pendek Pelajar', 'Lomba Desain Poster Digital'],
        ];
        $tingkat   = ['Kecamatan / Kabupaten', 'Kota / Madya', 'Provinsi', 'Nasional', 'Internasional'];
        $bobotTkt  = [0, 0, 0, 1, 1, 1, 2, 2, 3, 4]; // tingkat lokal lebih sering
        $peringkat = ['Juara 1', 'Juara 2', 'Juara 3', 'Harapan 1', 'Finalis', 'Peserta'];
        $statusVal = ['Approved', 'Approved', 'Approved', 'Pending', 'Pending', 'Rejected'];

        $prestasi = [$this->stamp([ // contoh tetap untuk siswa demo
            'user_id' => $budiId, 'nama_kegiatan' => 'LKS Software Application Development Tingkat Kota',
            'penyelenggara' => 'Dinas Pendidikan Kota Bandar Lampung', 'tingkat' => 'Kota / Madya', 'peringkat' => 'Juara 1',
            'tahun' => 2026, 'deskripsi' => 'Mewakili sekolah di bidang pengembangan aplikasi.', 'status_validasi' => 'Approved',
            'catatan' => 'Sertifikat valid.', 'validated_by' => $guruByJurusan['RPL'][0], 'validated_at' => $this->now,
        ])];
        $kandidat = array_slice($siswa, 1);
        shuffle($kandidat);
        foreach (array_slice($kandidat, 0, 44) as [$id, , $jurusan]) {
            $st = $statusVal[mt_rand(0, 5)];
            $prestasi[] = $this->stamp([
                'user_id' => $id, 'nama_kegiatan' => $lomba[$jurusan][mt_rand(0, 2)],
                'penyelenggara' => ['Dinas Pendidikan Provinsi Lampung', 'Kemendikbudristek', 'Universitas Lampung', 'Asosiasi Industri TIK'][mt_rand(0, 3)],
                'tingkat' => $tingkat[$bobotTkt[mt_rand(0, 9)]], 'peringkat' => $peringkat[mt_rand(0, 5)],
                'tahun' => mt_rand(2025, 2026), 'deskripsi' => "Kompetisi bidang $jurusan.",
                'status_validasi' => $st,
                'catatan' => $st === 'Rejected' ? 'Sertifikat tidak terbaca, mohon unggah ulang.' : null,
                'validated_by' => $st === 'Pending' ? null : $guruByJurusan[$jurusan][0],
                'validated_at' => $st === 'Pending' ? null : $this->now,
            ]);
        }
        DB::table('achievements')->insert($prestasi);

        // ─────────────────────────────────────────────────────────────────────
        // 6. KOMPETENSI / SKPI — alumni (4 kompetensi) + siswa XI–XII (2)
        // ─────────────────────────────────────────────────────────────────────
        $katalog = [
            'TKJ' => [
                ['Administrasi Server Linux', 'Sistem Operasi Jaringan', 'Instalasi DNS, Web Server, DHCP, FTP'],
                ['Routing MikroTik (MTCNA)', 'Jaringan Komputer', 'Static & dynamic routing, bandwidth management'],
                ['Instalasi Fiber Optic', 'Infrastruktur Jaringan', 'Splicing FO, pengujian OTDR & OPM'],
                ['Keamanan Jaringan & Firewall', 'Cyber Security', 'IPTables, VPN WireGuard'],
            ],
            'RPL' => [
                ['RESTful API dengan Laravel', 'Web Development', 'MVC, autentikasi JWT, Eloquent ORM'],
                ['Aplikasi Mobile Flutter', 'Mobile Development', 'State management GetX, integrasi REST API'],
                ['Basis Data MySQL', 'Database Engineering', 'Normalisasi, indexing, optimasi query'],
                ['Frontend Web Modern', 'Web Development', 'Responsive design, JavaScript async'],
            ],
            'Multimedia' => [
                ['Desain UI/UX (Figma)', 'Desain Grafis', 'Wireframe, prototipe, design system'],
                ['Video Editing (Premiere)', 'Audio-Visual', 'Multi-camera editing, audio mastering'],
                ['Motion Graphics (After Effects)', 'Animasi', 'Kinetic typography, 2D rigging'],
                ['Corporate Branding (Illustrator)', 'Desain Grafis', 'Logo vektor, brand guideline'],
            ],
        ];
        $level = ['Dasar', 'Terampil', 'Terampil', 'Mahir'];
        $peserta = [];
        foreach ($alumni as [$id, $jurusan, $angkatan]) $peserta[] = [$id, $jurusan, 4, ($angkatan - 1) . '/' . $angkatan];
        foreach ($siswa as [$id, $tkt, $jurusan]) if ($tkt !== 'X') $peserta[] = [$id, $jurusan, 2, '2025/2026'];

        $skill = [];
        foreach ($peserta as [$id, $jurusan, $jumlah, $tp]) {
            $penguji = $guruByJurusan[$jurusan];
            foreach (array_slice($katalog[$jurusan], 0, $jumlah) as $k) {
                $skill[] = $this->stamp([
                    'user_id' => $id, 'guru_id' => $penguji[mt_rand(0, count($penguji) - 1)],
                    'nama_kompetensi' => $k[0], 'kategori' => $k[1], 'level' => $level[mt_rand(0, 3)], 'keterangan' => $k[2],
                    'semester' => 'Genap', 'tahun_pelajaran' => $tp,
                ]);
            }
        }
        foreach (array_chunk($skill, 200) as $chunk) DB::table('skill_competencies')->insert($chunk);

        // ─────────────────────────────────────────────────────────────────────
        // Ringkasan
        // ─────────────────────────────────────────────────────────────────────
        $count = fn ($role) => DB::table('users')->where('role', $role)->count();
        $this->command->info('');
        $this->command->info('  SEEDER SALUT v3.0 SELESAI — total ' . DB::table('users')->count() . ' pengguna');
        $this->command->info("  Admin {$count('admin')} · Guru {$count('guru')} · Siswa {$count('siswa')} · Alumni {$count('alumni')}");
        $this->command->info('  Tracer terisi ' . count($tracer) . ' · Prestasi ' . count($prestasi) . ' · Kompetensi ' . count($skill));
        $this->command->info('  Login: Admin 0000000001/admin123 · Guru 0000000002/guru123');
        $this->command->info('         Siswa 0054321987/siswa123 · Alumni 0067890123/alumni123');
        $this->command->info('');
    }
}
