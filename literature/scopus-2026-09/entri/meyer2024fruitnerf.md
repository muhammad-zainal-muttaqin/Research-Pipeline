# FruitNeRF: A Unified Neural Radiance Field based Fruit Counting Framework

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `meyer2024fruitnerf` |
| Judul asli | FruitNeRF: A Unified Neural Radiance Field based Fruit Counting Framework |
| Penulis | Meyer, Lukas; Gilson, Andreas; Schmid, Ute; Stamminger, Marc |
| Tahun | 2024 |
| Venue | IEEE International Conference on Intelligent Robots and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, citrus, mango, peach/nectarine, pear, plum/apricot |

## Tautan Akses
- PDF: [meyer2024fruitnerf.pdf](../pdf/meyer2024fruitnerf.pdf)
- DOI resmi: https://doi.org/10.1109/iros58592.2024.10802065

## Gambaran Umum
Makalah ini mengusulkan FruitNeRF, kerangka pencacahan buah yang bekerja langsung di ruang 3D. Masukannya adalah kumpulan citra RGB tak berurutan dari satu kamera monokular dengan pose kamera yang diketahui. Citra disegmentasi menjadi masker buah, lalu sebuah medan pancaran saraf semantik (*semantic neural radiance field*, NeRF) dilatih dari RGB dan masker tersebut. Ruang volume disampel secara seragam untuk memperoleh awan titik yang hanya berisi buah, dan pengklasteran bertingkat pada awan titik itu menghasilkan jumlah buah. Pencacahan dilakukan setelah rekonstruksi 3D, sehingga buah yang tampak pada banyak citra hanya menjadi satu objek 3D.

Evaluasi memakai tiga set data: set data sintetis Blender berisi enam jenis pohon buah (apel, plum, lemon, pir, persik, mangga) dengan 300 citra per pohon, set data nyata berisi tiga pohon apel varietas Resista dengan hitungan manual, dan set data acuan Fuji-SfM (11 pohon dalam satu baris, 582 citra dari kedua sisi pohon). Pada data sintetis, rerata F1 enam jenis buah adalah 0,95 dengan masker acuan dan 0,88 dengan masker Grounded-SAM. Pada set data apel nyata, tingkat deteksi rerata sekitar 89% untuk Pohon 1 dan 2 serta sekitar 82% untuk Pohon 3. Pada Fuji-SfM, FruitNeRF-Big mencapai F1 0,79 (masker SAM) dan 0,78 (masker U-Net), dibandingkan 0,88 pada makalah acuan Fuji.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah untuk estimasi hasil memerlukan deteksi dan pelacakan buah lintas citra, atau kombinasinya dengan awan titik 3D, di tengah oklusi dan variasi cahaya. Penulis menyatakan sumber galat utama adalah penghitungan ganda (buah yang sama pada dua citra berurutan atau buah yang terlihat dari kedua sisi) dan penghitungan buah yang tidak relevan, seperti buah jatuh atau buah dari pohon pada baris belakang. Selain itu, metode yang ada umumnya spesifik pada jenis buah dan lingkungan.

Pendekatan terdahulu yang dirangkum mencakup penghitungan per citra, pelacakan antarbingkai berurutan, pemanfaatan awan titik renggang dari *structure from motion* (SfM) untuk menghitung lokasi buah, dan proyeksi segmentasi instan 2D ke ruang 3D. Menurut penulis, pendekatan itu menggabungkan SfM dengan masker segmentasi 2D, sedangkan FruitNeRF melakukan rekonstruksi semantik terlebih dahulu lalu menghitung di 3D.

## Ide Utama
Buah direpresentasikan sebagai medan semantik di dalam NeRF sehingga satu buah fisik menempati satu daerah dalam volume. Karena semua citra berkontribusi pada medan yang sama, buah yang tampak dari banyak sudut menyatu secara geometris dan tidak perlu dicocokkan antarcitra. Segmentasi memakai model fondasi (Grounded-SAM) sehingga metode tidak bergantung pada jenis buah dan tidak membutuhkan anotasi baru.

```
 Citra tak berurutan -> SfM (COLMAP): pose + intrinsik
        |
 Masker buah (Grounded-SAM atau U-Net)
        |
 FruitNeRF: medan kepadatan + medan tampilan + medan buah
        |
 Sampel volume seragam -> awan titik buah (ambang kepadatan)
        |
 Pembersihan derau -> DBSCAN -> klaster tunggal / ganda / kecil
        |
 Agglomeration + jarak Hausdorff untuk klaster ganda -> jumlah buah
```

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Set data sintetis dibuat di Blender dengan model pohon dari XFrog dan *plugin* BlenderNeRF yang menempatkan kamera virtual pada hemisfer. Panjang fokus 35 mm, ukuran citra 1024 x 1024 piksel, dan 300 citra per pohon, disertai masker semantik acuan.

Set data nyata direkam di Hiltpoltstein Fruit Information Center, Bavaria, Jerman, pada tiga pohon apel varietas Resista. Kamera Nikon D7100 dengan lensa 35 mm menghasilkan citra 4000 x 6000 piksel, sekitar 350 citra per pohon dari jarak 3 m, pada beberapa ketinggian di kedua sisi pohon. Pose dipulihkan dengan COLMAP, dan semua apel setiap pohon dihitung manual sebagai acuan.

### 2. Segmentasi buah
Model terpadu memakai Grounded-SAM, yaitu Grounding DINO yang menghasilkan kotak dari perintah teks lalu SAM yang menghasilkan masker, tanpa penyetelan halus. Perintah teks generik "fruits" memberi hasil memuaskan, tetapi nama buah dalam bentuk tunggal memberi hasil terbaik untuk apel, plum, lemon, pir, dan persik. Untuk mangga, perintah "apple" lebih baik. Model pembanding adalah U-Net yang dilatih pada subset 62 citra beranotasi dari data nyata (dipotong menjadi sub-citra 2000 x 2000 piksel dan diperkecil 0,5) ditambah data Fuji-SfM, dengan augmentasi. Pada set validasi Fuji, IoU berbobot prevalensi kelas rerata adalah 0,919 untuk SAM dan 0,962 untuk U-Net.

### 3. FruitNeRF
Arsitektur dibangun di atas Nerfacto dengan cabang semantik tambahan ("Fruit Field") yang hanya menerima vektor fitur kepadatan, bukan arah pandang. Fungsi kerugian adalah $L = L_{Photo} + L_{Sem}$, dengan kerugian fotometrik berupa galat kuadrat dan kerugian semantik berupa entropi silang biner. Gradien semantik dibatasi pada Fruit Field saja. Dua ukuran diuji: FruitNeRF (2 lapis, 64 neuron tersembunyi) dan FruitNeRF-Big (3 lapis, 128 neuron). Pelatihan memakai NVIDIA RTX A5000 24 GB, sekitar 12 menit untuk FruitNeRF dan sekitar 2 jam 30 menit untuk FruitNeRF-Big. Citra nyata diperkecil menjadi 1000 x 1500 piksel.

### 4. Ekspor awan titik
Volume disampel dengan kamera ortografik, dan titik dibuang bila kepadatan atau nilai semantiknya di bawah ambang tetap. Awan titik dipangkas manual agar hanya memuat pohon yang dievaluasi.

### 5. Pencacahan dengan pengklasteran bertingkat
Derau dihapus dengan membuang titik yang tidak memiliki cukup tetangga dalam radius tertentu. Tahap pertama memakai DBSCAN dan menghasilkan klaster tunggal (volume mirip templat buah), ganda (volume berlebih), dan kecil. Klaster kecil yang pusatnya lebih dekat daripada radius rerata buah digabung, dan sisanya dibuang bila volumenya tidak mirip volume buah. Tahap kedua pada klaster ganda memakai *agglomerative clustering* dengan ukuran klaster 1 sampai $N$ ($N = 6$ untuk apel) dan memilih ukuran dengan jarak Hausdorff minimum antara templat buah dan lambung awan titik.

## Eksperimen dan Hasil
Tiga percobaan dijalankan: (1) pencacahan pada enam jenis buah sintetis dengan masker acuan dan masker SAM; (2) pengaruh jumlah dan resolusi citra pada apel sintetis (jumlah acuan 283); (3) apel nyata dengan dua ukuran model dan dua sumber masker.

Hasil percobaan pertama (Tabel I, hitungan terdeteksi dari jumlah sebenarnya dan F1):

| Buah | Masker acuan: terdeteksi, F1 | Masker SAM: terdeteksi, F1 |
|---|---|---|
| Apel | 283/283, 1 | 282/283, 0,991 |
| Plum | 651/781, 0,885 | 315/781, 0,575 |
| Lemon | 316/326, 0,978 | 326/326, 0,982 |
| Pir | 236/250, 0,971 | 229/250, 0,956 |
| Persik | 148/152, 0,987 | 148/152, 0,987 |
| Mangga | 926/1150, 0,873 | 807/1150, 0,816 |

Rerata F1 adalah 0,95 (masker acuan) dan 0,88 (SAM). Penulis menyatakan kinerja SAM terendah pada plum dan mangga, dengan recall 0,4 dan 0,69, karena oklusi buah yang lebih besar. Pada percobaan kedua, dengan citra kurang dari 20 hasil tidak bermakna dan jumlah buah melonjak pada 20 sampai 30 citra karena informasi semantik menyebar ke seluruh pohon (contoh puncak 696 pada 20 bingkai). Hitungan akurat memerlukan 60 citra pada resolusi 128 piksel, 50 citra pada 256 piksel, dan 30 sampai 40 citra pada 512 serta 1024 piksel. Kesimpulan makalah menyebut hasil baik dengan 40 citra per pohon pada resolusi 512 x 512.

Pada percobaan ketiga, set data apel nyata menghasilkan tingkat deteksi rerata sekitar 89% untuk Pohon 1 dan 2 dengan masker U-Net maupun SAM, dan sekitar 82% untuk Pohon 3 yang strukturnya lebih kompleks dengan oklusi lebih banyak. Pada Fuji-SfM, FruitNeRF-Big mencapai F1 0,79 (SAM) dan 0,78 (U-Net) dibandingkan 0,88 pada makalah Fuji asli; model kecil lebih buruk pada data Fuji. Jumlah acuan Fuji adalah 1.455 apel. Angka hitungan per pohon pada Gambar 8 tidak dapat dipastikan dari ekstraksi teks.

## Kelebihan dan Keterbatasan
Kelebihan: satu kerangka berlaku untuk banyak jenis buah tanpa anotasi tambahan, kode dan set data dirilis, dan penghitungan dilakukan setelah buah menyatu di 3D sehingga penghitungan ganda dicegah secara geometris.

Keterbatasan yang dinyatakan penulis: waktu pelatihan dan memori GPU besar sehingga belum cocok untuk waktu-nyata atau komputasi tepi; kualitas bergantung pada cakupan dan mutu citra; hiperparameter pengklasteran perlu disetel manual per jenis buah; tahap pengklasteran kedua terikat pada ukuran buah nominal sehingga perlu diadaptasi untuk ukuran berbeda pada tahap pertumbuhan lain; cahaya rendah, perbedaan pencahayaan, dan adegan tidak statis akibat angin dapat memburuk rekonstruksi.

Menurut pembacaan ringkasan ini, evaluasi nyata hanya memakai tiga pohon satu varietas dan satu kebun, awan titik dipangkas manual per pohon, dan hasil pada Fuji lebih rendah daripada metode acuan (0,79 dibandingkan 0,88). Menurut pembacaan ringkasan ini pula, tidak ada perbandingan langsung dengan pelacak video pada data yang sama.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak citra, termasuk dari kedua sisi pohon, dengan mekanisme rekonstruksi 3D: citra berpose direkonstruksi menjadi medan semantik NeRF, buah diekstrak sebagai awan titik 3D, lalu dihitung melalui pengklasteran. Identitas lintas pandang diselesaikan secara implisit oleh konsistensi geometri NeRF, bukan oleh pencocokan eksplisit antar-instans.

Hitungan tidak dilaporkan per kelas; hanya satu kelas "buah" per jenis, dan jenis buah dibedakan dengan perintah teks. Acuan hitung adalah hitungan manual di lapangan untuk tiga pohon apel nyata, hitungan dari model untuk data sintetis, dan hitungan 1.455 apel untuk Fuji-SfM. Yang dapat dipindahkan ke tandan kelapa sawit multi-sisi adalah gagasan menghitung di ruang 3D setelah rekonstruksi bersama, serta pengurangan hitungan ganda tanpa pencocokan antarcitra. Hambatan yang tersirat dari teks adalah kebutuhan pose kamera akurat, puluhan citra per pohon, pangkas manual per pohon, dan klaster yang terikat pada ukuran buah nominal; atribut kelas seperti kematangan tidak ditangani.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `meyer2024fruitnerf`.

Meyer dkk. mengusulkan FruitNeRF, yaitu pencacahan buah tanpa bergantung pada jenis buah yang menggabungkan Grounded-SAM, medan pancaran saraf semantik, ekstraksi awan titik buah, dan pengklasteran bertingkat dengan jarak Hausdorff untuk menghitung buah di ruang 3D. Rerata F1 pada enam jenis buah sintetis adalah 0,95 dengan masker acuan dan 0,88 dengan masker SAM. Pada Fuji-SfM, F1 mencapai 0,79, dibandingkan 0,88 pada makalah acuan.

Catatan verifikasi data: F1 rerata 0,95 dan 0,88 serta nilai pada Tabel I terbaca dari teks (Bagian IV-C dan Tabel I). Tingkat deteksi sekitar 89% dan 82% serta F1 0,79 dan 0,78 diambil dari paragraf hasil Bagian IV-C dan Kesimpulan. Angka hitungan per pohon pada Gambar 8 tercampur pada ekstraksi teks sehingga tidak dikutip. Tidak dapat diverifikasi dari teks: jumlah apel acuan per pohon untuk Pohon 1 sampai 3, nilai ambang kepadatan dan parameter DBSCAN, serta jumlah citra untuk pelatihan NeRF pada set Fuji selain 582 citra set data.
