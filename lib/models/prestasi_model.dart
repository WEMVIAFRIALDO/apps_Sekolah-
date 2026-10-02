/// Model data Prestasi Siswa.
/// Digunakan untuk menampilkan daftar prestasi dan mengirim form input.
class PrestasiModel {
  final int? id;
  final String namaKegiatan;
  final String penyelenggara;
  final String tingkat;
  final String peringkat;
  final int tahun;
  final String deskripsi;
  final String statusValidasi; // 'Pending' | 'Approved' | 'Rejected'
  final String? sertifikatUrl;
  final String? catatan;       // Catatan dari guru saat reject

  const PrestasiModel({
    this.id,
    required this.namaKegiatan,
    required this.penyelenggara,
    required this.tingkat,
    required this.peringkat,
    required this.tahun,
    required this.deskripsi,
    this.statusValidasi = 'Pending',
    this.sertifikatUrl,
    this.catatan,
  });

  factory PrestasiModel.fromJson(Map<String, dynamic> json) {
    return PrestasiModel(
      id:              json['id']              as int?,
      namaKegiatan:    json['nama_kegiatan']   as String,
      penyelenggara:   json['penyelenggara']   as String,
      tingkat:         json['tingkat']         as String,
      peringkat:       json['peringkat']       as String,
      tahun:           (json['tahun'] as num).toInt(),
      deskripsi:       json['deskripsi']       as String? ?? '',
      statusValidasi:  json['status_validasi'] as String? ?? 'Pending',
      sertifikatUrl:   json['sertifikat_url']  as String?,
      catatan:         json['catatan']         as String?,
    );
  }

  Map<String, dynamic> toJson() => {
    'nama_kegiatan':   namaKegiatan,
    'penyelenggara':   penyelenggara,
    'tingkat':         tingkat,
    'peringkat':       peringkat,
    'tahun':           tahun,
    'deskripsi':       deskripsi,
  };

  /// Cek apakah prestasi sudah divalidasi guru
  bool get isApproved => statusValidasi == 'Approved';
  bool get isPending   => statusValidasi == 'Pending';
  bool get isRejected  => statusValidasi == 'Rejected';
}


/// Model untuk arsip digital alumni (Ijazah, SKHUN, SKL, dll.)
class ArsipDigitalModel {
  final int id;
  final String title;
  final String type;      // 'PDF' | 'Image'
  final String fileSize;
  final String fileUrl;   // URL di cloud storage (S3/Cloudinary)
  final bool isVerified;

  const ArsipDigitalModel({
    required this.id,
    required this.title,
    required this.type,
    required this.fileSize,
    required this.fileUrl,
    required this.isVerified,
  });

  factory ArsipDigitalModel.fromJson(Map<String, dynamic> json) {
    return ArsipDigitalModel(
      id:         json['id']          as int,
      title:      json['title']       as String,
      type:       json['type']        as String? ?? 'PDF',
      fileSize:   json['file_size']   as String? ?? '-',
      fileUrl:    json['file_url']    as String,
      isVerified: json['is_verified'] as bool? ?? false,
    );
  }
}
