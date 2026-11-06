# -*- coding: utf-8 -*-
"""
Script Penggabungan Dokumen Instalasi (Laporan 1 & 2) dengan Laporan 3, 4, 5, dan 6
Memformat seluruh teks: Times New Roman, 12 pt, Rata Kanan-Kiri (Justified), Spasi 1.5.
Mengganti mockup HP dengan Kotak Placeholder Template Resmi untuk Screenshot Asli HP.
Penulis: Wemvi Afrialdo (NPM: 2413025052)
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"d:\proyek_applikasi\apps_sekolah"
INSTALASI_DOCX = r"D:\proyek_applikasi\instalasi.docx"
IMG_DIR = os.path.join(BASE_DIR, "laporan_screenshots")

DOCX_OUTPUTS = [
    INSTALASI_DOCX,
    os.path.join(BASE_DIR, "Laporan_Lengkap_3_4_5_6.docx"),
    os.path.join(BASE_DIR, "Laporan_Lengkap_Sistem_SALUT_dan_Instalasi.docx"),
]
HTML_OUTPUT = os.path.join(BASE_DIR, "Laporan_Lengkap_3_4_5_6.html")
HTML_PRIMARY = os.path.join(BASE_DIR, "Laporan_3_dan_4.html")
DOC_PRIMARY = os.path.join(BASE_DIR, "Laporan_3_dan_4.doc")

def format_paragraph(p, name='Times New Roman', size_pt=12, bold=False, italic=False, color_rgb=(0,0,0), space_after_pt=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after_pt)
    p.paragraph_format.line_spacing = line_spacing
    for r in p.runs:
        r.font.name = name
        r.font.size = Pt(size_pt)
        if bold is not None:
            r.font.bold = bold
        if italic is not None:
            r.font.italic = italic
        r.font.color.rgb = RGBColor(*color_rgb)

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0, 51, 102)
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(20, 30, 60)
    return p

def add_body(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p

def add_bullet(doc, bold_prefix, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.3
    r_sym = p.add_run("•  ")
    r_sym.font.name = 'Times New Roman'
    r_sym.font.size = Pt(12)
    r1 = p.add_run(bold_prefix + ": ")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r2 = p.add_run(text)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    return p

def add_code_img(doc, img_filename, caption_text, width_inches=6.0):
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

def add_mobile_screenshot_placeholder(doc, title_screen, instruction, caption_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(5.8)
    
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
    tcPr.append(shd)
    
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="dashed" w:sz="12" w:space="0" w:color="94A3B8"/>
            <w:left w:val="dashed" w:sz="12" w:space="0" w:color="94A3B8"/>
            <w:bottom w:val="dashed" w:sz="12" w:space="0" w:color="94A3B8"/>
            <w:right w:val="dashed" w:sz="12" w:space="0" w:color="94A3B8"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)
    
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="450" w:type="dxa"/>
            <w:bottom w:w="450" w:type="dxa"/>
            <w:left w:w="300" w:type="dxa"/>
            <w:right w:w="300" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    
    r1 = p.add_run("[TEMPAT SCREENSHOT ASLI DARI HP]\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(11)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0, 51, 102)
    
    r2 = p.add_run(f"{title_screen}\n")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(11)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(15, 23, 42)
    
    r3 = p.add_run(f"({instruction} - klik kotak ini lalu tekan Ctrl+V untuk menempelkan gambar)")
    r3.font.name = 'Times New Roman'
    r3.font.size = Pt(9.5)
    r3.font.italic = True
    r3.font.color.rgb = RGBColor(100, 116, 139)
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(6)
    p_cap.paragraph_format.space_after = Pt(12)
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(10)
    r_cap.font.italic = True
    r_cap.font.color.rgb = RGBColor(90, 90, 90)

def merge_and_build():
    print(f"Membuka file {INSTALASI_DOCX}...")
    doc = docx.Document(INSTALASI_DOCX)
    
    # 1. Atur Margin Halaman (1 Inci sekeliling)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        header = section.header
        p_head = header.paragraphs[0]
        p_head.text = "Laporan Komprehensif Sistem SALUT | Universitas Lampung"
        p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_head.runs[0].font.name = 'Times New Roman'
        p_head.runs[0].font.size = Pt(9)
        p_head.runs[0].font.italic = True
        p_head.runs[0].font.color.rgb = RGBColor(128, 128, 128)

    # 2. Format ulang paragraf Laporan 1 & 2 yang sudah ada di instalasi.docx
    print("Memformat ulang paragraf Laporan 1 & 2...")
    total_existing = len(doc.paragraphs)
    
    # Bersihkan paragraf penutup bawaan dari indeks 50 sampai akhir
    # (indeks 50 ke atas adalah baris kosong dan placeholder 'LAPORAN 3')
    del_count = 0
    while len(doc.paragraphs) > 50:
        p_last = doc.paragraphs[-1]
        p_element = p_last._element
        p_element.getparent().remove(p_element)
        del_count += 1
    print(f"Menghapus {del_count} paragraf kosong/placeholder penutup dari file instalasi.docx")
    
    # Format paragraf konten Laporan 1 & 2
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if not txt and len(p.runs) == 0:
            continue
        if i <= 15:
            # Halaman Cover
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.2
            p.paragraph_format.space_after = Pt(6)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                if i in (0, 7, 9, 15):
                    r.font.bold = True
        else:
            # Isi teks Laporan 1 & 2
            if len(txt) > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.line_spacing = 1.5
                p.paragraph_format.space_after = Pt(6)
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(12)
            else:
                # Gambar tangkapan layar instalasi
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(8)

    # 3. Masukkan Page Break untuk memulai Laporan 3
    doc.add_page_break()

    # =========================================================================
    # BAB II: LAPORAN 3 - PENGEMBANGAN BACKEND API DAN BASIS DATA RELASIONAL
    # =========================================================================
    add_h1(doc, "LAPORAN 3\nPENGEMBANGAN BACKEND API DAN KONFIGURASI BASIS DATA PADA SISTEM SALUT")
    
    add_h2(doc, "1. Konfigurasi Lingkungan Backend (Laravel)")
    add_body(doc,
        "Pada tahap ini, dilakukan persiapan lingkungan backend menggunakan framework Laravel versi 12. "
        "Konfigurasi awal difokuskan pada pengaturan variabel lingkungan di dalam file .env, khususnya untuk "
        "menghubungkan aplikasi Laravel dengan database relasional (MySQL) yang berjalan pada server lokal XAMPP. "
        "Selain koneksi database, dikonfigurasikan pula kunci enkripsi rahasia (JWT_SECRET) menggunakan paket "
        "php-open-source-saver/jwt-auth guna mengamankan autentikasi token antara aplikasi klien mobile dan server backend."
    )
    add_code_img(doc, "laporan3_01_env.png", "Gambar 3.1: Konfigurasi file .env untuk koneksi database MySQL salut_db dan JWT Secret", width_inches=6.0)
    
    add_h2(doc, "2. Pembuatan Struktur Database (Migration dan Model)")
    add_body(doc,
        "Setelah koneksi berhasil, tahap selanjutnya adalah merancang struktur database yang mendukung sistem multi-role "
        "(Admin, Guru, Siswa Aktif, dan Alumni). Pembuatan tabel dilakukan menggunakan fitur Migration bawaan Laravel agar "
        "skema database terstruktur, aman, dan mudah di-reproduksi. Dibuat skema tabel migrations untuk users, academic_records, "
        "achievements, graduation_docs, dan tracer_studies dengan relasi foreign key berjenjang (cascading delete). "
        "Selain itu, dibuat pula Model Eloquent untuk merepresentasikan entitas bisnis tersebut di dalam kode program."
    )
    add_code_img(doc, "laporan3_02_migration_model.png", "Gambar 3.2: Struktur file Migration pada Laravel untuk relasi tabel akademik dan foreign key", width_inches=6.0)
    add_code_img(doc, "laporan3_03_phpmyadmin.png", "Gambar 3.3: Tampilan struktur tabel database salut_db yang berhasil di-migrate pada antarmuka phpMyAdmin", width_inches=6.0)
    
    add_h2(doc, "3. Pembuatan Endpoint API dan Implementasi Autentikasi JWT")
    add_body(doc,
        "Sistem SALUT menggunakan arsitektur Client-Server, sehingga diperlukan penyediaan API (Application Programming Interface). "
        "Untuk menjaga keamanan pertukaran data, diterapkan autentikasi berbasis token JSON Web Token (JWT). "
        "Rute publik POST /api/login disediakan untuk proses masuk pengguna, sedangkan endpoint untuk modul profil, prestasi siswa, "
        "arsip kelulusan, dan tracer study diproteksi menggunakan middleware jwt.auth yang mewajibkan penyertaan Bearer Token."
    )
    add_code_img(doc, "laporan3_04_routes_api.png", "Gambar 3.4: Definisi rute RESTful API dan proteksi middleware jwt.auth pada file routes/api.php", width_inches=6.0)
    
    add_h2(doc, "4. Pengujian API (API Testing)")
    add_body(doc,
        "Untuk memastikan endpoint API dan autentikasi JWT berjalan dengan sempurna sebelum diintegrasikan ke aplikasi mobile Flutter, "
        "dilakukan pengujian menggunakan perangkat lunak API Client. Pengujian dilakukan dengan mengirimkan request login berupa "
        "nomor induk (NISN) dan kata sandi. Server berhasil merespons dengan status 200 OK serta mengembalikan payload token akses JWT "
        "dan objek data profil pengguna secara lengkap."
    )
    add_code_img(doc, "laporan3_05_api_testing.png", "Gambar 3.5: Hasil pengujian API login dengan status HTTP 200 OK dan respons payload token JWT", width_inches=6.0)
    
    add_h2(doc, "5. Penyimpanan Repositori Backend ke GitHub")
    add_body(doc,
        "Setelah kerangka dasar backend selesai dan diuji, seluruh perubahan kode sumber disimpan ke version control system GitHub "
        "pada repositori WEMVIAFRIALDO/apps_Sekolah-. Langkah ini menjamin keamanan data proyek, mendokumentasikan riwayat perubahan kode, "
        "dan memudahkan pelacakan versi perangkat lunak."
    )
    add_code_img(doc, "laporan3_06_git_push_backend.png", "Gambar 3.6: Eksekusi perintah git commit dan git push pada terminal PowerShell untuk backend Laravel", width_inches=6.0)
    add_code_img(doc, "laporan3_07_github_backend.png", "Gambar 3.7: Tampilan repositori Backend SALUT yang telah tersinkronisasi di website GitHub", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB III: LAPORAN 4 - FRONTEND MOBILE FLUTTER & INTEGRASI API
    # =========================================================================
    add_h1(doc, "LAPORAN 4\nPENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API")
    
    add_h2(doc, "1. Pembuatan Antarmuka Pengguna (UI) Utama")
    add_body(doc,
        "Pada tahap ini, pengembangan beralih ke sisi frontend mobile menggunakan framework Flutter. "
        "Langkah pertama adalah menerjemahkan desain (mockup) menjadi kode Dart untuk membentuk antarmuka pengguna. "
        "Fokus utama diarahkan pada pembuatan halaman autentikasi (login_page.dart) dengan form validasi nomor induk dan kata sandi, "
        "serta perancangan halaman utama (dashboard_page.dart) yang responsif dan konsisten dengan warna identitas proyek (#1E3A5F)."
    )
    add_code_img(doc, "laporan4_01_login_page_code.png", "Gambar 4.1: Potongan kode antarmuka form validasi login pada file login_page.dart", width_inches=6.0)
    
    add_h2(doc, "2. Integrasi HTTP Request dan Pengelolaan Token JWT")
    add_body(doc,
        "Agar aplikasi mobile terhubung secara dinamis dengan Backend API yang telah dibangun pada Laporan 3, "
        "diterapkan pustaka HTTP client Dio di dalam kelas ApiService. Dikonfigurasikan Interceptor yang secara otomatis membaca token JWT "
        "dari penyimpanan aman perangkat (flutter_secure_storage) dan menyematkannya pada header Authorization di setiap request keluar. "
        "Selain itu, jika terjadi respons 401 Unauthorized karena token kedaluwarsa, aplikasi otomatis mengarahkan pengguna kembali ke halaman Login."
    )
    add_code_img(doc, "laporan4_02_api_service_code.png", "Gambar 4.2: Implementasi HTTP Client Dio dan Interceptor token JWT pada api_service.dart", width_inches=6.0)
    
    add_h2(doc, "3. Simulasi dan Pengujian Antarmuka pada Perangkat Mobile")
    add_body(doc,
        "Setelah integrasi selesai, aplikasi dijalankan untuk menguji alur autentikasi dan rendering antarmuka pengguna. "
        "Pengujian berhasil mendemonstrasikan dua skenario peran pengguna: akun Siswa Aktif (Budi Santoso) dan akun Alumni (Siti Rahayu)."
    )
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Halaman Login Aplikasi SALUT",
        "Ambil tangkapan layar langsung dari HP saat membuka halaman Login SALUT",
        "Gambar 4.3: Tampilan antarmuka Login aplikasi SALUT pada perangkat mobile"
    )
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Dashboard Siswa Aktif",
        "Ambil tangkapan layar langsung dari HP setelah login menggunakan akun Siswa Aktif (Budi Santoso)",
        "Gambar 4.4: Tampilan antarmuka Dashboard untuk peran Siswa Aktif (fitur Prestasi dan Rapor)"
    )
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Dashboard Alumni",
        "Ambil tangkapan layar langsung dari HP setelah login menggunakan akun Alumni (Siti Rahayu)",
        "Gambar 4.5: Tampilan antarmuka Dashboard untuk peran Alumni (fitur Arsip Digital dan Tracer Study)"
    )
    
    add_h2(doc, "4. Implementasi Logika Dynamic UI Rendering (Role-Based)")
    add_body(doc,
        "Sesuai dengan aturan bisnis sistem SALUT, tampilan antarmuka dirancang dinamis menyesuaikan role pengguna yang diperoleh "
        "dari token JWT. Menggunakan reactive state management GetX, jika pengguna teridentifikasi sebagai Siswa Aktif, "
        "maka navigasi dan menu difokuskan pada manajemen Prestasi dan Nilai Rapor; sedangkan jika terdeteksi sebagai Alumni, "
        "menu secara otomatis bertransformasi menjadi layanan Arsip Dokumen Digital Ijazah dan Kuesioner Tracer Study."
    )
    add_code_img(doc, "laporan4_06_role_logic_code.png", "Gambar 4.6: Potongan kode logika pengkondisian tampilan menu per-role pada dashboard_page.dart", width_inches=6.0)
    
    add_h2(doc, "5. Penyimpanan Repositori Frontend ke GitHub")
    add_body(doc,
        "Sebagai penutup tahap pengembangan antarmuka mobile, pembaruan kode aplikasi Flutter disinkronisasikan ke repositori GitHub."
    )
    add_code_img(doc, "laporan4_07_git_push_frontend.png", "Gambar 4.7: Eksekusi git push kode frontend Flutter pada terminal PowerShell", width_inches=6.0)
    add_code_img(doc, "laporan4_08_github_frontend.png", "Gambar 4.8: Tampilan repositori direktori Flutter apps_sekolah di GitHub", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB IV: LAPORAN 5 - EKOSISTEM KEJURUAN SMK (SKPI & ARSIP DIGITAL)
    # =========================================================================
    add_h1(doc, "LAPORAN 5\nPENGEMBANGAN FITUR LANJUTAN EKOSISTEM KEJURUAN SMK\n(PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)")
    
    add_h2(doc, "1. Perancangan Skema Database Portofolio Keahlian (SKPI)")
    add_body(doc,
        "Khusus bagi siswa Sekolah Menengah Kejuruan (SMK), nilai akademik ijazah perlu didukung dengan portofolio capaian "
        "unit kompetensi yang relevan dengan kebutuhan dunia kerja (DUDI). Oleh karena itu, dirancang skema database baru melalui "
        "tabel skill_competencies. Tabel ini menampung kode unit SKKNI, nama keahlian, tingkat kemahiran (Dasar, Terampil, Mahir), "
        "skor asesmen, dan identitas asesor penguji terlisensi BNSP."
    )
    add_code_img(doc, "laporan5_01_migration_skpi.png", "Gambar 5.1: Kode migration Laravel untuk pembuatan tabel skill_competencies (SKPI)", width_inches=6.0)
    add_code_img(doc, "laporan5_02_phpmyadmin_skpi.png", "Gambar 5.2: Tampilan record data 136 unit kompetensi keahlian siswa pada phpMyAdmin", width_inches=6.0)
    
    add_h2(doc, "2. Implementasi Endpoint API Portofolio Keahlian")
    add_body(doc,
        "Pada sisi server, dibangun SkillController.php dengan endpoint GET /api/skills/my. Endpoint ini menyajikan daftar seluruh "
        "unit kompetensi kejuruan yang telah diselesaikan oleh siswa yang sedang terautentikasi berdasarkan jurusannya "
        "(Rekayasa Perangkat Lunak, Teknik Komputer dan Jaringan, atau Multimedia)."
    )
    add_code_img(doc, "laporan5_03_skill_controller.png", "Gambar 5.3: Implementasi SkillController.php pada backend Laravel", width_inches=6.0)
    add_code_img(doc, "laporan5_04_api_skills_test.png", "Gambar 5.4: Hasil pengujian endpoint GET /api/skills/my dengan respons 200 OK data portofolio", width_inches=6.0)
    
    add_h2(doc, "3. Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)")
    add_body(doc,
        "Pada aplikasi Flutter, dibangun antarmuka skills_page.dart yang menyajikan kartu kompetensi kejuruan secara interaktif. "
        "Setiap kartu memuat rincian kode unit, predikat kemahiran dengan badge warna informatif, skor capaian, dan nama penguji."
    )
    add_code_img(doc, "laporan5_05_skills_page_code.png", "Gambar 5.5: Kode antarmuka reactive GetX pada file skills_page.dart", width_inches=6.0)
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Halaman Portofolio Keahlian (SKPI)",
        "Ambil tangkapan layar langsung dari HP pada menu Portofolio Keahlian SKPI",
        "Gambar 5.6: Tampilan antarmuka Portofolio Keahlian (SKPI) pada perangkat mobile"
    )
    
    add_h2(doc, "4. Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)")
    add_body(doc,
        "Untuk mencegah kerusakan dokumen fisik dan mempermudah proses verifikasi ijazah oleh alumni, "
        "dibangun modul arsip_page.dart. Alumni dapat melihat dan mengunduh berkas digital (Ijazah Asli, SKL, dan Transkrip Nilai) "
        "yang telah dibubuhi Tanda Tangan Elektronik (TTE) dan QR-Code verifikasi resmi."
    )
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Halaman Arsip Digital Kelulusan",
        "Ambil tangkapan layar langsung dari HP pada menu Arsip Digital Ijazah & SKL",
        "Gambar 5.7: Tampilan modul Arsip Digital Kelulusan dengan opsi unduh PDF terverifikasi pada HP"
    )
    
    add_h2(doc, "5. Sinkronisasi Repositori Fitur SKPI ke GitHub")
    add_body(doc,
        "Seluruh file controller baru, migration kejuruan SMK, dan modul Flutter didokumentasikan dan disinkronisasikan ke GitHub."
    )
    add_code_img(doc, "laporan5_08_git_push.png", "Gambar 5.8: Terminal eksekusi git push pembaruan fitur SKPI dan arsip digital", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB V: LAPORAN 6 - PUSH NOTIFIKASI, CRON JOB & PENGUJIAN AKHIR
    # =========================================================================
    add_h1(doc, "LAPORAN 6\nINTEGRASI PUSH NOTIFICATION, OTOMASI TRANSISI KELULUSAN,\nDAN PENGUJIAN MENYELURUH (END-TO-END)")
    
    add_h2(doc, "1. Integrasi Push Notification Firebase Cloud Messaging (FCM)")
    add_body(doc,
        "Untuk memastikan pengumuman kelulusan dan agenda tracer study diterima seketika oleh pengguna, "
        "diintegrasikan layanan Firebase Cloud Messaging (FCM). File fcm_service.dart menangani pendaftaran token perangkat, "
        "penerimaan notifikasi saat aplikasi dibuka (foreground), dan penanganan pesan di latar belakang (background handler)."
    )
    add_code_img(doc, "laporan6_01_fcm_service_code.png", "Gambar 6.1: Potongan kode implementasi FcmService.dart menggunakan GetX service", width_inches=6.0)
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Banner Push Notifikasi Resmi",
        "Ambil tangkapan layar langsung dari HP saat banner Push Notification kelulusan muncul di layar atas",
        "Gambar 6.2: Tampilan banner Push Notification resmi kelulusan pada perangkat mobile"
    )
    
    add_h2(doc, "2. Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)")
    add_body(doc,
        "Untuk meniadakan proses manual pemindahan status siswa, dibangun custom Artisan command: salut:promote-alumni. "
        "Perintah ini dijadwalkan secara berkala (cron job) setiap hari jam 00:00. Sistem secara otomatis memeriksa tanggal kelulusan, "
        "mengubah role 190 siswa aktif menjadi alumni, dan memicu pengiriman notifikasi FCM ke perangkat pengguna."
    )
    add_code_img(doc, "laporan6_03_cron_promote_code.png", "Gambar 6.3: Kode logika otomasi command PromoteAlumni.php pada Laravel Console", width_inches=6.0)
    add_code_img(doc, "laporan6_04_cron_execution_terminal.png", "Gambar 6.4: Log terminal eksekusi otomatis cron job salut:promote-alumni", width_inches=6.0)
    
    add_h2(doc, "3. Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile")
    add_body(doc,
        "Sesuai prinsip keamanan data pengguna, dibangun halaman change_password_page.dart. Pengguna dapat memperbarui kata sandi "
        "dengan validasi pencocokan kata sandi baru dan enkripsi bcrypt melalui endpoint terproteksi PATCH /api/profile/password."
    )
    add_code_img(doc, "laporan6_05_change_password_code.png", "Gambar 6.5: Potongan kode antarmuka dan validasi form pada change_password_page.dart", width_inches=6.0)
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Halaman Ubah Kata Sandi",
        "Ambil tangkapan layar langsung dari HP pada halaman Ubah Kata Sandi akun",
        "Gambar 6.6: Tampilan antarmuka Ubah Kata Sandi pada perangkat mobile"
    )
    
    add_h2(doc, "4. Implementasi Kuesioner Tracer Study Alumni")
    add_body(doc,
        "Aplikasi mobile menyediakan kuesioner dinamis untuk melacak keterserapan alumni (Bekerja, Melanjutkan Kuliah, Wirausaha). "
        "Data yang dikumpulkan mencakup nama perusahaan/kampus, sektor industri, rentang penghasilan pertama, dan tingkat keselarasan kurikulum."
    )
    add_mobile_screenshot_placeholder(
        doc,
        "Tampilan Kuesioner Tracer Study",
        "Ambil tangkapan layar langsung dari HP pada formulir kuesioner Tracer Study Alumni",
        "Gambar 6.7: Tampilan pengisian kuesioner Tracer Study pada perangkat mobile"
    )
    
    add_h2(doc, "5. Analitik Ekosistem Kejuruan SMK pada Web Admin")
    add_body(doc,
        "Data hasil tracer study dan capaian keahlian diolah secara visual pada dashboard Web Admin (dashboard.html). "
        "Pihak manajemen sekolah dapat memantau distribusi keterserapan lulusan (65% bekerja di DUDI, 25% kuliah, 10% wirausaha/lainnya), "
        "serta leaderboard 5 mitra industri dan kampus penyerap lulusan terbanyak."
    )
    add_code_img(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 6.8: Tampilan dasbor analitik keterserapan alumni SMK pada Web Admin panel", width_inches=6.0)
    
    add_h2(doc, "6. Rilis Final dan Tagging Repositori GitHub")
    add_body(doc,
        "Setelah seluruh pengujian integrasi akhir selesai dengan hasil 0 error, proyek dirilis secara resmi dengan tag "
        "v1.0.0-smk-release pada repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )
    add_code_img(doc, "laporan6_09_git_push_final.png", "Gambar 6.9: Terminal eksekusi rilis final dengan tagging v1.0.0-smk-release ke GitHub", width_inches=6.0)

    doc.add_page_break()

    # =========================================================================
    # BAB VI: KESIMPULAN DAN REKOMENDASI PENGEMBANGAN
    # =========================================================================
    add_h1(doc, "BAB VI\nKESIMPULAN DAN REKOMENDASI PENGEMBANGAN")
    
    add_h2(doc, "1. Kesimpulan")
    add_body(doc,
        "Berdasarkan seluruh rangkaian perancangan, implementasi, dan pengujian yang telah dipaparkan mulai dari tahap instalasi awal "
        "(Laporan 1 & 2), pengembangan backend dan database (Laporan 3), pengembangan antarmuka mobile Flutter (Laporan 4), "
        "penerapan ekosistem kejuruan SMK (Laporan 5), hingga integrasi notifikasi dan otomasi cron job (Laporan 6), "
        "dapat disimpulkan bahwa:"
    )
    add_bullet(doc, "Integrasi Multi-Platform Berhasil Penuh", "Sistem SALUT sukses menghubungkan Backend RESTful API Laravel, basis data relasional MySQL, panel Web Admin analitik, dan aplikasi mobile Flutter secara terintegrasi.");
    add_bullet(doc, "Kesesuaian dengan Ekosistem SMK", "Diterapkannya modul Portofolio Keahlian (SKPI) dan Tracer Study memberikan nilai tambah nyata bagi institusi SMK dalam mencatat kompetensi kejuruan siswa dan memantau keterserapan lulusan.");
    add_bullet(doc, "Efisiensi Melalui Otomasi", "Penggunaan Scheduled Cron Job dan Firebase Cloud Messaging (FCM) berhasil mengotomatiskan transisi status kelulusan dan pengiriman notifikasi instan kepada ratusan pengguna.");
    
    add_h2(doc, "2. Rekomendasi Pengembangan Lanjutan")
    add_body(doc,
        "Untuk pengembangan di masa depan, sistem dapat diperluas dengan mengintegrasikan Tanda Tangan Elektronik bersertifikasi BSrE, "
        "portal Bursa Kerja Khusus (BKK) yang terhubung langsung dengan rekrutmen mitra industri sekolah, "
        "serta penerapan kecerdasan buatan (AI) untuk merekomendasikan pelatihan upskilling bagi alumni sesuai tren lowongan kerja terkini."
    )

    # 4. Simpan ke seluruh file output
    for out_path in DOCX_OUTPUTS:
        try:
            doc.save(out_path)
            print("Berhasil menyimpan dokumen Word di:", out_path)
        except PermissionError:
            print(f"Peringatan: File {out_path} sedang dibuka di Microsoft Word. Lewati penyimpanan file terkunci.")
            
def build_html_with_placeholders():
    print("Membangun dokumen HTML dengan kotak placeholder...")
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Laporan Lengkap Progres Sistem SALUT</title>
<style>
  @page { size: A4; margin: 2.5cm; }
  body { 
    font-family: 'Times New Roman', serif; 
    font-size: 12pt; 
    line-height: 1.5; 
    padding: 40px; 
    max-width: 860px; 
    margin: auto; 
    color: #111;
    background-color: #fff;
  }
  .cover-box {
    text-align: center;
    border-bottom: 2px solid #003366;
    padding-bottom: 25px;
    margin-bottom: 35px;
  }
  h1.doc-title { font-size: 15pt; color: #003366; font-weight: bold; line-height: 1.3; }
  h2.chapter-title { 
    font-size: 13pt; text-align: center; font-weight: bold; 
    margin-top: 35px; margin-bottom: 20px; color: #003366; line-height: 1.3; 
  }
  h3.section-title { font-size: 12pt; font-weight: bold; margin-top: 22px; margin-bottom: 8px; color: #1a202c; }
  p { text-align: justify; margin-bottom: 12px; text-indent: 32px; }
  ul { margin-left: 20px; margin-bottom: 15px; }
  li { margin-bottom: 5px; line-height: 1.4; text-align: justify; }
  figure { text-align: center; margin: 22px 0; }
  figure img { max-width: 95%; height: auto; border: 1px solid #ddd; border-radius: 4px; }
  figcaption { font-size: 10pt; font-style: italic; color: #555; margin-top: 8px; text-align: center; }
  
  /* Kotak Placeholder Screenshot Asli HP */
  .mobile-placeholder {
    border: 2px dashed #94a3b8;
    background-color: #f8fafc;
    border-radius: 8px;
    padding: 30px 20px;
    margin: 20px auto;
    max-width: 500px;
    text-align: center;
  }
  .mobile-placeholder .tag {
    display: inline-block;
    background-color: #003366;
    color: #fff;
    font-weight: bold;
    font-size: 10.5pt;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 8px;
  }
  .mobile-placeholder .title {
    font-weight: bold;
    font-size: 11pt;
    color: #0f172a;
    margin-bottom: 4px;
  }
  .mobile-placeholder .note {
    font-size: 9.5pt;
    font-style: italic;
    color: #64748b;
  }
  .page-break { page-break-before: always; margin-top: 40px; border-top: 2px dashed #bbb; padding-top: 35px; }
</style>
</head>
<body>

<div class="cover-box">
  <h1 class="doc-title">LAPORAN KOMPREHENSIF PROGRES PENGEMBANGAN SISTEM SALUT<br>(SISTEM ARSIP KELULUSAN & TRACER STUDY SMK)</h1>
  <p style="text-align:center; text-indent:0; font-weight:bold; color:#4a5568;">
    Disusun untuk Memenuhi Tugas Perkuliahan Mobile Programming & Web Terpadu<br>
    Program Studi Pendidikan Teknologi Informasi - Universitas Lampung
  </p>
  <p style="text-align:center; text-indent:0; color:#2d3748; margin-top:12px;">
    <b>Pengembang:</b> Wemvi Afrialdo | <b>NPM:</b> 2413025052<br>
    <b>Dosen Pengampu:</b> Ghea Chandra Surawan, M.Pd.<br>
    <b>Cakupan Materi:</b> Laporan 1 & 2 (Instalasi), Laporan 3 (Backend API), Laporan 4 (Frontend Flutter), Laporan 5 (Portofolio SKPI), dan Laporan 6 (Push Notifikasi & Otomasi)
  </p>
</div>

<h2 class="chapter-title">LAPORAN 3<br>PENGEMBANGAN BACKEND API DAN KONFIGURASI BASIS DATA</h2>
<h3 class="section-title">1. Konfigurasi Lingkungan Backend (Laravel)</h3>
<p>Pada tahap ini, dilakukan persiapan lingkungan backend menggunakan framework Laravel versi 12. Konfigurasi awal difokuskan pada pengaturan variabel lingkungan di dalam file .env, khususnya untuk menghubungkan aplikasi Laravel dengan database relasional (MySQL) dan secret key HMAC-SHA256 untuk JWT Auth.</p>
<figure>
  <img src="laporan_screenshots/laporan3_01_env.png" alt="Konfigurasi .env Backend">
  <figcaption>Gambar 3.1: Konfigurasi file .env untuk koneksi database MySQL salut_db dan JWT Secret</figcaption>
</figure>

<h3 class="section-title">2. Pembuatan Struktur Database (Migration dan Model)</h3>
<p>Setelah koneksi berhasil, dirancang struktur database multi-role (Admin, Guru, Siswa Aktif, Alumni) menggunakan Migration Laravel agar skema database terstruktur, aman, dan mudah di-reproduksi.</p>
<figure>
  <img src="laporan_screenshots/laporan3_02_migration_model.png" alt="Kode Migration dan Model Laravel">
  <figcaption>Gambar 3.2: Struktur file Migration pada Laravel untuk relasi tabel akademik dan foreign key</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan3_03_phpmyadmin.png" alt="Tabel Database di phpMyAdmin">
  <figcaption>Gambar 3.3: Tampilan struktur tabel database salut_db yang berhasil di-migrate pada antarmuka phpMyAdmin</figcaption>
</figure>

<h3 class="section-title">3. Pembuatan Endpoint API dan Implementasi Autentikasi JWT</h3>
<p>Sistem SALUT menggunakan arsitektur Client-Server dengan 23 endpoint RESTful. Rute login publik disediakan pada POST /api/login, sedangkan rute modul lainnya diproteksi ketat menggunakan middleware jwt.auth.</p>
<figure>
  <img src="laporan_screenshots/laporan3_04_routes_api.png" alt="Kode Routing API Laravel">
  <figcaption>Gambar 3.4: Definisi rute RESTful API dan proteksi middleware jwt.auth pada file routes/api.php</figcaption>
</figure>

<h3 class="section-title">4. Pengujian API (API Testing)</h3>
<p>Pengujian dilakukan menggunakan perangkat lunak API Client. Server sukses merespons status 200 OK serta mengembalikan payload token akses JWT beserta objek data profil pengguna.</p>
<figure>
  <img src="laporan_screenshots/laporan3_05_api_testing.png" alt="Pengujian API Client 200 OK">
  <figcaption>Gambar 3.5: Hasil pengujian API login dengan status HTTP 200 OK dan respons payload token JWT</figcaption>
</figure>

<h3 class="section-title">5. Penyimpanan Repositori Backend ke GitHub</h3>
<p>Seluruh source code backend disimpan ke version control system GitHub pada repositori WEMVIAFRIALDO/apps_Sekolah-.</p>
<figure>
  <img src="laporan_screenshots/laporan3_06_git_push_backend.png" alt="Terminal Git Push Backend">
  <figcaption>Gambar 3.6: Eksekusi perintah git commit dan git push pada terminal PowerShell untuk backend Laravel</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan3_07_github_backend.png" alt="Repositori Backend di GitHub">
  <figcaption>Gambar 3.7: Tampilan repositori Backend SALUT yang telah tersinkronisasi di website GitHub</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">LAPORAN 4<br>PENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API</h2>
<h3 class="section-title">1. Pembuatan Antarmuka Pengguna (UI) Utama</h3>
<p>Pada tahap ini, pengembangan beralih ke mobile menggunakan framework Flutter. Dibuat halaman login_page.dart yang responsif dengan form validasi nomor induk dan kata sandi.</p>
<figure>
  <img src="laporan_screenshots/laporan4_01_login_page_code.png" alt="Kode Flutter Login Page">
  <figcaption>Gambar 4.1: Potongan kode antarmuka form validasi login pada file login_page.dart</figcaption>
</figure>

<h3 class="section-title">2. Integrasi HTTP Request dan Pengelolaan Token JWT</h3>
<p>Aplikasi Flutter dikonfigurasi menggunakan pustaka HTTP client Dio dengan arsitektur Interceptor pada ApiService untuk otomatisasi penyisipan Bearer Token pada setiap request keluar.</p>
<figure>
  <img src="laporan_screenshots/laporan4_02_api_service_code.png" alt="Kode ApiService Flutter Dio JWT">
  <figcaption>Gambar 4.2: Implementasi HTTP Client Dio dan Interceptor token JWT pada api_service.dart</figcaption>
</figure>

<h3 class="section-title">3. Simulasi dan Pengujian Antarmuka pada Perangkat Mobile</h3>
<p>Aplikasi dijalankan langsung pada gawai cerdas (smartphone) untuk menguji alur autentikasi dan rendering antarmuka pengguna.</p>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Halaman Login Aplikasi SALUT</div>
  <div class="note">Ambil tangkapan layar langsung dari HP saat membuka halaman Login SALUT</div>
</div>
<figcaption>Gambar 4.3: Tampilan antarmuka Login aplikasi SALUT pada perangkat mobile</figcaption>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Dashboard Siswa Aktif</div>
  <div class="note">Ambil tangkapan layar langsung dari HP setelah login akun Siswa Aktif (Budi Santoso)</div>
</div>
<figcaption>Gambar 4.4: Tampilan antarmuka Dashboard untuk peran Siswa Aktif (fitur Prestasi dan Rapor)</figcaption>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Dashboard Alumni</div>
  <div class="note">Ambil tangkapan layar langsung dari HP setelah login akun Alumni (Siti Rahayu)</div>
</div>
<figcaption>Gambar 4.5: Tampilan antarmuka Dashboard untuk peran Alumni (fitur Arsip Digital dan Tracer Study)</figcaption>

<h3 class="section-title">4. Implementasi Logika Dynamic UI Rendering Berdasarkan Role</h3>
<p>Menggunakan GetX state management, aplikasi secara otomatis menampilkan menu Prestasi bagi Siswa Aktif dan menu Arsip Digital & Tracer Study bagi Alumni.</p>
<figure>
  <img src="laporan_screenshots/laporan4_06_role_logic_code.png" alt="Kode Dynamic UI Role Dashboard">
  <figcaption>Gambar 4.6: Potongan kode logika pengkondisian tampilan menu per-role pada dashboard_page.dart</figcaption>
</figure>

<h3 class="section-title">5. Penyimpanan Repositori Frontend ke GitHub</h3>
<p>Pembaruan kode aplikasi mobile disimpan dan disinkronisasikan ke repositori GitHub.</p>
<figure>
  <img src="laporan_screenshots/laporan4_07_git_push_frontend.png" alt="Terminal Git Push Frontend Flutter">
  <figcaption>Gambar 4.7: Eksekusi git push kode frontend Flutter pada terminal PowerShell</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan4_08_github_frontend.png" alt="Repositori Frontend di GitHub">
  <figcaption>Gambar 4.8: Tampilan repositori direktori Flutter apps_sekolah di GitHub</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">LAPORAN 5<br>PENGEMBANGAN FITUR LANJUTAN EKOSISTEM KEJURUAN SMK (PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)</h2>
<h3 class="section-title">1. Perancangan Skema Database Portofolio Keahlian (SKPI)</h3>
<p>Dibuat tabel skill_competencies untuk mendokumentasikan capaian unit keahlian siswa SMK, nilai asesmen, tingkat kemahiran (Dasar, Terampil, Mahir), dan nama guru penguji LSP terlisensi BNSP.</p>
<figure>
  <img src="laporan_screenshots/laporan5_01_migration_skpi.png" alt="Migration SKPI">
  <figcaption>Gambar 5.1: Kode migration Laravel untuk pembuatan tabel skill_competencies (SKPI)</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan5_02_phpmyadmin_skpi.png" alt="Tabel phpMyAdmin SKPI">
  <figcaption>Gambar 5.2: Tampilan record data 136 unit kompetensi keahlian siswa pada phpMyAdmin</figcaption>
</figure>

<h3 class="section-title">2. Implementasi Controller API Portofolio Keahlian</h3>
<p>Dibangun SkillController.php dengan endpoint GET /api/skills/my yang menyajikan daftar capaian portofolio kejuruan siswa yang terautentikasi.</p>
<figure>
  <img src="laporan_screenshots/laporan5_03_skill_controller.png" alt="Controller Skill Laravel">
  <figcaption>Gambar 5.3: Implementasi SkillController.php pada backend Laravel</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan5_04_api_skills_test.png" alt="Pengujian API Skills">
  <figcaption>Gambar 5.4: Hasil pengujian endpoint GET /api/skills/my dengan respons 200 OK data portofolio</figcaption>
</figure>

<h3 class="section-title">3. Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)</h3>
<p>Pada aplikasi Flutter, dibangun antarmuka skills_page.dart yang menyajikan kartu-kartu sertifikasi kompetensi keahlian siswa secara interaktif.</p>
<figure>
  <img src="laporan_screenshots/laporan5_05_skills_page_code.png" alt="Kode Flutter Skills Page">
  <figcaption>Gambar 5.5: Kode antarmuka reactive GetX pada file skills_page.dart</figcaption>
</figure>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Halaman Portofolio Keahlian (SKPI)</div>
  <div class="note">Ambil tangkapan layar langsung dari HP pada menu Portofolio Keahlian SKPI</div>
</div>
<figcaption>Gambar 5.6: Tampilan antarmuka Portofolio Keahlian (SKPI) pada perangkat mobile</figcaption>

<h3 class="section-title">4. Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)</h3>
<p>Modul arsip_page.dart memfasilitasi alumni untuk melihat dan mengunduh berkas digital (Ijazah Asli, SKL, dan Transkrip Nilai) ber-watermark verifikasi sah.</p>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Halaman Arsip Digital Kelulusan</div>
  <div class="note">Ambil tangkapan layar langsung dari HP pada menu Arsip Digital Ijazah & SKL</div>
</div>
<figcaption>Gambar 5.7: Tampilan modul Arsip Digital Kelulusan dengan opsi unduh PDF terverifikasi pada HP</figcaption>

<h3 class="section-title">5. Sinkronisasi Repositori Fitur SKPI ke GitHub</h3>
<p>Pembaruan kode modul portofolio keahlian dan arsip digital disinkronisasikan ke repositori GitHub.</p>
<figure>
  <img src="laporan_screenshots/laporan5_08_git_push.png" alt="Git Push SKPI">
  <figcaption>Gambar 5.8: Terminal eksekusi git push pembaruan fitur SKPI dan arsip digital</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">LAPORAN 6<br>INTEGRASI PUSH NOTIFICATION, OTOMASI TRANSISI KELULUSAN, DAN PENGUJIAN MENYELURUH</h2>
<h3 class="section-title">1. Integrasi Push Notification Firebase Cloud Messaging (FCM)</h3>
<p>Dipasang fcm_service.dart untuk menangani penerimaan notifikasi siaran pengumuman kelulusan dan kuesioner tracer study secara langsung pada smartphone pengguna.</p>
<figure>
  <img src="laporan_screenshots/laporan6_01_fcm_service_code.png" alt="Kode FCM Service Flutter">
  <figcaption>Gambar 6.1: Potongan kode implementasi FcmService.dart menggunakan GetX service</figcaption>
</figure>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Banner Push Notifikasi Resmi</div>
  <div class="note">Ambil tangkapan layar langsung dari HP saat banner Push Notification kelulusan muncul di layar atas</div>
</div>
<figcaption>Gambar 6.2: Tampilan banner Push Notification resmi kelulusan pada perangkat mobile</figcaption>

<h3 class="section-title">2. Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)</h3>
<p>Dibangun command artisan salut:promote-alumni yang dijadwalkan otomatis setiap hari jam 00:00 untuk mengubah role siswa yang telah lulus menjadi alumni tanpa intervensi manual admin.</p>
<figure>
  <img src="laporan_screenshots/laporan6_03_cron_promote_code.png" alt="Kode Artisan Promote Alumni">
  <figcaption>Gambar 6.3: Kode logika otomasi command PromoteAlumni.php pada Laravel Console</figcaption>
</figure>
<figure>
  <img src="laporan_screenshots/laporan6_04_cron_execution_terminal.png" alt="Eksekusi Terminal Cron Job">
  <figcaption>Gambar 6.4: Log terminal eksekusi otomatis cron job salut:promote-alumni</figcaption>
</figure>

<h3 class="section-title">3. Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile</h3>
<p>Disediakan modul change_password_page.dart untuk validasi dan pembaruan kata sandi pengguna secara terenkripsi bcrypt.</p>
<figure>
  <img src="laporan_screenshots/laporan6_05_change_password_code.png" alt="Kode Change Password">
  <figcaption>Gambar 6.5: Potongan kode antarmuka dan validasi form pada change_password_page.dart</figcaption>
</figure>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Halaman Ubah Kata Sandi</div>
  <div class="note">Ambil tangkapan layar langsung dari HP pada halaman Ubah Kata Sandi akun</div>
</div>
<figcaption>Gambar 6.6: Tampilan antarmuka Ubah Kata Sandi pada perangkat mobile</figcaption>

<h3 class="section-title">4. Implementasi Kuesioner Tracer Study Alumni</h3>
<p>Kuesioner tracer study mencatat riwayat penyerapan kerja alumni (Bekerja, Kuliah, Wirausaha) beserta data nama perusahaan, prodi kampus, dan rentang penghasilan.</p>

<div class="mobile-placeholder">
  <div class="tag">TEMPAT SCREENSHOT ASLI DARI HP</div>
  <div class="title">Tampilan Kuesioner Tracer Study</div>
  <div class="note">Ambil tangkapan layar langsung dari HP pada formulir kuesioner Tracer Study Alumni</div>
</div>
<figcaption>Gambar 6.7: Tampilan pengisian kuesioner Tracer Study pada perangkat mobile</figcaption>

<h3 class="section-title">5. Analitik Ekosistem Kejuruan SMK pada Web Admin</h3>
<p>Web Admin panel menampilkan visualisasi data analitik penyerapan lulusan (65% bekerja di industri DUDI, 25% kuliah, 10% wirausaha/lainnya) serta top mitra institusi penyerap alumni.</p>
<figure>
  <img src="laporan_screenshots/laporan6_08_webadmin_smk_analytics.png" alt="Web Admin Analytics">
  <figcaption>Gambar 6.8: Tampilan dasbor analitik keterserapan alumni SMK pada Web Admin panel</figcaption>
</figure>

<h3 class="section-title">6. Rilis Final dan Tagging Repositori GitHub</h3>
<p>Setelah seluruh fitur diuji secara end-to-end dengan hasil 0 error, proyek dirilis secara resmi dengan tag v1.0.0-smk-release di GitHub.</p>
<figure>
  <img src="laporan_screenshots/laporan6_09_git_push_final.png" alt="Git Tag Final Release">
  <figcaption>Gambar 6.9: Terminal eksekusi rilis final dengan tagging v1.0.0-smk-release ke GitHub</figcaption>
</figure>

<div class="page-break"></div>

<h2 class="chapter-title">BAB VI: KESIMPULAN DAN REKOMENDASI PENGEMBANGAN</h2>
<h3 class="section-title">1. Kesimpulan</h3>
<p>Sistem SALUT telah berhasil diselesaikan secara menyeluruh, mencakup instalasi lingkungan (Laporan 1 & 2), integrasi backend RESTful API Laravel dan database MySQL (Laporan 3), aplikasi mobile Flutter (Laporan 4), ekosistem kejuruan SMK (Laporan 5), hingga otomasi push notifikasi dan cron job (Laporan 6).</p>

<h3 class="section-title">2. Rekomendasi</h3>
<p>Untuk masa depan, sistem dapat diperluas dengan integrasi sertifikat elektronik BSrE dan modul bursa kerja khusus (BKK) industri.</p>

</body>
</html>
"""
    with open(HTML_OUTPUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(HTML_PRIMARY, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(DOC_PRIMARY, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Berhasil menyimpan file HTML dan DOC dengan kotak placeholder!")

if __name__ == "__main__":
    merge_and_build()
    build_html_with_placeholders()
    print("Penggabungan dan pemformatan dokumen berhasil selesai!")
