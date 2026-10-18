import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../routes/app_routes.dart';
import '../services/auth_service.dart';

/// Controller untuk halaman Profil.
/// Menampilkan biodata pengguna dan menangani aksi Logout secara aman.
class ProfileController extends GetxController {
  final _auth = AuthService();

  // ─── Data Profil (Dimuat dari AuthService & Storage) ────────────────────────
  var userName = 'Budi Santoso'.obs;
  var userNisn = '0054321987'.obs;
  var userEmail = 'budi.santoso@siswa.smkn1teladan.sch.id'.obs;
  var userPhone = '+62 812-3456-7890'.obs;
  var userSchool = 'SMK Negeri 1 Teladan'.obs;
  var userClass = 'XII TKJ 1'.obs;
  var userAngkatan = '2024'.obs;
  var userRole = 'Siswa'.obs; // nilai: 'Siswa' atau 'Alumni'
  var userJoinDate = '15 Juli 2021'.obs;

  @override
  void onInit() {
    super.onInit();
    _loadProfileFromStorage();
  }

  /// Membaca info pengguna dari storage yang disimpan saat login
  Future<void> _loadProfileFromStorage() async {
    final name = await _auth.getName();
    final nisn = await _auth.getNisn();
    final role = await _auth.getRole();

    if (name != null && name.isNotEmpty) userName.value = name;
    if (nisn != null && nisn.isNotEmpty) userNisn.value = nisn;
    if (role != null && role.isNotEmpty) {
      userRole.value = role.toLowerCase() == 'alumni' ? 'Alumni' : 'Siswa';
    }
  }

  // ─── Aksi ──────────────────────────────────────────────────────────────────

  /// Navigasi ke halaman Ubah Password
  void handleChangePassword() {
    Get.toNamed(AppRoutes.changePassword);
  }

  /// Logout: hapus token JWT & seluruh data sesi dari Android Keystore, lalu kembali ke Login
  Future<void> handleLogout() async {
    final confirmed = await Get.dialog<bool>(
      AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: const Text('Keluar dari Akun'),
        content: const Text(
          'Apakah Anda yakin ingin keluar? Token sesi Anda akan dihapus dari perangkat.',
        ),
        actions: [
          TextButton(
            onPressed: () => Get.back(result: false),
            child: const Text('Batal'),
          ),
          FilledButton(
            onPressed: () => Get.back(result: true),
            style: FilledButton.styleFrom(
              backgroundColor: const Color(0xFFDC2626),
            ),
            child: const Text('Ya, Keluar'),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      await _auth.clearSession();
      Get.offAllNamed(AppRoutes.login);
    }
  }
}
