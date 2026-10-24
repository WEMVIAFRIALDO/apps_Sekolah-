import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:dio/dio.dart';
import '../services/api_service.dart';
import '../services/file_saver.dart';
import '../services/theme_service.dart';

/// REQ-F-09: Halaman Arsip Dokumen Digital untuk Alumni.
/// Alumni dapat melihat dan mengunduh:
///   - Ijazah, SKL, SKHUN, Rapor (dari graduation_docs)
/// Semua akses dilindungi JWT Bearer Token (REQ-NF-01).
/// Terintegrasi dengan ThemeService (Mode Gelap & Mode Terang).
class ArsipPage extends StatefulWidget {
  const ArsipPage({super.key});

  @override
  State<ArsipPage> createState() => _ArsipPageState();
}

class _ArsipPageState extends State<ArsipPage> {
  final _api = ApiService();

  List<Map<String, dynamic>> _dokumen = [];
  bool _isLoading = true;
  String? _error;

  // Track progress unduhan per dokumen id
  final Map<int, double> _downloadProgress = {};
  final Map<int, bool> _isDownloading = {};

  @override
  void initState() {
    super.initState();
    _loadArsip();
  }

  Future<void> _loadArsip() async {
    setState(() {
      _isLoading = true;
      _error = null;
    });
    try {
      final res = await _api.get('/arsip');
      final data = res.data as Map<String, dynamic>;
      final list = (data['data'] as List?) ?? [];
      setState(() {
        _dokumen = list.map((e) => Map<String, dynamic>.from(e as Map)).toList();
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
    final id = doc['id'] as int;
    final docType = (doc['doc_type'] ?? 'dokumen') as String;
    final title = (doc['title'] ?? docType) as String;

    setState(() {
      _isDownloading[id] = true;
      _downloadProgress[id] = 0.0;
    });

    try {
      final bytes = await _api.downloadBytes(
        '/arsip/$id/download',
        onProgress: (p) {
          if (mounted) setState(() => _downloadProgress[id] = p);
        },
      );

      setState(() {
        _isDownloading[id] = false;
      });

      final savedPath = await saveAndOpenFile(bytes, 'salut_${docType}_$id.pdf');
      if (savedPath != null) {
        _showSnack('File disimpan di: $savedPath', isError: false);
      }
    } catch (e) {
      setState(() {
        _isDownloading[id] = false;
      });
      _showSnack('Gagal mengunduh $title: ${ApiService.parseError(e)}', isError: true);
    }
  }

  void _showSnack(String msg, {bool isError = false}) {
    Get.snackbar(
      isError ? 'Gagal' : 'Sukses',
      msg,
      backgroundColor: isError ? Colors.red.shade800 : Colors.green.shade700,
      colorText: Colors.white,
      snackPosition: SnackPosition.BOTTOM,
      margin: const EdgeInsets.all(16),
      borderRadius: 12,
      duration: const Duration(seconds: 4),
      icon: Icon(
        isError ? Icons.error_outline : Icons.check_circle_outline,
        color: Colors.white,
      ),
    );
  }

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
    final theme = ThemeService.to;

    return Obx(() {
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
            'Arsip Dokumen',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
              color: theme.textPrimary,
            ),
          ),
          centerTitle: true,
          actions: [
            IconButton(
              icon: Icon(Icons.refresh_rounded, color: theme.textMuted),
              tooltip: 'Refresh',
              onPressed: _loadArsip,
            ),
          ],
        ),
        body: RefreshIndicator(
          onRefresh: _loadArsip,
          child: _buildBody(theme),
        ),
      );
    });
  }

  Widget _buildBody(ThemeService theme) {
    final isDark = theme.isDarkMode.value;

    if (_isLoading) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircularProgressIndicator(color: theme.primary),
            const SizedBox(height: 16),
            Text('Memuat arsip dokumen...', style: TextStyle(color: theme.textMuted)),
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
              Text('Gagal memuat arsip',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.red.shade700)),
              const SizedBox(height: 8),
              Text(_error!,
                  textAlign: TextAlign.center,
                  style: TextStyle(color: theme.textMuted, fontSize: 13)),
              const SizedBox(height: 24),
              ElevatedButton.icon(
                onPressed: _loadArsip,
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
                    color: isDark ? const Color(0xFF1E3A8A).withValues(alpha: 0.2) : Colors.indigo.shade50,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(Icons.folder_open_rounded, size: 64, color: theme.primary),
                ),
                const SizedBox(height: 20),
                Text(
                  'Belum Ada Arsip',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18, color: theme.textPrimary),
                ),
                const SizedBox(height: 8),
                Text(
                  'Dokumen ijazah, SKL, SKHUN, dan rapor\nbelum diunggah oleh Admin.',
                  textAlign: TextAlign.center,
                  style: TextStyle(color: theme.textMuted, fontSize: 13),
                ),
              ],
            ),
          ),
        ],
      );
    }

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
                  blurRadius: 16,
                  offset: const Offset(0, 6),
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
                  child: const Icon(Icons.folder_special_rounded, color: Colors.white, size: 30),
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
                        '${_dokumen.length} dokumen tersedia • Terenkripsi JWT',
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
              color: isDark ? const Color(0xFF064E3B).withValues(alpha: 0.25) : Colors.green.shade50,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: isDark ? const Color(0xFF059669).withValues(alpha: 0.4) : Colors.green.shade200,
              ),
            ),
            child: Row(
              children: [
                Icon(
                  Icons.lock_rounded,
                  size: 16,
                  color: isDark ? const Color(0xFF34D399) : Colors.green.shade700,
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    'Dokumen bersifat pribadi & dilindungi enkripsi JWT. Tautan tidak dapat diakses publik.',
                    style: TextStyle(
                      fontSize: 12,
                      color: isDark ? const Color(0xFF6EE7B7) : Colors.green.shade800,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
        const SliverToBoxAdapter(child: SizedBox(height: 16)),

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
                      color: _docColor(entry.key).withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Icon(_docIcon(entry.key), size: 18, color: _docColor(entry.key)),
                  ),
                  const SizedBox(width: 10),
                  Text(
                    _docLabel(entry.key),
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 15,
                      color: theme.textPrimary,
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                    decoration: BoxDecoration(
                      color: theme.cardSubtle,
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: theme.border),
                    ),
                    child: Text(
                      '${entry.value.length}',
                      style: TextStyle(fontSize: 11, fontWeight: FontWeight.w600, color: theme.textMuted),
                    ),
                  ),
                ],
              ),
            ),
          ),
          SliverList(
            delegate: SliverChildBuilderDelegate(
              (ctx, i) {
                final doc = entry.value[i];
                return _buildDocCard(doc, theme);
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

  Widget _buildDocCard(Map<String, dynamic> doc, ThemeService theme) {
    final id = doc['id'] as int;
    final type = (doc['doc_type'] ?? 'lainnya') as String;
    final title = (doc['title'] ?? _docLabel(type)) as String;
    final fileSize = doc['file_size'] as String?;
    final isVerified = (doc['is_verified'] as bool?) ?? false;
    final color = _docColor(type);

    final downloading = _isDownloading[id] ?? false;
    final progress = _downloadProgress[id] ?? 0.0;

    return Container(
      margin: const EdgeInsets.fromLTRB(16, 0, 16, 10),
      decoration: BoxDecoration(
        color: theme.card,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: theme.border),
        boxShadow: theme.cardShadow,
      ),
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                // Ikon dokumen
                Container(
                  width: 48,
                  height: 48,
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
                      Text(
                        title,
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 14,
                          color: theme.textPrimary,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Row(
                        children: [
                          if (fileSize != null) ...[
                            Icon(Icons.data_usage_rounded, size: 12, color: theme.textMuted),
                            const SizedBox(width: 3),
                            Text(fileSize, style: TextStyle(fontSize: 11, color: theme.textMuted)),
                            const SizedBox(width: 10),
                          ],
                          if (isVerified) ...[
                            const Icon(Icons.verified_rounded, size: 12, color: Color(0xFF10B981)),
                            const SizedBox(width: 3),
                            const Text(
                              'Terverifikasi',
                              style: TextStyle(fontSize: 11, color: Color(0xFF10B981), fontWeight: FontWeight.w600),
                            ),
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
                    width: 40,
                    height: 40,
                    child: Stack(
                      alignment: Alignment.center,
                      children: [
                        CircularProgressIndicator(value: progress, color: color, strokeWidth: 3),
                        Text(
                          '${(progress * 100).toInt()}%',
                          style: TextStyle(fontSize: 9, color: color, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
              ],
            ),
          ),

          // Progress bar saat mengunduh
          if (downloading)
            ClipRRect(
              borderRadius: const BorderRadius.only(
                bottomLeft: Radius.circular(16),
                bottomRight: Radius.circular(16),
              ),
              child: LinearProgressIndicator(
                value: progress,
                backgroundColor: theme.cardSubtle,
                color: color,
                minHeight: 4,
              ),
            ),
        ],
      ),
    );
  }
}
