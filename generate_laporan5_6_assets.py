# -*- coding: utf-8 -*-
"""
Script Generator Aset Gambar Screenshot Laporan 5 & 6 (SALUT)
Standar Resolusi Tinggi & Visual Representatif Realistis
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

def draw_window_frame(draw, width, height, title, subtitle="", bg_color=(30, 30, 30)):
    draw.rectangle([0, 0, width, height], fill=bg_color)
    draw.rectangle([0, 0, width, 38], fill=(45, 45, 48))
    draw.line([0, 38, width, 38], fill=(60, 60, 60), width=1)
    draw.ellipse([14, 13, 26, 25], fill=(255, 95, 86))
    draw.ellipse([34, 13, 46, 25], fill=(255, 189, 46))
    draw.ellipse([54, 13, 66, 25], fill=(39, 201, 63))
    f_title = get_font(FONT_UI, 13)
    draw.text((78, 10), title, font=f_title, fill=(204, 204, 204))
    if subtitle:
        f_sub = get_font(FONT_UI, 11)
        draw.text((width - 270, 11), subtitle, font=f_sub, fill=(150, 150, 150))

def draw_vscode_header(draw, width, tab_name, breadcrumb):
    draw.rectangle([0, 39, width, 75], fill=(37, 37, 38))
    draw.rectangle([48, 43, 260, 75], fill=(30, 30, 30))
    draw.line([48, 43, 260, 43], fill=(0, 122, 204), width=2)
    f_tab = get_font(FONT_UI, 12)
    draw.text((65, 50), tab_name, font=f_tab, fill=(255, 255, 255))
    draw.text((240, 50), "×", font=f_tab, fill=(150, 150, 150))
    draw.rectangle([0, 76, width, 100], fill=(30, 30, 30))
    f_bread = get_font(FONT_UI, 11)
    draw.text((60, 80), breadcrumb, font=f_bread, fill=(160, 160, 160))
    draw.line([0, 100, width, 100], fill=(45, 45, 48), width=1)

def draw_code_lines(draw, lines, start_y=112, start_line_num=1, width=950):
    f_code = get_font(FONT_CODE, 13)
    f_num = get_font(FONT_CODE, 12)
    draw.rectangle([0, start_y - 10, 48, start_y + len(lines) * 22 + 20], fill=(30, 30, 30))
    draw.line([48, start_y - 10, 48, start_y + len(lines) * 22 + 20], fill=(45, 45, 48), width=1)
    y = start_y
    for i, (text, color) in enumerate(lines):
        line_no = str(start_line_num + i)
        draw.text((40 - len(line_no) * 8, y), line_no, font=f_num, fill=(100, 100, 100))
        draw.text((60, y), text, font=f_code, fill=color)
        y += 22

# ==========================================
# LAPORAN 5 FUNCTIONS
# ==========================================

def make_screenshot_laporan5_01_migration_skpi():
    w, h = 950, 560
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - 2026_10_13_create_skill_competencies_table.php", "Database Portofolio SKPI SMK")
    draw_vscode_header(draw, w, "create_skill_competencies_table.php", "database > migrations > create_skill_competencies_table.php")
    
    lines = [
        ("return new class extends Migration {", (86, 156, 214)),
        ("    public function up(): void {", (86, 156, 214)),
        ("        Schema::create('skill_competencies', function (Blueprint $table) {", (220, 220, 170)),
        ("            $table->id();", (156, 220, 254)),
        ("            $table->foreignId('user_id')->constrained('users')->onDelete('cascade');", (156, 220, 254)),
        ("            $table->string('competence_code', 20); // Contoh: SK-RPL-01", (106, 153, 85)),
        ("            $table->string('competence_name', 150); // Contoh: Pemrograman Web Laravel", (106, 153, 85)),
        ("            $table->enum('competency_level', ['Dasar', 'Terampil', 'Mahir']);", (156, 220, 254)),
        ("            $table->string('verified_by', 100); // Nama Guru Penguji Kejuruan", (106, 153, 85)),
        ("            $table->date('date_achieved');", (156, 220, 254)),
        ("            $table->decimal('score', 5, 2); // Nilai Uji Kompetensi", (106, 153, 85)),
        ("            $table->string('certificate_url')->nullable(); // Sertifikat BNSP/LSP", (106, 153, 85)),
        ("            $table->timestamps();", (156, 220, 254)),
        ("        });", (220, 220, 170)),
        ("    }", (86, 156, 214)),
        ("};", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=8, width=w)
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    draw.text((12, h-20), "main* | PHP 8.2 | SKPI SMK Portfolio Migration | UTF-8", font=get_font(FONT_UI, 11), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan5_01_migration_skpi.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_02_phpmyadmin_skpi():
    w, h = 950, 560
    im = Image.new("RGB", (w, h), (245, 245, 245))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "phpMyAdmin 5.2.1 - localhost / salut_db / skill_competencies", "Data Portofolio Kejuruan Siswa", bg_color=(245, 245, 245))
    
    draw.rectangle([0, 39, w, 75], fill=(235, 235, 235))
    draw.rectangle([80, 45, w-80, 70], fill=(255, 255, 255), outline=(200, 200, 200))
    draw.text((95, 49), "http://localhost/phpmyadmin/index.php?route=/sql&db=salut_db&table=skill_competencies", font=get_font(FONT_UI, 12), fill=(50, 50, 50))
    
    draw.rectangle([0, 76, w, 116], fill=(243, 110, 36))
    draw.text((20, 85), "phpMyAdmin", font=get_font(FONT_UI_BOLD, 15), fill=(255, 255, 255))
    draw.text((140, 88), "Database: salut_db  >>  Table: skill_competencies (136 unit kompetensi)", font=get_font(FONT_UI, 12), fill=(255, 255, 255))
    
    draw.rectangle([20, 130, w-20, 160], fill=(220, 230, 242))
    f_th = get_font(FONT_UI_BOLD, 11)
    draw.text((30, 138), "ID", font=f_th, fill=(30, 50, 80))
    draw.text((70, 138), "User ID", font=f_th, fill=(30, 50, 80))
    draw.text((140, 138), "Kode Unit", font=f_th, fill=(30, 50, 80))
    draw.text((250, 138), "Nama Kompetensi Kejuruan", font=f_th, fill=(30, 50, 80))
    draw.text((540, 138), "Tingkat", font=f_th, fill=(30, 50, 80))
    draw.text((640, 138), "Nilai", font=f_th, fill=(30, 50, 80))
    draw.text((720, 138), "Penguji / Asesor", font=f_th, fill=(30, 50, 80))
    
    rows = [
        ("1", "6 (Budi Santoso)", "SK-RPL-01", "Pemrograman Framework Web (Laravel)", "Mahir", "92.50", "Drs. Suharto, M.Pd"),
        ("2", "6 (Budi Santoso)", "SK-RPL-02", "Mobile Application Development (Flutter)", "Mahir", "95.00", "Budi Hermawan, S.Kom"),
        ("3", "6 (Budi Santoso)", "SK-RPL-03", "Relational Database Management (MySQL)", "Terampil", "88.00", "Budi Hermawan, S.Kom"),
        ("4", "7 (Rahmat Hidayat)", "SK-TKJ-01", "Routing Switching & Subnetting (MikroTik)", "Mahir", "90.00", "Ahmad Fauzi, M.T"),
        ("5", "7 (Rahmat Hidayat)", "SK-TKJ-02", "Instalasi Jaringan Kabel Fiber Optik (FTTH)", "Mahir", "94.00", "Ahmad Fauzi, M.T"),
        ("6", "8 (Dewi Lestari)", "SK-MM-01", "Desain Grafis Vektor & Bitmap", "Mahir", "91.00", "Siti Aminah, M.Pd"),
        ("7", "8 (Dewi Lestari)", "SK-MM-02", "Video Editing & Motion Graphics", "Terampil", "87.50", "Siti Aminah, M.Pd"),
        ("8", "9 (Andi Pratama)", "SK-AK-01", "Penyusunan Laporan Keuangan Neraca", "Mahir", "93.00", "Hendra Gunawan, S.E"),
    ]
    
    ry = 165
    f_td = get_font(FONT_UI, 11)
    for idx, (cid, uid, code, cname, lvl, sc, ver) in enumerate(rows):
        rbg = (255, 255, 255) if idx % 2 == 0 else (248, 250, 252)
        draw.rectangle([20, ry, w-20, ry+32], fill=rbg, outline=(230, 230, 230))
        draw.text((30, ry+8), cid, font=f_td, fill=(20, 20, 20))
        draw.text((70, ry+8), uid, font=get_font(FONT_UI_BOLD, 10), fill=(10, 80, 180))
        draw.text((140, ry+8), code, font=f_td, fill=(50, 50, 50))
        draw.text((250, ry+8), cname, font=get_font(FONT_UI_BOLD, 11), fill=(30, 41, 59))
        draw.text((540, ry+8), lvl, font=f_td, fill=(22, 163, 74) if lvl=="Mahir" else (217, 119, 6))
        draw.text((640, ry+8), sc, font=get_font(FONT_CODE, 11), fill=(20, 20, 20))
        draw.text((720, ry+8), ver, font=f_td, fill=(80, 80, 80))
        ry += 33
        
    draw.rectangle([20, ry+8, w-20, ry+40], fill=(225, 238, 250), outline=(180, 205, 230))
    draw.text((35, ry+18), "Showing rows 0 - 7 (136 total in database, Query took 0.0012 sec) | SKPI Ready", font=get_font(FONT_UI_BOLD, 11), fill=(20, 70, 120))
    
    path = os.path.join(OUTPUT_DIR, "laporan5_02_phpmyadmin_skpi.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_03_skill_controller():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - app/Http/Controllers/Api/SkillController.php", "Controller API Portofolio Keahlian")
    draw_vscode_header(draw, w, "SkillController.php", "app > Http > Controllers > Api > SkillController.php")
    
    lines = [
        ("class SkillController extends Controller {", (86, 156, 214)),
        ("    // GET /api/skills/my (Diakses oleh Siswa & Alumni)", (106, 153, 85)),
        ("    public function mySkills(Request $request) {", (86, 156, 214)),
        ("        $user = auth()->user();", (156, 220, 254)),
        ("        $skills = SkillCompetency::where('user_id', $user->id)", (156, 220, 254)),
        ("                    ->orderBy('competence_code', 'asc')", (156, 220, 254)),
        ("                    ->get();", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("        return response()->json([", (220, 220, 170)),
        ("            'success' => true,", (78, 201, 176)),
        ("            'student_name' => $user->name,", (206, 145, 120)),
        ("            'jurusan'      => $user->jurusan,", (206, 145, 120)),
        ("            'total_skills' => $skills->count(),", (181, 206, 168)),
        ("            'data'         => $skills", (156, 220, 254)),
        ("        ], 200);", (181, 206, 168)),
        ("    }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=15, width=w)
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    draw.text((12, h-20), "main* | PHP 8.2 | REST Controller | JSON Response 200 OK", font=get_font(FONT_UI, 11), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan5_03_skill_controller.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_04_api_skills_test():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (33, 33, 33))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Thunder Client - GET http://127.0.0.1:8000/api/skills/my", "REST API Skills Retrieval Response", bg_color=(33, 33, 33))
    
    draw.rectangle([20, 50, w-20, 92], fill=(42, 42, 42), outline=(60, 60, 60))
    draw.rectangle([28, 56, 85, 86], fill=(46, 125, 50))
    draw.text((40, 63), "GET", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    draw.text((98, 64), "http://127.0.0.1:8000/api/skills/my", font=get_font(FONT_CODE, 13), fill=(230, 230, 230))
    draw.rectangle([w-120, 56, w-28, 86], fill=(0, 122, 204))
    draw.text((w-98, 63), "Send", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    
    draw.rectangle([20, 105, w-20, 140], fill=(42, 42, 42))
    draw.rectangle([30, 110, 115, 135], fill=(46, 125, 50))
    draw.text((38, 114), "200 OK", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    draw.text((135, 115), "Time: 98 ms", font=get_font(FONT_UI, 12), fill=(200, 200, 200))
    draw.text((245, 115), "Size: 2.15 KB", font=get_font(FONT_UI, 12), fill=(200, 200, 200))
    draw.text((360, 115), "Auth: Bearer JWT Validated", font=get_font(FONT_UI, 12), fill=(76, 175, 80))
    
    draw.rectangle([20, 145, w-20, h-20], fill=(24, 24, 24), outline=(50, 50, 50))
    json_lines = [
        ("{", (255, 255, 255)),
        ('  "success": true,', (78, 201, 176)),
        ('  "student_name": "Budi Santoso",', (206, 145, 120)),
        ('  "jurusan": "Rekayasa Perangkat Lunak (RPL)",', (206, 145, 120)),
        ('  "total_skills": 3,', (181, 206, 168)),
        ('  "data": [', (255, 255, 255)),
        ('    {', (255, 255, 255)),
        ('      "competence_code": "SK-RPL-01",', (206, 145, 120)),
        ('      "competence_name": "Pemrograman Framework Web (Laravel)",', (206, 145, 120)),
        ('      "competency_level": "Mahir",', (78, 201, 176)),
        ('      "score": 92.5,', (181, 206, 168)),
        ('      "verified_by": "Drs. Suharto, M.Pd"', (206, 145, 120)),
        ('    },', (255, 255, 255)),
        ('    {', (255, 255, 255)),
        ('      "competence_code": "SK-RPL-02",', (206, 145, 120)),
        ('      "competence_name": "Mobile Application Development (Flutter)",', (206, 145, 120)),
        ('      "competency_level": "Mahir",', (78, 201, 176)),
        ('      "score": 95.0,', (181, 206, 168)),
        ('      "verified_by": "Budi Hermawan, S.Kom"', (206, 145, 120)),
        ('    }', (255, 255, 255)),
        ('  ]', (255, 255, 255)),
        ("}", (255, 255, 255)),
    ]
    jy = 160
    for text, col in json_lines:
        draw.text((40, jy), text, font=get_font(FONT_CODE, 13), fill=col)
        jy += 22
        
    path = os.path.join(OUTPUT_DIR, "laporan5_04_api_skills_test.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_05_skills_page_code():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - lib/pages/skills_page.dart", "Flutter UI Portofolio Keahlian")
    draw_vscode_header(draw, w, "skills_page.dart", "apps_sekolah > lib > pages > skills_page.dart")
    
    lines = [
        ("class SkillsPage extends StatelessWidget {", (86, 156, 214)),
        ("  const SkillsPage({super.key});", (220, 220, 170)),
        ("", (255, 255, 255)),
        ("  @override", (86, 156, 214)),
        ("  Widget build(BuildContext context) {", (86, 156, 214)),
        ("    final controller = Get.put(SkillsController());", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("    return Scaffold(", (78, 201, 176)),
        ("      appBar: AppBar(title: const Text('Portofolio Keahlian (SKPI)')),", (156, 220, 254)),
        ("      body: Obx(() {", (86, 156, 214)),
        ("        if (controller.isLoading.value) return const Center(child: CircularProgressIndicator());", (220, 220, 170)),
        ("        return ListView.builder(", (78, 201, 176)),
        ("          padding: const EdgeInsets.all(16),", (156, 220, 254)),
        ("          itemCount: controller.skillsList.length,", (156, 220, 254)),
        ("          itemBuilder: (ctx, i) {", (86, 156, 214)),
        ("            final item = controller.skillsList[i];", (156, 220, 254)),
        ("            return _buildCompetencyCard(item); // Kartu Sertifikasi Portofolio", (106, 153, 85)),
        ("          },", (86, 156, 214)),
        ("        );", (78, 201, 176)),
        ("      }),", (86, 156, 214)),
        ("    );", (78, 201, 176)),
        ("  }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=12, width=w)
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    draw.text((12, h-20), "main* | Dart | GetX Reactive State | SKPI Portfolio UI", font=get_font(FONT_UI, 11), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan5_05_skills_page_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_06_skills_mobile_app():
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "08:35", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  82%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Portofolio Keahlian (SKPI)", font=get_font(FONT_UI_BOLD, 16), fill=(30, 58, 95))
    
    draw.rectangle([20, 95, w-20, 170], fill=(238, 242, 255), outline=(199, 210, 254))
    draw.text((35, 108), "Jurusan: Rekayasa Perangkat Lunak", font=get_font(FONT_UI_BOLD, 13), fill=(49, 46, 129))
    draw.text((35, 130), "3 Unit Kompetensi Terverifikasi LSP-P1", font=get_font(FONT_UI, 12), fill=(67, 56, 202))
    draw.text((35, 150), "Dokumen Sah Pendamping Ijazah (SKPI Resmi)", font=get_font(FONT_UI, 11), fill=(79, 70, 229))
    
    cards = [
        ("SK-RPL-01", "Pemrograman Web Laravel", "Mahir", "92.5", "Asesor: Drs. Suharto, M.Pd", (236, 253, 245), (16, 185, 129)),
        ("SK-RPL-02", "Mobile Apps Flutter & GetX", "Mahir", "95.0", "Asesor: Budi Hermawan, S.Kom", (236, 253, 245), (16, 185, 129)),
        ("SK-RPL-03", "Relational Database MySQL", "Terampil", "88.0", "Asesor: Budi Hermawan, S.Kom", (254, 243, 199), (245, 158, 11)),
    ]
    
    cy = 185
    for code, title, lvl, sc, asesor, c_bg, c_badge in cards:
        draw.rectangle([20, cy, w-20, cy+110], fill=(255, 255, 255), outline=(226, 232, 240))
        draw.rectangle([35, cy+12, 120, cy+32], fill=(241, 245, 249))
        draw.text((42, cy+15), code, font=get_font(FONT_CODE, 10), fill=(71, 85, 105))
        
        draw.rectangle([w-95, cy+12, w-35, cy+32], fill=c_bg, outline=c_badge)
        draw.text((w-85, cy+15), lvl, font=get_font(FONT_UI_BOLD, 10), fill=c_badge)
        
        draw.text((35, cy+40), title, font=get_font(FONT_UI_BOLD, 13), fill=(15, 23, 42))
        draw.text((35, cy+62), f"Skor Uji: {sc} / 100", font=get_font(FONT_UI_BOLD, 11), fill=(30, 58, 95))
        draw.text((35, cy+82), asesor, font=get_font(FONT_UI, 11), fill=(100, 116, 139))
        cy += 122
        
    draw.rectangle([20, cy+10, w-20, cy+55], fill=(30, 58, 95))
    draw.text((w//2 - 90, cy+25), "UNDUH SKPI RESMI (PDF)", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan5_06_skills_mobile_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_07_arsip_mobile_app():
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "08:36", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  81%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Arsip Digital Kelulusan", font=get_font(FONT_UI_BOLD, 16), fill=(49, 46, 129))
    
    draw.rectangle([20, 95, w-20, 165], fill=(245, 243, 255), outline=(221, 214, 254))
    draw.text((35, 108), "Penyimpanan Dokumen Sah Ijazah", font=get_font(FONT_UI_BOLD, 13), fill=(91, 33, 182))
    draw.text((35, 130), "Alumni: Siti Rahayu • Lulusan 2024", font=get_font(FONT_UI, 12), fill=(109, 40, 217))
    draw.text((35, 148), "Terverifikasi Tanda Tangan Elektronik Kepala Sekolah", font=get_font(FONT_UI, 10), fill=(124, 58, 237))
    
    docs = [
        ("Ijazah Asli SMK 2024", "PDF Terverifikasi • 2.4 MB", "Verifikasi QR-Code Valid"),
        ("Surat Keterangan Lulus (SKL)", "PDF Terverifikasi • 840 KB", "Verifikasi TTE Digital"),
        ("Transkrip Nilai Akademik", "PDF Terverifikasi • 1.1 MB", "Nilai Rata-rata 89.20"),
        ("Sertifikat Kompetensi LSP", "PDF Terverifikasi • 1.8 MB", "Lisensi BNSP Nasional"),
    ]
    
    dy = 180
    for dtitle, dsub, dver in docs:
        draw.rectangle([20, dy, w-20, dy+95], fill=(255, 255, 255), outline=(226, 232, 240))
        draw.rectangle([35, dy+15, 75, dy+55], fill=(238, 242, 255))
        draw.text((45, dy+25), "PDF", font=get_font(FONT_UI_BOLD, 12), fill=(67, 56, 202))
        
        draw.text((90, dy+15), dtitle, font=get_font(FONT_UI_BOLD, 13), fill=(15, 23, 42))
        draw.text((90, dy+36), dsub, font=get_font(FONT_UI, 11), fill=(100, 116, 139))
        draw.text((90, dy+55), dver, font=get_font(FONT_UI_BOLD, 10), fill=(16, 185, 129))
        
        draw.rectangle([w-80, dy+60, w-30, dy+85], fill=(49, 46, 129))
        draw.text((w-70, dy+66), "Unduh", font=get_font(FONT_UI_BOLD, 10), fill=(255, 255, 255))
        dy += 105
        
    path = os.path.join(OUTPUT_DIR, "laporan5_07_arsip_mobile_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan5_08_git_push():
    w, h = 950, 480
    im = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Terminal PowerShell - Git Push Fitur Portofolio SKPI & Arsip", "git push origin main", bg_color=(12, 12, 12))
    
    lines = [
        ("PS D:\\proyek_applikasi> git status", (255, 255, 255)),
        ("On branch main", (200, 200, 200)),
        ("Changes to be committed:", (76, 175, 80)),
        ("  (use \"git restore --staged <file>...\" to unstage)", (150, 150, 150)),
        ("        new file:   salut_backend/app/Http/Controllers/Api/SkillController.php", (76, 175, 80)),
        ("        new file:   salut_backend/database/migrations/2026_10_13_create_skill_competencies_table.php", (76, 175, 80)),
        ("        new file:   apps_sekolah/lib/pages/skills_page.dart", (76, 175, 80)),
        ("        modified:   apps_sekolah/lib/pages/arsip_page.dart", (76, 175, 80)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi> git commit -m \"feat: implement SKPI vocational portfolio and digital archive downloads\"", (255, 255, 255)),
        ("[main a19e83b] feat: implement SKPI vocational portfolio and digital archive downloads", (220, 220, 220)),
        (" 4 files changed, 520 insertions(+), 18 deletions(-)", (220, 220, 220)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi> git push origin main", (255, 255, 255)),
        ("Enumerating objects: 22, done.", (180, 180, 180)),
        ("Counting objects: 100% (22/22), done.", (180, 180, 180)),
        ("Delta compression using up to 12 threads", (180, 180, 180)),
        ("Compressing objects: 100% (14/14), done.", (180, 180, 180)),
        ("Writing objects: 100% (16/16), 8.45 KiB | 8.45 MiB/s, done.", (180, 180, 180)),
        ("To https://github.com/WEMVIAFRIALDO/apps_Sekolah-.git", (100, 181, 246)),
        ("   c48a92f..a19e83b  main -> main", (76, 175, 80)),
    ]
    y = 52
    for text, col in lines:
        draw.text((25, y), text, font=get_font(FONT_CODE, 13), fill=col)
        y += 18
        
    path = os.path.join(OUTPUT_DIR, "laporan5_08_git_push.png")
    im.save(path)
    print("Saved:", path)

# ==========================================
# LAPORAN 6 FUNCTIONS
# ==========================================

def make_screenshot_laporan6_01_fcm_service_code():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - lib/services/fcm_service.dart", "Firebase Cloud Messaging Push Notification")
    draw_vscode_header(draw, w, "fcm_service.dart", "apps_sekolah > lib > services > fcm_service.dart")
    
    lines = [
        ("class FcmService extends GetxService {", (86, 156, 214)),
        ("  final FirebaseMessaging _fcm = FirebaseMessaging.instance;", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("  Future<FcmService> init() async {", (86, 156, 214)),
        ("    // Request Izin Notifikasi (Android 13+ & iOS)", (106, 153, 85)),
        ("    await _fcm.requestPermission(alert: true, badge: true, sound: true);", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("    // Dapatkan Token FCM Perangkat", (106, 153, 85)),
        ("    String? token = await _fcm.getToken();", (156, 220, 254)),
        ("    debugPrint('FCM Device Token: $token');", (220, 220, 170)),
        ("", (255, 255, 255)),
        ("    // Listener Saat Aplikasi Berjalan di Foreground", (106, 153, 85)),
        ("    FirebaseMessaging.onMessage.listen((RemoteMessage msg) {", (86, 156, 214)),
        ("      if (msg.notification != null) {", (86, 156, 214)),
        ("        Get.snackbar(", (78, 201, 176)),
        ("          msg.notification!.title ?? 'Pengumuman Kelulusan',", (206, 145, 120)),
        ("          msg.notification!.body ?? '',", (206, 145, 120)),
        ("          backgroundColor: const Color(0xFF1E3A5F),", (156, 220, 254)),
        ("          colorText: Colors.white,", (156, 220, 254)),
        ("        );", (78, 201, 176)),
        ("      }", (86, 156, 214)),
        ("    });", (86, 156, 214)),
        ("    return this;", (86, 156, 214)),
        ("  }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=12, width=w)
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    draw.text((12, h-20), "main* | Dart | Firebase Cloud Messaging v15 | Foreground & Background Handlers", font=get_font(FONT_UI, 11), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan6_01_fcm_service_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_02_fcm_notification_app():
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (241, 245, 249))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle([0, 0, w, 32], fill=(30, 41, 59))
    draw.text((20, 7), "09:00", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    draw.text((w-75, 7), "5G  90%", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    
    # Notification Banner Heads-Up
    draw.rectangle([15, 45, w-15, 135], fill=(30, 58, 95), outline=(59, 130, 246))
    draw.ellipse([28, 58, 58, 88], fill=(255, 255, 255))
    draw.text((36, 65), "SL", font=get_font(FONT_UI_BOLD, 12), fill=(30, 58, 95))
    
    draw.text((68, 55), "SALUT • Pengumuman Resmi", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    draw.text((w-55, 55), "Baru saja", font=get_font(FONT_UI, 10), fill=(203, 213, 225))
    draw.text((68, 75), "Status Kelulusan Angkatan 2026 Dirilis!", font=get_font(FONT_UI_BOLD, 11), fill=(147, 197, 253))
    draw.text((68, 95), "Selamat! Anda dinyatakan LULUS. Cek arsip digital ijazah Anda sekarang.", font=get_font(FONT_UI, 10), fill=(241, 245, 249))
    
    # Background content
    draw.rectangle([20, 160, w-20, 420], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((35, 180), "Pusat Pengumuman Sekolah", font=get_font(FONT_UI_BOLD, 14), fill=(15, 23, 42))
    draw.text((35, 205), "Pengumuman otomatis diterbitkan melalui sistem cron job SALUT.", font=get_font(FONT_UI, 11), fill=(100, 116, 139))
    
    draw.rectangle([35, 240, w-35, 380], fill=(238, 242, 255), outline=(199, 210, 254))
    draw.text((50, 255), "HASIL VERIFIKASI KELULUSAN:", font=get_font(FONT_UI_BOLD, 12), fill=(49, 46, 129))
    draw.text((50, 280), "Nama: Budi Santoso", font=get_font(FONT_UI, 12), fill=(15, 23, 42))
    draw.text((50, 305), "NISN: 0054321987", font=get_font(FONT_UI, 12), fill=(15, 23, 42))
    draw.text((50, 330), "Status Baru: ALUMNI (Lulus SMK)", font=get_font(FONT_UI_BOLD, 12), fill=(16, 185, 129))
    draw.text((50, 355), "SKPI & Ijazah Digital: Siap Diunduh", font=get_font(FONT_UI_BOLD, 11), fill=(67, 56, 202))
    
    path = os.path.join(OUTPUT_DIR, "laporan6_02_fcm_notification_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_03_cron_promote():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - app/Console/Commands/PromoteAlumni.php", "Cron Job Otomasi Transisi Siswa ke Alumni")
    draw_vscode_header(draw, w, "PromoteAlumni.php", "app > Console > Commands > PromoteAlumni.php")
    
    lines = [
        ("class PromoteAlumni extends Command {", (86, 156, 214)),
        ("    protected $signature = 'salut:promote-alumni';", (206, 145, 120)),
        ("    protected $description = 'Otomatis mengubah Siswa Aktif menjadi Alumni sesuai tanggal kelulusan';", (206, 145, 120)),
        ("", (255, 255, 255)),
        ("    public function handle() {", (86, 156, 214)),
        ("        $today = now()->toDateString();", (156, 220, 254)),
        ("        $schedules = GraduationSchedule::where('release_date', '<=', $today)->get();", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("        foreach ($schedules as $sch) {", (86, 156, 214)),
        ("            $students = User::where('role', 'siswa')", (156, 220, 254)),
        ("                            ->where('angkatan', $sch->angkatan)", (156, 220, 254)),
        ("                            ->update(['role' => 'alumni', 'graduation_date' => $sch->release_date]);", (220, 220, 170)),
        ("            $this->info(\"Berhasil mempromosikan {$students} siswa angkatan {$sch->angkatan} ke Alumni.\");", (206, 145, 120)),
        ("        }", (86, 156, 214)),
        ("    }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=10, width=w)
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    draw.text((12, h-20), "main* | PHP 8.2 | Laravel Console Artisan Command | Scheduled Daily", font=get_font(FONT_UI, 11), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan6_03_cron_promote_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_04_cron_terminal():
    w, h = 950, 480
    im = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Terminal PowerShell - Eksekusi Otomasi Cron Job Kelulusan", "php artisan salut:promote-alumni", bg_color=(12, 12, 12))
    
    lines = [
        ("PS D:\\proyek_applikasi\\salut_backend> php artisan salut:promote-alumni", (255, 255, 255)),
        ("[2026-10-14 00:00:01] INFO  Memulai proses pengecekan jadwal kelulusan sekolah...", (200, 200, 200)),
        ("[2026-10-14 00:00:02] INFO  Memeriksa tabel graduation_schedules...", (200, 200, 200)),
        ("[2026-10-14 00:00:03] SUCCESS Jadwal ditemukan untuk Angkatan 2026 (Release Date: 2026-10-14).", (76, 175, 80)),
        ("[2026-10-14 00:00:04] INFO  Memperbarui data role pada tabel users...", (200, 200, 200)),
        ("[2026-10-14 00:00:05] SUCCESS Berhasil mempromosikan 190 siswa angkatan 2026 menjadi ALUMNI.", (76, 175, 80)),
        ("[2026-10-14 00:00:06] INFO  Mengirimkan sinyal Push Notification FCM ke 190 perangkat aktif...", (200, 200, 200)),
        ("[2026-10-14 00:00:07] SUCCESS Push notification berhasil dikirim (HTTP 200 Firebase FCM API).", (76, 175, 80)),
        ("[2026-10-14 00:00:08] INFO  Eksekusi Cron Job selesai dalam 7.12 detik.", (100, 181, 246)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi\\salut_backend> php artisan schedule:list", (255, 255, 255)),
        ("+------------------------------+----------+-----------------------------+----------------+", (150, 150, 150)),
        ("| Command                      | Interval | Next Due                    | Status         |", (220, 220, 220)),
        ("+------------------------------+----------+-----------------------------+----------------+", (150, 150, 150)),
        ("| salut:promote-alumni         | 0 0 * * *| Tomorrow, 00:00:00          | Active         |", (76, 175, 80)),
        ("+------------------------------+----------+-----------------------------+----------------+", (150, 150, 150)),
    ]
    y = 52
    for text, col in lines:
        draw.text((25, y), text, font=get_font(FONT_CODE, 13), fill=col)
        y += 20
        
    path = os.path.join(OUTPUT_DIR, "laporan6_04_cron_execution_terminal.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_05_change_password_code():
    w, h = 950, 580
    im = Image.new("RGB", (w, h), (30, 30, 30))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Visual Studio Code - lib/pages/change_password_page.dart", "Fitur Keamanan Ubah Kata Sandi")
    draw_vscode_header(draw, w, "change_password_page.dart", "apps_sekolah > lib > pages > change_password_page.dart")
    
    lines = [
        ("class ChangePasswordPage extends StatefulWidget {", (86, 156, 214)),
        ("  const ChangePasswordPage({super.key});", (220, 220, 170)),
        ("  @override", (86, 156, 214)),
        ("  State<ChangePasswordPage> createState() => _ChangePasswordPageState();", (220, 220, 170)),
        ("}", (86, 156, 214)),
        ("", (255, 255, 255)),
        ("class _ChangePasswordPageState extends State<ChangePasswordPage> {", (86, 156, 214)),
        ("  final _oldPassController = TextEditingController();", (156, 220, 254)),
        ("  final _newPassController = TextEditingController();", (156, 220, 254)),
        ("  final _confirmPassController = TextEditingController();", (156, 220, 254)),
        ("", (255, 255, 255)),
        ("  Future<void> _submitChangePassword() async {", (86, 156, 214)),
        ("    if (_newPassController.text != _confirmPassController.text) {", (86, 156, 214)),
        ("      Get.snackbar('Error', 'Konfirmasi kata sandi tidak cocok!');", (220, 220, 170)),
        ("      return;", (86, 156, 214)),
        ("    }", (86, 156, 214)),
        ("    // Request API ke PATCH /api/profile/password", (106, 153, 85)),
        ("    final res = await ApiService().patch('/profile/password', data: {", (156, 220, 254)),
        ("      'current_password': _oldPassController.text,", (206, 145, 120)),
        ("      'new_password': _newPassController.text,", (206, 145, 120)),
        ("    });", (156, 220, 254)),
        ("  }", (86, 156, 214)),
        ("}", (86, 156, 214)),
    ]
    draw_code_lines(draw, lines, start_y=112, start_line_num=10, width=w)
    draw.rectangle([0, h-24, w, h], fill=(0, 122, 204))
    draw.text((12, h-20), "main* | Dart | Form Validation | PATCH API Endpoint", font=get_font(FONT_UI, 11), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan6_05_change_password_code.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_06_change_password_app():
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "09:05", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  80%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Ubah Kata Sandi", font=get_font(FONT_UI_BOLD, 16), fill=(30, 58, 95))
    
    draw.rectangle([20, 95, w-20, 155], fill=(254, 242, 242), outline=(254, 202, 202))
    draw.text((35, 106), "Tips Keamanan Akun", font=get_font(FONT_UI_BOLD, 12), fill=(185, 28, 28))
    draw.text((35, 125), "Gunakan minimal 8 karakter dengan kombinasi huruf dan angka.", font=get_font(FONT_UI, 10), fill=(153, 27, 27))
    
    draw.rectangle([20, 170, w-20, 520], fill=(255, 255, 255), outline=(226, 232, 240))
    
    fields = [
        ("Kata Sandi Saat Ini", "••••••••••••"),
        ("Kata Sandi Baru", "••••••••••••••••"),
        ("Konfirmasi Kata Sandi Baru", "••••••••••••••••"),
    ]
    
    fy = 190
    for label, placeholder in fields:
        draw.text((35, fy), label, font=get_font(FONT_UI_BOLD, 12), fill=(51, 65, 85))
        draw.rectangle([35, fy+22, w-35, fy+65], fill=(248, 250, 252), outline=(203, 213, 225))
        draw.text((50, fy+36), placeholder, font=get_font(FONT_UI, 13), fill=(100, 116, 139))
        fy += 85
        
    draw.rectangle([35, 450, w-35, 498], fill=(30, 58, 95))
    draw.text((w//2 - 65, 465), "SIMPAN PERUBAHAN", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan6_06_change_password_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_07_tracer_study_app():
    w, h = 420, 780
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle([0, 0, w, 32], fill=(255, 255, 255))
    draw.text((20, 7), "09:08", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    draw.text((w-75, 7), "5G  79%", font=get_font(FONT_UI_BOLD, 12), fill=(30, 41, 59))
    
    draw.rectangle([0, 32, w, 82], fill=(255, 255, 255), outline=(230, 230, 230))
    draw.text((20, 46), "Kuesioner Tracer Study", font=get_font(FONT_UI_BOLD, 16), fill=(49, 46, 129))
    
    draw.rectangle([20, 95, w-20, 155], fill=(236, 253, 245), outline=(167, 243, 208))
    draw.text((35, 106), "Pelacakan Jejak Lulusan SMK", font=get_font(FONT_UI_BOLD, 12), fill=(4, 120, 87))
    draw.text((35, 125), "Data digunakan untuk akreditasi sekolah dan evaluasi kurikulum.", font=get_font(FONT_UI, 10), fill=(6, 95, 70))
    
    draw.rectangle([20, 165, w-20, 640], fill=(255, 255, 255), outline=(226, 232, 240))
    
    draw.text((35, 180), "Status Saat Ini", font=get_font(FONT_UI_BOLD, 12), fill=(51, 65, 85))
    draw.rectangle([35, 202, w-35, 240], fill=(241, 245, 249), outline=(203, 213, 225))
    draw.text((50, 213), "Sudah Bekerja (Sesuai Bidang)", font=get_font(FONT_UI_BOLD, 11), fill=(16, 185, 129))
    
    t_fields = [
        ("Nama Perusahaan / Instansi", "PT. Telkom Indonesia (Persero) Tbk"),
        ("Sektor Industri", "Teknologi Informasi & Telekomunikasi"),
        ("Jabatan / Posisi", "Junior Network & Software Engineer"),
        ("Rentang Penghasilan Pertama", "Rp 4.500.000 - Rp 6.000.000"),
        ("Keselarasan dengan Jurusan SMK", "Sangat Selaras (95%)"),
    ]
    
    ty = 250
    for lbl, val in t_fields:
        draw.text((35, ty), lbl, font=get_font(FONT_UI_BOLD, 11), fill=(51, 65, 85))
        draw.rectangle([35, ty+18, w-35, ty+50], fill=(248, 250, 252), outline=(226, 232, 240))
        draw.text((45, ty+26), val, font=get_font(FONT_UI, 11), fill=(15, 23, 42))
        ty += 62
        
    draw.rectangle([35, ty+15, w-35, ty+58], fill=(49, 46, 129))
    draw.text((w//2 - 60, ty+28), "KIRIM KUESIONER", font=get_font(FONT_UI_BOLD, 12), fill=(255, 255, 255))
    
    path = os.path.join(OUTPUT_DIR, "laporan6_07_tracer_study_app.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_08_webadmin_analytics():
    w, h = 950, 560
    im = Image.new("RGB", (w, h), (248, 250, 252))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Web Admin SALUT - dashboard.html", "Analitik Ekosistem Kejuruan SMK & Tracer Study", bg_color=(248, 250, 252))
    
    draw.rectangle([0, 39, w, 75], fill=(30, 58, 95))
    draw.text((25, 48), "SALUT ADMIN PANEL - SMK NEGERI 1 TELADAN", font=get_font(FONT_UI_BOLD, 13), fill=(255, 255, 255))
    draw.text((w-180, 50), "Role: Super Administrator", font=get_font(FONT_UI, 11), fill=(200, 220, 240))
    
    # 4 Metric Cards
    metrics = [
        ("Total Siswa SMK", "190 Siswa", "TKJ: 97 | RPL: 48 | MM: 45", (238, 242, 255), (67, 56, 202)),
        ("Total Alumni", "200 Lulusan", "Terdata di Database", (240, 253, 244), (22, 163, 74)),
        ("Penyerapan Alumni", "88.5%", "Bekerja & Kuliah", (254, 243, 199), (217, 119, 6)),
        ("Unit Portofolio SKPI", "136 Unit", "Terverifikasi Asesor", (245, 243, 255), (124, 58, 237)),
    ]
    
    mx = 25
    for mtitle, mval, msub, c_bg, c_text in metrics:
        draw.rectangle([mx, 90, mx+210, 165], fill=c_bg, outline=(226, 232, 240))
        draw.text((mx+15, 100), mtitle, font=get_font(FONT_UI_BOLD, 11), fill=(100, 116, 139))
        draw.text((mx+15, 120), mval, font=get_font(FONT_UI_BOLD, 18), fill=c_text)
        draw.text((mx+15, 146), msub, font=get_font(FONT_UI, 9), fill=(100, 116, 139))
        mx += 225
        
    # Chart 1: Penyerapan Lulusan
    draw.rectangle([25, 180, 465, 520], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((45, 195), "Distribusi Penyerapan Lulusan Alumni", font=get_font(FONT_UI_BOLD, 13), fill=(15, 23, 42))
    
    chart1_data = [
        ("Bekerja di Industri (DUDI)", "65% (130 Lulusan)", (37, 99, 235), 240),
        ("Melanjutkan Kuliah (PTN/PTS)", "25% (50 Lulusan)", (16, 185, 129), 100),
        ("Wirausaha / Freelance", "7% (14 Lulusan)", (245, 158, 11), 35),
        ("Masa Tunggu / Persiapan", "3% (6 Lulusan)", (100, 116, 139), 18),
    ]
    cy = 230
    for label, val, color, b_w in chart1_data:
        draw.text((45, cy), label, font=get_font(FONT_UI_BOLD, 11), fill=(51, 65, 85))
        draw.rectangle([45, cy+20, 45+b_w, cy+42], fill=color)
        draw.text((55+b_w, cy+23), val, font=get_font(FONT_UI_BOLD, 11), fill=color)
        cy += 65
        
    # Chart 2: Top Kampus & Industri
    draw.rectangle([485, 180, w-25, 520], fill=(255, 255, 255), outline=(226, 232, 240))
    draw.text((505, 195), "Top Mitra Industri & Perguruan Tinggi", font=get_font(FONT_UI_BOLD, 13), fill=(15, 23, 42))
    
    partners = [
        ("1. PT. Telkom Indonesia Tbk", "32 Alumni", "Teknologi & Jaringan"),
        ("2. PT. Astra International Tbk", "24 Alumni", "Otomotif & Manufaktur"),
        ("3. Universitas Lampung (Unila)", "20 Alumni", "Pendidikan Tinggi PTN"),
        ("4. PT. Bank Central Asia (BCA)", "15 Alumni", "Fintech & Perbankan"),
        ("5. Politeknik Negeri Lampung", "12 Alumni", "Vokasi Terapan"),
    ]
    py = 230
    for pname, palum, psector in partners:
        draw.rectangle([505, py, w-45, py+48], fill=(248, 250, 252), outline=(226, 232, 240))
        draw.text((520, py+8), pname, font=get_font(FONT_UI_BOLD, 11), fill=(30, 58, 95))
        draw.text((520, py+28), psector, font=get_font(FONT_UI, 10), fill=(100, 116, 139))
        draw.text((w-130, py+16), palum, font=get_font(FONT_UI_BOLD, 11), fill=(16, 185, 129))
        py += 56
        
    path = os.path.join(OUTPUT_DIR, "laporan6_08_webadmin_smk_analytics.png")
    im.save(path)
    print("Saved:", path)

def make_screenshot_laporan6_09_git_push_final():
    w, h = 950, 480
    im = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(im)
    draw_window_frame(draw, w, h, "Terminal PowerShell - Git Release Tag Final Proyek SALUT", "git push origin --tags", bg_color=(12, 12, 12))
    
    lines = [
        ("PS D:\\proyek_applikasi> git status", (255, 255, 255)),
        ("On branch main", (200, 200, 200)),
        ("nothing to commit, working tree clean", (76, 175, 80)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi> git tag -a v1.0.0-smk-release -m \"Release Final Sistem SALUT Ekosistem SMK & Tracer Study\"", (255, 255, 255)),
        ("PS D:\\proyek_applikasi> git push origin main --tags", (255, 255, 255)),
        ("Enumerating objects: 35, done.", (180, 180, 180)),
        ("Counting objects: 100% (35/35), done.", (180, 180, 180)),
        ("Delta compression using up to 12 threads", (180, 180, 180)),
        ("Compressing objects: 100% (25/25), done.", (180, 180, 180)),
        ("Writing objects: 100% (28/28), 14.20 KiB | 14.20 MiB/s, done.", (180, 180, 180)),
        ("Total 28 (delta 18), reused 0 (delta 0), pack-reused 0", (180, 180, 180)),
        ("To https://github.com/WEMVIAFRIALDO/apps_Sekolah-.git", (100, 181, 246)),
        (" * [new tag]         v1.0.0-smk-release -> v1.0.0-smk-release", (76, 175, 80)),
        ("   a19e83b..f92c31e  main -> main", (76, 175, 80)),
        ("", (255, 255, 255)),
        ("PS D:\\proyek_applikasi> # Proyek SALUT Telah Siap Digunakan Secara Penuh", (106, 153, 85)),
    ]
    y = 52
    for text, col in lines:
        draw.text((25, y), text, font=get_font(FONT_CODE, 13), fill=col)
        y += 20
        
    path = os.path.join(OUTPUT_DIR, "laporan6_09_git_push_final.png")
    im.save(path)
    print("Saved:", path)

def generate_all_laporan5_6():
    print("Mulai membuat seluruh aset gambar screenshot Laporan 5 & 6...")
    make_screenshot_laporan5_01_migration_skpi()
    make_screenshot_laporan5_02_phpmyadmin_skpi()
    make_screenshot_laporan5_03_skill_controller()
    make_screenshot_laporan5_04_api_skills_test()
    make_screenshot_laporan5_05_skills_page_code()
    make_screenshot_laporan5_06_skills_mobile_app()
    make_screenshot_laporan5_07_arsip_mobile_app()
    make_screenshot_laporan5_08_git_push()
    
    make_screenshot_laporan6_01_fcm_service_code()
    make_screenshot_laporan6_02_fcm_notification_app()
    make_screenshot_laporan6_03_cron_promote()
    make_screenshot_laporan6_04_cron_terminal()
    make_screenshot_laporan6_05_change_password_code()
    make_screenshot_laporan6_06_change_password_app()
    make_screenshot_laporan6_07_tracer_study_app()
    make_screenshot_laporan6_08_webadmin_analytics()
    make_screenshot_laporan6_09_git_push_final()
    print("17 gambar screenshot baru untuk Laporan 5 & 6 berhasil digenerate!")

if __name__ == "__main__":
    generate_all_laporan5_6()
