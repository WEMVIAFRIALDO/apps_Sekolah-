import 'dart:js_interop';
import 'dart:typed_data';

import 'package:web/web.dart' as web;

/// Picu unduhan browser untuk [bytes] dengan nama [fileName].
/// Selalu return null karena browser yang menangani penyimpanan file.
Future<String?> saveAndOpenFile(Uint8List bytes, String fileName) async {
  final blob = web.Blob(
    [bytes.toJS].toJS,
    web.BlobPropertyBag(type: 'application/octet-stream'),
  );
  final url = web.URL.createObjectURL(blob);
  final anchor = web.HTMLAnchorElement()
    ..href = url
    ..download = fileName;
  web.document.body?.append(anchor);
  anchor.click();
  anchor.remove();
  web.URL.revokeObjectURL(url);
  return null;
}
