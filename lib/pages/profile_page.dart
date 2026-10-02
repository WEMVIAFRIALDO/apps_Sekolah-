import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/profile_controller.dart';

/// Halaman Profil: menampilkan biodata pengguna dan tombol Logout.
class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = Get.find<ProfileController>();
    const primary = Color(0xFF1E3A5F);

    return Scaffold(
      backgroundColor: const Color(0xFFF8FAFC),
      appBar: AppBar(
        backgroundColor: Colors.white,
        surfaceTintColor: Colors.transparent,
        elevation: 0.5,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_ios_new_rounded, size: 20),
          onPressed: () => Get.back(),
        ),
        title: const Text(
          'Profil Saya',
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
        ),
        centerTitle: true,
      ),
      body: Obx(() {
        final isSiswa = c.userRole.value == 'Siswa';

        return SingleChildScrollView(
          child: Column(
            children: [
              // ── Hero Header ──────────────────────────────────────────
              Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 32, horizontal: 24),
                decoration: BoxDecoration(
                  color: Colors.white,
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withValues(alpha: 0.04),
                      blurRadius: 8,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Column(
                  children: [
                    // Avatar
                    CircleAvatar(
                      radius: 46,
                      backgroundColor: isSiswa
                          ? Colors.blue.shade100
                          : Colors.indigo.shade100,
                      child: Icon(
                        Icons.person_rounded,
                        size: 52,
                        color: isSiswa
                            ? Colors.blue.shade700
                            : Colors.indigo.shade700,
                      ),
                    ),
                    const SizedBox(height: 14),

                    // Nama
                    Text(
                      c.userName.value,
                      style: const TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF1E293B),
                      ),
                    ),
                    const SizedBox(height: 4),

                    // NISN
                    Text(
                      'NISN: ${c.userNisn.value}',
                      style: TextStyle(
                          fontSize: 14, color: Colors.grey.shade600),
                    ),
                    const SizedBox(height: 12),

                    // Lencana Peran
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 14, vertical: 6),
                      decoration: BoxDecoration(
                        color: isSiswa
                            ? const Color(0xFFE8F5E9)
                            : const Color(0xFFE0E7FF),
                        borderRadius: BorderRadius.circular(30),
                        border: Border.all(
                          color: isSiswa
                              ? Colors.green.shade400
                              : Colors.indigo.shade300,
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
                                ? Colors.green.shade800
                                : Colors.indigo.shade800,
                          ),
                          const SizedBox(width: 6),
                          Text(
                            isSiswa ? 'Siswa Aktif' : 'Alumni',
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w700,
                              color: isSiswa
                                  ? Colors.green.shade800
                                  : Colors.indigo.shade800,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 18),

                    // Tombol Ubah Password
                    OutlinedButton.icon(
                      onPressed: c.handleChangePassword,
                      icon: const Icon(Icons.lock_outline_rounded, size: 18),
                      label: const Text('Ubah Password'),
                      style: OutlinedButton.styleFrom(
                        foregroundColor: primary,
                        side: const BorderSide(color: Color(0xFF1E3A5F)),
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(30)),
                        padding: const EdgeInsets.symmetric(
                            horizontal: 20, vertical: 10),
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 12),

              // ── Biodata ──────────────────────────────────────────────
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const SizedBox(height: 8),
                    _sectionTitle('Informasi Akun'),
                    const SizedBox(height: 12),
                    _buildInfoCard(children: [
                      _infoRow(Icons.email_outlined, 'Email', c.userEmail.value),
                      _divider(),
                      _infoRow(Icons.phone_outlined, 'No. Telepon', c.userPhone.value),
                    ]),

                    const SizedBox(height: 20),
                    _sectionTitle('Informasi Sekolah'),
                    const SizedBox(height: 12),
                    _buildInfoCard(children: [
                      _infoRow(Icons.school_outlined, 'Sekolah', c.userSchool.value),
                      _divider(),
                      if (isSiswa) ...[
                        _infoRow(Icons.class_outlined, 'Kelas', c.userClass.value),
                        _divider(),
                      ],
                      _infoRow(Icons.calendar_today_outlined, 'Angkatan', c.userAngkatan.value),
                      _divider(),
                      _infoRow(Icons.access_time_rounded, 'Bergabung Sejak', c.userJoinDate.value),
                    ]),

                    const SizedBox(height: 28),

                    // ── Tombol Logout ────────────────────────────────────
                    SizedBox(
                      width: double.infinity,
                      height: 52,
                      child: OutlinedButton.icon(
                        onPressed: c.handleLogout,
                        icon: const Icon(Icons.logout_rounded, color: Colors.red),
                        label: const Text(
                          'Keluar dari Akun',
                          style: TextStyle(
                            color: Colors.red,
                            fontSize: 15,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        style: OutlinedButton.styleFrom(
                          side: const BorderSide(color: Colors.red, width: 1.5),
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(14)),
                        ),
                      ),
                    ),

                    const SizedBox(height: 8),
                    Center(
                      child: Text(
                        'SALUT v1.0.0 • SMA Negeri 1 Teladan',
                        style: TextStyle(
                            fontSize: 11, color: Colors.grey.shade400),
                      ),
                    ),
                    const SizedBox(height: 28),
                  ],
                ),
              ),
            ],
          ),
        );
      }),
    );
  }

  // ─── Helper Widgets ─────────────────────────────────────────────────────────

  Widget _sectionTitle(String text) => Text(
        text,
        style: const TextStyle(
          fontSize: 15,
          fontWeight: FontWeight.w700,
          color: Color(0xFF1E293B),
        ),
      );

  Widget _buildInfoCard({required List<Widget> children}) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.grey.shade200),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.02),
            blurRadius: 6,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Column(children: children),
    );
  }

  Widget _infoRow(IconData icon, String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      child: Row(
        children: [
          Icon(icon, size: 20, color: const Color(0xFF1E3A5F)),
          const SizedBox(width: 14),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(label,
                  style: TextStyle(fontSize: 11, color: Colors.grey.shade500)),
              const SizedBox(height: 2),
              Text(value,
                  style: const TextStyle(
                      fontSize: 14, fontWeight: FontWeight.w600)),
            ],
          ),
        ],
      ),
    );
  }

  Widget _divider() => Divider(
        height: 1,
        thickness: 1,
        color: Colors.grey.shade100,
        indent: 16,
        endIndent: 16,
      );
}
