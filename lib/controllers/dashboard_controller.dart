import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../routes/app_routes.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import '../services/file_saver.dart';
import '../services/theme_service.dart';

class DashboardController extends GetxController {
  final themeService = ThemeService.to;
  // Variabel statis sementara untuk peran pengguna (Dynamic UI)
  // Nilai yang didukung: 'Siswa' atau 'Alumni'
  var currentRole = 'Siswa'.obs;

  // Data profil dummy pengguna
  var userName = 'Budi Santoso'.obs;
  var userNisn = '0054321987'.obs;
  var userSchool = 'SMK Negeri 1 Teladan'.obs;
  var graduationYear = '2024'.obs;

  // Tab yang aktif jika menggunakan bottom navigation
  var selectedNavIndex = 0.obs;

  // Data Prestasi Siswa Aktif (Dinamis dari Backend Laravel)
  var achievements = <Map<String, dynamic>>[].obs;
  var isLoadingAchievements = false.obs;

  // Nilai Rapor Semester Siswa (Dinamis dari GET /api/rapor/my, diinput Guru)
  var semesterGrades = <Map<String, dynamic>>[].obs;

  // Arsip Digital Kelulusan Alumni (Dinamis dari GET /api/arsip, diunggah Admin)
  var alumniArchives = <Map<String, dynamic>>[].obs;

  // Status pengisian Tracer Study bagi Alumni
  var hasCompletedTracerStudy = false.obs;

  // Download progress per dokumen (key: title)
  var downloadProgress = <String, double>{}.obs;

  final _api  = ApiService();
  final _auth = AuthService();

  // Getter pembantu untuk pengecekan role
  bool get isSiswa  => currentRole.value == 'Siswa';
  bool get isAlumni => currentRole.value == 'Alumni';

  // ─── Inisialisasi: Load data real dari API saat Dashboard dibuka ───────────
  @override
  void onInit() {
    super.onInit();
    _loadUserProfile();
    fetchAchievements();
    fetchSemesterGrades();
    fetchAlumniArchives();
  }

  /// Mengambil nilai rapor per semester milik user login (GET /api/rapor/my)
  Future<void> fetchSemesterGrades() async {
    try {
      final response = await _api.get('/rapor/my');
      final List data = response.data['data'] ?? [];
      semesterGrades.assignAll(data.map<Map<String, dynamic>>((r) => {
            'semester': 'Semester ${r['semester']}',
            'average': (r['average_score'] ?? '-').toString(),
            'rank': (r['rank'] ?? '-').toString(),
            'status': (r['status'] ?? 'Draft').toString(),
          }));
    } catch (e) {
      debugPrint('Error fetchSemesterGrades: $e');
    }
  }

  /// Mengambil daftar arsip kelulusan milik alumni login (GET /api/arsip)
  Future<void> fetchAlumniArchives() async {
    try {
      final response = await _api.get('/arsip');
      final List data = response.data['data'] ?? [];
      alumniArchives.assignAll(data.map<Map<String, dynamic>>((d) => {
            'id': d['id'],
            'title': (d['title'] ?? '').toString(),
            'doc_type': (d['doc_type'] ?? 'dokumen').toString(),
            'type': (d['type'] ?? 'PDF').toString(),
            'size': (d['file_size'] ?? '-').toString(),
            'verified': d['is_verified'] == true || d['is_verified'] == 1,
          }));
    } catch (e) {
      debugPrint('Error fetchAlumniArchives: $e');
    }
  }

  /// Mengambil riwayat prestasi siswa dari backend Laravel (GET /api/prestasi)
  Future<void> fetchAchievements() async {
    try {
      isLoadingAchievements.value = true;
      final response = await _api.get('/prestasi');
      if (response.statusCode == 200 && response.data['success'] == true) {
        final List data = response.data['data'] ?? [];
        final mapped = data.map<Map<String, dynamic>>((a) {
          final tingkat = (a['tingkat'] ?? '').toString();
          final peringkat = (a['peringkat'] ?? '').toString();
          return {
            'id': a['id'],
            'title': (a['nama_kegiatan'] ?? '').toString(),
            'year': (a['tahun'] ?? '').toString(),
            'category': tingkat.isNotEmpty && peringkat.isNotEmpty
                ? '$tingkat • $peringkat'
                : (tingkat.isNotEmpty ? tingkat : peringkat),
            'tingkat': tingkat,
            'peringkat': peringkat,
            'status': (a['status_validasi'] ?? 'Pending').toString(),
            'penyelenggara': (a['penyelenggara'] ?? '').toString(),
            'deskripsi': (a['deskripsi'] ?? '').toString(),
            'catatan': (a['catatan'] ?? '').toString(),
            'created_at': (a['created_at'] ?? '').toString(),
          };
        }).toList();
        achievements.assignAll(mapped);
      }
    } catch (e) {
      debugPrint('Error fetchAchievements: $e');
    } finally {
      isLoadingAchievements.value = false;
    }
  }

  /// Load nama & NISN dari secure storage (sudah disimpan saat login)
  Future<void> _loadUserProfile() async {
    final name = await _auth.getName();
    final nisn = await _auth.getNisn();
    final role = await _auth.getRole();

    if (name != null) userName.value  = name;
    if (nisn != null) userNisn.value  = nisn;
    if (role != null) {
      // Normalisasi role dari API ('siswa'/'alumni') ke label tampilan
      currentRole.value =
          role.toLowerCase() == 'alumni' ? 'Alumni' : 'Siswa';
    }
  }

  // Aksi interaktif Siswa → navigasi ke halaman Input Prestasi
  void handleInputPrestasi() => Get.toNamed(AppRoutes.prestasi);

  // Aksi interaktif Alumni → navigasi ke halaman Tracer Study
  void handleOpenTracerStudy() => Get.toNamed(AppRoutes.tracer);

  // ─── Download Arsip Alumni dengan JWT Bearer Token ─────────────────────────
  /// REQ-NF-01: File bersifat private, HARUS menggunakan Bearer Token JWT.
  /// Proses:
  ///  1. Download via Dio dengan header `Authorization: Bearer <token>`.
  ///  2. Simpan ke folder dokumen aplikasi (tanpa izin storage) / unduhan browser.
  ///  3. Buka file dengan open_filex.
  Future<void> handleDownloadDocument(String title) async {
    final doc = alumniArchives.firstWhereOrNull((d) => d['title'] == title);
    if (doc == null) return;
    final id = doc['id'];

    // Tandai sedang mengunduh
    downloadProgress[title] = 0.0;

    Get.snackbar(
      '⬇️ Mengunduh...',
      'Sedang mengunduh "$title" dengan autentikasi JWT...',
      snackPosition: SnackPosition.BOTTOM,
      backgroundColor: Colors.grey.shade900,
      colorText: Colors.white,
      margin: const EdgeInsets.all(16),
      borderRadius: 12,
      duration: const Duration(seconds: 60), // Akan ditutup saat selesai
    );

    try {
      // Download dengan progress tracking
      final bytes = await _api.downloadBytes(
        '/arsip/$id/download',
        onProgress: (progress) {
          downloadProgress[title] = progress;
        },
      );

      downloadProgress.remove(title);
      Get.closeAllSnackbars();

      // Simpan lalu buka file setelah download selesai
      final safeTitle = title.replaceAll(RegExp(r'[^\w\s]'), '_');
      final savedPath = await saveAndOpenFile(bytes, '$safeTitle.pdf');
      if (savedPath != null) {
        Get.snackbar(
          '✅ Tersimpan',
          '"$title" berhasil diunduh ke penyimpanan lokal.',
          backgroundColor: Colors.green.shade800,
          colorText: Colors.white,
          snackPosition: SnackPosition.BOTTOM,
          margin: const EdgeInsets.all(16),
          borderRadius: 12,
        );
      }
    } catch (e) {
      downloadProgress.remove(title);
      Get.closeAllSnackbars();
      Get.snackbar(
        'Gagal Mengunduh',
        ApiService.parseError(e),
        backgroundColor: Colors.red.shade800,
        colorText: Colors.white,
        snackPosition: SnackPosition.BOTTOM,
        margin: const EdgeInsets.all(16),
      );
    }
  }

  // Navigasi bottom nav
  void handleNavTap(int index) {
    // Tab 1 & 2 membuka halaman baru, jadi sorotan tetap di Beranda
    switch (index) {
      case 0:
        // Sudah di dashboard, tidak perlu navigasi
        break;
      case 1:
        // Prestasi (Siswa) atau Arsip Digital (Alumni)
        Get.toNamed(isSiswa ? AppRoutes.prestasi : AppRoutes.arsip);
        break;
      case 2:
        Get.toNamed(AppRoutes.profile);
        break;
    }
  }
}
