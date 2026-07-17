# 015 - SSD: Single Shot MultiBox Detector

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2016ssd` |
| Judul asli | SSD: Single Shot MultiBox Detector |
| Penulis | Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-Yang Fu, Alexander C. Berg |
| Tahun | 2016 |
| Venue | European Conference on Computer Vision (ECCV 2016) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1512.02325
- **DOI (versi ECCV/Springer):** https://doi.org/10.1007/978-3-319-46448-0_2
- **Kode sumber resmi (Caffe):** https://github.com/weiliu89/caffe/tree/ssd
- **Google Scholar:** https://scholar.google.com/scholar?q=SSD%3A%20Single%20Shot%20MultiBox%20Detector
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=SSD%3A%20Single%20Shot%20MultiBox%20Detector&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan SSD (*Single Shot MultiBox Detector*), detektor objek satu tahap yang memprediksi kotak pembatas objek dan skor kelas langsung dari beberapa peta fitur beresolusi berbeda dalam satu jaringan konvolusi. Dua gagasan dibawanya: ruang keluaran kotak didiskritisasi menjadi himpunan *default box* (kotak acuan beragam skala dan rasio aspek) pada setiap lokasi peta fitur; dan prediksi dilakukan pada beberapa peta fitur berbeda kedalaman — objek kecil ditangani peta dangkal beresolusi tinggi, objek besar oleh peta dalam beresolusi rendah.

Hasilnya menutup sebagian besar jurang akurasi antara detektor satu tahap dan dua tahap. Pada PASCAL VOC 2007, SSD dengan masukan 300×300 piksel mencapai 74,3% mAP pada 59 *frame* per detik (FPS) — lebih akurat dari Faster R-CNN (73,2% mAP pada 7 FPS) sekaligus sekitar delapan kali lebih cepat, dan jauh di atas YOLO (63,4% mAP pada 45 FPS). Varian dengan masukan 512×512 mencapai 76,8% mAP.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada 2016, bidang deteksi objek terbelah dua. Di satu sisi, keluarga dua tahap — R-CNN ([bab 012](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md)), Fast R-CNN ([bab 013](./013%20-%202015%20-%20Fast%20R-CNN%20-%20Fondasi%20RGB.md)), dan Faster R-CNN ([bab 014](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)) — memegang akurasi tertinggi: Faster R-CNN mencapai 73,2% mAP pada VOC 2007, tetapi hanya berjalan 7 FPS karena tahap proposal dan pengambilan ulang fitur (*feature resampling*) yang mahal. Di sisi lain, YOLO ([bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)) membuang tahap proposal dan mencapai 45 FPS, tetapi akurasinya turun ke 63,4% mAP — selisih hampir 10 poin.

Kelemahan YOLO bersifat struktural: prediksinya hanya dibuat dari satu peta fitur terakhir beresolusi kasar (grid 7×7), dan setiap sel hanya boleh memprediksi dua kotak dengan satu kelas, sehingga objek kecil dan objek yang berdekatan sering terlewat dan *recall*-nya (proporsi objek yang berhasil ditemukan) rendah. Pertanyaan makalah ini: dapatkah detektor satu tahap mempertahankan kecepatan YOLO dengan akurasi setara Faster R-CNN — dengan kata lain, bagaimana menangani keragaman ukuran dan bentuk objek tanpa tahap proposal?

## Ide Utama

Gagasan inti SSD adalah menggantikan satu grid prediksi kasar dengan banyak peta fitur berjenjang, lalu memasang beberapa *default box* berbentuk tetap pada setiap lokasi peta fitur untuk dinilai secara konvolusional. Masukan berupa satu citra; keluaran berupa ribuan pasangan (skor kelas, koreksi posisi kotak) yang dihitung dalam satu lintasan maju jaringan.

Intuisi mekanisnya terletak pada sifat lapisan konvolusi: makin dalam suatu lapisan, makin luas wilayah citra yang dicakup satu selnya (*receptive field*), tetapi makin kasar resolusinya. Menempelkan prediktor pada lapisan dangkal sekaligus lapisan dalam memberikan calon kotak untuk objek kecil maupun besar tanpa memproses citra pada beberapa ukuran.

## Cara Kerja Langkah demi Langkah

### Backbone VGG16 yang Dimodifikasi

SSD dibangun di atas VGG16 — jaringan klasifikasi 16 lapisan, dipangkas sebelum lapisan klasifikasinya, dilatih awal pada ImageNet. Dua lapisan terhubung penuh (*fully connected*) fc6 dan fc7 diubah menjadi konvolusi; lapisan *pooling* kelima diperlambat langkahnya (stride 1 dengan konvolusi berlubang/*atrous*) agar peta fitur tidak terlalu menyusut. Di atasnya ditambahkan lapisan-lapisan konvolusi baru yang ukurannya menurun berjenjang.

### Peta Fitur Multi-Skala untuk Prediksi

Untuk model SSD300 (masukan 300×300 piksel), prediksi dibuat pada enam peta fitur sekaligus: conv4_3 (38×38), conv7 (19×19), conv8_2 (10×10), conv9_2 (5×5), conv10_2 (3×3), dan conv11_2 (1×1). Peta 38×38 (1.444 lokasi) mengawasi wilayah sempit untuk objek kecil; peta 1×1 mengawasi seluruh citra untuk objek besar. Aliran datanya dirangkum pada diagram berikut.

```
 citra 300x300
      │
      ▼
 VGG16 terpangkas + lapisan konvolusi tambahan
      │
      ├───────────── peta fitur untuk prediksi ─────────────┐
      │   conv4_3  38x38  k=4    conv9_2   5x5  k=6         │
      │   conv7    19x19  k=6    conv10_2  3x3  k=4         │
      │   conv8_2  10x10  k=6    conv11_2  1x1  k=4         │
      └────────────────────────┬────────────────────────────┘
                               ▼
      tiap lokasi: filter 3x3 -> k x (skor kelas + 4 offset)
                               ▼
      8732 kotak kandidat -> NMS per kelas -> maks. 200 deteksi
```

Keenam peta fitur bekerja paralel; gabungan prediksinya menghasilkan 8.732 kandidat yang kemudian dirampingkan oleh NMS.

### Default Box: Skala dan Rasio Aspek

Setiap lokasi peta fitur memiliki k *default box* yang berpusat tepat di tengah selnya. Ukurannya diatur agar tiap peta fitur bertanggung jawab pada rentang ukuran objek tertentu: skala s_k dihitung dengan interpolasi linier dari 0,2 (lapisan paling dangkal) sampai 0,9 (lapisan paling dalam). Untuk tiap skala dipakai rasio aspek {1, 2, 3, 1/2, 1/3}, dengan lebar s_k√a_r dan tinggi s_k/√a_r — rasio 2 menghasilkan kotak melebar, rasio 1/2 kotak meninggi. Khusus rasio 1 ditambah satu kotak ekstra berskala √(s_k·s_{k+1}), sehingga k = 6; pada conv4_3, conv10_2, dan conv11_2 rasio 3 dan 1/3 dihilangkan sehingga k = 4.

Contoh numerik: pada SSD300, skala 0,2 berarti sisi kotak 0,2 × 300 = 60 piksel untuk rasio 1. Total seluruh kandidat adalah 38²×4 + 19²×6 + 10²×6 + 5²×6 + 3²×4 + 1²×4 = 8.732 *default box* per citra — bandingkan dengan 98 kandidat pada YOLO.

### Prediktor Konvolusi

Prediksi dibuat oleh filter konvolusi 3×3 yang digeser ke seluruh lokasi peta fitur. Pada peta dengan k *default box* per lokasi dan c kelas, dipakai k × (c + 4) filter: tiap kotak memperoleh c skor kelas dan 4 angka *offset* (pergeseran pusat serta perubahan lebar-tinggi relatif terhadap bentuk *default box*). Berbeda dengan YOLO yang memakai lapisan terhubung penuh di ujung jaringan, prediktor konvolusional ini mempertahankan struktur spasial.

### Penetapan Target dan Fungsi Loss

Saat pelatihan, tiap kotak kebenaran (*ground truth*) harus ditugaskan ke *default box* tertentu. Aturannya dua langkah: (1) tiap kotak kebenaran dipasangkan dengan *default box* yang *jaccard overlap*-nya paling besar — *jaccard overlap* adalah rasio luas irisan terhadap luas gabungan dua kotak, identik dengan IoU; (2) setiap *default box* dengan overlap di atas 0,5 terhadap kotak kebenaran mana pun ikut dijadikan contoh positif. Langkah kedua membuat satu objek boleh diprediksi oleh beberapa kotak sekaligus, tanpa memaksa jaringan memilih satu-satunya kotak terbaik.

Fungsi loss adalah jumlah terbobot dua komponen, dinormalisasi dengan jumlah pasangan positif N: loss lokalisasi *Smooth L1* (selisih offset, kuadratik di dekat nol dan linier di luarnya) dan loss keyakinan *softmax* lintas kelas. Target offset dinyatakan relatif terhadap *default box*: pergeseran pusat dibagi ukuran kotak acuan, sedangkan perubahan lebar-tinggi dihitung dalam skala logaritmik.

### Hard Negative Mining dan Augmentasi Data

Dari 8.732 *default box*, hanya sebagian kecil yang positif; sisanya latar belakang. Bila semua negatif dipakai, gradien pelatihan didominasi contoh mudah. SSD menerapkan *hard negative mining* (penambangan negatif sulit): contoh negatif diurutkan menurut loss keyakinannya dan hanya yang paling sulit yang dipakai, dengan rasio negatif:positif maksimal 3:1. Pelatihan juga memakai augmentasi agresif: pemotongan acak dengan overlap minimal tertentu terhadap objek (0,1 sampai 0,9), pembalikan horizontal dengan peluang 0,5, dan distorsi fotometrik. Dalam ablasi penulis, strategi augmentasi ini menyumbang kenaikan 8,8 poin mAP.

### Inferensi

Saat inferensi, citra dilewatkan satu kali melalui jaringan. Kotak dengan skor di bawah 0,01 dibuang, lalu *Non-Maximum Suppression* (NMS — pembuangan kotak berlebih yang saling tumpang tindih untuk objek yang sama) diterapkan per kelas dengan ambang overlap 0,45, menyisakan maksimal 200 deteksi per citra. Tahap NMS hanya memakan 1,7 milidetik; sekitar 80% waktu komputasi justru berada di *backbone* VGG16.

## Eksperimen dan Hasil

Evaluasi dilakukan pada PASCAL VOC 2007/2012, MS COCO, dan ILSVRC, dengan metrik mAP (*mean Average Precision* — rata-rata presisi lintas kelas dan ambang; maksimal 100%). Hasil utama pada VOC 2007 *test*:

- YOLO: 63,4% mAP pada 45 FPS.
- Faster R-CNN (sisi masukan ±600 piksel): 73,2% mAP pada 7 FPS.
- SSD300: 74,3% mAP pada 59 FPS — melampaui Faster R-CNN 1,1 poin dengan kecepatan 8,4 kali lipat; menurut penulis, ini metode *real-time* pertama yang menembus 70% mAP.
- SSD512: 76,8% mAP, unggul 3,6 poin atas Faster R-CNN, dengan kecepatan sekitar tiga kali lebih cepat.

Kenaikan resolusi dari 300 ke 512 piksel menambah 2,5 poin mAP, terutama karena objek kecil lebih terwakili. Pada VOC 2012, SSD512 mencapai 74,9% mAP (80,0% bila dilatih awal dengan COCO). Pada COCO *test-dev* 2015, SSD512 mencapai 26,8% mAP pada metrik ketat [0,5:0,95] dan 46,5% pada IoU 0,5 — melampaui Faster R-CNN pada keduanya, dengan selisih terbesar pada ambang ketat 0,75 (+5,3 poin), yang menandakan lokalisasi SSD lebih tepat. Namun perbaikan untuk objek kecil jauh lebih kecil (+1,3 poin AP) dibanding objek besar (+4,8 poin AP), konsisten dengan analisis sensitivitas penulis bahwa kinerja SSD menurun tajam pada objek kecil.

Ablasi mengonfirmasi dua penyebab utama keunggulan. Pertama, prediksi multi-lapisan: memangkas jumlah peta fitur prediksi dari enam menjadi satu menurunkan mAP secara monoton dari 74,3% menjadi 62,4% — sampai di bawah akurasi YOLO. Kedua, keragaman bentuk *default box*: menghapus rasio 3 dan 1/3 menurunkan 0,6 poin mAP, dan menghapus rasio 2 dan 1/2 menurunkan 2,1 poin lagi. Analisis galat menunjukkan *recall* SSD sekitar 85–90% dan galat lokalisasi yang lebih rendah dari R-CNN, tetapi kebingungan antar-kelas serupa (terutama antar-hewan) lebih tinggi.

Trik augmentasi lanjutan ("zoom out": citra ditempatkan pada kanvas lebih besar sebelum pemotongan acak) menambah 2–3 poin mAP — SSD300 menjadi 77,2% dan SSD512 79,8% pada VOC 2007.

## Kelebihan dan Keterbatasan

Kelebihan: (1) akurasi setara atau melampaui detektor dua tahap dengan kecepatan *real-time*; (2) arsitektur tunggal yang dilatih *end-to-end* tanpa komponen eksternal; (3) prediksi multi-skala menangani keragaman ukuran objek tanpa memproses citra pada beberapa ukuran; (4) terbukti generik pada tiga dataset dan dapat dipindah ke *backbone* lain.

Keterbatasan: (1) objek kecil tetap lemah, karena peta fitur dangkal yang menanganinya miskin informasi semantik — penulis sendiri menunjukkan penurunan kinerja tajam pada objek kecil; (2) desain *default box* (skala, rasio, jumlah) merupakan hiperparameter yang disetel manual per dataset — pada COCO penulis memakai kotak lebih kecil daripada pada VOC; (3) dari sisi rekayasa, *backbone* VGG16 menyita 80% waktu inferensi, sehingga kecepatan sangat bergantung pada pilihan *backbone*; (4) secara konseptual, penetapan target statis dengan ambang overlap 0,5 tidak membedakan kualitas pasangan — kotak dengan overlap 0,51 diperlakukan sama dengan kotak dengan overlap 0,9.

## Kaitan dengan Bab Lain

Bab ini adalah jawaban langsung atas kelemahan YOLOv1 ([bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)): YOLO memakai satu peta fitur kasar dan dua kotak per sel, sedangkan SSD menggantinya dengan enam peta fitur berjenjang dan ribuan *default box*, sehingga akurasi *real-time* naik dari 63,4% menjadi 74,3% mAP. Dari garis dua tahap, SSD mewarisi konsep *anchor box* dari Faster R-CNN ([bab 014](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)) — bedanya, kotak acuan di SSD langsung diberi skor kelas tanpa tahap kedua. Gagasan ini memengaruhi garis YOLO: YOLOv2 ([bab 002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)) mengadopsi *anchor box* dan prediksi konvolusional, dan YOLOv3 ([bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)) mengadopsi prediksi multi-skala. Kelemahan SSD dalam ketidakseimbangan contoh latihan menjadi sasaran RetinaNet ([bab 016](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md)), yang menggantikan *hard negative mining* dengan *focal loss*. Pola "*backbone* + prediktor multi-skala" yang diletakkan di sini menjadi cikal bakal modul *neck* pada detektor modern, termasuk varian RGB-D dalam tinjauan ini.

## Poin untuk Sitasi

Kutip dengan kunci `liu2016ssd`. Ringkasan yang aman dikutip: "SSD melakukan deteksi satu tahap dengan memprediksi skor kelas dan *offset* untuk himpunan *default box* beragam skala dan rasio aspek pada beberapa peta fitur beresolusi berbeda; pada PASCAL VOC 2007, model SSD300 mencapai 74,3% mAP dengan kecepatan 59 FPS — melampaui akurasi Faster R-CNN sambil tetap *real-time*." Catatan verifikasi: kolom abstrak halaman arXiv memuat angka versi awal (72,1% mAP, 58 FPS, 75,1%), sedangkan badan naskah ECCV (arXiv v5) memakai 74,3%, 59 FPS, 76,9% — Tabel 1 naskah mencetak 76,8% untuk SSD512, jadi selisih 0,1 poin ini perlu dikonfirmasi ke naskah sebelum sitasi formal. Ukuran tiap peta fitur (38² sampai 1²) tidak dicetak eksplisit pada teks naskah, tetapi konsisten dengan total 8.732 *default box* yang dinyatakan naskah.
