import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/profile_controller.dart';
import '../services/theme_service.dart';

/// Halaman Profil: menampilkan biodata pengguna dan tombol Logout secara adaptif terhadap tema.
class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = Get.find<ProfileController>();
    final theme = ThemeService.to;

    return Obx(() {
      final isDark = theme.isDarkMode.value;
      final isSiswa = c.userRole.value == 'Siswa';

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
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios_new_rounded, size: 20, color: theme.textPrimary),
            onPressed: () => Get.back(),
          ),
          title: Text(
            'Profil Saya',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: theme.textPrimary,
            ),
          ),
          centerTitle: true,
        ),
        body: SingleChildScrollView(
          child: Column(
            children: [
              // ── Hero Header ──────────────────────────────────────────
              Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 32, horizontal: 24),
                decoration: BoxDecoration(
                  color: theme.card,
                  border: Border(bottom: BorderSide(color: theme.border)),
                  boxShadow: theme.cardShadow,
                ),
                child: Column(
                  children: [
                    // Avatar
                    CircleAvatar(
                      radius: 46,
                      backgroundColor: isSiswa
                          ? (isDark ? const Color(0xFF1E3A8A).withValues(alpha: 0.5) : const Color(0xFFDBEAFE))
                          : (isDark ? const Color(0xFF065F46).withValues(alpha: 0.5) : const Color(0xFFD1FAE5)),
                      child: Icon(
                        Icons.person_rounded,
                        size: 52,
                        color: isSiswa
                            ? (isDark ? const Color(0xFF60A5FA) : const Color(0xFF2563EB))
                            : (isDark ? const Color(0xFF34D399) : const Color(0xFF059669)),
                      ),
                    ),
                    const SizedBox(height: 14),

                    // Nama
                    Text(
                      c.userName.value,
                      style: TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                        color: theme.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 4),

                    // NISN
                    Text(
                      'NISN: ${c.userNisn.value}',
                      style: TextStyle(
                        fontSize: 14,
                        color: theme.textMuted,
                      ),
                    ),
                    const SizedBox(height: 12),

                    // Lencana Peran
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
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
                            isSiswa ? Icons.school_outlined : Icons.verified_user_rounded,
                            size: 14,
                            color: isSiswa
                                ? (isDark ? const Color(0xFF6EE7B7) : Colors.green.shade800)
                                : (isDark ? const Color(0xFFA5B4FC) : Colors.indigo.shade800),
                          ),
                          const SizedBox(width: 6),
                          Text(
                            isSiswa ? 'Siswa Aktif' : 'Alumni',
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w700,
                              color: isSiswa
                                  ? (isDark ? const Color(0xFF6EE7B7) : Colors.green.shade800)
                                  : (isDark ? const Color(0xFFA5B4FC) : Colors.indigo.shade800),
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 18),

                    // Tombol Ubah Password
                    OutlinedButton.icon(
                      onPressed: c.handleChangePassword,
                      icon: Icon(Icons.lock_outline_rounded, size: 18, color: theme.primary),
                      label: Text('Ubah Password', style: TextStyle(color: theme.primary, fontWeight: FontWeight.w600)),
                      style: OutlinedButton.styleFrom(
                        side: BorderSide(color: theme.primary.withValues(alpha: 0.6)),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 16),

              // ── Biodata ──────────────────────────────────────────────
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _sectionTitle('Informasi Akun', theme),
                    const SizedBox(height: 10),
                    _buildInfoCard(
                      theme: theme,
                      children: [
                        _infoRow(Icons.email_outlined, 'Email', c.userEmail.value, theme),
                        _divider(theme),
                        _infoRow(Icons.phone_outlined, 'No. Telepon', c.userPhone.value, theme),
                      ],
                    ),

                    const SizedBox(height: 20),
                    _sectionTitle('Informasi Sekolah', theme),
                    const SizedBox(height: 10),
                    _buildInfoCard(
                      theme: theme,
                      children: [
                        _infoRow(Icons.school_outlined, 'Sekolah', c.userSchool.value, theme),
                        _divider(theme),
                        if (isSiswa) ...[
                          _infoRow(Icons.class_outlined, 'Kelas', c.userClass.value, theme),
                          _divider(theme),
                        ],
                        _infoRow(Icons.calendar_today_outlined, 'Angkatan', c.userAngkatan.value, theme),
                        _divider(theme),
                        _infoRow(Icons.access_time_rounded, 'Bergabung Sejak', c.userJoinDate.value, theme),
                      ],
                    ),

                    const SizedBox(height: 28),

                    // ── Tombol Logout ────────────────────────────────────
                    SizedBox(
                      width: double.infinity,
                      height: 50,
                      child: OutlinedButton.icon(
                        onPressed: c.handleLogout,
                        icon: const Icon(Icons.logout_rounded, color: Color(0xFFEF4444)),
                        label: const Text(
                          'Keluar dari Akun',
                          style: TextStyle(
                            color: Color(0xFFEF4444),
                            fontSize: 15,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        style: OutlinedButton.styleFrom(
                          side: const BorderSide(color: Color(0xFFEF4444), width: 1.4),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                        ),
                      ),
                    ),

                    const SizedBox(height: 14),
                    Center(
                      child: Text(
                        'SALUT v1.0.0 • SMK Negeri 1 Teladan',
                        style: TextStyle(fontSize: 11, color: theme.textMuted),
                      ),
                    ),
                    const SizedBox(height: 32),
                  ],
                ),
              ),
            ],
          ),
        ),
      );
    });
  }

  // ─── Helper Widgets ─────────────────────────────────────────────────────────

  Widget _sectionTitle(String text, ThemeService theme) => Text(
        text,
        style: TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.w700,
          color: theme.textPrimary,
        ),
      );

  Widget _buildInfoCard({required List<Widget> children, required ThemeService theme}) {
    return Container(
      decoration: BoxDecoration(
        color: theme.card,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: theme.border),
        boxShadow: theme.cardShadow,
      ),
      child: Column(children: children),
    );
  }

  Widget _infoRow(IconData icon, String label, String value, ThemeService theme) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: theme.cardSubtle,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Icon(icon, size: 18, color: theme.primary),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  label,
                  style: TextStyle(fontSize: 11, color: theme.textMuted),
                ),
                const SizedBox(height: 2),
                Text(
                  value,
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                    color: theme.textPrimary,
                  ),
                  overflow: TextOverflow.ellipsis,
                  maxLines: 1,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _divider(ThemeService theme) => Divider(
        height: 1,
        thickness: 1,
        color: theme.border,
        indent: 16,
        endIndent: 16,
      );
}
