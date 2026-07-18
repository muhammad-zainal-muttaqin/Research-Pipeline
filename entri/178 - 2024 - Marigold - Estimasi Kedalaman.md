# 178 - Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ke2024marigold` |
| Judul asli | Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation |
| Penulis | Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, Konrad Schindler |
| Tahun | 2024 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2312.02145
- **Halaman proyek dan kode resmi:** https://marigoldmonodepth.github.io
- **Google Scholar:** https://scholar.google.com/scholar?q=Repurposing%20Diffusion-Based%20Image%20Generators%20for%20Monocular%20Depth%20Estimation

## Gambaran Umum

Makalah ini memperkenalkan Marigold, metode estimasi kedalaman monokular (memperkirakan jarak setiap piksel ke kamera dari satu citra tunggal) yang dibangun dengan menyetel ulang model difusi laten Stable Diffusion — sebuah model generatif citra yang dilatih pada miliaran pasangan citra-teks — menjadi prediktor peta kedalaman. Alih-alih melatih arsitektur diskriminatif dari nol atau dari bobot klasifikasi ImageNet, penulis memanfaatkan pengetahuan visual yang sudah tertanam dalam model difusi hasil pralatih tersebut. Model disetel halus (*fine-tuning*, melanjutkan pelatihan bobot yang sudah ada pada data baru) hanya dengan data sintetis berpasangan citra-kedalaman, dalam waktu beberapa hari pada satu GPU tunggal, tanpa pernah melihat citra kedalaman nyata selama pelatihan. Hasilnya adalah peta kedalaman dengan detail struktur halus yang tinggi dan generalisasi *zero-shot* (kemampuan bekerja pada domain data yang tidak pernah dilihat saat pelatihan) yang kuat ke berbagai citra dunia nyata, dengan penulis melaporkan peningkatan performa lebih dari 20% pada sejumlah kasus dibandingkan metode pembanding.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra bersifat *ill-posed* (kurang terdefinisi secara matematis): satu citra dua dimensi dapat berasal dari tak terhingga banyak konfigurasi geometri tiga dimensi yang berbeda, sehingga menyelesaikannya membutuhkan pemahaman konteks visual, bukan sekadar perhitungan geometris. Sejak kemunculan pembelajaran dalam (*deep learning*), estimator kedalaman diskriminatif — model yang dilatih langsung memetakan citra ke peta kedalaman lewat regresi terarah — berkembang dari jaringan konvolusi sederhana ke arsitektur *Transformer* berskala besar, seperti yang dibahas pada bab 176 (ZoeDepth) dan bab 177 (Metric3D). Pendekatan ini menuntut data latih berlabel kedalaman dalam jumlah besar, baik dari sensor nyata maupun sintetis; performanya pada domain yang tidak terwakili dalam data latih sering menurun tajam karena pengetahuan model tentang dunia visual dibatasi ketat oleh apa yang dilihat selama pelatihan.

Model difusi generatif seperti Stable Diffusion dilatih pada korpus citra-teks berskala miliaran, sehingga menyimpan prior (pengetahuan awal implisit) yang jauh lebih kaya tentang struktur, tekstur, dan tata letak *scene* dibanding data kedalaman berlabel yang tersedia untuk melatih estimator diskriminatif. Pertanyaan yang mendasari makalah ini adalah apakah prior generatif seluas itu dapat dipindahkan (*repurposed*, dialihfungsikan) untuk tugas prediksi kedalaman yang detail dan general, tanpa memerlukan data nyata berlabel kedalaman dalam jumlah besar.

## Ide Utama

Gagasan inti Marigold adalah memperlakukan estimasi kedalaman sebagai proses *denoising* (penghilangan derau) bersyarat pada citra masukan, memakai arsitektur U-Net difusi yang sudah pralatih pada Stable Diffusion. Model difusi bekerja dengan melatih jaringan memprediksi dan mengurangi derau yang ditambahkan secara bertahap pada data, sehingga dari derau murni jaringan dapat merekonstruksi sampel data yang valid lewat iterasi berulang. Pada Marigold, "data" yang direkonstruksi bukan citra baru, melainkan peta kedalaman, dan proses *denoising* dikondisikan pada representasi laten citra masukan sehingga peta kedalaman yang dihasilkan konsisten dengan isi citra tersebut. Karena bobot awal U-Net sudah memahami struktur visual dari pelatihan generatif skala besar, penyetelan halus untuk tugas kedalaman hanya memerlukan data sintetis berpasangan citra-kedalaman dalam jumlah relatif kecil dan waktu pelatihan singkat, alih-alih data nyata masif yang biasa dibutuhkan pendekatan diskriminatif.

## Cara Kerja Langkah demi Langkah

### Ruang Laten dan Peran VAE

Stable Diffusion tidak bekerja langsung pada piksel, melainkan pada ruang laten (*latent space*) berdimensi lebih kecil, hasil kompresi oleh *variational autoencoder* (VAE) — jaringan yang terdiri atas *encoder* untuk memampatkan citra menjadi representasi laten kompak dan *decoder* untuk mengembalikannya ke citra piksel penuh. Marigold memanfaatkan VAE Stable Diffusion yang sama, tanpa pelatihan ulang, untuk dua keperluan: memampatkan citra RGB masukan menjadi laten citra, dan memampatkan peta kedalaman (direplikasi ke tiga kanal agar sesuai format VAE) menjadi laten kedalaman. Bekerja di ruang laten yang jauh lebih kecil daripada ruang piksel membuat proses *denoising* iteratif jauh lebih murah secara komputasi.

### Kondisi Citra pada U-Net Difusi

U-Net (arsitektur konvolusi berbentuk kontraksi-ekspansi dengan koneksi pintas antar-lapis sejajar) pada Stable Diffusion awalnya dirancang menerima satu laten sebagai masukan. Marigold memodifikasi lapis pertama U-Net agar menerima laten citra dan laten kedalaman yang sedang di-*denoise* sekaligus, digabungkan pada dimensi kanal (*channel concatenation*). Dengan susunan ini, pada setiap langkah *denoising* jaringan melihat kondisi citra secara langsung, sehingga prediksi derau yang dikeluarkan selalu konsisten dengan tata letak dan struktur citra tersebut. Bobot lapis pertama yang baru ini diinisialisasi dari bobot Stable Diffusion asli dan digandakan agar mampu menerima masukan berdimensi kanal dua kali lipat.

### Penyetelan Halus pada Data Sintetis

Model dilatih dengan fungsi *loss* difusi standar: pada setiap iterasi, sejumlah derau Gaussian ditambahkan ke laten kedalaman kebenaran (*ground truth*), lalu U-Net dilatih memprediksi derau tersebut, dikondisikan pada laten citra bersih dan tingkat derau saat itu. Pelatihan hanya memakai dataset sintetis berpasangan citra-kedalaman — Hypersim untuk *scene* dalam ruangan dan Virtual KITTI untuk *scene* luar ruangan/jalan raya — karena data sintetis menyediakan peta kedalaman padat dan bebas derau sensor yang sulit diperoleh dari data nyata. Karena bobot dasar U-Net sudah membawa prior visual dari pelatihan generatif awal, penyetelan halus ini hanya memerlukan beberapa hari pada satu GPU, jauh lebih ringan daripada melatih estimator kedalaman dari awal.

### Inferensi: Denoising Bertahap dan Ensembling

Pada saat inferensi, laten kedalaman dimulai dari derau acak murni, lalu didenoise secara bertahap melalui sejumlah langkah T, dengan U-Net memprediksi dan mengurangi derau pada setiap langkah, selalu dikondisikan pada laten citra masukan yang tetap. Setelah langkah terakhir, laten kedalaman hasil didekode oleh *decoder* VAE menjadi peta kedalaman piksel penuh. Karena proses ini bersifat stokastik (bergantung pada derau awal acak), Marigold dapat menjalankan beberapa lintasan *denoising* independen untuk citra yang sama dan merata-ratakan hasilnya — teknik yang disebut *ensembling* — untuk menstabilkan prediksi dan menekan variasi antar-lintasan. Peta kedalaman yang dihasilkan bersifat *affine-invariant* (invarian afin): nilai kedalaman benar hanya sampai faktor skala dan pergeseran yang tidak diketahui, bukan kedalaman metrik dalam satuan nyata, sehingga penyelarasan skala terhadap referensi diperlukan sebelum dibandingkan dengan kedalaman metrik.

Alur data dapat diringkas sebagai berikut:

```
citra RGB              peta kedalaman (target)
   │                          │
   ▼ encoder VAE              ▼ encoder VAE (replikasi 3 kanal)
laten citra              laten kedalaman + derau
   │                          │
   └──────────► gabung kanal ◄┘
                    │
                    ▼
         U-Net difusi (dari Stable Diffusion)
         prediksi derau, T langkah iteratif
                    │
                    ▼
           laten kedalaman bersih
                    │
                    ▼ decoder VAE
           peta kedalaman affine-invariant
```

## Eksperimen dan Hasil

Marigold dievaluasi secara *zero-shot* — tanpa penyetelan tambahan pada data target — pada sejumlah tolok ukur estimasi kedalaman standar yang mencakup *scene* dalam ruangan dan luar ruangan, meliputi NYU Depth V2, KITTI, ETH3D, ScanNet, dan DIODE. Karena model hanya dilatih pada data sintetis Hypersim dan Virtual KITTI, seluruh dataset evaluasi ini benar-benar tidak terlihat selama pelatihan, menjadikan pengujian ini tolok ukur generalisasi murni. Penulis melaporkan bahwa Marigold memberikan performa mutakhir (*state-of-the-art*) di sebagian besar tolok ukur tersebut, dengan peningkatan lebih dari 20% pada kasus tertentu dibandingkan metode pembanding sezaman. Metrik AbsRel (*Absolute Relative error*, rata-rata selisih absolut antara kedalaman prediksi dan kebenaran dibagi kedalaman kebenaran) dan δ1 (persentase piksel dengan rasio kedalaman prediksi terhadap kebenaran di bawah ambang 1,25) dipakai sebagai standar evaluasi, tetapi nilai numerik persisnya tidak dapat dipastikan tanpa merujuk langsung ke tabel pada naskah asli.

Studi ablasi (pengujian pengaruh tiap komponen dengan menghapusnya satu per satu) pada makalah menunjukkan bahwa jumlah langkah *denoising* dan ukuran *ensemble* memengaruhi keseimbangan antara akurasi dan waktu inferensi: lebih banyak langkah dan lebih banyak lintasan *ensemble* meningkatkan stabilitas dan detail prediksi, tetapi memperlambat inferensi secara proporsional. Repositori resmi proyek mencantumkan bahwa versi lanjutan model (v1.1) dapat berjalan dengan jumlah langkah *denoising* yang jauh lebih sedikit dibanding versi awal (v1.0) tanpa mengorbankan kualitas secara signifikan, menunjukkan bahwa jadwal *denoising* dapat dipersingkat melalui penyetelan lanjutan.

## Kelebihan dan Keterbatasan

Kelebihan utama Marigold adalah generalisasi *zero-shot* yang kuat ke domain di luar data latih, dicapai hanya dengan data sintetis dan tanpa memerlukan kedalaman nyata berlabel besar-besaran, berkat prior visual yang diwariskan dari model difusi pralatih. Detail struktur halus pada peta kedalaman yang dihasilkan juga lebih tajam dibandingkan banyak estimator diskriminatif sezaman, karena U-Net difusi telah terlatih menangkap tekstur dan batas objek secara presisi dari tugas generasi citra.

Dari sisi rekayasa, pendekatan ini menanggung biaya komputasi inferensi yang jauh lebih tinggi daripada estimator diskriminatif satu-lintasan seperti bab 175 (Depth Anything V2): karena kedalaman diperoleh lewat iterasi *denoising* bertahap, dan *ensembling* memerlukan pengulangan seluruh proses beberapa kali, waktu inferensi per citra meningkat berkali-lipat dibandingkan model umpan-maju (*feed-forward*) tunggal. Secara konseptual, keluaran Marigold bersifat affine-invariant, bukan kedalaman metrik, sehingga tidak dapat langsung dipakai pada aplikasi yang membutuhkan jarak dalam satuan nyata (misalnya navigasi robot) tanpa langkah penyelarasan skala tambahan, berbeda dengan metode yang secara eksplisit menargetkan kedalaman metrik seperti bab 177 (Metric3D). Kualitas hasil juga bergantung pada seberapa baik prior Stable Diffusion dasar mencakup jenis *scene* yang diuji; domain yang sangat jauh dari distribusi citra pelatihan Stable Diffusion berpotensi tetap menurunkan performa.

## Kaitan dengan Bab Lain

Bab ini berada dalam klaster Estimasi Kedalaman bersama bab 175 ([Depth Anything V2](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)), bab 176 ([ZoeDepth](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)), bab 177 ([Metric3D](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md)), dan bab 179 ([NeWCRFs](./179%20-%202022%20-%20NeWCRFs%20-%20Estimasi%20Kedalaman.md)). Berbeda dari keempatnya yang membangun estimator diskriminatif dilatih langsung pada tujuan regresi kedalaman, Marigold mewakili jalur alternatif: memanfaatkan model generatif pralatih berskala sangat besar sebagai sumber prior visual, lalu menyetel ulang tujuannya untuk prediksi padat (*dense prediction*). Depth Anything V2 mencapai generalisasi luas lewat data berlabel semu (*pseudo-label*) dalam volume masif, sementara Marigold mencapai tujuan serupa dengan volume data latih jauh lebih kecil tetapi memanfaatkan bobot pralatih generatif — kedua strategi menawarkan jalan berbeda menuju masalah generalisasi *zero-shot* yang sama. Metric3D dan ZoeDepth berfokus pada kedalaman metrik yang langsung dapat dipakai dalam satuan nyata, sedangkan keluaran affine-invariant Marigold menuntut kalibrasi tambahan sebelum dipakai pada peran serupa. Prinsip mengalihfungsikan model difusi pralatih untuk prediksi padat yang diperkenalkan Marigold turut memengaruhi metode-metode belakangan yang menerapkan pendekatan serupa pada tugas prediksi kedalaman dan estimasi properti *scene* lain.

## Poin untuk Sitasi

Kutip dengan kunci `ke2024marigold`. Ringkasan yang aman dikutip: "Marigold menyetel ulang model difusi laten Stable Diffusion menjadi estimator kedalaman monokular affine-invariant, dilatih hanya dengan data sintetis (Hypersim, Virtual KITTI) dalam beberapa hari pada satu GPU, dan mencapai generalisasi zero-shot yang kuat dengan peningkatan performa lebih dari 20% pada sejumlah tolok ukur dibandingkan metode pembanding." Catatan verifikasi sebelum sitasi formal: nilai numerik AbsRel dan δ1 per dataset (NYU, KITTI, ETH3D, ScanNet, DIODE) belum dapat dipastikan dari sumber yang diakses dan wajib dicek langsung ke tabel hasil pada naskah CVPR 2024; jumlah langkah *denoising* T standar dan ukuran *ensemble* default pada protokol evaluasi akademik makalah juga perlu dikonfirmasi ke naskah asli, karena angka pada repositori kode (versi v1.1 vs v1.0) dapat berbeda dari konfigurasi yang dipakai untuk pelaporan hasil di tabel makalah.
