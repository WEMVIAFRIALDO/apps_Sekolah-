import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:dio/dio.dart';
import 'package:firebase_messaging/firebase_messaging.dart';

import '../routes/app_routes.dart';
import '../services/api_service.dart';
import '../services/auth_service.dart';
import '../widgets/theme_segmented_switch.dart';

/// Halaman Login Mobile - Konsep Cyber-Crystal Glassmorphism
/// Terinspirasi dari layout referensi: Hero 3D Crystal di atas + Floating Glassmorphism Card di bawah.
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
  int _activeDotIndex   = 0;

  final _api  = ApiService();
  final _auth = AuthService();

  // Kredensial demo untuk 3 dot indicator
  final List<Map<String, String>> _rolePresets = [
    {
      'title': 'Siswa Aktif',
      'nisn': '0054321987',
      'pass': 'siswa123',
    },
    {
      'title': 'Alumni',
      'nisn': '0067890123',
      'pass': 'alumni123',
    },
    {
      'title': 'Manual / Kustom',
      'nisn': '',
      'pass': '',
    },
  ];

  @override
  void initState() {
    super.initState();
    _applyPreset(0);
  }

  void _applyPreset(int index) {
    setState(() {
      _activeDotIndex = index;
      if (index < 2) {
        _nisnController.text     = _rolePresets[index]['nisn']!;
        _passwordController.text = _rolePresets[index]['pass']!;
      } else {
        _nisnController.clear();
        _passwordController.clear();
      }
    });
  }

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

      // Navigasi ke Dashboard
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
    final size = MediaQuery.of(context).size;

    return Scaffold(
        backgroundColor: const Color(0xFF050811),
        body: Stack(
          children: [
            // ── 1. Hero Background 3D Crystal & Sci-Fi Pedestal ─────────────
            Positioned(
              top: 0,
              left: 0,
              right: 0,
              height: size.height * 0.52,
              child: Stack(
                fit: StackFit.expand,
                children: [
                  Image.asset(
                    'assets/images/crystal_hero_mobile.jpg',
                    fit: BoxFit.cover,
                    alignment: Alignment.topCenter,
                    errorBuilder: (context, error, stackTrace) => Container(
                      color: const Color(0xFF0A0F1D),
                      child: Center(
                        child: Icon(
                          Icons.auto_awesome_rounded,
                          size: 80,
                          color: const Color(0xFF6366F1).withValues(alpha: 0.5),
                        ),
                      ),
                    ),
                  ),
                  // Gradasi bayangan halus menuju kartu bawah
                  Container(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          const Color(0xFF050811).withValues(alpha: 0.35),
                          Colors.transparent,
                          const Color(0xFF050811).withValues(alpha: 0.85),
                          const Color(0xFF050811),
                        ],
                        stops: const [0.0, 0.4, 0.85, 1.0],
                      ),
                    ),
                  ),
                ],
              ),
            ),

            // ── 2. Top Header Bar (Brand Logo + Theme Switcher) ──────────────
            SafeArea(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    // Brand Badge
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: const Color(0xFF0F172A).withValues(alpha: 0.65),
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(color: Colors.white.withValues(alpha: 0.15)),
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF6366F1).withValues(alpha: 0.25),
                            blurRadius: 12,
                          ),
                        ],
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Image.asset(
                            'assets/images/logo_salut.png',
                            width: 20,
                            height: 20,
                            fit: BoxFit.contain,
                            errorBuilder: (context, error, stackTrace) => const Icon(
                              Icons.diamond_outlined,
                              size: 16,
                              color: Color(0xFF818CF8),
                            ),
                          ),
                          const SizedBox(width: 8),
                          const Text(
                            'SALUT',
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w800,
                              letterSpacing: 1.2,
                              color: Colors.white,
                            ),
                          ),
                        ],
                      ),
                    ),

                    // Segmented Theme Switcher (Konsisten dengan Web Admin)
                    const ThemeSegmentedSwitch(),
                  ],
                ),
              ),
            ),

            // ── 3. Floating Frosted Glass Card (Exact to Reference Mockup) ────
            Align(
              alignment: Alignment.bottomCenter,
              child: SingleChildScrollView(
                physics: const ClampingScrollPhysics(),
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(20, 0, 20, 24),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(28),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 24, sigmaY: 24),
                      child: Container(
                        padding: const EdgeInsets.all(24),
                        decoration: BoxDecoration(
                          color: const Color(0xFF0F172A).withValues(alpha: 0.68),
                          borderRadius: BorderRadius.circular(28),
                          border: Border.all(
                            color: Colors.white.withValues(alpha: 0.14),
                            width: 1.2,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black.withValues(alpha: 0.6),
                              blurRadius: 35,
                              offset: const Offset(0, 15),
                            ),
                            BoxShadow(
                              color: const Color(0xFF6366F1).withValues(alpha: 0.12),
                              blurRadius: 25,
                            ),
                          ],
                        ),
                        child: Form(
                          key: _formKey,
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              // Mini Emblem di Atas Form
                              Container(
                                width: 44,
                                height: 44,
                                decoration: BoxDecoration(
                                  color: const Color(0xFF6366F1).withValues(alpha: 0.2),
                                  borderRadius: BorderRadius.circular(14),
                                  border: Border.all(
                                    color: Colors.white.withValues(alpha: 0.2),
                                  ),
                                  boxShadow: [
                                    BoxShadow(
                                      color: const Color(0xFF6366F1).withValues(alpha: 0.35),
                                      blurRadius: 16,
                                    ),
                                  ],
                                ),
                                child: Center(
                                  child: Image.asset(
                                    'assets/images/logo_salut.png',
                                    width: 26,
                                    height: 26,
                                    fit: BoxFit.contain,
                                    errorBuilder: (context, error, stackTrace) => const Icon(
                                      Icons.school_rounded,
                                      size: 22,
                                      color: Color(0xFF818CF8),
                                    ),
                                  ),
                                ),
                              ),
                              const SizedBox(height: 10),

                              const Text(
                                'SALUT PORTAL',
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w800,
                                  letterSpacing: 1.2,
                                  color: Colors.white,
                                ),
                              ),
                              const SizedBox(height: 2),
                              Text(
                                'SMK NEGERI 1 TELADAN',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600,
                                  letterSpacing: 0.6,
                                  color: Colors.white.withValues(alpha: 0.55),
                                ),
                              ),
                              const SizedBox(height: 22),

                              // Pill Input 1: User Icon + NISN Field
                              Container(
                                decoration: BoxDecoration(
                                  color: Colors.white.withValues(alpha: 0.06),
                                  borderRadius: BorderRadius.circular(30),
                                  border: Border.all(
                                    color: Colors.white.withValues(alpha: 0.12),
                                  ),
                                ),
                                child: TextFormField(
                                  controller: _nisnController,
                                  keyboardType: TextInputType.number,
                                  maxLength: 10,
                                  validator: (v) {
                                    if (v == null || v.isEmpty) return 'NISN wajib diisi';
                                    if (v.length < 10) return 'NISN harus 10 digit';
                                    return null;
                                  },
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w600,
                                  ),
                                  decoration: InputDecoration(
                                    hintText: 'NISN / ID Pengguna',
                                    hintStyle: TextStyle(
                                      color: Colors.white.withValues(alpha: 0.4),
                                      fontSize: 13.5,
                                    ),
                                    prefixIcon: Icon(
                                      Icons.person_outline_rounded,
                                      color: Colors.white.withValues(alpha: 0.7),
                                      size: 20,
                                    ),
                                    counterText: '',
                                    border: InputBorder.none,
                                    contentPadding: const EdgeInsets.symmetric(
                                      horizontal: 18,
                                      vertical: 14,
                                    ),
                                  ),
                                ),
                              ),
                              const SizedBox(height: 14),

                              // Pill Input 2: Lock Icon + Password Field + Eye Toggle
                              Container(
                                decoration: BoxDecoration(
                                  color: Colors.white.withValues(alpha: 0.06),
                                  borderRadius: BorderRadius.circular(30),
                                  border: Border.all(
                                    color: Colors.white.withValues(alpha: 0.12),
                                  ),
                                ),
                                child: TextFormField(
                                  controller: _passwordController,
                                  obscureText: _obscurePassword,
                                  validator: (v) {
                                    if (v == null || v.isEmpty) return 'Kata sandi wajib diisi';
                                    return null;
                                  },
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 14,
                                    fontWeight: FontWeight.w600,
                                  ),
                                  decoration: InputDecoration(
                                    hintText: 'Kata Sandi Akun',
                                    hintStyle: TextStyle(
                                      color: Colors.white.withValues(alpha: 0.4),
                                      fontSize: 13.5,
                                    ),
                                    prefixIcon: Icon(
                                      Icons.lock_outline_rounded,
                                      color: Colors.white.withValues(alpha: 0.7),
                                      size: 20,
                                    ),
                                    suffixIcon: IconButton(
                                      icon: Icon(
                                        _obscurePassword
                                            ? Icons.visibility_off_outlined
                                            : Icons.visibility_outlined,
                                        color: Colors.white.withValues(alpha: 0.6),
                                        size: 19,
                                      ),
                                      onPressed: () => setState(() => _obscurePassword = !_obscurePassword),
                                    ),
                                    border: InputBorder.none,
                                    contentPadding: const EdgeInsets.symmetric(
                                      horizontal: 18,
                                      vertical: 14,
                                    ),
                                  ),
                                ),
                              ),
                              const SizedBox(height: 20),

                              // Gradient Action Button with Right Arrow
                              Container(
                                width: double.infinity,
                                height: 50,
                                decoration: BoxDecoration(
                                  borderRadius: BorderRadius.circular(30),
                                  gradient: const LinearGradient(
                                    colors: [
                                      Color(0xFF6366F1),
                                      Color(0xFF8B5CF6),
                                      Color(0xFF3B82F6),
                                    ],
                                  ),
                                  boxShadow: [
                                    BoxShadow(
                                      color: const Color(0xFF6366F1).withValues(alpha: 0.45),
                                      blurRadius: 20,
                                      offset: const Offset(0, 6),
                                    ),
                                  ],
                                ),
                                child: Material(
                                  color: Colors.transparent,
                                  child: InkWell(
                                    borderRadius: BorderRadius.circular(30),
                                    onTap: _isLoading ? null : _handleLogin,
                                    child: Center(
                                      child: _isLoading
                                          ? const SizedBox(
                                              width: 22,
                                              height: 22,
                                              child: CircularProgressIndicator(
                                                strokeWidth: 2.5,
                                                valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                                              ),
                                            )
                                          : const Row(
                                              mainAxisAlignment: MainAxisAlignment.center,
                                              children: [
                                                Text(
                                                  'Masuk',
                                                  style: TextStyle(
                                                    color: Colors.white,
                                                    fontSize: 14.5,
                                                    fontWeight: FontWeight.w700,
                                                    letterSpacing: 0.5,
                                                  ),
                                                ),
                                                SizedBox(width: 8),
                                                Icon(
                                                  Icons.arrow_forward_rounded,
                                                  color: Colors.white,
                                                  size: 18,
                                                ),
                                              ],
                                            ),
                                    ),
                                  ),
                                ),
                              ),
                              const SizedBox(height: 18),

                              // Bottom 3-Dot Indicator Row (Exact to Reference Image)
                              Row(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: List.generate(3, (index) {
                                  final isActive = _activeDotIndex == index;
                                  return GestureDetector(
                                    onTap: () => _applyPreset(index),
                                    child: AnimatedContainer(
                                      duration: const Duration(milliseconds: 250),
                                      margin: const EdgeInsets.symmetric(horizontal: 5),
                                      height: 7,
                                      width: isActive ? 24 : 7,
                                      decoration: BoxDecoration(
                                        color: isActive
                                            ? const Color(0xFF818CF8)
                                            : Colors.white.withValues(alpha: 0.22),
                                        borderRadius: BorderRadius.circular(4),
                                        boxShadow: isActive
                                            ? [
                                                BoxShadow(
                                                  color: const Color(0xFF818CF8).withValues(alpha: 0.8),
                                                  blurRadius: 8,
                                                ),
                                              ]
                                            : null,
                                      ),
                                    ),
                                  );
                                }),
                              ),
                              const SizedBox(height: 8),

                              // Indikator Label Role Terpilih
                              Text(
                                'Mode Akses: ${_rolePresets[_activeDotIndex]['title']}',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600,
                                  color: Colors.white.withValues(alpha: 0.5),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      );
  }
}
