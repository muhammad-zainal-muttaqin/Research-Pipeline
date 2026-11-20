# On-the-tree mango detection based on image fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cao2025tree` |
| Judul asli | On-the-tree mango detection based on image fusion |
| Penulis | Cao, Weihua; Zhang, Zhao; Zhang, Fu; Li, Minzan; Zhang, Man; Zhang, Yao |
| Tahun | 2025 |
| Venue | IFAC Papersonline |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | mango |

## Tautan Akses
- PDF: [cao2025tree.pdf](../pdf/cao2025tree.pdf)
- DOI resmi: https://doi.org/10.1016/j.ifacol.2025.11.795

## Gambaran Umum

Kajian ini menguji apakah menggabungkan tiga jenis citra, yaitu citra warna (RGB), citra kedalaman (*depth*), dan citra termal (*thermal*), meningkatkan deteksi buah mangga di kebun. Detektor yang dipakai adalah YOLOv8. Hasil utamanya: fusi ketiga modalitas mencapai AP 97,2%, lebih tinggi dibanding RGB saja (AP 94,8%).

Data diambil di kebun mangga di Guangxi, Tiongkok. Kamera *RGB-D* Intel RealSense D435i merekam citra warna 1280×720 dan citra kedalaman 640×360. Kamera termal Optris PI menghasilkan citra 382×288. Kedua sumber citra diregistrasi secara *affine* dengan titik fitur yang ditentukan manual. Dataset berisi 353 set citra asli dan 2.118 set hasil augmentasi, tersebar dalam tujuh kategori. Kelas tunggal adalah "Mango". Pembagian data 80/10/10.

Peneliti melatih YOLOv8 pada tujuh konfigurasi masukan: tiga modalitas tunggal (RGB, depth, termal), tiga pasangan (RGB-depth, RGB-termal, depth-termal), dan satu kombinasi tiga modalitas (RGB-depth-termal). YOLOv8 adalah detektor satu tahap tanpa *anchor*, yang memprediksi kotak pembatas dan skor kelas dari satu kali lintasan jaringan. Metrik yang dilaporkan adalah presisi (P), *recall* (R), F1, dan *average precision* (AP). Kajian tidak menjelaskan cara fusi di tingkat jaringan (misalnya *early* atau *late fusion*), sehingga arsitektur fusi belum dapat dinilai.

Tabel 1 melaporkan nilai berikut (dalam persen):

- RGB: P 93,3; R 89,3; F1 91,3; AP 94,8.
- Depth: P 87,3; R 90,2; F1 88,7; AP 93,8.
- Termal: P 94,4; R 88,6; F1 91,4; AP 94,7.
- RGB-depth: P 94,3; R 89,2; F1 91,7; AP 95,1.
- RGB-termal: P 96,2; R 91,9; F1 94,0; AP 96,8.
- Depth-termal: P 94,5; R 92,3; F1 93,4; AP 96,4.
- RGB-depth-termal: P 97,8; R 93,0; F1 95,3; AP 97,2.

Selisih AP antara konfigurasi terbaik dan RGB saja adalah 2,4 poin. Depth saja adalah konfigurasi terlemah (AP 93,8). Penulis menafsirkan bahwa noise pada depth akibat bayangan dan pantulan membuat detektor salah mengenali objek. Kajian tidak melaporkan variasi antar-run atau uji signifikansi, sehingga selisih kecil (0,4 sampai 2,4 poin) belum dapat dibedakan dari fluktuasi pelatihan.

Kelebihan kajian ini adalah perbandingan sistematis tujuh konfigurasi pada dataset yang sama dengan metrik yang sama. Keterbatasannya: (1) hanya satu kelas dan satu spesies buah; (2) tidak ada penghitungan jumlah buah, sehingga klaim tentang produktivitas tidak diuji; (3) kesimpulan tentang "keandalan" dan "pengambilan keputusan" tidak didukung pengukuran di lapangan; (4) penulis menyatakan bahwa fusi membantu pemilihan buah dan estimasi kematangan, tetapi kematangan dan ukuran tidak diukur di kajian ini. Dari sisi rekayasa, sistem tiga kamera dengan registrasi manual menambah biaya kalibrasi yang tidak dibahas.
