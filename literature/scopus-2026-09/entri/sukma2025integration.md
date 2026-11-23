# Integration of Single Shot Multibox Detector and Single Scale Retinex in Detecting Oil Palm Fruit Bunches in Low Light Conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sukma2025integration` |
| Judul asli | Integration of Single Shot Multibox Detector and Single Scale Retinex in Detecting Oil Palm Fruit Bunches in Low Light Conditions |
| Penulis | Sukma, Erwin; Indrabayu |
| Tahun | 2025 |
| Venue | 2025 IEEE International Conference on Artificial Intelligence and Mechatronics Systems Aims 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [sukma2025integration.pdf](../pdf/sukma2025integration.pdf)
- DOI resmi: https://doi.org/10.1109/aims66189.2025.11229503

## Gambaran Umum

Penelitian ini bertujuan mendeteksi tandan buah segar (TBS) kelapa sawit pada kondisi cahaya rendah. Penulis menyebut penyebabnya: cuaca mendung, daun yang lebat, dan waktu pengambilan citra pagi atau sore. Penulis menyatakan studi terdahulu memakai YOLO dan *Faster R-CNN* tanpa uji pada kebun dengan intensitas cahaya rendah. Kontribusi yang diklaim adalah gabungan peningkatan citra dan model deteksi.

Citra diambil langsung pada pohon sawit setinggi 2 sampai 7 meter memakai drone DJI Neo yang berjarak tidak lebih dari 1 meter dari tandan. Resolusi citra 1920x1080 piksel, kecepatan rana 1/400, ISO 400. Pengambilan data latih berlangsung 3 hari. Setelah seleksi (citra mirip dan buram dibuang) tersisa 1.385 citra. Pembagian latih dan validasi 785 dan 600 citra. Augmentasi (rotasi 90 derajat, rotasi 45 derajat, pembalikan) menghasilkan 2.955 citra, dengan 2.355 untuk latih dan 600 untuk evaluasi. Anotasi memakai Roboflow dengan satu kelas. Pemberi label tidak disebut. Data uji berasal dari tempat berbeda: tiga kategori cahaya, masing-masing 104 citra dari 35 pohon dengan 245 tandan. Cahaya diukur dengan *lux meter*.

Metode memakai *Single Scale Retinex* (SSR) sebagai praproses. SSR mengurangi logaritma intensitas piksel dengan logaritma citra yang telah dihaluskan filter Gauss, sehingga pencahayaan tidak merata dikoreksi dan kontras lokal naik. Parameter sebaran Gauss 300. Deteksi memakai *Single Shot Multibox Detector* (SSD), yaitu detektor satu tahap yang memprediksi kotak dan kelas pada beberapa resolusi peta fitur dalam satu jaringan. Tulang punggung (*backbone*) yang dipakai EfficientNet, masukan 512x512, laju belajar 0,01, 30.000 langkah. Pembanding: ISO 400 tanpa pengolahan, ISO 3200 tanpa pengolahan, dan ISO 400 dengan *Multi Scale Retinex* (MSR).

Pada pelatihan, AP@0,5 mencapai 93,54%, AP@0,75 83,37%, dan *Average Recall* (AR) 85,95% pada langkah ke-30.000 (data evaluasi 600 citra). Pada data uji dengan ambang 50%, kategori 1000-1600 lux menghasilkan presisi 100,00%, *recall* 85,31%, F1 92,07% (TP 209, FP 0, FN 36). Kategori 500-999 lux: presisi 99,52%, *recall* 84,08%, F1 91,15%. Kategori 200-499 lux: presisi 98,55%, *recall* 84,30%, F1 90,87%. Pada 200-499 lux, F1 ISO 400 saja 28,37%, ISO 3200 21,66%, ISO 400 dengan MSR 88,18%. Penulis menyebut 36 tandan tidak terdeteksi pada kategori pertama sebagian besar tertutup pelepah dan tertutup tandan lain.

Keterbatasan yang dapat diperiksa: satu kelas, tanpa kematangan. Pembagian latih dan validasi tidak dinyatakan per pohon. Tidak ada set uji terpisah untuk metrik AP, karena angka AP berasal dari 600 citra evaluasi yang dipakai selama pelatihan. Teks menyebut 3 kategori cahaya diambil pada waktu dan hari berbeda sehingga pengaruh waktu dan cahaya tercampur. Ketidakkonsistenan teks: AR 83,37% pada teks dan 85,95% pada tabel, serta F1 91,07% pada kesimpulan dan 91,15% pada tabel. Tandan dihitung per citra, tanpa penautan antarcitra, sehingga tandan yang sama pada citra berbeda tidak disatukan.
