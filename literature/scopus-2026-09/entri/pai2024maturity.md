# Maturity and Yield Estimation of Tomatoes Using RGB and Multispectral Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pai2024maturity` |
| Judul asli | Maturity and Yield Estimation of Tomatoes Using RGB and Multispectral Images |
| Penulis | Pai, Chu-An; Lin, Huei-Yung |
| Tahun | 2024 |
| Venue | Proceedings of the IEEE International Conference on Industrial Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [pai2024maturity.pdf](../pdf/pai2024maturity.pdf)
- DOI resmi: https://doi.org/10.1109/icit58233.2024.10540838

## Gambaran Umum
Makalah konferensi ICIT 2024 ini mengusulkan sistem untuk mengestimasi kematangan dan hasil panen tomat ceri dari citra RGB dan multispektral. Sistem mendeteksi tomat dengan YOLOv8 yang dipadukan dengan OSNet, memberi setiap tomat satu ID melalui jaringan pelacakan (StrongSORT atau ByteTrack), mengklasifikasikan tingkat kematangan memakai nilai R, G, B dan indeks multispektral (NDVI, GNDVI, GRRI) dengan SVM, KNN, atau jaringan saraf tiruan (*artificial neural network*, ANN), lalu menghitung jumlah tomat pada tiap tingkat kematangan.

Data dikumpulkan di ladang tomat dengan kamera Parrot Sequoia+ pada tiga set data (19th tomato, lin tomato, 19th2 tomato) dengan gerakan kamera lateral di sepanjang rak tomat. Akurasi klasifikasi kematangan berkisar antara 38% dan 81% bergantung pada set data, algoritme, dan kombinasi fitur; RGB sering setara atau lebih baik daripada indeks multispektral. StrongSORT dipilih sebagai pelacak karena MOTA dan jumlah pergantian ID (IDs) lebih baik pada sebagian besar sekuens. Pada Tabel VI, selisih total jumlah tomat prediksi terhadap acuan berkisar dari −22 sampai +1 per sekuens uji.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Naiknya upah minimum dan kelangkaan pekerja musiman membuat petani perlu menjadwalkan panen sesuai jumlah dan bobot hasil yang diperkirakan. Untuk itu, kematangan dan hasil perlu diestimasi secara berkala. Penelitian terdahulu yang dirangkum penulis mengevaluasi kematangan buah dengan panjang gelombang pantulan (stroberi, blueberry), CNN (DenseNet, ResNet, Inception V3), atau indeks klorofil dan banyak indeks multispektral untuk prediksi hasil.

Makalah ini berfokus pada tomat ceri: mengidentifikasi tiap tomat, melacaknya sepanjang urutan citra, mengklasifikasikan kematangannya, dan menyajikan jumlah per kategori kematangan sebagai masukan alokasi tenaga kerja panen.

## Ide Utama
Pelacakan multi-objek memberi identitas tetap pada tiap tomat sehingga satu tomat yang muncul di banyak bingkai dihitung satu kali. Klasifikasi kematangan dilakukan pada tiap kotak per bingkai, lalu hasil per tomat ditetapkan melalui pemungutan suara mayoritas (*voting*) atas semua bingkai tomat yang sama. Hasil pelacakan dan klasifikasi digabung sehingga jumlah tomat per kelas kematangan dapat dilaporkan. Penulis juga membandingkan fitur RGB dengan indeks multispektral untuk menguji apakah multispektral benar-benar diperlukan.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data dan pelabelan kematangan
Data diambil dengan Parrot Sequoia+ (sensor multispektral dengan lima kamera: RGB, NIR, merah, hijau, dan *red-edge*, ditambah sensor cahaya matahari untuk kalibrasi). Tiga set data dikumpulkan sepanjang musim panen dengan pergerakan kamera lateral di sepanjang rak. Urutan citra diubah ke format IRIS dan format MOT untuk urutan uji. Nilai warna dan indeks per tomat dihitung dengan merata-ratakan intensitas piksel pada bagian kotak yang tidak tertutup masker.

Label kematangan ditentukan mingguan dengan membandingkan data lokasi yang sama pada minggu berbeda. Tomat yang hijau pada minggu ke-$n$, merah pada minggu ke-$(n+1)$, dan dipanen pada minggu ke-$(n+2)$ diberi label −2 pada minggu ke-$n$ dan −1 pada minggu ke-$(n+1)$. Tomat yang lebih dari tiga minggu dari matang diberi label −3. Jadi −1, −2, dan −3 masing-masing berarti siap panen (*mature*), satu minggu lagi (*almost mature*), dan dua minggu atau lebih (*immature*). Set data ketiga dikumpulkan dua kali seminggu karena warna berubah drastis pada sekitar satu setengah minggu terakhir sebelum matang.

### 2. Penyelarasan citra multispektral
Indeks dihitung dari citra NIR, merah, hijau, dan *red-edge* setelah empat langkah: penghilangan distorsi lensa, *warping* untuk menyelaraskan posisi, penyelarasan untuk tiap indeks, dan penerapan rumus indeks yang menghasilkan citra TIFF.

### 3. Indeks klasifikasi
NDVI $= (\text{NIR} - \text{RED})/(\text{NIR} + \text{RED})$, GNDVI $= (\text{NIR} - \text{GRE})/(\text{NIR} + \text{GRE})$, dan GRRI $= \text{RED}/\text{GRE}$.

### 4. Algoritme klasifikasi
SVM (kernel RBF, $C$ dari 10 sampai 40 dengan langkah 2), KNN ($K$ dari 2 sampai 30 dengan langkah 2), dan ANN (300 epoch, ukuran *batch* 40). Semua memakai validasi silang 10-lipat untuk memilih parameter. Fitur: R, G, B, NDVI, GNDVI, dan GRRI. Dimensi ruang klasifikasi mengikuti jumlah indikator yang dipakai. Pemungutan suara mayoritas atas bingkai-bingkai satu tomat menentukan kelas akhir.

### 5. Deteksi, pelacakan, dan segmentasi
Deteksi memakai YOLOv8 yang digabung dengan OSNet (jaringan awalnya untuk identifikasi ulang orang). Pelacak: StrongSORT (peningkatan DeepSORT dengan AFLink untuk menyambung lintasan pendek) dan ByteTrack (mempertahankan kotak berskor rendah dan menautkannya dengan filter Kalman); yang lebih baik dipilih untuk analisis akhir. Untuk mengurangi pengaruh ranting dan buah tetangga, kotak segmentasi diubah menjadi elips setelah konversi ruang warna YUV dan ambang Otsu pada kanal V.

## Eksperimen dan Hasil
Jumlah kotak tomat pada pelatihan dan pengujian klasifikasi (Tabel II): 19th tomato 4.247 dan 1.775; lin tomato 4.554 dan 2.423; 19th2 tomato 8.720 dan 4.338. Pada eksperimen klasifikasi, kotak berasal dari acuan (tanpa pelacakan). Akurasi didefinisikan sebagai jumlah kotak yang diklasifikasikan benar setelah *voting* dibagi seluruh kotak pada semua bingkai.

Akurasi klasifikasi (Tabel III), tiga kelas kematangan:

| Set data | Algoritme | R,G,B | GNDVI, NDVI, GRRI | R,G,B + ketiga indeks |
|---|---|---|---|---|
| 19th tomato | SVM | 63% | 70% | 63% |
| 19th tomato | KNN | 64% | 66% | 64% |
| 19th tomato | ANN | 62% | 73% | 73% |
| lin tomato | SVM | 64% | 55% | 65% |
| lin tomato | KNN | 58% | 58% | 58% |
| lin tomato | ANN | 38% | 75% | 46% |
| 19th2 tomato | SVM | 72% | 70% | 78% |
| 19th2 tomato | KNN | 81% | 59% | 81% |
| 19th2 tomato | ANN | 72% | 58% | 73% |

Penulis melaporkan bahwa pada dua set data selain 19th tomato, RGB lebih baik daripada indeks multispektral, dan analisis kontribusi indikator (Gambar 2) menunjukkan cahaya hijau memberi kontribusi tertinggi. Pada Tabel IV, penggunaan hanya kanal merah dan biru (R+B) menurunkan akurasi, misalnya SVM pada lin tomato dari 64% menjadi 44%, dan KNN pada 19th2 tomato dari 81% menjadi 64%. Matriks konfusi (Gambar 3) menunjukkan pemisahan −1 dan −2 lebih baik daripada −2 dan −3, karena warna kulit tomat hampir tidak berubah sampai sekitar satu setengah minggu sebelum matang. Nilai pada gambar tidak dapat dibaca dari teks.

Pelacakan (Tabel V) pada sekuens uji: StrongSORT unggul pada MOTA dan IDs di sebagian besar sekuens. Contoh: 19th tomato (7th) StrongSORT MOTA 59,80%, IDs 1, dibandingkan ByteTrack 54,00%, IDs 8; lin tomato (4th) StrongSORT MOTA 7,60% dan ByteTrack 4,40%. Pada 19th2 tomato (9th), ByteTrack MOTA 76,10% sedikit melampaui StrongSORT 75,80%, dan pada lin tomato (6th) ByteTrack 24,00% melampaui StrongSORT 23,30%. Jumlah FN besar pada beberapa sekuens (misalnya 1.394 FN pada lin tomato 4th).

Hasil gabungan (Tabel VI), sebagian baris, dengan urutan kelas −3/−2/−1/total:

| Sekuens | Acuan | Prediksi | Selisih total | RMSE |
|---|---|---|---|---|
| 19th2 tomato (5th), sekali seminggu | 19/17/1/37 | 19/7/1/27 | −10 | 5,77 |
| 19th2 tomato (9th), sekali seminggu | 0/1/10/11 | 1/1/10/12 | 1 | 0,58 |
| 19th tomato (6th) | 0/16/19/35 | 6/11/17/34 | −1 | 4,65 |
| lin tomato (4th) | 16/11/2/29 | 1/6/0/7 | −22 | 9,20 |
| lin tomato (8th) | 2/4/1/7 | 3/2/1/6 | −1 | 1,29 |
| 19th2 tomato (8th), dua kali seminggu | 4/10/29/43 | 2/7/26/35 | −8 | 2,71 |

Tabel VI memuat 14 sekuens (9 untuk pengumpulan sekali seminggu dan 5 untuk dua kali seminggu); baris selengkapnya ada di makalah. Makalah tidak merangkum RMSE keseluruhan.

## Kelebihan dan Keterbatasan
Kelebihan: alur lengkap dari deteksi sampai hitungan per kelas kematangan, perbandingan jujur RGB dan multispektral, dan penetapan kelas melalui *voting* lintas bingkai sehingga satu tomat menghasilkan satu keputusan.

Keterbatasan yang dinyatakan penulis: pembedaan kelas almost mature dan immature sulit karena warna kulit serupa, dan frekuensi pengumpulan mingguan terlalu jarang pada fase perubahan warna cepat. Penulis tidak menyatakan keterbatasan lain secara eksplisit.

Menurut pembacaan ringkasan ini: (1) akurasi klasifikasi sebagian besar di kisaran 58% sampai 81% dan sangat bervariasi antar algoritme (misalnya ANN 38% sampai 75% pada lin tomato), sehingga tidak ada kombinasi yang konsisten unggul; (2) MOTA rendah (4,40% sampai 76,10%) dengan FN tinggi menandakan banyak tomat tidak terdeteksi, dan selisih total negatif pada Tabel VI menunjukkan hitungan prediksi cenderung lebih rendah daripada acuan; (3) pembahasan hasil gabungan pada teks sangat singkat dan tidak memberi ringkasan galat keseluruhan; (4) pembagian pelatihan dan pengujian pada klasifikasi memakai kotak acuan, sehingga akurasi klasifikasi belum mencerminkan kinerja saat dipasangkan dengan detektor.

## Kaitan dengan Tinjauan main6
Makalah ini menangani tomat yang terlihat pada banyak bingkai dalam urutan citra dengan mekanisme pelacakan multi-objek berbasis deteksi (StrongSORT atau ByteTrack, dengan fitur tampilan OSNet) dan ID per tomat. Hitungan dilaporkan per kelas kematangan (−3, −2, −1) pada Tabel VI, dengan acuan berupa anotasi pada sekuens citra yang dilabeli kematangannya secara mingguan; acuan bukan hasil panen. Hanya satu sisi rak yang difoto dengan gerakan lateral, sehingga identitas lintas sisi tidak ditangani.

Hal yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pola menetapkan kelas kematangan satu objek melalui *voting* atas semua pengamatannya, serta pelaporan hitungan per kelas. Hasil makalah juga menunjukkan bahwa kelas kematangan yang berdekatan sulit dibedakan berdasarkan warna, yang relevan bagi kelas antara pada tandan sawit. Tantangannya, pelacakan pada makalah ini bergantung pada urutan bingkai kontinu dalam satu sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `pai2024maturity`.

Pai dan Lin mengusulkan sistem estimasi kematangan dan hasil tomat ceri dari citra RGB dan multispektral, yang menggabungkan deteksi YOLOv8 dengan OSNet, pelacakan StrongSORT atau ByteTrack, dan klasifikasi tiga kelas kematangan (SVM, KNN, ANN) dengan pemungutan suara lintas bingkai. Akurasi klasifikasi berkisar 38% sampai 81% pada tiga set data, dengan RGB sering sebanding atau lebih baik daripada indeks multispektral, dan selisih jumlah total tomat per sekuens uji berkisar −22 sampai +1.

Catatan verifikasi data: jumlah kotak dari Tabel II; akurasi klasifikasi dari Tabel III dan IV; MOTA, IDs, FP, dan FN dari Tabel V; hitungan per kelas, selisih, dan RMSE dari Tabel VI. Tabel dibaca dari ekstraksi yang terpecah per baris; urutan kolom pada Tabel VI direkonstruksi dari judul kolom (acuan −3/−2/−1/total, prediksi −3/−2/−1/total, selisih, RMSE) dan konsisten dengan penjumlahan baris yang diperiksa. Tidak dapat diverifikasi dari teks: jumlah pohon atau tanaman, lokasi dan kultivar, jumlah citra atau bingkai, metrik deteksi YOLOv8 (mAP), dan nilai Gambar 2 dan 3. Frasa "principal component analysis" disebut pada abstrak dan kesimpulan, tetapi metode dan hasilnya tidak diuraikan pada isi makalah.
