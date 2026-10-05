# AppleYOLO: Apple yield estimation method using improved YOLOv8 based on Deep OC-SORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tan2025appleyolo` |
| Judul asli | AppleYOLO: Apple yield estimation method using improved YOLOv8 based on Deep OC-SORT |
| Penulis | Tan, Shiting; Kuang, Zhufang; Jin, Boyu |
| Tahun | 2025 |
| Venue | Expert Systems with Applications |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [tan2025appleyolo.pdf](../pdf/tan2025appleyolo.pdf)
- DOI resmi: https://doi.org/10.1016/j.eswa.2025.126764

## Gambaran Umum
Makalah ini mengusulkan AppleYOLO, metode estimasi hasil apel yang menggabungkan detektor berbasis YOLOv8 yang dimodifikasi dengan pelacak multi-objek (*multi-object tracking*, MOT) Deep OC-SORT. Modifikasi pada detektor terdiri atas FasterNet sebagai *backbone*, Focal Modulation (FM) setelah *backbone*, dan KernelWarehouse (KWConv, konvolusi dinamis hemat parameter) pada bagian fusi fitur (*neck*). Pelacak ditempatkan setelah *head* deteksi agar setiap apel memperoleh nomor identitas unik dan tidak terhitung berulang pada video. Objek yang diteliti adalah apel di kebun komersial; satu kelas objek (apel) dipakai pada seluruh eksperimen.

Data berupa 797 citra beresolusi tinggi dari kebun apel yang diperoleh melalui pertukaran dengan akademisi lain. Citra dibagi 8:2 menjadi 637 citra latih dan 160 citra validasi, lalu citra latih diperbanyak menjadi 1.911 dengan *motion blur* dan derau Gaussian. Anotasi hanya diberikan pada apel baris depan pohon.

Hasil utama: AppleYOLO mencapai mAP50 98,5% dan mAP50-95 79,8%, atau naik 1% dan 5,1% dari YOLOv8 dasar (97,5% dan 74,7%), dengan 4,43 juta parameter, 9,7 GFLOPS, dan 100,3 FPS pada ukuran batch 1. Evaluasi pencacahan memakai 49 citra dengan hitungan manual sebagai acuan dan menghasilkan R² = 0,95 (persamaan regresi y = 0,9817x − 1,679); makalah menyatakan lebih dari 90% citra memiliki galat hitung paling banyak 6. Makalah ini berstatus pracetak yang belum ditelaah sejawat (SSRN).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil kebun secara tradisional bergantung pada penilaian petani berpengalaman atau pencuplikan area tertentu. Makalah mengutip bahwa pencuplikan acak umumnya memiliki galat sekitar 10% dan dapat mencapai 30% pada praktik lapangan (mengutip Gómez-Lagos dkk., 2023). Pendekatan berbasis visi komputer dapat menghitung buah individual, tetapi penulis menilai karya terdahulu belum memenuhi tiga syarat sekaligus: akurasi, kinerja waktu nyata, dan kompleksitas komputasi rendah sehingga dapat dijalankan pada perangkat kecil.

Di kebun apel, penulis mengidentifikasi empat faktor yang menurunkan akurasi: daun menutupi buah, buah saling tumpang tindih, apel hijau menyerupai daun, dan ukuran buah bervariasi (Gambar 4). Pada pencacahan dari video, buah yang tampak serupa mudah menimbulkan pelacakan ganda dan penghitungan berulang. Karena itu, penulis menggabungkan perbaikan arsitektur detektor dengan pelacak yang memakai fitur penampakan.

## Ide Utama
Gagasan makalah ini adalah memadukan detektor ringan yang diperkuat tiga modul dengan pelacak MOT yang memakai informasi gerak sekaligus penampakan, sehingga satu apel fisik mempertahankan satu nomor identitas sepanjang bingkai video. Pencacahan dilakukan dengan menghitung identitas unik yang dikeluarkan pelacak, bukan jumlah deteksi per bingkai.

Kontribusi arsitektur yang diklaim penulis adalah: FasterNet untuk mempelajari informasi tepi (kontur dan tekstur) secara efisien; FM untuk menangkap konteks dan meningkatkan persepsi spasial; KWConv untuk meningkatkan kemampuan ekstraksi fitur kompleks (misalnya akibat oklusi oleh batang, ranting, dan daun) dengan parameter efisien; serta Deep OC-SORT untuk mengatasi pelacakan tidak stabil dan penghitungan berulang.

## Cara Kerja Langkah demi Langkah
```
 Citra/video 640x640
        |
 [Backbone: FasterNet (PConv)] -> [Focal Modulation]
        |
 [Neck: Concat + KWConv + Conv]
        |
 [Head terpisah (decoupled), satu detektor per skala]
        |
 [Deep OC-SORT: CMC + ReID + Kalman + bobot adaptif]
        |
 ID unik per apel -> hitungan
```

### 1. Akuisisi dan penyiapan data
Sebanyak 797 citra apel di kebun nyata diperoleh melalui pertukaran dengan akademisi lain; jenis kamera, platform, lokasi kebun, kultivar, dan jumlah pohon tidak dilaporkan. Pembagian acak 8:2 menghasilkan 637 citra latih dan 160 citra validasi. Citra latih diperbanyak menjadi 1.911 dengan *motion blur* dan derau Gaussian, dan makalah menyebut 2.071 citra dianotasi dengan Labelimg (1.911 + 160 = 2.071, dihitung dari angka makalah). Anotasi memakai metode satu baris (*single-row annotation*): kamera memotret pohon per baris dari tampak depan dan hanya buah baris depan yang dianotasi agar model tidak mengenali apel di baris belakang. Penghentian awal (*early stopping*) memakai kesabaran 50 epoch terakhir.

### 2. Backbone FasterNet
FasterNet memakai konvolusi parsial (*partial convolution*, PConv) yang hanya mengonvolusi sebagian kanal. Pada rasio kanal 1/4, makalah menyatakan akses memori PConv menjadi 1/4 dan FLOPs menjadi 1/16 dari konvolusi biasa. Jaringan memiliki empat tahap dengan peta fitur 160x160, 80x80, 40x40, dan 20x20 untuk masukan 640x640. Tiap blok berisi satu PConv diikuti dua konvolusi *point-wise*, dengan normalisasi batch dan aktivasi hanya di antara kedua konvolusi *point-wise*.

### 3. Focal Modulation
FM menggantikan atensi diri (*self-attention*) dengan agregasi konteks lebih dahulu, kemudian memasukkan konteks ke token kueri sebagai modulasi. Prosesnya dua langkah: kontekstualisasi hierarkis (tumpukan konvolusi *depth-wise* dengan GeLU, ditambah *average pooling* global sehingga diperoleh $L+1$ peta fitur) dan agregasi berpintu (*gated aggregation*) yang memadatkan peta tersebut menjadi satu modulator dengan bobot gerbang peka spasial dan tingkat.

### 4. KernelWarehouse pada neck
KWConv membagi kernel statis menjadi $m$ bagian terpisah (*kernel partition*) dan membagikan unit kernel dalam satu gudang (*warehouse*) kepada beberapa lapisan pada tahap yang sama (*warehouse sharing*). Bobot atensi dihitung dari vektor hasil *global average pooling* dan dua lapisan *fully connected*, lalu menggabungkan unit kernel secara linear. Pada *neck*, KWConv dikombinasikan dengan konvolusi biasa. *Head* memakai desain terpisah untuk klasifikasi dan lokalisasi pada tiap skala.

### 5. Pencacahan dengan Deep OC-SORT
Posisi dan fitur apel dari detektor dikoreksi oleh modul kompensasi gerak kamera (*camera motion compensation*, CMC), sementara modul identifikasi ulang (*re-identification*, ReID) mengekstraksi fitur penampakan. Setelah digabungkan, filter Kalman milik OC-SORT memprediksi dan memperbarui keadaan apel. Modul pembobotan adaptif menyesuaikan bobot fitur menurut daya pembedanya, lalu matriks biaya dan penyelesai linear (*linear solver*) menuntaskan asosiasi data antarbingkai. Penghitungan identitas dilakukan atas keluaran pelacak. Makalah tidak menyebut parameter pelacak, model ReID yang dipakai, maupun cara penghitungan identitas pada akhir urutan.

### 6. Pengaturan pelatihan
Seluruh model dilatih pada lingkungan yang sama: Windows 11, GPU Nvidia GeForce RTX 3090 24 GB, Python 3.8, PyTorch 2.0.0, dan CUDA 11.7, dengan 300 epoch, ukuran batch 16, *imgsz* 640, dan optimizer Adam. Metrik yang dipakai adalah presisi, *recall*, mAP, jumlah parameter, GFLOPS, dan FPS pada batch 1.

## Eksperimen dan Hasil
Semua perbandingan detektor memakai satu kelas objek dan data yang sama; makalah tidak memerinci apakah angka diukur pada himpunan validasi 160 citra atau himpunan lain. Bagian ini juga tidak melaporkan pengulangan dengan beberapa *seed*.

Pengaruh ukuran masukan (Tabel 2) dan ablasi (Tabel 6) dirangkum berikut.

| Konfigurasi | mAP50 | mAP50-95 | Parameter (juta) | GFLOPS | FPS (b@1) |
|---|---|---|---|---|---|
| Masukan 320x320 | 0,926 | 0,62 | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan |
| Masukan 640x640 | 0,975 | 0,747 | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan |
| Masukan 1280x1280 | 0,986 | 0,796 | tidak dilaporkan | tidak dilaporkan | tidak dilaporkan |
| YOLOv8 | 0,975 | 0,747 | 3,01 | 8,1 | 112,4 |
| + FasterNet | 0,98 | 0,76 | 4,17 | 10,7 | 96,9 |
| + FasterNet + FM | 0,982 | 0,78 | 5,23 | 10,8 | 99,6 |
| + FasterNet + FM + KWConv (AppleYOLO) | 0,985 | 0,798 | 4,43 | 9,7 | 100,3 |

Memori GPU rerata pada masukan 320, 640, dan 1280 berturut-turut 1,23G, 5,38G, dan 20,9G; ukuran 640x640 dipilih sebagai kompromi. Perbandingan modul tunggal terhadap YOLOv8 dasar (mAP50-95 0,747): FM 0,771 (SPPF 0,747, LSKA 0,755, AIFI 0,751); KWConv 0,764 dengan 4,5 GFLOPS (pembanding DBB 0,751, DCNv3 0,742, SCConv 0,744, ODConv 0,734, D_LKA 0,741); FasterNet 0,76 (EfficientViT 0,743, Swin Transformer 0,753 dengan 29,9 juta parameter dan 79,1 GFLOPS). Augmentasi sampel dilaporkan meningkatkan kurva mAP50 dan mAP50-95 dibanding citra asli (Gambar 10 dan 11), tanpa angka tabel.

Perbandingan dengan detektor lain (Tabel 7, ukuran 640):

| Metode | Presisi | Recall | mAP50 | mAP50-95 | Parameter (juta) | GFLOPS | FPS |
|---|---|---|---|---|---|---|---|
| YOLOv3-tiny | 0,959 | 0,93 | 0,97 | 0,739 | 12,13 | 18,9 | 291,3 |
| YOLOv5 | 0,947 | 0,929 | 0,972 | 0,728 | 2,5 | 7,1 | 94,8 |
| YOLOv6 | 0,944 | 0,919 | 0,968 | 0,72 | 4,23 | 11,8 | 122,1 |
| YOLOv7 | 0,96 | 0,97 | 0,987 | 0,726 | 37,2 | 105,1 | 35,5 |
| YOLOv8 | 0,955 | 0,935 | 0,975 | 0,747 | 3,01 | 8,1 | 112,4 |
| RT-DETR | 0,955 | 0,943 | 0,978 | 0,738 | 9,48 | 16,7 | 43,6 |
| YOLOv9-c | 0,965 | 0,957 | 0,986 | 0,8 | 51 | 238,9 | 39 |
| AppleYOLO | 0,966 | 0,958 | 0,985 | 0,798 | 4,43 | 9,7 | 100,3 |

AppleYOLO memiliki mAP50-95 yang setara dengan YOLOv9-c (0,798 berbanding 0,8) dengan parameter, komputasi, dan kecepatan yang jauh lebih baik. YOLOv7 memiliki mAP50 dan recall lebih tinggi daripada AppleYOLO (0,987 dan 0,97). Pernyataan abstrak bahwa AppleYOLO lebih unggul daripada YOLOv9-c, RT-DETR, YOLOv8, dan YOLOv7 tidak sepenuhnya tecermin pada Tabel 7 untuk YOLOv9-c pada mAP50-95 maupun YOLOv7 pada mAP50.

Evaluasi pencacahan memakai 49 citra apel yang dihitung manual. Regresi antara hitungan algoritma dan hitungan manual menghasilkan y = 0,9817x − 1,679 dengan R² = 0,95304 (Gambar 22), jumlah apel per citra berada pada kisaran sekitar 10 sampai 80 menurut sumbu gambar. Selisih hitungan terpusat di sekitar nol, dan lebih dari 90% citra memiliki galat paling banyak 6 (Gambar 23). Galat relatif, galat absolut rerata, serta hasil pada video dan perbandingan dengan pelacak lain tidak dilaporkan.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis adalah keseimbangan akurasi dan efisiensi: parameter dan GFLOPS hanya sedikit di atas YOLOv8 dasar, kecepatan 100,3 FPS, dan ablasi menunjukkan peningkatan mAP50-95 pada setiap penambahan modul. Pembanding modul pada setiap komponen (agregasi fitur, konvolusi, *backbone*) disajikan pada kondisi pelatihan yang sama.

Keterbatasan yang dinyatakan penulis hanya berupa rencana ke depan: optimasi ukuran model dan kemampuan generalisasi, serta perluasan ke tanaman lain. Makalah tidak memuat bagian keterbatasan tersendiri.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pertama, dataset kecil (797 citra) dengan satu kelas, tanpa informasi lokasi, kultivar, dan kamera, serta tidak jelas apakah angka mAP diukur pada 160 citra validasi yang juga dipakai untuk penghentian awal; tidak ada himpunan uji terpisah yang dinyatakan. Kedua, mAP50 yang sudah mendekati 0,98 membuat selisih antarmodel kecil (misalnya 0,975 menjadi 0,985), dan tidak ada pengulangan *seed* atau uji signifikansi. Ketiga, nilai YOLOv8 pada Tabel 3 sampai 7 identik di semua tabel, sehingga hanya satu proses pelatihan yang tampak. Keempat, evaluasi pencacahan memakai 49 citra, bukan urutan video, sehingga tidak jelas bagaimana kemampuan Deep OC-SORT menghilangkan penghitungan berulang diuji; kontribusi pelacak terhadap galat hitung tidak diisolasi dari kontribusi detektor. Kelima, anotasi hanya baris depan, sehingga hitungan tidak mewakili seluruh apel pohon dan tidak ada pembandingan dengan hasil panen aktual.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali melalui pelacakan video: Deep OC-SORT memberi nomor identitas unik per apel antarbingkai berdasarkan gerak (filter Kalman), kompensasi gerak kamera, dan fitur penampakan ReID. Identitas bersifat temporal pada satu lintasan kamera; tidak ada pencocokan lintas sisi pohon, rekonstruksi 3D, atau koreksi statistik dua sisi. Anotasi hanya baris depan dipakai untuk menghindari penghitungan apel di baris belakang, bukan untuk menangani identitas lintas pandang.

Hitungan dilaporkan sebagai total per citra dan bukan per kelas, karena hanya ada satu kelas (apel). Acuannya adalah hitungan manual pada 49 citra, bukan hasil panen maupun hitung manual di lapangan pada pohon. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola detektor ringan ditambah pelacak berpenampakan untuk mempertahankan identitas pada urutan bingkai, serta pemilihan fitur penampakan untuk membedakan objek serupa. Namun, makalah ini tidak menyediakan mekanisme untuk menghubungkan tandan yang sama pada sisi pohon berbeda yang tidak berurutan sebagai video, dan tidak menyediakan inventaris per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `tan2025appleyolo`.

Tan dkk. mengusulkan AppleYOLO, metode estimasi hasil apel yang menggabungkan YOLOv8 yang dimodifikasi (*backbone* FasterNet, Focal Modulation, dan konvolusi dinamis KernelWarehouse pada *neck*) dengan pelacak Deep OC-SORT untuk menghindari penghitungan berulang. Pada dataset kustom 797 citra apel (satu kelas), model melaporkan mAP50 0,985 dan mAP50-95 0,798, naik 1% dan 5,1% dari YOLOv8 dasar, dengan 4,43 juta parameter dan 100,3 FPS. Pada 49 citra uji dengan hitungan manual, hitungan algoritma berkorelasi dengan R² = 0,95.

Catatan verifikasi data: angka deteksi utama (mAP50 0,985; mAP50-95 0,798; parameter 4,43 juta; GFLOPS 9,7; FPS 100,3) terdapat pada Tabel 6 dan Tabel 7 serta abstrak dan kesimpulan; angka ukuran masukan pada Tabel 2; perbandingan modul pada Tabel 3 sampai 5. Pembagian data (797, 637, 160, 1.911, 2.071) tertulis pada seksi 3. Hasil pencacahan (R² = 0,95; persamaan regresi; galat paling banyak 6 pada lebih dari 90% citra; 49 citra) tertulis pada seksi 4.9 dan Gambar 22 serta 23; nilai jumlah apel per citra pada sumbu gambar hanya dibaca kasar. Ekstraksi teks memotong angka tabel menjadi baris terpisah; nilai tabel dicocokkan menurut urutan kolom dan konsisten dengan teks. Lokasi kebun, kultivar, kamera, rincian himpunan uji, parameter Deep OC-SORT, galat hitung rerata, dan hasil pencacahan pada video tidak dapat diverifikasi dari teks. Makalah adalah pracetak SSRN yang belum ditelaah sejawat; status terbitan akhir tidak dapat diperiksa dari teks.
