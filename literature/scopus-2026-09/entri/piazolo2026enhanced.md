# Enhanced grape tracking (using deep neural networks) with an extended matching algorithm for SORT and DeepSORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `piazolo2026enhanced` |
| Judul asli | Enhanced grape tracking (using deep neural networks) with an extended matching algorithm for SORT and DeepSORT |
| Penulis | Piazolo, Jacob; Fischer, Benedikt; Gruna, Robin; Beyerer, J\"urgen |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [piazolo2026enhanced.pdf](../pdf/piazolo2026enhanced.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111529

## Gambaran Umum
Makalah ini membandingkan lima algoritma pelacakan multi-objek (*multi-object tracking*, MOT) untuk melacak dan menghitung tandan anggur dari video pesawat nirawak (*unmanned aerial vehicle*, UAV) di kebun anggur: SORT, DeepSORT, ByteTrack, serta dua algoritma baru yang diusulkan penulis, SORT+ dan DeepSORT+. Kedua algoritma baru memperluas tahap pencocokan (*matching cascade*) dengan menggabungkan jarak IoU, jarak Mahalanobis, dan jarak Euklides. Dengan cara itu SORT+ tidak memerlukan jaringan identifikasi ulang (*re-identification*, Re-ID) maupun data latih berlabel ID instans.

Data yang dipakai adalah dataset video UAV RGB tandan anggur (*Vitis vinifera*, empat baris, tahap awal pematangan) dari Sentís dkk. (2021). Seluruh pelacak memakai detektor Mask R-CNN yang sama. Detektor hanya mencapai mAP kotak pembatas 19,4 % dan mAP segmentasi 14,5 %, tetapi pelacakan tetap berjalan karena deteksi parsial sudah cukup untuk mempertahankan identitas.

Hasil utama: DeepSORT+ memperoleh MOTA 42,71 % dan IDF1 67,10 % dengan 14,90 pertukaran identitas; SORT+ menurunkan pertukaran identitas SORT dari 73,50 menjadi 28,24 dan menaikkan akurasi hitungan dari 32,7 % menjadi 96,8 % terhadap hitungan manual 186 tandan yang terlihat. Penulis menegaskan bahwa selang kepercayaan 95 % hasil *bootstrap* saling tumpang tindih sehingga pelacak terbaik tidak dapat dipastikan pada data serupa lain.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengelola kebun anggur menghitung tandan secara manual untuk estimasi hasil, pekerjaan yang lama, padat karya, dan rawan galat manusia. Tantangan penghitungan otomatis adalah mendeteksi setiap tandan unik dalam urutan video tanpa terlewat dan tanpa hitungan ganda. Dua pendekatan yang disebut penulis adalah penjahitan citra (*image stitching*) menjadi panorama dan pelacakan objek; penjahitan dinilai dapat menghilangkan tandan saat pembuatan panorama dan lebih rentan terhadap positif palsu, sehingga makalah berfokus pada pelacakan.

Pelacak mutakhir seperti DeepSORT dan StrongSORT bergantung pada jaringan Re-ID yang menuntut anotasi ID instans, yang menurut penulis sangat memakan tenaga dan rawan galat di pertanian dibandingkan anotasi kotak pembatas biasa. SORT asli hanya memakai tumpang tindih IoU, yang tidak memadai bila deteksi bersifat parsial atau terpecah akibat oklusi dedaunan. Penulis juga mencatat bahwa hanya dua dataset anggur yang memiliki ID instans (UAV RGB Video dan Lazio), dan bahwa penelitian pelacakan anggur sebelum 2023 sebagian besar berupa bukti konsep tanpa evaluasi pelacakan.

## Ide Utama
Gagasan utama adalah menyusun pencocokan sebagai kaskade bertahap yang memakai ukuran kemiripan geometris yang saling melengkapi: IoU yang ketat untuk pasangan yang jelas tumpang tindih, jarak Mahalanobis terhadap distribusi prediksi filter Kalman, IoU yang dilonggarkan, dan jarak Euklides antarpusat kotak untuk memulihkan deteksi parsial tanpa tumpang tindih. Ukuran-ukuran ini ringan secara komputasi dan tidak memerlukan data tambahan.

DeepSORT+ menambahkan tahap awal berbasis fitur penampilan dari jaringan klasifikasi (ResNet-50), lalu menjalankan empat tahap geometris yang sama seperti SORT+. Penulis mengklaim kaskade ini meningkatkan SORT secara besar dan DeepSORT secara tipis tanpa mengubah kompleksitas asimtotik algoritma.

## Cara Kerja Langkah demi Langkah

```
 Video UAV --> Mask R-CNN (deteksi) --> prediksi Kalman per jejak
                                              |
   (DeepSORT+: Tahap 0, fitur penampilan)     v
   Tahap 1: IoU ketat (IoU > 20 %)
   Tahap 2: Mahalanobis (< kuantil chi-kuadrat 0,9)
   Tahap 3: IoU longgar (IoU > 3,5 %)
   Tahap 4: Euklides pusat kotak (ambang dinamis)
                                              |
                       jejak terkonfirmasi setelah 5 bingkai --> hitungan
```

### 1. Data
Dataset UAV RGB Video (Sentís dkk., 2021) dibagi menjadi 528 citra latih dan 136 citra uji dari urutan video berbeda; setiap urutan berisi 250 sampai 2000 bingkai dan rata-rata sekitar 22 bingkai dianotasi. Resolusi citra tinggi adalah 2160 x 4096 piksel. Barisan uji: 4.2.1, 6.1.1, 6.1.2, 7.1.1, 7.1.2, dan 8.1. Penulis menyebut tiga masalah dataset: tandan sangat kecil (0,01 % sampai 0,17 % luas bingkai), sebagian tandan tidak dianotasi, dan tandan pada baris latar belakang terdeteksi sebagai positif palsu serta menggembungkan hitungan. Subset uji berisi 147 tandan beranotasi; hitungan manual dari video menemukan sedikitnya 150 tandan latar depan dan 36 latar belakang, total sedikitnya 186 tandan terlihat.

### 2. Detektor Mask R-CNN
Mask R-CNN dilatih pada 528 citra dengan optimizer Adam (laju belajar 0,000105). Karena fokus penelitian adalah pelacak, checkpoint dipilih dari epoch dengan kinerja terbaik pada set uji tanpa set validasi terpisah, agar semua pelacak mendapat masukan terbaik. Mask R-CNN dipilih karena menghasilkan luas tandan, yang menurut penulis berkorelasi lebih kuat dengan hasil panen dibanding jumlah buah.

### 3. Pelacak pembanding
SORT memakai filter Kalman dan algoritma Hungarian; jejak tak cocok diprediksi hingga 50 bingkai, dan jejak tentatif dikonfirmasi setelah lima bingkai. DeepSORT menambahkan jarak Mahalanobis (menyaring kecocokan di bawah probabilitas 0,5 %) dan fitur penampilan dari jaringan klasifikasi. ByteTrack memulihkan deteksi berkeyakinan rendah pada tahap pencocokan kedua.

### 4. Kaskade pencocokan yang diusulkan
Pada tiap tahap $k$, penugasan diselesaikan dengan algoritma Hungarian pada matriks biaya yang diberi ambang gerbang $\tau_k$ (biaya tak hingga bila melebihi ambang). SORT+ memakai empat tahap: (1) IoU ketat dengan tumpang tindih lebih dari 20 % ($d_{IoU} \le 0{,}8$); (2) Mahalanobis dengan ambang $\chi^2_{0{,}9;2} = 4{,}605$; (3) IoU longgar dengan tumpang tindih minimum 3,5 % ($d_{IoU} \le 0{,}965$); (4) jarak Euklides pusat kotak dengan ambang dinamis $\tau_4 = (w_i + h_i)/2$ untuk memulihkan deteksi parsial tanpa tumpang tindih. DeepSORT+ menambahkan Tahap 0 dengan syarat jarak Mahalanobis kurang dari $\chi^2_{0{,}995;2} = 10{,}597$ dan jarak Euklides antarvektor fitur kurang dari $\tau_0 = 1{,}5$.

### 5. Metrik
Deteksi dinilai dengan mAP COCO. Pelacakan dinilai dengan IDsw, MOTA, MOTP, IDF1, dan akurasi hitungan $1 - |AG - CT|/AG$, dengan ambang kecocokan IoU 20 % untuk evaluasi. Statistik pelacakan diperoleh dengan *bootstrap*: 1.000 resampel dengan pengembalian dari 6 urutan video uji, dilaporkan sebagai rerata dan selang kepercayaan 95 %. Akurasi hitungan memakai hitungan manual 186 tandan sebagai acuan, bukan jumlah anotasi.

## Eksperimen dan Hasil
Detektor Mask R-CNN mencapai mAP kotak 19,4 % (mAP50 44,8 %, mAP75 14,1 %, mAPs 5,5 %, mAPm 19,2 %, mAPl 28,0 %) dan mAP segmentasi 14,5 % (mAP50 44,3 %, mAP75 4,5 %). Jaringan klasifikasi ResNet-50 untuk fitur penampilan mencapai mAP 80,6 % (Adam, laju belajar 0,000105, *weight decay* 0,0001). Hasil pelacakan pada set uji (Tabel 5 makalah, rerata bootstrap dan selang kepercayaan 95 %):

| Pelacak | MOTA | IDF1 | IDsw | MOTP |
|---|---|---|---|---|
| SORT | 37,69 % ± 0,33 % | 60,42 % ± 0,09 % | 73,50 ± 1,20 | 65,41 % ± 0,08 % |
| DeepSORT | 42,25 % ± 0,37 % | 66,93 % ± 0,21 % | 17,05 ± 0,29 | 65,46 % ± 0,07 % |
| ByteTrack | 41,53 % ± 0,37 % | 66,01 % ± 0,19 % | 26,09 ± 0,33 | 65,44 % ± 0,08 % |
| SORT+ | 41,50 % ± 0,40 % | 66,48 % ± 0,18 % | 28,24 ± 0,49 | 65,40 % ± 0,07 % |
| DeepSORT+ | 42,71 % ± 0,37 % | 67,10 % ± 0,19 % | 14,90 ± 0,23 | 65,39 % ± 0,08 % |

Hitungan jejak terkonfirmasi dan akurasi hitungan terhadap 186 tandan terlihat (Tabel 6 makalah; anotasi 147, hitungan manual latar depan 150 dan latar belakang 36):

| Pelacak | Hitungan | Akurasi hitungan |
|---|---|---|
| SORT | 313 | 32,7 % |
| DeepSORT | 195 | 95,2 % |
| ByteTrack | 238 | 72,0 % |
| SORT+ | 192 | 96,8 % |
| DeepSORT+ | 186 | 100 % |

Pelacak cenderung menghitung berlebih hingga 68 %, sedangkan DeepSORT, SORT+, dan DeepSORT+ berlebih paling banyak 5 %. Penulis menduga ini disebabkan oleh pemakaian jarak Mahalanobis sebagai satu-satunya ukuran kemiripan yang sama pada ketiganya. SORT mengalami pertukaran identitas lebih dari dua kali lipat SORT+ dan ByteTrack serta lebih dari empat kali lipat DeepSORT dan DeepSORT+. SORT+ dan ByteTrack kehilangan sekitar 1 % MOTA dan IDF1 dibanding DeepSORT(+) dengan sekitar sepuluh pertukaran identitas lebih banyak. Karena selang kepercayaan MOTA dan IDF1 DeepSORT dan DeepSORT+ saling tumpang tindih, penulis menyatakan urutan terbaik pada data serupa tidak konklusif.

Perbandingan dengan penelitian lain yang dilaporkan makalah: PointTrack pada dataset yang sama (Ariza-Sentís dkk., 2023) memperoleh MOTSA -8,2 % dan MOTSP 66,6 %, namun penulis menyatakan data uji penelitian tersebut tidak diketahui sehingga perbandingan terbatas. Ciarfuglia dkk. (2023) pada WGISD memperoleh MOTA hingga 46,7 % dan MOTP hingga 72,9 % dengan mAP detektor 53,4 %. Saraceni dkk. (2024) pada dataset Lazio memperoleh MOTA hingga 66,1 % dan IDF1 hingga 73,7 % dengan AgriSORT, sedangkan SORT mencapai MOTA hingga 62,7 %.

## Kelebihan dan Keterbatasan
Kelebihan: SORT+ meningkatkan SORT secara besar tanpa jaringan Re-ID dan tanpa anotasi ID instans; semua pelacak diuji dengan detektor yang sama; hasil dilaporkan dengan *bootstrap* dan selang kepercayaan; hitungan dibandingkan terhadap hitungan manual tandan yang terlihat, bukan terhadap anotasi yang tidak lengkap; kode dan konfigurasi dinyatakan tersedia di GitHub.

Keterbatasan yang dinyatakan penulis: akurasi 100 % DeepSORT+ pada satu subset tidak boleh digeneralisasi karena margin galatnya tidak diketahui; estimasi hasil panen (bobot) tidak dapat dievaluasi karena dataset tidak memuat bobot buah; dataset hanya satu kultivar pada tahap awal pematangan sehingga kinerja pada dataset lain diperkirakan lebih rendah; dataset memiliki tandan sangat kecil, anotasi yang hilang, dan tandan latar belakang; Mask R-CNN dirancang untuk resolusi hingga 1280 x 720 piksel sehingga kurang cocok untuk citra beresolusi tinggi; detektor dipilih berdasarkan hasil pada set uji tanpa set validasi terpisah.

Menurut pembacaan ringkasan ini, set uji hanya terdiri atas 6 urutan video dan 147 tandan beranotasi (sedikitnya 186 terlihat), sehingga bukti statistik terbatas, dan *bootstrap* atas 6 urutan tidak menggantikan pengujian pada data independen. Menurut pembacaan ringkasan ini, pemilihan checkpoint detektor pada set uji dapat memberi keuntungan optimistis bagi seluruh pelacak. Menurut pembacaan ringkasan ini, akurasi hitungan SORT+ dapat mencerminkan galat yang saling meniadakan: penulis sendiri menduga jejak yang hilang dipulihkan oleh pertukaran identitas berikutnya, dan hitungan manual 186 adalah batas bawah ("sedikitnya"). Menurut pembacaan ringkasan ini, pernyataan abstrak bahwa MOTA dan IDF1 naik 5 % sampai 6 % tidak cocok dengan Tabel 5 bila dibaca sebagai selisih poin (MOTA 37,69 menjadi 41,50; IDF1 60,42 menjadi 66,48).

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan MOT (*tracking-by-detection*): filter Kalman memprediksi posisi, algoritma Hungarian menugaskan deteksi ke jejak, dan hitungan adalah jumlah jejak terkonfirmasi (jejak tentatif dikonfirmasi setelah lima bingkai). Identitas dijaga dalam satu video dari satu pandang yang bergerak (UAV), bukan lintas sisi atau lintas pohon, dan tidak ada pencocokan lintas pandang terpisah atau rekonstruksi 3D. Hitungan tidak dilaporkan per kelas; satu kelas (tandan anggur) yang dihitung. Acuan hitungan adalah hitungan manual tandan terlihat pada video (186), bukan hasil panen; estimasi hasil panen tidak dievaluasi.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan kaskade pencocokan geometris tanpa Re-ID untuk kasus ketika anotasi ID instans tidak tersedia, penggunaan ukuran jarak yang tidak bergantung pada tumpang tindih saat deteksi parsial, dan peringatan bahwa hitungan bisa terlihat akurat karena galat yang saling meniadakan sehingga akurasi hitungan perlu dibaca bersama IDsw. Mekanisme ini bekerja pada urutan bingkai berurutan dengan gerak kamera yang halus sehingga tidak langsung berlaku untuk citra diskret dari sisi pohon berbeda.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `piazolo2026enhanced`.

Ringkasan yang aman dikutip: Piazolo dkk. (2026) mengusulkan SORT+ dan DeepSORT+, yaitu perluasan kaskade pencocokan SORT dan DeepSORT dengan jarak IoU, Mahalanobis, dan Euklides, dan mengevaluasinya bersama SORT, DeepSORT, dan ByteTrack pada video UAV tandan anggur dengan detektor Mask R-CNN (mAP kotak 19,4 %). SORT+ menurunkan pertukaran identitas SORT dari 73,50 menjadi 28,24 dan menaikkan akurasi hitungan dari 32,7 % menjadi 96,8 % terhadap hitungan manual sedikitnya 186 tandan terlihat tanpa memerlukan jaringan Re-ID; DeepSORT+ memperoleh MOTA 42,71 %, IDF1 67,10 %, dan akurasi hitungan 100 %, tetapi selang kepercayaan DeepSORT dan DeepSORT+ saling tumpang tindih.

Catatan verifikasi data: Hasil deteksi tercantum pada Tabel 3 dan Tabel 4 (seksi 3.1), mAP jaringan klasifikasi pada seksi 3.2, hasil pelacakan pada Tabel 5 (seksi 4), dan hitungan serta akurasi hitungan pada Tabel 6 (seksi 5.1). Jumlah citra latih dan uji (528 dan 136) berada pada seksi 2.1. Teks ekstraksi tidak rusak berarti, tetapi gambar (Gambar 9 sampai 11) tidak dapat diperiksa dari teks. Angka "pertukaran identitas 15 dari 186 jejak" dan "17 dari 195 jejak" dikutip dari seksi 5.1; angka IDsw pada tabel adalah rerata bootstrap sehingga berupa pecahan. Abstrak menyatakan SORT+ menaikkan MOTA dan IDF1 sebesar 5 % sampai 6 % dan menurunkan pertukaran identitas 62 %; penurunan 62 % sesuai dengan selisih Tabel 5 (73,50 ke 28,24, kira-kira 61,6 %, dihitung), sedangkan 5 % sampai 6 % tidak dapat direproduksi sebagai selisih poin dari tabel. Tidak dilaporkan: bobot hasil panen, jumlah pohon atau baris untuk subset uji secara rinci selain daftar baris, dan waktu pemrosesan per bingkai (hanya argumen kompleksitas kualitatif).
