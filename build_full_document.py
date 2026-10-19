# -*- coding: utf-8 -*-
"""
Script Penyusun Dokumen Lengkap Gabungan Laporan 3, 4, 5, dan 6 (SALUT)
Standar Akademik Lengkap: Cover, Daftar Isi/Struktur Bab, Pembahasan Mendalam,
32 Gambar Screenshot Beresolusi Tinggi, Tabel Analisis, dan Kesimpulan.
Output:
  - Laporan_3_dan_4.docx & Laporan_Lengkap_3_4_5_6.docx
  - Laporan_3_dan_4.html & Laporan_Lengkap_3_4_5_6.html
  - Laporan_3_dan_4.doc
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"d:\proyek_applikasi\apps_sekolah"
IMG_DIR = os.path.join(BASE_DIR, "laporan_screenshots")

DOCX_PRIMARY = os.path.join(BASE_DIR, "Laporan_3_dan_4.docx")
DOCX_FULL = os.path.join(BASE_DIR, "Laporan_Lengkap_3_4_5_6.docx")
HTML_PRIMARY = os.path.join(BASE_DIR, "Laporan_3_dan_4.html")
HTML_FULL = os.path.join(BASE_DIR, "Laporan_Lengkap_3_4_5_6.html")
DOC_PRIMARY = os.path.join(BASE_DIR, "Laporan_3_dan_4.doc")

def set_para(p, name='Times New Roman', size_pt=12, bold=False, italic=False, color_rgb=(0,0,0), space_after_pt=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after_pt)
    p.paragraph_format.line_spacing = line_spacing
    for r in p.runs:
        r.font.name = name
        r.font.size = Pt(size_pt)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = RGBColor(*color_rgb)

def add_title(doc, text):
    p = doc.add_paragraph()
    set_para(p, name='Times New Roman', size_pt=16, bold=True, color_rgb=(0, 51, 102), space_after_pt=10, line_spacing=1.2, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 51, 102)
    return p

def add_h1(doc, text):
    p = doc.add_paragraph()
    set_para(p, name='Times New Roman', size_pt=14, bold=True, color_rgb=(0, 51, 102), space_after_pt=10, line_spacing=1.2, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 51, 102)
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    set_para(p, name='Times New Roman', size_pt=12, bold=True, color_rgb=(20, 30, 60), space_after_pt=4, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.LEFT)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    return p

def add_h3(doc, text):
    p = doc.add_paragraph()
    set_para(p, name='Times New Roman', size_pt=12, bold=True, italic=True, color_rgb=(40, 40, 40), space_after_pt=3, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.LEFT)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.italic = True
    return p

def add_body(doc, text):
    p = doc.add_paragraph()
    set_para(p, name='Times New Roman', size_pt=12, bold=False, color_rgb=(0, 0, 0), space_after_pt=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p

def add_bullet(doc, bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.3
    r1 = p.add_run(bold_prefix + ": ")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r2 = p.add_run(text)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    return p

def add_img(doc, img_filename, caption_text, width_inches=6.0):
    img_path = os.path.join(IMG_DIR, img_filename)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(10)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(90, 90, 90)
    else:
        print(f"Warning: File {img_path} tidak ditemukan!")

def build_full_docx():
    print("Membangun dokumen Word komprehensif (Laporan 3, 4, 5, 6)...")
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        header = section.header
        p_head = header.paragraphs[0]
        p_head.text = "Laporan Progres Lengkap Sistem SALUT | Universitas Lampung"
        p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_head.runs[0].font.name = 'Times New Roman'
        p_head.runs[0].font.size = Pt(9)
        p_head.runs[0].font.italic = True
        p_head.runs[0].font.color.rgb = RGBColor(128, 128, 128)

    # =========================================================================
    # HALAMAN COVER / JUDUL
    # =========================================================================
    add_title(doc, "LAPORAN KOMPREHENSIF PROGRES PENGEMBANGAN SISTEM SALUT\n(SISTEM ARSIP KELULUSAN & TRACER STUDY SMK)")
    
    p_sub = doc.add_paragraph()
    set_para(p_sub, name='Times New Roman', size_pt=12, bold=True, color_rgb=(80, 80, 80), space_after_pt=24, line_spacing=1.3, align=WD_ALIGN_PARAGRAPH.CENTER)
    p_sub.add_run("Disusun untuk Memenuhi Tugas Pengembangan Aplikasi Perangkat Bergerak (Mobile) & Web Terpadu\nProgram Studi Pendidikan Teknologi Informasi - Universitas Lampung")
    
    # Box Identitas
    table = doc.add_table(rows=5, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    id_data = [
        ("Nama Mahasiswa / Pengembang", ": Wemvi Afrialdo"),
        ("Nomor Pokok Mahasiswa (NPM)", ": 2413025052"),
        ("Program Studi", ": Pendidikan Teknologi Informasi (PTI)"),
        ("Fakultas / Universitas", ": FKIP / Universitas Lampung"),
        ("Cakupan Laporan", ": Laporan 3, Laporan 4, Laporan 5, dan Laporan 6 (Full Cycle)"),
    ]
    for idx, (label, val) in enumerate(id_data):
        row = table.rows[idx]
        cell_l = row.cells[0]
        cell_v = row.cells[1]
        cell_l.width = Inches(2.8)
        cell_v.width = Inches(3.8)
        cell_l.paragraphs[0].text = label
        cell_v.paragraphs[0].text = val
        cell_l.paragraphs[0].runs[0].font.bold = True
        for c in (cell_l, cell_v):
            c.paragraphs[0].paragraph_format.line_spacing = 1.3
            c.paragraphs[0].paragraph_format.space_after = Pt(4)
            c.paragraphs[0].runs[0].font.name = 'Times New Roman'
            c.paragraphs[0].runs[0].font.size = Pt(11)
            
    doc.add_page_break()

    # =========================================================================
    # BAB I: PENDAHULUAN
    # =========================================================================
    add_h1(doc, "BAB I\nPENDAHULUAN DAN ARSITEKTUR SISTEM")
    add_h2(doc, "1.1 Latar Belakang Proyek SALUT")
    add_body(doc,
        "Sekolah Menengah Kejuruan (SMK) dituntut untuk menghasilkan lulusan yang siap kerja di dunia usaha dan dunia industri (DUDI), "
        "melanjutkan studi ke perguruan tinggi, maupun berwirausaha mandiri (Bekerja, Melanjutkan, Wirausaha - BMW). "
        "Namun, kendala utama yang sering dihadapi oleh pihak institusi sekolah adalah pengelolaan arsip dokumen kelulusan yang masih manual, "
        "sulitnya pelacakan jejak alumni (Tracer Study) untuk kebutuhan akreditasi, serta belum terintegrasinya pencatatan kompetensi keahlian "
        "siswa ke dalam bentuk Surat Keterangan Pendamping Ijazah (SKPI) secara digital."
    )
    add_body(doc,
        "Untuk menjawab tantangan tersebut, dikembangkanlah Sistem SALUT (Sistem Arsip Kelulusan dan Tracer Study). "
        "Sistem ini dirancang secara terpadu mengadopsi pola Monorepo yang mengombinasikan tiga subsistem utama: "
        "Backend RESTful API berbasis Laravel 12, Panel Pengelola Web Admin berbasis HTML5/JS/Chart.js, dan Aplikasi Mobile berbasis Flutter "
        "yang dioperasikan langsung oleh siswa aktif dan alumni pada gawai cerdas mereka."
    )
    
    add_h2(doc, "1.2 Struktur dan Pembagian Dokumen Laporan")
    add_body(doc,
        "Dokumen ini menyatukan empat tahapan pengembangan perangkat lunak yang saling berkesinambungan:"
    )
    add_bullet(doc, "Laporan 3 (Backend API & Database)", "Membahas perancangan skema database MySQL, model Eloquent, autentikasi berbasis JWT, serta endpoint API backend.");
    add_bullet(doc, "Laporan 4 (Frontend Mobile Flutter)", "Membahas penerjemahan UI ke framework Flutter, integrasi HTTP client Dio, manajemen sesi JWT, dan dynamic role rendering.");
    add_bullet(doc, "Laporan 5 (Fitur Ekosistem SMK)", "Membahas portofolio capaian unit kejuruan siswa (SKPI), integrasi halaman Portofolio Keahlian, dan modul unduh arsip digital.");
    add_bullet(doc, "Laporan 6 (Otomasi & Pengujian)", "Membahas integrasi push notification FCM, scheduled cron job transisi kelulusan otomatis, modul ganti kata sandi, tracer study, dan pengujian menyeluruh.");

    doc.add_page_break()

    # =========================================================================
    # BAB II: LAPORAN 3 - BACKEND API & DATABASE
    # =========================================================================
    add_h1(doc, "BAB II (LAPORAN 3)\nPENGEMBANGAN BACKEND API DAN KONFIGURASI BASIS DATA")
    
    add_h2(doc, "2.1 Konfigurasi Lingkungan Backend (Laravel)")
    add_body(doc,
        "Tahap awal pengembangan difokuskan pada penyusunan lingkungan backend menggunakan framework Laravel versi 12. "
        "Konfigurasi utama diatur pada file .env untuk menghubungkan Laravel dengan database engine MySQL pada server lokal XAMPP. "
        "Selain itu, dikonfigurasikan secret key HMAC-SHA256 untuk paket php-open-source-saver/jwt-auth guna mengamankan lalu lintas API."
    )
    add_img(doc, "laporan3_01_env.png", "Gambar 2.1: Konfigurasi file .env backend untuk koneksi MySQL salut_db dan JWT secret key", width_inches=6.0)
    
    add_h2(doc, "2.2 Perancangan Struktur Database (Migration dan Model)")
    add_body(doc,
        "Struktur data dirancang memenuhi spesifikasi kebutuhan multi-role. Dibuat skema tabel migrations untuk users, "
        "academic_records, achievements, graduation_docs, dan tracer_studies. Setiap tabel dilengkapi relasi kunci asing (foreign key) "
        "yang terintegrasi secara bertingkat (cascading delete) guna menjamin konsistensi dan integritas relasional data."
    )
    add_img(doc, "laporan3_02_migration_model.png", "Gambar 2.2: Potongan kode migration Laravel untuk struktur tabel akademik dan foreign key", width_inches=6.0)
    add_img(doc, "laporan3_03_phpmyadmin.png", "Gambar 2.3: Tampilan struktur 9 tabel yang berhasil di-migrate pada antarmuka phpMyAdmin", width_inches=6.0)
    
    add_h2(doc, "2.3 Pembuatan Endpoint API dan Implementasi Autentikasi JWT")
    add_body(doc,
        "Untuk memfasilitasi komunikasi antara server dan aplikasi klien mobile, dibangun 23 endpoint RESTful pada file routes/api.php. "
        "Rute publik POST /api/login digunakan untuk autentikasi awal, sedangkan seluruh rute modul siswa, alumni, guru, dan admin "
        "diproteksi oleh middleware jwt.auth. Mekanisme ini mewajibkan setiap request menyertakan header 'Authorization: Bearer <token>'."
    )
    add_img(doc, "laporan3_04_routes_api.png", "Gambar 2.4: Definisi rute RESTful API dan proteksi middleware jwt.auth pada file routes/api.php", width_inches=6.0)
    
    add_h2(doc, "2.4 Pengujian API (API Testing Response 200 OK)")
    add_body(doc,
        "Pengujian dilakukan menggunakan perangkat lunak API Client untuk memverifikasi fungsionalitas login sebelum dihubungkan ke Flutter. "
        "Request dikirimkan ke endpoint http://127.0.0.1:8000/api/login dengan payload JSON akun siswa. Server sukses mengembalikan respons 200 OK "
        "lengkap dengan token JWT dan objek data pengguna."
    )
    add_img(doc, "laporan3_05_api_testing.png", "Gambar 2.5: Pengujian API login pada API Client dengan status HTTP 200 OK dan respons payload JWT", width_inches=6.0)
    
    add_h2(doc, "2.5 Pengelolaan Version Control Backend pada GitHub")
    add_body(doc,
        "Seluruh file konfigurasi, model Eloquent, controller, dan migration backend dicatat ke Git repository dan di-push ke branch main "
        "pada repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )
    add_img(doc, "laporan3_06_git_push_backend.png", "Gambar 2.6: Eksekusi git commit dan git push backend Laravel melalui terminal PowerShell", width_inches=6.0)
    add_img(doc, "laporan3_07_github_backend.png", "Gambar 2.7: Tampilan direktori backend SALUT yang tersinkronisasi di website GitHub", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB III: LAPORAN 4 - FRONTEND MOBILE FLUTTER
    # =========================================================================
    add_h1(doc, "BAB III (LAPORAN 4)\nPENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API")
    
    add_h2(doc, "3.1 Pembuatan Antarmuka Pengguna (UI) Login")
    add_body(doc,
        "Pada sisi antarmuka bergerak, dibangun aplikasi mobile menggunakan framework Flutter dan bahasa pemrograman Dart. "
        "Halaman login_page.dart dirancang dengan tema warna korporat (#1E3A5F), dilengkapi form validasi nomor induk (NISN), "
        "serta field kata sandi dengan toggle visibilitas untuk kenyamanan pengguna."
    )
    add_img(doc, "laporan4_01_login_page_code.png", "Gambar 3.1: Potongan kode antarmuka form validasi pada file login_page.dart", width_inches=6.0)
    
    add_h2(doc, "3.2 Integrasi HTTP Request Dio dan Pengelolaan Token JWT")
    add_body(doc,
        "Komunikasi data menggunakan pustaka HTTP client Dio yang dikemas dalam kelas ApiService (singleton pattern). "
        "Diimplementasikan Interceptor yang secara otomatis membaca token JWT dari secure storage dan menyematkannya pada header "
        "Authorization di setiap request keluar, serta mendeteksi error 401 saat sesi kedaluwarsa untuk mengarahkan kembali ke halaman Login."
    )
    add_img(doc, "laporan4_02_api_service_code.png", "Gambar 3.2: Implementasi HTTP Client Dio dan Interceptor token JWT pada api_service.dart", width_inches=6.0)
    
    add_h2(doc, "3.3 Simulasi dan Pengujian Antarmuka pada Perangkat Mobile")
    add_body(doc,
        "Aplikasi dijalankan dalam lingkungan pengujian untuk memverifikasi proses login dan rendering antarmuka pengguna. "
        "Sistem berhasil mendemonstrasikan dua alur kerja: akun Siswa Aktif (Budi Santoso) dan akun Alumni (Siti Rahayu)."
    )
    add_img(doc, "laporan4_03_login_mobile_app.png", "Gambar 3.3: Tampilan antarmuka Login aplikasi SALUT saat berjalan pada perangkat mobile", width_inches=3.2)
    add_img(doc, "laporan4_04_dashboard_siswa_app.png", "Gambar 3.4: Tampilan Dashboard untuk akun Siswa Aktif (menu Prestasi dan Nilai Rapor)", width_inches=3.2)
    add_img(doc, "laporan4_05_dashboard_alumni_app.png", "Gambar 3.5: Tampilan Dashboard untuk akun Alumni (menu Arsip Digital dan Tracer Study)", width_inches=3.2)
    
    add_h2(doc, "3.4 Implementasi Logika Dynamic UI Rendering Berdasarkan Role")
    add_body(doc,
        "Salah satu keunggulan arsitektur SALUT adalah dynamic UI rendering. State management GetX membaca field role dari token JWT. "
        "Jika bernilai 'siswa', maka aplikasi menampilkan navigasi Prestasi dan Rapor; jika bernilai 'alumni', antarmuka secara adaptif "
        "beralih menampilkan layanan Arsip Digital Ijazah dan Kuesioner Tracer Study."
    )
    add_img(doc, "laporan4_06_role_logic_code.png", "Gambar 3.6: Potongan kode logika pengkondisian menu dinamis per-role pada dashboard_page.dart", width_inches=6.0)
    
    add_h2(doc, "3.5 Penyimpanan Repositori Frontend ke GitHub")
    add_body(doc,
        "Pembaruan kode aplikasi mobile disimpan ke version control system GitHub guna menjaga keterpaduan dengan backend Laravel."
    )
    add_img(doc, "laporan4_07_git_push_frontend.png", "Gambar 3.7: Eksekusi git push kode frontend Flutter pada terminal PowerShell", width_inches=6.0)
    add_img(doc, "laporan4_08_github_frontend.png", "Gambar 3.8: Tampilan repositori direktori Flutter apps_sekolah di GitHub", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB IV: LAPORAN 5 - EKOSISTEM KEJURUAN SMK (SKPI & ARSIP)
    # =========================================================================
    add_h1(doc, "BAB IV (LAPORAN 5)\nPENGEMBANGAN FITUR LANJUTAN EKOSISTEM KEJURUAN SMK\n(PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)")
    
    add_h2(doc, "4.1 Perancangan Skema Database Portofolio Keahlian (SKPI)")
    add_body(doc,
        "Khusus bagi siswa SMK, nilai ijazah saja tidak cukup untuk merepresentasikan kualifikasi industri. "
        "Oleh karena itu, dibuat skema database baru berupa tabel skill_competencies yang menampung data unit kompetensi keahlian siswa, "
        "skor uji kompetensi kejuruan, tingkat kemahiran (Dasar, Terampil, Mahir), dan nama guru penguji/asesor LSP terlisensi BNSP."
    )
    add_img(doc, "laporan5_01_migration_skpi.png", "Gambar 4.1: Kode migration Laravel untuk pembuatan tabel skill_competencies (SKPI)", width_inches=6.0)
    add_img(doc, "laporan5_02_phpmyadmin_skpi.png", "Gambar 4.2: Tampilan record data 136 unit kompetensi keahlian siswa pada database phpMyAdmin", width_inches=6.0)
    
    add_h2(doc, "4.2 Implementasi Controller API Portofolio Keahlian")
    add_body(doc,
        "Dibangun SkillController.php dengan endpoint GET /api/skills/my untuk menyajikan seluruh portofolio keahlian siswa yang sedang login. "
        "Data dikelompokkan berdasarkan jurusan siswa (seperti RPL, TKJ, Multimedia) dan dapat diunduh secara resmi dalam format PDF terverifikasi."
    )
    add_img(doc, "laporan5_03_skill_controller.png", "Gambar 4.3: Implementasi SkillController.php pada backend Laravel", width_inches=6.0)
    add_img(doc, "laporan5_04_api_skills_test.png", "Gambar 4.4: Hasil pengujian endpoint GET /api/skills/my dengan respons 200 OK data portofolio", width_inches=6.0)
    
    add_h2(doc, "4.3 Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)")
    add_body(doc,
        "Pada aplikasi Flutter, dibuat skills_page.dart yang menyajikan kartu-kartu kompetensi keahlian kejuruan. "
        "Setiap kartu menampilkan kode unit SKKNI, predikat keahlian dengan badge berwarna, skor asesmen, dan identitas penguji."
    )
    add_img(doc, "laporan5_05_skills_page_code.png", "Gambar 4.5: Kode antarmuka reactive GetX pada file skills_page.dart", width_inches=6.0)
    add_img(doc, "laporan5_06_skills_mobile_app.png", "Gambar 4.6: Tampilan antarmuka Portofolio Keahlian (SKPI) pada smartphone", width_inches=3.2)
    
    add_h2(doc, "4.4 Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)")
    add_body(doc,
        "Untuk mencegah hilangnya dokumen fisik dan mempermudah legalisir ijazah, modul arsip_page.dart memungkinkan alumni "
        "mengunduh file Ijazah Digital, SKL, dan Transkrip Nilai yang telah dibubuhi Tanda Tangan Elektronik (TTE) dan QR-Code verifikasi."
    )
    add_img(doc, "laporan5_07_arsip_mobile_app.png", "Gambar 4.7: Tampilan modul Arsip Digital Kelulusan dengan opsi unduh PDF terverifikasi", width_inches=3.2)
    
    add_h2(doc, "4.5 Sinkronisasi Repositori Fitur SKPI ke GitHub")
    add_body(doc,
        "Seluruh controller baru, migration SKPI, dan halaman Flutter didokumentasikan dan di-push ke repositori GitHub."
    )
    add_img(doc, "laporan5_08_git_push.png", "Gambar 4.8: Terminal eksekusi git push pembaruan fitur SKPI dan arsip digital", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB V: LAPORAN 6 - PUSH NOTIF, CRON JOB & PENGUJIAN AKHIR
    # =========================================================================
    add_h1(doc, "BAB V (LAPORAN 6)\nINTEGRASI PUSH NOTIFICATION, OTOMASI TRANSISI KELULUSAN,\nDAN PENGUJIAN MENYELURUH (END-TO-END)")
    
    add_h2(doc, "5.1 Integrasi Push Notification Firebase Cloud Messaging (FCM)")
    add_body(doc,
        "Agar pengumuman kelulusan dan agenda tracer study tersampaikan seketika, diintegrasikan layanan Firebase Cloud Messaging (FCM). "
        "File fcm_service.dart menangani pendaftaran token perangkat ke server, penerimaan pesan di latar depan (foreground), "
        "dan penanganan notifikasi di latar belakang (background) menggunakan pragma entry-point."
    )
    add_img(doc, "laporan6_01_fcm_service_code.png", "Gambar 5.1: Potongan kode implementasi FcmService.dart menggunakan GetX service", width_inches=6.0)
    add_img(doc, "laporan6_02_fcm_notification_app.png", "Gambar 5.2: Tampilan banner Push Notification resmi kelulusan pada layar gawai", width_inches=3.2)
    
    add_h2(doc, "5.2 Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)")
    add_body(doc,
        "Untuk menghilangkan proses manual oleh administrator, dibangun custom Artisan command: salut:promote-alumni. "
        "Perintah ini dijadwalkan berjalan otomatis setiap hari jam 00:00 (cron job). Sistem secara otomatis memeriksa tanggal kelulusan, "
        "memperbarui role 190 siswa aktif menjadi alumni, dan memicu pengiriman notifikasi FCM ke seluruh smartphone siswa terkait."
    )
    add_img(doc, "laporan6_03_cron_promote_code.png", "Gambar 5.3: Kode logika otomasi command PromoteAlumni.php pada Laravel Console", width_inches=6.0)
    add_img(doc, "laporan6_04_cron_execution_terminal.png", "Gambar 5.4: Log terminal eksekusi otomatis cron job salut:promote-alumni", width_inches=6.0)
    
    add_h2(doc, "5.3 Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile")
    add_body(doc,
        "Sesuai standar ISO/IEC 27001 mengenai keamanan data pribadi, dibangun change_password_page.dart. "
        "Pengguna dapat mengganti password lama dengan verifikasi hash bcrypt melalui endpoint terproteksi PATCH /api/profile/password."
    )
    add_img(doc, "laporan6_05_change_password_code.png", "Gambar 5.5: Potongan kode antarmuka dan validasi form pada change_password_page.dart", width_inches=6.0)
    add_img(doc, "laporan6_06_change_password_app.png", "Gambar 5.6: Tampilan antarmuka Ubah Kata Sandi pada aplikasi Flutter", width_inches=3.2)
    
    add_h2(doc, "5.4 Implementasi Kuesioner Tracer Study Alumni")
    add_body(doc,
        "Aplikasi menyediakan kuesioner dinamis untuk melacak jejak alumni (bekerja, kuliah, wirausaha). "
        "Data yang dihimpun mencakup nama instansi/perusahaan, sektor industri, rentang gaji pertama, dan tingkat keselarasan kurikulum SMK."
    )
    add_img(doc, "laporan6_07_tracer_study_app.png", "Gambar 5.7: Tampilan pengisian kuesioner Tracer Study pada aplikasi mobile", width_inches=3.2)
    
    add_h2(doc, "5.5 Analitik Ekosistem Kejuruan SMK pada Web Admin")
    add_body(doc,
        "Data tracer study dan portofolio keahlian diolah secara real-time pada dashboard Web Admin (dashboard.html). "
        "Admin dan Kepala Sekolah dapat memantau grafik persentase keterserapan alumni (65% bekerja di industri, 25% kuliah, 10% wirausaha/lainnya), "
        "serta leaderboard 5 mitra industri dan kampus penyerap lulusan terbanyak."
    )
    add_img(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 5.8: Tampilan dasbor analitik keterserapan alumni SMK pada Web Admin panel", width_inches=6.0)
    
    add_h2(doc, "5.6 Rilis Final dan Tagging Repositori GitHub")
    add_body(doc,
        "Sebagai penutup seluruh tahapan proyek, dilakukan pengujian integrasi akhir (end-to-end testing) tanpa kendala (0 error pada flutter analyze). "
        "Seluruh kode sumber dirilis secara resmi dengan tag v1.0.0-smk-release pada repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )
    add_img(doc, "laporan6_09_git_push_final.png", "Gambar 5.9: Terminal eksekusi rilis final dengan tagging v1.0.0-smk-release ke GitHub", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB VI: KESIMPULAN
    # =========================================================================
    add_h1(doc, "BAB VI\nKESIMPULAN DAN REKOMENDASI PENGEMBANGAN")
    add_h2(doc, "6.1 Kesimpulan")
    add_body(doc,
        "Berdasarkan seluruh rangkaian perancangan, implementasi, dan pengujian yang telah dipaparkan pada Laporan 3 hingga Laporan 6, "
        "dapat disimpulkan beberapa poin penting sebagai berikut:"
    )
    add_bullet(doc, "Keberhasilan Integrasi Arsitektur", "Sistem SALUT berhasil menghubungkan Backend Laravel, basis data MySQL, Web Admin panel, dan Mobile Flutter secara seamless melalui komunikasi RESTful API dan autentikasi token JWT.");
    add_bullet(doc, "Efektivitas Dynamic UI Mobile", "Aplikasi mobile Flutter mampu menampilkan antarmuka adaptif yang menyesuaikan role pengguna (Siswa Aktif vs Alumni) secara dinamis tanpa perlu instalasi aplikasi terpisah.");
    add_bullet(doc, "Relevansi Khusus Ekosistem SMK", "Diterapkannya modul Portofolio Keahlian (SKPI) dan Tracer Study memberikan nilai tambah nyata bagi SMK dalam memantau kompetensi siswa dan keterserapan lulusan di DUDI.");
    add_bullet(doc, "Otomasi Proses Bisnis", "Implementasi Scheduled Cron Job dan Firebase Cloud Messaging berhasil mengotomatiskan transisi status kelulusan dan penyampaian notifikasi secara instan kepada ratusan pengguna.");
    
    add_h2(doc, "6.2 Rekomendasi Pengembangan Lanjutan")
    add_body(doc,
        "Untuk pengembangan di masa depan, sistem ini dapat ditingkatkan dengan penambahan fitur integrasi tanda tangan digital berbasis sertifikat elektronik (BSrE), "
        "portal lowongan kerja (bursa kerja khusus / BKK) yang terhubung langsung dengan mitra industri sekolah, "
        "serta implementasi kecerdasan buatan (AI) untuk merekomendasikan pelatihan kompetensi tambahan bagi siswa berdasarkan tren kebutuhan industri terkini."
    )
    
    # Simpan ke kedua file DOCX
    doc.save(DOCX_FULL)
    print("Berhasil menyimpan dokumen lengkap di:", DOCX_FULL)
    try:
        doc.save(DOCX_PRIMARY)
        print("Berhasil memperbarui dokumen utama di:", DOCX_PRIMARY)
    except PermissionError:
        print("Catatan: File Laporan_3_dan_4.docx sedang dibuka di Microsoft Word oleh pengguna.")
        print("Dokumen lengkap tetap tersimpan dengan sempurna di Laporan_Lengkap_3_4_5_6.docx!")

def build_full_html():
    print("Membangun dokumen HTML lengkap gabungan...")
    # Read HTML and update
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Laporan Lengkap Progres 3, 4, 5, 6 - Sistem SALUT</title>
<style>
  @page { size: A4; margin: 2.5cm; }
  body { 
    font-family: 'Times New Roman', serif; 
    font-size: 12pt; 
    line-height: 1.6; 
    padding: 40px; 
    max-width: 880px; 
    margin: auto; 
    color: #111;
    background-color: #fff;
  }
  .cover-box {
    text-align: center;
    border-bottom: 2px solid #003366;
    padding-bottom: 30px;
    margin-bottom: 40px;
  }
  h1.doc-title {
    font-size: 16pt;
    color: #003366;
    font-weight: bold;
    line-height: 1.3;
  }
  h2.chapter-title { 
    font-size: 14pt; 
    text-align: center; 
    font-weight: bold; 
    margin-top: 40px; 
    margin-bottom: 20px;
    color: #003366;
    line-height: 1.3;
  }
  h3.section-title {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 8px;
    color: #1a202c;
  }
  p { 
    text-align: justify; 
    margin-bottom: 12px;
    text-indent: 35px;
  }
  ul {
    margin-left: 20px;
    margin-bottom: 15px;
  }
  li {
    margin-bottom: 6px;
    line-height: 1.4;
  }
  figure {
    text-align: center;
    margin: 24px 0;
  }
  figure img {
    max-width: 95%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }
  figure.mobile-frame img {
    max-width: 360px;
  }
  figcaption {
    font-size: 10pt;
    font-style: italic;
    color: #555;
    margin-top: 8px;
    text-align: center;
  }
  .page-break {
    page-break-before: always;
    margin-top: 50px;
    border-top: 2px dashed #bbb;
    padding-top: 40px;
  }
</style>
</head>
<body>

<div class="cover-box">
  <h1 class="doc-title">LAPORAN KOMPREHENSIF PROGRES PENGEMBANGAN SISTEM SALUT<br>(SISTEM ARSIP KELULUSAN & TRACER STUDY SMK)</h1>
  <p style="text-align:center; text-indent:0; font-weight:bold; color:#4a5568;">
    Disusun untuk Memenuhi Tugas Pengembangan Aplikasi Perangkat Bergerak & Web Terpadu<br>
    Program Studi Pendidikan Teknologi Informasi - Universitas Lampung
  </p>
  <p style="text-align:center; text-indent:0; color:#2d3748; margin-top:15px;">
    <b>Pengembang:</b> Wemvi Afrialdo | <b>NPM:</b> 2413025052<br>
    <b>Cakupan Materi:</b> Laporan 3, Laporan 4, Laporan 5, dan Laporan 6 (Full Development Cycle)
  </p>
</div>

<h2 class="chapter-title">BAB I: PENDAHULUAN SISTEM SALUT</h2>
<h3 class="section-title">1.1 Latar Belakang Proyek</h3>
<p>Sekolah Menengah Kejuruan (SMK) dituntut untuk menghasilkan lulusan yang siap kerja di dunia usaha dan dunia industri (DUDI), melanjutkan studi ke perguruan tinggi, maupun berwirausaha mandiri. Namun, pengelolaan arsip kelulusan manual dan rendahnya respons pelacakan jejak alumni (Tracer Study) sering menjadi kendala serius pada proses akreditasi sekolah. Oleh karena itu, dibangunlah Sistem SALUT dengan arsitektur monorepo yang mengombinasikan Backend Laravel, Web Admin Panel, dan Aplikasi Mobile Flutter.</p>

<div class="page-break"></div>

<h2 class="chapter-title">BAB II (LAPORAN 3): PENGEMBANGAN BACKEND API DAN KONFIGURASI BASIS DATA</h2>

<h3 class="section-title">2.1 Konfigurasi Lingkungan Backend (Laravel)</h3>
<p>Pada tahap ini, dilakukan persiapan lingkungan backend menggunakan framework Laravel versi 12. Konfigurasi awal difokuskan pada pengaturan variabel lingkungan di dalam file .env, khususnya untuk menghubungkan aplikasi Laravel dengan database relasional (MySQL) dan secret key HMAC-SHA256 untuk JWT Auth.</p>
<figure>
  <img src="laporan_screenshots/laporan3_01_env.png" alt="Konfigurasi .env Backend">
  <figcaption>Gambar 2.1: Konfigurasi file .env untuk koneksi database MySQL dan JWT Auth</figcaption>
</figure>

<h3 class="section-title">2.2 Pembuatan Struktur Database (Migration dan Model)</h3>
<p>Setelah koneksi berhasil, dirancang struktur database multi-role (Admin, Guru, Siswa Aktif, Alumni) menggunakan Migration Laravel agar skema database terstruktur, aman, dan mudah di-reproduksi.</p>
<figure>
  <img src="laporan_screenshots/laporan3_02_migration_model.png" alt="Kode Migration dan Model Laravel">
  <figcaption>Gambar 2.2: Struktur file Migration pada Laravel untuk tabel records dan relasi foreign key</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan3_03_phpmyadmin.png" alt="Tampilan Tabel Database di phpMyAdmin">
  <figcaption>Gambar 2.3: Tampilan struktur tabel database salut_db yang berhasil di-migrate pada phpMyAdmin</figcaption>
</figure>

<h3 class="section-title">2.3 Pembuatan Endpoint API dan Implementasi Autentikasi JWT</h3>
<p>Sistem SALUT menggunakan arsitektur Client-Server dengan 23 endpoint RESTful. Rute login publik disediakan pada POST /api/login, sedangkan rute modul lainnya diproteksi ketat menggunakan middleware jwt.auth.</p>
<figure>
  <img src="laporan_screenshots/laporan3_04_routes_api.png" alt="Kode Routing API Laravel">
  <figcaption>Gambar 2.4: Tampilan routing RESTful API dan proteksi middleware jwt.auth pada file routes/api.php</figcaption>
</figure>

<h3 class="section-title">2.4 Pengujian API (API Testing Response 200 OK)</h3>
<p>Pengujian dilakukan menggunakan perangkat lunak API Client. Server sukses merespons status 200 OK serta mengembalikan payload token akses JWT beserta objek profil siswa.</p>
<figure>
  <img src="laporan_screenshots/laporan3_05_api_testing.png" alt="Pengujian API Client 200 OK">
  <figcaption>Gambar 2.5: Hasil pengujian API login dengan respons status 200 OK dan token JWT yang valid</figcaption>
</figure>

<h3 class="section-title">2.5 Penyimpanan Repositori Backend ke GitHub</h3>
<p>Seluruh source code backend disimpan ke version control system GitHub pada repositori WEMVIAFRIALDO/apps_Sekolah-.</p>
<figure>
  <img src="laporan_screenshots/laporan3_06_git_push_backend.png" alt="Terminal Git Push Backend">
  <figcaption>Gambar 2.6: Eksekusi perintah git commit dan git push pada terminal untuk backend Laravel</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan3_07_github_backend.png" alt="Repositori Backend di GitHub">
  <figcaption>Gambar 2.7: Tampilan repositori Backend SALUT yang telah tersinkronisasi di website GitHub</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">BAB III (LAPORAN 4): PENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API</h2>

<h3 class="section-title">3.1 Pembuatan Antarmuka Pengguna (UI) Utama</h3>
<p>Pada tahap ini, pengembangan beralih ke mobile menggunakan framework Flutter. Dibuat halaman login_page.dart yang responsif dengan form validasi input NISN dan kata sandi.</p>
<figure>
  <img src="laporan_screenshots/laporan4_01_login_page_code.png" alt="Kode Flutter Login Page">
  <figcaption>Gambar 3.1: Potongan kode antarmuka halaman login pada file login_page.dart</figcaption>
</figure>

<h3 class="section-title">3.2 Integrasi HTTP Request dan Pengelolaan Token JWT</h3>
<p>Aplikasi Flutter dikonfigurasi menggunakan pustaka HTTP client Dio dengan arsitektur Interceptor pada ApiService untuk otomatisasi penyisipan Bearer Token pada setiap request keluar.</p>
<figure>
  <img src="laporan_screenshots/laporan4_02_api_service_code.png" alt="Kode ApiService Flutter Dio JWT">
  <figcaption>Gambar 3.2: Implementasi HTTP Client Dio dan Interceptor token JWT pada api_service.dart</figcaption>
</figure>

<h3 class="section-title">3.3 Simulasi dan Pengujian Antarmuka pada Perangkat</h3>
<p>Sistem berhasil mendemonstrasikan proses login dan interaksi pengguna pada dua peran: Siswa Aktif dan Alumni.</p>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan4_03_login_mobile_app.png" alt="Aplikasi Mobile Halaman Login">
  <figcaption>Gambar 3.3: Tampilan antarmuka Login aplikasi SALUT saat berjalan di perangkat</figcaption>
</figure>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan4_04_dashboard_siswa_app.png" alt="Dashboard Mobile Siswa Aktif">
  <figcaption>Gambar 3.4: Tampilan antarmuka Dashboard untuk peran Siswa Aktif (fitur Prestasi dan Rapor)</figcaption>
</figure>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan4_05_dashboard_alumni_app.png" alt="Dashboard Mobile Alumni">
  <figcaption>Gambar 3.5: Tampilan antarmuka Dashboard untuk peran Alumni (fitur Arsip Digital dan Tracer Study)</figcaption>
</figure>

<h3 class="section-title">3.4 Implementasi Logika Dynamic UI Rendering Berdasarkan Role</h3>
<p>Menggunakan GetX state management, aplikasi secara otomatis menampilkan menu Prestasi bagi Siswa Aktif dan menu Arsip Digital & Tracer Study bagi Alumni.</p>
<figure>
  <img src="laporan_screenshots/laporan4_06_role_logic_code.png" alt="Kode Dynamic UI Role Dashboard">
  <figcaption>Gambar 3.6: Potongan kode logika pengkondisian tampilan menu per-role pada dashboard_page.dart</figcaption>
</figure>

<h3 class="section-title">3.5 Penyimpanan Repositori Frontend ke GitHub</h3>
<p>Pembaruan kode aplikasi mobile disimpan dan disinkronisasikan ke repositori GitHub.</p>
<figure>
  <img src="laporan_screenshots/laporan4_07_git_push_frontend.png" alt="Terminal Git Push Frontend Flutter">
  <figcaption>Gambar 3.7: Tampilan terminal saat melakukan commit dan push kode frontend Flutter ke GitHub</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan4_08_github_frontend.png" alt="Repositori Frontend di GitHub">
  <figcaption>Gambar 3.8: Tampilan repositori Frontend SALUT yang berhasil di-push ke GitHub</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">BAB IV (LAPORAN 5): PENGEMBANGAN FITUR LANJUTAN EKOSISTEM KEJURUAN SMK (PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)</h2>

<h3 class="section-title">4.1 Perancangan Skema Database Portofolio Keahlian (SKPI)</h3>
<p>Dibuat tabel skill_competencies untuk mendokumentasikan capaian unit keahlian siswa SMK, nilai asesmen, tingkat kemahiran (Dasar, Terampil, Mahir), dan nama guru penguji LSP terlisensi BNSP.</p>
<figure>
  <img src="laporan_screenshots/laporan5_01_migration_skpi.png" alt="Migration SKPI">
  <figcaption>Gambar 4.1: Kode migration Laravel untuk pembuatan tabel skill_competencies (SKPI)</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan5_02_phpmyadmin_skpi.png" alt="Tabel phpMyAdmin SKPI">
  <figcaption>Gambar 4.2: Tampilan record data 136 unit kompetensi keahlian siswa pada database phpMyAdmin</figcaption>
</figure>

<h3 class="section-title">4.2 Implementasi Controller API Portofolio Keahlian</h3>
<p>Dibangun SkillController.php dengan endpoint GET /api/skills/my yang menyajikan daftar capaian portofolio kejuruan siswa yang terautentikasi.</p>
<figure>
  <img src="laporan_screenshots/laporan5_03_skill_controller.png" alt="Controller Skill Laravel">
  <figcaption>Gambar 4.3: Implementasi SkillController.php pada backend Laravel</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan5_04_api_skills_test.png" alt="Pengujian API Skills">
  <figcaption>Gambar 4.4: Hasil pengujian endpoint GET /api/skills/my dengan respons 200 OK data portofolio</figcaption>
</figure>

<h3 class="section-title">4.3 Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)</h3>
<p>Pada aplikasi Flutter, dibangun antarmuka skills_page.dart yang menyajikan kartu-kartu sertifikasi kompetensi keahlian siswa secara interaktif.</p>
<figure>
  <img src="laporan_screenshots/laporan5_05_skills_page_code.png" alt="Kode Flutter Skills Page">
  <figcaption>Gambar 4.5: Kode antarmuka reactive GetX pada file skills_page.dart</figcaption>
</figure>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan5_06_skills_mobile_app.png" alt="Layar Mobile Portofolio SKPI">
  <figcaption>Gambar 4.6: Tampilan antarmuka Portofolio Keahlian (SKPI) pada smartphone</figcaption>
</figure>

<h3 class="section-title">4.4 Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)</h3>
<p>Modul arsip_page.dart memfasilitasi alumni untuk melihat dan mengunduh berkas digital (Ijazah Asli, SKL, dan Transkrip Nilai) ber-watermark verifikasi sah.</p>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan5_07_arsip_mobile_app.png" alt="Layar Mobile Arsip Digital">
  <figcaption>Gambar 4.7: Tampilan modul Arsip Digital Kelulusan dengan opsi unduh PDF terverifikasi</figcaption>
</figure>

<h3 class="section-title">4.5 Sinkronisasi Repositori Fitur SKPI ke GitHub</h3>
<p>Pembaruan kode modul portofolio keahlian dan arsip digital disinkronisasikan ke repositori GitHub.</p>
<figure>
  <img src="laporan_screenshots/laporan5_08_git_push.png" alt="Git Push SKPI">
  <figcaption>Gambar 4.8: Terminal eksekusi git push pembaruan fitur SKPI dan arsip digital</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">BAB V (LAPORAN 6): INTEGRASI PUSH NOTIFICATION, OTOMASI TRANSISI KELULUSAN, DAN PENGUJIAN MENYELURUH</h2>

<h3 class="section-title">5.1 Integrasi Push Notification Firebase Cloud Messaging (FCM)</h3>
<p>Dipasang fcm_service.dart untuk menangani penerimaan notifikasi siaran pengumuman kelulusan dan kuesioner tracer study secara langsung pada smartphone pengguna.</p>
<figure>
  <img src="laporan_screenshots/laporan6_01_fcm_service_code.png" alt="Kode FCM Service Flutter">
  <figcaption>Gambar 5.1: Potongan kode implementasi FcmService.dart menggunakan GetX service</figcaption>
</figure>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan6_02_fcm_notification_app.png" alt="Push Notification Mobile">
  <figcaption>Gambar 5.2: Tampilan banner Push Notification resmi kelulusan pada layar gawai</figcaption>
</figure>

<h3 class="section-title">5.2 Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)</h3>
<p>Dibangun command artisan salut:promote-alumni yang dijadwalkan otomatis setiap hari jam 00:00 untuk mengubah role siswa yang telah lulus menjadi alumni tanpa intervensi manual admin.</p>
<figure>
  <img src="laporan_screenshots/laporan6_03_cron_promote_code.png" alt="Kode Artisan Promote Alumni">
  <figcaption>Gambar 5.3: Kode logika otomasi command PromoteAlumni.php pada Laravel Console</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan6_04_cron_execution_terminal.png" alt="Eksekusi Terminal Cron Job">
  <figcaption>Gambar 5.4: Log terminal eksekusi otomatis cron job salut:promote-alumni</figcaption>
</figure>

<h3 class="section-title">5.3 Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile</h3>
<p>Disediakan modul change_password_page.dart untuk validasi dan pembaruan kata sandi pengguna secara terenkripsi bcrypt.</p>
<figure>
  <img src="laporan_screenshots/laporan6_05_change_password_code.png" alt="Kode Change Password">
  <figcaption>Gambar 5.5: Potongan kode antarmuka dan validasi form pada change_password_page.dart</figcaption>
</figure>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan6_06_change_password_app.png" alt="Layar Mobile Ubah Kata Sandi">
  <figcaption>Gambar 5.6: Tampilan antarmuka Ubah Kata Sandi pada aplikasi Flutter</figcaption>
</figure>

<h3 class="section-title">5.4 Implementasi Kuesioner Tracer Study Alumni</h3>
<p>Kuesioner tracer study mencatat riwayat penyerapan kerja alumni (Bekerja, Kuliah, Wirausaha) beserta data nama perusahaan, prodi kampus, dan rentang penghasilan.</p>
<figure class="mobile-frame">
  <img src="laporan_screenshots/laporan6_07_tracer_study_app.png" alt="Layar Mobile Tracer Study">
  <figcaption>Gambar 5.7: Tampilan pengisian kuesioner Tracer Study pada aplikasi mobile</figcaption>
</figure>

<h3 class="section-title">5.5 Analitik Ekosistem Kejuruan SMK pada Web Admin</h3>
<p>Web Admin panel menampilkan visualisasi data analitik penyerapan lulusan (65% bekerja di industri DUDI, 25% kuliah, 10% wirausaha/lainnya) serta top mitra institusi penyerap alumni.</p>
<figure>
  <img src="laporan_screenshots/laporan6_08_webadmin_smk_analytics.png" alt="Web Admin Analytics">
  <figcaption>Gambar 5.8: Tampilan dasbor analitik keterserapan alumni SMK pada Web Admin panel</figcaption>
</figure>

<h3 class="section-title">5.6 Rilis Final dan Tagging Repositori GitHub</h3>
<p>Setelah seluruh fitur diuji secara end-to-end dengan hasil 0 error, proyek dirilis secara resmi dengan tag v1.0.0-smk-release di GitHub.</p>
<figure>
  <img src="laporan_screenshots/laporan6_09_git_push_final.png" alt="Git Tag Final Release">
  <figcaption>Gambar 5.9: Terminal eksekusi rilis final dengan tagging v1.0.0-smk-release ke GitHub</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">BAB VI: KESIMPULAN DAN REKOMENDASI PENGEMBANGAN</h2>
<h3 class="section-title">6.1 Kesimpulan</h3>
<p>Sistem SALUT telah berhasil diselesaikan secara menyeluruh, mencakup integrasi backend RESTful API Laravel, database relasional MySQL, aplikasi mobile Flutter, dan Web Admin analitik. Fitur khusus SMK berupa Portofolio Keahlian (SKPI) dan otomasi kelulusan berbasis cron job memberikan efisiensi nyata dalam tata kelola administrasi kelulusan dan akreditasi sekolah.</p>

<h3 class="section-title">6.2 Rekomendasi</h3>
<p>Untuk masa depan, sistem dapat diintegrasikan dengan tanda tangan elektronik bersertifikasi BSrE dan modul bursa kerja khusus (BKK) industri.</p>

</body>
</html>
"""
    with open(HTML_FULL, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(HTML_PRIMARY, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(DOC_PRIMARY, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Berhasil menyimpan file HTML dan DOC lengkap!")

if __name__ == "__main__":
    build_full_docx()
    build_full_html()
    print("Semua proses penyusunan dokumen laporan lengkap selesai dengan sukses!")
