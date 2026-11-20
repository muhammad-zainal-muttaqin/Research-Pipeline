# FairMOT: On the Fairness of Detection and Re-identification in Multiple Object Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2021fairmot` |
| Judul asli | FairMOT: On the Fairness of Detection and Re-identification in Multiple Object Tracking |
| Penulis | Zhang, Yifu; Wang, Chunyu; Wang, Xinggang; Zeng, Wenjun; Liu, Wenyu |
| Tahun | 2021 |
| Venue | International Journal of Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhang2021fairmot.pdf](../pdf/zhang2021fairmot.pdf)
- DOI resmi: https://doi.org/10.1007/s11263-021-01513-4

## Gambaran Umum

Kajian ini mengatasi masalah ketidakadilan antara dua tugas dalam pelacakan objek tunggal (*one-shot multi-object tracking*), yaitu deteksi objek dan identifikasi ulang (*re-identification*, re-ID). Pendekatan dua model terpisah antara deteksi dan asosiasi akurat tetapi lambat dan tidak dapat mencapai kecepatan video. Penggabungan keduanya dalam satu jaringan lebih efisien, tetapi kinerja pelacakan menurun tajam karena tugas re-ID diperlakukan sebagai tugas sekunder. Penulis mengidentifikasi tiga penyebabnya: penggunaan *anchor* yang mengabaikan re-ID dan menimbulkan ambiguitas pada adegan padat, pembagian fitur yang berbenturan karena deteksi membutuhkan fitur dalam sementara re-ID membutuhkan fitur penampilan tingkat rendah, serta dimensi fitur re-ID yang terlalu besar (512 atau 1.024) dibanding deteksi.

Kajian ini bukan tentang tanaman; ia termasuk metode dari luar pertanian yang dapat ditransfer ke pelacakan dan asosiasi lintas pandang. Data latih mencakup ETH, CityPerson, CalTech, MOT17, CUHK-SYSU, dan PRW; CrowdHuman dipakai untuk pralatih dengan metode citra tunggal. Pengujian dilakukan pada empat benchmark MOT Challenge, yaitu 2DMOT15, MOT16, MOT17, dan MOT20. Metrik yang dipakai adalah AP untuk deteksi, TPR pada FAR 0,1 untuk kualitas fitur re-ID, serta MOTA, IDs, dan IDF1 untuk kinerja pelacakan keseluruhan.

Mekanisme utamanya adalah FairMOT, yang dibangun di atas arsitektur deteksi *anchor-free* CenterNet. Backbone-nya menggunakan ResNet-34 dengan Deep Layer Aggregation yang disempurnakan (DLA-34), termasuk lebih banyak *skip connection* dan konvolusi deformabel pada modul *upsampling*, menghasilkan peta fitur dengan *stride* 4. Dua cabang homogen ditaruh di atas *backbone*: cabang deteksi memprediksi *heatmap* pusat objek, ofset, dan ukuran kotak, sementara cabang re-ID menghasilkan fitur 128 dimensi untuk setiap piksel dan mengambil fitur tepat di pusat objek. Kedua tugas dilatih secara adil dengan menggabungkan rugi *focal* untuk *heatmap*, rugi L1 untuk ofset dan ukuran, serta rugi klasifikasi identitas, yang diseimbangkan otomatis dengan *uncertainty loss*. Pada inferensi, asosiasi online memakai dua tahap: jarak Mahalanobis dari Kalman Filter digabungkan dengan jarak kosinus fitur re-ID (bobot λ = 0,98) lalu diselesaikan dengan algoritma Hungaria (ambang 0,4), diikuti pencocokan berdasarkan tumpang tindih kotak (ambang 0,5); lintasan yang tak cocok disimpan selama 30 frame.

Hasil ablasi menunjukkan pilihan desain tersebut terukur. Pengambilan fitur di pusat objek memberi MOTA 69,1, IDF1 72,8, IDs 299, dan TPR 94,4 pada validasi MOT17, lebih baik daripada ROI-Align (68,7/71,0/331/93,1), POS-Anchor (69,0/70,3/434/93,9), maupun pendekatan dua tahap (69,0/68,2/388/90,5) (Tabel 1). Fitur re-ID berdimensi 64 memberi MOTA 69,2 dan kecepatan 26,8 FPS, sedangkan dimensi 512 memberi MOTA 68,5 dan 24,1 FPS (Tabel 6). Kombinasi IoU kotak, fitur re-ID, dan Kalman Filter menghasilkan MOTA 69,1 dan IDs 299, dibanding hanya IoU yang memberi MOTA 67,8 dan IDs 648 (Tabel 7). Secara keseluruhan, penulis melaporkan FairMOT menduduki peringkat pertama pada 2DMOT15, MOT16, MOT17, dan MOT20 melalui server evaluasi, dengan kecepatan 30 FPS pada satu GPU RTX 2080Ti. Semua angka di atas berasal dari tabel ablasi dan abstrak naskah, bukan dari percobaan baru di luar kajian ini.

Batasan yang dinyatakan penulis mencakup ketidakandalan fitur re-ID ketika objek sebagian tertutup, sehingga asosiasi perlu memakai IoU dan Kalman Filter sebagai cadangan. FairMOT hanya mengambil fitur pada titik pusat tanpa fitur wilayah, sehingga kinerjanya bergantung pada konvolusi deformabel; menggantinya dengan konvolusi biasa menurunkan hasil menjadi MOTA 65,0 dan AP 78,1. Waktu pencocokan re-ID bertambah secara linier dengan kepadatan objek karena pembaruan fitur setiap lintasan, meskipun waktu deteksi bersama re-ID hampir tidak terpengaruh kepadatan. Penulis juga mencatat bahwa jaringan yang lebih besar atau lebih kuat belum tentu meningkatkan akurasi pelacakan, dan bahwa metode penyeimbang rugi MGDA-UB mengarah pada MOTA paling rendah (63,6) karena terlalu bias ke re-ID.
