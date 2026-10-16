# Spatio-Temporal Metric-Semantic Mapping for Persistent Orchard Monitoring: Method and Dataset

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lei2025spatio` |
| Judul asli | Spatio-Temporal Metric-Semantic Mapping for Persistent Orchard Monitoring: Method and Dataset |
| Penulis | Lei, Jiuzhou; Prabhu, Ankit; Liu, Xu; Cladera, Fernando; Mortazavi, Mehrad; Ehsani, Reza; Chaudhari, Pratik; Kumar, Vijay |
| Tahun | 2025 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [lei2025spatio.pdf](../pdf/lei2025spatio.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2025.3588037

## Gambaran Umum
Makalah (pracetak arXiv, versi 3, Mei 2025) ini menyajikan sistem pemetaan metrik-semantik spatio-temporal 4D untuk memantau buah di kebun sepanjang musim tumbuh. Sistem terdiri atas modul lokalisasi buah 3D yang memadukan LiDAR dan RGB, serta metode asosiasi buah 4D lintas sesi yang memakai informasi posisi, tampilan visual, dan topologi (tata letak relatif antarbuah). Penulis juga merilis dataset multimodal untuk lima spesies buah selama musim tumbuh.

Data berasal dari kebun di Pennsylvania, Maryland, dan California (AS), April sampai Agustus 2024, pada 284 pohon (120 apel, 63 pir, 50 persik, 34 ceri, 17 pistachio). Evaluasi pencacahan memakai 60 pohon apel.

Hasil utama: estimasi 1.846 apel terhadap acuan 1.790 (galat total 3,1%, atau akurasi 96,9% menurut abstrak), galat rerata ukuran buah 1,10 cm, presisi asosiasi 4D rata-rata 93,5% dan F1 92,1%, dengan peningkatan presisi 23,7% terhadap baseline kedua.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan kebun pada tingkat pohon atau buah sepanjang musim diperlukan untuk fenotipe tanaman dan optimasi sumber daya (misalnya penjarangan kimia berdasarkan ukuran buah, irigasi menurut laju pertumbuhan, estimasi hasil). Metode terdahulu cukup akurat melokalisasi buah dalam satu sesi, tetapi tidak memantau pertumbuhan lintas waktu. Memperluas ke 4D memerlukan asosiasi data buah antarsesi yang sulit akibat perubahan posisi, ukuran, dan tampilan, serta oklusi kanopi, buah yang terlewat, hitungan ganda, dan munculnya buah baru. Metode registrasi awan titik, registrasi citra berbasis fitur, dan pendekatan hibrida 2D-3D dinilai kurang rinci untuk tingkat instans buah. Metode berbasis awan titik presisi tinggi memerlukan pelabelan ekstensif dan akuisisi lambat.

## Ide Utama
Penulis memisahkan masalah menjadi lokalisasi 3D tiap sesi dan pelacakan 4D antarsesi. Asosiasi 4D memakai dua tahap: tahap pertama memilih buah rujukan yang konsisten antarpandang, dan tahap kedua menambahkan biaya topologi yang dihitung dari vektor ke buah rujukan itu, sehingga pasangan yang melanggar kekonsistenan topologi ditolak. Metode ini memakai model pralatih dan fitur hasil rancangan manual, tanpa melatih jaringan saraf untuk asosiasi.

## Cara Kerja Langkah demi Langkah

```
 LiDAR + RGB + IMU -> Faster-LIO + YOLOv8 -> fusi LiDAR-RGB -> lintasan buah 3D
 -> optimasi reproyeksi -> asosiasi 4D dua tahap (posisi, DINOv2, topologi)
 -> peta 4D: hitungan, ukuran, posisi
```

### 1. Akuisisi data
Perangkat: LiDAR Ouster OS0-128, kamera RGB rana global FLIR Chameleon, kamera RGB-D Intel RealSense D435i, IMU VectorNav VN-100, dan GPS UBlox ZED-F9P. Sensor dibawa tangan menyusuri sisi barisan pohon (dapat dipasang pada quadrotor). Pengambilan data setiap dua atau tiga minggu dari awal April sampai akhir Agustus 2024. Lokasi: Hands on Earth Orchard (Lititz, Pennsylvania; apel dan pir), Shaw Orchards (Harford, Maryland; apel, persik, ceri), dan Merced, California (pistachio). Kultivar tidak dilaporkan. Jumlah citra tidak dilaporkan.

### 2. Lokalisasi 3D dalam satu sesi
Segmentasi instans buah memakai YOLOv8 yang disetel halus. Pose sensor diestimasi dengan Faster-LIO. Awan titik LiDAR diakumulasi 1,5 detik, diproyeksikan ke citra, dan posisi buah adalah titik berat awan titik di dalam masker. Pelacakan antarbingkai memakai algoritma Hungaria dengan biaya 1 - IoU masker setelah proyeksi, dengan biaya tambahan agar buah boleh tidak berpasangan. Hanya buah yang teramati lebih dari tiga bingkai berturut-turut dihitung. Posisi buah dan pose kamera dioptimalkan dengan meminimalkan galat reproyeksi (kuadrat terkecil nonlinier dengan batas jarak dari nilai awal). Jalur yang hilang lalu muncul kembali digabung bila IoU masker melebihi ambang dan deteksi keduanya terjadi pada bingkai yang berbeda.

### 3. Asosiasi 4D dua tahap
Tahap 1: untuk setiap citra sesi A dicari citra sesi B dengan pandangan paling mirip (jarak fitur DINOv2). Algoritma Hungaria dengan biaya posisi (jarak Euklides setelah penyelarasan awan titik antarsesi dengan ICP) ditambah biaya visual (jarak fitur DINOv2 potongan citra buah) dijalankan. Buah rujukan dipilih dengan ambang entropi 0,8 pada distribusi pasangan. Tahap 2: biaya topologi ditambahkan, yaitu jumlah pasangan vektor ke buah rujukan yang sudutnya melebihi 10 derajat. Keputusan akhir tiap buah ditentukan dengan suara terbanyak atas pasangan yang diperoleh dari berbagai citra. Jarak maksimum pencocokan sebesar 0,3 m disebut sebagai contoh dalam teks.

### 4. Pembuatan peta
Dari asosiasi diperoleh hitungan, ukuran, dan posisi buah sepanjang musim.

## Eksperimen dan Hasil
Acuan hitungan dibuat dengan menghitung manual dari citra video yang dipilih (pohon terlihat penuh dan di tengah) dengan penanda digital. Evaluasi dilakukan per kelompok 22 kelompok yang masing-masing berisi dua atau tiga pohon (60 pohon apel), karena batas pohon yang berdekatan sulit dibedakan.

Tabel I (pencacahan):

| Statistik | Hasil |
|---|---|
| Estimasi / acuan (total) | 1.846 / 1.790 |
| Galat absolut total | 56 / 3,1% |
| Rerata galat absolut per kelompok pohon (22 kelompok) | 6,0 / 8,0% |
| Simpangan baku galat absolut per kelompok | 5,0 / 6,4% |

Penyebab kelebihan hitung menurut penulis: hitungan ganda akibat awan titik buah yang bising, dan buah yang jatuh di tanah (dikeluarkan dari acuan).

Asosiasi 4D: acuan dibuat manual pada lima pohon untuk tiga rentang sesi (12 Juni ke 4 Juli, 4 Juli ke 19 Juli, 19 Juli ke 13 Agustus), dengan mengecualikan kurang dari 5% buah yang ambigu bagi manusia. Metrik: presisi dan F1 (recall tidak dipakai langsung karena dipengaruhi jangkauan pencocokan). Baseline pertama: pencocokan posisi 3D saja dengan Hungaria; baseline kedua: versi modifikasi metode Riccardi dkk. berbasis deskriptor histogram, diimplementasi ulang dan di-*tune* dengan Optuna.

| Hasil | Nilai |
|---|---|
| Presisi rata-rata metode usulan | 93,5% |
| F1 rata-rata metode usulan | 92,1% |
| Peningkatan presisi terhadap baseline kedua | 23,7% |
| Peningkatan F1 terhadap baseline kedua | 11,9% |

Ablasi: posisi ditambah visual sebanding dengan baseline; penambahan topologi menaikkan presisi dengan mengurangi positif palsu. Dari positif palsu yang berkurang, 43,2% ditolak dengan benar, 28,4% berubah menjadi positif benar, dan 28,4% ditolak keliru. Penghapusan acak sampai 50% buah dari masukan menunjukkan metode usulan tetap unggul dalam F1 (Gambar 7, angka tidak terbaca dari teks).

Ukuran buah: pada simulasi fisik pohon dengan 19 apel yang diukur dengan jangka sorong, galat absolut rerata 1,10 cm dan simpangan baku 0,45 cm.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: menjembatani lokalisasi 3D dan pemantauan 4D, tidak memerlukan pelatihan jaringan asosiasi, serta dataset yang mencakup seluruh siklus tumbuh dari fase tunas sampai panen untuk lima buah.

Keterbatasan yang dinyatakan penulis: kerapatan LiDAR yang rendah membatasi lokalisasi dan estimasi ukuran buah kecil; pemilihan buah rujukan tetap dapat memuat pencilan; biaya topologi dapat keliru menolak pasangan yang benar.

Menurut pembacaan ringkasan ini: evaluasi pencacahan hanya pada apel dan per kelompok dua atau tiga pohon, bukan per pohon; evaluasi asosiasi 4D hanya pada lima pohon; pengukuran ukuran divalidasi pada model simulasi fisik, bukan di kebun; metode dua tahap bergantung pada penyelarasan ICP antarsesi dan pada citra dengan sudut pandang serupa; hasil per spesies lain (pir, persik, ceri, pistachio) tidak dilaporkan.

## Kaitan dengan Tinjauan main6
Makalah menangani buah yang terlihat berulang pada dua tingkat: antarbingkai dalam satu sesi (pelacakan Hungaria berbasis IoU masker setelah proyeksi 3D, ditambah penggabungan ulang jalur yang terputus) dan antarsesi (asosiasi 4D dengan biaya posisi, visual DINOv2, dan topologi). Mekanismenya adalah pencocokan multi-pandang dengan landmark 3D dan optimasi reproyeksi. Hitungan tidak dilaporkan per kelas (hanya apel). Acuan hitungan adalah hitung manual dari citra video yang dipilih, bukan panen; untuk asosiasi 4D acuan adalah pencocokan manual dari citra.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: gagasan biaya topologi berbasis buah rujukan yang konsisten sebagai penalti terhadap pencocokan keliru, penggabungan jalur yang terputus dengan syarat tidak muncul pada bingkai yang sama, serta pemisahan evaluasi per kelompok pohon bila batas pohon sulit dipisahkan. Kebutuhan LiDAR dan pose yang akurat merupakan prasyarat yang berbeda dari citra RGB saja.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `lei2025spatio`.

Lei dkk. mengusulkan sistem pemetaan metrik-semantik 4D untuk kebun yang menggabungkan lokalisasi buah 3D berbasis LiDAR-RGB (YOLOv8, Faster-LIO, pelacakan Hungaria, optimasi reproyeksi) dengan asosiasi buah antarsesi dua tahap berbasis posisi, fitur DINOv2, dan topologi. Pada 60 pohon apel sistem menghitung 1.846 apel terhadap acuan 1.790 (galat total 3,1%), dan asosiasi 4D mencapai presisi 93,5% serta F1 92,1%, dengan dataset multimodal lima spesies buah selama satu musim tumbuh.

Catatan verifikasi data: Angka pencacahan ada pada Tabel I (Seksi V-A). Presisi dan F1 asosiasi 4D serta peningkatan 23,7% dan 11,9% ada pada Seksi V-B (angka batang pada Gambar 6 tidak terbaca dari teks). Galat ukuran 1,10 cm dan simpangan baku 0,45 cm ada pada teks Seksi V-C dan keterangan Gambar 5. Rincian dataset ada pada Seksi IV. Akurasi 96,9% dan galat 3,1% berasal dari acuan 1.790 dengan estimasi 1.846; abstrak menyebut keduanya. Jumlah citra dan kultivar tidak dilaporkan. Teks ekstraksi terbaca baik.
