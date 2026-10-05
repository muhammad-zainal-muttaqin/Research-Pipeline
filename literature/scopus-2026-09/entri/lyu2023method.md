# Method for estimation of bagged grape yield using a self-correcting NMS-ByteTrack

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lyu2023method` |
| Judul asli | Method for estimation of bagged grape yield using a self-correcting NMS-ByteTrack |
| Penulis | Lyu, J.; others |
| Tahun | 2023 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [lyu2023method.pdf](../pdf/lyu2023method.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202304116

## Gambaran Umum
Makalah ini mengusulkan metode pendugaan hasil panen anggur berkantong (*bagged grape*) dari video yang direkam dengan telepon pintar. Detektor berupa YOLOv5s, dan pelacak berupa ByteTrack yang dimodifikasi pada tiga hal: operasi penekanan non-maksimum (*non-maximum suppression*, NMS) dipindahkan dari tahap deteksi ke tahap pelacakan, kompensasi gerak kamera ditambahkan, dan vektor keadaan filter Kalman diubah dari rasio aspek menjadi lebar kotak. Penghitungan dilakukan dengan strategi garis hitung yang menghitung setiap ID satu kali.

Data berasal dari kebun peragaan Paidengte di Distrik Bishan, Chongqing, Tiongkok. Terdapat 500 citra asli yang diperluas menjadi 2.000 citra melalui augmentasi, serta enam video uji berdurasi rata-rata sekitar 20 detik. Pada pelacakan, metode usulan mencapai MOTA 64,6%, MOTP 82,4%, dan IDF1 80,8%, atau naik 1,7, 1,0, dan 4,1 poin persentase dibandingkan ByteTrack, dengan jumlah pertukaran ID turun dari 6 menjadi 3. Rerata akurasi penghitungan (*average counting precision*) terhadap hitungan manual pada enam video adalah 82,8%.

Makalah berbahasa Mandarin (dengan abstrak berbahasa Inggris); ringkasan ini dibuat dari teks berbahasa Mandarin.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pendugaan hasil anggur secara tradisional memakai penghitungan sampel manual yang menyita waktu dan hasilnya kurang akurat. Penghitungan dari citra tunggal dinilai tidak memadai untuk pohon besar karena satu citra tidak memuat seluruh buah pohon, sehingga video dipilih. Pada video, kesulitan utama terletak pada pelacakan.

Tiga masalah dirumuskan penulis. Pertama, setelah dikantongi, volume anggur membesar sehingga buah saling tumpang tindih, dan sebagian kotak deteksi tersaring pada tahap deteksi sehingga pelacakan tidak akurat. Kedua, video yang diambil tangan memiliki kecepatan tidak stabil sehingga target hilang. Ketiga, daun besar dan buah berkantong yang saling menutupi menyebabkan lintasan hilang atau identitas berganti, sehingga cara memberi ID berurutan pada tiap buah dan menghitung ID terbesar dinilai tidak cocok.

## Ide Utama
Ide utamanya adalah memperbaiki tiga titik lemah pelacakan berbasis deteksi untuk buah besar yang saling menutupi. NMS dipindahkan setelah penyaringan kotak berdasarkan IoU terhadap kotak prediksi filter Kalman, sehingga kotak buah tertutup yang biasanya terbuang pada tahap deteksi tetap tersedia bagi pelacak. Kompensasi gerak kamera mengoreksi posisi prediksi akibat gerakan tangan penyiam kamera. Garis hitung di tengah bingkai memastikan satu ID dihitung sekali walaupun lintasan sempat terputus.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Pengambilan data memakai kamera ponsel Redmi K40 dan OPPO Reno6 Pro+ pada anggur berkantong yang sama pada pukul 08.00, 12.00, dan 18.00, dengan sudut depan, samping, dan atas. Total waktu pemotretan sekitar 6 jam, tinggi kamera sekitar 1,5 m dari tanah, dan rute pemotretan baris demi baris. Diperoleh 500 citra beresolusi 4.000 × 3.000 atau 4.096 × 3.072 piksel dan enam video efektif berformat MP4, 1.920 × 1.080 piksel, 30 bingkai per detik, rata-rata berdurasi sekitar 20 detik dengan kecepatan tidak konstan. Kultivar anggur tidak dilaporkan.

### 2. Augmentasi dan anotasi
Lima ratus citra diperluas menjadi 2.000 citra dengan penguatan saturasi, peningkatan dan penurunan kecerahan, serta pencerminan. Citra dibagi acak 8:2 menjadi data latih dan validasi, dan enam video dijadikan data uji. Citra dianotasi dengan MAKE SENSE, dan video dianotasi bingkai demi bingkai dengan DarkLabel.

### 3. Detektor YOLOv5s
YOLOv5s dipilih karena cepat dan mudah diterapkan. Pelatihan memakai 600 epoch, ukuran batch 36, optimizer SGD dengan laju belajar awal 0,01 dan penurunan kosinus, momentum 0,937, dan *weight decay* 0,0005. Perangkat: Intel Core i5-12400F, RAM 16 GB, RTX 3060 12 GB, PyTorch 1.12.0.

### 4. NMS-ByteTrack
Pada tiap bingkai, filter Kalman memprediksi posisi target, lalu IoU antara kotak deteksi dan kotak prediksi dihitung. Kotak dengan IoU di atas ambang dipertahankan, kemudian NMS dijalankan pada kotak yang tersisa untuk mendapatkan kandidat pencocokan. Pencocokan dua tahap ByteTrack (kotak berkeyakinan tinggi lalu rendah) kemudian dipakai.

### 5. Kompensasi gerak kamera dan filter Kalman yang diperbaiki
Titik kunci latar belakang (selain target) diekstraksi dari bingkai sebelumnya dan bingkai saat ini, dicocokkan dengan aliran optik jarang (*sparse optical flow*), dan matriks transformasi afin gerak latar dihitung dengan RANSAC. Matriks itu dipakai untuk memindahkan kotak prediksi dari koordinat bingkai sebelumnya ke bingkai saat ini. Vektor keadaan filter Kalman diubah dari $[x, y, a, h, v_x, v_y, v_a, v_h]$ (a adalah rasio aspek) menjadi $[x, y, w, h, v_x, v_y, v_w, v_h]$ dengan w lebar; penulis menyatakan ablasi menunjukkan lebar lebih baik.

### 6. Garis hitung
Garis hitung diletakkan di tengah layar, dan beberapa detik pertama setiap video disisakan tanpa anggur. Sebuah buah dihitung ketika titik pusat kotak pelacaknya menabrak garis, dan ID yang sama hanya dihitung sekali. Akurasi penghitungan didefinisikan sebagai $A_{cp} = \frac{1}{n}\sum (1 - |S - G|/G) \times 100\%$ dengan S hitungan sistem dan G hitungan manual.

```
 video --> YOLOv5s --> IoU terhadap prediksi Kalman --> NMS
       --> ByteTrack + kompensasi gerak kamera + Kalman (lebar)
       --> pusat kotak menabrak garis tengah, ID baru --> hitungan + 1
```

## Eksperimen dan Hasil
Detektor dibandingkan dengan YOLOX-s dan YOLOv7. Pelacak dibandingkan dengan DeepSORT, MOTDT, Bot-SORT, StrongSORT, dan ByteTrack. Metrik deteksi adalah presisi, *recall*, dan AP; metrik pelacakan adalah MOTA, MOTP, IDF1, dan jumlah pertukaran ID (IDSW); metrik penghitungan adalah akurasi penghitungan rata-rata.

Tabel 1. Deteksi anggur berkantong (Tabel 1 makalah, dalam persen).

| Detektor | Presisi | Recall | AP |
|---|---|---|---|
| YOLOv5s | 97,6 | 96,2 | 97,6 |
| YOLOX-s | 94,8 | 93,1 | 90,0 |
| YOLOv7 | 97,1 | 96,4 | 97,2 |

Pembesaran data dari 500 menjadi 2.000 citra menaikkan presisi dari 94,3% menjadi 97,6%, recall dari 88,4% menjadi 96,2%, dan AP dari 95,0% menjadi 97,6% (Tabel 3).

Tabel 2. Perbandingan pelacak (Tabel 2 makalah).

| Pelacak | MOTA (%) | MOTP (%) | IDF1 (%) | IDSW |
|---|---|---|---|---|
| DeepSORT | 59,7 | 82,9 | 66,6 | 14 |
| MOTDT | 54,8 | 80,6 | 70,2 | 12 |
| Bot-SORT | 61,9 | 75,9 | 75,1 | 31 |
| StrongSORT | 59,4 | 78,1 | 74,6 | 14 |
| ByteTrack | 62,9 | 81,4 | 76,7 | 6 |
| Metode usulan | 64,6 | 82,4 | 80,8 | 3 |

Ablasi (Tabel 4): ByteTrack dasar memperoleh MOTA 62,9%, MOTP 81,4%, IDF1 76,7%, IDSW 6; ditambah filter Kalman yang diperbaiki menjadi 63,7%, 82,2%, 77,4%, dan 5; ditambah kompensasi gerak kamera menjadi 64,3%, 82,4%, 79,3%, dan 4; dan dengan NMS pasca-pelacakan (metode lengkap) menjadi 64,6%, 82,4%, 80,8%, dan 3.

Tabel 3. Penghitungan pada enam video (Tabel 5 makalah).

| | Video 1 | Video 2 | Video 3 | Video 4 | Video 5 | Video 6 |
|---|---|---|---|---|---|---|
| Hitungan manual | 22 | 7 | 22 | 11 | 13 | 19 |
| Metode usulan | 15 | 7 | 17 | 10 | 10 | 16 |

Rerata akurasi penghitungan dilaporkan 82,8%. Jumlah total manual 94 dan jumlah total sistem 75 dihitung dari tabel di atas oleh ringkasan ini; hasilnya menunjukkan penghitungan kurang pada lima dari enam video dan tepat pada video 2.

## Kelebihan dan Keterbatasan
Kelebihan yang tampak: tiga modifikasi diuji melalui ablasi bertahap, pelacak dibandingkan dengan lima metode pembanding, dan akuisisi memakai ponsel biasa dengan kecepatan tangan yang tidak seragam, sehingga mendekati praktik petani. Hitungan sistem dibandingkan dengan hitungan manual per video.

Keterbatasan yang dinyatakan penulis: kesimpulan hanya menyatakan bahwa hasil dapat dijadikan rujukan bagi pendugaan hasil nyata. Penulis tidak membahas keterbatasan secara terpisah.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Pengujian penghitungan hanya memakai enam video pendek (rata-rata sekitar 20 detik) dengan jumlah buah per video antara 7 dan 22, sehingga estimasi akurasi sangat peka terhadap satu atau dua buah. Sistem cenderung menghitung kurang (75 dibandingkan 94 secara total). Pelacak dibandingkan pada data yang sama tanpa ulangan atau uji kemaknaan, dan selisih MOTA terhadap ByteTrack hanya 1,7 poin. Aturan garis hitung bergantung pada gerakan kamera yang melintasi tanaman dan pada pengosongan bingkai awal, dan tidak ada pencocokan identitas antar-video atau antar-sisi. Hitungan acuan manual tidak dijelaskan prosedurnya, dan klaim pendugaan hasil tidak disertai konversi ke bobot atau perbandingan dengan panen.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dalam satu video yang bergerak. Mekanismenya adalah pelacakan berbasis deteksi dengan ByteTrack, kompensasi gerak kamera, dan aturan hitung satu kali per ID pada garis hitung. Tidak ada pencocokan antar-sisi atau antar-video dan tidak ada rekonstruksi 3D; identitas hanya dijaga secara berurutan dalam satu video.

Hitungan tidak dilaporkan per kelas (hanya satu kelas, yaitu anggur berkantong). Acuan hitungnya adalah hitungan manual pada video (bukan panen dan bukan anotasi citra). Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan mempertahankan kotak berkeyakinan rendah atau tertutup sampai tahap pelacakan, koreksi gerak kamera untuk rekaman tangan, dan registrasi ID untuk mencegah penghitungan ganda. Karena tandan sawit terlihat dari beberapa sisi pohon, garis hitung satu arah belum memadai tanpa mekanisme identitas lintas sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `lyu2023method`.

Lyu dkk. (2023) mengusulkan metode pendugaan hasil anggur berkantong dari video ponsel yang menggunakan YOLOv5s dengan ByteTrack yang diubah melalui NMS pasca-pelacakan, kompensasi gerak kamera, dan filter Kalman berbasis lebar kotak, serta strategi garis hitung. Pada data uji enam video, metode itu mencapai MOTA 64,6%, MOTP 82,4%, dan IDF1 80,8% (di atas ByteTrack dasar dengan selisih 1,7, 1,0, dan 4,1 poin persentase) serta rerata akurasi penghitungan 82,8% terhadap hitungan manual.

Catatan verifikasi data: Makalah berbahasa Mandarin (abstrak Inggris tersedia pada halaman akhir). Angka deteksi dibaca dari Tabel 1 dan Tabel 3, pelacakan dari Tabel 2 dan Tabel 4, dan penghitungan dari Tabel 5. Persamaan pada teks ekstraksi sebagian terpisah dari simbolnya, tetapi rumus akurasi penghitungan dan keadaan filter Kalman dapat dibaca. Rerata akurasi 82,8% sesuai dengan perhitungan dari enam pasang hitungan pada Tabel 5 (sekitar 82,9% bila dihitung oleh ringkasan ini; selisih berasal dari pembulatan). Jumlah total hitungan manual (94) dan sistem (75) dihitung oleh ringkasan ini. Kultivar anggur, ambang IoU dan keyakinan pelacak, serta jumlah anotasi tidak dilaporkan pada teks yang dibaca.
