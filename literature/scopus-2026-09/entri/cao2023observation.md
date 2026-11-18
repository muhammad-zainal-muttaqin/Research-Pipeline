# Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cao2023observation` |
| Judul asli | Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking |
| Penulis | Cao, Jinkun; Pang, Jiangmiao; Weng, Xinshuo; Khirodkar, Rawal; Kitani, Kris |
| Tahun | 2023 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [cao2023observation.pdf](../pdf/cao2023observation.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr52729.2023.00934

## Gambaran Umum

Penelitian ini mengatasi kelemahan pelacak berbasis model gerak pada pelacakan banyak objek, khususnya saat objek tertutup dan bergerak tidak linier. Metode yang menjadi titik berangkat adalah SORT, yang memakai filter Kalman dengan asumsi gerak linier. Penulis mengidentifikasi tiga keterbatasan SORT: sensitivitas terhadap derau estimasi keadaan pada video berlaju bingkai tinggi, penumpukan galat selama objek tidak memiliki pengamatan, dan ketergantungan pada estimasi keadaan alih-alih pengamatan detektor. Tujuan penelitian ini adalah menjaga pelacakan tetap tangguh dalam kondisi tersebut tanpa meninggalkan sifat sederhana, daring, dan waktu nyata.

Objek yang dilacak bukan tanaman, melainkan pedestrian, kendaraan, dan kepala manusia dalam lima himpunan data tolok ukur, yaitu MOT17, MOT20, KITTI, DanceTrack, dan CroHD. MOT17 dan MOT20 memuat pedestrian yang sebagian besar bergerak linier dengan kepadatan berbeda; KITTI memuat pedestrian dan mobil pada laju 10 bingkai per detik; DanceTrack memuat manusia dengan gerak sangat tidak linier, penampilan mirip, dan silang silang sering. Deteksi objek berasal dari bobot YOLOX yang dipakai ByteTrack untuk MOT17, MOT20, dan DanceTrack, serta dari PermaTrack untuk KITTI. Metrik utama adalah HOTA, dilengkapi AssA dan IDF1; MOTA hanya dianggap adil bila semua metode memakai deteksi yang sama.

Mekanisme yang diusulkan bernama Observation-Centric SORT (OC-SORT) dan berdiri atas dua komponen utama. Observation-centric Re-Update (ORU) menambahkan tahap pembaruan ulang setelah lintasan diaktifkan kembali pasca-oklusi. Tahap ini memakai lintasan virtual yang dibangun dari pengamatan terakhir sebelum oklusi dan pengamatan pertama setelah oklusi sebagai dua jangkar, lalu memperbaiki galat yang menumpuk selama objek tak teramati. Observation-Centric Momentum (OCM) memasukkan konsistensi arah gerak ke dalam matriks biaya asosiasi dengan menjumlahkan biaya IoU negatif dan biaya selisih sudut arah, dengan bobot 0,2 dan selisih waktu tiga langkah. Tambahan heuristik Observation-Centric Recovery (OCR) mencoba mengasosiasikan kembali pengamatan yang tak cocok guna memulihkan objek yang berhenti atau tertutup sebentar.

Hasil dilaporkan pada Tabel 1 sampai Tabel 4 dengan deteksi privat maupun publik. Pada MOT17-test dengan deteksi privat, OC-SORT mencatat HOTA 63,2, MOTA 78,0, IDF1 77,5, dan AssA 63,2, sementara ByteTrack dengan deteksi yang sama mencatat HOTA 63,1, MOTA 80,3, dan IDF1 77,3. Pada MOT20-test, OC-SORT mencapai HOTA 62,1 yang dinyatakan sebagai nilai terbaik pada kondisi oklusi pedestrian berat. Pada DanceTrack (Tabel 3), OC-SORT mencatat HOTA 54,6 dan MOTA 80,4; dengan interpolasi linier, HOTA naik menjadi 55,1. Kecepatan penyimpulan tercatat 793 bingkai per detik pada prosesor Intel i9-9980XE, sedangkan abstrak menyebut lebih dari 700 bingkai per detik pada satu CPU.

Penulis menyatakan beberapa batasan. OC-SORT sengaja tidak memakai ambang deteksi adaptif seperti ByteTrack, sehingga skor MOTA-nya lebih rendah meskipun akurasi asosiasi bersaing. Pada KITTI kategori mobil, asosiasi berbasis IoU menjadi lemah ketika kecepatan objek tinggi atau laju bingkai rendah karena IoU antarbingkai bisa sangat rendah bahkan nol; penulis menyebut hal ini sebagai kekurangan penerapan baku, bukan kelemahan rancangan inti. Seluruh percobaan memakai satu tumpuan parameter yang sama lintas himpunan data, sehingga penyesuaian parameter diyakini dapat menaikkan kinerja. Penulis juga tidak mengklaim keunggulan pada kategori mobil KITTI dan menekankan bahwa perbaikan terjadi terutama pada oklusi dan gerak tidak linier.

