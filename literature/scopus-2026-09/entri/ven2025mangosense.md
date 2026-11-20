# MangoSense: A time-series vision sensing dataset for mango tree segmentation and detection toward yield prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ven2025mangosense` |
| Judul asli | MangoSense: A time-series vision sensing dataset for mango tree segmentation and detection toward yield prediction |
| Penulis | Ven, Janaksinh; Sharma, Charu; Syed, Azeemuddin |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [ven2025mangosense.pdf](../pdf/ven2025mangosense.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110524

## Gambaran Umum

Kajian ini berangkat dari kebutuhan prediksi hasil panen mangga yang akurat. Penulis menyebut bahwa penghitungan manual sangat padat tenaga kerja dan rawan kesalahan, dan tidak praktis untuk kebun berskala besar. Masalah lain yang diangkat adalah kurangnya kumpulan data berkualitas tinggi. Sebagian besar kumpulan data yang ada hanya merekam satu waktu, sehingga tidak menangkap pola pertumbuhan dan pembungaan dari waktu ke waktu. Tujuan kajian adalah menyajikan kumpulan data deret waktu berbasis citra untuk segmentasi dan deteksi bunga serta buah muda, yang nantinya dipakai untuk prediksi hasil.

Data dikumpulkan dari 12 pohon mangga di India. Dua varietas tercakup, yaitu Banginapalli dan Rasalu. Pohon nomor 6 adalah varietas Rasalu, sedangkan pohon lainnya Banginapalli. Setiap pohon dipotret dari delapan arah, yaitu barat daya, selatan, tenggara, timur, timur laut, utara, barat laut, dan barat. Pengambilan citra berlangsung dari 15 Februari hingga 30 April 2024 dalam delapan kunjungan. Total tercatat 768 citra RGB dari kamera ponsel 48 MP. Pemotretan dilakukan pagi (pukul 07.30 sampai 11.00 IST) dan sore (pukul 17.30 sampai 19.00 IST). Pada kunjungan terakhir, jumlah buah tiap pohon dihitung secara manual dua kali dan diambil rata-ratanya sebagai kebenaran dasar. Citra asli berukuran 8000 × 6000 piksel dipecah menjadi 147.456 *patch* berukuran 500 × 500 piksel. Dari jumlah itu, 40.424 *patch* memuat anotasi. Sebanyak 23.541 *patch* memuat kelas bunga dan 25.380 *patch* memuat kelas buah muda. Anotasi kelas bunga menempati 295.879.615 piksel, dan anotasi buah muda menempati 175.175.608 piksel, atau sekitar 4,66 persen dari total area data.

Anotasi segmentasi dibuat dengan alur semi-otomatis. Sebagian kecil data, yaitu 2 persen, dipakai untuk melatih ulang YOLOv8 pada tugas *bounding box*. Kotak tersebut kemudian menjadi perintah bagi *Segment Anything Model* (SAM) untuk menghasilkan poligon. Poligon digabung antarpatch, lalu ditinjau dan dikoreksi di CVAT. Penulis membandingkan lima model segmentasi, yaitu DeepLabV3+, PSPNet, SegFormer, Swin-S, dan YOLO+SAM. Empat model deteksi juga diuji, yaitu Mask R-CNN, Faster R-CNN, DETR, dan YOLO. Pelatihan memakai pralatih COCO, dan metrik yang digunakan adalah IoU, mAP50, serta mAP50-95.

Pada segmentasi dengan 70 persen data latih, Swin-S memperoleh mIoU 70,68, dengan IoU bunga 67,35 dan IoU buah muda 74,01. SegFormer memperoleh mIoU 69,76, dengan IoU bunga 66,44 dan IoU buah muda 73,07. DeepLabV3+ dan PSPNet masing-masing memperoleh mIoU 67,69. Teks juga menyebut bahwa YOLO+SAM memperoleh IoU tertinggi untuk buah muda, yaitu 78,97. Pada deteksi, YOLO paling baik untuk kedua kelas, dengan mAP50 63,8 untuk bunga dan 80,5 untuk buah muda. Penulis menilai segmentasi cocok untuk ekstraksi fitur bunga dalam model prediksi hasil. SegFormer dipilih sebagai pilihan yang kuat karena biaya komputasinya lebih rendah, dengan 13,7 juta parameter dibanding 50 juta pada Swin-S. Kajian juga membahas hubungan antara pola arah angin dan rasio konversi bunga menjadi buah. Temuan ini, menurut penulis, menantang anggapan sebelumnya yang hanya menghubungkan perbedaan hasil dengan struktur tajuk menurut orientasi.

Penulis menyatakan bahwa jumlah buah hasil hitung manual pada kunjungan terakhir dapat dipakai untuk pengembangan dan validasi model prediksi hasil di masa depan. Kumpulan data ini juga dirancang untuk mengisi kekosongan data deret waktu yang selama ini tidak tersedia pada kumpulan data mangga sebelumnya. Dengan demikian, kontribusi utama kajian ini terletak pada data dan tolok ukur segmentasi serta deteksi, bukan pada pencacahan buah pada tingkat individu. Perlu dicatat bahwa penelitian ini tidak menyajikan pencacahan buah otomatis yang dibandingkan langsung dengan jumlah hitung manual.
