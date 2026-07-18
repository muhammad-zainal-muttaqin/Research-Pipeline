# 189 - Cross-Modality Fusion Transformer for Multispectral Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fang2022cft` |
| Judul asli | Cross-Modality Fusion Transformer for Multispectral Object Detection |
| Penulis | Qingyun Fang, Dapeng Han, Zhaokui Wang |
| Tahun | 2021 (arXiv), diproses untuk *Image and Vision Computing* |
| Venue | arXiv preprint arXiv:2111.00273 |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2111.00273
- **Kode resmi (GitHub):** https://github.com/DocF/multispectral-object-detection
- **Google Scholar:** https://scholar.google.com/scholar?q=Cross-Modality%20Fusion%20Transformer%20for%20Multispectral%20Object%20Detection

## Gambaran Umum

Makalah ini memperkenalkan CFT (*Cross-Modality Fusion Transformer*, Transformer fusi lintas-modal), sebuah modul yang menyisipkan mekanisme *self-attention* Transformer ke dalam *backbone* (jaringan penarik fitur) dua aliran YOLOv5 untuk menggabungkan citra RGB (merah-hijau-biru, citra warna biasa) dan citra termal (inframerah panjang gelombang jauh yang merekam suhu permukaan objek). Alih-alih menggabungkan fitur kedua modalitas secara bertahap dengan operasi konvolusi seperti pada metode sebelumnya, CFT mengubah peta fitur RGB dan termal menjadi barisan token, menggabungkan token dari kedua modalitas, lalu memprosesnya bersama dengan satu blok *encoder* Transformer.

Pendekatan ini diuji pada tiga dataset dengan karakteristik berbeda: FLIR (citra jalan siang-malam), VEDAI (citra udara), dan LLVIP (citra pejalan kaki malam hari beresolusi tinggi). Pada ketiganya, penyisipan modul CFT meningkatkan akurasi deteksi dibandingkan YOLOv5 dua aliran tanpa Transformer. Kontribusi utama makalah adalah menunjukkan bahwa fusi berbasis *attention* global menangkap ketergantungan antar-modal yang tidak terjangkau oleh konvolusi lokal, sambil tetap dapat dipasang sebagai modul tambahan pada arsitektur detektor yang sudah ada.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Detektor objek yang hanya memakai citra RGB — termasuk seluruh keluarga YOLO yang dibahas pada klaster Fondasi RGB, misalnya YOLOv1 (bab 001) — mengandalkan warna dan tekstur permukaan. Pada cahaya rendah, kabut, atau malam hari, kontras dan tekstur pada citra RGB menyusut sehingga tingkat kegagalan deteksi meningkat, terutama untuk objek bersuhu tubuh seperti pejalan kaki. Citra termal tidak bergantung pada pencahayaan tampak karena merekam radiasi panas, tetapi resolusinya lebih rendah dan tidak memuat informasi warna atau tekstur permukaan halus, sehingga objek dengan bentuk mirip pada suhu serupa sulit dibedakan.

Kombinasi kedua modalitas ini melahirkan sejumlah metode fusi RGB-termal sebelum CFT. Pendekatan fusi CNN (jaringan saraf konvolusi) bertahap, misalnya *halfway fusion*, menggabungkan peta fitur kedua modalitas pada satu titik tertentu di tengah jaringan memakai operasi seperti penjumlahan atau penggabungan kanal. MBNet (bab 102) menambahkan mekanisme untuk menangani ketimpangan keandalan antar-modal (*modality imbalance* — kondisi saat satu modal lebih dapat dipercaya daripada yang lain tergantung pencahayaan), sedangkan GAFF (bab 103) memakai *attention* berpemandu untuk memberi bobot fitur tiap modal. Namun, seluruh pendekatan ini beroperasi lewat konvolusi, yang secara alami hanya melihat wilayah lokal (ditentukan oleh ukuran *kernel*). Interaksi antar-piksel yang berjauhan pada satu modal (ketergantungan jarak jauh, *long-range dependency*) maupun antar-modal pada posisi berbeda sulit ditangkap tanpa menumpuk banyak lapisan konvolusi. Masalah inilah yang menjadi sasaran CFT: menyediakan mekanisme fusi yang dapat mempertimbangkan seluruh posisi peta fitur sekaligus, bukan hanya jendela lokal.

## Ide Utama

Gagasan inti CFT adalah memperlakukan penggabungan fitur RGB dan termal sebagai satu masalah *self-attention* atas satu barisan token gabungan, bukan sebagai operasi konvolusi terpisah per modal. Peta fitur konvolusi dari cabang RGB dan cabang termal, yang masing-masing berbentuk tiga dimensi (tinggi × lebar × kanal), diratakan (*flatten*) menjadi barisan vektor — setiap posisi spasial pada peta fitur menjadi satu token, mirip token kata pada teks. Token dari kedua modal digabungkan menjadi satu barisan panjang, ditambah *positional embedding* (penyandian posisi yang dapat dipelajari, agar Transformer tetap mengetahui letak asli tiap token setelah diratakan), lalu diproses oleh *encoder* Transformer standar dengan *multi-head self-attention* (perhatian diri bercabang, setiap token dapat "melihat" dan menimbang seluruh token lain saat memperbarui representasinya).

Karena token RGB dan token termal berada dalam satu barisan yang sama, *self-attention* secara otomatis menghitung dua jenis relasi sekaligus: relasi antar-token dalam modal yang sama (fusi intra-modal, mis. antar-bagian tubuh pejalan pada citra RGB) dan relasi antar-token lintas modal (fusi inter-modal, mis. antara wilayah bersuhu tinggi pada citra termal dan wilayah bertekstur pada citra RGB pada posisi yang sama). Kedua jenis fusi ini terjadi dalam satu operasi matriks tanpa desain terpisah untuk masing-masing, berbeda dari metode CNN yang umumnya memerlukan modul khusus untuk tiap jenis interaksi.

## Cara Kerja Langkah demi Langkah

### Backbone Dua Aliran

Arsitektur dasar CFT memakai YOLOv5 dengan *backbone* CSPDarknet53 (jaringan konvolusi berlapis dengan koneksi *cross-stage partial* yang memecah aliran data untuk mengurangi komputasi berulang) yang diduplikasi menjadi dua cabang paralel: satu menerima citra RGB, satu menerima citra termal. Kedua cabang mengekstrak fitur secara independen pada beberapa tahap kedalaman, menghasilkan peta fitur dengan resolusi spasial yang menyusut dan jumlah kanal yang membesar pada tiap tahap, sama seperti *backbone* YOLOv5 biasa.

### Modul CFT: Tokenisasi dan Self-Attention

Pada titik tertentu di tiap tahap, peta fitur RGB berukuran H×W×C dan peta fitur termal berukuran sama diratakan menjadi (H×W) token berdimensi C, kemudian keduanya digabungkan menjadi satu barisan sepanjang 2×(H×W) token. *Positional embedding* ditambahkan pada tiap token agar informasi posisi spasial dan asal-modal tidak hilang setelah perataan. Barisan ini melewati blok *encoder* Transformer: lapisan *multi-head self-attention* dengan koneksi sisa (*residual connection*) dan normalisasi lapisan (*layer normalization*), diikuti jaringan umpan-maju (*feed-forward network*) posisi-demi-posisi. Keluaran Transformer, dengan panjang barisan yang sama, ditata ulang (*reshape*) kembali menjadi dua peta fitur H×W×C dan dipisah kembali menurut asal modalnya untuk dilanjutkan ke tahap konvolusi berikutnya pada tiap cabang.

Skema alur satu modul CFT pada satu tahap *backbone*:

```
peta fitur RGB          peta fitur termal
  H x W x C                H x W x C
      |                        |
   flatten                  flatten
      |                        |
      +---------+   +----------+
                |   |
         gabung token: 2(HW) x C
                 |
        + positional embedding
                 |
      encoder Transformer
   (self-attention + FFN)
                 |
        pisah & reshape
      |                        |
  H x W x C                H x W x C
  (RGB terfusi)          (termal terfusi)
      |                        |
  lanjut konvolusi        lanjut konvolusi
  cabang RGB               cabang termal
```

Menurut deskripsi kode resmi, tiga modul CFT semacam ini disisipkan pada tiga kedalaman berbeda di *backbone*, sehingga fusi lintas-modal terjadi berulang pada beberapa skala resolusi, bukan hanya sekali di tengah jaringan seperti pada *halfway fusion*.

### Neck dan Head

Setelah *backbone* dua aliran dengan tiga titik fusi CFT, fitur dari kedua cabang pada tahap akhir digabungkan (mengikuti praktik YOLOv5, umumnya lewat konkatenasi kanal) sebelum masuk ke *neck* — struktur PANet (*Path Aggregation Network*, jaringan agregasi jalur yang menggabungkan fitur berbagai skala) — dan *head* deteksi standar YOLOv5 yang memprediksi kotak pembatas, skor keyakinan, dan kelas objek pada tiga skala grid.

## Eksperimen dan Hasil

Modul CFT diuji dengan menyisipkannya ke YOLOv5 dua aliran dan membandingkan hasilnya dengan YOLOv5 dua aliran tanpa Transformer (fusi lewat konkatenasi biasa) sebagai baseline, pada tiga dataset publik. Menurut hasil yang dilaporkan pada repositori kode resmi:

Pada FLIR (dataset citra jalan raya siang-malam berpasangan RGB-termal), mAP50 (rata-rata presisi pada ambang *Intersection over Union* 0,5) naik dari 73,0% pada baseline menjadi 78,7% dengan CFT, dan mAP (dirata-ratakan pada rentang ambang IoU 0,5–0,95) naik dari 37,4% menjadi 40,2%. Kenaikan 5,7 poin pada mAP50 menunjukkan CFT terutama memperbaiki deteksi yang sudah cukup tepat posisinya, sedangkan kenaikan mAP yang lebih kecil menandakan sebagian kotak masih kurang presisi pada ambang IoU ketat.

Pada VEDAI (dataset citra udara untuk deteksi kendaraan), mAP50 naik dari 79,7% menjadi 85,3%, dan mAP naik dari 46,8% menjadi 56,0% — kenaikan 9,2 poin pada mAP merupakan perbaikan relatif terbesar di antara ketiga dataset, menunjukkan fusi berbasis Transformer memberi manfaat lebih besar pada citra udara dengan objek kecil dan rapat.

Pada LLVIP (dataset pejalan kaki malam hari beresolusi tinggi), metrik yang dipakai adalah *log-average miss rate* (rata-rata logaritmik tingkat kelewatan — proporsi objek yang gagal terdeteksi, dirata-ratakan pada beberapa titik operasi; semakin kecil semakin baik). Nilainya turun dari 6,91% pada baseline menjadi 5,40% dengan CFT, penurunan 1,51 poin yang menunjukkan lebih sedikit pejalan kaki terlewat pada kondisi malam.

Konsistensi kenaikan akurasi pada tiga domain berbeda — jalan raya, udara, dan pejalan kaki malam — menjadi bukti utama makalah bahwa fusi berbasis *self-attention* bermanfaat secara umum, bukan hanya pada satu jenis skenario RGB-termal.

## Kelebihan dan Keterbatasan

Kelebihan utama CFT terletak pada kesederhanaan integrasinya: modul ini dipasang di titik-titik tertentu pada *backbone* yang sudah ada tanpa mengubah *neck* atau *head* deteksi, sehingga dapat dicangkokkan ke detektor berbasis YOLO lain dengan penyesuaian minimal. Mekanisme *self-attention* juga menyatukan fusi intra- dan inter-modal dalam satu operasi, menghindarkan kebutuhan merancang modul terpisah untuk tiap jenis interaksi seperti pada metode berbasis *attention* berpemandu sebelumnya. Perbaikan akurasi yang konsisten pada tiga dataset dengan karakteristik objek dan sudut pandang berbeda menunjukkan generalisasi metode.

Dari sisi rekayasa, penyisipan tiga modul *self-attention* pada beberapa skala menambah biaya komputasi dibandingkan *backbone* konvolusi murni, karena kompleksitas *self-attention* tumbuh kuadratik terhadap panjang barisan token — pada peta fitur beresolusi tinggi di tahap awal *backbone*, jumlah token bisa besar sehingga biaya memori dan waktu komputasi meningkat tajam. Makalah tidak melaporkan secara eksplisit angka FPS (*frame per second*) atau jumlah parameter tambahan akibat CFT dalam ringkasan yang tersedia, sehingga trade-off kecepatan-akurasi belum sepenuhnya terverifikasi dari sumber yang diakses. Secara konseptual, metode ini juga mensyaratkan pasangan citra RGB-termal yang sudah selaras secara spasial (teregistrasi); bila kalibrasi kedua kamera tidak presisi, token pada posisi yang sama dari kedua modal tidak lagi merujuk objek fisik yang sama, sehingga fusi *self-attention* berisiko menggabungkan informasi yang salah pasangan.

## Kaitan dengan Bab Lain

CFT memakai YOLOv5 sebagai kerangka detektor dasar, yang mewarisi formulasi grid dan regresi langsung dari YOLOv1 (bab 001) serta jalur pengembangan *backbone* CSPDarknet yang mulai dipakai pada generasi YOLOv4 (bab 004). Mekanisme *self-attention* yang menjadi inti CFT berakar pada arsitektur Transformer yang diadaptasi untuk citra oleh Vision Transformer (bab 024); CFT menerapkan prinsip yang sama pada peta fitur konvolusi menengah, bukan pada citra mentah yang dipecah menjadi *patch* seperti pada ViT.

Dalam klaster Pedestrian RGB-T, CFT berdiri di atas dataset KAIST (bab 100) yang menjadi tolok ukur awal deteksi pejalan multispektral, dan berdialog langsung dengan metode fusi CNN sebelumnya: IAF R-CNN (bab 101) yang memakai bobot sadar-cahaya, MBNet (bab 102) yang menangani ketimpangan modal, GAFF (bab 103) yang memakai *attention* berpemandu tanpa Transformer penuh, dan Cyclic Fuse-and-Refine (bab 104) yang memakai skema fusi siklik. CMPD (bab 105), yang terbit pada tahun yang sama, menempuh jalur berbeda dengan menambahkan ketidakpastian sebagai pemandu fusi. CFT menjadi rujukan bagi metode-metode fusi RGB-termal berbasis Transformer yang terbit setelahnya, yang umumnya membandingkan diri terhadap angka CFT sebagai baseline Transformer pertama pada tugas ini.

## Poin untuk Sitasi

Kutip dengan kunci `fang2022cft`. Ringkasan yang aman dikutip: "CFT menyisipkan modul *self-attention* Transformer ke dalam *backbone* dua aliran YOLOv5, menggabungkan token RGB dan termal menjadi satu barisan sehingga fusi intra-modal dan inter-modal terjadi dalam satu operasi, dan meningkatkan akurasi deteksi pada dataset FLIR, VEDAI, dan LLVIP dibandingkan fusi konvolusi biasa." Angka mAP50/mAP pada FLIR (73,0→78,7 / 37,4→40,2), VEDAI (79,7→85,3 / 46,8→56,0), dan *miss rate* LLVIP (6,91%→5,40%) berasal dari tabel hasil pada repositori kode resmi (DocF/multispectral-object-detection) dan sebaiknya dicocokkan ulang dengan tabel pada naskah arXiv final sebelum dikutip dalam karya formal. Penggunaan dataset KAIST oleh makalah ini, jumlah parameter tambahan, dan kecepatan inferensi (FPS) tidak berhasil diverifikasi secara pasti dari sumber yang diakses dan perlu dicek langsung pada teks lengkap arXiv:2111.00273 sebelum disitasi.
