# Color-, depth-, and shape-based 3D fruit detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2020color` |
| Judul asli | Color-, depth-, and shape-based 3D fruit detection |
| Penulis | Lin, Guichao; Tang, Yunchao; Zou, Xiangjun; Xiong, Juntao; Fang, Yamei |
| Tahun | 2020 |
| Venue | Precision Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | sweet pepper, persimmon/guava |

## Tautan Akses
- PDF: [lin2020color.pdf](../pdf/lin2020color.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-019-09654-w

## Gambaran Umum

Lin dkk. (2020) mengusulkan metode deteksi buah berbasis citra RGB-D dari sensor Kinect V2 untuk tiga jenis tanaman: cabai, terong, dan jambu biji (*guava*). Tujuannya adalah satu kerangka deteksi untuk berbagai jenis buah yang dipetik robot panen, dengan sensor berbiaya rendah. Metode ini menggabungkan segmentasi warna, pertumbuhan wilayah pada citra kedalaman, pencocokan bentuk 3D, dan klasifikasi SVM untuk membuang positif palsu.

Data terdiri dari 100 pasang citra RGB-D cabai, 100 pasang citra terong, dan 80 pasang citra jambu biji. Jumlah buah yang dianotasi adalah 1.083 untuk cabai, 305 untuk terong, dan 146 untuk jambu biji. Citra dibagi menjadi 15% latih, 5% validasi, dan 80% uji. Citra RGB 1080×1920 diselaraskan ke grid kedalaman 424×512. Penulis mengambil citra di kebun dengan latar belakang daun dan cabang.

Alur metodenya dimulai dari segmentasi probabilistik ruang warna HSV dengan naive Bayes, dengan ambang 0,1. Hasilnya dipakai sebagai kandidat wilayah pada citra kedalaman. Pertumbuhan wilayah dengan ambang selisih kedalaman 5 mm membentuk klaster, dan klaster di bawah 150 piksel dibuang. Setiap klaster diubah menjadi awan titik 3D, lalu MSAC mencocokkan bola untuk buah bulat (cabai) dan silinder untuk buah memanjang (terong). Setiap kandidat dijelaskan dengan deskriptor GPCD berdimensi 66, yang menggabungkan histogram sudut (27 bin), warna HSV (9 dimensi), dan histogram jarak D2 (30 bin). SVM yang dilatih pada GPCD memisahkan buah dari objek bukan buah.

Pada uji klasifikasi, penulis membandingkan GPCD dengan HOG dan LBP. Teks menyatakan GPCD memperoleh dua presisi terbaik, dua recall terbaik, dan tiga akurasi terbaik. Pada deteksi, metode ini dibandingkan dengan MNguyen, versi modifikasi Nguyen dkk. (2016) yang juga memakai SVM GPCD. Pada ambang 0,5, presisi metode ini untuk cabai, terong, dan jambu biji adalah 0,864, 0,886, dan 0,888. Recall-nya adalah 0,889, 0,762, dan 0,812. Nilai mAP adalah 0,863, 0,741, dan 0,807, dan semuanya lebih tinggi daripada MNguyen. Waktu rata-rata per buah adalah sekitar 1,41 detik untuk cabai, 4,07 detik untuk terong, dan 4,70 detik untuk jambu biji. Penulis sendiri menyebut waktu ini terlalu lama untuk robot panen.

Batasan yang dicatat penulis adalah daun yang berwarna dan berbentuk mirip buah sering lolos sebagai positif palsu, dan oklusi dapat membelah satu buah menjadi beberapa bagian. Penulis juga menyatakan bahwa jarak dibatasi pada 1.500 mm, dan hasil hanya diuji pada tiga jenis tanaman dengan jumlah citra yang kecil. Evaluasi tidak memakai kebun atau kamera lain.
