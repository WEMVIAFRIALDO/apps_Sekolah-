// Simpan & buka file hasil download.
// Android/Windows → folder dokumen aplikasi + open_filex.
// Web (Chrome)    → unduhan browser.
export 'file_saver_io.dart' if (dart.library.js_interop) 'file_saver_web.dart';
