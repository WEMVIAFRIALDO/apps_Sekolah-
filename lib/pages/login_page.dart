import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:dio/dio.dart';

import '../routes/app_routes.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _nisnController     = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final _formKey = GlobalKey<FormState>();

  bool _obscurePassword = true;
  bool _isLoading       = false;

  final _api  = ApiService();
  final _auth = AuthService();

  // ─── Logic: Login dengan JWT ───────────────────────────────────────────────
  Future<void> _handleLogin() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      // POST /api/login → { token, user: { id, name, nisn, role, ... } }
      final response = await _api.post(
        '/login',
        data: {
          'nisn':     _nisnController.text.trim(),
          'password': _passwordController.text,
        },
      );

      final data  = response.data as Map<String, dynamic>;
      final token = data['token'] as String;
      final user  = data['user']  as Map<String, dynamic>;

      // Simpan token JWT ke Android Keystore (aman)
      await _auth.saveToken(token);
      await _auth.saveUserInfo(
        role:   user['role']   as String,
        nisn:   user['nisn']   as String,
        name:   user['name']   as String,
        userId: user['id'].toString(),
      );

      // Navigasi ke Dashboard (replace stack agar tidak bisa back ke login)
      Get.offAllNamed(AppRoutes.dashboard);

    } on DioException catch (e) {
      final msg = ApiService.parseError(e);
      Get.snackbar(
        'Login Gagal',
        msg,
        backgroundColor: Colors.red.shade800,
        colorText:        Colors.white,
        snackPosition:    SnackPosition.TOP,
        margin:           const EdgeInsets.all(16),
        borderRadius:     12,
        icon:             const Icon(Icons.error_outline, color: Colors.white),
      );
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  void dispose() {
    _nisnController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF0F4FF),
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 24),
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // ── Logo & Branding ───────────────────────────────────────
                  Center(
                    child: Container(
                      padding: const EdgeInsets.all(22),
                      decoration: BoxDecoration(
                        color: const Color(0xFF1E3A5F),
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF1E3A5F).withValues(alpha: 0.3),
                            blurRadius: 24,
                            offset: const Offset(0, 10),
                          ),
                        ],
                      ),
                      child: const Icon(
                        Icons.school_rounded,
                        size: 64,
                        color: Colors.white,
                      ),
                    ),
                  ),
                  const SizedBox(height: 28),

                  const Text(
                    'SALUT',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 32,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 4,
                      color: Color(0xFF1E3A5F),
                    ),
                  ),
                  const SizedBox(height: 6),
                  const Text(
                    'Sistem Arsip Lulusan & Tracer Study',
                    textAlign: TextAlign.center,
                    style: TextStyle(fontSize: 14, color: Colors.grey),
                  ),
                  const SizedBox(height: 40),

                  // ── Form Card ─────────────────────────────────────────────
                  Container(
                    padding: const EdgeInsets.all(24),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withValues(alpha: 0.06),
                          blurRadius: 24,
                          offset: const Offset(0, 8),
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'Masuk ke Akun',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Color(0xFF1E293B),
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          'Gunakan NISN dan password Anda',
                          style:
                              TextStyle(fontSize: 13, color: Colors.grey.shade500),
                        ),
                        const SizedBox(height: 24),

                        // Input NISN
                        TextFormField(
                          controller: _nisnController,
                          keyboardType: TextInputType.number,
                          maxLength: 10,
                          validator: (v) {
                            if (v == null || v.isEmpty) return 'NISN wajib diisi';
                            if (v.length < 10) return 'NISN harus 10 digit';
                            return null;
                          },
                          decoration: InputDecoration(
                            labelText: 'NISN',
                            hintText: 'Masukkan 10 digit NISN',
                            prefixIcon: const Icon(Icons.badge_outlined),
                            counterText: '',
                            filled: true,
                            fillColor: Colors.grey.shade50,
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(12)),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide:
                                  BorderSide(color: Colors.grey.shade300),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: const BorderSide(
                                  color: Color(0xFF1E3A5F), width: 1.8),
                            ),
                          ),
                        ),
                        const SizedBox(height: 16),

                        // Input Password
                        TextFormField(
                          controller: _passwordController,
                          obscureText: _obscurePassword,
                          validator: (v) {
                            if (v == null || v.isEmpty) {
                              return 'Password wajib diisi';
                            }
                            if (v.length < 6) {
                              return 'Password minimal 6 karakter';
                            }
                            return null;
                          },
                          decoration: InputDecoration(
                            labelText: 'Password',
                            prefixIcon:
                                const Icon(Icons.lock_outline_rounded),
                            suffixIcon: IconButton(
                              icon: Icon(
                                _obscurePassword
                                    ? Icons.visibility_off_outlined
                                    : Icons.visibility_outlined,
                              ),
                              onPressed: () => setState(
                                  () => _obscurePassword = !_obscurePassword),
                            ),
                            filled: true,
                            fillColor: Colors.grey.shade50,
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(12)),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide:
                                  BorderSide(color: Colors.grey.shade300),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(12),
                              borderSide: const BorderSide(
                                  color: Color(0xFF1E3A5F), width: 1.8),
                            ),
                          ),
                        ),
                        const SizedBox(height: 28),

                        // Tombol Masuk
                        SizedBox(
                          width: double.infinity,
                          height: 52,
                          child: FilledButton(
                            onPressed: _isLoading ? null : _handleLogin,
                            style: FilledButton.styleFrom(
                              backgroundColor: const Color(0xFF1E3A5F),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(14),
                              ),
                            ),
                            child: _isLoading
                                ? const SizedBox(
                                    width: 22,
                                    height: 22,
                                    child: CircularProgressIndicator(
                                        color: Colors.white,
                                        strokeWidth: 2.5),
                                  )
                                : const Text(
                                    'Masuk',
                                    style: TextStyle(
                                      fontSize: 16,
                                      fontWeight: FontWeight.bold,
                                      letterSpacing: 0.5,
                                    ),
                                  ),
                          ),
                        ),
                      ],
                    ),
                  ),

                  const SizedBox(height: 24),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.lock_rounded,
                          size: 14, color: Colors.grey.shade400),
                      const SizedBox(width: 6),
                      Text(
                        'Koneksi aman dengan enkripsi JWT',
                        style: TextStyle(
                            fontSize: 12, color: Colors.grey.shade400),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
