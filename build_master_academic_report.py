# -*- coding: utf-8 -*-
"""
Script Pembangun Master Dokumen Laporan Akademik Sistem SALUT
Menyatukan Laporan 1 s.d. 6 dengan Format Akademik Standar:
- Font: Times New Roman, 12 pt, Spasi 1.5, Rata Kanan-Kiri (Justified)
- Margin: 1 inci (2.54 cm) pada seluruh sisi
- Tangkapan layar nyata & realistis (bukan mockup kosong)
- Jumlah Halaman: ~35 s.d. 45 Halaman
Penulis: Wemvi Afrialdo (NPM 2413025052)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE_DIR = r"d:\proyek_applikasi"
APPS_DIR = os.path.join(BASE_DIR, "apps_sekolah")
SCREENSHOTS_DIR = os.path.join(APPS_DIR, "laporan_screenshots")
INSTALASI_IMG_DIR = os.path.join(APPS_DIR, "instalasi_images")
LOGO_PATH = os.path.join(BASE_DIR, "logo_salut.png")

OUTPUT_DOCX_MASTER = os.path.join(APPS_DIR, "Laporan_Lengkap_Sistem_SALUT_dan_Instalasi.docx")
OUTPUT_DOCX_COMPILATION = os.path.join(APPS_DIR, "Laporan_Lengkap_3_4_5_6.docx")
OUTPUT_DOCX_ROOT = os.path.join(BASE_DIR, "instalasi.docx")
OUTPUT_HTML = os.path.join(APPS_DIR, "Laporan_Lengkap_3_4_5_6.html")

def format_run(run, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(*color)

def add_p(doc, text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.5, indent=0.35, bold=False, italic=False):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if indent and align == WD_ALIGN_PARAGRAPH.JUSTIFY:
        p.paragraph_format.first_line_indent = Inches(indent)
    if text:
        r = p.add_run(text)
        format_run(r, bold=bold, italic=italic)
    return p

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.line_spacing = 1.2
    r = p.add_run(text)
    format_run(r, size_pt=14, bold=True, color=(0, 51, 102))
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.3
    r = p.add_run(text)
    format_run(r, size_pt=12.5, bold=True, color=(15, 23, 42))
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.3
    r = p.add_run(text)
    format_run(r, size_pt=12, bold=True, italic=True, color=(30, 41, 69))
    return p

def add_image_with_caption(doc, img_path, caption, width_in=5.2):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
    else:
        print(f"[Peringatan] Gambar tidak ditemukan: {img_path}")
        
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(12)
    r_cap = p_cap.add_run(caption)
    format_run(r_cap, size_pt=10, italic=True, color=(80, 80, 80))

def build_master_document():
    print("Mempersiapkan dokumen Word Master...")
    doc = docx.Document()
    
    # 1. Konfigurasi Margin (1 Inci sekeliling)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        header = section.header
        p_h = header.paragraphs[0]
        p_h.text = "Laporan Komprehensif Sistem SALUT | Universitas Lampung"
        p_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        format_run(p_h.runs[0], size_pt=9, italic=True, color=(128, 128, 128))
        
    # =========================================================================
    # HALAMAN COVER / JUDUL
    # =========================================================================
    p_cov_title = doc.add_paragraph()
    p_cov_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cov_title.paragraph_format.space_before = Pt(20)
    p_cov_title.paragraph_format.space_after = Pt(12)
    p_cov_title.paragraph_format.line_spacing = 1.3
    r1 = p_cov_title.add_run("LAPORAN KOMPREHENSIF PROGRES PENGEMBANGAN SISTEM SALUT\n(SISTEM ARSIP KELULUSAN & TRACER STUDY SMK)")
    format_run(r1, size_pt=15, bold=True, color=(0, 51, 102))
    
    p_cov_sub = doc.add_paragraph()
    p_cov_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cov_sub.paragraph_format.space_after = Pt(25)
    r2 = p_cov_sub.add_run("Disusun untuk Memenuhi Tugas Perkuliahan Mobile Programming & Web Terpadu\nProgram Studi Pendidikan Teknologi Informasi")
    format_run(r2, size_pt=12, italic=True, color=(70, 70, 70))
    
    # Logo SALUT di Cover
    if os.path.exists(LOGO_PATH):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(30)
        p_logo.add_run().add_picture(LOGO_PATH, width=Inches(2.2))
        
    # Identitas Penyusun
    p_id = doc.add_paragraph()
    p_id.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_id.paragraph_format.line_spacing = 1.3
    p_id.paragraph_format.space_after = Pt(45)
    
    r_dosen = p_id.add_run("Dosen Pengampu Mata Kuliah:\n")
    format_run(r_dosen, size_pt=11.5, bold=True)
    r_dosen_val = p_id.add_run("Ghea Chandra Surawan, M.Pd.\n\n")
    format_run(r_dosen_val, size_pt=12)
    
    r_penyusun = p_id.add_run("Disusun Oleh:\n")
    format_run(r_penyusun, size_pt=11.5, bold=True)
    r_nama = p_id.add_run("Wemvi Afrialdo\n")
    format_run(r_nama, size_pt=13, bold=True, color=(0, 51, 102))
    r_npm = p_id.add_run("NPM: 2413025052\n")
    format_run(r_npm, size_pt=12, bold=True)
    
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.line_spacing = 1.2
    r_inst = p_inst.add_run(
        "PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI\n"
        "JURUSAN PENDIDIKAN MATEMATIKA DAN ILMU PENGETAHUAN ALAM\n"
        "FAKULTAS KEGURUAN DAN ILMU PENDIDIKAN\n"
        "UNIVERSITAS LAMPUNG\n"
        "2026"
    )
    format_run(r_inst, size_pt=12, bold=True, color=(15, 23, 42))
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM
    # =========================================================================
    add_heading_1(doc, "BAB I\nPENDAHULUAN DAN GAMBARAN UMUM SISTEM SALUT")
    
    add_heading_2(doc, "1.1 Latar Belakang Masalah")
    add_p(doc, "Institusi Sekolah Menengah Kejuruan (SMK) memiliki karakteristik pendidikan yang berorientasi pada kesiapan kerja, kewirausahaan, serta kelanjutan studi ke jenjang pendidikan tinggi. Namun, dalam tata kelola administrasi kelulusan dan pemantauan karir lulusan, sebagian besar institusi pendidikan masih menghadapi tantangan operasional yang signifikan. Berkas kelulusan seperti Ijazah, Surat Keterangan Lulus (SKL), dan transkrip nilai akademik sering kali masih dikelola dalam bentuk fisik yang rentan mengalami kerusakan, pemalsuan, atau kehilangan dalam kurun waktu tertentu.")
    add_p(doc, "Di sisi lain, kebutuhan pelacakan jejak alumni (tracer study) menjadi instrumen evaluasi akreditasi dan pemutakhiran kurikulum yang sangat vital bagi SMK. Ketiadaan sistem pendataan yang terintegrasi secara digital menyebabkan pihak sekolah kesulitan memetakan tingkat keterserapan lulusan di Dunia Usaha dan Dunia Industri (DUDI), perguruan tinggi mitra, maupun sektor wirausaha mandiri. Siswa juga memiliki beragam sertifikat uji kompetensi kejuruan dan portofolio keahlian yang belum terakomodasi secara resmi ke dalam format Surat Keterangan Pendamping Ijazah (SKPI).")
    
    add_heading_2(doc, "1.2 Solusi yang Dikembangkan: Sistem SALUT")
    add_p(doc, "Untuk menjawab tantangan tersebut, dikembangkan sistem SALUT (Sistem Arsip Kelulusan dan Tracer Study Terpadu). SALUT dirancang sebagai ekosistem teknologi modern berbasis multi-platform yang menghubungkan pihak sekolah (administrator dan guru), siswa aktif tingkat akhir, serta alumni dalam satu kesatuan sistem informasi yang aman, cepat, dan transparan.")
    add_p(doc, "Sistem ini mengakomodasi tiga komponen utama pengembangan, yaitu:")
    add_p(doc, "1. Aplikasi Klien Mobile (Flutter): Antarmuka smartphone untuk siswa aktif dan alumni yang menyediakan layanan verifikasi status kelulusan dinamis, pengunggahan sertifikat kejuruan untuk penerbitan SKPI, pengunduhan berkas arsip legalisir digital, pengisian kuesioner tracer study, serta penerimaan notifikasi siaran real-time.", indent=0.5)
    add_p(doc, "2. Backend RESTful API Engine (Laravel 11): Server komputasi dan pemrosesan logika bisnis terpusat yang menangani otentikasi berbasis JSON Web Token (JWT), enkripsi kata sandi Bcrypt, validasi portofolio kejuruan, serta engine automasi cron scheduler untuk pemindahan status kelulusan secara otomatis.", indent=0.5)
    add_p(doc, "3. Portal Web Administrator (Modern Web Admin): Panel pengelolaan berbasis web responsif yang diperuntukkan bagi operator sekolah dan dewan guru untuk memantau grafik analitik sebaran siswa per jurusan SMK, verifikasi berkas ijazah, approval sertifikasi SKPI, dan rekapitulasi data tracer study.", indent=0.5)
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB II: LAPORAN 1 & 2 - INSTALASI DAN PERSIAPAN ENVIRONMENT
    # =========================================================================
    add_heading_1(doc, "BAB II\nLAPORAN 1 & 2: INSTALASI PERANGKAT LUNAK DAN PENGATURAN SISTEM PENGEMBANGAN APLIKASI MOBILE")
    
    add_p(doc, "Pengembangan aplikasi mobile berbasis cross-platform membutuhkan persiapan lingkungan kerja (development environment) yang matang dan terkonfigurasi dengan tepat. Pada tahap awal ini, dilakukan serangkaian instalasi piranti lunak fundamental yang mencakup Flutter SDK, Java Development Kit (JDK), Visual Studio Code beserta ekstensinya, Android Studio, Android SDK Command-line Tools, CMake, serta Android NDK.")
    
    # Step 1
    add_heading_2(doc, "2.1 Akses Dokumentasi Resmi Flutter SDK")
    add_p(doc, "Pada bagian ini, saya mengakses situs web dokumentasi resmi Flutter (docs.flutter.dev) untuk mengikuti prosedur instalasi standar yang direkomendasikan bagi sistem operasi Windows 64-bit.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_00.png"), "Gambar 2.1: Halaman dokumentasi instalasi resmi Flutter SDK pada peramban web.")
    
    # Step 2
    add_heading_2(doc, "2.2 Pengunduhan Paket Bundel Flutter SDK")
    add_p(doc, "Selanjutnya, saya mengunduh bundel instalasi Flutter SDK versi stabil terbaru (flutter_windows_3.47.6-stable.zip) melalui menu Install manually untuk sistem operasi Windows.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_01.png"), "Gambar 2.2: Proses pengunduhan berkas arsip Flutter SDK stable zip.")
    
    # Step 3
    add_heading_2(doc, "2.3 Konfigurasi System Environment Variables")
    add_p(doc, "Setelah mengekstrak file Flutter SDK, saya mendaftarkan direktori instalasinya, yaitu C:\\Fluttersetup\\flutter_windows_3.47.4-stable\\flutter\\bin, ke dalam System Environment Variables. Langkah ini dilakukan agar perintah-perintah eksekusi Flutter dapat diakses secara global melalui command line interface atau terminal di VS Code.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_02.png"), "Gambar 2.3: Pendaftaran path binary Flutter ke dalam System Environment Variables Windows.")
    
    # Step 4
    add_heading_2(doc, "2.4 Verifikasi Deteksi Flutter Melalui Command Prompt")
    add_p(doc, "Untuk memastikan instalasi Flutter SDK berhasil dan jalurnya terbaca oleh sistem, saya menjalankan perintah flutter --version melalui Command Prompt. Hasilnya menunjukkan bahwa sistem telah berhasil mendeteksi Flutter versi 3.47.6 beserta kelengkapannya, termasuk Dart versi 3.13.5.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_03.png"), "Gambar 2.4: Hasil eksekusi perintah flutter --version pada Command Prompt.")
    
    # Step 5
    add_heading_2(doc, "2.5 Pengunduhan Java Development Kit (JDK 21)")
    add_p(doc, "Pada tahap awal persiapan lingkungan kerja, saya mengunduh Java Development Kit (JDK) versi 21.0.2 berformat zip khusus untuk sistem operasi Windows 64-bit melalui situs resminya guna mendukung kompilasi proyek Android berbasis Gradle.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_04.png"), "Gambar 2.5: Pengunduhan paket Java Development Kit (JDK 21) Windows x64.")
    
    # Step 6
    add_heading_2(doc, "2.6 Verifikasi Pendaftaran Jalur JDK")
    add_p(doc, "Setelah mengekstrak dan mendaftarkan jalur JDK ke dalam sistem (Environment Variables), saya memverifikasi instalasinya melalui terminal VS Code menggunakan perintah java -version. Hasilnya menunjukkan bahwa OpenJDK versi 21.0.2 telah berhasil terbaca oleh sistem.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_05.png"), "Gambar 2.6: Verifikasi eksekusi java -version di terminal lingkungan kerja.")
    
    # Step 7 & 8
    add_heading_2(doc, "2.7 Pemasangan Ekstensi Flutter & Dart pada Visual Studio Code")
    add_p(doc, "Pada tahap persiapan teks editor, saya memasang ekstensi resmi Flutter di dalam Visual Studio Code agar editor memiliki dukungan penuh untuk menulis kode, navigasi widget, hot reload, dan proses debugging aplikasi secara interaktif.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_06.png"), "Gambar 2.7: Pemasangan ekstensi Flutter resmi di Visual Studio Code.")
    add_p(doc, "Selain ekstensi Flutter, saya juga memastikan ekstensi Dart telah terinstal di Visual Studio Code, yang berfungsi sebagai penyedia dukungan sintaks dasar, penyorotan kode, dan analisis statis bahasa pemrograman Dart.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_07.png"), "Gambar 2.8: Pemasangan ekstensi Dart di Visual Studio Code.")
    
    # Step 9 & 10
    add_heading_2(doc, "2.8 Konfigurasi Android SDK Build Tools, CMake, dan Android NDK")
    add_p(doc, "Pada tahap konfigurasi Android Studio, saya membuka menu SDK Manager dan masuk ke tab SDK Tools untuk memastikan bahwa komponen perakit dasar seperti Android SDK Command-line Tools dan CMake sudah berstatus terinstal (Installed).")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_08.png"), "Gambar 2.9: Pengaturan Android SDK Command-line Tools dan CMake pada SDK Manager.")
    add_p(doc, "Pada tahap penyelesaian masalah (troubleshooting) akibat kegagalan build dari Gradle, saya menginstal komponen tambahan yaitu Android NDK (Side by side) versi 28.2.13676358 secara manual melalui SDK Manager.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_09.png"), "Gambar 2.10: Pemasangan Android NDK Side by side pada Android Studio.")
    
    # Step 11
    add_heading_2(doc, "2.9 Validasi Kesiapan Sistem Menggunakan Flutter Doctor")
    add_p(doc, "Sebagai tahap validasi akhir setelah seluruh proses instalasi selesai, saya menjalankan perintah flutter doctor pada Command Prompt. Hasilnya menunjukkan indikator centang hijau pada komponen utama pengembangan mobile seperti Flutter SDK dan Android toolchain, yang menandakan lingkungan pengembangan siap digunakan. Terdapat satu peringatan (tanda seru) pada bagian Visual Studio karena instalasi yang tidak lengkap. Namun, isu ini sengaja diabaikan karena fokus utama proyek pada mata kuliah ini ditujukan untuk pengembangan aplikasi mobile (Android), bukan aplikasi desktop berbasis Windows.")
    add_image_with_caption(doc, os.path.join(INSTALASI_IMG_DIR, "img_10.png"), "Gambar 2.11: Hasil diagnosa lengkap flutter doctor pada Command Prompt.")
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB III: LAPORAN 3 - PENGEMBANGAN BACKEND API DAN BASIS DATA
    # =========================================================================
    add_heading_1(doc, "BAB III\nLAPORAN 3: PENGEMBANGAN BACKEND RESTFUL API DAN BASIS DATA RELASIONAL")
    
    add_heading_2(doc, "3.1 Konfigurasi Lingkungan Backend (Laravel 11)")
    add_p(doc, "Pondasi server dibangun menggunakan framework Laravel 11 dengan orientasi arsitektur RESTful API murni. Konfigurasi server diatur melalui berkas .env untuk mendefinisikan port lokal (http://127.0.0.1:8000), koneksi basis data relasional MySQL dengan basis data salut_db, serta secret key otentikasi JWT (JSON Web Token).")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_01_env.png"), "Gambar 3.1: Konfigurasi file .env untuk koneksi database MySQL dan JWT secret.")
    
    add_heading_2(doc, "3.2 Pemodelan Relasional dan Model Eloquent")
    add_p(doc, "Dalam arsitektur basis data relasional SALUT, entitas pengguna dimodelkan melalui kelas User.php yang mengimplementasikan Tymon\\JWTAuth\\Contracts\\JWTSubject. Model ini mendefinisikan atribut sensitif yang diisi secara massal ($fillable) seperti name, email, nisn, password, role, class_name, major, dan graduation_status. Relasi data dibangun menggunakan relasi one-to-many (hasMany) menuju model StudentSkill dan relasi one-to-one (hasOne) menuju model TracerStudy.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_02_migration_model.png"), "Gambar 3.2: Implementasi Model User Eloquent dan relasi antar tabel.")
    
    add_heading_2(doc, "3.3 Visualisasi Struktur Basis Data di phpMyAdmin")
    add_p(doc, "Struktur tabel diuji dan dimonitor melalui antarmuka phpMyAdmin. Tabel-tabel utama yang terbentuk antara lain users, student_skills, graduation_schedules, tracer_studies, rapor, dan prestasi. Setiap tabel memiliki relasi foreign key berintegritas tinggi untuk menjamin konsistensi data transaksi akademik.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_03_phpmyadmin.png"), "Gambar 3.3: Struktur tabel basis data salut_db pada phpMyAdmin.")
    
    add_heading_2(doc, "3.4 Definisi Rute RESTful API (routes/api.php)")
    add_p(doc, "Routing API dipetakan secara modular pada berkas routes/api.php. Endpoint dipisahkan menjadi dua kelompok besar:")
    add_p(doc, "1. Rute Publik: POST /api/login untuk otentikasi kredensial awal.", indent=0.5)
    add_p(doc, "2. Rute Terproteksi Middleware auth:api: GET /api/me, POST /api/change-password, GET/POST /api/skills, GET /api/arsip, dan POST /api/tracer-study. Selain itu, terdapat grup khusus administrator (/api/admin) untuk monitoring statistik analitik kejuruan dan validasi arsip seluruh alumni.", indent=0.5)
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_04_routes_api.png"), "Gambar 3.4: Pemetaan rute RESTful API dengan proteksi JWT Bearer Middleware.")
    
    add_heading_2(doc, "3.5 Pengujian Endpoint API Login Menggunakan Postman")
    add_p(doc, "Untuk memvalidasi keandalan backend, dilakukan uji penetrasi endpoint POST /api/login menggunakan perkakas pengujian API (Postman / Thunder Client). Permintaan otentikasi dengan identifier NISN 1001 dan kata sandi valid menghasilkan respons HTTP 200 OK dalam format JSON yang mengembalikan token JWT bertipe Bearer beserta identitas peran (role) pengguna.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_05_api_testing.png"), "Gambar 3.5: Hasil pengujian API login dengan pengembalian token JWT (200 OK).")
    
    add_heading_2(doc, "3.6 Manajemen Repositori Backend ke GitHub")
    add_p(doc, "Seluruh kode sumber backend didokumentasikan dan disinkronkan ke dalam repositori remote GitHub menggunakan Git Version Control. Perintah git commit dan git push origin main memastikan seluruh modul server tercatat dalam riwayat pengembangan yang rapi.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_06_git_push_backend.png"), "Gambar 3.6: Eksekusi git push backend ke repositori remote GitHub.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan3_07_github_backend.png"), "Gambar 3.7: Tampilan repositori kode backend terkelola rapi pada remote GitHub.")
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB IV: LAPORAN 4 - FRONTEND MOBILE & DYNAMIC ROLE LOGIC
    # =========================================================================
    add_heading_1(doc, "BAB IV\nLAPORAN 4: PENGEMBANGAN FRONTEND MOBILE FLUTTER DAN LOGIKA KONTROL PERAN DINAMIS")
    
    add_heading_2(doc, "4.1 Arsitektur Antarmuka Mobile (Flutter 3.x)")
    add_p(doc, "Aplikasi klien mobile dibangun menggunakan framework Flutter 3.x yang mengadopsi filosofi desain visual Cyber-Academic Elite (Latar belakang Deep Obsidian #0A0F1D, kartu kaca buram frosted glass, tipografi kontras tinggi, dan logo resmi SALUT beresolusi tinggi tanpa latar kotak kaku). Sistem juga dilengkapi dengan Dual-Theme Engine yang memungkinkan pengguna berganti secara instan ke mode terang (Apple-Style Clean Pearl Slate #F8FAFC).")
    
    add_heading_2(doc, "4.2 Kode Antarmuka Login (login_page.dart)")
    add_p(doc, "Halaman login dirancang secara reaktif menggunakan widget StatefulWidget dengan validasi formulir terpadu. Pengguna dapat masuk menggunakan kombinasi NISN/Email dan kata sandi. Terdapat tombol pemilih tema cerdas (theme toggle button) di pojok kanan atas layar.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_01_login_page_code.png"), "Gambar 4.1: Struktur kode antarmuka halaman login pada login_page.dart.")
    
    add_heading_2(doc, "4.3 Integrasi HTTP Client Dio & JWT Keystore Interceptor")
    add_p(doc, "Komunikasi data antara Flutter dan server Laravel dikelola oleh modul ApiService berbasis Dio. Modul ini menyuntikkan interceptor khusus yang secara otomatis membaca token JWT dari media penyimpanan terenkripsi Android Keystore (FlutterSecureStorage) dan memasukkannya ke dalam header Authorization: Bearer <token> pada setiap transaksi HTTP.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_02_api_service_code.png"), "Gambar 4.2: Implementasi HTTP Client Dio dan Interceptor token JWT.")
    
    add_heading_2(doc, "4.4 Tampilan Antarmuka Halaman Login Mobile")
    add_p(doc, "Tampilan login pada layar perangkat smartphone menampilkan emblem logo resmi transparan SALUT yang melayang dengan pendaran cahaya biru cyan halus, lencana identitas PORTAL RESMI AKADEMIK & ALUMNI, serta formulir masukan dengan batas berpendar.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_03_login_mobile_app.png"), "Gambar 4.3: Tampilan antarmuka login mobile konsep Cyber-Academic Elite.")
    
    add_heading_2(doc, "4.5 Dashboard Siswa Aktif (Kelas X - XII)")
    add_p(doc, "Ketika akun siswa aktif masuk ke dalam sistem, dashboard secara cerdas menyesuaikan menu yang relevan bagi siswa yang masih menempuh pendidikan. Kartu identitas siswa menampilkan lencana hijau SISWA AKTIF - XII TKJ 1, menu Portofolio SKPI untuk mengajukan sertifikasi kejuruan, tabungan nilai rapor semester 1 s.d. 5, jadwal kelulusan, serta pengumuman batas waktu validasi berkas.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_04_dashboard_siswa_app.png"), "Gambar 4.4: Tampilan antarmuka Dashboard untuk peran Siswa Aktif.")
    
    add_heading_2(doc, "4.6 Dashboard Alumni (Kelulusan Terbit)")
    add_p(doc, "Sebaliknya, saat alumni yang telah dinyatakan lulus melakukan login, antarmuka dashboard bertransformasi menampilkan lencana ungu ALUMNI ANGKATAN 2024. Menu administrasi dialihkan menjadi pusat dokumen digital kelulusan seperti pengunduhan Ijazah resmi terenkripsi, Surat Keterangan Lulus (SKL), pengisian kuesioner Tracer Study alumni, dan info kemitraan industri DUDI.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_05_dashboard_alumni_app.png"), "Gambar 4.5: Tampilan antarmuka Dashboard untuk peran Alumni.")
    
    add_heading_2(doc, "4.7 Logika Kontrol Peran Dinamis (Role Dynamic Logic)")
    add_p(doc, "Pembeda tampilan antara siswa aktif dan alumni diatur melalui kondisional rendering pada DashboardController dan GetX state management. Sistem memeriksa atribut role dan graduation_status pada payload token pengguna untuk menentukan komponen antarmuka yang akan dirender secara dinamis tanpa perlu merilis aplikasi terpisah.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_06_role_logic_code.png"), "Gambar 4.6: Implementasi logika percabangan peran pada kode sumber Flutter.")
    
    add_heading_2(doc, "4.8 Repositori Frontend Mobile ke GitHub")
    add_p(doc, "Seluruh aset dan kode antarmuka Flutter disinkronkan ke remote repository GitHub untuk menjaga kesinambungan kolaborasi dan riwayat versi aplikasi.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_07_git_push_frontend.png"), "Gambar 4.7: Eksekusi git push kode frontend Flutter ke GitHub.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan4_08_github_frontend.png"), "Gambar 4.8: Tampilan repositori direktori Flutter apps_sekolah di GitHub.")
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB V: LAPORAN 5 - MANAJEMEN PORTOFOLIO SKPI & ARSIP DIGITAL
    # =========================================================================
    add_heading_1(doc, "BAB V\nLAPORAN 5: MANAJEMEN PORTOFOLIO SISWA, VALIDASI SKPI, DAN PENGARSIPAN DIGITAL")
    
    add_heading_2(doc, "5.1 Urgensi Portofolio SKPI bagi Siswa SMK")
    add_p(doc, "Surat Keterangan Pendamping Ijazah (SKPI) merupakan dokumen resmi rekam jejak kompetensi yang memuat capaian pembelajaran dan sertifikasi keahlian siswa SMK di luar ijazah formal. Pada Laporan 5, dikembangkan modul portofolio kejuruan mandiri yang memfasilitasi siswa untuk mengunggah sertifikat uji kompetensi BNSP, sertifikasi industri mitra (MikroTik, Cisco), serta kejuaraan teknologi.")
    
    add_heading_2(doc, "5.2 Migrasi Basis Data Portofolio (student_skills)")
    add_p(doc, "Tabel student_skills dirancang dengan skema atribut yang mencakup user_id (foreign key berelasi ke users), skill_name, certificate_no, issuer, document_path (tautan berkas sertifikat digital), dan status persetujuan berstatus enum ('pending', 'approved', 'rejected').")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_01_migration_skpi.png"), "Gambar 5.1: Berkas migrasi database untuk tabel portofolio student_skills.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_02_phpmyadmin_skpi.png"), "Gambar 5.2: Struktur tabel student_skills pada antarmuka phpMyAdmin.")
    
    add_heading_2(doc, "5.3 Controller Manajemen Skill & Validasi Guru")
    add_p(doc, "Pada sisi server, dibangun SkillController.php dengan endpoint komprehensif: index() untuk mengambil daftar portofolio terfilter milik siswa, store() untuk menangani pengunggahan berkas bukti sertifikasi, serta verify() yang memungkinkan dewan guru atau validator memberikan status validasi Approved atau Rejected disertai catatan koreksi.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_03_skill_controller.png"), "Gambar 5.3: Implementasi logika pengajuan dan verifikasi keahlian pada SkillController.php.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_04_api_skills_test.png"), "Gambar 5.4: Pengujian endpoint API pengajuan sertifikasi pada Postman.")
    
    add_heading_2(doc, "5.4 Antarmuka Halaman Portofolio Mobile (skills_page.dart)")
    add_p(doc, "Pada aplikasi mobile, siswa disajikan antarmuka visual daftar sertifikat yang telah diajukan beserta status verifikasinya. Sertifikat yang berstatus APPROVED ditandai dengan lencana hijau neon dan otomatis terdaftar ke dalam lampiran cetak SKPI resmi, sedangkan sertifikat yang masih menunggu evaluasi ditandai dengan lencana kuning PENDING.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_05_skills_page_code.png"), "Gambar 5.5: Kode antarmuka Flutter untuk halaman manajemen portofolio keahlian.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_06_skills_mobile_app.png"), "Gambar 5.6: Tampilan antarmuka mobile daftar portofolio keahlian SKPI siswa.")
    
    add_heading_2(doc, "5.5 Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)")
    add_p(doc, "Pusat arsip digital menyediakan repositori mandiri bagi alumni untuk mengunduh dokumen kelulusan resmi dalam format PDF beresolusi tinggi yang telah dilengkapi barcode verifikasi keabsahan. Dokumen mencakup Ijazah SMK Negeri 1 Teladan, Surat Keterangan Lulus (SKL), Transkrip Nilai Akademik Lengkap, dan SKHUN.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_07_arsip_mobile_app.png"), "Gambar 5.7: Tampilan antarmuka pengunduhan berkas arsip kelulusan digital.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan5_08_git_push.png"), "Gambar 5.8: Riwayat commit dan push modul Laporan 5 ke repositori GitHub.")
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB VI: LAPORAN 6 - AUTOMATION, FCM, TRACER, & WEB ADMIN SMK
    # =========================================================================
    add_heading_1(doc, "BAB VI\nLAPORAN 6: OTOMATISASI KELULUSAN, PUSH NOTIFICATION FCM, TRACER STUDY, DAN ANALITIK WEB ADMIN")
    
    add_heading_2(doc, "6.1 Layanan Notifikasi Push Real-Time (Firebase Cloud Messaging)")
    add_p(doc, "Untuk memastikan pengumuman kelulusan dan agenda tracer study tersampaikan secara instan ke genggaman alumni, sistem mengintegrasikan layanan Firebase Cloud Messaging (FCM). Modul FcmService pada Flutter mengelola pendaftaran token unik perangkat di Android Keystore dan menangani event onMessage saat aplikasi berjalan di foreground maupun background.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_01_fcm_service_code.png"), "Gambar 6.1: Implementasi FcmService untuk integrasi notifikasi push Firebase.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_02_fcm_notification_app.png"), "Gambar 6.2: Tampilan bilah notifikasi push broadcast kelulusan pada smartphone siswa.")
    
    add_heading_2(doc, "6.2 Engine Otomatisasi Kelulusan Berbasis Artisan Command")
    add_p(doc, "Untuk meniadakan proses manual pemindahan status ratusan siswa saat tanggal kelulusan tiba, dibangun custom command Laravel Artisan: php artisan students:promote-alumni. Command ini memeriksa tanggal kelulusan resmi pada tabel graduation_schedules; jika waktu pengumuman telah tercapai, sistem secara otomatis mengubah role siswa kelas XII menjadi alumni dan memicu pengiriman notifikasi broadcast kelulusan secara massal.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_03_cron_promote_code.png"), "Gambar 6.3: Implementasi logika penjadwalan otomatis pada PromoteAlumniCommand.php.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_04_cron_execution_terminal.png"), "Gambar 6.4: Log terminal eksekusi otomatisasi kelulusan 248 siswa kelas XII.")
    
    add_heading_2(doc, "6.3 Manajemen Keamanan Akun: Modul Ubah Kata Sandi Mandiri")
    add_p(doc, "Pengguna diberikan kendali penuh atas keamanan akun mereka melalui modul ganti kata sandi mandiri di aplikasi mobile. Sistem memvalidasi kesesuaian kata sandi lama, memverifikasi panjang kata sandi baru minimal 8 karakter, dan menyimpannya ke database dengan algoritma pengacakan satu arah Bcrypt.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_05_change_password_code.png"), "Gambar 6.5: Implementasi controller otentikasi untuk fitur ganti kata sandi.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_06_change_password_app.png"), "Gambar 6.6: Tampilan antarmuka formulir pengubahan kata sandi mandiri di HP.")
    
    add_heading_2(doc, "6.4 Implementasi Kuesioner Tracer Study Alumni")
    add_p(doc, "Alumni dapat mengisi kuesioner pelacakan karir secara periodik melalui form responsif di mobile. Parameter yang dikumpulkan mencakup status karir (Bekerja di Industri, Kuliah di PTN/PTS, Wirausaha, atau Mencari Kerja), nama instansi/perusahaan, estimasi pendapatan bulanan, serta tingkat keselarasan ilmu kejuruan SMK dengan pekerjaan saat ini.")
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_07_tracer_study_app.png"), "Gambar 6.7: Antarmuka formulir kuesioner pelacakan karir alumni (Tracer Study).")
    
    add_heading_2(doc, "6.5 Dashboard Web Administrator & Analitik Kejuruan SMK")
    add_p(doc, "Pihak manajemen sekolah dan dewan guru dibekali portal Web Administrator canggih yang berjalan dengan konsep visual Cyber-Academic Dark. Dashboard ini mengintegrasikan pustaka Chart.js secara lokal (offline-ready) untuk menyajikan grafik visual analitik kejuruan SMK Negeri 1 Teladan:")
    add_p(doc, "1. Grafik Batang Siswa per Jurusan: Menampilkan distribusi riil siswa di jurusan Teknik Komputer & Jaringan (X TKJ 1, X TKJ 2, XI TKJ 1, XI TKJ 2), Rekayasa Perangkat Lunak (XII RPL 1), dan Multimedia (XII MM 1).", indent=0.5)
    add_p(doc, "2. Grafik Donat Sebaran Tracer Study: Menunjukkan persentase alumni yang telah terserap di industri DUDI (62%), melanjutkan kuliah di perguruan tinggi (24%), wirausaha mandiri (10%), dan proses seleksi kerja (4%).", indent=0.5)
    add_p(doc, "3. Kartu Top Perguruan Tinggi & Top Industri: Menyajikan daftar institusi favorit alumni seperti Universitas Lampung (Unila), Institut Teknologi Sumatera (ITERA), Politeknik Negeri Lampung (Polinela), serta mitra industri utama seperti PT Telkom Indonesia Tbk, PT Astra Honda Motor, dan GoTo.", indent=0.5)
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_08_webadmin_smk_analytics.png"), "Gambar 6.8: Tampilan Dashboard Web Administrator Analitik Kejuruan SMK Negeri 1 Teladan.", width_in=5.8)
    add_image_with_caption(doc, os.path.join(SCREENSHOTS_DIR, "laporan6_09_git_push_final.png"), "Gambar 6.9: Eksekusi git push milestone final v1.0.0 ke repositori GitHub.")
    
    doc.add_page_break()
    
    # =========================================================================
    # BAB VII: KESIMPULAN & REKOMENDASI
    # =========================================================================
    add_heading_1(doc, "BAB VII\nKESIMPULAN DAN REKOMENDASI PENGEMBANGAN")
    
    add_heading_2(doc, "7.1 Kesimpulan Proyek")
    add_p(doc, "Berdasarkan seluruh tahapan perancangan, instalasi, pengembangan, dan pengujian sistem SALUT (Sistem Arsip Kelulusan dan Tracer Study Terpadu) dari Laporan 1 hingga Laporan 6, dapat ditarik beberapa kesimpulan penting sebagai berikut:")
    add_p(doc, "1. Ekosistem Multi-Platform Berhasil Diintegrasikan: Integrasi antara aplikasi mobile Flutter, backend RESTful API Laravel 11, dan portal Web Administrator berbasis Chart.js berjalan dengan harmonis dan stabil tanpa adanya konflik dependensi.", indent=0.5)
    add_p(doc, "2. Keamanan dan Kendali Peran Terjamin: Protokol otentikasi berbasis JSON Web Token (JWT) yang disimpan di Android Keystore berhasil melindungi data akademik sensitif dan menerapkan kontrol akses dinamis (RBAC) antara siswa aktif dan alumni secara instan.", indent=0.5)
    add_p(doc, "3. Efisiensi Pengelolaan Kelulusan & SKPI: Fitur otomatisasi cron scheduler mampu meniadakan proses manual promosi kelulusan tahunan, sementara modul portofolio kejuruan mempermudah verifikasi capaian kompetensi siswa untuk pencetakan SKPI resmi.", indent=0.5)
    add_p(doc, "4. Pelacakan Alumni yang Terukur: Fasilitas kuesioner tracer study dan visualisasi analitik grafik di web admin memberikan wawasan berharga bagi sekolah untuk mengevaluasi mutu kurikulum kejuruan terhadap kebutuhan dunia kerja nyata.", indent=0.5)
    
    add_heading_2(doc, "7.2 Rekomendasi Pengembangan Selanjutnya")
    add_p(doc, "Untuk meningkatkan fungsionalitas sistem SALUT di masa depan, diajukan beberapa rekomendasi pengembangan lanjutan:")
    add_p(doc, "1. Integrasi Digital Signature (Tanda Tangan Elektronik): Penerapan sertifikat digital tersertifikasi BSrE (Balai Sertifikasi Elektronik) pada berkas ijazah dan SKL PDF untuk legalisasi dokumen digital secara hukum nasional.", indent=0.5)
    add_p(doc, "2. Portal Lowongan Kerja Eksklusif Mitra DUDI: Penambahan fitur bursa kerja khusus (BKK) di mana perusahaan mitra industri dapat langsung memposting lowongan pekerjaan dan menyaring kandidat alumni berdasarkan portofolio SKPI mereka.", indent=0.5)
    add_p(doc, "3. Analisis Prediktif Karir Berbasis Machine Learning: Penggunaan algoritma kecerdasan buatan untuk merekomendasikan jenjang karir atau program studi perguruan tinggi yang paling cocok bagi siswa berdasarkan rekam jejak nilai rapor dan sertifikasi keahlian yang dimiliki.", indent=0.5)
    
    # Simpan ke beberapa file tujuan
    print(f"Menyimpan master docx ke {OUTPUT_DOCX_MASTER}...")
    doc.save(OUTPUT_DOCX_MASTER)
    
    print(f"Menyimpan kompilasi docx ke {OUTPUT_DOCX_COMPILATION}...")
    doc.save(OUTPUT_DOCX_COMPILATION)
    
    print(f"Menyimpan ke root repositori: {OUTPUT_DOCX_ROOT}...")
    doc.save(OUTPUT_DOCX_ROOT)
    
    print("=== Seluruh Dokumen Laporan Master Berhasil Disusun & Disimpan ===")

if __name__ == "__main__":
    build_master_document()
