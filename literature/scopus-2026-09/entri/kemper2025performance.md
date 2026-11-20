# Performance Evaluation of Detection and Tracking Algorithms for Automated Grape Cluster Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kemper2025performance` |
| Judul asli | Performance Evaluation of Detection and Tracking Algorithms for Automated Grape Cluster Counting |
| Penulis | Kemper, Ricardo Jesus Huaman; Manrique, Pedro Antonio Zamora; Rosas, Diego Dustin Herrera; Gardini, Sixto Ricardo Prado |
| Tahun | 2025 |
| Venue | C3 2025 IEEE Colombian Caribbean Conference |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [kemper2025performance.pdf](../pdf/kemper2025performance.pdf)
- DOI resmi: https://doi.org/10.1109/c366505.2025.11340275

## Gambaran Umum

Penelitian ini bertujuan menilai kinerja kombinasi deteksi objek dan pelacakan
multi-objek untuk menghitung tandan anggur secara otomatis di kebun. Latar
belakangnya adalah estimasi hasil panen Manual dengan penghitungan tandan oleh
manusia memiliki tingkat kesalahan lebih dari 20% dan tidak praktis untuk
pemantauan skala besar. Penulis membandingkan dua detektor, YOLOv12 dan
RF-DETR, yang masing-masing dipasangkan dengan dua pelacak, BoT-SORT dan
ByteTrack, menghasilkan empat konfigurasi penghitungan.

Data dikumpulkan di kebun anggur varietas Allison pada tahap pemasakan akhir,
dalam kondisi alami. Penulis mengumpulkan 880 citra beresolusi 4080 × 3072
piksel, lalu membaginya menjadi 704 citra latih (80%), 88 citra validasi
(10%), dan 88 citra uji (10%). Kotak pembatas tandan dibuat secara
semi-otomatis dengan model GroundingDINO dan diverifikasi manual. Augmentasi
berupa pembalikan horizontal dan penyesuaian warna diterapkan hanya pada data
latih sehingga jumlahnya menjadi 2112 citra. Pengujian penghitungan
menggunakan sepuluh sequence video dengan durasi 34–91 detik yang menampilkan
kabur gerak dan okklusi oleh daun. Nilai acuan penghitungan diperoleh dari
penghitungan manual oleh pengamat manusia.

YOLOv12l dilatih selama 60 epoch dengan masukan 640 × 640, optimizer SGD
bermomentum, laju pembelajaran 10⁻⁴, dan fungsi rugi BCE serta CIoU. RF-DETR
Base dilatih dengan masukan 640 × 640, optimizer AdamW, laju pembelajaran
10⁻⁴, 60 epoch, serta fungsi rugi cross-entropy, L1, dan GIoU. ByteTrack
memakai asosiasi ambang ganda, penyaring Kalman, dan matriks biaya IoU;
BoT-SORT menambahkan modul re-identifikasi berbasis penampilan, aliran
optik, Kalman dengan kovarians adaptif, serta asosiasi Hungarian memakai
jarak kosinus. Penghitungan dilakukan dengan mengagregasi identitas unik yang
bertahan sepanjang video. Metrik yang dipakai adalah mAP dengan ambang IoU
0,50–0,95, plus MAE, MRE, dan RMSE terhadap hitungan manual.

Hasil utama menunjukkan YOLOv12 dengan BoT-SORT memberi kinerja terbaik:
MRE 15,69% (akurasi penghitungan relatif 84,31%), MAE 17,16, dan RMSE 20,80.
Konfigurasi parameter ketiga pada pasangan ini memberi hasil individu terbaik
dengan MAE 12,10, MRE 10,89%, dan RMSE 14,84. Pasangan YOLOv12–ByteTrack
mencatat MAE 18,74 dan MRE 17,03%. RF-DETR–BoT-SORT mencatat MAE 23,40 dan
MRE 19,88%, sedangkan RF-DETR–ByteTrack paling lemah dengan MAE 29,28 dan
MRE 22,12%. Pada pelatihan deteksi, mAP@[.50:.95] YOLOv12 naik dari sekitar
0,25 menjadi 0,73, sementara RF-DETR mulai sekitar 0,71 dan stabil di
kisaran 0,72–0,74. Seluruh angka penghitungan diacu terhadap hitungan manual
sepuluh video, dengan delapan konfigurasi detektor-pelacak yang masing-masing
dijalankan pada sepuluh video sehingga total 200 percobaan.

Batasan yang dinyatakan penulis mencakup penurunan kinerja pada perubahan
pencahayaan mendadak, okklusi parah, dan tumpang tindih rapat. RF-DETR
cenderung menghitung berlebih, terutama saat dipasangkan dengan ByteTrack,
karena deteksi positif palsu diperkuat oleh pelacak. Penulis menyatakan
penerapan pada morfologi tanaman lain memerlukan kalibrasi ulang, dan
mengusulkan pelacakan berbasis pembelajaran mendalam serta metode asosiasi
seperti StrongSORT untuk pekerjaan berikutnya.
