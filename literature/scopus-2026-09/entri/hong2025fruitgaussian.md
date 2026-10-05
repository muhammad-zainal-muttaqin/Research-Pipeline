# Fruitgaussian: 3D Gaussian Splatting for Automated Fruit Counting in Natural Orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hong2025fruitgaussian` |
| Judul asli | Fruitgaussian: 3D Gaussian Splatting for Automated Fruit Counting in Natural Orchard |
| Penulis | Hong, Xiangyu; Qin, Linlin; Shi, Chun; Wu, Gang |
| Tahun | 2025 |
| Venue | Chinese Control Conference Ccc |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | persimmon/guava |

## Tautan Akses
- PDF: [hong2025fruitgaussian.pdf](../pdf/hong2025fruitgaussian.pdf)
- DOI resmi: https://doi.org/10.23919/ccc64809.2025.11179457

## Gambaran Umum
Makalah prosiding ini (Chinese Control Conference ke-44, 2025) mengusulkan FruitGaussian, kerangka kerja pencacahan buah berbasis *3D Gaussian Splatting* (3DGS), yaitu representasi adegan 3D eksplisit dari sekumpulan fungsi Gauss yang dirender secara diferensiabel. Sistem ini diterapkan pada kebun kesemek kultivar 'Taishuu' di Kabupaten Feidong, Hefei, Tiongkok. Buah dihitung dengan mengekstrak titik-titik Gauss berlabel "buah" dari adegan hasil rekonstruksi, lalu mengelompokkannya menjadi instans buah.

Dua komponen yang diklaim penulis sebagai kontribusi adalah penyematan semantik berjenjang (vektor semantik 16 dimensi pada setiap Gauss) dan regularisasi geometri berbasis kedalaman monokular dari Depth Anything V2. Hasil utama yang dilaporkan: akurasi pencacahan 96%, lebih tinggi 16 poin persentase daripada FruitNeRF, serta ekstraksi awan titik dalam hitungan detik dibandingkan 7 menit pada FruitNeRF.

Evaluasi dilakukan pada satu adegan kebun dengan 400 citra RGB. Makalah tidak melaporkan jumlah pohon, jumlah buah total pada acuan secara eksplisit di teks, maupun ulangan pada beberapa adegan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah di kebun alami terganggu oleh oklusi dedaunan, variasi pencahayaan, dan buah yang saling menumpuk. Kultivar yang diuji berwarna kuning-hijau sehingga spektrumnya tumpang tindih dengan daun. Penulis membagi metode terdahulu menjadi pengolahan citra 2D dan rekonstruksi 3D. Pada jalur 2D, pelacakan video berbasis filter Kalman mengalami penyimpangan pelacakan (*tracking drift*) saat oklusi karena hilangnya informasi akibat proyeksi 2D.

Pada jalur 3D, penulis menyebut dua kelemahan: ketergantungan pada sensor mahal (kamera stereo, LiDAR) untuk memperoleh kedalaman, dan awan titik jarang dari *Structure from Motion* (SfM) yang tidak memadai untuk analisis fenotipe halus atau robot pemetik. FruitNeRF, yang memakai *Neural Radiance Fields* (NeRF), dinilai berbiaya komputasi tinggi karena pengambilan sampel sinar yang rapat, menghasilkan artefak latar dan benda mengambang (*floaters*) pada adegan tak terbatas, dan hanya memakai satu batasan semantik.

## Ide Utama
Ide utamanya adalah mengganti representasi implisit NeRF dengan 3DGS eksplisit, sehingga pusat Gauss dapat langsung dipakai sebagai awan titik tanpa tahap pengambilan sampel voksel. Setiap Gauss diberi atribut semantik yang dipelajari bersama atribut warna, sehingga label kelas (langit, buah, lainnya) bersifat konsisten antarpandang karena melekat pada entitas 3D, bukan pada piksel.

Kedalaman monokular dari model terlatih dipakai sebagai prior geometri untuk menekan benda mengambang dan artefak pinggiran. Identitas buah antarpandang tidak ditangani dengan pencocokan antarcitra, melainkan ditentukan oleh posisi 3D bersama: Gauss yang sama diamati dari banyak pandangan, lalu klaster spasial pada awan titik dihitung sebagai satu buah.

## Cara Kerja Langkah demi Langkah
```
 Citra RGB -> COLMAP (pose + titik jarang)
 Citra RGB -> Grounding DINO + SAM 2 -> masker semantik
 Citra RGB -> Depth Anything V2 -> kedalaman, diselaraskan skala dengan SfM
              |
              v
   Pelatihan 3DGS (warna + semantik 16-D + kedalaman)
              |
              v
   Penyaringan label buah -> ambang RGB -> DBSCAN -> jumlah buah
```

### 1. Akuisisi data
Pengambilan citra dilakukan pada bulan September, musim panen kesemek, di kebun kesemek 'Taishuu' di Feidong, Hefei, Provinsi Anhui (31°59' LU, 117°51' BT). Kamera yang dipakai adalah Nikon D750 dengan lensa 24 mm dan bukaan f/8. Dikumpulkan 400 citra RGB beresolusi 4000×6000 piksel melalui akuisisi multi-pandang: 12 posisi azimut dalam radius 1 meter, masing-masing dengan 3 tingkat vertikal berjarak 0,5 meter. Jumlah pohon yang dipotret tidak dilaporkan. Jumlah buah sebenarnya ditentukan dengan hitung manual.

### 2. Persepsi multimodal
COLMAP memulihkan pose kamera dan awan titik jarang untuk inisialisasi 3DGS. Grounding DINO dan Segment Anything V2 menghasilkan masker semantik halus secara *zero-shot*. Depth Anything V2 menghasilkan peta kedalaman monokular padat $D_{mono}$, yang kemudian diselaraskan dengan awan titik SfM melalui transformasi afin $D_{dense} = s \cdot D_{mono} + t$. Skala $s$ dan offset $t$ diperoleh dengan meminimalkan galat kuadrat berbobot terhadap kedalaman SfM jarang.

### 3. Rekonstruksi adegan dengan 3DGS
Setiap Gauss memiliki pusat, kovarians (diuraikan menjadi rotasi dan skala), opasitas, dan warna dalam koefisien harmonik sferis orde tiga. Penulis menambahkan vektor semantik $f \in \mathbb{R}^{16}$ per Gauss. Adegan dibagi menjadi tiga kategori semantik terpisah: langit, buah, dan lainnya. Vektor semantik dirender ke 2D dengan pencampuran alfa yang sama dengan warna, lalu didekode oleh kepala klasifikasi linear menjadi label per piksel. Kedalaman dirender dengan formulasi volumetrik diskret yang analog dengan warna.

Fungsi kerugian terdiri atas tiga bagian: kerugian warna (SSIM dan norma L1), kerugian semantik (entropi silang atas fitur terender), dan kerugian kedalaman (konsistensi L1 antara kedalaman terender dan peta kedalaman padat yang dihitung sebelumnya). Bobot setiap kerugian tidak dilaporkan pada teks yang tersedia.

### 4. Ekstraksi awan titik dan pencacahan
Pusat Gauss hasil konvergensi dipakai sebagai koordinat titik, dan warna RGB diambil dari komponen DC koefisien harmonik sferis. Pengklasifikasi linear memberi label kategori pada tiap titik. Titik berlabel buah diambil, disaring dengan ambang RGB terpandu semantik, lalu dikelompokkan dengan DBSCAN (*Density-Based Spatial Clustering of Applications with Noise*). Alasan penulis memilih DBSCAN: tidak memerlukan jumlah klaster yang ditetapkan sebelumnya, kriteria keterjangkauan kepadatan memisahkan klaster buah rapat dari titik pencilan, dan bentuk klaster non-bulat dapat dipertahankan. Nilai parameter DBSCAN tidak dilaporkan.

## Eksperimen dan Hasil
Semua metode dibandingkan dengan protokol FruitNeRF, yakni pembagian latih-uji 9:1. FruitNeRF-big disesuaikan agar adil. Percobaan dijalankan pada satu GPU NVIDIA RTX 4090D (24 GB). Seluruh metode dilatih 30 ribu iterasi, kecuali FruitNeRF-big yang tetap 100 ribu iterasi dan memerlukan 3 jam pelatihan. Kualitas rendering diukur dengan PSNR, SSIM, dan LPIPS.

| Metode | PSNR (dB) | SSIM | LPIPS (lebih rendah lebih baik) |
|---|---|---|---|
| FruitNeRF | 14,57 | 0,44 | 0,71 |
| FruitNeRF-big | 14,40 | 0,43 | 0,72 |
| Base 3DGS | 16,21 | 0,49 | 0,54 |
| Gaussian Grouping | 16,15 | 0,50 | 0,58 |
| FruitGaussian | 16,56 | 0,54 | 0,49 |

Penulis menyatakan LPIPS 0,49 merupakan peningkatan relatif 30,99% terhadap varian FruitNeRF. Untuk ekspor awan titik, representasi eksplisit membutuhkan sekitar beberapa detik, dibandingkan 7 menit pada FruitNeRF, yang dinyatakan sebagai percepatan dua orde besaran.

Untuk pencacahan, penulis melaporkan akurasi 96% yang melampaui FruitNeRF sebesar 16 poin persentase (Gambar 8). Ekstraksi teks hanya memuat angka sumbu 24, 20, 22, dan 25 untuk "Fruit Num" dengan label Ours, FruitNeRF, FruitNeRF-big, dan GroundTruth. Urutan angka terhadap label tidak dapat dipastikan dari teks, sehingga jumlah buah per metode tidak dikutip di sini. Tidak ada metrik galat per pohon, bias, atau pembagian per kelas.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: representasi eksplisit memungkinkan ekstraksi awan titik dalam hitungan detik, rendering berkualitas lebih baik daripada varian NeRF pada ketiga metrik, dan regularisasi kedalaman menekan artefak mengambang. Keterbatasan yang dinyatakan penulis: asumsi adegan statis tidak mampu menangani gerak vegetasi akibat angin, yang menimbulkan kabur gerak pada area dedaunan rapat; dan SfM dengan citra tak berurutan hanya berhasil pada 30% percobaan lapangan akibat homogenitas struktur dan pengulangan tekstur pada kebun skala besar. Arah lanjutan yang disebut meliputi representasi Gauss temporal dan penggabungan 3DGS dengan SLAM.

Menurut pembacaan ringkasan ini, bukti pencacahan sangat terbatas: tampaknya satu adegan dengan jumlah buah acuan pada orde dua puluhan (berdasarkan angka sumbu Gambar 8), tanpa ulangan, tanpa interval kepercayaan, dan tanpa definisi tertulis tentang "akurasi pencacahan". Menurut pembacaan ringkasan ini, nilai PSNR yang rendah (16,56 dB) menunjukkan kualitas rendering absolut yang modest, dan penjelasan penulis tentang "kompensasi iluminasi dinamis" serta "modulasi kepadatan titik adaptif" tidak berkaitan dengan komponen yang diuraikan pada bagian metode. Perbandingan pencacahan hanya dengan keluarga FruitNeRF, bukan dengan pelacakan video.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat dari banyak pandangan melalui rekonstruksi 3D bersama: seluruh pandangan dioptimalkan ke dalam satu kumpulan Gauss, dan identitas buah ditetapkan oleh klaster DBSCAN pada awan titik, bukan oleh pencocokan atau pelacakan antarcitra. Mekanisme ini tergolong rekonstruksi 3D dengan pengelompokan spasial. Akuisisi mengelilingi satu pohon pada radius 1 meter dalam 12 azimut dan 3 tingkat tinggi, sehingga serupa dengan pengambilan multi-sisi.

Hitungan tidak dilaporkan per kelas; label semantik hanya membedakan langit, buah, dan lainnya. Acuan hitung adalah hitung manual, tanpa keterangan apakah di lapangan atau pada citra. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan pengelompokan spasial pada ruang 3D bersama dan atribut semantik per entitas 3D, yang dapat diperluas menjadi atribut kelas kematangan. Batasan yang relevan: ketergantungan pada keberhasilan SfM (30% pada citra tak berurutan), asumsi adegan statis, dan skala bukti yang sangat kecil.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `hong2025fruitgaussian`.

Hong dkk. mengusulkan FruitGaussian, kerangka pencacahan buah berbasis 3D Gaussian Splatting dengan penyematan semantik per Gauss dan regularisasi kedalaman monokular. Pencacahan dilakukan dengan mengelompokkan titik berlabel buah menggunakan DBSCAN. Pada satu adegan kebun kesemek (400 citra), penulis melaporkan akurasi pencacahan 96%, lebih tinggi 16 poin persentase daripada FruitNeRF, dan ekstraksi awan titik dalam hitungan detik dibandingkan 7 menit.

Catatan verifikasi data: Angka PSNR, SSIM, dan LPIPS terdapat pada Tabel 1; akurasi 96% dan selisih 16 poin persentase disebut pada teks Gambar 8 dan Kesimpulan; 400 citra, 4000×6000 piksel, 12 azimut, 3 tingkat, dan pembagian 9:1 ada pada Seksi 2.1 dan 3. Nilai jumlah buah per metode pada Gambar 8 tidak dapat dipetakan ke label dari teks ekstraksi. Definisi akurasi pencacahan, jumlah pohon, jumlah buah acuan, bobot kerugian, dan parameter DBSCAN tidak dilaporkan. Teks juga memuat klaim "kompensasi iluminasi dinamis" yang tidak dijelaskan pada metode.
