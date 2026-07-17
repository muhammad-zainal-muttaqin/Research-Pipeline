# 051 - FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hazirbas2016fusenet` |
| Judul asli | FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture |
| Penulis | Caner Hazirbas, Lingni Ma, Csaba Domokos, Daniel Cremers |
| Tahun | 2016 |
| Venue | Asian Conference on Computer Vision (ACCV 2016), hal. 213–228, Springer LNCS |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **DOI (Springer):** https://doi.org/10.1007/978-3-319-54181-5_14
- **PDF resmi (TUM):** https://vision.in.tum.de/_media/spezial/bib/hazirbasma2016fusenet.pdf
- **Kode resmi (Caffe):** https://github.com/tum-vision/fusenet
- **Google Scholar:** https://scholar.google.com/scholar?q=FuseNet%3A%20Incorporating%20Depth%20into%20Semantic%20Segmentation%20via%20Fusion-Based%20CNN%20Architecture
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=FuseNet%3A%20Incorporating%20Depth%20into%20Semantic%20Segmentation%20via%20Fusion-Based%20CNN%20Architecture&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan FuseNet, jaringan saraf konvolusi (CNN) untuk segmentasi semantik — pelabelan kelas pada setiap piksel citra — pada data RGB-D, yaitu citra yang memiliki tiga kanal warna (RGB) ditambah satu kanal kedalaman (*depth*) yang merekam jarak setiap piksel ke kamera. FuseNet memakai arsitektur *encoder-decoder* (jaringan yang mengecilkan resolusi fitur lalu memulihkannya) dengan dua cabang *encoder*: satu mengekstrak fitur dari citra RGB, satu lagi dari citra kedalaman. Fitur kedalaman kemudian disalurkan ke cabang RGB melalui penjumlahan elemen demi elemen pada beberapa tingkat kedalaman jaringan, dan satu *decoder* menghasilkan peta label akhir.

Hasil utamanya: pada tolok ukur SUN RGB-D (37 kelas ruangan dalam), varian FuseNet-SF5 mencapai akurasi piksel global 76,27%, akurasi kelas rata-rata 48,30%, dan IoU rata-rata 37,29% — mengungguli metode CNN pembanding saat itu dan hanya kalah dari Context-CRF yang memakai pasca-pemrosesan khusus. Uji ablasi menunjukkan fusi fitur lebih efektif daripada menumpuk kedalaman sebagai kanal keempat masukan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada 2015, segmentasi semantik berbasis CNN berkembang melalui dua garis arsitektur. FCN (*Fully Convolutional Network*) melatih jaringan secara *end-to-end* — dari citra masukan langsung ke peta label tanpa tahap terpisah. SegNet dan DeconvNet memperkenalkan pola *encoder-decoder* berbasis VGG-16: *encoder* memadatkan citra menjadi fitur beresolusi rendah dan *decoder* memulihkan resolusi penuh. Semuanya bekerja pada citra RGB saja.

Sementara itu, kamera RGB-D murah telah tersedia dan kanal kedalaman membawa informasi geometri — bentuk dan batas objek — yang komplementer terhadap warna: dua objek sewarna sering dapat dipisahkan oleh perbedaan jaraknya. Namun, cara memanfaatkan kedalaman belum mapan. Pendekatan HHA (Gupta dkk., 2014) mengubah kedalaman menjadi tiga kanal turunan — disparitas, tinggi piksel dari lantai, dan sudut antara normal permukaan dengan gravitasi — tetapi perhitungannya mahal dan tidak menambah informasi berarti dibanding kedalaman mentah. Cara paling langsung, menumpuk kedalaman sebagai kanal keempat masukan, tidak memanfaatkan struktur geometri secara eksplisit. Pendekatan LSTM-F menggabungkan konteks kedua modalitas dengan jaringan rekuren, tetapi arsitekturnya kompleks dan sulit dilatih. Cara optimal memadukan RGB dan kedalaman di dalam CNN dengan demikian masih menjadi pertanyaan terbuka.

## Ide Utama

Gagasan inti FuseNet: berikan kedalaman cabang *encoder* tersendiri yang identik dengan cabang RGB, lalu gabungkan kedua modalitas pada level fitur, bukan pada level piksel. Secara mekanis, citra RGB masuk ke cabang pertama dan citra kedalaman (dinormalisasi ke rentang [0,255], sama dengan kanal warna) masuk ke cabang kedua. Setelah blok konvolusi tertentu, peta fitur cabang kedalaman dijumlahkan elemen demi elemen ke peta fitur cabang RGB, dan satu *decoder* mengeluarkan probabilitas kelas per piksel.

Intuisi mekanisnya: fitur tingkat rendah kedua modalitas bersifat saling melengkapi. Citra RGB kuat pada tepi tekstur, sedangkan citra kedalaman kuat pada diskontinuitas geometri — misalnya batas antara laptop dan dinding yang sewarna tetapi berbeda jarak. Dengan menjumlahkan kedua jenis fitur di dalam jaringan, cabang RGB memperoleh isyarat geometri tanpa kehilangan fitur warnanya sendiri.

## Cara Kerja Langkah demi Langkah

### Dua Cabang Encoder dan Blok CBR

Kedua cabang *encoder* meniru struktur konvolusi VGG-16 (jaringan klasifikasi 16 lapis dengan 5 tingkat *pooling*), tanpa tiga lapis terhubung penuh di ujungnya yang memangkas resolusi terlalu jauh. Setiap blok dasar disebut CBR: konvolusi (*Conv*), diikuti *batch normalization* (BN) — normalisasi peta fitur ke rata-rata nol dan variansi satu, dilanjutkan penskalaan dan pergeseran yang dipelajari — lalu ReLU (*Rectified Linear Unit*, fungsi aktivasi σ(x) = maks(0, x)). BN sebelum fusi memiliki fungsi penting: karena skala fitur kedalaman dinormalisasi terhadap fitur warna, penjumlahan tidak membuat fitur kedalaman menimpa fitur warna.

Pada tiap tingkat *pooling* (operasi yang menurunkan resolusi spasial, di sini separuh setiap tingkat), indeks lokasi nilai maksimum pada cabang RGB disimpan. Dengan 5 tingkat pooling, fitur 224×224 menyusut menjadi 7×7 pada titik tersempit jaringan.

### Fusi Penjumlahan dan Dua Strateginya

Lapis fusi diimplementasikan sebagai penjumlahan elemen demi elemen antara peta fitur kedalaman dan peta fitur RGB yang berukuran sama. Penulis menguji dua penempatan:

1. **Fusi rapat (*dense fusion*, DF):** lapis fusi disisipkan setelah setiap blok CBR pada cabang RGB.
2. **Fusi jarang (*sparse fusion*, SF):** lapis fusi hanya disisipkan sebelum setiap lapis *pooling*.

Nama varian menyertakan jumlah lapis fusi: karena VGG-16 memiliki 5 tingkat pooling, SF5 berarti fusi pada kelima tingkat, sedangkan DF1 hanya satu kali fusi di blok pertama.

### Mengapa Fusi Setelah ReLU

Makalah memberikan argumen formal mengapa fusi aktivasi lebih baik daripada fusi masukan. Untuk masukan empat kanal, keluaran satu neuron adalah σ(〈u,a〉 + 〈v,b〉 + bias), dengan a aktivasi dari kanal warna dan b dari kanal kedalaman. Karena σ nonlinear dan monoton, berlaku σ(〈u,a〉 + 〈v,b〉) ≤ σ(〈u,a〉) + σ(〈v,b〉). Ruas kanan persis merupakan fusi FuseNet: aktivasi masing-masing cabang melewati ReLU dulu, baru dijumlahkan. Fusi sesudah ReLU mempertahankan aktivasi pada lokasi neuron yang berbeda — tepi warna dan tepi geometri sama-sama lestari, sedangkan penjumlahan sebelum ReLU dapat saling meniadakan. Visualisasi peta fitur blok pertama pada makalah memperkuat argumen ini: daerah tanpa tekstur dibedakan oleh fitur struktur dari kedalaman, dan daerah tanpa struktur dibedakan oleh fitur warna.

Skema aliran data FuseNet-SF5:

```
RGB 224x224                     depth 224x224 (diskala ke [0,255])
    │                                │
┌───▼────────────┐             ┌─────▼──────────┐
│ encoder RGB    │             │ encoder depth  │  CBR = Conv+BN+ReLU
│ (VGG-16, 5     │             │ (VGG-16)       │
│  blok pooling) │   ┌───┐     │                │
│ CBR1 ──────────┼──▶│ + │◀────┼──── CBR1       │  + = penjumlahan
│ pool1          │   └───┘     │                │      elemen-wise
│ CBR2 ──────────┼──▶│ + │◀────┼──── CBR2       │  (hanya sebelum
│ ...            │    ...      │     ...        │   pooling pada SF)
│ CBR5 ──────────┼──▶│ + │◀────┼──── CBR5       │
└───┬────────────┘   └───┘     └────────────────┘
    │ fitur 7x7
┌───▼────────────┐
│ decoder (cermin│  unpooling memakai indeks pooling RGB,
│  encoder)      │  diikuti blok CBR; dropout saat latih
└───┬────────────┘
    ▼
peta label 37 kelas (softmax per piksel)
```

### Decoder dan Pelatihan

*Decoder* adalah cerminan *encoder*: *unpooling* menaikkan resolusi dengan menempatkan nilai fitur kembali ke posisi indeks maksimum yang disimpan saat pooling (cara SegNet), lalu blok CBR memperhalus hasilnya. Lapisan akhir memakai *softmax* — fungsi yang mengubah skor kelas menjadi probabilitas yang berjumlah satu — sehingga setiap piksel memperoleh distribusi atas 37 kelas. *Dropout* (pemadaman acak sebagian neuron untuk menekan *overfitting*) aktif saat pelatihan dan dimatikan saat pengujian.

Pelatihan dilakukan *end-to-end* dengan fungsi *loss cross-entropy* per piksel. Karena SUN RGB-D sangat timpang (16 dari 37 kelas jarang muncul), loss setiap kelas dibobot *median frequency balancing*: bobot kelas berbanding terbalik dengan frekuensinya, sehingga kelas langka tidak tertutup kelas dominan. Citra diubah ke 224×224; bobot *encoder* disetel halus (*fine-tuning*) dari VGG-16 terlatih ImageNet, dan bobot konvolusi pertama cabang kedalaman diperoleh dengan merata-rata bobot kanal warna.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada tolok ukur SUN RGB-D: 10.335 pasangan citra RGB-D ruangan dalam dengan anotasi per piksel untuk 37 kelas, terbagi 5.285 citra latih/validasi dan 5.050 citra uji; 587 citra latih dari kamera RealSense dibuang karena banyak kedalaman yang tidak valid. Tiga metrik dipakai: akurasi global (persentase piksel benar), akurasi kelas rata-rata (*mean*), dan IoU (*Intersection over Union* — rata-rata rasio irisan terhadap gabungan antara prediksi dan kebenaran per kelas). IoU paling informatif karena tahan terhadap ketimpangan kelas.

Perbandingan dengan metode sezaman pada SUN RGB-D:

| Metode | Global | Mean | IoU |
|---|---|---|---|
| FCN-32s (RGB) | 68,35 | 41,13 | 29,00 |
| Bayesian SegNet (RGB) | 71,2 | 45,9 | 30,7 |
| LSTM-F (RGB-D) | — | 48,1 | — |
| Context-CRF (RGB) | 78,4 | 53,4 | 42,3 |
| FuseNet-DF1 | 73,37 | 50,07 | 34,02 |
| FuseNet-SF5 | 76,27 | 48,30 | 37,29 |

Interpretasinya: FuseNet-SF5 mengungguli semua pembanding CNN murni — selisih IoU terhadap Bayesian SegNet sebesar 6,6 poin, padahal SegNet memakai RGB saja dan FuseNet memakai modalitas tambahan. FuseNet hanya berada di bawah Context-CRF; penulis mencatat Context-CRF dilatih dengan fungsi loss khusus dan pasca-pemrosesan *Conditional Random Field* (CRF, model grafis yang menghaluskan label antar-piksel), sehingga perbandingannya tidak setara.

Ablasi membandingkan cara memanfaatkan kedalaman. Jaringan yang sama dilatih dengan masukan berbeda: kedalaman saja (IoU 28,49), HHA saja (28,88), RGB saja (32,47), RGB-D tumpukan empat kanal (31,95), dan RGB-HHA enam kanal (33,64). Dua hal menonjol. Pertama, menumpuk kedalaman sebagai kanal keempat justru menurunkan IoU di bawah RGB saja — bukti bahwa fusi masukan naif tidak efektif. Kedua, FuseNet-SF5 (IoU 37,29) mengalahkan semuanya, termasuk RGB-HHA, tanpa praproses HHA. Per kelas, SF5 mengungguli model RGB-D tumpukan pada 30 dari 37 kelas menurut IoU. Variasi jumlah fusi menunjukkan kenaikan IoU dari SF1 (35,99) hingga SF4 (37,76) lalu jenuh; penulis menduga kedalaman sudah memberi fitur pembeda yang kuat pada tingkat rendah sehingga fusi di tingkat dalam memberi manfaat kecil.

Sebagai tambahan di luar naskah, repositori resmi melaporkan model terlatih untuk NYUv2 (40 kelas): FuseNet-SF5 mencapai akurasi global 66,0%, akurasi kelas 43,4%, dan IoU 32,7% — konsisten dengan pola bahwa fusi kedalaman menaikkan akurasi.

## Kelebihan dan Keterbatasan

Kelebihan: (1) arsitektur sederhana — fusi hanya penjumlahan elemen demi elemen, sehingga mudah direplikasi dan dilatih *end-to-end*; (2) tidak memerlukan praproses HHA yang mahal; fitur kedalaman dipelajari langsung; (3) peningkatan akurasi konsisten terhadap RGB saja dan terhadap penumpukan kanal, didukung argumen formal dan ablasi; (4) kode dan model resmi dirilis, sehingga hasil dapat direproduksi.

Keterbatasan: (1) dari sisi rekayasa, dua cabang *encoder* VGG-16 membuat parameter hampir dua kali lipat model RGB biasa — berat untuk perangkat terbatas; (2) secara konseptual, penjumlahan bersifat tetap: semua lokasi piksel menerima kontribusi kedalaman dengan cara yang sama, tanpa mekanisme pemilihan adaptif; (3) akurasi kelas langka tetap rendah — kelas *mat* memperoleh akurasi 0% pada semua varian, sehingga pembobotan loss terbukti tidak menyelesaikan ketimpangan ekstrem; (4) kinerja bergantung pada kualitas kedalaman, terbukti dari dibuangnya 587 citra RealSense; (5) tanpa pasca-pemrosesan konteks, akurasinya tertinggal dari metode berbasis CRF.

## Kaitan dengan Bab Lain

FuseNet adalah fondasi klaster Segmentasi RGB-D dalam tinjauan ini: pola "dua *encoder*, fusi ke cabang RGB, satu *decoder*" menjadi titik tolak bab-bab berikutnya. [053 - 2017 - RDFNet](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md) mengganti penjumlahan tetap FuseNet dengan modul pemurnian fitur multimodal berbasis residual, dan [052 - 2018 - RedNet](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md) mempertahankan fusi penjumlahan di atas arsitektur residual ResNet. Keterbatasan fusi yang tidak adaptif dijawab oleh [054 - 2019 - ACNet](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) dan [055 - 2020 - SA-Gate](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md) melalui mekanisme gerbang yang menimbang kontribusi tiap modalitas per lokasi. [056 - 2021 - ESANet](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md) menyerang keterbatasan bobot komputasi dengan *encoder* yang jauh lebih ringan, dan [058 - 2023 - CMX](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) membawa gagasan fusi silang ini ke arsitektur Transformer.

## Poin untuk Sitasi

Kutip dengan kunci `hazirbas2016fusenet`. Ringkasan yang aman dikutip: "FuseNet memadukan RGB dan kedalaman untuk segmentasi semantik melalui dua cabang *encoder* VGG-16 yang fitur kedalamannya dijumlahkan ke cabang RGB sebelum setiap *pooling*; pada SUN RGB-D varian SF5 mencapai akurasi global 76,27% dan IoU 37,29%, mengungguli fusi kanal masukan dan representasi HHA." Seluruh angka SUN RGB-D pada bab ini terverifikasi langsung dari naskah ACCV 2016. Catatan verifikasi: angka NYUv2 (66,0% / 43,4% / 32,7%) bersumber dari README repositori resmi tum-vision/fusenet, bukan dari naskah — verifikasi ke sumber asli sebelum dikutip. Makalah ini tidak ada di arXiv; versi resminya adalah prosiding ACCV (DOI 10.1007/978-3-319-54181-5_14).
