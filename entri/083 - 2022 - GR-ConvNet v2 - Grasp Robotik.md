# 083 - GR-ConvNet v2: A Real-Time Multi-Grasp Detection Network for Robotic Grasping

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kumra2022grconvnetv2` |
| Judul asli | GR-ConvNet v2: A Real-Time Multi-Grasp Detection Network for Robotic Grasping |
| Penulis | Sulabh Kumra, Shirin Joshi, Ferat Sahin |
| Tahun | 2022 |
| Venue | Sensors (MDPI), vol. 22, no. 16, artikel 6208 |
| Tema | Grasp Robotik |

## Tautan Akses
- **DOI (penerbit, akses terbuka):** https://doi.org/10.3390/s22166208
- **PubMed Central (HTML/PDF gratis):** https://pmc.ncbi.nlm.nih.gov/articles/PMC9415764/
- **Google Scholar:** https://scholar.google.com/scholar?q=GR-ConvNet%20v2%3A%20A%20Real-Time%20Multi-Grasp%20Detection%20Network%20for%20Robotic%20Grasping
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=GR-ConvNet%20v2%3A%20A%20Real-Time%20Multi-Grasp%20Detection%20Network%20for%20Robotic%20Grasping&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan GR-ConvNet v2, jaringan konvolusi untuk *grasp detection* — tugas memprediksi cara sebuah lengan robot mencengkeram objek secara stabil dari citra. Keluarannya bukan kotak deteksi objek, melainkan *grasp rectangle*: kotak berorientasi yang menyatakan di mana penjepit dua-jari harus turun, pada sudut berapa, dan seberapa lebar bukaannya. GR-ConvNet v2 memetakan citra masukan RGB-D (warna tiga kanal ditambah satu kanal kedalaman) langsung ke empat peta per-piksel yang bersama-sama mendefinisikan cengkeraman terbaik pada setiap titik gambar, dalam satu evaluasi jaringan.

Model ini adalah penyempurnaan langsung atas GR-ConvNet (bab 082). Perubahannya bersifat teknis dan terukur: fungsi aktivasi, regularisasi, dan resep pelatihan diganti, sementara struktur *encoder–decoder* dipertahankan. Hasilnya, akurasi deteksi *grasp* mencapai 98,8% pada pembagian *image-wise* dan 97,7% pada pembagian *object-wise* dataset Cornell, serta 95,1% pada dataset Jacquard, dengan waktu inferensi sekitar 20 milidetik per citra. Ketika bobot yang telah dilatih dipindahkan langsung ke lengan robot 7 DoF (tujuh derajat kebebasan), tingkat keberhasilan cengkeraman mencapai 95,4% pada objek rumah tangga dan 93,0% pada objek bergeometri sulit yang belum pernah dilihat model.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pendekatan awal *grasp detection* berbasis pembelajaran, seperti Lenz dkk. (bab 080), memakai skema *sliding window*: banyak kandidat kotak cengkeraman dievaluasi satu per satu oleh pengklasifikasi, sehingga lambat — orde detik per citra. GG-CNN (bab 081) mengganti skema itu dengan prediksi per-piksel: satu jaringan konvolusi kecil menghasilkan peta kualitas cengkeraman untuk seluruh citra sekaligus, cukup cepat untuk kendali *closed-loop* (kendali berumpan-balik yang memperbarui target cengkeraman secara terus-menerus). GR-ConvNet v1 (bab 082) memperdalam gagasan itu dengan blok residual dan masukan RGB-D, menaikkan akurasi Cornell ke kisaran atas.

Dua kekurangan tetap tersisa. Pertama, meskipun peta per-piksel secara prinsip memuat banyak cengkeraman, evaluasi standar berhenti pada satu *grasp* terbaik per citra, sehingga kemampuan *multi-grasp* — memilih beberapa cengkeraman valid untuk beberapa objek sekaligus — tidak tergarap. Kedua, metrik akurasi *grasp* yang lazim, ambang IOU 25% dengan selisih sudut di bawah 30°, tergolong longgar; model dapat mencetak angka tinggi tanpa benar-benar presisi. Perbaikan lanjutan karena itu bukan soal arsitektur baru, melainkan menaikkan kualitas prediksi pada rangka kerja generatif yang sama sambil mempertahankan kecepatan.

## Ide Utama

Gagasan inti tidak berubah dari pendahulunya: cengkeraman diperlakukan sebagai regresi per-piksel. Alih-alih mengusulkan lalu memeringkat kandidat, jaringan menghasilkan empat citra keluaran seukuran masukan. Peta pertama, Q, memberi setiap piksel skor kualitas cengkeraman antara 0 dan 1. Dua peta berikutnya menyatakan sudut cengkeraman Θ dalam bentuk cos2Θ dan sin2Θ. Peta keempat, W, menyatakan lebar bukaan penjepit. Cengkeraman terbaik dibaca dari piksel dengan skor Q tertinggi; sudut dan lebar diambil dari peta lain pada piksel yang sama.

Penyandian sudut sebagai pasangan cos2Θ dan sin2Θ menyelesaikan satu masalah spesifik: cengkeraman *antipodal* (dua jari berlawanan arah) tidak berubah bila diputar 180°, sehingga sudut 10° dan 190° setara. Memakai sudut ganda (2Θ) memetakan rentang efektif [−90°, 90°] ke satu lingkaran penuh tanpa lompatan nilai, sehingga jaringan tidak perlu belajar diskontinuitas buatan. Untuk *multi-grasp*, prediksi tidak dibatasi ke satu puncak: seluruh puncak lokal pada peta Q dibaca, masing-masing menghasilkan satu *grasp rectangle*, sehingga beberapa objek atau beberapa titik cengkeram pada satu objek dapat dilayani serentak.

## Cara Kerja Langkah demi Langkah

### Masukan dan Representasi Cengkeraman

Masukan adalah citra *n*-kanal berukuran 224×224 piksel. Konfigurasi utama memakai empat kanal (RGB-D): tiga kanal warna dan satu kanal kedalaman yang telah di-*inpaint* (lubang pengukuran diisi) serta dinormalisasi. Setiap *grasp rectangle* keluaran dinyatakan lima parameter: koordinat pusat (x, y), sudut orientasi Θ, lebar bukaan W, dan tinggi (panjang jari penjepit) yang diperlakukan sebagai konstanta. Representasi lima parameter ini adalah bentuk baku sejak Lenz dkk. dan menjadi target yang diprediksi jaringan.

### Arsitektur Encoder–Decoder Residual

Jaringan berbentuk *encoder–decoder* dengan jembatan residual. Alur data dari citra masukan ke empat peta keluaran:

```
masukan RGB-D                         empat peta keluaran 224x224
 224 x 224 x 4                        ┌─ Q      (kualitas cengkeraman)
      │                               ├─ cos2Θ  (komponen sudut)
      ▼                               ├─ sin2Θ  (komponen sudut)
 [3 konvolusi]   encoder: perkecil    └─ W      (lebar bukaan)
      │          resolusi, perbanyak         ▲
      ▼          kanal fitur                 │
 [5 blok residual]  proses fitur       [3 konvolusi transpos]
      │             tanpa mengubah           ▲   decoder: perbesar
      └──────────── ukuran ────────────────► │   resolusi kembali
```

*Encoder* memakai tiga lapis konvolusi yang menurunkan resolusi spasial sambil menaikkan jumlah kanal fitur. Bagian tengah berisi lima *blok residual* — blok yang menambahkan masukannya sendiri ke keluaran (*skip connection*), sehingga jaringan dalam tetap dapat dilatih tanpa gradien mengecil. *Decoder* memakai tiga lapis konvolusi transpos (*transposed convolution*, operasi yang menaikkan resolusi) untuk mengembalikan peta ke ukuran 224×224. Dengan lebar kanal dasar k = 32 dan masukan empat kanal, seluruh jaringan hanya memuat sekitar 1,9 juta parameter — ringan dibandingkan detektor objek umum yang berukuran puluhan juta parameter, dan itulah dasar kecepatan 20 milidetik.

### Perubahan atas GR-ConvNet v1

Empat perubahan membedakan v2 dari v1. Pertama, fungsi aktivasi ReLU diganti Mish di seluruh jaringan; Mish adalah fungsi aktivasi mulus (*smooth*) yang membiarkan sedikit gradien negatif lewat, sehingga pelatihan cenderung lebih stabil. Kedua, ditambahkan lapis *dropout* — penonaktifan acak sebagian neuron saat pelatihan, dengan laju optimal 10% — setelah tiap keluaran sebagai regularisasi terhadap *overfitting*. Ketiga, pengoptimal Adam diganti Ranger, gabungan RAdam dan *lookahead* yang menstabilkan langkah pembaruan bobot. Keempat, jadwal laju belajar *fixed* diganti *Flat + Cosine annealing*: laju ditahan konstan pada 10⁻⁴ lalu diturunkan mengikuti kurva kosinus sampai 10⁻⁷. Struktur *encoder–decoder* itu sendiri tidak diubah.

### Fungsi Loss dan Pelatihan

Pelatihan meminimalkan *smooth L1 loss* (juga disebut *Huber loss*) — fungsi galat yang bersifat kuadratik untuk selisih kecil dan linear untuk selisih besar, sehingga tidak terlalu peka terhadap *outlier*. Loss total adalah jumlah galat keempat keluaran: L = L_quality + L_cos + L_sin + L_width. Dataset Cornell yang kecil diperbesar lewat augmentasi (pemotongan, penyekalaan, dan rotasi acak) menjadi sekitar 51 ribu contoh agar cukup untuk melatih jaringan tanpa *overfitting*. Ukuran *batch* yang diuji adalah 8 dan 16.

### Inferensi dan Multi-Grasp

Saat inferensi, satu lintasan menghasilkan keempat peta. Untuk mode *single-grasp*, piksel dengan Q maksimum dipilih; koordinatnya menjadi pusat cengkeraman, dan sudut serta lebar dibaca dari peta cos2Θ/sin2Θ dan W pada piksel itu. Untuk mode *multi-grasp*, seluruh puncak lokal pada peta Q diambil sekaligus, masing-masing menjadi satu *grasp rectangle*. Karena penyaringan puncak dan pembacaan peta jauh lebih murah daripada lintasan jaringan, penambahan ini tidak menaikkan waktu inferensi secara berarti.

## Eksperimen dan Hasil

Evaluasi utama memakai dua dataset. Cornell Grasp Dataset adalah himpunan kecil klasik dengan dua protokol pembagian: *image-wise* (citra acak dibagi latih/uji) dan *object-wise* (objek yang berbeda dipisah, menguji generalisasi ke benda baru). Jacquard adalah dataset sintetis berskala jauh lebih besar. Metrik keberhasilan adalah *rectangle metric*: sebuah prediksi dianggap benar bila IOU (*Intersection over Union*, rasio irisan terhadap gabungan) dengan kotak kebenaran melampaui 25% dan selisih sudutnya di bawah 30°.

GR-ConvNet v2 mencapai 98,8% (*image-wise*) dan 97,7% (*object-wise*) pada Cornell, serta 95,1% pada Jacquard. Interpretasinya: selisih tipis antara *image-wise* dan *object-wise* menunjukkan model tidak sekadar menghafal objek latih, melainkan menggeneralisasi ke bentuk baru. Pada Jacquard, makalah juga melaporkan 91,4% di bawah metrik SGT yang lebih ketat, menegaskan bahwa angka tinggi bertahan saat kriteria diperketat.

Pengujian robot memindahkan bobot terlatih langsung ke lengan 7 DoF tanpa pelatihan ulang. Tingkat keberhasilan cengkeraman: 95,4% pada objek rumah tangga terisolasi, 93,0% pada objek adversarial (bergeometri menyulitkan) terisolasi, 93,5% pada tumpukan objek rumah tangga, dan 91,0% pada tumpukan objek adversarial. Penurunan dari kondisi terisolasi ke tumpukan (*clutter*) kecil, yang konsisten dengan kemampuan *multi-grasp* menangani beberapa objek berhimpitan.

## Kelebihan dan Keterbatasan

Kelebihan: inferensi 20 milidetik memungkinkan kendali *closed-loop*; jaringan hanya 1,9 juta parameter, ringan untuk perangkat terbatas; transfer sim-ke-nyata berjalan tanpa penalaan ulang; dan mode *multi-grasp* menangani adegan berhimpitan. Peningkatan atas v1 dicapai lewat pergantian komponen pelatihan, bukan penambahan biaya arsitektur.

Keterbatasan: cengkeraman yang diprediksi bersifat planar — kotak berorientasi pada bidang citra — bukan *6-DoF* penuh di ruang tiga dimensi, sehingga pendekatan pengambilan terbatas pada arah vertikal terhadap permukaan kerja. Secara konseptual, ketergantungan pada kanal kedalaman membuat kinerja rentan terhadap kualitas sensor RGB-D pada objek transparan atau mengkilap. Dari sisi rekayasa, kenaikan akurasi atas v1 tergolong inkremental; kontribusi terbesar makalah adalah resep pelatihan yang lebih matang dan protokol evaluasi *multi-grasp* yang lebih realistis, bukan paradigma baru.

## Kaitan dengan Bab Lain

GR-ConvNet v2 adalah iterasi langsung atas [GR-ConvNet (bab 082)](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md), mewarisi struktur *encoder–decoder* residual dan masukan RGB-D-nya, lalu mengganti aktivasi, regularisasi, dan pengoptimal. Prinsip peta cengkeraman per-piksel yang mendasari keduanya berasal dari [GG-CNN (bab 081)](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md), yang pertama mengganti pendekatan *sliding window* dari [Lenz dkk. (bab 080)](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md) dengan regresi generatif. Evaluasi v2 memakai [dataset Jacquard (bab 086)](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md) sebagai tolok ukur berskala besar. Batas planar yang tersisa pada seluruh garis keturunan ini menjadi motivasi jalur *6-DoF*, yang digarap [GraspNet-1Billion (bab 084)](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md), serta fusi lintas-modal yang lebih dalam pada [BCMFNet (bab 085)](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md).

## Poin untuk Sitasi

Kutip dengan kunci `kumra2022grconvnetv2`. Ringkasan yang aman dikutip: "GR-ConvNet v2 menyempurnakan GR-ConvNet dengan aktivasi Mish, dropout, dan pengoptimal Ranger, mencapai 98,8% (*image-wise*) dan 97,7% (*object-wise*) pada Cornell serta 95,1% pada Jacquard dengan inferensi ±20 ms, dan mendukung deteksi *multi-grasp* melalui pembacaan puncak lokal pada peta kualitas." Angka akurasi Cornell/Jacquard, waktu 20 ms, jumlah parameter 1,9 juta, dan tingkat keberhasilan robot (95,4% / 93,0% / 93,5% / 91,0%) diverifikasi dari versi PMC makalah dan sebaiknya dicocokkan ulang ke tabel naskah asli sebelum sitasi formal. Belum terverifikasi dari sumber primer pada sesi ini: rincian metrik SGT (definisi dan pembanding), angka pembanding GR-ConvNet v1 pada tabel yang sama, model spesifik lengan robot 7 DoF, dan uraian kanal masukan alternatif (RGB saja / kedalaman saja) beserta akurasinya — semuanya perlu diperiksa langsung ke naskah.
