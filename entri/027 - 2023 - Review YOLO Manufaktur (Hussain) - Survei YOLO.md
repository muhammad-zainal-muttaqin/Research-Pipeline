# 027 - YOLO-v1 to YOLO-v8, the Rise of YOLO and Its Complementary Nature toward Digital Manufacturing and Industrial Defect Detection

## Metadata Ringkas

| Field | Nilai |
|---|---|
| Kunci BibTeX | `hussain2023yolo` |
| Judul asli | YOLO-v1 to YOLO-v8, the Rise of YOLO and Its Complementary Nature toward Digital Manufacturing and Industrial Defect Detection |
| Penulis | Muhammad Hussain (University of Huddersfield, Inggris) |
| Tahun | 2023 |
| Venue | *Machines*, volume 11, nomor 7, artikel 677 |
| Tema | Survei YOLO |

## Tautan Akses

- DOI (akses terbuka): https://doi.org/10.3390/machines11070677
- Halaman penerbit MDPI (teks lengkap): https://www.mdpi.com/2075-1702/11/7/677
- Google Scholar: https://scholar.google.com/scholar?q=YOLO-v1%20to%20YOLO-v8%2C%20the%20Rise%20of%20YOLO%20and%20Its%20Complementary%20Nature%20toward%20Digital%20Manufacturing%20and%20Industrial%20Defect%20Detection
- Semantic Scholar: https://www.semanticscholar.org/search?q=YOLO-v1%20to%20YOLO-v8%2C%20the%20Rise%20of%20YOLO%20and%20Its%20Complementary%20Nature%20toward%20Digital%20Manufacturing%20and%20Industrial%20Defect%20Detection&sort=relevance

## Gambaran Umum

Makalah ini adalah tinjauan atas evolusi keluarga detektor objek YOLO dari YOLO-v1 (2015) sampai YOLO-v8 (Januari 2023), ditulis dari sudut pandang manufaktur digital. Penulis menyatakannya sebagai tinjauan pertama yang membedah kemajuan arsitektur pada setiap iterasi YOLO sekaligus menilainya terhadap kebutuhan inspeksi kualitas otomatis di industri: deteksi cepat, akurasi tinggi, dan penerapan pada *edge device*, yaitu peranti komputasi di lokasi produksi dengan sumber daya terbatas.

Selain membedah arsitektur, tinjauan ini menghimpun literatur penerapan YOLO untuk deteksi cacat permukaan pada empat domain: kain, sel surya, baja, dan rak gudang. Simpulan utamanya: prinsip yang dipegang seluruh varian YOLO — waktu nyata, bobot komputasi ringan, dan akurasi tinggi — sejalan dengan persyaratan inspeksi cacat industri, dan arsitektur YOLO yang terbuka memungkinkan modifikasi modul internal, misalnya penambahan mekanisme atensi, tanpa menghilangkan kesesuaian waktu nyata.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Inspeksi kualitas merupakan bagian integral dari manufaktur karena menjamin integritas produk di mata klien. Inspeksi manual oleh manusia memiliki kelemahan yang terdokumentasi: bias penilaian, kelelahan, biaya tenaga kerja, dan waktu henti produksi. Cacat permukaan juga dapat berbentuk halus dan berukuran kecil sehingga sukar ditangkap konsisten oleh penglihatan manusia.

Otomatisasi inspeksi membutuhkan deteksi objek, bukan sekadar klasifikasi citra, karena proses produksi membutuhkan jumlah dan lokasi setiap cacat. Detektor objek dua tahap seperti R-CNN dan Faster R-CNN memisahkan pengusulan wilayah kandidat dan prediksi akhir; hasilnya akurat tetapi terlalu berat untuk lini produksi waktu nyata. Detektor satu tahap seperti SSD, RetinaNet, dan YOLO menggabungkan kedua proses itu dalam satu lintasan sehingga lebih ringan dan cepat, dengan konsekuensi akurasi yang umumnya lebih rendah.

Di antara detektor satu tahap, keluarga YOLO paling banyak diadopsi pada konteks industri. Masalahnya, delapan varian YOLO muncul dalam delapan tahun dengan kontributor berbeda, tetapi belum ada tinjauan kohesif yang memetakan kontribusi teknis tiap varian terhadap metrik penerapan industri: akurasi, kecepatan, dan efisiensi komputasi. Tanpa peta itu, praktisi memilih varian untuk tugas inspeksi tanpa acuan terstruktur. Bab ini menutup celah tersebut; mekanisme dasar YOLO-v1 dan YOLO-v3 dibahas lebih rinci pada [bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) dan [bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md).

## Ide Utama

Gagasan inti makalah ini adalah adanya hubungan komplementer antara prinsip desain keluarga YOLO dan kebutuhan manufaktur digital, yang diperiksa secara mekanis dalam tiga langkah. Pertama, perubahan arsitektur setiap varian dari YOLO-v1 sampai YOLO-v8 dibedah satu per satu. Kedua, setiap perubahan dinilai terhadap tiga metrik industri: akurasi deteksi, kecepatan inferensi, dan beban komputasi. Ketiga, klaim kesesuaian itu diuji terhadap literatur penerapan nyata pada deteksi cacat permukaan, sehingga dihasilkan peta kesesuaian antara karakter varian dan persyaratan tugas inspeksi industri.

## Cara Kerja Langkah demi Langkah

### Anatomi detektor satu tahap dan mekanisme dasar YOLO

Detektor satu tahap modern tersusun atas tiga komponen. *Backbone* adalah jaringan konvolusi yang mengekstraksi fitur visual dari citra masukan. *Neck* mengagregasi fitur dari beberapa tingkat resolusi agar objek besar dan kecil sama-sama terwakili. *Head* mengubah fitur agregat menjadi prediksi akhir berupa kelas objek dan posisinya. Aliran data ketiganya digambarkan pada diagram berikut.

```
┌───────────┐   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   Citra   │──▶│   Backbone    │──▶│     Neck      │──▶│     Head      │
│  masukan  │   │  (ekstraksi   │   │  (agregasi    │   │  (prediksi    │
└───────────┘   │    fitur)     │   │    fitur)     │   │   deteksi)    │
                └───────────────┘   └───────────────┘   └───────────────┘
                        │                   │                   │
                        ▼                   ▼                   ▼
                peta fitur visual   fitur multi-skala   kelas cacat,
                (Darknet-53,        (FPN, PANet,        bounding box,
                 CSPDarknet-53)      SPP)                confidence
```

Diagram di atas menunjukkan bahwa seluruh komputasi berlangsung dalam satu lintasan maju tanpa tahap pengusulan wilayah terpisah; inilah sumber kecepatan keluarga YOLO. Pada YOLO-v1, citra dibagi menjadi grid S×S (baku 7×7), dan sel yang memuat pusat objek bertanggung jawab atas deteksi objek itu. Setiap sel memprediksi B buah *bounding box* — kotak pembatas berparameter pusat (x, y), lebar w, dan tinggi h — beserta skor *confidence*, yaitu peluang adanya objek dikalikan IoU (*intersection over union*): rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak acuan (*ground truth*). Setiap sel juga memprediksi probabilitas C kelas, sehingga tensor keluaran berukuran S×S×(5B+C); dengan grid 7×7, B=2, dan C=80 kelas pada dataset COCO, ukurannya adalah 7×7×90. Kotak yang tumpang tindih untuk objek yang sama dirampingkan dengan *non-maximum suppression* (NMS): semua kotak yang IoU-nya terhadap kotak terbaik di bawah ambang tertentu dihapus.

### Evolusi arsitektur per varian

YOLO-v1 (2015) mencapai 63,4% mAP pada 45 FPS di dataset PASCAL VOC; mAP (*mean Average Precision*) adalah rerata presisi lintas kelas, dan FPS (*frames per second*) adalah jumlah citra yang diproses per detik. Varian ringkasnya, Fast YOLO, mencapai 52,7% mAP pada 155 FPS. Hasil ini melampaui detektor waktu nyata lain saat itu seperti DPM-v5 (33% mAP), tetapi tertinggal dari Faster R-CNN (71% mAP): akurasi ditukar dengan kecepatan dua orde lebih tinggi. Kelemahannya adalah *recall* rendah dan galat lokalisasi tinggi pada objek yang berdekatan, karena tiap sel dibatasi dua kotak.

YOLO-v2 (2016) memperbaikinya lewat empat teknik. *Batch normalization* (normalisasi aktivasi per batch pelatihan) menaikkan mAP 2 poin dan menghilangkan kebutuhan *dropout*. Pelatihan pengklasifikasi pada resolusi 448×448 selama 10 *epoch* menambah 4 poin mAP. Lapisan terhubung penuh digantikan *anchor box*, kotak acuan berdimensi pradefinisi yang dipilih dengan *k-means clustering* atas kotak ground truth data latih. Backbone baru Darknet-19 menekan komputasi ke 5,58 miliar operasi per citra, jauh di bawah VGG-16 (30,69 miliar). Hasilnya 76,8% mAP pada 67 FPS dan 78,6% mAP pada 40 FPS, melampaui SSD dan Faster R-CNN pada masanya. Varian YOLO9000 memperluas cakupan ke lebih dari 9000 kategori, tetapi mAP-nya turun ke 19,7%: perluasan kelas dibayar dengan akurasi.

YOLO-v3 (2018) mengganti backbone dengan Darknet-53 yang memakai koneksi residual, yaitu jalur pintas yang menjumlahkan keluaran lapisan dangkal ke lapisan lebih dalam agar gradien dan fitur halus tidak hilang. Total kedalamannya 106 lapisan konvolusi, dan prediksi dilakukan pada tiga skala resolusi sehingga deteksi objek kecil membaik; sifat ini kelak penting untuk cacat permukaan berukuran kecil.

YOLO-v4 (2020) adalah varian pertama tanpa penulis asli YOLO. Backbone dipilih dari tiga kandidat dan jatuh pada CSPDarknet-53. Pada komponen neck dipakai PANet, yaitu pengembangan FPN (*feature pyramid network*, penggabung peta fitur berbagai resolusi dari atas ke bawah) dengan tambahan jalur dari bawah ke atas, serta blok SPP (*spatial pyramid pooling*) untuk memperluas wilayah pandang fitur. YOLO-v4 memperkenalkan *bag-of-freebies*, teknik yang menaikkan akurasi tanpa biaya inferensi tambahan (augmentasi Mosaic, fungsi rugi CIoU), dan *bag-of-specials*, teknik berbiaya inferensi kecil dengan peningkatan kinerja berarti (aktivasi Mish, *cross mini-batch normalization*).

YOLO-v5 (2020) rilis kurang dari dua bulan setelah YOLO-v4 tanpa makalah pendamping, dan menjadi varian pertama yang ditulis dalam PyTorch alih-alih Darknet. Pemilihan anchor box diotomatisasi: jaringan mempelajari sendiri kotak acuan terbaik untuk dataset yang dipakai. YOLO-v5 tersedia dalam beberapa ukuran dengan berkas bobot 27 MB sampai 192 MB, sehingga pengguna dapat menukar akurasi dengan ukuran sesuai perangkat.

YOLO-v6 (2022) dirancang tim Meituan secara eksplisit untuk industri. Varian ini meninggalkan anchor box sepenuhnya (*anchor-free*: kotak diprediksi langsung tanpa acuan), yang diklaim 51% lebih cepat daripada pendekatan berbasis anchor. Backbone EfficientRep dan neck Rep-PAN memakai reparameterisasi, yaitu struktur bercabang saat pelatihan yang disederhanakan menjadi satu cabang saat inferensi. Kepala klasifikasi dan regresi dipisah (*decoupled head*), fungsi ruginya *varifocal loss* untuk klasifikasi dan *distribution focal loss* untuk regresi, dan *knowledge distillation* (model besar sebagai guru melatih model kecil sebagai murid) menekan ukuran model.

YOLO-v7 (2022) membawa empat reformasi: modul E-ELAN yang mengatur agregasi lapisan berdasarkan analisis biaya akses memori dan jalur gradien; *compound model scaling* yang menskalakan lebar dan kedalaman jaringan secara koheren; reparameterisasi tingkat modul; dan kepala bantu (*auxiliary head*) pada lapisan tengah selama pelatihan. Seluruh variannya melampaui pendahulu pada rentang 5–160 FPS di dataset COCO, dengan peruntukan tegas: tiny untuk GPU tepi, W6 untuk GPU awan, E6/D6/E6E untuk GPU awan kelas atas; tidak ada varian untuk peranti mobile berbasis CPU.

YOLO-v8 (Januari 2023) dirilis Ultralytics tanpa makalah ilmiah saat tinjauan ini ditulis. Berdasarkan *benchmark* awal repositori resmi pada resolusi masukan 640, seluruh varian YOLO-v8 menghasilkan *throughput* lebih tinggi daripada YOLO-v5 dan YOLO-v6 dengan jumlah parameter yang sebanding.

### Penerapan pada deteksi cacat permukaan industri

Bagian penerapan meninjau empat domain. Pada inspeksi kain, satu studi menambahkan atensi spasial pada YOLO-v5 lalu mendistilasi model guru ke model murid untuk peranti Jetson TX2; studi lain menyisipkan modul Swin Transformer dan atensi-diri jendela geser untuk menonjolkan cacat kecil. Pada sel surya, YOLO-v5 dimodifikasi dengan konvolusi deformable, mekanisme atensi, dan pemilihan anchor dengan K-means++; studi lain (AP-YOLO-v5) menambah himpunan anchor berskala kecil. Pada baja, YOLO-v5 diterapkan pada citra sinar-X las pipa, dan YOLO-v4 diperingan dengan *depth-wise separable convolution* — konvolusi yang memisahkan perhitungan spasial dan kanal — untuk strip aluminium. Pada rak gudang, YOLO-v7 dipasang pada forklift yang beroperasi sehingga deteksi harus selesai selama forklift mendekati rak.

### Kerangka penilaian survei

Seluruh pembahasan dinilai dengan tiga metrik: mAP, FPS, dan ukuran model. Penulis mengaitkan kebangkitan YOLO dengan dua faktor: komposisi satu tahap yang ringan, dan aksesibilitas yang melonjak sejak migrasi ke PyTorch pada YOLO-v5 — repositorinya mencatat 34,7 ribu bintang GitHub per Juni 2023, pelatihannya lebih singkat, dan konversi bobotnya ke format ONNX untuk perangkat tepi menjadi mudah.

## Eksperimen dan Hasil

Sebagai survei, makalah ini tidak mengandung eksperimen baru; buktinya berupa sintesis angka yang dilaporkan studi penerapan. Hasil-hasil utama pada deteksi cacat industri dirangkum pada tabel berikut.

| Domain | Arsitektur dasar | Hasil yang dilaporkan |
|---|---|---|
| Kain (distilasi) | YOLO-v5 + atensi spasial | AUC 95,2% (murid) vs 98,1% (guru); 16 ms vs 35 ms di Jetson TX2 |
| Kain (transformer) | YOLO-v5 + Swin Transformer | 76,5% mAP pada 58,8 FPS |
| Sel surya | YOLO-v5 dimodifikasi | 89,64% mAP |
| Sel surya (AP) | AP-YOLO-v5 | 87,8% mAP, recall 89,0%, F1 88,9%, 98,6 FPS |
| Las baja (sinar-X) | YOLO-v5 | 98,7% mAP (IoU 0,5); 0,12 s per citra |
| Strip aluminium | YOLO-v4 diperingan | 86,35% mAP pada 45 FPS (asli: 81,78% pada 52 FPS) |
| Rak gudang | YOLO-v7 | 91,1% mAP pada 19 FPS |

Interpretasi angka-angka tersebut adalah sebagai berikut. Pada kain, distilasi menukar sekitar 3 poin AUC dengan kecepatan lebih dari dua kali lipat, pertukaran yang rasional untuk perangkat tepi. Hasil 76,5% mAP pada 58,8 FPS menunjukkan penyisipan modul transformer sekalipun masih memenuhi syarat waktu nyata. Pada las baja, mAP 98,7% dengan 0,12 detik per citra memenuhi laju produksi pipa. Pada strip aluminium, modifikasi menaikkan mAP 4,6 poin dengan penurunan kecepatan dari 52 ke 45 FPS yang masih dapat diterima. Pada rak gudang, 91,1% mAP pada 19 FPS cukup untuk forklift yang bergerak, dan lebih ringan daripada Mask R-CNN yang lebih akurat tetapi terlalu berat untuk diterapkan. Angka lintas baris tabel tidak dapat dibandingkan langsung karena setiap studi memakai dataset dan perangkat berbeda.

## Kelebihan dan Keterbatasan

Kelebihan tinjauan ini terletak pada lensa manufaktur yang konsisten: setiap perubahan arsitektur diatribusikan pada variannya dengan jelas, lalu diuji relevansinya terhadap kebutuhan inspeksi nyata. Bukti penerapan konkret disajikan lintas empat domain industri, dan diskusi varian ukuran memberi panduan praktis memilih konfigurasi sesuai perangkat.

Keterbatasannya, cakupan berhenti pada YOLO-v8 yang rilis Januari 2023, sehingga varian sesudahnya tidak dibahas; ini konsekuensi alami waktu terbit. Dari sisi metodologis, tinjauan ini tidak menjalankan *benchmark* langsung pada dataset yang sama, sehingga perbandingan antarvarian bertumpu pada angka dari makalah masing-masing yang kondisi pengujiannya berbeda. Penilaian terhadap YOLO-v8 hanya bertumpu pada *benchmark* awal repositori tanpa makalah ilmiah. Dari sisi rekayasa, literatur penerapan yang ditinjau didominasi YOLO-v5, sehingga kesesuaian varian yang lebih baru untuk inspeksi cacat belum teruji di dalam tinjauan ini.

## Kaitan dengan Bab Lain

Bab ini mewarisi pembahasan mekanisme grid YOLO-v1 dari [bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) dan arsitektur multi-skala YOLO-v3 dari [bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md), lalu menyusunnya kembali sebagai satu garis evolusi berkelanjutan. Di dalam klaster survei, bab ini sejajar dengan [bab 026 (Terven dkk.)](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md) dan [bab 028 (Jiang dkk.)](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md), tetapi berbeda fokus: kedua survei itu bersifat umum, sedangkan bab ini menyaring silsilah yang sama lewat kebutuhan inspeksi cacat industri. Keterbatasan cakupannya dijawab sebagian oleh [bab 032 (Alif dan Hussain)](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md), yang memperluas tinjauan sampai YOLO-v10 dan menambahkan *benchmark* langsung yang tidak dilakukan bab ini.

## Poin untuk Sitasi

Kunci BibTeX: `hussain2023yolo`. Ringkasan yang aman dikutip: Hussain (2023) meninjau evolusi YOLO dari versi pertama sampai YOLO-v8 dengan sudut pandang manufaktur digital, membedah kontribusi arsitektur tiap varian terhadap akurasi, kecepatan, dan efisiensi komputasi, serta menghimpun bukti penerapannya pada deteksi cacat permukaan industri. Tinjauan ini menyimpulkan bahwa prinsip waktu nyata, ringan, dan akurat pada keluarga YOLO sejalan dengan kebutuhan inspeksi kualitas otomatis dalam kerangka Industry 4.0.

Catatan verifikasi sebelum sitasi formal: (1) angka kinerja tiap studi penerapan dikutip survei dari makalah pihak ketiga, sehingga sitasi langsung atas angka itu sebaiknya merujuk naskah studi asal; (2) jumlah bintang GitHub YOLO-v5 (34,7 ribu) tercatat per Juni 2023 dan cepat berubah; (3) makalah menulis awal YOLO sebagai 2015, sementara publikasi konferensi YOLO-v1 adalah CVPR 2016; (4) klaim sebagai tinjauan pertama berlensa manufaktur adalah klaim penulis per Juni 2023.
