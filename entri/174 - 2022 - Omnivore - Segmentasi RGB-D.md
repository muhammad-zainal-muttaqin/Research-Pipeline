# 174 - Omnivore: A Single Model for Many Visual Modalities

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `girdhar2022omnivore` |
| Judul asli | Omnivore: A Single Model for Many Visual Modalities |
| Penulis | Rohit Girdhar, Mannat Singh, Nikhila Ravi, Laurens van der Maaten, Armand Joulin, Ishan Misra |
| Tahun | 2022 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2201.08377
- **Google Scholar:** https://scholar.google.com/scholar?q=Omnivore%3A%20A%20Single%20Model%20for%20Many%20Visual%20Modalities
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Omnivore%3A%20A%20Single%20Model%20for%20Many%20Visual%20Modalities&sort=relevance

## Gambaran Umum

Omnivore adalah satu jaringan Transformer yang mengklasifikasikan tiga jenis data visual berbeda — citra tunggal, klip video, dan citra RGB-D (citra warna dengan kanal kedalaman tambahan) — memakai bobot yang sepenuhnya sama, tanpa cabang atau modul khusus per modalitas. Gagasan intinya adalah mengubah ketiga jenis masukan menjadi format token spatio-temporal yang seragam sehingga satu *backbone* Swin Transformer (varian Transformer visi yang memproses citra secara hierarkis dengan jendela lokal) dapat memprosesnya langsung. Model ini dilatih sekaligus pada ImageNet-1K (klasifikasi citra), Kinetics-400 (klasifikasi video), dan SUN RGB-D (klasifikasi citra RGB-D), dan pada konfigurasi Swin-L mencapai 86,0% akurasi top-1 di ImageNet, 84,1% di Kinetics-400, dan 67,1% di SUN RGB-D — hasil yang sepadan dengan model khusus per modalitas berukuran serupa. Kontribusi utamanya bukan arsitektur baru, melainkan bukti bahwa satu jaringan tunggal dapat menggantikan tiga jaringan terpisah tanpa kehilangan akurasi berarti, sekaligus memunculkan kemampuan lintas-modal yang tidak diajarkan secara eksplisit.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum Omnivore, model visi hampir selalu dirancang untuk satu jenis data. Klasifikasi citra memakai CNN atau Vision Transformer (ViT, bab 024) yang menerima tensor 2D H×W×3. Klasifikasi video memakai jaringan 3D CNN atau Transformer video yang menerima tensor tambahan berdimensi waktu. Pengenalan RGB-D — citra berpasangan dengan peta kedalaman, umum pada robotika dan pemahaman ruangan dalam ruangan — biasanya memakai dua cabang terpisah (satu untuk RGB, satu untuk kedalaman) yang digabungkan lewat mekanisme fusi khusus, seperti terlihat pada arsitektur segmentasi RGB-D di bab 171 (SegFormer) dan bab 172 (EMSANet).

Pendekatan per-modalitas ini menimbulkan dua masalah. Pertama, setiap modalitas memerlukan arsitektur, siklus pelatihan, dan penyetelan hiperparameter sendiri, sehingga pengetahuan visual yang dipelajari pada satu modalitas — misalnya bentuk objek dari jutaan citra ImageNet — tidak otomatis tersedia untuk modalitas lain seperti RGB-D yang datanya jauh lebih sedikit. Kedua, sistem yang harus menangani lebih dari satu jenis sensor (contohnya robot dengan kamera RGB dan sensor kedalaman) terpaksa menjalankan beberapa model paralel, menambah beban komputasi dan kompleksitas penerapan. Upaya pra-pelatihan multimodal sebelumnya, seperti MultiMAE, menunjukkan potensi berbagi representasi lintas modalitas, tetapi belum menunjukkan satu model tunggal yang bersaing setara dengan model khusus pada tugas klasifikasi standar di tiga modalitas visual sekaligus.

## Ide Utama

Gagasan inti Omnivore adalah menyamakan format token di tingkat masukan, bukan menyamakan arsitektur di tingkat tinggi. Setiap modalitas — citra, video, atau RGB-D — dipecah menjadi potongan (*patch*) berdimensi waktu×tinggi×lebar×kanal (t×h×w×3) sebelum masuk ke lapis penyemat (*embedding*) pertama. Video secara alami memiliki t > 1 karena memuat banyak bingkai; citra tunggal dan citra RGB-D hanya memiliki t = 1. Agar satu lapis penyemat yang sama dapat menerima ketiganya, patch bertingkat waktu tunggal diberi nilai nol tambahan (*zero-padding*) pada dimensi waktu sehingga bentuknya menyamai patch video. Dengan trik ini, tidak diperlukan lapis penyemat terpisah untuk citra dan video — hanya satu lapis konvolusi 3D yang sama dipakai untuk keduanya.

Kanal kedalaman pada RGB-D ditangani secara berbeda: patch kedalaman diproyeksikan lewat lapis linear-dan-normalisasi terpisah, lalu hasilnya dijumlahkan (bukan digabung/*concatenate*) dengan penyemat patch RGB pada posisi spasial yang sama. Dengan penjumlahan ini, dimensi token yang masuk ke Transformer tetap identik untuk ketiga modalitas, sehingga sisa jaringan — blok Swin Transformer, lapis normalisasi, mekanisme atensi — tidak perlu tahu dari modalitas mana token itu berasal.

## Cara Kerja Langkah demi Langkah

### Tokenisasi Spatio-Temporal Terpadu

Setiap masukan, apa pun modalitasnya, pertama-tama dipetakan menjadi barisan token berukuran tetap. Untuk video, potongan berdimensi t×h×w diambil langsung dari klip; untuk citra dan RGB-D, potongan tunggal (t=1) diperlakukan sebagai kasus khusus lewat *zero-padding* dimensi waktu seperti dijelaskan di atas. Skema ini membuat masukan berbeda bentuk fisiknya (gambar diam 2D versus klip video 3D) tetap keluar sebagai tensor token berbentuk sama sebelum masuk ke Transformer.

```
Citra (H,W,3)         Video (T,H,W,3)        RGB-D (H,W,3)+(H,W,1)
   |  t=1, pad             |  t>1                |  t=1, pad
   v                       v                      v
patch embed 3D  <---  patch embed 3D  --->  patch embed RGB (3D)
   |                       |                      |  + patch embed depth
   |                       |                      |    (linear+LN, dijumlahkan)
   v                       v                      v
      token spatio-temporal berdimensi sama --> Swin Transformer
```

Diagram di atas menunjukkan bahwa ketiga jalur masukan berbeda hanya pada tahap sebelum penyemat; sesudah token terbentuk, jaringan yang dilalui benar-benar identik.

### Backbone Swin Transformer untuk Spatio-Temporal

Token yang telah seragam diproses oleh Swin Transformer yang diperluas untuk video: atensi-diri (*self-attention*) dihitung dalam jendela lokal 3D yang mencakup dimensi waktu, tinggi, dan lebar sekaligus, bukan hanya dimensi spasial seperti Swin Transformer citra pada bab 025. Encoding posisi relatif dipecah menjadi dua komponen terpisah — satu untuk posisi spasial, satu untuk posisi temporal — sehingga jaringan dapat membedakan pergeseran ruang dari pergeseran waktu meski keduanya diproses oleh mekanisme atensi yang sama. Struktur berjenjang (*hierarchical*) Swin Transformer, yang mengecilkan resolusi token bertahap pada tiap tingkat, dipertahankan agar kompleksitas komputasi atensi tidak tumbuh kuadratik terhadap jumlah token.

### Kepala Klasifikasi dan Pelatihan Bersama

Backbone Transformer sepenuhnya dibagikan antar-modalitas, tetapi setiap dataset memiliki kepala klasifikasi linear sendiri di ujung jaringan, sesuai jumlah kelas masing-masing (1.000 kelas ImageNet, 400 kelas aksi Kinetics-400, dan kelas kategori SUN RGB-D). Pelatihan dilakukan dengan *mini-batch* SGD (*stochastic gradient descent*, optimisasi berbasis gradien pada subset data) secara bersamaan pada ketiga dataset. Penulis menguji dua strategi penyusunan *batch*: menyusun setiap *batch* hanya dari satu dataset secara bergantian, atau mencampur sampel dari ketiga dataset dalam satu *batch*. Kedua strategi menghasilkan akurasi yang sebanding; strategi *batch* per-dataset dipilih karena lebih sederhana diimplementasikan pada infrastruktur pelatihan terdistribusi.

Karena backbone dibagikan, gradien dari data ImageNet yang jumlahnya jauh lebih besar (1,28 juta citra latih) turut membentuk representasi yang dipakai untuk memproses video dan RGB-D, meski dataset SUN RGB-D jauh lebih kecil. Efek inilah yang mendasari klaim transfer lintas-modal: penulis menunjukkan bahwa ruang penyemat (*embedding space*) yang terbentuk memungkinkan pencarian peta kedalaman yang relevan dari kueri citra RGB biasa, meski Omnivore tidak pernah dilatih dengan pasangan citra ImageNet dan peta kedalamannya — kemampuan yang muncul semata dari berbagi bobot, bukan dari pengawasan langsung.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada tiga tolok ukur klasifikasi standar: ImageNet-1K untuk citra, Kinetics-400 untuk video, dan SUN RGB-D untuk citra RGB-D indoor. Pada konfigurasi terbesar, Omnivore Swin-L mencapai 86,0% akurasi top-1 di ImageNet-1K, 84,1% di Kinetics-400, dan 67,1% di SUN RGB-D; konfigurasi menengah Swin-B mencapai 84,0%, 83,3%, dan 65,4% secara berurutan pada ketiga tolok ukur tersebut. Angka-angka ini dilaporkan sepadan dengan model khusus per modalitas berukuran serupa — artinya Omnivore tidak membayar penalti akurasi yang berarti meski satu set bobot dipakai untuk tiga tugas berbeda, sekaligus menghapus kebutuhan menyimpan dan melatih tiga jaringan terpisah.

Selain akurasi klasifikasi standar, penulis menunjukkan demonstrasi kualitatif kemampuan lintas-modal: representasi yang dipelajari pada satu modalitas dapat dipakai untuk mengambil (*retrieve*) data pada modalitas lain yang berkaitan secara semantik, misalnya mencari peta kedalaman yang cocok dengan sebuah citra RGB. Kemampuan ini menegaskan bahwa berbagi bobot antar-modalitas bukan sekadar efisiensi rekayasa, melainkan juga menghasilkan representasi visual yang lebih umum.

## Kelebihan dan Keterbatasan

Kelebihan utama Omnivore adalah kesederhanaan rekayasa: satu jaringan, satu siklus pelatihan, tiga modalitas, dengan akurasi yang tidak kalah dari model khusus. Ini mengurangi biaya penerapan pada sistem yang harus menangani lebih dari satu jenis sensor visual sekaligus, misalnya platform robotika yang memiliki kamera RGB dan sensor kedalaman. Mekanisme tokenisasi terpadunya juga cukup umum untuk diperluas ke modalitas visual lain tanpa mengubah struktur Transformer inti.

Keterbatasan yang secara eksplisit disebutkan penulis adalah cakupan representasi 3D: Omnivore hanya menangani citra RGB-D satu sudut pandang (*single-view*) dan tidak menggeneralisasi ke representasi 3D lain seperti *voxel* atau awan titik (*point cloud*). Penulis juga mencatat bahwa masukan kedalaman tidak invarian terhadap skala, dan modalitas audio belum dimanfaatkan dalam kerangka kerja ini. Dari sisi rekayasa, model ini dirancang untuk tugas klasifikasi tingkat citra/klip, bukan tugas prediksi padat (*dense prediction*) seperti segmentasi semantik piksel-per-piksel yang menjadi fokus bab 171–173 pada klaster ini; adaptasi Omnivore ke segmentasi RGB-D memerlukan kepala dekoder tambahan yang tidak dibahas dalam makalah aslinya. Secara konseptual, keberhasilan pelatihan bersama juga bergantung pada ketersediaan dataset berlabel besar di tiap modalitas — SUN RGB-D yang jauh lebih kecil dari ImageNet dan Kinetics-400 tetap menghasilkan akurasi lebih rendah, mengindikasikan bahwa berbagi bobot tidak sepenuhnya mengatasi kesenjangan skala data antar-modalitas.

## Kaitan dengan Bab Lain

Omnivore memakai Swin Transformer (bab 025) sebagai *backbone* dan mewarisi mekanisme atensi jendela hierarkisnya, diperluas ke dimensi temporal untuk menangani video di samping citra. Berbeda dari jalur fusi RGB-D dua cabang yang dipakai SegFormer (bab 171) dan EMSANet (bab 172), yang secara eksplisit menggabungkan fitur RGB dan kedalaman lewat modul fusi pada tingkat tengah jaringan, Omnivore menyatukan kedua kanal itu sedini mungkin — pada tahap penyemat token — sehingga seluruh sisa jaringan tidak membedakan sumber datanya. GeminiFusion (bab 173), yang memakai atensi lintas-modal eksplisit antara cabang RGB dan kedalaman, dan Omnivore, yang menghindari cabang terpisah sama sekali, mewakili dua filosofi berlawanan dalam menangani data RGB-D: fusi eksplisit versus tokenisasi seragam sejak awal. Perbandingan ini relevan bagi pembaca yang mempertimbangkan trade-off antara akurasi tugas dense-prediction (kekuatan pendekatan fusi eksplisit) dan efisiensi model tunggal lintas-modalitas (kekuatan pendekatan Omnivore).

## Poin untuk Sitasi

Kutip dengan kunci `girdhar2022omnivore`. Ringkasan yang aman dikutip: "Omnivore adalah satu model Swin Transformer yang mengklasifikasikan citra, video, dan RGB-D dengan bobot bersama lewat tokenisasi spatio-temporal seragam, mencapai akurasi sepadan model khusus per modalitas pada ImageNet-1K, Kinetics-400, dan SUN RGB-D." Angka 86,0% (ImageNet, Swin-L), 84,1% (Kinetics-400, Swin-L), 67,1% (SUN RGB-D, Swin-L), serta 84,0%/83,3%/65,4% (Swin-B) diperoleh dari pembacaan naskah dan sebaiknya dicocokkan sekali lagi dengan tabel hasil resmi sebelum dikutip dalam karya formal. Rincian jumlah epoch pelatihan dan konfigurasi augmentasi data belum terverifikasi penuh dan perlu dicek ke naskah asli atau kode resmi di `facebookresearch/omnivore` sebelum dijadikan rujukan teknis rinci.
