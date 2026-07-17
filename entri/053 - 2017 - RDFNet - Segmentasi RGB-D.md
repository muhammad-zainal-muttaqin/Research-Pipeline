# 053 - RDFNet: RGB-D Multi-Level Residual Feature Fusion for Indoor Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `park2017rdfnet` |
| Judul asli | RDFNet: RGB-D Multi-level Residual Feature Fusion for Indoor Semantic Segmentation |
| Penulis | Seong-Jin Park, Ki-Sang Hong, Seungyong Lee |
| Tahun | 2017 |
| Venue | IEEE International Conference on Computer Vision (ICCV 2017), hal. 4980–4989 |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **CVF Open Access (PDF gratis):** https://openaccess.thecvf.com/content_ICCV_2017/papers/Park_RDFNet_RGB-D_Multi-Level_ICCV_2017_paper.pdf
- **Google Scholar:** https://scholar.google.com/scholar?q=RDFNet%3A%20RGB-D%20Multi-Level%20Residual%20Feature%20Fusion%20for%20Indoor%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=RDFNet%3A%20RGB-D%20Multi-Level%20Residual%20Feature%20Fusion%20for%20Indoor%20Semantic%20Segmentation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan RDFNet, jaringan segmentasi semantik untuk citra RGB-D dalam ruangan (*indoor*). Segmentasi semantik adalah tugas melabeli setiap piksel citra dengan kelas objeknya (dinding, lantai, kursi, dan sebagainya); citra RGB-D berarti masukan terdiri atas citra warna (RGB) dan peta kedalaman (*depth map*) yang merekam jarak kamera ke permukaan pada setiap piksel. RDFNet memperluas RefineNet — arsitektur segmentasi RGB yang menggabungkan fitur multi-tingkat melalui koneksi residual — menjadi arsitektur dua jalur yang memproses warna dan kedalaman secara terpisah, lalu memfusikannya pada empat tingkat resolusi melalui blok baru bernama *Multi-modal Feature Fusion* (MMF).

Gagasan kuncinya adalah memperlakukan fusi lintas modalitas sebagai masalah residual: fitur kedalaman dipelajari sebagai pelengkap (sisa) terhadap fitur warna yang umumnya lebih diskriminatif, sehingga pelatihan *end-to-end* (dari masukan ke keluaran tanpa tahap terpisah) tetap stabil pada jaringan yang sangat dalam. Hasilnya, RDFNet mencapai *mean IoU* 50,1% pada NYUDv2 (40 kelas) dan 47,7% pada SUN RGB-D (37 kelas), keduanya merupakan akurasi terbaik yang dilaporkan saat publikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Informasi kedalaman membantu membedakan objek yang warnanya serupa tetapi geometrinya berbeda — misalnya bantal di atas tempat tidur, atau pintu yang sewarna dengan dinding. Masalahnya adalah bagaimana menggabungkan kedua modalitas ini di dalam jaringan konvolusi. Sebelum 2017, strategi yang umum terbagi tiga. *Early fusion* menggabungkan kanal warna dan kedalaman di lapisan masukan, sehingga interaksi lintas modalitas hanya terjadi pada fitur paling dangkal. *Late fusion* melatih satu jaringan per modalitas dan merata-rata peta skor keluarannya, sehingga fitur perantara kedua modalitas tidak pernah saling bertemu. Pendekatan ketiga, misalnya FuseNet (bab 051), menjumlahkan fitur kedalaman ke jalur warna hanya di bagian *encoder*; akurasinya terbatas karena fusi tidak memanfaatkan fitur multi-tingkat dan tidak ditempatkan pada jalur pemulihan resolusi.

Pada saat yang sama, untuk segmentasi RGB saja, RefineNet (Lin et al., CVPR 2017) menunjukkan bahwa fitur dari banyak tingkat resolusi dapat digabungkan secara bertahap melalui koneksi residual (skip-connection) untuk menghasilkan prediksi tajam beresolusi tinggi. Celah yang diisi RDFNet: belum ada metode RGB-D yang menerapkan prinsip fusi residual multi-tingkat itu pada dua modalitas sekaligus. Segmentasi dalam ruangan menuntut keduanya sekaligus — detail batas objek dari fitur dangkal dan pemahaman semantik dari fitur dalam — sehingga fusi satu titik di awal atau di akhir jaringan tidak memadai.

## Ide Utama

Bentuk paling sederhana dari gagasan RDFNet: pasangkan dua jaringan ResNet — satu untuk citra warna, satu untuk representasi kedalaman — kemudian, pada setiap tingkat resolusi, gabungkan kedua fitur dengan blok fusi yang dilatih secara residual, dan lanjutkan dengan rangkaian blok RefineNet yang memurnikan fitur fusi dari resolusi kasar ke halus.

Kata "residual" di sini bermakna teknis yang diwarisi dari ResNet: setiap unit konvolusi memiliki jalan pintas identitas, sehingga unit tersebut hanya perlu mempelajari selisih (sisa) terhadap masukannya. Pada konteks fusi, konsekuensinya adalah blok MMF tidak perlu membentuk ulang representasi gabungan dari nol; blok cukup mempelajari bagian fitur kedalaman yang melengkapi fitur warna, lalu menambahkannya. Desain ini juga membuat gradien mengalir balik ke kedua jalur tanpa terputus, sehingga jaringan sedalam ResNet-152 dapat dilatih *end-to-end* pada satu GPU.

## Cara Kerja Langkah demi Langkah

### Representasi Kedalaman: HHA

Peta kedalaman mentah tidak langsung dipakai sebagai masukan. Mengikuti Gupta et al. (2014), kedalaman dikodekan menjadi citra tiga kanal bernama HHA: disparitas horizontal (jarak relatif permukaan), tinggi di atas lantai, dan sudut normal permukaan terhadap arah gravitasi. Representasi ini menonjolkan diskontinuitas geometris — tepi benda, bidang tegak, bidang datar — yang sukar dipelajari konvolusi dari nilai kedalaman mentah, dan membuat jalur kedalaman dapat diinisialisasi dari bobot ResNet yang telah terlatih untuk citra tiga kanal.

### Dua Jalur Ekstraksi Fitur

Citra RGB dan citra HHA masing-masing dilewatkan ke ResNet terpisah dengan jumlah lapisan yang sama (ResNet-50, -101, atau -152). Dari setiap jalur diambil empat tingkat fitur, yaitu keluaran blok res2, res3, res4, dan res5. Tingkat res2 beresolusi paling tinggi dan memuat detail tepi; tingkat res5 beresolusi paling rendah (1/32 dari citra masukan) tetapi memuat konteks semantik paling kuat. Delapan peta fitur inilah bahan fusi.

### Blok MMF: Fusi Residual Lintas Modalitas

Blok *Multi-modal Feature Fusion* (MMF) bekerja pada setiap tingkat secara independen. Tahapannya:

1. **Reduksi dimensi.** Fitur RGB dan fitur HHA masing-masing dilewatkan satu konvolusi untuk memangkas jumlah kanal — 512 kanal pada tingkat terdalam (MMF-4) dan 256 kanal pada tiga tingkat lainnya — agar jumlah parameter terkendali. Sebelum konvolusi ini dipasang *dropout* 0,5, yaitu teknik regularisasi yang menonaktifkan setengah unit secara acak saat pelatihan untuk mencegah *overfitting*.
2. **Transformasi per modalitas.** Setiap fitur melewati dua *Residual Convolutional Unit* (RCU), yaitu pasangan lapis ReLU–konvolusi 3×3 dengan jalan pintas identitas. Berbeda dengan RCU di dalam RefineNet yang bertugas memurnikan resolusi, RCU di sini bertugas membentuk representasi khusus untuk keperluan fusi.
3. **Konvolusi adaptasi dan penjumlahan.** Satu konvolusi tambahan pada tiap cabang menyesuaikan skala nilai fitur sebelum dijumlahkan elemen demi elemen. Karena fitur warna umumnya lebih diskriminatif untuk segmentasi, penjumlahan ini secara praktis mempelajari fitur kedalaman sebagai sisa pelengkap terhadap fitur warna; bobot konvolusi adaptasi yang dilatih mengatur seberapa besar kontribusi tiap modalitas.
4. **Pooling residual.** Satu operasi *max-pooling* 5×5 dengan stride 1 diikuti konvolusi, dijumlahkan kembali secara residual, untuk menyuntikkan konteks dari wilayah sekitar piksel. Penulis menemukan satu pooling per tingkat sudah cukup.

Susunan keseluruhan jaringan digambarkan sebagai berikut:

```
citra RGB ──► ResNet (warna)     peta depth ─► HHA ─► ResNet (kedalaman)
   fitur res2..res5                   fitur res2'..res5'

res5 ─┐
      ├─► MMF-4 (512 kanal) ─► RefineNet-4 ─┐
res5'─┘                                     │
res4 ─┐                                     ▼
      ├─► MMF-3 (256 kanal) ──────► RefineNet-3 ─┐
res4'─┘                                          │
res3 ─┐                                          ▼
      ├─► MMF-2 (256 kanal) ──────► RefineNet-2 ─┐
res3'─┘                                          │
res2 ─┐                                          ▼
      ├─► MMF-1 (256 kanal) ──────► RefineNet-1
res2'─┘                                          │
                                                 ▼
                          2× RCU ─► konvolusi 1×1 ─► softmax
                          peta label per piksel (40 kelas, NYUDv2)
```

Aliran berjalan dari tingkat terdalam ke terdangkal: keluaran RefineNet-4 menjadi masukan RefineNet-3 bersama hasil fusi tingkat berikutnya, dan seterusnya, sehingga konteks semantik dari res5 dibawa naik dan dipertajam oleh detail dari res2.

### Rangkaian RefineNet

Setiap blok RefineNet menerima fitur fusi dari MMF pada tingkatnya ditambah fitur hasil pemurnian tingkat sebelumnya (kecuali RefineNet-4 yang hanya menerima MMF-4). Di dalamnya, RCU menyesuaikan fitur, *multi-resolution fusion* menaikkan resolusi masukan beresolusi rendah lalu menjumlahkannya dengan masukan beresolusi tinggi, dan *chained residual pooling* — rantai beberapa pooling 5×5 ber-konvolusi yang dijumlahkan residual — menangkap konteks wilayah luas. Keluaran RefineNet-1 dilewatkan dua RCU tambahan dan konvolusi 1×1 ber-*dropout* 0,5 untuk menghasilkan peta skor kelas per piksel, kemudian dilatih dengan *softmax loss*.

### Pelatihan

Implementasi memakai Caffe pada satu GPU GTX Titan X. Pelatihan menggunakan momentum 0,9, *weight decay* 0,0005, laju pembelajaran awal 10⁻⁴ yang dibagi sepuluh saat *loss* berhenti turun, dan laju 0,1 kali lebih kecil untuk lapisan ResNet dasar. Augmentasi data berupa penskalaan, pemotongan, dan pembalikan acak; saat pengujian dipakai evaluasi multi-skala dengan merata-rata prediksi.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur RGB-D dalam ruangan. NYUDv2 memuat 1.449 pasang citra berlabel padat (795 latih, 654 uji) dengan 40 kelas; SUN RGB-D memuat 10.335 pasang citra dari empat sensor berbeda (5.285 latih, 5.050 uji) dengan 37 kelas. Tiga metrik dilaporkan: akurasi piksel (proporsi piksel benar), akurasi rata-rata kelas, dan *mean IoU* (rata-rata rasio irisan terhadap gabungan antara wilayah prediksi dan kebenaran per kelas) — metrik paling ketat karena menghukum baik piksel yang terlewat maupun yang salah label.

| Metode | Data | Akurasi piksel | Akurasi rata-rata | mIoU |
|---|---|---|---|---|
| FCN (Long et al.) | RGB-D | 65,4 | 46,1 | 34,0 |
| FuseNet (SUN RGB-D) | RGB-D | 76,3 | 48,3 | 37,3 |
| RefineNet-152 (NYUDv2) | RGB | 73,6 | 58,9 | 46,5 |
| RefineNet-152 (SUN RGB-D) | RGB | 80,6 | 58,5 | 45,9 |
| **RDFNet-152 (NYUDv2)** | RGB-D | **76,0** | **62,8** | **50,1** |
| **RDFNet-152 (SUN RGB-D)** | RGB-D | **81,5** | **60,1** | **47,7** |

Interpretasi angka utama: pada NYUDv2, menambahkan jalur kedalaman dan fusi MMF menaikkan mIoU dari 46,5% (RefineNet-152 berbasis RGB) menjadi 50,1%, naik 3,6 poin; akurasi rata-rata kelas naik 3,9 poin. Pada SUN RGB-D kenaikannya 1,8 poin mIoU (45,9% → 47,7%) — lebih kecil, dan penulis menjelaskan sebabnya: dataset ini memuat banyak peta kedalaman rusak (pengukuran tidak valid dari sensor RealSense) yang tidak dibersihkan, sehingga manfaat modalitas kedalaman berkurang. Terhadap metode RGB-D sebelumnya marginnya besar: FuseNet hanya 37,3% mIoU pada SUN RGB-D, dan FCN 34,0% pada NYUDv2.

Tiga temuan ablatif memperkuat klaim desain. Pertama, mengganti MMF dengan fusi konkatenasi multi-tingkat (baseline terkuat yang diuji penulis) hanya menghasilkan 47,0% mIoU pada NYUDv2 (ResNet-101), tertinggal 2,1 poin dari RDF-101 (49,1%) — bukti bahwa keuntungan berasal dari mekanisme fusi residual, bukan sekadar dari tambahan data kedalaman. Kedua, membuang konvolusi adaptasi menurunkan mIoU ke 47,7%, dan membuang koneksi residual di dalam RCU menurunkannya ke 45,8% — keduanya komponen kritis, sedangkan membuang pooling residual hanya menurunkan ke 48,7% sehingga bersifat opsional. Ketiga, RDF-50 (mIoU 47,7%) sudah melampaui RefineNet-152 berbasis RGB (46,5%), artinya fusi kedalaman memberi keuntungan lebih besar daripada memperdalam backbone tiga kali lipat. Pada tabel per kelas, peningkatan terbesar terjadi pada kategori dengan perbedaan geometris tegas — *table* (40,1 → 49,7), *counter* (56,8 → 65,5), *dresser* (38,3 → 54,0) — sedangkan kelas *board* justru turun (63,7 → 46,0) karena contohnya sedikit dan secara geometris nyaris identik dengan kelas *picture*. Penggunaan peta kedalaman mentah tanpa HHA tetap membaik atas RefineNet (48,2%), tetapi lebih rendah dari HHA (49,1%), menegaskan nilai pengkodean geometris.

## Kelebihan dan Keterbatasan

Kelebihan utama RDFNet adalah fusi yang ditempatkan pada semua tingkat resolusi sekaligus, bukan satu titik, sehingga informasi geometris kedalaman ikut membentuk fitur dangkal maupun dalam. Desain residual menjaga pelatihan dua backbone dalam tetap stabil pada satu GPU, dan ablasi menunjukkan setiap komponen inti (konvolusi adaptasi, koneksi residual) berkontribusi pada akurasi. Metode ini juga tidak bergantung pada jenis masukan kedalaman: HHA maupun kedalaman mentah sama-sama dapat dipakai.

Keterbatasannya sebagian dicatat penulis, sebagian analisis penulis bab. Penulis makalah mengakui manfaat kedalaman menyusut pada data sensor berkualitas rendah, seperti citra RealSense di SUN RGB-D, dan kelas yang geometrinya tidak khas (seperti *board*) tidak terbantu. Dari sisi rekayasa, dua jalur ResNet penuh menggandakan biaya komputasi dan memori dibanding segmentasi RGB biasa, sehingga arsitektur ini berat untuk perangkat waktu-nyata — persoalan yang kemudian menjadi fokus metode seperti ESANet (bab 056). Secara konseptual, fusi dilakukan dengan penjumlahan yang bobotnya dipelajari secara implisit lewat konvolusi adaptasi; tidak ada mekanisme perhatian atau gerbang eksplisit untuk menimbang modalitas per piksel, sesuatu yang baru diperkenalkan karya-karya sesudahnya (misalnya ACNet pada bab 054).

## Kaitan dengan Bab Lain

RDFNet melanjutkan garis fusi RGB-D yang dimulai FuseNet pada bab 051 ([051 - 2016 - FuseNet](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)): bila FuseNet hanya menjumlahkan fitur kedalaman di bagian *encoder*, RDFNet menggeser fusi ke seluruh tingkat dan ke jalur pemulihan resolusi, dengan mekanisme residual yang dipinjam dari RefineNet di ranah RGB. Penerusnya memperbaiki dua sisi berbeda. RedNet pada bab 052 ([052 - 2018 - RedNet](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)) mempertahankan pola dua backbone tetapi memindahkan fusi ke struktur *encoder-decoder* yang lebih efisien. ACNet pada bab 054 ([054 - 2019 - ACNet](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)) mengganti penjumlahan fusi dengan modul perhatian yang menimbang kontribusi modalitas secara eksplisit. ESANet pada bab 056 ([056 - 2021 - ESANet](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)) menjawab masalah biaya ganda dua backbone dengan arsitektur ringan berbasis ResNet-34 untuk pemakaian waktu-nyata. Dengan demikian RDFNet menjadi titik acuan "fusi berat tapi akurat" yang menjadi pembanding bagi seluruh karya sesudahnya di klaster ini.

## Poin untuk Sitasi

Kutip dengan kunci `park2017rdfnet`. Ringkasan yang aman dikutip: "RDFNet memperluas RefineNet menjadi arsitektur dua jalur RGB-D yang memfusikan fitur warna dan kedalaman (HHA) secara residual pada empat tingkat resolusi melalui blok *Multi-modal Feature Fusion*, mencapai mIoU 50,1% pada NYUDv2 dan 47,7% pada SUN RGB-D — terbaik pada masanya." Seluruh angka pada bab ini diverifikasi langsung terhadap naskah ICCV 2017 (CVF Open Access, hal. 4980–4989). Dua hal patut dicatat sebelum sitasi formal: hasil dilaporkan dengan evaluasi multi-skala saat pengujian, dan venue adalah konferensi utama ICCV 2017 (bukan *workshop*).
