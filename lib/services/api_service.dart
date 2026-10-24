import 'package:dio/dio.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart' hide Response, FormData;

import 'auth_service.dart';

/// Konfigurasi base URL Backend Laravel.
/// - Web / Windows      : http://localhost:8000/api
/// - Emulator Android   : http://10.0.2.2:8000/api (alias localhost laptop)
/// - HP Android asli    : jalankan `php artisan serve --host=0.0.0.0` lalu
///   `flutter run --dart-define=API_BASE_URL=http://<IP-laptop>:8000/api`
const String _kBaseUrlOverride = String.fromEnvironment('API_BASE_URL');
final String kBaseUrl = _kBaseUrlOverride.isNotEmpty
    ? _kBaseUrlOverride
    : (!kIsWeb && defaultTargetPlatform == TargetPlatform.android)
        ? 'http://10.0.2.2:8000/api'
        : 'http://localhost:8000/api';

/// Singleton HTTP client berbasis Dio.
/// Fitur:
///  - Otomatis menyisipkan Bearer Token JWT di setiap request (Interceptor).
///  - Menangani error 401 (token expired) → redirect ke Login.
///  - Timeout 30 detik untuk connect & receive.
class ApiService {
  static final ApiService _instance = ApiService._internal();
  factory ApiService() => _instance;

  late final Dio _dio;
  Dio get dio => _dio;

  ApiService._internal() {
    _dio = Dio(
      BaseOptions(
        baseUrl: kBaseUrl,
        connectTimeout: const Duration(seconds: 30),
        receiveTimeout: const Duration(seconds: 30),
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
      ),
    );

    // ── Interceptor: sisipkan JWT Token otomatis ──────────────────────────
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await AuthService().getToken();
          if (token != null && token.isNotEmpty) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          return handler.next(options);
        },
        onError: (DioException err, handler) async {
          // Token kadaluarsa / tidak valid → paksa logout ke Login
          // Catatan: JANGAN intercept jika request berasal dari endpoint /login atau /auth
          // karena 401 saat login berarti kredensial salah, bukan token kadaluarsa.
          final requestPath = err.requestOptions.path;
          final isLoginEndpoint = requestPath.contains('/login') || requestPath.contains('/auth');

          if (err.response?.statusCode == 401 && !isLoginEndpoint) {
            await AuthService().deleteToken();
            Get.offAllNamed('/login');
            Get.snackbar(
              'Sesi Berakhir',
              'Token Anda telah kadaluarsa. Silakan login kembali.',
              backgroundColor: Colors.red.shade800,
              colorText: Colors.white,
              snackPosition: SnackPosition.TOP,
            );
          }
          return handler.next(err);
        },
      ),
    );
  }

  // ─── Generic HTTP Methods ──────────────────────────────────────────────────

  /// GET request. Otomatis menyisipkan JWT header.
  Future<Response> get(
    String path, {
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    return _dio.get(
      path,
      queryParameters: queryParameters,
      options: options,
    );
  }

  /// POST request dengan JSON body.
  Future<Response> post(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    return _dio.post(
      path,
      data: data,
      queryParameters: queryParameters,
      options: options,
    );
  }

  /// POST request dengan multipart/form-data (untuk upload file).
  Future<Response> postMultipart(
    String path, {
    required FormData formData,
  }) async {
    return _dio.post(
      path,
      data: formData,
      options: Options(contentType: 'multipart/form-data'),
    );
  }

  /// Download file dengan JWT Bearer Token sebagai bytes (jalan di Android & Web).
  /// [path]      : Path endpoint relatif terhadap [kBaseUrl], mis. '/arsip/3/download'.
  /// [onProgress]: Callback progress (0.0 – 1.0).
  Future<Uint8List> downloadBytes(
    String path, {
    void Function(double progress)? onProgress,
  }) async {
    final res = await _dio.get<List<int>>(
      path,
      options: Options(responseType: ResponseType.bytes),
      onReceiveProgress: (received, total) {
        if (total > 0 && onProgress != null) {
          onProgress(received / total);
        }
      },
    );
    return Uint8List.fromList(res.data ?? const []);
  }

  /// Parsing error dari DioException menjadi pesan yang ramah pengguna.
  static String parseError(Object error) {
    if (error is DioException) {
      final data = error.response?.data;
      if (data is Map && data['message'] != null) {
        return data['message'].toString();
      }
      switch (error.type) {
        case DioExceptionType.connectionTimeout:
        case DioExceptionType.receiveTimeout:
          return 'Koneksi timeout. Periksa jaringan Anda.';
        case DioExceptionType.connectionError:
          return 'Tidak dapat terhubung ke server. Periksa URL atau jaringan.';
        default:
          return 'Terjadi kesalahan. Coba lagi.';
      }
    }
    return error.toString();
  }
}
