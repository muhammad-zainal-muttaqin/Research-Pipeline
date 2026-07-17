# 017 - Mask R-CNN

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `he2017maskrcnn` |
| Judul asli | Mask R-CNN |
| Penulis | Kaiming He, Georgia Gkioxari, Piotr Dollár, Ross Girshick |
| Tahun | 2017 |
| Venue | IEEE International Conference on Computer Vision (ICCV 2017), hlm. 2961–2969 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1703.06870
- **Google Scholar:** https://scholar.google.com/scholar?q=Mask%20R-CNN
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Mask%20R-CNN&sort=relevance
- **Kode sumber (Detectron):** https://github.com/facebookresearch/Detectron

## Gambaran Umum

Makalah ini memperkenalkan Mask R-CNN, kerangka untuk *instance segmentation* — tugas menemukan tiap objek dalam citra sekaligus menandai piksel milik tiap objek secara terpisah. Metodenya memperluas detektor dua tahap Faster R-CNN (bab 014) dengan satu cabang tambahan yang memprediksi mask biner untuk tiap kandidat objek, paralel dengan cabang klasifikasi kelas dan regresi *bounding box* yang sudah ada. Dua keputusan desain menjadi kunci akurasinya: lapisan RoIAlign yang menghilangkan kesalahan kesejajaran spasial akibat pembulatan koordinat pada RoIPool, dan prediksi mask per kelas yang dipisahkan dari prediksi kelas sehingga mask antarkelas tidak saling bersaing.

Tanpa rekayasa tambahan, Mask R-CNN melampaui seluruh model tunggal pemenang COCO 2016 pada tiga tugas sekaligus: segmentasi instans (37,1 AP mask), deteksi kotak (39,8 AP), dan estimasi pose manusia (63,1 AP *keypoint*), pada kecepatan sekitar 5 FPS (*frame* per detik).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek konvensional menghasilkan kotak pembatas tiap objek. Bagi aplikasi seperti robotika dan pemetaan, kotak saja tidak cukup: sistem memerlukan batas objek presisi tingkat piksel dan harus membedakan dua objek sekelas yang saling menempel. Tugas inilah *instance segmentation*, gabungan deteksi objek (menemukan tiap individu objek) dan segmentasi semantik (mengklasifikasikan tiap piksel tanpa membedakan individu).

Sebelum 2017, pendekatan dominan mendahulukan segmentasi: DeepMask mengusulkan kandidat potongan (*segment proposal*) yang kemudian diklasifikasikan; MNC dan FCIS (pemenang COCO 2015 dan 2016) menyusun tahapan prediksi potongan yang lebih rumit. Segmentasi yang mendahului pengenalan membuat sistem lambat atau menghasilkan galat sistematis pada objek yang saling tumpang tindih.

Masalah kedua bersifat teknis. Detektor dua tahap keluarga R-CNN (bab 012–014) mengekstrak fitur tiap kandidat wilayah dengan RoIPool, yang membulatkan koordinat wilayah ke kisi diskrit peta fitur. Pembulatan ini menimbulkan ketidaksejajaran (*misalignment*) antara wilayah objek dan fitur yang diekstrak. Klasifikasi toleran terhadap pergeseran kecil; prediksi mask yang menuntut ketepatan piksel demi piksel rusak olehnya. Mask R-CNN menjawab keduanya sekaligus.

## Ide Utama

Gagasan inti Mask R-CNN: pada tiap kandidat objek dari Faster R-CNN, tambahkan cabang ketiga yang memprediksi mask biner, paralel dengan cabang kelas dan cabang kotak yang sudah ada. Masukan cabang ini adalah fitur wilayah objek; keluarannya adalah mask kecil yang menyatakan piksel mana yang termasuk objek. Deteksi dan segmentasi diselesaikan satu jaringan dalam satu lintasan, bukan oleh dua sistem berurutan.

Dua prinsip melengkapi gagasan itu. Pertama, kesejajaran piksel harus dijaga: koordinat wilayah tidak boleh dibulatkan saat fitur diekstrak, sehingga mask benar-benar menempel pada posisi objek. Kedua, mask dan kelas dipisahkan: jaringan memprediksi satu mask biner per kelas tanpa kompetisi antarkelas, dan cabang klasifikasilah yang memutuskan mask kelas mana yang dipakai. Pemisahan ini berkebalikan dengan segmentasi semantik lazim yang memakai *softmax* per piksel, di mana piksel yang sama diperebutkan antarkelas.

## Cara Kerja Langkah demi Langkah

### Fondasi: Faster R-CNN dan RoIPool

Mask R-CNN mewarisi struktur dua tahap Faster R-CNN. Tahap pertama, *Region Proposal Network* (RPN), adalah jaringan konvolusi kecil yang mengusulkan kandidat kotak objek beserta skor *objectness* (peluang kotak memuat objek). Tahap kedua mengekstrak fitur tiap kandidat wilayah (*Region of Interest*, RoI) dari peta fitur citra, lalu mengklasifikasikan kelasnya dan meregresikan kotak yang lebih tepat. Kedua tahap berbagi peta fitur dari *backbone* ResNet atau ResNeXt berkedalaman 50 atau 101 lapis.

Operasi ekstraksi fitur RoI pada Faster R-CNN adalah RoIPool. Misalkan sebuah RoI berukuran 165×97 piksel pada citra dan peta fitur memiliki *stride* 16 (satu sel peta fitur mewakili 16×16 piksel citra). RoIPool mengubah koordinat kontinu x menjadi x/16 lalu membulatkannya ke bilangan bulat, membagi RoI menjadi kotak-kotak (*bin*) 7×7 yang juga dibulatkan ukurannya, kemudian mengambil nilai maksimum tiap kotak. Dua kali pembulatan ini menggeser batas wilayah hingga hampir satu sel peta fitur.

### RoIAlign: Ekstraksi Fitur Tanpa Kuantisasi

RoIAlign menggantikan RoIPool dengan satu perubahan prinsip: tidak ada pembulatan sama sekali, baik pada batas RoI, pembagian kotak, maupun titik pengambilan sampel — koordinat pecahan x/16 dipakai apa adanya. Pada tiap sel diambil empat titik sampel berjarak teratur. Nilai fitur pada tiap titik dihitung dengan interpolasi bilinear — rata-rata berbobot menurut jarak dari empat sel peta fitur terdekat — karena titik sampel umumnya jatuh di antara sel-sel diskrit. Nilai keempat titik dalam satu sel diagregasi dengan rata-rata atau maksimum. Hasilnya, fitur yang diekstrak selalu sejajar dengan posisi objek.

### Cabang Mask dan Representasi per Kelas

Cabang mask adalah jaringan konvolusi penuh (*Fully Convolutional Network*, FCN) kecil yang diterapkan pada fitur tiap RoI. Berbeda dengan lapis terhubung penuh yang meratakan fitur menjadi vektor dan menghilangkan struktur ruang, FCN mempertahankan susunan spasial m×m sepanjang cabang sehingga mask diprediksi piksel demi piksel. Pada arsitektur ber-FPN, cabang ini terdiri atas empat konvolusi 3×3 diikuti satu dekvolusi (konvolusi transposisi yang menaikkan resolusi spasial dua kali lipat), menghasilkan mask 28×28 untuk tiap kelas.

Untuk K kelas, cabang mengeluarkan K mask biner, bukan satu mask multi-kelas. Tiap piksel mask dilewatkan fungsi sigmoid — yang memetakan nilai apa pun ke rentang 0–1 secara independen per piksel — dan dilatih dengan *binary cross-entropy* (galat klasifikasi biner per piksel). Fungsi *loss* total tiap RoI adalah L = L_cls + L_box + L_mask, dengan L_cls (galat klasifikasi) dan L_box (galat regresi kotak) sama seperti Fast R-CNN. L_mask hanya dihitung pada mask ke-k, dengan k kelas kebenaran RoI tersebut; keluaran mask kelas lain tidak memberi gradien. Target mask adalah irisan antara RoI dan mask kebenaran. Saat inferensi, mask yang dipakai adalah mask ke-k dengan k dari cabang klasifikasi; mask 28×28 diubah ukurannya ke ukuran RoI lalu dibinerkan pada ambang 0,5.

### Arsitektur Lengkap dan Alur Inferensi

Mask R-CNN diuji dalam dua konfigurasi *backbone*. Konfigurasi pertama mengambil fitur dari tahap keempat ResNet (C4, *stride* 16). Konfigurasi kedua memakai *Feature Pyramid Network* (FPN, bab 018), piramida fitur multi-skala dengan koneksi lateral: RoI kecil diekstrak dari tingkat beresolusi tinggi, RoI besar dari tingkat rendah. Alur lengkap sistem:

```
citra masukan
     │
     ▼
┌─────────────────┐   peta fitur multi-skala
│ backbone ResNet │
│ /ResNeXt (+FPN) │
└───────┬─────────┘
        │                 ┌────────────────┐
        ├────────────────►│ RPN: usulan RoI│── kandidat kotak
        │                 └────────────────┘        │
        ▼                                           ▼
┌──────────────────────────────────────────────────────────┐
│ RoIAlign: fitur RoI tanpa kuantisasi (interp. bilinear)  │
└───┬───────────────────────┬───────────────────────┬──────┘
    ▼                       ▼                       ▼
┌─────────┐           ┌─────────┐           ┌──────────────┐
│ cabang  │           │ cabang  │           │ cabang mask  │
│ kelas   │           │ kotak   │           │ FCN: K mask  │
│ (fc)    │           │ (fc)    │           │ m×m, sigmoid │
└────┬────┘           └────┬────┘           └──────┬───────┘
     └──────────┬──────────┴───────────────────────┘
                ▼
   kelas + box + mask per instans (mask kelas k dipilih
   oleh hasil klasifikasi; di-resize ke ukuran RoI)
```

Saat inferensi, RPN menghasilkan 300 usulan (C4) atau 1000 usulan (FPN). Cabang kotak dijalankan pada semua usulan, lalu *Non-Maximum Suppression* (NMS) membuang kotak berlebih yang saling menutupi. Cabang mask hanya dijalankan pada 100 deteksi berskor tertinggi, sehingga hanya menambah sekitar 20% waktu komputasi dibanding Faster R-CNN. Pada pelatihan, sisi pendek citra diubah menjadi 800 piksel; tiap citra mengambil 64 RoI (C4) atau 512 RoI (FPN) dengan rasio positif:negatif 1:3; RoI positif berarti IoU-nya terhadap kotak kebenaran minimal 0,5. IoU (*Intersection over Union*) adalah rasio luas irisan terhadap luas gabungan dua kotak.

### Perluasan ke Estimasi Pose

Kerangka yang sama dipakai untuk deteksi *keypoint* manusia (titik sendi tubuh) dengan memodelkan tiap keypoint sebagai mask *one-hot*: mask biner m×m yang hanya satu pikselnya aktif. Mask R-CNN memprediksi K mask, satu per jenis keypoint, dengan kepala delapan konvolusi 3×3 diikuti dekvolusi hingga resolusi keluaran 56×56 — lebih tinggi dari mask objek karena posisi sendi menuntut ketelitian lokasi lebih halus. Tidak ada pemodelan struktur tubuh khusus; yang berubah hanya definisi target mask.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada dataset COCO (80 kategori), dilatih pada 115 ribu citra latih (*trainval35k*) dan dilaporkan pada 5 ribu citra validasi (*minival*) serta *test-dev*. Metriknya AP COCO: rata-rata presisi pada berbagai ambang IoU, dihitung atas IoU mask untuk segmentasi dan IoU kotak untuk deteksi.

Hasil utama pada *test-dev*: Mask R-CNN dengan ResNet-101-FPN mencapai 35,7 AP mask pada 5 FPS; dengan ResNeXt-101-FPN mencapai 37,1 AP mask dan 39,8 AP kotak. Angka 37,1 melampaui FCIS+++, pemenang segmentasi COCO 2016 yang memakai lebih banyak rekayasa tambahan. Selisih AP mask dan AP kotak pada model yang sama hanya 2,7 poin (37,1 vs 39,8), diinterpretasikan penulis sebagai bukti bahwa kerangka ini hampir menutup jarak antara deteksi kotak dan segmentasi instans.

Eksperimen ablasi (mengubah satu komponen sekali jalan) mengukur kontribusi tiap keputusan desain:

- **RoIAlign.** Pada ResNet-50-C4, mengganti RoIPool dengan RoIAlign menaikkan AP mask dari 26,9 menjadi 30,3, dengan kenaikan terbesar pada metrik ketat AP75 (26,4 menjadi 31,5). Artinya perbaikan terutama terjadi pada prediksi yang menuntut lokalisasi presisi. Pada fitur *stride* 32, di mana ketidaksejajaran lebih parah, RoIAlign menaikkan AP mask 7,3 poin dan AP75 10,5 poin (perbaikan relatif 50%). RoIWarp dari MNC, yang tetap membulatkan batas RoI, hanya mencapai 27,1–27,2, setara RoIPool.
- **Mask terpisah dari kelas.** Sigmoid per kelas mengungguli *softmax* multi-kelas dengan selisih 5,5 poin AP mask. Varian agnostik-kelas (satu mask untuk semua kelas) hanya turun tipis ke 29,7 dari 30,3 — bukti lanjutan bahwa pembagian kerja klasifikasi-segmentasi berjalan.
- **FCN sebagai cabang mask.** Mengganti FCN dengan lapis terhubung penuh menurunkan AP mask 2,1 poin, mendukung keputusan mempertahankan struktur spasial.

Pada deteksi kotak, RoIAlign menyumbang +1,1 AP dan pelatihan multi-tugas +0,9 AP terhadap Faster R-CNN ber-FPN — menambahkan tugas mask justru memperbaiki deteksi. Model ResNet-101-FPN berjalan 195 milidetik per citra pada GPU Nvidia Tesla M40 (5 FPS); varian C4 sekitar 400 milidetik karena kepala jaringannya lebih berat.

Pada tugas *keypoint* COCO, Mask R-CNN (ResNet-50-FPN) mencapai 62,7 AP — 0,9 poin di atas pemenang kompetisi 2016 — dan naik menjadi 63,1 bila cabang mask diikutsertakan. RoIAlign menaikkan AP *keypoint* 4,4 poin, konsisten dengan kepekaan tugas ini terhadap ketelitian lokasi. Pada dataset Cityscapes, Mask R-CNN mencapai 26,2 AP hanya dengan data anotasi halus (naik lebih dari 30% relatif dari pembanding terbaik sebelumnya) dan 32,0 AP bila diinisialisasi dari model COCO.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah kesederhanaan yang terbukti kuat: satu kerangka dua tahap menangani deteksi, segmentasi instans, dan pose dengan hasil terbaik di masanya, dan tiap keputusan desainnya dibuktikan oleh ablasi. Ketiga tim pemenang kompetisi segmentasi instans COCO 2017 membangun sistemnya di atas kerangka ini.

Keterbatasannya: (1) sebagai detektor dua tahap, kecepatannya (±5 FPS) jauh di bawah detektor satu tahap seperti YOLO (45 FPS pada bab 001) — dari sisi rekayasa, desainnya memang tidak dioptimalkan untuk kecepatan, sebagaimana diakui penulis; (2) mask diprediksi per RoI secara lokal, sehingga objek yang terpotong kotak proposal akan terpotong pula masknya — secara konseptual, kualitas mask bergantung penuh pada kualitas proposal; (3) pelatihan menuntut anotasi mask tingkat piksel, yang jauh lebih mahal daripada anotasi kotak; (4) penambahan cabang *keypoint* sedikit menurunkan AP kotak dan mask pada pelatihan gabungan, menunjukkan transfer multi-tugas tidak selalu simetris.

## Kaitan dengan Bab Lain

Bab ini meneruskan garis keluarga R-CNN: [bab 012](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md) memperkenalkan deteksi berbasis wilayah, [bab 013](./013%20-%202015%20-%20Fast%20R-CNN%20-%20Fondasi%20RGB.md) mempercepatnya dengan berbagi konvolusi dan RoIPool, dan [bab 014](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md) melengkapinya dengan RPN — ketiganya fondasi yang diperluas Mask R-CNN dengan satu cabang. Penggunaan FPN menghubungkan bab ini dengan [bab 018](./018%20-%202017%20-%20Feature%20Pyramid%20Networks%20%28FPN%29%20-%20Fondasi%20RGB.md). Posisinya kontras dengan paradigma satu tahap pada [bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) dan [bab 016](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md): Mask R-CNN mengutamakan akurasi dan keluwesan tugas, keduanya mengutamakan kecepatan. Dalam tinjauan ini, Mask R-CNN juga menjadi komponen pemberi mask objek pada pipeline RGB-D dan SLAM dinamis di klaster aplikatif.

## Poin untuk Sitasi

Kutip dengan kunci `he2017maskrcnn`. Ringkasan yang aman dikutip: "Mask R-CNN memperluas Faster R-CNN dengan cabang prediksi mask paralel dan lapisan RoIAlign bebas kuantisasi, mencapai 37,1 AP mask pada COCO *test-dev* dan melampaui pemenang COCO 2016 pada segmentasi instans, deteksi kotak, dan deteksi *keypoint*, dengan kecepatan sekitar 5 FPS." Seluruh angka pada bab ini diverifikasi dari naskah arXiv v3; untuk sitasi formal, cocokkan kembali dengan tabel versi prosiding ICCV karena penomoran hasil dapat berbeda tipis antarversi.
