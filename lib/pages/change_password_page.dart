import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/change_password_controller.dart';
import '../services/theme_service.dart';

/// Halaman Ubah Password: memungkinkan siswa dan alumni memperbarui kata sandi secara aman.
/// Terintegrasi dengan ThemeService (Mode Gelap & Mode Terang).
class ChangePasswordPage extends StatelessWidget {
  const ChangePasswordPage({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = Get.put(ChangePasswordController());
    final theme = ThemeService.to;

    return Obx(() {
      return Scaffold(
        backgroundColor: theme.bg,
        appBar: AppBar(
          title: Text(
            'Ubah Password',
            style: TextStyle(
              color: theme.textPrimary,
              fontWeight: FontWeight.bold,
              fontSize: 18,
            ),
          ),
          centerTitle: true,
          backgroundColor: theme.appBar,
          surfaceTintColor: Colors.transparent,
          elevation: 0,
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(1),
            child: Container(color: theme.border, height: 1),
          ),
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios_new_rounded, size: 20, color: theme.textPrimary),
            onPressed: () => Get.back(),
          ),
        ),
        body: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Demi keamanan akun Anda, pastikan password baru memiliki minimal 6 karakter kombinasi yang kuat.',
                  style: TextStyle(color: theme.textMuted, height: 1.5, fontSize: 13),
                ),
                const SizedBox(height: 24),
                Form(
                  key: controller.formKey,
                  child: Column(
                    children: [
                      // Password Saat Ini
                      GetBuilder<ChangePasswordController>(
                        builder: (c) => TextFormField(
                          obscureText: c.obscureCurrent,
                          style: TextStyle(color: theme.textPrimary, fontSize: 14),
                          decoration: InputDecoration(
                            labelText: 'Password Saat Ini',
                            labelStyle: TextStyle(color: theme.textMuted, fontSize: 13),
                            prefixIcon: Icon(Icons.lock_outline, color: theme.primary, size: 20),
                            suffixIcon: IconButton(
                              icon: Icon(
                                c.obscureCurrent ? Icons.visibility_off : Icons.visibility,
                                color: theme.textMuted,
                                size: 20,
                              ),
                              onPressed: c.toggleCurrent,
                            ),
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.border),
                            ),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.border),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.primary, width: 1.8),
                            ),
                            filled: true,
                            fillColor: theme.cardSubtle,
                            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                          ),
                          onChanged: (val) => c.currentPassword.value = val,
                          validator: (val) => val == null || val.isEmpty ? 'Masukkan password saat ini' : null,
                        ),
                      ),
                      const SizedBox(height: 16),

                      // Password Baru
                      GetBuilder<ChangePasswordController>(
                        builder: (c) => TextFormField(
                          obscureText: c.obscureNew,
                          style: TextStyle(color: theme.textPrimary, fontSize: 14),
                          decoration: InputDecoration(
                            labelText: 'Password Baru',
                            labelStyle: TextStyle(color: theme.textMuted, fontSize: 13),
                            prefixIcon: Icon(Icons.lock_reset, color: theme.primary, size: 20),
                            suffixIcon: IconButton(
                              icon: Icon(
                                c.obscureNew ? Icons.visibility_off : Icons.visibility,
                                color: theme.textMuted,
                                size: 20,
                              ),
                              onPressed: c.toggleNew,
                            ),
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.border),
                            ),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.border),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.primary, width: 1.8),
                            ),
                            filled: true,
                            fillColor: theme.cardSubtle,
                            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                          ),
                          onChanged: (val) => c.newPassword.value = val,
                          validator: (val) => val != null && val.length < 6 ? 'Minimal 6 karakter' : null,
                        ),
                      ),
                      const SizedBox(height: 16),

                      // Konfirmasi Password Baru
                      GetBuilder<ChangePasswordController>(
                        builder: (c) => TextFormField(
                          obscureText: c.obscureConfirm,
                          style: TextStyle(color: theme.textPrimary, fontSize: 14),
                          decoration: InputDecoration(
                            labelText: 'Konfirmasi Password Baru',
                            labelStyle: TextStyle(color: theme.textMuted, fontSize: 13),
                            prefixIcon: Icon(Icons.check_circle_outline, color: theme.primary, size: 20),
                            suffixIcon: IconButton(
                              icon: Icon(
                                c.obscureConfirm ? Icons.visibility_off : Icons.visibility,
                                color: theme.textMuted,
                                size: 20,
                              ),
                              onPressed: c.toggleConfirm,
                            ),
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.border),
                            ),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.border),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: BorderSide(color: theme.primary, width: 1.8),
                            ),
                            filled: true,
                            fillColor: theme.cardSubtle,
                            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                          ),
                          onChanged: (val) => c.confirmPassword.value = val,
                          validator: (val) => val != c.newPassword.value ? 'Password tidak cocok' : null,
                        ),
                      ),
                      const SizedBox(height: 32),

                      // Tombol Simpan
                      Obx(() => SizedBox(
                            width: double.infinity,
                            height: 52,
                            child: ElevatedButton.icon(
                              onPressed: controller.isLoading.value ? null : () => controller.submit(),
                              style: ElevatedButton.styleFrom(
                                backgroundColor: theme.primary,
                                foregroundColor: Colors.white,
                                elevation: 4,
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                              ),
                              icon: controller.isLoading.value
                                  ? const SizedBox(
                                      height: 20,
                                      width: 20,
                                      child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2),
                                    )
                                  : const Icon(Icons.check_rounded),
                              label: Text(
                                controller.isLoading.value ? 'Menyimpan...' : 'Simpan Password Baru',
                                style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                              ),
                            ),
                          )),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      );
    });
  }
}
