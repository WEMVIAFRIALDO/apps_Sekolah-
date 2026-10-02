/// Model data pengguna yang di-parse dari response JWT login.
/// Contoh response Laravel:
/// {
///   "token": "eyJ...",
///   "user": {
///     "id": 1,
///     "name": "Budi Santoso",
///     "nisn": "0054321987",
///     "email": "budi@siswa.sch.id",
///     "phone": "+62812...",
///     "role": "siswa",          // 'siswa' | 'alumni' | 'guru' | 'admin'
///     "school": "SMA N 1 Teladan",
///     "class": "XII IPA 3",
///     "angkatan": "2024",
///     "joined_at": "2021-07-15"
///   }
/// }
class UserModel {
  final int id;
  final String name;
  final String nisn;
  final String email;
  final String phone;
  final String role;       // 'siswa' | 'alumni'
  final String school;
  final String userClass;
  final String angkatan;
  final String joinedAt;

  const UserModel({
    required this.id,
    required this.name,
    required this.nisn,
    required this.email,
    required this.phone,
    required this.role,
    required this.school,
    required this.userClass,
    required this.angkatan,
    required this.joinedAt,
  });

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id:        json['id']       as int,
      name:      json['name']     as String,
      nisn:      json['nisn']     as String,
      email:     json['email']    as String? ?? '',
      phone:     json['phone']    as String? ?? '',
      role:      json['role']     as String,
      school:    json['school']   as String? ?? '',
      userClass: json['class']    as String? ?? '',
      angkatan:  json['angkatan'] as String? ?? '',
      joinedAt:  json['joined_at'] as String? ?? '',
    );
  }

  Map<String, dynamic> toJson() => {
    'id':        id,
    'name':      name,
    'nisn':      nisn,
    'email':     email,
    'phone':     phone,
    'role':      role,
    'school':    school,
    'class':     userClass,
    'angkatan':  angkatan,
    'joined_at': joinedAt,
  };

  /// Getter untuk pengecekan role (case-insensitive)
  bool get isSiswa  => role.toLowerCase() == 'siswa';
  bool get isAlumni => role.toLowerCase() == 'alumni';

  /// Tampilkan role dalam bahasa Indonesia
  String get roleLabel => isSiswa ? 'Siswa Aktif' : 'Alumni';
}
