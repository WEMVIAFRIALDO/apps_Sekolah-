import 'package:flutter_secure_storage/flutter_secure_storage.dart';

/// Service untuk menyimpan, membaca, dan menghapus JWT Token
/// menggunakan Android Keystore (aman, tidak bisa dibaca app lain).
class AuthService {
  static final AuthService _instance = AuthService._internal();
  factory AuthService() => _instance;
  AuthService._internal();

  // Menggunakan Android Keystore untuk keamanan ekstra
  // flutter_secure_storage v11+ sudah enkripsi secara default
  static const _storage = FlutterSecureStorage(
    aOptions: AndroidOptions(),
  );

  // Key constants
  static const _keyToken  = 'jwt_token';
  static const _keyRole   = 'user_role';
  static const _keyNisn   = 'user_nisn';
  static const _keyName   = 'user_name';
  static const _keyUserId = 'user_id';

  // ─── Token ────────────────────────────────────────────────────────────────

  /// Simpan JWT Token ke Keystore setelah login berhasil.
  Future<void> saveToken(String token) async =>
      _storage.write(key: _keyToken, value: token);

  /// Baca JWT Token (null jika belum login).
  Future<String?> getToken() async => _storage.read(key: _keyToken);

  /// Hapus JWT Token saat logout.
  Future<void> deleteToken() async => _storage.delete(key: _keyToken);

  /// Cek apakah pengguna masih login (token ada).
  Future<bool> isLoggedIn() async {
    final token = await getToken();
    return token != null && token.isNotEmpty;
  }

  // ─── User Info ─────────────────────────────────────────────────────────────

  /// Simpan data profil pengguna dari response login.
  Future<void> saveUserInfo({
    required String role,
    required String nisn,
    required String name,
    required String userId,
  }) async {
    await Future.wait([
      _storage.write(key: _keyRole,   value: role),
      _storage.write(key: _keyNisn,   value: nisn),
      _storage.write(key: _keyName,   value: name),
      _storage.write(key: _keyUserId, value: userId),
    ]);
  }

  Future<String?> getRole()   async => _storage.read(key: _keyRole);
  Future<String?> getNisn()   async => _storage.read(key: _keyNisn);
  Future<String?> getName()   async => _storage.read(key: _keyName);
  Future<String?> getUserId() async => _storage.read(key: _keyUserId);

  // ─── Clear All ─────────────────────────────────────────────────────────────

  /// Hapus semua data sesi (dipanggil saat logout).
  Future<void> clearSession() async => _storage.deleteAll();
}
