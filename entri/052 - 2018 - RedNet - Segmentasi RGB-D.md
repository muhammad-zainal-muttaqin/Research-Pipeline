# 052 - RedNet: Residual Encoder-Decoder Network for Indoor RGB-D Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jiang2018rednet` |
| Judul asli | RedNet: Residual Encoder-Decoder Network for Indoor RGB-D Semantic Segmentation |
| Penulis | Jindong Jiang, Lunan Zheng, Fei Luo, Zhijun Zhang (South China University of Technology) |
| Tahun | 2018 |
| Venue | arXiv preprint arXiv:1806.01054 (v2, Agustus 2018) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1806.01054
- **DOI (arXiv):** https://doi.org/10.48550/arXiv.1806.01054
- **Google Scholar:** https://scholar.google.com/scholar?q=RedNet%3A%20Residual%20Encoder-Decoder%20Network%20for%20Indoor%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=RedNet%3A%20Residual%20Encoder-Decoder%20Network%20for%20Indoor%20RGB-D%20Semantic%20Segmentation&sort=relevance
- **Kode sumber resmi (PyTorch):** https://github.com/JindongJiang/RedNet

## Gambaran Umum

RedNet (*Residual Encoder-Decoder Network*) adalah arsitektur jaringan saraf konvolusi untuk segmentasi semantik citra RGB-D dalam ruangan. Segmentasi semantik adalah tugas memberi label kelas pada setiap piksel; citra RGB-D adalah pasangan citra warna tiga kanal (merah, hijau, biru) dan peta kedalaman satu kanal berisi jarak tiap piksel ke kamera. Dua masalah ditangani: jaringan segmentasi yang dalam sulit dilatih karena gradien menghilang, dan informasi kedalaman belum dimanfaatkan efektif.

Jawabannya tiga rancangan: blok residual menjadi satuan dasar pada jalur *encoder* maupun *decoder*; fitur cabang kedalaman dijumlahkan ke cabang RGB pada lima lapis encoder; dan pelatihan diawasi pada lima keluaran beresolusi berbeda (*pyramid supervision*). Hasilnya, RedNet dengan encoder ResNet-50 mencapai 47,8% mIoU pada tolok ukur SUN RGB-D — dilaporkan penulis sebagai nilai tertinggi saat rilis — dengan encoder lebih dangkal dari pesaingnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Segmentasi dalam ruangan sulit karena objek ruangan sering mirip warna dan bentuknya, sedangkan pencahayaan tidak seragam. Sensor kedalaman menyediakan informasi geometri yang tidak dimiliki citra warna, sehingga metode segmentasi ruangan umumnya memakai masukan RGB-D.

Arsitektur saat itu terbagi dua keluarga, keduanya turunan FCN (*fully convolutional network*, jaringan yang seluruh lapisnya konvolusi sehingga mengeluarkan peta prediksi). Keluarga *encoder-decoder* mengecilkan resolusi untuk menangkap makna lalu memulihkannya; kelemahannya, detail spasial hilang saat pengecilan dan harus dipulihkan koneksi pintas antarjalur. Keluarga konvolusi terdilatasi (*dilated convolution*, konvolusi dengan jeda antartitik sampel yang memperbesar wilayah pandang tanpa mengecilkan resolusi) mempertahankan detail, tetapi peta aktivasinya tetap besar di sepanjang jaringan: boros memori dan sulit diperdalam.

Tiga karya menjadi pijakan. ResNet (He dkk., 2016) mengatasi degradasi — akurasi jenuh lalu menurun saat jaringan diperdalam — melalui blok residual yang menjumlahkan masukan dengan hasil transformasi sisa, sehingga gradien selalu punya jalur pendek. FuseNet (bab 051) menunjukkan kedalaman efektif diproses pada cabang tersendiri yang fiturnya dijumlahkan ke cabang RGB. LinkNet (2017) menyusun encoder-decoder berbasis ResNet secara ringkas. RedNet menggabungkan ketiganya dan menambah supervisi bertingkat.

## Ide Utama

Gagasan inti RedNet: encoder-decoder yang dalam untuk RGB-D dapat dilatih baik bila setiap satuan perhitungannya residual dan pelatihannya diawasi tidak hanya pada keluaran akhir. Masukan citra RGB dan kedalaman 480×640 piksel diproses dua cabang encoder identik; pada lima titik, fitur kedalaman dijumlahkan ke fitur RGB; decoder berjenjang memulihkan resolusi sambil menerima fitur encoder lewat koneksi pintas; keluaran akhir peta skor 480×640 untuk 37 kelas. Perubahan kunci ada dua: setiap lapis dibangun dari blok residual, bukan konvolusi polos; dan selama pelatihan decoder mengeluarkan empat prediksi perantara yang ikut dihitung galatnya (*pyramid supervision*).

## Cara Kerja Langkah demi Langkah

Alur data dari masukan sampai keluaran diringkas pada diagram berikut.

```
 RGB 480x640                    Depth 480x640 (1 kanal)
     │                                │
     ▼                                ▼
 Conv1 7x7 s2 + maxpool 3x3 s2    Conv1_d 7x7 s2 + maxpool 3x3 s2
     │                                │
     ▼                                ▼
 ┌─ ENCODER (ResNet-34/50) ─────────┐
 │  Conv1+pool 120x160 (1) <--+     │   (1)-(5): fusi kedalaman,
 │  Layer1     120x160 (2) <--+     │   penjumlahan per elemen
 │  Layer2      60x80  (3) <--+     │   dari cabang Depth ke
 │  Layer3      30x40  (4) <--+     │   cabang RGB
 │  Layer4      15x20  (5) <--+     │   (Depth berhenti di Layer4_d)
 └──────────────────────────────────┘
     │
     │  skip connection ke decoder
     │  (lewat Agent 1x1 bila ResNet-50)
     ▼
 Trans1   30x40 -> Out1 ---┐
 Trans2   60x80 -> Out2 ---┤  pyramid supervision:
 Trans3  120x160 -> Out3 --┤  tiap Out = conv 1x1, lalu
 Trans4  240x320 -> Out4 --┤  cross-entropy thd label yang
     │                     │  diperkecil; total loss =
     ▼                     │  jumlah kelima loss
 Final Conv (transpose 2x2 s2)
     ▼
 Output 480x640 (37 kelas)
```

Bagian atas menunjukkan encoder dua cabang dengan lima titik fusi; bagian bawah decoder empat lapis Trans yang masing-masing menaikkan resolusi dua kali dan mengeluarkan satu prediksi samping.

### Encoder Dua Cabang

Kedua cabang encoder identik; cabang kedalaman hanya berbeda pada konvolusi pertamanya (Conv1_d) yang berkanal masukan satu. Struktur tiap cabang diambil dari ResNet (ResNet-34 atau ResNet-50) dengan dua lapis terakhir dibuang: *global average pooling* (perata-rataan peta fitur menjadi satu vektor) dan lapis terhubung penuh.

Aliran dimulai dengan dua penurunan resolusi: konvolusi 7×7 ber-*stride* (langkah geser) 2, lalu *max-pooling* 3×3 stride 2 (pengambilan nilai maksimum tiap jendela 3×3). Pooling ini satu-satunya di seluruh jaringan; perubahan resolusi lain memakai konvolusi dan konvolusi transpos ber-stride 2. Selanjutnya empat lapis residual, Layer1 sampai Layer4. Hanya Layer1 yang tidak mengecilkan peta; tiga lainnya diawali unit residual yang mengecilkan peta setengah dan menggandakan kanal. Contoh numerik: 480×640 menjadi 120×160 setelah Conv1 dan pooling, 60×80 setelah Layer2, 30×40 setelah Layer3, dan 15×20 setelah Layer4, yaitu 1/32 resolusi masukan.

### Fusi Fitur Kedalaman

Pada lima lapis encoder, keluaran cabang kedalaman dijumlahkan per elemen ke cabang RGB: tiap nilai pada peta fitur kedalaman ditambahkan ke nilai pada posisi dan kanal yang sama di peta fitur RGB. Operasi ini tidak menambah parameter. Cabang kedalaman berhenti di Layer4_d; setelah itu hanya representasi gabungan yang diteruskan ke decoder. Teknik ini sama dengan fusi FuseNet (bab 051) dan hanya terjadi pada jalur penurunan resolusi.

### Decoder Residual dan Koneksi Pintas

Decoder dimulai dari keluaran Layer4 (15×20), tersusun atas empat lapis residual Trans1–Trans4 dan satu Final Conv. Berbeda dengan encoder ResNet-50 yang memakai blok *bottleneck* (tiga konvolusi: 1×1 peramping, 3×3, 1×1 pengembang), decoder memakai blok residual standar berupa dua konvolusi 3×3. Setiap lapis Trans diakhiri satu unit upsample: konvolusi transpos 2×2 stride 2 yang menggandakan tinggi-lebar peta dan membagi dua kanal. Konvolusi transpos adalah kebalikan konvolusi ber-stride: satu nilai disebar ke beberapa nilai keluaran sehingga peta membesar.

Koneksi pintas (*skip connection*) menjembatani keluaran lapis encoder ke lapis decoder yang resolusinya sepadan. Pada varian ResNet-50, fitur encoder dilewatkan dahulu melalui lapis *Agent* — konvolusi 1×1 stride 1 peramping kanal — karena ekspansi kanal blok bottleneck membuat fitur encoder sangat besar. Pada varian ResNet-34 lapis Agent dihilangkan (bloknya tidak mengekspansi kanal), dan koneksi pintas Conv1–Trans4 juga dihilangkan karena empiris lebih baik. Setiap konvolusi di seluruh jaringan diikuti *batch normalization* (penormalan statistik tiap kanal) dan aktivasi ReLU.

### Pyramid Supervision

Galat yang hanya dihitung pada keluaran akhir membuat gradien menempuh seluruh decoder dan dapat menghilang sebelum mencapai lapisan awal. *Pyramid supervision* mengatasinya dengan empat peta prediksi samping (*side output*) dari empat lapis Trans, di samping keluaran akhir. Tiap peta samping dihitung dengan satu konvolusi 1×1 stride 1, sehingga resolusinya mengikuti lapisnya: Out1 berukuran 30×40 (1/16 resolusi penuh), Out2 60×80, Out3 120×160, dan Out4 240×320.

Kelima keluaran masuk fungsi *softmax* (pengubah skor menjadi distribusi probabilitas) lalu dihitung galat *cross-entropy*-nya (negatif logaritma probabilitas kelas benar, dirata-ratakan atas piksel). Untuk keluaran samping, label kebenaran (*ground truth*) diperkecil dengan interpolasi *nearest-neighbor* agar label tetap diskrit. Galat total adalah jumlah kelima galat. Karena peta kecil berisi lebih sedikit piksel tetapi galatnya dijumlahkan utuh, piksel keluaran beresolusi rendah secara implisit terbobot lebih besar; penulis melaporkannya lebih baik daripada pembobotan merata. Keluaran samping hanya berperan saat pelatihan; prediksi akhir diambil dari keluaran resolusi penuh.

### Pelatihan

Masukan diubah ukurannya menjadi 480×640; label supervisi samping diperkecil sampai 30×40. Augmentasi: penskalaan dan pemotongan acak serta penyesuaian hue, brightness, dan saturation acak khusus RGB. Encoder memakai bobot pralatih ImageNet; lapis lain diinisialisasi Xavier (varians bobot awal disesuaikan jumlah koneksi). Karena jumlah piksel antarkelas timpang, galat tiap piksel ditimbang *median frequency balancing* (bobot kelas adalah median frekuensi semua kelas dibagi frekuensi kelasnya), sehingga kelas langka terbobot lebih besar. Optimisasi memakai penurunan gradien stokastik bermomentum 0,9, laju pembelajaran 0,002 yang dikali 0,8 tiap 100 epoch, *weight decay* 0,0004, dan batch 5 pada satu GPU GTX 1080.

## Eksperimen dan Hasil

Evaluasi dilakukan pada SUN RGB-D, tolok ukur ruangan dalam terbesar saat itu: 10.335 citra RGB-D beranotasi padat dari 20 jenis ruangan (mencakup seluruh NYUv2 dan sebagian B3DO–SUN3D), dengan kedalaman yang diperbaiki rekonstruksi 3D multi-bingkai. Setiap piksel berlabel satu dari 37 kelas atau *unknown*. Pembagian baku dipakai: 5.285 citra latih/validasi dan 5.050 citra uji. Metriknya tiga: akurasi piksel (persentase piksel benar), akurasi rata-rata (rerata akurasi per kelas), dan IoU (*Intersection over Union*, rasio irisan terhadap gabungan wilayah prediksi dan kebenaran); mIoU, rerata IoU seluruh kelas, adalah yang paling ketat.

Hasil utama: RedNet (ResNet-50) mencapai 47,8% mIoU pada data uji, dilaporkan penulis sebagai nilai tertinggi saat rilis. Dua perbandingan memberi konteks. Pertama, FuseNet-SF5 dan DFCN-DCRF pada tabel pembanding memakai teknik fusi yang sama, sehingga keunggulan RedNet atas keduanya menunjukkan sumbangan arsitektur residual dan supervisinya. Kedua, RefineNet-152 dan CFN memakai ekstraktor fitur ResNet-152 — tiga kali lebih dalam — sehingga 47,8% mIoU dicapai dengan backbone jauh lebih ringan. Perbandingan internal kedua varian, yang berbagi decoder identik, menunjukkan encoder lebih dalam memberi akurasi lebih tinggi.

Uji ablasi membandingkan pelatihan dengan dan tanpa pyramid supervision; hasilnya ketiga metrik meningkat pada kedua varian encoder. Temuan paling tegas: RedNet (ResNet-34) dengan pyramid supervision mengalahkan RedNet (ResNet-50) tanpanya — skema ini menyumbang peningkatan lebih besar daripada pendalaman encoder dari 34 ke 50 lapis.

## Kelebihan dan Keterbatasan

Kelebihan RedNet: desain residual menyeluruh membuat jaringan sedalam ResNet-50 stabil dilatih untuk segmentasi; fusi penjumlahan tidak menambah parameter; pyramid supervision meningkatkan akurasi tanpa mengubah arsitektur inferensi; dan akurasi tertinggi dicapai dengan backbone lebih dangkal dari pesaing.

Keterbatasannya: pertama, kecepatan inferensi dan jumlah parameter tidak dilaporkan; dari sisi rekayasa, decoder yang mempertahankan blok residual hingga resolusi penuh berpotensi boros memori (pelatihannya saja memakai batch sekecil 5). Kedua, secara konseptual, penjumlahan per elemen memberi bobot sama pada kedua modalitas di semua kondisi; tidak ada mekanisme meredam fitur kedalaman berisik. Ketiga, evaluasi hanya pada satu dataset; generalisasi ke sensor atau lingkungan lain tidak teruji. Keempat, 47,8% mIoU berarti irisan prediksi dengan kebenaran belum mencapai separuh luas gabungannya — segmentasi ruangan masih jauh dari tuntas.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis fusi RGB-D yang dibuka [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md): penjumlahan fitur kedalaman diwarisi langsung, tetapi dipindahkan ke kerangka residual lebih dalam dan ditambah supervisi bertingkat. Pemakaian ResNet menghubungkan bab ini dengan klaster Fondasi RGB.

Garis berikutnya mengoreksi dua titik lemah RedNet. [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md) memperluas fusi ke banyak tingkat dengan modul penyempurnaan fitur. [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) mengganti penjumlahan kaku dengan mekanisme komplementer berbasis perhatian (*attention*) yang menimbang modalitas secara adaptif. [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md) menunjukkan fusi RGB-D dapat dibuat jauh lebih ringan untuk waktu nyata.

## Poin untuk Sitasi

Kutip dengan kunci `jiang2018rednet`. Ringkasan yang aman dikutip: "RedNet adalah arsitektur encoder-decoder residual untuk segmentasi semantik RGB-D dalam ruangan. Fitur kedalaman difusikan ke cabang RGB melalui penjumlahan per elemen pada lima lapis encoder, dan pelatihannya memakai pyramid supervision atas lima keluaran beresolusi berbeda. Dengan encoder ResNet-50, RedNet mencapai 47,8% mIoU pada tolok ukur SUN RGB-D dan dilaporkan sebagai yang tertinggi saat rilis."

Catatan verifikasi sebelum sitasi formal: (a) angka rinci per metode pada Tabel 2 (pembanding) dan Tabel 3 (ablasi) tidak terekstrak dari sumber HTML dan wajib dicocokkan dengan PDF naskah; (b) klaim "nilai tertinggi saat rilis" berasal dari penulis dan sebaiknya diverifikasi terhadap tabel pembanding naskah serta karya sezaman; (c) makalah ini preprint arXiv tanpa venue konferensi atau jurnal yang tercatat, sehingga kesesuaiannya dengan kebutuhan sitasi perlu diperiksa.
