import 'dart:io';
import 'dart:typed_data';

import 'package:open_filex/open_filex.dart';
import 'package:path_provider/path_provider.dart';

/// Simpan [bytes] ke folder dokumen aplikasi lalu buka dengan aplikasi default.
/// Return path file jika file tidak bisa langsung dibuka, null jika berhasil dibuka.
Future<String?> saveAndOpenFile(Uint8List bytes, String fileName) async {
  final dir = await getApplicationDocumentsDirectory();
  final file = File('${dir.path}/$fileName');
  await file.writeAsBytes(bytes);

  final result = await OpenFilex.open(file.path);
  return result.type == ResultType.done ? null : file.path;
}
