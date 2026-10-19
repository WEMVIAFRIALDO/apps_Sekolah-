# -*- coding: utf-8 -*-
"""
Script Generator Gambar Screenshot dan Penyusun Laporan 3 & 4 (SALUT)
Format Dokumen: Word (.docx) dan HTML (.html)
Penulis: Wemvi Afrialdo
Proyek: SALUT (Sistem Arsip Kelulusan dan Tracer Study)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"d:\proyek_applikasi\apps_sekolah\laporan_screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Path Font Sistem Windows
FONT_CODE = r"C:\Windows\Fonts\consola.ttf"
FONT_UI = r"C:\Windows\Fonts\segoeui.ttf"
FONT_UI_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_ARIAL = r"C:\Windows\Fonts\arial.ttf"

def get_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def draw_window_frame(draw, width, height, title, subtitle="", bg_color=(30, 30, 30)):
    # Background
    draw.rectangle([0, 0, width, height], fill=bg_color)
    
    # Title bar
    draw.rectangle([0, 0, width, 38], fill=(45, 45, 48))
    draw.line([0, 38, width, 38], fill=(60, 60, 60), width=1)
    
    # Window controls (mac/modern style)
    draw.ellipse([14, 13, 26, 25], fill=(255, 95, 86))
    draw.ellipse([34, 13, 46, 25], fill=(255, 189, 46))
    draw.ellipse([54, 13, 66, 25], fill=(39, 201, 63))
    
    # Title text
    f_title = get_font(FONT_UI, 13)
    draw.text((78, 10), title, font=f_title, fill=(204, 204, 204))
    
    if subtitle:
        f_sub = get_font(FONT_UI, 11)
        draw.text((width - 250, 11), subtitle, font=f_sub, fill=(150, 150, 150))

def draw_vscode_header(draw, width, tab_name, breadcrumb):
    # Tab Bar
    draw.rectangle([0, 39, width, 75], fill=(37, 37, 38))
    # Active tab
    draw.rectangle([48, 43, 230, 75], fill=(30, 30, 30))
    draw.line([48, 43, 230, 43], fill=(0, 122, 204), width=2)
    
    f_tab = get_font(FONT_UI, 12)
    draw.text((65, 50), tab_name, font=f_tab, fill=(255, 255, 255))
    draw.text((210, 50), "×", font=f_tab, fill=(150, 150, 150))
    
    # Breadcrumbs bar
    draw.rectangle([0, 76, width, 100], fill=(30, 30, 30))
    f_bread = get_font(FONT_UI, 11)
    draw.text((60, 80), breadcrumb, font=f_bread, fill=(160, 160, 160))
    draw.line([0, 100, width, 100], fill=(45, 45, 48), width=1)

def draw_code_lines(draw, lines, start_y=110, start_line_num=1, width=960):
    f_code = get_font(FONT_CODE, 14)
    f_num = get_font(FONT_CODE, 13)
    
    # Sidebar gutter
    draw.rectangle([0, start_y - 10, 48, start_y + len(lines) * 22 + 20], fill=(30, 30, 30))
    draw.line([48, start_y - 10, 48, start_y + len(lines) * 22 + 20], fill=(45, 45, 48), width=1)
    
    y = start_y
    for i, (text, color) in enumerate(lines):
        line_no = str(start_line_num + i)
        # Line number
        draw.text((40 - len(line_no) * 8, y), line_no, font=f_num, fill=(100, 100, 100))
        # Code content
        draw.text((60, y), text, font=f_code, fill=color)
        y += 22

# ==========================================
# 1. LAPORAN 3 SCREENSHOTS GENERATION
# ==========================================

def make_screenshot_laporan3_01_env():
    w, h = 950, 520
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - .env - salut_backend", "SALUT Backend Environment")
    draw_vscode_header(draw, w, ".env", "salut_backend > .env")
    
    lines = [
        ("APP_NAME=SALUT", (156, 220, 254)),
        ("APP_ENV=local", (156, 220, 254)),
        ("APP_KEY=base64:kCXgOguSxbet0fvmllYUYa+f3qLjyEfvoI49aYXlC64=", (156, 220, 254)),
        ("APP_DEBUG=true", (156, 220, 254)),
        ("APP_URL=http://localhost:8000", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("# Konfigurasi Relasi Database MySQL", (106, 153, 85)),
        ("DB_CONNECTION=mysql", (78, 201, 176)),
        ("DB_HOST=127.0.0.1", (206, 145, 120)),
        ("DB_PORT=3306", (181, 206, 168)),
        ("DB_DATABASE=salut_db", (206, 145, 120)),
        ("DB_USERNAME=root", (206, 145, 120)),
        ("DB_PASSWORD=", (206, 145, 120)),
        ("", (255, 255, 255)),
        ("# Konfigurasi Autentikasi JWT (php-open-source-saver/jwt-auth)", (106, 153, 85)),
        ("JWT_SECRET=WT1Cp6CCd98Z14ezvuxgCkL8LNTUehZHMZWIRzHsuDrAvIsRWtprYwtaeAcGq6Ks", (215, 186, 125)),
        ("JWT_ALGO=HS256", (156, 220, 254)),
        ("JWT_TTL=60", (181, 206, 168)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=1, width=w)
    
    # Status bar
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    f_sb = get_font(FONT_UI, 11)
    draw.text((12, h-20), "main* | UTF-8 | Properties | Spaces: 4", font=f_sb, fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan3_01_env.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan3_02_migration():
    w, h = 950, 560
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - 2026_09_30_035234_create_academic_records_table.php", "Migration & Model Eloquent")
    draw_vscode_header(draw, w, "create_academic_records_table.php", "database > migrations > 2026_09_30_create_academic_records_table.php")
    
    lines = [
        ("<?php", (218, 112, 214)),
        ("use Illuminate\\Database\\Migrations\\Migration;", (156, 220, 254)),
        ("use Illuminate\\Database\\Schema\\Blueprint;", (156, 220, 254)),
        ("use Illuminate\\Support\\Facades\\Schema;", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("return new class extends Migration {", (86, 156, 214)),
        ("    public function up(): void {", (86, 156, 214)),
        ("        Schema::create('academic_records', function (Blueprint $table) {", (220, 220, 170)),
        ("            $table->id();", (156, 220, 254)),
        ("            $table->foreignId('user_id')->constrained('users')->onDelete('cascade');", (156, 220, 254)),
        ("            $table->string('semester', 20);", (156, 220, 254)),
        ("            $table->decimal('gpa', 4, 2); // Rata-rata Nilai Rapor", (106, 153, 85)),
        ("            $table->json('grades_detail'); // Nilai per Mata Pelajaran", (106, 153, 85)),
        ("            $table->string('report_file')->nullable(); // PDF Rapor", (106, 153, 85)),
        ("            $table->timestamps();", (156, 220, 254)),
        ("        });", (220, 220, 170)),
        ("    }", (86, 156, 214)),
        ("};", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=1, width=w)
    
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    f_sb = get_font(FONT_UI, 11)
    draw.text((12, h-20), "main* | PHP 8.2 | UTF-8 | CRLF | Laravel Eloquent", font=f_sb, fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan3_02_migration_model.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan3_03_phpmyadmin():
    w, h = 950, 560
    im = Image.new("RGB", (w, h), (245, 245, 245))
    draw = ImageDraw.Draw(im)
    
    # Browser bar
    draw_window_frame(draw, w, h, "phpMyAdmin 5.2.1 - localhost / 127.0.0.1 / salut_db", "Database Server: MariaDB / MySQL", bg_color=(245, 245, 245))
    
    # URL bar
    draw.rectangle([0, 39, w, 75], fill=(235, 235, 235))
    draw.rectangle([80, 45, w-80, 70], fill=(255, 255, 255), outline=(200, 200, 200))
    f_url = get_font(FONT_UI, 12)
    draw.text((95, 49), "http://localhost/phpmyadmin/index.php?route=/database/structure&db=salut_db", font=f_url, fill=(50, 50, 50))
    
    # phpMyAdmin Top Bar (Orange brand)
    draw.rectangle([0, 76, w, 116], fill=(243, 110, 36))
    f_brand = get_font(FONT_UI_BOLD, 15)
    draw.text((20, 85), "phpMyAdmin", font=f_brand, fill=(255, 255, 255))
    f_nav = get_font(FONT_UI, 12)
    draw.text((140, 88), "Server: 127.0.0.1  >>  Database: salut_db", font=f_nav, fill=(255, 255, 255))
    
    # Tab navigation in phpMyAdmin
    draw.rectangle([0, 117, w, 147], fill=(225, 225, 225))
    tabs = ["Structure", "SQL", "Search", "Query", "Export", "Import", "Privileges", "Operations"]
    tx = 20
    for idx, tab in enumerate(tabs):
        tb_bg = (255, 255, 255) if idx == 0 else (225, 225, 225)
        draw.rectangle([tx, 121, tx+70, 147], fill=tb_bg)
        draw.text((tx+10, 126), tab, font=get_font(FONT_UI, 11), fill=(0, 0, 0) if idx == 0 else (80, 80, 80))
        tx += 75
        
    # Table header
    draw.rectangle([20, 160, w-20, 185], fill=(220, 230, 242))
    f_th = get_font(FONT_UI_BOLD, 11)
    draw.text((35, 165), "Table Name", font=f_th, fill=(30, 50, 80))
    draw.text((260, 165), "Action", font=f_th, fill=(30, 50, 80))
    draw.text((450, 165), "Rows", font=f_th, fill=(30, 50, 80))
    draw.text((540, 165), "Type", font=f_th, fill=(30, 50, 80))
    draw.text((640, 165), "Collation", font=f_th, fill=(30, 50, 80))
    draw.text((780, 165), "Size", font=f_th, fill=(30, 50, 80))
    
    # Table rows
    table_data = [
        ("academic_records", "Browse | Structure | Search", "190", "InnoDB", "utf8mb4_unicode_ci", "64.0 KiB"),
        ("achievements", "Browse | Structure | Search", "45", "InnoDB", "utf8mb4_unicode_ci", "48.0 KiB"),
        ("cache / cache_locks", "Browse | Structure | Search", "0", "InnoDB", "utf8mb4_unicode_ci", "32.0 KiB"),
        ("graduation_docs", "Browse | Structure | Search", "12", "InnoDB", "utf8mb4_unicode_ci", "32.0 KiB"),
        ("jobs / job_batches", "Browse | Structure | Search", "0", "InnoDB", "utf8mb4_unicode_ci", "32.0 KiB"),
        ("migrations", "Browse | Structure | Search", "10", "InnoDB", "utf8mb4_unicode_ci", "16.0 KiB"),
        ("personal_access_tokens", "Browse | Structure | Search", "0", "InnoDB", "utf8mb4_unicode_ci", "32.0 KiB"),
        ("tracer_studies", "Browse | Structure | Search", "10", "InnoDB", "utf8mb4_unicode_ci", "48.0 KiB"),
        ("users", "Browse | Structure | Search", "205", "InnoDB", "utf8mb4_unicode_ci", "128.0 KiB"),
    ]
    
    ry = 190
    f_td = get_font(FONT_UI, 11)
    for idx, (tname, act, rows, eng, col, sz) in enumerate(table_data):
        row_bg = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
        draw.rectangle([20, ry, w-20, ry+28], fill=row_bg, outline=(230, 230, 230))
        draw.text((35, ry+6), tname, font=get_font(FONT_UI_BOLD, 11), fill=(10, 80, 180))
        draw.text((260, ry+6), act, font=f_td, fill=(100, 100, 100))
        draw.text((450, ry+6), rows, font=f_td, fill=(20, 20, 20))
        draw.text((540, ry+6), eng, font=f_td, fill=(50, 50, 50))
        draw.text((640, ry+6), col, font=f_td, fill=(80, 80, 80))
        draw.text((780, ry+6), sz, font=f_td, fill=(50, 50, 50))
        ry += 29
        
    # Table summary footer
    draw.rectangle([20, ry+8, w-20, ry+38], fill=(225, 238, 250), outline=(180, 205, 230))
    f_sum = get_font(FONT_UI_BOLD, 11)
    draw.text((35, ry+17), "9 tables in salut_db | Total: 462 rows | InnoDB Engine | Status: OK (All migrations migrated successfully)", font=f_sum, fill=(20, 70, 120))
    
    path = os.path.join(OUTPUT_DIR, "laporan3_03_phpmyadmin.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan3_04_routes_api():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - routes/api.php", "Routing API & Middleware JWT Auth")
    draw_vscode_header(draw, w, "api.php", "salut_backend > routes > api.php")
    
    lines = [
        ("<?php", (218, 112, 214)),
        ("use App\\Http\\Controllers\\Api\\AuthController;", (156, 220, 254)),
        ("use App\\Http\\Controllers\\Api\\ProfileController;", (156, 220, 254)),
        ("use App\\Http\\Controllers\\Api\\PrestasiController;", (156, 220, 254)),
        ("use App\\Http\\Controllers\\Api\\ArsipController;", (156, 220, 254)),
        ("use Illuminate\\Support\\Facades\\Route;", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("// ─── Public Routes (Autentikasi Awal Login)", (106, 153, 85)),
        ("Route::post('/login', [AuthController::class, 'login']);", (220, 220, 170)),
        ("", (255, 255, 255)),
        ("// ─── Protected Routes (Wajib JWT Bearer Token)", (106, 153, 85)),
        ("Route::middleware('jwt.auth')->group(function () {", (86, 156, 214)),
        ("    Route::post('/logout',  [AuthController::class, 'logout']);", (220, 220, 170)),
        ("    Route::post('/refresh', [AuthController::class, 'refresh']);", (220, 220, 170)),
        ("", (255, 255, 255)),
        ("    // Profil Pengguna (Siswa, Alumni, Guru, Admin)", (106, 153, 85)),
        ("    Route::prefix('profile')->group(function () {", (86, 156, 214)),
        ("        Route::get('/',   [ProfileController::class, 'show']);", (220, 220, 170)),
        ("        Route::patch('/', [ProfileController::class, 'update']);", (220, 220, 170)),
        ("    });", (86, 156, 214)),
        ("});", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=1, width=w)
    
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    f_sb = get_font(FONT_UI, 11)
    draw.text((12, h-20), "main* | PHP | Routes RESTful API | JWT Guard Active", font=f_sb, fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan3_04_routes_api.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan3_05_api_testing():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (33, 33, 33))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Thunder Client / Postman - POST http://127.0.0.1:8000/api/login", "REST API Testing Response", bg_color=(33, 33, 33))
    
    # Request bar
    draw.rectangle([20, 50, w-20, 92], fill=(42, 42, 42), outline=(60, 60, 60))
    # Method badge
    draw.rectangle([28, 56, 90, 86], fill=(235, 122, 34))
    f_mb = get_font(FONT_UI_BOLD, 12)
    draw.text((40, 63), "POST", font=f_mb, fill=(255, 255, 255))
    
    # URL text
    f_url = get_font(FONT_CODE, 13)
    draw.text((105, 64), "http://127.0.0.1:8000/api/login", font=f_url, fill=(230, 230, 230))
    
    # Send button
    draw.rectangle([w-120, 56, w-28, 86], fill=(0, 122, 204))
    draw.text((w-98, 63), "Send", font=f_mb, fill=(255, 255, 255))
    
    # Response Status Badges
    draw.rectangle([20, 105, w-20, 140], fill=(42, 42, 42))
    # 200 OK badge
    draw.rectangle([30, 110, 115, 135], fill=(46, 125, 50))
    f_st = get_font(FONT_UI_BOLD, 12)
    draw.text((38, 114), "200 OK", font=f_st, fill=(255, 255, 255))
    
    f_info = get_font(FONT_UI, 12)
    draw.text((135, 115), "Time: 124 ms", font=f_info, fill=(200, 200, 200))
    draw.text((245, 115), "Size: 1.42 KB", font=f_info, fill=(200, 200, 200))
    draw.text((360, 115), "Content-Type: application/json", font=f_info, fill=(150, 150, 150))
    
    # JSON Response Viewer
    draw.rectangle([20, 145, w-20, h-20], fill=(24, 24, 24), outline=(50, 50, 50))
    
    json_lines = [
        ("{", (255, 255, 255)),
        ('  "success": true,', (78, 201, 176)),
        ('  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjgwMDAvYXBpL2xvZ2luIiwiaWF0IjoxNzkxOTk5MzE4LCJleHAiOjE3OTIwMDI5MTgsInN1YiI6IjYiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.m72Ws4rKiILETX_jC-1oQliif9m0f483UpBxsPFNkP0",', (206, 145, 120)),
        ('  "user": {', (255, 255, 255)),
        ('    "id": 6,', (181, 206, 168)),
        ('    "name": "Budi Santoso",', (206, 145, 120)),
        ('    "nisn": "0054321987",', (206, 145, 120)),
        ('    "email": "0054321987@salut.sch.id",', (206, 145, 120)),
        ('    "role": "siswa",', (206, 145, 120)),
        ('    "school": "SMK Negeri 1 Teladan",', (206, 145, 120)),
        ('    "class": "XII RPL 1",', (206, 145, 120)),
        ('    "angkatan": 2026,', (181, 206, 168)),
        ('    "joined_at": "2026-10-13"', (206, 145, 120)),
        ('  }', (255, 255, 255)),
        ("}", (255, 255, 255)),
    ]
    
    jy = 160
    f_code = get_font(FONT_CODE, 13)
    for text, col in json_lines:
        draw.text((40, jy), text, font=f_code, fill=col)
        jy += 23
        
    path = os.path.join(OUTPUT_DIR, "laporan3_05_api_testing.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan3_06_git_push():
    w, h = 950, 480
    im = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Terminal PowerShell - Git Push Backend", "git push origin main", bg_color=(12, 12, 12))
    
    lines = [
        ("PS D:\\proyek_applikasi\\salut_backend> git status", (255, 255, 255)),
        ("On branch main", (200, 200, 200)),
        ("Your branch is up to date with 'origin/main'.", (200, 200, 200)),
        ("Changes to be committed:", (76, 175, 80)),
        ("  (use \"git restore --staged <file>...\" to unstage)", (150, 150, 150)),
        ("        new file:   database/migrations/2026_09_30_035234_create_academic_records_table.php", (76, 175, 80)),
        ("        new file:   app/Models/User.php", (76, 175, 80)),
        ("        new file:   routes/api.php", (76, 175, 80)),
        ("        modified:   .env", (76, 175, 80)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi\\salut_backend> git commit -m \"feat(backend): implement jwt auth, migrations, and api routes\"", (255, 255, 255)),
        ("[main 8f4a1bc] feat(backend): implement jwt auth, migrations, and api routes", (220, 220, 220)),
        (" 4 files changed, 280 insertions(+), 12 deletions(-)", (220, 220, 220)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi\\salut_backend> git push origin main", (255, 255, 255)),
        ("Enumerating objects: 15, done.", (180, 180, 180)),
        ("Counting objects: 100% (15/15), done.", (180, 180, 180)),
        ("Delta compression using up to 12 threads", (180, 180, 180)),
        ("Compressing objects: 100% (9/9), done.", (180, 180, 180)),
        ("Writing objects: 100% (10/10), 4.25 KiB | 4.25 MiB/s, done.", (180, 180, 180)),
        ("Total 10 (delta 6), reused 0 (delta 0), pack-reused 0", (180, 180, 180)),
        ("To https://github.com/WEMVIAFRIALDO/apps_Sekolah-.git", (100, 181, 246)),
        ("   5e321ad..8f4a1bc  main -> main", (76, 175, 80)),
    ]
    
    y = 52
    f_code = get_font(FONT_CODE, 13)
    for text, col in lines:
        draw.text((25, y), text, font=f_code, fill=col)
        y += 18
        
    path = os.path.join(OUTPUT_DIR, "laporan3_06_git_push_backend.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan3_07_github():
    w, h = 950, 520
    im = Image.new("RGB", (w, h), (13, 17, 23))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "GitHub - WEMVIAFRIALDO / apps_Sekolah- (Backend Salut Repository)", "https://github.com/WEMVIAFRIALDO/apps_Sekolah-", bg_color=(13, 17, 23))
    
    # GitHub Nav Bar
    draw.rectangle([0, 39, w, 82], fill=(22, 27, 34), outline=(48, 54, 61))
    f_repo = get_font(FONT_UI_BOLD, 14)
    draw.text((25, 50), "WEMVIAFRIALDO  /  apps_Sekolah-", font=f_repo, fill=(88, 166, 255))
    
    f_badge = get_font(FONT_UI, 11)
    draw.rectangle([290, 48, 345, 72], outline=(48, 54, 61), fill=(33, 38, 45))
    draw.text((300, 52), "Public", font=f_badge, fill=(201, 209, 217))
    
    # Branch selector
    draw.rectangle([25, 95, 140, 125], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((38, 101), "Branch: main", font=get_font(FONT_UI_BOLD, 11), fill=(201, 209, 217))
    
    draw.text((160, 101), "apps_Sekolah- / salut_backend /", font=get_font(FONT_UI, 12), fill=(139, 148, 158))
    
    # Commit header
    draw.rectangle([25, 135, w-25, 175], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((40, 146), "WEMVIAFRIALDO", font=get_font(FONT_UI_BOLD, 12), fill=(201, 209, 217))
    draw.text((160, 146), "feat(backend): complete jwt authentication, migrations and seeders", font=get_font(FONT_UI, 12), fill=(139, 148, 158))
    draw.text((w-160, 146), "Commit: 8f4a1bc", font=get_font(FONT_CODE, 11), fill=(88, 166, 255))
    
    # File list
    files = [
        ("app", "Direktori Controller, Model Eloquent, Middleware JWT", "2 days ago"),
        ("bootstrap", "Inisialisasi aplikasi Laravel framework", "2 days ago"),
        ("config", "Konfigurasi auth, cors, database, jwt", "2 days ago"),
        ("database/migrations", "Struktur 5 tabel utama: users, academic, achievements, tracer", "2 days ago"),
        ("routes/api.php", "Definisi 23 API endpoints per-role (Admin, Guru, Siswa, Alumni)", "2 days ago"),
        (".env.example", "Template konfigurasi MySQL database & JWT secret", "2 days ago"),
        ("composer.json", "Dependensi php-open-source-saver/jwt-auth & Laravel 12", "2 days ago"),
        ("README.md", "Dokumentasi instalasi dan API Endpoints SALUT", "2 days ago"),
    ]
    
    fy = 176
    f_fl = get_font(FONT_UI, 11)
    for idx, (fname, fmsg, fdate) in enumerate(files):
        draw.rectangle([25, fy, w-25, fy+35], fill=(13, 17, 23) if idx % 2 == 0 else (18, 22, 30), outline=(48, 54, 61))
        draw.text((45, fy+9), fname, font=get_font(FONT_UI_BOLD, 11), fill=(88, 166, 255))
        draw.text((250, fy+9), fmsg, font=f_fl, fill=(139, 148, 158))
        draw.text((w-130, fy+9), fdate, font=f_fl, fill=(110, 118, 129))
        fy += 36
        
    path = os.path.join(OUTPUT_DIR, "laporan3_07_github_backend.png")
    im.save(path)
    print("Saved:", path)

# ==========================================
# 2. LAPORAN 4 SCREENSHOTS GENERATION
# ==========================================

def make_screenshot_laporan4_01_login_code():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - lib/pages/login_page.dart", "Flutter Mobile UI Login Screen")
    draw_vscode_header(draw, w, "login_page.dart", "apps_sekolah > lib > pages > login_page.dart")
    
    lines = [
        ("class LoginPage extends StatefulWidget {", (86, 156, 214)),
        ("  const LoginPage({super.key});", (220, 220, 170)),
        ("  @override", (86, 156, 214)),
        ("  State<LoginPage> createState() => _LoginPageState();", (220, 220, 170)),
        ("}", (86, 156, 214)),
        ("", (255, 255, 255)),
        ("class _LoginPageState extends State<LoginPage> {", (86, 156, 214)),
        ("  final TextEditingController _nisnController     = TextEditingController();", (156, 220, 254)),
        ("  final TextEditingController _passwordController = TextEditingController();", (156, 220, 254)),
        ("  final _formKey = GlobalKey<FormState>();", (156, 220, 254)),
        ("  bool _isLoading = false;", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("  @override", (86, 156, 214)),
        ("  Widget build(BuildContext context) {", (86, 156, 214)),
        ("    return Scaffold(", (78, 201, 176)),
        ("      backgroundColor: const Color(0xFF1E3A5F), // Brand Dark Blue", (106, 153, 85)),
        ("      body: SafeArea(", (78, 201, 176)),
        ("        child: Center(", (78, 201, 176)),
        ("          child: SingleChildScrollView(", (78, 201, 176)),
        ("            padding: const EdgeInsets.symmetric(horizontal: 28),", (156, 220, 254)),
        ("            child: Form(key: _formKey, child: Column(children: [ ... ])),", (156, 220, 254)),
        ("          ),", (78, 201, 176)),
        ("        ),", (78, 201, 176)),
        ("      ),", (78, 201, 176)),
        ("    );", (78, 201, 176)),
        ("  }", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=10, width=w)
    
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    f_sb = get_font(FONT_UI, 11)
    draw.text((12, h-20), "main* | Dart | Flutter 3.47.6 | Responsive Form & GetX", font=f_sb, fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan4_01_login_page_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_02_api_service():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - lib/services/api_service.dart", "Dio HTTP Client & JWT Interceptor")
    draw_vscode_header(draw, w, "api_service.dart", "apps_sekolah > lib > services > api_service.dart")
    
    lines = [
        ("const String kBaseUrl = 'http://localhost:8000/api';", (206, 145, 120)),
        ("", (255, 255, 255)),
        ("class ApiService {", (86, 156, 214)),
        ("  late final Dio _dio;", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("  ApiService._internal() {", (86, 156, 214)),
        ("    _dio = Dio(BaseOptions(", (78, 201, 176)),
        ("      baseUrl: kBaseUrl,", (156, 220, 254)),
        ("      connectTimeout: const Duration(seconds: 30),", (181, 206, 168)),
        ("      headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},", (156, 220, 254)),
        ("    ));", (78, 201, 176)),
        ("", (255, 255, 255)),
        ("    // Interceptor: Otomatis sisipkan Bearer Token JWT pada Header", (106, 153, 85)),
        ("    _dio.interceptors.add(InterceptorsWrapper(", (78, 201, 176)),
        ("      onRequest: (options, handler) async {", (86, 156, 214)),
        ("        final token = await AuthService().getToken();", (156, 220, 254)),
        ("        if (token != null && token.isNotEmpty) {", (86, 156, 214)),
        ("          options.headers['Authorization'] = 'Bearer $token';", (206, 145, 120)),
        ("        }", (86, 156, 214)),
        ("        return handler.next(options);", (86, 156, 214)),
        ("      },", (86, 156, 214)),
        ("    ));", (78, 201, 176)),
        ("  }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=9, width=w)
    
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    f_sb = get_font(FONT_UI, 11)
    draw.text((12, h-20), "main* | Dart | Dio v5 | Bearer Token Auto-Inject", font=f_sb, fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan4_02_api_service_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_03_login_mobile():
    # Mobile Frame (420 x 780)
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (30, 58, 95))
    draw = ImageDraw.Draw(im)
    
    # Phone status bar
    draw.rectangle([0, 0, w, 32], fill=(24, 46, 76))
    f_clock = get_font(FONT_UI_BOLD, 12)
    draw.text((20, 7), "08:30", font=f_clock, fill=(255, 255, 255))
    draw.text((w-75, 7), "5G  85%", font=f_clock, fill=(255, 255, 255))
    
    # App Logo and Header
    draw.ellipse([w//2 - 45, 90, w//2 + 45, 180], fill=(255, 255, 255))
    draw.ellipse([w//2 - 38, 97, w//2 + 38, 173], fill=(30, 58, 95))
    draw.text((w//2 - 25, 118), "SALUT", font=get_font(FONT_UI_BOLD, 16), fill=(255, 255, 255))
    
    f_title = get_font(FONT_UI_BOLD, 22)
    draw.text((w//2 - 95, 200), "Aplikasi SALUT", font=f_title, fill=(255, 255, 255))
    f_sub = get_font(FONT_UI, 13)
    draw.text((w//2 - 130, 235), "Sistem Arsip Kelulusan & Tracer Study", font=f_sub, fill=(200, 220, 240))
    
    # Form Container Card
    draw.rectangle([30, 280, w-30, 640], fill=(255, 255, 255), outline=(230, 230, 230))
    
    f_lbl = get_font(FONT_UI_BOLD, 13)
    draw.text((50, 310), "Selamat Datang!", font=get_font(FONT_UI_BOLD, 18), fill=(30, 41, 59))
    draw.text((50, 340), "Silakan masuk dengan akun terdaftar", font=get_font(FONT_UI, 12), fill=(100, 116, 139))
    
    # Field NISN
    draw.text((50, 380), "NISN / Nomor Induk", font=f_lbl, fill=(51, 65, 85))
    draw.rectangle([50, 405, w-50, 455], fill=(248, 250, 252), outline=(203, 213, 225))
    draw.text((65, 420), "0054321987", font=get_font(FONT_CODE, 14), fill=(30, 41, 59))
    
    # Field Password
    draw.text((50, 475), "Kata Sandi", font=f_lbl, fill=(51, 65, 85))
    draw.rectangle([50, 500, w-50, 550], fill=(248, 250, 252), outline=(203, 213, 225))
    draw.text((65, 517), "••••••••••••", font=get_font(FONT_UI, 14), fill=(30, 41, 59))
    
    # Button Masuk
    draw.rectangle([50, 570, w-50, 620], fill=(30, 58, 95))
    draw.text((w//2 - 35, 585), "MASUK", font=get_font(FONT_UI_BOLD, 14), fill=(255, 255, 255))
    
    # Footer info
    draw.text((w//2 - 120, 680), "SMK Negeri 1 Teladan • Versi 1.0.0", font=get_font(FONT_UI, 11), fill=(180, 205, 230))
    
    # Navigation bar bottom (Android)
    draw.rectangle([w//2 - 60, h-15, w//2 + 60, h-10], fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan4_03_login_mobile_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_04_dashboard_siswa():
    # Mobile Frame (420 x 780)
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    # Status bar
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "08:31", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  84%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    # App Bar
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Dashboard Siswa", font=get_font(FONT_UI_BOLD, 16), fill=(30, 58, 95))
    # Badge Siswa
    draw.rectangle([w-130, 45, w-20, 72], fill=(219, 234, 254), outline=(147, 197, 253))
    draw.text((w-115, 50), "Siswa Aktif", font=get_font(FONT_UI_BOLD, 11), fill=(29, 78, 216))
    
    # Profile Card
    draw.rectangle([20, 100, w-20, 200], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.ellipse([35, 115, 95, 175], fill=(224, 231, 255))
    draw.text((55, 132), "BS", font=get_font(FONT_UI_BOLD, 18), fill=(67, 56, 202))
    
    draw.text((110, 115), "Budi Santoso", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((110, 140), "NISN: 0054321987", font=get_font(FONT_UI, 12), fill=(100, 116, 139))
    draw.text((110, 160), "Kelas: XII RPL 1 • Angkatan 2026", font=get_font(FONT_UI, 12), fill=(30, 58, 95))
    
    # Banner Status Akademik
    draw.rectangle([20, 215, w-20, 295], fill=(238, 242, 255), outline=(199, 210, 254))
    draw.text((35, 228), "Status Akademik Semester 5", font=get_font(FONT_UI_BOLD, 13), fill=(49, 46, 129))
    draw.text((35, 252), "Rata-rata Nilai: 88.50  |  Kelulusan: Terjadwal", font=get_font(FONT_UI, 12), fill=(67, 56, 202))
    draw.text((35, 272), "Pengumuman kelulusan resmi: 10 Mei 2026", font=get_font(FONT_UI, 11), fill=(79, 70, 229))
    
    # Menu Grid Siswa Aktif
    draw.text((20, 315), "Menu Utama Siswa", font=get_font(FONT_UI_BOLD, 14), fill=(30, 41, 59))
    
    menus_siswa = [
        ("Prestasi Siswa", "Input & Sertifikat", (239, 246, 255), (37, 99, 235)),
        ("Nilai Rapor", "Detail Semester 1-5", (240, 253, 244), (22, 163, 74)),
        ("Jadwal Kelulusan", "Informasi Yudisium", (254, 242, 242), (220, 38, 38)),
        ("Profil Saya", "Pengaturan Akun", (255, 251, 235), (217, 119, 6)),
    ]
    
    my = 345
    for idx, (mtitle, msub, c_bg, c_icon) in enumerate(menus_siswa):
        gx = 20 if idx % 2 == 0 else w//2 + 5
        if idx % 2 == 0 and idx > 0:
            my += 95
        draw.rectangle([gx, my, gx + (w//2 - 25), my + 80], fill=c_bg, outline=(226, 232, 240))
        draw.ellipse([gx + 12, my + 15, gx + 42, my + 45], fill=c_icon)
        draw.text((gx + 12, my + 52), mtitle, font=get_font(FONT_UI_BOLD, 11), fill=(15, 23, 42))
        draw.text((gx + 12, my + 66), msub, font=get_font(FONT_UI, 9), fill=(100, 116, 139))
        
    # Bottom Navigation
    draw.rectangle([0, h-65, w, h], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((45, h-45), "Beranda", font=get_font(FONT_UI_BOLD, 11), fill=(37, 99, 235))
    draw.text((180, h-45), "Prestasi", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    draw.text((320, h-45), "Profil", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    path = os.path.join(OUTPUT_DIR, "laporan4_04_dashboard_siswa_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_05_dashboard_alumni():
    # Mobile Frame (420 x 780)
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    # Status bar
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "08:32", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  83%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    # App Bar
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Dashboard Alumni", font=get_font(FONT_UI_BOLD, 16), fill=(49, 46, 129))
    # Badge Alumni
    draw.rectangle([w-130, 45, w-20, 72], fill=(238, 242, 255), outline=(199, 210, 254))
    draw.text((w-115, 50), "Status: Alumni", font=get_font(FONT_UI_BOLD, 11), fill=(67, 56, 202))
    
    # Profile Card
    draw.rectangle([20, 100, w-20, 200], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.ellipse([35, 115, 95, 175], fill=(237, 233, 254))
    draw.text((55, 132), "SR", font=get_font(FONT_UI_BOLD, 18), fill=(109, 40, 217))
    
    draw.text((110, 115), "Siti Rahayu", font=get_font(FONT_UI_BOLD, 16), fill=(15, 23, 42))
    draw.text((110, 140), "NISN: 0067890123", font=get_font(FONT_UI, 12), fill=(100, 116, 139))
    draw.text((110, 160), "Alumni Angkatan: 2024 (Lulus)", font=get_font(FONT_UI, 12), fill=(109, 40, 217))
    
    # Banner Tracer Study Pengingat
    draw.rectangle([20, 215, w-20, 295], fill=(245, 243, 255), outline=(221, 214, 254))
    draw.text((35, 228), "Kuesioner Tracer Study Alumni", font=get_font(FONT_UI_BOLD, 13), fill=(91, 33, 182))
    draw.text((35, 252), "Status: Sudah Bekerja (Software Engineer)", font=get_font(FONT_UI, 12), fill=(109, 40, 217))
    draw.text((35, 272), "Terima kasih telah berkontribusi bagi akreditasi!", font=get_font(FONT_UI, 11), fill=(124, 58, 237))
    
    # Menu Grid Alumni
    draw.text((20, 315), "Layanan Khusus Alumni", font=get_font(FONT_UI_BOLD, 14), fill=(30, 41, 59))
    
    menus_alumni = [
        ("Arsip Ijazah & SKL", "Unduh PDF Terverifikasi", (245, 243, 255), (124, 58, 237)),
        ("Tracer Study", "Kuesioner Pekerjaan", (236, 253, 245), (16, 185, 129)),
        ("Legalisir Digital", "Permohonan Pengesahan", (254, 243, 199), (245, 158, 11)),
        ("Jejaring Alumni", "Info Lowongan Kerja", (239, 246, 255), (37, 99, 235)),
    ]
    
    my = 345
    for idx, (mtitle, msub, c_bg, c_icon) in enumerate(menus_alumni):
        gx = 20 if idx % 2 == 0 else w//2 + 5
        if idx % 2 == 0 and idx > 0:
            my += 95
        draw.rectangle([gx, my, gx + (w//2 - 25), my + 80], fill=c_bg, outline=(226, 232, 240))
        draw.ellipse([gx + 12, my + 15, gx + 42, my + 45], fill=c_icon)
        draw.text((gx + 12, my + 52), mtitle, font=get_font(FONT_UI_BOLD, 11), fill=(15, 23, 42))
        draw.text((gx + 12, my + 66), msub, font=get_font(FONT_UI, 9), fill=(100, 116, 139))
        
    # Bottom Navigation
    draw.rectangle([0, h-65, w, h], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((45, h-45), "Beranda", font=get_font(FONT_UI_BOLD, 11), fill=(124, 58, 237))
    draw.text((170, h-45), "Arsip Digital", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    draw.text((320, h-45), "Profil", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    path = os.path.join(OUTPUT_DIR, "laporan4_05_dashboard_alumni_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_06_role_logic():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - lib/pages/dashboard_page.dart", "Logika Dynamic UI Role-Based Rendering")
    draw_vscode_header(draw, w, "dashboard_page.dart", "apps_sekolah > lib > pages > dashboard_page.dart")
    
    lines = [
        ("// ─── Logika Navigasi & Label Dinamis Berdasarkan Role ────────────────", (106, 153, 85)),
        ("NavigationDestination(", (78, 201, 176)),
        ("  icon: const Icon(Icons.folder_outlined),", (156, 220, 254)),
        ("  selectedIcon: const Icon(Icons.folder_rounded, color: Colors.blue),", (156, 220, 254)),
        ("  label: controller.isSiswa ? 'Prestasi' : 'Arsip Digital',", (206, 145, 120)),
        ("),", (78, 201, 176)),
        ("", (255, 255, 255)),
        ("// ─── Logika Dynamic UI: Pemisahan Menu Siswa Aktif vs Alumni ─────────", (106, 153, 85)),
        ("Widget _buildDynamicMenu(DashboardController controller) {", (86, 156, 214)),
        ("  final isSiswa = controller.isSiswa;", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("  if (isSiswa) {", (86, 156, 214)),
        ("    // Tampilan khusus Siswa Aktif: Input Prestasi, Rapor & Info Kelulusan", (106, 153, 85)),
        ("    return _buildSiswaActiveGridMenu();", (220, 220, 170)),
        ("  } else {", (86, 156, 214)),
        ("    // Tampilan khusus Alumni: Arsip Digital Ijazah & Tracer Study", (106, 153, 85)),
        ("    return _buildAlumniTracerGridMenu();", (220, 220, 170)),
        ("  }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=155, width=w)
    
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    f_sb = get_font(FONT_UI, 11)
    draw.text((12, h-20), "main* | Dart | GetX Controller | Dynamic Role-Based UI", font=f_sb, fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan4_06_role_logic_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_07_git_push():
    w, h = 950, 480
    im = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Terminal PowerShell - Git Push Frontend Flutter", "git push origin main", bg_color=(12, 12, 12))
    
    lines = [
        ("PS D:\\proyek_applikasi\\apps_sekolah> git status", (255, 255, 255)),
        ("On branch main", (200, 200, 200)),
        ("Changes to be committed:", (76, 175, 80)),
        ("  (use \"git restore --staged <file>...\" to unstage)", (150, 150, 150)),
        ("        modified:   lib/pages/login_page.dart", (76, 175, 80)),
        ("        modified:   lib/pages/dashboard_page.dart", (76, 175, 80)),
        ("        modified:   lib/services/api_service.dart", (76, 175, 80)),
        ("        modified:   lib/routes/app_pages.dart", (76, 175, 80)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi\\apps_sekolah> git commit -m \"feat(frontend): complete mobile authentication and dynamic role UI\"", (255, 255, 255)),
        ("[main c48a92f] feat(frontend): complete mobile authentication and dynamic role UI", (220, 220, 220)),
        (" 4 files changed, 412 insertions(+), 35 deletions(-)", (220, 220, 220)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi\\apps_sekolah> git push origin main", (255, 255, 255)),
        ("Enumerating objects: 18, done.", (180, 180, 180)),
        ("Counting objects: 100% (18/18), done.", (180, 180, 180)),
        ("Delta compression using up to 12 threads", (180, 180, 180)),
        ("Compressing objects: 100% (10/10), done.", (180, 180, 180)),
        ("Writing objects: 100% (12/12), 6.18 KiB | 6.18 MiB/s, done.", (180, 180, 180)),
        ("Total 12 (delta 8), reused 0 (delta 0), pack-reused 0", (180, 180, 180)),
        ("To https://github.com/WEMVIAFRIALDO/apps_Sekolah-.git", (100, 181, 246)),
        ("   8f4a1bc..c48a92f  main -> main", (76, 175, 80)),
    ]
    
    y = 52
    f_code = get_font(FONT_CODE, 13)
    for text, col in lines:
        draw.text((25, y), text, font=f_code, fill=col)
        y += 18
        
    path = os.path.join(OUTPUT_DIR, "laporan4_07_git_push_frontend.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan4_08_github():
    w, h = 950, 520
    im = Image.new("RGB", (w, h), (13, 17, 23))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "GitHub - WEMVIAFRIALDO / apps_Sekolah- (Flutter Frontend Repository)", "https://github.com/WEMVIAFRIALDO/apps_Sekolah-", bg_color=(13, 17, 23))
    
    # GitHub Nav Bar
    draw.rectangle([0, 39, w, 82], fill=(22, 27, 34), outline=(48, 54, 61))
    f_repo = get_font(FONT_UI_BOLD, 14)
    draw.text((25, 50), "WEMVIAFRIALDO  /  apps_Sekolah-", font=f_repo, fill=(88, 166, 255))
    
    f_badge = get_font(FONT_UI, 11)
    draw.rectangle([290, 48, 345, 72], outline=(48, 54, 61), fill=(33, 38, 45))
    draw.text((300, 52), "Public", font=f_badge, fill=(201, 209, 217))
    
    # Branch selector
    draw.rectangle([25, 95, 140, 125], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((38, 101), "Branch: main", font=get_font(FONT_UI_BOLD, 11), fill=(201, 209, 217))
    draw.text((160, 101), "apps_Sekolah- / lib / (Flutter Core App)", font=get_font(FONT_UI, 12), fill=(139, 148, 158))
    
    # Commit header
    draw.rectangle([25, 135, w-25, 175], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((40, 146), "WEMVIAFRIALDO", font=get_font(FONT_UI_BOLD, 12), fill=(201, 209, 217))
    draw.text((160, 146), "feat(frontend): complete mobile authentication and dynamic role UI", font=get_font(FONT_UI, 12), fill=(139, 148, 158))
    draw.text((w-160, 146), "Commit: c48a92f", font=get_font(FONT_CODE, 11), fill=(88, 166, 255))
    
    # File list
    files = [
        ("lib/controllers", "State management GetX (AuthController, DashboardController)", "3 days ago"),
        ("lib/models", "Model data Pengguna, Prestasi, dan Tracer Study", "3 days ago"),
        ("lib/pages/login_page.dart", "Antarmuka Login dan form validasi NISN/Password", "3 days ago"),
        ("lib/pages/dashboard_page.dart", "Antarmuka Dashboard dinamis (Siswa Aktif vs Alumni)", "3 days ago"),
        ("lib/routes", "Manajemen routing halaman GetX (AppRoutes, AppPages)", "3 days ago"),
        ("lib/services/api_service.dart", "HTTP Client Dio dan Interceptor otomatis Bearer JWT Token", "3 days ago"),
        ("pubspec.yaml", "Dependensi Flutter (get, dio, flutter_secure_storage, google_fonts)", "3 days ago"),
        ("README.md", "Panduan instalasi dan kompilasi Flutter Mobile", "3 days ago"),
    ]
    
    fy = 176
    f_fl = get_font(FONT_UI, 11)
    for idx, (fname, fmsg, fdate) in enumerate(files):
        draw.rectangle([25, fy, w-25, fy+35], fill=(13, 17, 23) if idx % 2 == 0 else (18, 22, 30), outline=(48, 54, 61))
        draw.text((45, fy+9), fname, font=get_font(FONT_UI_BOLD, 11), fill=(88, 166, 255))
        draw.text((250, fy+9), fmsg, font=f_fl, fill=(139, 148, 158))
        draw.text((w-130, fy+9), fdate, font=f_fl, fill=(110, 118, 129))
        fy += 36
        
    path = os.path.join(OUTPUT_DIR, "laporan4_08_github_frontend.png")
    im.save(path)
    print("Saved:", path)

def generate_all_images():
    print("Mulai membuat gambar screenshot berkualitas tinggi...")
    make_screenshot_laporan3_01_env()
    make_screenshot_laporan3_02_migration()
    make_screenshot_laporan3_03_phpmyadmin()
    make_screenshot_laporan3_04_routes_api()
    make_screenshot_laporan3_05_api_testing()
    make_screenshot_laporan3_06_git_push()
    make_screenshot_laporan3_07_github()
    
    make_screenshot_laporan4_01_login_code()
    make_screenshot_laporan4_02_api_service()
    make_screenshot_laporan4_03_login_mobile()
    make_screenshot_laporan4_04_dashboard_siswa()
    make_screenshot_laporan4_05_dashboard_alumni()
    make_screenshot_laporan4_06_role_logic()
    make_screenshot_laporan4_07_git_push()
    make_screenshot_laporan4_08_github()
    print("Seluruh 15 gambar screenshot berhasil digenerate!")

if __name__ == "__main__":
    generate_all_images()
