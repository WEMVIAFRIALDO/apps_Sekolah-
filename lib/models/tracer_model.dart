/// Model data Tracer Study Alumni.
/// REQ-F-08: Form dinamis berdasarkan status aktivitas.
class TracerStudyModel {
  final int? id;
  final String status;        // 'Bekerja' | 'Kuliah' | 'Wirausaha' | dst
  final String namaInstansi;
  final String kota;
  final String tahunMasuk;
  final String jabatan;       // Field kondisional: Bekerja / Wirausaha
  final String prodi;         // Field kondisional: Kuliah
  final String keterangan;
  final String? submittedAt;

  const TracerStudyModel({
    this.id,
    required this.status,
    required this.namaInstansi,
    required this.kota,
    required this.tahunMasuk,
    this.jabatan = '',
    this.prodi = '',
    this.keterangan = '',
    this.submittedAt,
  });

  factory TracerStudyModel.fromJson(Map<String, dynamic> json) {
    return TracerStudyModel(
      id:           json['id']           as int?,
      status:       json['status']        as String,
      namaInstansi: json['nama_instansi'] as String? ?? '',
      kota:         json['kota']          as String? ?? '',
      tahunMasuk:   json['tahun_masuk']   as String? ?? '',
      jabatan:      json['jabatan']       as String? ?? '',
      prodi:        json['prodi']         as String? ?? '',
      keterangan:   json['keterangan']    as String? ?? '',
      submittedAt:  json['submitted_at']  as String?,
    );
  }

  /// Konversi ke JSON untuk dikirim ke API Laravel
  /// POST /api/tracer-study
  Map<String, dynamic> toJson() => {
    'status':        status,
    'nama_instansi': namaInstansi,
    'kota':          kota,
    'tahun_masuk':   tahunMasuk,
    'jabatan':       jabatan,
    'prodi':         prodi,
    'keterangan':    keterangan,
  };
}
