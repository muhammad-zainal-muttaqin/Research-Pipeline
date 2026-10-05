# Semantic NeRF-Oriented 3-D Object Counting for Industrial Fruit Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2026semantic` |
| Judul asli | Semantic NeRF-Oriented 3-D Object Counting for Industrial Fruit Harvesting |
| Penulis | Wang, Yimo; Kang, Bin; Liu, Jian; Sun, Changyin |
| Tahun | 2026 |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [wang2026semantic.pdf](../pdf/wang2026semantic.pdf)
- DOI resmi: https://doi.org/10.1109/tase.2026.3700861

## Gambaran Umum

Makalah ini mengusulkan kerangka penghitungan objek 3D untuk buah yang menggabungkan *Neural Radiance Field* (NeRF) semantik dengan algoritme klasterisasi awan titik adaptif berpemandu fisika (*physics-guided adaptive clustering*). Tujuannya mengatasi penghitungan ganda (*double counting*) yang muncul ketika pengamatan dari banyak pandangan citra digabungkan tanpa pengetahuan spasial. Citra multi-pandang diolah melalui *structure-from-motion* (SfM) untuk memperoleh pose kamera, lalu NeRF semantik direkonstruksi dan titik hanya buah diekstraksi, dan klasterisasi berbasis kepadatan titik, vektor normal permukaan, dan gradien elevasi memisahkan setiap buah untuk dihitung.

Evaluasi memakai data sintetis (Blender, delapan jenis buah) dan data nyata dari tolok ukur FruitNeRF (tiga pohon apel), ditambah Fuji-SfM (11 pohon apel Fuji, 582 citra). Pembanding adalah metode 2D berbasis kepadatan dan deteksi serta FruitNeRF sebagai metode penghitungan 3D mutakhir. Hasil yang dilaporkan: Acc 0,996 (sintetis), 0,979 (nyata), dan 0,916 (Fuji), dengan peningkatan akurasi rata-rata 9,0 poin persentase (pp) terhadap FruitNeRF, yaitu 6,9 pp pada sintetis, 7,2 pp pada nyata, dan 12,9 pp pada Fuji.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penghitungan buah mendukung estimasi hasil dan perencanaan panen robotik, tetapi buah tumbuh bergerombol sehingga oklusi parah menyamarkan batas antarbuah. Metode 2D berbasis warna atau tepi dinilai gagal pada adegan seperti itu. Metode penghitungan multi-pandang berbasis pembelajaran mendalam mengalami penghitungan berulang saat menggabungkan pengamatan antar-pandangan. Penulis menyebut dua penyebabnya: ketidakmampuan membedakan instans pada area tumpang-tindih dan tidak adanya pelacakan identitas yang konsisten antar-pandangan.

Rekonstruksi 3D dianggap menjanjikan, tetapi titik awan dari NeRF belum menyelesaikan masalah karena algoritme klasterisasi yang ada (DBSCAN, klasterisasi Euklides) bergantung pada penyetelan hiperparameter dan sulit menangani morfologi tidak beraturan. Metode berbasis jarak sulit memisahkan area cekung pada buah yang berdekatan, metode berbasis kepadatan keliru pada titik periferal yang jarang, dan metode terawasi memerlukan data berlabel banyak. Penulis juga menyatakan bahwa kebanyakan metode mengabaikan petunjuk geometris seperti normal permukaan dan gradien elevasi.

## Ide Utama

Masalah penghitungan multi-pandang dirumuskan ulang di ranah 3D sehingga identitas buah ditentukan oleh kedudukan di ruang dunia, bukan oleh pencocokan antar-citra. Dengan begitu penghitungan ganda dihilangkan oleh konstruksi. Bagian novel menurut penulis adalah formulasi NeRF semantik terpisah-instans (*instance-decoupled*) dan klasterisasi berpemandu fisika. Modul SfM, tulang punggung Nerfacto, dan prior segmentasi (Grounded-SAM atau U-Net) dipakai tanpa modifikasi.

Gagasan klasterisasi: pada titik kontak dua buah cembung kepadatan titik tetap tinggi sehingga jarak dan kepadatan tidak dapat memisahkannya, tetapi arah normal berubah tajam di lipatan kontak, dan profil elevasi tidak kontinu di sambungan buah yang bertumpuk. Kedua petunjuk itu dipakai untuk menekan ambang klaster tepat di batas antarbuah.

## Cara Kerja Langkah demi Langkah

```
 citra multi-pandang --> SfM (pose kamera) --> NeRF semantik (+ masker buah)
        --> ekstraksi titik buah (ray-marching ortografik, enam pandangan)
        --> praproses (voxel, buang pencilan)
        --> klasterisasi adaptif (representatif + ambang dinamis)
        --> volume convex hull per klaster --> hitungan buah
```

### 1. Akuisisi data

Data sintetis dibuat dengan Blender dan plugin BlenderNeRF, berisi delapan jenis buah (apel, plum, lemon, pir, persik, mangga, stroberi, blueberry). Setiap pohon diwakili 300 citra berukuran 1024 × 1024 piksel. Kerapatan buah dikontrol pada tiga tingkat berdasarkan jarak antarbuah: jarang (lebih dari 5 cm), sedang (2 sampai 5 cm), dan padat (kurang dari 2 cm). Hitungan acuan diambil langsung dari graf adegan. Data nyata terdiri dari tiga pohon apel FruitNeRF (sekitar 350 citra per pohon, 1000 × 1500 piksel, Nikon D7100, lensa 35 mm) dengan hitungan acuan 179, 113, dan 291 dari hitung manual di lokasi. Fuji-SfM berisi 11 pohon apel Fuji dalam satu barisan dengan 582 citra dan anotasi 3D per buah. Data kelapa sawit tidak dipakai.

### 2. SfM dan NeRF semantik

SfM mengestimasi parameter kamera dan struktur 3D lewat *bundle adjustment*. NeRF memiliki tiga medan: medan kepadatan, medan tampilan (bergantung arah pandang), dan medan semantik (bergantung hanya pada posisi). Gradien kerugian semantik hanya dialirkan melalui medan semantik agar kepadatan tidak runtuh pada permukaan buah saja. Kerugian total adalah jumlah kerugian fotometrik (MSE) dan kerugian semantik (*binary cross-entropy*, BCE). Dua strategi segmentasi dibandingkan (Grounded-SAM dengan perintah "fruit" dan U-Net terlatih pada data beranotasi), serta dua kapasitas NeRF (kecil: 2 lapisan, 64 unit; besar: 3 lapisan, 128 unit).

### 3. Ekstraksi awan titik

Titik diambil dengan *ray-marching* ortografik dari enam pandangan. Titik dipertahankan bila kepadatan melebihi $\tau_\sigma$ dan probabilitas semantik melebihi $\tau_s$ (nilai tetap $\tau_\sigma = 0{,}01$ dan $\tau_s = 0{,}5$).

### 4. Praproses

Penurunan resolusi dengan filter voxel berukuran $v = 0{,}01$ m, lalu pembuangan pencilan statistik ($k = 20$, pengali 2,0).

### 5. Klasterisasi adaptif

Tahap pertama memilih representatif otomatis dengan meminimalkan fungsi energi $E = \sum_i \min_j d(p'_i, r_j) + \lambda K$, melalui penggabungan dari bawah ke atas. $\lambda$ diinisialisasi sebagai median jarak tetangga terdekat dan digandakan setiap iterasi hingga $|\Delta E| < 10^{-4}$. Tahap kedua menetapkan setiap titik ke representatif terdekat melalui pencarian *depth-first* (DFS) dengan ambang dinamis $\theta = \alpha \cdot \delta \cdot \frac{|p'_{i,z} - p'_{j,z}|}{\|p'_i - p'_j\|} \cdot \arccos(\kappa(n_i \cdot n_j))$, dengan $\alpha = 0{,}5$, $\delta$ kepadatan lokal, dan normal $n$ diestimasi dengan PCA (radius 0,05 m, 8 tetangga). Tahap ketiga menyempurnakan batas klaster dengan penugasan ulang label dominan lingkungan.

### 6. Penghitungan

Volume *convex hull* tiap klaster dihitung, dan volume acuan $V_{ref}$ adalah median volume klaster. Hitungan klaster adalah 1 bila $0{,}9 V_{ref} \le V_j \le 1{,}1 V_{ref}$, $\lfloor V_j / V_{ref} \rceil$ bila $V_j > 1{,}1 V_{ref}$ (klaster gabungan), dan 0 bila $V_j < 0{,}9 V_{ref}$ (serpihan derau). Hitungan total adalah jumlahnya. Perangkat: NVIDIA RTX 3090, AMD Ryzen 9 5950X, Ubuntu 22.04, CUDA 11.8.

## Eksperimen dan Hasil

Metrik: Acc ($1 - |N_{pred} - N_{gt}|/N_{gt}$, tingkat adegan), *recall* dan F1 (pencocokan tingkat instans), MAE, dan RMSE. Pembanding: berbasis kepadatan (GMN, FamNet, CounTR), berbasis deteksi (FR, FSOD, PseCo), dan FruitNeRF (3D). Untuk pembanding 2D, kolom pertama berisi presisi dari makalah asli karena akurasi tingkat adegan tidak tersedia. Hiperparameter yang sama dipakai pada semua dataset.

Tabel II makalah tidak terbaca pada teks ekstraksi, sehingga angka berikut diambil dari narasi seksi IV-C:

| Dataset | Metode | Acc | F1 | MAE | RMSE |
|---|---|---|---|---|---|
| Sintetis | FruitNeRF | 0,927 (dari kesimpulan) | 0,750 | 15,75 | 31,42 |
| Sintetis | Metode ini | 0,996 | 0,977 | 13,26 | 25,38 |
| Nyata (3 pohon apel) | FruitNeRF | tidak terbaca | 0,783 | 16,94 | 25,87 |
| Nyata (3 pohon apel) | Metode ini | 0,979 | 0,960 | 14,15 | 19,33 |
| Fuji-SfM | FruitNeRF | tidak terbaca | 0,760 | 20,86 | 47,36 |
| Fuji-SfM | Metode ini | 0,916 | 0,840 | 16,14 | 34,84 |

Selisih Acc terhadap FruitNeRF dinyatakan makalah sebesar 6,9 pp (sintetis), 7,2 pp (nyata), dan 12,9 pp (Fuji). Uji peringkat bertanda Wilcoxon berpasangan pada MAE per pohon (tiga pohon nyata ditambah 11 pohon Fuji, $n = 14$) menunjukkan seluruh 14 selisih menguntungkan metode ini ($W^+ = 105$, $p < 0{,}001$). Di antara pembanding 2D, CounTR memiliki F1 0,818 dan MAE 18,74 pada sintetis, F1 0,833 dan MAE 19,27 pada data nyata, serta F1 0,721 pada Fuji.

Ablasi dan analisis lain (angka tabel tidak terbaca, hanya narasi): pada mangga, NeRF besar dengan U-Net mencapai F1 0,95 dan MAE 13,0, dibanding NeRF kecil dengan U-Net F1 0,93 dan MAE 14,0; pada pir, NeRF besar dengan U-Net F1 0,96 dan MAE 12,3 dibanding NeRF besar dengan SAM F1 0,90 dan MAE 16,5; IoU segmentasi mangga 0,60 (U-Net) dibanding 0,52 (SAM). Pada ablasi $\lambda$, F1 di atas 0,95 untuk $\beta$ antara 0,80 dan 1,00 pada data sintetis dan nyata, dan puncak pada $\beta = 1{,}0$ (F1 0,977 sintetis, 0,960 nyata); pada Fuji F1 optimal 0,931 dicapai pada $\beta = 0{,}80$, dibanding 0,840 pada $\beta = 1{,}0$. Pada kerapatan padat, F1 FruitNeRF turun menjadi 0,643 sedangkan metode ini 0,966. Waktu: pelatihan NeRF mendominasi lebih dari 95% total, dan tahap pasca-NeRF adalah 72 ± 3 detik dibanding 73 ± 3 detik untuk FruitNeRF.

## Kelebihan dan Keterbatasan

Keterbatasan yang dinyatakan penulis: beban komputasi rekonstruksi NeRF yang menjadikan alur kerja bersifat luring (pra-panen, dengan alur tepi-awan); pengambilan citra harus mencakup orbit hemisferik yang memadai (kegagalan pada Pohon 3 Fuji-SfM karena lintasan linear terbatas); buah yang sepenuhnya tertutup di dalam gerombol, seperti buah beri bagian dalam tandan anggur atau blueberry padat, berada di luar cakupan; asumsi kekakuan adegan dilanggar oleh gerakan angin. Penulis menyatakan kerangka berlaku pada buah yang kira-kira cembung dan setidaknya sebagian terlihat dari lintasan kamera.

Menurut pembacaan ringkasan ini, evaluasi data nyata hanya mencakup tiga pohon apel FruitNeRF dan 11 pohon Fuji dari satu barisan, sehingga generalisasi ke tanaman dengan tandan padat belum diuji. Angka pada tabel utama berpotensi dipengaruhi oleh pengaturan tetap (misalnya $\alpha$ dan ambang volume 0,9 serta 1,1) yang diklaim tanpa penyetelan per dataset tetapi tidak dibandingkan dengan sistem lain pada kondisi yang sama. Pada Fuji, penulis sendiri mencatat kecenderungan segmentasi berlebih (*recall* 0,970 dengan F1 0,840). Aturan penghitungan klaster gabungan mengasumsikan buah bervolume serupa, yang tidak berlaku bila ukuran buah dalam satu adegan sangat beragam, seperti buah dengan kematangan atau ukuran campuran.

## Kaitan dengan Tinjauan main6

Makalah ini secara langsung menangani buah yang terlihat lebih dari sekali: penulis menyebut penghitungan ganda multi-pandang sebagai masalah pusat. Mekanismenya adalah rekonstruksi 3D bersama (SfM lalu NeRF semantik) sehingga setiap buah menempati satu posisi di ruang dunia, lalu klasterisasi awan titik dan hitungan klaster. Identitas ditentukan secara geometris, bukan melalui pelacakan atau pencocokan fitur antar-citra. Hitungan tidak dilaporkan per kelas (hanya kelas buah versus latar). Acuan hitung adalah graf adegan (sintetis), hitung manual di lokasi (tiga pohon apel) dan anotasi 3D per buah (Fuji-SfM), bukan panen.

Yang dapat dipindahkan ke tandan sawit multi-sisi adalah gagasan penghitungan di ruang 3D bersama dan pemisahan objek bersentuhan dengan normal permukaan, serta aturan penghitungan klaster gabungan berbasis volume median. Syaratnya adalah cakupan pandang yang cukup di sekeliling objek dan objek yang kira-kira cembung. Penulis menunjukkan bahwa lintasan terbatas dan oklusi permanen merusak hasil, dan kedua kondisi ini relevan pada tandan sawit yang tertanam di antara pelepah. Penghitungan per kelas kematangan belum dilakukan dan harus ditambahkan di luar kerangka ini.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `wang2026semantic`.

Wang dkk. mengusulkan kerangka penghitungan buah 3D yang menggabungkan NeRF semantik dengan klasterisasi awan titik adaptif berbasis kepadatan, normal permukaan, dan gradien elevasi untuk menghilangkan penghitungan ganda antar-pandangan. Pada data sintetis, tiga pohon apel nyata, dan Fuji-SfM, metode ini melaporkan Acc 0,996, 0,979, dan 0,916 serta peningkatan akurasi 6,9, 7,2, dan 12,9 pp terhadap FruitNeRF.

Catatan verifikasi data: Angka Acc, F1, MAE, dan RMSE metode ini serta FruitNeRF berasal dari narasi seksi IV-C (Tabel II); angka sampingan berasal dari seksi IV-D sampai V. Isi Tabel II sampai X tidak terbaca pada teks ekstraksi (tabel berupa gambar), sehingga Acc FruitNeRF pada data nyata dan Fuji, angka pembanding lain, dan data per kerapatan dan pencahayaan tidak dapat diverifikasi. Acc FruitNeRF pada sintetis (0,927) diambil dari kalimat kesimpulan. Lampiran daftar pustaka terpotong dan tidak dipakai. Makalah berbahasa Inggris. Hasil per kelas dan data kelapa sawit tidak dilaporkan.
