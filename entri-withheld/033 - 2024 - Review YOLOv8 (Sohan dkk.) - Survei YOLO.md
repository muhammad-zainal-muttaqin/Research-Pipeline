# 033 - A Review on YOLOv8 and Its Advancements

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sohan2024yolov8review` |
| Judul asli | A Review on YOLOv8 and Its Advancements |
| Penulis | Mupparaju Sohan, Thotakura Sai Ram, Ch. Venkata Rami Reddy |
| Tahun | 2024 |
| Venue | Data Intelligence and Cognitive Informatics (seri *Algorithms for Intelligent Systems*, Springer), hal. 529–545, DOI 10.1007/978-981-99-7962-2_39 |
| Tema | Survei YOLO |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1007/978-981-99-7962-2_39
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Review%20on%20YOLOv8%20and%20Its%20Advancements
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=A%20Review%20on%20YOLOv8%20and%20Its%20Advancements&sort=relevance
- **Dokumentasi resmi YOLOv8 (rujukan teknis pendamping):** https://docs.ultralytics.com/models/yolov8/

## Gambaran Umum

Bab ini adalah tinjauan terhadap YOLOv8, detektor objek yang dirilis Ultralytics pada 10 Januari 2023. Tinjauan ini mengisi celah dokumentasi yang khas: Ultralytics tidak menerbitkan makalah formal untuk YOLOv8 — informasi tentangnya tersebar di repositori kode dan dokumentasi daring — sehingga bab semacam ini menjadi rujukan akademis yang dapat disitasi untuk model tersebut.

Isi tinjauan mencakup tiga hal. Pertama, arsitektur YOLOv8: *backbone* (jaringan pengekstrak fitur) dengan blok C2f, *neck* penggabung fitur multi-skala, dan *head* (kepala prediksi) yang terpisah serta bebas jangkar (*anchor-free*). Kedua, dukungan multi-tugas: satu kerangka untuk deteksi objek, segmentasi instans, estimasi pose, klasifikasi, dan deteksi berorientasi. Ketiga, rangkuman tolok ukur COCO untuk kelima skala model (n, s, m, l, x). Hasil utamanya bersifat dokumentatif: pembaca memperoleh satu acuan ringkas tentang apa yang berubah relatif terhadap YOLOv5–v7 dan apa kemampuan tiap variannya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Silsilah YOLO (bab 001) merumuskan deteksi objek sebagai regresi satu tahap yang cepat. Sejak YOLOv2, keluarga ini memakai *anchor box*: sekumpulan kotak acuan berukuran tetap yang disebar pada setiap sel grid, dan jaringan memprediksi koreksi terhadap kotak-kotak acuan itu, bukan koordinat objek secara langsung. Desain berbasis jangkar menanggung dua biaya. Pertama, ukuran dan jumlah jangkar adalah hiperparameter yang harus disetel per dataset; jangkar yang keliru menurunkan *recall*. Kedua, jangkar memperbanyak kandidat prediksi, sehingga menambah beban pasca-pemrosesan.

YOLOX (bab 005) pada 2021 menunjukkan bahwa jangkar dapat dilepaskan: kepala prediksi dibuat *anchor-free* dan dipisah (*decoupled*) menjadi cabang klasifikasi dan cabang regresi kotak. YOLOv7 (bab 007) pada 2022 memperkenalkan ELAN, struktur blok yang mengatur aliran gradien dengan menggabungkan keluaran banyak lapisan secara berlapis. Ketika YOLOv8 muncul pada awal 2023, model ini merangkai kedua gagasan tersebut — kepala *anchor-free* terpisah dan blok turunan ELAN bernama C2f — tetapi tanpa makalah pendamping. Bagi peneliti dan praktisi, pertanyaan praktisnya sederhana: apa sebenarnya isi YOLOv8, apa bedanya dengan pendahulunya, dan seberapa baik kinerjanya? Tinjauan Sohan dkk. disusun untuk menjawab pertanyaan itu dalam satu dokumen.

## Ide Utama

Gagasan inti YOLOv8 yang didokumentasikan bab ini dapat dinyatakan dalam satu kalimat: deteksi objek dilakukan tanpa kotak acuan, dengan kepala prediksi yang memisahkan tugas regresi kotak dan klasifikasi, di atas *backbone* yang memakai blok C2f, dalam satu kerangka yang sama untuk lima tugas penglihatan komputer.

Secara mekanis, perubahan terpenting terjadi pada keluaran jaringan. Pada YOLO berjangkar, setiap sel grid mengeluarkan koreksi terhadap sejumlah jangkar. Pada YOLOv8, setiap titik grid langsung memprediksi empat jarak dari titik itu ke sisi kiri, atas, kanan, dan bawah kotak objek, ditambah skor kelas. Hiperparameter ukuran jangkar hilang dan jumlah kandidat prediksi menyusut. Sementara itu, blok C2f memperkaya aliran gradien dengan menggabungkan keluaran semua sub-bloknya, bukan hanya keluaran terakhir, sehingga fitur yang dipelajari lebih kaya tanpa banyak tambahan biaya.

## Cara Kerja Langkah demi Langkah

### Kerangka Tiga Bagian

Seperti detektor YOLO lain, YOLOv8 terdiri atas tiga bagian berurutan. *Backbone* menerima citra masukan (standar tolok ukur: 640×640 piksel) dan mengekstrak peta fitur pada tiga skala resolusi: 80×80, 40×40, dan 20×20 (masing-masing disebut P3, P4, P5). Skala besar menangkap objek kecil, skala kecil menangkap objek besar. *Neck* menggabungkan ketiga skala secara dua arah (dari fitur dangkal ke dalam dan sebaliknya) mengikuti pola PAN (*Path Aggregation Network*), yaitu struktur yang menyalurkan informasi lokasi dari fitur beresolusi tinggi ke fitur beresolusi rendah. *Head* kemudian menghasilkan prediksi akhir pada setiap skala.

Alur data lengkapnya diringkas pada diagram berikut:

```
citra 640x640x3
      |
      v
+-- BACKBONE (Conv + blok C2f) ---------------+
|  peta fitur P3: 80x80, P4: 40x40, P5: 20x20 |
+------+-------------+-------------+----------+
       v             v             v
+-- NECK (penggabungan dua arah, gaya PAN) ---+
|  fitur tiga skala dilebur dan disebar balik |
+------+-------------+-------------+----------+
       v             v             v
+-- HEAD terpisah, anchor-free (per skala) ---+
|  cabang kotak : 2 conv -> 4x16 kanal (DFL)  |
|  cabang kelas : 2 conv -> 80 kanal (COCO)   |
+----------------------+----------------------+
                       v
        jarak (kiri,atas,kanan,bawah) dari titik
        grid + skor kelas -> NMS -> deteksi
```

Diagram menunjukkan aliran dari citra ke deteksi: tiga skala fitur diekstrak, dilebur di *neck*, lalu dinilai oleh kepala yang sama strukturnya pada tiap skala. *Non-Maximum Suppression* (NMS) pada ujungnya membuang kotak ganda: dari sekumpulan kotak yang saling tumpang tindih untuk objek yang sama, hanya kotak berskor tertinggi yang dipertahankan.

### Blok C2f pada Backbone

C2f adalah blok ekstraksi fitur berjenis CSP (*Cross Stage Partial*). Prinsip CSP: aliran fitur dibelah dua; satu cabang diolah oleh serangkaian sub-blok, cabang lain dilewatkan langsung, lalu keduanya digabung kembali. Pembelahan ini mengurangi perhitungan berulang dan memperbaiki aliran gradien saat pelatihan.

Mekanisme C2f, sesuai implementasi resminya, berjalan sebagai berikut. Konvolusi pertama menggandakan kanal menjadi 2c, lalu peta fitur dibelah menjadi dua bagian masing-masing c kanal. Satu bagian dipertahankan apa adanya; bagian kedua masuk ke rangkaian n sub-blok *bottleneck* (sub-blok yang menyempitkan lalu mengembangkan kanal untuk menekan biaya). Yang membedakan C2f dari blok C3 pada YOLOv5: keluaran **setiap** sub-blok ikut digabung, bukan hanya keluaran terakhir. Hasil gabungan berukuran (2 + n) × c kanal kemudian dipadatkan konvolusi kedua menjadi c kanal keluaran. Pada blok dengan n = 3 sub-blok, lima peta fitur digabungkan — dua dari pembelahan awal dan tiga dari tiap sub-blok. Struktur ini melanjutkan gagasan ELAN dari YOLOv7: aliran gradien dibuat lebih panjang dan lebih beragam agar jaringan belajar fitur yang lebih kaya.

### Kepala Terpisah dan Bebas Jangkar

Kepala YOLOv8 *decoupled* (terpisah): regresi kotak dan klasifikasi dihitung oleh dua cabang konvolusi yang berbeda, karena kedua tugas itu menuntut fitur yang berbeda sifatnya. Cabang kotak terdiri atas dua konvolusi 3×3 diikuti konvolusi akhir yang mengeluarkan 4 × 16 = 64 kanal; cabang kelas mengeluarkan sejumlah kanal sama dengan jumlah kelas (80 pada COCO).

Angka 16 adalah parameter *Distribution Focal Loss* (DFL). Alih-alih memprediksi satu angka untuk setiap sisi kotak, jaringan memprediksi distribusi probabilitas atas 16 nilai diskrit untuk tiap sisi, dan nilai akhir diambil sebagai nilai harapannya. Representasi distribusi ini membuat regresi lebih presisi pada tepi objek yang kabur. Karena tidak ada jangkar, prediksi berbentuk jarak dari titik grid ke keempat sisi kotak. Sebagai contoh numerik: pada skala P3 (80×80 untuk citra 640×640), satu titik grid mewakili wilayah 8×8 piksel; bila titik itu berada 24 piksel di kanan sisi kiri objek dan 40 piksel di bawah sisi atasnya, target regresinya adalah jarak (24, 40, dan dua jarak lainnya) dibagi langkah grid 8, yaitu (3, 5, …).

### Fungsi Loss dan Penetapan Target

Pelatihan memakai tiga komponen loss, sesuai kode sumber resmi: (1) *Binary Cross-Entropy* untuk skor kelas, yang menilai tiap kelas secara independen; (2) loss CIoU untuk kotak, yaitu penalti berbasis IOU (*Intersection over Union* — rasio luas irisan terhadap luas gabungan kotak prediksi dan kotak benar) yang ditambah suku jarak pusat dan konsistensi rasio aspek; (3) DFL untuk distribusi jarak sisi kotak.

Penetapan target positif memakai *Task-Aligned Assigner*: untuk setiap objek benar, 10 titik grid dengan skor keselarasan tertinggi dipilih sebagai penanggung jawab prediksi. Skor keselarasan menggabungkan skor klasifikasi dan IOU secara berbobot (pangkat α = 0,5 untuk skor kelas dan β = 6 untuk IOU), sehingga titik terpilih adalah titik yang sekaligus yakin kelasnya dan tepat kotaknya, bukan sekadar titik yang secara geometris dekat pusat objek.

### Dukungan Multi-Tugas

Kerangka yang sama diperluas ke empat tugas lain dengan mengganti kepala. Segmentasi instans menambah cabang *prototype*: jaringan menghasilkan 32 peta prototipe masker untuk seluruh citra dan tiap deteksi memprediksi 32 koefisien; masker akhir objek adalah kombinasi linear prototipe dengan koefisien itu, dipotong pada kotak deteksi. Estimasi pose menambah cabang titik kunci (17 titik tubuh manusia pada COCO). Klasifikasi mengganti kepala deteksi dengan pengklasifikasi biasa. Deteksi berorientasi (OBB) menambah prediksi sudut rotasi kotak. Tiap varian tersedia dalam lima skala: n (*nano*), s (*small*), m (*medium*), l (*large*), x (*extra-large*).

## Eksperimen dan Hasil

Sebagai tinjauan, bab ini tidak menjalankan eksperimen baru; evaluasinya berupa rangkuman tolok ukur COCO dari sumber resmi Ultralytics. Metrik utamanya mAP 50-95 (*mean Average Precision* yang dirata-rata pada ambang IOU 0,50 sampai 0,95): semakin tinggi semakin baik, dan penilaian pada banyak ambang membuatnya lebih ketat daripada mAP pada satu ambang. Angka resmi untuk model deteksi pada citra 640 piksel:

| Model | mAP 50-95 (%) | Latensi A100 TensorRT (ms) | Parameter (juta) | FLOPs (miliar) |
|---|---|---|---|---|
| YOLOv8n | 37,3 | 0,99 | 3,2 | 8,7 |
| YOLOv8s | 44,9 | 1,20 | 11,2 | 28,6 |
| YOLOv8m | 50,2 | 1,83 | 25,9 | 78,9 |
| YOLOv8l | 52,9 | 2,39 | 43,7 | 165,2 |
| YOLOv8x | 53,9 | 3,53 | 68,2 | 257,8 |

Interpretasinya terbaca pada dua arah. Menurun secara ukuran: YOLOv8n mempertahankan 37,3% mAP dengan hanya 3,2 juta parameter dan latensi di bawah satu milidetik per citra pada GPU A100 — layak untuk penerapan waktu nyata di perangkat terbatas. Menaik secara ukuran: dari n ke x, mAP naik 16,6 poin tetapi parameter membesar 21 kali lipat dan FLOPs hampir 30 kali lipat; lonjakan terbesar terjadi antara s dan m (+5,3 poin), sementara dari l ke x hanya bertambah 1,0 poin untuk biaya komputasi 1,6 kali lipat — tanda jenuhnya skala model pada dataset ini. Rentang latensi 0,99–3,53 ms per citra (setara kasar 280–1000 FPS) menegaskan posisi YOLOv8 sebagai detektor waktu nyata di seluruh skalanya.

## Kelebihan dan Keterbatasan

Sebagai objek tinjauan, YOLOv8 unggul pada tiga hal: desain *anchor-free* menghapus hiperparameter jangkar yang sensitif; satu kerangka melayani lima tugas sehingga ekosistem pemakaiannya seragam; dan kelima skalanya menutup rentang kebutuhan dari perangkat kecil sampai server. Tinjauan Sohan dkk. sendiri bernilai karena YOLOv8 tidak berdokumen formal — bab ini menyediakan deskripsi terstruktur yang dapat disitasi.

Keterbatasannya juga jelas. Pertama, tinjauan ini bersifat satu versi: cakupannya berhenti pada YOLOv8 sehingga cepat tertinggal oleh generasi berikutnya. Kedua, angka tolok ukurnya bersumber dari pengembang model itu sendiri, bukan pengujian ulang independen, dan angka dari pembuat model cenderung disajikan pada kondisi terbaik. Ketiga, dari sisi rekayasa, YOLOv8 tetap bergantung pada NMS, sehingga waktu inferensi akhir tidak sepenuhnya ditentukan jaringan — masalah yang baru ditangani pada YOLOv10. Keempat, lisensi AGPL-3.0 pada pustaka resminya membatasi pemakaian komersial tertutup.

## Kaitan dengan Bab Lain

Bab ini berdiri di ujung garis pewarisan yang panjang. Formulasi satu tahap "citra masuk, deteksi keluar" diwarisi dari bab 001 ([YOLOv1](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)); pelepasan jangkar dan pemisahan kepala prediksi dipelopori bab 005 ([YOLOX](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)); dan blok C2f melanjutkan prinsip agregasi gradien ELAN dari bab 007 ([YOLOv7](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)). Ketergantungan pada NMS menjadi sasaran perbaikan pada bab 009 ([YOLOv10](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md)). Dalam klaster survei, bab ini melengkapi bab 032 ([YOLO Evolution Benchmark](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md)): bab 032 menilai banyak versi YOLO secara komparatif, sedangkan bab ini membedah satu versi secara mendalam. Karena YOLOv8 menjadi tulang punggung deteksi 2D pada banyak entri klaster RGB-D, bab ini sekaligus menjadi rujukan teknis untuk entri-entri tersebut.

## Poin untuk Sitasi

Kutip dengan kunci `sohan2024yolov8review`. Ringkasan yang aman dikutip: "Sohan dkk. (2024) meninjau arsitektur dan kemajuan YOLOv8 — blok C2f, kepala terpisah bebas jangkar, serta dukungan multi-tugas dalam satu kerangka — dan merangkum kinerjanya pada tolok ukur COCO sebagai acuan bagi pengguna model tersebut."

Catatan verifikasi sebelum sitasi formal: (1) naskah penuh bab ini berada di balik akses Springer dan tidak berhasil dibuka selama penulisan; rumusan isi di atas disusun dari metadata terbitan (DOI 10.1007/978-981-99-7962-2_39, hal. 529–545) dan dokumentasi primer YOLOv8, sehingga pernyataan spesifik atas nama penulis bab wajib dikonfirmasi ke naskah asli. (2) Angka tolok ukur pada tabel diambil dari dokumentasi resmi Ultralytics, bukan dari bab tinjauan; pastikan sumber yang disebut sesuai dengan angka yang dikutip. (3) Rincian mekanisme (struktur C2f, reg_max = 16, loss BCE + CIoU + DFL, *Task-Aligned Assigner*, 32 prototipe masker) diverifikasi dari kode sumber resmi Ultralytics; bila bab tinjauan menyebut nilai berbeda, naskah yang berlaku.
