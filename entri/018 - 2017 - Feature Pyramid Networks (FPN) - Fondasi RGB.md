# 018 - Feature Pyramid Networks for Object Detection

## Metadata Ringkas

| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2017fpn` |
| Judul asli | Feature Pyramid Networks for Object Detection |
| Penulis | Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He, Bharath Hariharan, Serge Belongie |
| Tahun | 2017 |
| Venue | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), hal. 2117–2125 |
| Tema | Fondasi RGB |

## Tautan Akses

- **arXiv (naskah lengkap):** https://arxiv.org/abs/1612.03144
- **DOI:** https://doi.org/10.48550/arXiv.1612.03144
- **CVPR Open Access:** https://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.html
- **Google Scholar:** https://scholar.google.com/scholar?q=Feature%20Pyramid%20Networks%20for%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Feature%20Pyramid%20Networks%20for%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan *Feature Pyramid Network* (FPN), arsitektur yang membangun piramida fitur bersemantik kuat pada semua skala dari satu citra masukan berskala tunggal. Masalah yang dipecahkan adalah ketimpangan pada jaringan konvolusi dalam: peta fitur beresolusi tinggi tepat lokalisasinya tetapi lemah semantiknya, sedangkan peta fitur dalam kaya semantik tetapi kasar resolusinya. FPN menyelesaikannya dengan jalur *top-down* yang mengalirkan semantik ke resolusi tinggi dan koneksi lateral yang menggabungkannya dengan fitur *backbone* (jaringan konvolusi ekstraksi fitur utama), hampir tanpa biaya tambahan karena memakai kembali fitur yang sudah dihitung. Dipasang pada detektor Faster R-CNN, FPN mencapai 36,2 *Average Precision* (AP) pada COCO *test-dev*, melampaui semua hasil model tunggal sebelumnya termasuk pemenang kompetisi COCO 2016, dengan kecepatan inferensi sekitar 5 *frame* per detik (FPS).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Mengenali objek pada ukuran yang sangat bervariasi merupakan tantangan dasar dalam deteksi objek. Solusi standar sebelum jaringan konvolusi dalam adalah piramida citra berfitur: citra diubah ukurannya ke banyak skala, lalu fitur (misalnya HOG atau SIFT) dihitung pada setiap skala secara independen; detektor DPM bahkan mengambil sampel hingga 10 skala per oktaf. Pendekatan ini akurat tetapi mahal: waktu inferensi meningkat hingga empat kali lipat, dan pelatihan *end-to-end* pada piramida citra tidak memungkinkan karena keterbatasan memori. Akibatnya, detektor berbasis jaringan dalam seperti Fast R-CNN dan Faster R-CNN — detektor dua tahap yang memakai proposal wilayah (lihat [bab 014](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)) — memakai peta fitur satu skala saja demi kecepatan, dengan konsekuensi deteksi objek kecil yang terbatas.

Jaringan konvolusi sebenarnya sudah menghasilkan hierarki fitur multi-skala secara internal, tetapi terdapat jurang semantik antarlevel: fitur dangkal hanya mengodekan pola tingkat rendah seperti tepi. Detektor satu tahap SSD (lihat [bab 015](./015%20-%202016%20-%20SSD%20-%20Fondasi%20RGB.md)) memakai hierarki ini untuk prediksi multi-skala, tetapi sengaja menghindari peta fitur dangkal dan mulai membangun piramida dari lapisan atas (misalnya conv4_3), sehingga kehilangan peta beresolusi tinggi yang justru penting bagi objek kecil. Inilah yang diperbaiki FPN: piramida fitur internal yang kuat semantik di semua level, tanpa harga komputasi piramida citra.

## Ide Utama

Gagasan inti FPN sederhana: hierarki multi-skala yang sudah ada di dalam jaringan konvolusi dapat dijadikan piramida fitur penuh asalkan setiap levelnya diperkaya dengan semantik dari level di atasnya. Masukannya satu citra berskala tunggal; keluarannya sekumpulan peta fitur pada beberapa resolusi, masing-masing dengan jumlah kanal sama dan semantik kuat. Pengayaan dilakukan oleh jalur *top-down*: peta fitur kasar dari level atas diperbesar resolusinya (*upsampling*) lalu dijumlahkan elemen demi elemen dengan peta fitur *backbone* pada resolusi yang sama melalui koneksi lateral berupa konvolusi 1×1. Prediksi dilakukan independen pada setiap level, seperti pada piramida citra berfitur, tetapi hampir tanpa biaya tambahan.

## Cara Kerja Langkah demi Langkah

### Jalur Bottom-Up

Jalur *bottom-up* adalah perhitungan umpan maju *backbone* konvolusi biasa; makalah ini memakai ResNet, jaringan konvolusi dalam dengan koneksi residual. *Backbone* dibagi menjadi beberapa tahap (*stage*) yang masing-masing menurunkan resolusi spasial dengan faktor dua. Keluaran blok residual terakhir setiap tahap diambil sebagai acuan, diberi nama {C2, C3, C4, C5} dengan *stride* {4, 8, 16, 32} piksel terhadap citra masukan. *Stride* adalah jarak piksel pada citra asal yang diwakili satu sel peta fitur; stride 32 berarti satu sel mencakup wilayah 32×32 piksel. Tahap conv1 tidak disertakan karena jejak memorinya besar. Sebagai contoh, untuk citra 800×800 piksel, C2 berukuran 200×200, C3 100×100, C4 50×50, dan C5 25×25.

### Jalur Top-Down dan Koneksi Lateral

Pembangunan piramida dimulai dari atas: C5 dilewatkan ke konvolusi 1×1 yang mereduksi jumlah kanal menjadi 256. Konvolusi 1×1 (kernel satu kali satu piksel) mengubah jumlah kanal tanpa mengubah resolusi spasial. Hasilnya kemudian diperbesar resolusinya dua kali lipat dengan *upsampling* *nearest neighbor* (setiap nilai disalin ke empat sel berdekatan), lalu dijumlahkan elemen demi elemen dengan hasil konvolusi 1×1 dari C4. Proses yang sama diulang hingga level paling halus. Terakhir, setiap peta hasil penjumlahan dilewatkan ke konvolusi 3×3 untuk meredam efek *aliasing* (artefak tepi akibat *upsampling*), menghasilkan himpunan akhir {P2, P3, P4, P5}. Semua level piramida memiliki dimensi kanal tetap d = 256, dan lapisan-lapisan tambahan ini tidak memakai fungsi nonlinier karena pengaruhnya terbukti kecil. Satu level tambahan, P6, dibentuk dengan pencuplikan P5 berstride dua dan hanya dipakai oleh RPN untuk menampung *anchor* terbesar.

Diagram berikut menggambarkan aliran data antara kedua jalur pada ResNet dengan citra masukan 800×800 piksel.

```
 bottom-up (ResNet)      fusi                top-down        piramida akhir
                                                              (d = 256 kanal)

 C5 (25x25)  ──[1x1 konv]────────────────────────[3x3 konv]──► P5 (s=32)
                    │
                    ▼ upsampling 2x (nearest neighbor)
 C4 (50x50)  ──[1x1 konv]──►(+) penjumlahan ────[3x3 konv]──► P4 (s=16)
                    │
                    ▼ upsampling 2x
 C3 (100x100)──[1x1 konv]──►(+) penjumlahan ────[3x3 konv]──► P3 (s=8)
                    │
                    ▼ upsampling 2x
 C2 (200x200)──[1x1 konv]──►(+) penjumlahan ────[3x3 konv]──► P2 (s=4)
```

Titik (+) menunjukkan penjumlahan elemen demi elemen antara peta hasil *upsampling* dari level di atasnya dan peta hasil konvolusi 1×1 dari *backbone*. Karena penjumlahan memerlukan dimensi sama, konvolusi 1×1 menyetarakan jumlah kanal terlebih dahulu. Hasilnya, P2 beresolusi tinggi tetapi kini membawa semantik kuat yang diwariskan berjenjang dari C5.

### FPN pada RPN

*Region Proposal Network* (RPN) adalah detektor *sliding window* kelas-agnostik: jaringan kecil digeser rapat di atas peta fitur untuk memprediksi skor keberadaan objek dan regresi *bounding box* (kotak pembatas objek) terhadap sekumpulan kotak acuan berukuran tetap yang disebut *anchor*. RPN asli bekerja pada satu peta fitur skala tunggal sehingga memerlukan banyak skala *anchor*. Dengan FPN, *head* yang sama (konvolusi 3×3 diikuti dua konvolusi 1×1 untuk klasifikasi dan regresi) dipasang pada setiap level, dan setiap level cukup diberi satu skala *anchor*: {32², 64², 128², 256², 512²} piksel pada {P2, P3, P4, P5, P6}, masing-masing dengan tiga rasio aspek {1:2, 1:1, 2:1}, total 15 *anchor* di seluruh piramida. Parameter *head* dibagi di semua level; pembagian ini tidak menurunkan akurasi, bukti bahwa semua level memiliki tingkat semantik setara. Pelabelan mengikuti aturan RPN asli berdasarkan *Intersection over Union* (IoU), rasio luas irisan terhadap gabungan dua kotak: *anchor* ber-IoU di atas 0,7 terhadap kotak benar berlabel positif, di bawah 0,3 berlabel negatif.

### FPN pada Fast R-CNN

Fast R-CNN adalah detektor berbasis wilayah: setiap proposal wilayah (*Region of Interest*, RoI) diekstrak fiturnya dengan *RoI pooling* lalu diklasifikasikan. Agar RoI berbagai ukuran diarahkan ke level piramida yang tepat, dipakai rumus penempatan k = ⌊k₀ + log₂(√(wh)/224)⌋, dengan w dan h lebar-tinggi RoI pada citra masukan dan k₀ = 4 sebagai level acuan untuk RoI 224×224 (ukuran kanonis pra-pelatihan ImageNet). Contohnya, RoI 112×112 menghasilkan √(wh) = 112, sehingga log₂(112/224) = −1 dan k = 3: objek kecil diarahkan ke level beresolusi lebih halus. Setiap RoI kemudian dipooling ke ukuran 7×7 dan dilewatkan ke dua lapisan terhubung penuh (*fully-connected*) 1024 dimensi sebelum lapisan klasifikasi dan regresi. *Head* dua lapisan ini lebih ringan daripada *head* conv5 sembilan lapis pada Faster R-CNN berbasis ResNet, sehingga sebagian biaya piramida terkompensasi.

## Eksperimen dan Hasil

Eksperimen dilakukan pada dataset COCO 80 kelas: pelatihan pada gabungan 80 ribu citra latih dan 35 ribu citra validasi (*trainval35k*), ablasi pada 5 ribu citra *minival*, dan hasil akhir pada *test-dev* yang labelnya tidak dipublikasikan. Sisi pendek citra diubah menjadi 800 piksel saat pelatihan dan pengujian.

Hasil utama dengan ResNet-50 dirangkum pada tabel berikut.

| Pengujian | Metrik | Baseline | FPN | Selisih |
|---|---|---|---|---|
| RPN (proposal) | AR1k | 48,3 (pada C4) | 56,3 | +8,0 |
| RPN, objek kecil | AR1k-S | 32,0 | 44,9 | +12,9 |
| Fast R-CNN (proposal tetap) | AP | 31,9 | 33,9 | +2,0 |
| Fast R-CNN, objek kecil | AP-S | 15,7 | 17,8 | +2,1 |
| Faster R-CNN (test-dev, ResNet-101) | AP | 35,7 (G-RMI, pemenang 2016) | 36,2 | +0,5 |

Interpretasinya sebagai berikut. Pada RPN, metrik AR1k (rata-rata *recall*, yakni proporsi objek benar yang terjangkau, dengan 1000 proposal per citra) naik 8,0 poin, dan kenaikan terbesar terjadi pada objek kecil (+12,9 poin), menegaskan bahwa level halus bersemantik kuat menjawab kelemahan pendekatan skala tunggal. Pada Fast R-CNN dengan proposal yang sama, AP naik 2,0 poin, sehingga perbaikan tidak hanya datang dari proposal yang lebih baik tetapi juga dari fitur klasifikasi yang lebih kuat. Pada sistem Faster R-CNN penuh, FPN mengungguli baseline skala tunggal yang kuat sebesar 2,3 poin AP dan 3,8 poin AP@0,5 (AP pada ambang IoU 0,5). Di papan peringkat COCO, model tunggal ini melampaui pemenang kompetisi 2016 (G-RMI) tanpa memakai piramida citra.

Uji ablasi menegaskan peran tiap komponen. Menghapus koneksi lateral menurunkan AR1k RPN dari 56,3 menjadi 46,1 (turun 10,2 poin) karena lokalisasi fitur tidak lagi tepat setelah penurunan-penaikan resolusi berulang. Menghapus jalur *top-down* menurunkan AP Fast R-CNN dari 33,9 menjadi 24,9 (−9,0 poin), bukti kerugian besar bila fitur dangkal dipakai tanpa pengayaan semantik. Memakai hanya level P2 (dengan 750 ribu *anchor*) hanya mencapai 33,4 AP, sehingga jumlah *anchor* besar saja tidak menggantikan representasi piramida. Dari sisi kecepatan, inferensi memerlukan 0,148 detik per citra (ResNet-50) dan 0,172 detik (ResNet-101) pada satu GPU NVIDIA M40, lebih cepat daripada baseline skala tunggal ResNet-50 (0,32 detik) karena *head* yang lebih ringan. Sebagai ekstraktor fitur generik, FPN juga dipakai untuk proposal segmentasi: AR 48,1, melampaui DeepMask, SharpMask, dan InstanceFCN lebih dari 8,3 poin dengan kecepatan 6–7 FPS.

## Kelebihan dan Keterbatasan

Kelebihan utama FPN adalah manfaat piramida citra berfitur dengan biaya tambahan marjinal: semua level dihitung dari satu skala masukan, dilatih *end-to-end*, dan konsisten antara pelatihan dan pengujian. Perbaikan terbesar terjadi pada objek kecil. Rancangannya sederhana dan independen terhadap pilihan *backbone*, sehingga mudah dipasang pada berbagai detektor.

Keterbatasannya bersifat halus. Penulis melaporkan bahwa lapisan ekstra menambah jejak memori, meski sebagian terkompensasi oleh *head* yang lebih ringan. Dari sisi rekayasa, fusi penjumlahan memperlakukan kontribusi kedua jalur sama rata, dan *upsampling* *nearest neighbor* tidak menyelaraskan fitur secara adaptif; PANet menambahkan jalur agregasi *bottom-up* kedua dan BiFPN memakai fusi berbobot untuk menutup kekurangan ini. Secara konseptual, rumus penempatan RoI adalah heuristik tetap dengan acuan 224 piksel, sehingga pembagian objek ke level piramida tidak dipelajari dari data.

## Kaitan dengan Bab Lain

Bab ini melanjutkan silsilah detektor dua tahap: FPN menggantikan peta fitur skala tunggal pada Faster R-CNN ([bab 014](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)) dan menjawab keterbatasan SSD ([bab 015](./015%20-%202016%20-%20SSD%20-%20Fondasi%20RGB.md)) yang memakai hierarki fitur tanpa pengayaan *top-down*. Dua makalah dari kelompok yang sama membangun di atasnya: RetinaNet ([bab 016](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md)) memakai FPN sebagai tulang punggung detektor satu tahapnya, dan Mask R-CNN ([bab 017](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md)) memadukan FPN untuk deteksi sekaligus segmentasi instans. Di jalur YOLO, prediksi multi-skala pada piramida fitur muncul pada YOLOv3 ([bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)), lalu *neck* turunan FPN seperti PAN dipakai pada YOLOv4 ([bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)); FPN kemudian menjadi pola *neck* standar, yakni modul penghubung *backbone* dan *head*, pada hampir semua detektor modern.

## Poin untuk Sitasi

Kunci BibTeX: `lin2017fpn`. Ringkasan yang aman dikutip: FPN membangun piramida fitur kaya semantik pada semua skala melalui jalur *top-down* dan koneksi lateral di atas hierarki bawaan jaringan konvolusi, dengan biaya komputasi tambahan marjinal; dipasang pada Faster R-CNN, metode ini mencapai 36,2 AP pada COCO *test-dev* dan melampaui seluruh hasil model tunggal sebelumnya, termasuk pemenang kompetisi COCO 2016. Catatan verifikasi: abstrak versi CVPR menyebut 5 FPS sedangkan abstrak arXiv v2 menyebut 6 FPS; cocokkan versi naskah yang dikutip sebelum sitasi formal.
