# StableSort-CMC: a tracking algorithm for robot dog based orchard fruit counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2024stablesort` |
| Judul asli | StableSort-CMC: a tracking algorithm for robot dog based orchard fruit counting |
| Penulis | Zhang, Wenli; Huang, Ansheng; Zheng, Chao; Jiang, Kaiwen; Guo, Wei |
| Tahun | 2024 |
| Venue | Proceedings 2024 China Automation Congress Cac 2024 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | peach/nectarine |

## Tautan Akses
- PDF: [zhang2024stablesort.pdf](../pdf/zhang2024stablesort.pdf)
- DOI resmi: https://doi.org/10.1109/cac63892.2024.10865478

## Gambaran Umum
Makalah prosiding (China Automation Congress 2024) ini mengusulkan StableSort-CMC, yaitu algoritma pelacakan buah yang menambahkan modul kompensasi gerak kamera (*camera motion compensation*, CMC) pada pelacak OrangeSort untuk pencacahan buah dari video. Masalah yang dituju adalah getaran kamera gimbal pada anjing robot (CyberDog, Xiaomi) yang berjalan di medan kebun tidak rata. Getaran menimbulkan rotasi dan perubahan skala antarbingkai yang sulit diprediksi oleh filter Kalman linear, sehingga identitas buah berganti dan buah yang sama terhitung ulang.

Data berupa sebelas video nektarin yang diambil pada 16 Juni 2023 di kebun Beijing Alumni Base of Jilin University, Distrik Shunyi, Beijing. Detektor yang dipakai adalah DomAda-FruitDet (mAP_0.5 sebesar 0,783 menurut teks). Pada perbandingan dengan ByteTrack dan BoT-SORT, StableSort-CMC memperoleh *Multiple Object Tracking Accuracy* (MOTA) 63,4% dan *Multiple Object Tracking Precision* (MOTP) 74,6%. Pada ablasi terhadap OrangeSort, penambahan CMC menaikkan MOTA dari 60,5 menjadi 63,4 dan menurunkan galat hitung dari 0,667 menjadi 0,571 terhadap hitungan manual 84 buah.

Perlu dicatat bahwa hitungan algoritma (132) masih jauh di atas hitungan manual (84), sehingga semua pelacak yang dibandingkan menghitung berlebih.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penaksiran hasil panen sebelum panen membantu pengelola mengalokasikan tenaga kerja, dan hitung manual di lapangan memakan waktu serta rentan terhadap kesalahan penghitung. Pencacahan berbasis video dengan deteksi dan pelacakan telah menjadi pendekatan utama. Penulis menyebut contoh dari literatur: YOLOv4 dengan DeepSORT untuk buah pir, MangoYOLO dengan filter Kalman dan pencocokan Hungarian untuk mangga, YOLOv4-tiny untuk apel, dan OrangeSort untuk jeruk (karya tim penulis sendiri).

Masalah yang diangkat adalah bahwa pelacak yang bergantung pada filter Kalman dan pencocokan Hungarian mengasumsikan gerak linear-Gaussian. Pada kamera yang bergetar, urutan citra tidak hanya mengalami translasi tetapi juga rotasi dan penskalaan, sehingga prediksi posisi buah meleset, pencocokan gagal, dan buah yang sama menerima nomor identitas baru.

## Ide Utama
Gerak kamera antarbingkai diestimasi dengan registrasi citra klasik dan dimasukkan ke langkah prediksi filter Kalman, sehingga prediksi posisi buah sudah memperhitungkan getaran. Gagasan ini diambil dari BoT-SORT. Pelacak dasarnya OrangeSort, dan detektornya DomAda-FruitDet. Identitas buah antarbingkai dipertahankan lewat pencocokan Hungarian pada matriks biaya IoU antara kotak prediksi dan kotak deteksi.

## Cara Kerja Langkah demi Langkah

```
  Video -> bingkai -> +--> Deteksi (DomAda-FruitDet) --------+
                      |                                      v
                      +--> Titik sudut -> optical flow  --> Kalman (dikoreksi)
                           -> matriks afin 2x3               -> IoU -> Hungarian
                                                              -> ID & hitungan
```

### 1. Akuisisi data
Anjing robot CyberDog berjalan di antara barisan pohon dan merekam video dua sisi setiap baris pohon. Laju bingkai diatur agar sekitar 30 citra diperoleh pada tiap sisi pohon, sehingga sekitar 60 citra untuk sisi kiri dan kanan satu pohon. Total sebelas video nektarin dikumpulkan. Kultivar tidak dilaporkan. Untuk deteksi, dibuat 678 citra nektarin yang diacak dan dibagi 7:3 menjadi data latih dan validasi; untuk pelacakan dibuat 1.061 urutan citra. Komputer pelatihan memakai GPU yang ditulis "GEFORCE GTX 3090" dan CPU Intel i7 generasi ke-8.

### 2. Kompensasi gerak kamera
Pada setiap bingkai dideteksi titik sudut citra (*corner points*). Titik sudut dua bingkai bersebelahan dicocokkan dengan aliran optik jarang (*sparse optical flow*), lalu fungsi transformasi afin menghitung matriks 2×3 yang berisi bagian skala-rotasi $M_{2\times 2}$ dan translasi $T_{2\times 1}$. Parameter ini dipakai untuk mengoreksi rerata dan varians filter Kalman melalui operasi matriks, mengikuti cara BoT-SORT.

### 3. Deteksi
DomAda-FruitDet adalah detektor buah bebas-jangkar (*anchor-free*) adaptasi domain berbasis CenterNet yang dikembangkan tim penulis. Bingkai diskalakan lalu dimasukkan ke model untuk memperoleh posisi buah.

### 4. Pelacakan dan pencacahan
Hasil deteksi dan parameter gerak dipakai untuk menghitung kecocokan antara prediksi Kalman dan deteksi bingkai berjalan. Matriks biaya IoU dibangun, dan pencocokan Hungarian menghasilkan tiga keluaran: deteksi tak terpasang, deteksi terpasang benar, dan pelacak tak terpasang. Posisi pelacak tak terpasang diperkirakan dari rerata perpindahan buah yang terlacak. Filter Kalman baru dibuat untuk deteksi tak terpasang, dan pelacak yang melewati daerah hitung dihapus. Daerah hitung ditetapkan pada 3/5 bagian tengah citra, mengikuti penelitian sebelumnya tim penulis.

## Eksperimen dan Hasil
Hitungan algoritma dibandingkan dengan hitungan manual sebesar 84 buah. Metrik hitung meliputi hitungan benar, hitungan keliru (daun latar belakang terhitung buah), hitungan ganda (buah sama terhitung berulang), dan galat hitung. Metrik pelacakan memakai MOTA dan MOTP dari tantangan MOT, dengan $\text{MOTA} = 1 - \sum(FN+FP+IDS)/\sum GT$. Sumber ketiga angka subset data yang dihitung manual (84 buah) tidak dijelaskan pada teks.

Tabel I (galat hitung):

| Pelacak | Manual | Hitungan | Benar | Keliru | Ganda | Galat |
|---|---|---|---|---|---|---|
| ByteTrack | 84 | 143 | 72 | 36 | 35 | 0,702 |
| BoT-SORT | 84 | 138 | 77 | 30 | 31 | 0,642 |
| StableSort-CMC | 84 | 132 | 75 | 33 | 24 | 0,571 |

Tabel II (pelacakan):

| Pelacak | MOTA | MOTP | FP | FN | IDS |
|---|---|---|---|---|---|
| ByteTrack | 55,5 | 72,4 | 131 | 936 | 35 |
| BoT-SORT | 59,4 | 73,2 | 104 | 871 | 31 |
| StableSort-CMC | 63,4 | 74,6 | 178 | 706 | 24 |

Tabel III dan IV (ablasi CMC pada OrangeSort):

| Pelacak | MOTA | FP | FN | IDS | Hitungan | Benar | Keliru | Ganda | Galat |
|---|---|---|---|---|---|---|---|---|---|
| OrangeSort | 60,5 | 196 | 755 | 32 | 140 | 74 | 34 | 32 | 0,667 |
| OrangeSort+CMC | 63,4 | 178 | 706 | 24 | 132 | 75 | 33 | 24 | 0,571 |

Teks menyatakan CMC menaikkan MOTA sebesar 2,9% (selisih 63,4 dan 60,5, poin persentase) dan menurunkan galat hitung sebesar 9,6% (selisih 0,667 dan 0,571). Hitungan ganda turun dari 32 menjadi 24. Gambar 3 memperlihatkan contoh dua buah yang tetap bernomor sama dengan CMC, sedangkan tanpa CMC nomornya berganti (dari 5 dan 6 menjadi 8 dan 7) sehingga terhitung dua kali. Perlu dicatat bahwa StableSort-CMC memiliki FP paling tinggi di antara tiga pelacak pada Tabel II, tetapi FN dan IDS paling rendah.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: CMC mengurangi hitungan ganda akibat getaran, dan pelacak dengan CMC lebih unggul daripada ByteTrack yang hanya memakai filter Kalman serta daripada BoT-SORT pada data yang sama.

Keterbatasan yang dinyatakan penulis dibatasi pada rencana lanjutan: model ringan untuk perangkat tepi (*edge device*), pencacahan waktu-nyata pada anjing robot, dan penggunaan registrasi citra sebagai pengganti pelacakan bingkai demi bingkai.

Menurut pembacaan ringkasan ini, terdapat keterbatasan lain. Hitungan 132 masih 57,1% di atas hitungan manual 84 (dihitung dari selisih), sehingga masalah hitungan berlebih tidak terselesaikan. Evaluasi hanya satu jenis buah (nektarin), satu lokasi, dan satu tanggal. Jumlah pohon dan keterkaitan antara 84 buah hitungan manual dengan sebelas video tidak dijelaskan. Tidak ada hitungan per kelas, tidak ada ulangan atau uji signifikansi, dan sumber hitungan manual (panen atau hitung lapangan) tidak dijelaskan. Perbandingan hanya mencakup dua pelacak pembanding.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dalam satu video lintasan, bukan lintas sisi pohon. Mekanismenya adalah pelacakan-oleh-deteksi (*tracking-by-detection*) dengan filter Kalman, pencocokan Hungarian berbasis IoU, kompensasi gerak kamera, dan daerah hitung di tengah citra. Video dua sisi baris pohon direkam, tetapi makalah tidak menjelaskan penggabungan identitas buah dari sisi kiri dengan sisi kanan; sekitar 30 citra per sisi dilaporkan sebagai pengambilan sampel. Hitungan per kelas tidak dilaporkan. Acuan hitung adalah hitungan manual (84 buah), dengan ketentuan lokasi dan waktu pencacahan manual tidak dijelaskan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan mengoreksi prediksi gerak dengan estimasi gerak kamera agar identitas bertahan selama video mengitari pohon, serta rancangan daerah hitung untuk mengurangi hitungan ulang. Makalah ini tidak menawarkan mekanisme untuk mencocokkan tandan antar sisi pohon yang tidak berurutan dalam video.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhang2024stablesort`.

Zhang dkk. (2024) mengusulkan StableSort-CMC, pelacak buah yang menambahkan kompensasi gerak kamera berbasis registrasi citra pada OrangeSort untuk video dari anjing robot di kebun nektarin. Pada data mereka, MOTA mencapai 63,4% dan MOTP 74,6%, lebih tinggi daripada ByteTrack (55,5% dan 72,4%) dan BoT-SORT (59,4% dan 73,2%). Hitungan algoritma (132) masih melebihi hitungan manual (84), dengan galat hitung 0,571.

Catatan verifikasi data: Angka MOTA, MOTP, FP, FN, dan IDS diambil dari Tabel II dan III; angka hitungan dari Tabel I dan IV; jumlah video (sebelas), tanggal, dan pembagian 7:3 dari Seksi III-A dan III-B; mAP_0.5 0,783 dari Seksi III-C. Berkas teks ekstraksi memuat dua lapisan: lapisan pertama terenkode rusak (karakter bergeser) dan tidak terbaca, sehingga angka diambil dari lapisan OCR yang tersedia di bagian berikutnya. Angka pada lapisan OCR konsisten secara internal (misalnya 72+36+35=143, 77+30+31=138, 75+33+24=132). Penentuan jumlah pohon dan sumber hitungan manual 84 tidak dapat diverifikasi dari teks, dan kolom beberapa tabel diekstraksi tidak berurutan sehingga urutan kolom disimpulkan dari konsistensi jumlah.
