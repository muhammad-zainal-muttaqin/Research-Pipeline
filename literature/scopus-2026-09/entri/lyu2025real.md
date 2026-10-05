# Real-time detecting and counting dual-association bagged grape clusters using EMO-YOLOv5s

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lyu2025real` |
| Judul asli | Real-time detecting and counting dual-association bagged grape clusters using EMO-YOLOv5s |
| Penulis | Lyu, J.; others |
| Tahun | 2025 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [lyu2025real.pdf](../pdf/lyu2025real.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202412150

## Gambaran Umum

Makalah ini mengusulkan metode deteksi dan pencacahan tandan anggur berkantong (*bagged grape clusters*) secara waktu-nyata dari video genggam. Metode itu terdiri dari tiga bagian: detektor EMO-YOLOv5s, pelacak dua-asosiasi berbasis BIoU dan jarak Euklides di atas ByteTrack, serta aturan hitung berupa wilayah persegi panjang. Tanaman yang diteliti adalah anggur yang dikantongi sebelum matang, dan data diambil di satu kebun di Distrik Bishan, Chongqing, Tiongkok. Makalah ditulis dalam bahasa Mandarin dengan abstrak berbahasa Inggris.

Pada tahap deteksi, penggantian *backbone* YOLOv5s dengan EMO menurunkan jumlah parameter sebesar 38,6% dan FLOPs sebesar 39,0%, dengan AP 96,5% dan kecepatan 77 frame/s. Pada tahap pelacakan, HOTA, MOTA, dan IDF1 masing-masing naik 3,6, 4,1, dan 6,0 poin persentase terhadap konfigurasi dasar (YOLOv5s dengan ByteTrack). Pada tahap pencacahan, aturan wilayah persegi panjang mencapai ACP rata-rata 93,1% dan MAE 1,3% pada enam video uji.

Pembandingan dilakukan pada data yang kecil: 700 citra untuk detektor dan enam video berdurasi sekitar 20 detik untuk pelacakan dan pencacahan. Penulis menyatakan sendiri bahwa pengujian hanya dilakukan di satu kebun dan dengan perangkat genggam.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil kebun bergantung pada pencacahan buah. Satu citra tidak dapat mencakup seluruh buah pada pohon anggur yang besar, sehingga penulis memilih pencacahan berbasis video, yaitu deteksi yang dilanjutkan dengan pelacakan. Kualitas hitungan sangat bergantung pada kualitas deteksi dan pelacakan.

Penulis menyebut tiga masalah pada pencacahan tandan anggur berkantong. Pertama, model pencacah umumnya mengutamakan akurasi sehingga besar dan lambat, padahal model perlu dijalankan di perangkat bergerak. Kedua, tandan berkantong tumbuh rapat dan saling menutupi, sedangkan kamera genggam bergetar atau bergeser. Hal itu menyebabkan pergeseran antarbingkai yang tidak linear sehingga kotak deteksi dan kotak prediksi tidak saling tumpang tindih (IoU bernilai 0) dan asosiasi gagal. Ketiga, perubahan sudut pandang mengubah latar depan dan latar belakang, sehingga daun dan tandan di dekatnya mengganggu pelacakan dan tandan hilang dari lintasan. Cara hitung yang sebelumnya dipakai penulis, yaitu garis vertikal di tengah video, menyebabkan tandan terlewat.

## Ide Utama

Penulis memperbaiki tiga tahap satu per satu. Pada deteksi, *backbone* YOLOv5s diganti EMO yang ringan. Pada asosiasi, IoU dalam ByteTrack diganti oleh gabungan BIoU (IoU dengan kotak yang diperbesar) dan jarak pusat Euklides. Pada hitungan, garis tunggal diganti oleh wilayah persegi panjang pada layar. Setiap tandan dihitung sekali berdasarkan ID lintasannya, sehingga kemampuan asosiasi antarbingkai menentukan apakah satu tandan yang tampak berkali-kali dihitung satu kali.

## Cara Kerja Langkah demi Langkah

```
  Bingkai video -> EMO-YOLOv5s -> ByteTrack dua-asosiasi -> Wilayah persegi
                   (deteksi)      (BIoU + jarak Euklides)    panjang -> hitungan
```

### 1. Akuisisi data

Data diambil di kebun percontohan di Distrik Bishan, Chongqing (106,221 BT; 29,753 LU). Anggur ditanam berbaris dengan jarak antarbaris yang hampir sama. Pada 22 Juli 2022, peneliti merekam pada pukul 08:00, 12:00, dan 18:00 (cuaca mendung) dengan ponsel genggam OPPO Reno6pro+ dan Redmi K40 dari sudut depan, atas, bawah, dan samping. Jarak horizontal 0,1 sampai 1,0 m, jarak vertikal 1,0 sampai 1,8 m, dan kecepatan gerak sekitar 1 m/s. Hasilnya adalah 500 citra asli dan enam video valid (1.920×1.080 piksel, 30 frame/s, sekitar 20 detik, kecepatan tidak seragam). Pada 1 September 2023 (berawan) ditambahkan 200 citra beresolusi 4.096×3.072 piksel. Kultivar anggur tidak dilaporkan.

Total 700 citra dibagi acak 7:2:1 menjadi 490 citra latih, 140 citra validasi, dan 70 citra uji. Enam video dipakai untuk menguji pencacahan. Penambahan data (saturasi, derau Gauss, pembalikan citra) menaikkan citra latih dari 490 menjadi 2.100 citra. Teks menyebut 2.310 citra beranotasi setelah penambahan data, tetapi tidak menjelaskan selisih 210 citra dari jumlah 2.100 tersebut. Citra dianotasi dengan Make Sense (jumlah, kelas, titik pusat, panjang, lebar), dan video dianotasi dengan Dark Label (ID, koordinat kotak, kelas tiap bingkai).

### 2. Deteksi EMO-YOLOv5s

Penulis memilih YOLOv5s sebagai dasar karena ringan dan memberi AP tertinggi di antara model pembanding (Tabel 1). EMO menggantikan *backbone* aslinya. EMO tersusun dari modul *inverted residual mobile block* (iRMB) yang menggabungkan blok residual terbalik MobileNetv2 dengan *expanded window multi-head self-attention* (EW-MHSA) dan konvolusi *depthwise separable*. Jaringan dibagi menjadi empat tahap dengan N1 sampai N4 modul iRMB. Jumlah modul per tahap tidak disebutkan dalam teks yang diekstraksi. Pelatihan memakai SGD dengan laju belajar awal 0,01, momentum 0,937, peluruhan bobot 0,0005, dan 500 epoch pada GPU NVIDIA RTX 3060.

### 3. Pelacakan dua-asosiasi

ByteTrack memisahkan kotak deteksi berkeyakinan tinggi dan rendah dan mengasosiasikan keduanya secara bertahap. Penulis mengganti IoU dengan biaya total

$$\mathrm{Cost}^{total}_{ij} = \alpha\,\mathrm{Cost}^{BIoU}_{ij} + (1-\alpha)\,\mathrm{Cost}^{Dist}_{ij}$$

dengan $\mathrm{Cost}^{BIoU}_{ij} = 1-\mathrm{BIoU}_{ij}$ dan $\mathrm{Cost}^{Dist}_{ij}$ berupa jarak Euklides antara pusat kotak deteksi dan kotak prediksi. BIoU memperbesar lebar dan tinggi kedua kotak dengan rasio penyangga $b$ pada pusat yang sama. Asosiasi dilakukan berjenjang: rasio kecil $b_1$ lebih dahulu, kemudian rasio besar $b_2$ untuk kotak yang belum cocok. Nilai terbaik hasil ablasi adalah $b_1=0{,}4$, $b_2=0{,}5$, dan $\alpha=0{,}7$. Prediksi gerak memakai filter Kalman. Penulis berargumen bahwa BIoU saja dapat menyebabkan kesalahan antartandan yang berdekatan, sedangkan jarak pusat mengurangi ketergantungan itu.

### 4. Hitungan wilayah persegi panjang

Persegi panjang ditetapkan pada layar. Tandan dihitung ketika titik pusatnya $(x_c, y_c)$ memenuhi $x_1\le x_c\le x_2$ dan $y_1\le y_c\le y_2$. ID yang sama hanya dihitung sekali, dan hitungan ditampilkan di sudut kiri atas layar. Penulis menyatakan bahwa area hitung yang lebih luas mengurangi tandan yang terlewat akibat lintasan terputus.

### 5. Metrik

Detektor dinilai dengan AP, jumlah parameter, FLOPs, dan FPS. Pelacak dinilai dengan HOTA, MOTA, IDF1, dan IDS (jumlah pergantian ID). Pencacahan dinilai dengan ACP dan MAE: $\mathrm{ACP}=\frac{1}{n}\sum\left(1-\frac{|S-G|}{G}\right)\times100\%$ dan $\mathrm{MAE}=\frac{1}{n}\sum|S-G|\times100\%$, dengan $S$ hitungan metode, $G$ hitungan sebenarnya, dan $n$ jumlah video.

## Eksperimen dan Hasil

Detektor dibandingkan dengan lima varian YOLO lain pada data uji kebun tersebut (Tabel 1). Pelacak dibandingkan dengan SORT, DeepSORT, ByteTrack, SMILEtrack, dan C-BIoU Tracker (Tabel 2). Cara hitung dibandingkan dengan hitungan berdasarkan ID dan hitungan garis tabrak pada enam video (Tabel 5). Hitungan sebenarnya berasal dari anotasi video.

**Tabel 1. Deteksi (Tabel 1 makalah)**

| Model | Parameter | FLOPs (G) | FPS | AP (%) |
|---|---|---|---|---|
| YOLOv5s | 7,0×10^6 | 15,9 | 57 | 95,7 |
| YOLOv7-tiny | 6,0×10^6 | 13,0 | 64 | 95,4 |
| YOLOv8s | 11,1×10^6 | 28,4 | 20 | 95,3 |
| YOLOv9-tiny | 2,6×10^6 | 10,7 | 65 | 95,4 |
| YOLOv10 | 8,0×10^6 | 24,4 | 19 | 95,0 |
| YOLOv11s | 9,4×10^6 | 21,3 | 72 | 94,9 |
| EMO-YOLOv5s | 4,3×10^6 | 9,7 | 77 | 96,5 |

**Tabel 2. Pelacakan (Tabel 2 makalah)**

| Pelacak | HOTA (%) | MOTA (%) | IDF1 (%) | IDS |
|---|---|---|---|---|
| SORT | 52,9 | 53,9 | 67,3 | 17 |
| DeepSORT | 50,8 | 50,2 | 67,4 | 16 |
| ByteTrack | 53,7 | 53,8 | 70,4 | 5 |
| SMILEtrack | 49,2 | 47,8 | 67,5 | 16 |
| C-BIoU Tracker | 48,6 | 55,6 | 62,9 | 10 |
| BIoU + jarak Euklides | 58,6 | 64,7 | 80,0 | 2 |

Terhadap ByteTrack, kenaikan HOTA, MOTA, dan IDF1 adalah 4,9, 10,9, dan 9,6 poin persentase, dan IDS turun 3 kali (angka ini dinyatakan di Subbab 3.2.1). Penulis menjelaskan bahwa SORT dan C-BIoU Tracker mengabaikan kotak berkeyakinan rendah, sedangkan DeepSORT dan SMILEtrack memakai fitur tampilan yang kurang berguna karena tandan berkantong tampak sangat mirip.

**Tabel 3. Ablasi pelacakan (Tabel 3 makalah)**

| EMO | BIoU | Jarak Euklides | HOTA (%) | MOTA (%) | IDF1 (%) | IDS |
|---|---|---|---|---|---|---|
| tidak | tidak | tidak | 55,0 | 60,6 | 74,0 | 3 |
| ya | tidak | tidak | 57,3 | 64,2 | 77,6 | 4 |
| ya | ya | tidak | 57,9 | 64,3 | 79,2 | 3 |
| ya | tidak | ya | 58,4 | 64,3 | 79,7 | 2 |
| ya | ya | ya | 58,6 | 64,7 | 80,0 | 2 |

Konfigurasi dasar pada ablasi (55,0; 60,6; 74,0; IDS 3) berbeda dari baris ByteTrack pada Tabel 2 (53,7; 53,8; 70,4; IDS 5), dan makalah tidak menjelaskan perbedaan tersebut. Kenaikan 3,6, 4,1, dan 6,0 poin yang dinyatakan pada abstrak sesuai dengan selisih terhadap konfigurasi dasar ablasi (58,6 − 55,0; 64,7 − 60,6; 80,0 − 74,0). Teks Subbab 3.2.2 menyebut IDS turun 1 kali, yaitu dari 3 menjadi 2.

Ablasi $\alpha$ (Tabel 4 makalah, HOTA/MOTA/IDF1/IDS): 0,5 memberi 58,4/63,6/76,0/4; 0,6 memberi 58,4/64,0/79,7/1; 0,7 memberi 58,4/64,3/79,7/2; 0,8 memberi 58,2/64,1/79,4/3; 0,9 memberi 57,1/64,3/77,2/7. Penulis memilih 0,7 meskipun $\alpha=0{,}6$ memiliki IDS lebih kecil. Ablasi $b_1$ dan $b_2$ disajikan pada Gambar 8, dan angka per sel gambar tidak terbaca utuh pada teks ekstraksi.

**Tabel 5. Hitungan per video (Tabel 5 makalah)**

| Metode | V1 | V2 | V3 | V4 | V5 | V6 | ACP (%) | MAE (%) |
|---|---|---|---|---|---|---|---|---|
| Hitungan sebenarnya | 22 | 7 | 22 | 11 | 13 | 19 | - | - |
| Hitungan ID | 23 | 8 | 24 | 10 | 15 | 27 | 84,2 | 2,5 |
| Garis tabrak | 16 | 7 | 16 | 10 | 11 | 17 | 85,1 | 2,8 |
| Wilayah persegi panjang | 20 | 7 | 18 | 10 | 13 | 18 | 93,1 | 1,3 |

Wilayah persegi panjang memperbaiki ACP sebesar 8,9 poin terhadap hitungan ID dan 8,0 poin terhadap garis tabrak. MAE turun 1,2 dan 1,5 poin. Jumlah sebenarnya seluruh video, bila dijumlahkan dari baris pertama, adalah 94 tandan (dihitung ringkasan ini), dan jumlah dari wilayah persegi panjang adalah 86. Hitungan ID cenderung berlebih akibat pergantian ID, sedangkan hitungan garis tabrak cenderung kurang akibat lintasan terputus.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: model lebih ringan dan lebih cepat daripada YOLOv5s sambil menaikkan AP; asosiasi lebih tahan terhadap getaran kamera dan kepadatan tandan; dan hitungan wilayah persegi panjang mengurangi tandan yang terlewat dan hitungan ganda. Ablasi disajikan untuk tiap komponen.

Keterbatasan yang dinyatakan penulis: EMO hanya menggantikan *backbone* tanpa optimasi parameter berlebih lain; rasio penyangga BIoU yang tetap dapat menimbulkan salah asosiasi bila kecepatan kamera berubah terus-menerus; pelacak masih dapat kehilangan target atau berganti ID pada oklusi panjang; pengujian hanya di satu kebun anggur; dan semua data diambil dengan perangkat genggam.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Pertama, evaluasi pencacahan hanya memakai enam video pendek dengan hitungan 7 sampai 22 tandan per video, sehingga ACP dan MAE rentan terhadap variasi kecil. Kedua, hitungan wilayah persegi panjang dikalibrasi pada layar tunggal dan tidak menyelesaikan identitas tandan antara video atau antarsisi pohon yang berbeda. Ketiga, ada satu kelas objek saja (tandan berkantong), sehingga tidak ada pencacahan per kelas. Keempat, konfigurasi dasar ablasi berbeda dari baris ByteTrack pada Tabel 2 tanpa penjelasan. Kelima, parameter $b_1$, $b_2$, dan $\alpha$ dipilih pada video yang sama dengan evaluasi, sehingga hasil terbaik dapat terlalu optimistis. Teks tidak menyebutkan pemisahan video untuk penyetelan.

## Kaitan dengan Tinjauan main6

Makalah ini menangani tandan yang tampak pada banyak bingkai video dengan mekanisme pelacakan: ByteTrack yang dimodifikasi menjaga ID tiap tandan antarbingkai, dan hitungan dilakukan sekali per ID. Identitas tidak dikaitkan melalui pencocokan antarsisi atau rekonstruksi 3D, melainkan melalui kontinuitas gerak dan tumpang tindih kotak dalam satu rekaman yang kontinu. Hitungan hanya melaporkan satu kelas, jadi tidak ada hitungan per kelas. Acuan hitungan adalah anotasi video (jumlah tandan unik pada tiap video), bukan hasil panen atau hitung manual di lapangan, sebagaimana tampak pada baris "Hitungan sebenarnya".

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan asosiasi dengan kotak yang diperbesar dan jarak pusat untuk menangani pergeseran antarbingkai; pemisahan kotak berkeyakinan tinggi dan rendah untuk menangani oklusi; serta fakta bahwa hitungan berbasis ID sangat sensitif terhadap pergantian ID (hitungan ID memberi ACP 84,2% dibandingkan 93,1% untuk aturan wilayah). Batasan pemindahan: metode bergantung pada kontinuitas video dari satu gerakan kamera dan tidak menangani buah yang sama pada sisi pohon yang tidak berurutan. Selain itu, makalah tidak menyajikan atribut kelas seperti tingkat kematangan.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `lyu2025real`.

Ringkasan yang aman dikutip: Lyu dan Zhang (2025) mengusulkan pencacahan tandan anggur berkantong waktu-nyata dari video genggam dengan detektor EMO-YOLOv5s, pelacak dua-asosiasi berbasis BIoU dan jarak Euklides di atas ByteTrack, dan aturan hitung berupa wilayah persegi panjang. Pada enam video dari satu kebun, hitungan wilayah persegi panjang mencapai ACP rata-rata 93,1% dan MAE 1,3%, dibandingkan 84,2% dan 2,5% untuk hitungan berdasarkan ID, dengan acuan berupa anotasi video.

Catatan verifikasi data: Makalah ini berbahasa Mandarin dan diringkas dari bahasa aslinya, dengan abstrak dan judul tabel dalam bahasa Inggris. Angka deteksi (96,5% AP; 77 frame/s; penurunan 38,6% dan 39,0%) ada pada abstrak, Subbab 3.1.1, dan Tabel 1. Angka pelacakan ada pada Tabel 2 sampai Tabel 4 dan Subbab 3.2. Angka hitungan (ACP 93,1% dan MAE 1,3%) ada pada Tabel 5 dan Subbab 3.3.1. Jumlah citra (700; 490, 140, 70; 2.100 setelah penambahan data) tertulis pada Subbab 1.1 dan 1.2, sedangkan angka 2.310 pada Subbab 1.3 tidak dapat dicocokkan dengan 2.100. Angka tabel pada teks ekstraksi terbaca per sel sehingga urutan kolom disimpulkan dari header, dan nilai pada Gambar 8 tidak terbaca utuh. Jumlah modul iRMB per tahap, kultivar anggur, dan hasil di luar kebun tersebut tidak dilaporkan. Total 94 dan 86 tandan dihitung dari baris Tabel 5, bukan dilaporkan penulis.
