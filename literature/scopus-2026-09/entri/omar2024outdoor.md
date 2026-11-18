# Outdoor oil palm fruit ripeness dataset

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `omar2024outdoor` |
| Judul asli | Outdoor oil palm fruit ripeness dataset |
| Penulis | Omar, Zaid; P.P. Abdul Majeed, Anwar; Rosbi, Munirah; Ghazalli, Shuwaibatul Aslamiah; Selamat, Hazlina |
| Tahun | 2024 |
| Venue | Data in Brief |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [omar2024outdoor.pdf](../pdf/omar2024outdoor.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2024.110667

## Gambaran Umum

Artikel ini menyajikan dataset citra tandan buah segar (TBS) kelapa sawit untuk penelitian deteksi kematangan berbasis pengolahan citra. Tujuannya menyediakan data dunia nyata di kondisi luar ruangan yang mencakup TBS masih menempel di pohon (sebelum panen) maupun di tanah (sesudah panen), guna mengembangkan dan menguji alur pembelajaran mesin untuk penilaian mutu TBS otomatis di luar ruangan. Dataset juga ditujukan untuk menguji algoritma koreksi warna, karena pencahayaan luar ruangan yang hangat dapat membuat tandan mentah tampak matang.

Tanaman yang dicitrakan adalah kelapa sawit (Elaeis guineensis) varietas Tenera, yang matang dalam 20–22 minggu dan berubah warna dari hitam ke merah, lalu jingga. Data dikumpulkan di perkebunan di Johor, Negeri Sembilan (melalui MPOB), dan Perak, Malaysia, dengan smartphone iPhone 11 dan Xiaomi 12 Lite yang dipasang pada monopod, memakai pengaturan kamera otomatis dan pencahayaan alami dari berbagai sudut. Sampel terdiri atas 176 buah dengan rata-rata tiga sampai empat citra per tandan, menghasilkan 466 citra berlabel dari lima kelas, yaitu damaged bunch, empty bunch, overripe, ripe, dan unripe; tiga kelas kematangan dan dua kelas mutu. Ukuran citra berkisar 757×568 sampai 3024×4032 piksel. Pelabelan ground truth dilakukan oleh grader berpengalaman berdasarkan panduan MPOB, yang membedakan kematangan warna dan persentase soket kosong (1–9% untuk underripe, 10–50% untuk ripe). Pembagian data berupa 371 citra latih dan 95 citra uji, dengan proporsi uji 20,3%; jumlah per kelas adalah damaged 12/3, empty 9/3, overripe 60/14, ripe 160/41, dan unripe 130/34 untuk latih/uji.

Penulis tidak menguji mekanisme deteksi atau penghitungan, melainkan klasifikasi citra. Dataset diuji pada jaringan YOLOv4-Tiny dengan teknik augmentasi khusus yang terdiri atas lima metode, yaitu perubahan warna pada ruang HSV, translasi pada sumbu x, penyesuaian kontras acak, serta overlay mask hujan dan mask bayangan, sehingga ukuran dataset menjadi enam kali lipat. Sebagai pembanding, penulis juga mengevaluasi classifier berbasis CNN dengan 371 citra latih, satu CPU, 100 epoch, learning rate 0,01, dan frekuensi validasi 30 iterasi.

Hasil yang dilaporkan berupa akurasi klasifikasi, bukan mAP atau metrik deteksi. YOLOv4-Tiny yang dilatih pada 371 citra latih setelah augmentasi mencapai akurasi uji 82,11%, sedangkan classifier CNN mencapai 55,79%. Metrik dihitung pada 95 citra uji yang terpisah dari 371 citra latih; penulis tidak menyatakan ambang IoU, split validasi, atau angka mAP.

Penulis menyatakan beberapa batasan. Dataset bias karena representasi TBS di pohon terbatas, terutama untuk kelas damaged, empty, dan overripe yang umumnya berasal dari tandan yang terlepas atau jatuh, sehingga jumlah tandan ripe dan unripe di pohon tidak seimbang. Distribusi kelas tidak terstandardisasi dengan variasi besar, khususnya pada kelas empty dan damaged yang populasi alaminya jauh lebih sedikit di perkebunan terawat. Pengambilan dengan monopod tidak menjangkau pohon lebih tinggi dari 3 meter, sehingga penulis menyarankan drone atau mekanisme lain. Penggunaan hanya dua model smartphone juga membatasi keragaman perangkat, dan penulis menyarankan lebih banyak model ponsel.

