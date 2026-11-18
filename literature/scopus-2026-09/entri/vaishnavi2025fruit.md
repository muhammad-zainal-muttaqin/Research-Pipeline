# Fruit Detection and Yield Estimation using Path Aggregation Feature Pyramid Network and Deep SORT Algorithm: A Case Study on Orange Fruit

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vaishnavi2025fruit` |
| Judul asli | Fruit Detection and Yield Estimation using Path Aggregation Feature Pyramid Network and Deep SORT Algorithm: A Case Study on Orange Fruit |
| Penulis | Vaishnavi, M; Bharaniharan, A; Mohanapriya, S; Thanush, P |
| Tahun | 2025 |
| Venue | Proceedings of the 9th International Conference on Electronics Communication and Aerospace Technology Iceca 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [vaishnavi2025fruit.pdf](../pdf/vaishnavi2025fruit.pdf)
- DOI resmi: https://doi.org/10.1109/iceca66444.2025.11383116

## Gambaran Umum

Studi ini mengatasi kesalahan dan inefisiensi pada deteksi buah serta estimasi panen jeruk. Buah jeruk sulit dideteksi karena tingkat kematangannya beragam, warnanya menyatu dengan daun di dalam dan di sekitar pohon, serta tertutup oleh ranting atau buah yang bergerombol. Penulis mengusulkan kerangka yang menggabungkan Mask R-CNN, Path Aggregation Feature Pyramid Network (PA-FPN), dan Deep SORT untuk mendeteksi, mengsegmentasi, melacak, dan menghitung buah, sekaligus membedakan buah matang dan belum matang.

Tanaman yang dipelajari adalah jeruk (citrus). Data berupa 2.500 citra beresolusi 1920×1080 piksel dari beberapa kebun jeruk, dengan variasi cahaya pagi, siang, dan sore; cuaca cerah, berawan, dan setelah hujan; tahap tumbuh dan kerapatan buah; sudut serta jarak kamera; dan tingkat penutupan daun. Anotasi kebenaran dibuat manual oleh pakar pertanian untuk lokasi, tingkat kematangan, dan status oklusi. Data dibagi menjadi 70% latih, 15% validasi, dan 15% uji. Model Mask R-CNN memakai backbone ResNet-101 dengan bobot awal dari COCO yang disetel ulang. PA-FPN menambah jalur bottom-up di samping aliran top-down FPN, memakai koneksi lateral 256 kanal dan konvolusi 3×3 pada level P2 sampai P5. Region Proposal Network menghasilkan usulan menjadi kotak dan masker instance. Deep SORT memakai filter Kalman untuk prediksi gerak dengan asumsi kecepatan konstan, fitur penampilan 128 dimensi dari CNN terlatih, kesamaan kosinus, dan penugasan Hungarian yang menggabungkan jarak Mahalanobis dan kosinus. Klasifikasi kematangan mengubah RGB ke HSV, mengekstrak histogram, lalu memakai Support Vector Machine dengan validasi silang. Pencegahan penghitungan ganda memakai registri buah global, pengelompokan spasial, dan pemeriksaan konsistensi temporal.

Asosiasi lintas frame dijalankan dengan Deep SORT berdasarkan deteksi Mask R-CNN, dan setiap buah dihitung sekali melalui identitas lintas frame yang stabil. Pelatihan memakai PyTorch dan CUDA, laju pembelajaran 0,001 dengan cosine annealing, ukuran batch 8, 100 epoch dengan early stopping, optimizer Adam dengan weight decay 0,0001, serta augmentasi rotasi, skala, dan color jittering. Konfigurasi pelacak memakai usia lintasan maksimum 70 frame, hit minimum 3 deteksi, ambang IoU 0,3, dan dimensi fitur tampilan 128.

Angka hasil dinyatakan dengan metrik mAP@0.5 dan AP menurut ukuran buah untuk deteksi; MOTA, MOTP, jumlah identity switch (IDS), MAE, dan RMSE untuk pelacakan pada sekuens video; serta presisi, recall, dan F1 untuk klasifikasi kematangan. Pada data uji, AP buah kecil (luas di bawah 32² piksel) sebesar 91,3%, buah sedang (antara 32² dan 96² piksel) 94,7%, dan buah besar (di atas 96² piksel) 96,2%. Metode yang diusulkan mencatat MOTA 88,7%, MOTP 84,6%, IDS 34, MAE 1,6, dan RMSE 2,3, dibandingkan Deep SORT 82,4%, 81,2%, 89, 2,8, dan 4,1 serta SORT 76,2%, 78,5%, 142, 3,7, dan 5,2. Klasifikasi kematangan memberi F1 keseluruhan 93,2% (presisi 93,5%, recall 92,9%), dengan F1 buah matang 95,4% dan buah belum matang 91,0%. Ablasi pada Tabel IV menunjukkan mAP@0.5 naik dari 89,7% pada Mask R-CNN dasar menjadi 91,2% dengan FPN, 92,8% dengan PA-FPN, dan 93,2% setelah pengelompokan spasial; kecepatan inferensi turun dari 24,3 menjadi 18,7 FPS. Abstrak menyebutkan akurasi deteksi 95,8% dan presisi penghitungan 92,3% tanpa merinci acuan hitungnya. Batasan yang dinyatakan penulis: tidak dinyatakan. Naskah tidak memuat bagian khusus mengenai keterbatasan.

