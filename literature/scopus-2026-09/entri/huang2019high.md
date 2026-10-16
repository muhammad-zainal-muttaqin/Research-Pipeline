# High-throughput image analysis framework for fruit detection, localization and measurement from video streams

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `huang2019high` |
| Judul asli | High-throughput image analysis framework for fruit detection, localization and measurement from video streams |
| Penulis | Huang, Yi Hsuan; Lin, Ta Te |
| Tahun | 2019 |
| Venue | 2019 Asabe Annual International Meeting |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [huang2019high.pdf](../pdf/huang2019high.pdf)
- DOI resmi: https://doi.org/10.13031/aim.201900487

## Gambaran Umum
Makalah presentasi ASABE 2019 ini (bukan makalah jurnal yang ditelaah sejawat, sebagaimana dinyatakan pada catatan halaman pertama) mengusulkan kerangka analisis citra berlaju tinggi (*high-throughput*) untuk mendeteksi, melokalisasi, dan mengukur buah dari aliran video. Sistem memindai tanaman baris demi baris di rumah kaca dengan kamera RGB-D. Keluarannya meliputi hitungan buah, tahap kematangan tiap buah, ukuran relatif buah, dan peta distribusi spasial 2D.

Deteksi memakai YOLOv2 (masukan 416 x 416). Identitas buah antarbingkai dijaga oleh pelacakan berbasis mesin keadaan terhingga (*finite state machine*, FSM) dengan *structure from motion* (SfM) berupa pencocokan fitur, aliran optik, dan transformasi kaku. Pelacakan daring (*online*) mengaitkan buah antarbingkai dan menangani oklusi, sedangkan pelacakan luring (*offline*) membuang alarm palsu dengan pemungutan suara.

Data berupa 15 aliran video tomat dari rumah kaca eksperimen di Chin-Yong farm, Hsinchu, Taiwan. Hasil utama: model YOLOv2 yang dilatih pada buah dengan area terlihat di atas 50% mencapai *hit rate* 84,98%, sedangkan galat relatif absolut hitungan buah rata-rata terendah adalah 12%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Fenotipe tanaman yang akurat diperlukan untuk pemuliaan, tetapi pengukuran manual memakan waktu, padat karya, dan rentan galat manusia. Penulis menyebut bahwa penelitian terdahulu umumnya dikembangkan untuk satu jenis buah. Mereka ingin kerangka serbaguna yang dapat dipakai pada jenis buah lain dengan hanya melatih ulang detektor.

Penulis menyebut pustaka terdahulu tentang deteksi dan pelacakan, antara lain Faster R-CNN dan YOLO untuk deteksi, serta pelacakan buah dengan SfM (Moonrinta dkk., 2010; Liu dkk., 2018). Tujuan khusus: mengumpulkan citra dan video RGB-D untuk melatih detektor, mengembangkan algoritma pelacakan buah, dan mengukur serta memvalidasi sifat tiap buah.

## Ide Utama
Identitas buah dijaga lintas bingkai dengan memprediksi posisi buah pada bingkai berikutnya melalui transformasi kaku yang diestimasi dari titik fitur latar, lalu mencocokkan hasil prediksi dengan deteksi YOLO berdasarkan jarak L2, IoU, dan selisih median kedalaman. Informasi kedalaman dipakai untuk menyaring tanaman baris depan saja (0,3 sampai 1,0 m) sehingga buah baris belakang tidak terhitung. Buah yang sempat tak terdeteksi disimpan dalam keadaan "hilang" agar dapat dikenali ulang setelah oklusi, dan alarm palsu dibuang bila muncul terlalu sedikit dalam urutan.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Peralatan: tripod, kereta tripod, penstabil genggam 3 sumbu Feiyu SPG, dan kamera kedalaman Intel RealSense D435. Citra RGB beresolusi 1920 x 1080 dan kedalaman 1280 x 720. Resolusi kedalaman minimum terkalibrasi 0,256 m, sehingga kamera ditempatkan 0,3 m dari target. Lima baris tanaman direkam, masing-masing tiga kali, menghasilkan 15 aliran video. Jenis buah adalah tomat (tertulis pada Tabel 1). Kultivar tidak dilaporkan.

### 2. Deteksi buah
YOLOv2 dengan masukan 416 x 416 dilatih. Anotasi memakai LabelImg. Delapan dari 15 video dipilih acak dan satu citra pelatihan diambil tiap 20 bingkai. Dari set itu, 100 citra dipilih acak sebagai validasi. Dua model dilatih: model 50%-terlihat (hanya buah dengan area terlihat di atas 50% yang dilabeli) dan model 100%-terlihat (hanya buah terlihat penuh). Tabel 1: 340 citra tomat untuk pelatihan dan 100 citra untuk validasi pada tiap model. Pengujian memakai 100 citra yang berbeda dari data pelatihan, diambil dari 15 video. Metrik: *hit rate* (TP dibagi seluruh positif sebenarnya), *miss rate* (FN dibagi seluruh positif sebenarnya), dan *false alarm rate* (FP dibagi seluruh negatif).

### 3. Pelacakan daring
Penyaringan kedalaman (Persamaan 4): piksel dengan kedalaman di luar 0,3 sampai 1,0 m diredupkan dengan faktor α (nilai 0, 1/4, dan 1/5 diuji). Deteksi positif palsu disaring dengan dua kriteria: median jarak kotak harus dalam rentang batas bawah dan atas, dan simpangan baku jarak kotak harus di bawah ambang agar objek berbentuk bundar halus. FSM memiliki tiga keadaan: terlacak (*tracked*), hilang (*lost*), dan tidak aktif (*inactive*). Buah yang hilang menjadi tidak aktif bila keluar dari bidang pandang kamera dan kembali terlacak bila dideteksi ulang.

Titik fitur dideteksi dengan Shi-Tomasi dan dicocokkan antarbingkai dengan aliran optik Lucas-Kanade, setelah fitur yang terlalu jauh dibuang. Gerak antarbingkai diperkirakan sebagai transformasi kaku H (empat derajat kebebasan). Posisi prediksi dibandingkan dengan deteksi lewat jarak L2 (Persamaan 5 sampai 7), dengan ambang jarak dinamis menurut ukuran objek yang dibagi dua bila dua objek terlalu dekat. IoU (Persamaan 8) dan selisih median kedalaman turut dipakai. Tahap kedua menangani oklusi untuk buah yang tidak cocok dengan prediksi tetapi mungkin dideteksi ulang dari keadaan hilang.

### 4. Pelacakan luring dan pengukuran
Bila suatu buah berada dalam keadaan terlacak kurang dari ambang pada seluruh urutan, buah itu dianggap alarm palsu. Pada kerja ini ambang ditetapkan 2 melalui penyetelan parameter awal, dengan detektor memiliki *hit rate* 84,98% dan *false alarm rate* 15,02%. Ukuran relatif buah dihitung dari lebar dan tinggi kotak YOLO. Tahap kematangan ditentukan dengan algoritma GraphCut dan penentuan ambang warna pada bagian yang terlihat, dan peta sebaran 2D dibentuk dengan transformasi kaku balik.

## Eksperimen dan Hasil
Detektor dilatih paling banyak 45.000 iterasi, dengan model disimpan tiap 100 iterasi pada 1.000 iterasi pertama dan tiap 1.000 iterasi pada 44.000 iterasi sisanya (maksimum 54 model). Model 50%-terlihat konvergen sekitar 20.000 iterasi. Pelacakan dievaluasi dengan galat relatif absolut hitungan (Persamaan 10) per video terhadap hitungan sebenarnya.

| Perbandingan | Hasil |
|---|---|
| Hit rate model 50%-terlihat | 84,98% |
| Hit rate model 100%-terlihat | 67,91% |
| Galat relatif absolut rata-rata, pipeline lengkap | 12% |
| Tanpa praproses citra (kedalaman) | 29% |
| Tanpa transformasi kaku | 25% |

Model 100%-terlihat dinilai overfitting (lebih baik pada data latih, lebih buruk pada data uji), sehingga model 50%-terlihat dipakai untuk pelacakan. Praproses terbaik terjadi pada α = 0. Contoh pada Gambar 8: buah ber-ID 10 hilang karena tertutup daun pada bingkai 117 sampai 154; tanpa praproses fitur, buah itu diberi ID yang salah (23). Alarm palsu umumnya berasal dari buah bergerombol dan daun. Kematangan dibagi menjadi tahap 5 dan 6 dari enam tahap pertumbuhan tomat, dan ukuran tidak dengan sendirinya menunjukkan kematangan. Galat per video hanya tampak pada Gambar 7.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: kerangka dapat dipakai pada jenis buah lain dengan melatih ulang detektor; keluaran fenotipe mencakup hitungan, ukuran, kematangan, dan peta 2D; serta berpotensi dipakai pada operasi robotik.

Keterbatasan yang dinyatakan penulis: galat masih muncul akibat alarm palsu detektor, pencocokan fitur yang tidak akurat, dan citra kabur akibat kesalahan akuisisi; hasil kematangan dipengaruhi variasi iluminasi meskipun di rumah kaca; kotak deteksi bias pada buah yang tertutup atau berkelompok. Penulis menyarankan penambahan data pelatihan.

Menurut pembacaan ringkasan ini, evaluasi hitungan hanya terdiri atas 15 video dari lima baris pada satu rumah kaca dengan satu jenis buah, tanpa pembanding metode lain. Model 100%-terlihat dipilih berdasarkan uji pada citra, dan ambang luring ditentukan melalui penyetelan awal, tanpa uraian pemisahan data penyetelan dari evaluasi. Sistem menghitung hanya baris depan dari satu sisi, sehingga buah pada sisi lain atau baris belakang sengaja dikeluarkan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dengan pelacakan berbasis deteksi: prediksi posisi lewat transformasi kaku dari fitur latar, penugasan berdasarkan jarak, IoU, dan kedalaman, FSM untuk buah hilang, serta penyaringan alarm palsu pada tahap luring. Hitungan dilaporkan sebagai total buah per video, bukan per kelas; tahap kematangan hanya dihitung sebagai ukuran fenotipe individual dan tidak dikaitkan dengan hitungan per kelas. Acuan hitungan berupa hitungan sebenarnya per video (Persamaan 10); cara penghitungan acuan tidak diuraikan pada teks.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: penyaringan berbasis kedalaman untuk memisahkan objek di bidang depan dari latar, penggunaan keadaan "hilang" untuk pengenalan ulang pasca-oklusi, dan penyaringan alarm palsu dengan syarat jumlah kemunculan minimum. Metode ini bergantung pada kontinuitas gerak antarbingkai dan hanya melacak satu sisi baris, sehingga tidak langsung berlaku untuk pencocokan antar-sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `huang2019high`.

Huang dan Lin (2019) mengusulkan kerangka pencacahan buah dari video RGB-D di rumah kaca dengan detektor YOLOv2 dan pelacakan FSM berbasis SfM (aliran optik dan transformasi kaku) serta penyaringan alarm palsu luring. Model 50%-terlihat mencapai hit rate 84,98%, dan galat relatif absolut hitungan rata-rata terendah adalah 12%.

Catatan verifikasi data: hit rate 84,98% dan 67,91% serta galat 12%, 29%, dan 25% tertulis pada bagian Results and Discussion dan Conclusion; jumlah citra pelatihan dan validasi pada Tabel 1; 15 video dari lima baris (tiga rekaman per baris) pada Materials and Methods. Hasil per video (Gambar 7) hanya berupa grafik dan tidak dapat diverifikasi. Rumus pada teks ekstraksi sebagian rusak, dan tidak ada nilai ambang jarak, kultivar, atau jumlah total tomat yang dilaporkan. Makalah merupakan presentasi rapat tanpa penelaahan sejawat formal.
