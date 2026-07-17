# 021 - EfficientDet: Scalable and Efficient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tan2020efficientdet` |
| Judul asli | EfficientDet: Scalable and Efficient Object Detection |
| Penulis | Mingxing Tan, Ruoming Pang, Quoc V. Le (Google Research, Brain Team) |
| Tahun | 2020 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1911.09070
- **Kode sumber resmi:** https://github.com/google/automl/tree/master/efficientdet
- **Google Scholar:** https://scholar.google.com/scholar?q=EfficientDet%3A%20Scalable%20and%20Efficient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=EfficientDet%3A%20Scalable%20and%20Efficient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan EfficientDet, sebuah keluarga detektor objek satu tahap (*one-stage*, tanpa tahap pengusulan wilayah) yang dirancang dengan dua prinsip: fusi fitur multi-skala yang efisien dan penskalaan model yang terkoordinasi. Kontribusi pertamanya adalah BiFPN (*bi-directional feature pyramid network*), modul penggabung fitur lintas skala yang mengalirkan informasi dua arah (atas ke bawah dan bawah ke atas) dan memberi setiap masukan bobot yang dipelajari. Kontribusi keduanya adalah *compound scaling*: satu koefisien φ yang menskalakan resolusi masukan, kedalaman, dan lebar seluruh komponen detektor secara serentak.

Hasilnya adalah delapan model bernama EfficientDet-D0 sampai D7 (ditambah varian D7x) yang mencakup rentang biaya 2,5 miliar hingga 410 miliar FLOPs (*floating-point operations*, jumlah operasi kali-tambah per citra). Model terkecil, D0, menandingi akurasi YOLOv3 dengan 28 kali lebih sedikit FLOPs. Model terbesar mencapai 55,1 AP pada COCO *test-dev* — akurasi terbaik pada masanya — dengan 77 juta parameter, 2,7 kali lebih kecil dan 7,4 kali lebih hemat FLOPs daripada detektor terbaik sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Menjelang 2020, peningkatan akurasi detektor objek dibayar dengan biaya komputasi yang terus naik. Detektor berbasis AmoebaNet dan NAS-FPN (pencari arsitektur piramida fitur secara otomatis) memerlukan 167 juta parameter dan 3045 miliar FLOPs, sekitar 30 kali lipat RetinaNet, demi akurasi tertinggi pada COCO. Ukuran dan latensi sebesar itu menyulitkan penerapan pada robotika dan kendaraan otonom. Upaya efisiensi yang sudah ada — detektor satu tahap, detektor *anchor-free* (tanpa kotak acuan), atau kompresi model — umumnya mengorbankan akurasi dan hanya menyasar satu rentang sumber daya tertentu.

Penulis mengidentifikasi dua kelemahan spesifik pada desain yang berlaku. Pertama, fusi fitur multi-skala. FPN (*feature pyramid network*, piramida fitur) menggabungkan fitur dari berbagai resolusi hanya ke satu arah, dari skala kasar ke skala halus, dan menjumlahkan semua fitur masukan tanpa pembeda; padahal fitur pada resolusi berbeda tidak memberi kontribusi yang sama besar. PANet memperbaiki arah aliran dengan menambah jalur bawah ke atas, tetapi tetap menjumlahkan fitur secara setara. NAS-FPN mencari topologi fusi secara otomatis, tetapi memerlukan ribuan jam GPU dan menghasilkan struktur tak beraturan yang sukar ditafsirkan. Kedua, penskalaan model. Detektor lazim diperbesar hanya dengan mengganti *backbone* (jaringan pengekstrak fitur awal) yang lebih besar atau menaikkan resolusi masukan, tanpa menyentuh jaringan fitur dan jaringan prediksi. Penskalaan satu dimensi seperti ini terbukti tidak efisien.

## Ide Utama

Gagasan pertama makalah ini: fusi fitur multi-skala sebaiknya dipandang sebagai masalah pembobotan yang dapat dipelajari. Setiap fitur masukan diberi satu bobot skalar; jaringan mempelajari bobot itu selama pelatihan, sehingga fitur yang lebih berguna mendapat porsi lebih besar pada keluaran. Aliran informasi dibuat dua arah dan blok fusi diulang beberapa kali agar fitur bercampur lebih dalam.

Gagasan kedua: ukuran model sebaiknya tidak diskalakan per komponen, melainkan lewat satu koefisien φ yang menaikkan resolusi masukan, kedalaman dan lebar *backbone*, jaringan fitur (BiFPN), dan jaringan prediksi secara bersamaan. Prinsip ini diadaptasi dari EfficientNet — keluarga pengklasifikasi citra yang menskalakan lebar, kedalaman, dan resolusi secara gabungan — dan EfficientNet pula yang dipakai sebagai *backbone*. Dari satu baseline φ = 0, menaikkan φ satu per satu menghasilkan keluarga D0 sampai D7 untuk anggaran komputasi yang berbeda-beda.

## Cara Kerja Langkah demi Langkah

### Backbone dan Fitur Multi-Skala

Detektor menerima citra masukan, lalu *backbone* EfficientNet (varian B0–B7 yang telah dilatih sebelumnya pada ImageNet) menghasilkan fitur pada lima tingkat resolusi, dinamai P3 sampai P7. Fitur P_i memiliki resolusi 1/2^i dari citra masukan. Pada masukan 640×640 piksel, P3 berukuran 80×80 (640/2³) dan P7 berukuran 5×5 (640/2⁷). Fitur resolusi tinggi seperti P3 peka terhadap objek kecil; fitur resolusi rendah seperti P7 membawa konteks objek besar.

### Struktur BiFPN

BiFPN menggabungkan kelima tingkat fitur melalui dua jalur. Jalur *top-down* mengalirkan informasi dari P7 ke P3: fitur kasar di-*resize* (diperbesar) lalu digabung dengan fitur halus satu tingkat di bawahnya. Jalur *bottom-up* mengalirkan informasi sebaliknya, dari P3 ke P7, dengan pengecilan resolusi. Dibanding PANet, tiga penyederhanaan dilakukan: (1) simpul yang hanya memiliki satu sisi masukan dibuang, karena tanpa fusi ia hampir tidak berkontribusi; (2) ditambah sisi pintas dari fitur masukan asli ke simpul keluaran pada tingkat yang sama, sehingga lebih banyak fitur tergabung dengan biaya kecil; (3) satu pasang jalur atas-bawah diperlakukan sebagai satu lapis, dan lapis ini diulang beberapa kali. Hasilnya adalah topologi teratur yang dapat ditumpuk, berbeda dengan topologi tak beraturan keluaran NAS-FPN.

Alur keseluruhan detektor dirangkum pada diagram berikut:

```
citra R x R ──► ┌──────────────┐
                │  backbone    │
                │ EfficientNet │
                └──────┬───────┘
        P3    P4    P5    P6    P7     <- P_i: resolusi R/2^i
        │     │     │     │     │
   ┌────▼─────▼─────▼─────▼─────▼─────┐
   │  BiFPN (diulang D = 3+phi kali)  │
   │   top-down:  P7 ► P6 ► P5 ► P4 ► P3
   │   bottom-up: P3 ► P4 ► P5 ► P6 ► P7
   │   tiap fusi: O = Σ wi·Ii/(ε+Σwj) │
   └────┬─────────────────────────────┘
        ▼
   head kelas + head box (bobot dibagi antar-level)
        ▼
   prediksi: kelas + bounding box tiap anchor
```

### Fusi Terbobot

Pada setiap simpul fusi, fitur-fitur masukan tidak dijumlah mentah, melainkan dikalikan bobot lalu dinormalisasi. Penulis menguji tiga skema. Fusi tak berbatas (O = Σ w_i·I_i) berisiko membuat pelatihan tidak stabil karena bobot bebas membesar. Fusi berbasis *softmax* membatasi bobot ke rentang 0–1, tetapi operasi softmax menambah latensi berarti pada GPU. Skema yang dipilih adalah fusi ternormalisasi cepat: O = Σ w_i·I_i / (ε + Σ w_j), dengan w_i ≥ 0 dijamin oleh fungsi ReLU (penyearah yang memetakan nilai negatif ke nol) dan ε = 0,0001 untuk mencegah pembagian nol. Sebagai contoh numerik, bila dua fitur masukan memiliki bobot 2 dan 1, keluarannya adalah 2/3 kali fitur pertama ditambah 1/3 kali fitur kedua. Skema ini mencapai akurasi setara softmax tetapi berjalan 1,26–1,31 kali lebih cepat pada GPU. Setiap fusi memakai konvolusi terpisah-per-kedalaman (*depthwise separable convolution*), yaitu konvolusi yang memproses tiap kanal secara terpisah sebelum menggabungkannya, sehingga biayanya jauh lebih murah dari konvolusi biasa.

### Compound Scaling

Satu koefisien φ mengatur seluruh dimensi model. Lebar BiFPN (jumlah kanal) tumbuh eksponensial, W = 64·(1,35^φ); kedalamannya tumbuh linier, D = 3+φ; kedalaman jaringan prediksi kotak/kelas mengikuti 3+⌊φ/3⌋; resolusi masukan naik 128 piksel per tingkat, R = 512+128φ (kelipatan 128 diperlukan karena fitur terkasar berukuran 1/128 masukan). Faktor 1,35 dipilih lewat pencarian grid pada enam kandidat nilai. Pada φ = 3 diperoleh D3: 6 lapis BiFPN selebar 64·1,35³ ≈ 157 kanal, resolusi masukan 896×896. *Backbone* mengikuti koefisien EfficientNet B0 sampai B6 agar bobot pralatih ImageNet dapat dipakai ulang. D7x menambah satu tingkat fitur (P3–P8) dan *backbone* lebih besar pada resolusi yang sama dengan D7.

### Kepala Prediksi dan Pelatihan

Fitur keluaran BiFPN diteruskan ke dua kepala: pengklasifikasi kelas dan peramalan *bounding box* (kotak pembatas objek). Seperti RetinaNet, bobot kedua kepala dibagi di seluruh tingkat fitur, dan prediksi dilakukan relatif terhadap *anchor* (kotak acuan dengan rasio aspek tetap; di sini {1/2, 1, 2}). Pelatihan pada COCO 2017 (118 ribu citra) memakai *focal loss* — fungsi galat yang menekan kontribusi contoh mudah agar model fokus pada contoh sulit — dengan α = 0,25 dan γ = 1,5, selama 300 *epoch* untuk D0–D6 dan 600 *epoch* untuk D7/D7x pada TPUv3. Evaluasi memakai *soft-NMS*, varian penekanan duplikat deteksi yang menurunkan skor alih-alih membuang kotak yang tumpang tindih.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada COCO 2017 dengan metrik AP (*average precision*; rata-rata presisi pada berbagai ambang tumpang tindih, semakin tinggi semakin baik), dilaporkan pada himpunan validasi (5 ribu citra) dan *test-dev* (20 ribu citra tanpa kebenaran dasar publik). Semua hasil memakai satu model dan satu skala uji.

Hasil kunci dan interpretasinya:

- D0 (512×512): 34,6 AP *test-dev*, 3,9 juta parameter, 2,5 miliar FLOPs. YOLOv3 pada perbandingan yang sama mencapai 33,0 AP dengan 71 miliar FLOPs — akurasi D0 lebih tinggi dengan 28 kali lebih sedikit komputasi.
- D1 (640×640): 40,5 AP dengan 6,6 juta parameter dan 6,1 miliar FLOPs, melawan RetinaNet-R50 39,2 AP dengan 34 juta parameter dan 97 miliar FLOPs — sekitar 5 kali lebih kecil dan 16 kali lebih hemat.
- D7 (1536×1536): 53,7 AP dengan 52 juta parameter dan 325 miliar FLOPs; D7x: 55,1 AP, 77 juta parameter, 410 miliar FLOPs. Detektor terbaik sebelumnya, AmoebaNet + NAS-FPN, mencapai 50,7 AP validasi dengan 209 juta parameter dan 3045 miliar FLOPs — D7x melampauinya 4 poin AP dengan biaya komputasi 7,4 kali lebih rendah.
- Latensi terukur (ukuran batch 1, perangkat keras sama): keluarga EfficientDet berjalan hingga 4,1 kali lebih cepat pada GPU dan 10,8 kali lebih cepat pada CPU dibanding pesaing berakurasi setara.

Studi ablasi memisahkan sumbangan tiap komponen. Mulai dari RetinaNet standar (ResNet-50 + FPN), mengganti *backbone* dengan EfficientNet-B3 menambah sekitar 3 AP dengan biaya yang sedikit lebih rendah; mengganti FPN dengan BiFPN menambah sekitar 4 AP lagi sekaligus mengurangi parameter dan FLOPs. Perbandingan antar-jaringan fitur menunjukkan BiFPN terbobot mengungguli FPN, PANet berulang, dan NAS-FPN pada akurasi sekaligus biaya. Sebagai uji transfer, varian segmentasi citra pada PASCAL VOC 2012 mencapai 81,74% mIoU (rata-rata irisan-per-gabungan per piksel), 1,7 poin di atas DeepLabV3+ dengan 9,8 kali lebih sedikit FLOPs.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah efisiensi yang konsisten di seluruh rentang biaya: setiap anggota keluarga D0–D7 mengungguli pesaing pada kelas komputasinya, sehingga satu resep arsitektur melayani kebutuhan dari perangkat kecil hingga server. BiFPN juga menawarkan struktur fusi yang teratur dan mudah direplikasi, berbeda dengan keluaran pencarian arsitektur otomatis. Resep *compound scaling* memberikan cara sederhana menaikkan atau menurunkan kapasitas tanpa merancang ulang model.

Keterbatasannya: penskalaan majemuk di sini berbasis heuristik dan diakui penulis belum tentu optimal; lebar *backbone* mengikuti koefisien EfficientNet demi ketersediaan bobot pralatih, bukan hasil optimasi. Pelatihannya mahal — 300 sampai 600 *epoch* dengan ukuran batch besar pada puluhan inti TPUv3 — sehingga reproduksi penuh menuntut sumber daya besar. Dari sisi rekayasa, FLOPs yang rendah tidak otomatis berarti latensi rendah pada semua perangkat keras; angka latensi makalah diukur pada GPU Titan V dan V100 tertentu, dan model terbesar tetap memerlukan ratusan milidetik per citra pada GPU kelas tersebut, jauh dari kebutuhan *real-time*.

## Kaitan dengan Bab Lain

EfficientDet melanjutkan dua garis yang dibahas pada bab-bab sebelumnya. Dari silsilah detektor satu tahap, ia mewarisi formulasi prediksi berbasis *anchor* dan *focal loss* yang juga dipakai YOLOv3 ([bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)); YOLOv3 pula yang menjadi tolok ukur efisiensi pada rezim akurasi rendah dalam makalah ini. Gagasan fusi lintas skala dua arah mengembangkan PANet, yang pada tahun yang sama diadopsi oleh YOLOv4 ([bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)) sebagai *neck*-nya; BiFPN menambahkan pembobotan terlatih dan pengulangan blok di atas gagasan itu. Kerangka *backbone*–*neck*–*head* sebagai tiga komponen yang masing-masing dapat dioptimalkan berguna untuk membaca bab-bab berikutnya, termasuk desain leher piramida pada YOLOX ([bab 005](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)) dan YOLOv7 ([bab 007](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)).

## Poin untuk Sitasi

Kutip dengan kunci `tan2020efficientdet`. Ringkasan yang aman dikutip: "EfficientDet menggabungkan BiFPN — fusi piramida fitur dua arah dengan bobot terlatih — dan *compound scaling* yang menskalakan resolusi, kedalaman, dan lebar seluruh komponen detektor dengan satu koefisien, menghasilkan keluarga D0–D7 yang mencapai akurasi COCO setara atau lebih tinggi dari detektor sebelumnya dengan parameter 4–9 kali lebih sedikit dan FLOPs 13–42 kali lebih rendah." Catatan verifikasi: abstrak arXiv menyebut "D7 mencapai 55,1 AP", tetapi tabel hasil menunjukkan angka 55,1 AP / 77 juta parameter / 410 miliar FLOPs dicapai oleh varian D7x, sedangkan D7 mencapai 53,7 AP — cocokkan penamaan model dengan tabel naskah sebelum mengutip angka spesifik. Angka latensi GPU/CPU bergantung pada perangkat keras dan implementasi; kutip dengan konteks pengukurannya.
