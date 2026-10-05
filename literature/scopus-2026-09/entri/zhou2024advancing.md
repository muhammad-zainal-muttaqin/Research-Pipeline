# Advancing tracking-by-detection with MultiMap: Towards occlusion-resilient online multiclass strawberry counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2024advancing` |
| Judul asli | Advancing tracking-by-detection with MultiMap: Towards occlusion-resilient online multiclass strawberry counting |
| Penulis | Zhou, Xuehai; Zhang, Yuyang; Jiang, Xintong; Riaz, Kashif; Rosenbaum, Phil; Lefsrud, Mark; Sun, Shangpeng |
| Tahun | 2024 |
| Venue | Expert Systems with Applications |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [zhou2024advancing.pdf](../pdf/zhou2024advancing.pdf)
- DOI resmi: https://doi.org/10.1016/j.eswa.2024.124587

## Gambaran Umum

Makalah ini mengusulkan sistem pencacahan stroberi daring (*online*) per kelas dari video, yaitu kelas matang (*ripe*) dan mentah (*unripe*). Sistem terdiri atas detektor YOLOv5s yang diperkuat modul atensi (*attention*), pelacak berbasis pelacakan-melalui-deteksi (*tracking-by-detection*), dan algoritma baru bernama MultiMap yang mengubah nomor identitas lintasan (*Track ID*) menjadi nomor hitung yang berurutan per kelas. Video diambil dengan ponsel Google Pixel 7 Pro pada gimbal di dua kebun stroberi dalam ruangan di wilayah Greater Montréal, Kanada (Ferme d'Hiver dan Ferme Gush).

Masalah yang ditangani adalah selisih besar antara nomor identitas terbesar pada pelacak bawaan dan jumlah buah sebenarnya. Selisih ini disebut penulis sebagai lompatan ID (*ID jump*). MultiMap hanya menghitung lintasan berstatus terkonfirmasi dan memetakannya ke bilangan urut per kelas.

Hasil utamanya: detektor terbaik (YOLOv5s + ViT dengan 16 kepala atensi) mencapai mAP50 0,929 dan mAP50:95 0,563. Galat relatif rerata (*mean relative error*, MRE) pencacahan total turun dari 209,8% menjadi 6,7% pada DeepSORT, dari 356,5% menjadi 23,8% pada ByteTrack, dan dari 110,2% menjadi 10,0% pada StrongSORT setelah MultiMap ditambahkan. Galat terendah per kelas adalah 8,7% (matang) dan 9,9% (mentah).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Stroberi tumbuh dalam kelompok yang saling menutupi, sehingga oklusi menyulitkan pencacahan akurat untuk prakiraan hasil dan seleksi genotipe. Penulis menyatakan bahwa metode 3D efektif mengatasi oklusi, tetapi data 3D beresolusi tinggi sulit diperoleh pada skala lahan dan menuntut komputasi besar. Metode citra tunggal dinilai kurang tahan terhadap oklusi, dan pada kebun besar sering memerlukan penyambungan banyak foto sehingga kehilangan sifat waktu nyata.

Pelacakan-melalui-deteksi pada video menangkap objek dari banyak sudut seiring gerak kamera. Namun, pelacak lazimnya dirancang untuk merekam lintasan, bukan menghitung. Penulis menyebut metode terdahulu memakai garis silang (*cross-line*) atau jendela tumpang-tindih (*window overlay*) untuk menyaring hitungan, dan tidak ada yang menyediakan pencacahan multikelas maupun evaluasi efisiensi daring.

## Ide Utama

ID lintasan dibuat sebelum lintasan lolos seleksi status. Akibatnya, deteksi palsu dan kegagalan asosiasi sudah menaikkan nomor ID walaupun lintasan itu kemudian dibuang. Nomor ID yang ditampilkan menjadi tidak berurutan (lompatan ID). Penulis membedakan hal ini dari pertukaran ID (*ID switch*), yaitu satu objek keliru dikenali sebagai dua entitas atau dua objek bertukar identitas.

MultiMap menghitung hanya lintasan terkonfirmasi. Sebuah acuan (*reference*) dua lapis menyimpan lintasan terkonfirmasi, dikelompokkan per kelas. Setiap ID terkonfirmasi dipetakan ke bilangan urut berikutnya pada kelasnya. Nomor hitung dan nama kelas ditampilkan di samping kotak pembatas.

## Cara Kerja Langkah demi Langkah

```
  Video --> Detektor (YOLOv5s + atensi) --> Pelacak (DeepSORT /
  ByteTrack / StrongSORT) --> Track ID --> MultiMap --> hitungan per kelas
```

### 1. Akuisisi data

Video validasi diambil di Ferme d'Hiver (30 video; lift platform; kecepatan sekitar 0,8 m/s; rak sepanjang 13,4 m dan tinggi 4,9 m) dan Ferme Gush (10 video; kamera dibawa berjalan; sekitar 0,15 m/s; rak sepanjang 3,0 m dan tinggi 2,9 m). Resolusi 1920 × 1080 pada 30 FPS. Rerata jumlah buah per video adalah 49 matang dan 139 mentah di Ferme d'Hiver, serta 28 matang dan 86 mentah di Ferme Gush. Durasi per video rata-rata 30 detik (teks juga memuat total durasi 15 menit dan 5 menit pada Tabel 1). Kultivar tidak dilaporkan. Acuan hitung (*ground truth*) adalah rerata hitungan independen dua orang, yang dilakukan terhadap video.

Data pelatihan detektor berupa 440 citra beranotasi dan teraugmentasi dari dataset terbuka. Data validasi detektor terdiri atas 20 citra yang diambil dari video penulis ditambah 80 citra stroberi dari skenario terbuka lain.

### 2. Detektor

Baseline adalah YOLOv5s. Lapisan konvolusi kesembilan (peta fitur 20 × 20 dengan 1.024 kanal) diganti modul ViT atau Swin Transformer dengan beragam jumlah kepala atensi. Modul lain yang dibandingkan adalah CBAM, SA-Net, dan SimAM. Pelatihan memakai optimizer Adam dengan laju belajar awal $10^{-3}$, 300 epoch, ukuran *batch* 16, dan ukuran jendela Swin 8. Ambang keyakinan dan ambang IoU *non-maximum suppression* sama-sama 0,85. Lapisan *Layer Normalization* pada ViT dan Swin dihapus.

### 3. Pelacak

Tiga pelacak dipakai: DeepSORT, ByteTrack, dan StrongSORT. Semuanya memakai filter Kalman untuk prediksi dan algoritma Hungarian (varian Jonker-Volgenant) untuk asosiasi. DeepSORT memadukan jarak Mahalanobis dan jarak kosinus fitur penampilan. Setelah asosiasi pertama, pencocokan IoU memberi kesempatan kedua. Status lintasan berubah dari *Tentative* ke *Confirmed* setelah $n$ keberhasilan berturut-turut, dan ke *Deleted* setelah $m$ kegagalan berturut-turut. Nilai yang dipakai: $n=3$, $m=15$, ambang IoU pelacakan 0,7.

### 4. MultiMap

MultiMap memproses himpunan lintasan terkonfirmasi. Untuk tiap lintasan, bila ID belum ada di peta kelasnya, ID itu diberi bilangan urut maksimum sebelumnya ditambah satu; bila kelas belum ada, peta kelas dibuat dan ID pertama diberi nomor 1. Agar acuan tidak membesar pada ribuan objek, penulis menambahkan ambang $s$: objek yang bertahan di acuan melebihi $s$ bingkai dipangkas. Nilai $s$ tidak dilaporkan pada teks yang dibaca.

## Eksperimen dan Hasil

Perangkat keras: GPU GeForce RTX 3060 12 GB dan CPU Intel Core i7-12700KF. Metrik detektor: mAP, memori GPU, dan durasi pelatihan. Metrik pencacahan: $R^2_{adj}$, RMSE, MAE, MRE, dan FPS rerata.

Tabel detektor (Tabel 2, ukuran *batch* 16; hanya baris terpilih):

| Model | Kepala atensi | Memori | mAP50 | mAP50:95 |
|---|---|---|---|---|
| YOLOv5s | tidak ada | 4,69 G | 0,836 | 0,459 |
| + CBAM | tidak ada | 4,19 G | 0,899 | 0,545 |
| + SA-Net | tidak ada | 4,34 G | 0,917 | 0,559 |
| + SimAM | tidak ada | 4,67 G | 0,854 | 0,476 |
| + ViT | 16 | 4,97 G | 0,929 | 0,563 |
| + Swin | 16 | 4,75 G | 0,904 | 0,560 |
| + Swin | 32 | 4,95 G | 0,880 | 0,536 |

Tabel pencacahan total (Tabel 3, 30 video Ferme d'Hiver; pelacak bawaan memakai ID terbesar sebagai hasil hitung):

| Metode | FPS | $R^2_{adj}$ | RMSE | MAE | MRE (%) |
|---|---|---|---|---|---|
| DeepSORT | 23,7 | 0,61 | 458,1 | 394,7 | 209,8 |
| DeepSORT + MultiMap | 22,3 | 0,95 | 17,8 | 12,9 | 6,7 |
| ByteTrack | 39,8 | 0,59 | 865,8 | 699,9 | 356,5 |
| ByteTrack + MultiMap | 37,2 | 0,88 | 51,3 | 43,2 | 23,8 |
| StrongSORT | 26,4 | 0,77 | 214,2 | 201,0 | 110,2 |
| StrongSORT + MultiMap | 25,8 | 0,99 | 18,8 | 17,4 | 10,0 |

Tabel per kelas (Tabel 4, 40 video dari dua kebun):

| Metode | Kelas | $R^2_{adj}$ | RMSE | MAE | MRE (%) |
|---|---|---|---|---|---|
| DeepSORT + MultiMap | Matang | 0,94 | 5,9 | 4,4 | 8,7 |
| DeepSORT + MultiMap | Mentah | 0,94 | 16,1 | 12,4 | 10,4 |
| StrongSORT + MultiMap | Matang | 0,97 | 5,8 | 4,9 | 9,9 |
| StrongSORT + MultiMap | Mentah | 0,99 | 13,0 | 11,5 | 9,9 |

Penulis menyatakan bahwa DeepSORT menghasilkan galat terendah untuk kelas matang dan StrongSORT untuk kelas mentah, tetapi sebaran titik DeepSORT lebih besar (nilai $R^2_{adj}$ lebih rendah). ByteTrack tanpa penyetelan parameter memberi hasil hitung kurang baik, tetapi tercepat. Kecepatan akhir setelah MultiMap: 22 FPS (DeepSORT), 25 FPS (StrongSORT), dan 37 FPS (ByteTrack).

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: masukan cukup berupa video ponsel; hitungan per kelas; beban komputasi tambahan MultiMap minimal sehingga tetap waktu nyata; hitungan ditampilkan di samping kotak pembatas agar dapat diverifikasi pengguna.

Keterbatasan yang dinyatakan penulis: pertukaran ID tetap menjadi sumber galat utama; kecepatan awal filter Kalman belum diinisialisasi; ekstraktor fitur ReID masih bawaan, bukan khusus stroberi; ponsel menimbulkan guncangan dan pengaburan fokus sehingga video dari UAV mungkin lebih stabil; validasi hanya pada dua kebun milik penulis; baris target dan non-target belum dibedakan.

Menurut pembacaan ringkasan ini, acuan hitung berasal dari hitungan manual dua orang atas video, bukan dari panen, dan teks tidak melaporkan galat antar-penghitung. Menurut pembacaan ringkasan ini, MultiMap tidak mengoreksi pertukaran ID yang memecah satu buah menjadi dua hitungan, sehingga galat tetap bergantung pada pelacak. Menurut pembacaan ringkasan ini, kelas hanya dua (matang dan mentah), dan pengujian dilakukan pada lingkungan dalam ruangan dengan kamera yang bergerak lurus di sepanjang rak.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat pada banyak bingkai dengan mekanisme pelacakan-melalui-deteksi: identitas dipertahankan antarbingkai oleh asosiasi filter Kalman, algoritma Hungarian, dan fitur penampilan. Kontribusi khusus MultiMap adalah memisahkan identitas pelacak dari nomor hitung, yaitu hanya lintasan terkonfirmasi yang dihitung dan dinomori per kelas. Pandangan berbeda berasal dari gerak kamera dalam satu video kontinu, bukan dari beberapa sisi pohon yang diambil terpisah.

Hitungan dilaporkan per kelas (matang dan mentah) dengan galat per kelas pada Tabel 4. Acuan hitungnya adalah hitungan manual dua orang atas video, bukan panen dan bukan anotasi citra. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pemisahan ID pelacak dari nomor hitung serta penomoran per kelas dari lintasan terkonfirmasi. Mekanisme ini mengandaikan aliran video kontinu, sehingga tidak langsung berlaku untuk citra dari sisi pohon yang terpisah tanpa urutan temporal. Makalah tidak menangani pencocokan identitas antarsisi pohon.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zhou2024advancing`.

Ringkasan yang aman dikutip: Zhou dkk. (2024) mengusulkan MultiMap, algoritma pemetaan yang mengubah ID lintasan pada pelacak DeepSORT, ByteTrack, dan StrongSORT menjadi hitungan berurutan per kelas, dan mengujinya pada video stroberi matang dan mentah dari dua kebun dalam ruangan. Galat relatif rerata pencacahan total turun dari 209,8% menjadi 6,7% (DeepSORT), dari 356,5% menjadi 23,8% (ByteTrack), dan dari 110,2% menjadi 10,0% (StrongSORT), sementara galat per kelas terendah adalah 8,7% untuk buah matang dan 9,9% untuk buah mentah.

Catatan verifikasi data: Angka detektor terdapat di Tabel 2 dan Bagian 3.2. Angka pencacahan total terdapat di Tabel 3 (30 video Ferme d'Hiver) dan angka per kelas di Tabel 4 (40 video). Deskripsi dataset terdapat di Tabel 1 dan Bagian 2.1. Teks ekstraksi memuat dua nilai untuk MRE StrongSORT bawaan (110,1% pada kalimat Bagian 3.3 dan 110,2% pada Tabel 3 serta Kesimpulan); entri ini memakai 110,2%. Sel yang dicetak tebal pada tabel asli tidak terbedakan pada teks ekstraksi. Teks juga menyebut durasi rata-rata 30 detik per video sekaligus total 15 menit dan 5 menit pada Tabel 1; keduanya dicatat sebagaimana tertulis. Jumlah buah sebenarnya per video dan nilai ambang $s$ tidak dilaporkan pada teks. Data dinyatakan tersedia atas permintaan, dan kode terbuka di repositori MultiMap.
