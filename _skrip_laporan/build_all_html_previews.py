# -*- coding: utf-8 -*-
"""
Script Pembangun File Preview HTML Interaktif untuk 5 Dokumen Laporan SALUT
Standar: Times New Roman 12pt, Warna Hitam Murni, Rata Kanan-Kiri, Tanpa Font Biru
Penulis: Wemvi Afrialdo
"""

import os

ROOT_DIR = r"d:\proyek_applikasi"
BASE_DIR = r"d:\proyek_applikasi\apps_sekolah"

def get_base_css(title):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            background: #F4F4F5;
            color: #000000;
            line-height: 1.5;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #FFFFFF;
            border: 1px solid #D4D4D8;
            border-radius: 4px;
            padding: 60px 70px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
        }}
        .cover-box {{
            text-align: center;
            border-bottom: 2px solid #000000;
            padding-bottom: 30px;
            margin-bottom: 35px;
        }}
        .univ-title {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            text-transform: uppercase;
            line-height: 1.3;
        }}
        .doc-title {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin: 20px 0 10px;
            line-height: 1.4;
            text-transform: uppercase;
        }}
        .doc-subtitle {{
            font-size: 12pt;
            color: #000000;
            font-style: italic;
        }}
        .author-box {{
            margin-top: 20px;
            font-size: 12pt;
            color: #000000;
        }}
        .author-box strong {{
            font-size: 12pt;
            color: #000000;
        }}
        h2 {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin: 26px 0 10px;
            text-align: justify;
        }}
        h3 {{
            font-size: 12pt;
            font-weight: bold;
            font-style: italic;
            color: #000000;
            margin: 18px 0 8px;
            text-align: justify;
        }}
        p {{
            font-size: 12pt;
            color: #000000;
            margin-bottom: 12px;
            text-align: justify;
            line-height: 1.5;
        }}
        .figure-box {{
            text-align: center;
            margin: 20px 0 24px;
            border: 1px solid #D4D4D8;
            border-radius: 4px;
            padding: 14px;
            background: #FAFAFA;
        }}
        .figure-box img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #E4E4E7;
        }}
        .figure-box.mobile img {{
            max-width: 300px;
        }}
        .caption {{
            font-size: 12pt;
            color: #000000;
            font-style: italic;
            margin-top: 8px;
            text-align: justify;
        }}
        .placeholder-box {{
            border: 2px dashed #000000;
            background: #FAFAFA;
            border-radius: 4px;
            padding: 20px;
            text-align: justify;
            margin: 16px 0 24px;
        }}
        .placeholder-box .p-title {{
            font-size: 12pt;
            font-weight: bold;
            color: #000000;
            margin-bottom: 4px;
        }}
        .placeholder-box .p-sub {{
            font-size: 12pt;
            font-style: italic;
            color: #000000;
        }}
        .summary-card {{
            border: 1px solid #000000;
            border-radius: 4px;
            padding: 18px 22px;
            margin-top: 26px;
            background: #FAFAFA;
        }}
        .summary-card h3 {{
            color: #000000;
            margin-bottom: 10px;
            font-style: normal;
        }}
        .summary-card ul {{
            padding-left: 20px;
            font-size: 12pt;
            color: #000000;
        }}
        .summary-card li {{
            margin-bottom: 6px;
            text-align: justify;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 12pt;
            margin: 20px 0 24px;
        }}
        th, td {{
            padding: 8px 10px;
            border: 1px solid #000000;
            text-align: justify;
            color: #000000;
        }}
        th {{
            background: #E5E7EB;
            color: #000000;
            font-weight: bold;
            text-align: justify;
        }}
        tr:nth-child(even) {{
            background: #FAFAFA;
        }}
        .btn-print {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #000000;
            color: #FFFFFF;
            padding: 10px 18px;
            border-radius: 4px;
            text-decoration: none;
            font-size: 12pt;
            font-family: 'Times New Roman', serif;
            font-weight: bold;
            border: none;
            cursor: pointer;
            z-index: 100;
        }}
        .btn-print:hover {{
            background: #333333;
        }}
        @media print {{
            body {{ padding: 0; background: #FFF; }}
            .container {{ box-shadow: none; border: none; padding: 0; }}
            .btn-print {{ display: none; }}
        }}
    </style>
</head>
<body>
<button class="btn-print" onclick="window.print()">🖨️ Cetak / Simpan PDF</button>
<div class="container">
"""

def get_base_footer():
    return """
    <div style="text-align: center; margin-top: 40px; padding-top: 16px; border-top: 1px solid #000000; font-size: 12pt; color: #000000;">
        Dokumen Laporan Resmi Proyek SALUT &copy; 2026 • Universitas Lampung
    </div>
</div>
</body>
</html>
"""

def generate_html_laporan_1():
    title = "Laporan Perkembangan Proyek 1 - Backend API, Database & JWT (SALUT)"
    h = get_base_css(title)
    h += """
    <div class="cover-box">
        <div class="univ-title">KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI<br>UNIVERSITAS LAMPUNG • FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>JURUSAN PENDIDIKAN MIPA • PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI</div>
        <div class="doc-title">LAPORAN PERKEMBANGAN PROYEK 1<br>PENGEMBANGAN BACKEND API, STRUKTUR DATABASE, DAN SISTEM AUTENTIKASI JWT</div>
        <div class="doc-subtitle">Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK (SALUT)</div>
        <div class="author-box">Disusun Oleh: <strong>WEMVI AFRIALDO</strong> (NPM. 2413025052)</div>
    </div>

    <h2>1. Konfigurasi Lingkungan Backend (Laravel 12 & MySQL)</h2>
    <p>Tahap awal pengembangan difokuskan pada penyiapan arsitektur server menggunakan framework PHP Laravel versi 12. Konfigurasi utama dilakukan pada file environment (.env) untuk menghubungkan backend dengan basis data relasional MySQL (db_salut). Konfigurasi ini memastikan server dapat melakukan operasi Create, Read, Update, Delete (CRUD) secara terenkripsi dan andal.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_01_env.png" alt="Konfigurasi .env Laravel">
        <div class="caption">Gambar 1.1: Konfigurasi file environment (.env) untuk koneksi database MySQL pada backend Laravel</div>
    </div>

    <h2>2. Perancangan Struktur Database (Migrations dan Models)</h2>
    <p>Untuk mengakomodasi kebutuhan tata kelola data sekolah menengah kejuruan (SMK) yang dinamis, dirancang skema database menggunakan fitur Database Migrations Laravel. Skema mencakup tabel users (multi-role: Admin, Guru, Siswa, Alumni), student_profiles, academic_records, achievements, tracer_studies, dan graduation_schedules. Seluruh tabel direpresentasikan dalam Model Eloquent dengan relasi one-to-many dan one-to-one yang kokoh.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_02_migration_model.png" alt="Migration dan Model Eloquent">
        <div class="caption">Gambar 1.2: Potongan kode migration dan model Eloquent relasional pada VS Code</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_03_phpmyadmin.png" alt="Tabel Database di phpMyAdmin">
        <div class="caption">Gambar 1.3: Tampilan visual struktur tabel basis data db_salut yang telah berhasil dimigrasi di phpMyAdmin</div>
    </div>

    <h2>3. Pembuatan RESTful API Endpoint dan Keamanan JWT</h2>
    <p>Sistem SALUT mengusung arsitektur Client-Server murni, di mana pertukaran data antara aplikasi mobile, web admin, dan server dijembatani oleh RESTful API. Untuk menjamin otorisasi yang aman tanpa state sesi (stateless), diimplementasikan JSON Web Token (JWT) menggunakan paket php-open-source-saver/jwt-auth. Rute login publik memverifikasi NISN dan kata sandi, lalu menerbitkan Bearer Token yang wajib disertakan pada setiap request menuju rute terproteksi middleware jwt.auth.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_04_routes_api.png" alt="Routing RESTful API">
        <div class="caption">Gambar 1.4: Definisi routing RESTful API dan proteksi middleware jwt.auth pada file routes/api.php</div>
    </div>

    <h2>4. Pengujian Endpoint API (API Testing 200 OK)</h2>
    <p>Sebelum diintegrasikan ke antarmuka aplikasi Flutter, seluruh endpoint API diuji secara menyeluruh menggunakan API Client. Pengujian fungsional pada endpoint otentikasi POST /api/login dengan parameter NISN dan password berhasil mengembalikan respons HTTP Status 200 OK beserta payload token JWT yang valid dan objek informasi profil pengguna.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_05_api_testing.png" alt="Pengujian API Testing 200 OK">
        <div class="caption">Gambar 1.5: Hasil pengujian API login dengan status HTTP 200 OK dan payload token JWT</div>
    </div>

    <h2>5. Manajemen Version Control dan Sinkronisasi ke GitHub</h2>
    <p>Sebagai bagian dari praktik rekayasa perangkat lunak standar industri, seluruh kode backend dan konfigurasi database didokumentasikan menggunakan version control system Git dan disinkronisasikan ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-. Hal ini menjamin integritas kode sumber dan rekam jejak perubahan proyek yang transparan.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_06_git_push_backend.png" alt="Git Push Backend Terminal">
        <div class="caption">Gambar 1.6: Eksekusi terminal PowerShell untuk perintah git commit dan git push backend</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan3_07_github_backend.png" alt="Repositori Backend di GitHub">
        <div class="caption">Gambar 1.7: Tampilan repositori Backend SALUT yang telah tersinkronisasi di website GitHub</div>
    </div>

    <div class="summary-card">
        <h3>Ringkasan Capaian Perkembangan 1</h3>
        <ul>
            <li>Infrastruktur server Laravel 12 dan MySQL terkonfigurasi penuh di port 8000.</li>
            <li>Keamanan token JWT stateless teruji 100% dengan respon 200 OK payload lengkap.</li>
            <li>Skema database multi-role (Admin, Guru, Siswa, Alumni) berhasil di-migrate.</li>
            <li>Seluruh repositori tersimpan dan terkelola aman pada branch main GitHub.</li>
        </ul>
    </div>
    """
    h += get_base_footer()
    with open(os.path.join(ROOT_DIR, "Laporan_Perkembangan_1.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Perkembangan_1.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Perkembangan_1.html")

def generate_html_laporan_2():
    title = "Laporan Perkembangan Proyek 2 - Frontend Mobile Flutter & Dynamic UI (SALUT)"
    h = get_base_css(title)
    h += """
    <div class="cover-box">
        <div class="univ-title">KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI<br>UNIVERSITAS LAMPUNG • FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>JURUSAN PENDIDIKAN MIPA • PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI</div>
        <div class="doc-title">LAPORAN PERKEMBANGAN PROYEK 2<br>PENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API BERBASIS TOKEN JWT</div>
        <div class="doc-subtitle">Implementasi Dynamic UI Rendering Multi-Role Siswa Aktif dan Alumni SMK</div>
        <div class="author-box">Disusun Oleh: <strong>WEMVI AFRIALDO</strong> (NPM. 2413025052)</div>
    </div>

    <h2>1. Perancangan Antarmuka Pengguna Mobile (Flutter)</h2>
    <p>Tahap perkembangan kedua berfokus pada pembangunan antarmuka mobile menggunakan framework Flutter. Desain antarmuka dirancang responsif dengan mengadopsi estetika clean academic modern. Komponen utama meliputi halaman autentikasi (login_page.dart) dengan validasi form nomor induk siswa (NISN) dan kata sandi, serta dasbor utama (dashboard_page.dart) dengan kartu ringkasan informasi akademik dan menu aksi cepat.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan4_01_login_page_code.png" alt="Kode login_page.dart">
        <div class="caption">Gambar 2.1: Potongan kode antarmuka halaman login pada file login_page.dart</div>
    </div>

    <h2>2. Integrasi HTTP Client Dio dan Pengelolaan Token JWT</h2>
    <p>Aplikasi Flutter dihubungkan dengan Backend API Laravel melalui kelas ApiService yang memanfaatkan pustaka Dio HTTP Client. Diterapkan mekanisme Interceptor yang secara otomatis membaca token JWT dari media penyimpanan aman perangkat (flutter_secure_storage) dan menyematkannya pada header Authorization di setiap permintaan data ke server. Interceptor juga mendeteksi status 401 Unauthorized guna mengarahkan pengguna kembali ke halaman Login saat sesi berakhir.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan4_02_api_service_code.png" alt="Implementasi ApiService Dio">
        <div class="caption">Gambar 2.2: Implementasi HTTP Client Dio dan Interceptor token JWT pada api_service.dart</div>
    </div>

    <h2>3. Pengujian dan Simulasi Antarmuka pada Perangkat</h2>
    <p>Aplikasi mobile dikompilasi dan dijalankan pada emulator Android serta perangkat fisik HP Samsung. Pengujian memvalidasi dua skenario login peran: akun Siswa Aktif (Budi Santoso) dan akun Alumni (Siti Rahayu).</p>
    
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan4_03_login_mobile_app.png" alt="Tampilan Antarmuka Login">
        <div class="caption">Gambar 2.3: Tampilan antarmuka Login aplikasi SALUT pada perangkat mobile</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: HALAMAN LOGIN MOBILE]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP saat berada di halaman Login SALUT. Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan4_04_dashboard_siswa_app.png" alt="Dashboard Siswa Aktif">
        <div class="caption">Gambar 2.5: Tampilan antarmuka Dashboard untuk peran Siswa Aktif</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: DASHBOARD SISWA AKTIF]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP saat login sebagai Siswa Aktif (Budi Santoso). Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan4_05_dashboard_alumni_app.png" alt="Dashboard Alumni">
        <div class="caption">Gambar 2.7: Tampilan antarmuka Dashboard untuk peran Alumni</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: DASHBOARD ALUMNI]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP saat login sebagai Alumni (Siti Rahayu). Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <h2>4. Penerapan Logika Dynamic UI Rendering Berbasis Peran</h2>
    <p>Menggunakan reactive state management GetX, antarmuka aplikasi SALUT dapat bertransformasi secara dinamis menyesuaikan data peran (role) yang diperoleh dari payload token JWT. Jika pengguna berstatus 'Siswa Aktif', menu yang ditampilkan berfokus pada pemantauan nilai rapor dan pengajuan prestasi; sebaliknya jika berstatus 'Alumni', tampilan otomatis berubah menyajikan menu arsip dokumen ijazah sah dan kuesioner tracer study.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan4_06_role_logic_code.png" alt="Logika Dynamic UI GetX">
        <div class="caption">Gambar 2.9: Potongan kode logika pengkondisian tampilan menu per-role pada dashboard_page.dart</div>
    </div>

    <h2>5. Sinkronisasi Kode Frontend ke Repositori GitHub</h2>
    <p>Seluruh pembaruan antarmuka mobile Flutter, GetX controller, model data, dan service disinkronisasikan ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan4_07_git_push_frontend.png" alt="Git Push Frontend Terminal">
        <div class="caption">Gambar 2.10: Terminal eksekusi git push kode frontend Flutter pada PowerShell</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan4_08_github_frontend.png" alt="Repositori Frontend di GitHub">
        <div class="caption">Gambar 2.11: Tampilan repositori direktori Flutter apps_sekolah di GitHub</div>
    </div>

    <div class="summary-card">
        <h3>Ringkasan Capaian Perkembangan 2</h3>
        <ul>
            <li>UI Mobile responsif & elegan berhasil diimplementasikan dengan Flutter GetX.</li>
            <li>Integrasi Dio HTTP Client dan interceptor Bearer Token JWT berjalan lancar.</li>
            <li>Dynamic UI Rendering Siswa Aktif vs Alumni terbukti bekerja secara adaptif.</li>
            <li>Source code frontend tersinkronisasi rapi pada repositori resmi GitHub.</li>
        </ul>
    </div>
    """
    h += get_base_footer()
    with open(os.path.join(ROOT_DIR, "Laporan_Perkembangan_2.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Perkembangan_2.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Perkembangan_2.html")

def generate_html_laporan_3():
    title = "Laporan Perkembangan Proyek 3 - Fitur Kejuruan SMK SKPI & Arsip (SALUT)"
    h = get_base_css(title)
    h += """
    <div class="cover-box">
        <div class="univ-title">KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI<br>UNIVERSITAS LAMPUNG • FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>JURUSAN PENDIDIKAN MIPA • PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI</div>
        <div class="doc-title">LAPORAN PERKEMBANGAN PROYEK 3<br>PENGEMBANGAN FITUR EKOSISTEM KEJURUAN SMK (PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)</div>
        <div class="doc-subtitle">Pencatatan Kompetensi Keahlian Siswa dan Validasi Kelulusan Digital Terverifikasi</div>
        <div class="author-box">Disusun Oleh: <strong>WEMVI AFRIALDO</strong> (NPM. 2413025052)</div>
    </div>

    <h2>1. Perancangan Skema Database Portofolio Keahlian (SKPI)</h2>
    <p>Untuk memenuhi kebutuhan spesifik Sekolah Menengah Kejuruan (SMK), nilai akademik ijazah perlu dilengkapi dengan Surat Keterangan Pendamping Ijazah (SKPI) yang memuat unit kompetensi keahlian standar SKKNI dan BNSP. Dirancang migration tabel baru skill_competencies yang memuat data user_id, competence_code, competence_name, competency_level (Dasar, Terampil, Mahir), score asesmen, dan verified_by (asesor).</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan5_01_migration_skpi.png" alt="Migration SKPI">
        <div class="caption">Gambar 3.1: Kode migration Laravel untuk pembuatan tabel skill_competencies (SKPI)</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan5_02_phpmyadmin_skpi.png" alt="Tabel SKPI di phpMyAdmin">
        <div class="caption">Gambar 3.2: Tampilan record data 136 unit kompetensi keahlian siswa pada phpMyAdmin</div>
    </div>

    <h2>2. Implementasi Endpoint API Portofolio Keahlian</h2>
    <p>Pada sisi backend dibangun SkillController.php dengan endpoint utama GET /api/skills/my. Endpoint ini menyajikan daftar seluruh unit kompetensi kejuruan yang telah diselesaikan oleh siswa terautentikasi sesuai bidang jurusannya (RPL, TKJ, atau Multimedia). Pengujian endpoint menunjukkan respons 200 OK dengan payload data kompetensi yang lengkap.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan5_03_skill_controller.png" alt="SkillController Laravel">
        <div class="caption">Gambar 3.3: Implementasi SkillController.php pada backend Laravel</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan5_04_api_skills_test.png" alt="Uji Endpoint Skills API">
        <div class="caption">Gambar 3.4: Hasil pengujian endpoint GET /api/skills/my dengan respons 200 OK</div>
    </div>

    <h2>3. Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)</h2>
    <p>Pada aplikasi Flutter, dibangun antarmuka skills_page.dart yang menyajikan kartu-kartu capaian unit kompetensi keahlian. Setiap kartu memuat rincian kode unit, predikat kemahiran dengan badge warna informatif (Mahir hijau, Terampil oranye), skor capaian, dan nama asesor penguji, serta dilengkapi tombol aksi untuk mengunduh berkas SKPI resmi.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan5_05_skills_page_code.png" alt="Kode skills_page.dart">
        <div class="caption">Gambar 3.5: Kode antarmuka reactive GetX pada file skills_page.dart</div>
    </div>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan5_06_skills_mobile_app.png" alt="Tampilan SKPI Mobile">
        <div class="caption">Gambar 3.6: Tampilan antarmuka Portofolio Keahlian (SKPI) pada mobile app</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: PORTOFOLIO KEAHLIAN SKPI]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP pada menu Portofolio Keahlian SKPI. Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <h2>4. Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)</h2>
    <p>Untuk mencegah kerusakan atau kehilangan ijazah fisik serta mempermudah legalisir digital bagi alumni, dibangun modul arsip_page.dart. Alumni dapat melihat dan mengunduh berkas digital (Ijazah Asli, SKL, dan Transkrip Nilai) yang telah dibubuhi QR-Code verifikasi resmi dan Tanda Tangan Elektronik.</p>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan5_07_arsip_mobile_app.png" alt="Modul Arsip Digital">
        <div class="caption">Gambar 3.8: Tampilan modul Arsip Digital Kelulusan dengan opsi unduh PDF pada mobile</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: ARSIP DIGITAL KELULUSAN]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP pada menu Arsip Dokumen Digital Ijazah. Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <h2>5. Sinkronisasi Repositori Fitur SKPI ke GitHub</h2>
    <p>Seluruh controller, migration kejuruan SMK, dan modul antarmuka Flutter disinkronisasikan ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan5_08_git_push.png" alt="Git Push SKPI Terminal">
        <div class="caption">Gambar 3.10: Terminal eksekusi git push pembaruan fitur SKPI dan arsip digital</div>
    </div>

    <div class="summary-card">
        <h3>Ringkasan Capaian Perkembangan 3</h3>
        <ul>
            <li>Tabel skill_competencies dan SKPI berhasil merekam kompetensi siswa per jurusan SMK.</li>
            <li>API /api/skills/my menyajikan data kompetensi dan asesor penguji berlisensi BNSP.</li>
            <li>Ijazah dan SKL digital tersimpan aman dalam format PDF terenkripsi ber-TTE.</li>
            <li>Pembaruan kode sumber terdokumentasi rapi pada commit Git terbaru.</li>
        </ul>
    </div>
    """
    h += get_base_footer()
    with open(os.path.join(ROOT_DIR, "Laporan_Perkembangan_3.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Perkembangan_3.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Perkembangan_3.html")

def generate_html_laporan_4():
    title = "Laporan Perkembangan Proyek 4 - Push Notifikasi, Otomasi Cron & Tracer Study (SALUT)"
    h = get_base_css(title)
    h += """
    <div class="cover-box">
        <div class="univ-title">KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI<br>UNIVERSITAS LAMPUNG • FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>JURUSAN PENDIDIKAN MIPA • PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI</div>
        <div class="doc-title">LAPORAN PERKEMBANGAN PROYEK 4<br>INTEGRASI PUSH NOTIFICATION, OTOMASI CRON JOB TRANSISI KELULUSAN, MODUL KEAMANAN, TRACER STUDY & RILIS FINAL</div>
        <div class="doc-subtitle">Otomatisasi Sistem Akademik dan Monitoring Penyerapan Lulusan SMK</div>
        <div class="author-box">Disusun Oleh: <strong>WEMVI AFRIALDO</strong> (NPM. 2413025052)</div>
    </div>

    <h2>1. Integrasi Push Notification Firebase Cloud Messaging (FCM)</h2>
    <p>Untuk memastikan pengumuman kelulusan dan agenda tracer study diterima seketika oleh pengguna, diintegrasikan layanan Firebase Cloud Messaging (FCM). File fcm_service.dart menangani pendaftaran token perangkat, penerimaan notifikasi saat aplikasi dibuka (foreground), dan penanganan pesan di latar belakang (background handler).</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan6_01_fcm_service_code.png" alt="Implementasi FcmService.dart">
        <div class="caption">Gambar 4.1: Kode implementasi FcmService.dart menggunakan GetX service</div>
    </div>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan6_02_fcm_notification_app.png" alt="Banner Notifikasi Mobile">
        <div class="caption">Gambar 4.2: Tampilan banner Push Notification resmi kelulusan pada mobile app</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: BANNER PUSH NOTIFICATION]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP saat banner Push Notification muncul di bagian atas layar. Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <h2>2. Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)</h2>
    <p>Untuk meniadakan proses manual pemindahan status siswa, dibangun custom Artisan command: salut:promote-alumni. Perintah ini dijadwalkan secara berkala (cron job) setiap hari jam 00:00. Sistem secara otomatis memeriksa tanggal kelulusan, mengubah role 190 siswa aktif menjadi alumni, dan memicu pengiriman notifikasi FCM ke perangkat pengguna.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan6_03_cron_promote_code.png" alt="Logika PromoteAlumni.php">
        <div class="caption">Gambar 4.4: Kode logika otomasi command PromoteAlumni.php pada Laravel Console</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan6_04_cron_execution_terminal.png" alt="Log Terminal Cron Job">
        <div class="caption">Gambar 4.5: Log terminal eksekusi otomatis cron job salut:promote-alumni</div>
    </div>

    <h2>3. Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile</h2>
    <p>Sesuai prinsip keamanan data pengguna, dibangun halaman change_password_page.dart. Pengguna dapat memperbarui kata sandi dengan validasi pencocokan kata sandi baru dan enkripsi bcrypt melalui endpoint terproteksi PATCH /api/profile/password.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan6_05_change_password_code.png" alt="Kode change_password_page.dart">
        <div class="caption">Gambar 4.6: Potongan kode antarmuka dan validasi form pada change_password_page.dart</div>
    </div>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan6_06_change_password_app.png" alt="Halaman Ubah Kata Sandi">
        <div class="caption">Gambar 4.7: Tampilan antarmuka Ubah Kata Sandi pada perangkat mobile</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: HALAMAN UBAH KATA SANDI]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP pada halaman Ubah Kata Sandi akun. Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <h2>4. Implementasi Kuesioner Tracer Study Alumni</h2>
    <p>Aplikasi mobile menyediakan kuesioner dinamis untuk melacak keterserapan alumni (Bekerja, Melanjutkan Kuliah, Wirausaha). Data yang dikumpulkan mencakup nama perusahaan/kampus, sektor industri, rentang penghasilan pertama, dan tingkat keselarasan kurikulum.</p>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan6_07_tracer_study_app.png" alt="Formulir Tracer Study">
        <div class="caption">Gambar 4.9: Tampilan pengisian kuesioner Tracer Study pada perangkat mobile</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: KUESIONER TRACER STUDY]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP pada formulir kuesioner Tracer Study Alumni. Anda dapat menempelkan hasil tangkapan layar langsung ke dalam kotak ini.</div>
    </div>

    <h2>5. Analitik Ekosistem Kejuruan SMK pada Web Admin</h2>
    <p>Data hasil tracer study dan capaian keahlian diolah secara visual pada dashboard Web Admin (dashboard.html). Pihak manajemen sekolah dapat memantau distribusi keterserapan lulusan (65% bekerja di DUDI, 25% kuliah, 10% wirausaha/lainnya), serta leaderboard 5 mitra industri dan kampus penyerap lulusan terbanyak.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan6_08_webadmin_smk_analytics.png" alt="Dasbor Analitik SMK Web Admin">
        <div class="caption">Gambar 4.11: Tampilan dasbor analitik keterserapan alumni SMK pada Web Admin panel</div>
    </div>

    <h2>6. Rilis Final dan Tagging Repositori GitHub</h2>
    <p>Setelah seluruh pengujian integrasi akhir selesai dengan hasil 0 error, proyek dirilis secara resmi dengan tag v1.0.0-smk-release pada repositori GitHub WEMVIAFRIALDO/apps_Sekolah-.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/laporan6_09_git_push_final.png" alt="Tagging Rilis Final GitHub">
        <div class="caption">Gambar 4.12: Terminal eksekusi rilis final dengan tagging v1.0.0-smk-release ke GitHub</div>
    </div>

    <div class="summary-card">
        <h3>Ringkasan Capaian Perkembangan 4</h3>
        <ul>
            <li>Push Notification FCM aktif mentransmisikan notifikasi kelulusan ke HP siswa.</li>
            <li>Cron job otomatis mengubah status siswa aktif menjadi alumni secara terjadwal.</li>
            <li>Tracer study interaktif memetakan penyerapan alumni di DUDI dan perguruan tinggi.</li>
            <li>Rilis v1.0.0-smk-release terbit resmi pada repositori GitHub.</li>
        </ul>
    </div>
    """
    h += get_base_footer()
    with open(os.path.join(ROOT_DIR, "Laporan_Perkembangan_4.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Perkembangan_4.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Perkembangan_4.html")

def generate_html_laporan_akhir():
    title = "Laporan Akhir Lengkap Proyek SALUT - Gabungan, Timeline & Prototype 4 Role"
    h = get_base_css(title)
    h += """
    <div class="cover-box">
        <div class="univ-title">KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI<br>UNIVERSITAS LAMPUNG • FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN<br>JURUSAN PENDIDIKAN MIPA • PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI</div>
        <div class="doc-title">LAPORAN AKHIR PROYEK PERANGKAT LUNAK<br>RANCANG BANGUN SISTEM INFORMASI ARSIP KELULUSAN DAN TRACER STUDY ALUMNI SMK (SALUT) BERBASIS MOBILE FLUTTER DAN WEB LARAVEL</div>
        <div class="doc-subtitle">Dokumen Komprehensif Perancangan, Instalasi, Perkembangan, Timeline, dan Prototype Akhir Sistem Multi-Role</div>
        <div class="author-box">Disusun Oleh: <strong>WEMVI AFRIALDO</strong> (NPM. 2413025052)</div>
    </div>

    <h2>KATA PENGANTAR</h2>
    <p>Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan hidayah-Nya sehingga Laporan Akhir Pengembangan Proyek Perangkat Lunak 'SALUT' (Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK) ini dapat diselesaikan dengan baik. Laporan ini merupakan rangkuman utuh dari seluruh tahapan siklus hidup pengembangan perangkat lunak (SDLC), mencakup perancangan spesifikasi kebutuhan (SRS & Mockup), instalasi dan konfigurasi lingkungan pengembangan, perkembangan arsitektur backend dan database, antarmuka mobile Flutter, integrasi portofolio kejuruan SMK (SKPI), otomasi transisi kelulusan, jadwal linimasa proyek, serta pengujian prototype akhir pada seluruh aktor sistem.</p>

    <h2>BAB I: RINGKASAN DESAIN DAN MOCKUP SISTEM (LAPORAN 1)</h2>
    <p>Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK (SALUT) dirancang untuk memecahkan problematika pengelolaan dokumen kelulusan yang masih terfragmentasi, risiko kerusakan fisik arsip ijazah, serta kesulitan pelacakan keterserapan lulusan ke dunia kerja dan perguruan tinggi. Sistem ini dibangun dengan arsitektur Client-Server yang melayani siklus hidup data siswa sejak awal masuk jenjang SMK hingga menjadi alumni.</p>
    <div class="figure-box mobile">
        <img src="srs_mockup_images/image12.png" alt="Mockup Mobile Android SALUT">
        <div class="caption">Gambar 1.1: Desain Mockup Antarmuka Mobile Android - Halaman Manajemen dan Akses Data Pengguna</div>
    </div>
    <div class="figure-box">
        <img src="srs_mockup_images/image14.png" alt="Mockup Desktop Web Admin SALUT">
        <div class="caption">Gambar 1.2: Desain Mockup Antarmuka Desktop Web Admin - Panel Manajemen Civitas Akademika</div>
    </div>

    <h2>BAB II: INSTALASI DAN KONFIGURASI LINGKUNGAN PENGEMBANGAN (LAPORAN 2)</h2>
    <p>Lingkungan pengembangan disiapkan secara komprehensif mencakup instalasi Flutter SDK stabil, pendaftaran Environment Variables PATH, pemasangan Java Development Kit 21 (JDK 21 LTS), Android SDK Command-line Tools & CMake, ekstensi Flutter/Dart pada Visual Studio Code, serta verifikasi kelayakan melalui perintah flutter doctor.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/instalasi/step03_environment_variables.png" alt="Konfigurasi PATH">
        <div class="caption">Gambar 2.1: Konfigurasi System Environment Variables PATH pada Windows</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/instalasi/step11_flutter_doctor_output.png" alt="Hasil Flutter Doctor">
        <div class="caption">Gambar 2.2: Hasil diagnosa perintah flutter doctor dengan status seluruh komponen centang hijau</div>
    </div>

    <h2>BAB III - VI: RINGKASAN PERKEMBANGAN PROYEK 1 HINGGA 4</h2>
    <p><strong>Perkembangan 1:</strong> Membangun backend Laravel 12, konfigurasi database MySQL, Model Eloquent, dan endpoint RESTful API terproteksi JWT.<br>
    <strong>Perkembangan 2:</strong> Mengembangkan antarmuka mobile Flutter dengan HTTP Client Dio dan logika Dynamic UI Rendering GetX.<br>
    <strong>Perkembangan 3:</strong> Menyesuaikan sistem dengan ekosistem kejuruan SMK melalui modul Portofolio Keahlian (SKPI) dan arsip ijazah digital ber-TTE.<br>
    <strong>Perkembangan 4:</strong> Mengintegrasikan Push Notification Firebase Cloud Messaging, scheduled cron job kelulusan, dan modul tracer study.</p>

    <h2>BAB VII: TABEL TIMELINE PELAKSANAAN DAN PERKEMBANGAN PROYEK</h2>
    <p>Matriks timeline berikut menggambarkan perjalanan implementasi proyek dari tahap inisiasi hingga kompilasi rilis standalone APK:</p>
    <table>
        <thead>
            <tr>
                <th>Fase Perkembangan</th>
                <th>Rentang Waktu</th>
                <th>Deskripsi Aktivitas</th>
                <th>Luaran (Deliverables)</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Fase 1: Inisiasi & Desain</strong></td>
                <td>28 - 29 Sep 2026</td>
                <td>Penyusunan dokumen SRS SALUT, perancangan arsitektur sistem, dan perancangan mockup UI/UX mobile dan desktop.</td>
                <td>Dokumen SRS & Mockup Desain (Laporan 1)</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 2: Instalasi Lingkungan</strong></td>
                <td>30 Sep 2026</td>
                <td>Instalasi Flutter SDK, Dart, Android Studio, SDK Command-line Tools, JDK 21, VS Code, dan verifikasi flutter doctor.</td>
                <td>Lingkungan Dev Siap (Laporan 2)</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 3: Perkembangan 1</strong></td>
                <td>1 - 2 Okt 2026</td>
                <td>Setup Laravel 12, konfigurasi .env, migration database, model Eloquent, autentikasi JWT, API testing 200 OK, dan git push.</td>
                <td>Backend REST API & DB (Laporan 3)</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 4: Perkembangan 2</strong></td>
                <td>3 - 5 Okt 2026</td>
                <td>Implementasi Flutter UI login & dashboard, integrasi Dio interceptor JWT, Dynamic UI Rendering Siswa vs Alumni, dan git push.</td>
                <td>Aplikasi Mobile Flutter (Laporan 4)</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 5: Perkembangan 3</strong></td>
                <td>12 - 13 Okt 2026</td>
                <td>Migration tabel skill_competencies, SkillController, antarmuka skills_page.dart (SKPI), arsip digital ber-TTE, dan seeder data.</td>
                <td>Modul Portofolio SKPI (Laporan 5)</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 6: Perkembangan 4</strong></td>
                <td>14 - 15 Okt 2026</td>
                <td>Integrasi Firebase FCM, scheduled cron job salut:promote-alumni, tracer study dinamis, dashboard chart analitik, dan tag v1.0.0.</td>
                <td>Otomasi & Tracer (Laporan 6)</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 7: Desain Apple-Style</strong></td>
                <td>15 - 17 Okt 2026</td>
                <td>Redesign UI ke konsep Apple-Style Clean Academic, pembuatan splash screen 3 detik, logo resmi baru, perbaikan modal arsip dan grafik.</td>
                <td>UI Modern Apple-Style</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
            <tr>
                <td><strong>Fase 8: Approval & Release APK</strong></td>
                <td>18 Okt 2026</td>
                <td>Dialog konfirmasi pop-up prestasi berpendar, pull-to-refresh real-time approval admin ke siswa, build standalone APK release, dan install ke Samsung A25.</td>
                <td>Release Standalone APK</td>
                <td><strong>Selesai (100%)</strong></td>
            </tr>
        </tbody>
    </table>

    <h2>BAB VIII: PROTOTYPE AKHIR APLIKASI SISTEM SALUT LENGKAP 4 ROLE</h2>

    <h3>8.1 Prototype Peran Administrator (Web Admin Panel)</h3>
    <p>Menyajikan dasbor analitik kejuruan SMK, master data siswa & kelas, kelola arsip digital ijazah, penjadwalan kelulusan otomatis, dan tracer study.</p>
    <div class="figure-box">
        <img src="laporan_screenshots/proto_admin_students.png" alt="Web Admin Siswa">
        <div class="caption">Gambar 8.1: Antarmuka Master Data Siswa & Alumni pada Web Admin Administrator</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/proto_admin_arsip.png" alt="Web Admin Arsip">
        <div class="caption">Gambar 8.2: Antarmuka Pengelolaan Arsip Digital Ijazah & SKL pada Web Admin Administrator</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/proto_admin_schedules.png" alt="Web Admin Jadwal">
        <div class="caption">Gambar 8.3: Antarmuka Penjadwalan Rilis Kelulusan Otomatis pada Web Admin Administrator</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/proto_admin_tracer.png" alt="Web Admin Tracer">
        <div class="caption">Gambar 8.4: Antarmuka Rekapitulasi & Grafik Tracer Study pada Web Admin Administrator</div>
    </div>

    <h3>8.2 Prototype Peran Guru (Web Admin Panel)</h3>
    <p>Menyajikan modul penginputan nilai rapor siswa per semester dan validasi portofolio keahlian siswa (SKPI).</p>
    <div class="figure-box">
        <img src="laporan_screenshots/proto_guru_rapor.png" alt="Web Admin Rapor">
        <div class="caption">Gambar 8.5: Antarmuka Penginputan Nilai Rapor Siswa pada Web Admin Guru</div>
    </div>
    <div class="figure-box">
        <img src="laporan_screenshots/proto_guru_skills.png" alt="Web Admin SKPI Guru">
        <div class="caption">Gambar 8.6: Antarmuka Validasi Portofolio Keahlian (SKPI) pada Web Admin Guru</div>
    </div>

    <h3>8.3 Prototype Peran Siswa Aktif (Mobile Flutter App)</h3>
    <p>Menyajikan form login multi-role, dashboard siswa aktif, pengajuan prestasi dengan pop-up modal dialog, dan portofolio keahlian siswa.</p>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan4_04_dashboard_siswa_app.png" alt="Dashboard Siswa">
        <div class="caption">Gambar 8.7: Antarmuka Dashboard Siswa Aktif pada Mobile App</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: DASHBOARD SISWA AKTIF]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP Samsung saat berada di beranda Siswa Aktif.</div>
    </div>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/proto_siswa_prestasi.png" alt="Prestasi Pop-Up">
        <div class="caption">Gambar 8.8: Antarmuka Pengajuan Prestasi & Modal Pop-Up Dialog Sukses</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: PENGAJUAN PRESTASI SISWA]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP Samsung saat dialog konfirmasi prestasi muncul.</div>
    </div>

    <h3>8.4 Prototype Peran Alumni (Mobile Flutter App)</h3>
    <p>Menyajikan dashboard alumni, akses unduh arsip ijazah & SKL terverifikasi, form kuesioner tracer study, dan keamanan akun ganti kata sandi.</p>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan4_05_dashboard_alumni_app.png" alt="Dashboard Alumni">
        <div class="caption">Gambar 8.9: Antarmuka Dashboard Alumni pada Mobile App</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: DASHBOARD ALUMNI]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP Samsung saat login sebagai Alumni.</div>
    </div>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan5_07_arsip_mobile_app.png" alt="Arsip Digital Alumni">
        <div class="caption">Gambar 8.10: Antarmuka Arsip Dokumen Digital Kelulusan Alumni</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: ARSIP DIGITAL ALUMNI]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP Samsung pada daftar berkas arsip ijazah.</div>
    </div>
    <div class="figure-box mobile">
        <img src="laporan_screenshots/laporan6_07_tracer_study_app.png" alt="Tracer Study Alumni">
        <div class="caption">Gambar 8.11: Antarmuka Formulir Kuesioner Tracer Study Alumni</div>
    </div>
    <div class="placeholder-box">
        <div class="p-title">📱 [AREA TEMPEL SCREENSHOT HP RESMI: FORMULIR TRACER STUDY]</div>
        <div class="p-sub">Ambil tangkapan layar langsung dari HP Samsung pada formulir kuesioner tracer study.</div>
    </div>

    <h2>BAB IX: KESIMPULAN DAN REKOMENDASI PENGEMBANGAN</h2>
    <p>Sistem SALUT berhasil diwujudkan sebagai solusi terintegrasi antara backend Laravel 12, web admin analitik, dan aplikasi mobile Flutter. Konsep Dynamic UI Rendering, pencatatan kompetensi SKPI SMK, serta otomasi transisi kelulusan berbasis cron job dan FCM berjalan secara handal. Aplikasi telah teruji 100% pada perangkat fisik HP Samsung Galaxy A25 5G sebagai standalone release APK.</p>
    """
    h += get_base_footer()
    with open(os.path.join(ROOT_DIR, "Laporan_Akhir_Lengkap.html"), "w", encoding="utf-8") as f:
        f.write(h)
    with open(os.path.join(BASE_DIR, "Laporan_Akhir_Lengkap.html"), "w", encoding="utf-8") as f:
        f.write(h)
    print("Selesai Laporan_Akhir_Lengkap.html")

if __name__ == "__main__":
    generate_html_laporan_1()
    generate_html_laporan_2()
    generate_html_laporan_3()
    generate_html_laporan_4()
    generate_html_laporan_akhir()
    print("Semua file HTML preview selesai dibangun dengan format standar!")
