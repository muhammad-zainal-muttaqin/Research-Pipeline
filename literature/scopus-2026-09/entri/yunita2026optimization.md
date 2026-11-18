# Optimization of the EfficientNet-Swin Transformer Hybrid Model with Dynamic Attention and Multi-task Learning for Accurate Palm Fruit Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yunita2026optimization` |
| Judul asli | Optimization of the EfficientNet-Swin Transformer Hybrid Model with Dynamic Attention and Multi-task Learning for Accurate Palm Fruit Classification |
| Penulis | Yunita, Fitri; Usman, Usman; Sawitri, Nina |
| Tahun | 2026 |
| Venue | International Journal of Intelligent Engineering and Systems |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [yunita2026optimization.pdf](../pdf/yunita2026optimization.pdf)
- DOI resmi: https://doi.org/10.22266/ijies2026.0131.10

## Gambaran Umum

Kajian ini mengatasi penilaian kematangan tandan buah sawit yang masih dilakukan secara manual dan dianggap subjektif, tidak konsisten, serta lambat untuk skala industri. Tujuan kajian adalah membangun model hibrida EfficientNet-Swin Transformer dengan perhatian dinamis dan pembelajaran banyak tugas (multi-task learning) untuk mengklasifikasikan kematangan buah sekaligus mendeteksi cacat. Penulis mengaitkan kematangan dengan rendemen minyak, mutu minyak, dan kemudahan pemurnian.

Data berupa 12.550 citra RGB tandan buah sawit dalam lima kelas: Defect, Overripe, Ripe, Underripe, dan Unripe. Pembagiannya adalah 10.085 citra latihan, 1.630 validasi, dan 835 uji. Tugas terpisah memakai 12.450 citra beranotasi untuk empat jenis cacat, yaitu retak, busuk, warna tidak normal, dan kerusakan, dengan pembagian 9.986/1.608/856. Masker cacat dibuat dengan pemrosesan citra: CLAHE dan deteksi tepi Canny untuk retak, ambang pada ruang warna HSV untuk busuk dan warna tidak normal, serta ambang adaptif untuk kerusakan, lalu disaring memakai luas minimum dan aproksimasi poligon Douglas-Peucker. Citra dinormalisasi ke rentang [0, 1], diperbanyak dengan rotasi, pergeseran, pembalikan, dan zoom, serta diubah menjadi 224 × 224 piksel. Validasi memakai StratifiedGroupKFold lima lipat.

Arsitektur memakai EfficientNet-B3 terlatih sebagai ekstraktor fitur lokal dengan tujuh blok MBConv dan modul squeeze-excitation. Peta fitur masuk ke dua blok Swin Transformer, yaitu W-MSA untuk perhatian dalam jendela dan SW-MSA untuk perhatian antarjendela, lalu diperbaiki dengan perhatian dinamis berupa perhatian kanal dan spasial CBAM. Modul adaptif menghitung indikator kandangan gambar dari kecerahan dan warna, menyusun peta saliensi, lalu mengatur bobot perhatian spasial dan kanal serta gain pada wilayah kritis. Fitur dari kedua jalur digabung dengan bobot campuran yang dipelajari. Kepala klasifikasi terdiri dari global average pooling, dropout, dense layer, dan softmax lima kelas. Pelatihan memakai AdamW, categorical cross-entropy, early stopping, dan ReduceLROnPlateau. Tugas bantu segmentasi cacat menambahkan loss IoU dan Dice.

Hasil utama adalah akurasi validasi rata-rata 97,16% ± 0,47% pada validasi silang lima lipat, dengan presisi 97,17%, recall 97,16%, F1 97,16%, dan AUC rata-rata 99,79%. Teks juga mencatat akurasi uji rata-rata 97,16% ± 0,34%. Padanan ablasi EfficientNet-B3 saja mencapai 95,21%; EffNetB3+SwinT 94,01%; EffNetB3+SwinT+SA 93,65%; EffNetB3+SwinT+CA 94,49%; dan EffNetB3+SwinT+DA 97,16%. Tugas segmentasi cacat memberi IoU 0,7305 dan koefisien Dice 0,7342. Waktu inferensi rata-rata 94,21 ms ± 2,20 ms dengan pemakaian memori rata-rata 6.588,9 MB.

Penulis menyatakan dua batasan. Pertama, kesalahan terjadi pada batas antar tahap kematangan yang berurutan karena perubahan warna berlangsung bertahap; pada lipat pertama Underripe hanya mencapai 93,26% dan banyak tertukar dengan Ripe dan Unripe. Kedua, model belum efisien untuk penerapan waktu nyata, dengan waktu 275-287 detik per epoch pada 50 epoch awal dan 82-90 detik per epoch setelahnya. Penulis mengusulkan transformer ringan, distillation pengetahuan, perhatian jarang, data multispektral, pembelajaran berkelanjutan, serta uji terhadap kompresi gambar, hilangnya frame, dan perubahan cahaya ekstrem.

