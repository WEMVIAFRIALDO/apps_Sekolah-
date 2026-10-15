import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:dio/dio.dart';
import 'package:firebase_messaging/firebase_messaging.dart';

import '../routes/app_routes.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import '../services/theme_service.dart';

/// Halaman Login Mobile - Konsep Dual Theme (Dark / Light)
/// Antarmuka fleksibel dan modern untuk seluruh peran (Siswa & Alumni).
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

  // ── Logic: Login dengan JWT & Android Keystore ────────────────────────────
  Future<void> _handleLogin() async {
    if (!_formKey.currentState!.validate()) return;

    setState(() => _isLoading = true);

    try {
      String? fcmToken;
      try {
        fcmToken = await FirebaseMessaging.instance.getToken();
      } catch (e) {
        debugPrint("Gagal mengambil FCM token: $e");
      }

      final Map<String, dynamic> requestData = {
        'nisn':     _nisnController.text.trim(),
        'password': _passwordController.text,
      };
      if (fcmToken != null) {
        requestData['fcm_token'] = fcmToken;
      }

      // POST /api/login → { token, user: { id, name, nisn, role, ... } }
      final response = await _api.post('/login', data: requestData);

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
        'Autentikasi Gagal',
        msg,
        backgroundColor: const Color(0xFFDC2626),
        colorText:        Colors.white,
        snackPosition:    SnackPosition.TOP,
        margin:           const EdgeInsets.all(16),
        borderRadius:     14,
        icon:             const Icon(Icons.error_outline_rounded, color: Colors.white),
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
    final size  = MediaQuery.of(context).size;
    final theme = ThemeService.to;

    return Obx(() {
      final isDark = theme.isDarkMode.value;

      return Scaffold(
        backgroundColor: theme.bg,
        body: Stack(
          children: [
            // ── Ambient Glow Aurora (Biru Sapphire & Amber Gold) ───────────────
            Positioned(
              top: -size.width * 0.45,
              right: -size.width * 0.35,
              child: Container(
                width: size.width * 1.2,
                height: size.width * 1.2,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: RadialGradient(
                    colors: [
                      isDark
                          ? const Color(0xFF2563EB).withValues(alpha: 0.22)
                          : const Color(0xFF3B82F6).withValues(alpha: 0.08),
                      Colors.transparent,
                    ],
                  ),
                ),
              ),
            ),
            Positioned(
              bottom: -size.width * 0.5,
              left: -size.width * 0.4,
              child: Container(
                width: size.width * 1.2,
                height: size.width * 1.2,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: RadialGradient(
                    colors: [
                      isDark
                          ? const Color(0xFF06B6D4).withValues(alpha: 0.14)
                          : const Color(0xFF06B6D4).withValues(alpha: 0.06),
                      Colors.transparent,
                    ],
                  ),
                ),
              ),
            ),

            // ── Tombol Switch Theme di Pojok Kanan Atas ───────────────────────
            SafeArea(
              child: Align(
                alignment: Alignment.topRight,
                child: Padding(
                  padding: const EdgeInsets.only(top: 12, right: 16),
                  child: InkWell(
                    borderRadius: BorderRadius.circular(20),
                    onTap: theme.toggleTheme,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: theme.card,
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(color: theme.border),
                        boxShadow: theme.cardShadow,
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            isDark ? Icons.wb_sunny_rounded : Icons.nightlight_round,
                            size: 16,
                            color: isDark ? const Color(0xFFFBBF24) : const Color(0xFF4F46E5),
                          ),
                          const SizedBox(width: 6),
                          Text(
                            isDark ? 'Mode Terang' : 'Mode Gelap',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w700,
                              color: theme.textPrimary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ),

            // ── Form Login Utama ───────────────────────────────────────────────
            SafeArea(
              child: Center(
                child: SingleChildScrollView(
                  physics: const ClampingScrollPhysics(),
                  padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
                  child: Form(
                    key: _formKey,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        // Badge Resmi Institusi (Glass-Pill Neon)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                          decoration: BoxDecoration(
                            color: theme.cardSubtle,
                            borderRadius: BorderRadius.circular(30),
                            border: Border.all(
                              color: theme.borderGlow,
                              width: 1.2,
                            ),
                            boxShadow: [
                              BoxShadow(
                                color: theme.primary.withValues(alpha: 0.15),
                                blurRadius: 10,
                              ),
                            ],
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Container(
                                width: 7,
                                height: 7,
                                decoration: BoxDecoration(
                                  color: const Color(0xFF00F2FE),
                                  shape: BoxShape.circle,
                                  boxShadow: [
                                    BoxShadow(
                                      color: const Color(0xFF00F2FE).withValues(alpha: 0.8),
                                      blurRadius: 6,
                                    ),
                                  ],
                                ),
                              ),
                              const SizedBox(width: 8),
                              Text(
                                'PORTAL RESMI AKADEMIK & ALUMNI',
                                style: TextStyle(
                                  fontSize: 10.5,
                                  fontWeight: FontWeight.w700,
                                  letterSpacing: 1.2,
                                  color: isDark ? const Color(0xFF93C5FD) : const Color(0xFF1D4ED8),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 20),

                        // Logo Transparan SALUT (Bebas Kotak)
                        Container(
                          width: 110,
                          height: 110,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            boxShadow: [
                              BoxShadow(
                                color: const Color(0xFF00F2FE).withValues(alpha: isDark ? 0.25 : 0.15),
                                blurRadius: 28,
                                spreadRadius: 2,
                              ),
                              BoxShadow(
                                color: const Color(0xFF2563EB).withValues(alpha: isDark ? 0.35 : 0.15),
                                blurRadius: 36,
                              ),
                            ],
                          ),
                          child: Image.asset(
                            'assets/images/logo_salut.png',
                            fit: BoxFit.contain,
                            errorBuilder: (context, error, stackTrace) => Icon(
                              Icons.school_rounded,
                              size: 64,
                              color: theme.primary,
                            ),
                          ),
                        ),
                        const SizedBox(height: 16),

                        Text(
                          'SMK NEGERI 1 TELADAN',
                          style: TextStyle(
                            fontSize: 17,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 2.0,
                            color: theme.textPrimary,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          'Masuk menggunakan NISN & kata sandi Anda',
                          style: TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w500,
                            color: theme.textMuted,
                          ),
                        ),
                        const SizedBox(height: 28),

                        // ── Kartu Input Form Frosted Glass ────────────────
                        Container(
                          padding: const EdgeInsets.all(26),
                          decoration: BoxDecoration(
                            color: theme.card,
                            borderRadius: BorderRadius.circular(24),
                            border: Border.all(
                              color: theme.border,
                              width: 1.2,
                            ),
                            boxShadow: theme.cardShadow,
                          ),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'NISN / ID Pengguna',
                                style: TextStyle(
                                  fontSize: 13,
                                  fontWeight: FontWeight.w700,
                                  color: theme.textSecondary,
                                ),
                              ),
                              const SizedBox(height: 8),
                              TextFormField(
                                controller: _nisnController,
                                keyboardType: TextInputType.number,
                                maxLength: 10,
                                validator: (v) {
                                  if (v == null || v.isEmpty) return 'NISN wajib diisi';
                                  if (v.length < 10) return 'NISN harus 10 digit';
                                  return null;
                                },
                                style: TextStyle(
                                  fontSize: 14.5,
                                  fontWeight: FontWeight.w600,
                                  color: theme.textPrimary,
                                ),
                                decoration: InputDecoration(
                                  hintText: 'Contoh: 0054321987',
                                  hintStyle: TextStyle(color: theme.textMuted, fontSize: 14),
                                  prefixIcon: Icon(Icons.badge_outlined, color: theme.primary, size: 20),
                                  counterText: '',
                                  filled: true,
                                  fillColor: theme.cardSubtle,
                                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                                  border: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    borderSide: BorderSide(color: theme.border),
                                  ),
                                  enabledBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    borderSide: BorderSide(color: theme.border),
                                  ),
                                  focusedBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    borderSide: BorderSide(color: theme.primary, width: 1.8),
                                  ),
                                ),
                              ),
                              const SizedBox(height: 18),

                              Text(
                                'Kata Sandi',
                                style: TextStyle(
                                  fontSize: 13,
                                  fontWeight: FontWeight.w700,
                                  color: theme.textSecondary,
                                ),
                              ),
                              const SizedBox(height: 8),
                              TextFormField(
                                controller: _passwordController,
                                obscureText: _obscurePassword,
                                validator: (v) {
                                  if (v == null || v.isEmpty) return 'Password wajib diisi';
                                  return null;
                                },
                                style: TextStyle(
                                  fontSize: 14.5,
                                  fontWeight: FontWeight.w600,
                                  color: theme.textPrimary,
                                ),
                                decoration: InputDecoration(
                                  hintText: 'Masukkan kata sandi',
                                  hintStyle: TextStyle(color: theme.textMuted, fontSize: 14),
                                  prefixIcon: Icon(Icons.lock_outline_rounded, color: theme.primary, size: 20),
                                  suffixIcon: IconButton(
                                    icon: Icon(
                                      _obscurePassword ? Icons.visibility_off_outlined : Icons.visibility_outlined,
                                      color: theme.textMuted,
                                      size: 20,
                                    ),
                                    onPressed: () => setState(() => _obscurePassword = !_obscurePassword),
                                  ),
                                  filled: true,
                                  fillColor: theme.cardSubtle,
                                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                                  border: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    borderSide: BorderSide(color: theme.border),
                                  ),
                                  enabledBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    borderSide: BorderSide(color: theme.border),
                                  ),
                                  focusedBorder: OutlineInputBorder(
                                    borderRadius: BorderRadius.circular(14),
                                    borderSide: BorderSide(color: theme.primary, width: 1.8),
                                  ),
                                ),
                              ),
                              const SizedBox(height: 24),

                              // Tombol Masuk Royal Blue dengan Neon Glow
                              SizedBox(
                                width: double.infinity,
                                height: 52,
                                child: ElevatedButton(
                                  onPressed: _isLoading ? null : _handleLogin,
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: theme.primary,
                                    foregroundColor: Colors.white,
                                    elevation: 4,
                                    shadowColor: theme.primary.withValues(alpha: 0.5),
                                    shape: RoundedRectangleBorder(
                                      borderRadius: BorderRadius.circular(14),
                                    ),
                                  ),
                                  child: _isLoading
                                      ? const SizedBox(
                                          width: 22,
                                          height: 22,
                                          child: CircularProgressIndicator(
                                            strokeWidth: 2.5,
                                            valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                                          ),
                                        )
                                      : const Text(
                                          'Masuk ke Akun',
                                          style: TextStyle(
                                            fontSize: 15,
                                            fontWeight: FontWeight.w700,
                                            letterSpacing: 0.3,
                                          ),
                                        ),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 24),

                        // Footer Keamanan Resmi
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                          decoration: BoxDecoration(
                            color: theme.cardSubtle,
                            borderRadius: BorderRadius.circular(20),
                            border: Border.all(
                              color: theme.border,
                            ),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(Icons.lock_outline_rounded, size: 12, color: theme.textMuted),
                              const SizedBox(width: 6),
                              Text(
                                'Terenkripsi Aman • SALUT v1.0.0',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600,
                                  color: theme.textMuted,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      );
    });
  }
}
