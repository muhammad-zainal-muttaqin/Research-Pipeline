# Frontiers and advances of deep learning-based fruit and vegetable image analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ma2026frontiers` |
| Judul asli | Frontiers and advances of deep learning-based fruit and vegetable image analysis |
| Penulis | Ma, Jinlin; Wan, Yuetong; Min, Weiqing; Ma, Ziping; Tan, Lidao; Jiang, Shuqiang |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [ma2026frontiers.pdf](../pdf/ma2026frontiers.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.111256

## Gambaran Umum

Kajian ini adalah tinjauan (survei) tentang analisis citra buah dan sayuran yang memakai pembelajaran mendalam (*deep learning*). Penulisnya J. Ma dan kawan-kawan, terbit di *Computers and Electronics in Agriculture* volume 241 (2026), artikel 111256. Tinjauan ini merangkum lebih dari 270 studi yang relevan, sesuai pernyataan di bagian simpulan. Cakupannya luas: klasifikasi, deteksi, segmentasi, penilaian mutu, estimasi hasil, dan lokalisasi objek pada buah dan sayuran.

Penilaian mutu dibahas di bagian 5.2, yang dibagi menjadi analisis kematangan (5.2.1) dan evaluasi mutu (5.2.2). Bagian 5.3 membahas estimasi hasil. Pembukaannya menyebut bahwa penghitungan buah secara akurat penting untuk mengetahui jumlah hasil panen di lapangan, dan bahwa cara manual memakan waktu dan biaya tinggi (Du dan Liu, 2023). Metode estimasi hasil dibagi menjadi dua kelompok: penghitungan langsung dan penghitungan tidak langsung berbasis penghitungan. Tinjauan ini tidak membahas penghitungan sebagai topik tunggal. Penghitungan menjadi salah satu tugas di antara beberapa tugas analisis citra lainnya.

Dalam bagian 5.2 dan 5.3, tinjauan mengutip beberapa angka hasil dari studi asli. Liu (2020) memakai jaringan Interfruit untuk klasifikasi buah dan melaporkan akurasi klasifikasi 93,17% pada dataset privat. Zhu dkk. (2018) memakai AlexNet untuk klasifikasi sayuran dan melaporkan akurasi 92,1%. Tinjauan menyebut hasil itu jauh melampaui dua metode pembelajaran mesin tradisional yang dibandingkan. Dong dkk. (2021) memodifikasi AlexNet untuk klasifikasi penyakit stroberi. Peningkatan akurasi yang dilaporkan sebesar 3,55% dibanding baseline, waktu pelatihan rata-rata turun 44,3%, dan ukuran model mengecil menjadi 12% dari ukuran asli. Angka-angka ini berasal dari studi yang dikutip, bukan hasil yang diverifikasi ulang oleh tinjauan. Dataset dan kondisi uji studi-studi itu berbeda satu sama lain, sehingga angkanya tidak bisa langsung dibandingkan. Tinjauan juga mencantumkan metrik yang dipakai di berbagai studi: akurasi, presisi, recall, F1, IoU, galat L2, RMSE, MRE, mAP, MPA, dan AP.

Simpulan tinjauan menyebut empat tantangan. Pertama, kebutuhan dataset besar dan berkualitas tinggi. Kedua, gangguan latar belakang dan kebutuhan model ringan. Ketiga, penggunaan UAV dan robot otonom. Keempat, model besar dan AIGC yang berhadapan dengan keterbatasan daya komputasi. Tiga dari empat tantangan itu berkaitan dengan kondisi lapangan dan perangkat, bukan dengan arsitektur model.
