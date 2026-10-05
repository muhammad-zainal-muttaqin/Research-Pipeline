# Greenhouse Tomato Fruit Inspection and Counting Method Based on Improved YOLO v8n ByteTrack

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `feng2026greenhouse` |
| Judul asli | Greenhouse Tomato Fruit Inspection and Counting Method Based on Improved YOLO v8n ByteTrack |
| Penulis | Feng, Q.; others |
| Tahun | 2026 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [feng2026greenhouse.pdf](../pdf/feng2026greenhouse.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2026.05.011

## Gambaran Umum
Makalah ini (berbahasa Mandarin, *Transactions of the Chinese Society for Agricultural Machinery* 2026, vol. 57 no. 5) mengusulkan metode pencacahan dinamis buah tomat matang di rumah kaca dari video yang direkam robot inspeksi. Kerangkanya terdiri atas detektor YOLO v8n yang dimodifikasi (YOLO v8n-MAFP), pelacak ByteTrack yang diperluas dengan strategi pencocokan ulang skor rendah adaptif (*adaptive low-score re-matching*, ALRM; pelacak hasilnya disebut ALRM-Track), dan mekanisme pencacahan berbasis pencocokan wilayah berurutan (*sequence region matching*) di sekitar sumbu tengah bingkai.

Data pelatihan dan validasi berasal dari 900 citra yang dipotret kamera pada robot inspeksi (1.280 x 720 piksel, 30 bingkai per detik). Pada deteksi, YOLO v8n-MAFP mencapai mAP@0,5 sebesar 96,9%, naik 2,4 poin persentase dari YOLO v8n (94,5%). Pada pelacakan, ALRM-Track mencapai MOTA 88,2%, HOTA 75,3%, IDF1 87,9%, dan hanya 2 kali pergantian ID, dibandingkan 16 kali pada ByteTrack asli.

Pada pencacahan, lima video rumah kaca menghasilkan galat absolut rata-rata (*mean absolute error*, MAE) 1,4 buah dan akurasi pencacahan rata-rata (ACP) 96,6%, lebih baik daripada pencacahan garis (MAE 5; ACP 88,0%) dan pencacahan wilayah (MAE 10,4; ACP 75,1%).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan tomat yang akurat diperlukan untuk penilaian hasil panen dan pengelolaan cerdas rumah kaca. Hitung manual tidak efisien, mahal, rentan melewatkan atau menghitung ganda, dan masuknya petugas berulang kali dapat mengganggu lingkungan tanam. Penulis membedakan pencacahan statis berbasis citra tunggal, yang terbatas oleh lebar bidang pandang dan perubahan sudut pandang sehingga sulit digabung menjadi estimasi area besar, dari pencacahan dinamis berbasis video yang mengombinasikan deteksi dengan pelacakan multi-objek.

Menurut penulis, metode pelacakan terdahulu menghitung ID unik hasil pelacakan, padahal penutupan oleh daun dan tumpukan buah menyebabkan kegagalan pencocokan sehingga ID berubah, yang meningkatkan buah terlewat dan penghitungan ganda. ByteTrack memakai ambang IoU tetap pada tahap asosiasi kedua; ketika deteksi berubah bentuk akibat penutupan atau gerak kamera, IoU antara deteksi dan prediksi Kalman dapat turun sementara di bawah ambang dan pasangan yang benar terbuang.

## Ide Utama
Ide utama ada pada tiga tingkat. Pertama, detektor diperbaiki untuk buah kecil dan tertutup lewat pengambilan sampel turun berbasis wavelet, kepala deteksi P2, dan atensi linear MLLA. Kedua, ambang asosiasi ByteTrack dibuat adaptif terhadap distribusi IoU pada bingkai berjalan, dan ditambahkan tahap ketiga "percobaan ulang" dengan ambang IoU sangat rendah. Ketiga, hitungan tidak lagi bergantung pada ID unik saja atau satu garis, melainkan pada urutan lintasan pusat kotak melewati dua zona di kedua sisi sumbu tengah, sehingga sebuah ID dihitung hanya bila terlihat di zona awal lalu zona akhir.

Dengan demikian, identitas buah dijaga dalam satu video dengan pelacakan, dan pencacahan dibuat lebih tahan terhadap pergantian ID dengan aturan lintas zona. Makalah tidak menyatukan identitas lintas video atau lintas sisi tanaman.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Kamera Hikvision Ezviz dipasang pada tiang naik-turun robot inspeksi, beresolusi 1.280 x 720 piksel dan 30 bingkai per detik. Robot bergerak dengan kecepatan tetap 0,5 m/s menyusuri jalur antarbaris; tinggi kamera dari tanah 0,6 m dan jarak lateral ke tanaman terdekat 0,4 m. Area pantau adalah zona buah matang pada ketinggian tanaman hingga 80 cm. Lokasi rumah kaca, kultivar tomat, dan jumlah video pelatihan tidak dilaporkan pada teks.

### 2. Anotasi dan pembagian data
Anotasi memakai LabelImg dengan kotak pembatas minimum. Hanya tomat yang dapat dikenali jelas dan tertutup kurang dari 50% yang dianotasi; tomat di belakang guludan atau jatuh di tanah tidak dianotasi. Sebanyak 900 citra asli dibagi 7:3 menjadi data latih dan validasi, lalu data latih diaugmentasi (pembalikan horizontal, derau Gauss, *motion blur*, pemangkasan dan pengisian acak, kecerahan dan kontras) hingga 2.000 citra.

### 3. Detektor YOLO v8n-MAFP
Modul Down_wt (pengambilan sampel turun wavelet) memakai transformasi Haar yang membagi fitur $H \times W \times C$ menjadi empat sub-pita frekuensi berukuran $[H/2, W/2, 4C]$, lalu unit Conv + BN + ReLU memadatkan kanal. Kepala deteksi P2 ditambahkan untuk objek kecil. Modul MLLA (*Mamba-inspired linear attention*) di ujung tulang punggung memiliki cabang lokal (proyeksi linear dan konvolusi kedalaman 3 x 3) serta cabang atensi linear global dengan gerbang lupa, yang digabung dengan perkalian elemen demi elemen dan koneksi residu. Pelatihan memakai transfer belajar dari bobot pralatih, SGD dengan momentum 0,937, peluruhan bobot 0,0005, laju belajar awal 0,0001, dan ukuran batch 16, pada GPU RTX 4090 24 GB.

### 4. Pelacakan ALRM-Track
Kerangkanya adalah *tracking-by-detection* berbasis ByteTrack: prediksi posisi dengan filter Kalman dan pencocokan Hungarian. Stage 1 mencocokkan deteksi skor tinggi dengan lintasan aktif memakai ambang IoU tetap yang ketat. Stage 2 mencocokkan sisa lintasan dengan deteksi skor rendah dengan ambang adaptif. Ambang dihitung dari $u_i = \max_j \mathrm{IoU}(d_i, t_j)$, nilai tengah $\mu = \mathrm{median}(u_1, \ldots, u_M)$, lalu $\tau_{adapt} = \max(0{,}2, \min(0{,}5, \mu))$. Stage 3 mencoba sekali lagi lintasan yang tersisa dengan ambang IoU sangat rendah (nilainya tidak dilaporkan) untuk menangkap sampel dengan skor rendah dan penyimpangan posisi besar.

### 5. Pencacahan dengan pencocokan wilayah berurutan
Pada kedua sisi sumbu tengah citra dibuat zona penyangga selebar 150 piksel: Region 0 (urutan awal) dan Region 1 (urutan akhir). Untuk setiap lintasan, bila pusat kotak berada di Region 0, ID dicatat di List0. Bila pusat berada di Region 1, ID dicatat di List1 dan, jika ID juga ada di List0, hitungan $O$ bertambah satu dan ID dihapus dari kedua daftar. Algoritme menerima label kelas pada setiap lintasan dan mengembalikan hitungan tomat matang, tetapi hitungan per kelas tidak dilaporkan.

## Eksperimen dan Hasil
Detektor dievaluasi pada data validasi (porsi 30% dari 900 citra, sekitar 270 citra; angka ini dihitung dari rasio 7:3, bukan dilaporkan langsung) dengan presisi, *recall*, mAP@0,5, mAP@0,5:0,95, dan jumlah parameter. Pelacakan dievaluasi dengan MOTA, HOTA, IDF1, dan IDSW (jumlah pergantian ID). Pencacahan dievaluasi pada lima video dengan acuan jumlah sebenarnya (GT). Cara memperoleh GT tidak diuraikan pada teks.

| Model deteksi | Presisi (%) | *Recall* (%) | mAP@0,5 (%) | Parameter |
|---|---|---|---|---|
| YOLO v8n | 87,7 | 88,0 | 94,5 | 3,01 x 10^6 |
| YOLO v5s | 86,1 | 86,5 | 93,4 | 7,20 x 10^6 |
| YOLO v7-tiny | 88,4 | 87,5 | 94,2 | 5,90 x 10^6 |
| YOLO v9n | 87,2 | 88,9 | 95,1 | 2,90 x 10^6 |
| YOLO 11n | 89,5 | 89,2 | 96,6 | 2,70 x 10^6 |
| YOLO v8n-MAFP | 92,5 | 90,6 | 96,9 | 3,08 x 10^6 |

Pada ablasi (Tabel 1), Down_wt saja menghasilkan mAP@0,5 95,2% dan mAP@0,5:0,95 73,7%; MLLA saja 95,7% dan 75,1%; kombinasi keduanya 96,9% dan 75,7%, dibandingkan baseline 94,5% dan 72,1%.

| Pelacak | IDSW | MOTA (%) | HOTA (%) | IDF1 (%) | FPS rata-rata |
|---|---|---|---|---|---|
| SORT | 28 | 74,9 | 67,0 | 76,7 | 24,6 |
| DeepSORT | 21 | 81,7 | 71,9 | 78,8 | 17,3 |
| BoT-SORT | 19 | 83,6 | 70,6 | 82,0 | 18,2 |
| ByteTrack asli | 16 | 84,9 | 71,8 | 82,5 | tidak dilaporkan |
| ALRM-Track | 2 | 88,2 | 75,3 | 87,9 | 23,8 |

Ablasi pelacak: ambang IoU adaptif saja menghasilkan MOTA 86,7%, HOTA 74,8%, IDF1 85,6%, IDSW 13; pencocokan ulang skor rendah saja 85,1%, 72,5%, 83,2%, dan 8; keduanya 88,2%, 75,3%, 87,9%, dan 2.

| Video | GT | Garis: hitungan (galat) | Wilayah: hitungan (galat) | Wilayah berurutan: hitungan (galat) |
|---|---|---|---|---|
| 01 | 46 | 40 (6) | 53 (7) | 45 (1) |
| 02 | 51 | 43 (8) | 65 (14) | 48 (3) |
| 03 | 37 | 35 (2) | 49 (12) | 37 (0) |
| 04 | 34 | 29 (5) | 43 (9) | 33 (1) |
| 05 | 41 | 37 (4) | 51 (10) | 41 (2) |
| MAE | | 5 | 10,4 | 1,4 |
| ACP (%) | | 88,0 | 75,1 | 96,6 |

Galat absolut kumulatif metode wilayah berurutan adalah 7 buah (teks), konsisten dengan penjumlahan kolom galat (dihitung: 1 + 3 + 0 + 1 + 2 = 7). Seluruh lima video diambil pada periode waktu dan pencahayaan yang sama, tetapi dengan tingkat penutupan daun dan buah yang berbeda.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: ALRM-Track menurunkan pergantian ID secara besar dengan kecepatan 23,8 bingkai per detik yang dinyatakan memenuhi kebutuhan waktu nyata; detektor tetap ringan (3,08 x 10^6 parameter); dan aturan lintas zona mengurangi penghitungan ganda dan buah terlewat dibandingkan pencacahan garis atau wilayah. Pencacahan garis dilaporkan sensitif terhadap penutupan tepi, dan pencacahan wilayah sensitif terhadap kehilangan target dan pergantian ID.

Penulis tidak memuat bagian keterbatasan khusus pada teks yang tersedia. Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan. Pertama, uji pencacahan hanya memakai lima video dengan GT 34 sampai 51 buah per video, sehingga hasil 96,6% belum mencerminkan variasi lokasi atau waktu. Kedua, hanya satu pencahayaan, dan rumah kaca serta kultivar tidak dirinci. Ketiga, evaluasi dilakukan pada jalur satu arah dengan kamera berjarak 0,4 m; aturan lintas sumbu tengah mengandaikan gerak kamera sejajar baris dan arah tetap, sehingga tidak berlaku langsung pada sudut pandang berbeda atau gerak balik. Keempat, deskripsi ambang adaptif tidak seragam: Seksi 2.2.2 memakai median IoU maksimum, sedangkan Seksi 2.2.3 menyebut rata-rata skor keyakinan. Kelima, ablasi pelacak dan pembandingan pelacak tidak merinci video yang dipakai. Keenam, tidak ada penyatuan identitas lintas video atau lintas sisi.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dalam satu video pindai lurus dengan pelacakan berbasis deteksi (Kalman, Hungarian, asosiasi skor tinggi dan rendah) ditambah aturan hitung lintas dua zona di sumbu tengah. Penutupan oleh daun dan tumpukan buah ditangani dengan asosiasi skor rendah adaptif dan percobaan ulang. Hitungan dilaporkan hanya sebagai total tomat matang per video, bukan per kelas kematangan. Acuan hitungnya adalah jumlah sebenarnya (GT) per video; sumber GT (hitung manual dari video atau lapangan) tidak diuraikan.

Untuk pencacahan tandan sawit multi-sisi, aturan lintas zona berurutan dan ambang IoU adaptif dapat dipindahkan sebagai cara mengurangi penghitungan ganda akibat pergantian ID dalam urutan video yang mengelilingi pohon. Namun, aturan itu bergantung pada gerak kamera yang beraturan dan satu arah, serta tidak menyatukan buah yang sama pada sisi pohon yang berbeda.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `feng2026greenhouse`.

Feng dkk. (2026) mengusulkan pencacahan tomat rumah kaca dari video robot inspeksi dengan YOLO v8n-MAFP (pengambilan sampel turun wavelet, kepala P2, atensi MLLA), pelacak ALRM-Track berbasis ByteTrack dengan ambang IoU adaptif dan pencocokan ulang skor rendah, serta pencacahan wilayah berurutan di sekitar sumbu tengah bingkai. Pada lima video, MAE adalah 1,4 buah dan ACP 96,6%, sedangkan pelacakan mencapai MOTA 88,2% dengan 2 pergantian ID.

Catatan verifikasi data: Teks berbahasa Mandarin dan telah diringkas dari bahasa aslinya; ekstraksi PDF terbaca baik, tetapi gambar tidak terbaca. Angka deteksi ada pada Tabel 1 (ablasi) dan Tabel 2 (perbandingan model); angka pelacakan pada Tabel 3 (ablasi) dan Tabel 4 (perbandingan); angka pencacahan pada Tabel 5 (Seksi 3.5). Jumlah citra validasi (sekitar 270) adalah turunan dari 900 x 30% dan bukan angka yang dilaporkan. Jumlah video pelatihan, lokasi, kultivar, cara memperoleh GT, jumlah iterasi pelatihan, dan nilai ambang IoU tahap ketiga tidak dilaporkan. Teks menyebut MOTA naik "6,5, 4,6, 13,3 poin persentase" terhadap DeepSORT, BoT-SORT, dan SORT, yang konsisten dengan Tabel 4.
