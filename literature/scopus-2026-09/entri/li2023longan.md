# A longan yield estimation approach based on UAV images and deep learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2023longan` |
| Judul asli | A longan yield estimation approach based on UAV images and deep learning |
| Penulis | Li, Denghui; Sun, Xiaoxuan; Jia, Yuhang; Yao, Zhongwei; Lin, Peiyi; Chen, Yingyi; Zhou, Haobo; Zhou, Zhengqi; Wu, Kaixuan; Shi, Linlin; Li, Jun |
| Tahun | 2023 |
| Venue | Frontiers in Plant Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [li2023longan.pdf](../pdf/li2023longan.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2023.1132909

## Gambaran Umum

Penelitian ini bertujuan mengestimasi hasil panen longan per pohon sebelum panen dalam lingkungan kebun yang kompleks. Penghitungan hasil secara visual manual memerlukan biaya tenaga kerja tinggi, memakan waktu, dipengaruhi subjektivitas pengamat, serta memiliki akurasi dan efisiensi rendah. Penulis mengusulkan metode yang menggabungkan citra UAV, pembelajaran mendalam, dan analisis regresi. Buah longan tumbuh bergerombol di bagian luar kanopi dan sering tertutup daun serta ranting, sehingga deteksi buah menjadi bagian yang menentukan akurasi estimasi.

Data dikumpulkan di kebun longan Guangzhou pada 1–25 Juli 2021 dan 1–26 Juli 2022, pada dua rentang waktu, yaitu 07.30–11.30 dan 13.30–18.30. Penulis memperoleh 1.100 citra valid dan 16 video kanopi lengkap, serta menghitung secara manual jumlah tandan (Cluster_Fruit), jumlah buah tunggal (Single_Fruit), dan mutu 16 tandan dari 16 pohon. Kamera RGB 12 megapiksel dengan sudut pandang 85 derajat dipasang pada UAV DJI Mavic 2 Pro. UAV terbang mengelilingi pohon dengan kamera menghadap ke tengah pohon; citra disimpan pada resolusi 1280×720 piksel pada hari cerah dan berawan. Kedua varietas yang dicitrakan adalah Shixia dan Chuliang. Dari proses pemotongan dan anotasi, dibangun dua himpunan data: 1.100 citra tandan dengan 11.239 anotasi tandan dan 1.100 citra buah tunggal dengan 24.045 anotasi buah. Masing-masing dibagi menjadi data latih, validasi, dan uji dengan rasio 8:1:1, yaitu 880/110/110 citra.

Sistem memakai model dua tahap. Model CF-YD menggabungkan YOLOv5s yang dimodifikasi dengan DeepSORT untuk mendeteksi tandan pada video kanopi dan memberikan nomor identitas; jumlah ID maksimum diambil sebagai jumlah tandan. Model SF-YD menggabungkan YOLOv7 dengan DeepSORT: setiap tandan hasil CF-YD dipotong dari citra asli, lalu buah tunggal di dalamnya dideteksi dan dihitung memakai ID maksimum. Hasil kedua model dikoreksi dengan persamaan regresi yang dibangun dari 10 pohon yang dihitung manual: jumlah tandan mengikuti regresi binomial y=0,0023x²+0,7155x+19,562 (R²=0,9970), sedangkan jumlah buah per tandan mengikuti regresi eksponensial y=7,822e^(0,0565x) (R²=0,9953). Hasil panen per pohon dihitung dari jumlah buah tunggal terkoreksi, selisih tandan prediksi dan terdeteksi, jumlah buah rata-rata per tandan, serta berat buah rata-rata. Berat buah rata-rata yang dipakai adalah 13 g untuk Chuliang dan 8 g untuk Shixia, menurut pakar hortikultura yang dikutip penulis.

Pelatihan CF-YD memakai ukuran citra 1280×1280, IoU 0,5, laju pembelajaran awal 1e−4 hingga 1e−5, rasio latih–validasi 90:10, dan 500 epoch. SF-YD menormalkan citra menjadi 640×640, memakai SGD dengan laju awal 0,01, momentum 0,9, peluruhan bobot 5e−4, serta penjadwalan cosine annealing; tahap Freeze berlangsung 50 epoch dengan batch 4 dan tahap UnFreeze 250 epoch dengan batch 2. Anchor box diperoleh dengan k-means dan algoritma genetika, sembilan ukuran per model. Pada himpunan uji, CF-YD mencatat precision 83,50%, recall 85,70%, AP 82,40%, F1 0,85, dan 56,21 frame per detik; SF-YD mencatat 93,23%, 91,97%, 97,12%, 0,93, dan 98,35 frame per detik. Untuk pelacakan, CF-YD memiliki 5 pergantian ID, MOTA 95,30%, dan MOTP 92,60%; SF-YD memiliki 2 pergantian ID, MOTA 97,20%, dan MOTP 94,70%. Pengujian pada enam pohon dan enam tandan lain memberi tingkat galat rata-rata 2,66% untuk jumlah tandan dan 2,99% untuk jumlah buah tunggal, dengan seluruh galat di bawah 5%.

Penulis menyatakan beberapa batasan. Kebun longan sebagian besar tidak terstruktur, sehingga kemampuan deteksi dan pelacakan perlu ditingkatkan. UAV terutama merekam kanopi dari arah elevasi dan tidak memperoleh citra menyeluruh dari dalam kanopi, sehingga data yang terkumpul berbeda dari nilai sebenarnya. Galat juga timbul karena model memiliki akurasi terbatas dan karena acuan manual dihitung dari banyak sudut serta seluruh bagian pohon, sementara UAV hanya menangkap bagian luar kanopi dari depan. Penulis menganjurkan perencanaan lintasan UAV otomatis, pemroses citra di UAV untuk penghitungan langsung, penambahan data hitung manual untuk memperbaiki persamaan regresi, serta pengujian pada lebih banyak varietas.

