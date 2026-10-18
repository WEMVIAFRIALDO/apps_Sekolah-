import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/prestasi_controller.dart';
import '../services/theme_service.dart';

/// REQ-F-03: Halaman Input Prestasi untuk Siswa Aktif.
/// Form dinamis terintegrasi ThemeService (mendukung Mode Gelap & Mode Terang).
class PrestasiPage extends StatelessWidget {
  const PrestasiPage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = Get.find<PrestasiController>();
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
            'Input Prestasi',
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
                // ── Header Info ──────────────────────────────────────────
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: isDark ? const Color(0xFF1E3A8A).withValues(alpha: 0.3) : Colors.blue.shade50,
                    borderRadius: BorderRadius.circular(14),
                    border: Border.all(
                      color: isDark ? const Color(0xFF38BDF8).withValues(alpha: 0.3) : Colors.blue.shade100,
                    ),
                  ),
                  child: Row(
                    children: [
                      Icon(
                        Icons.info_outline_rounded,
                        color: isDark ? const Color(0xFF38BDF8) : Colors.blue.shade700,
                        size: 20,
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Text(
                          'Data yang dikirim akan berstatus Pending dan menunggu validasi dari Guru Pembina.',
                          style: TextStyle(
                            color: isDark ? const Color(0xFF93C5FD) : Colors.blue.shade900,
                            fontSize: 12.5,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 24),

                // ── Section: Detail Kegiatan ────────────────────────────
                _sectionTitle('Detail Kegiatan', theme),
                const SizedBox(height: 12),

                _buildTextField(
                  controller: c.namaKegiatanController,
                  label: 'Nama Kegiatan / Lomba *',
                  hint: 'cth. Olimpiade Sains Nasional (OSN) Matematika',
                  icon: Icons.emoji_events_outlined,
                  theme: theme,
                  validator: (v) =>
                      v == null || v.isEmpty ? 'Nama kegiatan wajib diisi' : null,
                ),
                const SizedBox(height: 14),

                _buildTextField(
                  controller: c.penyelenggaraController,
                  label: 'Penyelenggara *',
                  hint: 'cth. Kemendikbud RI',
                  icon: Icons.business_rounded,
                  theme: theme,
                  validator: (v) =>
                      v == null || v.isEmpty ? 'Nama penyelenggara wajib diisi' : null,
                ),
                const SizedBox(height: 14),

                _buildTextField(
                  controller: c.tahunController,
                  label: 'Tahun Kegiatan *',
                  hint: 'cth. 2024',
                  icon: Icons.calendar_month_rounded,
                  inputType: TextInputType.number,
                  theme: theme,
                  validator: (v) {
                    if (v == null || v.isEmpty) return 'Tahun wajib diisi';
                    final y = int.tryParse(v);
                    if (y == null || y < 2000 || y > 2030) {
                      return 'Masukkan tahun yang valid (2000 – 2030)';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 20),

                // ── Section: Tingkat & Peringkat ────────────────────────
                _sectionTitle('Tingkat & Capaian', theme),
                const SizedBox(height: 12),

                _buildDropdown(
                  label: 'Tingkat Kejuaraan *',
                  hint: 'Pilih tingkat kejuaraan',
                  icon: Icons.public_rounded,
                  theme: theme,
                  value: c.selectedTingkat.value.isEmpty ? null : c.selectedTingkat.value,
                  items: c.tingkatOptions,
                  onChanged: (val) => c.selectedTingkat.value = val ?? '',
                ),
                const SizedBox(height: 14),

                _buildDropdown(
                  label: 'Peringkat / Posisi *',
                  hint: 'Pilih peringkat yang diraih',
                  icon: Icons.military_tech_rounded,
                  theme: theme,
                  value: c.selectedPeringkat.value.isEmpty ? null : c.selectedPeringkat.value,
                  items: c.peringkatOptions,
                  onChanged: (val) => c.selectedPeringkat.value = val ?? '',
                ),
                const SizedBox(height: 14),

                _buildTextField(
                  controller: c.deskripsiController,
                  label: 'Deskripsi Singkat (opsional)',
                  hint: 'Ceritakan sedikit tentang kegiatan ini...',
                  icon: Icons.notes_rounded,
                  maxLines: 3,
                  theme: theme,
                ),
                const SizedBox(height: 20),

                // ── Section: Unggah Sertifikat ──────────────────────────
                _sectionTitle('Bukti Sertifikat', theme),
                const SizedBox(height: 12),

                _buildCertificateUploadBox(c, theme),
                const SizedBox(height: 32),

                // ── Tombol Submit ───────────────────────────────────────
                SizedBox(
                  width: double.infinity,
                  height: 52,
                  child: ElevatedButton.icon(
                    onPressed: c.isLoading.value ? null : c.submitPrestasi,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: theme.primary,
                      foregroundColor: Colors.white,
                      elevation: 4,
                      shadowColor: theme.primary.withValues(alpha: 0.5),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                    icon: c.isLoading.value
                        ? const SizedBox(
                            width: 20,
                            height: 20,
                            child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2),
                          )
                        : const Icon(Icons.send_rounded),
                    label: Text(
                      c.isLoading.value ? 'Mengirim...' : 'Kirim Prestasi',
                      style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
                const SizedBox(height: 12),

                Center(
                  child: Text(
                    'Prestasi akan masuk status Pending setelah dikirim.',
                    style: TextStyle(fontSize: 12, color: theme.textMuted),
                  ),
                ),
                const SizedBox(height: 24),
              ],
            ),
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

  Widget _buildDropdown({
    required String label,
    required String hint,
    required IconData icon,
    required String? value,
    required List<String> items,
    required ThemeService theme,
    required void Function(String?) onChanged,
  }) {
    return DropdownButtonFormField<String>(
      initialValue: value,
      onChanged: onChanged,
      isExpanded: true,
      dropdownColor: theme.card,
      style: TextStyle(color: theme.textPrimary, fontSize: 14),
      decoration: InputDecoration(
        labelText: label,
        labelStyle: TextStyle(color: theme.textMuted, fontSize: 13),
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
      hint: Text(hint, style: TextStyle(color: theme.textMuted, fontSize: 13)),
      items: items
          .map((e) => DropdownMenuItem(
                value: e,
                child: Text(e, style: TextStyle(color: theme.textPrimary)),
              ))
          .toList(),
    );
  }

  Widget _buildCertificateUploadBox(PrestasiController c, ThemeService theme) {
    final hasFile = c.selectedFileName.value.isNotEmpty;
    final isDark = theme.isDarkMode.value;

    return GestureDetector(
      onTap: c.pickCertificate,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        width: double.infinity,
        padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 20),
        decoration: BoxDecoration(
          color: hasFile
              ? (isDark ? const Color(0xFF064E3B).withValues(alpha: 0.3) : Colors.green.shade50)
              : theme.cardSubtle,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: hasFile
                ? (isDark ? const Color(0xFF10B981) : Colors.green.shade400)
                : theme.border,
            width: 1.5,
          ),
        ),
        child: Column(
          children: [
            Icon(
              hasFile ? Icons.check_circle_rounded : Icons.upload_file_rounded,
              size: 40,
              color: hasFile
                  ? (isDark ? const Color(0xFF34D399) : Colors.green.shade600)
                  : theme.primary,
            ),
            const SizedBox(height: 10),
            Text(
              hasFile ? c.selectedFileName.value : 'Ketuk untuk memilih file sertifikat',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w600,
                color: hasFile
                    ? (isDark ? const Color(0xFF6EE7B7) : Colors.green.shade800)
                    : theme.textPrimary,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              hasFile
                  ? 'Ketuk untuk mengganti file'
                  : 'Mendukung format PDF, JPG, PNG (maks. 5 MB)',
              style: TextStyle(fontSize: 11, color: theme.textMuted),
            ),
          ],
        ),
      ),
    );
  }
}
