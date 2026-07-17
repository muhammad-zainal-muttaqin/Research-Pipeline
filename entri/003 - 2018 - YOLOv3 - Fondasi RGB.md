# 003 - YOLOv3: An Incremental Improvement

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `redmon2018yolov3` |
| Judul asli | YOLOv3: An Incremental Improvement |
| Penulis | Joseph Redmon, Ali Farhadi |
| Tahun | 2018 |
| Venue | arXiv preprint arXiv:1804.02767 (laporan teknis) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1804.02767
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLOv3%3A%20An%20Incremental%20Improvement
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLOv3%3A%20An%20Incremental%20Improvement&sort=relevance

## Gambaran Umum

YOLOv3 adalah pemutakhiran inkremental atas YOLOv2 (bab 002): tidak ada perubahan paradigma, melainkan tiga perbaikan terarah. Pertama, backbone Darknet-19 diganti Darknet-53 — jaringan 53 lapis dengan koneksi residual yang memperkuat ekstraksi fitur tanpa memperlambat berarti. Kedua, prediksi dilakukan pada tiga skala peta fitur sekaligus (bukan satu skala seperti sebelumnya), yang secara langsung menyerang kelemahan terbesar YOLOv2: deteksi objek kecil. Ketiga, klasifikasi memakai pengklasifikasi logistik independen per kelas alih-alih *softmax*, sehingga label yang saling tumpang tindih dapat ditangani.

Hasilnya adalah keseimbangan kecepatan-akurasi yang matang: YOLOv3-608 mencapai 33,0% AP pada COCO dengan 51 milidetik per citra — sekitar 3,8 kali lebih cepat dari RetinaNet pada akurasi yang masih kompetitif, dan unggul pada metrik longgar (AP50 57,9%). Kombinasi kecepatan, kemudahan modifikasi, dan dokumentasi yang terbuka menjadikan YOLOv3 baseline paling banyak dipakai dalam tinjauan ini, termasuk pada klaster aplikasi pertanian dan integrasi RGB-D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Dua masalah tersisa dari YOLOv2. Masalah pertama adalah objek kecil. YOLOv2 memang menambahkan *passthrough layer*, tetapi prediksi tetap dilakukan pada satu peta fitur 13×13: pada peta serinci itu, objek yang hanya berukuran beberapa piksel pada citra asal sudah terlalu tereduksi untuk dikenali. Detektor pesaing seperti RetinaNet (bab 016) dan SSD (bab 015) mengatasi masalah ini dengan memprediksi pada beberapa skala fitur sekaligus — fitur dangkal yang rinci untuk objek kecil, fitur dalam yang kaya makna untuk objek besar.

Masalah kedua adalah kapasitas fitur. Darknet-19 relatif dangkal; menambah kedalaman jaringan biasa justru menurunkan kinerja karena degradasi gradien — masalah yang di komunitas visi dipecahkan oleh koneksi residual pada ResNet (bab 147). Selain itu, mekanisme WordTree dari YOLO9000 terbukti rumit dan tidak dilanjutkan; sebagai gantinya diperlukan cara sederhana untuk menangani label yang saling tumpang tindih (mis. sebuah kotak bisa sah berlabel "perempuan" dan "orang" sekaligus), yang tidak dapat dilakukan *softmax* karena *softmax* memaksa satu kelas pemenang.

## Ide Utama

Gagasan YOLOv3 dapat diringkas menjadi: pertahankan mesin prediksi YOLOv2 yang sudah stabil, lalu perkuat dua komponen penentunya — fitur dan skala. Fitur diperkuat dengan backbone residual yang dalam; skala diperbanyak dengan menempelkan kepala prediksi pada tiga tingkat kedalaman jaringan, mengikuti pola piramida fitur (FPN, bab 018). Setiap skala diberi tanggung jawab terhadap ukuran objek yang berbeda melalui pembagian *anchor*, sehingga objek kecil dideteksi pada peta rinci dan objek besar pada peta kasar. Untuk klasifikasi, satu *softmax* diganti banyak pengklasifikasi biner independen — perubahan kecil yang menghapus asumsi bahwa kelas-kelas saling eksklusif.

## Cara Kerja Langkah demi Langkah

### Darknet-53

Backbone baru ini memiliki 53 lapis konvolusi, tersusun dari pasangan konvolusi 1×1 dan 3×3 yang diulang, dengan **koneksi residual**: keluaran suatu blok ditambahkan dengan masukannya sendiri sebelum diteruskan. Penjumlahan pintas ini memberi gradien jalur langsung saat pelatihan, sehingga jaringan yang dalam tetap dapat dilatih tanpa degradasi. Tidak ada *pooling*; pengecilan resolusi dilakukan konvolusi berlangkah (*stride*) 2. Menurut naskah, Darknet-53 mencapai akurasi klasifikasi ImageNet setara ResNet-101 dengan kecepatan 1,5 kali lipat, dan setara ResNet-152 dengan kecepatan 2 kali lipat.

### Prediksi Tiga Skala

Keluaran Darknet-53 pada citra masukan 416×416 menghasilkan peta fitur 13×13 (dibagi 32). YOLOv3 memasang kepala prediksi pada peta ini, kemudian mengambil fitur dua tingkat lebih awal: peta 13×13 di-*upsample* dua kali menjadi 26×26 dan digabung (*concatenate*) dengan fitur dari lapis tengah; kepala kedua memprediksi pada 26×26 (dibagi 16). Proses yang sama diulang sekali lagi untuk menghasilkan kepala ketiga pada 52×52 (dibagi 8). Dengan demikian objek besar dideteksi pada peta 13×13, objek sedang pada 26×26, dan objek kecil pada peta 52×52 yang rinci.

```
citra 416x416
     │
     ▼
Darknet-53 (residual)                 kepala prediksi (per skala:
     │                                3 anchor × (4 box + 1 objek + C kelas))
     ├── 13x13  ──────────────────►  objek besar   (anchor terbesar)
     │      │
     │      └─ upsample ×2, gabung fitur lapis tengah
     ├── 26x26  ──────────────────►  objek sedang
     │      │
     │      └─ upsample ×2, gabung fitur lapis awal
     └── 52x52  ──────────────────►  objek kecil   (anchor terkecil)
```

Setiap skala memakai 3 *anchor box*, sehingga totalnya 9 anchor yang ditentukan dengan *k-means clustering* pada dataset COCO (mewarisi teknik dimension clusters dari bab 002). Anchor terbesar ditempatkan pada skala terkasar, anchor terkecil pada skala terinci. Rumus prediksi kotak identik dengan YOLOv2: offset pusat diikat pada sel melalui fungsi logistik, ukuran diprediksi sebagai faktor skala terhadap anchor.

### Skor Objek dan Klasifikasi Multi-Label

Setiap kotak prediksi memperoleh skor *objectness* melalui regresi logistik: nilai 1 untuk anchor yang tumpang tindih paling baik dengan objek kebenaran, 0 untuk lainnya. Untuk kelas, YOLOv3 mengganti *softmax* dengan **pengklasifikasi logistik independen per kelas** yang dilatih dengan *binary cross-entropy*. Artinya setiap kelas dinilai sendiri-sendiri "ya/tidak", sehingga satu kotak dapat memperoleh beberapa label sekaligus tanpa dipaksa memilih satu pemenang. Perubahan ini sekaligus menutup mekanisme WordTree yang rumit dari generasi sebelumnya.

## Eksperimen dan Hasil

Evaluasi dilakukan pada COCO dengan metrik AP rata-rata pada ambang IOU 0,5:0,95 (metrik ketat), AP50 (ambang longgar), serta AP per ukuran objek (kecil/sedang/besar). Hasil utama:

- YOLOv3-608: 33,0% AP, 57,9% AP50, pada 51 ms per citra (Titan X).
- YOLOv3-320: 28,2% AP pada 22 ms — setara akurasi SSD-321 tetapi tiga kali lebih cepat.
- Pembanding: RetinaNet-101-800 mencapai 37,8% AP dan 61,1% AP50 pada 198 ms.

Interpretasinya dua sisi. Pada ambang longgar (AP50) YOLOv3 nyaris menyamai RetinaNet dengan kecepatan hampir 4 kali lipat — untuk banyak aplikasi praktis, ini titik yang lebih berguna. Namun pada ambang ketat YOLOv3 tertinggal, yang menunjukkan lokalisasinya masih kurang halus: kotaknya benar, tetapi tidak tepat-tepat. Pada sisi positif, AP untuk objek kecil naik jelas dibanding YOLOv2 berkat prediksi tiga skala — persis masalah yang hendak dipecahkan.

## Kelebihan dan Keterbatasan

Kelebihan: (1) keseimbangan kecepatan-akurasi terbaik pada masanya untuk kelas detektor *real-time*; (2) deteksi objek kecil membaik signifikan lewat prediksi tiga skala; (3) backbone residual menjadi fondasi yang kuat untuk modifikasi lanjutan; (4) desainnya sederhana, terdokumentasi terbuka, dan mudah dipotong-tempel — alasan utamanya menjadi baseline de-facto pada banyak bab aplikasi dalam tinjauan ini.

Keterbatasan: (1) AP pada ambang IOU ketat kalah dari detektor yang berorientasi akurasi seperti RetinaNet; (2) masih bergantung pada *anchor* yang harus disetel per dataset (baru dihapus pada bab 005); (3) objek yang sangat kecil atau berhimpitan rapat tetap sulit; (4) dari sisi ilmiah, makalah ini berupa laporan teknis tanpa ablation formal yang mendalam — klaim kontribusi tiap komponen tidak sekuat makalah konferensi penuh.

## Kaitan dengan Bab Lain

Bab ini melanjutkan langsung bab 002: mesin prediksi (anchor, offset terikat sel, *objectness* logistik) diwarisi, sedangkan WordTree ditinggalkan. Dua komponen barunya adalah adopsi dari luar keluarga YOLO: koneksi residual dari ResNet (bab 147) dan piramida fitur multi-skala dari FPN (bab 018), keduanya menjawab kelemahan objek kecil yang tersisa sejak bab 001. Resep YOLOv3 inilah yang disempurnakan secara masif oleh bab 004 (YOLOv4), dan head-nya yang berbasis *anchor* menjadi titik berangkat pembaruan bab 005 (YOLOX). Pada klaster aplikasi — terutama pertanian (bab 120–127) — YOLOv3 adalah backbone yang paling sering dimodifikasi.

## Poin untuk Sitasi

Kutip dengan kunci `redmon2018yolov3`; perhatikan bahwa terbitannya berupa laporan teknis arXiv, bukan prosiding konferensi. Ringkasan yang aman dikutip: "YOLOv3 memadukan backbone residual Darknet-53 dengan prediksi tiga skala bergaya piramida fitur dan klasifikasi logistik multi-label, mencapai 33,0% AP (57,9% AP50) pada COCO dengan 51 ms per citra." Angka hasil di atas dari tabel naskah; perbandingan kecepatan antarperangkat keras sebaiknya dikutip bersama keterangan GPU yang dipakai naskah.
