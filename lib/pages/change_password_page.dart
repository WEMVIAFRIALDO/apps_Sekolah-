import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/change_password_controller.dart';

class ChangePasswordPage extends StatelessWidget {
  const ChangePasswordPage({super.key});

  @override
  Widget build(BuildContext context) {
    // Inject Controller jika belum ada
    final controller = Get.put(ChangePasswordController());

    return Scaffold(
      backgroundColor: const Color(0xFFF3F4F6),
      appBar: AppBar(
        title: const Text(
          'Ubah Password',
          style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 18),
        ),
        backgroundColor: const Color(0xFF1E3A5F),
        iconTheme: const IconThemeData(color: Colors.white),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Demi keamanan akun Anda, pastikan password baru memiliki minimal 6 karakter.',
                style: TextStyle(color: Colors.black54, height: 1.5),
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
                        decoration: InputDecoration(
                          labelText: 'Password Saat Ini',
                          prefixIcon: const Icon(Icons.lock_outline),
                          suffixIcon: IconButton(
                            icon: Icon(c.obscureCurrent ? Icons.visibility_off : Icons.visibility),
                            onPressed: c.toggleCurrent,
                          ),
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                          filled: true,
                          fillColor: Colors.white,
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
                        decoration: InputDecoration(
                          labelText: 'Password Baru',
                          prefixIcon: const Icon(Icons.lock_reset),
                          suffixIcon: IconButton(
                            icon: Icon(c.obscureNew ? Icons.visibility_off : Icons.visibility),
                            onPressed: c.toggleNew,
                          ),
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                          filled: true,
                          fillColor: Colors.white,
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
                        decoration: InputDecoration(
                          labelText: 'Konfirmasi Password Baru',
                          prefixIcon: const Icon(Icons.check_circle_outline),
                          suffixIcon: IconButton(
                            icon: Icon(c.obscureConfirm ? Icons.visibility_off : Icons.visibility),
                            onPressed: c.toggleConfirm,
                          ),
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                          filled: true,
                          fillColor: Colors.white,
                        ),
                        onChanged: (val) => c.confirmPassword.value = val,
                        validator: (val) => val != c.newPassword.value ? 'Password tidak cocok' : null,
                      ),
                    ),
                    const SizedBox(height: 32),

                    // Tombol Simpan
                    Obx(() => SizedBox(
                      width: double.infinity,
                      height: 50,
                      child: FilledButton(
                        onPressed: controller.isLoading.value ? null : () => controller.submit(),
                        style: FilledButton.styleFrom(
                          backgroundColor: const Color(0xFF10B981),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
                        child: controller.isLoading.value
                            ? const SizedBox(height: 20, width: 20, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
                            : const Text('Simpan Password', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
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
  }
}
