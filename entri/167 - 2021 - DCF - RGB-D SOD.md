# 167 - Calibrated RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ji2021dcf` |
| Judul asli | Calibrated RGB-D Salient Object Detection |
| Penulis | Wei Ji, Jingjing Li, Shuang Yu, Miao Zhang, Yongri Piao, Shunyu Yao, Qi Bi, Kai Ma, Yefeng Zheng, Huchuan Lu, Li Cheng |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021) |
| Tema | RGB-D SOD |

## Tautan Akses
- **CVF Open Access (PDF resmi):** https://openaccess.thecvf.com/content/CVPR2021/papers/Ji_Calibrated_RGB-D_Salient_Object_Detection_CVPR_2021_paper.pdf
- **Kode sumber (GitHub):** https://github.com/jiwei0921/DCF
- **Google Scholar:** https://scholar.google.com/scholar?q=Calibrated%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Calibrated%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini mengusulkan DCF (*Depth Calibration and Fusion*), kerangka kerja untuk *salient object detection* (SOD, deteksi objek paling menonjol pada suatu citra) berbasis pasangan citra RGB dan peta kedalaman (*depth map*, citra yang tiap pikselnya menyatakan jarak permukaan ke sensor). Masalah yang disasar adalah peta kedalaman pada dataset RGB-D SOD sering mengandung derau dan bias yang tidak konsisten dengan struktur objek sebenarnya, sehingga metode fusi RGB-*depth* yang memperlakukan kedua modalitas itu setara justru dapat menurunkan akurasi dibandingkan model RGB tunggal. DCF menjawab masalah ini dengan dua komponen: strategi kalibrasi kedalaman yang memperbaiki bias laten pada peta kedalaman mentah sebelum dipakai, dan modul referensi silang (*cross reference module*, CRM) yang menukar informasi antara fitur RGB dan fitur kedalaman secara dua arah untuk menghasilkan fitur gabungan. Menurut klaim penulis, pendekatan ini mengungguli 27 metode SOD RGB-D sezaman pada tolok ukur standar bidang tersebut, dan strategi kalibrasi kedalamannya dapat dipasang sebagai modul praproses pada model RGB-D SOD lain untuk menaikkan akurasinya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD bertugas menandai wilayah citra yang paling menarik perhatian visual, berguna sebagai tahap awal bagi banyak aplikasi seperti penyuntingan citra, kompresi berbasis wilayah penting, dan segmentasi objek. Pada citra RGB tunggal, SOD sulit ketika latar belakang memiliki tekstur atau warna mirip objek utama, karena sinyal warna saja tidak selalu membedakan objek dari latarnya. Menambahkan peta kedalaman sebagai modalitas kedua — pendekatan yang dikenal sebagai RGB-D SOD — bertujuan memberi isyarat geometris tambahan, sebab objek yang menonjol umumnya berada pada jarak berbeda dari latar belakangnya.

Masalahnya, peta kedalaman pada dataset RGB-D SOD diperoleh dari sensor *time-of-flight*, kamera stereo, atau algoritme estimasi kedalaman, yang semuanya menghasilkan keluaran dengan derau, area kosong, atau bias sistematis. Metode sebelumnya yang relevan bagi klaster ini, seperti CoNet (bab 166) dengan fusi kolaboratif tiga aliran, umumnya mengasumsikan kedalaman sebagai sumber informasi yang dapat dipercaya sepenuhnya dan menggabungkannya langsung dengan fitur RGB. Ketika kedalaman berkualitas buruk, asumsi ini membuat kesalahan pada peta kedalaman ikut terbawa ke prediksi saliency, bahkan dapat menurunkan performa di bawah model yang hanya memakai RGB. Metode berbasis kesadaran kualitas kedalaman yang muncul sebelum DCF, seperti D3Net dan UC-Net, mencoba menyaring atau memberi bobot ketidakpastian pada kedalaman, tetapi belum secara eksplisit mengoreksi isi peta kedalaman itu sendiri sebelum fusi. DCF memosisikan diri pada celah ini: mengalibrasi kedalaman terlebih dahulu, bukan sekadar menyaring atau membobotnya saat fusi.

## Ide Utama

Gagasan inti DCF adalah memisahkan proses menjadi dua tahap yang jelas: kalibrasi kedalaman, lalu fusi. Pada tahap kalibrasi, jaringan mempelajari koreksi terhadap peta kedalaman mentah dengan memakai citra RGB sebagai rujukan, sehingga keluarannya berupa peta kedalaman yang lebih konsisten dengan batas dan struktur objek yang terlihat pada RGB. Pada tahap fusi, fitur dari citra RGB dan fitur dari kedalaman terkalibrasi saling bertukar informasi lewat modul referensi silang, alih-alih digabungkan begitu saja lewat penjumlahan atau penggabungan kanal (*concatenation*) seperti pada banyak metode fusi awal. Intuisi mekanisnya: RGB memasok bentuk dan tekstur objek, kedalaman terkalibrasi memasok pemisahan jarak antara objek dan latar, dan keduanya saling mengoreksi lewat referensi silang sebelum diputuskan menjadi peta saliency akhir.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Dua Aliran

DCF memakai jaringan dua aliran (*two-stream network*): satu aliran menerima citra RGB, satu aliran lain menerima peta kedalaman yang telah dikalibrasi. Kedua aliran memakai arsitektur ekstraksi fitur berbasis CPD (*Cascaded Partial Decoder*, kerangka dekoder kaskade yang sebelumnya dipakai untuk SOD RGB tunggal) sebagai basis pembanding, menghasilkan peta fitur bertingkat pada beberapa resolusi dari kasar ke halus.

### Strategi Kalibrasi Kedalaman

Sebelum masuk ke aliran kedalaman, peta kedalaman mentah diproses oleh modul kalibrasi yang dilatih untuk mengurangi bias laten — pergeseran atau distorsi sistematis pada nilai kedalaman yang tidak sesuai dengan struktur objek pada RGB. Modul ini memakai isyarat dari citra RGB berpasangan sebagai rujukan koreksi, sehingga keluarannya adalah peta kedalaman yang lebih selaras dengan tepi dan bentuk objek yang tampak pada RGB. Menurut penulis, langkah kalibrasi ini bersifat modular: dapat dipasang di depan model RGB-D SOD lain sebagai praproses tanpa mengubah arsitektur model tersebut, dan dilaporkan tetap memberi kenaikan akurasi ketika diuji pada model RGB-D SOD lain.

### Modul Referensi Silang (Cross Reference Module)

Fitur RGB dan fitur kedalaman terkalibrasi pada tiap tingkat resolusi dipertukarkan lewat modul referensi silang. Alih-alih fusi satu arah — misalnya kedalaman hanya dipakai untuk membobot fitur RGB — CRM membiarkan kedua modalitas saling memberi isyarat: fitur RGB dipakai untuk menyaring fitur kedalaman, dan sebaliknya fitur kedalaman dipakai untuk menajamkan fitur RGB. Hasil pertukaran ini membentuk fitur gabungan lintas-modal pada tiap tingkat, yang kemudian diteruskan ke tahap dekoding.

### Tiga Cabang Dekoding

Fitur bertingkat dari aliran RGB, aliran kedalaman terkalibrasi, dan fitur gabungan hasil CRM masing-masing diteruskan ke cabang dekoder terpisah yang menghasilkan peta saliency dari sudut pandang modalitasnya sendiri, sebelum digabung menjadi prediksi akhir. Skema alir data secara ringkas:

```
RGB ─────► aliran fitur RGB ──────────┐
                                       ├─► CRM (referensi silang) ─► dekoder gabungan ─┐
depth mentah ─► kalibrasi ─► aliran   ─┘                                              ├─► saliency akhir
              fitur depth terkalibrasi ─────────────────────────► dekoder depth ──────┤
             aliran fitur RGB (jalur terpisah) ────────────────► dekoder RGB ─────────┘
```

Desain tiga cabang ini membuat pelatihan dapat diawasi (*supervised*) pada tiap cabang secara terpisah dengan peta saliency kebenaran (*ground truth*) yang sama, sehingga tiap aliran dipaksa menghasilkan prediksi yang masuk akal sendiri-sendiri, bukan hanya bergantung pada cabang gabungan.

## Eksperimen dan Hasil

Pengujian dilakukan pada tolok ukur standar RGB-D SOD yang lazim dipakai bidang ini, dengan set pelatihan yang menurut repositori kode resmi terdiri atas gabungan NJU2K dan NLPR (2.185 citra), serta varian yang menambahkan DUT-RGBD (2.985 citra). Evaluasi memakai metrik baku SOD: S-measure (kemiripan struktural antara peta saliency prediksi dan kebenaran), F-measure (rerata harmonik presisi dan recall pada peta biner saliency), E-measure (kesesuaian keselarasan piksel secara lokal dan global), dan MAE atau *Mean Absolute Error* (rerata selisih absolut piksel-per-piksel antara prediksi dan kebenaran, semakin rendah semakin baik). Penulis melaporkan bahwa DCF mengungguli 27 metode RGB-D SOD sezaman pada pengujian tersebut, tanpa merinci di sini nilai numerik tiap dataset karena angka pasti perlu dikonfirmasi langsung ke tabel pada naskah asli.

Selain evaluasi tolok ukur utama, penulis melaporkan pengujian tambahan pada dataset ReDWeb-S, dataset kedalaman yang lebih menantang, serta studi ablasi yang memisahkan kontribusi strategi kalibrasi kedalaman dari kontribusi modul referensi silang. Studi ablasi semacam ini penting karena membuktikan bahwa kenaikan akurasi berasal dari kedua komponen baru, bukan sekadar dari arsitektur backbone yang dipakai. Penulis juga mengklaim strategi kalibrasi kedalaman, ketika dipasangkan di depan model RGB-D SOD lain yang sudah ada, memberi kenaikan akurasi tambahan — bukti bahwa manfaat kalibrasi tidak terikat pada arsitektur fusi khusus DCF.

## Kelebihan dan Keterbatasan

Kelebihan utama DCF adalah pemisahan eksplisit antara masalah kualitas data (kedalaman berderau) dan masalah fusi (bagaimana menggabungkan dua modalitas), yang sebelumnya sering ditangani sekaligus lewat pembobotan implisit. Modularitas strategi kalibrasi kedalaman — dapat dipasang pada model lain sebagai praproses — memperluas relevansi metode ini di luar arsitektur DCF sendiri. Modul referensi silang yang dua arah juga lebih seimbang dibandingkan skema fusi satu arah yang hanya membiarkan satu modalitas mendominasi.

Dari sisi rekayasa, tiga cabang dekoder dan modul kalibrasi tambahan berarti biaya komputasi dan jumlah parameter DCF lebih besar dibandingkan model fusi satu aliran, sehingga penerapan pada perangkat dengan sumber daya terbatas memerlukan pertimbangan tambahan; makalah yang tersedia untuk telaah ini tidak memuat rincian FLOPs atau kecepatan inferensi yang dapat dikutip dengan pasti di sini. Secara konseptual, kualitas kalibrasi kedalaman bergantung pada seberapa informatif citra RGB berpasangan; pada kondisi RGB juga buruk (misalnya pencahayaan sangat rendah atau motion blur), rujukan kalibrasi ikut melemah sehingga manfaat kalibrasi dapat berkurang. Kasus kedalaman yang hilang total pada area luas (bukan sekadar berderau) juga kemungkinan tetap menjadi tantangan, karena kalibrasi memperbaiki bias, bukan mengisi data yang sama sekali tidak ada.

## Kaitan dengan Bab Lain

DCF melanjutkan arah metode-metode RGB-D SOD yang menyadari ketidaksempurnaan kedalaman, termasuk CoNet pada [166 - 2020 - CoNet - RGB-D SOD](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md), yang memakai fusi kolaboratif tiga aliran tetapi belum mengoreksi isi kedalaman secara eksplisit sebelum fusi. Perbedaan tegasnya terletak pada tahap kalibrasi eksplisit yang ditambahkan DCF sebelum fusi berlangsung, alih-alih hanya membobot atau menyaring kontribusi kedalaman saat fusi. Gagasan memisahkan kualitas modalitas dari mekanisme fusi ini relevan dibandingkan dengan pendekatan lain di klaster RGB-D SOD yang ditulis pada periode berdekatan, seperti [168 - 2021 - SPNet - RGB-D SOD](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md), serta metode yang datang setelahnya dan dapat dibandingkan dari sisi efisiensi maupun akurasi, seperti [170 - 2022 - MobileSal - RGB-D SOD](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md) yang menyasar kecepatan pada perangkat terbatas, dan [169 - 2023 - CAVER - RGB-D SOD](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md) yang mengeksplorasi mekanisme fusi berbasis attention lintas-modal pada generasi berikutnya. Prinsip kalibrasi kedalaman sebelum fusi yang diperkenalkan DCF menjadi acuan bagi pembaca yang membandingkan strategi mana yang lebih menekankan koreksi data mentah versus mekanisme fusi itu sendiri.

## Poin untuk Sitasi

Kutip dengan kunci `ji2021dcf`. Ringkasan yang aman dikutip: "DCF mengusulkan kerangka kerja dua tahap untuk RGB-D SOD yang terdiri atas strategi kalibrasi kedalaman untuk mengoreksi bias pada peta kedalaman mentah, dan modul referensi silang untuk fusi fitur RGB-kedalaman dua arah, dilaporkan mengungguli 27 metode sezaman pada tolok ukur RGB-D SOD standar (CVPR 2021)." Catatan verifikasi: nilai numerik S-measure, F-measure, E-measure, dan MAE per dataset (NJU2K, NLPR, STERE, DES, SIP, dan dataset lain yang mungkin diuji) belum dapat diambil dari sumber yang berhasil diakses saat penulisan bab ini karena versi PDF resmi CVF dan IEEE Xplore memblokir pengambilan otomatis; nilai-nilai ini wajib dikonfirmasi langsung dari tabel pada naskah asli atau repositori GitHub `jiwei0921/DCF` sebelum dikutip dalam karya formal. Detail arsitektur backbone CPD dan komposisi persis set pelatihan/pengujian juga sebaiknya dicocokkan ulang dengan naskah asli.
