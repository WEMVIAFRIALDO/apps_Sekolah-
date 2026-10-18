import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../services/theme_service.dart';

/// Saklar Segmented Dual-Pill Switch Mode Gelap / Terang (Android Mobile)
/// Desain presisi selaras dengan Web Admin: [ 🌙 Gelap | ☀️ Terang ]
/// Memiliki visual affordance tinggi, slider beranimasi, dan area sentuh nyaman.
class ThemeSegmentedSwitch extends StatelessWidget {
  const ThemeSegmentedSwitch({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = ThemeService.to;

    return Obx(() {
      final isDark = theme.isDarkMode.value;

      return GestureDetector(
        onTap: theme.toggleTheme,
        child: Container(
          width: 136,
          height: 32,
          padding: const EdgeInsets.all(2.5),
          decoration: BoxDecoration(
            color: isDark
                ? const Color(0xFF0F172A).withValues(alpha: 0.85)
                : const Color(0xFFF1F5F9).withValues(alpha: 0.95),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: isDark
                  ? Colors.white.withValues(alpha: 0.16)
                  : const Color(0xFFCBD5E1),
              width: 1,
            ),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: isDark ? 0.35 : 0.06),
                blurRadius: 8,
                offset: const Offset(0, 2),
              ),
            ],
          ),
          child: Stack(
            children: [
              // Sliding Animated Thumb
              AnimatedAlign(
                duration: const Duration(milliseconds: 250),
                curve: Curves.easeOutCubic,
                alignment: isDark ? Alignment.centerLeft : Alignment.centerRight,
                child: Container(
                  width: 65,
                  height: 27,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(16),
                    gradient: LinearGradient(
                      colors: isDark
                          ? const [Color(0xFF4F46E5), Color(0xFF6366F1)]
                          : const [Color(0xFFF59E0B), Color(0xFFFBBF24)],
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: (isDark
                                ? const Color(0xFF6366F1)
                                : const Color(0xFFF59E0B))
                            .withValues(alpha: 0.5),
                        blurRadius: 8,
                        offset: const Offset(0, 1),
                      ),
                    ],
                  ),
                ),
              ),

              // Labels: Gelap & Terang
              Row(
                children: [
                  Expanded(
                    child: Center(
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Text('🌙', style: TextStyle(fontSize: 11)),
                          const SizedBox(width: 3),
                          Text(
                            'Gelap',
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w700,
                              color: isDark
                                  ? Colors.white
                                  : const Color(0xFF64748B),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  Expanded(
                    child: Center(
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Text('☀️', style: TextStyle(fontSize: 11)),
                          const SizedBox(width: 3),
                          Text(
                            'Terang',
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w700,
                              color: !isDark
                                  ? const Color(0xFF1E293B)
                                  : const Color(0xFF94A3B8),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      );
    });
  }
}
