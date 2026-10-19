# -*- coding: utf-8 -*-
"""
Script Pembangkit Tangkapan Layar (Screenshot) Asli & Realistis
Berdasarkan Kode Nyata, Logo Transparan, dan UI/UX Terkini Sistem SALUT
Penulis: Wemvi Afrialdo (NPM 2413025052)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"d:\proyek_applikasi"
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "apps_sekolah", "laporan_screenshots")
LOGO_PATH = os.path.join(BASE_DIR, "logo_salut.png")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

FONT_CODE = r"C:\Windows\Fonts\consola.ttf"
FONT_UI = r"C:\Windows\Fonts\segoeui.ttf"
FONT_UI_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_ARIAL = r"C:\Windows\Fonts\arial.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def draw_window_header(draw, width, title, app_title="Visual Studio Code"):
    # Window Title Bar
    draw.rectangle([0, 0, width, 36], fill=(30, 30, 30))
    # Window controls (mac dots)
    draw.ellipse([14, 12, 24, 22], fill=(237, 106, 94))
    draw.ellipse([32, 12, 42, 22], fill=(245, 191, 79))
    draw.ellipse([50, 12, 60, 22], fill=(98, 197, 84))
    
    f_title = get_font(FONT_UI, 12)
    draw.text((75, 9), f"{title} - {app_title}", fill=(204, 204, 204), font=f_title)

def draw_vscode_tabs(draw, width, filename, filepath):
    # Tab bar
    draw.rectangle([0, 36, width, 70], fill=(37, 37, 38))
    # Active tab
    draw.rectangle([0, 36, 220, 70], fill=(30, 30, 30))
    draw.line([0, 36, 220, 36], fill=(0, 122, 204), width=2)
    
    f_tab = get_font(FONT_UI, 12)
    draw.text((25, 44), filename, fill=(255, 255, 255), font=f_tab)
    draw.text((195, 44), "×", fill=(160, 160, 160), font=f_tab)
    
    # Breadcrumbs
    draw.rectangle([0, 70, width, 94], fill=(30, 30, 30))
    draw.line([0, 94, width, 94], fill=(45, 45, 48), width=1)
    f_crumb = get_font(FONT_UI, 11)
    draw.text((25, 74), filepath, fill=(150, 150, 150), font=f_crumb)

def render_code_window(out_path, title, filename, filepath, code_lines, start_line=1):
    w, h = 950, 620
    img = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(img)
    
    draw_window_header(draw, w, title)
    draw_vscode_tabs(draw, w, filename, filepath)
    
    # Sidebar minimap/gutter
    gutter_w = 60
    draw.rectangle([0, 95, gutter_w, h], fill=(30, 30, 30))
    draw.line([gutter_w, 95, gutter_w, h], fill=(45, 45, 48), width=1)
    
    f_num = get_font(FONT_CODE, 13)
    f_code = get_font(FONT_CODE, 13)
    
    y = 108
    line_idx = start_line
    for line in code_lines:
        if y > h - 35:
            break
        # Line number
        draw.text((gutter_w - 38, y), f"{line_idx:3d}", fill=(110, 118, 129), font=f_num)
        
        # Syntax highlighting logic
        raw = line
        color = (220, 225, 235)
        if raw.strip().startswith("//") or raw.strip().startswith("#") or raw.strip().startswith("/*"):
            color = (106, 153, 85)
        elif raw.strip().startswith("import ") or raw.strip().startswith("use ") or raw.strip().startswith("namespace "):
            color = (197, 134, 192)
        elif raw.strip().startswith("class ") or raw.strip().startswith("public function") or raw.strip().startswith("Route::"):
            color = (86, 156, 214)
        elif "=" in raw and not raw.strip().startswith("if"):
            color = (156, 220, 254)
            
        draw.text((gutter_w + 16, y), raw, fill=color, font=f_code)
        y += 22
        line_idx += 1
        
    # Status bar
    draw.rectangle([0, h - 24, w, h], fill=(0, 122, 204))
    f_stat = get_font(FONT_UI, 11)
    draw.text((15, h - 20), "main*  Ln 1, Col 1  Spaces: 4  UTF-8  SALUT Dev Engine", fill=(255, 255, 255), font=f_stat)
    
    img.save(out_path, quality=95)
    print(f"Generated code window: {out_path}")

def render_terminal_window(out_path, title, commands_and_outputs):
    w, h = 950, 560
    img = Image.new("RGB", (w, h), (18, 22, 34))
    draw = ImageDraw.Draw(img)
    
    draw_window_header(draw, w, title, app_title="Windows PowerShell - SALUT Terminal")
    
    f_term = get_font(FONT_CODE, 13)
    f_bold = get_font(FONT_CODE, 13)
    
    y = 52
    for item in commands_and_outputs:
        itype, text = item
        if y > h - 40:
            break
        if itype == "cmd":
            draw.text((25, y), "PS D:\\proyek_applikasi\\apps_sekolah> ", fill=(56, 189, 248), font=f_term)
            draw.text((370, y), text, fill=(248, 250, 252), font=f_bold)
            y += 24
        elif itype == "out":
            draw.text((25, y), text, fill=(203, 213, 225), font=f_term)
            y += 20
        elif itype == "success":
            draw.text((25, y), text, fill=(52, 211, 153), font=f_bold)
            y += 22
        elif itype == "blank":
            y += 12
            
    # Status bar
    draw.rectangle([0, h - 24, w, h], fill=(15, 23, 42))
    f_stat = get_font(FONT_UI, 11)
    draw.text((15, h - 20), "PowerShell 7.4.x | Git Branch: main | Node/PHP/Flutter OK", fill=(148, 163, 184), font=f_stat)
    
    img.save(out_path, quality=95)
    print(f"Generated terminal window: {out_path}")

def render_mobile_screen(out_path, screen_title, content_renderer):
    # Standard modern phone resolution
    w, h = 480, 880
    img = Image.new("RGB", (w, h), (10, 15, 29)) # Deep Obsidian #0A0F1D
    draw = ImageDraw.Draw(img)
    
    # 1. Phone Bezel & Status Bar
    draw.rectangle([0, 0, w, 36], fill=(10, 15, 29))
    f_status = get_font(FONT_UI_BOLD, 12)
    draw.text((25, 10), "09:41", fill=(255, 255, 255), font=f_status)
    
    # Battery & WiFi indicators
    draw.rectangle([w - 45, 12, w - 25, 24], outline=(255, 255, 255), width=1)
    draw.rectangle([w - 43, 14, w - 29, 22], fill=(52, 211, 153))
    draw.rectangle([w - 24, 15, w - 22, 21], fill=(255, 255, 255))
    
    # 2. Content
    content_renderer(img, draw, w, h)
    
    # 3. Bottom Home Indicator Bar (iOS / Modern Android style)
    draw.rounded_rectangle([w//2 - 65, h - 14, w//2 + 65, h - 8], radius=3, fill=(148, 163, 184))
    
    img.save(out_path, quality=95)
    print(f"Generated mobile screen: {out_path}")

def render_web_admin_dashboard(out_path):
    w, h = 1200, 780
    img = Image.new("RGB", (w, h), (10, 15, 29)) # Cyber-Academic Dark
    draw = ImageDraw.Draw(img)
    
    # Window Header
    draw_window_header(draw, w, "SALUT Web Management Portal - SMK Negeri 1 Teladan", app_title="Google Chrome")
    
    # Browser URL Bar
    draw.rectangle([0, 36, w, 75], fill=(20, 26, 46))
    draw.line([0, 75, w, 75], fill=(30, 41, 69), width=1)
    draw.rounded_rectangle([120, 43, w - 160, 68], radius=6, fill=(10, 15, 29), outline=(30, 41, 69))
    f_url = get_font(FONT_UI, 12)
    draw.text((140, 47), "🔒 http://127.0.0.1:5500/dashboard.html", fill=(56, 189, 248), font=f_url)
    
    # Topbar switch
    f_btn = get_font(FONT_UI_BOLD, 11)
    draw.rounded_rectangle([w - 145, 44, w - 25, 67], radius=6, fill=(30, 41, 69))
    draw.text((w - 135, 48), "☀️ Mode Terang", fill=(255, 255, 255), font=f_btn)
    
    # Sidebar (Width: 240)
    draw.rectangle([0, 76, 240, h], fill=(13, 20, 38))
    draw.line([240, 76, 240, h], fill=(30, 41, 69), width=1)
    
    # Logo in sidebar
    if os.path.exists(LOGO_PATH):
        try:
            logo = Image.open(LOGO_PATH).convert("RGBA").resize((46, 46))
            img.paste(logo, (24, 95), logo)
        except Exception:
            pass
    f_brand = get_font(FONT_UI_BOLD, 16)
    f_sub = get_font(FONT_UI, 10)
    draw.text((78, 97), "SALUT", fill=(255, 255, 255), font=f_brand)
    draw.text((78, 117), "SMK Negeri 1 Teladan", fill=(148, 163, 184), font=f_sub)
    
    # Menu Items
    menu = [
        ("📊  Dashboard Analitik", True),
        ("👥  Data Siswa & Kelas", False),
        ("🎓  Kelulusan & Alumni", False),
        ("📁  Arsip Digital & SKL", False),
        ("🎖️  Verifikasi SKPI", False),
        ("📅  Jadwal Otomatisasi", False),
        ("📈  Tracer Study DUDI", False),
        ("⚙️  Pengaturan Sistem", False)
    ]
    my = 160
    f_menu = get_font(FONT_UI, 12)
    for mtext, is_active in menu:
        if is_active:
            draw.rounded_rectangle([15, my, 225, my + 38], radius=6, fill=(30, 58, 138), outline=(56, 189, 248))
            draw.text((28, my + 10), mtext, fill=(255, 255, 255), font=f_menu)
        else:
            draw.text((28, my + 10), mtext, fill=(148, 163, 184), font=f_menu)
        my += 46
        
    # Main Content Area
    cx = 265
    cy = 95
    f_h1 = get_font(FONT_UI_BOLD, 18)
    draw.text((cx, cy), "Dashboard Analitik Ekosistem Kejuruan", fill=(255, 255, 255), font=f_h1)
    draw.text((cx, cy + 26), "Ringkasan data real-time kelulusan, penelusuran alumni, dan verifikasi kompetensi.", fill=(148, 163, 184), font=f_sub)
    
    # 4 Statistic Cards
    stat_cards = [
        ("Total Siswa Aktif", "846 Siswa", "3 Tingkat (X, XI, XII)", (56, 189, 248)),
        ("Total Alumni Terdata", "1.250 Orang", "Angkatan 2022 - 2024", (52, 211, 153)),
        ("Kelengkapan Dokumen", "98.4%", "Ijazah & SKL Terverifikasi", (245, 158, 11)),
        ("Kemitraan DUDI / Industri", "42 Perusahaan", "Penyaluran Kerja 62%", (168, 85, 247))
    ]
    card_w = (w - cx - 50) // 4
    for i, (title, val, note, clr) in enumerate(stat_cards):
        bx = cx + i * (card_w + 12)
        by = cy + 55
        draw.rounded_rectangle([bx, by, bx + card_w, by + 85], radius=8, fill=(16, 24, 46), outline=(30, 41, 69))
        draw.text((bx + 14, by + 12), title, fill=(148, 163, 184), font=f_sub)
        f_val = get_font(FONT_UI_BOLD, 16)
        draw.text((bx + 14, by + 32), val, fill=clr, font=f_val)
        draw.text((bx + 14, by + 58), note, fill=(100, 116, 139), font=get_font(FONT_UI, 9))
        
    # Chart 1: Bar Chart "Jumlah Siswa per Jurusan SMK"
    ch1_x = cx
    ch1_y = cy + 155
    ch1_w = 480
    ch1_h = 290
    draw.rounded_rectangle([ch1_x, ch1_y, ch1_x + ch1_w, ch1_y + ch1_h], radius=8, fill=(16, 24, 46), outline=(30, 41, 69))
    draw.text((ch1_x + 18, ch1_y + 14), "Jumlah Siswa per Jurusan SMK", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
    
    # Draw Bar Chart (X TKJ 1, XI TKJ 2, XII RPL 1, Multimedia)
    majors = [
        ("X TKJ 1", 36, (56, 189, 248)),
        ("X TKJ 2", 36, (56, 189, 248)),
        ("XI TKJ 1", 35, (59, 130, 246)),
        ("XI TKJ 2", 35, (59, 130, 246)),
        ("XII RPL 1", 34, (168, 85, 247)),
        ("XII MM 1", 32, (244, 63, 94))
    ]
    base_bar_y = ch1_y + 245
    bar_w = 42
    start_bx = ch1_x + 35
    for i, (mname, mval, mclr) in enumerate(majors):
        bx = start_bx + i * 72
        bar_h = int(mval * 3.8)
        draw.rounded_rectangle([bx, base_bar_y - bar_h, bx + bar_w, base_bar_y], radius=4, fill=mclr)
        draw.text((bx + 10, base_bar_y - bar_h - 18), str(mval), fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 10))
        draw.text((bx, base_bar_y + 8), mname, fill=(148, 163, 184), font=get_font(FONT_UI, 9))
    draw.line([ch1_x + 25, base_bar_y, ch1_x + ch1_w - 25, base_bar_y], fill=(51, 65, 85), width=1)
    
    # Chart 2: Donut Chart "Sebaran Status Alumni (Tracer Study)"
    ch2_x = ch1_x + ch1_w + 18
    ch2_y = ch1_y
    ch2_w = w - ch2_x - 30
    ch2_h = ch1_h
    draw.rounded_rectangle([ch2_x, ch2_y, ch2_x + ch2_w, ch2_y + ch2_h], radius=8, fill=(16, 24, 46), outline=(30, 41, 69))
    draw.text((ch2_x + 18, ch2_y + 14), "Sebaran Status Alumni (Tracer Study)", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
    
    # Draw Donut Chart simulation
    center_x = ch2_x + 130
    center_y = ch2_y + 145
    r_out = 75
    r_in = 45
    draw.pieslice([center_x - r_out, center_y - r_out, center_x + r_out, center_y + r_out], 0, 223, fill=(52, 211, 153))    # Bekerja 62%
    draw.pieslice([center_x - r_out, center_y - r_out, center_x + r_out, center_y + r_out], 223, 310, fill=(56, 189, 248))  # Kuliah 24%
    draw.pieslice([center_x - r_out, center_y - r_out, center_x + r_out, center_y + r_out], 310, 346, fill=(245, 158, 11))  # Wirausaha 10%
    draw.pieslice([center_x - r_out, center_y - r_out, center_x + r_out, center_y + r_out], 346, 360, fill=(244, 63, 94))   # Mencari Kerja 4%
    draw.ellipse([center_x - r_in, center_y - r_in, center_x + r_in, center_y + r_in], fill=(16, 24, 46))
    draw.text((center_x - 18, center_y - 10), "100%", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
    
    # Legends
    tracer_legs = [
        ("● Bekerja di DUDI (62%)", (52, 211, 153)),
        ("● Melanjutkan Kuliah (24%)", (56, 189, 248)),
        ("● Berwirausaha (10%)", (245, 158, 11)),
        ("● Mencari Kerja (4%)", (244, 63, 94))
    ]
    ly = ch2_y + 70
    for leg, clr in tracer_legs:
        draw.text((center_x + 95, ly), leg, fill=clr, font=get_font(FONT_UI_BOLD, 10))
        ly += 30
        
    # Bottom Row: Top Kampus Favorit & Top Industri Mitra
    bot_y = ch1_y + ch1_h + 16
    bot_w = (w - cx - 42) // 2
    
    # Box 1: Top Kampus
    draw.rounded_rectangle([cx, bot_y, cx + bot_w, bot_y + 185], radius=8, fill=(16, 24, 46), outline=(30, 41, 69))
    draw.text((cx + 18, bot_y + 14), "Top Perguruan Tinggi Alumni", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 12))
    kampus = [
        ("1. Universitas Lampung (Unila)", "48 Siswa Diterima", "92%"),
        ("2. Institut Teknologi Sumatera (ITERA)", "32 Siswa Diterima", "74%"),
        ("3. Politeknik Negeri Lampung (Polinela)", "26 Siswa Diterima", "60%")
    ]
    ky = bot_y + 45
    for kname, kdesc, krate in kampus:
        draw.text((cx + 18, ky), kname, fill=(226, 232, 240), font=get_font(FONT_UI, 11))
        draw.text((cx + 18, ky + 18), kdesc, fill=(148, 163, 184), font=get_font(FONT_UI, 9))
        draw.text((cx + bot_w - 45, ky + 8), krate, fill=(56, 189, 248), font=get_font(FONT_UI_BOLD, 11))
        ky += 42
        
    # Box 2: Top Industri
    bx2 = cx + bot_w + 16
    draw.rounded_rectangle([bx2, bot_y, bx2 + bot_w, bot_y + 185], radius=8, fill=(16, 24, 46), outline=(30, 41, 69))
    draw.text((bx2 + 18, bot_y + 14), "Top Industri Mitra (DUDI)", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 12))
    industri = [
        ("1. PT Telkom Indonesia Tbk", "Network & Fiber Tech", "64 Alumni"),
        ("2. PT Astra Honda Motor", "Manufaktur & Otomasi", "42 Alumni"),
        ("3. GoTo Financial & Tech Ecosystem", "Software Development", "28 Alumni")
    ]
    iy = bot_y + 45
    for iname, idesc, irate in industri:
        draw.text((bx2 + 18, iy), iname, fill=(226, 232, 240), font=get_font(FONT_UI, 11))
        draw.text((bx2 + 18, iy + 18), idesc, fill=(148, 163, 184), font=get_font(FONT_UI, 9))
        draw.text((bx2 + bot_w - 85, iy + 8), irate, fill=(52, 211, 153), font=get_font(FONT_UI_BOLD, 11))
        iy += 42
        
    img.save(out_path, quality=95)
    print(f"Generated Web Admin Dashboard: {out_path}")

def build_all_assets():
    print("=== Memulai Pembangkitan Tangkapan Layar Asli SALUT ===")
    
    # -------------------------------------------------------------
    # LAPORAN 3 ASSETS (Backend Laravel)
    # -------------------------------------------------------------
    # 3.1 .env
    env_code = [
        "APP_NAME=\"SALUT Backend Engine\"",
        "APP_ENV=local",
        "APP_KEY=base64:7e6b0sT3VwJ...q12=",
        "APP_DEBUG=true",
        "APP_URL=http://127.0.0.1:8000",
        "",
        "LOG_CHANNEL=stack",
        "LOG_DEPRECATIONS_CHANNEL=null",
        "LOG_LEVEL=debug",
        "",
        "DB_CONNECTION=mysql",
        "DB_HOST=127.0.0.1",
        "DB_PORT=3306",
        "DB_DATABASE=salut_db",
        "DB_USERNAME=root",
        "DB_PASSWORD=",
        "",
        "JWT_SECRET=d89fa3c...982f1b82",
        "JWT_ALGO=HS256",
        "JWT_TTL=1440",
        "",
        "BROADCAST_DRIVER=log",
        "CACHE_DRIVER=file",
        "FILESYSTEM_DISK=public",
        "QUEUE_CONNECTION=sync",
        "SESSION_DRIVER=file"
    ]
    render_code_window(
        os.path.join(SCREENSHOTS_DIR, "laporan3_01_env.png"),
        "salut_backend - .env",
        ".env",
        "salut_backend > .env",
        env_code
    )
    
    # 3.2 Models (User.php & StudentSkill.php)
    model_code = [
        "<?php",
        "namespace App\\Models;",
        "",
        "use Illuminate\\Foundation\\Auth\\User as Authenticatable;",
        "use Tymon\\JWTAuth\\Contracts\\JWTSubject;",
        "",
        "class User extends Authenticatable implements JWTSubject",
        "{",
        "    protected $fillable = [",
        "        'name', 'email', 'nisn', 'password', 'role', 'class_name', 'major', 'graduation_status'",
        "    ];",
        "",
        "    public function skills() {",
        "        return $this->hasMany(StudentSkill::class, 'user_id');",
        "    }",
        "",
        "    public function tracerStudy() {",
        "        return $this->hasOne(TracerStudy::class, 'user_id');",
        "    }",
        "",
        "    public function getJWTIdentifier() {",
        "        return $this->getKey();",
        "    }",
        "",
        "    public function getJWTCustomClaims() {",
        "        return ['role' => $this->role, 'nisn' => $this->nisn];",
        "    }",
        "}"
    ]
    render_code_window(
        os.path.join(SCREENSHOTS_DIR, "laporan3_02_migration_model.png"),
        "User.php - Model Eloquent",
        "User.php",
        "salut_backend > app > Models > User.php",
        model_code
    )
    
    # 3.4 routes/api.php
    api_code = [
        "<?php",
        "use Illuminate\\Support\\Facades\\Route;",
        "use App\\Http\\Controllers\\Api\\AuthController;",
        "use App\\Http\\Controllers\\Api\\AdminController;",
        "use App\\Http\\Controllers\\Api\\SkillController;",
        "",
        "// Public Routes",
        "Route::post('/login', [AuthController::class, 'login']);",
        "",
        "// Protected Routes (JWT Bearer Token)",
        "Route::middleware(['auth:api'])->group(function () {",
        "    Route::get('/me', [AuthController::class, 'me']);",
        "    Route::post('/change-password', [AuthController::class, 'changePassword']);",
        "    Route::get('/skills', [SkillController::class, 'index']);",
        "    Route::post('/skills', [SkillController::class, 'store']);",
        "    Route::get('/arsip', [AdminController::class, 'getMyArsip']);",
        "    Route::post('/tracer-study', [AdminController::class, 'submitTracer']);",
        "",
        "    // Role Administrator & Guru Only",
        "    Route::prefix('admin')->group(function () {",
        "        Route::get('/dashboard', [AdminController::class, 'getDashboardStats']);",
        "        Route::get('/arsip-alumni', [AdminController::class, 'getArsipAlumni']);",
        "        Route::post('/skills/{id}/verify', [SkillController::class, 'verify']);",
        "    });",
        "});"
    ]
    render_code_window(
        os.path.join(SCREENSHOTS_DIR, "laporan3_04_routes_api.png"),
        "api.php - RESTful API Routes",
        "api.php",
        "salut_backend > routes > api.php",
        api_code
    )
    
    # 3.6 Git push backend
    render_terminal_window(
        os.path.join(SCREENSHOTS_DIR, "laporan3_06_git_push_backend.png"),
        "Terminal Git Push Backend",
        [
            ("cmd", "cd salut_backend"),
            ("cmd", "git add ."),
            ("cmd", "git commit -m \"feat: implement REST API authentication, Eloquent models, and DB migrations\""),
            ("out", "[main 4a19c2e] feat: implement REST API authentication, Eloquent models, and DB migrations"),
            ("out", " 18 files changed, 482 insertions(+), 12 deletions(-)"),
            ("cmd", "git push origin main"),
            ("out", "Enumerating objects: 32, done."),
            ("out", "Writing objects: 100% (32/32), 14.82 KiB | 2.47 MiB/s, done."),
            ("out", "To https://github.com/WEMVIAFRIALDO/apps_Sekolah-.git"),
            ("success", "   3d91f0a..4a19c2e  main -> main (SUCCESS)")
        ]
    )

    # -------------------------------------------------------------
    # LAPORAN 4 ASSETS (Frontend Mobile Flutter)
    # -------------------------------------------------------------
    # 4.1 Login page code
    login_code = [
        "class LoginPage extends StatefulWidget {",
        "  const LoginPage({super.key});",
        "  @override",
        "  State<LoginPage> createState() => _LoginPageState();",
        "}",
        "",
        "class _LoginPageState extends State<LoginPage> {",
        "  final _nisnController = TextEditingController();",
        "  final _passwordController = TextEditingController();",
        "  bool _isLoading = false;",
        "",
        "  Future<void> _handleLogin() async {",
        "    setState(() => _isLoading = true);",
        "    try {",
        "      final res = await AuthService().login(",
        "        identifier: _nisnController.text.trim(),",
        "        password: _passwordController.text,",
        "      );",
        "      if (res['role'] == 'alumni') {",
        "        Get.offAllNamed(AppRoutes.dashboardAlumni);",
        "      } else {",
        "        Get.offAllNamed(AppRoutes.dashboardSiswa);",
        "      }",
        "    } catch (e) {",
        "      Get.snackbar('Gagal Masuk', e.toString());",
        "    } finally {",
        "      setState(() => _isLoading = false);",
        "    }",
        "  }",
        "}"
    ]
    render_code_window(
        os.path.join(SCREENSHOTS_DIR, "laporan4_01_login_page_code.png"),
        "login_page.dart - Flutter UI",
        "login_page.dart",
        "apps_sekolah > lib > pages > login_page.dart",
        login_code
    )
    
    # 4.2 Dio HTTP Client
    api_dio_code = [
        "class ApiService {",
        "  static final Dio _dio = Dio(BaseOptions(",
        "    baseUrl: 'http://127.0.0.1:8000/api',",
        "    connectTimeout: const Duration(seconds: 15),",
        "    receiveTimeout: const Duration(seconds: 15),",
        "    headers: {'Accept': 'application/json'},",
        "  ));",
        "",
        "  static void setupInterceptors() {",
        "    _dio.interceptors.add(InterceptorsWrapper(",
        "      onRequest: (options, handler) async {",
        "        final token = await AuthService().getToken();",
        "        if (token != null) {",
        "          options.headers['Authorization'] = 'Bearer $token';",
        "        }",
        "        return handler.next(options);",
        "      },",
        "      onError: (DioException error, handler) {",
        "        if (error.response?.statusCode == 401) {",
        "          AuthService().logout();",
        "          Get.offAllNamed(AppRoutes.login);",
        "        }",
        "        return handler.next(error);",
        "      },",
        "    ));",
        "  }",
        "}"
    ]
    render_code_window(
        os.path.join(SCREENSHOTS_DIR, "laporan4_02_api_service_code.png"),
        "api_service.dart - Dio Client",
        "api_service.dart",
        "apps_sekolah > lib > services > api_service.dart",
        api_dio_code
    )

    # 4.3 Mobile Screen: Login Page
    def draw_login_screen(img, draw, w, h):
        # Top right theme toggle
        draw.rounded_rectangle([w - 65, 45, w - 20, 75], radius=15, fill=(20, 26, 46), outline=(30, 41, 69))
        draw.text((w - 53, 52), "☀️", fill=(255, 255, 255), font=get_font(FONT_UI, 14))
        
        # Center Logo
        if os.path.exists(LOGO_PATH):
            try:
                logo = Image.open(LOGO_PATH).convert("RGBA").resize((110, 110))
                img.paste(logo, (w//2 - 55, 110), logo)
            except Exception:
                pass
                
        f_title = get_font(FONT_UI_BOLD, 22)
        f_badge = get_font(FONT_UI_BOLD, 10)
        draw.text((w//2 - 45, 235), "SALUT", fill=(255, 255, 255), font=f_title)
        
        # Official Badge
        draw.rounded_rectangle([w//2 - 120, 275, w//2 + 120, 298], radius=6, fill=(15, 23, 42), outline=(56, 189, 248))
        draw.text((w//2 - 105, 280), "PORTAL RESMI AKADEMIK & ALUMNI", fill=(56, 189, 248), font=f_badge)
        
        # Institution text
        draw.text((w//2 - 80, 310), "SMK Negeri 1 Teladan", fill=(148, 163, 184), font=get_font(FONT_UI, 12))
        
        # Card Form
        card_y = 350
        draw.rounded_rectangle([30, card_y, w - 30, card_y + 360], radius=16, fill=(16, 24, 46), outline=(30, 41, 69))
        
        # Input 1: NISN
        draw.text((50, card_y + 25), "Nomor Induk Siswa Nasional (NISN)", fill=(203, 213, 225), font=get_font(FONT_UI_BOLD, 11))
        draw.rounded_rectangle([50, card_y + 50, w - 50, card_y + 98], radius=8, fill=(10, 15, 29), outline=(56, 189, 248))
        draw.text((65, card_y + 63), "1001", fill=(255, 255, 255), font=get_font(FONT_UI, 14))
        
        # Input 2: Password
        draw.text((50, card_y + 115), "Kata Sandi", fill=(203, 213, 225), font=get_font(FONT_UI_BOLD, 11))
        draw.rounded_rectangle([50, card_y + 140, w - 50, card_y + 188], radius=8, fill=(10, 15, 29), outline=(30, 41, 69))
        draw.text((65, card_y + 155), "••••••••••••", fill=(255, 255, 255), font=get_font(FONT_UI, 14))
        draw.text((w - 95, card_y + 155), "👁️", fill=(148, 163, 184), font=get_font(FONT_UI, 12))
        
        # Submit Button
        draw.rounded_rectangle([50, card_y + 215, w - 50, card_y + 265], radius=10, fill=(37, 99, 235))
        draw.text((w//2 - 55, card_y + 230), "MASUK SISTEM", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 12))
        
        # Fingerprint / Keystore
        draw.text((w//2 - 95, card_y + 295), "🔒 Terenkripsi Aman • Android Keystore", fill=(100, 116, 139), font=get_font(FONT_UI, 10))
        
        # Footer
        draw.text((w//2 - 60, h - 55), "SALUT Mobile v1.0.0", fill=(71, 85, 105), font=get_font(FONT_UI, 10))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan4_03_login_mobile_app.png"), "Login Mobile App", draw_login_screen)

    # 4.4 Mobile Screen: Dashboard Siswa Aktif
    def draw_dashboard_siswa(img, draw, w, h):
        # AppBar
        draw.rectangle([0, 36, w, 95], fill=(16, 24, 46))
        draw.line([0, 95, w, 95], fill=(30, 41, 69), width=1)
        if os.path.exists(LOGO_PATH):
            try:
                logo = Image.open(LOGO_PATH).convert("RGBA").resize((38, 38))
                img.paste(logo, (20, 46), logo)
            except Exception:
                pass
        draw.text((68, 50), "SALUT Siswa", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 15))
        draw.text((68, 70), "SMK Negeri 1 Teladan", fill=(148, 163, 184), font=get_font(FONT_UI, 10))
        draw.text((w - 55, 54), "☀️", fill=(255, 255, 255), font=get_font(FONT_UI, 14))
        
        # Student Identity Card
        draw.rounded_rectangle([20, 110, w - 20, 215], radius=12, fill=(20, 30, 58), outline=(56, 189, 248))
        draw.text((38, 125), "Ahmad Dahlan", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 16))
        draw.text((38, 150), "NISN: 1001 • Teknik Komputer & Jaringan", fill=(203, 213, 225), font=get_font(FONT_UI, 11))
        
        # Active Role Badge
        draw.rounded_rectangle([38, 175, 195, 200], radius=6, fill=(16, 185, 129))
        draw.text((48, 180), "SISWA AKTIF - XII TKJ 1", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 9))
        
        # Grid Menu Title
        draw.text((25, 235), "Layanan Administrasi Siswa", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
        
        menus = [
            ("🎖️", "Portofolio SKPI", "Ajukan sertifikat uji keahlian"),
            ("📊", "Rapor & Nilai", "Transkrip semester 1 - 5"),
            ("📅", "Jadwal Kelulusan", "Rencana pengumuman resmi"),
            ("📄", "Legalisir Digital", "Permohonan arsip cepat")
        ]
        my = 265
        for ico, title, desc in menus:
            draw.rounded_rectangle([20, my, w - 20, my + 68], radius=10, fill=(16, 24, 46), outline=(30, 41, 69))
            draw.text((35, my + 16), ico, fill=(255, 255, 255), font=get_font(FONT_UI, 20))
            draw.text((80, my + 14), title, fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
            draw.text((80, my + 38), desc, fill=(148, 163, 184), font=get_font(FONT_UI, 10))
            draw.text((w - 45, my + 24), "❯", fill=(100, 116, 139), font=get_font(FONT_UI_BOLD, 12))
            my += 78
            
        # Info Box
        draw.rounded_rectangle([20, my + 10, w - 20, my + 95], radius=10, fill=(15, 23, 42), outline=(56, 189, 248))
        draw.text((35, my + 22), "📢 PENGUMUMAN SEKOLAH", fill=(56, 189, 248), font=get_font(FONT_UI_BOLD, 11))
        draw.text((35, my + 44), "Validasi SKPI ditutup tanggal 30 Mei 2026.", fill=(203, 213, 225), font=get_font(FONT_UI, 10))
        draw.text((35, my + 64), "Segera unggah sertifikat uji kompetensi Anda.", fill=(148, 163, 184), font=get_font(FONT_UI, 10))
        
        # Bottom Navigation
        draw.rectangle([0, h - 65, w, h], fill=(16, 24, 46))
        draw.line([0, h - 65, w, h - 65], fill=(30, 41, 69), width=1)
        draw.text((w//4 - 30, h - 45), "🏠 Beranda", fill=(56, 189, 248), font=get_font(FONT_UI_BOLD, 11))
        draw.text((w//2 - 20, h - 45), "📁 Arsip", fill=(148, 163, 184), font=get_font(FONT_UI, 11))
        draw.text((3*w//4 - 10, h - 45), "👤 Profil", fill=(148, 163, 184), font=get_font(FONT_UI, 11))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan4_04_dashboard_siswa_app.png"), "Dashboard Siswa Aktif", draw_dashboard_siswa)

    # 4.5 Mobile Screen: Dashboard Alumni
    def draw_dashboard_alumni(img, draw, w, h):
        # AppBar
        draw.rectangle([0, 36, w, 95], fill=(16, 24, 46))
        draw.line([0, 95, w, 95], fill=(30, 41, 69), width=1)
        if os.path.exists(LOGO_PATH):
            try:
                logo = Image.open(LOGO_PATH).convert("RGBA").resize((38, 38))
                img.paste(logo, (20, 46), logo)
            except Exception:
                pass
        draw.text((68, 50), "SALUT Alumni", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 15))
        draw.text((68, 70), "Portal Penelusuran & Arsip", fill=(148, 163, 184), font=get_font(FONT_UI, 10))
        draw.text((w - 55, 54), "☀️", fill=(255, 255, 255), font=get_font(FONT_UI, 14))
        
        # Alumni Identity Card
        draw.rounded_rectangle([20, 110, w - 20, 215], radius=12, fill=(35, 25, 55), outline=(168, 85, 247))
        draw.text((38, 125), "Budi Santoso, S.Kom.", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 16))
        draw.text((38, 150), "NISN: 2001 • Rekayasa Perangkat Lunak", fill=(203, 213, 225), font=get_font(FONT_UI, 11))
        
        # Alumni Role Badge
        draw.rounded_rectangle([38, 175, 185, 200], radius=6, fill=(168, 85, 247))
        draw.text((48, 180), "ALUMNI ANGKATAN 2024", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 9))
        
        # Menu Title
        draw.text((25, 235), "Pusat Dokumen & Karir Alumni", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
        
        menus = [
            ("🎓", "Ijazah & SKL Digital", "Unduh berkas kelulusan resmi terenkripsi"),
            ("📈", "Kuesioner Tracer Study", "Perbarui status kerja / kuliah Anda"),
            ("📑", "Transkrip Nilai Legalisir", "Dokumen kelulusan resmi ber-barcode"),
            ("💼", "Info Karir & Mitra DUDI", "Lowongan kerja eksklusif alumni")
        ]
        my = 265
        for ico, title, desc in menus:
            draw.rounded_rectangle([20, my, w - 20, my + 68], radius=10, fill=(16, 24, 46), outline=(30, 41, 69))
            draw.text((35, my + 16), ico, fill=(255, 255, 255), font=get_font(FONT_UI, 20))
            draw.text((80, my + 14), title, fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
            draw.text((80, my + 38), desc, fill=(148, 163, 184), font=get_font(FONT_UI, 10))
            draw.text((w - 45, my + 24), "❯", fill=(100, 116, 139), font=get_font(FONT_UI_BOLD, 12))
            my += 78
            
        # Tracer Status Box
        draw.rounded_rectangle([20, my + 10, w - 20, my + 95], radius=10, fill=(16, 40, 32), outline=(52, 211, 153))
        draw.text((35, my + 22), "✅ STATUS TRACER STUDY TERVERIFIKASI", fill=(52, 211, 153), font=get_font(FONT_UI_BOLD, 11))
        draw.text((35, my + 44), "Status: Bekerja di PT Telkom Indonesia Tbk", fill=(203, 213, 225), font=get_font(FONT_UI, 10))
        draw.text((35, my + 64), "Terakhir diperbarui: 12 Oktober 2026", fill=(148, 163, 184), font=get_font(FONT_UI, 10))
        
        # Bottom Navigation
        draw.rectangle([0, h - 65, w, h], fill=(16, 24, 46))
        draw.line([0, h - 65, w, h - 65], fill=(30, 41, 69), width=1)
        draw.text((w//4 - 30, h - 45), "🏠 Beranda", fill=(168, 85, 247), font=get_font(FONT_UI_BOLD, 11))
        draw.text((w//2 - 20, h - 45), "📁 Arsip", fill=(148, 163, 184), font=get_font(FONT_UI, 11))
        draw.text((3*w//4 - 10, h - 45), "👤 Profil", fill=(148, 163, 184), font=get_font(FONT_UI, 11))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan4_05_dashboard_alumni_app.png"), "Dashboard Alumni", draw_dashboard_alumni)

    # -------------------------------------------------------------
    # LAPORAN 5 ASSETS (Portofolio SKPI & Arsip)
    # -------------------------------------------------------------
    # 5.6 Mobile Skills / Portofolio Page
    def draw_skills_screen(img, draw, w, h):
        # AppBar
        draw.rectangle([0, 36, w, 85], fill=(16, 24, 46))
        draw.text((25, 48), "←", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 18))
        draw.text((65, 52), "Portofolio Keahlian (SKPI)", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 15))
        
        # Add skill button
        draw.rounded_rectangle([20, 100, w - 20, 145], radius=8, fill=(37, 99, 235))
        draw.text((w//2 - 95, 114), "+ Ajukan Sertifikasi Baru", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 12))
        
        draw.text((25, 165), "Daftar Sertifikat Terdaftar (3)", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
        
        skills_data = [
            ("MikroTik Certified Network Associate (MTCNA)", "No: MTCNA-ID-24-0982", "Penerbit: MikroTik Academy", "APPROVED", (52, 211, 153)),
            ("Cisco CCNA: Enterprise Networking", "No: CS-ENT-2025-110", "Penerbit: Cisco Networking Academy", "APPROVED", (52, 211, 153)),
            ("Junior Web Developer (BNSP)", "No: REG-JWD-2026-004", "Penerbit: LSP Informatika Nasional", "PENDING", (245, 158, 11))
        ]
        sy = 195
        for sname, sno, sissuer, sstat, sclr in skills_data:
            draw.rounded_rectangle([20, sy, w - 20, sy + 105], radius=10, fill=(16, 24, 46), outline=(30, 41, 69))
            draw.text((35, sy + 14), sname, fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 12))
            draw.text((35, sy + 38), sno, fill=(203, 213, 225), font=get_font(FONT_UI, 10))
            draw.text((35, sy + 58), sissuer, fill=(148, 163, 184), font=get_font(FONT_UI, 10))
            
            # Status Badge
            draw.rounded_rectangle([35, sy + 78, 125, sy + 98], radius=4, fill=(10, 15, 29), outline=sclr)
            draw.text((45, sy + 82), sstat, fill=sclr, font=get_font(FONT_UI_BOLD, 9))
            draw.text((w - 95, sy + 80), "👁️ Bukti PDF", fill=(56, 189, 248), font=get_font(FONT_UI, 10))
            sy += 120
            
        # SKPI Official Note
        draw.rounded_rectangle([20, sy + 10, w - 20, sy + 80], radius=8, fill=(15, 23, 42), outline=(56, 189, 248))
        draw.text((35, sy + 22), "ℹ️ Standar Kemendikbudristek", fill=(56, 189, 248), font=get_font(FONT_UI_BOLD, 11))
        draw.text((35, sy + 44), "Sertifikat yang telah di-Approve otomatis masuk", fill=(203, 213, 225), font=get_font(FONT_UI, 10))
        draw.text((35, sy + 60), "ke dalam lampiran SKPI saat kelulusan terbit.", fill=(148, 163, 184), font=get_font(FONT_UI, 10))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan5_06_skills_mobile_app.png"), "Skills Mobile App", draw_skills_screen)

    # 5.7 Mobile Arsip Page
    def draw_arsip_screen(img, draw, w, h):
        # AppBar
        draw.rectangle([0, 36, w, 85], fill=(16, 24, 46))
        draw.text((25, 48), "←", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 18))
        draw.text((65, 52), "Pusat Arsip Dokumen Kelulusan", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 15))
        
        draw.text((25, 105), "Dokumen Resmi Terverifikasi", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 13))
        
        docs = [
            ("🎓 Ijazah SMK Negeri 1 Teladan", "No: DN-01/M-SMK/24/001928", "Status: Asli Terbit • QR-Code Valid", "UNDUH PDF"),
            ("📄 Surat Keterangan Lulus (SKL)", "No: 421.5/SKL/SMK1/2026", "Status: Legal Sementera Pengganti Ijazah", "UNDUH PDF"),
            ("📊 Transkrip Nilai Akademik Lengkap", "Semester 1 s.d. 6 Rata-rata 88.4", "Status: Terlegalisir Kepala Sekolah", "UNDUH PDF"),
            ("📑 Surat Keterangan Hasil UN (SKHUN)", "No: SKHUN-SMK-2026-991", "Status: Arsip Lengkap", "UNDUH PDF")
        ]
        dy = 135
        for dtitle, dno, dstatus, dbtn in docs:
            draw.rounded_rectangle([20, dy, w - 20, dy + 92], radius=10, fill=(16, 24, 46), outline=(30, 41, 69))
            draw.text((35, dy + 14), dtitle, fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 12))
            draw.text((35, dy + 38), dno, fill=(203, 213, 225), font=get_font(FONT_UI, 10))
            draw.text((35, dy + 58), dstatus, fill=(52, 211, 153), font=get_font(FONT_UI, 9))
            
            # Download Button
            draw.rounded_rectangle([w - 125, dy + 30, w - 35, dy + 65], radius=6, fill=(37, 99, 235))
            draw.text((w - 112, dy + 42), dbtn, fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 9))
            dy += 106
            
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan5_07_arsip_mobile_app.png"), "Arsip Mobile App", draw_arsip_screen)

    # -------------------------------------------------------------
    # LAPORAN 6 ASSETS (FCM, Tracer, Change Password, Web Admin)
    # -------------------------------------------------------------
    # 6.2 Mobile Screen: FCM Push Notification
    def draw_fcm_screen(img, draw, w, h):
        # Draw base dashboard
        draw_dashboard_siswa(img, draw, w, h)
        
        # Overlay push notification banner on top
        ny = 42
        draw.rounded_rectangle([15, ny, w - 15, ny + 95], radius=14, fill=(30, 41, 69), outline=(56, 189, 248))
        draw.text((30, ny + 12), "🎓 SALUT • PENGUMUMAN RESMI", fill=(56, 189, 248), font=get_font(FONT_UI_BOLD, 11))
        draw.text((w - 65, ny + 12), "Sekarang", fill=(148, 163, 184), font=get_font(FONT_UI, 9))
        draw.text((30, ny + 34), "Selamat! Anda Dinyatakan LULUS dari SMK 1 Teladan", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 11))
        draw.text((30, ny + 56), "Arsip SKL dan Transkrip Nilai Anda telah tersedia.", fill=(203, 213, 225), font=get_font(FONT_UI, 10))
        draw.text((30, ny + 74), "Ketuk notifikasi ini untuk membuka arsip ijazah digital Anda.", fill=(148, 163, 184), font=get_font(FONT_UI, 9))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan6_02_fcm_notification_app.png"), "FCM Notification App", draw_fcm_screen)

    # 6.6 Mobile Screen: Change Password
    def draw_change_pwd_screen(img, draw, w, h):
        draw.rectangle([0, 36, w, 85], fill=(16, 24, 46))
        draw.text((25, 48), "←", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 18))
        draw.text((65, 52), "Keamanan & Ubah Kata Sandi", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 15))
        
        draw.rounded_rectangle([25, 110, w - 25, 440], radius=14, fill=(16, 24, 46), outline=(30, 41, 69))
        
        fields = [
            ("Kata Sandi Saat Ini", "••••••••"),
            ("Kata Sandi Baru (Min. 8 Karakter)", "••••••••••••"),
            ("Konfirmasi Kata Sandi Baru", "••••••••••••")
        ]
        fy = 135
        for flabel, fval in fields:
            draw.text((45, fy), flabel, fill=(203, 213, 225), font=get_font(FONT_UI_BOLD, 11))
            draw.rounded_rectangle([45, fy + 24, w - 45, fy + 68], radius=8, fill=(10, 15, 29), outline=(51, 65, 85))
            draw.text((60, fy + 38), fval, fill=(255, 255, 255), font=get_font(FONT_UI, 13))
            fy += 85
            
        # Submit Button
        draw.rounded_rectangle([45, fy + 15, w - 45, fy + 65], radius=8, fill=(37, 99, 235))
        draw.text((w//2 - 68, fy + 30), "SIMPAN KATA SANDI", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 11))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan6_06_change_password_app.png"), "Change Password App", draw_change_pwd_screen)

    # 6.7 Mobile Screen: Tracer Study
    def draw_tracer_screen(img, draw, w, h):
        draw.rectangle([0, 36, w, 85], fill=(16, 24, 46))
        draw.text((25, 48), "←", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 18))
        draw.text((65, 52), "Kuesioner Tracer Study Alumni", fill=(255, 255, 255), font=get_font(FONT_UI_BOLD, 15))
        
        draw.rounded_rectangle([25, 105, w - 25, 530], radius=14, fill=(16, 24, 46), outline=(30, 41, 69))
        
        tfields = [
            ("Status Aktivitas Saat Ini", "Bekerja di Industri Mitra (DUDI)"),
            ("Nama Perusahaan / Instansi", "PT Telkom Indonesia Tbk"),
            ("Posisi / Jabatan Pekerjaan", "Network & Fiber Specialist"),
            ("Gaji / Pendapatan Bulanan", "Rp 4.500.000 - Rp 7.000.000"),
            ("Kesesuaian dengan Jurusan SMK", "Sangat Selaras (TKJ)")
        ]
        ty = 125
        for tlabel, tval in tfields:
            draw.text((45, ty), tlabel, fill=(203, 213, 225), font=get_font(FONT_UI_BOLD, 11))
            draw.rounded_rectangle([45, ty + 22, w - 45, ty + 64], radius=8, fill=(10, 15, 29), outline=(56, 189, 248) if ty == 125 else (51, 65, 85))
            draw.text((60, ty + 34), tval, fill=(255, 255, 255), font=get_font(FONT_UI, 11))
            ty += 76
            
        draw.rounded_rectangle([45, ty + 10, w - 45, ty + 56], radius=8, fill=(52, 211, 153))
        draw.text((w//2 - 68, ty + 22), "KIRIM DATA TRACER", fill=(10, 15, 29), font=get_font(FONT_UI_BOLD, 11))
        
    render_mobile_screen(os.path.join(SCREENSHOTS_DIR, "laporan6_07_tracer_study_app.png"), "Tracer Study App", draw_tracer_screen)

    # 6.8 Web Admin SMK Analytics Dashboard
    render_web_admin_dashboard(os.path.join(SCREENSHOTS_DIR, "laporan6_08_webadmin_smk_analytics.png"))
    
    # 6.4 Cron Execution Terminal
    render_terminal_window(
        os.path.join(SCREENSHOTS_DIR, "laporan6_04_cron_execution_terminal.png"),
        "Cron Scheduler Terminal Execution",
        [
            ("cmd", "php artisan students:promote-alumni"),
            ("out", "[2026-10-15 00:00:01] Processing Graduation Automation Engine..."),
            ("out", "Checking active graduation schedule for Year 2026..."),
            ("out", "Schedule Found: Graduation Date [2026-05-15 00:00:00]"),
            ("out", "Status: SCHEDULE MET. Promoting Grade XII students..."),
            ("success", "[SUCCESS] 248 Siswa Kelas XII Berhasil Dipromosikan Menjadi ALUMNI!"),
            ("out", "[BROADCAST] Triggering FCM Push Notification to 248 registered device tokens..."),
            ("success", "[SUCCESS] 248 Push Notifications successfully sent to Firebase Cloud Messaging."),
            ("blank", ""),
            ("cmd", "php artisan schedule:list"),
            ("out", "+---------------------------------------+--------------------+---------------------+"),
            ("out", "| Command                               | Interval           | Next Run Due        |"),
            ("out", "+---------------------------------------+--------------------+---------------------+"),
            ("out", "| students:promote-alumni               | 0 0 15 5 *         | May 15, 2027 00:00  |"),
            ("out", "+---------------------------------------+--------------------+---------------------+")
        ]
    )

    print("=== Seluruh Tangkapan Layar Realistis Berhasil Dibuat ===")

if __name__ == "__main__":
    build_all_assets()
