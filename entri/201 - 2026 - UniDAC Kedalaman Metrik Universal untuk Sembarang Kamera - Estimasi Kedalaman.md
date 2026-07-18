# 201 - UniDAC: Universal Metric Depth Estimation for Any Camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ganesan2026unidac` |
| Judul asli | UniDAC: Universal Metric Depth Estimation for Any Camera |
| Penulis | Girish Chandar Ganesan, Yuliang Guo, Liu Ren, Xiaoming Liu |
| Tahun | 2026 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026); praversi arXiv:2603.27105 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2603.27105
- **Google Scholar:** https://scholar.google.com/scholar?q=UniDAC%3A%20Universal%20Metric%20Depth%20Estimation%20for%20Any%20Camera
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=UniDAC%3A%20Universal%20Metric%20Depth%20Estimation%20for%20Any%20Camera&sort=relevance

## Gambaran Umum

UniDAC mengusulkan sebuah kerangka *monocular metric depth estimation* (MMDE, estimasi kedalaman berskala nyata dari satu citra) yang bekerja untuk sembarang jenis kamera — perspektif biasa, *fisheye* (lensa sudut sangat lebar dengan distorsi radial kuat), maupun 360° (panorama penuh) — memakai satu model tunggal tanpa dilatih ulang atau dikalibrasi per kamera. Gagasan intinya adalah memecah masalah kedalaman metrik menjadi dua bagian yang lebih mudah digeneralisasi: prediksi kedalaman relatif (peta kedalaman yang benar urutannya tetapi belum berskala nyata) dan estimasi medan skala yang bervariasi secara spasial (faktor pengali per lokasi yang mengubah kedalaman relatif menjadi metrik). Model dilatih hanya pada citra perspektif berlabel kedalaman metrik, tetapi pada saat pengujian mampu menggeneralisasi ke citra *fisheye* dan 360° tanpa data pelatihan bersudut pandang lebar dan tanpa model terpisah per domain kamera. Menurut penulis, pendekatan ini mencapai kinerja *state-of-the-art* (tercanggih) pada generalisasi lintas kamera, mengungguli metode sebelumnya secara konsisten di seluruh himpunan data yang diuji.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman metrik dari satu citra RGB berbeda dari estimasi kedalaman relatif: kedalaman metrik menghasilkan jarak dalam satuan nyata (misalnya meter), sedangkan kedalaman relatif hanya menghasilkan urutan jarak antar-piksel tanpa skala pasti. Persoalan mendasar pada estimasi kedalaman metrik adalah ambiguitas skala-jarak (*scale ambiguity*): dari satu citra tunggal, objek besar yang jauh dan objek kecil yang dekat dapat menghasilkan proyeksi piksel yang identik, sehingga model harus menyimpulkan skala dari petunjuk geometris kamera, bukan hanya dari tekstur citra. Karena itu, keluaran metrik model sangat sensitif terhadap parameter intrinsik kamera (panjang fokus, titik pusat optis, dan koefisien distorsi) yang menentukan bagaimana titik tiga dimensi diproyeksikan ke piksel.

Metric3D (bab 177) dan ZoeDepth (bab 176) menunjukkan bahwa kedalaman metrik dapat digeneralisasi lintas dataset dengan mengondisikan model pada informasi kamera atau dengan menormalkan citra ke ruang kamera kanonik (representasi kamera acuan tunggal yang dipetakan balik ke kamera asli). Namun, metode-metode tersebut, sebagaimana juga UniDepth yang menjadi pembanding utama UniDAC, umumnya dilatih dan diuji pada kamera perspektif dengan bidang pandang (*field of view*, FOV — sudut cakupan citra) sempit hingga sedang. Kamera *fisheye* dan 360° memiliki distorsi geometris yang jauh lebih ekstrem: proyeksi ke bidang datar tidak lagi berlaku, dan representasi *equirectangular projection* (ERP — pemetaan bola 360° ke citra persegi panjang datar, umum dipakai untuk panorama) mengalami peregangan spasial yang tidak seragam, terutama di dekat kutub gambar. Pendahulu langsung UniDAC, Depth Any Camera atau DAC (Guo dkk., CVPR 2025), menunjukkan bahwa model yang dilatih murni pada citra perspektif dapat digeneralisasi ke *fisheye* dan 360° melalui pelatihan berbasis geometri, mengungguli Metric3D-v2 dan UniDepth pada data tersebut meski memakai data latih jauh lebih sedikit (sekitar 800 ribu citra dibandingkan 16 juta). Meski demikian, generalisasi lintas kamera pada metode-metode terdahulu — termasuk DAC — belum menyelesaikan persoalan skala yang bervariasi secara lokal di dalam satu citra bersudut lebar, karena satu faktor skala tunggal per citra tidak cukup ketika distorsi geometris berubah drastis dari pusat ke tepi bidang pandang.

## Ide Utama

UniDAC memisahkan prediksi kedalaman metrik menjadi dua keluaran yang dihasilkan secara terpisah lalu digabungkan: cabang kedalaman relatif yang memprediksi bentuk geometris adegan (urutan jarak antar-piksel, tanpa satuan), dan cabang skala yang memprediksi berapa faktor pengali dibutuhkan pada setiap lokasi citra agar kedalaman relatif tersebut menjadi metrik. Pemisahan ini penting karena kedua sub-masalah memiliki sifat generalisasi yang berbeda: bentuk geometris adegan (misalnya bahwa dinding lebih jauh daripada meja di depannya) relatif konsisten lintas jenis kamera, sedangkan skala metrik sangat bergantung pada parameter proyeksi kamera tertentu. Dengan memisahkan keduanya, model dapat menggeneralisasi bagian kedalaman relatif dari data perspektif yang berlimpah, sementara bagian skala dipelajari sebagai medan spasial (bukan angka tunggal) yang dapat menyesuaikan diri terhadap distorsi lokal pada kamera bersudut lebar, termasuk kamera yang tidak pernah dilihat model saat pelatihan.

## Cara Kerja Langkah demi Langkah

### Cabang Kedalaman Relatif

Jaringan tulang punggung (*backbone*, jaringan ekstraksi fitur utama) memproses citra masukan dan menghasilkan peta kedalaman relatif — nilai per piksel yang mencerminkan urutan jarak, dinormalisasi tanpa satuan nyata. Cabang ini dilatih agar tidak bergantung pada geometri proyeksi kamera tertentu, sehingga polanya dapat dipelajari dari citra perspektif biasa dan tetap berlaku ketika diuji pada citra *fisheye* atau ERP.

### Modul Depth-Guided Scale Estimation (DGSE)

Modul ini memprediksi peta skala kasar beresolusi rendah, kemudian menaikkan resolusinya (*upsampling*) ke resolusi penuh dengan memakai peta kedalaman relatif sebagai penuntun. Penuntunan ini serupa dengan penapisan sadar-tepi (*edge-aware filtering*): batas objek pada peta kedalaman relatif dipakai untuk menjaga agar transisi skala tidak melebar melewati batas objek saat resolusi dinaikkan. Hasil akhirnya adalah medan skala beresolusi tinggi yang bervariasi antar-lokasi dalam satu citra, bukan satu angka skala global seperti pada pendekatan yang lebih sederhana. Kedalaman metrik akhir diperoleh dengan mengalikan peta kedalaman relatif dengan medan skala ini secara per piksel.

### RoPE-φ untuk Citra Equirectangular Projection

Untuk menangani citra 360° dalam format ERP, UniDAC memperkenalkan RoPE-φ, sebuah modifikasi dari *Rotary Positional Embedding* (RoPE — teknik penyematan posisi pada arsitektur *transformer* yang mengkodekan posisi token lewat rotasi vektor fitur). Penyematan posisi standar mengasumsikan kisi piksel yang seragam, padahal pada proyeksi ERP, satu baris piksel dekat kutub (bagian atas/bawah panorama) mewakili wilayah sudut pandang riil yang jauh lebih sempit dibandingkan satu baris piksel di dekat garis khatulistiwa citra — inilah peregangan spasial yang disebutkan pada bagian latar belakang. RoPE-φ menimbang penyematan posisi berdasarkan garis lintang (*latitude-aware weighting*) sehingga jaringan memperlakukan jarak antar-piksel sesuai sudut pandang riilnya, bukan sesuai jarak piksel mentah pada citra ERP yang sudah terdistorsi.

Alur ringkas dari citra masukan ke kedalaman metrik dapat digambarkan sebagai berikut:

```
citra masukan (perspektif / fisheye / ERP 360)
            │
            ▼
   backbone + RoPE-φ (bila ERP)
            │
   ┌────────┴────────┐
   ▼                  ▼
cabang kedalaman   cabang skala kasar
relatif (per piksel) │
   │              modul DGSE: upsampling
   │              dituntun kedalaman relatif
   │                  │
   └──────► perkalian per piksel ◄──┘
                  │
                  ▼
         peta kedalaman metrik
```

Diagram ini menegaskan bahwa kedua cabang bekerja paralel sebelum digabungkan lewat perkalian, bukan lewat tahap berurutan seperti pada model kanonik-lalu-skala pada Metric3D.

### Pelatihan Lintas-Domain tanpa Data Bersudut Lebar

Berbeda dari pendekatan yang menambahkan citra *fisheye*/360° ke data pelatihan, atau melatih model terpisah untuk setiap domain kamera, UniDAC dilatih seluruhnya pada citra perspektif berlabel kedalaman metrik. Generalisasi ke kamera bersudut lebar diperoleh dari kombinasi desain cabang relatif yang tidak bergantung geometri proyeksi, modul DGSE yang bekerja secara lokal per piksel, dan RoPE-φ yang mengoreksi distorsi ERP pada tahap pengkodean posisi — bukan dari paparan langsung terhadap data pelatihan bersudut lebar.

## Eksperimen dan Hasil

Evaluasi generalisasi kamera dilakukan pada berkas data dengan model distorsi berbeda-beda: ScanNet++ dan KITTI-360 untuk kamera *fisheye* — masing-masing mengikuti model distorsi Kannala-Brandt (KB) dan model Mei (MEI), dua parameterisasi matematis berbeda untuk memetakan sudut datang cahaya ke posisi piksel pada lensa sudut lebar — serta Pano3D-GV2 dan Matterport3D untuk citra 360° dalam format ERP. Metrik evaluasi yang lazim dipakai pada literatur kedalaman metrik adalah AbsRel (*Absolute Relative error*, rata-rata selisih absolut kedalaman prediksi terhadap kebenaran lapangan dibagi kedalaman kebenaran lapangan; makin kecil makin baik), RMSE (*Root Mean Square Error*, akar rata-rata kuadrat galat; makin kecil makin baik), dan delta<1.25 (persentase piksel yang rasio prediksi-terhadap-kebenarannya berada dalam rentang toleransi 1,25 kali; makin besar makin baik).

Menurut ringkasan yang berhasil diverifikasi dari sumber sekunder, UniDAC mengungguli pembanding utama — UniDepth, Metric3D-v2, dan DAC — secara konsisten pada seluruh dataset uji tersebut dengan satu model tunggal, tanpa memerlukan data pelatihan bersudut lebar maupun model terpisah per domain. Namun, angka AbsRel/RMSE/delta<1.25 yang tepat untuk masing-masing dataset dan pembanding tidak berhasil diambil dari naskah utama dalam riset ini, karena berkas PDF penuh melebihi batas pengambilan otomatis dan halaman prosiding CVPR memblokir akses langsung. Nilai numerik hasil eksperimen harus dikonfirmasi langsung dari naskah arXiv 2603.27105 atau tabel resmi prosiding CVPR 2026 sebelum dikutip dalam karya formal.

## Kelebihan dan Keterbatasan

Kelebihan utama UniDAC adalah kemampuan menggeneralisasi ke kamera *fisheye* dan 360° hanya dari pelatihan pada citra perspektif, menghindari kebutuhan mengumpulkan data metrik berlabel untuk setiap jenis kamera baru — sebuah hambatan praktis yang nyata karena data kedalaman metrik berlabel untuk kamera bersudut sangat lebar jauh lebih langka daripada untuk kamera perspektif. Pemisahan kedalaman relatif dan skala spasial memberi kerangka yang secara konseptual masuk akal untuk sumber ambiguitas skala, dan modul DGSE mengatasi keterbatasan pendekatan skala tunggal-per-citra dengan memungkinkan variasi skala lokal.

Dari sisi rekayasa, kerangka ini menambah kompleksitas dibandingkan model kedalaman metrik satu cabang: dua cabang prediksi, modul *upsampling* berpandu, dan skema penyematan posisi khusus ERP berarti lebih banyak komponen yang harus dilatih dan diselaraskan dengan benar agar perkalian kedalaman relatif dan skala menghasilkan keluaran metrik yang konsisten. Secara konseptual, keandalan RoPE-φ bergantung pada asumsi bahwa distorsi kamera dapat dikarakterisasi lewat parameter geometris yang diketahui (model proyeksi ERP, KB, atau MEI); kamera dengan model distorsi di luar kategori tersebut, atau distorsi tidak reguler akibat kerusakan lensa, berpotensi berada di luar jangkauan generalisasi yang telah diverifikasi. Karena makalah ini baru dipublikasikan pada 2026, belum tersedia validasi independen dari kelompok riset lain, dan kode sumber publik belum berhasil ditelusuri pada riset ini — replikasi hasil belum dapat dipastikan.

## Kaitan dengan Bab Lain

UniDAC melanjutkan garis kerja kedalaman metrik lintas domain yang dirintis Metric3D ([bab 177](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md)) lewat ruang kamera kanonik dan ZoeDepth ([bab 176](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)) lewat penggabungan kedalaman relatif dan metrik, tetapi mengganti strategi kanonisasi tunggal dengan pemisahan eksplisit cabang relatif dan medan skala spasial. Secara arsitektural, cabang kedalaman relatif UniDAC berdiri di atas garis kerja fondasi model kedalaman relatif berskala besar seperti Depth Anything V2 ([bab 175](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)), yang menunjukkan bahwa kedalaman relatif dapat dipelajari secara sangat general dari data berlimpah sebelum digabungkan dengan informasi skala metrik. Posisi UniDAC dalam peta metode kedalaman metrik monokular dapat dibandingkan dengan taksonomi yang disusun pada survei bab 199 ([Survei Estimasi Kedalaman Metrik Monokular](./199%20-%202025%20-%20Survei%20Estimasi%20Kedalaman%20Metrik%20Monokular%20-%20Estimasi%20Kedalaman.md)), khususnya pada kategori metode yang menangani variasi parameter kamera. Dalam klaster kedalaman 2026, UniDAC melengkapi AsyncMDE ([bab 200](./200%20-%202026%20-%20AsyncMDE%20Kedalaman%20Monokular%20Real-Time%20Memori%20Spasial%20-%20Estimasi%20Kedalaman.md)), yang menyasar efisiensi waktu-nyata dengan memori spasial, dan Focusable Monocular Depth Estimation ([bab 202](./202%20-%202026%20-%20Focusable%20Monocular%20Depth%20Estimation%20-%20Estimasi%20Kedalaman.md)), yang menyasar kontrol area fokus prediksi; ketiganya menunjukkan bahwa perbaikan kedalaman monokular pada 2026 bergerak ke arah kebutuhan penerapan spesifik — generalisasi kamera, kecepatan, dan kontrol pengguna — di atas fondasi kedalaman metrik yang sudah cukup matang.

## Poin untuk Sitasi

Kutip dengan kunci `ganesan2026unidac`. Ringkasan yang aman dikutip: "UniDAC (Ganesan, Guo, Ren, dan Liu, CVPR 2026) mengusulkan estimasi kedalaman metrik monokular yang menggeneralisasi ke kamera perspektif, *fisheye*, dan 360° dengan satu model, melalui pemisahan cabang kedalaman relatif dan medan skala spasial yang dihasilkan modul Depth-Guided Scale Estimation, serta penyematan posisi RoPE-φ untuk citra *equirectangular projection*." Klaim berikut belum terverifikasi langsung dari naskah utama dan wajib dikonfirmasi sebelum dikutip formal: (1) seluruh angka AbsRel, RMSE, dan delta<1.25 pada dataset ScanNet++, KITTI-360, Pano3D-GV2, dan Matterport3D; (2) afiliasi institusi masing-masing penulis; (3) rincian arsitektur *backbone* dan ukuran model; (4) ketersediaan dan tautan kode sumber publik. Klaim keunggulan atas UniDepth, Metric3D-v2, dan DAC berasal dari ringkasan sumber sekunder yang mengacu pada abstrak dan bagian metode makalah, bukan dari pembacaan langsung tabel hasil.
