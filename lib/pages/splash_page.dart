import 'dart:async';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../routes/app_routes.dart';
import '../services/auth_service.dart';

/// Halaman Splash Screen - Konsep "Cyber-Academic Elite"
/// Memadukan estetika futuristik modern (Deep Obsidian, Electric Cyan Glow, Frosted Glass)
/// dengan wibawa institusi SMK Negeri 1 Teladan.
class SplashPage extends StatefulWidget {
  const SplashPage({super.key});

  @override
  State<SplashPage> createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> with TickerProviderStateMixin {
  late AnimationController _introController;
  late Animation<double> _fadeAnimation;
  late Animation<double> _scaleAnimation;
  late Animation<Offset> _slideAnimation;

  // Animasi pulsing untuk ambient halo & dot indicator
  late AnimationController _pulseController;

  @override
  void initState() {
    super.initState();

    // ── Setup Animasi Pembuka Elegan ─────────────────────────────────────────
    _introController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1400),
    );

    _fadeAnimation = CurvedAnimation(
      parent: _introController,
      curve: const Interval(0.0, 0.85, curve: Curves.easeOutCubic),
    );

    _scaleAnimation = Tween<double>(begin: 0.88, end: 1.0).animate(
      CurvedAnimation(
        parent: _introController,
        curve: const Interval(0.0, 0.90, curve: Curves.easeOutBack),
      ),
    );

    _slideAnimation = Tween<Offset>(
      begin: const Offset(0, 0.08),
      end: Offset.zero,
    ).animate(
      CurvedAnimation(
        parent: _introController,
        curve: const Interval(0.15, 1.0, curve: Curves.easeOutCubic),
      ),
    );

    _pulseController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1100),
    )..repeat(reverse: true);

    _introController.forward();

    // ── Timer Tepat 3 Detik dengan Autentikasi ───────────────────────────────
    Timer(const Duration(seconds: 3), _checkAuthAndNavigate);
  }

  /// Cek JWT token di Android Keystore untuk menentukan rute navigasi
  Future<void> _checkAuthAndNavigate() async {
    if (!mounted) return;

    try {
      final isLoggedIn = await AuthService().isLoggedIn();
      if (isLoggedIn) {
        Get.offAllNamed(AppRoutes.dashboard);
      } else {
        Get.offAllNamed(AppRoutes.login);
      }
    } catch (_) {
      Get.offAllNamed(AppRoutes.login);
    }
  }

  @override
  void dispose() {
    _introController.dispose();
    _pulseController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Scaffold(
      backgroundColor: const Color(0xFF070B14), // Deep Space Obsidian
      body: Stack(
        children: [
          // ── Ambient Glow Aurora (Biru Sapphire & Amber Gold) ───────────────
          Positioned(
            top: -size.width * 0.4,
            right: -size.width * 0.3,
            child: Container(
              width: size.width * 1.2,
              height: size.width * 1.2,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: RadialGradient(
                  colors: [
                    const Color(0xFF2563EB).withValues(alpha: 0.22),
                    const Color(0xFF06B6D4).withValues(alpha: 0.08),
                    Colors.transparent,
                  ],
                ),
              ),
            ),
          ),
          Positioned(
            bottom: -size.width * 0.45,
            left: -size.width * 0.35,
            child: Container(
              width: size.width * 1.2,
              height: size.width * 1.2,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: RadialGradient(
                  colors: [
                    const Color(0xFFF59E0B).withValues(alpha: 0.12),
                    Colors.transparent,
                  ],
                ),
              ),
            ),
          ),

          // ── Konten Utama ───────────────────────────────────────────────────
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
              child: Column(
                children: [
                  const Spacer(flex: 3),

                  // ── Logo & Kartu Glowing Glass ──────────────────────────────
                  FadeTransition(
                    opacity: _fadeAnimation,
                    child: ScaleTransition(
                      scale: _scaleAnimation,
                      child: SlideTransition(
                        position: _slideAnimation,
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            // Badge Resmi Institusi (Glass-Pill Neon)
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                              decoration: BoxDecoration(
                                color: const Color(0xFF1E293B).withValues(alpha: 0.6),
                                borderRadius: BorderRadius.circular(30),
                                border: Border.all(
                                  color: const Color(0xFF3B82F6).withValues(alpha: 0.4),
                                  width: 1.2,
                                ),
                                boxShadow: [
                                  BoxShadow(
                                    color: const Color(0xFF3B82F6).withValues(alpha: 0.15),
                                    blurRadius: 12,
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
                                  const Text(
                                    'PORTAL RESMI AKADEMIK & ALUMNI',
                                    style: TextStyle(
                                      fontSize: 10.5,
                                      fontWeight: FontWeight.w700,
                                      letterSpacing: 1.4,
                                      color: Color(0xFF93C5FD),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 28),

                            // Logo Transparan SALUT dengan Glowing Ambient Halus (Bebas Kotak)
                            AnimatedBuilder(
                              animation: _pulseController,
                              builder: (context, child) {
                                final glowVal = _pulseController.value;
                                return Container(
                                  width: 175,
                                  height: 175,
                                  decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    boxShadow: [
                                      BoxShadow(
                                        color: const Color(0xFF00F2FE).withValues(alpha: 0.22 + (glowVal * 0.15)),
                                        blurRadius: 36 + (glowVal * 16),
                                        spreadRadius: 4,
                                      ),
                                      BoxShadow(
                                        color: const Color(0xFF2563EB).withValues(alpha: 0.3),
                                        blurRadius: 55,
                                      ),
                                    ],
                                  ),
                                  child: child,
                                );
                              },
                              child: Image.asset(
                                'assets/images/logo_salut.png',
                                fit: BoxFit.contain,
                                errorBuilder: (context, error, stackTrace) {
                                  return const Icon(
                                    Icons.school_rounded,
                                    size: 80,
                                    color: Color(0xFF38BDF8),
                                  );
                                },
                              ),
                            ),
                            const SizedBox(height: 28),

                            // Identitas Sekolah & Aplikasi
                            const Text(
                              'SMK NEGERI 1 TELADAN',
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontSize: 17,
                                fontWeight: FontWeight.w900,
                                letterSpacing: 2.2,
                                color: Colors.white,
                              ),
                            ),
                            const SizedBox(height: 6),
                            const Text(
                              'Sistem Administrasi Kelulusan & Tracer Study',
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.w500,
                                letterSpacing: 0.3,
                                color: Color(0xFF94A3B8),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),

                  const Spacer(flex: 4),

                  // ── Indikator Loading & Footer Keamanan Prestisius ───────────
                  FadeTransition(
                    opacity: _fadeAnimation,
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        // Animated Neon 3-Dot Indicator
                        AnimatedBuilder(
                          animation: _pulseController,
                          builder: (context, child) {
                            return Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: List.generate(3, (index) {
                                final double delay = index * 0.25;
                                final double animValue = (_pulseController.value + delay) % 1.0;
                                final double scale = 0.75 + (animValue * 0.45);
                                final double opacity = 0.4 + (animValue * 0.6);

                                return Container(
                                  margin: const EdgeInsets.symmetric(horizontal: 5),
                                  width: 8 * scale,
                                  height: 8 * scale,
                                  decoration: BoxDecoration(
                                    color: index == 1
                                        ? const Color(0xFFF59E0B).withValues(alpha: opacity)
                                        : const Color(0xFF38BDF8).withValues(alpha: opacity),
                                    shape: BoxShape.circle,
                                    boxShadow: [
                                      BoxShadow(
                                        color: (index == 1 ? const Color(0xFFF59E0B) : const Color(0xFF38BDF8))
                                            .withValues(alpha: opacity * 0.6),
                                        blurRadius: 8,
                                      ),
                                    ],
                                  ),
                                );
                              }),
                            );
                          },
                        ),
                        const SizedBox(height: 20),

                        // Security & Version Tag
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                          decoration: BoxDecoration(
                            color: const Color(0xFF0F172A).withValues(alpha: 0.7),
                            borderRadius: BorderRadius.circular(20),
                            border: Border.all(
                              color: Colors.white.withValues(alpha: 0.08),
                            ),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: const [
                              Icon(
                                Icons.lock_outline_rounded,
                                size: 12,
                                color: Color(0xFF94A3B8),
                              ),
                              SizedBox(width: 6),
                              Text(
                                'Terenkripsi Aman • SALUT v1.0.0',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600,
                                  letterSpacing: 0.5,
                                  color: Color(0xFF94A3B8),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 8),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
