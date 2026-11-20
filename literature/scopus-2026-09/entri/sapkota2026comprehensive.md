# Comprehensive performance evaluation of YOLOv12, YOLO11, YOLOv10, YOLOv9 and YOLOv8 on detecting and counting fruitlet in complex orchard environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sapkota2026comprehensive` |
| Judul asli | Comprehensive performance evaluation of YOLOv12, YOLO11, YOLOv10, YOLOv9 and YOLOv8 on detecting and counting fruitlet in complex orchard environments |
| Penulis | Sapkota, Ranjan; Meng, Zhichao; Churuvija, Martin; Du, Xiaoqiang; Ma, Zenghong; Karkee, Manoj |
| Tahun | 2026 |
| Venue | Agriculture Communications |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [sapkota2026comprehensive.pdf](../pdf/sapkota2026comprehensive.pdf)
- DOI resmi: https://doi.org/10.1016/j.agrcom.2026.100125

## Gambaran Umum

Penelitian ini bertujuan mengevaluasi secara menyeluruh semua konfigurasi YOLOv8, YOLOv9, YOLOv10, YOLO11, dan YOLOv12 untuk mendeteksi buah muda hijau sebelum penjarangan di kebun apel komersial. Deteksi buah muda menjadi dasar otomatisasi penjarangan, tetapi buah hijau memiliki warna dan pantulan cahaya yang mirip daun, serta tertutup daun, cabang, dan buah lain. Penulis juga menguji akurasi penghitungan buah di lapang pada empat kultivar yang tidak dipakai saat latih dan membandingkan dua jenis sensor.

Tanaman yang diamati adalah apel kultivar SciFresh, SciLate, Cosmic Crisp, dan Honeycrisp. Pengambilan data dilakukan di kebun Allan Brothers di Prosser dan Naches, Washington, Amerika Serikat, serta di stasiun percobaan ROZA WSU IAREC untuk Cosmic Crisp. Citra latih berupa 1.147 gambar RGB yang diambil dengan kamera Intel RealSense D435i (1280 × 720 piksel) pada Juni 2024, terdiri atas 592 citra SciFresh dan 555 citra SciLate. Keadaan pencahayaan sengaja divariasikan, mulai dari cahaya pagi, sinar tengah hari, langit mendung, hingga bayang-bayang campuran, dengan sudut pandang 30°–90° pada sumbu zenit dan 0°–180° pada sumbu azimut. Anotasi kotak pembatas dibuat dengan Roboflow dan data dibagi latih serta validasi 8:2 tanpa praproses citra. Validasi penghitungan memakai 128 citra iPhone 14 Pro Max (32 per kultivar) dan 32 citra RealSense tambahan; kebenaran berupa hitungan manual buah tampak dan tertutup yang dicatat di lapang saat pengambilan citra.

Sebanyak 26 konfigurasi diuji: lima YOLOv8, enam YOLOv9, enam YOLOv10, lima YOLO11, dan empat YOLOv12. Semua model dilatih dengan pengaturan sama, yaitu 700 epoch, ukuran kelompok 8, citra 640 × 640, pengoptimal SGD, ambang kepercayaan 0,25, dan IoU 0,7. Fitur yang membedakan keluarga model meliputi strategi penugasan ganda tanpa NMS pada YOLOv10, blok C3k2 dan perhatian C2PSA pada YOLO11, GELAN dan PGI pada YOLOv9, serta Area Attention dan R-ELAN pada YOLOv12. Pengukuran mencakup presisi, recall, mAP@50, waktu praproses, inferensi, dan pascaolahan, serta RMSE dan MAE untuk hitungan buah.

Hasil deteksi menunjukkan presisi tertinggi 0,908 pada YOLOv10x dan 0,903 pada YOLOv9 GELAN-c, sedangkan recall tertinggi 0,900 pada YOLOv12l. Nilai mAP@50 tertinggi 0,935 dicapai bersama oleh YOLOv9 GELAN-e dan GELAN-base, diikuti YOLO11s 0,933 dan YOLOv12l 0,931. YOLO11n memiliki inferensi tercepat, 2,4 ms, dengan waktu praproses 0,1 ms; inferensi tercepat pada keluarga lain berturut-turut 4,1 ms untuk YOLOv8n, 11,5 ms untuk YOLOv9 GELAN-s, 5,5 ms untuk YOLOv10n, dan 4,6 ms untuk YOLOv12n. Pada citra iPhone, YOLO11n menghasilkan RMSE berturut-turut 4,51 (Honeycrisp), 4,59 (Cosmic Crisp), 4,83 (SciLate), dan 4,96 (SciFresh), dengan MAE 4,07; 3,98; 7,73; dan 3,85. Pada citra RealSense untuk SciFresh, YOLO11n mencatat RMSE 3,06 dan MAE 2,33, sedangkan YOLOv9 GELAN-e mencatat 3,11 dan 2,46.

Penulis menyatakan beberapa batasan. YOLOv12x tidak dapat dilatih tuntas karena keterbatasan memori. Latih memakai RealSense, sementara validasi memakai iPhone yang berbeda resolusi, warna, kalibrasi, dan lensa; penulis tidak menerapkan adaptasi ranah atau penyetelan ulang pada citra ponsel. Model yang dilatih khusus pada satu sensor lebih baik saat diuji pada sensor yang sama, sehingga penulis menekankan perlunya data dari berbagai sensor. Pada citra kultivar baru dan daerah padat, semua konfigurasi masih melewatkan buah: YOLOv8n melewatkan sekitar 10% buah tampak pada daerah yang sebagian tertutup, YOLO11n melewatkan dua buah karena oklusi, dan YOLOv12 gagal mendeteksi satu buah yang tampak jelas. Penulis menyebut perlunya himpunan data yang lebih besar dan beragam serta lingkungan latih yang lebih kuat, dan mengusulkan perbandingan lanjutan dengan YOLOv13 dan YOLO26. Data dan kode tersedia atas permintaan penulis.
