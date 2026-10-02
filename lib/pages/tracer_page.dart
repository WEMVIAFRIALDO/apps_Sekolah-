import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/tracer_controller.dart';

/// REQ-F-08: Halaman Tracer Study untuk Alumni.
/// Form dinamis: field tambahan muncul berdasarkan status yang dipilih.
class TracerPage extends StatelessWidget {
  const TracerPage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = Get.find<TracerController>();
    const primary = Color(0xFF1E1B4B); // indigo gelap (warna tema alumni)

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
          'Tracer Study',
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
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
                            'Data ini membantu sekolah memantau rekam jejak '
                            'keberhasilan para lulusan.',
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
              _sectionTitle('Status Aktivitas Saat Ini'),
              const SizedBox(height: 6),
              Text(
                'Pilih status yang paling sesuai dengan kondisi Anda saat ini.',
                style: TextStyle(fontSize: 12, color: Colors.grey.shade600),
              ),
              const SizedBox(height: 12),

              Obx(() => Column(
                    children: c.statusOptions
                        .map((status) => _buildStatusCard(c, status))
                        .toList(),
                  )),
              const SizedBox(height: 20),

              // ── Section: Detail Instansi (Selalu Tampil jika ada status) ──
              Obx(() {
                if (c.selectedStatus.value.isEmpty) {
                  return const SizedBox.shrink();
                }
                return Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _sectionTitle(_getInstansiLabel(c.selectedStatus.value)),
                    const SizedBox(height: 12),

                    _buildTextField(
                      controller: c.namaInstansiController,
                      label: _getInstansiFieldLabel(c.selectedStatus.value),
                      hint: _getInstansiHint(c.selectedStatus.value),
                      icon: Icons.business_rounded,
                      validator: (v) => v == null || v.isEmpty
                          ? 'Field ini wajib diisi'
                          : null,
                    ),
                    const SizedBox(height: 14),

                    // ── Field Kondisional: Bekerja / Wirausaha ─────────
                    if (c.isBekerja) ...[
                      _buildTextField(
                        controller: c.jabatanController,
                        label: 'Jabatan / Posisi *',
                        hint: 'cth. Software Engineer, Marketing Manager',
                        icon: Icons.work_rounded,
                        validator: (v) => v == null || v.isEmpty
                            ? 'Jabatan wajib diisi'
                            : null,
                      ),
                      const SizedBox(height: 14),
                    ],

                    // ── Field Kondisional: Kuliah ──────────────────────
                    if (c.isKuliah) ...[
                      _buildTextField(
                        controller: c.prodiController,
                        label: 'Program Studi *',
                        hint: 'cth. Teknik Informatika, Manajemen',
                        icon: Icons.school_rounded,
                        validator: (v) => v == null || v.isEmpty
                            ? 'Program studi wajib diisi'
                            : null,
                      ),
                      const SizedBox(height: 14),
                    ],

                    _buildTextField(
                      controller: c.kotaController,
                      label: 'Kota / Lokasi',
                      hint: 'cth. Bandung, Jakarta, Surabaya',
                      icon: Icons.location_on_rounded,
                    ),
                    const SizedBox(height: 14),

                    _buildTextField(
                      controller: c.tahunMasukController,
                      label: 'Tahun Masuk / Bergabung',
                      hint: 'cth. 2024',
                      icon: Icons.calendar_month_rounded,
                      inputType: TextInputType.number,
                    ),
                    const SizedBox(height: 14),

                    _buildTextField(
                      controller: c.keteranganController,
                      label: 'Keterangan Tambahan (opsional)',
                      hint: 'Ceritakan perjalanan Anda...',
                      icon: Icons.notes_rounded,
                      maxLines: 3,
                    ),
                    const SizedBox(height: 32),

                    // ── Tombol Submit ──────────────────────────────────
                    Obx(() => SizedBox(
                          width: double.infinity,
                          height: 52,
                          child: FilledButton.icon(
                            onPressed: c.isLoading.value
                                ? null
                                : c.submitTracerStudy,
                            style: FilledButton.styleFrom(
                              backgroundColor: primary,
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(14)),
                            ),
                            icon: c.isLoading.value
                                ? const SizedBox(
                                    width: 20,
                                    height: 20,
                                    child: CircularProgressIndicator(
                                        color: Colors.white, strokeWidth: 2),
                                  )
                                : const Icon(Icons.save_rounded),
                            label: Text(
                              c.isLoading.value ? 'Menyimpan...' : 'Simpan Data Tracer Study',
                              style: const TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                          ),
                        )),
                    const SizedBox(height: 24),
                  ],
                );
              }),
            ],
          ),
        ),
      ),
    );
  }

  // ─── Helper: Status Card ────────────────────────────────────────────────────
  Widget _buildStatusCard(TracerController c, String status) {
    final color = _statusColor(status);

    return Obx(() {
      final selected = c.selectedStatus.value == status;
      return GestureDetector(
        onTap: () => c.selectedStatus.value = status,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          margin: const EdgeInsets.only(bottom: 10),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          decoration: BoxDecoration(
            color: selected ? color.withValues(alpha: 0.08) : Colors.white,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: selected ? color : Colors.grey.shade300,
              width: selected ? 2 : 1,
            ),
          ),
          child: Row(
            children: [
              Icon(
                _statusIcon(status),
                color: selected ? color : Colors.grey.shade400,
                size: 22,
              ),
              const SizedBox(width: 12),
              Text(
                status,
                style: TextStyle(
                  fontSize: 14,
                  fontWeight:
                      selected ? FontWeight.bold : FontWeight.w500,
                  color:
                      selected ? color : const Color(0xFF334155),
                ),
              ),
              const Spacer(),
              Icon(
                selected
                    ? Icons.check_circle_rounded
                    : Icons.radio_button_unchecked_rounded,
                color: selected ? color : Colors.grey.shade300,
              ),
            ],
          ),
        ),
      );
    });
  }

  // ─── Helper: TextField ──────────────────────────────────────────────────────
  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    required String hint,
    required IconData icon,
    String? Function(String?)? validator,
    TextInputType inputType = TextInputType.text,
    int maxLines = 1,
  }) {
    return TextFormField(
      controller: controller,
      validator: validator,
      keyboardType: inputType,
      maxLines: maxLines,
      decoration: InputDecoration(
        labelText: label,
        hintText: hint,
        prefixIcon: Icon(icon, size: 20),
        filled: true,
        fillColor: Colors.white,
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: BorderSide(color: Colors.grey.shade300),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide:
              const BorderSide(color: Color(0xFF1E1B4B), width: 1.8),
        ),
        contentPadding:
            const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      ),
    );
  }

  Widget _sectionTitle(String text) => Text(
        text,
        style: const TextStyle(
          fontSize: 15,
          fontWeight: FontWeight.w700,
          color: Color(0xFF1E293B),
        ),
      );

  // ─── Helper: Data Mapping ───────────────────────────────────────────────────
  Color _statusColor(String status) {
    switch (status) {
      case 'Bekerja':        return Colors.green.shade700;
      case 'Kuliah / Melanjutkan Studi': return Colors.blue.shade700;
      case 'Wirausaha':      return Colors.orange.shade700;
      case 'Mencari Kerja':  return Colors.purple.shade600;
      default:               return Colors.grey.shade600;
    }
  }

  IconData _statusIcon(String status) {
    switch (status) {
      case 'Bekerja':        return Icons.work_rounded;
      case 'Kuliah / Melanjutkan Studi': return Icons.school_rounded;
      case 'Wirausaha':      return Icons.store_rounded;
      case 'Mencari Kerja':  return Icons.search_rounded;
      default:               return Icons.hourglass_empty_rounded;
    }
  }

  String _getInstansiLabel(String status) {
    switch (status) {
      case 'Bekerja':        return 'Data Pekerjaan';
      case 'Kuliah / Melanjutkan Studi': return 'Data Perguruan Tinggi';
      case 'Wirausaha':      return 'Data Usaha';
      case 'Mencari Kerja':  return 'Keterangan';
      default:               return 'Keterangan Tambahan';
    }
  }

  String _getInstansiFieldLabel(String status) {
    switch (status) {
      case 'Bekerja':        return 'Nama Perusahaan *';
      case 'Kuliah / Melanjutkan Studi': return 'Nama Perguruan Tinggi *';
      case 'Wirausaha':      return 'Nama Usaha *';
      default:               return 'Keterangan *';
    }
  }

  String _getInstansiHint(String status) {
    switch (status) {
      case 'Bekerja':        return 'cth. PT. Telkom Indonesia';
      case 'Kuliah / Melanjutkan Studi': return 'cth. Universitas Lampung';
      case 'Wirausaha':      return 'cth. Toko Online XYZ';
      default:               return 'Jelaskan kondisi Anda saat ini...';
    }
  }
}
