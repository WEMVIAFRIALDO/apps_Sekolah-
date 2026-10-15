import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'auth_service.dart';

/// Service pengendali Mode Gelap / Mode Terang aplikasi SALUT
class ThemeService extends GetxService {
  static ThemeService get to => Get.find<ThemeService>();

  final _auth = AuthService();
  final isDarkMode = true.obs;

  @override
  void onInit() {
    super.onInit();
    _loadTheme();
  }

  Future<void> _loadTheme() async {
    final saved = await _auth.getTheme();
    if (saved != null) {
      isDarkMode.value = (saved == 'dark');
    }
  }

  void toggleTheme() {
    isDarkMode.value = !isDarkMode.value;
    _auth.saveTheme(isDarkMode.value ? 'dark' : 'light');
  }

  // ─── Token Warna Dinamis ───────────────────────────────────────────────────
  Color get bg => isDarkMode.value ? const Color(0xFF070B14) : const Color(0xFFF8FAFC);
  Color get appBar => isDarkMode.value ? const Color(0xFF0D1321) : Colors.white;
  Color get card => isDarkMode.value ? const Color(0xFF0F172A) : Colors.white;
  Color get cardSubtle => isDarkMode.value ? const Color(0xFF1E293B) : const Color(0xFFF1F5F9);
  Color get navBar => isDarkMode.value ? const Color(0xFF0D1321) : Colors.white;

  Color get textPrimary => isDarkMode.value ? Colors.white : const Color(0xFF0F172A);
  Color get textSecondary => isDarkMode.value ? const Color(0xFFE2E8F0) : const Color(0xFF334155);
  Color get textMuted => isDarkMode.value ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

  Color get border => isDarkMode.value ? Colors.white.withValues(alpha: 0.10) : const Color(0xFFE2E8F0);
  Color get borderGlow => isDarkMode.value ? const Color(0xFF3B82F6).withValues(alpha: 0.3) : const Color(0xFF93C5FD);

  Color get primary => isDarkMode.value ? const Color(0xFF3B82F6) : const Color(0xFF2563EB);
  Color get accent => const Color(0xFF06B6D4);

  List<BoxShadow> get cardShadow => isDarkMode.value
      ? [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.45),
            blurRadius: 18,
            offset: const Offset(0, 8),
          ),
        ]
      : [
          BoxShadow(
            color: const Color(0xFF0F172A).withValues(alpha: 0.06),
            blurRadius: 16,
            offset: const Offset(0, 4),
          ),
          BoxShadow(
            color: const Color(0xFF0F172A).withValues(alpha: 0.03),
            blurRadius: 4,
            offset: const Offset(0, 1),
          ),
        ];
}
