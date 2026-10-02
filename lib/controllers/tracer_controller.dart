import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../models/tracer_model.dart';
import '../services/api_service.dart';

/// REQ-F-08: Controller Form Dinamis Tracer Study untuk Alumni.
/// Jika status "Bekerja" dipilih → field Perusahaan & Jabatan muncul.
/// Jika status "Kuliah"   dipilih → field Nama Perguruan Tinggi & Prodi muncul.
/// Data dikirim ke endpoint API secara asinkron.
class TracerController extends GetxController {
  // ─── State Form ────────────────────────────────────────────────────────────
  final formKey = GlobalKey<FormState>();

  // Field selalu tampil
  final namaInstansiController  = TextEditingController();
  final kotaController           = TextEditingController();
  final tahunMasukController     = TextEditingController();
  final keteranganController     = TextEditingController();

  // Field kondisional "Bekerja"
  final jabatanController        = TextEditingController();

  // Field kondisional "Kuliah"
  final prodiController          = TextEditingController();

  /// Status aktivitas alumni pasca-lulus (Dynamic Form)
  var selectedStatus = ''.obs;
  final statusOptions = [
    'Bekerja',
    'Kuliah / Melanjutkan Studi',
    'Wirausaha',
    'Mencari Kerja',
    'Belum Memutuskan',
  ];

  var isLoading = false.obs;

  final _api = ApiService();

  // ─── Getter untuk memutuskan field mana yang tampil ────────────────────────
  bool get isBekerja   => selectedStatus.value == 'Bekerja' || selectedStatus.value == 'Wirausaha';
  bool get isKuliah    => selectedStatus.value == 'Kuliah / Melanjutkan Studi';

  // ─── Aksi ──────────────────────────────────────────────────────────────────
  Future<void> submitTracerStudy() async {
    if (!formKey.currentState!.validate()) return;
    if (selectedStatus.value.isEmpty) {
      Get.snackbar(
        'Perhatian',
        'Pilih status aktivitas Anda saat ini.',
        backgroundColor: Colors.orange.shade800,
        colorText: Colors.white,
        snackPosition: SnackPosition.BOTTOM,
      );
      return;
    }

    isLoading.value = true;

    try {
      // Buat model payload sesuai SRS
      final payload = TracerStudyModel(
        status:       selectedStatus.value,
        namaInstansi: namaInstansiController.text.trim(),
        kota:         kotaController.text.trim(),
        tahunMasuk:   tahunMasukController.text.trim(),
        jabatan:      jabatanController.text.trim(),
        prodi:        prodiController.text.trim(),
        keterangan:   keteranganController.text.trim(),
      );

      // POST /api/tracer-study (JWT Bearer Token otomatis via interceptor)
      await _api.post('/tracer-study', data: payload.toJson());

      Get.snackbar(
        '✅ Tracer Study Tersimpan!',
        'Data aktivitas pasca-lulus Anda berhasil disimpan.\nTerima kasih telah membantu almamater!',
        snackPosition: SnackPosition.BOTTOM,
        backgroundColor: Colors.indigo.shade900,
        colorText: Colors.white,
        margin: const EdgeInsets.all(16),
        borderRadius: 12,
        duration: const Duration(seconds: 4),
      );
      Get.back();
    } on DioException catch (e) {
      Get.snackbar(
        'Gagal Menyimpan',
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
    namaInstansiController.dispose();
    kotaController.dispose();
    tahunMasukController.dispose();
    keteranganController.dispose();
    jabatanController.dispose();
    prodiController.dispose();
    super.onClose();
  }
}
