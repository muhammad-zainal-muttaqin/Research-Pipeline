# Efficient AI-Powered Orange Health Assessment And Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bakas2026efficient` |
| Judul asli | Efficient AI-Powered Orange Health Assessment And Yield Estimation |
| Penulis | Bakas, Khaoula; Saddik, Amine; Dliou, Azzedine; Hssaisoune, Mohammed; El Hachemy, Said; Ait-Ichou, Hamza; Bouchaou, Lhoussaine |
| Tahun | 2026 |
| Venue | Lecture Notes in Networks and Systems |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [bakas2026efficient.pdf](../pdf/bakas2026efficient.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-032-18857-1_30

## Gambaran Umum

Makalah konferensi ini (Lecture Notes in Networks and Systems, 2026) membandingkan empat varian YOLO ringan untuk mendeteksi jeruk dan mengelaskannya sebagai sehat atau sakit di ponsel. Varian yang dibandingkan adalah YOLOv5nu, YOLOv9t, YOLOv10n, dan YOLO11n.

Data berupa 4.212 citra dari kebun jeruk milik perusahaan agribisnis di Sebt El Guerdane, cekungan Souss Massa, Maroko. Citra diubah ke 640×640, dilabeli di Roboflow dalam dua kelas, lalu dibagi acak 80:20. Jumlah buah sehat dan sakit tidak seimbang, sehingga augmentasi ditambahkan.

YOLOv10n memberi presisi tertinggi (88,8%) dengan *recall* 78,9%. YOLOv9t memberi mAP50 tertinggi (87,6%) dan F1 84,3%. YOLO11n dipilih karena presisi 87,2%, *recall* 80,5%, dan waktu inferensi 1,7 ms. Model ini dipasang di aplikasi Android yang mencatat waktu deteksi, jumlah jeruk, dan jumlah per kelas.

Jumlah jeruk dari aplikasi tidak dibandingkan dengan hitungan lapangan. Penulis menyatakan bahwa buah belum dilacak antarbingkai, sehingga hitung ganda belum dicegah. Kajian ini berbeda dari artikel Bakas dkk. 2025 tentang pencacahan pohon jeruk dari UAV.
