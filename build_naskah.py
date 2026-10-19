# -*- coding: utf-8 -*-
"""
Script Generator Dokumen Naskah Video Presentasi LMS Moodle 4.5+ LTS
Standar Akademik: Times New Roman 12 pt, Rata Kanan Kiri (Justified), Tanpa Garis Paragraf.
Penulis: Wemvi Afrialdo (NPM: 2413025052)
Universitas Lampung
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

MD_OUTPUT_PATH = r"c:\kuliah\WEMVI\Semester 5\Learning Management Sytem\Modul Ajar\NASKAH_VIDEO_PRESENTASI_LMS.md"
DOCX_OUTPUT_PATH = r"c:\kuliah\WEMVI\Semester 5\Learning Management Sytem\Modul Ajar\NASKAH_VIDEO_PRESENTASI_LMS.docx"

# ==========================================
# 1. KONTEN LENGKAP MARKDOWN (UTF-8)
# ==========================================
MARKDOWN_CONTENT = """# NASKAH & SKRIP REKAMAN VIDEO PRESENTASI
## PENGEMBANGAN LEARNING MANAGEMENT SYSTEM (LMS) BERBASIS MOODLE 4.5+ LTS
### MATA PELAJARAN INFORMATIKA KELAS X (FASE E) – KURIKULUM MERDEKA

---

### INFORMASI PRODUKSI VIDEO
- **Presenter / Pembicara:** Wemvi Afrialdo
- **NPM:** 2413025052
- **Program Studi:** Pendidikan Teknologi Informasi (PTI)
- **Jurusan / Fakultas:** Pendidikan MIPA / FKIP Universitas Lampung
- **Mata Kuliah:** Learning Management System (LMS)
- **Dosen Pengampu:** Ibu Ghea Chandra Surawan, M.Pd.
- **Platform E-Learning:** Moodle 4.5.13+ LTS (Long Term Support, Build: 20260911)
- **Lingkungan Hosting:** On-Premise / Localhost XAMPP (Apache 2.4, PHP 8.2, MariaDB 10.4)
- **Sasaran Pengguna:** Peserta Didik Sekolah Menengah Kejuruan (SMK) Kelas X (Fase E)
- **Target Durasi Video:** 12 – 15 Menit

---

### PANDUAN PRAKTIK PEMBUKTIAN VISUAL (DEMO REAL-TIME DI LAYAR)
Agar presentasi tidak terkesan hanya berbicara teori (*tidak hanya sekadar ngomong saja*), presenter wajib memperlihatkan bukti teknis operasional secara langsung di layar monitor melalui urutan aksi berikut:

1. **Pembuktian Visual Server XAMPP:**
   - Buka dan tampilkan jendela **XAMPP Control Panel v3.3.0** di layar.
   - Sorot dengan kursor mouse bahwa modul **Apache** berstatus aktif (PID terisi, Port 80, 443 berlatar hijau terang).
   - Sorot modul **MySQL / MariaDB** berstatus aktif (PID terisi, Port 3306 berlatar hijau terang).
   - Klik tombol **Explorer** pada panel XAMPP untuk membuka jendela direktori Windows.

2. **Pembuktian Visual Struktur Direktori & Keamanan Dataroot:**
   - Tunjukkan folder instalasi Moodle di `C:\\xampp\\htdocs\\moodle` sebagai root aplikasi publik.
   - Tunjukkan folder penyimpanan dokumen siswa di `C:\\xampp\\moodledata` yang terisolasi di luar folder `htdocs`.
   - Jelaskan bahwa pemisahan fisik ini adalah bukti kepatuhan keamanan data tingkat tinggi (*security hardening*) agar dokumen rahasia rapor/tugas siswa tidak dapat diakses langsung melalui URL browser.

3. **Pembuktian Visual Versi Rilis Moodle 4.5.13+ LTS:**
   - Di antarmuka Moodle Administrator, buka menu: **Administrasi Situs > Pemberitahuan (Notifications)** pada URL `http://localhost/moodle/admin/index.php`.
   - Arahkan kamera/kursor ke bagian bawah halaman yang memuat label rilis resmi: **Moodle 4.5.13+ (Build: 20260911)**.
   - Buka menu: **Administrasi Situs > Server > Lingkungan (Environment)** pada URL `http://localhost/moodle/admin/environment.php` untuk memperlihatkan tabel versi PHP 8.2.x dan komponen server berstatus centang **OK (Hijau)**.

4. **Pembuktian Visual Laporan Audit Keamanan (Security Overview):**
   - Buka menu: **Administrasi Situs > Laporan > Pemeriksaan Keamanan** (`http://localhost/moodle/report/security/index.php`).
   - Gulir (*scroll*) perlahan memperlihatkan seluruh parameter berstatus **HIJAU / OK** (termasuk `display_errors = Off` dan proteksi berkas privat).

---

### SPESIFIKASI TEKNIS & LINGKUNGAN SISTEM MOODLE
Sistem E-Learning ini dibangun menggunakan konfigurasi perangkat lunak standar industri pendidikan untuk menjamin performa, keamanan, dan keandalan data pembelajaran:

| Komponen Sistem | Spesifikasi / Konfigurasi | Keterangan Fungsional & Pembuktian Layar |
|---|---|---|
| **Moodle Core Engine** | Moodle 4.5.13+ (Build: 20260911) | Rilis **LTS (Long-Term Support)**. Dibuktikan langsung via menu Notifications & Environment Admin. |
| **Web Server** | Apache 2.4.58 (XAMPP v3.3.0) | Menangani koneksi HTTP lokal. Dibuktikan via XAMPP Control Panel (Port 80, 443 aktif hijau). |
| **PHP Runtime** | PHP 8.2.12 | Kompatibel penuh dengan Moodle 4.5; `memory_limit = 512M`, `display_errors = Off`. |
| **Database Server** | MariaDB 10.4.32 | Engine InnoDB, Collation `utf8mb4_general_ci`. Dibuktikan via port 3306 XAMPP aktif hijau. |
| **Dataroot Storage** | `C:\\xampp\\moodledata` | Terisolasi di luar `htdocs`. Dibuktikan via File Explorer untuk memastikan proteksi berkas. |
| **UI / Theme Framework** | Boost Theme + Custom SCSS Vokasi | Dilengkapi *Hero Banner SMK*, *Hover Lift Card Effect*, *Dynamic Progress Bar*, dan *Grid*. |

---

### RASIONALISASI: MENGAPA MEMILIH MOODLE 4.5+ LTS UNTUK INFORMATIKA SMK FASE E?
Pemilihan platform Moodle versi 4.5+ LTS didasarkan pada pertimbangan pedagogis, teknis, dan strategis vokasi yang matang, bukan sekadar alternatif repositori berkas sederhana:

1. **Keselarasan Pedagogis dengan Paradigma Kurikulum Merdeka (Konstruktivisme Sosial):**
   Platform pembelajaran vokasi tidak boleh hanya berfungsi sebagai "gudang file statis" (*file dump*) seperti Google Classroom biasa. Moodle dibangun di atas filosofi konstruktivisme sosial di mana pengetahuan dibangun melalui interaksi aktif: eksplorasi materi mandiri ber-multimedia, dialektika nalar kritis di forum diskusi terarah, dan pembuktian kompetensi praktikum melalui penugasan LKPD.

2. **Kedaulatan & Keamanan Data (Self-Hosted / On-Premise Data Sovereignty):**
   Seluruh data profil siswa, portofolio tugas coding/jaringan, serta rekaman transkrip nilai tersimpan 100% di server mandiri milik sekolah tanpa bergantung pada server pihak ketiga luar negeri. Hal ini menghilangkan risiko kebocoran data pribadi peserta didik dan memenuhi regulasi perlindungan data pendidikan nasional.

3. **Efisiensi Anggaran Lembaga (Zero Licensing Fee / Free & Open Source):**
   Moodle berlisensi GNU GPL (bebas biaya langganan berulang). Sekolah kejuruan dapat mengalokasikan anggaran untuk peningkatan fasilitas laboratorium komputer fisik daripada membayar biaya lisensi per akun siswa setiap bulan.

4. **Engine Asesmen Terstandarisasi Industri (Gradebook Presisi 100% & Analytic Rubric):**
   Kompetensi kejuruan menuntut penilaian yang objektif, transparan, dan terukur. Moodle menyediakan kalkulasi *Gradebook* otomatis berbobot presisi 100% (Presensi 10%, LKPD Praktik 30%, Forum Diskusi 10%, UTS 20%, UAS 30%) serta fitur **Rubrik Penilaian Analitik 3 Dimensi** yang dapat dipelajari siswa sebelum mengumpulkan tugas.

5. **Manajemen Kontrol Waktu & Integritas Ujian (Time-Based Restrict Access):**
   Moodle memiliki kapabilitas penguncian materi dan asesmen berbasis waktu otomatis (contoh: UTS terkunci hingga 19 Oktober 2026 pukul 08:00 WIB), memastikan kedisiplinan dan integritas evaluasi tanpa perlu intervensi manual guru saat jam ujian dimulai.

6. **Stabilitas Jangka Panjang (LTS) & Antarmuka Ramah Generasi Z:**
   Versi 4.5 berstatus Long-Term Support (LTS) memberikan jaminan stabilitas sistem multi-tahun tanpa gangguan *breaking changes*, dipadukan dengan kustomisasi UI bertema teknologi modern yang meningkatkan motivasi belajar siswa SMK.

---

### KREDENSIAL AKUN DEMONSTRASI (MULTI-ROLE LOGIN MURNI)
Untuk mendemonstrasikan sistem secara autentik, presenter **wajib melakukan Log Out** dan **Log In menggunakan masing-masing akun terpisah** (bukan sekadar menggunakan fitur *Switch role / Ganti peran*):

1. **Role Administrator (Tata Kelola & Keamanan Sistem):**
   - **Username:** `admin` | **Password:** *(Kata sandi akun admin Anda)*
   - **Nama Tampilan:** Admin Pengguna (Inisial AP)
   - **Hak Akses Layar:** Memiliki menu navigasi *Administrasi situs*, tombol *Mode Edit*, dan kontrol penuh infrastruktur server.

2. **Role Guru Pengampu (Pedagogis & Asesmen Kelas):**
   - **Username:** `guru` | **Password:** `Guru123!`
   - **Nama Tampilan:** Wemvi Afrialdo, S.Kom., M.Kom.
   - **Hak Akses Layar:** Memiliki hak pengajar (*editing teacher*), sakelar *Mode Edit* di dalam kursus Informatika, manajemen Gradebook 100%, konfigurasi Restrict Access, dan penilaian Rubrik LKPD.

3. **Role Siswa SMK (Pengalaman Belajar Murni Peserta Didik):**
   - **Username:** `siswa` *(atau `siswa_fahri`)* | **Password:** `Siswa123!`
   - **Nama Tampilan:** Fahri Ramadhan (Siswa X RPL 1)
   - **Hak Akses Layar Murni Siswa:** 
     - **TIDAK MEMILIKI** menu *Administrasi situs*.
     - **TIDAK MEMILIKI** sakelar *Mode Edit*.
     - **TIDAK MEMILIKI** tombol *Buat kursus* maupun *Mengelola kursus*.
     - Layar siswa murni 100% berfokus pada: eksplorasi kartu kelas Informatika di Beranda & Kursusku, pemutaran modul video tersemat, partisipasi forum, dan pengumpulan tugas LKPD.

---

### PETUNJUK TEKNIS SEBELUM REKAMAN (CHECKLIST PERSIAPAN)
Sebelum memulai perekaman video, pastikan langkah-langkah persiapan berikut telah terpenuhi:
1. **Jendela XAMPP & Folder Siap:** XAMPP Control Panel diminimalkan di taskbar bersama File Explorer direktori `C:\\xampp\\` agar siap di-*Alt+Tab* ke layar saat demonstrasi.
2. **Kesiapan Kredensial Multi-Role:** Pastikan telah menguji login akun Guru (`guru` / `Guru123!`) dan akun Siswa (`siswa` / `Siswa123!`) di tab penyamaran (*Incognito*) atau dengan alur Log Out terlebih dahulu.
3. **Tab Browser Tersusun Rapi:**
   - Tab 1: `http://localhost/moodle/login/index.php` (Halaman Login Moodle)
   - Tab 2: `http://localhost/moodle/admin/index.php` (Halaman Pemberitahuan Admin & Bukti Versi Moodle 4.5 LTS)
   - Tab 3: `http://localhost/moodle/report/security/index.php` (Laporan Pemeriksaan Keamanan Admin - Status Hijau)
   - Tab 4: `http://localhost/moodle/course/view.php?id=2` (Halaman Kursus Informatika Kelas X)
   - Tab 5: `http://localhost/moodle/grade/edit/tree/index.php?id=2` (Pengaturan Buku Nilai / Gradebook)
   - Tab 6: `http://localhost/moodle/mod/assign/view.php?id=63` (Rubrik Penilaian LKPD Pertemuan 1)
   - Tab 7: `http://localhost/moodle/` (Halaman Beranda Modern Tech Vokasi)
   - Tab 8: `http://localhost/moodle/my/courses.php` (Halaman Kursusku dengan Animasi Hover Lift)
   - Tab 9: `http://localhost/moodle/mod/page/view.php?id=5` (Materi 2 dengan Video YouTube Tersemat)
4. **Perekam Layar (OBS Studio):** Resolusi kanvas 1080p (1920x1080), framerate 60 FPS, mikrofon teruji jernih tanpa noise berlebih.

---

## SUSUNAN SCENE & NASKAH LENGKAP

---

### SCENE 1: PEMBUKAAN, IDENTITAS DIRI, & URGENSI SISTEM (OPENING)
- **Estimasi Durasi:** 00:00 – 02:00 (2 Menit)
- **Layout Layar:** Kamera Penuh (Full Face) beralih ke Split Screen (Wajah Presenter + Cover Dokumen & Badge Moodle 4.5+ LTS).

#### [PANDUAN VISUAL & LANGKAH AKSI LAYAR]
1. Wajah presenter tampak tegak, ramah, dan profesional dengan pencahayaan optimal.
2. Pada detik ke-20, munculkan teks identitas grafis (*lower-third*) di layar:
   - Nama: Wemvi Afrialdo (NPM: 2413025052)
   - Program Studi: Pendidikan Teknologi Informasi, FKIP Universitas Lampung
   - Mata Kuliah: Learning Management System (LMS)
   - Dosen Pengampu: Ibu Ghea Chandra Surawan, M.Pd.
3. Pada detik ke-50, tampilkan slide pengantar grafis berjudul: *"Pengembangan LMS Informatika SMK Kelas X Fase E Berbasis Moodle 4.5+ LTS"*.

#### [NARASI LISAN PRESENTER]
"Assalamu’alaikum Warahmatullahi Wabarakatuh. Selamat pagi, siang, atau sore, salam sejahtera bagi kita semua, Shalom, Oom Swastiastu, Namo Buddhaya, Salam Kebajikan.

Yang saya hormati, Ibu Ghea Chandra Surawan, M.Pd., selaku Dosen Pengampu mata kuliah Learning Management System, serta rekan-rekan mahasiswa Program Studi Pendidikan Teknologi Informasi, Jurusan Pendidikan MIPA, Fakultas Keguruan dan Ilmu Pendidikan, Universitas Lampung yang saya banggakan.

Perkenalkan, nama saya Wemvi Afrialdo dengan NPM 2413025052. Pada kesempatan yang sangat berharga ini, saya akan mendemonstrasikan secara komprehensif hasil perancangan dan implementasi Learning Management System (LMS) berbasis Moodle versi 4.5+ Long Term Support untuk mata pelajaran Informatika Kelas X (Fase E) Sekolah Menengah Kejuruan, selaras dengan paradigma Kurikulum Merdeka.

Mengapa kami memilih Moodle 4.5+ LTS untuk ekosistem pembelajaran ini? Pertama, karena pendidikan vokasi SMK membutuhkan platform konstruktivisme sosial yang interaktif—bukan sekadar gudang penyimpanan berkas statis. Moodle menyediakan integrasi modul multimedia, dialektika forum nalar kritis, hingga praktikum vokasi nyata. Kedua, Moodle memberikan kedaulatan penuh atas data siswa melalui sistem on-premise yang aman, tanpa biaya lisensi per siswa, serta memiliki engine kalkulasi Gradebook 100% dan Rubrik Analitik yang sangat akuntabel.

Video presentasi ini akan membedah alur sistem secara berjenjang dari tiga sudut pandang peran pengguna: Pertama, Sisi Administrator: meninjau fondasi arsitektur server, manajemen sistem, dan audit keamanan berstatus hijau; Kedua, Sisi Guru Pengampu: meninjau struktur 16 pertemuan lengkap, penerapan 4 komponen wajib per sesi, time-based restrict access, dan pembobotan buku nilai; Dan ketiga, Sisi Siswa: merasakan langsung antarmuka modern tech vokasi yang estetik, modul video responsif, dan fleksibilitas pengumpulan tugas. Mari kita langsung menuju pembuktian sistem pada layar komputer."

---

### SCENE 2: PEMBUKTIAN XAMPP, ARSITEKTUR MOODLE 4.5+ LTS, & AUDIT KEAMANAN (ADMIN VIEW)
- **Estimasi Durasi:** 02:00 – 05:30 (3,5 Menit)
- **Layout Layar:** Screen Capture XAMPP Control Panel ➔ File Explorer Dataroot ➔ Halaman Login Moodle ➔ Admin Notifications (Versi Moodle) ➔ Security Overview Berstatus Hijau.

#### [PANDUAN VISUAL & LANGKAH AKSI LAYAR]
1. **Langkah 1 - Buka XAMPP Control Panel di Layar:**
   - Buka jendela XAMPP Control Panel v3.3.0 ke layar penuh.
   - Gerakkan kursor menyorot modul **Apache**: perlihatkan indikator teks berlatar belakang hijau menyala, PID aktif, dan Port 80, 443 berjalan stabil.
   - Gerakkan kursor menyorot modul **MySQL / MariaDB**: perlihatkan indikator teks berlatar belakang hijau menyala, PID aktif, dan Port 3306 berjalan normal.
2. **Langkah 2 - Buka File Explorer Direktori Server:**
   - Lakukan *Alt+Tab* ke jendela File Explorer direktori `C:\\xampp\\`.
   - Sorot folder `C:\\xampp\\htdocs\\moodle` (web root aplikasi).
   - Sorot folder `C:\\xampp\\moodledata` dan jelaskan secara visual bahwa folder data rahasia ini berada di luar folder publik `htdocs` demi standar keamanan berkas siswa.
3. **Langkah 3 - Halaman Login & Akses Administrator:**
   - Buka browser pada URL `http://localhost/moodle/login/index.php`.
   - Masukkan username `admin` dan kata sandi, lalu klik tombol **Masuk**.
4. **Langkah 4 - Buktikan Versi Rilis Moodle 4.5+ LTS:**
   - Di panel Moodle Admin, buka menu **Administrasi Situs > Pemberitahuan (Notifications)** (`http://localhost/moodle/admin/index.php`).
   - Sorot dengan kursor tulisan rilis sistem: **Moodle 4.5.13+ (Build: 20260911)**.
   - Buka menu **Administrasi Situs > Server > Lingkungan (Environment)** untuk memperlihatkan bahwa konfigurasi PHP 8.2 dan seluruh dependensi Moodle berstatus centang **OK (Hijau)**.
5. **Langkah 5 - Tunjukkan Laporan Audit Keamanan (Security Overview):**
   - Buka menu: **Administrasi Situs > Laporan > Pemeriksaan Keamanan** (`http://localhost/moodle/report/security/index.php`).
   - *Scroll perlahan* memperlihatkan bahwa seluruh indikator berstatus **HIJAU / OK**.
   - Sorot 4 parameter keamanan vital: penonaktifan `display_errors`, isolasi direktori berkas privat, standar kata sandi ketat minimal 8 karakter bersimbol, dan integritas basis data MariaDB.

#### [NARASI LISAN PRESENTER]
"(Menampilkan Jendela XAMPP Control Panel)
Kita mengawali pembuktian dari fondasi mesin server lokal. Pada layar monitor, Ibu Dosen dan rekan-rekan dapat melihat langsung jendela XAMPP Control Panel v3.3.0 yang sedang berjalan aktif. Di sini terlihat jelas bahwa modul web server Apache berjalan dengan PID aktif pada port 80 dan 443 berstatus hijau stabil, serta database server MariaDB berjalan pada port 3306 berstatus hijau menyala. Ini membuktikan bahwa sistem e-learning ini sepenuhnya siap melayani request secara on-premise.

(Beralih ke File Explorer Direktori C:\\xampp)
Bukan hanya itu, mari kita buktikan struktur keamanannya di File Explorer. Di sini kami menempatkan berkas aplikasi Moodle di dalam folder htdocs/moodle, sementara seluruh dokumen rahasia dan portofolio tugas siswa kami tempatkan di folder moodledata yang terisolasi secara fisik di luar htdocs. Isolasi ini menjamin bahwa dokumen pribadi siswa tidak dapat disusupi atau diunduh secara ilegal melalui tautan browser luar.

(Masuk ke Halaman Login & Dashboard Admin)
Sekarang, kita beralih ke peramban web pada Halaman Login Moodle. Saya masuk menggunakan akun Administrator untuk memperlihatkan tata kelola sistem.

(Membuka Menu Notifications & Lingkungan Server)
Untuk membuktikan versi platform yang digunakan, mari kita buka menu Administrasi Situs bagian Pemberitahuan. Di sini tertera secara gamblang bahwa sistem beroperasi di atas rilis resmi Moodle 4.5.13+ Long-Term Support (LTS) dengan tanggal build 11 September 2026. Dan pada menu Lingkungan Server, terlihat seluruh kriteria sistem—termasuk PHP 8.2 dan ekstensi basis data—seluruhnya berstatus centang OK atau Hijau. Pemilihan versi 4.5 LTS ini menjamin stabilitas performa multi-tahun bagi institusi kejuruan tanpa risiko gangguan sistem.

(Membuka Laporan Pemeriksaan Keamanan / Security Overview)
Puncaknya, mari kita tinjau Laporan Pemeriksaan Keamanan atau Security Overview Report. Seperti yang tampak pada layar, seluruh indikator pemeriksaan keamanan berstatus HIJAU atau OK. Kami telah menonaktifkan display_errors pada PHP agar kode internal server tidak bocor, memperkuat proteksi .htaccess pada moodledata, menegakkan aturan kata sandi kuat minimal 8 karakter, serta menjaga integritas basis data MariaDB. Fondasi administrator yang kokoh ini memastikan operasional pembelajaran bebas dari celah kerentanan."

---

### SCENE 3: SISI GURU PENGAMPU (TEACHER VIEW - STRUKTUR 16 PERTEMUAN, GRADEBOOK 100%, RESTRICT ACCESS, & RUBRIK)
- **Estimasi Durasi:** 05:30 – 09:30 (4 Menit)
- **Layout Layar:** Screen Capture Moodle (Buka Kelas Informatika ➔ Masuk Akun Guru ➔ Aktifkan Mode Edit ➔ Bedah 4 Komponen Wajib ➔ Restrict Access UTS ➔ Gradebook Setup 100% ➔ Rubrik Analitik LKPD).

#### [PANDUAN VISUAL & LANGKAH AKSI LAYAR]
1. Masuk ke kursus **Informatika Kelas X (Fase E)** (`http://localhost/moodle/course/view.php?id=2`) menggunakan akun guru pengampu (`guru` / `Guru123!`). Aktifkan tombol **Mode Edit (Edit Mode ON)** di pojok kanan atas hingga muncul ikon-ikon kontrol aktivitas.
2. *Scroll* dari Pertemuan 1 hingga Pertemuan 16 secara runut memperlihatkan keselarasan kurikulum: Berpikir Komputasional, Algoritma Pemrograman, Arsitektur Komputer, Jaringan Komputer, Analisis Data, hingga Proyek Akhir.
3. Tunjukkan bahwa tiap sesi wajib memiliki 4 Komponen Pembelajaran: Presensi Digital (P/L/E/A), Modul Ajar Interaktif (Page ber-video YouTube), Forum Diskusi Nalar Kritis, dan LKPD Praktikum.
4. Buka pengaturan Pertemuan 8 (UTS). Sorot aturan Restrict Access: *"Restricted: Not available unless it is on or after 19 October 2026, 08:00 AM"*.
5. Buka **Nilai > Pengaturan Buku Nilai (Gradebook Setup)**. Tunjukkan pembobotan kategori: Presensi 10%, Tugas LKPD 30%, Forum Diskusi 10%, UTS 20%, UAS 30% (Total Tepat 100%).
6. Buka penugasan **LKPD 1 > Penilaian Tingkat Lanjut > Rubrik**. Sorot 3 Kriteria Penilaian: Ketepatan Logika (40 pt), Kualitas & Kerapian Kode (35 pt), dan Format Laporan & Orisinalitas (25 pt) = 100 Poin.

#### [NARASI LISAN PRESENTER]
"(Di Halaman Kursus Informatika Sisi Guru)
Sekarang, kita beralih ke Sisi Guru Pengampu. Sebagai pendidik vokasi, guru memegang kendali pedagogis untuk memastikan kompetensi siswa terbangun secara runtut dan terukur.

(Mengaktifkan Mode Edit)
Dengan mengaktifkan Fitur Mode Edit, guru memiliki fleksibilitas penuh untuk menyusun dan mengelola aktivitas pembelajaran.

(Menunjukkan Struktur 16 Pertemuan)
Kurikulum yang kami kembangkan ini mencakup 16 Sesi Pertemuan Penuh untuk satu semester pembelajaran Informatika Fase E. Dimulai dari fondasi Berpikir Komputasional, Algoritma Pemrograman dasar Python, Arsitektur Komputer dan Jaringan, hingga Proyek Kolaboratif terpadu.

(Menjelaskan 4 Komponen Pembelajaran)
Guna menjaga konsistensi mutu, kami menetapkan Standar Mutu Empat Komponen Wajib pada setiap pertemuan pembelajaran: Pertama, Presensi Kehadiran Terintegrasi untuk memantau kedisiplinan peserta didik; Kedua, Modul Pembelajaran Interaktif berupa halaman materi yang diperkaya video edukasi kontekstual; Ketiga, Forum Diskusi Kolaboratif untuk melatih kemampuan nalar kritis dan pemecahan masalah; Dan keempat, Lembar Kerja Peserta Didik (LKPD) sebagai instrumen unjuk kerja praktikum.

(Menyorot Restrict Access Pertemuan 8 UTS)
Salah satu fitur krusial Moodle yang kami terapkan adalah Pembatasan Akses Berbasis Waktu (Time-based Restrict Access). Pada sesi Pertemuan 8 Ujian Tengah Semester ini, akses materi terkunci secara otomatis hingga tanggal 19 Oktober 2026 tepat pukul 08:00 WIB. Mekanisme ini menjamin integritas jadwal evaluasi secara disiplin tanpa memerlukan pembukaan manual oleh pengajar.

(Buka Halaman Gradebook Setup)
Keunggulan Moodle paling signifikan dibandingkan platform kelas lainnya terletak pada Sistem Penilaian Berstandar Industri (Gradebook Calculation). Pada menu Pengaturan Buku Nilai ini, kami telah mengalibrasi pembobotan kategori secara presisi mencapai akumulasi total tepat 100%: Presensi 10%, Tugas LKPD 30%, Forum Diskusi 10%, UTS 20%, dan UAS 30%.

(Buka Halaman Rubrik LKPD)
Tidak hanya itu, dalam menilai tugas vokasi, kami menerapkan Rubrik Penilaian Analitik Tiga Kriteria: Ketepatan Logika berbobot 40 poin, Kualitas dan Kerapian Kode berbobot 35 poin, serta Format Laporan dan Orisinalitas berbobot 25 poin. Dengan instrumen ini, proses asesmen berlangsung adil, akuntabel, dan bebas dari subjektivitas."

---

### SCENE 4: SISI SISWA (STUDENT VIEW - PENGALAMAN BELAJAR INTERAKTIF VOKASI SMK)
- **Estimasi Durasi:** 09:30 – 13:00 (3,5 Menit)
- **Layout Layar:** Screen Capture Moodle (Logout Akun Guru/Admin ➔ Login Akun Siswa `siswa` / `Siswa123!` ➔ Beranda Modern Tech ➔ Kursusku Bersih Tanpa Tombol Buat Kursus ➔ Materi 2 Video Responsif ➔ Form LKPD ➔ Materi Terkunci).

#### [PANDUAN VISUAL & LANGKAH AKSI LAYAR]
1. **Langkah Penting - Login Akun Siswa Murni:**
   - Lakukan **Log Out** dari akun sebelumnya.
   - Pada halaman login, masukkan kredensial siswa murni: Username `siswa` *(atau `siswa_fahri`)* dan Password `Siswa123!`.
   - Sorot avatar profil di pojok kanan atas yang kini bertuliskan **Fahri Ramadhan (Siswa X RPL 1)** dengan inisial **FR**.
2. **Pembuktian Dynamic UI & Pembatasan Role Siswa:**
   - Sorot navbar atas: perlihatkan bahwa menu *Administrasi situs* **sama sekali tidak muncul**.
   - Sorot pojok kanan atas: perlihatkan bahwa sakelar *Mode Edit* **tidak ada**.
   - Buka menu **Kursusku (`/my/courses.php`)**: perlihatkan bahwa tombol *Buat kursus* dan *Mengelola kursus* **sama sekali tidak ada** pada layar siswa. Ini membuktikan sistem hak akses (*role permissions*) Moodle telah terisolasi sempurna.
3. **Eksplorasi Beranda & Kursusku Siswa:**
   - Tunjukkan Hero Section bertema teknologi vokasi SMK dan tombol aksi cepat *"Buka Kelas Informatika"*.
   - Pada halaman Kursusku, gerakkan kursor ke kartu kursus memperlihatkan Efek Hover Lift (-6px) melayang halus dan Dynamic Progress Bar bergradasi *Electric Indigo to Emerald*.
4. **Eksplorasi Modul 2 dengan Video YouTube Responsif:**
   - Buka Materi 2. Tunjukkan video edukasi Berpikir Komputasional yang tersemat rapi (*Responsive Video Wrapper*) dan putar video selama beberapa detik.
5. **Partisipasi Forum Diskusi & Pratinjau Rubrik LKPD:**
   - Buka Forum Diskusi. Buka LKPD 1 memperlihatkan pratinjau matriks rubrik transparan. Klik *"Tambahkan pengajuan"* memperlihatkan form Multi-format Submission (teks daring & unggah berkas PDF).
6. **Transparansi Pertemuan Terkunci:**
   - Tunjukkan topik Pertemuan 8 (UTS) dari sudut pandang siswa, menampilkan ikon gembok dan tanggal buka secara gamblang.

#### [NARASI LISAN PRESENTER]
"(Di Halaman Beranda dari Sudut Pandang Siswa Murni)
Sekarang, mari kita buktikan bagaimana sistem ini membatasi hak akses dan memberikan pengalaman belajar yang aman melalui Sisi Siswa. Saya telah melakukan log out dan masuk secara autentik menggunakan akun siswa bernama Fahri Ramadhan dari kelas X RPL 1.

(Sorot Navbar & Halaman Kursusku yang Bersih)
Dapat kita saksikan bersama, sistem Dynamic Role Rendering Moodle berjalan sempurna. Pada akun siswa ini, menu Administrasi Situs dan sakelar Mode Edit sama sekali tidak ada. Begitu pula pada halaman Kursusku, siswa tidak memiliki tombol 'Buat kursus' maupun hak mengelola sistem. Antarmuka siswa murni terisolasi hanya untuk keperluan belajar.

(Sorot Hero Banner Beranda)
Siswa disambut oleh antarmuka modern dengan Hero Section bertema teknologi vokasi SMK, memuat ringkasan Tiga Pilar Kejuruan dan tombol aksi cepat untuk langsung memulai belajar.

(Buka Halaman Kursusku & Gerakkan Kursor)
Ketika siswa membuka menu Kursusku, nuansa interaktif semakin terasa: Header halaman dibalut banner bergaya portal teknologi, sementara kartu kursus dilengkapi Efek Hover Lift yang melayang dinamis saat disentuh kursor. Dilengkapi pula cover kelas berkualitas tinggi dan progress bar gamifikasi yang secara visual memotivasi siswa untuk terus menuntaskan setiap target pembelajaran.

(Buka Materi 2 Video YouTube)
Saat siswa mempelajari konsep, kami menghadirkan Fitur Multimedia Learning Wrapper pada modul Halaman Materi. Sebagaimana yang tampak pada Materi Pertemuan 2 ini, video pembelajaran YouTube mengenai Fondasi Berpikir Komputasional tersemat secara responsif. Siswa dapat memutar dan menyimak penjelasan audio visual secara langsung di dalam Moodle tanpa risiko terdistraksi oleh algoritma rekomendasi aplikasi luar.

(Buka LKPD 1 dari Sudut Pandang Siswa)
Ketika siswa hendak mengerjakan lembar kerja praktikum, prinsip transparansi penilaian terwujud secara nyata. Siswa dapat membaca Matriks Rubrik Penilaian terlebih dahulu, sehingga mereka memahami standar kualitas apa yang harus dipenuhi untuk meraih poin maksimal 100.

(Tunjukkan Form Pengumpulan Tugas)
Melalui Fitur Multi-Format Submission, siswa diberikan kemudahan: Mereka dapat mengetikkan penjelasan ringkas pada kotak teks daring, sekaligus mengunggah berkas laporan formal format PDF atau DOCX melalui kotak unggah berkas yang terlindungi sistem validasi.

Pengalaman belajar siswa ditutup dengan kepastian jadwal, di mana materi evaluasi yang terkunci menampilkan informasi tanggal buka secara gamblang. Rangkaian fitur ini membuktikan bahwa Moodle mampu menjadi ruang belajar digital yang ramah, mandiri, dan berpusat pada siswa SMK masa kini."

---

### SCENE 5: REKAPITULASI PROGRES 7 MINGGU & PENUTUP (CLOSING)
- **Estimasi Durasi:** 13:00 – 15:00 (2 Menit)
- **Layout Layar:** Tampilkan Tabel Rekapitulasi Progres 7 Pertemuan Pengembangan di Layar, lalu beralih ke Kamera Penuh Presenter (Full Face).

#### [PANDUAN VISUAL & LANGKAH AKSI LAYAR]
1. Tampilkan Tabel Rekapitulasi Progres 7 Pertemuan Pengembangan LMS (Minggu 1 s/d Minggu 7).
2. Beralih ke kamera penuh presenter (*Full Face*) untuk penyampaian pesan penutup secara santun, berwibawa, dan penuh percaya diri.

#### [NARASI LISAN PRESENTER]
"(Sorot Tabel Rekapitulasi Progres)
Seluruh rangkaian pengembangan LMS Informatika ini telah dikerjakan secara sistematis dan terdokumentasi rapi dalam tabel rekapitulasi progres selama tujuh siklus pengembangan terhitung mundur dari 13 Oktober 2026. Dimulai dari tahapan analisis pedagogis Kurikulum Merdeka, instalasi infrastruktur Moodle 4.5+ LTS, perancangan 16 pertemuan lengkap, hingga tahap penghalusan antarmuka modern dan verifikasi multi-role yang baru saja kita saksikan bersama.

(Kamera Penuh Presenter)
Sebagai kesimpulan, proyek Learning Management System Informatika Kelas X Fase E ini telah membuktikan integrasi yang harmonis antara kekuatan filosofi Kurikulum Merdeka, keandalan teknis Moodle dari sisi Admin dan Guru, serta kenyamanan pengalaman belajar interaktif dari sisi Siswa.

Saya mengucapkan terima kasih yang sebesar-besarnya kepada Dosen Pengampu kami, Ibu Ghea Chandra Surawan, M.Pd., atas bimbingan, arahan, dan inspirasi berharga yang telah dicurahkan sepanjang perkuliahan Learning Management System ini. Semoga karya sistem e-learning ini dapat memberikan kontribusi nyata bagi pengembangan teknologi pendidikan kejuruan di tanah air.

Mohon maaf atas segala keterbatasan dalam penyampaian dan tutur kata saya. Terima kasih atas perhatian Ibu Dosen dan rekan-rekan sekalian. Wabillahi taufiq wal hidayah, Wassalamu’alaikum Warahmatullahi Wabarakatuh."

---

### RINGKASAN TIMELINE & CUE CARD PEREKAMAN

| Menit Ke- | Bagian / Scene | Sudut Pandang / Fokus | Aksi Layar Utama |
|---|---|---|---|
| **00:00 – 02:00** | **Scene 1: Pembukaan & Urgensi** | Identitas Presenter, Pengantar LMS & Alasan Memilih Moodle 4.5+ LTS | Kamera Penuh ➔ Grafis Identitas UNILA & Slide Judul |
| **02:00 – 05:30** | **Scene 2: Sisi Administrator** | Demo XAMPP Control Panel, Direktori Dataroot, Versi Moodle 4.5 LTS & Audit Keamanan | XAMPP Panel ➔ File Explorer ➔ Moodle Admin Notifications ➔ Security Report (Hijau) |
| **05:30 – 09:30** | **Scene 3: Sisi Guru Pengampu** | Mode Edit ON, 16 Sesi Lengkap, Restrict Access, Gradebook 100%, Rubrik LKPD | Kursus Informatika ➔ Edit Section ➔ Gradebook Setup ➔ Rubrik LKPD |
| **09:30 – 13:00** | **Scene 4: Sisi Siswa SMK** | Login Siswa Murni, UI Bersih Tanpa Buat Kursus, Modul Video YouTube, Form LKPD | Beranda Modern ➔ Kursusku ➔ Modul 2 Video ➔ Form Tugas LKPD |
| **13:00 – 15:00** | **Scene 5: Rekapitulasi & Penutup** | Tabel Progres 7 Minggu Pengembangan & Salam Penutup | Tabel Rekapitulasi Progres ➔ Kamera Penuh Presenter |

---
"""

# ==========================================
# 2. WRITE MARKDOWN FILE (UTF-8)
# ==========================================
def write_markdown_file():
    print(f"Menulis file Markdown ke: {MD_OUTPUT_PATH}")
    with open(MD_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(MARKDOWN_CONTENT)
    print("File Markdown berhasil diperbarui!")

# ==========================================
# 3. BUILD DOCX WITH TIMES NEW ROMAN 12 PT JUSTIFIED (NO PARAGRAPH BORDER LINES)
# ==========================================
def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0B0B0", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def build_docx_file():
    print(f"Membangun file DOCX ke: {DOCX_OUTPUT_PATH}")
    doc = docx.Document()

    # Set Margins: 1 inch (standard academic)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
        # Header & Footer in Times New Roman
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Naskah Presentasi LMS Moodle 4.5+ LTS | Informatika SMK Fase E")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(10)
        hrun.font.color.rgb = RGBColor(100, 100, 100)

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Pendidikan Teknologi Informasi - FKIP Universitas Lampung")
        frun.font.name = "Times New Roman"
        frun.font.size = Pt(10)
        frun.font.color.rgb = RGBColor(100, 100, 100)

    # Base Normal Style: Times New Roman 12 pt, Justified
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0) # Black academic

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_subtitle(text, size=12):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_para(text, bold_prefix="", italic=False, space_after=6, indent=0):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if indent > 0:
            p.paragraph_format.left_indent = Inches(indent)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = 'Times New Roman'
            r_pre.font.size = Pt(12)
            r_pre.font.color.rgb = RGBColor(0, 0, 0)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.italic = italic

    # ------------------------------------------
    # HEADER DOKUMEN
    # ------------------------------------------
    add_title("NASKAH & SKRIP REKAMAN VIDEO PRESENTASI")
    add_subtitle("PENGEMBANGAN LEARNING MANAGEMENT SYSTEM (LMS) BERBASIS MOODLE 4.5+ LTS", size=13)
    add_subtitle("MATA PELAJARAN INFORMATIKA KELAS X (FASE E) – KURIKULUM MERDEKA", size=12)

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(8)

    # ------------------------------------------
    # INFORMASI PRODUKSI VIDEO
    # ------------------------------------------
    add_h1("INFORMASI PRODUKSI VIDEO")
    prod_data = [
        ("Presenter / Pembicara", "Wemvi Afrialdo"),
        ("NPM", "2413025052"),
        ("Program Studi", "Pendidikan Teknologi Informasi (PTI)"),
        ("Jurusan / Fakultas", "Pendidikan MIPA / FKIP Universitas Lampung"),
        ("Mata Kuliah", "Learning Management System (LMS)"),
        ("Dosen Pengampu", "Ibu Ghea Chandra Surawan, M.Pd."),
        ("Platform E-Learning", "Moodle 4.5.13+ LTS (Long Term Support, Build: 20260911)"),
        ("Lingkungan Hosting", "On-Premise / Localhost XAMPP (Apache 2.4, PHP 8.2, MariaDB 10.4)"),
        ("Sasaran Pengguna", "Peserta Didik Sekolah Menengah Kejuruan (SMK) Kelas X (Fase E)"),
        ("Target Durasi Video", "12 – 15 Menit")
    ]
    tbl_prod = doc.add_table(rows=len(prod_data), cols=2)
    tbl_prod.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_prod, color="D0D0D0", sz="4", val="single")
    for idx, (lbl, val) in enumerate(prod_data):
        c0 = tbl_prod.cell(idx, 0)
        c1 = tbl_prod.cell(idx, 1)
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_margins(c0, top=50, bottom=50, left=100, right=100)
        set_cell_margins(c1, top=50, bottom=50, left=100, right=100)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r0 = p0.add_run(lbl)
        r0.bold = True
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(11)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r1 = p1.add_run(val)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)

    # ------------------------------------------
    # PANDUAN PRAKTIK PEMBUKTIAN VISUAL
    # ------------------------------------------
    add_h1("PANDUAN PRAKTIK PEMBUKTIAN VISUAL (DEMO REAL-TIME DI LAYAR)")
    add_para("Agar presentasi tidak terkesan hanya berbicara teori (tidak hanya sekadar ngomong saja), presenter wajib memperlihatkan bukti teknis operasional secara langsung di layar monitor melalui urutan aksi berikut:")
    add_para(" Buka dan tampilkan jendela XAMPP Control Panel v3.3.0 di layar. Sorot dengan kursor mouse bahwa modul Apache berstatus aktif (PID terisi, Port 80, 443 berlatar hijau terang), serta modul MySQL/MariaDB berstatus aktif (PID terisi, Port 3306 berlatar hijau terang). Klik tombol Explorer pada panel XAMPP untuk membuka jendela direktori Windows.", bold_prefix="1. Pembuktian Visual Server XAMPP:")
    add_para(" Tunjukkan folder instalasi Moodle di C:\\xampp\\htdocs\\moodle sebagai root aplikasi publik. Tunjukkan pula folder penyimpanan dokumen siswa di C:\\xampp\\moodledata yang terisolasi di luar folder htdocs. Jelaskan bahwa pemisahan fisik ini adalah bukti kepatuhan keamanan data tingkat tinggi (security hardening) agar dokumen rahasia rapor/tugas siswa tidak dapat diakses langsung melalui URL browser.", bold_prefix="2. Pembuktian Visual Struktur Direktori & Keamanan Dataroot:")
    add_para(" Di antarmuka Moodle Administrator, buka menu Administrasi Situs > Pemberitahuan (Notifications) pada URL http://localhost/moodle/admin/index.php. Arahkan kamera/kursor ke bagian bawah halaman yang memuat label rilis resmi: Moodle 4.5.13+ (Build: 20260911). Buka pula menu Administrasi Situs > Server > Lingkungan (Environment) pada URL http://localhost/moodle/admin/environment.php untuk memperlihatkan tabel versi PHP 8.2.x dan komponen server berstatus centang OK (Hijau).", bold_prefix="3. Pembuktian Visual Versi Rilis Moodle 4.5.13+ LTS:")
    add_para(" Buka menu Administrasi Situs > Laporan > Pemeriksaan Keamanan (http://localhost/moodle/report/security/index.php). Gulir (scroll) perlahan memperlihatkan seluruh parameter berstatus HIJAU / OK (termasuk display_errors = Off dan proteksi berkas privat).", bold_prefix="4. Pembuktian Visual Laporan Audit Keamanan (Security Overview):")

    # ------------------------------------------
    # SPESIFIKASI TEKNIS & LINGKUNGAN SISTEM MOODLE
    # ------------------------------------------
    add_h1("SPESIFIKASI TEKNIS & LINGKUNGAN SISTEM MOODLE")
    add_para("Sistem E-Learning ini dibangun menggunakan konfigurasi perangkat lunak standar industri pendidikan untuk menjamin performa, keamanan, dan keandalan data pembelajaran:")

    spec_data = [
        ("Moodle Core Engine", "Moodle 4.5.13+ (Build: 20260911)", "Rilis LTS (Long-Term Support). Dibuktikan langsung via menu Notifications & Environment Admin."),
        ("Web Server", "Apache 2.4.58 (XAMPP v3.3.0)", "Menangani koneksi HTTP lokal. Dibuktikan via XAMPP Control Panel (Port 80, 443 aktif hijau)."),
        ("PHP Runtime", "PHP 8.2.12", "Kompatibel penuh dengan Moodle 4.5; memory_limit = 512M, display_errors = Off."),
        ("Database Server", "MariaDB 10.4.32", "Engine InnoDB, Collation utf8mb4_general_ci. Dibuktikan via port 3306 XAMPP aktif hijau."),
        ("Dataroot Storage", "C:\\xampp\\moodledata", "Terisolasi di luar htdocs. Dibuktikan via File Explorer untuk memastikan proteksi berkas."),
        ("UI / Theme Framework", "Boost Theme + Custom SCSS Vokasi", "Dilengkapi Hero Banner SMK, Hover Lift Card Effect, Dynamic Progress Bar, dan Grid.")
    ]
    tbl_spec = doc.add_table(rows=len(spec_data) + 1, cols=3)
    tbl_spec.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_spec, color="D0D0D0", sz="4", val="single")

    headers_spec = ["Komponen Sistem", "Spesifikasi / Konfigurasi", "Keterangan Fungsional & Pembuktian Layar"]
    widths_spec = [Inches(1.8), Inches(2.2), Inches(2.5)]
    for j, h in enumerate(headers_spec):
        c = tbl_spec.cell(0, j)
        c.width = widths_spec[j]
        set_cell_margins(c, top=60, bottom=60, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    for i, row in enumerate(spec_data):
        for j in range(3):
            c = tbl_spec.cell(i + 1, j)
            c.width = widths_spec[j]
            set_cell_margins(c, top=50, bottom=50, left=100, right=100)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r = p.add_run(row[j])
            if j == 0:
                r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)

    # ------------------------------------------
    # RASIONALISASI PEMILIHAN MOODLE
    # ------------------------------------------
    add_h1("RASIONALISASI: MENGAPA MEMILIH MOODLE 4.5+ LTS UNTUK INFORMATIKA SMK FASE E?")
    add_para("Pemilihan platform Moodle versi 4.5+ LTS didasarkan pada pertimbangan pedagogis, teknis, dan strategis vokasi yang matang, bukan sekadar alternatif repositori berkas sederhana:")
    
    reasons = [
        ("1. Keselarasan Pedagogis Kurikulum Merdeka (Konstruktivisme Sosial):",
         " Platform e-learning vokasi tidak boleh sekadar berfungsi sebagai 'gudang file statis' (file dump). Moodle dibangun di atas filosofi konstruktivisme sosial di mana pengetahuan dibangun melalui interaksi aktif: eksplorasi materi mandiri ber-multimedia, dialektika nalar kritis di forum diskusi terarah, dan pembuktian kompetensi praktikum melalui penugasan LKPD berbobot."),
        ("2. Kedaulatan & Keamanan Data (Self-Hosted / On-Premise Data Sovereignty):",
         " Seluruh data profil siswa, portofolio tugas coding/jaringan, serta rekaman transkrip nilai tersimpan 100% di server mandiri milik sekolah tanpa bergantung pada server pihak ketiga luar negeri. Ini menjamin privasi siswa dan kepatuhan regulasi data pendidikan."),
        ("3. Efisiensi Anggaran Lembaga (Zero Licensing Fee / Free & Open Source):",
         " Moodle berlisensi GNU GPL (bebas biaya langganan berulang). Sekolah kejuruan dapat mengalokasikan anggaran untuk peningkatan fasilitas lab komputer fisik daripada membayar biaya lisensi per akun siswa setiap bulan."),
        ("4. Engine Asesmen Terstandarisasi Industri (Gradebook Presisi 100% & Analytic Rubric):",
         " Kompetensi kejuruan menuntut penilaian yang objektif, transparan, dan terukur. Moodle menyediakan kalkulasi Gradebook otomatis berbobot presisi 100% (Presensi 10%, LKPD Praktik 30%, Forum Diskusi 10%, UTS 20%, UAS 30%) serta fitur Rubrik Penilaian Analitik 3 Dimensi yang dapat dipelajari siswa sebelum mengumpulkan tugas."),
        ("5. Manajemen Kontrol Waktu & Integritas Ujian (Time-Based Restrict Access):",
         " Moodle memiliki kapabilitas penguncian materi dan asesmen berbasis waktu otomatis (contoh: UTS terkunci hingga 19 Oktober 2026 pukul 08:00 WIB), memastikan kedisiplinan dan integritas evaluasi tanpa perlu intervensi manual guru saat jam ujian dimulai."),
        ("6. Stabilitas Jangka Panjang (LTS) & Antarmuka Ramah Generasi Z:",
         " Versi 4.5 berstatus Long-Term Support (LTS) memberikan jaminan stabilitas sistem multi-tahun tanpa gangguan breaking changes, dipadukan dengan kustomisasi UI bertema teknologi modern yang meningkatkan motivasi belajar siswa SMK.")
    ]
    for title, desc in reasons:
        add_para(desc, bold_prefix=title)

    # ------------------------------------------
    # KREDENSIAL AKUN DEMONSTRASI
    # ------------------------------------------
    add_h1("KREDENSIAL AKUN DEMONSTRASI (MULTI-ROLE LOGIN MURNI)")
    add_para("Untuk mendemonstrasikan sistem secara autentik, presenter wajib melakukan Log Out dan Log In menggunakan masing-masing akun terpisah (bukan sekadar menggunakan fitur Switch role / Ganti peran):")
    add_para(" Username: admin | Password: (Kata sandi akun admin Anda) | Nama: Admin Pengguna (Inisial AP). Peran: Memiliki menu navigasi Administrasi situs, tombol Mode Edit, dan kontrol penuh infrastruktur server.", bold_prefix="1. Role Administrator (Tata Kelola & Keamanan Sistem):")
    add_para(" Username: guru | Password: Guru123! | Nama: Wemvi Afrialdo, S.Kom., M.Kom. Peran: Pengaktifan Mode Edit, manajemen 16 pertemuan lengkap, penataan 4 komponen pembelajaran, konfigurasi pembatasan waktu (Restrict Access), dan pembobotan nilai Gradebook 100%.", bold_prefix="2. Role Guru Pengampu (Pedagogis & Asesmen):")
    add_para(" Username: siswa (atau siswa_fahri) | Password: Siswa123! | Nama: Fahri Ramadhan (Siswa X RPL 1). Hak Akses Layar Murni Siswa: TIDAK MEMILIKI menu Administrasi situs, TIDAK MEMILIKI sakelar Mode Edit, dan TIDAK MEMILIKI tombol Buat kursus. Layar siswa murni 100% bersih hanya untuk belajar, membuka modul video, berdiskusi di forum, dan mengumpulkan LKPD.", bold_prefix="3. Role Siswa SMK (Pengalaman Belajar Interaktif Murni):")

    # ------------------------------------------
    # SUSUNAN SCENE & NASKAH LENGKAP (NO PARAGRAPH BORDER LINES)
    # ------------------------------------------
    add_h1("SUSUNAN SCENE & NASKAH LENGKAP")

    # SCENE 1
    add_h2("SCENE 1: PEMBUKAAN, IDENTITAS DIRI, & URGENSI SISTEM (OPENING)")
    add_para(" 00:00 – 02:00 (2 Menit)", bold_prefix="Estimasi Durasi:")
    add_para(" Kamera Penuh (Full Face) beralih ke Split Screen (Wajah Presenter + Cover Dokumen & Badge Moodle 4.5+ LTS).", bold_prefix="Layout Layar:")
    
    add_para("", bold_prefix="[PANDUAN VISUAL & LANGKAH AKSI LAYAR]")
    add_para("1. Wajah presenter tampak tegak, ramah, dan profesional dengan pencahayaan optimal.")
    add_para("2. Pada detik ke-20, munculkan teks identitas grafis (lower-third) di layar: Nama Wemvi Afrialdo (NPM: 2413025052), Program Studi Pendidikan Teknologi Informasi, FKIP Universitas Lampung, Mata Kuliah Learning Management System (LMS), Dosen Pengampu Ibu Ghea Chandra Surawan, M.Pd.")
    add_para("3. Pada detik ke-50, tampilkan slide pengantar grafis berjudul: 'Pengembangan LMS Informatika SMK Kelas X Fase E Berbasis Moodle 4.5+ LTS'.")

    add_para("", bold_prefix="[NARASI LISAN PRESENTER]")
    add_para('"Assalamu’alaikum Warahmatullahi Wabarakatuh. Selamat pagi, siang, atau sore, salam sejahtera bagi kita semua, Shalom, Oom Swastiastu, Namo Buddhaya, Salam Kebajikan."', italic=True, indent=0.35)
    add_para('"Yang saya hormati, Ibu Ghea Chandra Surawan, M.Pd., selaku Dosen Pengampu mata kuliah Learning Management System, serta rekan-rekan mahasiswa Program Studi Pendidikan Teknologi Informasi, Jurusan Pendidikan MIPA, Fakultas Keguruan dan Ilmu Pendidikan, Universitas Lampung yang saya banggakan."', italic=True, indent=0.35)
    add_para('"Perkenalkan, nama saya Wemvi Afrialdo dengan NPM 2413025052. Pada kesempatan yang sangat berharga ini, saya akan mendemonstrasikan secara komprehensif hasil perancangan dan implementasi Learning Management System (LMS) berbasis Moodle versi 4.5+ Long Term Support untuk mata pelajaran Informatika Kelas X (Fase E) Sekolah Menengah Kejuruan, selaras dengan paradigma Kurikulum Merdeka."', italic=True, indent=0.35)
    add_para('"Mengapa kami memilih Moodle 4.5+ LTS untuk ekosistem pembelajaran ini? Pertama, karena pendidikan vokasi SMK membutuhkan platform konstruktivisme sosial yang interaktif—bukan sekadar gudang penyimpanan berkas statis. Moodle menyediakan integrasi modul multimedia, dialektika forum nalar kritis, hingga praktikum vokasi nyata. Kedua, Moodle memberikan kedaulatan penuh atas data siswa melalui sistem on-premise yang aman, tanpa biaya lisensi per siswa, serta memiliki engine kalkulasi Gradebook 100% dan Rubrik Analitik yang sangat akuntabel."', italic=True, indent=0.35)
    add_para('"Video presentasi ini akan membedah alur sistem secara berjenjang dari tiga sudut pandang peran pengguna: Pertama, Sisi Administrator: meninjau fondasi arsitektur server, manajemen sistem, dan audit keamanan berstatus hijau; Kedua, Sisi Guru Pengampu: meninjau struktur 16 pertemuan lengkap, penerapan 4 komponen wajib per sesi, time-based restrict access, dan pembobotan buku nilai; Dan ketiga, Sisi Siswa: merasakan langsung antarmuka modern tech vokasi yang estetik, modul video responsif, dan fleksibilitas pengumpulan tugas. Mari kita langsung menuju pembuktian sistem pada layar komputer."', italic=True, indent=0.35)

    # SCENE 2
    add_h2("SCENE 2: PEMBUKTIAN XAMPP, ARSITEKTUR MOODLE 4.5+ LTS, & AUDIT KEAMANAN (ADMIN VIEW)")
    add_para(" 02:00 – 05:30 (3,5 Menit)", bold_prefix="Estimasi Durasi:")
    add_para(" Screen Capture XAMPP Control Panel ➔ File Explorer Dataroot ➔ Halaman Login Moodle ➔ Admin Notifications (Versi Moodle) ➔ Security Overview Berstatus Hijau.", bold_prefix="Layout Layar:")

    add_para("", bold_prefix="[PANDUAN VISUAL & LANGKAH AKSI LAYAR]")
    add_para("1. Langkah 1 - Buka XAMPP Control Panel di Layar: Buka jendela XAMPP Control Panel v3.3.0 ke layar penuh. Gerakkan kursor menyorot modul Apache: perlihatkan indikator teks berlatar belakang hijau menyala, PID aktif, dan Port 80, 443 berjalan stabil. Gerakkan kursor menyorot modul MySQL / MariaDB: perlihatkan indikator teks berlatar belakang hijau menyala, PID aktif, dan Port 3306 berjalan normal.")
    add_para("2. Langkah 2 - Buka File Explorer Direktori Server: Lakukan Alt+Tab ke jendela File Explorer direktori C:\\xampp\\. Sorot folder C:\\xampp\\htdocs\\moodle (web root aplikasi). Sorot folder C:\\xampp\\moodledata dan jelaskan secara visual bahwa folder data rahasia ini berada di luar folder publik htdocs demi standar keamanan berkas siswa.")
    add_para("3. Langkah 3 - Halaman Login & Akses Administrator: Buka browser pada URL http://localhost/moodle/login/index.php. Masukkan username admin dan kata sandi, lalu klik tombol Masuk.")
    add_para("4. Langkah 4 - Buktikan Versi Rilis Moodle 4.5+ LTS: Di panel Moodle Admin, buka menu Administrasi Situs > Pemberitahuan (Notifications) pada URL http://localhost/moodle/admin/index.php. Sorot dengan kursor tulisan rilis sistem: Moodle 4.5.13+ (Build: 20260911). Buka menu Administrasi Situs > Server > Lingkungan (Environment) untuk memperlihatkan bahwa konfigurasi PHP 8.2 dan seluruh dependensi Moodle berstatus centang OK (Hijau).")
    add_para("5. Langkah 5 - Tunjukkan Laporan Audit Keamanan (Security Overview): Buka menu Administrasi Situs > Laporan > Pemeriksaan Keamanan (http://localhost/moodle/report/security/index.php). Scroll perlahan memperlihatkan bahwa seluruh indikator berstatus HIJAU / OK. Sorot 4 parameter keamanan vital: penonaktifan display_errors, isolasi direktori berkas privat, standar kata sandi ketat minimal 8 karakter bersimbol, dan integritas basis data MariaDB.")

    add_para("", bold_prefix="[NARASI LISAN PRESENTER]")
    add_para('"(Menampilkan Jendela XAMPP Control Panel)\nKita mengawali pembuktian dari fondasi mesin server lokal. Pada layar monitor, Ibu Dosen dan rekan-rekan dapat melihat langsung jendela XAMPP Control Panel v3.3.0 yang sedang berjalan aktif. Di sini terlihat jelas bahwa modul web server Apache berjalan dengan PID aktif pada port 80 dan 443 berstatus hijau stabil, serta database server MariaDB berjalan pada port 3306 berstatus hijau menyala. Ini membuktikan bahwa sistem e-learning ini sepenuhnya siap melayani request secara on-premise."', italic=True, indent=0.35)
    add_para('"(Beralih ke File Explorer Direktori C:\\xampp)\nBukan hanya itu, mari kita buktikan struktur keamanannya di File Explorer. Di sini kami menempatkan berkas aplikasi Moodle di dalam folder htdocs/moodle, sementara seluruh dokumen rahasia dan portofolio tugas siswa kami tempatkan di folder moodledata yang terisolasi secara fisik di luar htdocs. Isolasi ini menjamin bahwa dokumen pribadi siswa tidak dapat disusupi atau diunduh secara ilegal melalui tautan browser luar."', italic=True, indent=0.35)
    add_para('"(Masuk ke Halaman Login & Dashboard Admin)\nSekarang, kita beralih ke peramban web pada Halaman Login Moodle. Saya masuk menggunakan akun Administrator untuk memperlihatkan tata kelola sistem."', italic=True, indent=0.35)
    add_para('"(Membuka Menu Notifications & Lingkungan Server)\nUntuk membuktikan versi platform yang digunakan, mari kita buka menu Administrasi Situs bagian Pemberitahuan. Di sini tertera secara gamblang bahwa sistem beroperasi di atas rilis resmi Moodle 4.5.13+ Long-Term Support (LTS) dengan tanggal build 11 September 2026. Dan pada menu Lingkungan Server, terlihat seluruh kriteria sistem—termasuk PHP 8.2 dan ekstensi basis data—seluruhnya berstatus centang OK atau Hijau. Pemilihan versi 4.5 LTS ini menjamin stabilitas performa multi-tahun bagi institusi kejuruan tanpa risiko gangguan sistem."', italic=True, indent=0.35)
    add_para('"(Membuka Laporan Pemeriksaan Keamanan / Security Overview)\nPuncaknya, mari kita tinjau Laporan Pemeriksaan Keamanan atau Security Overview Report. Seperti yang tampak pada layar, seluruh indikator pemeriksaan keamanan berstatus HIJAU atau OK. Kami telah menonaktifkan display_errors pada PHP agar kode internal server tidak bocor, memperkuat proteksi .htaccess pada moodledata, menegakkan aturan kata sandi kuat minimal 8 karakter, serta menjaga integritas basis data MariaDB. Fondasi administrator yang kokoh ini memastikan operasional pembelajaran bebas dari celah kerentanan."', italic=True, indent=0.35)

    # SCENE 3
    add_h2("SCENE 3: SISI GURU PENGAMPU (TEACHER VIEW - STRUKTUR 16 PERTEMUAN, GRADEBOOK 100%, RESTRICT ACCESS, & RUBRIK)")
    add_para(" 05:30 – 09:30 (4 Menit)", bold_prefix="Estimasi Durasi:")
    add_para(" Screen Capture Moodle (Buka Kelas Informatika ➔ Masuk Akun Guru 'guru' / 'Guru123!' ➔ Aktifkan Mode Edit ➔ Bedah 4 Komponen Wajib ➔ Restrict Access UTS ➔ Gradebook Setup 100% ➔ Rubrik Analitik LKPD).", bold_prefix="Layout Layar:")

    add_para("", bold_prefix="[PANDUAN VISUAL & LANGKAH AKSI LAYAR]")
    add_para("1. Masuk ke kursus Informatika Kelas X (Fase E) (http://localhost/moodle/course/view.php?id=2) menggunakan akun guru pengampu (guru / Guru123!). Aktifkan tombol Mode Edit (Edit Mode ON) di pojok kanan atas hingga muncul ikon-ikon kontrol aktivitas.")
    add_para("2. Scroll dari Pertemuan 1 hingga Pertemuan 16 secara runut memperlihatkan keselarasan kurikulum: Berpikir Komputasional, Algoritma Pemrograman, Arsitektur Komputer, Jaringan Komputer, Analisis Data, hingga Proyek Akhir.")
    add_para("3. Tunjukkan bahwa tiap sesi wajib memiliki 4 Komponen Pembelajaran: Presensi Digital (P/L/E/A), Modul Ajar Interaktif (Page ber-video YouTube), Forum Diskusi Nalar Kritis, dan LKPD Praktikum.")
    add_para("4. Buka pengaturan Pertemuan 8 (UTS). Sorot aturan Restrict Access: 'Restricted: Not available unless it is on or after 19 October 2026, 08:00 AM'.")
    add_para("5. Buka Nilai > Pengaturan Buku Nilai (Gradebook Setup). Tunjukkan pembobotan kategori: Presensi 10%, Tugas LKPD 30%, Forum Diskusi 10%, UTS 20%, UAS 30% (Total Tepat 100%).")
    add_para("6. Buka penugasan LKPD 1 > Penilaian Tingkat Lanjut > Rubrik. Sorot 3 Kriteria Penilaian: Ketepatan Logika (40 pt), Kualitas & Kerapian Kode (35 pt), dan Format Laporan & Orisinalitas (25 pt) = 100 Poin.")

    add_para("", bold_prefix="[NARASI LISAN PRESENTER]")
    add_para('"(Di Halaman Kursus Informatika Sisi Guru)\nSekarang, kita beralih ke Sisi Guru Pengampu. Sebagai pendidik vokasi, guru memegang kendali pedagogis untuk memastikan kompetensi siswa terbangun secara runtut dan terukur."', italic=True, indent=0.35)
    add_para('"(Mengaktifkan Mode Edit)\nDengan mengaktifkan Fitur Mode Edit, guru memiliki fleksibilitas penuh untuk menyusun dan mengelola aktivitas pembelajaran."', italic=True, indent=0.35)
    add_para('"(Menunjukkan Struktur 16 Pertemuan)\nKurikulum yang kami kembangkan ini mencakup 16 Sesi Pertemuan Penuh untuk satu semester pembelajaran Informatika Fase E. Dimulai dari fondasi Berpikir Komputasional, Algoritma Pemrograman dasar Python, Arsitektur Komputer dan Jaringan, hingga Proyek Kolaboratif terpadu."', italic=True, indent=0.35)
    add_para('"(Menjelaskan 4 Komponen Pembelajaran)\nGuna menjaga konsistensi mutu, kami menetapkan Standar Mutu Empat Komponen Wajib pada setiap pertemuan pembelajaran: Pertama, Presensi Kehadiran Terintegrasi untuk memantau kedisiplinan peserta didik; Kedua, Modul Pembelajaran Interaktif berupa halaman materi yang diperkaya video edukasi kontekstual; Ketiga, Forum Diskusi Kolaboratif untuk melatih kemampuan nalar kritis dan pemecahan masalah; Dan keempat, Lembar Kerja Peserta Didik (LKPD) sebagai instrumen unjuk kerja praktikum."', italic=True, indent=0.35)
    add_para('"(Menyorot Restrict Access Pertemuan 8 UTS)\nSalah satu fitur krusial Moodle yang kami terapkan adalah Pembatasan Akses Berbasis Waktu (Time-based Restrict Access). Pada sesi Pertemuan 8 Ujian Tengah Semester ini, akses materi terkunci secara otomatis hingga tanggal 19 Oktober 2026 tepat pukul 08:00 WIB. Mekanisme ini menjamin integritas jadwal evaluasi secara disiplin tanpa memerlukan pembukaan manual oleh pengajar."', italic=True, indent=0.35)
    add_para('"(Buka Halaman Gradebook Setup)\nKeunggulan Moodle paling signifikan dibandingkan platform kelas lainnya terletak pada Sistem Penilaian Berstandar Industri (Gradebook Calculation). Pada menu Pengaturan Buku Nilai ini, kami telah mengalibrasi pembobotan kategori secara presisi mencapai akumulasi total tepat 100%: Presensi 10%, Tugas LKPD 30%, Forum Diskusi 10%, UTS 20%, dan UAS 30%."', italic=True, indent=0.35)
    add_para('"(Buka Halaman Rubrik LKPD)\nTidak hanya itu, dalam menilai tugas vokasi, kami menerapkan Rubrik Penilaian Analitik Tiga Kriteria: Ketepatan Logika berbobot 40 poin, Kualitas dan Kerapian Kode berbobot 35 poin, serta Format Laporan dan Orisinalitas berbobot 25 poin. Dengan instrumen ini, proses asesmen berlangsung adil, akuntabel, dan bebas dari subjektivitas."', italic=True, indent=0.35)

    # SCENE 4
    add_h2("SCENE 4: SISI SISWA (STUDENT VIEW - PENGALAMAN BELAJAR INTERAKTIF VOKASI SMK)")
    add_para(" 09:30 – 13:00 (3,5 Menit)", bold_prefix="Estimasi Durasi:")
    add_para(" Screen Capture Moodle (Logout Akun Guru/Admin ➔ Login Akun Siswa 'siswa' / 'Siswa123!' ➔ Beranda Modern Tech ➔ Kursusku Bersih Tanpa Tombol Buat Kursus ➔ Materi 2 Video Responsif ➔ Form LKPD ➔ Materi Terkunci).", bold_prefix="Layout Layar:")

    add_para("", bold_prefix="[PANDUAN VISUAL & LANGKAH AKSI LAYAR]")
    add_para("1. Langkah Penting - Login Akun Siswa Murni: Lakukan Log Out dari akun sebelumnya. Pada halaman login, masukkan kredensial siswa murni: Username siswa (atau siswa_fahri) dan Password Siswa123!. Sorot avatar profil di pojok kanan atas yang kini bertuliskan Fahri Ramadhan (Siswa X RPL 1) dengan inisial FR.")
    add_para("2. Pembuktian Dynamic UI & Pembatasan Role Siswa: Sorot navbar atas: perlihatkan bahwa menu Administrasi situs sama sekali tidak muncul. Sorot pojok kanan atas: perlihatkan bahwa sakelar Mode Edit tidak ada. Buka menu Kursusku (/my/courses.php): perlihatkan bahwa tombol Buat kursus dan Mengelola kursus sama sekali tidak ada pada layar siswa. Ini membuktikan sistem hak akses (role permissions) Moodle telah terisolasi sempurna.")
    add_para("3. Eksplorasi Beranda & Kursusku Siswa: Tunjukkan Hero Section bertema teknologi vokasi SMK dan tombol aksi cepat 'Buka Kelas Informatika'. Pada halaman Kursusku, gerakkan kursor ke kartu kursus memperlihatkan Efek Hover Lift (-6px) melayang halus dan Dynamic Progress Bar bergradasi Electric Indigo to Emerald.")
    add_para("4. Eksplorasi Modul 2 dengan Video YouTube Responsif: Buka Materi 2. Tunjukkan video edukasi Berpikir Komputasional yang tersemat rapi (Responsive Video Wrapper) dan putar video selama beberapa detik.")
    add_para("5. Partisipasi Forum Diskusi & Pratinjau Rubrik LKPD: Buka Forum Diskusi. Buka LKPD 1 memperlihatkan pratinjau matriks rubrik transparan. Klik 'Tambahkan pengajuan' memperlihatkan form Multi-format Submission (teks daring & unggah berkas PDF).")
    add_para("6. Transparansi Pertemuan Terkunci: Tunjukkan topik Pertemuan 8 (UTS) dari sudut pandang siswa, menampilkan ikon gembok dan tanggal buka secara gamblang.")

    add_para("", bold_prefix="[NARASI LISAN PRESENTER]")
    add_para('"(Di Halaman Beranda dari Sudut Pandang Siswa Murni)\nSekarang, mari kita buktikan bagaimana sistem ini membatasi hak akses dan memberikan pengalaman belajar yang aman melalui Sisi Siswa. Saya telah melakukan log out dan masuk secara autentik menggunakan akun siswa bernama Fahri Ramadhan dari kelas X RPL 1."', italic=True, indent=0.35)
    add_para('"(Sorot Navbar & Halaman Kursusku yang Bersih)\nDapat kita saksikan bersama, sistem Dynamic Role Rendering Moodle berjalan sempurna. Pada akun siswa ini, menu Administrasi Situs dan sakelar Mode Edit sama sekali tidak ada. Begitu pula pada halaman Kursusku, siswa tidak memiliki tombol \'Buat kursus\' maupun hak mengelola sistem. Antarmuka siswa murni terisolasi hanya untuk keperluan belajar."', italic=True, indent=0.35)
    add_para('"(Sorot Hero Banner Beranda)\nSiswa disambut oleh antarmuka modern dengan Hero Section bertema teknologi vokasi SMK, memuat ringkasan Tiga Pilar Kejuruan dan tombol aksi cepat untuk langsung memulai belajar."', italic=True, indent=0.35)
    add_para('"(Buka Halaman Kursusku & Gerakkan Kursor)\nKetika siswa membuka menu Kursusku, nuansa interaktif semakin terasa: Header halaman dibalut banner bergaya portal teknologi, sementara kartu kursus dilengkapi Efek Hover Lift yang melayang dinamis saat disentuh kursor. Dilengkapi pula cover kelas berkualitas tinggi dan progress bar gamifikasi yang secara visual memotivasi siswa untuk terus menuntaskan setiap target pembelajaran."', italic=True, indent=0.35)
    add_para('"(Buka Materi 2 Video YouTube)\nSaat siswa mempelajari konsep, kami menghadirkan Fitur Multimedia Learning Wrapper pada modul Halaman Materi. Sebagaimana yang tampak pada Materi Pertemuan 2 ini, video pembelajaran YouTube mengenai Fondasi Berpikir Komputasional tersemat secara responsif. Siswa dapat memutar dan menyimak penjelasan audio visual secara langsung di dalam Moodle tanpa risiko terdistraksi oleh algoritma rekomendasi aplikasi luar."', italic=True, indent=0.35)
    add_para('"(Buka LKPD 1 dari Sudut Pandang Siswa)\nKetika siswa hendak mengerjakan lembar kerja praktikum, prinsip transparansi penilaian terwujud secara nyata. Siswa dapat membaca Matriks Rubrik Penilaian terlebih dahulu, sehingga mereka memahami standar kualitas apa yang harus dipenuhi untuk meraih poin maksimal 100."', italic=True, indent=0.35)
    add_para('"(Tunjukkan Form Pengumpulan Tugas)\nMelalui Fitur Multi-Format Submission, siswa diberikan kemudahan: Mereka dapat mengetikkan penjelasan ringkas pada kotak teks daring, sekaligus mengunggah berkas laporan formal format PDF atau DOCX melalui kotak unggah berkas yang terlindungi sistem validasi."', italic=True, indent=0.35)
    add_para('"Pengalaman belajar siswa ditutup dengan kepastian jadwal, di mana materi evaluasi yang terkunci menampilkan informasi tanggal buka secara gamblang. Rangkaian fitur ini membuktikan bahwa Moodle mampu menjadi ruang belajar digital yang ramah, mandiri, dan berpusat pada siswa SMK masa kini."', italic=True, indent=0.35)

    # SCENE 5
    add_h2("SCENE 5: REKAPITULASI PROGRES 7 MINGGU & PENUTUP (CLOSING)")
    add_para(" 13:00 – 15:00 (2 Menit)", bold_prefix="Estimasi Durasi:")
    add_para(" Tampilkan Tabel Rekapitulasi Progres 7 Pertemuan Pengembangan di Layar, lalu beralih ke Kamera Penuh Presenter (Full Face).", bold_prefix="Layout Layar:")

    add_para("", bold_prefix="[PANDUAN VISUAL & LANGKAH AKSI LAYAR]")
    add_para("1. Tampilkan Tabel Rekapitulasi Progres 7 Pertemuan Pengembangan LMS (Minggu 1 s/d Minggu 7).")
    add_para("2. Beralih ke kamera penuh presenter (Full Face) untuk penyampaian pesan penutup secara santun, berwibawa, dan penuh percaya diri.")

    add_para("", bold_prefix="[NARASI LISAN PRESENTER]")
    add_para('"(Sorot Tabel Rekapitulasi Progres)\nSeluruh rangkaian pengembangan LMS Informatika ini telah dikerjakan secara sistematis dan terdokumentasi rapi dalam tabel rekapitulasi progres selama tujuh siklus pengembangan terhitung mundur dari 13 Oktober 2026. Dimulai dari tahapan analisis pedagogis Kurikulum Merdeka, instalasi infrastruktur Moodle 4.5+ LTS, perancangan 16 pertemuan lengkap, hingga tahap penghalusan antarmuka modern dan verifikasi multi-role yang baru saja kita saksikan bersama."', italic=True, indent=0.35)
    add_para('"(Kamera Penuh Presenter)\nSebagai kesimpulan, proyek Learning Management System Informatika Kelas X Fase E ini telah membuktikan integrasi yang harmonis antara kekuatan filosofi Kurikulum Merdeka, keandalan teknis Moodle dari sisi Admin dan Guru, serta kenyamanan pengalaman belajar interaktif dari sisi Siswa."', italic=True, indent=0.35)
    add_para('"Saya mengucapkan terima kasih yang sebesar-besarnya kepada Dosen Pengampu kami, Ibu Ghea Chandra Surawan, M.Pd., atas bimbingan, arahan, dan inspirasi berharga yang telah dicurahkan sepanjang perkuliahan Learning Management System ini. Semoga karya sistem e-learning ini dapat memberikan kontribusi nyata bagi pengembangan teknologi pendidikan kejuruan di tanah air."', italic=True, indent=0.35)
    add_para('"Mohon maaf atas segala keterbatasan dalam penyampaian dan tutur kata saya. Terima kasih atas perhatian Ibu Dosen dan rekan-rekan sekalian. Wabillahi taufiq wal hidayah, Wassalamu’alaikum Warahmatullahi Wabarakatuh."', italic=True, indent=0.35)

    # ------------------------------------------
    # TABEL CUE CARD & TIMELINE
    # ------------------------------------------
    add_h1("RINGKASAN TIMELINE & CUE CARD PEREKAMAN")
    
    cue_data = [
        ("00:00 – 02:00", "Scene 1: Pembukaan & Urgensi", "Identitas Presenter, Pengantar LMS & Alasan Memilih Moodle 4.5+ LTS", "Kamera Penuh ➔ Grafis Identitas UNILA & Slide Judul"),
        ("02:00 – 05:30", "Scene 2: Sisi Administrator", "Demo XAMPP Control Panel, Direktori Dataroot, Versi Moodle 4.5 LTS & Audit Keamanan", "XAMPP Panel ➔ File Explorer ➔ Moodle Admin Notifications ➔ Security Report (Hijau)"),
        ("05:30 – 09:30", "Scene 3: Sisi Guru Pengampu", "Mode Edit ON, 16 Sesi Lengkap, Restrict Access, Gradebook 100%, Rubrik LKPD", "Kursus Informatika ➔ Edit Section ➔ Gradebook Setup ➔ Rubrik LKPD"),
        ("09:30 – 13:00", "Scene 4: Sisi Siswa SMK", "Login Siswa Murni, UI Bersih Tanpa Buat Kursus, Modul Video YouTube, Form LKPD", "Beranda Modern ➔ Kursusku ➔ Modul 2 Video ➔ Form Tugas LKPD"),
        ("13:00 – 15:00", "Scene 5: Rekapitulasi & Penutup", "Tabel Progres 7 Minggu Pengembangan & Salam Penutup", "Tabel Rekapitulasi Progres ➔ Kamera Penuh Presenter")
    ]
    tbl_cue = doc.add_table(rows=len(cue_data) + 1, cols=4)
    tbl_cue.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_cue, color="D0D0D0", sz="4", val="single")

    cue_headers = ["Menit Ke-", "Bagian / Scene", "Sudut Pandang / Fokus", "Aksi Layar Utama"]
    cue_widths = [Inches(1.2), Inches(1.8), Inches(1.8), Inches(1.7)]
    for j, h in enumerate(cue_headers):
        c = tbl_cue.cell(0, j)
        c.width = cue_widths[j]
        set_cell_margins(c, top=60, bottom=60, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    for i, row in enumerate(cue_data):
        for j in range(4):
            c = tbl_cue.cell(i + 1, j)
            c.width = cue_widths[j]
            set_cell_margins(c, top=50, bottom=50, left=100, right=100)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r = p.add_run(row[j])
            if j == 0:
                r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)

    doc.save(DOCX_OUTPUT_PATH)
    print("File DOCX berhasil disimpan!")

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    write_markdown_file()
    build_docx_file()
    print("Semua proses pembaruan naskah berhasil!")
