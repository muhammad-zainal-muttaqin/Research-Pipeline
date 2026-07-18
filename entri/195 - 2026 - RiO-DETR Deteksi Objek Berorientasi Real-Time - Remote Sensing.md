# 195 - RiO-DETR: DETR for Real-time Oriented Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hu2026riodetr` |
| Judul asli | RiO-DETR: DETR for Real-time Oriented Object Detection |
| Penulis | Zhangchi Hu, Yifan Zhao, Yansong Peng, Wenzhang Sun, Xiangchen Yin, Jie Chen, Peixi Wu, Hebei Li, Xinghao Wang, Dongsheng Jiang, Xiaoyan Sun |
| Tahun | 2026 |
| Venue | arXiv preprint arXiv:2603.09411 |
| Tema | Remote Sensing |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2603.09411
- **Google Scholar:** https://scholar.google.com/scholar?q=RiO-DETR%3A%20DETR%20for%20Real-time%20Oriented%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=RiO-DETR%3A%20DETR%20for%20Real-time%20Oriented%20Object%20Detection&sort=relevance

## Gambaran Umum

RiO-DETR adalah detektor transformer *real-time* pertama untuk deteksi objek berorientasi (*oriented object detection*), tugas mengeluarkan kotak pembatas berputar (*oriented bounding box*, OBB) alih-alih kotak aksis-sejajar biasa, sebagaimana dibutuhkan pada citra penginderaan jauh (*remote sensing*) tempat objek — kapal, kendaraan, lapangan — muncul dalam sudut sembarang. Makalah ini mengidentifikasi tiga kesulitan spesifik saat kerangka DETR (*Detection Transformer*, detektor berbasis *query* yang memprediksi himpunan objek tanpa *anchor* maupun *Non-Maximum Suppression*/NMS) diperluas ke OBB, lalu mengajukan tiga mekanisme untuk mengatasinya: estimasi sudut yang digerakkan konten (*Content-Driven Angle Estimation*) dengan atensi ortogonal terkoreksi rotasi, pemurnian periodik terpisah (*Decoupled Periodic Refinement*) dengan fungsi kerugian jalur-terpendek untuk sudut, dan augmentasi padat berorientasi (*Oriented Dense O2O*). Pada benchmark DOTA-1.0, DIOR-R, dan FAIR-1M-2.0, varian terbesar RiO-DETR (RiO-DETR-x) mencapai 81,8% AP50 pada DOTA-1.0 dengan latensi 29,9 milidetik, melampaui pembanding sekelas YOLO26x-obb (80,4% AP50, 30,5 ms) dan RHINO-DETR (79,4% AP50, 242,6 ms).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek berorientasi dibutuhkan ketika kotak aksis-sejajar (sisi selalu horizontal/vertikal) gagal membungkus objek secara rapat — kasus lazim pada citra udara, tempat kapal panjang atau pesawat dapat menghadap ke segala arah. Metode arus utama untuk OBB, seperti Oriented R-CNN atau S2A-Net, mewarisi kerangka dua tahap berbasis *anchor* (kotak kandidat berukuran dan berorientasi tetap yang disebar merata pada citra) dan memerlukan NMS berorientasi sebagai pasca-proses. Pendekatan ini akurat tetapi rumit dan lambat karena jumlah *anchor* per orientasi jauh lebih besar daripada deteksi aksis-sejajar.

Di sisi lain, RT-DETR (dibahas pada bab 155) membuktikan DETR dapat berjalan *real-time* untuk deteksi aksis-sejajar biasa dengan menghapus komponen *anchor* dan NMS sepenuhnya, menggantinya dengan pencocokan himpunan (*set-based matching*) antara prediksi dan kebenaran lapangan. Namun, memindahkan resep ini ke OBB tidak sederhana. RiO-DETR menunjukkan tiga kendala konkret: pertama, sudut orientasi bergantung pada semantik tekstur objek (arah serat, sumbu dominan), bukan semata posisi geometris, sehingga menyandikan sudut sebagai bagian dari *positional query* (representasi posisi yang dipelajari jaringan untuk menargetkan lokasi tertentu) justru menambah derau dan mengacaukan mekanisme atensi. Kedua, sudut bersifat periodik — 0 dan π secara geometris berdekatan meski secara numerik jauh — sehingga pemurnian bertahap gaya DETR yang memakai pembaruan aditif Euclidean menghasilkan gradien tidak kontinu di sekitar batas periode. Ketiga, derajat kebebasan tambahan dari sudut memperluas ruang pencarian pencocokan himpunan, memperlambat konvergensi pelatihan dibandingkan deteksi aksis-sejajar biasa.

## Ide Utama

Gagasan inti RiO-DETR adalah memisahkan penanganan sudut dari penanganan posisi-ukuran di seluruh tahap arsitektur DETR, alih-alih memperlakukan sudut sebagai dimensi kelima yang digabung begitu saja ke dalam representasi kotak (x, y, w, h). Pemisahan ini diterapkan pada tiga titik: representasi *query* (sudut tidak disandikan sebagai prior posisi, melainkan diregresi dari fitur konten), mekanisme atensi (sebagian kepala atensi menyampel searah objek, sebagian lagi tegak lurus terhadapnya), dan pemurnian iteratif (pembaruan posisi memakai skema Euclidean baku, sedangkan pembaruan sudut memakai skema terbatas-berkala yang menghormati periodisitas). Prinsip yang sama diterapkan pada fungsi kerugian dan strategi augmentasi data: keduanya dirancang ulang agar sadar bahwa sudut hidup pada lingkaran, bukan pada garis bilangan.

## Cara Kerja Langkah demi Langkah

### Estimasi Sudut yang Digerakkan Konten

Pada DETR baku, setiap *query* deteksi membawa *positional embedding* yang menyandikan perkiraan lokasi kotak. RiO-DETR membatasi *positional embedding* ini hanya pada empat dimensi spasial (pusat x, pusat y, lebar, tinggi) dan secara eksplisit mengeluarkan sudut θ darinya. Sudut kemudian diregresi dari *content embedding* (representasi fitur yang dipelajari dari isi citra, bukan dari posisi), sehingga jaringan dipaksa mengambil isyarat rotasi dari tekstur dan bentuk objek pada peta fitur, bukan dari prior geometris yang kaku. Pendekatan ini didukung oleh atensi ortogonal terkoreksi rotasi (*Rotation-Rectified Orthogonal Attention*): kepala atensi (unit paralel dalam mekanisme *multi-head attention* yang masing-masing mempelajari pola sampling berbeda) dibagi dua kelompok. Kelompok pertama menyampel fitur searah sumbu panjang objek dengan rotasi θ, kelompok kedua menyampel tegak lurus dengannya dengan rotasi θ + π/2. Pembagian ini mencegah *feature collapse* — kondisi ketika seluruh kepala atensi menumpuk pada sumbu utama objek sehingga struktur lateral (misalnya lebar kapal, bukan hanya panjangnya) kurang tertangkap — tanpa menambah parameter atau operasi hitung (*GFLOPs*) baru karena hanya arah sampling yang diubah.

### Pemurnian Periodik Terpisah dan Kerugian Jalur-Terpendek

DETR menghaluskan prediksi kotak secara bertahap lintas lapisan dekoder memakai pembaruan invers-sigmoid, cocok untuk koordinat yang hidup pada rentang linear [0,1]. RiO-DETR mempertahankan skema ini untuk posisi dan ukuran, tetapi mengganti pembaruan sudut dengan skema terbatas: θ_baru = θ_referensi + tanh(Δθ) × α, dengan α mengecil secara eksponensial di tiap lapisan dekoder (koreksi besar di lapisan awal, koreksi halus di lapisan akhir), diikuti normalisasi periodik yang memetakan hasil ke rentang [0, π). Skema ini disebut *Decoupled Periodic Refinement* karena posisi dan sudut dimurnikan dengan aturan berbeda meski berbagi lapisan dekoder yang sama.

Pemurnian ini dipasangkan dengan fungsi kerugian baru, *Shortest-Path Periodic Loss*, yang mengganti selisih absolut L1 baku dengan L_sudut = min(|θ_prediksi − θ_target|, π − |θ_prediksi − θ_target|). Contoh numerik: bila sudut target 5° dan prediksi 175°, selisih absolut biasa adalah 170°, padahal keduanya hampir berimpit secara geometris (selisih sebenarnya 10° bila kotak dianggap simetris pada kelipatan π). Rumus jalur-terpendek mengambil nilai minimum antara selisih langsung dan pelengkapnya terhadap π, sehingga gradien selalu mengikuti jarak sudut terpendek pada lingkaran, bukan jarak semu akibat pembungkusan periode.

### Oriented Dense O2O

*Dense O2O* (*one-to-one*, istilah untuk strategi memperkaya jumlah pasangan *query*-target unik per gambar guna mempercepat konvergensi pencocokan himpunan) pada RiO-DETR diperluas dengan menempelkan empat potongan citra ke dalam satu mozaik, masing-masing dirotasikan secara independen dan acak sebesar 0°, 90°, 180°, atau 270° sebelum digabung. Teknik ini disebut *Oriented Dense O2O*: tanpa menambah biaya komputasi, ia memperkaya keragaman sudut yang dilihat jaringan dalam satu iterasi pelatihan, sehingga mempercepat konvergensi estimasi sudut dibandingkan augmentasi mozaik biasa yang tidak memutar potongan.

Diagram berikut merangkum bagaimana jalur posisi dan jalur sudut berpisah sejak *query* dibentuk hingga kerugian dihitung:

```
fitur backbone (HGNet)
        │
        ▼
   query DETR ── posisi (cx,cy,w,h) ──► update invers-sigmoid ──► L1 posisi
        │
        └──────── sudut θ (dari content embedding)
                       │
                       ▼
            atensi ortogonal terkoreksi rotasi
              (separuh head: arah θ; separuh: θ+90°)
                       │
                       ▼
        update terbatas: θ_ref + tanh(Δθ)·α  (α mengecil per lapis)
                       │
                       ▼
              normalisasi periodik ke [0, π)
                       │
                       ▼
        Shortest-Path Periodic Loss: min(|Δθ|, π−|Δθ|)
```

Diagram ini menegaskan bahwa satu-satunya percabangan arsitektural inti RiO-DETR terletak pada perlakuan sudut: jalur posisi mengikuti resep DETR baku, sedangkan jalur sudut memakai atensi, pembaruan, dan kerugian yang dirancang khusus untuk mengakomodasi periodisitas dan ketergantungan semantik.

## Eksperimen dan Hasil

RiO-DETR dievaluasi pada tiga benchmark deteksi berorientasi: DOTA-1.0 (citra udara beragam kategori objek), DIOR-R (citra optik penginderaan jauh dengan anotasi berorientasi), dan FAIR-1M-2.0 (citra satelit resolusi tinggi berskala besar). Model disediakan dalam lima ukuran (n, s, m, l, x) memakai backbone keluarga HGNet berbeda, dengan parameter berkisar 4,0 juta (RiO-DETR-n, backbone HGNet-B0) hingga 62,5 juta (RiO-DETR-x, backbone HGNet-B5), dan beban komputasi 17 hingga 527 miliar operasi (GFLOPs).

Pada DOTA-1.0 skala tunggal, RiO-DETR-x mencapai 81,8% AP50 (*Average Precision* pada ambang IoU 0,5, metrik standar deteksi berorientasi) dengan latensi 29,9 milidetik, mengungguli YOLO26x-obb (80,4% AP50, 30,5 ms; bab 192) dan RHINO-DETR (79,4% AP50, 242,6 ms) — akurasi lebih tinggi dari YOLO26 pada latensi setara, dan delapan kali lebih cepat daripada RHINO-DETR pada akurasi yang mirip. Pada multi-skala DOTA-1.0, RiO-DETR-x mencatat 81,76% AP50, sedikit di atas YOLO26x-obb (81,70%). Pada DIOR-R, RiO-DETR-x mencapai 77,43% AP50 pada 17,31 ms, melampaui YOLO26x-obb (76,48%, 17,66 ms), sementara varian terkecil RiO-DETR-s mencatat 74,44% AP50 pada 3,01 ms — menunjukkan lini produk dengan titik keseimbangan kecepatan-akurasi berbeda. Pada FAIR-1M-2.0 multi-skala, RiO-DETR-x mencatat 47,4% AP50, di atas YOLO26x-obb (46,7%) dan metode berbasis CNN seperti LSKNet-S (46,3%) serta ReDet (43,2%).

Studi ablasi pada DIOR-R dengan RiO-DETR-m menelusuri kontribusi tiap komponen dari baseline RT-DETRv2 (varian RT-DETR yang ditambah kepala prediksi OBB) sebesar 70,35% AP50 hingga 75,73% AP50 setelah seluruh komponen ditambahkan bertahap — pencocokan Hausdorff dan kerugian KLD (*Kullback-Leibler Divergence* antar-distribusi Gaussian representasi kotak), pencocokan universal, Dense O2O, Content-Driven Angle Estimation, Decoupled Periodic Refinement, hingga Oriented Dense O2O — kenaikan total 5,38 poin. Ablasi lain menunjukkan bahwa memasukkan sudut langsung ke *positional query* justru menurunkan akurasi (72,34% AP50) dibandingkan representasi posisi-ukuran terpisah tanpa sudut (73,81%), mengonfirmasi bahwa penggabungan naif sudut ke posisi merugikan, bukan menguntungkan. Untuk konvergensi, Oriented Dense O2O mencapai 73,88% AP50 hanya dalam 60 *epoch* (satu putaran penuh atas data latih), lebih cepat daripada Dense O2O biasa (73,47% pada 68 *epoch*) dan augmentasi reguler (73,33% pada 86 *epoch*).

## Kelebihan dan Keterbatasan

RiO-DETR menghilangkan kebutuhan *anchor* berorientasi dan NMS berorientasi pada tugas OBB, mewarisi kesederhanaan pipeline yang sebelumnya hanya tersedia untuk deteksi aksis-sejajar melalui RT-DETR. Pemisahan eksplisit antara jalur posisi dan jalur sudut di representasi *query*, atensi, pemurnian, dan kerugian memberikan penjelasan mekanistik yang konsisten untuk setiap komponen, didukung ablasi yang menunjukkan setiap bagian menyumbang kenaikan akurasi. Rentang lima ukuran model memberi fleksibilitas memilih titik kecepatan-akurasi sesuai kebutuhan penerapan.

Dari sisi rekayasa, penulis makalah sendiri mencatat bahwa RiO-DETR masih memakai backbone (jaringan ekstraksi fitur awal) umum dari keluarga HGNet yang tidak dirancang khusus untuk citra penginderaan jauh, dan menyebut perancangan backbone real-time khusus deteksi berorientasi sebagai tantangan terbuka. Secara konseptual, generalisasi ke domain lain (radar apertur sintetis, hiperspektral) atau ke objek berbentuk mendekati persegi — kasus yang menurut ablasi augmentasi rotasi memberi manfaat lebih kecil karena ambiguitas orientasi — belum tercakup dalam eksperimen yang dilaporkan. Karena publikasi ini baru diunggah Maret 2026, belum ada validasi independen atau tinjauan sejawat penuh; ketersediaan kode yang dijanjikan penulis juga belum dapat diverifikasi pada saat penulisan bab ini.

## Kaitan dengan Bab Lain

RiO-DETR mewarisi kerangka *real-time end-to-end* DETR tanpa NMS yang dirintis RT-DETR (bab [155](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)) dan disempurnakan Co-DETR (bab [165](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md)) melalui pelatihan kolaboratif untuk mempercepat konvergensi pencocokan himpunan — masalah konvergensi yang sama, dalam konteks sudut tambahan, menjadi salah satu dari tiga kendala yang diatasi RiO-DETR. Di antara detektor real-time generasi 2025-2026, RiO-DETR berbagi filosofi efisiensi dengan YOLO26 (bab [192](./192%20-%202025%20-%20YOLO26%20Detektor%20Real-Time%20End-to-End%20-%20Fondasi%20RGB.md)), pembanding utama pada seluruh benchmark OBB di makalah ini, RF-DETR (bab [193](./193%20-%202025%20-%20RF-DETR%20NAS%20untuk%20Detektor%20Transformer%20Real-Time%20-%20Fondasi%20RGB.md)), dan Le-DETR (bab [194](./194%20-%202026%20-%20Le-DETR%20Encoder%20Efisien%20untuk%20DETR%20Real-Time%20-%20Fondasi%20RGB.md)), meski ketiganya menyasar deteksi aksis-sejajar, bukan berorientasi.

Pada klaster Remote Sensing, RiO-DETR melengkapi bab-bab berbasis YOLO yang menangani citra udara dengan kotak aksis-sejajar: TPH-YOLOv5 (bab [137](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md)) untuk deteksi objek kecil dari drone, UAV-YOLOv8 (bab [139](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md)), dan YOLT (bab [140](./140%20-%202018%20-%20YOLT%20%28Satellite%20Imagery%29%20-%20Remote%20Sensing.md)) untuk citra satelit berskala besar. Berbeda dari bab-bab tersebut, RiO-DETR menyasar representasi kotak berorientasi secara spesifik, menjadikannya rujukan bagi kasus objek berputar (kapal, kendaraan miring) yang tidak tercakup baik oleh formulasi kotak aksis-sejajar YOLO klasik.

## Poin untuk Sitasi

Kutip dengan kunci `hu2026riodetr`. Ringkasan yang aman dikutip: "RiO-DETR memperluas kerangka DETR real-time ke deteksi objek berorientasi dengan memisahkan penanganan sudut dari posisi pada representasi query, atensi, pemurnian iteratif, dan fungsi kerugian, mencapai 81,8% AP50 pada DOTA-1.0 dengan latensi 29,9 ms (varian RiO-DETR-x), melampaui YOLO26x-obb dan RHINO-DETR pada titik operasi yang sebanding."

Catatan verifikasi: seluruh angka pada bab ini (AP50 per varian dan dataset, latensi, jumlah parameter/GFLOPs, hasil ablasi, jumlah epoch konvergensi) diambil dari versi HTML arXiv v1 (2603.09411) hasil ekstraksi otomatis, bukan pembacaan langsung tabel PDF asli oleh penulis bab — sebelum sitasi formal, cocokkan ulang setiap angka dengan tabel dan gambar pada PDF resmi. Karena makalah ini diunggah Maret 2026, belum ada versi terbit (published version), tinjauan sejawat independen, atau repositori kode terverifikasi; daftar penulis, definisi RHINO-DETR sebagai pembanding, dan status ketersediaan kode juga perlu dikonfirmasi ulang terhadap naskah final sebelum dipakai dalam karya formal.
