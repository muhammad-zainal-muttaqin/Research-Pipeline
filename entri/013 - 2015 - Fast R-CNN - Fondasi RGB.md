# 013 - Fast R-CNN

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `girshick2015fastrcnn` |
| Judul asli | Fast R-CNN |
| Penulis | Ross Girshick |
| Tahun | 2015 |
| Venue | IEEE International Conference on Computer Vision (ICCV 2015) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1504.08083
- **Kode sumber (lisensi MIT, Python/C++ dengan Caffe):** https://github.com/rbgirshick/fast-rcnn
- **Google Scholar:** https://scholar.google.com/scholar?q=Fast%20R-CNN
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Fast%20R-CNN&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Fast R-CNN (*Fast Region-based Convolutional Network*), detektor objek karya Ross Girshick pada ICCV 2015. Gagasan utamanya: peta fitur konvolusi dihitung satu kali untuk seluruh citra, fitur setiap usulan wilayah (*proposal*) diekstrak dari peta itu melalui lapis *RoI pooling*, dan satu jaringan berkepala ganda — klasifikasi *softmax* dan regresi kotak — dilatih dalam satu tahap memakai *multi-task loss*. Rumusan ini menghapus pelatihan tiga tahap dan ekstraksi fitur per proposal yang membuat pendahulunya, R-CNN dan SPPnet, lambat serta boros penyimpanan.

Hasilnya: pelatihan VGG16 sekitar 9 kali lebih cepat daripada R-CNN, pengujian 213 kali lebih cepat, dengan akurasi lebih tinggi — 70,0% mAP pada PASCAL VOC 2007 dengan data latih gabungan, dibandingkan 66,0% pada R-CNN. Arsitektur ini menjadi cetak biru detektor dua tahap berikutnya; Faster R-CNN dan Mask R-CNN dibangun langsung di atasnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, detektor paling akurat adalah R-CNN (dibahas pada [bab 012](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md)). R-CNN bekerja dalam dua tahap: algoritme *selective search* mengusulkan sekitar 2.000 kandidat wilayah citra (*region proposal*, potongan segi empat yang mungkin berisi objek), kemudian setiap wilayah diubah ukurannya dan diproses satu per satu oleh jaringan saraf konvolusi (CNN), diklasifikasikan oleh SVM (*support vector machine*, pengklasifikasi yang dilatih terpisah), lalu posisinya diperbaiki regresor kotak.

Makalah ini mencatat tiga kelemahan R-CNN. Pertama, pelatihannya multi-tahap — CNN, SVM, dan regresor dilatih terpisah tanpa saling mengoptimalkan. Kedua, mahal dalam waktu dan ruang: fitur setiap proposal ditulis ke disk, memakan 2,5 hari-GPU untuk 5 ribu citra latih VOC07 dan ratusan gigabita penyimpanan. Ketiga, deteksi lambat: 47 detik per citra dengan VGG16, karena setiap proposal memicu satu *forward pass* CNN tanpa berbagi komputasi.

SPPnet (*Spatial Pyramid Pooling network*) mempercepat R-CNN 10–100 kali dengan menghitung peta fitur konvolusi sekali untuk seluruh citra; fitur tiap proposal diekstrak lewat *spatial pyramid pooling*, pembagian wilayah fitur ke beberapa tingkat kisi tetap yang di-*max-pooling* lalu digabung. Namun SPPnet tetap dilatih multi-tahap, tetap menulis fitur ke disk, dan penyetelan halusnya tidak dapat memperbarui lapis konvolusi di bawah lapis SPP — keterbatasan yang menahan akurasi jaringan dalam, dan menjadi celah yang diisi Fast R-CNN.

## Ide Utama

Gagasan inti Fast R-CNN adalah memindahkan proposal dari ruang piksel ke ruang fitur. Alih-alih memotong dan memproses ulang setiap proposal sebagai citra terpisah, citra utuh dilewatkan melalui lapis konvolusi satu kali; setiap proposal kemudian cukup dibaca dari peta fitur hasilnya. Karena proposal yang tumpang tindih menutupi wilayah citra yang sama, komputasi konvolusi tidak pernah diulang.

Secara mekanis, masukan jaringan adalah satu citra dan daftar proposalnya; keluaran tiap proposal berupa dua hal sekaligus: distribusi probabilitas atas K kelas objek plus satu kelas latar, dan empat angka koreksi kotak untuk setiap kelas. Kedua tugas dilatih bersama dengan satu fungsi loss, sehingga seluruh jaringan — termasuk semua lapis konvolusi — diperbarui dalam satu tahap. Tidak ada lagi SVM terpisah, tidak ada lagi berkas fitur di disk.

## Cara Kerja Langkah demi Langkah

### Arsitektur Keseluruhan

Alur data Fast R-CNN dari masukan ke keluaran digambarkan sebagai berikut:

```
MASUKAN: 1 citra utuh (sisi pendek 600 piksel) + sekitar 2000 proposal

   citra ──> ┌──────────────────────────┐
              │ konvolusi VGG16          │  peta fitur dihitung
              │ 13 conv + 5 max pooling  │  SATU KALI per citra
              └────────────┬─────────────┘
                           v
              peta fitur conv, stride 16
              (citra 600x1000 -> 37x62 x 512 kanal)
                           |
   proposal (r,c,h,w) ──> proyeksi jendela h x w
                           v
              ┌──────────────────────────┐
              │ RoI pooling              │  per proposal:
              │ jendela dibagi grid 7x7, │  fitur ukuran tetap
              │ max pooling tiap sel     │  7x7x512
              └────────────┬─────────────┘
                           v
                fc6 (4096) -> fc7 (4096)
                       ┌───┴───┐
                       v       v
                softmax     regresi kotak:
                K+1 kelas   4 offset per kelas
                (VOC: 21)   (tx, ty, tw, th)
```

Citra masukan diskalakan agar sisi pendeknya 600 piksel (sisi panjang maksimal 1000) — satu skala tunggal, tanpa piramida citra. Pada VGG16, lima lapis *max pooling* (pengambilan nilai maksimum dalam jendela kecil, yang mereduksi resolusi spasial) menghasilkan *stride* total 16, sehingga citra 600×1000 piksel menjadi peta fitur sekitar 37×62 posisi dengan 512 kanal. Setiap proposal dinyatakan sebagai jendela (r, c, h, w) — pojok kiri atas, tinggi, lebar — yang diproyeksikan ke peta fitur ini, lalu diproses seperti pada diagram.

### Lapis RoI Pooling

*RoI pooling* (*Region of Interest pooling*) mengubah jendela fitur berukuran sembarang menjadi fitur berukuran tetap. Jendela h×w dibagi kisi H×W sel (untuk VGG16, H = W = 7), lalu nilai maksimum setiap sel diambil per kanal. Contoh numerik: proposal 256×256 piksel menjadi jendela 16×16 pada peta fitur (karena stride 16); jendela itu dibagi kisi 7×7 sehingga tiap sel mencakup sekitar 2×2 posisi; *max pooling* tiap sel menghasilkan keluaran 7×7 per kanal, atau 7×7×512 — berapa pun ukuran proposal awalnya. Lapis ini adalah kasus khusus *spatial pyramid pooling* dengan satu tingkat piramida. Bedanya dari SPPnet: gradien dialirkan balik menembus lapis ini dengan mengikuti posisi argmax saat *max pooling*, diakumulasikan untuk semua proposal, sehingga lapis konvolusi di bawahnya ikut belajar.

### Inisialisasi dari Jaringan Praterlatih

Fast R-CNN tidak dilatih dari nol. Tiga jaringan ImageNet menjadi titik awal: CaffeNet (varian AlexNet, model S), VGG_CNN_M_1024 (model M), dan VGG16 (model L). Setiap jaringan dimodifikasi tiga kali: lapis *max pooling* terakhir diganti lapis *RoI pooling*; lapis *fully connected* (terhubung penuh) dan *softmax* klasifikasi ImageNet 1000 kelas diganti dua kepala baru — *softmax* K+1 kelas dan regresor kotak per kelas; dan jaringan diubah agar menerima dua masukan, citra dan daftar proposalnya.

### Loss Multi-Tugas

Setiap proposal latih berlabel kelas u (u = 0 untuk latar) dan target regresi v. Loss per proposal adalah L = L_cls + λ·[u ≥ 1]·L_loc. Komponen L_cls adalah *log loss* −log p_u, negatif logaritma probabilitas *softmax* pada kelas benar. Komponen L_loc hanya aktif untuk proposal objek (penanda [u ≥ 1] bernilai 1 bila dipenuhi), menjumlahkan selisih offset prediksi dan target pada keempat koordinat dengan *smooth L1*: fungsi bernilai 0,5x² bila |x| < 1 dan |x| − 0,5 bila tidak. Bentuk kuadrat-linear ini lebih tahan pencilan daripada loss kuadrat milik R-CNN, sehingga gradien tidak mudah meledak. Offset berparameterkan geser skala-invarian untuk pusat dan geser logaritmik untuk lebar-tinggi. Semua eksperimen memakai λ = 1 dengan target dinormalisasi ke rerata nol dan variansi satu.

### Pengambilan Mini-Batch dan Pelatihan

Efisiensi pelatihan berasal dari pengambilan contoh berjenjang. Setiap *mini-batch* SGD (*stochastic gradient descent*) berisi R = 128 proposal dari hanya N = 2 citra, 64 proposal per citra. Proposal secitra berbagi komputasi dan memori pada *forward* dan *backward pass*, sehingga skema ini sekitar 64 kali lebih cepat daripada mengambil satu proposal dari 128 citra berbeda — strategi R-CNN dan SPPnet. Seperempat proposal adalah contoh objek, yaitu yang irisan dengan kotak kebenaran memiliki IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan dua kotak) minimal 0,5; sisanya contoh latar dengan IoU maksimum antara 0,1 dan 0,5 — batas 0,1 berperan sebagai heuristik penambangan contoh sulit. Augmentasi hanya pembalikan horizontal dengan peluang 0,5. Pelatihan berjalan 30 ribu iterasi dengan laju 0,001, dilanjutkan 10 ribu iterasi dengan 0,0001.

### Deteksi dan Akselerasi SVD

Saat pengujian, sekitar 2.000 proposal per citra dinilai dalam satu *forward pass*, lalu *Non-Maximum Suppression* (NMS — pembuangan kotak ganda yang saling menutupi, mempertahankan yang berskor tertinggi) diterapkan per kelas. Sebanyak 45% waktu *forward pass* deteksi pada VGG16 habis di lapis *fully connected* karena jumlah proposal besar. Makalah ini memangkasnya dengan *truncated SVD*: matriks bobot lapis didekomposisi dan hanya nilai singular teratas yang dipertahankan, sehingga satu lapis besar digantikan dua lapis kecil tanpa non-linearitas. Pada VGG16, lapis fc6 (25088×4096) dipangkas ke 1024 nilai singular dan fc7 (4096×4096) ke 256; waktu deteksi turun lebih dari 30% dengan penurunan mAP hanya 0,3 poin (66,9% menjadi 66,6%), tanpa penyetelan ulang.

## Eksperimen dan Hasil

Evaluasi dilakukan pada PASCAL VOC 2007, 2010, dan 2012 dengan metrik mAP (*mean Average Precision*, rerata presisi di seluruh kelas; maksimal 100%). Semua pengukuran waktu memakai satu GPU Nvidia K40.

Pada VOC 2007 (model L), Fast R-CNN mencapai 66,9% mAP, mengalahkan R-CNN (66,0%) dan SPPnet (63,1%). Selisih 3,8 poin atas SPPnet penting karena dicapai dengan pelatihan satu skala, sedangkan SPPnet memakai lima skala — bukti bahwa menyetel halus lapis konvolusi lebih berharga daripada piramida citra. Dengan data latih digabung (VOC07+VOC12, tiga kali lipat menjadi 16,5 ribu citra), mAP naik menjadi 70,0%. Pada VOC 2010, Fast R-CNN mencapai 68,8% dengan data gabungan, melampaui SegDeepM (67,2%) yang memakai anotasi segmentasi. Pada VOC 2012, skornya 65,7% — teratas di papan peringkat saat itu — dan 68,4% dengan data gabungan, dibandingkan 62,4% untuk R-CNN.

Kecepatan berubah lebih besar lagi. Pelatihan VGG16 turun dari 84 jam (R-CNN) menjadi 9,5 jam; waktu uji turun dari 47,0 detik per citra menjadi 0,32 detik (146 kali) dan menjadi 0,22 detik dengan SVD (213 kali). Terhadap SPPnet, pelatihan 2,7 kali lebih cepat dan pengujian 7–10 kali lebih cepat, sekaligus lebih akurat.

Ablasi menguatkan pilihan desain. Pelatihan multi-tugas menaikkan mAP klasifikasi murni +0,8 hingga +1,1 poin dibanding pelatihan klasifikasi saja, dan mengalahkan pelatihan bertahap. Membekukan lapis konvolusi (hanya lapis *fully connected* yang disetel, meniru SPPnet) menjatuhkan mAP dari 66,9% ke 61,4%; menyetel dari conv3_1 ke atas (9 dari 13 lapis) terbukti cukup. *Softmax* bawaan mengalahkan SVM *post-hoc* sebesar +0,1 hingga +0,8 poin pada ketiga model. Menambah proposal dari 1.000 ke 10.000 tidak menaikkan mAP, dan 45 ribu kotak rapat malah menjatuhkannya ke 52,9% — proposal *selective search* yang jarang berperan sebagai kaskade penyaring yang menguntungkan. Sebagai baseline awal di MS COCO, Fast R-CNN memperoleh 35,9% mAP gaya PASCAL dan 19,7% AP gaya COCO yang juga direrata atas ambang IoU — jauh di bawah angka VOC, menggambarkan ketatnya metrik baru tersebut.

## Kelebihan dan Keterbatasan

Kelebihan utama Fast R-CNN adalah penyederhanaan menyeluruh: satu tahap pelatihan menggantikan tiga, semua lapis ikut diperbarui, ratusan gigabita cache fitur di disk hilang, dan akurasi justru naik. Kecepatannya membuat eksperimen yang sebelumnya mahal menjadi praktis, dan kode sumbernya dirilis dengan lisensi MIT.

Keterbatasannya berlapis. Pertama, proposal tetap dari algoritme eksternal yang tidak dilatih; angka 0,32 detik per citra secara eksplisit tidak memasukkan waktu pembangkitan proposal, sehingga dari sisi rekayasa tahap inilah hambatan berikutnya. Kedua, model terbesar tidak dapat memakai multi-skala karena keterbatasan memori GPU saat itu. Ketiga, secara konseptual, komputasi lapis *fully connected* tetap diulang untuk setiap proposal, termasuk yang saling tumpang tindih. Keempat, laju sekitar 3–5 citra per detik masih jauh dari *real-time*.

## Kaitan dengan Bab Lain

Bab ini adalah kelanjutan langsung [bab 012 (R-CNN)](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md): kerangka proposal–CNN–klasifikasi dipertahankan, tetapi struktur pelatihannya diganti total. Dari SPPnet dipinjam gagasan berbagi peta fitur; kontribusi bab ini adalah membuatnya dapat dilatih penuh. Keterbatasan proposal eksternal yang tersisa dijawab [bab 014 (Faster R-CNN)](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md), yang mengganti *selective search* dengan jaringan pengusul wilayah yang dilatih bersama detektor. [Bab 017 (Mask R-CNN)](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md) kemudian memperhalus *RoI pooling* menjadi *RoIAlign* demi segmentasi instans. Di arah berlawanan, [bab 001 (YOLOv1)](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) membuang proposal sama sekali demi kecepatan; perbandingannya dengan Fast R-CNN pada VOC 2007 (63,4% mAP pada 45 FPS melawan 70,0% pada sekitar 3 FPS) menjadi titik tolak perdebatan satu tahap versus dua tahap yang membingkai klaster Fondasi RGB.

## Poin untuk Sitasi

Kutip dengan kunci `girshick2015fastrcnn`. Ringkasan yang aman dikutip: "Fast R-CNN menghitung peta fitur konvolusi satu kali untuk seluruh citra dan mengekstrak fitur setiap proposal melalui RoI pooling, lalu melatih klasifikasi softmax dan regresi kotak bersama dalam satu tahap; pelatihan VGG16 sekitar 9 kali lebih cepat dari R-CNN, pengujian hingga 213 kali lebih cepat, dengan mAP lebih tinggi pada PASCAL VOC." Seluruh angka pada bab ini diverifikasi terhadap teks lengkap arXiv:1504.08083, versi yang dinyatakan tampil di ICCV 2015. Dua catatan sebelum sitasi formal: angka "66% lawan 62%" pada pendahuluan makalah adalah pembulatan dari 65,7% lawan 62,4% pada VOC 2012 tanpa data tambahan; dan hasil MS COCO (35,9% dan 19,7%) dinyatakan penulis sebagai baseline awal, bukan hasil akhir.
