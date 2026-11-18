# Physics-Informed Neural Network-Assisted Imaging for Oil Palm Fruit Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ng2026physics` |
| Judul asli | Physics-Informed Neural Network-Assisted Imaging for Oil Palm Fruit Ripeness Classification |
| Penulis | Ng, Kuan-Huei; Azaman, Mohd Ikmal Hafizi; Udos, Waldo; Khalid, Mohd Ramdhan Mohd; Mohd Bakri, Mohd Azwan; Lim, Kok-Sing |
| Tahun | 2026 |
| Venue | Electronics Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [ng2026physics.pdf](../pdf/ng2026physics.pdf)
- DOI resmi: https://doi.org/10.3390/electronics15030671

## Gambaran Umum

Kajian ini mengatasi penilaian kematangan tandan buah segar (TBS) kelapa sawit yang masih manual, subjektif, dan padat karya. Penulis menyatakan bahwa convolutional neural network (CNN) murni sangat bergantung pada dataset besar, beragam, dan berlabel baik, yang sulit diperoleh di pertanian. Kinerjanya menurun ketika data terbatas atau tidak seimbang serta ketika pencahayaan tidak merata. Tujuan kajian adalah menguji *Physics-Informed Neural Network* (PINN) yang menyisipkan pengetahuan fisik berupa indeks warna rasio merah–hijau langsung ke dalam arsitektur dan fungsi rugi, agar model lebih tangguh pada data yang sedikit dan tidak seimbang.

Tanaman yang dikaji adalah kelapa sawit. Dataset berisi 112 citra TBS yang diambil dengan kamera CMOS di bawah tiga kondisi pencahayaan: lampu halogen standar, lampu halogen dengan filter biru, dan lampu halogen dengan filter merah. Tiga kelas kematangan adalah *unripe* (18), *underripe* (49), dan *ripe* (45). Penulis memastikan sekurangnya 50 persen citra sebagian besar berisi buah murni agar duri, soket kosong, dan noda tidak mengganggu. Citra diubah ke ukuran 128 × 128 × 3. Sebanyak 62 citra dialokasikan ke latih dan 50 ke uji secara acak; karena sampel *unripe* sedikit, 13 di antaranya selalu masuk ke data latih. Pembagian acak diulang 15 kali, dan untuk validasi dipakai pembagian berlapis 80/20. Tidak ada augmentasi data.

Mekanisme deteksi memakai CNN dasar berupa tiga lapisan Conv2D (8, 16, dan 32 filter) dengan MaxPooling2D, GlobalAveragePooling2D, satu Dense 32 unit dengan regularisasi L2 faktor 0,01, dropout 0,4, serta kepala klasifikasi Softmax. PINN menambahkan skalar γRG, yaitu median nilai piksel merah dibagi median nilai piksel hijau dari citra mentah. Median dipilih karena lebih tahan terhadap nilai ekstrem dari duri, soket kosong, noda, dan pantulan spekular. Vektor fitur citra dikonkatenasi dengan γRG sebelum memasuki kepala klasifikasi. Fungsi rugi total dirumuskan sebagai Lcls + λ·Lphys, dengan Lcls berupa *sparse categorical cross-entropy* dan Lphys berupa kesalahan kuadrat rata-rata antara indeks kelas yang ditentukan persamaan linier γRG dan ekspektasi indeks kelas dari PINN. Persamaan linier tersebut diperoleh dari regresi least squares pada data latih, dengan slope m dalam [2,04; 2,53], intersep c dalam [−2,65; −1,84], dan R² dalam [0,61; 0,71]; nilainya dibatasi pada rentang [0, 3] dan dipotong menjadi 3 jika melebihi. Pelatihan memakai Adam dengan laju pembelajaran 0,001, batch 16, dan maksimal 500 epoch dengan penghentian awal patience 10.

Evaluasi memakai akurasi serta presisi, *recall*, dan F1 per kelas pada cawat uji 50 citra, dirata-ratakan atas 15 pembagian acak. PINN dengan λ = 0,6 mencapai akurasi puncak 0,73 ± 0,05, mengungguli CNN murni 0,68; bagian simpulan menulis angka 0,72. Kisaran λ 0,1–1,5 memberi akurasi 0,70–0,73, sedangkan λ = 5 menurunkan akurasi menjadi 0,69 dan λ = 50 menjadi 0,53. Pada kelas minoritas *unripe*, presisi PINN 0,59 ± 0,21 berbanding 0,41 ± 0,11 pada CNN. Pada kelas *underripe*, *recall* PINN 0,79 ± 0,10 berbanding 0,68 ± 0,08 dan F1 0,73 ± 0,06 berbanding 0,68 ± 0,05. Di bawah lampu halogen asli, PINN unggul pada kelas 2 dan 3 dengan F1 kelas 3 sebesar 0,84 ± 0,09 berbanding 0,82 ± 0,11. Dengan filter biru, PINN unggul pada kelas 1 dan 2, dengan presisi kelas 1 sebesar 0,47 ± 0,29 berbanding 0,32 ± 0,15. Dengan filter merah, PINN hanya unggul pada kelas 1.

Penulis menyatakan sejumlah keterbatasan. Kinerja PINN sangat sensitif terhadap koefisien λ; bobot fisika yang terlalu besar mengganggu optimasi karena dua tujuan tidak dapat dipenuhi secara bersamaan. Indeks γRG dibatasi pada rentang [0, 3], dan persamaan linier yang dipakai hanya memiliki R² antara 0,61 dan 0,71. Jumlah citra hanya 112 dengan kelas *unripe* berisi 18 sampel, 13 di antaranya selalu masuk ke data latih. Tidak ada augmentasi data. Data tidak tersedia untuk umum karena menjadi milik Malaysian Palm Oil Board dan masih menjadi bagian dari proyek yang berjalan. Penulis juga mencatat bahwa pada lampu halogen asli dan filter merah, CNN lebih baik pada kelas matang, masing-masing karena kurangnya kontras dan karena batasan fisik menjadi redundan atau menambah derau spektral.

