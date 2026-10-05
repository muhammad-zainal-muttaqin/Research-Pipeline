# On-Tree Mango Fruit Count Using Live Video-Split Image Dataset to Predict Better Yield at Pre-Harvesting Stage

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nenavath2024tree` |
| Judul asli | On-Tree Mango Fruit Count Using Live Video-Split Image Dataset to Predict Better Yield at Pre-Harvesting Stage |
| Penulis | Nayak Nenavath, Devender; Perumal, Boominathan |
| Tahun | 2024 |
| Venue | International Journal of Electrical and Computer Engineering Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | mango |

## Tautan Akses
- PDF: [nenavath2024tree.pdf](../pdf/nenavath2024tree.pdf)
- DOI resmi: https://doi.org/10.32985/ijeces.15.9.5

## Gambaran Umum
Makalah ini mengusulkan cara menghitung buah mangga pada pohon dari video yang direkam mengelilingi pohon sebesar 360 derajat. Video dipecah menjadi bingkai, delapan bingkai dipilih sebagai wakil delapan arah mata angin (timur, selatan, barat, utara, tenggara, barat daya, timur laut, barat laut), dan buah pada bingkai itu dideteksi dengan YOLOv7. Pemilihan delapan bingkai dimaksudkan untuk menghindari penghitungan ganda. Mangga yang berada di tepi bingkai (*corner mango*) dikoreksi dengan persamaan yang tidak terbaca pada teks ekstraksi.

Data berasal dari kebun di Distrik Vikarabad, Negara Bagian Telangana, India, pada kultivar 'Banganapalle'. Pada satu pohon dengan acuan hitung manual 130 buah, YOLOv7 dengan teknik delapan sisi menghasilkan hitungan 133 buah, yang dilaporkan sebagai akurasi 97,7% dengan waktu inferensi rerata 17,112 ms. Pada 14 pohon, akurasi YOLOv7 dilaporkan 95,48% dengan waktu inferensi 17 ms. Penulis juga melaporkan bahwa pengambilan citra pada pagi hari memberikan akurasi deteksi terbaik.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Hitung manual buah pada pohon bersifat mahal dan memakan waktu. Penaksiran jumlah buah sebelum panen membantu petani memperkirakan hasil dan menentukan harga jual. Pada pohon mangga, buah sering tersembunyi di balik daun atau cabang dan saling menutupi, sehingga hitungan dari citra tunggal tidak lengkap, sedangkan penggabungan banyak citra berisiko menghitung buah yang sama lebih dari sekali.

Pada tinjauan pustaka makalah, penulis menyebut bahwa metode penghitungan yang ada mencakup hitung kotak pembatas (*bounding box*), garis vertikal atau horizontal, SORT, ROS, serta ROI dengan ID unik. Penulis juga menyatakan bahwa satu model tidak dapat dipakai untuk semua varietas mangga karena variasi bentuk dan warna, sehingga dataset khusus diperlukan.

## Ide Utama
Gagasannya adalah memakai jumlah bingkai yang kecil dan tetap per pohon, yaitu delapan bingkai pada delapan arah, sehingga setiap bagian pohon hanya tampil sekali atau dua kali dan hitungan ganda terkontrol. Bingkai diambil dari video putar penuh dengan membagi jumlah seluruh bingkai dengan delapan, lalu mengambil satu bingkai pada tiap segmen. Mangga yang terpotong di tepi bingkai dikoreksi lewat Persamaan (5), dengan FTM sebagai total mangga pada bingkai dan FCM sebagai mangga di tepi bingkai. Bentuk persamaan itu tidak terbaca dari teks ekstraksi.

Jadi, identitas lintas pandang ditangani secara geometris dan tidak lewat pelacakan atau pencocokan buah: arah pandang dipilih sehingga hanya tumpang tindih tepi yang tersisa.

## Cara Kerja Langkah demi Langkah

```
  Video 360 derajat -> pecah ke bingkai -> pilih 8 bingkai (8 arah)
        -> YOLOv7 (deteksi, kelas: Mango / Hidden-Mango / Corner-Mango)
        -> hitungan per bingkai -> koreksi mangga tepi (Pers. 5) -> total
```

### 1. Akuisisi data
Video direkam pada kultivar 'Banganapalle' di Distrik Vikarabad, Telangana, India, antara pukul 06.00 dan 08.00 pagi dengan ponsel iQOO Z3 5G. Kamera bergerak searah jarum jam mengelilingi pohon selama 45 sampai 75 detik, dengan resolusi 1080×1920 (potret), sekitar 30 bingkai per detik, dan format mp4 berukuran 70 sampai 160 MB. Contoh video 152 MB menghasilkan 2.228 bingkai. Rekaman di kebun yang diuji untuk satu pohon dilakukan dengan hitung manual pada 30 Mei 2022.

### 2. Anotasi dan pembagian data
Anotasi memakai LabelImg dalam format YOLO. Dari 360 bingkai, 288 dipakai untuk pelatihan dan 72 untuk pengujian dan validasi (rasio 80:20). Pada percobaan satu pohon, 179 dari 224 citra dipakai untuk pelatihan dan sisanya (20%) untuk pengujian dan validasi. Makalah menyebut tiga kelas pada Gambar 4: *Hidden-Mango*, *Mango*, dan *Corner-Mango*, dan menggambarkan keluaran sebagai klasifikasi multikelas. Kelas ini adalah kategori visibilitas dan posisi, bukan tingkat kematangan.

### 3. Model dan pelatihan
Model yang dibandingkan adalah YOLOv5n, YOLOv5s, YOLOv7, dan YOLOv7-tiny. Pelatihan memakai PyTorch (CUDA 11.6, Python 3.9.0) pada GPU NVIDIA GeForce RTX 2080 SUPER dengan ukuran masukan 640×640, 500 epoch, laju belajar awal 0,01, dan ukuran batch 8. Pada pembahasan, model dibandingkan pada 100 dan 500 epoch dan pada ukuran batch 8 dan 16.

### 4. Penghitungan
Hitungan tiap pohon diperoleh dari delapan bingkai. Makalah juga menyebut penggunaan algoritma DeepSORT-count dan SORT pada bagian metode, tetapi pada bagian hasil tidak ada hasil pelacakan: seluruh hitungan pohon diperoleh dari delapan bingkai terpilih. Hubungan antara SORT dan penghitungan delapan sisi tidak dijelaskan.

## Eksperimen dan Hasil
Percobaan satu pohon membandingkan hitungan model terhadap hitung manual 130 buah, dengan masukan empat sisi dan delapan sisi (Tabel 1 makalah).

| Model | Manual | Hitungan 4 sisi | Inferensi 4 sisi (s) | Hitungan 8 sisi | Inferensi 8 sisi (s) |
|---|---|---|---|---|---|
| YOLOv5n | 130 | 66 | 0,0384 | 135 | 0,03927 |
| YOLOv5s | 130 | 71 | 0,07155 | 145 | 0,07292 |
| YOLOv7 | 130 | 60 | 0,01575 | 133 | 0,01711 |
| YOLOv7-tiny | 130 | 71 | 0,01075 | 141 | 0,01200 |

Hitungan empat sisi jauh di bawah acuan (60 sampai 71 dari 130), sedangkan delapan sisi mendekati acuan. YOLOv7 delapan sisi menghasilkan 133 dan dilaporkan sebagai akurasi 97,7% pada 17,112 ms. Rumus akurasi tidak terbaca dari teks.

Percobaan 14 pohon dengan model delapan sisi. Hitungan manual 14 pohon disajikan pada Gambar 6 dan perbandingan model pada Gambar 7; kedua gambar tidak terbaca pada teks ekstraksi. Angka yang tertulis di teks adalah sebagai berikut.

| Model | Akurasi (%) | Waktu inferensi rerata |
|---|---|---|
| YOLOv7 | 95,48 | 17 ms |
| YOLOv7-tiny | 94,1 | 16 ms |
| YOLOv5n | 94,1 | 104,5 ms |
| YOLOv5s | 97,2 | 85,69 ms |

Catatan: teks menyebut YOLOv5s 97,2%, lebih tinggi daripada YOLOv7 (95,48%), tetapi makalah menyimpulkan bahwa YOLOv7 terbaik berdasarkan akurasi dan waktu inferensi. Kalimat pada teks untuk YOLOv5n dan YOLOv5s menyebut "waktu inferensi rerata 94,1%" dan "97,2%", sehingga tampak bahwa angka itu adalah akurasi.

Waktu pengambilan citra. Dengan 96 citra per periode, akurasi deteksi pagi (06.00 sampai 09.00) adalah 84%, siang (10.00 sampai 15.00) 42%, dan sore (16.00 sampai 18.00) 57% (Tabel 2). Pada Tabel 3, hasil model per periode terhadap hitungan aktual hanya disajikan sebagai nilai tanpa label kolom yang jelas pada teks ekstraksi, sehingga tidak diinterpretasikan di sini. Penulis menyimpulkan bahwa pagi hari adalah waktu terbaik.

## Kelebihan dan Keterbatasan
Kelebihan menurut makalah: prosedur pengambilan data sederhana (satu video dari ponsel), jumlah bingkai kecil sehingga komputasi ringan, inferensi sekitar 17 ms, dan rekomendasi praktis waktu perekaman. Hitungan delapan sisi jauh lebih dekat ke hitung manual daripada empat sisi pada satu pohon.

Keterbatasan yang dinyatakan penulis: video harus direkam hanya ke arah maju, tidak dalam gerak lambat, dan tidak dalam arah terbalik. Penulis juga menyebut bahwa model untuk satu varietas mangga tidak dapat diterapkan pada varietas lain.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Validasi pada satu pohon dan 14 pohon hanya memakai satu kultivar dari satu lokasi. Hitung manual tunggal dipakai sebagai acuan tanpa pengulangan. Hanya jumlah, bukan kecocokan buah per buah, yang dibandingkan, sehingga kesalahan yang saling meniadakan tidak terdeteksi. Pada Tabel 1, hitungan delapan sisi untuk semua model melebihi acuan (133 sampai 145 dari 130), sehingga hitungan berlebih tidak dibahas. Prosedur pemilihan bingkai dengan membagi jumlah bingkai dengan delapan mengasumsikan kecepatan keliling yang seragam; asumsi ini tidak diuji. Persamaan akurasi dan koreksi mangga tepi tidak terbaca. Pembagian data latih dan uji dilakukan pada bingkai dari video yang sama, sehingga bingkai uji berpotensi mirip dengan bingkai latih; makalah tidak menjelaskan pemisahan per pohon.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali, yakni dari banyak sisi pohon, dengan mekanisme geometris sederhana: delapan bingkai pada delapan arah dan koreksi untuk mangga yang berada di tepi bingkai. Tidak ada pencocokan identitas antar-bingkai dan tidak ada rekonstruksi 3D. Dengan demikian, identitas lintas pandang tidak dipertahankan secara eksplisit. Hitungan tidak dilaporkan per kelas kematangan. Kelas yang ada adalah *Mango*, *Hidden-Mango*, dan *Corner-Mango*. Acuan hitung adalah hitung manual pada pohon (130 buah pada satu pohon dan sejumlah pohon pada percobaan 14 pohon), dan bukan hasil panen.

Untuk pencacahan tandan kelapa sawit multi-sisi, makalah ini berguna sebagai contoh dasar (*baseline*) tanpa pencocokan identitas: kelemahannya terlihat pada hitungan empat sisi yang jauh di bawah acuan dan hitungan delapan sisi yang lebih tinggi dari acuan, yang menunjukkan bahwa tumpang tindih antar-sisi tidak dikendalikan secara tepat. Gagasan kelas posisi tepi bingkai dapat dipertimbangkan, tetapi tidak menggantikan pencocokan antar-pandang.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `nenavath2024tree`.

Nenavath dan Perumal merekam video 360 derajat di sekitar pohon mangga 'Banganapalle', memilih delapan bingkai pada delapan arah, dan menghitung buah dengan YOLOv7. Pada satu pohon dengan hitung manual 130 buah, hitungan empat sisi hanya 60 sampai 71 buah, sedangkan hitungan delapan sisi 133 buah untuk YOLOv7 (akurasi dilaporkan 97,7%). Pada 14 pohon, akurasi YOLOv7 dilaporkan 95,48%.

Catatan verifikasi data: Angka satu pohon bersumber dari Tabel 1 (seksi 4.1) dan angka 14 pohon dari seksi 4.2; grafik pendukungnya (Gambar 6 dan 7) tidak terbaca pada teks ekstraksi. Angka waktu pengambilan citra bersumber dari Tabel 2 dan 3, dan Tabel 3 tidak dapat ditafsirkan dari teks. Persamaan (4) dan (5) tidak terbaca, sehingga rumus akurasi dan koreksi mangga tepi tidak dapat diverifikasi. Jumlah pohon pada percobaan 14 pohon, dan jumlah total buah yang dihitung manual, tidak tertera selain pada gambar. Kelas, ukuran dataset, dan akurasi dinyatakan penulis dan tidak diverifikasi ulang. Teks ekstraksi secara umum utuh.
