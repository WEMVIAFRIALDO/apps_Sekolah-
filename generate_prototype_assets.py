# -*- coding: utf-8 -*-
"""
Script Generator Aset Screenshot Prototype Akhir Sistem SALUT
Mencakup Tampilan 4 Role:
1. Admin (Web Admin: Students, Arsip, Schedules, Tracer)
2. Guru (Web Admin: Rapor, Skills/SKPI)
3. Siswa (Mobile: Prestasi Pop-up)
Penulis: Wemvi Afrialdo
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"d:\proyek_applikasi\apps_sekolah\laporan_screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_CODE = r"C:\Windows\Fonts\consola.ttf"
FONT_UI = r"C:\Windows\Fonts\segoeui.ttf"
FONT_UI_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_ARIAL = r"C:\Windows\Fonts\arial.ttf"

def get_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def draw_window_frame(draw, width, height, title, subtitle="", bg_color=(248, 250, 252)):
    draw.rectangle([0, 0, width, height], fill=bg_color)
    draw.rectangle([0, 0, width, 38], fill=(30, 41, 59))
    draw.line([0, 38, width, 38], fill=(51, 65, 85), width=1)
    draw.ellipse([14, 13, 26, 25], fill=(239, 68, 68))
    draw.ellipse([34, 13, 46, 25], fill=(245, 158, 11))
    draw.ellipse([54, 13, 66, 25], fill=(34, 197, 94))
    f_title = get_font(FONT_UI_BOLD, 12)
    draw.text((78, 11), title, font=f_title, fill=(241, 245, 249))
    if subtitle:
        f_sub = get_font(FONT_UI, 11)
        draw.text((width - 320, 12), subtitle, font=f_sub, fill=(148, 163, 184))

def draw_web_sidebar(draw, active_menu="Dashboard", is_guru=False):
    draw.rectangle([0, 39, 210, 620], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.rectangle([18, 52, 46, 80], fill=(30, 58, 95))
    draw.text((26, 56), "S", font=get_font(FONT_UI_BOLD, 18), fill=(255, 255, 255))
    draw.text((54, 54), "SALUT ADMIN", font=get_font(FONT_UI_BOLD, 12), fill=(15, 23, 42))
    draw.text((54, 69), "SMK Negeri 1 Teladan", font=get_font(FONT_UI, 9), fill=(100, 116, 139))
    draw.line([0, 94, 210, 94], fill=(226, 232, 240), width=1)
    
    if not is_guru:
        menus = [
            ("Dashboard", "📊"),
            ("Siswa & Alumni", "👥"),
            ("Arsip Dokumen", "📁"),
            ("Jadwal Lulus", "📅"),
            ("Tracer Study", "🎓"),
            ("Input Rapor", "📝"),
            ("Portofolio SKPI", "⭐"),
        ]
    else:
        menus = [
            ("Dashboard", "📊"),
            ("Input Rapor", "📝"),
            ("Portofolio SKPI", "⭐"),
        ]
    
    my = 108
    for mname, micon in menus:
        if mname == active_menu:
            draw.rectangle([10, my, 200, my+34], fill=(238, 242, 255), outline=(199, 210, 254))
            draw.text((22, my+8), micon, font=get_font(FONT_UI, 12), fill=(67, 56, 202))
            draw.text((45, my+8), mname, font=get_font(FONT_UI_BOLD, 11), fill=(67, 56, 202))
        else:
            draw.text((22, my+8), micon, font=get_font(FONT_UI, 12), fill=(100, 116, 139))
            draw.text((45, my+8), mname, font=get_font(FONT_UI, 11), fill=(71, 85, 105))
        my += 38
        
    draw.line([0, 560, 210, 560], fill=(226, 232, 240), width=1)
    user_name = "Budi Hermawan (Guru)" if is_guru else "Administrator TU"
    draw.text((20, 570), user_name, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
    draw.text((20, 586), "Online • Sesi Terproteksi", font=get_font(FONT_UI, 9), fill=(16, 185, 129))

def make_proto_admin_students():
    w, h = 980, 620
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - Manajemen Data Siswa & Alumni", "Role: Administrator")
    draw_web_sidebar(draw, "Siswa & Alumni", is_guru=False)
    
    draw.text((230, 55), "Master Data Siswa & Alumni", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((230, 78), "Pengelolaan seluruh civitas siswa SMK aktif dan lulusan", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    draw.rectangle([w-250, 55, w-130, 85], fill=(30, 58, 95))
    draw.text((w-235, 62), "+ Tambah Siswa", font=get_font(FONT_UI_BOLD, 10), fill=(255, 255, 255))
    draw.rectangle([w-120, 55, w-20, 85], fill=(16, 185, 129))
    draw.text((w-110, 62), "📥 Import CSV", font=get_font(FONT_UI_BOLD, 10), fill=(255, 255, 255))
    
    draw.rectangle([230, 105, 450, 135], fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((240, 113), "🔍 Cari Nama / NISN...", font=get_font(FONT_UI, 10), fill=(148, 163, 184))
    
    draw.rectangle([460, 105, 580, 135], fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((470, 113), "Role: Semua ▼", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    
    draw.rectangle([590, 105, 730, 135], fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((600, 113), "Jurusan: Semua ▼", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    
    draw.rectangle([230, 150, w-20, 570], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.rectangle([230, 150, w-20, 185], fill=(241, 245, 249))
    
    cols = [
        ("NISN", 245),
        ("Nama Lengkap", 345),
        ("Jurusan SMK", 520),
        ("Kelas / Angkatan", 670),
        ("Role", 780),
        ("Aksi", 880)
    ]
    for cname, cx in cols:
        draw.text((cx, 160), cname, font=get_font(FONT_UI_BOLD, 10), fill=(71, 85, 105))
        
    rows = [
        ("0051234567", "Budi Santoso", "Rekayasa Perangkat Lunak", "XII RPL 1 (2026)", "Siswa", (238, 242, 255), (67, 56, 202)),
        ("0051234568", "Ahmad Fauzi", "Teknik Komputer & Jaringan", "XII TKJ 1 (2026)", "Siswa", (238, 242, 255), (67, 56, 202)),
        ("0051234569", "Dewi Anggraini", "Multimedia", "XII MM 1 (2026)", "Siswa", (238, 242, 255), (67, 56, 202)),
        ("0067890123", "Siti Rahayu", "Rekayasa Perangkat Lunak", "Lulusan 2024", "Alumni", (236, 253, 245), (16, 185, 129)),
        ("0043219876", "Rian Hidayat", "Teknik Komputer & Jaringan", "Lulusan 2024", "Alumni", (236, 253, 245), (16, 185, 129)),
        ("0051234570", "Farhan Pratama", "Rekayasa Perangkat Lunak", "XI RPL 1 (2027)", "Siswa", (238, 242, 255), (67, 56, 202)),
        ("0051234571", "Nadia Permata", "Teknik Komputer & Jaringan", "XI TKJ 2 (2027)", "Siswa", (238, 242, 255), (67, 56, 202)),
        ("0051234572", "Yoga Saputra", "Multimedia", "X MM 1 (2028)", "Siswa", (238, 242, 255), (67, 56, 202)),
    ]
    
    ry = 195
    for nisn, nama, jur, kls, role, bg_badge, fg_badge in rows:
        draw.line([230, ry+35, w-20, ry+35], fill=(241, 245, 249), width=1)
        draw.text((245, ry+8), nisn, font=get_font(FONT_CODE, 10), fill=(15, 23, 42))
        draw.text((345, ry+8), nama, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
        draw.text((520, ry+8), jur, font=get_font(FONT_UI, 10), fill=(71, 85, 105))
        draw.text((670, ry+8), kls, font=get_font(FONT_UI, 10), fill=(71, 85, 105))
        
        draw.rectangle([780, ry+5, 835, ry+26], fill=bg_badge, outline=fg_badge)
        draw.text((792, ry+7), role, font=get_font(FONT_UI_BOLD, 9), fill=fg_badge)
        
        draw.rectangle([875, ry+5, 935, ry+26], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((885, ry+7), "Edit / Detail", font=get_font(FONT_UI, 9), fill=(30, 58, 95))
        ry += 42
        
    path = os.path.join(OUTPUT_DIR, "proto_admin_students.png")
    im.save(path)
    print("Saved:", path)

def make_proto_admin_arsip():
    w, h = 980, 620
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - Manajemen Arsip Digital Ijazah & SKL", "Modul Tata Usaha")
    draw_web_sidebar(draw, "Arsip Dokumen", is_guru=False)
    
    draw.text((230, 55), "Arsip Digital Kelulusan & Ijazah Siswa", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((230, 78), "Pengunggahan dan validasi berkas ijazah sah dengan QR-Code verifikasi", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    cards = [
        ("Total Berkas Tersimpan", "380 Berkas", "📁 100% Terenkripsi", (238, 242, 255), (67, 56, 202)),
        ("Ijazah Terverifikasi", "190 Siswa", "✅ TTE Kepala Sekolah", (236, 253, 245), (16, 185, 129)),
        ("Menunggu Unggah", "0 Berkas", "⚡ Seluruh Angkatan Lengkap", (254, 243, 199), (245, 158, 11)),
    ]
    cx = 230
    for ctitle, cval, csub, bg_c, fg_c in cards:
        draw.rectangle([cx, 105, cx+225, 175], fill=bg_c, outline=fg_c)
        draw.text((cx+15, 115), ctitle, font=get_font(FONT_UI, 10), fill=fg_c)
        draw.text((cx+15, 132), cval, font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
        draw.text((cx+15, 155), csub, font=get_font(FONT_UI, 9), fill=(71, 85, 105))
        cx += 245
        
    draw.rectangle([230, 190, w-20, 580], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.rectangle([230, 190, w-20, 225], fill=(241, 245, 249))
    cols = [
        ("NISN", 245),
        ("Nama Siswa/Alumni", 350),
        ("Ijazah Asli", 520),
        ("SKL Digital", 640),
        ("Transkrip", 750),
        ("Kelola Berkas", 860)
    ]
    for cname, cx_col in cols:
        draw.text((cx_col, 200), cname, font=get_font(FONT_UI_BOLD, 10), fill=(71, 85, 105))
        
    rows = [
        ("0067890123", "Siti Rahayu (Alumni 2024)", "Tersedia (2.4 MB)", "Tersedia (840 KB)", "Tersedia (1.1 MB)"),
        ("0043219876", "Rian Hidayat (Alumni 2024)", "Tersedia (2.3 MB)", "Tersedia (820 KB)", "Tersedia (1.0 MB)"),
        ("0051234567", "Budi Santoso (XII RPL 1)", "Draft Terverifikasi", "Tersedia (810 KB)", "Semester 1-5 Sah"),
        ("0051234568", "Ahmad Fauzi (XII TKJ 1)", "Draft Terverifikasi", "Tersedia (815 KB)", "Semester 1-5 Sah"),
        ("0051234569", "Dewi Anggraini (XII MM 1)", "Draft Terverifikasi", "Tersedia (805 KB)", "Semester 1-5 Sah"),
        ("0051234570", "Farhan Pratama (XI RPL 1)", "Belum Terbit", "Belum Terbit", "Semester 1-3 Sah"),
    ]
    ry = 235
    for nisn, nama, ijz, skl, trs in rows:
        draw.line([230, ry+38, w-20, ry+38], fill=(241, 245, 249), width=1)
        draw.text((245, ry+10), nisn, font=get_font(FONT_CODE, 10), fill=(15, 23, 42))
        draw.text((350, ry+10), nama, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
        
        draw.rectangle([520, ry+6, 620, ry+28], fill=(236, 253, 245), outline=(16, 185, 129))
        draw.text((526, ry+9), ijz[:14], font=get_font(FONT_UI, 9), fill=(16, 185, 129))
        
        draw.rectangle([640, ry+6, 730, ry+28], fill=(238, 242, 255), outline=(99, 102, 241))
        draw.text((646, ry+9), skl[:12], font=get_font(FONT_UI, 9), fill=(79, 70, 229))
        
        draw.rectangle([750, ry+6, 840, ry+28], fill=(241, 245, 249), outline=(148, 163, 184))
        draw.text((756, ry+9), trs[:12], font=get_font(FONT_UI, 9), fill=(51, 65, 85))
        
        draw.rectangle([860, ry+6, 940, ry+28], fill=(30, 58, 95))
        draw.text((870, ry+9), "Kelola Berkas", font=get_font(FONT_UI_BOLD, 9), fill=(255, 255, 255))
        ry += 45
        
    path = os.path.join(OUTPUT_DIR, "proto_admin_arsip.png")
    im.save(path)
    print("Saved:", path)

def make_proto_admin_schedules():
    w, h = 980, 620
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - Pengaturan Jadwal Rilis Kelulusan Otomatis", "Otomasi Sistem")
    draw_web_sidebar(draw, "Jadwal Lulus", is_guru=False)
    
    draw.text((230, 55), "Jadwal Pengumuman & Transisi Kelulusan", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((230, 78), "Sistem otomatis mengeksekusi cron job transisi status Siswa menjadi Alumni secara serentak", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    draw.rectangle([w-230, 55, w-20, 85], fill=(30, 58, 95))
    draw.text((w-210, 62), "+ Tambah Jadwal Angkatan", font=get_font(FONT_UI_BOLD, 10), fill=(255, 255, 255))
    
    draw.rectangle([230, 105, w-20, 165], fill=(238, 242, 255), outline=(199, 210, 254))
    draw.text((245, 116), "⚡ Mekanisme Otomasi Kelulusan Terjadwal", font=get_font(FONT_UI_BOLD, 11), fill=(67, 56, 202))
    draw.text((245, 136), "Ketika tanggal dan jam pengumuman tercapai, Artisan command `salut:promote-alumni` akan otomatis aktif,", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    draw.text((245, 150), "mengubah status siswa angkatan tersebut menjadi alumni, dan memicu push notification Firebase secara massal.", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    
    draw.rectangle([230, 180, w-20, 570], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.rectangle([230, 180, w-20, 215], fill=(241, 245, 249))
    cols = [
        ("Tahun Angkatan", 245),
        ("Tanggal Rilis Resmi", 370),
        ("Jam Pengumuman", 510),
        ("Target Siswa", 640),
        ("Status Eksekusi", 760),
        ("Aksi Kontrol", 880)
    ]
    for cname, cx_col in cols:
        draw.text((cx_col, 190), cname, font=get_font(FONT_UI_BOLD, 10), fill=(71, 85, 105))
        
    schedules = [
        ("Angkatan 2024", "15 Mei 2024", "10:00:00 WIB", "185 Siswa", "Completed", (236, 253, 245), (16, 185, 129)),
        ("Angkatan 2025", "20 Mei 2025", "10:00:00 WIB", "192 Siswa", "Completed", (236, 253, 245), (16, 185, 129)),
        ("Angkatan 2026 (Aktif)", "18 Mei 2026", "10:00:00 WIB", "190 Siswa", "Scheduled", (238, 242, 255), (67, 56, 202)),
        ("Angkatan 2027", "20 Mei 2027", "10:00:00 WIB", "195 Siswa", "Pending", (241, 245, 249), (100, 116, 139)),
    ]
    ry = 225
    for angk, tgl, jam, jml, st, bg_st, fg_st in schedules:
        draw.line([230, ry+42, w-20, ry+42], fill=(241, 245, 249), width=1)
        draw.text((245, ry+12), angk, font=get_font(FONT_UI_BOLD, 11), fill=(15, 23, 42))
        draw.text((370, ry+12), tgl, font=get_font(FONT_UI, 10), fill=(71, 85, 105))
        draw.text((510, ry+12), jam, font=get_font(FONT_CODE, 10), fill=(71, 85, 105))
        draw.text((640, ry+12), jml, font=get_font(FONT_UI_BOLD, 10), fill=(30, 58, 95))
        
        draw.rectangle([760, ry+8, 840, ry+30], fill=bg_st, outline=fg_st)
        draw.text((770, ry+11), st, font=get_font(FONT_UI_BOLD, 9), fill=fg_st)
        
        draw.rectangle([875, ry+8, 940, ry+30], fill=(241, 245, 249), outline=(203, 213, 225))
        draw.text((885, ry+11), "Edit / Uji", font=get_font(FONT_UI, 9), fill=(30, 58, 95))
        ry += 50
        
    path = os.path.join(OUTPUT_DIR, "proto_admin_schedules.png")
    im.save(path)
    print("Saved:", path)

def make_proto_admin_tracer():
    w, h = 980, 620
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - Rekapitulasi & Grafik Analitik Tracer Study", "Data Penyerapan Alumni")
    draw_web_sidebar(draw, "Tracer Study", is_guru=False)
    
    draw.text((230, 55), "Analitik Keterserapan Lulusan (Tracer Study)", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((230, 78), "Monitoring sebaran alumni SMK di dunia usaha & industri (DUDI) serta perguruan tinggi", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    draw.rectangle([230, 105, 570, 320], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((245, 118), "Distribusi Status Keterserapan Alumni", font=get_font(FONT_UI_BOLD, 12), fill=(15, 23, 42))
    draw.line([245, 140, 555, 140], fill=(241, 245, 249), width=1)
    
    draw.ellipse([270, 160, 390, 280], fill=(16, 185, 129))
    draw.pieslice([270, 160, 390, 280], start=234, end=324, fill=(59, 130, 246))
    draw.pieslice([270, 160, 390, 280], start=324, end=360, fill=(245, 158, 11))
    draw.ellipse([305, 195, 355, 245], fill=(255, 255, 255))
    
    legend = [
        ("Bekerja (DUDI)", "65% (124 Alumni)", (16, 185, 129)),
        ("Melanjutkan Kuliah", "25% (48 Alumni)", (59, 130, 246)),
        ("Wirausaha / Mandiri", "10% (18 Alumni)", (245, 158, 11)),
    ]
    ly = 175
    for ltitle, lval, col in legend:
        draw.rectangle([415, ly, 427, ly+12], fill=col)
        draw.text((435, ly), ltitle, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
        draw.text((435, ly+14), lval, font=get_font(FONT_UI, 9), fill=(100, 116, 139))
        ly += 36
        
    draw.rectangle([585, 105, w-20, 320], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((600, 118), "Keselarasan Bidang Kerja dengan Jurusan", font=get_font(FONT_UI_BOLD, 12), fill=(15, 23, 42))
    draw.line([600, 140, w-35, 140], fill=(241, 245, 249), width=1)
    
    bars = [
        ("Sangat Selaras (Sesuai Kompetensi)", 82, (16, 185, 129)),
        ("Cukup Selaras (Bidang IT Terkait)", 12, (59, 130, 246)),
        ("Lintas Bidang (Non-IT)", 6, (148, 163, 184)),
    ]
    by = 160
    for btitle, bpct, bcol in bars:
        draw.text((600, by), f"{btitle} - {bpct}%", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
        draw.rectangle([600, by+18, w-40, by+30], fill=(241, 245, 249))
        draw.rectangle([600, by+18, 600 + int((w - 640) * (bpct / 100)), by+30], fill=bcol)
        by += 44
        
    draw.rectangle([230, 335, w-20, 580], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((245, 348), "Data Terbaru Pengisian Kuesioner Alumni", font=get_font(FONT_UI_BOLD, 12), fill=(15, 23, 42))
    draw.line([245, 370, w-35, 370], fill=(241, 245, 249), width=1)
    
    t_cols = [("Nama Alumni", 245), ("Jurusan", 380), ("Status Lulusan", 520), ("Instansi / Kampus", 660), ("Gaji / Kategori", 820)]
    for cname, cx_col in t_cols:
        draw.text((cx_col, 380), cname, font=get_font(FONT_UI_BOLD, 9), fill=(100, 116, 139))
        
    alumni_feed = [
        ("Siti Rahayu", "RPL", "Bekerja", "PT Telkom Indonesia", "Rp 5.500.000 / bln"),
        ("Rian Hidayat", "TKJ", "Bekerja", "PT Indosat Ooredoo", "Rp 5.000.000 / bln"),
        ("Dian Sastro", "Multimedia", "Melanjutkan Kuliah", "Institut Teknologi Bandung", "S1 Desain Komunikasi"),
        ("Bagus Pratama", "RPL", "Wirausaha", "Creative Software Studio", "Omset Mandiri"),
    ]
    ay = 405
    for anama, ajur, ast, ains, agj in alumni_feed:
        draw.line([245, ay+30, w-35, ay+30], fill=(248, 250, 252), width=1)
        draw.text((245, ay+6), anama, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
        draw.text((380, ay+6), ajur, font=get_font(FONT_UI, 10), fill=(71, 85, 105))
        draw.text((520, ay+6), ast, font=get_font(FONT_UI, 10), fill=(16, 185, 129))
        draw.text((660, ay+6), ains, font=get_font(FONT_UI, 10), fill=(15, 23, 42))
        draw.text((820, ay+6), agj, font=get_font(FONT_CODE, 10), fill=(30, 58, 95))
        ay += 36
        
    path = os.path.join(OUTPUT_DIR, "proto_admin_tracer.png")
    im.save(path)
    print("Saved:", path)

def make_proto_guru_rapor():
    w, h = 980, 620
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - Modul Input Nilai Rapor Siswa", "Role: Guru Pengajar")
    draw_web_sidebar(draw, "Input Rapor", is_guru=True)
    
    draw.text((230, 55), "Penginputan Nilai Rapor Akademik Siswa", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((230, 78), "Pengelolaan nilai per mata pelajaran dan per semester untuk transkrip kelulusan", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    draw.rectangle([230, 105, 380, 135], fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((240, 113), "Kelas: XII RPL 1 ▼", font=get_font(FONT_UI, 10), fill=(15, 23, 42))
    
    draw.rectangle([390, 105, 540, 135], fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((400, 113), "Semester: Semester 5 ▼", font=get_font(FONT_UI, 10), fill=(15, 23, 42))
    
    draw.rectangle([w-220, 105, w-20, 135], fill=(16, 185, 129))
    draw.text((w-180, 112), "💾 Simpan Nilai Massal", font=get_font(FONT_UI_BOLD, 10), fill=(255, 255, 255))
    
    draw.rectangle([230, 150, w-20, 570], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.rectangle([230, 150, w-20, 185], fill=(241, 245, 249))
    
    cols = [
        ("No", 245),
        ("NISN", 280),
        ("Nama Siswa", 380),
        ("Pemrograman Web", 530),
        ("Basis Data", 660),
        ("Pemrograman Mobile", 790),
        ("Rata-rata", 910)
    ]
    for cname, cx_col in cols:
        draw.text((cx_col, 160), cname, font=get_font(FONT_UI_BOLD, 9), fill=(71, 85, 105))
        
    students = [
        ("1", "0051234567", "Budi Santoso", "92", "90", "95", "92.33"),
        ("2", "0051234568", "Ahmad Fauzi", "88", "89", "87", "88.00"),
        ("3", "0051234569", "Dewi Anggraini", "94", "92", "91", "92.33"),
        ("4", "0051234570", "Farhan Pratama", "85", "86", "88", "86.33"),
        ("5", "0051234571", "Nadia Permata", "90", "91", "93", "91.33"),
        ("6", "0051234572", "Yoga Saputra", "87", "85", "86", "86.00"),
        ("7", "0051234573", "Rina Marlina", "95", "96", "94", "95.00"),
    ]
    ry = 195
    for no, nisn, nama, n1, n2, n3, avg in students:
        draw.line([230, ry+38, w-20, ry+38], fill=(241, 245, 249), width=1)
        draw.text((245, ry+10), no, font=get_font(FONT_UI, 10), fill=(100, 116, 139))
        draw.text((280, ry+10), nisn, font=get_font(FONT_CODE, 10), fill=(71, 85, 105))
        draw.text((380, ry+10), nama, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
        
        for nx, nval in [(545, n1), (675, n2), (805, n3)]:
            draw.rectangle([nx, ry+5, nx+45, ry+28], fill=(255, 255, 255), outline=(203, 213, 225))
            draw.text((nx+12, ry+9), nval, font=get_font(FONT_CODE, 10), fill=(15, 23, 42))
            
        draw.text((915, ry+10), avg, font=get_font(FONT_UI_BOLD, 10), fill=(16, 185, 129))
        ry += 45
        
    path = os.path.join(OUTPUT_DIR, "proto_guru_rapor.png")
    im.save(path)
    print("Saved:", path)

def make_proto_guru_skills():
    w, h = 980, 620
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - Portofolio Capaian Keahlian Siswa (SKPI)", "Modul Asesmen Guru")
    draw_web_sidebar(draw, "Portofolio SKPI", is_guru=True)
    
    draw.text((230, 55), "Validasi & Sertifikasi Kompetensi Keahlian (SKPI)", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((230, 78), "Pengesahan unit kompetensi kejuruan SMK berdasarkan standar SKKNI & BNSP", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    draw.rectangle([w-230, 55, w-20, 85], fill=(30, 58, 95))
    draw.text((w-210, 62), "+ Tambah Unit Kompetensi", font=get_font(FONT_UI_BOLD, 10), fill=(255, 255, 255))
    
    draw.rectangle([230, 105, 420, 135], fill=(255, 255, 255), outline=(203, 213, 225))
    draw.text((240, 113), "Jurusan: Rekayasa Perangkat Lunak ▼", font=get_font(FONT_UI, 10), fill=(15, 23, 42))
    
    draw.rectangle([230, 150, w-20, 570], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.rectangle([230, 150, w-20, 185], fill=(241, 245, 249))
    cols = [
        ("Kode Unit", 245),
        ("Judul Unit Kompetensi Kejuruan", 360),
        ("Tingkat Kemahiran", 620),
        ("Siswa Lulus Uji", 760),
        ("Status Asesor", 870)
    ]
    for cname, cx_col in cols:
        draw.text((cx_col, 160), cname, font=get_font(FONT_UI_BOLD, 10), fill=(71, 85, 105))
        
    skills = [
        ("SK-RPL-01", "Pemrograman Web Berbasis Framework (Laravel 12)", "Mahir", "48 Siswa", "Terverifikasi"),
        ("SK-RPL-02", "Mobile Application Development (Flutter & GetX)", "Mahir", "48 Siswa", "Terverifikasi"),
        ("SK-RPL-03", "Relational Database Management (MySQL & Indexing)", "Terampil", "48 Siswa", "Terverifikasi"),
        ("SK-RPL-04", "RESTful API Integration & JWT Security", "Mahir", "45 Siswa", "Terverifikasi"),
        ("SK-TKJ-01", "Konfigurasi Jaringan Routing & Switching Mikrotik", "Mahir", "97 Siswa", "Terverifikasi"),
        ("SK-TKJ-02", "Instalasi dan Administrasi Server Linux Debian", "Terampil", "97 Siswa", "Terverifikasi"),
        ("SK-MM-01", "Desain Grafis Vektor dan Ilustrasi Digital", "Mahir", "45 Siswa", "Terverifikasi"),
    ]
    ry = 195
    for code, title, lvl, jml, st in skills:
        draw.line([230, ry+38, w-20, ry+38], fill=(241, 245, 249), width=1)
        draw.text((245, ry+10), code, font=get_font(FONT_CODE, 10), fill=(30, 58, 95))
        draw.text((360, ry+10), title, font=get_font(FONT_UI_BOLD, 10), fill=(15, 23, 42))
        
        draw.rectangle([620, ry+6, 680, ry+28], fill=(236, 253, 245), outline=(16, 185, 129))
        draw.text((630, ry+9), lvl, font=get_font(FONT_UI_BOLD, 9), fill=(16, 185, 129))
        
        draw.text((760, ry+10), jml, font=get_font(FONT_UI, 10), fill=(71, 85, 105))
        
        draw.rectangle([870, ry+6, 950, ry+28], fill=(238, 242, 255), outline=(99, 102, 241))
        draw.text((880, ry+9), "✅ " + st, font=get_font(FONT_UI_BOLD, 8), fill=(67, 56, 202))
        ry += 45
        
    path = os.path.join(OUTPUT_DIR, "proto_guru_skills.png")
    im.save(path)
    print("Saved:", path)

def make_proto_siswa_prestasi():
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "09:15", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  92%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Prestasi & Penghargaan", font=get_font(FONT_UI_BOLD, 16), fill=(30, 58, 95))
    
    draw.rectangle([20, 95, w-20, 205], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((35, 108), "Form Pengajuan Prestasi Baru", font=get_font(FONT_UI_BOLD, 12), fill=(15, 23, 42))
    draw.text((35, 128), "Nama Lomba: Juara 1 LKS Web Tech", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    draw.text((35, 145), "Tingkat: Provinsi Lampung (Juara 1)", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    draw.text((35, 162), "Tahun: 2026 • Penyelenggara: Dinas Pendidikan", font=get_font(FONT_UI, 10), fill=(71, 85, 105))
    draw.rectangle([35, 180, 150, 198], fill=(236, 253, 245), outline=(16, 185, 129))
    draw.text((42, 182), "Status: Approved ✅", font=get_font(FONT_UI_BOLD, 9), fill=(16, 185, 129))
    
    # Modal Pop-up Dialog
    draw.rectangle([0, 0, w, h], fill=(0, 0, 0, 140)) # Overlay
    draw.rectangle([30, 220, w-30, 560], fill=(255, 255, 255), outline=(226, 232, 240))
    
    draw.ellipse([w//2 - 35, 245, w//2 + 35, 315], fill=(236, 253, 245), outline=(16, 185, 129))
    draw.text((w//2 - 12, 260), "✓", font=get_font(FONT_UI_BOLD, 34), fill=(16, 185, 129))
    
    draw.text((w//2 - 110, 330), "Prestasi Berhasil Dikirim!", font=get_font(FONT_UI_BOLD, 15), fill=(15, 23, 42))
    draw.text((50, 358), "Pengajuan prestasi Anda telah berhasil disimpan", font=get_font(FONT_UI, 11), fill=(71, 85, 105))
    draw.text((45, 375), "ke sistem SALUT dan sedang menunggu verifikasi Guru.", font=get_font(FONT_UI, 11), fill=(71, 85, 105))
    
    draw.rectangle([50, 405, w-50, 480], fill=(248, 250, 252), outline=(226, 232, 240))
    draw.text((65, 415), "Rincian Kegiatan:", font=get_font(FONT_UI_BOLD, 10), fill=(100, 116, 139))
    draw.text((65, 432), "LKS Tingkat Provinsi Bidang Web Technologies", font=get_font(FONT_UI_BOLD, 11), fill=(30, 58, 95))
    draw.text((65, 452), "Lampiran Sertifikat: Berhasil Diunggah (PDF)", font=get_font(FONT_UI, 10), fill=(16, 185, 129))
    
    draw.rectangle([50, 498, w-50, 540], fill=(30, 58, 95))
    draw.text((w//2 - 60, 510), "Lihat di Beranda", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "proto_siswa_prestasi.png")
    im.save(path)
    print("Saved:", path)

if __name__ == "__main__":
    make_proto_admin_students()
    make_proto_admin_arsip()
    make_proto_admin_schedules()
    make_proto_admin_tracer()
    make_proto_guru_rapor()
    make_proto_guru_skills()
    make_proto_siswa_prestasi()
    print("Semua gambar prototype selesai di-generate!")
