# 055 - Bi-Directional Cross-Modality Feature Propagation with Separation-and-Aggregation Gate for RGB-D Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2020sagate` |
| Judul asli | Bi-Directional Cross-Modality Feature Propagation with Separation-and-Aggregation Gate for RGB-D Semantic Segmentation |
| Penulis | Xiaokang Chen, Kwan-Yee Lin, Jingbo Wang, Wayne Wu, Chen Qian, Hongsheng Li, Gang Zeng |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV 2020) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2007.09183
- **DOI arXiv:** https://doi.org/10.48550/arXiv.2007.09183
- **Kode resmi (PyTorch):** https://github.com/charlesCXK/RGBD_Semantic_Segmentation_PyTorch
- **Google Scholar:** https://scholar.google.com/scholar?q=Bi-Directional%20Cross-Modality%20Feature%20Propagation%20with%20Separation-and-Aggregation%20Gate%20for%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Bi-Directional%20Cross-Modality%20Feature%20Propagation%20with%20Separation-and-Aggregation%20Gate%20for%20RGB-D%20Semantic%20Segmentation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan SA-Gate (*Separation-and-Aggregation Gate*), unit gerbang untuk menggabungkan fitur RGB dan kedalaman pada segmentasi semantik RGB-D, yaitu tugas melabeli setiap piksel dengan kelasnya dari masukan citra warna dan peta kedalaman. Masalah yang ditangani adalah derau kedalaman: metode fusi sebelumnya mengasumsikan kedalaman akurat dan selaras dengan piksel RGB, padahal sensor menghasilkan nilai yang salah pada banyak area. SA-Gate menerapkan prinsip "saring dulu, baru gabung": fitur setiap modalitas disaring oleh gerbang kanal yang dihitung dari informasi gabungan kedua modalitas (*feature separation*), baru digabung secara selektif di setiap posisi spasial (*feature aggregation*). Hasil fusi dipropagasikan dua arah antar-tahap melalui strategi *Bi-direction Multi-step Propagation* (BMP).

Hasil utamanya adalah akurasi tertinggi saat rilis pada dua tolok ukur: 52,4% mIoU pada NYUDv2 (dalam ruang) dan 82,8% mIoU pada *test set* Cityscapes (luar ruang), dengan model yang lebih ringan daripada garis dasar dua jaringan penuh.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Kedalaman memberi informasi geometri tiga dimensi yang melengkapi warna: ia tidak berubah saat pencahayaan berubah dan membantu memisahkan objek yang warnanya serupa. Fusi RGB-D berkembang dari penggabungan sederhana menuju penggabungan berlapis: FuseNet (bab 051) menjumlahkan fitur dua aliran jaringan, RedNet (bab 052) memakai dua *backbone* (jaringan pengekstrak fitur) residu dengan penjumlahan antar-tingkat, RDFNet (bab 053) memperluas fusi residu ke banyak tingkat, dan ACNet (bab 054) memakai modul perhatian untuk memetik fitur komplementer. Semuanya menangani perbedaan karakteristik kedua modalitas, tetapi mengasumsikan kedalaman masukan berkualitas baik.

Asumsi itu tidak berlaku pada data nyata. Sensor kedalaman seperti Kinect dan RealSense menghasilkan pengukuran yang salah di sekitar batas objek, pada permukaan gelap atau mengilap, dan pada jarak di luar jangkauan sensor. Derau ini jauh lebih parah di luar ruang, sehingga fusi naif justru meneruskan kesalahan kedalaman ke dalam fitur RGB. Jalur alternatif seperti PADNet dan PAP menjadikan kedalaman sebagai sinyal pengawasan tambahan dalam pembelajaran multi-tugas, bukan sebagai masukan; pendekatan itu lebih tahan derau, tetapi interaksi kedua modalitas hanya dimodelkan secara implisit. Celah inilah yang diisi makalah ini: fusi eksplisit yang sekaligus sadar terhadap derau kedalaman.

## Ide Utama

Gagasan inti makalah ini dua hal. Pertama, jangan menggabungkan fitur kedua modalitas apa adanya: saring dulu setiap modalitas dengan gerbang yang dihitung dari modalitas lainnya, sehingga respons yang berasal dari pengukuran kedalaman keliru ditekan sebelum mencemari representasi gabungan. Kedua, jangan menggabung hanya sekali: lakukan fusi di setiap tahap jaringan dan kembalikan hasilnya ke kedua aliran, sehingga informasi mengalir dua arah sementara masing-masing modalitas tetap mempertahankan kekhasannya.

Masukan berupa sepasang peta fitur RGB dan HHA berukuran sama; keluarannya peta fitur gabungan yang kanalnya sudah disaring dan posisinya sudah ditimbang. Yang berubah dibanding fusi biasa hanyalah dua gerbang kecil di antara kedua aliran, sehingga modul ini dapat disisipkan ke arsitektur segmentasi yang ada.

## Cara Kerja Langkah demi Langkah

### Arsitektur Keseluruhan

Jaringan memakai dua aliran *encoder* ResNet-101; *encoder* adalah bagian jaringan yang memadatkan citra menjadi peta fitur, dan ResNet adalah jaringan konvolusi dengan koneksi pintas (*skip connection*) yang menjumlahkan masukan suatu blok dengan keluarannya sehingga jaringan dalam tetap dapat dilatih. Satu aliran menerima citra RGB; aliran lain menerima peta HHA, yaitu pengkodean kedalaman menjadi tiga kanal — disparitas horizontal, tinggi di atas tanah, dan sudut normal permukaan terhadap gravitasi — agar kedalaman dapat diolah seperti citra tiga kanal biasa. Setelah setiap blok disisipkan satu SA-Gate; strategi BMP mengatur pengembalian hasil fusi ke kedua aliran. Hasil fusi dari SA-Gate pertama dan terakhir diteruskan ke *decoder* DeepLab V3+, yaitu pemulih peta fitur menjadi peta kelas per piksel, yang memakai konvolusi *atrous* (konvolusi berlubang untuk memperluas cakupan pandang tanpa menambah parameter).

Susunan aliran data tersebut digambarkan pada diagram berikut:

```
              ENCODER DUA ALIRAN (2 x ResNet-101)
 ┌────────────────────────────────────────────────────────────┐
 │                                                            │
 RGB  ─► [Blok1] ─► [Blok2] ─► [Blok3] ─► [Blok4] ─┐          │
           │         │         │         │         │ BMP:     │
          SAG1      SAG2      SAG3      SAG4       │ M_l      │
           │         │         │         │         │ dibagi 2 │
 HHA  ─► [Blok1] ─► [Blok2] ─► [Blok3] ─► [Blok4] ◄┘          │
 │                                                            │
 │  SAG = SA-Gate (saring kanal + gabung spasial)              │
 │  keluaran SAG1 dan SAG4 ─► decoder DeepLab V3+ ─► peta kelas│
 └────────────────────────────────────────────────────────────┘
```

Setiap panah vertikal SAG menandai penyaringan dan penggabungan pada tahap itu; panah BMP menunjukkan hasil gabungan M_l yang dikembalikan ke kedua aliran.

### Feature Separation: Menyaring Kanal yang Derau

Tahap pertama SA-Gate adalah *feature separation* (FS): menekan kanal fitur yang membawa derau sebelum modalitas itu dipakai mengkalibrasi pasangannya. Kedua peta fitur, RGB_in dan HHA_in yang masing-masing berukuran C×H×W (C kanal, tinggi H, lebar W), diringkas per kanal dengan *global average pooling* (setiap kanal menjadi satu angka rata-rata). Hasilnya digabung menjadi vektor 2C, deskriptor global lintas-modal. Vektor ini dilewatkan ke sebuah MLP (*multi-layer perceptron*, jaringan lapis terhubung penuh kecil) dan fungsi sigmoid yang memetakan keluaran ke rentang (0,1), menghasilkan gerbang kanal W_hha sepanjang C. Peta kedalaman dikalikan kanal-per-kanal dengan gerbang ini menjadi HHA_tersaring; kanal yang menurut jaringan membawa derau mendapat bobot mendekati nol.

Fitur kedalaman tersaring lalu dipakai mengkalibrasi ulang fitur RGB melalui penjumlahan: RGB_kal = HHA_tersaring + RGB_in. Penjumlahan menjadikan fitur kedalaman ofset yang menggeser respons RGB, bukan pengali yang dapat menumpulkannya; uji ablation makalah (membandingkan varian desain dengan mengganti satu komponen) menunjukkan penjumlahan mengungguli perkalian (48,6% lawan 47,5% mIoU pada NYUDv2 tanpa decoder). Proses ini berjalan simetris dua arah: fitur RGB disaring dengan cara yang sama dan dipakai mengkalibrasi fitur kedalaman, karena RGB pun keliru ketika dua objek tampak serupa.

### Feature Aggregation: Menggabung Selektif per Posisi

Tahap kedua, *feature aggregation* (FA), memutuskan di setiap posisi spasial modalitas mana yang lebih dipercaya. Kedua fitur hasil kalibrasi dikonkatenasi menjadi 2C×H×W, lalu sebuah konvolusi 1×1 (konvolusi yang hanya mencampur informasi antar-kanal di satu piksel) memetakannya menjadi dua gerbang spasial G_rgb dan G_hha, masing-masing berukuran 1×H×W. Fungsi *softmax* membuat bobot keduanya berjumlah satu di setiap posisi: A_rgb(i,j) + A_hha(i,j) = 1. Fitur gabungan akhir adalah jumlah berbobot M(i,j) = RGB_in(i,j)·A_rgb(i,j) + HHA_in(i,j)·A_hha(i,j).

Contoh numerik: pada area silau yang membutakan kamera tetapi tidak memengaruhi sensor kedalaman, jaringan dapat menghasilkan A_hha = 0,8 dan A_rgb = 0,2, sehingga 80% kontribusi fitur di posisi itu berasal dari kedalaman; pada batas objek yang tajam secara warna tetapi kabur secara kedalaman, bobot berbalik memihak RGB.

### Bi-direction Multi-step Propagation

Pada strategi BMP, setiap blok l merata-ratakan keluaran SA-Gate M_l dengan keluaran blok masing-masing aliran: RGB_out = (RGB_in + M_l)/2, dan setara untuk aliran HHA; hasilnya menjadi masukan blok berikutnya. Karena bobot softmax berjumlah satu, skala fitur tidak berubah sehingga bobot *pre-trained* ResNet tetap kompatibel. Propagasi berlangsung dua arah sepanjang empat blok, sementara penjumlahan dengan keluaran asli tiap blok menjaga kekhasan masing-masing modalitas agar tidak larut seluruhnya.

### Decoder dan Pelatihan

Karena bekerja di sisi *encoder*, decoder dapat diganti bebas; makalah memilih DeepLab V3+ yang memberi hasil terbaik. Pelatihan memakai SGD dengan momentum 0,9 dan *batch* 16; pada NYUDv2 digunakan potongan citra 480×480 selama 800 *epoch*, pada Cityscapes potongan 800×800 selama 240 *epoch*.

## Eksperimen dan Hasil

Evaluasi memakai dua tolok ukur. NYUDv2 berisi 1.449 pasangan citra RGB-D dalam ruang (795 latih, 654 uji, 40 kelas); Cityscapes berisi citra jalanan 2048×1024 (2.975 latih, 500 validasi, 1.525 uji, 19 kelas) dengan kedalaman stereo yang derau. Metrik utama adalah mIoU (*mean Intersection over Union*): rasio irisan terhadap gabungan antara piksel prediksi dan kebenaran per kelas, dirata-ratakan antar-kelas; maksimum 100%.

Hasil utama pada NYUDv2: 52,4% mIoU dan 77,9% akurasi piksel dengan inferensi multi-skala, melampaui pembanding terkuat — PAP 50,4%, PADNet 50,2%, RDFNet-101 49,1%, dan ACNet 48,3%. Selisih 2,0 poin atas PAP berarti fusi eksplisit yang sadar derau mengalahkan distilasi multi-tugas pemegang rekor sebelumnya; dengan *backbone* ResNet-50 yang setara pembanding, model ini tetap unggul pada 51,3%.

Hasil Cityscapes membuktikan tesis makalah. Garis dasar RGB-D naif (dua DeepLab V3+ yang hasilnya dirata-rata) hanya mencapai 80,9% mIoU, lebih rendah dari garis dasar RGB murni (81,8%) — bukti langsung bahwa kedalaman derau luar ruang merusak model yang menggabungkannya tanpa penyaringan. Model ini mencapai 82,8% pada *test set* dan 81,7% pada validasi, mengungguli metode RGB kuat seperti DANet (81,5%) dan Choi dkk. (82,1%). Kedalaman yang sama, setelah disaring SA-Gate, berbalik memberi keuntungan 1,9 poin atas garis dasar RGB-D.

Uji ablation pada NYUDv2 tanpa decoder menunjukkan: garis dasar dua aliran yang dirata-rata memperoleh 45,9%; menambah SA-Gate saja memberi +1,5 poin, BMP saja +1,9 poin, dan keduanya bersama-sama +2,7 poin menjadi 48,6%. Penyaringan lintas-modal terbukti penting: menyaring dengan informasi modalitas sendiri turun ke 47,5%. Uji *plug-and-play* pada tujuh decoder berbeda konsisten menambah 1,5 hingga 3,7 poin mIoU terhadap versi RGB-D naifnya. Model ini juga lebih hemat dari garis dasar dua DeepLab V3+ penuh: 63,4 juta parameter dan 204,9 GFLOPs (miliar operasi titik-mengambang per citra) berbanding 78,2 juta dan 269,6 GFLOPs, sekaligus lebih akurat (50,4% lawan 46,7%).

## Kelebihan dan Keterbatasan

Kelebihannya empat hal. Pertama, prinsip saring-sebelum-gabung menjadikan fusi tahan derau kedalaman, terbukti pada Cityscapes di mana metode fusi lain justru dirugikan oleh kedalaman. Kedua, modulnya *plug-and-play* dengan keuntungan konsisten pada tujuh decoder. Ketiga, gerbangnya terinterpretasi: peta bobot menunjukkan modalitas yang dipercaya di setiap area. Keempat, desainnya lebih efisien daripada dua model segmentasi penuh.

Keterbatasannya sebagian bersifat analisis. Secara konseptual, SA-Gate bergantung pada pengkodean HHA yang dihitung terlebih dahulu dari peta kedalaman, menambah tahap pra-pemrosesan di luar jaringan. Dari sisi rekayasa, dua aliran ResNet-101 tetap mahal dilatih (800 *epoch* pada NYUDv2), dan keuntungan penumpukan SA-Gate jenuh di blok tinggi — tiga gerbang pertama sudah memberi 48,3% dari 48,6% maksimal — sehingga gerbang terakhir dapat dipangkas dengan kerugian kecil. Hasil 52,4% diperoleh dengan inferensi multi-skala; repositori resmi mencatat skala tunggal sekitar 51,4–51,5% — tetap di atas pembanding, tetapi perlu dicantumkan agar perbandingan adil.

## Kaitan dengan Bab Lain

Bab ini meneruskan garis fusi RGB-D dari [FuseNet (bab 051)](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md), [RedNet (bab 052)](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md), dan [RDFNet (bab 053)](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md) yang menggabungkan fitur kedua modalitas apa adanya, serta [ACNet (bab 054)](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) yang sudah memakai perhatian untuk fitur komplementer tetapi belum menyaring derau; SA-Gate menutup celah itu dengan gerbang lintas-modal dan propagasi dua arah. Arah yang dibukanya — fusi selektif yang sadar keandalan modalitas — dilanjutkan [ESANet (bab 056)](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md) menuju arsitektur yang lebih ringan dan [CMX (bab 058)](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) menuju fusi berbasis *transformer* untuk pasangan modalitas umum (RGB-X). Bagi klaster deteksi objek, bab ini menjadi rujukan konseptual untuk menyaring kedalaman sebelum digabung ke fitur visual.

## Poin untuk Sitasi

Kutip dengan kunci `chen2020sagate`. Ringkasan yang aman dikutip: "SA-Gate (ECCV 2020) menggabungkan fitur RGB dan kedalaman dengan prinsip saring-sebelum-gabung — gerbang kanal lintas-modal menekan fitur derau sebelum gerbang spasial menimbang kontribusi tiap modalitas per posisi — disertai propagasi dua arah multi-tahap; metode ini mencapai 52,4% mIoU pada NYUDv2 dan 82,8% mIoU pada *test set* Cityscapes, melampaui metode fusi maupun distilasi sebelumnya." Catatan verifikasi: angka inferensi skala tunggal (±51,4–51,5% NYUDv2) berasal dari README repositori resmi, bukan naskah; hasil pada SUN RGB-D hanya dilaporkan di materi suplemen makalah; nomor halaman 561–577 pada metadata lama belum diverifikasi ke prosiding ECCV.
