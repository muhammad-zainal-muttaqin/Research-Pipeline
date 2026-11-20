# A Review of Multi-Object Tracking in Recent Times

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2025reviewc` |
| Judul asli | A Review of Multi-Object Tracking in Recent Times |
| Penulis | Li, Suya; Ren, Hengyi; Xie, Xin; Cao, Ying |
| Tahun | 2025 |
| Venue | Iet Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [li2025reviewc.pdf](../pdf/li2025reviewc.pdf)
- DOI resmi: https://doi.org/10.1049/cvi2.70010

## Gambaran Umum

Kajian ini berjudul "A Review of Multi-Object Tracking in Recent Times" dan terbit di IET Computer Vision pada 2025. Objek tinjauannya adalah pelacakan banyak objek (*multi-object tracking*, MOT), yaitu tugas mempertahankan identitas setiap objek yang bergerak di dalam video dari satu bingkai ke bingkai berikutnya. Kajian ini membahas metode berbasis pembelajaran mendalam. Abstraknya membagi metode menjadi tiga kelompok: berbasis deteksi, berbasis pelacak objek tunggal (*single-object tracking*, SOT), dan berbasis segmentasi.

Pembagian berbasis deteksi memisahkan pelacakan menjadi dua tahap. Pertama, detektor menemukan objek pada setiap bingkai. Kedua, asosiasi menghubungkan deteksi di bingkai sekarang dengan lintasan yang sudah ada. Paradigma ini sering disebut *tracking-by-detection*. Kajian ini juga membahas paradigma *joint detection and tracking* (JDT), yang menjalankan deteksi dan asosiasi dalam satu jaringan. Metode yang disebut dalam bagian ini antara lain JDE, CSTrack, CSTrackV2, RetinaTrack, Chained-Tracker, FairMOT, dan UTM. Bagian lain menyebut SUSHI, CenterTrack, dan PermaTrack. Kelompok SOT memakai pelacak objek tunggal untuk mengikuti setiap objek. Kelompok segmentasi memakai masker piksel, bukan kotak pembatas, untuk menandai objek.

Tabel perbandingan memuat nilai MOTA (*multiple object tracking accuracy*), yaitu metrik yang menggabungkan galat deteksi dan galat identitas. Dalam tabel awal, SORT, DeepSORT, MPNTrack, MAT, DET, dan ByteTrack dibandingkan. ByteTrack tercatat 80,3 pada MOT17 dan 77,8 pada MOT20. StrongSORT juga muncul dalam tabel. Kajian DET [29] memakai informasi kedalaman (*depth*) bersama RGB untuk pelacakan dalam ruangan. Ini satu-satunya rujukan dalam bagian yang dibaca yang menyinggung masukan sensor kedalaman.

Bagian kesimpulan menyatakan bahwa tinjauan mencakup metode MOT berbasis pembelajaran mendalam, dikelompokkan menurut tiga kelompok di atas, beserta metrik, dataset, tantangan, dan arah riset ke depan. Bagian ketersediaan data menyatakan tidak ada dataset baru yang dihasilkan. Kajian ini menjadi contoh mekanisme asosiasi lintas bingkai dari luar pertanian. Mekanisme tersebut dapat dipertimbangkan bila sumber bukti dari luar pertanian dipakai untuk masalah identitas lintas pandang.

Klaim bahwa kajian ini tidak memuat materi pertanian hanya berlaku untuk bagian yang sudah dibaca.
