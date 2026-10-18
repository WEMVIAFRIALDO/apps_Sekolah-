import 'package:dio/dio.dart';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart' hide FormData, MultipartFile;

import '../services/api_service.dart';
import '../services/theme_service.dart';
import 'dashboard_controller.dart';

/// REQ-F-03: Controller untuk halaman Input Prestasi Siswa.
/// Data prestasi dikirim ke API Laravel dengan multipart/form-data.
/// Status default setelah submit: "Pending" (menunggu validasi guru).
class PrestasiController extends GetxController {
  // ─── State Form ────────────────────────────────────────────────────────────
  final formKey = GlobalKey<FormState>();

  final namaKegiatanController  = TextEditingController();
  final penyelenggaraController  = TextEditingController();
  final tahunController          = TextEditingController();
  final deskripsiController      = TextEditingController();

  /// Tingkat: Kecamatan → Kota → Provinsi → Nasional → Internasional
  var selectedTingkat = ''.obs;
  final tingkatOptions = [
    'Kecamatan / Kabupaten',
    'Kota / Madya',
    'Provinsi',
    'Nasional',
    'Internasional',
  ];

  /// Peringkat yang diraih
  var selectedPeringkat = ''.obs;
  final peringkatOptions = [
    'Juara 1',
    'Juara 2',
    'Juara 3',
    'Finalis',
    'Harapan 1',
    'Harapan 2',
    'Harapan 3',
    'Peserta',
  ];

  /// File sertifikat yang dipilih dari perangkat
  var selectedFileName = ''.obs;
  var selectedFilePath = ''.obs; // Path absolut file di device
  var isLoading = false.obs;

  final _api = ApiService();

  // ─── Aksi: Pilih File Sertifikat ───────────────────────────────────────────

  /// REQ-F-03: Membuka file picker → pilih PDF atau gambar sertifikat.
  /// Mendukung format: PDF, JPG, PNG. Maks. 5 MB.
  Future<void> pickCertificate() async {
    try {
      // file_picker v13: pickFiles adalah static method, return List<PlatformFile>
      final files = await FilePicker.pickFiles(
        type: FileType.custom,
        allowedExtensions: ['pdf', 'jpg', 'jpeg', 'png'],
      );

      if (files.isEmpty) return; // User membatalkan

      final file = files.first;

      // Validasi ukuran file (maks 5 MB)
      final sizeBytes = file.lengthSync() ?? await file.length() ?? 0;
      final fileSizeInMB = (sizeBytes / (1024 * 1024));
      if (fileSizeInMB > 5) {
        Get.snackbar(
          'File Terlalu Besar',
          'Ukuran file maksimal 5 MB. File Anda: ${fileSizeInMB.toStringAsFixed(1)} MB',
          backgroundColor: Colors.orange.shade800,
          colorText: Colors.white,
          snackPosition: SnackPosition.BOTTOM,
          margin: const EdgeInsets.all(16),
          borderRadius: 12,
        );
        return;
      }

      selectedFileName.value = file.name;
      selectedFilePath.value = file.path ?? '';

      Get.snackbar(
        '✅ File Dipilih',
        '"${file.name}" (${fileSizeInMB.toStringAsFixed(1)} MB) siap diunggah.',
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: Colors.green.shade800,
        colorText: Colors.white,
        margin: const EdgeInsets.all(16),
        borderRadius: 12,
        icon: const Icon(Icons.attach_file_rounded, color: Colors.white),
      );
    } catch (e) {
      Get.snackbar(
        'Gagal Memilih File',
        'Terjadi kesalahan: $e',
        backgroundColor: Colors.red.shade800,
        colorText: Colors.white,
        snackPosition: SnackPosition.BOTTOM,
      );
    }
  }

  // ─── Aksi: Submit Prestasi ke API ──────────────────────────────────────────

  /// Mengirim data prestasi ke POST /api/prestasi menggunakan
  /// multipart/form-data agar file sertifikat ikut terupload.
  /// JWT Bearer Token disisipkan otomatis oleh ApiService interceptor.
  Future<void> submitPrestasi() async {
    if (!formKey.currentState!.validate()) return;

    if (selectedTingkat.value.isEmpty) {
      Get.snackbar('Perhatian', 'Pilih tingkat kejuaraan.',
          backgroundColor: Colors.orange.shade800,
          colorText: Colors.white,
          snackPosition: SnackPosition.BOTTOM);
      return;
    }
    if (selectedPeringkat.value.isEmpty) {
      Get.snackbar('Perhatian', 'Pilih peringkat yang diraih.',
          backgroundColor: Colors.orange.shade800,
          colorText: Colors.white,
          snackPosition: SnackPosition.BOTTOM);
      return;
    }
    if (selectedFilePath.value.isEmpty) {
      Get.snackbar('Perhatian', 'Unggah sertifikat terlebih dahulu.',
          backgroundColor: Colors.orange.shade800,
          colorText: Colors.white,
          snackPosition: SnackPosition.BOTTOM);
      return;
    }

    isLoading.value = true;

    try {
      // Buat FormData dengan file sertifikat
      final formData = FormData.fromMap({
        'nama_kegiatan':  namaKegiatanController.text.trim(),
        'penyelenggara':  penyelenggaraController.text.trim(),
        'tingkat':        selectedTingkat.value,
        'peringkat':      selectedPeringkat.value,
        'tahun':          tahunController.text.trim(),
        'deskripsi':      deskripsiController.text.trim(),
        'status_validasi': 'Pending',
        // File sertifikat dikirim sebagai multipart
        'sertifikat': await MultipartFile.fromFile(
          selectedFilePath.value,
          filename: selectedFileName.value,
        ),
      });

      // POST /api/prestasi (JWT otomatis disertakan oleh interceptor)
      await _api.postMultipart('/prestasi', formData: formData);

      final namaKegiatan = namaKegiatanController.text.trim();
      final tingkat = selectedTingkat.value;
      final peringkat = selectedPeringkat.value;
      final tahun = tahunController.text.trim();

      // Tampilkan Pop-Up Dialog Konfirmasi yang Jelas & Elegan
      _showSuccessDialog(
        namaKegiatan: namaKegiatan,
        tingkat: tingkat,
        peringkat: peringkat,
        tahun: tahun,
      );
    } on DioException catch (e) {
      Get.snackbar(
        'Gagal Mengirim',
        ApiService.parseError(e),
        backgroundColor: Colors.red.shade800,
        colorText: Colors.white,
        snackPosition: SnackPosition.BOTTOM,
        margin: const EdgeInsets.all(16),
      );
    } finally {
      isLoading.value = false;
    }
  }

  /// Menampilkan Pop-Up Modal Konfirmasi Pengajuan Prestasi Berhasil
  void _showSuccessDialog({
    required String namaKegiatan,
    required String tingkat,
    required String peringkat,
    required String tahun,
  }) {
    final theme = Get.find<ThemeService>();

    Get.dialog(
      Dialog(
        backgroundColor: Colors.transparent,
        insetPadding: const EdgeInsets.symmetric(horizontal: 24, vertical: 24),
        child: Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: theme.card,
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: theme.border),
            boxShadow: theme.cardShadow,
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Ikon Trofi / Centang Sukses dengan Glow
              Container(
                width: 72,
                height: 72,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: const LinearGradient(
                    colors: [Color(0xFF10B981), Color(0xFF059669)],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF10B981).withValues(alpha: 0.35),
                      blurRadius: 18,
                      offset: const Offset(0, 6),
                    ),
                  ],
                ),
                child: const Icon(
                  Icons.check_rounded,
                  size: 40,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 18),

              // Judul Dialog
              Text(
                'Prestasi Berhasil Dikirim!',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 19,
                  fontWeight: FontWeight.bold,
                  color: theme.textPrimary,
                ),
              ),
              const SizedBox(height: 8),

              // Penjelasan Status Pending
              Text(
                'Pengajuan prestasi Anda telah berhasil diunggah ke server dan sedang menunggu validasi oleh Guru Pembina.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 13,
                  color: theme.textMuted,
                  height: 1.4,
                ),
              ),
              const SizedBox(height: 16),

              // Kartu Ringkasan Pengajuan
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: theme.cardSubtle,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: theme.border),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      namaKegiatan,
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w700,
                        color: theme.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 6),
                    Row(
                      children: [
                        Icon(Icons.emoji_events_outlined, size: 14, color: theme.primary),
                        const SizedBox(width: 5),
                        Text(
                          '$peringkat • $tingkat',
                          style: TextStyle(fontSize: 12, color: theme.textMuted),
                        ),
                      ],
                    ),
                    const SizedBox(height: 4),
                    Row(
                      children: [
                        Icon(Icons.calendar_today_outlined, size: 14, color: theme.primary),
                        const SizedBox(width: 5),
                        Text(
                          'Tahun $tahun',
                          style: TextStyle(fontSize: 12, color: theme.textMuted),
                        ),
                        const Spacer(),
                        // Status Badge Pending
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                          decoration: BoxDecoration(
                            color: Colors.amber.withValues(alpha: 0.15),
                            borderRadius: BorderRadius.circular(6),
                            border: Border.all(color: Colors.amber.withValues(alpha: 0.4)),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(Icons.access_time_rounded, size: 11, color: Colors.amber.shade500),
                              const SizedBox(width: 4),
                              Text(
                                'Pending',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.amber.shade500,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 22),

              // Tombol Konfirmasi "Kembali ke Beranda"
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: () {
                    // 1. Tutup modal dialog
                    Get.back();
                    // 2. Tutup form prestasi (kembali ke dashboard)
                    Get.back();
                    // 3. Reset form
                    clearForm();
                    // 4. Trigger pembaruan data riwayat prestasi di dashboard
                    if (Get.isRegistered<DashboardController>()) {
                      Get.find<DashboardController>().fetchAchievements();
                    }
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: theme.primary,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 14),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(14),
                    ),
                    elevation: 3,
                  ),
                  child: const Text(
                    'Lihat di Beranda',
                    style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
      barrierDismissible: false,
    );
  }

  /// Reset seluruh input pada form pengajuan prestasi
  void clearForm() {
    namaKegiatanController.clear();
    penyelenggaraController.clear();
    tahunController.clear();
    deskripsiController.clear();
    selectedTingkat.value = '';
    selectedPeringkat.value = '';
    selectedFileName.value = '';
    selectedFilePath.value = '';
  }

  @override
  void onClose() {
    namaKegiatanController.dispose();
    penyelenggaraController.dispose();
    tahunController.dispose();
    deskripsiController.dispose();
    super.onClose();
  }
}
