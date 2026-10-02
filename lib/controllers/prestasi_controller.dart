import 'package:dio/dio.dart';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart' hide FormData, MultipartFile;

import '../services/api_service.dart';

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
      final result = await FilePicker.platform.pickFiles(
        type: FileType.custom,
        allowedExtensions: ['pdf', 'jpg', 'jpeg', 'png'],
        allowMultiple: false,
      );

      if (result == null || result.files.isEmpty) return; // User membatalkan

      final file = result.files.first;

      // Validasi ukuran file (maks 5 MB)
      final fileSizeInMB = (file.size / (1024 * 1024));
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

      Get.snackbar(
        '🎉 Prestasi Terkirim!',
        '"${namaKegiatanController.text}" berhasil dikirim.\nMenunggu validasi Guru Pembina.',
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: Colors.blue.shade900,
        colorText: Colors.white,
        margin: const EdgeInsets.all(16),
        borderRadius: 12,
        duration: const Duration(seconds: 4),
      );
      Get.back();
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

  @override
  void onClose() {
    namaKegiatanController.dispose();
    penyelenggaraController.dispose();
    tahunController.dispose();
    deskripsiController.dispose();
    super.onClose();
  }
}
