import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/tracer_controller.dart';
import '../services/theme_service.dart';

/// REQ-F-08: Halaman Tracer Study untuk Alumni.
/// Form dinamis terintegrasi ThemeService (mendukung Mode Gelap & Mode Terang).
class TracerPage extends StatelessWidget {
  const TracerPage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = Get.find<TracerController>();
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
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios_new_rounded, size: 20, color: theme.textPrimary),
            onPressed: () => Get.back(),
          ),
          title: Text(
            'Tracer Study',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: theme.textPrimary,
            ),
          ),
          centerTitle: true,
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Form(
            key: c.formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // ── Header / Hero Card ───────────────────────────────────
                Container(
                  padding: const EdgeInsets.all(18),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [Colors.indigo.shade600, const Color(0xFF1E1B4B)],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(16),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.indigo.shade900.withValues(alpha: 0.3),
                        blurRadius: 10,
                        offset: const Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: Colors.white.withValues(alpha: 0.15),
                          shape: BoxShape.circle,
                        ),
                        child: const Icon(
                          Icons.assignment_turned_in_rounded,
                          color: Colors.tealAccent,
                          size: 28,
                        ),
                      ),
                      const SizedBox(width: 14),
                      const Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'Pelacakan Alumni',
                              style: TextStyle(
                                color: Colors.white,
                                fontSize: 16,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            SizedBox(height: 4),
                            Text(
                              'Data ini membantu sekolah memantau rekam jejak keberhasilan para lulusan.',
                              style: TextStyle(color: Colors.white70, fontSize: 12),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 24),

                // ── Section: Status Aktivitas (PILIHAN UTAMA) ────────────
                _sectionTitle('Status Aktivitas Saat Ini', theme),
                const SizedBox(height: 6),
                Text(
                  'Pilih status yang paling sesuai dengan kondisi Anda saat ini.',
                  style: TextStyle(fontSize: 12, color: theme.textMuted),
                ),
                const SizedBox(height: 12),

                Column(
                  children: c.statusOptions
                      .map((status) => _buildStatusCard(c, status, theme))
                      .toList(),
                ),
                const SizedBox(height: 20),

                // ── Section: Detail Instansi (Kondisional sesuai status) ──
                if (c.selectedStatus.value.isNotEmpty) ...[
                  _sectionTitle(_getInstansiLabel(c.selectedStatus.value), theme),
                  const SizedBox(height: 12),

                  _buildTextField(
                    controller: c.namaInstansiController,
                    label: _getInstansiFieldLabel(c.selectedStatus.value),
                    hint: _getInstansiHint(c.selectedStatus.value),
                    icon: Icons.business_rounded,
                    theme: theme,
                    validator: (v) => v == null || v.isEmpty ? 'Field ini wajib diisi' : null,
                  ),
                  const SizedBox(height: 14),

                  // Field Kondisional: Bekerja / Wirausaha
                  if (c.isBekerja) ...[
                    _buildTextField(
                      controller: c.jabatanController,
                      label: 'Jabatan / Posisi *',
                      hint: 'cth. Network Engineer, Web Developer',
                      icon: Icons.work_rounded,
                      theme: theme,
                      validator: (v) => v == null || v.isEmpty ? 'Jabatan wajib diisi' : null,
                    ),
                    const SizedBox(height: 14),
                  ],

                  // Field Kondisional: Kuliah
                  if (c.isKuliah) ...[
                    _buildTextField(
                      controller: c.prodiController,
                      label: 'Program Studi *',
                      hint: 'cth. Teknik Informatika, Sistem Informasi',
                      icon: Icons.school_rounded,
                      theme: theme,
                      validator: (v) => v == null || v.isEmpty ? 'Program studi wajib diisi' : null,
                    ),
                    const SizedBox(height: 14),
                  ],

                  _buildTextField(
                    controller: c.kotaController,
                    label: 'Kota / Lokasi',
                    hint: 'cth. Bandar Lampung, Jakarta, Bandung',
                    icon: Icons.location_on_rounded,
                    theme: theme,
                  ),
                  const SizedBox(height: 14),

                  _buildTextField(
                    controller: c.tahunMasukController,
                    label: 'Tahun Masuk / Bergabung',
                    hint: 'cth. 2024',
                    icon: Icons.calendar_month_rounded,
                    inputType: TextInputType.number,
                    theme: theme,
                  ),
                  const SizedBox(height: 14),

                  _buildTextField(
                    controller: c.keteranganController,
                    label: 'Keterangan Tambahan (opsional)',
                    hint: 'Ceritakan perjalanan Anda...',
                    icon: Icons.notes_rounded,
                    maxLines: 3,
                    theme: theme,
                  ),
                  const SizedBox(height: 32),

                  // ── Tombol Submit ──────────────────────────────────
                  SizedBox(
                    width: double.infinity,
                    height: 52,
                    child: ElevatedButton.icon(
                      onPressed: c.isLoading.value ? null : c.submitTracerStudy,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: isDark ? const Color(0xFF6366F1) : const Color(0xFF1E1B4B),
                        foregroundColor: Colors.white,
                        elevation: 4,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                      ),
                      icon: c.isLoading.value
                          ? const SizedBox(
                              width: 20,
                              height: 20,
                              child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2),
                            )
                          : const Icon(Icons.save_rounded),
                      label: Text(
                        c.isLoading.value ? 'Menyimpan...' : 'Simpan Data Tracer Study',
                        style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                  const SizedBox(height: 24),
                ],
              ],
            ),
          ),
        ),
      );
    });
  }

  // ─── Helper: Status Card ────────────────────────────────────────────────────
  Widget _buildStatusCard(TracerController c, String status, ThemeService theme) {
    final color = _statusColor(status);
    final selected = c.selectedStatus.value == status;
    final isDark = theme.isDarkMode.value;

    return GestureDetector(
      onTap: () => c.selectedStatus.value = status,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(
          color: selected
              ? (isDark ? color.withValues(alpha: 0.18) : color.withValues(alpha: 0.08))
              : theme.cardSubtle,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: selected ? color : theme.border,
            width: selected ? 2 : 1,
          ),
        ),
        child: Row(
          children: [
            Icon(
              _statusIcon(status),
              color: selected ? color : theme.textMuted,
              size: 22,
            ),
            const SizedBox(width: 12),
            Text(
              status,
              style: TextStyle(
                fontSize: 14,
                fontWeight: selected ? FontWeight.bold : FontWeight.w500,
                color: selected ? (isDark ? Colors.white : color) : theme.textPrimary,
              ),
            ),
            const Spacer(),
            Icon(
              selected ? Icons.check_circle_rounded : Icons.radio_button_unchecked_rounded,
              color: selected ? color : theme.border,
            ),
          ],
        ),
      ),
    );
  }

  // ─── Helper: TextField ──────────────────────────────────────────────────────
  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    required String hint,
    required IconData icon,
    required ThemeService theme,
    String? Function(String?)? validator,
    TextInputType inputType = TextInputType.text,
    int maxLines = 1,
  }) {
    return TextFormField(
      controller: controller,
      validator: validator,
      keyboardType: inputType,
      maxLines: maxLines,
      style: TextStyle(color: theme.textPrimary, fontSize: 14),
      decoration: InputDecoration(
        labelText: label,
        labelStyle: TextStyle(color: theme.textMuted, fontSize: 13),
        hintText: hint,
        hintStyle: TextStyle(color: theme.textMuted.withValues(alpha: 0.6), fontSize: 13),
        prefixIcon: Icon(icon, size: 20, color: theme.primary),
        filled: true,
        fillColor: theme.cardSubtle,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide(color: theme.border),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide(color: theme.border),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide(color: theme.primary, width: 1.8),
        ),
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      ),
    );
  }

  Widget _sectionTitle(String text, ThemeService theme) => Text(
        text,
        style: TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.w700,
          color: theme.textPrimary,
        ),
      );

  // ─── Helper: Data Mapping ───────────────────────────────────────────────────
  Color _statusColor(String status) {
    switch (status) {
      case 'Bekerja':                    return const Color(0xFF10B981);
      case 'Kuliah / Melanjutkan Studi': return const Color(0xFF38BDF8);
      case 'Wirausaha':                  return const Color(0xFFF59E0B);
      case 'Mencari Kerja':              return const Color(0xFFA855F7);
      default:                           return const Color(0xFF94A3B8);
    }
  }

  IconData _statusIcon(String status) {
    switch (status) {
      case 'Bekerja':                    return Icons.work_rounded;
      case 'Kuliah / Melanjutkan Studi': return Icons.school_rounded;
      case 'Wirausaha':                  return Icons.store_rounded;
      case 'Mencari Kerja':              return Icons.search_rounded;
      default:                           return Icons.hourglass_empty_rounded;
    }
  }

  String _getInstansiLabel(String status) {
    switch (status) {
      case 'Bekerja':                    return 'Data Pekerjaan';
      case 'Kuliah / Melanjutkan Studi': return 'Data Perguruan Tinggi';
      case 'Wirausaha':                  return 'Data Usaha';
      case 'Mencari Kerja':              return 'Keterangan';
      default:                           return 'Keterangan Tambahan';
    }
  }

  String _getInstansiFieldLabel(String status) {
    switch (status) {
      case 'Bekerja':                    return 'Nama Perusahaan *';
      case 'Kuliah / Melanjutkan Studi': return 'Nama Perguruan Tinggi *';
      case 'Wirausaha':                  return 'Nama Usaha *';
      default:                           return 'Keterangan *';
    }
  }

  String _getInstansiHint(String status) {
    switch (status) {
      case 'Bekerja':                    return 'cth. PT. Telkom Indonesia';
      case 'Kuliah / Melanjutkan Studi': return 'cth. Universitas Lampung';
      case 'Wirausaha':                  return 'cth. Bengkel Komputer & Jaringan';
      default:                           return 'Jelaskan kondisi Anda saat ini...';
    }
  }
}
