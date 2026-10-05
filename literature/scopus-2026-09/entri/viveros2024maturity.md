# Maturity Recognition and Fruit Counting for Sweet Peppers in Greenhouses Using Deep Learning Neural Networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `viveros2024maturity` |
| Judul asli | Maturity Recognition and Fruit Counting for Sweet Peppers in Greenhouses Using Deep Learning Neural Networks |
| Penulis | Viveros Escamilla, Luis David; G\'omez-Espinosa, Alfonso; Escobedo Cabello, Jes\'us Arturo; Cantoral-Ceballos, Jose Antonio |
| Tahun | 2024 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus, sweet pepper |

## Tautan Akses
- PDF: [viveros2024maturity.pdf](../pdf/viveros2024maturity.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture14030331

## Gambaran Umum
Makalah ini membangun sistem pengenalan tingkat kematangan dan penghitungan buah paprika manis (*sweet pepper*, *Capsicum annuum*) di rumah kaca. Detektor YOLOv5s mengklasifikasikan setiap buah ke dalam empat kelas kematangan (*immature*, *early-mid*, *mid-late*, *mature*), dan pelacak DeepSORT memberi identitas pada buah di sepanjang urutan citra agar setiap buah dihitung satu kali. Citra diambil dengan kamera RGB-D Intel RealSense D435i di rumah kaca CAETEC (Tecnologico de Monterrey, Meksiko), dengan jarak horizontal kamera ke tanaman sekitar 60 cm pada ketinggian sekitar 1,3 m.

Kumpulan data untuk detektor terdiri dari 1.863 citra (gabungan dataset CAETEC dan dataset Roboflow) yang dibagi 70% latih, 20% validasi, dan 10% uji; sebanyak 186 citra dipakai untuk evaluasi. Bobot terbaik diperoleh pada epoch 250 dengan mAP@0,5 sebesar 0,803 dan mAP@0,95 sebesar 0,575 (Tabel 4). F1 gabungan tertinggi 0,77 pada ambang keyakinan 0,538, dan presisi terbaik dicapai pada keyakinan 0,973.

Penghitungan diuji pada dua video simulasi yang dibuat dari 70 citra rumah kaca yang disusun menyamping untuk meniru gerak robot menyusuri lorong. MOTA yang dilaporkan 0,88 (video 1) dan 0,87 (video 2) pada Tabel 6. Abstrak menyebut "tingkat akurasi 85,7%" pada dua lingkungan simulasi; angka itu tidak muncul di bagian hasil pada teks yang tersedia.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa prakiraan hasil panen memerlukan penghitungan buah dan penilaian tingkat kematangan, sedangkan penghitungan manual lambat dan rawan galat. Di rumah kaca, penempatan kamera terbatas, penampilan paprika berubah sepanjang perkembangannya, dan vegetasi yang rapat menimbulkan oklusi daun dan ranting. Paprika hijau (belum matang) sulit dibedakan dari latar daun hijau.

Pada penghitungan, kesulitan yang disebut adalah deteksi yang tidak konsisten antarbingkai dan risiko penghitungan ganda. Penulis menyatakan bahwa pada pustaka yang ditinjau belum ada penelitian yang mengklasifikasikan kematangan paprika sekaligus melacaknya di rumah kaca.

## Ide Utama
Gagasan utamanya adalah memisahkan dua tugas: YOLOv5 menghasilkan kotak, kelas kematangan, dan skor keyakinan per bingkai, sedangkan DeepSORT menghubungkan deteksi yang sama antarbingkai sehingga jumlah lintasan unik menjadi hitungan buah per lorong. Penulis berargumen bahwa kesalahan klasifikasi kematangan berdampak kecil pada penghitungan, karena DeepSORT bertujuan menghitung dan yang terpenting adalah keberhasilan deteksi dan pelacakan, bukan benarnya kelas kematangan.

Makalah ini tidak memakai kanal kedalaman untuk pelacakan; kamera RGB-D hanya dikonfigurasi menghasilkan citra RGB dan kedalaman terselaras pada resolusi 1280 × 720, dan analisis memakai citra RGB yang diubah ukurannya menjadi 640 × 640.

## Cara Kerja Langkah demi Langkah

```
  citra RGB (640x640) --> YOLOv5s --> kotak + kelas + keyakinan
                                         |
                                         v
                                  DeepSORT (Kalman, Hungarian,
                                   fitur penampilan, jarak kosinus)
                                         |
                                         v
                              identitas lintasan --> hitungan buah
```

### 1. Akuisisi Data
Citra diambil di rumah kaca paprika CAETEC oleh pihak lain (Montoya Cavero) dengan Intel RealSense D435i; kamera tegak lurus terhadap tanaman pada tinggi kira-kira 1,3 m dan jarak horizontal kira-kira 60 cm, antara pukul 11.00 dan 16.00 pada hari cerah tanpa awan. Dataset dasar berisi 620 citra paprika hijau, merah, kuning, dan oranye dengan berbagai oklusi dan tumpang tindih. Dataset Roboflow ("Maturity Peppers in Greenhouses by Object Detection Image Dataset") ditambahkan untuk memperbanyak data. Pendahuluan menyebut 1.127 citra dari CAETEC; jumlah total yang dipakai adalah 1.863 citra. Rincian jumlah citra tiap sumber tidak dijelaskan lebih lanjut. Jumlah tanaman dan kultivar tidak dilaporkan.

### 2. Definisi Kelas Kematangan
Empat kelas didefinisikan pada Tabel 3: *Immature* (seluruhnya hijau), *Early-Mid* (kematangan 10 sampai 50%), *Mid-Late* (50 sampai 90%), dan *Mature* (lebih dari 90%). Jumlah anotasi tiap kelas disajikan hanya pada Gambar 13a dan tidak terbaca dari teks. Penulis menyatakan kelas immature paling banyak muncul, sedangkan di bagian lain menyatakan kelas early-mid memiliki sampel latih lebih banyak; kedua pernyataan ini tidak sama dan tidak dapat diselesaikan dari teks.

### 3. Pelatihan YOLOv5s
Model YOLOv5s (Ultralytics) dilatih dengan transfer belajar dari bobot COCO, *batch* 10 citra, laju belajar 0,001 dan 0,0001 yang dicoba, momentum 0,937, dan *weight decay* 0,005. Jumlah epoch yang dicoba adalah 80, 200, 250, 300, dan 500, dengan penghentian dini. Augmentasi mencakup rotasi 90°, pemotongan (zoom 0 sampai 20%), pengaburan hingga 2,5 piksel, dan derau hingga 5% piksel. Saat inferensi, ambang keyakinan minimum 85%. Perangkat keras: Dell G7 7790 dengan Intel Core i7-9750H, NVIDIA GeForce RTX 2060 Laptop, dan RAM 16 GB.

### 4. Pelacakan dan Penghitungan
SORT memakai filter Kalman dan algoritma Hungarian dengan matriks biaya berbasis IoU. DeepSORT menambahkan jaringan konvolusi residual lebar yang menghasilkan vektor fitur penampilan 128 dimensi, jarak Mahalanobis untuk gerak, dan jarak kosinus terkecil untuk penampilan. Algoritma 1 menambahkan penyaring ukuran (*size filter*) pada luas kotak keluaran sebelum penghitungan per kelas. Dua video simulasi dibuat dengan DaVinci Resolve 18.5.1 dari masing-masing 70 citra 640 × 640 yang disusun horizontal, 5 bingkai per detik. Video pertama berisi 300 bingkai dan video kedua berisi 300 bingkai (durasi disebut 1,53 menit dan 2,17 menit, sedangkan teks juga menyebut "1 menit"). Metrik pelacakan adalah MOTA: $\text{MOTA} = 1 - \sum_t (FN_t + FP_t + IDS_t) / \sum_t GT_t$.

## Eksperimen dan Hasil
**Deteksi dan kematangan (Tabel 4, epoch 250, 186 citra evaluasi).**

| Kelas | P | R | mAP@0,5 | mAP@0,95 |
|---|---|---|---|---|
| Semua | 0,807 | 0,736 | 0,803 | 0,575 |
| Early-Mid | 0,845 | 0,682 | 0,800 | 0,584 |
| Immature | 0,796 | 0,732 | 0,816 | 0,563 |
| Mature | 0,818 | 0,812 | 0,831 | 0,547 |
| Mid-Late | 0,771 | 0,720 | 0,765 | 0,606 |

Teks menyatakan bahwa kelas early-mid memiliki akurasi prediksi terbaik, sedangkan pada Tabel 4 mAP@0,5 tertinggi ada pada kelas mature (0,831); ketidaksesuaian ini dicatat apa adanya. F1 per kelas pada keyakinan 0,538 adalah mature 0,82, immature 0,76, early-mid 0,69, dan mid-late 0,68; F1 gabungan 0,77. *Recall* per kelas dari matriks konfusi: early-mid 69%, immature 79%, mature 86%, dan mid-late 71%. Sekitar 7% buah mid-late dikenali sebagai early-mid dan 2% sebagai immature; sekitar 1% buah mature dikenali sebagai immature dan 2% sebagai mid-late; sekitar 5% buah early-mid dikenali sebagai mature. Penulis menyatakan bahwa kurang dari 2% dari seluruh deteksi salah. Epoch 250 memberi hasil terbaik, disusul epoch 200.

**Penghitungan (Tabel 6).**

| Lingkungan simulasi | FP | FN | IDS | MOTA |
|---|---|---|---|---|
| Video simulasi 1 | 0 | 15 | 2 | 0,88 |
| Video simulasi 2 | 1 | 7 | 8 | 0,87 |

Jumlah buah acuan (GT) pada tiap video tidak dilaporkan dalam teks, sehingga hitungan akhir tidak dapat dibandingkan dengan acuan. Penulis menyatakan satu kasus FP berupa pantulan paprika mid-late yang dikenali sebagai immature. Penulis juga membandingkan mAP 80% pada makalah ini dengan mAP 72,64% pada Mask R-CNN pada studi lain yang tugasnya berbeda (deteksi buah dan tangkai).

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: sistem menggabungkan klasifikasi kematangan empat kelas dengan penghitungan, menangani paprika hijau yang sulit, memakai perangkat keras yang relatif sederhana, dan kode serta data tersedia di GitHub.

Keterbatasan yang dinyatakan penulis: dataset hanya mengenali buah pada skenario tertentu; deteksi dapat gagal pada rumah kaca dengan cahaya terlalu kuat atau terlalu lemah serta pada daun yang menutupi buah hampir seluruhnya; ketidakseimbangan kelas menurunkan akurasi; sistem perlu dataset khusus dan adaptasi untuk rumah kaca lain; kelas mid-late memiliki anotasi paling sedikit dan perilaku yang tidak stabil; kesalahan klasifikasi antartingkat kematangan terjadi; dan sistem perlu disesuaikan untuk aplikasi waktu nyata.

Menurut pembacaan ringkasan ini, evaluasi penghitungan lemah: hanya dua video simulasi yang dirakit dari 70 foto statis berurutan, bukan video lorong sungguhan, sehingga pergerakan, pergeseran pandangan, dan perubahan pencahayaan antarbingkai tidak mewakili kondisi lapangan. Tidak ada hitungan acuan yang dilaporkan, dan hitungan per kelas tidak dilaporkan dalam hasil. Angka 85,7% pada abstrak tidak terlacak ke tabel. Kelas yang paling penting untuk panen (kelas antara) memiliki *recall* terendah (sekitar 69 sampai 71%). Pada dataset gabungan, apakah citra uji dan latih berasal dari urutan atau tanaman yang sama tidak dinyatakan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang tampak pada lebih dari satu citra dengan pelacakan berbasis deteksi (DeepSORT: filter Kalman, algoritma Hungarian, dan fitur penampilan serta jarak kosinus) pada urutan citra yang disusun menyamping. Mekanismenya bekerja pada urutan satu arah dengan tumpang tindih antarbingkai; makalah tidak menggabungkan beberapa sisi tanaman. Detektor menghasilkan kelas kematangan per buah, tetapi hitungan per kelas tidak dilaporkan sebagai hasil; yang dilaporkan hanya MOTA (0,88 dan 0,87), FP, FN, dan IDS. Acuan hitung adalah anotasi pada video simulasi (GT per bingkai untuk MOTA); hitungan panen atau hitungan manual lapangan tidak dilaporkan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola detektor yang memberi kelas kematangan per objek ditambah pelacak identitas, serta pernyataan penulis bahwa kesalahan kelas kematangan tidak harus mengganggu identitas. Menurut pembacaan ringkasan ini, pernyataan itu belum teruji karena hitungan per kelas tidak dilaporkan; pada inventaris per kelas, pergantian kelas pada satu objek yang sama justru memengaruhi hasil. Selain itu, simulasi dari foto statis menunjukkan perlunya evaluasi pada urutan yang sesungguhnya.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `viveros2024maturity`.

Viveros Escamilla dkk. (2024, *Agriculture* 14, 331) mengembangkan sistem pengenalan kematangan dan penghitungan paprika manis di rumah kaca dengan YOLOv5s (empat kelas kematangan) dan DeepSORT. Pada 1.863 citra dengan 186 citra evaluasi, bobot terbaik mencapai mAP@0,5 0,803 dan mAP@0,95 0,575; pada dua video simulasi dari 70 foto statis, MOTA sebesar 0,88 dan 0,87.

Catatan verifikasi data: angka deteksi diambil dari Tabel 4 dan teks bagian 4.2; angka pelacakan dari Tabel 6; parameter pelatihan dari bagian 3.4; spesifikasi akuisisi dari bagian 3.1. Tabel diekstraksi satu sel per baris sehingga pemetaan kolom disimpulkan dari urutan dan terbaca konsisten. Tidak dapat diverifikasi dari teks: angka 85,7% pada abstrak, jumlah anotasi per kelas (hanya pada Gambar 13), GT jumlah buah pada video, jumlah tanaman, kultivar, dan pembagian citra antara dua sumber data. Teks berbahasa Inggris dan terbaca baik.
