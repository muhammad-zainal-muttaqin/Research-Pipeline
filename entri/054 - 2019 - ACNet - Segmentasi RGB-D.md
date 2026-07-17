# 054 - ACNet: Attention Based Network to Exploit Complementary Features for RGBD Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hu2019acnet` |
| Judul asli | ACNet: Attention Based Network to Exploit Complementary Features for RGBD Semantic Segmentation |
| Penulis | Xinxin Hu, Kailun Yang, Lei Fei, Kaiwei Wang |
| Tahun | 2019 |
| Venue | IEEE International Conference on Image Processing (ICIP 2019), hal. 1440–1444 |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1905.10089
- **DOI (versi penerbit IEEE):** https://doi.org/10.1109/ICIP.2019.8803025
- **Kode sumber (PyTorch):** https://github.com/anheidelonghu/ACNet
- **Google Scholar:** https://scholar.google.com/scholar?q=ACNet%3A%20Attention%20Based%20Network%20to%20Exploit%20Complementary%20Features%20for%20RGBD%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ACNet%3A%20Attention%20Based%20Network%20to%20Exploit%20Complementary%20Features%20for%20RGBD%20Semantic%20Segmentation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan ACNet (*Attention Complementary Network*), jaringan untuk segmentasi semantik RGB-D pada adegan dalam ruangan. Segmentasi semantik adalah tugas memberi label kelas pada setiap piksel citra; pada varian RGB-D, masukannya berupa citra warna (RGB) beserta citra kedalaman (D) yang merekam jarak setiap piksel ke kamera. Masalah yang diangkat adalah ketidakseimbangan informasi antarmodalitas: RGB dan kedalaman tidak sama informatifnya di semua tempat, sehingga penggabungan fitur tanpa pembobotan menjadi tidak optimal.

Solusinya terdiri atas dua komponen. Pertama, arsitektur tiga cabang paralel berbasis ResNet: cabang RGB, cabang kedalaman, dan cabang fusi yang masing-masing tetap utuh sampai akhir *encoder*. Kedua, modul bernama *Attention Complementary Module* (ACM), yakni mekanisme *attention* per kanal yang menimbang fitur kedua cabang modalitas sesuai jumlah informasi yang dibawanya sebelum ditambahkan ke cabang fusi. Dengan ResNet-50 sebagai *backbone* (jaringan pengekstrak fitur utama), ACNet mencapai mIoU 48,3% pada NYUDv2, melampaui metode terbaik sebelumnya dengan selisih 0,6 poin, dan menyamai akurasi metode CFN pada SUN RGB-D dengan backbone yang lebih ringan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Segmentasi dalam ruangan lebih sulit daripada segmentasi luar ruangan karena pencahayaan tidak merata dan objek saling bertumpuk. Ketersediaan kamera RGB-D seperti Kinect dan RealSense memungkinkan pemakaian informasi geometrik dari citra kedalaman untuk membantu tugas ini. Pendekatan awal memperlakukan kedalaman sebagai kanal tambahan yang digabung langsung dengan RGB, atau menguraikannya menjadi tiga kanal HHA (disparitas, tinggi, sudut). Pendekatan berikutnya memakai dua *encoder* terpisah untuk RGB dan kedalaman, lalu menggabungkan fitur keduanya pada titik tertentu — misalnya FuseNet (bab 051) yang menjumlahkan peta fitur di dalam *encoder*, dan RedNet (bab 052) yang menyalurkan fitur kedalaman ke fitur RGB pada setiap tingkat resolusi.

Menurut penulis makalah, arsitektur-arsitektur tersebut terbagi ke dalam dua tipe yang sama-sama bermasalah. Tipe pertama menggabungkan fitur tepat sebelum atau selama tahap *upsampling* (pemulihan resolusi); akibatnya, informasi kedua modalitas tidak tergabung memadai karena interaksi baru terjadi pada fitur akhir yang sudah sangat terkompresi. Tipe kedua menggabungkan fitur sejak tahap *downsampling* (penurunan resolusi) dan menggantikan cabang modalitas asli dengan cabang gabungan; akibatnya, aliran informasi RGB dan kedalaman yang asli hilang sebelum dimanfaatkan penuh. Di atas kedua masalah struktural itu terdapat masalah yang lebih mendasar: distribusi fitur RGB dan kedalaman berbeda secara signifikan antaradegan, bahkan antardaerah dalam satu citra. Pada daerah bertekstur, citra warna memuat informasi dominan; pada daerah polos, bentuk geometrik dari kedalaman yang menentukan kelas piksel. Jaringan yang menggabungkan kedua modalitas dengan bobot tetap tidak dapat menyesuaikan diri dengan variasi ini.

## Ide Utama

Gagasan inti ACNet adalah memisahkan dua persoalan: bagaimana struktur jaringan mempertahankan aliran fitur tiap modalitas, dan bagaimana jaringan menentukan proporsi kontribusi tiap modalitas pada setiap titik penggabungan. Persoalan pertama dijawab dengan tiga cabang lengkap yang tidak saling menggantikan. Persoalan kedua dijawab dengan attention: proporsi penggabungan tidak ditetapkan di muka, melainkan dihitung oleh jaringan dari fitur masukan itu sendiri. Secara mekanis, setiap ACM menerima peta fitur RGB dan kedalaman pada satu tingkat resolusi, menimbang masing-masing dengan bobot per kanal, lalu menjumlahkan hasilnya ke cabang fusi, sementara cabang RGB dan kedalaman tetap berjalan tanpa diganggu.

## Cara Kerja Langkah demi Langkah

### Attention Complementary Module (ACM)

ACM merupakan bentuk *channel attention* (attention per kanal): alih-alih menimbang posisi spasial, modul ini menimbang kanal-kanal peta fitur, karena setiap kanal pada jaringan konvolusi merespons pola visual yang berbeda. Mekanismenya diilhami *squeeze-and-excitation* dan bekerja dalam empat langkah atas peta fitur masukan A berukuran C×H×W (C kanal, tinggi H, lebar W).

1. **Perangkapan global.** Setiap kanal dirata-ratakan pada seluruh piksel melalui *global average pooling*: nilai kanal ke-k adalah Z_k = (1/(H×W)) × Σ A_k(i,j). Hasilnya vektor Z berukuran C×1×1 yang merangkum kekuatan respons tiap kanal.
2. **Ekstraksi korelasi antarkanal.** Vektor Z dilewatkan ke konvolusi 1×1 (konvolusi yang mengombinasikan kanal tanpa mengubah dimensi spasial) untuk menggali keterkaitan antarkanal.
3. **Aktivasi sigmoid.** Hasil konvolusi dilewatkan ke fungsi sigmoid, yang memetakan setiap nilai ke rentang 0–1. Diperoleh vektor bobot V berukuran C×1×1.
4. **Pembobotan.** Setiap kanal peta fitur A dikalikan dengan bobotnya pada V. Secara formal, U = A ⊗ σ(φ(Z)), dengan ⊗ perkalian luar, σ sigmoid, dan φ konvolusi 1×1.

Pada pasangan modalitas, ACM cabang RGB menghasilkan bobot dari fitur RGB dan ACM cabang kedalaman menghasilkan bobot dari fitur kedalaman; kedua fitur terbobot lalu dijumlahkan per elemen ke dalam fitur cabang fusi. Visualisasi bobot pada makalah menunjukkan perilaku sesuai tujuan: kanal yang fitur RGB-nya lebih informatif menerima bobot RGB lebih besar, dan sebaliknya untuk kedalaman.

### Arsitektur Tiga Cabang

*Backbone* ACNet terdiri atas tiga ResNet-50 lengkap: satu memproses citra RGB, satu memproses citra kedalaman, satu menjadi cabang fusi. Karena citra kedalaman hanya berisi satu kanal, bobot tiga kanal pada lapis pertama ResNet-50 dirata-rata menjadi satu kanal untuk cabang kedalaman. Ketiga cabang berjalan melalui tahap-tahap standar ResNet (Conv, Layer1, Layer2, Layer3, Layer4) yang menghasilkan peta fitur pada resolusi makin kecil. Pada tahap pertama (Conv), fitur RGB dan kedalaman yang telah ditimbang ACM dijumlahkan per elemen dan menjadi masukan cabang fusi. Pada tahap berikutnya, fitur terbobot kedua modalitas dijumlahkan ke keluaran cabang fusi pada tahap yang bersesuaian. Dengan skema ini cabang RGB dan kedalaman tidak pernah digantikan oleh cabang gabungan, sementara cabang fusi menerima fitur lintas-modalitas pada semua tingkat, dari fitur tingkat rendah (tekstur, tepi) hingga tingkat tinggi (bentuk, semantik).

Aliran data tiga cabang dan peran ACM dirangkum pada diagram berikut:

```
 citra RGB                citra kedalaman
    │                          │
 ┌──▼──────────┐          ┌────▼─────────┐
 │ ResNet-50   │          │ ResNet-50    │
 │ cabang RGB  │          │ cabang D     │
 └──┬──────────┘          └────┬─────────┘
    │ Conv, Layer1..4          │ Conv, Layer1..4
    ▼                          ▼
  [ACM]                      [ACM]
    │ A_rgb x V_rgb            │ A_d x V_d
    └────────────┬─────────────┘
                 ▼ jumlah per elemen
        ┌─────────────────────────┐
        │ cabang fusi: ResNet-50  │
        │ Conv      : jadi masukan│
        │ Layer1..4 : ditambahkan │
        └───────────┬─────────────┘
                    ▼
        decoder + skip connection
                    ▼
        peta label kelas per piksel

 cabang RGB dan cabang D tetap utuh hingga Layer4
```

Diagram di atas memperlihatkan bahwa ACM hanya menarik bobot dari cabang modalitas dan menyuntikkan fitur terbobot ke cabang fusi; tidak ada aliran balik yang mengubah isi cabang RGB atau kedalaman.

### Decoder dan Pelatihan

Tahap *upsampling* memakai *skip connection* (sambungan pintas yang menyalin fitur dari tahap *downsampling* ke tahap pemulihan resolusi yang setara) mengikuti pola RedNet, dengan biaya komputasi kecil. Jaringan menghasilkan lima keluaran pada lima resolusi (up1 hingga up5): saat pelatihan, *loss* dihitung sebagai rata-rata *loss* kelima keluaran agar gradien menjangkau seluruh tingkat; saat pengujian, hanya keluaran terakhir yang dinilai demi kesetaraan dengan metode pembanding.

Data latih diperkaya dengan penskalaan acak, pemotongan, dan pembalikan horizontal yang diterapkan serentak pada RGB dan kedalaman, ditambah perubahan warna acak pada ruang HSV khusus untuk RGB. Fungsi *loss* yang dipakai adalah *focal loss* dengan parameter fokus γ = 2, yakni modifikasi *cross-entropy* yang menurunkan bobot contoh yang sudah mudah diklasifikasikan — berguna karena sebagian besar piksel adegan dalam ruangan berasal dari sedikit kelas dominan seperti dinding dan lantai. Optimisasi memakai SGD (*stochastic gradient descent*) dengan laju pembelajaran awal 0,002, momentum 0,9, dan *weight decay* 0,004, pada satu GPU NVIDIA TITAN Xp dengan ukuran *batch* 4.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur standar segmentasi RGB-D dalam ruangan. NYUDv2 memuat 1.449 citra RGB-D beranotasi padat, dibagi 795 citra latih dan 654 citra uji sesuai pembagian resmi, dengan 40 kelas. SUN RGB-D V1 memuat 10.335 citra dalam 37 kelas, dibagi 5.285 citra latih dan 5.050 citra uji. Metrik yang dipakai adalah mIoU (*mean Intersection-over-Union*): untuk setiap kelas dihitung rasio luas irisan terhadap luas gabungan antara piksel prediksi dan piksel kebenaran, lalu dirata-ratakan ke seluruh kelas; maksimal 100%.

Hasil utama: dengan ResNet-50, ACNet mencapai mIoU 48,3% pada *test set* NYUDv2, melampaui metode terbaik sebelumnya dengan selisih 0,6 poin dan menetapkan rekor baru pada tolok ukur itu. Pada SUN RGB-D, ACNet mencapai mIoU yang sama dengan CFN yang berbasis RefineNet-152 — akurasi setara diperoleh dengan backbone 50 lapis alih-alih 152 lapis, sehingga beban komputasi jauh lebih kecil.

Studi ablasi pada NYUDv2 memisahkan kontribusi kedua komponen. Model-1, tanpa ACM dan tanpa cabang RGB/kedalaman setelah lapis Conv, memperoleh 44,3% mIoU. Model-2, yang mempertahankan arsitektur tiga cabang tetapi membuang seluruh ACM, memperoleh 46,8%. Model lengkap memperoleh 48,3%. Selisih Model-2 terhadap Model-1 (+2,5 poin) mengukur sumbangan arsitektur tiga cabang, dan selisih model lengkap terhadap Model-2 (+1,5 poin) mengukur sumbangan ACM; keduanya positif, tetapi arsitektur multi-cabang menyumbang kenaikan yang lebih besar daripada modul attention.

Analisis bobot ACM pada makalah memberi gambaran tambahan: rata-rata bobot RGB lebih tinggi pada Conv dan Layer1, konsisten dengan kaya-teksturnya citra RGB pada tingkat rendah; bobot kedua cabang hampir setara pada Layer2 hingga Layer4. Simpangan baku bobot menurun dari Conv ke Layer3 — distribusi informasi antarkanal diratakan — lalu melonjak pada Layer4, tahap terakhir *encoder* yang menyeleksi fitur berguna sekaligus membuang redundansi.

## Kelebihan dan Keterbatasan

Kelebihan ACNet bersifat struktural. Arsitektur tiga cabang mempertahankan aliran inferensi RGB dan kedalaman yang asli sekaligus memungkinkan fusi pada semua tingkat resolusi, mengatasi dua kelemahan arsitektur pendahulu yang diidentifikasi penulis. ACM memberi mekanisme adaptif isi: proporsi kontribusi modalitas ditentukan per kanal oleh data itu sendiri, bukan bobot tetap. Kenaikan akurasi didukung ablasi yang memisahkan kontribusi tiap komponen, dan kode sumber PyTorch beserta model terlatih dirilis terbuka.

Keterbatasannya: tiga ResNet-50 penuh berarti jumlah parameter dan operasi hampir tiga kali lipat model satu *encoder*, dan makalah tidak melaporkan waktu inferensi — penulis sendiri menyebut kinerja waktu nyata sebagai pekerjaan lanjutan. Bobot ACM dihitung dari fitur tiap modalitas secara terpisah, bukan dari gabungan keduanya, sehingga pembobotan tidak memodelkan interaksi langsung antarmodalitas. Dari sisi rekayasa, akurasi model bergantung pada kualitas citra kedalaman; lubang dan derau hasil penginderaan Kinect tidak ditangani secara khusus oleh metode ini. Secara konseptual, keunggulan 0,6 poin atas metode sebelumnya juga perlu dibaca bersama biaya komputasi yang lebih besar daripada pembanding satu atau dua *encoder*.

## Kaitan dengan Bab Lain

Secara silsilah, ACNet melanjutkan garis dua *encoder* yang dibahas pada [051 - FuseNet](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md) dan [052 - RedNet](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md); pola *skip connection* pada *decoder*-nya diwarisi langsung dari RedNet. ACNet bersaing dengan [053 - RDFNet](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md), yang menangani ketidakselarasan fitur antarmodalitas dengan konvolusi multi-modal. Mekanisme pembobotan adaptifnya membuka lini fusi berbasis attention yang diteruskan [055 - SA-Gate](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md) — gerbang timbal balik antarmodalitas — serta [056 - ESANet](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md) dan [058 - CMX](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) yang mengejar efisiensi dan generalisasi lintas-modalitas.

## Poin untuk Sitasi

Kutip dengan kunci `hu2019acnet`. Ringkasan yang aman dikutip: "ACNet menggabungkan fitur RGB dan kedalaman melalui arsitektur tiga cabang paralel berbasis ResNet dan modul attention kanal (ACM) yang menimbang kontribusi tiap modalitas secara adaptif, mencapai mIoU 48,3% pada NYUDv2 (40 kelas) dengan backbone ResNet-50." Seluruh angka di atas (48,3%; ablasi 44,3%/46,8%/48,3%; pembagian data 795/654 dan 5.285/5.050) berasal dari naskah arXiv 1905.10089. Dua klaim belum terverifikasi penuh dan wajib dicek ke tabel naskah sebelum sitasi formal: (1) angka mIoU pasti ACNet pada SUN RGB-D — teks hanya menyatakan setara dengan CFN tanpa nilai yang dapat diekstrak; (2) identitas metode yang dilampaui dengan selisih 0,6 poin pada NYUDv2.
