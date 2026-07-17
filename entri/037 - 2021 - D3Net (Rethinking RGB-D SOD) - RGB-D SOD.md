# 037 - Rethinking RGB-D Salient Object Detection: Models, Data Sets, and Large-Scale Benchmarks

## Metadata Ringkas

| Field | Nilai |
|---|---|
| Kunci BibTeX | `fan2020d3net` |
| Judul asli | Rethinking RGB-D Salient Object Detection: Models, Data Sets, and Large-Scale Benchmarks |
| Penulis | Deng-Ping Fan, Zheng Lin, Zhao Zhang, Menglong Zhu, Ming-Ming Cheng |
| Tahun | 2021 |
| Venue | IEEE Transactions on Neural Networks and Learning Systems, 32(5): 2075–2089 |
| Tema | RGB-D SOD |

## Tautan Akses

- **arXiv (naskah lengkap):** https://arxiv.org/abs/1907.06781
- **DOI (versi jurnal):** https://doi.org/10.1109/TNNLS.2020.2996406
- **Kode, dataset SIP, dan alat evaluasi:** https://github.com/DengPingFan/D3NetBenchmark
- **Google Scholar:** https://scholar.google.com/scholar?q=Rethinking%20RGB-D%20Salient%20Object%20Detection%3A%20Models%2C%20Data%20Sets%2C%20and%20Large-Scale%20Benchmarks

## Gambaran Umum

Makalah ini menata ulang bidang deteksi objek menonjol (*salient object detection*, SOD) pada citra RGB-D, yaitu citra berwarna dengan peta kedalaman (jarak tiap piksel ke kamera). Penulis melakukan tiga hal sekaligus: membangun dataset SIP berisi 929 citra orang menonjol dari ponsel, menjalankan *benchmark* terbesar pada masanya dengan meringkas 32 model dan mengevaluasi 18 model pada tujuh dataset (±97 ribu citra), serta mengusulkan model D3Net (*Deep Depth-Depurator Network*). Gagasan kuncinya: kedalaman tidak selalu bermanfaat — peta berkualitas rendah justru merusak prediksi — sehingga D3Net dilengkapi unit penyaring yang otomatis membuang kedalaman buruk. Hasilnya, D3Net mengungguli 17 model pembanding pada kelima metrik dengan kecepatan ±65 citra per detik pada satu GPU.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD adalah tugas memetakan objek yang paling menarik perhatian dalam citra menjadi peta saliensi, yaitu citra keabuan yang tiap pikselnya bernilai 0 sampai 1 sesuai tingkat kemenonjolannya. Aplikasinya meliputi pemrosesan potret dan pemisahan latar di ponsel. Sebagian besar metode SOD awal hanya memakai citra RGB. Informasi kedalaman kemudian dimanfaatkan karena batas objek yang samar pada citra warna sering kali tegas pada peta kedalaman, sehingga muncul aliran RGB-D SOD yang menggabungkan (memfusikan) fitur warna dan fitur kedalaman.

Sebelum makalah ini, tiga masalah menahan bidang tersebut. Pertama, hampir semua model mengasumsikan kedalaman selalu membantu, padahal peta dari sensor nyata sering berderau; fusi buta menurunkan kinerja, dan belum ada model yang secara eksplisit membuang peta kedalaman buruk. Kedua, dataset RGB-D yang ada direkam dengan kamera Kinect atau kamera *light field*, bukan dengan ponsel, dan belum ada yang berfokus pada manusia, padahal aplikasi ponsel hampir selalu memotret orang. Ketiga, evaluasi antarmodel tidak setara: makalah terdahulu umumnya hanya menguji satu sampai empat dataset, memakai metrik tingkat piksel yang tidak menilai struktur objek, serta melaporkan F-measure tanpa menyebut statistik dan ambang yang dipakai. Kondisi ini menjadi konteks bagi bab fusi sebelumnya, misalnya [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md), yang memakai protokol berbeda.

## Ide Utama

Ide utama makalah ini dapat dinyatakan dalam satu kalimat: kedalaman adalah masukan opsional yang harus lulus uji kualitas sebelum dipakai. Secara mekanis, D3Net menerima citra RGB dan peta kedalaman, lalu menghasilkan tiga peta saliensi dari tiga aliran terpisah: satu dari RGB saja, satu dari gabungan RGB dan kedalaman, satu dari kedalaman saja. Pada saat pengujian, sebuah gerbang bernama *depth depurator unit* (DDU) memutuskan apakah hasil fusi boleh dipakai. Ujinya sederhana: bila prediksi aliran fusi konsisten dengan prediksi aliran kedalaman, kedalaman dianggap andal dan hasil fusi dipilih; bila tidak, kedalaman dianggap menyesatkan dan model kembali ke prediksi RGB saja. Masukannya dua citra, keluarannya satu peta saliensi, dan yang berubah dibanding fusi biasa adalah keputusan biner per citra tentang boleh tidaknya kedalaman dipakai.

## Cara Kerja Langkah demi Langkah

### Modul Pembelajaran Fitur Tiga Aliran (FLM)

Komponen pertama adalah *feature learning module* (FLM), yang terdiri atas tiga sub-jaringan paralel: RgbNet, RgbdNet, dan DepthNet. Ketiganya berarsitektur sama dan hanya berbeda kanal masukan: RgbNet menerima RGB tiga kanal, RgbdNet menerima gabungan RGB dan kedalaman empat kanal, DepthNet menerima kedalaman satu kanal; semua masukan diubah ukurannya menjadi 224×224 piksel.

Setiap sub-jaringan adalah modifikasi *Feature Pyramid Network* (FPN), yaitu struktur yang mengekstraksi fitur pada beberapa resolusi sekaligus melalui jalur menurun (menangkap makna global) dan jalur menaik (menggabungkan kembali detail halus). *Backbone* (jaringan pengekstraksi fitur dasar) yang dipakai adalah VGG-16, jaringan konvolusi 16 lapis yang umum pada masanya, ditambah lapisan keenam berisi dua konvolusi 3×3 untuk memperkuat fitur semantik lokasi objek. Berbeda dari FPN asli yang menggabungkan fitur dengan penjumlahan, D3Net memakai konkatenasi: fitur kasar dinaikkan resolusinya dua kali lipat dengan *nearest neighbor*, fitur halus dikurangi kanalnya dengan konvolusi 1×1, lalu keduanya disambungkan. Pada masukan 224×224, tensor fitur menyusuri piramida dari 64×224×224 hingga 32×7×7, lalu menaik kembali sampai peta akhir 32×224×224. Keluarannya tiga peta saliensi ukuran penuh: *S_rgb*, *S_rgbd*, *S_depth*.

### Unit Penyaring Kedalaman (DDU)

Komponen kedua adalah DDU, yang hanya aktif pada fase pengujian. Dasar pemikirannya: pada peta kedalaman berkualitas tinggi, objek menonjol berbatas tegas dengan distribusi kedalaman berpuncak dua (objek dan latar), sehingga aliran DepthNet akan menemukan objek yang sama dengan aliran RgbdNet dan kedua peta keluarannya mirip; pada peta buruk, keduanya berbeda jauh.

Kemiripan itu diukur unit pembanding *F_cu* dengan fungsi jarak MAE (*mean absolute error*), yaitu rata-rata selisih mutlak antarpiksel dua peta pada rentang 0 sampai 1. Bila jarak antara *S_rgbd* dan *S_depth* tidak melebihi ambang *t*, unit bernilai 1; selain itu bernilai 0. Peta akhir ditentukan rumus gerbang *P = F_cu · S_rgbd + (1 − F_cu) · S_rgb*. Ambang *t* = 0,15 dipilih dari enam nilai kandidat (0,01 sampai 0,20) karena berkinerja terbaik. Contoh numerik: bila MAE kedua peta adalah 0,10, maka *F_cu* = 1 dan keluaran berupa *S_rgbd*; bila MAE-nya 0,23, kedalaman dibuang dan keluaran berupa *S_rgb*. Diagram berikut merangkum alur datanya.

```
citra RGB 224x224 ──┬─► RgbNet (3 kanal) ────────► S_rgb ─────────┐
                    │                                             │
                    └─► RgbdNet (RGB+depth, 4 kanal) ─► S_rgbd ──┤
                                                                  │
peta kedalaman ─────┴─► DepthNet (1 kanal) ─────────► S_depth ──┤
224x224                                                         ▼
                                        ┌──────────────────────────────┐
                                        │ DDU (hanya saat pengujian):  │
                                        │ δ = MAE(S_rgbd, S_depth)     │
                                        │ δ ≤ 0,15 → P = S_rgbd        │
                                        │ δ > 0,15 → P = S_rgb         │
                                        └──────────────┬───────────────┘
                                                       ▼
                                          peta saliensi akhir P
```

Ketiga sub-jaringan dilatih bersama sebagai struktur bersarang, sedangkan keputusan gerbang dibuat per citra saat inferensi, sehingga DDU tidak menambah parameter yang harus dilatih.

### Pelatihan

Ketiga aliran dilatih dengan fungsi rugi *cross-entropy* per piksel, yang mengukur selisih peta prediksi bernilai 0–1 terhadap peta kebenaran biner pada seluruh 224×224 = 50.176 piksel. Data latih mengikuti protokol model CPFP agar perbandingan adil: 1.485 pasang citra dari NJU2K dan 700 pasang dari NLPR. Optimisasi memakai Adam dengan laju pembelajaran 10⁻⁴, *batch* 8, selama 30 epoch pada satu GPU GTX TITAN X, dengan augmentasi pembalikan horizontal. D3Net tidak memakai pasca-pemrosesan CRF (*conditional random field*, pemulus batas objek untuk menaikkan skor), sehingga hasilnya murni keluaran jaringan.

### Dataset SIP

Dataset ini dibangun untuk skenario ponsel: citra direkam dengan kamera belakang Huawei Mate 10 (sensor RGB 12 MP dan monokrom 20 MP), dan peta kedalamannya diestimasi otomatis oleh ponsel. Dari 5.269 citra mentah hasil aksi sembilan orang pada berbagai latar luar ruang, seleksi manual, pemungutan suara enam penilai, dan penapisan kualitas anotasi menyisakan 929 citra final dengan anotasi tingkat piksel yang halus. Cakupannya meliputi delapan kategori latar (mobil, bunga, rumput, jalan, pohon, rambu, penghalang, lainnya), kondisi pencahayaan gelap dan terang, serta satu sampai lima objek menonjol per citra. Ukuran objek relatif terhadap luas citra berkisar 0,48%–66,85% (rata-rata 20,43%), dan berbeda dari kebanyakan dataset pendahulu, SIP nyaris bebas bias ke tengah citra.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tujuh dataset (STERE, NJU2K, DES, NLPR, SSD, LFSD, SIP) dengan total 5.398 citra uji dikali 18 model, atau sekitar 97 ribu evaluasi. Lima metrik dipakai serentak: MAE (galat rata-rata peta, makin kecil makin baik), kurva *precision-recall* dan F-measure maksimum (keseimbangan presisi dan rekoleksi pada berbagai ambang), S-measure (kemiripan struktur objek dan region dengan peta kebenaran), serta E-measure (keselarasan tingkat piksel dan tingkat citra).

Pada S-measure, D3Net mencapai 0,899 pada NJU2K dan 0,912 pada NLPR, dibanding pesaing terkuat CPFP dengan 0,879 dan 0,888; selisih 2,0 dan 2,4 poin berarti struktur objek hasil D3Net lebih menyerupai kebenaran pada dua dataset terbesar. Secara keseluruhan D3Net mengalahkan hasil terbaik yang pernah dipublikasikan dengan margin 1,0% sampai 5,8% pada enam dari tujuh dataset, termasuk 1,4% pada SIP; satu-satunya pengecualian adalah LFSD, tempat D3Net (0,825) sedikit di bawah CPFP (0,828), sehingga keunggulannya tidak mutlak. D3Net juga tercepat dalam tabel: 0,015 detik per citra (±65 FPS), lebih dari sepuluh kali kecepatan CPFP (0,170 detik), tanpa pasca-pemrosesan CRF.

Studi ablasi mengukur kontribusi tiap komponen. Pada NJU2K, S-measure RgbNet saja 0,888, RgbdNet saja 0,898, DepthNet saja 0,857, dan D3Net lengkap 0,900; fusi terbukti membantu bila kedalaman baik, dan gerbang DDU masih menambah 0,2 poin di atas jalur fusi saja. Pada STERE, DepthNet anjlok ke 0,713 karena banyak peta kedalamannya rusak, tetapi D3Net tetap mencapai 0,899 — bukti langsung bahwa penyaringan melindungi model dari kedalaman buruk. Penulis juga menghitung batas bawah (selalu memilih jalur terburuk) dan batas atas (selalu memilih jalur terbaik per citra): rata-rata D3Net masih terpaut 1,6% dari batas atasnya, artinya gerbang biner ini belum optimal.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini terletak pada tiga lapis. Sebagai model, D3Net adalah kerangka sederhana yang tidak mengikat backbone tertentu, unggul pada lima metrik sekaligus, dan cukup cepat untuk aplikasi waktu nyata. Sebagai *benchmark*, evaluasi 18 model pada tujuh dataset dengan statistik metrik yang dinyatakan eksplisit menghilangkan ketidakadilan perbandingan yang sebelumnya umum terjadi, dan papan peringkat daringnya terus diperbarui. Sebagai data, SIP mengisi celah dataset berorientasi manusia dari sensor ponsel sungguhan, lengkap dengan pasangan citra RGB dan monokrom untuk riset kedalaman stereo.

Keterbatasannya diakui penulis: ukuran SIP (929 citra) kecil dibanding dataset SOD berbasis RGB; arsitektur tiga aliran melipatgandakan kebutuhan memori, sehingga penulis menyarankan penggantian backbone dengan MobileNet V2 atau ESPNet V2 untuk perangkat ringan; dan DDU tidak mencapai batas atasnya sendiri (selisih rata-rata 1,6%). Dari sisi rekayasa, keputusan biner dengan ambang tetap *t* = 0,15 adalah heuristik kasar: citra dengan kedalaman berkualitas menengah dipaksa memilih satu jalur sepenuhnya, padahal pembobotan adaptif berpotensi lebih baik — penulis sendiri mencadangkannya sebagai pekerjaan lanjutan. Secara konseptual, kualitas kedalaman hanya dinilai tidak langsung lewat konsistensi dua prediksi, dengan asumsi DepthNet pasti gagal saat kedalaman buruk; asumsi ini tidak selalu terpenuhi, misalnya pada dataset DES tempat DepthNet justru menjadi aliran terkuat.

## Kaitan dengan Bab Lain

Bab ini menjadi titik balik dalam klaster RGB-D SOD. Model yang dibahas sebelumnya, seperti [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md), berfokus pada cara memfusikan kedua modalitas sebaik mungkin, sedangkan D3Net menambah pertanyaan yang mendahuluinya: apakah modalitas kedalaman layak ikut serta. *Benchmark*-nya mengevaluasi pendahulu seperti CPFP, TANet, dan PCF, sehingga bab ini menjadi titik pembanding baku. Setelah naskah ini terbit, model seperti [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md), [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md), dan [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md) dimasukkan penulis ke papan peringkat daringnya, dan dataset SIP menjadi dataset uji standar bagi bab-bab selanjutnya, termasuk [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md) yang mengganti backbone CNN dengan transformer.

## Poin untuk Sitasi

Kunci BibTeX: `fan2020d3net`. Ringkasan yang aman dikutip: Fan dkk. (2021) meninjau ulang RGB-D SOD secara sistematis dengan membangun dataset SIP (929 citra orang menonjol dari ponsel), mengevaluasi 18 model pada tujuh dataset (±97 ribu citra), serta mengusulkan D3Net yang menyaring peta kedalaman berkualitas rendah melalui unit gerbang DDU di atas tiga aliran FPN; model ini dilaporkan mengungguli 17 pembanding pada lima metrik dengan kecepatan ±65 FPS. Catatan verifikasi: seluruh angka pada bab ini diambil dari versi arXiv v2 (1907.06781) yang identitas jurnalnya cocok dengan TNNLS 32(5): 2075–2089; sebelum sitasi formal, cocokkan angka Tabel IV dan Tabel V dengan PDF jurnal, karena tabelnya padat dan rawan salah baca kolom.
