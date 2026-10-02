import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../routes/app_routes.dart';

/// Controller untuk halaman Profil.
/// Menampilkan biodata pengguna dan menangani aksi Logout.
class ProfileController extends GetxController {
  // ─── Dummy Data Profil (akan diganti dari JWT payload / SharedPreferences) ──
  var userName = 'Budi Santoso'.obs;
  var userNisn = '0054321987'.obs;
  var userEmail = 'budi.santoso@siswa.sman1teladan.sch.id'.obs;
  var userPhone = '+62 812-3456-7890'.obs;
  var userSchool = 'SMA Negeri 1 Teladan'.obs;
  var userClass = 'XII IPA 3'.obs;
  var userAngkatan = '2024'.obs;
  var userRole = 'Siswa'.obs; // nilai: 'Siswa' atau 'Alumni'
  var userJoinDate = '15 Juli 2021'.obs;

  // ─── Aksi ──────────────────────────────────────────────────────────────────

  /// Ganti password (placeholder – arahkan ke halaman terpisah nantinya)
  void handleChangePassword() {
    Get.snackbar(
      'Ubah Password',
      'Fitur ini akan aktif saat backend Laravel terhubung.',
      snackPosition: SnackPosition.BOTTOM,
    );
  }

  /// Logout: hapus token dan kembali ke halaman Login
  Future<void> handleLogout() async {
    final confirmed = await Get.dialog<bool>(
      AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: const Text('Keluar dari Akun'),
        content: const Text(
          'Apakah Anda yakin ingin keluar? Token sesi Anda akan dihapus.',
        ),
        actions: [
          TextButton(
            onPressed: () => Get.back(result: false),
            child: const Text('Batal'),
          ),
          FilledButton(
            onPressed: () => Get.back(result: true),
            style: FilledButton.styleFrom(
              backgroundColor: const Color(0xFF1E3A5F),
            ),
            child: const Text('Ya, Keluar'),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      // TODO: Hapus JWT dari SharedPreferences / FlutterSecureStorage
      // await storage.delete(key: 'jwt_token');
      Get.offAllNamed(AppRoutes.login);
    }
  }
}
