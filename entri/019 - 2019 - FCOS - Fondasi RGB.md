# 019 - FCOS: Fully Convolutional One-Stage Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tian2019fcos` |
| Judul asli | FCOS: Fully Convolutional One-Stage Object Detection |
| Penulis | Zhi Tian, Chunhua Shen, Hao Chen, Tong He |
| Tahun | 2019 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV 2019) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1904.01355
- **Kode sumber resmi:** https://github.com/tianzhi0549/FCOS
- **Google Scholar:** https://scholar.google.com/scholar?q=FCOS%3A%20Fully%20Convolutional%20One-Stage%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=FCOS%3A%20Fully%20Convolutional%20One-Stage%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan FCOS (*Fully Convolutional One-Stage*), detektor objek satu tahap yang menghapus *anchor box* (kotak acuan berukuran dan berrasio tetap yang menjadi titik tolak regresi pada Faster R-CNN, SSD, dan RetinaNet). Deteksi dirumuskan sebagai prediksi per piksel, meniru kerangka segmentasi semantik: setiap lokasi peta fitur yang jatuh di dalam sebuah objek memprediksi kelas objek itu dan empat jarak dari lokasi ke keempat sisi kotak pembatas (*bounding box*). Dua mekanisme melengkapinya: prediksi multi-tingkat di atas FPN (*Feature Pyramid Network*, jaringan piramida fitur multi-skala) untuk memisahkan objek yang tumpang tindih, dan cabang *centerness* satu lapis yang menekan skor kotak dari lokasi jauh dari pusat objek.

Dengan *backbone* (jaringan pengekstrak fitur utama) ResNeXt-64x4d-101, FCOS mencapai 44,7% AP pada COCO *test-dev*, melampaui detektor satu tahap sebelumnya dengan desain lebih sederhana: tanpa *anchor*, tanpa *region proposal*, dan pasca-pemrosesan hanya NMS. Hasil ini membantah anggapan bahwa *anchor* wajib bagi detektor akurat dan menjadi fondasi desain *anchor-free* generasi berikutnya, termasuk YOLOX.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak Faster R-CNN (bab 014), hampir semua detektor arus utama — SSD (bab 015), RetinaNet (bab 016), YOLOv2 (bab 002), dan YOLOv3 (bab 003) — bergantung pada *anchor box* yang disebar rapat pada citra sebagai titik tolak klasifikasi dan regresi kotak. Desain ini membawa empat masalah. Pertama, kinerja sensitif terhadap hiperparameter *anchor*: pada RetinaNet, mengubah jumlah, skala, atau rasionya menggeser AP hingga 4 poin pada COCO. Kedua, skala-rasio tetap menyulitkan objek bervariasi bentuk, terutama objek kecil, dan memaksa perancangan ulang saat berpindah dataset. Ketiga, demi *recall* (proporsi objek yang berhasil ditemukan) tinggi, *anchor* disebar sangat rapat — lebih dari 180 ribu kotak per citra bersisi pendek 800 piksel pada FPN — dan hampir semuanya menjadi sampel negatif, memperparah ketidakseimbangan sampel. Keempat, pelatihan menuntut perhitungan IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak) antara setiap *anchor* dan setiap kotak kebenaran — komputasi yang murni biaya tambahan desain ber-*anchor*.

Upaya melepaskan *anchor* sudah ada tetapi belum memuaskan. YOLOv1 (bab 001) memprediksi kotak langsung dari sel *grid*, tetapi *recall*-nya rendah karena hanya lokasi dekat pusat objek yang dipakai, sehingga YOLOv2 kembali memakai *anchor*. Detektor per piksel seperti DenseBox memprediksi empat jarak ke sisi kotak dari setiap lokasi, tetapi dianggap gagal pada deteksi generik: bila dua kotak objek tumpang tindih, lokasi di daerah irisan tidak jelas harus meregresi kotak yang mana. CornerNet mendeteksi pasangan sudut kotak, tetapi memerlukan pasca-pemrosesan pengelompokan yang rumit. FCOS menunjukkan keberatan *recall* rendah dan ambiguitas tumpang tindih dapat diselesaikan tanpa *anchor*.

## Ide Utama

Gagasan inti FCOS: jadikan **lokasi**, bukan kotak acuan, sebagai sampel pelatihan. Setiap lokasi peta fitur dipetakan ke posisi tertentu pada citra; bila posisi itu jatuh di dalam sebuah kotak kebenaran (*ground truth*), lokasi tersebut menjadi sampel positif dan bertugas dua hal: memprediksi kelas objeknya, dan meregresikan empat bilangan positif (l, t, r, b) — jarak dari lokasi ke sisi kiri, atas, kanan, dan bawah kotak. Kotak prediksi direkonstruksi dari keempat jarak dan posisi lokasi, tanpa bentuk kotak yang perlu dirancang sebelumnya.

Dua pelengkap diperlukan: prediksi multi-tingkat FPN memisahkan lokasi ambigu di daerah tumpang tindih berdasarkan ukuran objek, dan cabang *centerness* menekan skor kotak dari lokasi jauh dari pusat objek agar tersingkir oleh NMS saat inferensi.

## Cara Kerja Langkah demi Langkah

### Formulasi Prediksi per Piksel

Misalkan peta fitur suatu tingkat memiliki *stride* total s terhadap citra masukan (*stride* = faktor pengecilan resolusi; *stride* 8 berarti satu sel mewakili 8×8 piksel citra). Lokasi (x, y) pada peta fitur berkorespondensi dengan titik (⌊s/2⌋ + x·s, ⌊s/2⌋ + y·s) pada citra, yaitu posisi dekat pusat *receptive field* (wilayah citra yang memengaruhi nilai fitur) lokasi itu. FCOS langsung meregresi kotak target dari titiknya, tanpa kotak acuan. Sebuah lokasi menjadi sampel positif bila titik korespondensinya jatuh di dalam kotak kebenaran mana pun, dengan label kelas kotak tersebut; lokasi di luar semua kotak menjadi sampel negatif (kelas latar). Untuk kotak berpojok kiri-atas (x0, y0) dan pojok kanan-bawah (x1, y1), target regresinya empat jarak: l* = x − x0, t* = y − y0, r* = x1 − x, b* = y1 − y. Contoh numerik: lokasi (100, 120) di dalam kotak berpojok (60, 40) dan (220, 200) memiliki target (40, 80, 120, 80). Nilai target selalu positif, sehingga cabang regresi diakhiri fungsi eksponensial. Bila satu lokasi jatuh di dalam dua kotak sekaligus (sampel ambigu), kotak berluas terkecil dipilih sebagai targetnya. Dengan satu kotak per lokasi, variabel keluaran FCOS 9 kali lebih sedikit daripada detektor dengan 9 *anchor* per lokasi.

Ilustrasi target regresi untuk satu lokasi:

```
  (x0,y0) ┌────────────────────┐
          │         t          │
          │         │          │
          │   l ── (x,y) ── r  │
          │         │          │
          │         b          │
          └────────────────────┘ (x1,y1)
```

Keempat panah adalah bilangan yang diprediksi jaringan untuk lokasi (x, y); kotak prediksi diperoleh dengan membalik persamaan target, misalnya sisi kiri terletak pada x − l.

### Arsitektur: Backbone, FPN, dan Head Bersama

Alur data jaringan:

```
citra masukan (sisi pendek 800, sisi panjang <= 1333)
   │
   ▼
backbone CNN (ResNet-50) -> peta fitur C3, C4, C5
   │
   ▼
FPN: konvolusi 1x1 + koneksi top-down;
P6, P7 dibentuk dari konvolusi stride-2 pada P5 dan P6
   │
   ▼
P3(/8)   P4(/16)   P5(/32)   P6(/64)   P7(/128)
   │  (semua tingkat melewati head yang sama)
   ▼
head: 4 lapis konvolusi per cabang, tiga keluaran
 ├─ klasifikasi -> 80 skor kelas (focal loss)
 ├─ regresi     -> (l, t, r, b), diaktivasi exp(si.x)
 └─ centerness  -> 1 skor pada [0,1] (BCE)
```

FPN (bab 018) menghasilkan lima tingkat fitur P3–P7 dengan *stride* 8 hingga 128: tingkat beresolusi tinggi menangani objek kecil, tingkat beresolusi rendah objek besar. Head deteksi dibagi (*shared*) oleh semua tingkat agar hemat parameter; mengikuti RetinaNet, tiap cabang terdiri atas empat lapis konvolusi dengan *Group Normalization* (normalisasi per kelompok kanal), dan klasifikasi dilatih sebagai 80 pengklasifikasi biner (satu per kelas COCO). Karena head yang sama melayani rentang jarak berbeda per tingkat, aktivasi regresi memakai exp(si · x) dengan skalar si yang ikut dilatih per tingkat, menggantikan exp(x) baku.

### Pembagian Rentang Ukuran antar Tingkat

Penetapan objek ke tingkat tidak memakai *anchor*, melainkan pembatasan langsung pada target regresi: lokasi pada tingkat ke-i hanya meregresi bila max(l*, t*, r*, b*) berada pada rentang tingkat itu; batasnya 0, 64, 128, 256, 512, dan tak hingga untuk P3–P7, dan lokasi di luar rentang menjadi sampel negatif. Contoh: lokasi dengan jarak sisi terjauh 50 piksel hanya diregresi oleh P3 (rentang 0–64), sedangkan lokasi dengan jarak 200 piksel hanya oleh P5 (rentang 128–256). Karena tumpang tindih umumnya terjadi antarobjek yang jauh berbeda ukurannya, sebagian besar kasus ambigu terpisah ke tingkat berbeda.

### Cabang Centerness

Prediksi multi-tingkat menyisakan satu galat: lokasi jauh dari pusat objek menghasilkan kotak ber-IoU rendah yang skor kelasnya bisa tetap tinggi sehingga lolos sebagai *false positive*. FCOS menambahkan cabang satu lapis, sejajar dengan cabang klasifikasi, yang memprediksi *centerness* — ukuran kedekatan lokasi terhadap pusat objeknya. Targetnya √( min(l,r)/max(l,r) × min(t,b)/max(t,b) ) bernilai 1 di pusat dan meluruh ke 0 di tepi; akar kuadrat menjaga peluruhan tidak terlalu cepat. Pada contoh numerik sebelumnya, centerness = √(40/120 × 80/80) ≈ 0,58. Target pada rentang [0,1] ini dilatih dengan *binary cross-entropy* (BCE). Saat inferensi, skor akhir setiap kotak adalah skor kelas dikalikan *centerness* prediksi, sehingga kotak dari lokasi pinggir tertekan skornya dan berpeluang besar dibuang oleh NMS (*Non-Maximum Suppression*, prosedur yang mempertahankan hanya kotak berskor tertinggi di antara kotak yang saling menutupi).

### Pelatihan dan Inferensi

Fungsi *loss* terdiri atas *focal loss* (*loss* dari RetinaNet, bab 016, yang menekan kontribusi sampel mudah agar sampel negatif tidak mendominasi) untuk klasifikasi, *IoU loss* ala UnitBox (mengoptimalkan IoU kotak prediksi secara langsung) untuk regresi, dan BCE untuk *centerness*, dengan bobot penyeimbang 1. Jaringan dilatih dengan SGD 90 ribu iterasi, laju pembelajaran 0,01 (diturunkan sepersepuluh pada iterasi ke-60 dan ke-80 ribu), *batch* 16 citra, dan bobot awal *backbone* dari ImageNet. Inferensi cukup satu umpan-maju: lokasi dengan skor di atas 0,05 dipertahankan, persamaan regresi dibalik menjadi koordinat kotak, lalu NMS merampingkan hasilnya.

## Eksperimen dan Hasil

Seluruh eksperimen memakai COCO: pelatihan pada 115 ribu citra, ablasi pada split *minival* (5 ribu), hasil utama pada *test-dev* (20 ribu); metriknya AP (*Average Precision* versi COCO, rata-rata presisi pada sepuluh ambang IoU 0,50–0,95). Soal *recall*: batas atas *recall* (BPR) FCOS 95,55% dengan satu tingkat fitur dan 98,40% dengan FPN — hampir menyamai batas terbaik RetinaNet (99,23%) dan jauh di atas implementasi resminya (90,92%); selisih ini tidak berdampak karena *recall* aktual detektor saat itu di bawah 90%. Soal ambiguitas: sampel ambigu turun dari 23,16% tanpa FPN menjadi 7,14% dengan FPN (3,75% untuk irisan antar kelas berbeda), dan hanya 2,3% kotak terdeteksi yang berasal dari lokasi ambigu.

Ablasi *centerness* pada *minival* (backbone ResNet-50) menaikkan AP dari 33,5% menjadi 37,1% — lonjakan 3,6 poin dari satu lapis tambahan; *centerness* yang dihitung analitis dari vektor regresi tidak memberi kenaikan (tetap 33,5%), sehingga cabang khusus memang diperlukan. Pada pengaturan persis sama dengan RetinaNet, FCOS unggul tipis 36,3% berbanding 35,9% AP.

Pada *test-dev*, dengan *backbone* sama (ResNet-101-FPN), FCOS mencapai 41,5% AP, 2,4 poin di atas RetinaNet (39,1%) dan di atas CornerNet (40,5%). Dengan ResNeXt-64x4d-101-FPN dicapai 43,2% AP, dan versi berpenyempurnaan pasca-submisi (*centerness* di cabang regresi, sampel daerah pusat, GIoU, normalisasi target) mencapai 44,7% AP, terbaik di antara detektor satu tahap saat itu. Sebagai pengganti RPN pada Faster R-CNN, FCOS menaikkan AR100 dari 44,7% menjadi 52,8% dan AR1k dari 56,9% menjadi 60,3%, bukti gagasannya berlaku pula untuk detektor dua tahap.

## Kelebihan dan Keterbatasan

Kelebihan: (1) seluruh hiperparameter dan komputasi terkait *anchor* hilang — desain dan pelatihan lebih sederhana, jejak memori lebih kecil; (2) semua lokasi latar-depan menjadi sampel regresi, jauh lebih banyak daripada sampel positif hasil pencocokan IoU *anchor*, yang diduga menjadi salah satu sumber keunggulan akurasi; (3) akurasi melampaui pembanding ber-*anchor* pada pengaturan setara; (4) kerangka per piksel menyatukan deteksi dengan tugas prediksi rapat lain dan mudah dipindahkan ke segmentasi instans atau menjadi pengganti RPN.

Keterbatasan: (1) aturan luas-terkecil pada lokasi ambigu berisiko membuat objek besar yang tumpang tindih terlewat, sebagaimana diakui makalah; (2) NMS tetap diperlukan sebagai pasca-pemrosesan; (3) dari sisi rekayasa, batas rentang regresi per tingkat (0, 64, 128, 256, 512) tetap konstanta desain yang bergantung pada distribusi ukuran dataset — fungsinya menyerupai skala *anchor*, meski lebih sedikit dan tanpa pencocokan IoU; (4) secara konseptual, kualitas deteksi masih bertumpu pada FPN, sehingga kompleksitas *neck* piramida tidak ikut hilang bersama *anchor*.

## Kaitan dengan Bab Lain

FCOS berdiri di atas dua fondasi: piramida fitur dari [018 - Feature Pyramid Networks (FPN)](./018%20-%202017%20-%20Feature%20Pyramid%20Networks%20%28FPN%29%20-%20Fondasi%20RGB.md) yang memasok tingkat P3–P7, dan *focal loss* dari [016 - RetinaNet (Focal Loss)](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md) — pembanding langsung yang dikalahkan FCOS pada backbone setara. Terhadap [001 - You Only Look Once (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), FCOS menuntaskan gagasan prediksi tanpa *anchor* yang sebelumnya gagal karena *recall* rendah. Pengaruh terbesarnya mengalir ke [005 - YOLOX](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md), yang mengadopsi formulasi *anchor-free* per piksel ini ke dalam keluarga YOLO (diteruskan ke bab 006–009). Jalur *anchor-free* alternatif pada masa yang sama dibahas pada [020 - CenterNet (Objects as Points)](./020%20-%202019%20-%20CenterNet%20%28Objects%20as%20Points%29%20-%20Fondasi%20RGB.md), yang merepresentasikan objek sebagai titik pusat, bukan jarak ke empat sisi.

## Poin untuk Sitasi

Kutip dengan kunci `tian2019fcos`. Ringkasan yang aman dikutip: "FCOS merumuskan deteksi objek sebagai prediksi per piksel tanpa *anchor* dan tanpa *proposal*: setiap lokasi di dalam kotak objek meregresi empat jarak ke sisi kotak, dibantu prediksi multi-tingkat FPN dan cabang *centerness* yang menekan kotak berkualitas rendah. Pada COCO *test-dev*, FCOS mengungguli RetinaNet ber-*backbone* setara (41,5% berbanding 39,1% AP) dan mencapai 44,7% AP dengan ResNeXt-64x4d-101." Catatan verifikasi: angka 44,7% berasal dari baris *improvements* pada revisi arXiv (penyempurnaan pasca-submisi), bukan konfigurasi dasar; rincian ablasi (BPR 98,40%, ambiguitas 3,75%, lonjakan *centerness* 33,5→37,1) dikutip dari arXiv v5 dan sebaiknya dicocokkan dengan versi prosiding ICCV sebelum sitasi formal.
