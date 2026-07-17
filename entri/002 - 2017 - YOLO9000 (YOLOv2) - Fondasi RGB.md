# 002 - YOLO9000: Better, Faster, Stronger

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `redmon2017yolo9000` |
| Judul asli | YOLO9000: Better, Faster, Stronger |
| Penulis | Joseph Redmon, Ali Farhadi |
| Tahun | 2017 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2017) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1612.08242
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLO9000%3A%20Better%2C%20Faster%2C%20Stronger
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLO9000%3A%20Better%2C%20Faster%2C%20Stronger&sort=relevance

## Gambaran Umum

Makalah ini memperbaiki YOLOv1 (bab 001) pada tiga poros yang menjadi judulnya. *Better*: serangkaian perbaikan arsitektur dan pelatihan — *batch normalization*, pengklasifikasi resolusi tinggi, *anchor box* yang ditentukan dari data, dan pelatihan multi-skala — menaikkan akurasi dari 63,4% menjadi 78,6% mAP pada PASCAL VOC 2007 sambil mempertahankan kecepatan *real-time*. *Faster*: backbone baru Darknet-19 yang jauh lebih ringan dari pendahulunya. *Stronger*: mekanisme pelatihan gabungan bernama WordTree yang memungkinkan model mendeteksi lebih dari 9.000 kategori objek, jauh melampaui 20–80 kelas yang umum saat itu.

Kontribusi yang paling tahan lama dari makalah ini adalah *anchor box* dan pelatihan multi-skala; keduanya menjadi komponen baku pada hampir semua YOLO generasi berikutnya hingga era *anchor-free* (bab 005).

## Latar Belakang: Masalah yang Ingin Dipecahkan

YOLOv1 membuktikan deteksi *real-time* itu mungkin, tetapi membayar dua harga. Pertama, *recall*-nya rendah: karena setiap sel grid hanya memprediksi satu kelas dan dua kotak, banyak objek — terutama objek kecil berkelompok — terlewat. Kedua, lokalisasinya kurang presisi; galat lokalisasi adalah sumber kesalahan dominannya. Akibatnya mAP YOLOv1 (63,4%) tertinggal sekitar 10 poin dari detektor dua tahap seperti Faster R-CNN (73,2%).

Ada pula masalah kedua yang lebih mendasar: jumlah kategori yang dapat dideteksi. Dataset deteksi mahal dibuat karena setiap objek harus dilabeli kotak; VOC hanya memiliki 20 kelas dan COCO 80 kelas. Sementara itu, dataset klasifikasi seperti ImageNet memiliki ribuan kelas karena pelabelan per citra jauh lebih murah. Tanpa mekanisme baru, kosakata deteksi objek akan selalu tertinggal jauh di belakang klasifikasi.

## Ide Utama

Untuk masalah akurasi, gagasannya bukan satu perubahan besar, melainkan akumulasi perbaikan yang masing-masing diukur kontribusinya: sebagian membuat pelatihan lebih stabil, sebagian membuat prediksi lebih fleksibel, sebagian memperkuat fitur. Prinsipnya adalah mempertahankan formulasi satu jaringan dari YOLOv1, tetapi menghilangkan hambatan-hambatan yang menekan recall dan presisi lokalisasi.

Untuk masalah kosakata, gagasannya adalah **pelatihan gabungan**: saat menerima citra dari dataset deteksi, jaringan belajar mendeteksi; saat menerima citra dari dataset klasifikasi (yang tidak punya label kotak), jaringan hanya belajar mengenali kelasnya. Hambatannya, label kedua dataset tidak konsisten — ImageNet memiliki "Norfolk terrier", COCO hanya memiliki "anjing". Solusinya adalah WordTree: label-label dari semua dataset disusun dalam satu pohon hierarki (dari umum ke khusus), dan jaringan memprediksi probabilitas di setiap tingkat pohon, bukan satu *softmax* datar. Dengan cara ini, kelas yang saling beririsan tidak lagi bertentangan.

## Cara Kerja Langkah demi Langkah

### Batch Normalization

Semua lapis konvolusi diberi *batch normalization* (normalisasi keluaran lapis terhadap statistik satu *batch* data). Teknik ini menstabilkan distribusi sinyal selama pelatihan sehingga laju pembelajaran bisa lebih besar dan konvergensi lebih cepat; sebagai bonus, ia bertindak sebagai regularisasi sehingga *dropout* dapat dibuang tanpa *overfitting*. Kontribusinya terukur +2% mAP.

### Pengklasifikasi Resolusi Tinggi

YOLOv1 melatih backbone sebagai pengklasifikasi ImageNet pada 224×224, lalu langsung menaikkan resolusi ke 448×448 untuk deteksi — jaringan harus beradaptasi pada resolusi baru dan tugas baru secara bersamaan. YOLOv2 memecah transisi ini: backbone terlebih dahulu disetel halus sebagai pengklasifikasi pada 448×448 selama 10 *epoch*, baru kemudian dipasang ke tugas deteksi. Kontribusinya +4% mAP.

### Anchor Box dan Penentuannya dari Data

Ini perubahan struktural terbesar. YOLOv1 memprediksi koordinat kotak secara bebas; YOLOv2 mengadopsi *anchor box* dari Faster R-CNN: setiap sel tidak lagi memprediksi kotak dari nol, melainkan memprediksi **koreksi** terhadap beberapa kotak acuan (anchor) berbentuk tetap. Belajar menjadi lebih mudah karena jaringan hanya menyesuaikan, bukan mengarang bentuk. Lapis *fully connected* dibuang dan prediksi dipindah ke peta fitur konvolusional.

Berbeda dari Faster R-CNN yang memilih bentuk anchor secara manual, YOLOv2 menentukannya dari data dengan **dimension clusters**: seluruh kotak kebenaran pada dataset pelatihan dikelompokkan dengan *k-means*, dengan jarak d(kotak, pusat) = 1 − IOU(kotak, pusat). Memakai IOU alih-alih jarak Euclidean penting, karena yang dicari adalah anchor yang "paling mudah disesuaikan menjadi kotak nyata", dan IOU mengukur tepat itu. Dipilih k = 5 anchor sebagai titik imbang recall-kompleksitas. Dengan anchor, recall naik dari 81% menjadi 88% dengan harga mAP yang nyaris tidak berubah.

### Prediksi Lokasi Langsung

Memakai anchor saja ternyata membuat pelatihan awal tidak stabil: prediksi posisi yang bebas dapat mengirim kotak ke mana saja di citra. Solusinya, YOLOv2 mengikat prediksi posisi pada sel asalnya: jaringan memprediksi offset yang dilewatkan fungsi logistik (σ, pembatas nilai 0–1), sehingga pusat kotak selalu jatuh di dalam (atau dekat) sel yang memprediksinya. Kombinasi dimension clusters dan prediksi lokasi langsung ini menyumbang sekitar +5% mAP.

Cara sebuah sel mengubah prediksi mentah menjadi kotak akhir:

```
sel grid (cx, cy)                rumus konversi
┌─────────────┐    pusat:  bx = σ(tx) + cx   → diikat di dalam sel
│  ●(bx,by)   │            by = σ(ty) + cy
│ ┌─────────┐ │    ukuran: bw = pw · e^(tw)  → skala thd anchor
│ │ kotak   │ │            bh = ph · e^(th)
│ │ prediksi│ │    keyakinan: σ(to) = Pr(objek) × IOU
│ └─────────┘ │
│ ░ anchor    │    jaringan hanya memprediksi tx, ty, tw, th, to;
│ ░ (pw, ph)  │    anchor (pw, ph) menyediakan bentuk awal
└─────────────┘
```

### Fitur Rinci dan Pelatihan Multi-Skala

YOLOv2 memprediksi pada peta fitur 13×13 (citra 416×416 dibagi 32). Untuk membantu deteksi objek kecil, fitur dari lapis lebih awal beresolusi 26×26 disalurkan melalui *passthrough layer*: peta 26×26×512 disusun ulang menjadi 13×13×2048 lalu digabung (*concatenate*) dengan peta utama. Kontribusinya +1% mAP.

Terakhir, karena arsitekturnya sepenuhnya konvolusional, ukuran masukan dapat diubah-ubah. Setiap 10 *batch*, pelatihan berganti resolusi secara acak dari himpunan {320, 352, …, 608} piksel. Model yang sama dengan demikian belajar bekerja pada banyak resolusi; saat dipakai, pengguna dapat memilih sendiri titik imbang kecepatan-akurasi (masukan kecil = cepat, masukan besar = akurat) tanpa melatih ulang.

### Darknet-19 (Faster)

Backbone baru, Darknet-19, terdiri atas 19 lapis konvolusi (mayoritas 3×3 dengan konvolusi 1×1 sebagai pereduksi kanal) dan 5 lapis *max-pooling*, ditutup *global average pooling*. Biayanya hanya 5,58 miliar FLOPs per citra, dibandingkan ±30,7 miliar pada VGG-16, dengan akurasi klasifikasi ImageNet top-1 72,9% — jauh lebih ringan dengan akurasi yang layak.

### WordTree (Stronger)

WordTree dibangun dari graf konsep WordNet: setiap label ditelusuri jalurnya ke akar (mis. "Norfolk terrier" → "terrier" → "anjing pemburu" → "anjing" → … → "objek fisik"). Prediksi kelas dilakukan secara hierarkis: pada setiap simpul, jaringan menghitung *softmax* hanya terhadap saudara-saudara satu induk; probabilitas sebuah kelas adalah perkalian probabilitas sepanjang jalurnya. Dengan struktur ini, dataset deteksi dan klasifikasi dapat dilatih bergantian pada satu jaringan — citra COCO memperbarui seluruh komponen deteksi, citra ImageNet hanya memperbarui bagian klasifikasi. Hasilnya, YOLO9000 mengenali 9.418 kategori.

## Eksperimen dan Hasil

Deteksi diuji pada PASCAL VOC 2007 dan COCO; mekanisme WordTree diuji pada tugas deteksi ImageNet. Hasil utama:

- YOLOv2 416×416: 76,8% mAP pada 67 FPS (VOC 2007).
- YOLOv2 544×544: 78,6% mAP pada 40 FPS — melampaui Faster R-CNN (73,2% pada 7 FPS) baik dalam akurasi maupun kecepatan.
- Fleksibilitas resolusi: pada 288×288 model tetap berjalan ±90 FPS dengan mAP ±69%, sehingga satu model melayani spektrum kecepatan-akurasi.
- YOLO9000 pada tugas deteksi ImageNet (200 kelas, hanya 44 yang memiliki label kotak saat pelatihan): 19,7% mAP keseluruhan; pada 156 kelas yang tidak pernah berlabel kotak, 16,0% mAP.

Interpretasi baris terakhir: akurasi pada kelas tanpa label kotak memang jauh di bawah kelas berlabel penuh, tetapi angka itu membuktikan pengetahuan klasifikasi benar-benar berpindah ke kemampuan deteksi — sesuatu yang tidak mungkin dilakukan pelatihan deteksi biasa.

## Kelebihan dan Keterbatasan

Kelebihan: (1) akurasi dan recall naik tajam tanpa mengorbankan kecepatan; (2) satu model fleksibel terhadap resolusi masukan; (3) Darknet-19 ringan dan menjadi fondasi Darknet-53 pada generasi berikutnya; (4) WordTree membuka pelatihan lintas-dataset berskala ribuan kelas.

Keterbatasan: (1) objek kecil membaik tetapi belum tuntas — prediksi tetap pada satu skala 13×13; (2) deteksi 9.000 kelas jauh lebih lemah daripada deteksi kelas berlabel penuh, sehingga WordTree lebih bernilai sebagai bukti konsep; (3) kualitas WordTree bergantung pada kualitas hierarki WordNet; (4) dari sisi rekayasa, banyaknya perbaikan yang ditumpuk membuat kontribusi masing-masing sulit dipisahkan di luar ablation makalah.

## Kaitan dengan Bab Lain

Bab ini adalah perbaikan langsung atas kelemahan bab 001 (recall rendah, lokalisasi kasar). Gagasan *anchor box*-nya dipinjam dari Faster R-CNN (keluarga bab 012–014), lalu disempurnakan dengan penentuan dari data. Bab 003 (YOLOv3) akan mengganti Darknet-19 dengan backbone residual dan menyerang sisa masalah objek kecil lewat prediksi multi-skala — pelatihan multi-skala di bab ini adalah pendahulunya. *Anchor* berbasis klaster yang diperkenalkan di sini menjadi standar hingga dihapus oleh bab 005 (YOLOX).

## Poin untuk Sitasi

Kutip dengan kunci `redmon2017yolo9000`. Ringkasan yang aman dikutip: "YOLOv2 meningkatkan akurasi YOLO melalui *anchor box* berbasis klaster dimensi, prediksi lokasi langsung, dan pelatihan multi-skala (76,8–78,6% mAP VOC 2007 pada 40–67 FPS); mekanisme WordTree memperluas deteksi ke 9.418 kategori melalui pelatihan gabungan deteksi-klasifikasi." Seluruh angka di atas berasal dari naskah; rincian ablation per komponen (mis. +2%, +4%, +5%) sebaiknya dikutip langsung dari tabel ablation naskah bila diperlukan.
