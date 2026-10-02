import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../controllers/prestasi_controller.dart';

/// REQ-F-03: Halaman Input Prestasi untuk Siswa Aktif.
/// Form berisi: nama kegiatan, penyelenggara, tingkat, peringkat,
/// tahun, deskripsi singkat, dan tombol unggah sertifikat.
class PrestasiPage extends StatelessWidget {
  const PrestasiPage({super.key});

  @override
  Widget build(BuildContext context) {
    final c = Get.find<PrestasiController>();
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
          'Input Prestasi',
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
              // ── Header Info ──────────────────────────────────────────
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.blue.shade50,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: Colors.blue.shade100),
                ),
                child: Row(
                  children: [
                    Icon(Icons.info_outline_rounded,
                        color: Colors.blue.shade700, size: 20),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(
                        'Data yang dikirim akan berstatus Pending dan '
                        'menunggu validasi dari Guru Pembina.',
                        style: TextStyle(
                            color: Colors.blue.shade800, fontSize: 12.5),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 24),

              // ── Section: Detail Kegiatan ────────────────────────────
              _sectionTitle('Detail Kegiatan'),
              const SizedBox(height: 12),

              _buildTextField(
                controller: c.namaKegiatanController,
                label: 'Nama Kegiatan / Lomba *',
                hint: 'cth. Olimpiade Sains Nasional (OSN) Matematika',
                icon: Icons.emoji_events_outlined,
                validator: (v) =>
                    v == null || v.isEmpty ? 'Nama kegiatan wajib diisi' : null,
              ),
              const SizedBox(height: 14),

              _buildTextField(
                controller: c.penyelenggaraController,
                label: 'Penyelenggara *',
                hint: 'cth. Kemendikbud RI',
                icon: Icons.business_rounded,
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
              _sectionTitle('Tingkat & Capaian'),
              const SizedBox(height: 12),

              Obx(() => _buildDropdown(
                    label: 'Tingkat Kejuaraan *',
                    hint: 'Pilih tingkat kejuaraan',
                    icon: Icons.public_rounded,
                    value: c.selectedTingkat.value.isEmpty
                        ? null
                        : c.selectedTingkat.value,
                    items: c.tingkatOptions,
                    onChanged: (val) => c.selectedTingkat.value = val ?? '',
                  )),
              const SizedBox(height: 14),

              Obx(() => _buildDropdown(
                    label: 'Peringkat / Posisi *',
                    hint: 'Pilih peringkat yang diraih',
                    icon: Icons.military_tech_rounded,
                    value: c.selectedPeringkat.value.isEmpty
                        ? null
                        : c.selectedPeringkat.value,
                    items: c.peringkatOptions,
                    onChanged: (val) => c.selectedPeringkat.value = val ?? '',
                  )),
              const SizedBox(height: 14),

              _buildTextField(
                controller: c.deskripsiController,
                label: 'Deskripsi Singkat (opsional)',
                hint: 'Ceritakan sedikit tentang kegiatan ini...',
                icon: Icons.notes_rounded,
                maxLines: 3,
              ),
              const SizedBox(height: 20),

              // ── Section: Unggah Sertifikat ──────────────────────────
              _sectionTitle('Bukti Sertifikat'),
              const SizedBox(height: 12),

              Obx(() => _buildCertificateUploadBox(c)),
              const SizedBox(height: 32),

              // ── Tombol Submit ───────────────────────────────────────
              Obx(() => SizedBox(
                    width: double.infinity,
                    height: 52,
                    child: FilledButton.icon(
                      onPressed: c.isLoading.value ? null : c.submitPrestasi,
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
                          : const Icon(Icons.send_rounded),
                      label: Text(
                        c.isLoading.value ? 'Mengirim...' : 'Kirim Prestasi',
                        style: const TextStyle(
                            fontSize: 16, fontWeight: FontWeight.bold),
                      ),
                    ),
                  )),
              const SizedBox(height: 12),

              Center(
                child: Text(
                  'Prestasi akan masuk status Pending setelah dikirim.',
                  style: TextStyle(fontSize: 12, color: Colors.grey.shade500),
                ),
              ),
              const SizedBox(height: 24),
            ],
          ),
        ),
      ),
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
          borderSide: const BorderSide(color: Color(0xFF1E3A5F), width: 1.8),
        ),
        contentPadding:
            const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      ),
    );
  }

  Widget _buildDropdown({
    required String label,
    required String hint,
    required IconData icon,
    required String? value,
    required List<String> items,
    required void Function(String?) onChanged,
  }) {
    return DropdownButtonFormField<String>(
      initialValue: value,
      onChanged: onChanged,
      isExpanded: true,
      decoration: InputDecoration(
        labelText: label,
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
          borderSide: const BorderSide(color: Color(0xFF1E3A5F), width: 1.8),
        ),
        contentPadding:
            const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      ),
      hint: Text(hint, style: TextStyle(color: Colors.grey.shade500)),
      items: items
          .map((e) => DropdownMenuItem(value: e, child: Text(e)))
          .toList(),
    );
  }

  Widget _buildCertificateUploadBox(PrestasiController c) {
    final hasFile = c.selectedFileName.value.isNotEmpty;
    return GestureDetector(
      onTap: c.pickCertificate,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        width: double.infinity,
        padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 20),
        decoration: BoxDecoration(
          color: hasFile ? Colors.green.shade50 : Colors.grey.shade50,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: hasFile ? Colors.green.shade400 : Colors.grey.shade300,
            width: 1.8,
            style: BorderStyle.solid,
          ),
        ),
        child: Column(
          children: [
            Icon(
              hasFile
                  ? Icons.check_circle_rounded
                  : Icons.upload_file_rounded,
              size: 40,
              color: hasFile ? Colors.green.shade600 : Colors.grey.shade400,
            ),
            const SizedBox(height: 10),
            Text(
              hasFile ? c.selectedFileName.value : 'Ketuk untuk memilih file',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w600,
                color: hasFile ? Colors.green.shade800 : Colors.grey.shade600,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              hasFile
                  ? 'Ketuk untuk mengganti file'
                  : 'Mendukung format PDF, JPG, PNG (maks. 5 MB)',
              style: TextStyle(fontSize: 11, color: Colors.grey.shade500),
            ),
          ],
        ),
      ),
    );
  }
}
