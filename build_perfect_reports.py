# -*- coding: utf-8 -*-
"""
Script Pembangun Dokumen Laporan Komprehensif SALUT Sesuai Format Contoh Makalah Unila:
1. Laporan Instalasi (Murni hanya instalasi) (.docx & .html)
2. Laporan Perkembangan 1 (.docx & .html)
3. Laporan Perkembangan 2 (.docx & .html)
4. Laporan Perkembangan 3 (.docx & .html)
5. Laporan Perkembangan 4 (.docx & .html)
6. Laporan Akhir Lengkap (Laporan 7 Gabungan: Bab I-IV + Lampiran I & II) (.docx & .html)

ATURAN FORMAT MUTLAK:
- Font: Times New Roman, ukuran 12 pt untuk SEMUA elemen.
- Judul BAB: Center, Bold, 12 pt (tidak rata kanan-kiri).
- Subbab (1.1, 2.1, dst): Left (Rata Kiri), Bold, 12 pt (tidak rata kanan-kiri).
- Sub-subbab (A., B., dst): Left (Rata Kiri), Bold, 12 pt (tidak rata kanan-kiri).
- Paragraf Isi: Justified (Rata Kanan-Kiri), 12 pt, Spasi 1.5.
- Caption Gambar: Center, Bold, 12 pt (Gambar X.X. Judul Gambar).
- Warna Teks: Murni Hitam (RGB: 0, 0, 0), bebas warna biru.
- Nomor Halaman: Romawi kecil (i, ii) untuk kata pengantar & daftar isi, Angka Arab (1, 2, 3...) untuk isi bab.
- Lampiran II: Kotak Template Resmi bagi pengguna untuk menempelkan screenshot seluruh aktor.
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

# =============================================================================
# HELPER PEMBUATAN DOKUMEN & FORMATTING
# =============================================================================

def create_doc_with_margins():
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

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_academic_cover(doc, title_main, subtitle_text):
    sec = doc.sections[0]
    
    # Judul Dokumen (Atas, Center, Bold 12pt)
    p_t = doc.add_paragraph()
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t.paragraph_format.space_before = Pt(20)
    p_t.paragraph_format.space_after = Pt(2)
    p_t.paragraph_format.line_spacing = 1.15
    r_t = p_t.add_run(title_main.upper())
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(12)
    r_t.font.bold = True
    r_t.font.color.rgb = BLACK

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run(subtitle_text)
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = BLACK

    # Logo Universitas Lampung (Center)
    logo_path = os.path.join(INST_IMG_DIR, "logo_unila.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(12)
        p_logo.paragraph_format.space_after = Pt(24)
        p_logo.add_run().add_picture(logo_path, width=Inches(2.0))

    # Dosen Pengampu & Mahasiswa
    p_dosen = doc.add_paragraph()
    p_dosen.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dosen.paragraph_format.space_before = Pt(8)
    p_dosen.paragraph_format.space_after = Pt(2)
    r_d1 = p_dosen.add_run("Dosen Mata Kuliah :\n")
    r_d1.font.name = 'Times New Roman'
    r_d1.font.size = Pt(12)
    r_d1.font.bold = True
    r_d1.font.color.rgb = BLACK
    r_d2 = p_dosen.add_run("Ghea Chandra Surawan, M.Pd.")
    r_d2.font.name = 'Times New Roman'
    r_d2.font.size = Pt(12)
    r_d2.font.bold = True
    r_d2.font.color.rgb = BLACK

    p_mhs = doc.add_paragraph()
    p_mhs.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_mhs.paragraph_format.space_before = Pt(14)
    p_mhs.paragraph_format.space_after = Pt(2)
    r_m1 = p_mhs.add_run("Disusun Oleh:\n")
    r_m1.font.name = 'Times New Roman'
    r_m1.font.size = Pt(12)
    r_m1.font.bold = True
    r_m1.font.color.rgb = BLACK
    r_m2 = p_mhs.add_run("Wemvi Afrialdo (2413025052)")
    r_m2.font.name = 'Times New Roman'
    r_m2.font.size = Pt(12)
    r_m2.font.bold = True
    r_m2.font.color.rgb = BLACK

    p_repo = doc.add_paragraph()
    p_repo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_repo.paragraph_format.space_before = Pt(14)
    p_repo.paragraph_format.space_after = Pt(28)
    r_rp1 = p_repo.add_run("Tautan Repositori GitHub:\n")
    r_rp1.font.name = 'Times New Roman'
    r_rp1.font.size = Pt(12)
    r_rp1.font.bold = True
    r_rp1.font.color.rgb = BLACK
    r_rp2 = p_repo.add_run("https://github.com/WEMVIAFRIALDO/apps_Sekolah-")
    r_rp2.font.name = 'Times New Roman'
    r_rp2.font.size = Pt(12)
    r_rp2.font.underline = True
    r_rp2.font.color.rgb = BLACK

    # Lembaga & Tahun (Bawah)
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(20)
    p_inst.paragraph_format.space_after = Pt(0)
    p_inst.paragraph_format.line_spacing = 1.15
    r_in = p_inst.add_run("PROGRAM STUDI PENDIDIKAN TEKNOLOGI INFORMASI\nJURUSAN PENDIDIKAN MATEMATIKA DAN ILMU PENGETAHUAN ALAM\nFAKULTAS KEGURUAN DAN ILMU PENDIDIKAN\nUNIVERSITAS LAMPUNG\n2026")
    r_in.font.name = 'Times New Roman'
    r_in.font.size = Pt(12)
    r_in.font.bold = True
    r_in.font.color.rgb = BLACK

    doc.add_page_break()

def setup_page_numbering(sec, fmt="lowerRoman", start=1):
    sec._sectPr.append(parse_xml(f'<w:pgNumType {nsdecls("w")} w:fmt="{fmt}" w:start="{start}"/>'))
    footer = sec.footer
    p_ft = footer.paragraphs[0]
    p_ft.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ft._p.append(parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>'))

def add_bab_title(doc, bab_num_str, bab_title_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.15
    r1 = p.add_run(bab_num_str.upper() + "\n")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r1.font.color.rgb = BLACK
    
    r2 = p.add_run(bab_title_str.upper())
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    r2.font.bold = True
    r2.font.color.rgb = BLACK
    return p

def add_subbab(doc, subbab_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(subbab_str)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = BLACK
    return p

def add_sub_subbab(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
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
    r2.font.color.rgb = BLACK
    return p

def add_toc_entry(doc, title, page_str, is_bold=False, indent_inch=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    if indent_inch > 0:
        p.paragraph_format.left_indent = Inches(indent_inch)
    pPr = p._p.get_or_add_pPr()
    tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="9072"/></w:tabs>')
    pPr.append(tabs)
    r1 = p.add_run(title)
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = is_bold
    r1.font.color.rgb = BLACK
    if page_str:
        r2 = p.add_run(f"\t{page_str}")
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(12)
        r2.font.bold = is_bold
        r2.font.color.rgb = BLACK
    return p

def add_img_academic(doc, img_filename_or_path, caption_title, width_inches=5.8):
    if os.path.isabs(img_filename_or_path):
        img_path = img_filename_or_path
    else:
        img_path = os.path.join(IMG_DIR, img_filename_or_path)
        if not os.path.exists(img_path):
            img_path = os.path.join(SRS_IMG_DIR, img_filename_or_path)
            
    # Caption di ATAS gambar seperti contoh makalah Unila
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(8)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.line_spacing = 1.15
    r_cap = p_cap.add_run(caption_title)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(12)
    r_cap.font.bold = True
    r_cap.font.color.rgb = BLACK

    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(8)
        r_img = p_img.add_run()
        r_img.add_picture(img_path, width=Inches(width_inches))

def add_template_placeholder(doc, placeholder_title, instruction_text):
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(8)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.line_spacing = 1.15
    r_cap = p_cap.add_run(placeholder_title)
    r_cap.font.name = 'Times New Roman'
    r_cap.font.size = Pt(12)
    r_cap.font.bold = True
    r_cap.font.color.rgb = BLACK

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(5.8)
    set_cell_background(cell, "FAFAFA")
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
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(10)
    p1.paragraph_format.space_after = Pt(4)
    r1 = p1.add_run("📷 [AREA TEMPEL SCREENSHOT PENGGUNA]")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r1.font.color.rgb = BLACK

    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(10)
    r2 = p2.add_run(instruction_text + "\n(Silakan tempelkan / Paste tangkapan layar langsung ke dalam kotak ini)")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(11)
    r2.font.italic = True
    r2.font.color.rgb = BLACK

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(8)

# =============================================================================
# 1. FILE KHUSUS: LAPORAN INSTALASI (HANYA SAMPAI INSTALASI)
# =============================================================================
def build_laporan_instalasi_only():
    doc = create_doc_with_margins()
    add_academic_cover(doc, 
        "LAPORAN INSTALASI DAN KONFIGURASI TOOLCHAIN\nPENGEMBANGAN APLIKASI MOBILE DAN SERVER SISTEM SALUT",
        "Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile")

    # Bagian Awal: Romawi
    sec1 = doc.add_section()
    setup_page_numbering(sec1, fmt="lowerRoman", start=1)

    # KATA PENGANTAR
    p_kp = doc.add_paragraph()
    p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp.paragraph_format.space_before = Pt(10)
    p_kp.paragraph_format.space_after = Pt(14)
    r_kp = p_kp.add_run("KATA PENGANTAR")
    r_kp.font.name = 'Times New Roman'
    r_kp.font.size = Pt(12)
    r_kp.font.bold = True
    r_kp.font.color.rgb = BLACK

    add_body(doc,
        "Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat dan karunia-Nya, sehingga Laporan Teknis "
        "Instalasi dan Konfigurasi Toolchain Pengembangan Aplikasi Mobile SALUT ini dapat diselesaikan dengan baik dan tepat waktu."
    )
    add_body(doc,
        "Laporan ini mendokumentasikan tahapan fundamental dalam penyiapan lingkungan pengembangan, mencakup pemasangan Flutter SDK, "
        "Dart, Java Development Kit (JDK 21 LTS), Android Studio, Android SDK Command-line Tools, CMake, NDK, editor Visual Studio Code, "
        "hingga konfigurasi server lokal XAMPP dan framework Laravel 12."
    )
    add_body(doc,
        "Ucapan terima kasih penulis sampaikan kepada Bapak Dosen Pengampu serta rekan-rekan mahasiswa yang telah memberikan bimbingan "
        "dan masukan konstruktif dalam penyelesaian instalasi ini. Semoga laporan ini bermanfaat bagi pembaca."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\nPenyusun,\n\n\nWemvi Afrialdo\nNPM. 2413025052")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    doc.add_page_break()

    # DAFTAR ISI INSTALASI
    p_di = doc.add_paragraph()
    p_di.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_di.paragraph_format.space_before = Pt(10)
    p_di.paragraph_format.space_after = Pt(14)
    r_di = p_di.add_run("DAFTAR ISI")
    r_di.font.name = 'Times New Roman'
    r_di.font.size = Pt(12)
    r_di.font.bold = True
    r_di.font.color.rgb = BLACK

    di_items = [
        ("HALAMAN JUDUL", ""),
        ("KATA PENGANTAR", "i"),
        ("DAFTAR ISI", "ii"),
        ("BAB I PENDAHULUAN", "1"),
        ("  1.1 Latar Belakang Penyiapan Lingkungan", "1"),
        ("  1.2 Tujuan Penyiapan Toolchain", "1"),
        ("  1.3 Manfaat Praktis", "2"),
        ("BAB II LAPORAN INSTALASI TOOLCHAIN & SERVER", "3"),
        ("  2.1 Persiapan Lingkungan dan Pengunduhan Flutter SDK", "3"),
        ("  2.2 Ekstraksi Berkas dan Konfigurasi Environment Variables PATH", "4"),
        ("  2.3 Instalasi dan Konfigurasi Java Development Kit (JDK 21)", "5"),
        ("  2.4 Instalasi Ekstensi Flutter dan Dart pada Visual Studio Code", "6"),
        ("  2.5 Konfigurasi Android Studio, SDK Tools, dan CMake", "7"),
        ("  2.6 Pengujian Kelayakan Toolchain dengan Flutter Doctor", "8"),
        ("  2.7 Penyiapan Web Server Lokal XAMPP dan MySQL", "9"),
        ("  2.8 Instalasi Backend Laravel 12", "10"),
        ("BAB III PENUTUP", "11"),
        ("  3.1 Kesimpulan Instalasi", "11"),
        ("  3.2 Saran Perawatan Lingkungan Pengembangan", "11"),
    ]
    for it_name, it_pg in di_items:
        is_bold = it_name.startswith("BAB ") or it_name in ["HALAMAN JUDUL", "KATA PENGANTAR", "DAFTAR ISI"]
        indent = 0.25 if it_name.startswith("  ") else 0
        add_toc_entry(doc, it_name.strip(), it_pg, is_bold=is_bold, indent_inch=indent)

    # Bagian Isi: Angka Arab (1, 2, 3...)
    sec2 = doc.add_section()
    setup_page_numbering(sec2, fmt="decimal", start=1)

    # BAB I PENDAHULUAN
    add_bab_title(doc, "BAB I", "PENDAHULUAN")
    add_subbab(doc, "1.1 Latar Belakang Penyiapan Lingkungan")
    add_body(doc,
        "Keberhasilan pembangunan aplikasi lintas platform (cross-platform mobile) berakar pada kesiapan toolchain dan rantai kompilasi "
        "yang kokoh. Pengembangan sistem informasi SALUT (Sistem Arsip Kelulusan dan Tracer Study Alumni SMK) memerlukan integrasi antara "
        "frontend mobile berbasis Flutter dan backend server berbasis PHP Laravel 12 dengan basis data relasional MySQL. Oleh karena itu, "
        "penyiapan lingkungan pengembangan yang presisi menjadi prasyarat mutlak sebelum tahap perancangan logika bisnis dimulai."
    )

    add_subbab(doc, "1.2 Tujuan Penyiapan Toolchain")
    add_body(doc,
        "Tujuan dari penyiapan lingkungan instalasi ini adalah:\n"
        "1. Mengunduh dan mengonfigurasi Flutter SDK versi stabil dan Dart SDK pada sistem operasi Windows.\n"
        "2. Mengonfigurasi Java Development Kit (JDK 21 LTS) dan Android SDK Command-line Tools untuk kompilasi APK.\n"
        "3. Mempersiapkan IDE Visual Studio Code beserta ekstensi pendukung rekayasa Flutter.\n"
        "4. Memastikan seluruh dependensi berstatus siap pakai melalui verifikasi `flutter doctor` tanpa kesalahan.\n"
        "5. Menyiapkan web server lokal XAMPP dan framework Laravel 12 sebagai fondasi RESTful API."
    )

    add_subbab(doc, "1.3 Manfaat Praktis")
    add_body(doc,
        "Manfaat penyiapan lingkungan ini adalah tersedianya ekosistem pengkodean yang stabil, mendukung proses kompilasi cepat (hot-reload), "
        "dan memudahkan deployment aplikasi secara mandiri baik pada emulator maupun perangkat fisik Android."
    )

    doc.add_page_break()

    # BAB II LAPORAN INSTALASI TOOLCHAIN & SERVER
    add_bab_title(doc, "BAB II", "LAPORAN INSTALASI TOOLCHAIN & SERVER")
    add_body(doc,
        "Bab ini menguraikan tahapan teknis pelaksanaan instalasi lingkungan pengembangan aplikasi SALUT secara berurutan, "
        "dimulai dari pengunduhan paket resmi Flutter, konfigurasi variabel sistem, penyiapan Android SDK, hingga verifikasi diagnosa."
    )

    add_subbab(doc, "2.1 Persiapan Lingkungan dan Pengunduhan Flutter SDK")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step01_flutter_website.png"), "Gambar 2.1. Halaman Pengunduhan Flutter SDK dari Portal Resmi flutter.dev")
    add_body(doc,
        "Gambar 2.1 memperlihatkan halaman pengunduhan resmi Flutter SDK pada peramban web. Pengembang mengunduh bundel kompilasi stabil "
        "untuk sistem operasi Windows guna memperoleh pustaka inti antarmuka grafis dan Dart compiler."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step02_download_flutter_zip.png"), "Gambar 2.2. Berkas Arsip Terkompresi Flutter SDK pada Folder Unduhan")
    add_body(doc,
        "Gambar 2.2 mendokumentasikan berkas arsip zip Flutter SDK yang telah berhasil diunduh. Berkas ini kemudian diekstrak ke direktori "
        "penyimpanan lokal tanpa spasi (misalnya `C:\\src\\flutter` atau direktori kerja pengembang)."
    )

    add_subbab(doc, "2.2 Ekstraksi Berkas dan Konfigurasi Environment Variables PATH")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step03_environment_variables.png"), "Gambar 2.3. Konfigurasi Variabel Lingkungan Sistem (System Environment Variables)")
    add_body(doc,
        "Gambar 2.3 menunjukkan jendela konfigurasi Environment Variables pada Windows. Jalur direktori `flutter\\bin` ditambahkan ke variabel "
        "PATH sistem agar perintah terminal `flutter` dan `dart` dapat dipanggil secara global dari sesi terminal mana pun."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step04_flutter_version_cmd.png"), "Gambar 2.4. Verifikasi Versi Flutter SDK dan Dart pada Terminal Command Prompt")
    add_body(doc,
        "Gambar 2.4 membuktikan keberhasilan pengenalan perintah `flutter --version` pada command prompt, yang menampilkan rincian rilis "
        "Flutter Channel stable beserta versi Dart SDK yang menyertainya."
    )

    add_subbab(doc, "2.3 Instalasi dan Konfigurasi Java Development Kit (JDK 21)")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step05_download_jdk21.png"), "Gambar 2.5. Berkas Instalasi Java Development Kit 21 (JDK 21 LTS)")
    add_body(doc,
        "Gambar 2.5 menampilkan berkas pemasangan Java Development Kit (JDK 21 LTS). JDK 21 diperlukan oleh Gradle untuk memproses "
        "kompilasi kode Kotlin dan Java pada layer platform Android."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step06_java_version_terminal.png"), "Gambar 2.6. Verifikasi Java Runtime Environment dan JAVA_HOME")
    add_body(doc,
        "Gambar 2.6 memvalidasi eksekusi `java -version` yang mengonfirmasi bahwa OpenJDK 64-Bit Server VM telah aktif dengan benar di sistem."
    )

    add_subbab(doc, "2.4 Instalasi Ekstensi Flutter dan Dart pada Visual Studio Code")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step07_vscode_flutter_extension.png"), "Gambar 2.7. Instalasi Ekstensi Resmi Flutter pada Marketplace VS Code")
    add_body(doc,
        "Gambar 2.7 memperlihatkan pemasangan ekstensi Flutter pada Visual Studio Code. Ekstensi ini menyediakan fitur code completion, "
        "hot reload, widget tree inspection, dan debugging langsung."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step08_vscode_dart_extension.png"), "Gambar 2.8. Instalasi Ekstensi Bahasa Dart pada Visual Studio Code")
    add_body(doc,
        "Gambar 2.8 mendokumentasikan ekstensi bahasa Dart yang memberikan dukungan linter dan analisis statis kode aplikasi."
    )

    add_subbab(doc, "2.5 Konfigurasi Android Studio, SDK Tools, dan CMake")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step09_android_sdk_tools_cmake.png"), "Gambar 2.9. Pengaturan Android SDK Command-line Tools dan CMake")
    add_body(doc,
        "Gambar 2.9 menampilkan panel Android SDK Manager. Dipasang komponen Android SDK Command-line Tools (latest) dan CMake guna "
        "menjamin kesiapan toolchain kompilasi native C/C++ pada pustaka tertentu."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step10_android_ndk_installed.png"), "Gambar 2.10. Status Pemasangan Android NDK pada SDK Tools")
    add_body(doc,
        "Gambar 2.10 memverifikasi status pemasangan Android NDK (Side by side) yang diperlukan untuk proses linking kode native Android."
    )

    add_subbab(doc, "2.6 Pengujian Kelayakan Toolchain dengan Flutter Doctor")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step11_flutter_doctor_output.png"), "Gambar 2.11. Hasil Diagnosa Menyeluruh Perintah flutter doctor")
    add_body(doc,
        "Gambar 2.11 menampilkan laporan diagnosa `flutter doctor` yang mengonfirmasi bahwa seluruh komponen vital: Flutter SDK, "
        "Android toolchain (licenses accepted), Android Studio, VS Code, dan perangkat terhubung (connected device) telah berstatus centang hijau (No issues found!)."
    )

    doc.add_page_break()

    # BAB III PENUTUP
    add_bab_title(doc, "BAB III", "PENUTUP")
    add_subbab(doc, "3.1 Kesimpulan Instalasi")
    add_body(doc,
        "Seluruh rangkaian tahapan instalasi dan konfigurasi toolchain untuk pengembangan aplikasi SALUT telah berhasil diselesaikan dengan baik. "
        "Sistem operasi Windows telah terkonfigurasi dengan Flutter SDK, Dart, JDK 21, Android SDK Tools, VS Code IDE, dan XAMPP Server. "
        "Hasil diagnosa `flutter doctor` membuktikan tidak ada kendala dependensi sehingga lingkungan pengembangan siap digunakan untuk perancangan aplikasi."
    )

    add_subbab(doc, "3.2 Saran Perawatan Lingkungan Pengembangan")
    add_body(doc,
        "Disarankan untuk rutin memperbarui Android SDK Build-Tools dan memelihara cache Flutter melalui perintah `flutter clean` "
        "sebelum melakukan kompilasi rilis agar tidak terjadi konflik file binary."
    )

    out_docx = os.path.join(ROOT_DIR, "Laporan_Instalasi.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Instalasi.docx")
    out_docx_inst = os.path.join(ROOT_DIR, "instalasi.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    doc.save(out_docx_inst)
    print("Selesai membuat Laporan_Instalasi.docx (Murni Instalasi):", out_docx)

# =============================================================================
# 2. LAPORAN PERKEMBANGAN 1 (BACKEND & DATABASE)
# =============================================================================
def build_laporan_perkembangan_1():
    doc = create_doc_with_margins()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 1\nPENGEMBANGAN BACKEND API, STRUKTUR DATABASE, DAN AUTENTIKASI JWT",
        "Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile")

    # Bagian Awal: Romawi
    sec1 = doc.add_section()
    setup_page_numbering(sec1, fmt="lowerRoman", start=1)

    p_kp = doc.add_paragraph()
    p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp.paragraph_format.space_before = Pt(10)
    p_kp.paragraph_format.space_after = Pt(14)
    r_kp = p_kp.add_run("KATA PENGANTAR")
    r_kp.font.name = 'Times New Roman'
    r_kp.font.size = Pt(12)
    r_kp.font.bold = True
    r_kp.font.color.rgb = BLACK

    add_body(doc,
        "Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas terselesaikannya Laporan Perkembangan Proyek 1 "
        "Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK (SALUT). Laporan ini mendokumentasikan implementasi backend RESTful API, "
        "perancangan skema database MySQL multi-role, pembuatan model Eloquent, serta penerapan autentikasi token JWT."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\nPenyusun,\n\n\nWemvi Afrialdo\nNPM. 2413025052")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    # Bagian Isi: Angka Arab
    sec2 = doc.add_section()
    setup_page_numbering(sec2, fmt="decimal", start=1)

    add_bab_title(doc, "BAB I", "PENGEMBANGAN BACKEND API DAN BASIS DATA")

    add_subbab(doc, "1.1 Konfigurasi Lingkungan Backend (Laravel 12 & MySQL)")
    add_img_academic(doc, "laporan3_01_env.png", "Gambar 1.1. Konfigurasi Variabel Lingkungan .env pada Backend Laravel 12")
    add_body(doc,
        "Gambar 1.1 memperlihatkan konfigurasi koneksi basis data MySQL pada berkas .env. Parameter koneksi DB_CONNECTION=mysql, "
        "DB_HOST=127.0.0.1, DB_PORT=3306, dan DB_DATABASE=db_salut disetel guna memastikan backend dapat berkomunikasi dengan database server."
    )

    add_subbab(doc, "1.2 Perancangan Struktur Database (Migrations dan Models)")
    add_img_academic(doc, "laporan3_02_migration_model.png", "Gambar 1.2. Potongan Kode Migrations dan Model Eloquent Relasional")
    add_body(doc,
        "Gambar 1.2 mendokumentasikan pembuatan skema tabel menggunakan Migration Laravel. Struktur mencakup entitas users, student_profiles, "
        "academic_records, achievements, dan graduation_schedules dengan integritas referensial foreign key."
    )

    add_img_academic(doc, "laporan3_03_phpmyadmin.png", "Gambar 1.3. Struktur Tabel Basis Data db_salut pada phpMyAdmin")
    add_body(doc,
        "Gambar 1.3 membuktikan bahwa seluruh berkas migrasi berhasil dieksekusi ke basis data db_salut dengan struktur kolom yang sesuai rancangan SRS."
    )

    add_subbab(doc, "1.3 Pembuatan RESTful API Endpoint dan Keamanan JWT")
    add_img_academic(doc, "laporan3_04_routes_api.png", "Gambar 1.4. Definisi Routing RESTful API pada routes/api.php")
    add_body(doc,
        "Gambar 1.4 menampilkan pendefinisian rute API publik POST /api/login dan proteksi rute tertutup menggunakan middleware jwt.auth "
        "untuk menjamin pertukaran data yang aman dan stateless."
    )

    add_subbab(doc, "1.4 Pengujian Endpoint API (API Testing 200 OK)")
    add_img_academic(doc, "laporan3_05_api_testing.png", "Gambar 1.5. Hasil Pengujian API Login dengan Respons HTTP 200 OK")
    add_body(doc,
        "Gambar 1.5 mengonfirmasi keberhasilan pengujian login via API Client yang mengembalikan respons status HTTP 200 OK dan token Bearer JWT."
    )

    add_subbab(doc, "1.5 Sinkronisasi Kode Sumber Backend ke GitHub")
    add_img_academic(doc, "laporan3_06_git_push_backend.png", "Gambar 1.6. Eksekusi Perintah git push Backend pada Terminal PowerShell")
    add_body(doc,
        "Gambar 1.6 mendokumentasikan proses push kode sumber backend ke repositori GitHub WEMVIAFRIALDO/apps_Sekolah-."
    )

    add_img_academic(doc, "laporan3_07_github_backend.png", "Gambar 1.7. Tampilan Repositori Backend SALUT di GitHub")
    add_body(doc,
        "Gambar 1.7 memperlihatkan repositori backend yang telah tersimpan rapi dan terkelola secara aman di GitHub."
    )

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_1.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_1.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai Laporan_Perkembangan_1.docx:", out_docx)

# =============================================================================
# 3. LAPORAN PERKEMBANGAN 2 (FRONTEND FLUTTER & DYNAMIC UI)
# =============================================================================
def build_laporan_perkembangan_2():
    doc = create_doc_with_margins()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 2\nPENGEMBANGAN ANTARMUKA MOBILE (FLUTTER) DAN INTEGRASI JWT",
        "Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile")

    sec1 = doc.add_section()
    setup_page_numbering(sec1, fmt="lowerRoman", start=1)

    p_kp = doc.add_paragraph()
    p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp.paragraph_format.space_before = Pt(10)
    p_kp.paragraph_format.space_after = Pt(14)
    r_kp = p_kp.add_run("KATA PENGANTAR")
    r_kp.font.name = 'Times New Roman'
    r_kp.font.size = Pt(12)
    r_kp.font.bold = True
    r_kp.font.color.rgb = BLACK

    add_body(doc,
        "Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas terselesaikannya Laporan Perkembangan Proyek 2 "
        "yang memaparkan perancangan antarmuka pengguna mobile Flutter, integrasi HTTP Client Dio, pengelolaan token JWT, "
        "serta penerapan logika Dynamic UI Rendering multi-role Siswa Aktif dan Alumni."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\nPenyusun,\n\n\nWemvi Afrialdo\nNPM. 2413025052")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    sec2 = doc.add_section()
    setup_page_numbering(sec2, fmt="decimal", start=1)

    add_bab_title(doc, "BAB I", "PENGEMBANGAN ANTARMUKA MOBILE FLUTTER")

    add_subbab(doc, "1.1 Pembuatan Antarmuka Pengguna Utama (Login & Dashboard)")
    add_img_academic(doc, "laporan4_01_login_page_code.png", "Gambar 1.1. Kode Antarmuka login_page.dart pada Visual Studio Code")
    add_body(doc,
        "Gambar 1.1 mengilustrasikan potongan kode form login pada Flutter yang dilengkapi validasi NISN dan kata sandi."
    )

    add_subbab(doc, "1.2 Integrasi HTTP Client Dio dan Interceptor Token JWT")
    add_img_academic(doc, "laporan4_02_api_service_code.png", "Gambar 1.2. Implementasi ApiService dan Interceptor JWT pada Flutter")
    add_body(doc,
        "Gambar 1.2 memperlihatkan implementasi Dio HTTP Client yang secara otomatis membaca token dari penyimpanan aman dan menyematkannya pada header."
    )

    add_subbab(doc, "1.3 Pengujian Antarmuka pada Perangkat Mobile")
    add_img_academic(doc, "laporan4_03_login_mobile_app.png", "Gambar 1.3. Antarmuka Halaman Login Aplikasi SALUT Mobile", width_inches=2.8)
    add_body(doc, "Gambar 1.3 menunjukkan tampilan halaman Login aplikasi yang telah berjalan responsif pada perangkat mobile.")

    add_img_academic(doc, "laporan4_04_dashboard_siswa_app.png", "Gambar 1.4. Antarmuka Dashboard untuk Peran Siswa Aktif", width_inches=2.8)
    add_body(doc, "Gambar 1.4 menampilkan beranda Siswa Aktif dengan menu prestasi, nilai rapor, dan profil akademik.")

    add_img_academic(doc, "laporan4_05_dashboard_alumni_app.png", "Gambar 1.5. Antarmuka Dashboard untuk Peran Alumni", width_inches=2.8)
    add_body(doc, "Gambar 1.5 membuktikan transformasi antarmuka Alumni dengan menu arsip dokumen dan tracer study.")

    add_subbab(doc, "1.4 Penerapan Logika Dynamic UI Rendering Berbasis Peran")
    add_img_academic(doc, "laporan4_06_role_logic_code.png", "Gambar 1.6. Kode Logika Pengkondisian Tampilan Menu Per-Role")
    add_body(doc, "Gambar 1.6 memperlihatkan logika reactive GetX yang mengondisikan menu antarmuka secara adaptif berdasarkan role.")

    add_subbab(doc, "1.5 Sinkronisasi Kode Frontend ke GitHub")
    add_img_academic(doc, "laporan4_07_git_push_frontend.png", "Gambar 1.7. Eksekusi Perintah git push Frontend pada Terminal PowerShell")
    add_body(doc, "Gambar 1.7 mendokumentasikan proses sinkronisasi kode aplikasi mobile Flutter ke GitHub.")

    add_img_academic(doc, "laporan4_08_github_frontend.png", "Gambar 1.8. Repositori Frontend apps_sekolah di GitHub")
    add_body(doc, "Gambar 1.8 memperlihatkan struktur proyek Flutter yang tersinkronisasi di GitHub.")

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_2.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_2.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai Laporan_Perkembangan_2.docx:", out_docx)

# =============================================================================
# 4. LAPORAN PERKEMBANGAN 3 (SKPI & ARSIP DIGITAL)
# =============================================================================
def build_laporan_perkembangan_3():
    doc = create_doc_with_margins()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 3\nPENGEMBANGAN FITUR EKOSISTEM KEJURUAN SMK (SKPI & ARSIP DIGITAL)",
        "Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile")

    sec1 = doc.add_section()
    setup_page_numbering(sec1, fmt="lowerRoman", start=1)

    p_kp = doc.add_paragraph()
    p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp.paragraph_format.space_before = Pt(10)
    p_kp.paragraph_format.space_after = Pt(14)
    r_kp = p_kp.add_run("KATA PENGANTAR")
    r_kp.font.name = 'Times New Roman'
    r_kp.font.size = Pt(12)
    r_kp.font.bold = True
    r_kp.font.color.rgb = BLACK

    add_body(doc,
        "Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas rampungnya Laporan Perkembangan Proyek 3 "
        "yang memaparkan integrasi ekosistem kejuruan SMK, pencatatan 136 unit kompetensi keahlian siswa (SKPI), "
        "pengembangan antarmuka skills_page.dart, serta modul arsip dokumen digital kelulusan ber-TTE."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\nPenyusun,\n\n\nWemvi Afrialdo\nNPM. 2413025052")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    sec2 = doc.add_section()
    setup_page_numbering(sec2, fmt="decimal", start=1)

    add_bab_title(doc, "BAB I", "PENGEMBANGAN FITUR KEJURUAN SMK (SKPI & ARSIP)")

    add_subbab(doc, "1.1 Perancangan Skema Database Portofolio Keahlian (SKPI)")
    add_img_academic(doc, "laporan5_01_migration_skpi.png", "Gambar 1.1. Migration Tabel skill_competencies untuk Modul SKPI SMK")
    add_body(doc, "Gambar 1.1 menampilkan kode migration tabel skill_competencies yang menampung capaian unit keahlian siswa.")

    add_img_academic(doc, "laporan5_02_phpmyadmin_skpi.png", "Gambar 1.2. Data Unit Kompetensi Keahlian Siswa pada phpMyAdmin")
    add_body(doc, "Gambar 1.2 menunjukkan 136 unit kompetensi siswa kejuruan yang tersimpan di basis data.")

    add_subbab(doc, "1.2 Implementasi Endpoint API Portofolio Keahlian")
    add_img_academic(doc, "laporan5_03_skill_controller.png", "Gambar 1.3. Implementasi SkillController.php pada Backend Laravel")
    add_body(doc, "Gambar 1.3 memperlihatkan method GET /api/skills/my untuk menyajikan data unit kompetensi siswa.")

    add_img_academic(doc, "laporan5_04_api_skills_test.png", "Gambar 1.4. Hasil Uji Endpoint GET /api/skills/my dengan Respons 200 OK")
    add_body(doc, "Gambar 1.4 membuktikan respons payload 200 OK berisi data keahlian dan asesor BNSP.")

    add_subbab(doc, "1.3 Pengembangan Halaman Portofolio Keahlian Mobile (skills_page.dart)")
    add_img_academic(doc, "laporan5_05_skills_page_code.png", "Gambar 1.5. Potongan Kode skills_page.dart pada Visual Studio Code")
    add_body(doc, "Gambar 1.5 memperlihatkan rancangan widget reactive GetX pada antarmuka portofolio keahlian.")

    add_img_academic(doc, "laporan5_06_skills_mobile_app.png", "Gambar 1.6. Antarmuka Portofolio Keahlian (SKPI) pada Aplikasi Mobile", width_inches=2.8)
    add_body(doc, "Gambar 1.6 menampilkan kartu-kartu kompetensi keahlian dengan predikat Mahir/Terampil.")

    add_subbab(doc, "1.4 Modul Arsip Digital Kelulusan Mobile (arsip_page.dart)")
    add_img_academic(doc, "laporan5_07_arsip_mobile_app.png", "Gambar 1.7. Modul Arsip Digital Kelulusan dengan Tombol Unduh PDF", width_inches=2.8)
    add_body(doc, "Gambar 1.7 mendokumentasikan daftar berkas Ijazah, SKL, dan Transkrip Nilai ber-TTE.")

    add_subbab(doc, "1.5 Sinkronisasi Repositori Fitur SKPI ke GitHub")
    add_img_academic(doc, "laporan5_08_git_push.png", "Gambar 1.8. Eksekusi git push Pembaruan Fitur SKPI dan Arsip Digital")
    add_body(doc, "Gambar 1.8 memperlihatkan terminal eksekusi git push pembaruan modul SKPI ke GitHub.")

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_3.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_3.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai Laporan_Perkembangan_3.docx:", out_docx)

# =============================================================================
# 5. LAPORAN PERKEMBANGAN 4 (PUSH NOTIF, CRON, TRACER & RELEASE)
# =============================================================================
def build_laporan_perkembangan_4():
    doc = create_doc_with_margins()
    add_academic_cover(doc, 
        "LAPORAN PERKEMBANGAN PROYEK 4\nINTEGRASI PUSH NOTIFICATION, OTOMASI TRANSISI KELULUSAN,\nMODUL KEAMANAN, TRACER STUDY & RILIS FINAL",
        "Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile")

    sec1 = doc.add_section()
    setup_page_numbering(sec1, fmt="lowerRoman", start=1)

    p_kp = doc.add_paragraph()
    p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp.paragraph_format.space_before = Pt(10)
    p_kp.paragraph_format.space_after = Pt(14)
    r_kp = p_kp.add_run("KATA PENGANTAR")
    r_kp.font.name = 'Times New Roman'
    r_kp.font.size = Pt(12)
    r_kp.font.bold = True
    r_kp.font.color.rgb = BLACK

    add_body(doc,
        "Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas terselesaikannya Laporan Perkembangan Proyek 4 "
        "yang memaparkan integrasi Push Notification Firebase Cloud Messaging, cron job transisi kelulusan otomatis, "
        "modul keamanan ubah kata sandi, kuesioner tracer study, dan rilis final v1.0.0-smk-release."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(20)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\nPenyusun,\n\n\nWemvi Afrialdo\nNPM. 2413025052")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    sec2 = doc.add_section()
    setup_page_numbering(sec2, fmt="decimal", start=1)

    add_bab_title(doc, "BAB I", "OTOMATISASI SISTEM, TRACER STUDY, DAN RILIS FINAL")

    add_subbab(doc, "1.1 Integrasi Push Notification Firebase Cloud Messaging (FCM)")
    add_img_academic(doc, "laporan6_01_fcm_service_code.png", "Gambar 1.1. Kode Implementasi FcmService.dart pada Flutter")
    add_body(doc, "Gambar 1.1 memperlihatkan kode service FCM untuk penerimaan push notifikasi pesan kelulusan.")

    add_img_academic(doc, "laporan6_02_fcm_notification_app.png", "Gambar 1.2. Banner Push Notification Resmi Kelulusan pada Mobile App", width_inches=2.8)
    add_body(doc, "Gambar 1.2 membuktikan notifikasi pengumuman kelulusan yang muncul secara instan di layar HP pengguna.")

    add_subbab(doc, "1.2 Otomasi Transisi Status Siswa ke Alumni (Scheduled Cron Job)")
    add_img_academic(doc, "laporan6_03_cron_promote_code.png", "Gambar 1.3. Kode Logika Otomasi Command PromoteAlumni.php")
    add_body(doc, "Gambar 1.3 menampilkan logika Artisan command salut:promote-alumni yang dijadwalkan jam 00:00.")

    add_img_academic(doc, "laporan6_04_cron_execution_terminal.png", "Gambar 1.4. Log Terminal Eksekusi Otomatis Cron Job")
    add_body(doc, "Gambar 1.4 membuktikan keberhasilan eksekusi transisi peran 190 siswa aktif menjadi alumni secara massal.")

    add_subbab(doc, "1.3 Peningkatan Keamanan Pengguna: Modul Ubah Kata Sandi Mobile")
    add_img_academic(doc, "laporan6_05_change_password_code.png", "Gambar 1.5. Potongan Kode Validasi Form change_password_page.dart")
    add_body(doc, "Gambar 1.5 menampilkan logika validasi kecocokan kata sandi dan enkripsi bcrypt.")

    add_img_academic(doc, "laporan6_06_change_password_app.png", "Gambar 1.6. Antarmuka Halaman Ubah Kata Sandi pada Mobile App", width_inches=2.8)
    add_body(doc, "Gambar 1.6 menampilkan antarmuka pembaruan kata sandi mandiri oleh pengguna.")

    add_subbab(doc, "1.4 Implementasi Kuesioner Tracer Study Alumni Mobile")
    add_img_academic(doc, "laporan6_07_tracer_study_app.png", "Gambar 1.7. Antarmuka Formulir Kuesioner Tracer Study Alumni", width_inches=2.8)
    add_body(doc, "Gambar 1.7 menampilkan formulir dinamis pelacakan status penyerapan kerja dan kuliah alumni.")

    add_subbab(doc, "1.5 Analitik Ekosistem Kejuruan SMK pada Web Admin")
    add_img_academic(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 1.8. Dasbor Analitik Penyerapan Alumni SMK pada Web Admin")
    add_body(doc, "Gambar 1.8 memperlihatkan grafik doughnut dan batang sebaran keterserapan alumni di DUDI.")

    add_subbab(doc, "1.6 Rilis Final dan Tagging Repositori GitHub")
    add_img_academic(doc, "laporan6_09_git_push_final.png", "Gambar 1.9. Eksekusi Rilis Final dengan Tagging v1.0.0-smk-release ke GitHub")
    add_body(doc, "Gambar 1.9 membuktikan rilis resmi repositori sistem SALUT dengan tag v1.0.0-smk-release.")

    out_docx = os.path.join(ROOT_DIR, "Laporan_Perkembangan_4.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Perkembangan_4.docx")
    doc.save(out_docx)
    doc.save(out_docx_app)
    print("Selesai Laporan_Perkembangan_4.docx:", out_docx)

# =============================================================================
# 6. LAPORAN AKHIR LENGKAP (LAPORAN 7 GABUNGAN: BAB I - IV + LAMPIRAN I & II)
# =============================================================================
def build_laporan_akhir_lengkap():
    doc = create_doc_with_margins()
    add_academic_cover(doc, 
        "LAPORAN AKHIR PENGEMBANGAN SISTEM INFORMASI ARSIP KELULUSAN DAN TRACER STUDY ALUMNI SMK (SALUT)",
        "Disusun untuk memenuhi tugas Matakuliah Pengembangan Aplikasi Mobile")

    # Bagian Awal: Romawi
    sec1 = doc.add_section()
    setup_page_numbering(sec1, fmt="lowerRoman", start=1)

    # KATA PENGANTAR (Halaman i)
    p_kp = doc.add_paragraph()
    p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kp.paragraph_format.space_before = Pt(10)
    p_kp.paragraph_format.space_after = Pt(14)
    r_kp = p_kp.add_run("KATA PENGANTAR")
    r_kp.font.name = 'Times New Roman'
    r_kp.font.size = Pt(12)
    r_kp.font.bold = True
    r_kp.font.color.rgb = BLACK

    add_body(doc,
        "Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa atas segala limpahan rahmat, hidayah, dan karunia-Nya, "
        "sehingga Laporan Komprehensif Perancangan, Instalasi, dan Pengembangan Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK "
        "(SALUT) ini dapat diselesaikan dengan baik dan tepat waktu."
    )
    add_body(doc,
        "Laporan ini disusun sebagai bentuk pertanggungjawaban akademis sekaligus pemenuhan tugas akhir dalam mata kuliah "
        "Pengembangan Aplikasi Mobile pada Program Studi Pendidikan Teknologi Informasi, Jurusan Pendidikan MIPA, Fakultas Keguruan dan "
        "Ilmu Pendidikan, Universitas Lampung. Laporan ini mendokumentasikan pilar utama pengembangan: perancangan spesifikasi kebutuhan dan "
        "mockup antarmuka (SRS), laporan teknis instalasi dan konfigurasi toolchain pengembangan, arsitektur backend RESTful API Laravel 12 dan MySQL, "
        "antarmuka mobile Flutter dengan Dynamic UI Rendering, integrasi portofolio kejuruan SMK (SKPI), otomatisasi kelulusan berbasis cron job "
        "dan Push Notification Firebase, linimasa progres proyek, hingga prototype antarmuka sistem untuk semua peran pengguna."
    )
    add_body(doc,
        "Dalam proses perencanaan, instalasi lingkungan web server, konfigurasi basis data, hingga penyusunan laporan ini, penulis memperoleh "
        "banyak bimbingan, arahan pedagogis, serta dukungan moril maupun teknis dari berbagai pihak. Oleh karena itu, pada kesempatan ini "
        "penulis menyampaikan rasa terima kasih dan apresiasi yang setinggi-tingginya kepada:\n"
        "1. Bapak Ghea Chandra Surawan, M.Pd., selaku Dosen Pengampu mata kuliah Pengembangan Aplikasi Mobile yang senantiasa memberikan "
        "bimbingan, arahan konseptual, dan masukan konstruktif dalam setiap tahapan pengembangan aplikasi ini.\n"
        "2. Bapak dan Ibu Dosen Program Studi Pendidikan Teknologi Informasi FKIP Universitas Lampung atas dedikasi dan transfer wawasan "
        "keilmuan yang sangat berharga.\n"
        "3. Rekan-rekan mahasiswa Program Studi Pendidikan Teknologi Informasi angkatan 2024 yang saling bertukar wawasan, gagasan, dan motivasi "
        "selama perkuliahan.\n"
        "4. Seluruh pihak yang secara langsung maupun tidak langsung telah memberikan kontribusi dan bantuan teknis hingga sistem SALUT dan "
        "laporan ini dapat diselesaikan."
    )
    add_body(doc,
        "Penulis menyadari sepenuhnya bahwa penyusunan laporan ini masih memiliki ruang untuk penyempurnaan. Oleh karena itu, penulis senantiasa "
        "terbuka menerima kritik dan saran yang membangun dari pembaca demi penyempurnaan sistem di masa mendatang. Akhir kata, semoga laporan ini "
        "dapat memberikan manfaat nyata bagi pengembangan teknologi pendidikan dan transformasi digital di institusi kejuruan."
    )

    p_ttd = doc.add_paragraph()
    p_ttd.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_ttd.paragraph_format.space_before = Pt(16)
    p_ttd.paragraph_format.space_after = Pt(20)
    p_ttd.paragraph_format.line_spacing = 1.5
    r_ttd = p_ttd.add_run("Bandar Lampung, 19 Oktober 2026\nPenyusun,\n\n\nWemvi Afrialdo\nNPM. 2413025052")
    r_ttd.font.name = 'Times New Roman'
    r_ttd.font.size = Pt(12)
    r_ttd.font.color.rgb = BLACK

    doc.add_page_break()

    # DAFTAR ISI (Halaman ii)
    p_di = doc.add_paragraph()
    p_di.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_di.paragraph_format.space_before = Pt(10)
    p_di.paragraph_format.space_after = Pt(14)
    r_di = p_di.add_run("DAFTAR ISI")
    r_di.font.name = 'Times New Roman'
    r_di.font.size = Pt(12)
    r_di.font.bold = True
    r_di.font.color.rgb = BLACK

    # Matriks Daftar Isi Selaras Persis dengan Halaman Dokumen
    daftar_isi_master = [
        ("HALAMAN JUDUL", ""),
        ("KATA PENGANTAR", "i"),
        ("DAFTAR ISI", "ii"),
        ("BAB I PENDAHULUAN", "1"),
        ("  1.1 Latar Belakang", "1"),
        ("  1.2 Rumusan Masalah", "1"),
        ("  1.3 Tujuan Pengembangan", "2"),
        ("  1.4 Manfaat Pengembangan", "2"),
        ("BAB II LAPORAN INSTALASI TOOLCHAIN & SERVER", "3"),
        ("  2.1 Persiapan Lingkungan dan Pengunduhan Flutter SDK", "3"),
        ("  2.2 Ekstraksi Berkas dan Konfigurasi Environment Variables PATH", "4"),
        ("  2.3 Instalasi dan Konfigurasi Java Development Kit (JDK 21)", "5"),
        ("  2.4 Instalasi Ekstensi Flutter dan Dart pada Visual Studio Code", "6"),
        ("  2.5 Konfigurasi Android Studio, SDK Tools, dan CMake", "7"),
        ("  2.6 Pengujian Kelayakan Toolchain dengan Flutter Doctor", "8"),
        ("  2.7 Penyiapan Web Server Lokal XAMPP dan Basis Data MySQL", "9"),
        ("  2.8 Instalasi Backend Framework Laravel 12", "10"),
        ("BAB III PEMBAHASAN PENGEMBANGAN SISTEM SALUT", "11"),
        ("  3.1 Perancangan Desain Sistem dan Mockup UI (Laporan 1)", "11"),
        ("  3.2 Pengembangan Backend RESTful API dan Database (Laporan Perkembangan 1)", "14"),
        ("  3.3 Pengembangan Antarmuka Mobile Flutter dan Dynamic UI (Laporan Perkembangan 2)", "17"),
        ("  3.4 Pengembangan Fitur Kejuruan SMK dan Portofolio SKPI (Laporan Perkembangan 3)", "21"),
        ("  3.5 Integrasi Push Notification, Otomasi Cron, dan Tracer Study (Laporan Perkembangan 4)", "25"),
        ("BAB IV PENUTUP", "29"),
        ("  4.1 Kesimpulan", "29"),
        ("  4.2 Saran", "30"),
        ("LAMPIRAN", "31"),
        ("  Lampiran I: Tabel Progres Mingguan Pengembangan Sistem SALUT", "31"),
        ("  Lampiran II: Dokumentasi Screenshot Antarmuka Pengguna Seluruh Role (Admin, Guru, Siswa, Alumni)", "33"),
    ]

    for item_t, item_p in daftar_isi_master:
        is_bold = item_t.startswith("BAB ") or item_t in ["HALAMAN JUDUL", "KATA PENGANTAR", "DAFTAR ISI", "LAMPIRAN"]
        indent = 0.25 if item_t.startswith("  ") else 0
        add_toc_entry(doc, item_t.strip(), item_p, is_bold=is_bold, indent_inch=indent)

    # Bagian Isi: Angka Arab (Mulai Halaman 1)
    sec2 = doc.add_section()
    setup_page_numbering(sec2, fmt="decimal", start=1)

    # =========================================================================
    # BAB I PENDAHULUAN (Halaman 1)
    # =========================================================================
    add_bab_title(doc, "BAB I", "PENDAHULUAN")
    add_subbab(doc, "1.1 Latar Belakang")
    add_body(doc,
        "Perkembangan teknologi informasi dan komunikasi di era Revolusi Industri 4.0 dan Society 5.0 telah mendorong transformasi mendasar "
        "dalam manajemen operasional dan tata kelola administrasi pendidikan kejuruan. Sekolah Menengah Kejuruan (SMK) dituntut untuk mencetak "
        "lulusan yang kompeten, siap kerja, dan terserap optimal di Dunia Usaha dan Dunia Industri (DUDI) maupun melanjutkan pendidikan ke "
        "perguruan tinggi. Namun, pengelolaan dokumen kelulusan (Ijazah Asli, Surat Keterangan Lulus, Transkrip Nilai) saat ini sebagian besar "
        "masih mengandalkan pengarsipan fisik konvensional yang rentan terhadap risiko kerusakan, kehilangan, dan pemalsuan."
    )
    add_body(doc,
        "Di sisi lain, proses pelacakan rekam jejak lulusan (Tracer Study) sering kali menghadapi kendala keterputusan komunikasi antara pihak "
        "sekolah dan alumni. Penyerapan kerja dan keselarasan kurikulum kejuruan menjadi sulit dipantau secara berkala tanpa adanya platform "
        "terintegrasi. Selain itu, nilai rapor akademik siswa kejuruan perlu diperkuat dengan portofolio capaian unit kompetensi keahlian resmi "
        "(SKPI) yang diakui standar Badan Nasional Sertifikasi Profesi (BNSP)."
    )
    add_body(doc,
        "Berdasarkan urgensi tersebut, proyek ini mengembangkan Sistem Informasi Arsip Kelulusan dan Tracer Study Alumni SMK (SALUT) "
        "berbasis arsitektur Client-Server yang memadukan aplikasi mobile Flutter dengan Dynamic UI Rendering serta backend RESTful API "
        "Laravel 12 dan MySQL. Sistem ini dilengkapi fitur otomatisasi transisi status siswa ke alumni melalui scheduled cron job, notifikasi "
        "kelulusan seketika via Firebase Cloud Messaging (FCM), modul SKPI kejuruan, dan panel web admin analitik keterserapan alumni."
    )

    add_subbab(doc, "1.2 Rumusan Masalah")
    add_body(doc,
        "Berdasarkan latar belakang tersebut, rumusan masalah dalam pengembangan ini adalah:\n"
        "1. Bagaimana tahapan instalasi dan konfigurasi toolchain Flutter, Android SDK, JDK 21, dan web server lokal agar sistem dapat dikembangkan secara optimal?\n"
        "2. Bagaimana merancang dan membangun arsitektur backend RESTful API Laravel 12 dan basis data MySQL yang mendukung otorisasi multi-role berbasis token JWT?\n"
        "3. Bagaimana mengimplementasikan antarmuka mobile Flutter yang adaptif dengan konsep Dynamic UI Rendering untuk membedakan peran Siswa Aktif dan Alumni?\n"
        "4. Bagaimana merancang modul Portofolio Capaian Keahlian (SKPI) dan pengarsipan ijazah digital terverifikasi Tanda Tangan Elektronik (TTE) bagi ekosistem kejuruan SMK?\n"
        "5. Bagaimana mengintegrasikan Push Notification FCM dan scheduled cron job untuk mengotomatiskan pengumuman transisi kelulusan secara massal?\n"
        "6. Bagaimana memvisualisasikan data keterserapan lulusan hasil Tracer Study pada panel Web Admin secara interaktif?"
    )

    add_subbab(doc, "1.3 Tujuan Pengembangan")
    add_body(doc,
        "Tujuan dari pengembangan Sistem SALUT ini adalah:\n"
        "1. Mendokumentasikan dan melaksanakan tahapan instalasi toolchain pengembangan secara terstandar tanpa kendala dependensi.\n"
        "2. Menghasilkan backend RESTful API yang aman dengan otentikasi stateless JSON Web Token (JWT) dan skema basis data relasional multi-role.\n"
        "3. Mengembangkan antarmuka mobile Flutter responsif yang mampu bertransformasi dinamis menyesuaikan peran pengguna.\n"
        "4. Menyediakan modul pencatatan 136 unit kompetensi keahlian siswa kejuruan (SKPI) dan penyimpanan aman dokumen ijazah sah ber-TTE.\n"
        "5. Mengotomatiskan transisi status kelulusan siswa menjadi alumni secara serentak menggunakan cron job dan notifikasi push real-time.\n"
        "6. Menyajikan dasbor analitik keterserapan alumni pada Web Admin guna mendukung pengambilan keputusan manajemen sekolah."
    )

    add_subbab(doc, "1.4 Manfaat Pengembangan")
    add_body(doc,
        "Pengembangan sistem SALUT ini diharapkan memberikan manfaat teoretis dan praktis, antara lain:\n"
        "1. Bagi Mahasiswa / Pengembang: Mengasah kompetensi profesional dalam rekayasa perangkat lunak multi-platform, arsitektur REST API, dan tata kelola basis data.\n"
        "2. Bagi SMK Negeri 1 Teladan: Memperoleh sistem tata kelola arsip digital yang aman dari pemalsuan serta memudahkan pemantauan penyerapan lulusan di DUDI.\n"
        "3. Bagi Siswa dan Alumni: Mempermudah akses legalisir berkas ijazah digital kapan saja dan memberikan wadah resmi untuk pelaporan karier pascakelulusan."
    )

    doc.add_page_break()

    # =========================================================================
    # BAB II LAPORAN INSTALASI TOOLCHAIN & SERVER (Halaman 3)
    # =========================================================================
    add_bab_title(doc, "BAB II", "LAPORAN INSTALASI TOOLCHAIN & SERVER")
    add_body(doc,
        "Bab ini menguraikan tahapan teknis pelaksanaan instalasi lingkungan pengembangan aplikasi SALUT pada sistem operasi Windows. "
        "Tahapan dimulai dari pengunduhan paket resmi Flutter, konfigurasi variabel lingkungan, pemasangan Java JDK 21 LTS, penyiapan Android SDK "
        "Command-line Tools, hingga verifikasi menyeluruh melalui perintah `flutter doctor`."
    )

    add_subbab(doc, "2.1 Persiapan Lingkungan dan Pengunduhan Flutter SDK")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step01_flutter_website.png"), "Gambar 2.1. Halaman Pengunduhan Flutter SDK dari Portal Resmi flutter.dev")
    add_body(doc,
        "Gambar 2.1 memperlihatkan portal resmi pengunduhan Flutter SDK stabil. Pengembang mengunduh bundel rilis Windows guna "
        "memperoleh pustaka widget dan kompiler Dart."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step02_download_flutter_zip.png"), "Gambar 2.2. Berkas Arsip Terkompresi Flutter SDK pada Folder Unduhan")
    add_body(doc,
        "Gambar 2.2 mendokumentasikan arsip zip Flutter SDK yang telah diunduh dan siap diekstrak ke direktori kerja sistem."
    )

    add_subbab(doc, "2.2 Ekstraksi Berkas dan Konfigurasi Environment Variables PATH")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step03_environment_variables.png"), "Gambar 2.3. Konfigurasi Variabel Lingkungan Sistem (System Environment Variables)")
    add_body(doc,
        "Gambar 2.3 menunjukkan penambahan jalur direktori `flutter\\bin` ke variabel PATH sistem agar perintah dapat diakses dari terminal PowerShell."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step04_flutter_version_cmd.png"), "Gambar 2.4. Verifikasi Versi Flutter SDK dan Dart pada Terminal Command Prompt")
    add_body(doc,
        "Gambar 2.4 membuktikan keberhasilan pengenalan perintah `flutter --version` pada command prompt dengan channel stable aktif."
    )

    add_subbab(doc, "2.3 Instalasi dan Konfigurasi Java Development Kit (JDK 21)")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step05_download_jdk21.png"), "Gambar 2.5. Berkas Instalasi Java Development Kit 21 (JDK 21 LTS)")
    add_body(doc,
        "Gambar 2.5 menampilkan berkas pemasangan Java Development Kit (JDK 21 LTS) yang dibutuhkan Gradle untuk kompilasi modul Android."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step06_java_version_terminal.png"), "Gambar 2.6. Verifikasi Java Runtime Environment pada Terminal")
    add_body(doc,
        "Gambar 2.6 memvalidasi eksekusi `java -version` yang mengonfirmasi bahwa OpenJDK 64-Bit Server VM telah aktif."
    )

    add_subbab(doc, "2.4 Instalasi Ekstensi Flutter dan Dart pada Visual Studio Code")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step07_vscode_flutter_extension.png"), "Gambar 2.7. Instalasi Ekstensi Resmi Flutter pada Marketplace VS Code")
    add_body(doc,
        "Gambar 2.7 memperlihatkan pemasangan ekstensi Flutter pada VS Code untuk mendukung navigasi kode dan debugging terintegrasi."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step08_vscode_dart_extension.png"), "Gambar 2.8. Instalasi Ekstensi Bahasa Dart pada Visual Studio Code")
    add_body(doc,
        "Gambar 2.8 mendokumentasikan instalasi ekstensi bahasa Dart untuk fitur syntax highlighting dan auto-formatting."
    )

    add_subbab(doc, "2.5 Konfigurasi Android Studio, SDK Tools, dan CMake")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step09_android_sdk_tools_cmake.png"), "Gambar 2.9. Pengaturan Android SDK Command-line Tools dan CMake")
    add_body(doc,
        "Gambar 2.9 menampilkan pemasangan komponen Android SDK Command-line Tools (latest) dan CMake melalui SDK Manager."
    )

    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step10_android_ndk_installed.png"), "Gambar 2.10. Status Pemasangan Android NDK pada SDK Tools")
    add_body(doc,
        "Gambar 2.10 memverifikasi ketersediaan Android NDK untuk proses kompilasi native C/C++ pada layer Android."
    )

    add_subbab(doc, "2.6 Pengujian Kelayakan Toolchain dengan Flutter Doctor")
    add_img_academic(doc, os.path.join(INST_IMG_DIR, "step11_flutter_doctor_output.png"), "Gambar 2.11. Hasil Diagnosa Menyeluruh Perintah flutter doctor")
    add_body(doc,
        "Gambar 2.11 menunjukkan hasil diagnosa `flutter doctor` dengan status seluruh komponen bertanda centang hijau tanpa kendala (No issues found!)."
    )

    doc.add_page_break()

    # =========================================================================
    # BAB III PEMBAHASAN PENGEMBANGAN SISTEM SALUT (Halaman 11)
    # =========================================================================
    add_bab_title(doc, "BAB III", "PEMBAHASAN PENGEMBANGAN SISTEM SALUT")
    add_body(doc,
        "Bab ini membahas secara komprehensif siklus perancangan dan implementasi sistem informasi SALUT, meliputi pemodelan spesifikasi "
        "kebutuhan perangkat lunak (SRS) dan mockup UI, arsitektur backend RESTful API Laravel 12 dan MySQL, antarmuka mobile Flutter "
        "dengan Dynamic UI Rendering, modul ekosistem kejuruan SMK (SKPI), hingga integrasi Push Notification FCM dan scheduled cron job."
    )

    # 3.1 MOCKUP DESAIN (LAPORAN 1)
    add_subbab(doc, "3.1 Perancangan Desain Sistem dan Mockup UI (Laporan 1)")
    add_body(doc,
        "Perancangan antarmuka sistem SALUT berpedoman pada konsep clean academic modern. Antarmuka terbagi menjadi dua ranah utama: "
        "aplikasi mobile bagi Siswa Aktif dan Alumni yang mengedepankan kemudahan navigasi satu tangan, serta Web Admin panel bagi Administrator "
        "Tata Usaha dan Guru yang berfungsi sebagai pusat kendali verifikasi data."
    )
    add_img_academic(doc, "image12.png", "Gambar 3.1. Desain Mockup Antarmuka Mobile Android - Halaman Manajemen dan Akses Data", width_inches=2.8)
    add_body(doc,
        "Gambar 3.1 menampilkan desain mockup mobile Android dengan navigasi bawah (bottom navigation) dan filter terstruktur."
    )
    add_img_academic(doc, "image14.png", "Gambar 3.2. Desain Mockup Antarmuka Desktop Web Admin Panel", width_inches=5.8)
    add_body(doc,
        "Gambar 3.2 mengilustrasikan dasbor desktop dengan sidebar menu navigasi dan tabel master data civitas sekolah."
    )

    # 3.2 BACKEND & DATABASE (LAPORAN PERKEMBANGAN 1)
    add_subbab(doc, "3.2 Pengembangan Backend RESTful API dan Database (Laporan Perkembangan 1)")
    add_body(doc,
        "Pada sisi server, dibangun RESTful API menggunakan framework Laravel 12 yang berkomunikasi dengan basis data MySQL (db_salut). "
        "Sistem otorisasi stateless diimplementasikan menggunakan paket JSON Web Token (php-open-source-saver/jwt-auth) untuk mengamankan data pengguna."
    )
    add_img_academic(doc, "laporan3_01_env.png", "Gambar 3.3. Konfigurasi Variabel Lingkungan .env untuk Koneksi Basis Data MySQL")
    add_body(doc, "Gambar 3.3 menunjukkan pengaturan koneksi MySQL pada port 3306.")
    
    add_img_academic(doc, "laporan3_03_phpmyadmin.png", "Gambar 3.4. Tampilan Tabel Basis Data db_salut pada phpMyAdmin")
    add_body(doc, "Gambar 3.4 memvalidasi keberhasilan migrasi skema tabel pengguna, profil siswa, nilai, dan prestasi.")

    add_img_academic(doc, "laporan3_04_routes_api.png", "Gambar 3.5. Definisi Rute RESTful API dan Proteksi JWT pada routes/api.php")
    add_body(doc, "Gambar 3.5 menampilkan proteksi middleware jwt.auth pada rute tertutup.")

    add_img_academic(doc, "laporan3_05_api_testing.png", "Gambar 3.6. Hasil Uji API Login dengan Status HTTP 200 OK dan Payload Token")
    add_body(doc, "Gambar 3.6 membuktikan pengujian API login berhasil mengembalikan respons 200 OK dan token otorisasi.")

    # 3.3 FRONTEND FLUTTER & DYNAMIC UI (LAPORAN PERKEMBANGAN 2)
    add_subbab(doc, "3.3 Pengembangan Antarmuka Mobile Flutter dan Dynamic UI (Laporan Perkembangan 2)")
    add_body(doc,
        "Aplikasi mobile dikembangkan menggunakan framework Flutter dengan menerapkan state management reactive GetX. "
        "Diterapkan konsep Dynamic UI Rendering di mana tampilan dashboard secara otomatis bertransformasi menyesuaikan peran pengguna (Siswa Aktif vs Alumni)."
    )
    add_img_academic(doc, "laporan4_02_api_service_code.png", "Gambar 3.7. Implementasi Dio HTTP Client dan Interceptor Token JWT")
    add_body(doc, "Gambar 3.7 memperlihatkan kelas ApiService yang menyematkan Bearer Token pada setiap request data.")

    add_img_academic(doc, "laporan4_04_dashboard_siswa_app.png", "Gambar 3.8. Antarmuka Dasbor untuk Peran Siswa Aktif", width_inches=2.8)
    add_body(doc, "Gambar 3.8 menyajikan dasbor Siswa Aktif dengan menu pengajuan prestasi dan nilai rapor.")

    add_img_academic(doc, "laporan4_05_dashboard_alumni_app.png", "Gambar 3.9. Antarmuka Dasbor untuk Peran Alumni", width_inches=2.8)
    add_body(doc, "Gambar 3.9 menampilkan transformasi beranda Alumni dengan akses unduh ijazah dan formulir tracer study.")

    add_img_academic(doc, "laporan4_06_role_logic_code.png", "Gambar 3.10. Kode Logika Pengkondisian Menu Per-Role pada Flutter")
    add_body(doc, "Gambar 3.10 membuktikan logika seleksi menu berbasis role yang dieksekusi secara otomatis.")

    # 3.4 EKOSISTEM SMK & SKPI (LAPORAN PERKEMBANGAN 3)
    add_subbab(doc, "3.4 Pengembangan Fitur Kejuruan SMK dan Portofolio SKPI (Laporan Perkembangan 3)")
    add_body(doc,
        "Untuk mengakomodasi kekhususan SMK, dirancang tabel skill_competencies yang menampung 136 unit kompetensi keahlian siswa "
        "sesuai jurusan (RPL, TKJ, Multimedia). Dibangun modul skills_page.dart serta arsip dokumen kelulusan digital ber-TTE."
    )
    add_img_academic(doc, "laporan5_01_migration_skpi.png", "Gambar 3.11. Migration Tabel skill_competencies untuk Modul SKPI SMK")
    add_body(doc, "Gambar 3.11 mendokumentasikan skema pencatatan keahlian siswa dengan predikat kemahiran dan nama asesor.")

    add_img_academic(doc, "laporan5_04_api_skills_test.png", "Gambar 3.12. Hasil Uji Endpoint GET /api/skills/my dengan Respons 200 OK")
    add_body(doc, "Gambar 3.12 membuktikan ketersediaan data unit kompetensi keahlian secara real-time via API.")

    add_img_academic(doc, "laporan5_06_skills_mobile_app.png", "Gambar 3.13. Antarmuka Portofolio Keahlian (SKPI) pada Mobile App", width_inches=2.8)
    add_body(doc, "Gambar 3.13 menampilkan kartu kompetensi kejuruan dengan predikat Mahir dan opsi unduh SKPI.")

    add_img_academic(doc, "laporan5_07_arsip_mobile_app.png", "Gambar 3.14. Modul Arsip Dokumen Digital Kelulusan Mobile", width_inches=2.8)
    add_body(doc, "Gambar 3.14 mendokumentasikan daftar unduhan berkas PDF Ijazah Asli, SKL, dan Transkrip Nilai sah ber-TTE.")

    # 3.5 OTOMASI, PUSH NOTIF & TRACER STUDY (LAPORAN PERKEMBANGAN 4)
    add_subbab(doc, "3.5 Integrasi Push Notification, Otomasi Cron, dan Tracer Study (Laporan Perkembangan 4)")
    add_body(doc,
        "Pada tahap akhir pengembangan, diintegrasikan layanan Push Notification Firebase Cloud Messaging (fcm_service.dart), "
        "otomasi transisi kelulusan siswa ke alumni via scheduled cron job `salut:promote-alumni` jam 00:00, modul tracer study dinamis, "
        "serta rilis resmi standalone APK pada perangkat HP Samsung Galaxy A25 5G."
    )
    add_img_academic(doc, "laporan6_01_fcm_service_code.png", "Gambar 3.15. Kode Implementasi FcmService.dart untuk Notifikasi Kelulusan")
    add_body(doc, "Gambar 3.15 memperlihatkan integrasi Firebase Cloud Messaging untuk notifikasi real-time.")

    add_img_academic(doc, "laporan6_03_cron_promote_code.png", "Gambar 3.16. Kode Logika Otomasi Command PromoteAlumni.php")
    add_body(doc, "Gambar 3.16 menampilkan artisan command yang secara otomatis mempromosikan siswa menjadi alumni.")

    add_img_academic(doc, "laporan6_07_tracer_study_app.png", "Gambar 3.17. Formulir Kuesioner Tracer Study Alumni pada Mobile", width_inches=2.8)
    add_body(doc, "Gambar 3.17 mendokumentasikan form pelacakan keterserapan alumni di industri dan kampus.")

    add_img_academic(doc, "laporan6_08_webadmin_smk_analytics.png", "Gambar 3.18. Dasbor Analitik Penyerapan Alumni SMK pada Web Admin")
    add_body(doc, "Gambar 3.18 menampilkan grafik sebaran keterserapan alumni (Bekerja 65%, Kuliah 25%, Wirausaha 10%).")

    doc.add_page_break()

    # =========================================================================
    # BAB IV PENUTUP (Halaman 29)
    # =========================================================================
    add_bab_title(doc, "BAB IV", "PENUTUP")
    add_subbab(doc, "4.1 Kesimpulan")
    add_body(doc,
        "Berdasarkan seluruh rangkaian perancangan, instalasi toolchain, pengembangan modul backend dan mobile, integrasi ekosistem kejuruan SMK, "
        "hingga pengujian rilis mandiri yang telah dipaparkan, dapat ditarik beberapa kesimpulan pokok sebagai berikut:\n"
        "1. Keberhasilan Penyiapan Toolchain: Rantai perkakas Flutter SDK, Dart, JDK 21 LTS, Android SDK Tools, dan XAMPP Server berhasil dikonfigurasi tanpa kendala (flutter doctor 100% OK).\n"
        "2. Integritas Arsitektur Client-Server: Backend RESTful API Laravel 12 dan basis data MySQL terhubung sempurna dengan aplikasi mobile Flutter melalui otentikasi stateless Bearer Token JWT.\n"
        "3. Efektivitas Dynamic UI Rendering: Konsep antarmuka adaptif berbasis reactive GetX terbukti sukses membedakan hak akses dan menu navigasi antara Siswa Aktif dan Alumni secara real-time.\n"
        "4. Keselarasan dengan Kebutuhan SMK: Penyediaan modul Portofolio Keahlian (SKPI) 136 unit kompetensi dan modul arsip ijazah digital ber-TTE memberikan nilai tambah nyata bagi SMK Negeri 1 Teladan.\n"
        "5. Efisiensi Melalui Otomatisasi: Pemanfaatan scheduled cron job `salut:promote-alumni` dan Firebase Cloud Messaging berhasil meniadakan pemindahan status kelulusan secara manual.\n"
        "6. Kesiapan Operasional Standalone: Aplikasi Flutter berhasil dikompilasi menjadi Standalone Release APK (54.6 MB) dan berjalan mulus 100% pada perangkat fisik HP Samsung Galaxy A25 5G."
    )

    add_subbab(doc, "4.2 Saran")
    add_body(doc,
        "Demi penyempurnaan dan keberlanjutan pemanfaatan sistem informasi SALUT di masa mendatang, beberapa saran konstruktif yang direkomendasikan adalah:\n"
        "1. Integrasi Tanda Tangan Elektronik Tersertifikasi BSrE: Disarankan untuk mengintegrasikan layanan Balai Sertifikasi Elektronik (BSrE) guna memperkuat keabsahan yuridis dokumen ijazah digital secara nasional.\n"
        "2. Pengembangan Modul Bursa Kerja Khusus (BKK): Mengintegrasikan portal lowongan kerja mitra industri sekolah agar alumni dapat langsung melamar pekerjaan dari aplikasi mobile.\n"
        "3. Uji Beban Server Berskala Besar: Melakukan stress testing pada backend server menjelang hari pengumuman kelulusan untuk memastikan kestabilan saat diakses ribuan pengguna secara serentak."
    )

    doc.add_page_break()

    # =========================================================================
    # LAMPIRAN (Halaman 31)
    # =========================================================================
    p_lamp = doc.add_paragraph()
    p_lamp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lamp.paragraph_format.space_before = Pt(14)
    p_lamp.paragraph_format.space_after = Pt(4)
    r_lp = p_lamp.add_run("LAMPIRAN\n")
    r_lp.font.name = 'Times New Roman'
    r_lp.font.size = Pt(12)
    r_lp.font.bold = True
    r_lp.font.color.rgb = BLACK
    
    r_lp2 = p_lamp.add_run("TABEL PROGRES KEGIATAN MINGGUAN PENGEMBANGAN SISTEM SALUT")
    r_lp2.font.name = 'Times New Roman'
    r_lp2.font.size = Pt(12)
    r_lp2.font.bold = True
    r_lp2.font.color.rgb = BLACK

    add_body(doc,
        "Tabel di bawah ini mendokumentasikan rekam jejak progres mingguan pengembangan sistem informasi SALUT mulai dari inisiasi konsep, "
        "penyiapan lingkungan server, pembuatan arsitektur basis data, pengembangan antarmuka mobile, hingga pengujian dan deployment akhir:"
    )

    timeline_data = [
        ("1", "28 - 29 Sep 2026", "Inisiasi Proyek, Analisis Kebutuhan SRS, dan Perancangan Desain Mockup UI", "Dokumen SRS SALUT & Mockup Desain Mobile dan Desktop", "Selesai (100%)"),
        ("2", "30 Sep 2026", "Instalasi Lingkungan Toolchain (Flutter SDK, Dart, JDK 21, Android Studio, VS Code)", "Toolchain siap pakai & verifikasi flutter doctor centang hijau", "Selesai (100%)"),
        ("3", "01 - 02 Okt 2026", "Setup Backend Laravel 12, Migrations Database, Model Eloquent, dan Autentikasi JWT", "Backend RESTful API aktif & pengujian login 200 OK berhasil", "Selesai (100%)"),
        ("4", "03 - 05 Okt 2026", "Pengembangan UI Mobile Flutter, HTTP Dio Interceptor, dan Dynamic UI Rendering", "Aplikasi mobile login & dashboard adaptif Siswa vs Alumni", "Selesai (100%)"),
        ("5", "12 - 13 Okt 2026", "Implementasi Ekosistem SMK: Tabel SKPI, SkillController, dan Modul Arsip Ijazah", "Tercatat 136 unit kompetensi keahlian dan arsip digital ber-TTE", "Selesai (100%)"),
        ("6", "14 - 15 Okt 2026", "Integrasi Push Notification FCM, Scheduled Cron Kelulusan, dan Tracer Study", "Otomasi transisi status jam 00:00 & analitik penyerapan alumni", "Selesai (100%)"),
        ("7", "16 - 18 Okt 2026", "Redesign Modern UI, Pembuatan Splash Screen 3 Detik, dan Rilis Standalone APK", "Standalone APK Release (54.6 MB) terpasang di HP Samsung A25", "Selesai (100%)"),
    ]

    tbl_tl = doc.add_table(rows=len(timeline_data) + 1, cols=5)
    tbl_tl.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["No.", "Tanggal", "Agenda & Kegiatan Pengembangan", "Output / Capaian Kegiatan", "Status / Progres"]
    col_widths = [0.5, 1.1, 2.2, 1.8, 0.8]

    hdr_cells = tbl_tl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        hdr_cells[i].width = Inches(col_widths[i])
        set_cell_background(hdr_cells[i], "E5E7EB")
        set_cell_margins(hdr_cells[i], top=80, bottom=80, left=80, right=80)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = BLACK

    for row_idx, data in enumerate(timeline_data, start=1):
        row_cells = tbl_tl.rows[row_idx].cells
        bg_color = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(data):
            row_cells[col_idx].text = text
            row_cells[col_idx].width = Inches(col_widths[col_idx])
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=80, right=80)
            p = row_cells[col_idx].paragraphs[0]
            if col_idx in [0, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif col_idx == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.3
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10.5)
                r.font.color.rgb = BLACK
                if col_idx in [0, 4]:
                    r.font.bold = True

    doc.add_page_break()

    # LAMPIRAN II: TEMPLATE SCREENSHOT SEMUA USER (Halaman 33)
    p_lamp2 = doc.add_paragraph()
    p_lamp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lamp2.paragraph_format.space_before = Pt(14)
    p_lamp2.paragraph_format.space_after = Pt(4)
    r_l2 = p_lamp2.add_run("LAMPIRAN II\n")
    r_l2.font.name = 'Times New Roman'
    r_l2.font.size = Pt(12)
    r_l2.font.bold = True
    r_l2.font.color.rgb = BLACK
    
    r_l2b = p_lamp2.add_run("DOKUMENTASI SCREENSHOT ANTARMUKA PENGGUNA SELURUH ROLE\n(ADMINISTRATOR, GURU, SISWA AKTIF, ALUMNI)")
    r_l2b.font.name = 'Times New Roman'
    r_l2b.font.size = Pt(12)
    r_l2b.font.bold = True
    r_l2b.font.color.rgb = BLACK

    add_body(doc,
        "Bagian ini disediakan secara khusus sebagai lembar kerja dokumentasi visual tangkapan layar langsung (screenshot) "
        "yang diambil oleh pengembang dari perangkat uji coba aktual. Disediakan kotak templat resmi bergaris batas presisi "
        "untuk seluruh 4 aktor sistem SALUT (Administrator, Guru, Siswa Aktif, dan Alumni):"
    )

    # 1. ROLE ADMINISTRATOR
    add_sub_subbab(doc, "1. DOKUMENTASI ANTARMUKA ROLE ADMINISTRATOR (WEB ADMIN PANEL)")
    add_template_placeholder(doc, "Gambar L.1. Dasbor Statistik & Analitik Kejuruan SMK (Role Admin)", "Tempelkan tangkapan layar dasbor analitik keterserapan alumni, sebaran jurusan, dan metrik sistem.")
    add_template_placeholder(doc, "Gambar L.2. Manajemen Master Data Siswa & Alumni (Role Admin)", "Tempelkan tangkapan layar tabel data siswa, filter kelas/angkatan, dan fitur Import CSV.")
    add_template_placeholder(doc, "Gambar L.3. Pengelolaan Arsip Dokumen Digital Ijazah & SKL (Role Admin)", "Tempelkan tangkapan layar verifikasi berkas ijazah sah dan modal unggah dokumen alumni.")
    add_template_placeholder(doc, "Gambar L.4. Penjadwalan Rilis Kelulusan Otomatis (Role Admin)", "Tempelkan tangkapan layar pengaturan tanggal/jam rilis pengumuman kelulusan terjadwal.")
    add_template_placeholder(doc, "Gambar L.5. Rekapitulasi & Grafik Analitik Tracer Study (Role Admin)", "Tempelkan tangkapan layar grafik doughnut sebaran alumni (Bekerja, Kuliah, Wirausaha).")

    # 2. ROLE GURU
    add_sub_subbab(doc, "2. DOKUMENTASI ANTARMUKA ROLE GURU (WEB ADMIN PANEL)")
    add_template_placeholder(doc, "Gambar L.6. Modul Penginputan Nilai Rapor Siswa Per Semester (Role Guru)", "Tempelkan tangkapan layar tabel input nilai mata pelajaran per semester siswa.")
    add_template_placeholder(doc, "Gambar L.7. Validasi Portofolio Capaian Keahlian Siswa SKPI (Role Guru)", "Tempelkan tangkapan layar pengesahan unit kompetensi kejuruan dan penetapan skor uji siswa.")

    # 3. ROLE SISWA AKTIF
    add_sub_subbab(doc, "3. DOKUMENTASI ANTARMUKA ROLE SISWA AKTIF (MOBILE FLUTTER APP)")
    add_template_placeholder(doc, "Gambar L.8. Halaman Splash Screen & Autentikasi Login Siswa (Role Siswa)", "Tempelkan tangkapan layar tampilan splash screen 3 detik dan form login pada HP Samsung Anda.")
    add_template_placeholder(doc, "Gambar L.9. Halaman Dasbor Utama Siswa Aktif (Role Siswa)", "Tempelkan tangkapan layar beranda siswa aktif berisi kartu profil, banner SKPI, dan riwayat prestasi.")
    add_template_placeholder(doc, "Gambar L.10. Halaman Pengajuan Prestasi & Modal Pop-Up Konfirmasi (Role Siswa)", "Tempelkan tangkapan layar form pengajuan prestasi dan dialog pop-up konfirmasi berhasil dikirim.")
    add_template_placeholder(doc, "Gambar L.11. Halaman Portofolio Capaian Keahlian Siswa SKPI (Role Siswa)", "Tempelkan tangkapan layar kartu kompetensi kejuruan siswa lengkap dengan predikat kemahiran.")

    # 4. ROLE ALUMNI
    add_sub_subbab(doc, "4. DOKUMENTASI ANTARMUKA ROLE ALUMNI (MOBILE FLUTTER APP)")
    add_template_placeholder(doc, "Gambar L.12. Halaman Dasbor Utama Alumni (Role Alumni)", "Tempelkan tangkapan layar beranda alumni dengan status kelulusan dan menu tracer study di HP Samsung.")
    add_template_placeholder(doc, "Gambar L.13. Modul Arsip Digital Kelulusan Ijazah & SKL Sah Ber-TTE (Role Alumni)", "Tempelkan tangkapan layar daftar unduhan berkas PDF Ijazah Asli dan SKL terverifikasi.")
    add_template_placeholder(doc, "Gambar L.14. Formulir Kuesioner Tracer Study Alumni Dinamis (Role Alumni)", "Tempelkan tangkapan layar pengisian form tracer study (status bekerja/kuliah dan nama instansi).")
    add_template_placeholder(doc, "Gambar L.15. Modul Pengaturan Keamanan Akun & Ubah Kata Sandi (Role Alumni)", "Tempelkan tangkapan layar halaman ubah kata sandi akun pada perangkat mobile.")

    out_docx = os.path.join(ROOT_DIR, "Laporan_Akhir_Lengkap.docx")
    out_docx_app = os.path.join(BASE_DIR, "Laporan_Akhir_Lengkap.docx")
    try:
        doc.save(out_docx)
        print("Selesai Laporan_Akhir_Lengkap.docx:", out_docx)
    except PermissionError:
        alt_out = os.path.join(ROOT_DIR, "Laporan_Akhir_Lengkap_Makalah_Unila.docx")
        doc.save(alt_out)
        print("File utama sedang dibuka di Word, berhasil disimpan sebagai:", alt_out)
    try:
        doc.save(out_docx_app)
        print("Selesai Laporan_Akhir_Lengkap.docx di apps_sekolah:", out_docx_app)
    except PermissionError:
        pass

if __name__ == "__main__":
    print("Memulai kompilasi seluruh laporan sesuai standar dokumen makalah Unila...")
    build_laporan_instalasi_only()
    build_laporan_perkembangan_1()
    build_laporan_perkembangan_2()
    build_laporan_perkembangan_3()
    build_laporan_perkembangan_4()
    build_laporan_akhir_lengkap()
    print("SELURUH 6 DOKUMEN LAPORAN BERHASIL DIBUAT DENGAN SEMPURNA!")
