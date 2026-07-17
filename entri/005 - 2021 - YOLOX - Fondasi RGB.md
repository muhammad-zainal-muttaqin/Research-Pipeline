# 005 - YOLOX: Exceeding YOLO Series in 2021

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ge2021yolox` |
| Judul asli | YOLOX: Exceeding YOLO Series in 2021 |
| Penulis | Zheng Ge, Songtao Liu, Feng Wang, Zeming Li, Jian Sun |
| Tahun | 2021 |
| Venue | arXiv preprint arXiv:2107.08430 (Megvii Technology) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2107.08430
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOX%3A%20Exceeding%20YOLO%20Series%20in%202021
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOX%3A%20Exceeding%20YOLO%20Series%20in%202021&sort=relevance

## Gambaran Umum

YOLOX membongkar tiga asumsi desain yang diwarisi YOLO sejak bab 002: penggunaan *anchor box*, head yang menggabungkan klasifikasi dan regresi dalam satu cabang, dan penetapan label positif yang statis. Ketiganya diganti: prediksi menjadi *anchor-free* (setiap lokasi pada peta fitur langsung memprediksi satu objek), head dipisah menjadi cabang klasifikasi dan cabang regresi (*decoupled head*), dan penetapan label dilakukan secara dinamis oleh algoritme SimOTA yang memilih kandidat terbaik berdasarkan biaya prediksi.

Dampaknya konsisten di seluruh skala model. YOLOX menaikkan YOLOv3-Darknet53 menjadi 47,3% AP pada COCO (melampaui praktik terbaik saat itu sebesar 3,0 poin), YOLOX-L mencapai 50,0% AP pada 68,9 FPS (V100) melampaui YOLOv5-L sebesar 1,8 poin, dan YOLOX-Nano — hanya 0,91 juta parameter — mencapai 25,3% AP. Satu model YOLOX-L juga memenangi Streaming Perception Challenge pada Workshop on Autonomous Driving, CVPR 2021.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv2 (bab 002), keluarga YOLO memprediksi kotak sebagai koreksi terhadap *anchor* — kotak acuan yang bentuknya ditentukan lebih dahulu. Desain ini membawa tiga beban. Pertama, *anchor* adalah hiperparameter: jumlah, skala, dan rasionya harus disetel per dataset (mis. lewat klastering), dan setelan yang baik pada COCO belum tentu baik pada domain lain — inilah salah satu sumber bias domain. Kedua, penggunaan banyak *anchor* per lokasi memperbesar kepala prediksi. Ketiga, mekanisme penetapan label positif yang berbasis *anchor* bersifat statis: kandidat ditetapkan positif bila IOU-nya dengan objek kebenaran melampaui ambang tetap, tanpa memperhitungkan kualitas prediksi itu sendiri.

Di sisi lain, komunitas deteksi telah menunjukkan dua hal. FCOS (bab 019) membuktikan detektor *anchor-free* — satu prediksi per lokasi, langsung dari titik — dapat menyamai detektor berbasis *anchor*. Dan studi tentang *label assignment* menunjukkan bahwa memilih kandidat positif secara dinamis berdasarkan biaya (seperti OTA, *Optimal Transport Assignment*) menaikkan akurasi tanpa mengubah arsitektur. YOLOX adalah upaya membawa dua gagasan itu — ditambah pemisahan head — ke dalam keluarga YOLO yang telah terbukti praktis.

## Ide Utama

Gagasan pemersatu ketiga perubahan YOLOX adalah menyederhanakan apa yang dapat disederhanakan dan memindahkan kompleksitas ke tempat yang dapat dihitung otomatis. *Anchor* dihapus sehingga tidak ada lagi hiperparameter bentuk kotak yang harus disetel manusia. Head dipisah karena klasifikasi dan regresi adalah dua tugas berbeda yang selama ini dipaksa berbagi fitur yang sama. Dan penetapan label — keputusan "kandidat mana yang menjadi contoh positif untuk objek ini" — diserahkan kepada optimisasi biaya yang dihitung dari prediksi model itu sendiri, bukan aturan ambang tetap.

## Cara Kerja Langkah demi Langkah

### Anchor-Free

Pada YOLO berbasis *anchor*, setiap lokasi peta fitur mengeluarkan beberapa prediksi (satu per anchor). YOLOX mereduksi ini menjadi **satu prediksi per lokasi**: setiap titik pada peta fitur langsung memprediksi empat nilai — dua offset pusat relatif terhadap titik itu dan dua dimensi kotak — plus skor objek dan skor kelas. Titik-titik yang jatuh di dalam wilayah pusat objek (bukan hanya satu sel, tetapi area 3×3 di sekitar pusat, disebut *multi positives*) menjadi kandidat positif. Hasilnya: jumlah prediksi dan parameter head menyusut, dan seluruh hiperparameter *anchor* hilang.

### Decoupled Head

Pada YOLO klasik, satu cabang konvolusi menghasilkan keluaran klasifikasi dan regresi sekaligus. Kedua tugas ini memiliki kebutuhan fitur berbeda: klasifikasi membutuhkan fitur semantik "objek apa", regresi membutuhkan fitur geometris "di mana dan seberapa besar". YOLOX memisahkannya: satu konvolusi 1×1 mereduksi kanal, lalu dua cabang paralel (masing-masing dua konvolusi 3×3) menghasilkan keluaran klasifikasi dan regresi-objek secara terpisah. Efek yang dilaporkan: konvergensi pelatihan jauh lebih cepat dan akurasi akhir naik sekitar 1 poin AP — biaya komputasi tambahannya kecil.

```
peta fitur dari backbone+neck
        │  konvolusi 1×1 (reduksi kanal)
        ├──────────────┬──────────────────┐
        ▼              ▼                  ▼
  cabang klasifikasi  cabang regresi     (skor objek)
  2× konvolusi 3×3    2× konvolusi 3×3
        │              │                  │
        ▼              ▼                  ▼
   skor kelas      x, y, w, h         objectness
   per lokasi      per lokasi         per lokasi

  setiap lokasi = SATU prediksi (anchor-free, tanpa anchor berlapis)
```

### SimOTA: Penetapan Label Dinamis

Ini komponen paling teknis. Saat melatih detektor, setiap objek kebenaran harus "dipasangkan" dengan kandidat prediksi yang akan diawasi — pasangan inilah *label assignment*. OTA memformulasikannya sebagai masalah *optimal transport*: memasangkan pemasok (kandidat prediksi) ke penerima (objek kebenaran dan latar) dengan biaya total minimum, di mana biaya sebuah pasangan dihitung dari kualitas prediksi (galat klasifikasi + galat regresi). Formulasi ini bagus tetapi mahal — menambah ±25% waktu pelatihan karena algoritme iteratifnya.

SimOTA adalah penyederhanaannya: alih-alih menyelesaikan transport optimal penuh, untuk setiap objek dipilih **top-k** kandidat berbiaya terendah — dan k-nya sendiri diperkirakan dinamis dari distribusi IOU kandidat terbaik objek itu. Objek yang memiliki banyak kandidat berkualitas mendapat banyak contoh positif; objek yang sulit mendapat sedikit tetapi yang terbaik. Menurut naskah, SimOTA mempertahankan seluruh keuntungan OTA tanpa biaya iterasinya.

### Pelatihan

Di atas tiga perubahan itu, YOLOX memakai resep pelatihan kuat: augmentasi Mosaic (dari bab 004) ditambah MixUp (mencampur dua citra dan labelnya secara proporsional), keduanya dimatikan pada 15 *epoch* terakhir agar model menutup pelatihan pada data bersih. Baseline-nya sendiri sudah kuat: YOLOv3-SPP dengan *weight averaging* (EMA), penjadwalan kosinus, dan IoU loss.

## Eksperimen dan Hasil

Pengujian utama pada COCO lintas skala model, dari Nano hingga X, dengan ablation atas tiap komponen. Hasil utama:

- YOLOX-DarkNet53: 47,3% AP — menaikkan backbone YOLOv3 melampaui praktik terbaik sebelumnya sebesar 3,0 poin.
- YOLOX-L: 50,0% AP pada 68,9 FPS (Tesla V100), melampaui YOLOv5-L sebesar 1,8 poin pada jumlah parameter setara.
- YOLOX-Nano: 25,3% AP dengan 0,91 juta parameter dan 1,08 GFLOPs (melampaui NanoDet 1,8 poin); YOLOX-Tiny 32,8% AP — membuka pemakaian pada perangkat tepi.
- Satu model YOLOX-L memenangi Streaming Perception Challenge (WAD, CVPR 2021).

Ablation menunjukkan kontribusi berjenjang: augmentasi kuat memberi lompatan terbesar dari baseline, disusul *decoupled head* (yang juga mempercepat konvergensi) dan SimOTA sebagai pendorong akhir tanpa biaya inferensi.

## Kelebihan dan Keterbatasan

Kelebihan: (1) akurasi naik konsisten pada semua skala model, dari perangkat tepi hingga server; (2) desain lebih sederhana — tanpa *anchor*, tanpa hiperparameter bentuk kotak; (3) SimOTA memberi gain tanpa menambah biaya inferensi; (4) dukungan *deployment* luas (ONNX, TensorRT, NCNN, OpenVINO).

Keterbatasan: (1) SimOTA menambah kompleksitas prosedur pelatihan dibanding penetapan statis; (2) resep augmentasi kuat menuntut penjadwalan cermat (harus dimatikan di akhir pelatihan); (3) opsi *end-to-end* tanpa NMS yang dieksplorasi makalah masih kalah dari varian ber-NMS; (4) dari sisi konseptual, perubahan-perubahan ini adalah adopsi terukur dari literatur (FCOS, OTA) — kekuatan makalah ada pada integrasinya, bukan pada kebaruan tiap komponen.

## Kaitan dengan Bab Lain

YOLOX menutup garis evolusi yang dimulai bab 001: formulasi grid-regresi dipertahankan, tetapi *anchor* yang diperkenalkan bab 002 justru dihapus — kembali ke prediksi langsung, kini dengan mesin yang jauh lebih matang. Gagasan *anchor-free*-nya mewarisi FCOS (bab 019), resep pelatihannya mewarisi Mosaic dari bab 004, dan backbone-nya adalah Darknet-53 dari bab 003. Ke depan, desain *anchor-free* + *decoupled head* + penetapan label dinamis menjadi cetak biru yang diikuti banyak YOLO generasi berikutnya dalam tinjauan ini (bab 006–009), dan menjadi titik berangkat alami bagi integrasi RGB-D modern.

## Poin untuk Sitasi

Kutip dengan kunci `ge2021yolox`. Ringkasan yang aman dikutip: "YOLOX mengonversi YOLO menjadi detektor *anchor-free* dengan *decoupled head* dan penetapan label dinamis SimOTA, mencapai 47,3% AP (backbone YOLOv3) hingga 50,0% AP pada 68,9 FPS (YOLOX-L) pada COCO." Seluruh angka pada bab ini berasal dari abstrak dan tabel naskah; rincian ablation per komponen sebaiknya dikutip langsung dari tabel naskah.
