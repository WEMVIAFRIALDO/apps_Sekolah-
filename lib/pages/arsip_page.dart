import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:dio/dio.dart';
import 'package:path_provider/path_provider.dart';
import 'package:open_filex/open_filex.dart';
import 'dart:io';

import '../services/api_service.dart';
import '../services/auth_service.dart';

/// REQ-F-09: Halaman Arsip Dokumen Digital untuk Alumni.
/// Alumni dapat melihat dan mengunduh:
///   - Ijazah, SKL, SKHUN, Rapor (dari graduation_docs)
/// Semua akses dilindungi JWT Bearer Token (REQ-NF-01).
class ArsipPage extends StatefulWidget {
  const ArsipPage({super.key});

  @override
  State<ArsipPage> createState() => _ArsipPageState();
}

class _ArsipPageState extends State<ArsipPage> {
  final _api  = ApiService();
  final _auth = AuthService();

  List<Map<String, dynamic>> _dokumen = [];
  bool   _isLoading = true;
  String? _error;

  // Track progress unduhan per dokumen id
  final Map<int, double> _downloadProgress = {};
  final Map<int, bool>   _isDownloading    = {};

  @override
  void initState() {
    super.initState();
    _loadArsip();
  }

  Future<void> _loadArsip() async {
    setState(() { _isLoading = true; _error = null; });
    try {
      final res = await _api.get('/arsip');
      final data = res.data as Map<String, dynamic>;
      final list = (data['data'] as List?) ?? [];
      setState(() {
        _dokumen  = list.map((e) => Map<String, dynamic>.from(e as Map)).toList();
        _isLoading = false;
      });
    } on DioException catch (e) {
      setState(() {
        _error = ApiService.parseError(e);
        _isLoading = false;
      });
    }
  }

  Future<void> _downloadDokumen(Map<String, dynamic> doc) async {
    final id        = doc['id'] as int;
    final docType   = (doc['doc_type'] ?? 'dokumen') as String;
    final title     = (doc['title'] ?? docType) as String;

    setState(() {
      _isDownloading[id] = true;
      _downloadProgress[id] = 0.0;
    });

    try {
      final dir      = await getApplicationDocumentsDirectory();
      final savePath = '${dir.path}/salut_${docType}_$id.pdf';

      await _api.downloadFile(
        url: '$kBaseUrl/arsip/$id/download',
        savePath: savePath,
        onProgress: (p) {
          if (mounted) setState(() => _downloadProgress[id] = p);
        },
      );

      setState(() { _isDownloading[id] = false; });

      // Buka file langsung setelah unduh
      final result = await OpenFilex.open(savePath);
      if (result.type != ResultType.done) {
        _showSnack('File disimpan di: $savePath', isError: false);
      }
    } catch (e) {
      setState(() { _isDownloading[id] = false; });
      _showSnack('Gagal mengunduh $title: ${e.toString()}', isError: true);
    }
  }

  void _showSnack(String msg, {bool isError = false}) {
    Get.snackbar(
      isError ? 'Gagal' : 'Sukses',
      msg,
      backgroundColor: isError ? Colors.red.shade800 : Colors.green.shade700,
      colorText:       Colors.white,
      snackPosition:   SnackPosition.BOTTOM,
      margin:          const EdgeInsets.all(16),
      borderRadius:    12,
      duration:        const Duration(seconds: 4),
      icon: Icon(
        isError ? Icons.error_outline : Icons.check_circle_outline,
        color: Colors.white,
      ),
    );
  }

  // ── Warna & ikon per tipe dokumen ─────────────────────────────────────────
  Color _docColor(String type) {
    switch (type.toLowerCase()) {
      case 'ijazah': return const Color(0xFF6366F1);
      case 'skl':    return const Color(0xFF10B981);
      case 'skhun':  return const Color(0xFF06B6D4);
      case 'rapor':  return const Color(0xFFF59E0B);
      default:       return const Color(0xFF8B5CF6);
    }
  }

  IconData _docIcon(String type) {
    switch (type.toLowerCase()) {
      case 'ijazah': return Icons.workspace_premium_rounded;
      case 'skl':    return Icons.verified_rounded;
      case 'skhun':  return Icons.article_rounded;
      case 'rapor':  return Icons.school_rounded;
      default:       return Icons.description_rounded;
    }
  }

  String _docLabel(String type) {
    switch (type.toLowerCase()) {
      case 'ijazah': return 'Ijazah';
      case 'skl':    return 'Surat Keterangan Lulus';
      case 'skhun':  return 'SKHUN';
      case 'rapor':  return 'Rapor';
      default:       return type.toUpperCase();
    }
  }

  @override
  Widget build(BuildContext context) {
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
          'Arsip Dokumen',
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
        ),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh_rounded),
            tooltip: 'Refresh',
            onPressed: _loadArsip,
          ),
        ],
      ),
      body: RefreshIndicator(
        onRefresh: _loadArsip,
        child: _buildBody(),
      ),
    );
  }

  Widget _buildBody() {
    if (_isLoading) {
      return const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircularProgressIndicator(color: Color(0xFF6366F1)),
            SizedBox(height: 16),
            Text('Memuat arsip dokumen...', style: TextStyle(color: Colors.grey)),
          ],
        ),
      );
    }

    if (_error != null) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.cloud_off_rounded, size: 64, color: Colors.red.shade300),
              const SizedBox(height: 16),
              Text('Gagal memuat arsip', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.red.shade700)),
              const SizedBox(height: 8),
              Text(_error!, textAlign: TextAlign.center, style: const TextStyle(color: Colors.grey, fontSize: 13)),
              const SizedBox(height: 24),
              FilledButton.icon(
                onPressed: _loadArsip,
                icon: const Icon(Icons.refresh_rounded),
                label: const Text('Coba Lagi'),
                style: FilledButton.styleFrom(backgroundColor: const Color(0xFF6366F1)),
              ),
            ],
          ),
        ),
      );
    }

    if (_dokumen.isEmpty) {
      return ListView(
        children: [
          const SizedBox(height: 80),
          Center(
            child: Column(
              children: [
                Container(
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: Colors.indigo.shade50,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(Icons.folder_open_rounded, size: 64, color: Colors.indigo.shade300),
                ),
                const SizedBox(height: 20),
                const Text('Belum Ada Arsip', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18, color: Color(0xFF1E293B))),
                const SizedBox(height: 8),
                const Text(
                  'Dokumen ijazah, SKL, SKHUN, dan rapor\nbelum diunggah oleh Admin.',
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.grey, fontSize: 13),
                ),
              ],
            ),
          ),
        ],
      );
    }

    // Group dokumen berdasarkan doc_type
    final Map<String, List<Map<String, dynamic>>> grouped = {};
    for (final doc in _dokumen) {
      final type = (doc['doc_type'] ?? 'lainnya') as String;
      grouped.putIfAbsent(type, () => []).add(doc);
    }

    return CustomScrollView(
      slivers: [
        // ── Header Hero ─────────────────────────────────────────────────────
        SliverToBoxAdapter(
          child: Container(
            margin: const EdgeInsets.all(16),
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                colors: [Color(0xFF6366F1), Color(0xFF4F46E5)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: BorderRadius.circular(20),
              boxShadow: [
                BoxShadow(
                  color: const Color(0xFF6366F1).withValues(alpha: 0.35),
                  blurRadius: 20,
                  offset: const Offset(0, 8),
                ),
              ],
            ),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.15),
                    borderRadius: BorderRadius.circular(14),
                  ),
                  child: const Icon(Icons.folder_special_rounded, color: Colors.white, size: 32),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Arsip Digital Saya',
                        style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 17),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        '${_dokumen.length} dokumen tersedia • Aman dengan JWT',
                        style: TextStyle(color: Colors.white.withValues(alpha: 0.8), fontSize: 12),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),

        // ── Info keamanan ────────────────────────────────────────────────────
        SliverToBoxAdapter(
          child: Container(
            margin: const EdgeInsets.symmetric(horizontal: 16),
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            decoration: BoxDecoration(
              color: Colors.green.shade50,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.green.shade200),
            ),
            child: Row(
              children: [
                Icon(Icons.lock_rounded, size: 16, color: Colors.green.shade700),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    'Dokumen bersifat pribadi & dilindungi enkripsi JWT. Tautan tidak dapat diakses publik.',
                    style: TextStyle(fontSize: 12, color: Colors.green.shade800),
                  ),
                ),
              ],
            ),
          ),
        ),
        const SliverToBoxAdapter(child: SizedBox(height: 20)),

        // ── Daftar dokumen per kategori ──────────────────────────────────────
        for (final entry in grouped.entries) ...[
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(6),
                    decoration: BoxDecoration(
                      color: _docColor(entry.key).withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Icon(_docIcon(entry.key), size: 18, color: _docColor(entry.key)),
                  ),
                  const SizedBox(width: 10),
                  Text(
                    _docLabel(entry.key),
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: Color(0xFF1E293B)),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                    decoration: BoxDecoration(
                      color: Colors.grey.shade100,
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text('${entry.value.length}', style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w600)),
                  ),
                ],
              ),
            ),
          ),
          SliverList(
            delegate: SliverChildBuilderDelegate(
              (ctx, i) {
                final doc = entry.value[i];
                return _buildDocCard(doc);
              },
              childCount: entry.value.length,
            ),
          ),
          const SliverToBoxAdapter(child: SizedBox(height: 8)),
        ],
        const SliverToBoxAdapter(child: SizedBox(height: 32)),
      ],
    );
  }

  Widget _buildDocCard(Map<String, dynamic> doc) {
    final id        = doc['id'] as int;
    final type      = (doc['doc_type'] ?? 'lainnya') as String;
    final title     = (doc['title'] ?? _docLabel(type)) as String;
    final fileSize  = doc['file_size'] as String?;
    final isVerified = (doc['is_verified'] as bool?) ?? false;
    final color     = _docColor(type);

    final downloading = _isDownloading[id] ?? false;
    final progress    = _downloadProgress[id] ?? 0.0;

    return Container(
      margin: const EdgeInsets.fromLTRB(16, 0, 16, 10),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.05),
            blurRadius: 12,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                // Ikon dokumen
                Container(
                  width: 48, height: 48,
                  decoration: BoxDecoration(
                    color: color.withValues(alpha: 0.12),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Icon(_docIcon(type), color: color, size: 26),
                ),
                const SizedBox(width: 14),

                // Info dokumen
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Color(0xFF1E293B))),
                      const SizedBox(height: 4),
                      Row(
                        children: [
                          if (fileSize != null) ...[
                            Icon(Icons.data_usage_rounded, size: 12, color: Colors.grey.shade400),
                            const SizedBox(width: 3),
                            Text(fileSize, style: TextStyle(fontSize: 11, color: Colors.grey.shade500)),
                            const SizedBox(width: 10),
                          ],
                          if (isVerified) ...[
                            Icon(Icons.verified_rounded, size: 12, color: Colors.green.shade600),
                            const SizedBox(width: 3),
                            Text('Terverifikasi', style: TextStyle(fontSize: 11, color: Colors.green.shade600, fontWeight: FontWeight.w600)),
                          ],
                        ],
                      ),
                    ],
                  ),
                ),

                // Tombol unduh
                if (!downloading)
                  IconButton(
                    onPressed: () => _downloadDokumen(doc),
                    icon: Icon(Icons.download_rounded, color: color),
                    style: IconButton.styleFrom(
                      backgroundColor: color.withValues(alpha: 0.10),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                    ),
                  )
                else
                  SizedBox(
                    width: 40, height: 40,
                    child: Stack(
                      alignment: Alignment.center,
                      children: [
                        CircularProgressIndicator(value: progress, color: color, strokeWidth: 3),
                        Text('${(progress * 100).toInt()}%', style: TextStyle(fontSize: 9, color: color, fontWeight: FontWeight.bold)),
                      ],
                    ),
                  ),
              ],
            ),
          ),

          // Progress bar saat mengunduh
          if (downloading)
            ClipRRect(
              borderRadius: const BorderRadius.only(bottomLeft: Radius.circular(16), bottomRight: Radius.circular(16)),
              child: LinearProgressIndicator(
                value: progress,
                backgroundColor: Colors.grey.shade100,
                color: color,
                minHeight: 4,
              ),
            ),
        ],
      ),
    );
  }
}
