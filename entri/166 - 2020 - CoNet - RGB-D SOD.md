# 166 - Accurate RGB-D Salient Object Detection via Collaborative Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ji2020conet` |
| Judul asli | Accurate RGB-D Salient Object Detection via Collaborative Learning |
| Penulis | Wei Ji, Jingjing Li, Miao Zhang, Yongri Piao, Huchuan Lu |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV 2020) |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2007.11782
- **Google Scholar:** https://scholar.google.com/scholar?q=Accurate%20RGB-D%20Salient%20Object%20Detection%20via%20Collaborative%20Learning
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Accurate%20RGB-D%20Salient%20Object%20Detection%20via%20Collaborative%20Learning&sort=relevance
- **Kode sumber:** https://github.com/jiwei0921/CoNet

## Gambaran Umum

Makalah ini mengusulkan CoNet, kerangka *deep learning* untuk *RGB-D salient object detection* (SOD, deteksi objek salien pada pasangan citra RGB dan peta kedalaman) yang melatih tiga tugas — saliency, deteksi tepi, dan estimasi *depth* (kedalaman) — secara bersamaan dalam satu jaringan yang berbagi *encoder* (bagian jaringan yang mengekstrak fitur dari citra masukan). Ketiga tugas ini disebut penulis sebagai tiga *collaborator* (kolaborator) yang saling menguatkan selama pelatihan. Titik pembeda utama CoNet dari metode fusi RGB-D sebelumnya adalah peta *depth* hanya dipakai sebagai sinyal supervisi saat pelatihan, bukan sebagai masukan saat inferensi (proses menghasilkan prediksi pada data baru). Akibatnya, model tidak memerlukan cabang jaringan *depth* terpisah maupun peta kedalaman pada saat digunakan, sehingga lebih ringan dan lebih cepat dibandingkan metode dua-aliran (*two-stream*) yang memproses RGB dan *depth* secara paralel hingga tahap akhir. Pada dataset NJUD, CoNet mencapai *F-measure* 0,872 dan *mean absolute error* (MAE, rata-rata galat absolut) 0,047 — MAE lebih rendah daripada DMRA (0,051) dan CPFP (0,053) — dengan kecepatan inferensi 34 *frame* per detik (FPS), diklaim 55% lebih cepat daripada DMRA.

## Latar Belakang: Masalah yang Ingin Dipecahkan

*Salient object detection* bertugas menyorot wilayah citra yang paling menarik perhatian visual, dituangkan sebagai peta abu-abu bernilai 0 sampai 1 per piksel. Menambahkan peta kedalaman pada RGB memberi isyarat geometris — jarak antar-permukaan — yang membantu memisahkan objek dari latar ketika warna dan tekstur RGB serupa. Sebelum CoNet, metode RGB-D SOD umumnya memakai dua jaringan konvolusi terpisah, satu untuk RGB dan satu untuk *depth*, kemudian menggabungkan fiturnya lewat modul fusi (misalnya penjumlahan, perkalian, atau *attention* lintas-modal). Skema ini memiliki dua kelemahan yang menjadi sasaran CoNet. Pertama, jaringan berbasis *fully convolutional network* (FCN) memakai operasi *pooling* (peringkasan spasial, memperkecil resolusi peta fitur) dan *upsampling* (pembesaran kembali resolusi) berulang kali; proses ini mengaburkan batas objek, sehingga peta saliency yang dihasilkan sering memiliki tepi kabur meskipun area intinya sudah terdeteksi dengan benar. Kedua, jaringan *depth* tambahan menggandakan jumlah parameter dan biaya penyimpanan, serta membuat sistem bergantung pada ketersediaan sensor kedalaman yang andal saat digunakan — padahal sensor *depth* murah (mis. Kinect struktur-cahaya) sering menghasilkan peta berderau atau berlubang pada permukaan mengilap dan jauh. Kedua masalah ini — batas kabur dan ketergantungan pada *depth* saat inferensi — menjadi dasar rancangan CoNet.

## Ide Utama

Gagasan inti CoNet adalah memisahkan tiga sub-tugas yang saling berkaitan — saliency, tepi, dan *depth* — menjadi tiga kepala prediksi (*collaborator*) yang berbagi satu *encoder* citra RGB, alih-alih melatih jaringan *depth* terpisah untuk difusikan. Kolaborator tepi belajar dari fitur tingkat-rendah (resolusi tinggi, kaya detail tekstur) untuk memprediksi kontur objek secara eksplisit, sehingga batas saliency akhir menjadi tajam. Kolaborator *depth* belajar dari fitur tingkat-tinggi (resolusi rendah, kaya konteks semantik) untuk memprediksi peta kedalaman sebagai bentuk supervisi tambahan yang memaksa fitur tersebut memuat isyarat geometris, tanpa pernah membutuhkan citra *depth* asli sebagai masukan pada saat pengujian. Kolaborator saliency memakai kedua sinyal itu — kontur dari kolaborator tepi dan fitur yang telah "diperkaya geometri" oleh tugas *depth* — untuk menghasilkan peta saliency akhir. Karena ketiga tugas dilatih bersama dengan gradien yang saling memengaruhi lewat fitur bersama, penulis menyebut skema ini pembelajaran kolaboratif atau *mutual-benefit learning* (pembelajaran saling menguntungkan): tugas *depth* dan tepi berperan sebagai bentuk regularisasi (batasan tambahan yang mencegah *overfitting* dan mengarahkan fitur ke representasi yang lebih berguna) bagi tugas utama saliency.

## Cara Kerja Langkah demi Langkah

### Encoder Bersama dan Tiga Kolaborator

CoNet memakai satu *backbone* (jaringan tulang punggung ekstraksi fitur, umumnya berbasis VGG atau ResNet pada makalah ini) yang menerima citra RGB dan menghasilkan fitur pada beberapa tingkat resolusi. Diagram berikut merangkum alur data dari citra masukan ke tiga keluaran kolaboratif:

```
citra RGB ──► encoder bersama (backbone konvolusi)
                  │
                  ├─ fitur tingkat-rendah ──► Kolaborator Tepi
                  │                            (peta kontur objek)
                  │
                  ├─ fitur tingkat-tinggi ──► Kolaborator Depth
                  │                            (peta kedalaman, hanya
                  │                             dipakai saat latih)
                  │
                  └─ fitur gabungan ────────► Kolaborator Saliency
                       (dipandu tepi & fitur                │
                        kaya-geometri dari                  ▼
                        kolaborator depth)          peta saliency akhir
```

Ketiga kolaborator memakai fitur dari *encoder* yang sama, sehingga gradien dari ketiga tugas mengalir balik ke bobot bersama itu selama pelatihan. Konsekuensinya, fitur yang dipelajari *encoder* dipaksa berguna sekaligus untuk mengenali kontur, memperkirakan kedalaman, dan menandai wilayah salien — bukan hanya dioptimalkan untuk satu tugas saja.

### Kolaborator Tepi

Kolaborator ini memprediksi peta tepi biner dari fitur tingkat-rendah, dengan label kebenaran (*ground truth*) tepi diturunkan dari kontur peta saliency anotasi memakai operator deteksi tepi klasik (Canny). Karena fitur tingkat-rendah masih memiliki resolusi spasial tinggi, kolaborator ini efektif menandai batas objek secara presisi, dan hasil tersebut kemudian digabung ke jalur prediksi saliency untuk mempertajam tepi keluaran akhir — mengatasi masalah kabur akibat *pooling*/*upsampling* berulang yang disebutkan pada bagian latar belakang.

### Kolaborator Depth

Kolaborator ini memprediksi peta kedalaman dari fitur tingkat-tinggi memakai label peta *depth* asli yang tersedia pada data latih. Karena tugas ini hanya aktif selama pelatihan — cabang ini dan masukan *depth*-nya dapat dibuang saat inferensi — CoNet tidak memerlukan sensor kedalaman maupun jaringan *depth* tambahan ketika dipakai pada citra baru. Sifat inilah yang penulis maksudkan dengan "bebas dari jaringan *depth* tambahan dan masukan *depth* tambahan untuk melakukan inferensi", membuat model lebih ringan dan lebih fleksibel dibandingkan metode fusi dua-aliran yang selalu membutuhkan *depth* saat digunakan.

### Fungsi Loss dan Pelatihan

Pelatihan memakai empat komponen *loss* (fungsi galat yang diminimalkan): galat tepi, galat saliency kasar, galat *depth*, dan galat saliency akhir, masing-masing dibandingkan dengan label kebenarannya sendiri. Bobot relatif dilaporkan λ tepi = λ saliency = λ akhir = 1, sedangkan λ *depth* = 3, artinya sinyal *depth* diberi penekanan lebih besar agar fitur bersama benar-benar terdorong menyerap isyarat geometris, bukan hanya menumpang sebagai tugas sekunder. Seluruh jaringan dioptimalkan *end-to-end* dengan *stochastic gradient descent* (SGD, penurunan gradien memakai sampel data secara bertahap).

### Inferensi

Pada saat pengujian, hanya citra RGB yang dilewatkan ke *encoder* dan kolaborator saliency (dibantu keluaran kolaborator tepi); kolaborator *depth* tidak dieksekusi. Skema ini membuat kecepatan inferensi CoNet lebih tinggi dibandingkan metode yang harus memproses dua aliran (RGB dan *depth*) secara paralel hingga lapisan akhir.

## Eksperimen dan Hasil

CoNet dievaluasi pada tujuh dataset benchmark RGB-D SOD standar: NJUD (1.985 pasangan citra), NLPR (1.000 pasangan), STEREO (797 pasangan), RGBD135/DES (135 pasangan), LFSD (100 pasangan), SIP (929 pasangan), dan DUT-D (1.200 pasangan). Metrik yang dipakai meliputi *F-measure* (Fβ, harmonik presisi-recall pada peta saliency biner), *weighted F-measure* (Fβʷ, varian F-measure berbobot yang lebih sensitif terhadap kesalahan lokal), *S-measure* (kemiripan struktural antara peta prediksi dan kebenaran), *E-measure* (kesesuaian piksel sekaligus statistik citra global), dan MAE (rata-rata selisih absolut piksel demi piksel, semakin kecil semakin baik).

Pada dataset NJUD, CoNet mencapai Fβ 0,872 — setara dengan DMRA (0,872) dan di atas CPFP (0,850) — tetapi dengan MAE 0,047, lebih rendah (lebih baik) daripada DMRA (0,051) dan CPFP (0,053). Interpretasinya: pada metrik F-measure ketiganya sebanding, tetapi CoNet menghasilkan peta saliency dengan galat piksel rata-rata lebih kecil, konsisten dengan klaim batas objek yang lebih tajam berkat kolaborator tepi. Dari sisi efisiensi, penulis melaporkan ukuran model 167,6 MB dan kecepatan 34 FPS, diklaim 55% lebih cepat daripada DMRA — selisih kecepatan ini konsisten dengan desain CoNet yang tidak menjalankan cabang *depth* terpisah saat inferensi. Penulis juga melaporkan hasil kompetitif pada NLPR, STEREO, SIP, LFSD, RGBD135, dan DUT-D, serta studi ablasi yang menunjukkan bahwa menghapus kolaborator tepi atau kolaborator *depth* menurunkan metrik dibandingkan model penuh, mengonfirmasi kontribusi tiap cabang terhadap hasil akhir.

## Kelebihan dan Keterbatasan

Kelebihan utama CoNet adalah efisiensi inferensi: karena *depth* hanya dipakai sebagai supervisi pelatihan, model menghindari biaya komputasi dan penyimpanan dari cabang jaringan *depth* terpisah, serta tidak bergantung pada ketersediaan sensor kedalaman saat digunakan pada data baru. Kolaborator tepi juga secara langsung menyasar masalah batas kabur yang melekat pada arsitektur FCN, dan hasil MAE yang konsisten lebih rendah daripada DMRA dan CPFP pada NJUD mendukung klaim ini. Dari sisi rekayasa, keterbatasan pertama adalah pelatihan multi-tugas menambah kerumitan penyetelan hyperparameter — bobot λ *depth* = 3 pada makalah menunjukkan sensitivitas terhadap pembobotan antar-tugas, yang berarti performa dapat berubah signifikan bila bobot ini tidak disetel dengan tepat pada dataset lain. Kedua, karena label tepi diturunkan otomatis dari kontur anotasi saliency memakai operator Canny, kualitas supervisi tepi bergantung pada akurasi anotasi asli; anotasi saliency yang kasar akan menghasilkan label tepi yang juga kasar. Ketiga, secara konseptual, meskipun *depth* tidak dibutuhkan saat inferensi, kualitas pembelajaran kolaborator *depth* selama pelatihan tetap bergantung pada ketersediaan data latih RGB-D berlabel yang memadai — keunggulan efisiensi saat inferensi tidak menghapus kebutuhan data *depth* berkualitas pada tahap pelatihan.

## Kaitan dengan Bab Lain

CoNet berada dalam garis metode RGB-D SOD yang mempertanyakan keharusan fusi dua-aliran penuh. Ia berbeda dari [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md), yang tetap memproses RGB dan *depth* sebagai dua aliran paralel dengan modul fusi bertingkat, dan dari [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md), yang menggabungkan kedua modal lewat pembelajaran gabungan pada satu jaringan siam. CoNet juga berbagi kepedulian terhadap kualitas *depth* dengan [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md), yang menyaring peta *depth* buruk sebelum fusi, tetapi menempuh jalan berbeda: alih-alih menyaring *depth* saat inferensi, CoNet meniadakan kebutuhan *depth* pada tahap itu sama sekali. Gagasan menangani ketidakandalan *depth* berlanjut pada [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md), yang mengalibrasi peta *depth* memakai isyarat RGB sebelum fusi timbal balik. Pemanfaatan tepi eksplisit untuk mempertajam batas saliency, sebagaimana pada kolaborator tepi CoNet, juga menjadi tema pada [168 - 2021 - SPNet - RGB-D SOD](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md) dan pada arsitektur berbasis *attention* lintas-modal seperti [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md). Perhatian terhadap efisiensi komputasi tanpa mengorbankan akurasi juga menjadi fokus [170 - 2022 - MobileSal - RGB-D SOD](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md), yang merancang arsitektur ringan untuk RGB-D SOD pada perangkat terbatas.

## Poin untuk Sitasi

Kutip dengan kunci `ji2020conet`. Ringkasan yang aman dikutip: "CoNet melatih tiga tugas berbagi *encoder* — saliency, tepi, dan *depth* — secara kolaboratif, dan menggunakan *depth* hanya sebagai supervisi pelatihan sehingga inferensi tidak memerlukan masukan *depth*, mencapai F-measure 0,872 dan MAE 0,047 pada NJUD, diklaim 55% lebih cepat daripada DMRA." Angka Fβ 0,872 / MAE 0,047 pada NJUD, perbandingan dengan DMRA (Fβ 0,872, MAE 0,051) dan CPFP (Fβ 0,850, MAE 0,053), ukuran model 167,6 MB, kecepatan 34 FPS, klaim "55% lebih cepat", serta bobot *loss* λ tepi=λ saliency=λ akhir=1 dan λ *depth*=3 diperoleh dari ekstraksi otomatis naskah arXiv (versi ar5iv) dan **wajib diverifikasi ulang terhadap tabel dan persamaan pada PDF asli atau versi ECCV/Springer** sebelum dikutip dalam karya formal, karena belum dicocokkan langsung dengan tabel makalah oleh penulis bab ini.
