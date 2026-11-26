# Evaluating Orchard Fruit Quality from Monocular and Stereo RGB-D Imagery: A Comparative Study

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `piani2025evaluating` |
| Judul asli | Evaluating Orchard Fruit Quality from Monocular and Stereo RGB-D Imagery: A Comparative Study |
| Penulis | Piani, Mirko; Scalisi, Alessio; Bortolotti, Gianmarco; Mengoli, Dario; Manfrini, Luigi |
| Tahun | 2025 |
| Venue | Conference Proceedings 2025 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2025 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [piani2025evaluating.pdf](../pdf/piani2025evaluating.pdf)
- DOI resmi: https://doi.org/10.1109/metroagrifor66923.2025.11512584

## Gambaran Umum

Kajian ini (makalah konferensi IEEE, 2025) membandingkan dua kamera untuk mencacah apel serta mengukur ukuran dan warnanya di kebun. Kamera pertama adalah kamera stereo Intel RealSense D435i. Kamera kedua adalah kamera monokular Raspberry Pi Camera Module 3 Wide, dengan depth yang diperkirakan model Depth Anything V2.

Kedua kamera dipasang pada satu rumah sensor, disinkronkan waktunya, dan ditempatkan diam 2,5 m dari empat pohon apel. Buah yang tidak terlihat oleh kedua kamera dijarangkan tangan, sehingga tersisa 66 buah, 56 di antaranya terlihat penuh. Setiap kamera mengambil 17 bingkai. Enam model YOLO diuji, dan hanya YOLO11 yang memberi keluaran andal.

RealSense memperkirakan 56 buah (85% dari total), sedangkan kamera monokular rata-rata 19 buah (29% dari total). Untuk ukuran, depth monokular gagal mengukur 64,1% buah terdeteksi, sedangkan RealSense gagal pada 9,2%. Pada RealSense, kesalahan pencocokan lingkaran membuat 21,2% kotak lainnya tanpa ukuran. Bias ukuran stereo 0,59 mm, sedangkan kamera monokular lebih baik untuk indeks warna kulit, dengan bias 0,12.

Buah tidak ditautkan antarbingkai. Hitungan adalah perkiraan per plot dari kamera diam. Tabel II mencatat 33 citra untuk kedua kamera bersama.
