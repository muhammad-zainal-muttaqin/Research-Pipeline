# Yield estimation and visualization solution for precision agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `osman2021yield` |
| Judul asli | Yield estimation and visualization solution for precision agriculture |
| Penulis | Osman, Youssef; Dennis, Reed; Elgazzar, Khalid |
| Tahun | 2021 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, citrus, pumpkin/squash |

## Tautan Akses
- PDF: [osman2021yield.pdf](../pdf/osman2021yield.pdf)
- DOI resmi: https://doi.org/10.3390/s21196657

## Gambaran Umum
Makalah ini menyajikan kerangka kerja menyeluruh (*end-to-end*) untuk pemanenan cerdas: estimasi hasil panen dengan menghitung buah pada video, pemetaan hasil panen berdasarkan koordinat GPS, dan penentuan penempatan wadah panen yang meminimalkan jumlah wadah. Penghitungan memakai detektor YOLOv3 dengan *spatial pyramid pooling* (YOLOv3-SPP) dan pelacak DeepSORT yang dimodifikasi: ekstraktor fitur penampilan bawaan DeepSORT, yang dilatih hanya pada data pejalan kaki, diganti dengan ResNet18 berbobot ImageNet sehingga tidak perlu dilatih ulang untuk buah.

Data berupa video apel dari kebun apel, video jeruk (*oranges*), dan video labu (*pumpkins*) dari pesawat nirawak. Pada potongan pohon apel (sekitar 300 apel), bobot yang disesuaikan (*fine-tuned*) mencapai akurasi 91,5% (313 terhitung dari 342 acuan, Tabel 5). Pada tiga baris pohon apel utuh (sekitar 3.000 sampai 4.000 apel per baris), akurasi 90,6%, 93,0%, dan 95,8% (Tabel 6). Pada jeruk dengan bobot praterlatih, akurasi 79,3%, dan pada labu 93,9% (Tabel 7). Akurasi didefinisikan sebagai $(GT - L)/GT \times 100$ dengan $L$ galat L1 antara hitungan prediksi dan hitungan manual.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa estimasi hasil (penghitungan buah) membantu petani merencanakan tenaga kerja, kendaraan, penyimpanan, dan pengemasan. Metode lama berbasis warna dan tekstur spesifik pada satu tanaman dan lemah di luar lingkungan terkendali. Karya pembelajaran mendalam yang ditinjau (misalnya Faster R-CNN, CNN pada citra tunggal) bekerja pada citra, bukan video, padahal rekaman lapangan umumnya berupa video. Pelacakan diperlukan agar buah yang sama pada banyak bingkai hanya dihitung sekali.

Penulis juga menilai pekerjaan terdahulu pada video (FCN dengan pelacak optical flow KLT, ditambah *Structure from Motion* untuk menghindari penghitungan apel antarbaris) dilakukan pada iluminasi terkendali dan berat secara komputasi. DeepSORT asli tidak dapat dipakai untuk buah karena ekstraktor fiturnya dilatih pada data pejalan kaki.

## Ide Utama
Gagasan utamanya adalah memakai pelacakan berbasis deteksi dengan ekstraktor fitur penampilan generik (ResNet18 praterlatih ImageNet, keluaran lapisan *average pooling* berdimensi 512) sehingga pelacak dapat dipakai untuk buah apa pun tanpa pelatihan, dan hanya detektor yang dilatih ulang pada buah baru. Penulis menyatakan bahwa pemilihan pelacak tertentu bukan inti penelitian dan pelacak lain dapat saling menggantikan. Detektor diakui sebagai hambatan utama sistem.

Dua komponen tambahan menyusun kerangka itu: anotasi GPS pada kelompok bingkai untuk memetakan hasil, dan pengoptimalan penempatan wadah dengan batasan kapasitas serta jarak maksimum antarwadah.

## Cara Kerja Langkah demi Langkah

```
  video --> YOLOv3-SPP --> kotak (+ filter ukuran 30 px) --> DeepSORT
                                                          (ResNet18, cosine,
                                                           Hungarian, IoU 0,3)
                                                               |
                                    GPS tiap 3 s (90 bingkai) <-+--> hitungan
                                                               |
                                                    peta (Folium) + penempatan wadah
```

### 1. Akuisisi Data
Dua set apel disiapkan dari rekaman kebun apel: sekitar 150 citra (set awal, apel belum sepenuhnya matang) dan sekitar 100 citra (set untuk estimasi baris penuh, apel matang). Set labu terdiri dari 30 citra, sebagian besar pandangan udara dari pesawat nirawak. Video jeruk dipakai dengan bobot COCO praterlatih tanpa pelatihan tambahan. Video apel direkam pada 30 bingkai per detik dengan GPS tersinkronisasi; lokasi kebun disebut berada di sekitar Oshawa, Ontario (berdasarkan afiliasi penulis dan koordinat pada Tabel 3), tanpa nama kebun, kultivar, atau jumlah pohon dalam teks. Anotasi memakai YOLOLabel dengan satu kelas "apple".

Aturan anotasi (Tabel 4) mencakup apel yang tertutup sebagian daun, setengah tertutup, tertutup berat (hanya bagian tampak yang dianotasi), saling tumpang tindih, dan berbagai kondisi cahaya. Apel yang hampir seluruhnya tertutup daun tidak dianotasi agar detektor tidak keliru mengenali daun sebagai apel.

### 2. Deteksi dengan YOLOv3-SPP
YOLOv3 (*backbone* Darknet-53) dengan SPP dipilih berdasarkan perbandingan AP dan FPS pada Tabel 1 (misalnya YOLOv3-608 AP 43% pada 43,1 FPS, EfficientDet-D3 AP 47,2% pada 34,4 FPS; angka dikutip dari makalah lain). Arsitektur tidak diubah; bobot COCO disesuaikan pada data kecil. Mekanisme koreksi: kotak dengan tinggi dan lebar di bawah 30 piksel dibuang agar apel baris pohon di belakang tidak ikut terhitung.

### 3. Pelacakan DeepSORT dengan ResNet18
Keadaan Kalman berdimensi 8 (pusat x, y, rasio aspek, tinggi, dan kecepatannya) dengan model kecepatan konstan. Hanya fitur penampilan yang dipakai sebagai metrik (jarak kosinus antara vektor fitur trek dan deteksi), dengan algoritma Hungarian untuk penugasan. Parameter: jarak maksimum 0,15; trek dikonfirmasi setelah lebih dari 2 *hit*; usia maksimum 30 bingkai; deteksi yang tak terasosiasi diuji dengan IoU (ambang 0,3 atau lebih) sebelum dibuat trek baru; keyakinan minimum detektor 0,4. Apel dihitung hanya saat trek berstatus *confirmed*. Uji awal menunjukkan tidak ada perbedaan akurasi hitung antara ResNet18 dan ResNet101.

### 4. Pemetaan GPS dan Penempatan Wadah
Satu titik GPS dicatat tiap 3 detik, sehingga tiap 90 bingkai (30 FPS) dipasangkan dengan satu titik dan jumlah apel baru pada periode itu. Peta dibuat dengan paket Folium di atas OpenStreetMap. Penempatan wadah dirumuskan sebagai minimisasi jumlah wadah dengan syarat tiap apel masuk tepat satu wadah, bobot dalam wadah tidak melebihi kapasitas, dan jarak antarwadah tidak melampaui batas; hasilnya jumlah wadah dan koordinat GPS-nya.

## Eksperimen dan Hasil
Acuan adalah hitungan manual oleh manusia.

**Potongan pohon apel (Tabel 5).**

| Metrik | Praterlatih | Praterlatih + koreksi | Fine-tuned |
|---|---|---|---|
| Prediksi/acuan | 523/342 | 299/342 | 313/342 |
| Galat L1 | 181 | 43 | 29 |
| Akurasi | 47,06% | 87,43% | 91,5% |

**Baris apel penuh (Tabel 6, bobot fine-tuned).**

| Metrik | Baris 1 | Baris 2 | Baris 3 |
|---|---|---|---|
| Prediksi/acuan | 4.375/4.827 | 3.647/3.921 | 3.530/3.683 |
| Galat L1 | 452 | 276 | 153 |
| Akurasi | 90,6% | 93,0% | 95,8% |

Penulis menjelaskan baris 1 memiliki beberapa pohon sangat rimbun sehingga banyak apel tidak terdeteksi, baris 2 terkena sinar matahari langsung pada kamera sehingga apel tampak lebih gelap, dan baris 3 memiliki pencahayaan baik.

**Jeruk dan labu (Tabel 7).**

| Metrik | Labu | Jeruk |
|---|---|---|
| Prediksi/acuan | 219/233 | 96/121 |
| Galat L1 | 14 | 25 |
| Akurasi | 93,9% | 79,3% |

Teks utama menyebut akurasi labu 94,9%, sedangkan tabel dan abstrak menyebut 93,9%; dari 219/233 tampak sekitar 94,0%, sehingga angka 94,9% pada teks diperkirakan salah ketik (menurut pembacaan ringkasan ini). Jeruk memakai bobot praterlatih tanpa fine-tuning; jeruk yang tertutup berat tidak terdeteksi.

**Penempatan wadah (baris apel 3).** Dengan wadah berkapasitas 300 apel dan jarak maksimum 40 kaki (juga sama pada 100 kaki), ditempatkan 12 wadah: 11 terpakai 100% dan satu terpakai 77% karena sisa 230 apel (Tabel 8). Dengan kapasitas 1.000 apel dan jarak 40 kaki, ditempatkan 4 wadah dengan pemanfaatan 97,4%, 80%, 76,7%, dan 98,9% (Tabel 9); dengan jarak 100 kaki, 4 wadah dengan pemanfaatan 100%, 100%, 100%, dan 53% (Tabel 10) dan jarak antarwadah tidak merata. Pada kapasitas 2.000 apel, hasil sama dengan kapasitas 1.000 untuk jarak 40 kaki, dan hanya dua wadah untuk jarak 100 kaki.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: pelacak dapat dipakai pada banyak buah tanpa pelatihan ulang; kerangka bekerja pada video apel skala baris penuh; anotasi yang mencakup oklusi dan variasi cahaya meningkatkan kinerja; hasil dapat dipetakan dan dipakai untuk logistik panen.

Keterbatasan yang dinyatakan penulis: kinerja dibatasi oleh detektor dan tantangan visual seperti oklusi, dan detektor tetap menjadi hambatan; buah yang tertutup besar tidak terdeteksi (hitungan kurang dari acuan); data labu dan jeruk sangat terbatas (30 citra labu, tanpa data jeruk riil sendiri); pelatihan lebih banyak data berisiko terlalu cocok (*overfitting*) pada baris tertentu.

Menurut pembacaan ringkasan ini: (1) evaluasi hanya berupa hitungan total per video, tanpa metrik pelacakan (MOTA, IDF1, pergantian identitas) sehingga kesalahan yang saling meniadakan antara penghitungan ganda dan buah terlewat tidak dapat dipisahkan; semua hasil apel dan labu menghitung kurang dari acuan, tetapi hitungan praterlatih melebihi acuan; (2) ambang 30 piksel ditentukan dari satu video yang sama dengan evaluasi, sehingga koreksi mungkin disesuaikan pada data uji; (3) tidak disebutkan apakah video uji terpisah dari citra latih; (4) metode penghitungan hanya mengandalkan satu lintasan kamera dan tidak menangani sisi lain pohon, sehingga buah di sisi berlawanan tidak dihitung; (5) kondisi GPS dan jumlah pohon tidak dirinci.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada lebih dari satu bingkai melalui pelacakan berbasis deteksi (DeepSORT dengan fitur ResNet18, jarak kosinus, algoritma Hungarian, dan pencocokan IoU cadangan), dan hitungan diambil dari trek yang terkonfirmasi. Mekanisme ini berlaku pada satu video berkelanjutan dari satu sisi baris pohon; tidak ada penggabungan lintas sisi atau lintas baris, dan penulis justru menyaring apel baris belakang dengan ambang ukuran. Hitungan tidak dilaporkan per kelas (hanya satu kelas "apple"; labu dan jeruk dihitung terpisah per jenis). Acuan hitung adalah hitungan manual oleh manusia pada video, bukan hasil panen.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola ekstraktor fitur penampilan generik berbobot praterlatih yang dipasang pada pelacak sehingga hanya detektor yang dilatih ulang, hitungan hanya dari trek yang dikonfirmasi, dan penyaringan objek jauh berdasarkan ukuran kotak. Penggunaan koordinat GPS per kelompok bingkai juga relevan untuk memetakan hitungan, tetapi tidak menyelesaikan identitas lintas sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `osman2021yield`.

Osman dkk. (2021, *Sensors* 21, 6657) mengusulkan kerangka estimasi hasil dan visualisasi untuk pertanian presisi yang memakai YOLOv3-SPP dan DeepSORT dengan ekstraktor fitur ResNet18 sebagai pengganti jaringan khusus pejalan kaki, sehingga pelacak berfungsi pada berbagai buah tanpa pelatihan ulang. Akurasi hitung terhadap hitungan manual adalah 91,5% pada potongan pohon apel (313 dari 342), 90,6% sampai 95,8% pada tiga baris apel penuh, 93,9% pada labu, dan 79,3% pada jeruk dengan bobot praterlatih; hasil juga dipetakan dengan GPS dan dipakai untuk menentukan penempatan wadah panen.

Catatan verifikasi data: angka Tabel 5, 6, 7, 8, 9, dan 10 dibaca langsung dari teks ekstraksi, dengan pemetaan kolom disimpulkan dari urutan sel yang konsisten dengan keterangan tabel; angka akurasi cocok dengan rumus $(GT-L)/GT$. Akurasi labu tertulis 93,9% pada abstrak dan Tabel 7 tetapi 94,9% pada teks bagian 4.3. Angka AP dan FPS pada Tabel 1 dikutip penulis dari makalah lain. Tidak dapat diverifikasi dari teks: jumlah pohon, kultivar, nama kebun, pembagian latih dan uji, serta resolusi video. Teks berbahasa Inggris dan terbaca baik.
