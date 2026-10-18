import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../controllers/dashboard_controller.dart';
import '../routes/app_routes.dart';
import '../services/theme_service.dart';
import '../widgets/theme_segmented_switch.dart';

class DashboardPage extends StatelessWidget {
  const DashboardPage({super.key});

  @override
  Widget build(BuildContext context) {
    // Controller sudah di-inject via AppPages binding (Get.lazyPut)
    final DashboardController controller = Get.find<DashboardController>();
    final theme = ThemeService.to;

    return Obx(() {
      final isDark = theme.isDarkMode.value;

      return Scaffold(
        backgroundColor: theme.bg,
        appBar: AppBar(
          backgroundColor: theme.appBar,
          surfaceTintColor: Colors.transparent,
          elevation: 0,
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(1),
            child: Container(color: theme.border, height: 1),
          ),
          titleSpacing: 20,
          title: Row(
            children: [
              Image.asset(
                'assets/images/logo_salut.png',
                height: 38,
                fit: BoxFit.contain,
                errorBuilder: (context, error, stackTrace) => Icon(
                  Icons.school_rounded,
                  color: isDark ? const Color(0xFF38BDF8) : const Color(0xFF2563EB),
                  size: 26,
                ),
              ),
            ],
          ),
          actions: [
            // Switch Role Toggle (Untuk mempermudah simulasi/testing Dynamic UI)
            Container(
              margin: const EdgeInsets.symmetric(vertical: 8),
              decoration: BoxDecoration(
                color: theme.cardSubtle,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: theme.borderGlow),
              ),
              child: InkWell(
                borderRadius: BorderRadius.circular(20),
                onTap: controller.toggleRole,
                child: Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 10,
                    vertical: 4,
                  ),
                  child: Row(
                    children: [
                      Icon(
                        Icons.swap_horiz_rounded,
                        size: 16,
                        color: isDark ? const Color(0xFF38BDF8) : const Color(0xFF2563EB),
                      ),
                      const SizedBox(width: 4),
                      Text(
                        'Role: ${controller.currentRole.value}',
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w700,
                          color: isDark ? const Color(0xFF93C5FD) : const Color(0xFF1D4ED8),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            // Saklar Switch Theme Segmented (Konsisten dengan Web Admin)
            const ThemeSegmentedSwitch(),
            const SizedBox(width: 4),

            IconButton(
              onPressed: () {
                Get.snackbar(
                  'Notifikasi',
                  'Tidak ada pengumuman baru saat ini.',
                  snackPosition: SnackPosition.TOP,
                  backgroundColor: theme.card,
                  colorText: theme.textPrimary,
                );
              },
              icon: const Icon(Icons.notifications_none_rounded),
              color: theme.textMuted,
            ),
            const SizedBox(width: 8),
          ],
        ),
        body: RefreshIndicator(
          color: theme.primary,
          backgroundColor: theme.card,
          onRefresh: () async {
            await Future.wait([
              controller.fetchAchievements(),
              Future.delayed(const Duration(milliseconds: 400)),
            ]);
          },
          child: SingleChildScrollView(
            physics: const AlwaysScrollableScrollPhysics(),
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // 1. Kartu Profil Siswa / Alumni dengan Lencana Dinamis
                _buildProfileCard(context, controller, theme),
                const SizedBox(height: 20),

                // 2. Menu Aksi Utama Dinamis (Input Prestasi vs Tracer Study)
                if (controller.isSiswa)
                  _buildSiswaActionCard(context, controller)
                else
                  _buildAlumniActionCard(context, controller),

                const SizedBox(height: 24),

                // 3. Konten Utama Dinamis Berdasarkan Peran
                if (controller.isSiswa) ...[
                  _buildSiswaDashboardContent(context, controller, theme),
                ] else ...[
                  _buildAlumniDashboardContent(context, controller, theme),
                ],

                const SizedBox(height: 24),
              ],
            ),
          ),
        ),
        bottomNavigationBar: NavigationBar(
          selectedIndex: controller.selectedNavIndex.value,
          onDestinationSelected: controller.handleNavTap,
          elevation: 4,
          backgroundColor: theme.navBar,
          indicatorColor: theme.primary.withValues(alpha: 0.15),
          destinations: [
            NavigationDestination(
              icon: Icon(Icons.dashboard_outlined, color: theme.textMuted),
              selectedIcon: Icon(Icons.dashboard_rounded, color: theme.primary),
              label: 'Beranda',
            ),
            NavigationDestination(
              icon: Icon(Icons.folder_outlined, color: theme.textMuted),
              selectedIcon: Icon(Icons.folder_rounded, color: theme.primary),
              label: controller.isSiswa ? 'Prestasi' : 'Arsip Digital',
            ),
            NavigationDestination(
              icon: Icon(Icons.person_outline_rounded, color: theme.textMuted),
              selectedIcon: Icon(Icons.person_rounded, color: theme.primary),
              label: 'Profil',
            ),
          ],
        ),
      );
    });
  }

  // --- WIDGET PROFIL DENGAN LENCANA ROLE DINAMIS ---
  Widget _buildProfileCard(
    BuildContext context,
    DashboardController controller,
    ThemeService theme,
  ) {
    final isSiswa = controller.isSiswa;
    final isDark = theme.isDarkMode.value;

    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: theme.card,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: theme.border),
        boxShadow: theme.cardShadow,
      ),
      child: Row(
        children: [
          // Foto Profil / Avatar
          CircleAvatar(
            radius: 30,
            backgroundColor: isSiswa
                ? (isDark ? const Color(0xFF1E3A8A).withValues(alpha: 0.5) : const Color(0xFFDBEAFE))
                : (isDark ? const Color(0xFF065F46).withValues(alpha: 0.5) : const Color(0xFFD1FAE5)),
            child: Icon(
              Icons.person_rounded,
              size: 34,
              color: isSiswa
                  ? (isDark ? const Color(0xFF60A5FA) : const Color(0xFF2563EB))
                  : (isDark ? const Color(0xFF34D399) : const Color(0xFF059669)),
            ),
          ),
          const SizedBox(width: 16),
          // Biodata Pengguna
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  controller.userName.value,
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: theme.textPrimary,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'NISN: ${controller.userNisn.value}',
                  style: TextStyle(fontSize: 13, color: theme.textMuted),
                ),
                const SizedBox(height: 8),
                // Lencana Peran Dinamis (Dynamic Role Badge)
                AnimatedSwitcher(
                  duration: const Duration(milliseconds: 300),
                  child: Container(
                    key: ValueKey(controller.currentRole.value),
                    padding: const EdgeInsets.symmetric(
                      horizontal: 10,
                      vertical: 4,
                    ),
                    decoration: BoxDecoration(
                      color: isSiswa
                          ? (isDark ? const Color(0xFF064E3B).withValues(alpha: 0.5) : const Color(0xFFE8F5E9))
                          : (isDark ? const Color(0xFF312E81).withValues(alpha: 0.5) : const Color(0xFFE0E7FF)),
                      borderRadius: BorderRadius.circular(30),
                      border: Border.all(
                        color: isSiswa
                            ? (isDark ? const Color(0xFF059669) : Colors.green.shade400)
                            : (isDark ? const Color(0xFF6366F1) : Colors.indigo.shade300),
                      ),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          isSiswa
                              ? Icons.school_outlined
                              : Icons.verified_user_rounded,
                          size: 14,
                          color: isSiswa
                              ? (isDark ? const Color(0xFF6EE7B7) : Colors.green.shade800)
                              : (isDark ? const Color(0xFFA5B4FC) : Colors.indigo.shade800),
                        ),
                        const SizedBox(width: 6),
                        Text(
                          isSiswa ? 'Siswa Aktif' : 'Alumni',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w700,
                            color: isSiswa
                                ? (isDark ? const Color(0xFF6EE7B7) : Colors.green.shade800)
                                : (isDark ? const Color(0xFFA5B4FC) : Colors.indigo.shade800),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // --- WIDGET AKSI UTAMA: SISWA (INPUT PRESTASI) ---
  Widget _buildSiswaActionCard(
    BuildContext context,
    DashboardController controller,
  ) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.blue.shade700, Colors.blue.shade900],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.blue.shade800.withValues(alpha: 0.3),
            blurRadius: 12,
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
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.15),
                  shape: BoxShape.circle,
                ),
                child: const Icon(
                  Icons.emoji_events_rounded,
                  color: Colors.amberAccent,
                  size: 26,
                ),
              ),
              const SizedBox(width: 12),
              const Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Portofolio & Prestasi',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 2),
                    Text(
                      'Tabung sertifikat lomba sebelum lulus',
                      style: TextStyle(color: Colors.white70, fontSize: 12),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          ElevatedButton.icon(
            onPressed: controller.handleInputPrestasi,
            icon: const Icon(Icons.add_circle_outline_rounded, size: 18),
            label: const Text(
              'Input Prestasi',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.white,
              foregroundColor: Colors.blue.shade900,
              minimumSize: const Size(double.infinity, 44),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
              ),
              elevation: 0,
            ),
          ),
        ],
      ),
    );
  }

  // --- WIDGET AKSI UTAMA: ALUMNI (TRACER STUDY) ---
  Widget _buildAlumniActionCard(
    BuildContext context,
    DashboardController controller,
  ) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.indigo.shade600, const Color(0xFF1E1B4B)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.indigo.shade900.withValues(alpha: 0.3),
            blurRadius: 12,
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
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.15),
                  shape: BoxShape.circle,
                ),
                child: const Icon(
                  Icons.school_rounded,
                  color: Colors.tealAccent,
                  size: 26,
                ),
              ),
              const SizedBox(width: 12),
              const Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Layanan Alumni',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 2),
                    Text(
                      'Tracer study & unduh arsip ijazah/rapor',
                      style: TextStyle(color: Colors.white70, fontSize: 12),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 20),
          Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: controller.handleOpenTracerStudy,
                  icon: const Icon(Icons.edit_note_rounded, size: 18),
                  label: const Text('Tracer Study', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.tealAccent.shade400,
                    foregroundColor: const Color(0xFF0F172A),
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    elevation: 0,
                  ),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => Get.toNamed('/arsip'),
                  icon: const Icon(Icons.folder_shared_rounded, size: 18),
                  label: const Text('Arsip Dokumen', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: Colors.indigo.shade700,
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    elevation: 0,
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  // --- KONTEN DASHBOARD SISWA AKTIF ---
  Widget _buildSiswaDashboardContent(
    BuildContext context,
    DashboardController controller,
    ThemeService theme,
  ) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // 0. Banner Portofolio Keahlian SMK (SKPI)
        _buildSkillPortfolioBanner(context, theme),
        const SizedBox(height: 18),

        // Bagian Tabungan Nilai Rapor
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              'Tabungan Nilai Rapor',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: theme.textPrimary,
              ),
            ),
            TextButton(
              onPressed: () {},
              child: Text('Detail Nilai', style: TextStyle(color: theme.primary, fontWeight: FontWeight.w600)),
            ),
          ],
        ),
        const SizedBox(height: 8),
        SizedBox(
          height: 110,
          child: ListView.separated(
            scrollDirection: Axis.horizontal,
            itemCount: controller.semesterGrades.length,
            separatorBuilder: (_, _) => const SizedBox(width: 12),
            itemBuilder: (context, index) {
              final grade = controller.semesterGrades[index];
              return Container(
                width: 140,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: theme.card,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: theme.border),
                  boxShadow: theme.cardShadow,
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      grade['semester']!,
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: theme.textMuted,
                      ),
                    ),
                    const SizedBox(height: 6),
                    Text(
                      'Rata-rata: ${grade['average']}',
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.bold,
                        color: theme.primary,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      'Peringkat #${grade['rank']}',
                      style: TextStyle(
                        fontSize: 11,
                        color: Colors.green.shade600,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              );
            },
          ),
        ),

        const SizedBox(height: 24),

        // Bagian Riwayat Prestasi
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              'Prestasi Diajukan',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: theme.textPrimary,
              ),
            ),
            Row(
              children: [
                if (controller.isLoadingAchievements.value) ...[
                  SizedBox(
                    width: 12,
                    height: 12,
                    child: CircularProgressIndicator(
                      strokeWidth: 2,
                      color: theme.primary,
                    ),
                  ),
                  const SizedBox(width: 6),
                ],
                Text(
                  '${controller.achievements.length} Prestasi',
                  style: TextStyle(fontSize: 12, color: theme.textMuted),
                ),
              ],
            ),
          ],
        ),
        const SizedBox(height: 10),

        if (controller.achievements.isEmpty && !controller.isLoadingAchievements.value)
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 16),
            decoration: BoxDecoration(
              color: theme.card,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: theme.border),
              boxShadow: theme.cardShadow,
            ),
            child: Column(
              children: [
                Icon(
                  Icons.emoji_events_outlined,
                  size: 38,
                  color: theme.textMuted.withValues(alpha: 0.4),
                ),
                const SizedBox(height: 8),
                Text(
                  'Belum Ada Prestasi Diajukan',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: theme.textPrimary,
                    fontSize: 14,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'Tekan "Ajukan Prestasi" di atas untuk menambahkan portofolio Anda.',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    fontSize: 12,
                    color: theme.textMuted,
                  ),
                ),
              ],
            ),
          )
        else
          ListView.separated(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: controller.achievements.length,
            separatorBuilder: (_, _) => const SizedBox(height: 10),
            itemBuilder: (context, index) {
              final item = controller.achievements[index];
              final status = (item['status'] ?? 'Pending').toString();
              final isApproved = status == 'Approved';
              final isRejected = status == 'Rejected';

              final Color statusColor = isApproved
                  ? Colors.green.shade500
                  : (isRejected ? Colors.red.shade500 : Colors.amber.shade500);

              final Color statusBg = isApproved
                  ? Colors.green.withValues(alpha: 0.12)
                  : (isRejected
                      ? Colors.red.withValues(alpha: 0.12)
                      : Colors.amber.withValues(alpha: 0.12));

              final Color statusBorder = isApproved
                  ? Colors.green.withValues(alpha: 0.3)
                  : (isRejected
                      ? Colors.red.withValues(alpha: 0.3)
                      : Colors.amber.withValues(alpha: 0.3));

              final catatan = (item['catatan'] ?? '').toString();

              return Container(
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: theme.card,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: theme.border),
                  boxShadow: theme.cardShadow,
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          padding: const EdgeInsets.all(10),
                          decoration: BoxDecoration(
                            color: statusBg,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Icon(
                            isApproved
                                ? Icons.military_tech_rounded
                                : (isRejected
                                    ? Icons.cancel_outlined
                                    : Icons.access_time_rounded),
                            color: statusColor,
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                item['title'] ?? '',
                                style: TextStyle(
                                  fontSize: 13,
                                  fontWeight: FontWeight.w600,
                                  color: theme.textPrimary,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                '${item['category'] ?? ''} • Tahun ${item['year'] ?? ''}',
                                style: TextStyle(
                                  fontSize: 11,
                                  color: theme.textMuted,
                                ),
                              ),
                              if (item['penyelenggara'] != null &&
                                  item['penyelenggara'].toString().isNotEmpty) ...[
                                const SizedBox(height: 2),
                                Text(
                                  'Penyelenggara: ${item['penyelenggara']}',
                                  style: TextStyle(
                                    fontSize: 10,
                                    color: theme.textMuted.withValues(alpha: 0.8),
                                  ),
                                ),
                              ],
                            ],
                          ),
                        ),
                        const SizedBox(width: 8),
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 4,
                          ),
                          decoration: BoxDecoration(
                            color: statusBg,
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(color: statusBorder),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                isApproved
                                    ? Icons.check_circle_outline_rounded
                                    : (isRejected
                                        ? Icons.close_rounded
                                        : Icons.schedule_rounded),
                                size: 12,
                                color: statusColor,
                              ),
                              const SizedBox(width: 4),
                              Text(
                                status,
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                  color: statusColor,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    if (catatan.isNotEmpty) ...[
                      const SizedBox(height: 10),
                      Container(
                        width: double.infinity,
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: BoxDecoration(
                          color: theme.cardSubtle,
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: theme.border),
                        ),
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Icon(
                              Icons.feedback_outlined,
                              size: 13,
                              color: isRejected ? Colors.red.shade400 : theme.textMuted,
                            ),
                            const SizedBox(width: 6),
                            Expanded(
                              child: Text(
                                'Catatan Validator: $catatan',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontStyle: FontStyle.italic,
                                  color: isRejected ? Colors.red.shade400 : theme.textMuted,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ],
                ),
              );
            },
          ),
      ],
    );
  }

  // --- KONTEN DASHBOARD ALUMNI ---
  Widget _buildAlumniDashboardContent(
    BuildContext context,
    DashboardController controller,
    ThemeService theme,
  ) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // 0. Banner Portofolio Keahlian SMK (SKPI)
        _buildSkillPortfolioBanner(context, theme),
        const SizedBox(height: 18),

        // Judul Bagian Arsip Digital
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              'Riwayat Arsip Digital Pribadi',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: theme.textPrimary,
              ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
              decoration: BoxDecoration(
                color: theme.primary.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(6),
                border: Border.all(color: theme.primary.withValues(alpha: 0.3)),
              ),
              child: Text(
                'JWT Secured',
                style: TextStyle(
                  fontSize: 10,
                  fontWeight: FontWeight.w700,
                  color: theme.primary,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 6),
        Text(
          'Seluruh dokumen kelulusan final yang telah tervalidasi sekolah:',
          style: TextStyle(fontSize: 12, color: theme.textMuted),
        ),
        const SizedBox(height: 12),

        // Daftar Dokumen Digital (Ijazah, SKHUN, SKL, dll.)
        ListView.separated(
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          itemCount: controller.alumniArchives.length,
          separatorBuilder: (_, _) => const SizedBox(height: 10),
          itemBuilder: (context, index) {
            final doc = controller.alumniArchives[index];

            return Container(
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: theme.card,
                borderRadius: BorderRadius.circular(14),
                border: Border.all(color: theme.border),
                boxShadow: theme.cardShadow,
              ),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: Colors.red.withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Icon(
                      Icons.picture_as_pdf_rounded,
                      color: Colors.red.shade400,
                      size: 24,
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          doc['title']!,
                          style: TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w600,
                            color: theme.textPrimary,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          '${doc['type']} • ${doc['size']}',
                          style: TextStyle(
                            fontSize: 11,
                            color: theme.textMuted,
                          ),
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    style: IconButton.styleFrom(
                      backgroundColor: theme.cardSubtle,
                      foregroundColor: theme.primary,
                    ),
                    onPressed: () =>
                        controller.handleDownloadDocument(doc['title']!),
                    icon: const Icon(Icons.download_rounded, size: 20),
                    tooltip: 'Unduh Dokumen',
                  ),
                ],
              ),
            );
          },
        ),
      ],
    );
  }

  // --- WIDGET BANNER PORTOFOLIO KEAHLIAN SMK (SKPI) ---
  Widget _buildSkillPortfolioBanner(BuildContext context, ThemeService theme) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: theme.card,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: theme.border),
        boxShadow: theme.cardShadow,
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.purple.withValues(alpha: 0.15),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Icon(Icons.workspace_premium_rounded, color: Colors.purple.shade400, size: 28),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Portofolio Keahlian SMK',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                    color: theme.textPrimary,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  'Sertifikasi & SKPI Kejuruan',
                  style: TextStyle(fontSize: 12, color: theme.textMuted),
                ),
              ],
            ),
          ),
          ElevatedButton(
            onPressed: () => Get.toNamed(AppRoutes.skills),
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.purple.shade600,
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              elevation: 0,
            ),
            child: const Text('Buka SKPI', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
          ),
        ],
      ),
    );
  }
}
