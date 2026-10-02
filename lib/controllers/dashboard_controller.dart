import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:open_filex/open_filex.dart';
import 'package:path_provider/path_provider.dart';
import 'package:permission_handler/permission_handler.dart';

import '../routes/app_routes.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';

class DashboardController extends GetxController {
  // Variabel statis sementara untuk peran pengguna (Dynamic UI)
  // Nilai yang didukung: 'Siswa' atau 'Alumni'
  var currentRole = 'Siswa'.obs;

  // Data profil dummy pengguna
  var userName = 'Budi Santoso'.obs;
  var userNisn = '0054321987'.obs;
  var userSchool = 'SMA Negeri 1 Teladan'.obs;
  var graduationYear = '2024'.obs;

  // Tab yang aktif jika menggunakan bottom navigation
  var selectedNavIndex = 0.obs;

  // Dummy data: Prestasi Siswa Aktif
  var achievements = <Map<String, dynamic>>[
    {
      'title': 'Juara 1 FLS2N Tingkat Provinsi',
      'year': '2023',
      'category': 'Seni & Budaya',
      'status': 'Approved',
    },
    {
      'title': 'Juara 2 Olimpiade Sains Nasional (OSN) Matematika',
      'year': '2023',
      'category': 'Akademik',
      'status': 'Pending',
    },
    {
      'title': 'Finalis Lomba Karya Tulis Ilmiah Nasional',
      'year': '2022',
      'category': 'Riset',
      'status': 'Approved',
    },
  ].obs;

  // Dummy data: Nilai Rapor Semester Siswa
  var semesterGrades = <Map<String, dynamic>>[
    {'semester': 'Semester 1', 'average': '88.5', 'rank': '3', 'status': 'Tervalidasi'},
    {'semester': 'Semester 2', 'average': '90.2', 'rank': '2', 'status': 'Tervalidasi'},
    {'semester': 'Semester 3', 'average': '89.8', 'rank': '2', 'status': 'Tervalidasi'},
    {'semester': 'Semester 4', 'average': '91.4', 'rank': '1', 'status': 'Tervalidasi'},
    {'semester': 'Semester 5', 'average': '92.0', 'rank': '1', 'status': 'Tervalidasi'},
  ].obs;

  // Dummy data: Arsip Digital Kelulusan Alumni
  var alumniArchives = <Map<String, dynamic>>[
    {
      'title': 'Ijazah Asli Digital',
      'type': 'PDF',
      'size': '2.4 MB',
      'status': 'Tersedia',
      'verified': true,
    },
    {
      'title': 'Surat Keterangan Hasil Ujian Nasional (SKHUN)',
      'type': 'PDF',
      'size': '1.8 MB',
      'status': 'Tersedia',
      'verified': true,
    },
    {
      'title': 'Surat Keterangan Lulus (SKL)',
      'type': 'PDF',
      'size': '1.1 MB',
      'status': 'Tersedia',
      'verified': true,
    },
    {
      'title': 'Transkrip Nilai Rapor Komprehensif (Sem 1 - 6)',
      'type': 'PDF',
      'size': '3.2 MB',
      'status': 'Tersedia',
      'verified': true,
    },
    {
      'title': 'Portofolio Prestasi Terverifikasi',
      'type': 'PDF',
      'size': '4.5 MB',
      'status': 'Tersedia',
      'verified': true,
    },
  ].obs;

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

  // Fungsi untuk mengganti role secara dinamis (memudahkan pengujian)
  void switchRole(String role) => currentRole.value = role;

  void toggleRole() {
    currentRole.value =
        currentRole.value == 'Siswa' ? 'Alumni' : 'Siswa';
  }

  // Aksi interaktif Siswa → navigasi ke halaman Input Prestasi
  void handleInputPrestasi() => Get.toNamed(AppRoutes.prestasi);

  // Aksi interaktif Alumni → navigasi ke halaman Tracer Study
  void handleOpenTracerStudy() => Get.toNamed(AppRoutes.tracer);

  // ─── Download Arsip Alumni dengan JWT Bearer Token ─────────────────────────
  /// REQ-NF-01: File bersifat private, HARUS menggunakan Bearer Token JWT.
  /// Proses:
  ///  1. Minta izin storage (Android 10+ pakai scoped storage).
  ///  2. Download via Dio dengan header `Authorization: Bearer <token>`.
  ///  3. Simpan ke folder Download lokal HP.
  ///  4. Buka file dengan open_filex.
  Future<void> handleDownloadDocument(String title) async {
    // 1. Cek & minta izin storage
    final status = await Permission.storage.request();
    if (!status.isGranted) {
      Get.snackbar(
        'Izin Ditolak',
        'Akses penyimpanan diperlukan untuk mengunduh dokumen.',
        backgroundColor: Colors.orange.shade800,
        colorText: Colors.white,
        snackPosition: SnackPosition.BOTTOM,
        margin: const EdgeInsets.all(16),
      );
      return;
    }

    // 2. Cari URL dokumen dari daftar arsip alumni
    final doc = alumniArchives.firstWhereOrNull((d) => d['title'] == title);
    // Gunakan URL dari data atau fallback ke endpoint API
    final fileUrl = doc?['file_url'] as String? ??
        '${ApiService().toString()}/arsip/$title';

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
      // 3. Tentukan lokasi simpan file
      final dir = await getApplicationDocumentsDirectory();
      final safeTitle = title.replaceAll(RegExp(r'[^\w\s]'), '_');
      final savePath  = '${dir.path}/$safeTitle.pdf';

      // 4. Download dengan progress tracking
      await _api.downloadFile(
        url: fileUrl,
        savePath: savePath,
        onProgress: (progress) {
          downloadProgress[title] = progress;
        },
      );

      downloadProgress.remove(title);
      Get.closeAllSnackbars();

      // 5. Buka file setelah download selesai
      final result = await OpenFilex.open(savePath);
      if (result.type != ResultType.done) {
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
    selectedNavIndex.value = index;
    switch (index) {
      case 0:
        // Sudah di dashboard, tidak perlu navigasi
        break;
      case 1:
        // Prestasi (Siswa) atau Arsip Digital (Alumni) – tetap di halaman ini untuk sekarang
        if (isSiswa) {
          Get.toNamed(AppRoutes.prestasi);
        }
        break;
      case 2:
        Get.toNamed(AppRoutes.profile);
        break;
    }
  }
}
