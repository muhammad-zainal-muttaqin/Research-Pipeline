# 199 - Survey on Monocular Metric Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2025metricdepthsurvey` |
| Judul asli | Survey on Monocular Metric Depth Estimation |
| Penulis | Jiuling Zhang |
| Tahun | 2025 |
| Venue | arXiv preprint (arXiv:2501.11841) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2501.11841
- **Google Scholar:** https://scholar.google.com/scholar?q=Survey%20on%20Monocular%20Metric%20Depth%20Estimation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Survey%20on%20Monocular%20Metric%20Depth%20Estimation&sort=relevance

## Gambaran Umum

Makalah ini adalah survei yang merangkum perkembangan *Monocular Metric Depth Estimation* (MMDE, estimasi kedalaman metrik dari satu citra), yaitu cabang estimasi kedalaman monokular (*Monocular Depth Estimation*/MDE) yang keluarannya berupa peta kedalaman dengan skala nyata (metrik), bukan sekadar urutan jarak relatif antarpiksel. Survei ini menelusuri evolusi MMDE dari metode berbasis geometri klasik hingga model pembelajaran mendalam (*deep learning*) mutakhir, dengan penekanan khusus pada peran kumpulan data (*dataset*) sebagai pendorong kemajuan bidang ini. Empat tolok ukur (*benchmark*) utama dibahas dari segi modalitas, jenis adegan (*scene*), dan domain aplikasinya: KITTI, NYU-D, ApolloScape, dan TartanAir.

Kontribusi utama makalah bukan metode baru, melainkan sintesis: pengelompokan kemajuan metodologis — generalisasi lintas domain, pelestarian batas objek pada peta kedalaman, serta pemaduan data sintetis dan data nyata — dan evaluasi berimbang atas sejumlah teknik, meliputi pembelajaran tanpa-pengawasan (*unsupervised*) dan semi-pengawasan (*semi-supervised*), inferensi berbasis potongan citra (*patch-based inference*), inovasi arsitektur, serta pemodelan generatif berbasis difusi. Pembaca yang hanya mengambil bagian ini memperoleh inti bab: makalah berperan sebagai peta rujukan MMDE per awal 2025, bukan sumber angka hasil tunggal untuk dikutip.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra RGB adalah persoalan bermakna ganda (*ill-posed*): dari satu citra saja, secara matematis tidak ada solusi tunggal yang pasti benar, karena kombinasi jarak objek dan ukuran objek yang berbeda dapat menghasilkan citra yang identik pada bidang gambar. Sebagian besar pendekatan pembelajaran mendalam yang berkembang sejak pertengahan dekade 2010-an mengatasi ambiguitas ini dengan memprediksi kedalaman **relatif** — urutan jarak antarbagian citra tanpa satuan nyata. Keluaran semacam ini memadai untuk tugas seperti penyusunan ulang tampilan (*view synthesis*) sederhana, tetapi tidak dapat langsung dipakai pada aplikasi yang menuntut jarak sebenarnya dalam meter, misalnya *Simultaneous Localization and Mapping* (SLAM, penentuan posisi kamera dan pemetaan lingkungan secara bersamaan), pemodelan 3D presisi, atau navigasi robot — kecuali dilakukan kalibrasi tambahan yang merepotkan penerapan.

Masalah kedua yang diangkat survei ini adalah generalisasi lintas kamera dan domain. Model yang dilatih pada satu kumpulan data dengan parameter intrinsik kamera tertentu (fokus lensa, ukuran sensor) sering gagal memprediksi skala metrik yang benar ketika dihadapkan pada kamera atau adegan berbeda, karena hubungan antara ukuran objek pada citra dan jarak sebenarnya bergantung langsung pada parameter kamera tersebut. Masalah ketiga adalah hilangnya detail pada batas objek (*boundary*): banyak arsitektur cenderung menghaluskan tepi antarobjek, sehingga kontur benda kabur pada peta kedalaman yang dihasilkan. Karena jumlah metode yang mencoba mengatasi ketiga masalah ini bertambah cepat dan tersebar pada arsitektur yang beragam, survei ini disusun untuk memberi taksonomi terpadu yang memetakan hubungan antarmetode.

## Ide Utama

Sebagai makalah survei, gagasan intinya bukan mekanisme model baru, melainkan kerangka klasifikasi yang menempatkan metode MMDE ke dalam kategori berdasarkan dua sumbu: bagaimana metode memperoleh sinyal pelatihan (berbasis geometri, diawasi penuh, diawasi sebagian, atau tanpa pengawasan) dan bagaimana metode menangani ambiguitas skala metrik (memprediksi kedalaman metrik langsung dari data berlabel skala nyata, atau memprediksi kedalaman relatif terlebih dahulu kemudian menyisipkan informasi skala lewat parameter kamera). Sumbu kedua inilah yang menjadi benang merah pembeda MMDE generasi lama dan generasi model fondasi (*foundation model*) terbaru: metode lama umumnya dilatih ulang per kumpulan data dengan skala metrik yang tetap, sedangkan metode fondasi terbaru dirancang agar satu model dapat menghasilkan kedalaman metrik yang benar pada kamera dan domain yang belum pernah dilihat saat pelatihan (generalisasi *zero-shot*, yaitu kinerja pada data yang sama sekali baru tanpa pelatihan tambahan).

## Cara Kerja Langkah demi Langkah

### Kelompok Metode Berbasis Geometri dan Diawasi Klasik

Sebelum era pembelajaran mendalam dominan, kedalaman metrik diturunkan dari isyarat geometris eksplisit: pergeseran piksel pada pasangan citra stereo (disparitas), pergerakan piksel pada video (*structure from motion*), atau sensor tambahan. Generasi awal pembelajaran mendalam menggantikan sebagian isyarat ini dengan jaringan konvolusi yang dilatih memakai peta kedalaman berlabel dari sensor LiDAR atau kamera depth. Survei mencatat pendekatan berbasis pembagian rentang kedalaman menjadi kelas-kelas diskret (*binning*), tempat jaringan memprediksi probabilitas setiap piksel termasuk kelas rentang jarak tertentu alih-alih meregresi satu angka kontinu langsung — strategi ini mengurangi ketidakstabilan pelatihan dibanding regresi langsung.

### Kelompok Metode Semi- dan Tanpa-Pengawasan

Karena label kedalaman metrik mahal diperoleh (memerlukan sensor khusus), sekelompok metode memakai sinyal pelatihan tidak langsung. Pendekatan tanpa-pengawasan memanfaatkan konsistensi fotometrik: citra pada satu waktu diproyeksikan ulang ke waktu lain memakai kedalaman dan pergerakan kamera yang diprediksi, lalu selisih dengan citra asli dipakai sebagai sinyal galat. Pendekatan semi-pengawasan menggabungkan sebagian label nyata dengan sinyal konsistensi ini, mengurangi kebutuhan data berlabel penuh tanpa kehilangan patokan skala metrik.

### Kelompok Model Fondasi dan Strategi Scale-Agnostic

Kelompok ini adalah fokus utama perkembangan terbaru yang disorot survei. Model fondasi dilatih pada gabungan besar kumpulan data lintas domain (dalam ruangan, luar ruangan, sintetis, nyata) agar representasi fitur yang dipelajari cukup umum untuk digeneralisasi. Untuk menangani perbedaan skala antarkumpulan data pelatihan, sebagian metode memakai strategi *scale-agnostic* (tak bergantung skala tunggal): kedalaman relatif diprediksi lebih dulu oleh tulang punggung (*backbone*) bersama, kemudian kepala jaringan terpisah menyisipkan faktor skala metrik berdasarkan parameter kamera atau kepala regresi tambahan. Pendekatan ini memisahkan masalah "bentuk permukaan adegan" dari masalah "berapa skala sebenarnya", sehingga bagian pertama dapat dilatih pada data lintas domain yang jauh lebih banyak, sementara bagian kedua ditangani terpisah.

Skema hubungan antara dua sumbu klasifikasi tersebut dapat digambarkan sebagai berikut:

```
Sumber sinyal pelatihan        Penanganan skala metrik
┌─────────────────────┐        ┌──────────────────────────┐
│ berbasis geometri    │        │ metrik langsung            │
│ diawasi penuh         │──────▶│ (dilatih per skala tetap)  │
│ semi-diawasi          │        ├──────────────────────────┤
│ tanpa pengawasan      │──────▶│ relatif + skala terpisah   │
└─────────────────────┘        │ (scale-agnostic, zero-shot)│
                                └──────────────────────────┘
```

Diagram ini menunjukkan bahwa metode lama umumnya berujung pada kolom "metrik langsung", sedangkan sebagian besar model fondasi terbaru berujung pada kolom "relatif + skala terpisah" karena kolom ini yang memungkinkan generalisasi lintas kamera.

### Kelompok Model Difusi Generatif

Bagian akhir taksonomi membahas model difusi (*diffusion model*, model generatif yang belajar membalikkan proses penambahan derau bertahap pada data) yang diadaptasi untuk estimasi kedalaman. Karena model difusi awalnya dilatih untuk menghasilkan citra realistis dengan detail frekuensi tinggi, adaptasinya untuk kedalaman berpotensi memulihkan detail tepi objek yang lazim hilang pada arsitektur regresi langsung. Survei menempatkan kelompok ini sebagai arah yang masih berkembang, dengan biaya komputasi inferensi yang umumnya lebih tinggi dibanding jaringan regresi satu tahap.

### Peran Kumpulan Data dan Inferensi Berbasis Potongan

Survei menekankan bahwa kemajuan MMDE tidak dapat dipisahkan dari ketersediaan data pelatihan yang beragam. Karena resolusi tinggi dan variasi skala adegan sulit ditangani jaringan tunggal secara langsung, sebagian metode memproses citra sebagai potongan-potongan (*patch*) yang dievaluasi terpisah kemudian digabungkan (*patch-based inference*), sehingga detail resolusi tinggi tetap terjaga tanpa membengkakkan kebutuhan memori.

## Eksperimen dan Hasil

Survei ini bukan penelitian eksperimen baru, melainkan tinjauan sistematis atas hasil yang telah dilaporkan pada literatur MMDE. Empat kumpulan data disorot sebagai tolok ukur utama: KITTI (adegan luar ruangan dari kendaraan berkamera, umum dipakai untuk skenario mengemudi otonom), NYU-D atau NYU Depth v2 (adegan dalam ruangan berlabel kedalaman dari sensor Kinect), ApolloScape (kumpulan data luar ruangan berskala besar untuk mengemudi otonom dengan anotasi padat), dan TartanAir (kumpulan data sintetis yang mencakup kondisi lingkungan sulit seperti pencahayaan ekstrem dan cuaca beragam). Setiap kumpulan data dibandingkan dari segi modalitas sensor, jenis adegan, dan domain aplikasi yang diwakilinya — perbandingan ini menjadi dasar bagi survei untuk menjelaskan mengapa model yang unggul pada satu kumpulan data belum tentu digeneralisasi ke kumpulan data lain.

Metrik evaluasi standar yang dirujuk mengikuti konvensi umum literatur MDE: *Absolute Relative Error* (AbsRel, rata-rata selisih absolut antara kedalaman prediksi dan kebenaran lapangan dibagi kedalaman kebenaran lapangan — makin kecil makin baik), *Root Mean Square Error* (RMSE, akar rata-rata kuadrat selisih dalam satuan meter), dan akurasi ambang delta (δ < 1,25; δ < 1,25²; δ < 1,25³ — persentase piksel yang rasio prediksi-terhadap-kebenarannya berada di bawah ambang tertentu, makin besar makin baik). Survei menyintesis pola umum dari metrik-metrik ini lintas metode, bukan melaporkan tabel angka barunya sendiri; karena itu, angka spesifik per metode pada makalah ini perlu dicek langsung ke naskah sebelum dikutip sebagai perbandingan kuantitatif.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah cakupannya yang menyatukan dua sumbu klasifikasi (sumber sinyal pelatihan dan strategi penanganan skala) yang pada literatur asli tersebar di berbagai makalah individual tanpa kerangka pembanding yang seragam. Penekanan pada peran kumpulan data — bukan hanya arsitektur — juga relevan secara praktis karena banyak kegagalan generalisasi MMDE pada penerapan nyata bersumber dari ketidaksesuaian domain data pelatihan, bukan semata keterbatasan arsitektur.

Dari sisi rekayasa, keterbatasan struktural survei adalah tidak adanya kontribusi metode baru maupun eksperimen ulang yang independen; seluruh angka dan klaim kinerja bersumber dari makalah asli masing-masing metode, sehingga kesalahan pelaporan pada sumber aslinya berpotensi terbawa. Secara konseptual, karena makalah ini adalah prapublikasi (*preprint*) yang terus direvisi — versi terbaru tercatat Agustus 2025 — cakupan metode bergantung pada tanggal revisi yang dipakai; metode yang dipublikasikan setelah revisi terakhir tidak tercakup. Survei juga tidak melaporkan metodologi seleksi makalah secara eksplisit (misalnya kriteria basis data pencarian atau rentang tahun sistematis), sehingga cakupannya kemungkinan mengikuti penilaian penulis, bukan protokol survei sistematis formal.

## Kaitan dengan Bab Lain

Makalah ini berfungsi sebagai peta payung bagi metode-metode individual pada klaster Estimasi Kedalaman dalam tinjauan ini. Sebagian metode yang termasuk dalam taksonomi survei — model fondasi dan pendekatan *scale-agnostic* — dibahas tersendiri pada [175 - 2024 - Depth Anything V2 - Estimasi Kedalaman](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md) sebagai model fondasi kedalaman relatif dan metrik, [176 - 2023 - ZoeDepth - Estimasi Kedalaman](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md) sebagai contoh arsitektur yang menggabungkan pelatihan kedalaman relatif dan metrik, [177 - 2023 - Metric3D - Estimasi Kedalaman](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md) sebagai metode prediksi kedalaman metrik zero-shot lintas kamera, [178 - 2024 - Marigold - Estimasi Kedalaman](./178%20-%202024%20-%20Marigold%20-%20Estimasi%20Kedalaman.md) sebagai representasi kelompok model difusi generatif yang disorot survei, dan [179 - 2022 - NeWCRFs - Estimasi Kedalaman](./179%20-%202022%20-%20NeWCRFs%20-%20Estimasi%20Kedalaman.md) sebagai contoh arsitektur diawasi penuh berbasis medan acak bersyarat (*conditional random field*) yang mewakili generasi metode sebelum era model fondasi.

Bab ini sebaiknya dibaca sebelum kelima bab tersebut ketika pembaca memerlukan konteks posisi setiap metode dalam lanskap MMDE secara keseluruhan, dan dibaca kembali setelahnya untuk menilai sejauh mana klaim generalisasi tiap metode individual konsisten dengan tantangan umum yang diidentifikasi survei ini.

## Poin untuk Sitasi

Kutip dengan kunci `zhang2025metricdepthsurvey`. Ringkasan yang aman dikutip: "Survei ini menelusuri evolusi estimasi kedalaman metrik monokular dari metode berbasis geometri hingga model pembelajaran mendalam mutakhir, dengan penekanan pada peran kumpulan data KITTI, NYU-D, ApolloScape, dan TartanAir, serta menganalisis kemajuan metodologis pada generalisasi domain, pelestarian batas objek, dan pemaduan data sintetis-nyata." Rincian taksonomi metode spesifik (daftar lengkap metode per kategori seperti AdaBins, BinsFormer, PatchFusion, UniDepth, GeoWizard) diperoleh dari ringkasan otomatis atas isi naskah, bukan pembacaan langsung tabel taksonomi asli, sehingga penempatan metode ke kategori tertentu **wajib diverifikasi ulang** ke naskah sebelum dikutip. Metrik evaluasi (AbsRel, RMSE, delta<1,25) mengikuti konvensi umum bidang dan kemungkinan besar dipakai naskah, tetapi angka hasil kuantitatif per metode tidak dikutip di bab ini dan harus diambil langsung dari naskah asli.
