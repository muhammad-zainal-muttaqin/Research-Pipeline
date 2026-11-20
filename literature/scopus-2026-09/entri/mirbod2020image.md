# Towards image-based measurement of accurate apple size and yield using stereo vision cameras

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mirbod2020image` |
| Judul asli | Towards image-based measurement of accurate apple size and yield using stereo vision cameras |
| Penulis | Mirbod, Omeed; Choi, Daeun; Heinemann, Paul H; Marini, Richard P |
| Tahun | 2020 |
| Venue | Asabe 2020 Annual International Meeting |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [mirbod2020image.pdf](../pdf/mirbod2020image.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202001115

## Gambaran Umum

Makalah ASABE 2020 ini mengukur ukuran buah apel langsung di pohon sebelum panen. Ukuran buah penting karena harga apel untuk pasar segar jauh lebih tinggi daripada untuk pengolahan, sedangkan pengukuran manual di kebun memakan banyak tenaga. Penulis mengusulkan sistem pencitraan yang memakai penglihatan stereo untuk menghitung luas permukaan metrik setiap apel yang layak diukur.

Data dikumpulkan di Russell E. Larson Agricultural Research Center, Pennsylvania Furnace, Pennsylvania, pada 18 September 2019. Sistem memakai dua kamera FLIR Blackfly S (BFS-U3-88S6C-C) dalam konfigurasi stereo dan lampu kilat LED. Kamera dipasang pada kereta yang ditarik melewati dua baris pohon dengan kecepatan sekitar 1 m/s dan mengambil 3 citra per detik, sehingga terkumpul 380 citra dari 30 pohon. Kebenaran dasar berasal dari pengukuran diameter 10 apel per pohon dengan perangkat EFM dan dari berat hasil panen per pohon.

Metode terdiri atas empat tahap. Deteksi apel memakai random forest pada fitur SIFT dari lingkaran kandidat. Klasifikasi kelayakan memakai VGG-16 yang disesuaikan untuk klasifikasi biner, dilatih dengan 105 kandidat baik dan 90 kandidat tidak layak, lalu diperluas menjadi 4.600 potongan citra melalui rotasi. Segmentasi memakai Mask R-CNN yang dilatih dari 85 apel yang digambar manual. Luas permukaan dihitung dari jumlah piksel mask dan panjang piksel metrik yang diturunkan dari kedalaman stereo. Hasilnya, luas permukaan rata-rata per pohon berkorelasi dengan berat apel rata-rata per pohon dengan R2 0,69 saat kandidat dipilih jaringan, dan R2 0,75 saat kandidat dipilih manual. Penambahan ukuran buah pada hitungan buah meningkatkan korelasi terhadap hasil, tetapi peningkatannya disebut kecil.

Batasan yang dinyatakan penulis mencakup satu varietas dan satu jenis tajuk. Penulis juga mencatat bahwa jumlah kandidat yang kecil per pohon membatasi korelasi, dan bahwa perhitungan luas mengasumsikan permukaan buah datar pada satu kedalaman. Rencana kerja lanjutan adalah membandingkan sistem dengan sistem sortir pengemas dan memakai beberapa sudut pandang per pohon.
