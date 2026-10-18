import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/skills_controller.dart';
import '../services/theme_service.dart';

/// Halaman Portofolio Keahlian SMK (SKPI) untuk Siswa & Alumni.
/// Terintegrasi ThemeService (Mode Gelap & Mode Terang).
class SkillsPage extends StatelessWidget {
  const SkillsPage({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = Get.put(SkillsController());
    final theme = ThemeService.to;

    return Obx(() {
      return Scaffold(
        backgroundColor: theme.bg,
        appBar: AppBar(
          title: Text(
            'Portofolio Keahlian SMK',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: theme.textPrimary,
            ),
          ),
          centerTitle: true,
          elevation: 0,
          backgroundColor: theme.appBar,
          surfaceTintColor: Colors.transparent,
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(1),
            child: Container(color: theme.border, height: 1),
          ),
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios_new_rounded, size: 20, color: theme.textPrimary),
            onPressed: () => Get.back(),
          ),
        ),
        body: Obx(() {
          if (controller.isLoading.value) {
            return Center(
              child: CircularProgressIndicator(color: theme.primary),
            );
          }

          if (controller.errorMessage.isNotEmpty) {
            return Center(
              child: Padding(
                padding: const EdgeInsets.all(24.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Icon(Icons.error_outline_rounded, size: 56, color: Colors.red),
                    const SizedBox(height: 16),
                    Text(
                      controller.errorMessage.value,
                      textAlign: TextAlign.center,
                      style: TextStyle(fontSize: 14, color: theme.textMuted),
                    ),
                    const SizedBox(height: 16),
                    ElevatedButton.icon(
                      onPressed: controller.fetchMySkills,
                      icon: const Icon(Icons.refresh_rounded),
                      label: const Text('Coba Lagi'),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: theme.primary,
                        foregroundColor: Colors.white,
                      ),
                    ),
                  ],
                ),
              ),
            );
          }

          return RefreshIndicator(
            onRefresh: controller.fetchMySkills,
            child: SingleChildScrollView(
              physics: const AlwaysScrollableScrollPhysics(),
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // 1. Header Card: Jurusan & SKPI Info
                  _buildHeaderCard(context, controller),
                  const SizedBox(height: 16),

                  // 2. Ringkasan Tingkat Kemahiran
                  _buildSummaryRow(controller, theme),
                  const SizedBox(height: 20),

                  // 3. Filter Chips
                  _buildFilterChips(controller, theme),
                  const SizedBox(height: 16),

                  // 4. Daftar Kartu Kompetensi
                  if (controller.filteredSkills.isEmpty)
                    Container(
                      padding: const EdgeInsets.all(32),
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: theme.card,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: theme.border),
                      ),
                      child: Column(
                        children: [
                          Icon(Icons.workspace_premium_outlined, size: 48, color: theme.textMuted),
                          const SizedBox(height: 12),
                          Text(
                            'Belum ada kompetensi pada kategori ini.',
                            style: TextStyle(color: theme.textMuted, fontSize: 14),
                          ),
                        ],
                      ),
                    )
                  else
                    ...controller.filteredSkills.map((skill) => _buildSkillCard(skill, theme)),

                  const SizedBox(height: 24),
                ],
              ),
            ),
          );
        }),
      );
    });
  }

  Widget _buildHeaderCard(BuildContext context, SkillsController controller) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.indigo.shade700, Colors.purple.shade800],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.indigo.shade900.withValues(alpha: 0.25),
            blurRadius: 14,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  'SKPI • ${controller.userJurusan.value}',
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 0.5,
                  ),
                ),
              ),
              const Spacer(),
              const Icon(Icons.verified_rounded, color: Colors.amberAccent, size: 22),
            ],
          ),
          const SizedBox(height: 12),
          const Text(
            'Surat Keterangan Pendamping Ijazah',
            style: TextStyle(
              color: Colors.white,
              fontSize: 17,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          const Text(
            'Portofolio capaian unit kompetensi keahlian kejuruan yang telah diverifikasi guru pembimbing.',
            style: TextStyle(color: Colors.white70, fontSize: 12, height: 1.4),
          ),
        ],
      ),
    );
  }

  Widget _buildSummaryRow(SkillsController controller, ThemeService theme) {
    return Row(
      children: [
        _buildStatBox('Total Unit', '${controller.allSkills.length}', const Color(0xFF38BDF8), theme),
        const SizedBox(width: 8),
        _buildStatBox('Mahir', '${controller.countByLevel('Mahir')}', const Color(0xFF10B981), theme),
        const SizedBox(width: 8),
        _buildStatBox('Terampil', '${controller.countByLevel('Terampil')}', const Color(0xFFA855F7), theme),
        const SizedBox(width: 8),
        _buildStatBox('Dasar', '${controller.countByLevel('Dasar')}', const Color(0xFFF59E0B), theme),
      ],
    );
  }

  Widget _buildStatBox(String label, String count, Color color, ThemeService theme) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 6),
        decoration: BoxDecoration(
          color: theme.card,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: theme.border),
          boxShadow: theme.cardShadow,
        ),
        child: Column(
          children: [
            Text(
              count,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: color,
              ),
            ),
            const SizedBox(height: 2),
            Text(
              label,
              style: TextStyle(fontSize: 11, color: theme.textMuted, fontWeight: FontWeight.w600),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildFilterChips(SkillsController controller, ThemeService theme) {
    final filters = ['Semua', 'Mahir', 'Terampil', 'Dasar'];
    final isDark = theme.isDarkMode.value;

    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(
        children: filters.map((f) {
          final isSelected = controller.selectedFilter.value == f;
          return Padding(
            padding: const EdgeInsets.only(right: 8.0),
            child: ChoiceChip(
              label: Text(f),
              selected: isSelected,
              onSelected: (_) => controller.applyFilter(f),
              selectedColor: isDark ? const Color(0xFF6366F1) : const Color(0xFF4F46E5),
              labelStyle: TextStyle(
                color: isSelected ? Colors.white : theme.textPrimary,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                fontSize: 12,
              ),
              backgroundColor: theme.card,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
                side: BorderSide(
                  color: isSelected ? (isDark ? const Color(0xFF818CF8) : const Color(0xFF4F46E5)) : theme.border,
                ),
              ),
            ),
          );
        }).toList(),
      ),
    );
  }

  Widget _buildSkillCard(Map<String, dynamic> skill, ThemeService theme) {
    final level = skill['level']?.toString() ?? 'Terampil';
    final isDark = theme.isDarkMode.value;
    final Color badgeColor;
    final Color badgeBg;

    if (level == 'Mahir') {
      badgeColor = const Color(0xFF10B981);
      badgeBg = isDark ? const Color(0xFF064E3B).withValues(alpha: 0.4) : const Color(0xFFECFDF5);
    } else if (level == 'Terampil') {
      badgeColor = const Color(0xFF38BDF8);
      badgeBg = isDark ? const Color(0xFF0369A1).withValues(alpha: 0.3) : const Color(0xFFEFF6FF);
    } else {
      badgeColor = const Color(0xFFF59E0B);
      badgeBg = isDark ? const Color(0xFF78350F).withValues(alpha: 0.3) : const Color(0xFFFFFBEB);
    }

    final guru = skill['guru'] is Map ? skill['guru']['name'] : 'Guru Pembimbing';

    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: theme.card,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: theme.border),
        boxShadow: theme.cardShadow,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(
                child: Text(
                  skill['nama_kompetensi'] ?? 'Kompetensi',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                    color: theme.textPrimary,
                  ),
                ),
              ),
              const SizedBox(width: 8),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: badgeBg,
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: badgeColor.withValues(alpha: 0.4)),
                ),
                child: Text(
                  level,
                  style: TextStyle(
                    color: badgeColor,
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          Row(
            children: [
              Icon(Icons.category_outlined, size: 13, color: theme.textMuted),
              const SizedBox(width: 4),
              Text(
                skill['kategori'] ?? 'Kategori Kejuruan',
                style: TextStyle(fontSize: 12, color: theme.textMuted),
              ),
              const SizedBox(width: 12),
              Icon(Icons.calendar_today_outlined, size: 13, color: theme.textMuted),
              const SizedBox(width: 4),
              Text(
                '${skill['semester'] ?? ''} ${skill['tahun_pelajaran'] ?? ''}',
                style: TextStyle(fontSize: 12, color: theme.textMuted),
              ),
            ],
          ),
          if (skill['keterangan'] != null && skill['keterangan'].toString().isNotEmpty) ...[
            const SizedBox(height: 10),
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: theme.cardSubtle,
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: theme.border),
              ),
              child: Text(
                skill['keterangan'],
                style: TextStyle(fontSize: 12, color: theme.textPrimary, height: 1.3),
              ),
            ),
          ],
          const SizedBox(height: 10),
          Row(
            children: [
              Icon(Icons.school_outlined, size: 14, color: theme.textMuted),
              const SizedBox(width: 4),
              Text(
                'Penguji: $guru',
                style: TextStyle(fontSize: 11, color: theme.textMuted),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
