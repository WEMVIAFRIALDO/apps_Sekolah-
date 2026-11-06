# -*- coding: utf-8 -*-
"""
Script Pembangun Otomatis Dokumen Laporan Proyek SALUT:
1. Laporan Perkembangan 1 (.docx)
2. Laporan Perkembangan 2 (.docx)
3. Laporan Perkembangan 3 (.docx)
4. Laporan Perkembangan 4 (.docx)
5. Laporan Akhir Lengkap (Laporan 7 Gabungan) (.docx)

STANDARISASI FORMAT:
- Font: Times New Roman
- Ukuran: 12 pt untuk SEMUA elemen (judul, subjudul, teks isi, tabel, caption)
- Judul & Subjudul: BOLD
- Warna: HITAM MURNI (RGB: 0, 0, 0) - Tidak ada font biru sama sekali
- Alignment: Rata Kanan-Kiri (JUSTIFIED)
- Spasi: 1.5 Spasi
Penulis: Wemvi Afrialdo (NPM: 2413025052)
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = r"d:\proyek_applikasi\apps_sekolah"
ROOT_DIR = r"d:\proyek_applikasi"
IMG_DIR = os.path.join(BASE_DIR, "laporan_screenshots")
SRS_IMG_DIR = os.path.join(BASE_DIR, "srs_mockup_images")
INST_IMG_DIR = os.path.join(IMG_DIR, "instalasi")

BLACK = RGBColor(0, 0, 0)

def create_document():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
    return doc

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_academic_cover(doc, title, subtitle):
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(6)
    p_inst.paragraph_format.line_spacing = 1.15
    r_inst = p_inst.add_run("KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI\nUNIVERSITAS LAMPUNG\nFAKULTAS KEGURUAN DAN ILMU PENDIDIKAN\nJURUSAN PENDIDIKAN MATEMATIKA DAN ILMU PENGETAHUAN ALAM\nPROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True
    r_inst.font.color.rgb = BLACK

    logo_path = os.path.join(INST_IMG_DIR, "logo_unila.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(14)
        p_logo.paragraph_format.space_after = Pt(14)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.8))

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(6)
    p_title.paragraph_format.line_spacing = 1.5
    r_title = p_title.add_run(title.upper())
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(12)
    r_title.font.bold = True
    r_title.font.color.rgb = BLACK

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(20)
    p_sub.paragraph_format.line_spacing = 1.5
    r_sub = p_sub.add_run(subtitle)
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = BLACK

    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.space_before = Pt(16)
    p_by.paragraph_format.space_after = Pt(4)
    p_by.paragraph_format.line_spacing = 1.5
    r_by = p_by.add_run("Disusun Oleh:\n")
    r_by.font.name = 'Times New Roman'
    r_by.font.size = Pt(12)
    r_by.font.color.rgb = BLACK
    
    r_nm = p_by.add_run("WEMVI AFRIALDO\nNPM. 2413025052")
    r_nm.font.name = 'Times New Roman'
    r_nm.font.size = Pt(12)
    r_nm.font.bold = True
    r_nm.font.color.rgb = BLACK

    p_ft = doc.add_paragraph()
    p_ft.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ft.paragraph_format.space_before = Pt(24)
    p_ft.paragraph_format.line_spacing = 1.5
    r_ft = p_ft.add_run("BANDAR LAMPUNG\n2026")
    r_ft.font.name = 'Times New Roman'
    r_ft.font.size = Pt(12)
    r_ft.font.bold = True
    r_ft.font.color.rgb = BLACK

    doc.add_page_break()

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = BLACK
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = BLACK
    return p

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.italic = True
    r.font.color.rgb = BLACK
    return p

def add_body(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.color.rgb = BLACK
    return p

def add_bullet(doc, bold_prefix, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.5
    r_sym = p.add_run("•  ")
    r_sym.font.name = 'Times New Roman'
    r_sym.font.size = Pt(12)
    r_sym.font.color.rgb = BLACK
    
    r1 = p.add_run(bold_prefix + ": ")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r1.font.color.rgb = BLACK
    
    r2 = p.add_run(text)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    r2.font.color.rgb = BLACK
    return p

def add_img(doc, img_filename_or_path, caption_text, width_inches=5.8):
    if os.path.isabs(img_filename_or_path):
        img_path = img_filename_or_path
    else:
        img_path = os.path.join(IMG_DIR, img_filename_or_path)
        if not os.path.exists(img_path):
            img_path = os.path.join(SRS_IMG_DIR, img_filename_or_path)
            
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=Inches(width_inches))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_cap.paragraph_format.space_after = Pt(10)
        p_cap.paragraph_format.line_spacing = 1.5
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(12)
        r_cap.font.italic = True
        r_cap.font.color.rgb = BLACK

def add_placeholder_box(doc, screen_title, instruction, caption_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(5.8)
    set_cell_background(cell, "F9F9F9")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="dashed" w:sz="8" w:space="0" w:color="000000"/>'
        f'<w:bottom w:val="dashed" w:sz="8" w:space="0" w:color="000000"/>'
        f'<w:left w:val="dashed" w:sz="8" w:space="0" w:color="000000"/>'
        f'<w:right w:val="dashed" w:sz="8" w:space="0" w:color="000000"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

    p1 = cell.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p1.paragraph_format.space_before = Pt(4)
    p1.paragraph_format.space_after = Pt(2)
    p1.paragraph_format.line_spacing = 1.5
    r1 = p1.add_run(f"📱 [AREA TEMPEL SCREENSHOT HP RESMI: {screen_title.upper()}]")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r1.font.color.rgb = BLACK

    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(4)
    p2.paragraph_format.line_spacing = 1.5
    r2 = p2.add_run(f"{instruction}. Anda dapat menempelkan (Paste) hasil tangkapan layar langsung dari HP ke dalam kotak ini.")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    r2.font.italic = True
    r2.font.color.rgb = BLACK

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cap.paragraph_format.space_before = Pt(4)
    p_cap.paragraph_format.space_after = Pt(12)
    p_cap.paragraph_format.line_spacing = 1.5
    r_cap = p_cap.add_run(caption_text)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(12)
    r_cap.font.italic = True
    r_cap.font.color.rgb = BLACK

# =============================================================================
# LAPORAN PERKEMBANGAN 1
# =============================================================================
def build_laporan_perkembangan_1():
    doc = create_document()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 1\nPENGEMBANGAN BACKEND API, STRUKTUR DATABASE, DAN AUTENTIKASI JWT SISTEM SALUT",
        "Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK Berbasis Client-Server")

    add_h1(doc, "LAPORAN PERKEMBANGAN PROYEK 1\nPENGEMBANGAN BACKEND API, STRUKTUR DATABASE, DAN SISTEM AUTENTIKASI JWT")
    
    add_h2(doc, "1. Konfigurasi Lingkungan Backend (Laravel 12 & MySQL)")
    add_body(doc,
        "Tahap awal pengembangan difokuskan pada penyiapan arsitektur server menggunakan framework PHP Laravel versi 12. "
        "Konfigurasi utama dilakukan pada file environment (.env) untuk menghubungkan backend dengan basis data relasional MySQL (db_salut). "
        "Konfigurasi ini memastikan server dapat melakukan operasi Create, Read, Update, Delete (CRUD) secara terenkripsi dan andal."
    )
    add_img(doc, "laporan3_01_env.png", "Gambar 1.1: Konfigurasi file environment (.env) untuk koneksi database MySQL pada backend Laravel")

    add_h2(doc, "2. Perancangan Struktur Database (Migrations dan Models)")
    add_body(doc,
        "Untuk mengakomodasi kebutuhan tata kelola data sekolah menengah kejuruan (SMK) yang dinamis, dirancang skema database menggunakan fitur "
        "Database Migrations Laravel. Skema mencakup tabel users (mendukung multi-role: Admin, Guru, Siswa, Alumni), student_profiles, "
        "academic_records, achievements, tracer_studies, dan graduation_schedules. Seluruh tabel direpresentasikan dalam Model Eloquent "
        "dengan relasi one-to-many dan one-to-one yang kokoh."
    )
    add_img(doc, "laporan3_02_migration_model.png", "Gambar 1.2: Potongan kode migration dan model Eloquent relasional pada VS Code")
    add_img(doc, "laporan3_03_phpmyadmin.png", "Gambar 1.3: Tampilan visual struktur tabel basis data db_salut yang telah berhasil dimigrasi di phpMyAdmin")

    add_h2(doc, "3. Pembuatan RESTful API Endpoint dan Keamanan JWT")
    add_body(doc,
        "Sistem SALUT mengusung arsitektur Client-Server murni, di mana pertukaran data antara aplikasi mobile, web admin, dan server "
        "dijembatani oleh RESTful API (Application Programming Interface). Untuk menjamin otorisasi yang aman tanpa state sesi (stateless), "
        "diimplementasikan JSON Web Token (JWT) menggunakan paket php-open-source-saver/jwt-auth. Rute login publik memverifikasi NISN dan kata sandi, "
        "lalu menerbitkan Bearer Token yang wajib disertakan pada setiap request menuju rute terproteksi middleware jwt.auth."
    )
    add_img(doc, "laporan3_04_routes_api.png", "Gambar 1.4: Definisi routing RESTful API dan proteksi middleware jwt.auth pada file routes/api.php")

    add_h2(doc, "4. Pengujian Endpoint API (API Testing 200 OK)")
    add_body(doc,
        "Sebelum diintegrasikan ke antarmuka aplikasi Flutter, seluruh endpoint API diuji secara menyeluruh menggunakan API Client. "
        "Pengujian fungsional pada endpoint otentikasi POST /api/login dengan parameter NISN dan password berhasil mengembalikan respons "
        "HTTP Status 200 OK beserta payload token JWT yang valid dan objek informasi profil pengguna."
    )
    add_img(doc, "laporan3_05_api_testing.png", "Gambar 1.5: Hasil pengujian API login dengan status HTTP 200 OK dan payload token JWT")

    add_h2(doc, "5. Manajemen Version Control dan Sinkronisasi ke GitHub")
    add_body(doc,
        "Sebagai bagian dari praktik rekayasa perangkat lunak standar industri, seluruh kode backend dan konfigurasi database didokumentasikan "
        "menggunakan version control system Git dan disinkronisasikan ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-. "
        "Hal ini menjamin integritas kode sumber dan rekam jejak perubahan proyek yang transparan."
    )
    add_img(doc, "laporan3_06_git_push_backend.png", "Gambar 1.6: Eksekusi terminal PowerShell untuk perintah git commit dan git push backend")
    add_img(doc, "laporan3_07_github_backend.png", "Gambar 1.7: Tampilan repositori Backend SALUT yang telah tersinkronisasi di website GitHub")

    doc.add_page_break()
    add_h1(doc, "RINGKASAN HASIL PERKEMBANGAN 1")
    add_bullet(doc, "Infrastruktur Backend Siap", "Backend Laravel 12 terkonfigurasi penuh dengan database relasional MySQL di port 8000.");
    add_bullet(doc, "Keamanan JWT Teruji", "Sistem autentikasi stateless Bearer Token JWT berfungsi 100% dengan respons payload lengkap.");
    add_bullet(doc, "Skema Database Multi-Role", "Tabel pengguna, profil akademik, prestasi, dan jadwal kelulusan berhasil di-migrate.");
    add_bullet(doc, "Repositori Terpusat", "Kode tersimpan rapi pada GitHub branch main.");

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_1.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_1.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai membuat Laporan Perkembangan 1:", out_docx)

# =============================================================================
# LAPORAN PERKEMBANGAN 2
# =============================================================================
def build_laporan_perkembangan_2():
    doc = create_document()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 2\nPENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API BERBASIS JWT",
        "Implementasi Dynamic UI Rendering Multi-Role Siswa Aktif dan Alumni SMK")

    add_h1(doc, "LAPORAN PERKEMBANGAN PROYEK 2\nPENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI API BERBASIS TOKEN JWT")
    
    add_h2(doc, "1. Perancangan Antarmuka Pengguna Mobile (Flutter)")
    add_body(doc,
        "Tahap perkembangan kedua berfokus pada pembangunan antarmuka mobile menggunakan framework Flutter. "
        "Desain antarmuka dirancang responsif dengan mengadopsi estetika clean academic modern. Komponen utama meliputi "
        "halaman autentikasi (login_page.dart) dengan validasi form nomor induk siswa (NISN) dan kata sandi, "
        "serta dasbor utama (dashboard_page.dart) dengan kartu ringkasan informasi akademik dan menu aksi cepat."
    )
    add_img(doc, "laporan4_01_login_page_code.png", "Gambar 2.1: Potongan kode antarmuka halaman login pada file login_page.dart")

    add_h2(doc, "2. Integrasi HTTP Client Dio dan Pengelolaan Token JWT")
    add_body(doc,
        "Aplikasi Flutter dihubungkan dengan Backend API Laravel melalui kelas ApiService yang memanfaatkan pustaka Dio HTTP Client. "
        "Diterapkan mekanisme Interceptor yang secara otomatis membaca token JWT dari media penyimpanan aman perangkat "
        "(flutter_secure_storage) dan menyematkannya pada header Authorization di setiap permintaan data ke server. "
        "Interceptor juga mendeteksi status 401 Unauthorized guna mengarahkan pengguna kembali ke halaman Login saat sesi berakhir."
    )
    add_img(doc, "laporan4_02_api_service_code.png", "Gambar 2.2: Implementasi HTTP Client Dio dan Interceptor token JWT pada api_service.dart")

    add_h2(doc, "3. Pengujian dan Simulasi Antarmuka pada Perangkat")
    add_body(doc,
        "Aplikasi mobile dikompilasi dan dijalankan pada emulator Android serta perangkat fisik HP Samsung. "
        "Pengujian memvalidasi dua skenario login peran: akun Siswa Aktif (Budi Santoso) dan akun Alumni (Siti Rahayu)."
    )
    add_img(doc, "laporan4_03_login_mobile_app.png", "Gambar 2.3: Tampilan antarmuka Login aplikasi SALUT pada perangkat mobile", width_inches=3.0)
    add_placeholder_box(doc, "Halaman Login Mobile", "Ambil tangkapan layar langsung dari HP saat berada di halaman Login SALUT", "Gambar 2.4: Tangkapan layar fisik antarmuka Login di HP")
    
    add_img(doc, "laporan4_04_dashboard_siswa_app.png", "Gambar 2.5: Tampilan antarmuka Dashboard untuk peran Siswa Aktif", width_inches=3.0)
    add_placeholder_box(doc, "Dashboard Siswa Aktif", "Ambil tangkapan layar langsung dari HP saat login sebagai Siswa Aktif (Budi Santoso)", "Gambar 2.6: Tangkapan layar fisik Dashboard Siswa Aktif di HP")
    
    add_img(doc, "laporan4_05_dashboard_alumni_app.png", "Gambar 2.7: Tampilan antarmuka Dashboard untuk peran Alumni", width_inches=3.0)
    add_placeholder_box(doc, "Dashboard Alumni", "Ambil tangkapan layar langsung dari HP saat login sebagai Alumni (Siti Rahayu)", "Gambar 2.8: Tangkapan layar fisik Dashboard Alumni di HP")

    add_h2(doc, "4. Penerapan Logika Dynamic UI Rendering Berbasis Peran")
    add_body(doc,
        "Menggunakan reactive state management GetX, antarmuka aplikasi SALUT dapat bertransformasi secara dinamis menyesuaikan data peran (role) "
        "yang diperoleh dari payload token JWT. Jika pengguna berstatus 'Siswa Aktif', menu yang ditampilkan berfokus pada pemantauan nilai rapor "
        "dan pengajuan prestasi; sebaliknya jika berstatus 'Alumni', tampilan otomatis berubah menyajikan menu arsip dokumen ijazah sah dan kuesioner tracer study."
    )
    add_img(doc, "laporan4_06_role_logic_code.png", "Gambar 2.9: Potongan kode logika pengkondisian tampilan menu per-role pada dashboard_page.dart")

    add_h2(doc, "5. Sinkronisasi Kode Frontend ke Repositori GitHub")
    add_body(doc,
        "Seluruh pembaruan antarmuka mobile Flutter, GetX controller, model data, dan service disinkronisasikan ke repositori GitHub."
    )
    add_img(doc, "laporan4_07_git_push_frontend.png", "Gambar 2.10: Terminal eksekusi git push kode frontend Flutter pada PowerShell")
    add_img(doc, "laporan4_08_github_frontend.png", "Gambar 2.11: Tampilan repositori direktori Flutter apps_sekolah di GitHub")

    doc.add_page_break()
    add_h1(doc, "RINGKASAN HASIL PERKEMBANGAN 2")
    add_bullet(doc, "UI Mobile Responsif & Elegan", "Halaman Login dan Dashboard Siswa/Alumni berhasil diwujudkan dalam Flutter.");
    add_bullet(doc, "Integrasi Dio JWT Sempurna", "Komunikasi HTTP Client Dio dan flutter_secure_storage berjalan lancar.");
    add_bullet(doc, "Dynamic UI Rendering Terbukti", "Perubahan tampilan berdasarkan role Siswa vs Alumni bekerja otomatis.");
    add_bullet(doc, "Sinkronisasi Repositori", "Branch main memuat seluruh source code frontend Flutter.");

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_2.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_2.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai membuat Laporan Perkembangan 2:", out_docx)

# =============================================================================
# LAPORAN PERKEMBANGAN 3
# =============================================================================
def build_laporan_perkembangan_3():
    doc = create_document()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 3\nPENGEMBANGAN FITUR EKOSISTEM KEJURUAN SMK (PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)",
        "Pencatatan Kompetensi Keahlian Siswa dan Validasi Kelulusan Digital Terverifikasi")

    add_h1(doc, "LAPORAN PERKEMBANGAN PROYEK 3\nPENGEMBANGAN FITUR EKOSISTEM KEJURUAN SMK (PORTOFOLIO SKPI & ARSIP DOKUMEN DIGITAL)")
    
    add_h2(doc, "1. Perancangan Skema Database Portofolio Keahlian (SKPI)")
    add_body(doc,
        "Untuk memenuhi kebutuhan spesifik Sekolah Menengah Kejuruan (SMK), nilai akademik ijazah perlu dilengkapi dengan Surat Keterangan Pendamping "
        "Ijazah (SKPI) yang memuat unit kompetensi keahlian standar SKKNI dan BNSP. Dirancang migration tabel baru skill_competencies "
        "yang memuat data user_id, competence_code, competence_name, competency_level (Dasar, Terampil, Mahir), score asesmen, dan verified_by (asesor)."
    )
    add_img(doc, "laporan5_01_migration_skpi.png", "Gambar 3.1: Kode migration Laravel untuk pembuatan tabel skill_competencies (SKPI)")
    add_img(doc, "laporan5_02_phpmyadmin_skpi.png", "Gambar 3.2: Tampilan record data 136 unit kompetensi keahlian siswa pada phpMyAdmin")

    add_h2(doc, "2. Implementasi Endpoint API Portofolio Keahlian")
    add_body(doc,
        "Pada sisi backend dibangun SkillController.php dengan endpoint utama GET /api/skills/my. Endpoint ini menyajikan daftar seluruh unit "
        "kompetensi kejuruan yang telah diselesaikan oleh siswa terautentikasi sesuai bidang jurusannya (RPL, TKJ, atau Multimedia). "
        "Pengujian endpoint menunjukkan respons 200 OK dengan payload data kompetensi yang lengkap."
    )
    add_img(doc, "laporan5_03_skill_controller.png", "Gambar 3.3: Implementasi SkillController.php pada backend Laravel")
    add_img(doc, "laporan5_04_api_skills_test.png", "Gambar 3.4: Hasil pengujian endpoint GET /api/skills/my dengan respons 200 OK")

    add_h2(doc, "3. Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)")
    add_body(doc,
        "Pada aplikasi Flutter, dibangun antarmuka skills_page.dart yang menyajikan kartu-kartu capaian unit kompetensi keahlian. "
        "Setiap kartu memuat rincian kode unit, predikat kemahiran dengan badge warna informatif (Mahir hijau, Terampil oranye), skor capaian, "
        "dan nama asesor penguji, serta dilengkapi tombol aksi untuk mengunduh berkas SKPI resmi."
    )
    add_img(doc, "laporan5_05_skills_page_code.png", "Gambar 3.5: Kode antarmuka reactive GetX pada file skills_page.dart")
    add_img(doc, "laporan5_06_skills_mobile_app.png", "Gambar 3.6: Tampilan antarmuka Portofolio Keahlian (SKPI) pada mobile app", width_inches=3.0)
    add_placeholder_box(doc, "Portofolio Keahlian SKPI", "Ambil tangkapan layar langsung dari HP pada menu Portofolio Keahlian SKPI", "Gambar 3.7: Tangkapan layar fisik modul SKPI di HP")

    add_h2(doc, "4. Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)")
    add_body(doc,
        "Untuk mencegah kerusakan atau kehilangan ijazah fisik serta mempermudah legalisir digital bagi alumni, dibangun modul arsip_page.dart. "
        "Alumni dapat melihat dan mengunduh berkas digital (Ijazah Asli, SKL, dan Transkrip Nilai) yang telah dibubuhi QR-Code verifikasi resmi dan Tanda Tangan Elektronik."
    )
    add_img(doc, "laporan5_07_arsip_mobile_app.png", "Gambar 3.8: Tampilan modul Arsip Digital Kelulusan dengan opsi unduh PDF pada mobile", width_inches=3.0)
    add_placeholder_box(doc, "Arsip Digital Kelulusan", "Ambil tangkapan layar langsung dari HP pada menu Arsip Dokumen Digital Ijazah", "Gambar 3.9: Tangkapan layar fisik modul Arsip Digital di HP")

    add_h2(doc, "5. Sinkronisasi Repositori Fitur SKPI ke GitHub")
    add_body(doc,
        "Seluruh controller, migration kejuruan SMK, dan modul antarmuka Flutter disinkronisasikan ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )
    add_img(doc, "laporan5_08_git_push.png", "Gambar 3.10: Terminal eksekusi git push pembaruan fitur SKPI dan arsip digital")

    doc.add_page_break()
    add_h1(doc, "RINGKASAN HASIL PERKEMBANGAN 3")
    add_bullet(doc, "Standar Kejuruan SMK Terwujud", "Tabel skill_competencies dan SKPI berhasil merekam kompetensi siswa per jurusan.");
    add_bullet(doc, "API Portofolio Terintegrasi", "Endpoint /api/skills/my menyajikan data kompetensi dan asesor penguji berlisensi.");
    add_bullet(doc, "Arsip Digital Terlindungi", "Ijazah dan SKL digital tersimpan aman dalam format PDF ber-TTE.");
    add_bullet(doc, "Sinkronisasi Kode", "Seluruh fitur terdokumentasi rapi pada commit Git terbaru.");

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_3.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_3.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai membuat Laporan Perkembangan 3:", out_docx)

# =============================================================================
# LAPORAN PERKEMBANGAN 4
# =============================================================================
def build_laporan_perkembangan_4():
    doc = create_document()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 4\nINTEGRASI PUSH NOTIFICATION, OTOMASI CRON JOB TRANSISI KELULUSAN, MODUL KEAMANAN, TRACER STUDY & RILIS FINAL",
        "Otomatisasi Sistem Akademik dan Monitoring Penyerapan Lulusan SMK")

    add_h1(doc, "LAPORAN PERKEMBANGAN PROYEK 4\nINTEGRASI PUSH NOTIFICATION, OTOMASI TRANSISI KELULUSAN, DAN PENGUJIAN MENYELURUH (END-TO-END)")
    
    add_h2(doc, "1. Integrasi Push Notification Firebase Cloud Messaging (FCM)")
    add_body(doc,
        "Untuk memastikan pengumuman kelulusan dan agenda tracer study diterima seketika oleh pengguna, diintegrasikan layanan Firebase Cloud Messaging (FCM). "
        "File fcm_service.dart menangani pendaftaran token perangkat, penerimaan notifikasi saat aplikasi dibuka (foreground), "
        "dan penanganan pesan di latar belakang (background handler)."
    )
    add_img(doc, "laporan6_01_fcm_service_code.png", "Gambar 4.1: Kode implementasi FcmService.dart menggunakan GetX service")
    add_img(doc, "laporan6_02_fcm_notification_app.png", "Gambar 4.2: Tampilan banner Push Notification resmi kelulusan pada mobile app", width_inches=3.0)
    add_placeholder_box(doc, "Banner Push Notification", "Ambil tangkapan layar langsung dari HP saat banner Push Notification muncul di bagian atas layar", "Gambar 4.3: Tangkapan layar fisik push notifikasi di HP")

    add_h2(doc, "2. Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)")
    add_body(doc,
        "Untuk meniadakan proses manual pemindahan status siswa, dibangun custom Artisan command: salut:promote-alumni. "
        "Perintah ini dijadwalkan secara berkala (cron job) setiap hari jam 00:00. Sistem secara otomatis memeriksa tanggal kelulusan, "
        "mengubah role 190 siswa aktif menjadi alumni, dan memicu pengiriman notifikasi FCM ke perangkat pengguna."
    )
    add_img(doc, "laporan6_03_cron_promote_code.png", "Gambar 4.4: Kode logika otomasi command PromoteAlumni.php pada Laravel Console")
    add_img(doc, "laporan6_04_cron_execution_terminal.png", "Gambar 4.5: Log terminal eksekusi otomatis cron job salut:promote-alumni")

    add_h2(doc, "3. Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile")
    add_body(doc,
        "Sesuai prinsip keamanan data pengguna, dibangun halaman change_password_page.dart. Pengguna dapat memperbarui kata sandi "
        "dengan validasi pencocokan kata sandi baru dan enkripsi bcrypt melalui endpoint terproteksi PATCH /api/profile/password."
    )
    add_img(doc, "laporan6_05_change_password_code.png", "Gambar 4.6: Potongan kode antarmuka dan validasi form pada change_password_page.dart")
    add_img(doc, "laporan6_06_change_password_app.png", "Gambar 4.7: Tampilan antarmuka Ubah Kata Sandi pada perangkat mobile", width_inches=3.0)
    add_placeholder_box(doc, "Halaman Ubah Kata Sandi", "Ambil tangkapan layar langsung dari HP pada halaman Ubah Kata Sandi akun", "Gambar 4.8: Tangkapan layar fisik modul ganti password di HP")

    add_h2(doc, "4. Implementasi Kuesioner Tracer Study Alumni")
    add_body(doc,
        "Aplikasi mobile menyediakan kuesioner dinamis untuk melacak keterserapan alumni (Bekerja, Melanjutkan Kuliah, Wirausaha). "
        "Data yang dikumpulkan mencakup nama perusahaan/kampus, sektor industri, rentang penghasilan pertama, dan tingkat keselarasan kurikulum."
    )
    add_img(doc, "laporan6_07_tracer_study_app.png", "Gambar 4.9: Tampilan pengisian kuesioner Tracer Study pada perangkat mobile", width_inches=3.0)
    add_placeholder_box(doc, "Kuesioner Tracer Study", "Ambil tangkapan layar langsung dari HP pada formulir kuesioner Tracer Study Alumni", "Gambar 4.10: Tangkapan layar fisik form tracer study di HP")

    add_h2(doc, "5. Analitik Ekosistem Kejuruan SMK pada Web Admin")
    add_body(doc,
        "Data hasil tracer study dan capaian keahlian diolah secara visual pada dashboard Web Admin (dashboard.html). "
        "Pihak manajemen sekolah dapat memantau distribusi keterserapan lulusan (65% bekerja di DUDI, 25% kuliah, 10% wirausaha/lainnya), "
        "serta leaderboard 5 mitra industri dan kampus penyerap lulusan terbanyak."
    )
    add_img(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 4.11: Tampilan dasbor analitik keterserapan alumni SMK pada Web Admin panel")

    add_h2(doc, "6. Rilis Final dan Tagging Repositori GitHub")
    add_body(doc,
        "Setelah seluruh pengujian integrasi akhir selesai dengan hasil 0 error, proyek dirilis secara resmi dengan tag "
        "v1.0.0-smk-release pada repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )
    add_img(doc, "laporan6_09_git_push_final.png", "Gambar 4.12: Terminal eksekusi rilis final dengan tagging v1.0.0-smk-release ke GitHub")

    doc.add_page_break()
    add_h1(doc, "RINGKASAN HASIL PERKEMBANGAN 4")
    add_bullet(doc, "Notifikasi Real-Time", "FCM aktif mengirimkan push notification pengumuman kelulusan ke HP siswa.");
    add_bullet(doc, "Otomasi Transisi Mandiri", "Cron job salut:promote-alumni mengubah role siswa ke alumni otomatis jam 00:00.");
    add_bullet(doc, "Tracer Study Komprehensif", "Alumni dapat mengisi kuesioner penyerapan kerja dan kuliah.");
    add_bullet(doc, "Analitik Web Admin Siap", "Visualisasi chart keterserapan kerja SMK tersaji interaktif.");

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_4.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_4.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai membuat Laporan Perkembangan 4:", out_docx)

# =============================================================================
# LAPORAN AKHIR LENGKAP (GABUNGAN + TIMELINE + PROTOTYPE 4 ROLE)
# =============================================================================
def build_laporan_akhir_lengkap():
    doc = create_document()
    add_academic_cover(doc, 
        "LAPORAN AKHIR PROYEK PERANGKAT LUNAK\nRANCANG BANGUN SISTEM INFORMASI ARSIP KELULUSAN DAN TRACER STUDY ALUMNI SMK (SALUT) BERBASIS MOBILE FLUTTER DAN WEB LARAVEL",
        "Dokumen Komprehensif Perancangan, Instalasi, Perkembangan, Timeline, dan Prototype Akhir Sistem Multi-Role")

    # KATA PENGANTAR
    add_h1(doc, "KATA PENGANTAR")
    add_body(doc,
        "Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan hidayah-Nya sehingga Laporan Akhir "
        "Pengembangan Proyek Perangkat Lunak 'SALUT' (Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK) ini dapat diselesaikan dengan baik. "
        "Laporan ini merupakan rangkuman utuh dari seluruh tahapan siklus hidup pengembangan perangkat lunak (SDLC), mencakup perancangan spesifikasi "
        "kebutuhan (SRS & Mockup), instalasi dan konfigurasi lingkungan pengembangan, perkembangan arsitektur backend dan database, antarmuka mobile Flutter, "
        "integrasi portofolio kejuruan SMK (SKPI), otomasi transisi kelulusan, jadwal linimasa proyek, serta pengujian prototype akhir pada seluruh aktor sistem."
    )
    add_body(doc,
        "Penulis menyadari bahwa keberhasilan proyek ini tidak lepas dari bimbingan, arahan, dan dukungan berbagai pihak. Semoga perangkat lunak "
        "yang telah dibangun ini dapat memberikan kontribusi nyata bagi transformasi tata kelola arsip digital dan pelacakan keterserapan alumni di sekolah menengah kejuruan."
    )
    
    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(14)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\n\n\nPenulis,\nWemvi Afrialdo")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    doc.add_page_break()

    # DAFTAR ISI RINGKAS
    add_h1(doc, "DAFTAR ISI")
    daftar_isi = [
        ("BAB I", "RINGKASAN DESAIN DAN MOCKUP SISTEM (LAPORAN 1)", "3"),
        ("BAB II", "INSTALASI DAN LINGKUNGAN PENGEMBANGAN (LAPORAN 2)", "7"),
        ("BAB III", "LAPORAN PERKEMBANGAN 1: BACKEND API DAN DATABASE", "12"),
        ("BAB IV", "LAPORAN PERKEMBANGAN 2: FRONTEND MOBILE DAN INTEGRASI JWT", "17"),
        ("BAB V", "LAPORAN PERKEMBANGAN 3: FITUR KEJURUAN SMK (SKPI & ARSIP)", "22"),
        ("BAB VI", "LAPORAN PERKEMBANGAN 4: PUSH NOTIF, OTOMASI & TRACER STUDY", "27"),
        ("BAB VII", "TIMELINE PELAKSANAAN DAN PERKEMBANGAN PROYEK", "32"),
        ("BAB VIII", "PROTOTYPE AKHIR APLIKASI SISTEM SALUT LENGKAP 4 ROLE", "35"),
        ("BAB IX", "KESIMPULAN DAN REKOMENDASI PENGEMBANGAN", "45"),
    ]
    for b_code, b_title, b_page in daftar_isi:
        p_toc = doc.add_paragraph()
        p_toc.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_toc.paragraph_format.space_after = Pt(4)
        p_toc.paragraph_format.line_spacing = 1.5
        r1 = p_toc.add_run(f"{b_code}: {b_title}")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(12)
        r1.font.bold = True
        r1.font.color.rgb = BLACK
        
        dots_count = max(4, 70 - len(b_code) - len(b_title))
        r_dots = p_toc.add_run(" " + "." * dots_count + " ")
        r_dots.font.name = 'Times New Roman'
        r_dots.font.size = Pt(12)
        r_dots.font.color.rgb = BLACK
        
        r2 = p_toc.add_run(b_page)
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(12)
        r2.font.bold = True
        r2.font.color.rgb = BLACK

    doc.add_page_break()

    # BAB I: MOCKUP DESAIN (LAPORAN 1)
    add_h1(doc, "BAB I\nRINGKASAN DESAIN DAN MOCKUP SISTEM (LAPORAN 1)")
    add_h2(doc, "1.1 Deskripsi Umum Kebutuhan Sistem (SRS SALUT)")
    add_body(doc,
        "Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK (SALUT) dirancang untuk memecahkan problematika "
        "pengelolaan dokumen kelulusan yang masih terfragmentasi, risiko kerusakan fisik arsip ijazah, serta kesulitan pelacakan "
        "keterserapan lulusan ke dunia kerja dan perguruan tinggi. Sistem ini dibangun dengan arsitektur Client-Server yang melayani siklus hidup "
        "data siswa sejak awal masuk jenjang SMK hingga menjadi alumni."
    )
    add_body(doc,
        "Antarmuka sistem terdiri dari dua bagian utama: Panel Web Admin yang diperuntukkan bagi Administrator Tata Usaha dan Guru "
        "untuk melakukan manajemen master data, penginputan nilai rapor, dan verifikasi kompetensi keahlian; serta Aplikasi Mobile "
        "berbasis Flutter untuk Siswa Aktif dan Alumni yang menerapkan konsep Dynamic UI Rendering."
    )

    add_h2(doc, "1.2 Desain Mockup Antarmuka Mobile (Android)")
    add_body(doc,
        "Antarmuka mobile dirancang dengan memprioritaskan kemudahan akses satu tangan, tipografi yang jelas, serta navigasi yang adaptif. "
        "Pada bagian bawah layar disediakan bottom navigation bar yang memuat menu utama, tombol aksi cepat di posisi atas yang mudah dijangkau, "
        "serta kotak pencarian dan filter data terstruktur."
    )
    add_img(doc, "image12.png", "Gambar 1.1: Desain Mockup Antarmuka Mobile Android - Halaman Manajemen dan Akses Data Pengguna", width_inches=2.8)
    add_img(doc, "image13.png", "Gambar 1.2: Desain Mockup Antarmuka Mobile Android - Navigasi dan Filter Kategori Pengguna", width_inches=2.8)

    add_h2(doc, "1.3 Desain Mockup Antarmuka Desktop (Web Admin Panel)")
    add_body(doc,
        "Antarmuka desktop dirancang sebagai pusat kendali terintegrasi (Command Center) bagi pihak manajemen sekolah. "
        "Tersedia sidebar navigasi di sisi kiri, kartu statistik ringkasan di bagian atas, bilah aksi cepat untuk ekspor data CSV dan impor siswa massal, "
        "serta tabel master data yang dilengkapi paginasi dan filter peran (Admin, Guru, Siswa, Alumni)."
    )
    add_img(doc, "image14.png", "Gambar 1.3: Desain Mockup Antarmuka Desktop Web Admin - Panel Manajemen Civitas Akademika", width_inches=5.8)

    doc.add_page_break()

    # BAB II: INSTALASI DAN LINGKUNGAN PENGEMBANGAN (LAPORAN 2)
    add_h1(doc, "BAB II\nINSTALASI DAN KONFIGURASI LINGKUNGAN PENGEMBANGAN (LAPORAN 2)")
    add_h2(doc, "2.1 Penyiapan Flutter SDK dan Dart")
    add_body(doc,
        "Langkah pertama penyiapan lingkungan frontend mobile adalah mengunduh Flutter SDK versi 3.x stabil dari portal resmi flutter.dev, "
        "kemudian mengekstrak paket ke direktori sistem lokal. Selanjutnya, path bin direktori Flutter didaftarkan ke variabel lingkungan sistem "
        "(Environment Variables PATH) agar perintah flutter dan dart dapat diakses dari terminal PowerShell mana pun."
    )
    add_img(doc, os.path.join(INST_IMG_DIR, "step01_flutter_website.png"), "Gambar 2.1: Portal resmi Flutter untuk pengunduhan SDK stabil")
    add_img(doc, os.path.join(INST_IMG_DIR, "step02_download_flutter_zip.png"), "Gambar 2.2: Berkas instalasi zip Flutter SDK pada direktori penyimpanan")
    add_img(doc, os.path.join(INST_IMG_DIR, "step03_environment_variables.png"), "Gambar 2.3: Konfigurasi System Environment Variables PATH pada sistem operasi Windows")
    add_img(doc, os.path.join(INST_IMG_DIR, "step04_flutter_version_cmd.png"), "Gambar 2.4: Verifikasi instalasi Flutter SDK dan Dart pada terminal Command Prompt")

    add_h2(doc, "2.2 Konfigurasi Java Development Kit (JDK 21) dan Android SDK")
    add_body(doc,
        "Untuk kebutuhan kompilasi Gradle ke platform Android, dipasang Java Development Kit versi 21 (JDK 21 LTS). Variabel sistem JAVA_HOME "
        "dikonfigurasikan menuju folder instalasi JDK. Selain itu, dipasang komponen Android SDK Build-Tools, NDK, dan CMake melalui Android Studio SDK Manager."
    )
    add_img(doc, os.path.join(INST_IMG_DIR, "step05_download_jdk21.png"), "Gambar 2.5: Berkas instalasi Java Development Kit 21 (JDK 21 LTS)")
    add_img(doc, os.path.join(INST_IMG_DIR, "step06_java_version_terminal.png"), "Gambar 2.6: Verifikasi versi Java runtime pada terminal")
    add_img(doc, os.path.join(INST_IMG_DIR, "step09_android_sdk_tools_cmake.png"), "Gambar 2.7: Konfigurasi Android SDK Command-line Tools dan CMake")
    add_img(doc, os.path.join(INST_IMG_DIR, "step10_android_ndk_installed.png"), "Gambar 2.8: Status instalasi Android NDK pada SDK Tools")

    add_h2(doc, "2.3 Konfigurasi Editor Visual Studio Code dan Flutter Doctor")
    add_body(doc,
        "Visual Studio Code digunakan sebagai Integrated Development Environment (IDE) utama. Dipasang ekstensi resmi Flutter dan Dart "
        "yang menyediakan fitur sintaks highlighting, widget inspector, dan hot-reload instan. Eksekusi flutter doctor mengonfirmasi bahwa "
        "seluruh komponen rantai perkakas (toolchain) berada dalam kondisi optimal tanpa kendala."
    )
    add_img(doc, os.path.join(INST_IMG_DIR, "step07_vscode_flutter_extension.png"), "Gambar 2.9: Instalasi ekstensi Flutter pada VS Code")
    add_img(doc, os.path.join(INST_IMG_DIR, "step08_vscode_dart_extension.png"), "Gambar 2.10: Instalasi ekstensi bahasa pemrograman Dart")
    add_img(doc, os.path.join(INST_IMG_DIR, "step11_flutter_doctor_output.png"), "Gambar 2.11: Hasil diagnosa perintah flutter doctor dengan status seluruh komponen centang hijau")

    doc.add_page_break()

    # BAB III: LAPORAN PERKEMBANGAN 1 (RINGKASAN BAB)
    add_h1(doc, "BAB III\nLAPORAN PERKEMBANGAN PROYEK 1: PENGEMBANGAN BACKEND API, DATABASE, DAN JWT")
    add_body(doc,
        "Pada tahap perkembangan 1, arsitektur server backend dibangun menggunakan framework PHP Laravel 12. "
        "Fokus utama mencakup integrasi basis data MySQL melalui konfigurasi file .env, pembuatan skema tabel multi-role dengan Migration, "
        "penyusunan Model Eloquent, implementasi mekanisme autentikasi stateless JSON Web Token (JWT), pengujian respon API 200 OK, "
        "serta pengarsipan kode sumber ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )
    add_img(doc, "laporan3_01_env.png", "Gambar 3.1: Konfigurasi variabel lingkungan .env untuk koneksi basis data MySQL")
    add_img(doc, "laporan3_03_phpmyadmin.png", "Gambar 3.2: Tampilan tabel database db_salut yang berhasil di-migrate pada phpMyAdmin")
    add_img(doc, "laporan3_04_routes_api.png", "Gambar 3.3: Definisi routing RESTful API terproteksi JWT pada routes/api.php")
    add_img(doc, "laporan3_05_api_testing.png", "Gambar 3.4: Hasil pengujian API login dengan balasan HTTP 200 OK dan token JWT")
    add_img(doc, "laporan3_07_github_backend.png", "Gambar 3.5: Repositori Backend Laravel SALUT yang tersinkronisasi di GitHub")

    doc.add_page_break()

    # BAB IV: LAPORAN PERKEMBANGAN 2 (RINGKASAN BAB)
    add_h1(doc, "BAB IV\nLAPORAN PERKEMBANGAN PROYEK 2: FRONTEND MOBILE FLUTTER DAN INTEGRASI JWT")
    add_body(doc,
        "Tahap perkembangan 2 melanjutkan pembuatan antarmuka mobile menggunakan Flutter. Dibangun halaman login_page.dart "
        "dan dashboard_page.dart dengan memanfaatkan Dio HTTP Client dan interceptor JWT untuk otorisasi bearer token. "
        "Aplikasi menerapkan Dynamic UI Rendering menggunakan GetX state management sehingga antarmuka Siswa Aktif dan Alumni "
        "dapat berubah secara adaptif sesuai peran pengguna."
    )
    add_img(doc, "laporan4_01_login_page_code.png", "Gambar 4.1: Kode antarmuka login form pada login_page.dart")
    add_img(doc, "laporan4_02_api_service_code.png", "Gambar 4.2: Implementasi HTTP Client Dio dan interceptor JWT pada api_service.dart")
    add_img(doc, "laporan4_04_dashboard_siswa_app.png", "Gambar 4.3: Tampilan antarmuka Dashboard Siswa Aktif", width_inches=2.8)
    add_img(doc, "laporan4_05_dashboard_alumni_app.png", "Gambar 4.4: Tampilan antarmuka Dashboard Alumni", width_inches=2.8)
    add_img(doc, "laporan4_06_role_logic_code.png", "Gambar 4.5: Kode logika kondisional Dynamic UI Rendering pada dashboard_page.dart")

    doc.add_page_break()

    # BAB V: LAPORAN PERKEMBANGAN 3 (RINGKASAN BAB)
    add_h1(doc, "BAB V\nLAPORAN PERKEMBANGAN PROYEK 3: FITUR EKOSISTEM KEJURUAN SMK (SKPI & ARSIP DIGITAL)")
    add_body(doc,
        "Tahap perkembangan 3 didedikasikan untuk penyesuaian sistem dengan ekosistem kejuruan SMK. Dibuat tabel database skill_competencies "
        "untuk menampung 136 unit kompetensi keahlian siswa (SKPI), endpoint backend SkillController.php (GET /api/skills/my), antarmuka mobile "
        "skills_page.dart, serta modul arsip dokumen kelulusan digital (arsip_page.dart) untuk pengunduhan ijazah dan SKL ber-TTE."
    )
    add_img(doc, "laporan5_01_migration_skpi.png", "Gambar 5.1: Migration tabel skill_competencies untuk modul SKPI SMK")
    add_img(doc, "laporan5_04_api_skills_test.png", "Gambar 5.2: Uji endpoint GET /api/skills/my dengan respon data kejuruan 200 OK")
    add_img(doc, "laporan5_06_skills_mobile_app.png", "Gambar 5.3: Antarmuka Portofolio Keahlian (SKPI) pada mobile app", width_inches=2.8)
    add_img(doc, "laporan5_07_arsip_mobile_app.png", "Gambar 5.4: Modul Arsip Digital Kelulusan dengan tombol unduh berkas", width_inches=2.8)

    doc.add_page_break()

    # BAB VI: LAPORAN PERKEMBANGAN 4 (RINGKASAN BAB)
    add_h1(doc, "BAB VI\nLAPORAN PERKEMBANGAN PROYEK 4: PUSH NOTIFICATION, OTOMASI CRON & TRACER STUDY")
    add_body(doc,
        "Tahap perkembangan 4 mengintegrasikan layanan Push Notification Firebase Cloud Messaging (FCM) melalui fcm_service.dart, "
        "otomasi transisi kelulusan massal dengan scheduled cron job command salut:promote-alumni setiap jam 00:00, modul keamanan "
        "ubah kata sandi mobile, kuesioner dinamis tracer study penyerapan alumni, visualisasi analitik pada dashboard Web Admin, "
        "serta rilis final proyek dengan tagging versi v1.0.0-smk-release di GitHub."
    )
    add_img(doc, "laporan6_01_fcm_service_code.png", "Gambar 6.1: Implementasi FcmService.dart untuk notifikasi kelulusan")
    add_img(doc, "laporan6_03_cron_promote_code.png", "Gambar 6.2: Logika otomasi transisi status pada PromoteAlumni.php")
    add_img(doc, "laporan6_07_tracer_study_app.png", "Gambar 6.3: Formulir kuesioner Tracer Study Alumni pada mobile", width_inches=2.8)
    add_img(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 6.4: Dasbor analitik penyerapan alumni SMK pada Web Admin")
    add_img(doc, "laporan6_09_git_push_final.png", "Gambar 6.5: Terminal eksekusi rilis final dengan tagging GitHub")

    doc.add_page_break()

    # BAB VII: TABEL TIMELINE PERKEMBANGAN PROYEK
    add_h1(doc, "BAB VII\nTABEL TIMELINE PELAKSANAAN DAN PERKEMBANGAN PROYEK")
    add_body(doc,
        "Pengembangan sistem SALUT dilaksanakan secara bertahap dan terstruktur berdasarkan metodologi rekayasa perangkat lunak iteratif. "
        "Tabel 7.1 menyajikan matriks linimasa (timeline) pengerjaan proyek dari tahap inisiasi, pengembangan modul backend dan mobile, "
        "integrasi ekosistem kejuruan SMK, pengujian menyeluruh, hingga deployment APK standalone pada perangkat fisik."
    )

    timeline_data = [
        ("Fase 1: Inisiasi & Desain", "28 - 29 Sep 2026", "Penyusunan dokumen SRS SALUT, perancangan arsitektur sistem, dan perancangan mockup UI/UX mobile dan desktop.", "Dokumen SRS & Mockup Desain (Laporan 1)", "Selesai (100%)"),
        ("Fase 2: Instalasi Lingkungan", "30 Sep 2026", "Instalasi Flutter SDK, Dart, Android Studio, SDK Command-line Tools, JDK 21, VS Code, dan verifikasi flutter doctor.", "Lingkungan Dev Siap (Laporan 2)", "Selesai (100%)"),
        ("Fase 3: Perkembangan 1 (Backend & DB)", "1 - 2 Okt 2026", "Setup Laravel 12, konfigurasi .env, migration database, model Eloquent, autentikasi JWT, API testing 200 OK, dan git push.", "Backend REST API & DB (Laporan 3)", "Selesai (100%)"),
        ("Fase 4: Perkembangan 2 (Frontend Mobile)", "3 - 5 Okt 2026", "Implementasi Flutter UI login & dashboard, integrasi Dio interceptor JWT, Dynamic UI Rendering Siswa vs Alumni, dan git push.", "Aplikasi Mobile Flutter (Laporan 4)", "Selesai (100%)"),
        ("Fase 5: Perkembangan 3 (Ekosistem SMK)", "12 - 13 Okt 2026", "Migration tabel skill_competencies, SkillController, antarmuka skills_page.dart (SKPI), arsip digital ber-TTE, dan seeder data.", "Modul Portofolio SKPI (Laporan 5)", "Selesai (100%)"),
        ("Fase 6: Perkembangan 4 (Otomasi & Analitik)", "14 - 15 Okt 2026", "Integrasi Firebase FCM, scheduled cron job salut:promote-alumni, tracer study dinamis, dashboard chart analitik, dan tag v1.0.0.", "Otomasi & Tracer (Laporan 6)", "Selesai (100%)"),
        ("Fase 7: Desain Apple-Style & Perbaikan", "15 - 17 Okt 2026", "Redesign UI ke konsep Apple-Style Clean Academic, pembuatan splash screen 3 detik, logo resmi baru, perbaikan modal arsip dan grafik.", "UI Modern Apple-Style", "Selesai (100%)"),
        ("Fase 8: Approval Realtime & Build APK", "18 Okt 2026", "Dialog konfirmasi pop-up prestasi berpendar, pull-to-refresh real-time approval admin ke siswa, build standalone APK release, dan install ke Samsung A25.", "Release Standalone APK", "Selesai (100%)"),
    ]

    tbl_tl = doc.add_table(rows=len(timeline_data) + 1, cols=5)
    tbl_tl.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Fase Perkembangan", "Rentang Waktu", "Deskripsi Aktivitas", "Luaran (Deliverables)", "Status"]
    col_widths = [1.2, 0.9, 2.2, 1.2, 0.7]

    hdr_cells = tbl_tl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        hdr_cells[i].width = Inches(col_widths[i])
        set_cell_background(hdr_cells[i], "E5E7EB") # Netral abu-abu terang
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.bold = True
            r.font.color.rgb = BLACK

    for row_idx, data in enumerate(timeline_data, start=1):
        row_cells = tbl_tl.rows[row_idx].cells
        bg_color = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data):
            row_cells[col_idx].text = text
            row_cells[col_idx].width = Inches(col_widths[col_idx])
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=100, right=100)
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.font.color.rgb = BLACK
                if col_idx == 0:
                    r.font.bold = True
                if col_idx == 4:
                    r.font.bold = True

    doc.add_page_break()

    # BAB VIII: PROTOTYPE AKHIR APLIKASI LENGKAP 4 ROLE
    add_h1(doc, "BAB VIII\nPROTOTYPE AKHIR APLIKASI SISTEM SALUT LENGKAP 4 ROLE")
    add_body(doc,
        "Bab ini menyajikan dokumentasi prototype akhir sistem informasi SALUT yang telah beroperasi secara penuh (live operational) "
        "pada seluruh aktor pengguna: Administrator Tata Usaha, Guru Pembina/Wali Jurusan, Siswa Aktif SMK, dan Alumni Kelulusan. "
        "Setiap sub-bab memaparkan fungsionalitas antarmuka sistem beserta tangkapan layar antarmuka aktual dan templat resmi untuk penyisipan foto fisik perangkat."
    )

    # 8.1 PROTOTYPE ROLE ADMINISTRATOR
    add_h2(doc, "8.1 Prototype Antarmuka Peran Administrator (Web Admin Panel)")
    add_body(doc,
        "Administrator Tata Usaha bertindak sebagai pengelola sistem utama. Panel kontrol web admin menyediakan dasbor analitik "
        "kejuruan SMK, manajemen basis data civitas sekolah, pengunggahan dan validasi arsip ijazah resmi, pengaturan jadwal rilis "
        "kelulusan otomatis, serta pemantauan hasil penyerapan tracer study."
    )
    add_h3(doc, "A. Dasbor Statistik & Analitik Kejuruan SMK")
    add_body(doc, "Dasbor utama menyajikan visualisasi sebaran siswa per jurusan SMK, metrik kompetensi keahlian, status alumni, serta leaderboard mitra DUDI.")
    add_img(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 8.1: Dasbor Analitik Kejuruan SMK pada Web Admin Administrator")

    add_h3(doc, "B. Modul Manajemen Master Data Siswa & Alumni")
    add_body(doc, "Menyajikan tabel master data 200+ civitas sekolah dengan fitur pencarian live search NISN/nama, filter kelas, dan tombol Import CSV massal.")
    add_img(doc, "proto_admin_students.png", "Gambar 8.2: Antarmuka Master Data Siswa & Alumni pada Web Admin Administrator")

    add_h3(doc, "C. Modul Pengelolaan Arsip Dokumen Digital Ijazah & SKL")
    add_body(doc, "Pusat verifikasi dan penyimpanan berkas sah digital (Ijazah Asli, SKL, Transkrip) dengan status kelengkapan dan modal kelola berkas.")
    add_img(doc, "proto_admin_arsip.png", "Gambar 8.3: Antarmuka Pengelolaan Arsip Digital Ijazah & SKL pada Web Admin Administrator")

    add_h3(doc, "D. Modul Pengaturan Jadwal Rilis Kelulusan Otomatis")
    add_body(doc, "Modul bagi Admin untuk mengatur tanggal dan jam pengumuman resmi kelulusan angkatan yang akan mentrigger cron job transisi status.")
    add_img(doc, "proto_admin_schedules.png", "Gambar 8.4: Antarmuka Penjadwalan Rilis Kelulusan Otomatis pada Web Admin Administrator")

    add_h3(doc, "E. Modul Rekapitulasi & Grafik Analitik Tracer Study")
    add_body(doc, "Menyajikan grafik doughnut penyerapan alumni (Bekerja 65%, Kuliah 25%, Wirausaha 10%) dan feed data kuesioner terkini.")
    add_img(doc, "proto_admin_tracer.png", "Gambar 8.5: Antarmuka Rekapitulasi & Grafik Tracer Study pada Web Admin Administrator")

    doc.add_page_break()

    # 8.2 PROTOTYPE ROLE GURU
    add_h2(doc, "8.2 Prototype Antarmuka Peran Guru (Web Admin Panel)")
    add_body(doc,
        "Guru Pengajar dan Asesor memiliki hak akses khusus yang berfokus pada evaluasi akademik dan pengesahan portofolio keahlian siswa. "
        "Sesuai prinsip Role-Based Access Control (RBAC), menu administratif yang tidak terkait dengan tugas guru secara otomatis disembunyikan."
    )
    add_h3(doc, "A. Modul Penginputan Nilai Rapor Siswa Per Semester")
    add_body(doc, "Guru dapat memilih kelas binaan dan semester aktif untuk menginput serta memperbarui nilai per mata pelajaran secara massal.")
    add_img(doc, "proto_guru_rapor.png", "Gambar 8.6: Antarmuka Penginputan Nilai Rapor Siswa pada Web Admin Guru")

    add_h3(doc, "B. Modul Asesmen & Validasi Portofolio Keahlian Siswa (SKPI)")
    add_body(doc, "Guru asesor mengesahkan capaian unit kompetensi kejuruan siswa (SKKNI/BNSP) berdasarkan tingkat kemahiran (Mahir/Terampil) dan skor uji.")
    add_img(doc, "proto_guru_skills.png", "Gambar 8.7: Antarmuka Validasi Portofolio Keahlian (SKPI) pada Web Admin Guru")

    doc.add_page_break()

    # 8.3 PROTOTYPE ROLE SISWA AKTIF
    add_h2(doc, "8.3 Prototype Antarmuka Peran Siswa Aktif (Mobile Flutter App)")
    add_body(doc,
        "Siswa Aktif SMK mengakses sistem melalui aplikasi mobile Android. Antarmuka menerapkan tema clean academic modern "
        "dengan fitur pemantauan profil, pengajuan prestasi non-akademik, verifikasi portofolio capaian keahlian (SKPI), dan nilai rapor."
    )
    add_h3(doc, "A. Halaman Splash Screen & Autentikasi Login Siswa")
    add_body(doc, "Splash screen transisi halus berlogo resmi SALUT 3 detik dilanjutkan form login cerdas dengan validasi NISN dan kata sandi.")
    add_img(doc, "laporan4_03_login_mobile_app.png", "Gambar 8.8: Antarmuka Login Siswa pada Mobile App", width_inches=2.8)
    add_placeholder_box(doc, "Login Siswa Aktif", "Ambil tangkapan layar langsung dari HP saat membuka form login di HP Samsung", "Gambar 8.9: Tangkapan layar fisik Login Siswa di HP Samsung")

    add_h3(doc, "B. Halaman Dasbor Utama Siswa Aktif")
    add_body(doc, "Menyajikan kartu profil siswa, jurusan SMK, status aktif, banner portofolio SKPI, serta ringkasan riwayat prestasi.")
    add_img(doc, "laporan4_04_dashboard_siswa_app.png", "Gambar 8.10: Antarmuka Dashboard Siswa Aktif pada Mobile App", width_inches=2.8)
    add_placeholder_box(doc, "Dashboard Siswa Aktif", "Ambil tangkapan layar langsung dari HP saat berada di beranda Siswa Aktif", "Gambar 8.11: Tangkapan layar fisik Dashboard Siswa di HP Samsung")

    add_h3(doc, "C. Halaman Pengajuan Prestasi & Modal Pop-Up Konfirmasi")
    add_body(doc, "Formulir pengajuan sertifikat prestasi lomba yang dilengkapi pop-up dialog resmi konfirmasi keberhasilan pengiriman berkas.")
    add_img(doc, "proto_siswa_prestasi.png", "Gambar 8.12: Antarmuka Pengajuan Prestasi & Pop-Up Konfirmasi Sukses", width_inches=2.8)
    add_placeholder_box(doc, "Pengajuan Prestasi Siswa", "Ambil tangkapan layar langsung dari HP pada dialog konfirmasi prestasi berhasil dikirim", "Gambar 8.13: Tangkapan layar fisik pengajuan prestasi di HP Samsung")

    add_h3(doc, "D. Halaman Portofolio Capaian Keahlian Siswa (SKPI)")
    add_body(doc, "Daftar unit kompetensi keahlian terverifikasi BNSP sesuai bidang kejuruan siswa lengkap dengan predikat kemahiran dan nama asesor.")
    add_img(doc, "laporan5_06_skills_mobile_app.png", "Gambar 8.14: Antarmuka Portofolio Capaian Keahlian (SKPI) Siswa", width_inches=2.8)
    add_placeholder_box(doc, "Portofolio SKPI Siswa", "Ambil tangkapan layar langsung dari HP pada daftar unit kompetensi SKPI", "Gambar 8.15: Tangkapan layar fisik modul SKPI di HP Samsung")

    doc.add_page_break()

    # 8.4 PROTOTYPE ROLE ALUMNI
    add_h2(doc, "8.4 Prototype Antarmuka Peran Alumni (Mobile Flutter App)")
    add_body(doc,
        "Ketika siswa dinyatakan lulus oleh sistem, antarmuka aplikasi mobile secara otomatis bertransformasi menjadi Portal Alumni. "
        "Fokus layanan beralih pada pengunduhan arsip dokumen ijazah sah ber-TTE, pengisian kuesioner tracer study penyerapan kerja/kuliah, "
        "serta manajemen keamanan kata sandi."
    )
    add_h3(doc, "A. Halaman Dasbor Utama Alumni")
    add_body(doc, "Menyajikan status kelulusan resmi, tahun angkatan kelulusan, tautan unduh ijazah, dan pengingat pengisian tracer study.")
    add_img(doc, "laporan4_05_dashboard_alumni_app.png", "Gambar 8.16: Antarmuka Dashboard Alumni pada Mobile App", width_inches=2.8)
    add_placeholder_box(doc, "Dashboard Alumni", "Ambil tangkapan layar langsung dari HP saat login sebagai Alumni", "Gambar 8.17: Tangkapan layar fisik Dashboard Alumni di HP Samsung")

    add_h3(doc, "B. Modul Arsip Digital Kelulusan Ijazah & SKL Sah")
    add_body(doc, "Daftar dokumen kelulusan berformat PDF terenkripsi (Ijazah Asli, SKL, Transkrip) yang dapat diunduh kapan saja oleh alumni.")
    add_img(doc, "laporan5_07_arsip_mobile_app.png", "Gambar 8.18: Antarmuka Arsip Dokumen Digital Kelulusan Alumni", width_inches=2.8)
    add_placeholder_box(doc, "Arsip Digital Alumni", "Ambil tangkapan layar langsung dari HP pada daftar berkas arsip ijazah", "Gambar 8.19: Tangkapan layar fisik Arsip Digital di HP Samsung")

    add_h3(doc, "C. Formulir Kuesioner Tracer Study Alumni Dinamis")
    add_body(doc, "Formulir pelacakan status lulusan (Bekerja, Melanjutkan Kuliah, Wirausaha) dengan kolom isian adaptif nama instansi dan penghasilan.")
    add_img(doc, "laporan6_07_tracer_study_app.png", "Gambar 8.20: Antarmuka Formulir Kuesioner Tracer Study Alumni", width_inches=2.8)
    add_placeholder_box(doc, "Kuesioner Tracer Study", "Ambil tangkapan layar langsung dari HP pada form kuesioner tracer study alumni", "Gambar 8.21: Tangkapan layar fisik Tracer Study di HP Samsung")

    add_h3(doc, "D. Modul Pengaturan Keamanan Akun & Ubah Kata Sandi")
    add_body(doc, "Formulir pembaruan kata sandi mandiri dengan verifikasi kata sandi lama dan enkripsi bcrypt pada backend.")
    add_img(doc, "laporan6_06_change_password_app.png", "Gambar 8.22: Antarmuka Modul Ubah Kata Sandi pada Mobile App", width_inches=2.8)
    add_placeholder_box(doc, "Ubah Kata Sandi Alumni", "Ambil tangkapan layar langsung dari HP pada menu Ubah Kata Sandi", "Gambar 8.23: Tangkapan layar fisik ubah kata sandi di HP Samsung")

    doc.add_page_break()

    # BAB IX: KESIMPULAN DAN REKOMENDASI
    add_h1(doc, "BAB IX\nKESIMPULAN DAN REKOMENDASI PENGEMBANGAN")
    add_h2(doc, "9.1 Kesimpulan")
    add_body(doc,
        "Berdasarkan seluruh rangkaian proses perancangan, implementasi, integrasi, dan pengujian yang telah dipaparkan dalam laporan ini, "
        "dapat disimpulkan bahwa:"
    )
    add_bullet(doc, "Keberhasilan Integrasi Multi-Platform", "Sistem SALUT sukses menghubungkan Backend RESTful API Laravel 12, basis data MySQL, Web Admin panel, dan aplikasi mobile Flutter dalam satu ekosistem client-server terpadu.");
    add_bullet(doc, "Implementasi Konsep Dynamic UI Rendering", "Aplikasi mobile berhasil melakukan transformasi antarmuka secara adaptif berdasarkan peran pengguna (Siswa Aktif vs Alumni) yang dienkapsulasi dalam token JWT.");
    add_bullet(doc, "Relevansi dengan Ekosistem Kejuruan SMK", "Penyediaan modul Portofolio Capaian Keahlian (SKPI) dan Tracer Study memberikan solusi konkret bagi SMK Negeri 1 Teladan dalam merekam kompetensi siswa dan memantau keterserapan kerja lulusan.");
    add_bullet(doc, "Efisiensi Melalui Otomatisasi Sistem", "Pemanfaatan scheduled cron job command salut:promote-alumni dan Push Notification FCM secara efektif menghilangkan proses manual pemindahan status kelulusan ratusan siswa.");
    add_bullet(doc, "Kesiapan Operasional Standalone", "Aplikasi Flutter berhasil di-compile ke format rilis resmi standalone APK (54.6 MB) dan terpasang sempurna pada perangkat fisik HP Samsung Galaxy A25 5G dengan kinerja 100% lancar.");

    add_h2(doc, "9.2 Rekomendasi Pengembangan Lanjutan")
    add_body(doc,
        "Untuk peningkatan sistem SALUT pada tahap pengembangan berikutnya, disarankan beberapa poin rekomendasi:"
    )
    add_bullet(doc, "Integrasi Sertifikasi BSrE", "Menerapkan Tanda Tangan Elektronik tersertifikasi Badan Siber dan Sandi Negara (BSrE) untuk meningkatkan kekuatan hukum berkas ijazah digital secara nasional.");
    add_bullet(doc, "Portal Bursa Kerja Khusus (BKK)", "Mengembangkan modul rekrutmen terintegrasi yang menghubungkan alumni secara langsung dengan lowongan kerja mitra industri sekolah (DUDI).");
    add_bullet(doc, "Penerapan Kecerdasan Buatan (AI Analytics)", "Memanfaatkan algoritma machine learning untuk memprediksi tren kompetensi kejuruan yang paling diminati industri serta merekomendasikan program pelatihan tambahan bagi siswa.");

    out_docx = os.path.join(ROOT_DIR, "Laporan_Akhir_Lengkap.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Akhir_Lengkap.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai membuat Laporan Akhir Lengkap:", out_docx)

if __name__ == "__main__":
    print("Membangun seluruh laporan dengan format: Times New Roman 12pt, Hitam, Rata Kanan-Kiri...")
    build_laporan_perkembangan_1()
    build_laporan_perkembangan_2()
    build_laporan_perkembangan_3()
    build_laporan_perkembangan_4()
    build_laporan_akhir_lengkap()
    print("SEMUA DOKUMEN DOCX SELESAI DIPERBARUI SECARA STANDAR!")
