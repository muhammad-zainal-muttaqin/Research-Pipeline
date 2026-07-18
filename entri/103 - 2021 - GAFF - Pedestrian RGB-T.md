# 103 - Guided Attentive Feature Fusion for Multispectral Pedestrian Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2021gaff` |
| Judul asli | Guided Attentive Feature Fusion for Multispectral Pedestrian Detection |
| Penulis | Heng Zhang, Elisa Fromont, Sébastien Lefèvre, Bruno Avignon |
| Tahun | 2021 |
| Venue | IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2021) |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **Kode resmi (GitHub):** https://github.com/zhanghengdev/GAFF
- **Naskah (CVF Open Access):** https://openaccess.thecvf.com/content/WACV2021/papers/Zhang_Guided_Attentive_Feature_Fusion_for_Multispectral_Pedestrian_Detection_WACV_2021_paper.pdf
- **Naskah versi penulis (HAL):** https://hal.science/hal-03119907
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Guided%20Attentive%20Feature%20Fusion%20for%20Multispectral%20Pedestrian%20Detection&sort=relevance

## Gambaran Umum

Makalah ini mengusulkan GAFF (*Guided Attentive Feature Fusion*), sebuah metode fusi fitur untuk deteksi pejalan kaki dari pasangan citra RGB (warna tampak) dan *thermal* (inframerah panjang, sensitif terhadap suhu benda). Alih-alih menggabungkan fitur kedua modal secara seragam di seluruh citra, GAFF memakai dua modul *attention* (penyorotan bobot perhatian) berurutan: satu bekerja di dalam tiap modal secara terpisah, satu lagi bekerja lintas modal untuk menentukan seberapa besar kontribusi tiap modal pada tiap posisi fitur. Kedua modul ini memandu proses penggabungan sehingga fitur yang tidak relevan atau berderau dari salah satu modal ditekan sebelum ikut memengaruhi prediksi.

Metode diuji pada dua tolok ukur deteksi pejalan multispektral publik, KAIST dan CVC-14. Pada KAIST, penulis melaporkan *miss rate* (tingkat kegagalan deteksi; makin rendah makin baik) 6,48% pada subset Reasonable-All, dengan waktu inferensi 9,34 milidetik per citra di GPU GTX 1080Ti — sekitar 107 citra per detik. Angka ini menunjukkan bahwa penambahan dua modul *attention* tidak membebani kecepatan model secara berarti dibandingkan tulang punggung (*backbone*) konvolusi yang dipakai. Makalah ini menjadi salah satu rujukan penting pada garis kerja fusi RGB-*thermal* yang memandu penggabungan fitur secara adaptif, bukan sekadar menggabungkannya secara statis.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi pejalan kaki dengan kamera RGB tunggal gagal pada kondisi minim cahaya: pada malam hari, tekstur dan warna yang menjadi andalan fitur RGB nyaris tidak terlihat. Kamera *thermal* mengatasi ini karena mengukur radiasi panas tubuh, sehingga tetap berfungsi dalam gelap, tetapi kehilangan detail tekstur dan warna yang berguna pada siang hari, dan rentan salah kenali sumber panas non-manusia (misalnya kendaraan atau permukaan jalan yang panas) sebagai objek. Karena kelemahan kedua modal saling melengkapi, banyak sistem menggabungkan keduanya. Dataset KAIST Multispectral Pedestrian (dibahas pada bab 100) menjadi tolok ukur standar untuk menguji pendekatan semacam ini.

Pendekatan fusi paling sederhana, dikenal sebagai *halfway fusion*, menggabungkan peta fitur RGB dan *thermal* pada satu kedalaman jaringan tertentu — biasanya dengan penggabungan kanal (*concatenation*) — tanpa mekanisme yang memutuskan modal mana yang lebih dapat dipercaya pada posisi tertentu. Penggabungan seragam semacam ini menyertakan fitur yang tidak relevan dari modal yang sedang tidak andal, misalnya derau termal pada siang hari yang terang atau area gelap tanpa kontras pada citra RGB malam hari. IAF R-CNN (bab 101) memperbaiki ini dengan memakai satu skalar estimasi iluminasi per citra untuk memberi bobot pada tiap modal, tetapi bobot itu berlaku sama untuk seluruh citra — tidak membedakan wilayah spasial atau kanal fitur tertentu di dalam citra yang sama. Masalah yang belum terpecahkan adalah bagaimana memandu fusi secara lebih halus: menyoroti wilayah penting di dalam tiap modal sebelum digabung, dan memutuskan bobot kontribusi antar-modal secara lokal, bukan dengan satu angka global.

## Ide Utama

Gagasan inti GAFF adalah memecah proses fusi menjadi dua tahap *attention* yang saling melengkapi. Tahap pertama, *attention* intra-modal, bekerja di dalam satu modal (RGB atau *thermal*) sendiri-sendiri: modul ini mempelajari peta bobot yang menonjolkan wilayah dan kanal fitur yang informatif pada modal itu, dan menekan wilayah yang kurang relevan, sebelum modal tersebut dipertemukan dengan modal lain. Tahap kedua, *attention* inter-modal, mengambil fitur yang telah disaring itu dari kedua modal lalu mempelajari bobot yang menentukan seberapa besar kontribusi tiap modal pada tiap posisi fitur gabungan. Dengan urutan ini, penggabungan fitur tidak lagi berupa penjumlahan atau penggabungan kanal yang seragam, melainkan hasil dua keputusan berjenjang: "bagian mana dari modal ini yang penting" diikuti "modal mana yang lebih dipercaya di posisi ini".

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Dua Cabang

Citra RGB dan citra *thermal* dari pasangan yang sama diproses oleh dua cabang jaringan konvolusi yang berjalan paralel, satu untuk tiap modal. Kedua cabang menghasilkan peta fitur dengan resolusi spasial yang sama pada tiap tahap, sehingga fitur dari posisi piksel yang sama pada kedua modal dapat dibandingkan dan digabung langsung.

### Attention Intra-Modal

Pada tiap cabang, modul *attention* intra-modal menghitung peta bobot dari peta fitur cabang itu sendiri, lalu memakainya untuk menskalakan ulang fitur asli — memperkuat wilayah yang informatif dan melemahkan wilayah yang tidak relevan. Pada cabang *thermal*, misalnya, ini berguna untuk menekan sumber panas yang bukan pejalan kaki; pada cabang RGB, untuk menekan latar belakang bertekstur ramai yang tidak berkaitan dengan objek. Proses ini terjadi sebelum informasi dari kedua modal dipertemukan, sehingga tiap modal "membersihkan" fiturnya sendiri lebih dulu.

### Attention Inter-Modal

Setelah tiap modal melalui penyaringan intra-modal, modul *attention* inter-modal membandingkan fitur kedua cabang dan mempelajari bobot yang menentukan proporsi kontribusi RGB versus *thermal* pada tiap posisi fitur. Berbeda dari IAF R-CNN yang memberi satu bobot iluminasi untuk seluruh citra, mekanisme ini beroperasi pada level fitur yang lebih rinci, sehingga wilayah berbeda dalam citra yang sama dapat memiliki bobot modal yang berbeda pula.

### Modul Fusi Terpandu

Fitur RGB dan *thermal* yang telah diberi bobot oleh kedua tahap *attention* kemudian digabung menjadi satu peta fitur tunggal. Peta fitur gabungan inilah yang diteruskan ke kepala deteksi (bagian jaringan yang memprediksi kotak pembatas dan kelas objek).

Alur pemrosesan dari dua citra masukan hingga fitur gabungan dapat diringkas sebagai berikut.

```
 citra RGB ──> cabang konv. RGB ──> attention intra-modal (RGB)
                                            │
                                            ▼
                                   attention inter-modal
                                   (bobot kontribusi per
                                    posisi & per modal)
                                            ▲
                                            │
 citra thermal ─> cabang konv. IR ──> attention intra-modal (IR)
                                            │
                                            ▼
                                  modul fusi terpandu
                                            │
                                            ▼
                                    kepala deteksi
                                 (kotak + kelas pejalan)
```

### Kepala Deteksi dan Pelatihan

Peta fitur gabungan dipakai oleh kepala deteksi untuk memprediksi kotak pembatas pejalan kaki beserta skor keyakinannya. Karena seluruh komponen — dua cabang ekstraksi fitur, dua modul *attention*, dan kepala deteksi — merupakan bagian dari satu jaringan, seluruh parameter dilatih bersama secara *end-to-end* terhadap tujuan akhir deteksi, sehingga bobot *attention* yang dipelajari langsung diarahkan untuk memperbaiki akurasi deteksi, bukan tujuan antara yang terpisah.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada KAIST Multispectral Pedestrian Benchmark, tolok ukur pasangan RGB-*thermal* yang menjadi rujukan standar pada klaster ini (bab 100), dan pada CVC-14, dataset pejalan kaki siang-malam RGB-*thermal* kedua. Metrik yang dipakai adalah *miss rate* (MR) skala-log rata-rata: proporsi pejalan kaki yang gagal terdeteksi pada rentang tingkat *false positive* tertentu — semakin rendah nilainya semakin baik.

Pada KAIST, GAFF mencapai MR 6,48% pada subset Reasonable-All (kondisi pejalan kaki berukuran wajar, tidak terhalang berat, digabung siang dan malam), 8,35% pada subset Reasonable-Day, dan 3,46% pada subset Reasonable-Night. Interpretasinya: performa pada malam hari justru lebih baik daripada siang hari untuk metode ini, konsisten dengan gagasan bahwa *attention* inter-modal berhasil memberi bobot lebih besar pada fitur *thermal* saat kondisi cahaya kurang mendukung modal RGB. Waktu inferensi 9,34 milidetik per citra pada satu GPU GTX 1080Ti (setara sekitar 107 citra per detik) menunjukkan bahwa dua modul *attention* tambahan tidak menimbulkan beban komputasi yang berat dibandingkan komputasi cabang konvolusi utama.

Penulis juga melaporkan pengujian pada CVC-14 dan menyatakan bahwa mekanisme *attention* terpandu memberi perbaikan dibandingkan metode fusi RGB-*thermal* lain yang mereka bandingkan pada saat publikasi. Angka MR spesifik pada CVC-14 serta rincian tabel perbandingan lengkap terhadap metode-metode pembanding (misalnya *halfway fusion* dan metode berbasis *attention* lain pada KAIST) tidak berhasil dipastikan dari sumber yang terjangkau untuk penulisan bab ini, sehingga tidak dicantumkan sebagai angka pasti dan perlu diverifikasi langsung ke tabel naskah asli sebelum dikutip. Studi ablasi pada makalah membandingkan kontribusi modul *attention* intra-modal dan inter-modal secara terpisah; penulis melaporkan bahwa kedua modul memberi kontribusi masing-masing terhadap penurunan MR, tetapi nilai numerik tiap konfigurasi ablasi juga belum dapat dipastikan dari sumber yang terjangkau.

## Kelebihan dan Keterbatasan

Kelebihan metode ini terletak pada granularitas pembobotan fusi. Dibandingkan dengan pembobotan iluminasi tunggal per citra pada IAF R-CNN, GAFF memberi bobot yang bervariasi antar-posisi dan antar-kanal fitur, sehingga dapat menangani kondisi pencahayaan campuran dalam satu citra yang sama (misalnya bagian citra yang terkena bayangan sementara bagian lain tersinari terang). Pemisahan tahap intra-modal dan inter-modal juga membuat tiap modul menangani masalah yang berbeda secara eksplisit: intra-modal menyaring derau di dalam satu modal, inter-modal memutuskan kepercayaan relatif antar-modal. Kecepatan inferensi yang dilaporkan (9,34 ms per citra) menunjukkan tambahan komputasi dari kedua modul *attention* relatif kecil terhadap keseluruhan jaringan.

Dari sisi rekayasa, kedua modul *attention* menambah operasi dan parameter pada dua cabang jaringan sekaligus, sehingga anggaran komputasi total tetap lebih besar daripada jaringan satu-modal saja; angka biaya komputasi (jumlah parameter, FLOPs) di luar waktu inferensi tidak tercakup dalam sumber yang terjangkau untuk bab ini. Secara konseptual, metode ini mengasumsikan pasangan RGB-*thermal* yang telah sejajar secara spasial (piksel pada posisi yang sama di kedua modal merujuk titik fisik yang sama); bila penyejajaran kedua kamera tidak presisi, asumsi ini dapat menurunkan efektivitas *attention* inter-modal. Evaluasi pada makalah juga terbatas pada tugas deteksi pejalan kaki di dua dataset; generalisasi mekanisme *attention* terpandu ini ke tugas deteksi objek multispektral lain di luar domain pejalan kaki tidak diuji dalam makalah ini.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis kerja fusi RGB-*thermal* pada dataset KAIST (bab 100) dan secara langsung memperbaiki keterbatasan IAF R-CNN (bab 101): bobot iluminasi tunggal per citra pada IAF R-CNN digantikan dengan dua tahap *attention* yang beroperasi pada level fitur lokal. Bab ini juga berdampingan dengan MBNet (bab 102), yang menangani ketimpangan keandalan modal (*modality imbalance*) melalui desain cabang berbeda, sehingga kedua bab dapat dibandingkan sebagai dua strategi berbeda untuk masalah yang sama: MBNet melalui arsitektur cabang yang dibedakan sejak awal, GAFF melalui mekanisme *attention* terpandu yang dipelajari. Gagasan pembobotan lintas-modal yang dipelajari secara lokal ini diteruskan pada karya-karya berikutnya di klaster yang sama, termasuk Cyclic Fuse-and-Refine (bab 104) dan CMPD (bab 105), yang mengembangkan mekanisme pemanduan fusi lebih lanjut dengan mempertimbangkan ketidakpastian antar-modal.

Tautan bab terkait:
- [100 - 2015 - KAIST Multispectral Pedestrian - Pedestrian RGB-T](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md)
- [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md)
- [102 - 2020 - MBNet - Pedestrian RGB-T](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)
- [104 - 2020 - Cyclic Fuse-and-Refine (CFR) - Pedestrian RGB-T](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md)
- [105 - 2022 - CMPD (Uncertainty-Guided Cross-Modal) - Pedestrian RGB-T](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md)

## Poin untuk Sitasi

Kutip dengan kunci `zhang2021gaff`. Ringkasan yang aman dikutip: "GAFF memandu fusi fitur RGB-*thermal* untuk deteksi pejalan kaki melalui dua tahap *attention* berjenjang — intra-modal lalu inter-modal — dan mencapai *miss rate* 6,48% pada subset Reasonable-All KAIST dengan waktu inferensi 9,34 milidetik per citra pada GPU GTX 1080Ti." Angka MR (6,48%; 8,35%; 3,46%) dan waktu inferensi (9,34 ms) berasal dari repositori kode resmi penulis dan diyakini konsisten dengan naskah, tetapi sebaiknya dicocokkan langsung ke tabel naskah WACV sebelum dikutip dalam karya formal. Belum terverifikasi dari sumber yang terjangkau untuk bab ini: angka *miss rate* pada CVC-14, tabel perbandingan numerik terhadap metode pembanding (*halfway fusion*, metode *attention* KAIST lain), rincian numerik studi ablasi intra- vs inter-modal, nama tulang punggung (*backbone*) konvolusi yang dipakai, dan jumlah parameter/FLOPs model.
