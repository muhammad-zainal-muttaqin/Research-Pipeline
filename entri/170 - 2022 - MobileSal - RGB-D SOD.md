# 170 - MobileSal: Extremely Efficient RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2022mobilesal` |
| Judul asli | MobileSal: Extremely Efficient RGB-D Salient Object Detection |
| Penulis | Yu-Huan Wu, Yun Liu, Jun Xu, Jia-Wang Bian, Yu-Chao Gu, Ming-Ming Cheng |
| Tahun | 2022 |
| Venue | IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2012.13095
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=MobileSal%3A%20Extremely%20Efficient%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=MobileSal%3A%20Extremely%20Efficient%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini mengajukan MobileSal, jaringan *RGB-D Salient Object Detection* (SOD, deteksi objek paling menonjol pada citra) yang dirancang untuk berjalan pada perangkat dengan sumber daya komputasi terbatas. Berbeda dari mayoritas metode RGB-D SOD sebelumnya yang memakai *backbone* (jaringan ekstraksi fitur utama) berat seperti VGG atau ResNet dengan puluhan juta parameter, MobileSal memakai jaringan mobile ringan sebagai *backbone* dan menambahkan dua komponen baru: *Implicit Depth Restoration* (IDR, pemulihan kedalaman implisit) dan *Compact Pyramid Refinement* (CPR, penyempurnaan piramida ringkas). IDR memanfaatkan citra kedalaman (*depth map* — citra yang setiap pikselnya menyatakan jarak permukaan ke kamera) hanya selama pelatihan untuk memperkuat representasi fitur *backbone*, sehingga saat inferensi tidak ada biaya komputasi tambahan akibat pemrosesan kedalaman. CPR menggabungkan fitur dari berbagai tingkat kedalaman jaringan secara hemat komputasi untuk menghasilkan peta saliency dengan batas objek yang tegas.

Menurut naskah, MobileSal diuji pada tujuh tolok ukur (*benchmark*) RGB-D SOD standar dan mencapai kecepatan 450 *frame* per detik (FPS) pada resolusi masukan 320×320 di GPU RTX 2080Ti, dengan hanya 6,5 juta parameter — jauh di bawah model RGB-D SOD berat yang umumnya berjumlah puluhan juta parameter. Kontribusi utamanya adalah menunjukkan bahwa efisiensi ekstrem dan akurasi kompetitif dapat dicapai bersamaan pada tugas RGB-D SOD, membuka jalan bagi penerapan pada perangkat mobile dan sistem *real-time*.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Metode RGB-D SOD yang berkembang pada periode 2019-2021 — termasuk DMRA, CPFP, D3Net, S2MA, dan JL-DCF — berfokus pada peningkatan akurasi fusi lintas-modal (penggabungan fitur RGB dan kedalaman) memakai *backbone* konvolusi berat dan modul fusi bertingkat yang rumit. Bab-bab lain dalam klaster RGB-D SOD pada tinjauan ini, misalnya CoNet (bab 166), DCF (bab 167), SPNet (bab 168), dan CAVER (bab 169), juga menekankan strategi fusi yang semakin canggih — kolaborasi multi-cabang, kalibrasi fitur dinamis, atau *attention* lintas-modal berbasis *transformer*. Strategi-strategi ini menaikkan akurasi tetapi juga menaikkan jumlah parameter dan biaya komputasi, karena setiap peningkatan kualitas fusi umumnya menambah cabang jaringan atau lapisan pemrosesan baru.

Konsekuensinya, model-model tersebut sulit dijalankan secara *real-time* pada perangkat dengan daya komputasi terbatas, seperti telepon pintar, kamera edge, atau robot kecil. Pemrosesan citra kedalaman itu sendiri turut menambah beban: banyak metode memakai cabang encoder terpisah khusus untuk kedalaman, sehingga total komputasi kira-kira berlipat dibandingkan jaringan RGB tunggal. Pada saat yang sama, citra kedalaman yang diperoleh dari sensor murah atau estimasi monokuler sering kali berderau atau memiliki resolusi rendah, sehingga manfaat akurasinya tidak selalu sepadan dengan biaya komputasi yang ditanggung. Masalah yang diangkat MobileSal adalah bagaimana mempertahankan manfaat informasi kedalaman untuk RGB-D SOD tanpa menanggung biaya komputasi cabang kedalaman saat inferensi, sekaligus memakai *backbone* seringan mungkin agar model dapat berjalan pada perangkat mobile.

## Ide Utama

Gagasan inti MobileSal adalah memisahkan peran citra kedalaman antara fase pelatihan dan fase inferensi. Selama pelatihan, jaringan diberi tugas tambahan berupa memulihkan informasi kedalaman dari fitur RGB yang sudah diekstraksi *backbone* — sebuah tugas bantu (*auxiliary task*) yang memaksa *backbone* mempelajari fitur yang lebih peka terhadap struktur geometris adegan, seperti batas objek dan urutan kedalaman relatif antarbagian citra. Setelah pelatihan selesai, cabang pemulihan kedalaman ini dibuang; saat inferensi, jaringan hanya memproses citra RGB melalui *backbone* mobile yang sudah "terlatih dipandu kedalaman", tanpa perlu memproses peta kedalaman sama sekali. Dengan demikian, manfaat informasi kedalaman terserap ke dalam bobot jaringan tanpa menambah komputasi saat digunakan.

Gagasan kedua adalah menyempurnakan fitur multi-tingkat dari *backbone* mobile memakai modul ringkas berbentuk piramida, bukan modul fusi lintas-modal yang berat seperti pada metode-metode sebelumnya. Karena cabang kedalaman sudah tidak ada saat inferensi, penyempurnaan ini hanya perlu menggabungkan fitur RGB dari berbagai resolusi di dalam satu jaringan, sehingga jumlah parameter dan operasi yang dibutuhkan jauh lebih sedikit dibandingkan modul fusi dua-cabang.

## Cara Kerja Langkah demi Langkah

### Backbone Mobile

MobileSal memakai jaringan konvolusi mobile — kelas jaringan seperti MobileNet yang menggantikan konvolusi standar dengan konvolusi *depthwise separable* (konvolusi yang memisahkan pemrosesan spasial per kanal dari penggabungan antarkanal) untuk memangkas jumlah operasi dan parameter secara drastis dibandingkan konvolusi biasa. *Backbone* ini mengekstraksi fitur RGB pada beberapa tingkat resolusi, dari resolusi tinggi dengan detail spasial halus di lapisan awal hingga resolusi rendah dengan konteks semantik luas di lapisan akhir. Fitur multi-tingkat inilah yang menjadi masukan bagi modul CPR pada tahap berikutnya.

### Implicit Depth Restoration (IDR)

IDR ditempatkan sebagai cabang tambahan yang aktif hanya selama pelatihan. Cabang ini mengambil fitur dari *backbone* RGB dan dilatih memprediksi peta kedalaman yang berpadanan dengan citra RGB masukan, memakai fungsi kerugian (*loss function*) regresi terhadap kedalaman sebenarnya dari data latih berpasangan RGB-D. Karena tugas ini dipaksakan pada representasi *backbone* yang sama yang dipakai untuk memprediksi saliency, *backbone* terdorong mempelajari fitur yang lebih sensitif terhadap batas objek dan struktur tiga dimensi adegan — sifat yang relevan bagi deteksi objek menonjol tetapi biasanya baru diperoleh lewat cabang kedalaman eksplisit pada metode lain. Sebagai contoh konseptual, dua objek dengan warna dan tekstur serupa namun berada pada jarak berbeda dari kamera akan menghasilkan sinyal pemulihan kedalaman yang berbeda, sehingga fitur RGB yang dipelajari ikut membawa informasi pemisah tersebut. Saat model dipakai untuk inferensi, cabang IDR dilepas sepenuhnya sehingga tidak ada penambahan waktu komputasi maupun parameter aktif.

### Compact Pyramid Refinement (CPR)

CPR menerima fitur multi-tingkat dari *backbone* dan menggabungkannya secara bertahap dari resolusi rendah ke resolusi tinggi, mirip struktur piramida fitur pada jaringan deteksi umum, tetapi dengan jumlah kanal dan operasi yang ditekan agar tetap ringan. Tujuannya menghasilkan peta saliency akhir yang mempertahankan detail batas objek dari fitur resolusi tinggi sekaligus konteks semantik dari fitur resolusi rendah, tanpa memerlukan cabang kedalaman terpisah sebagai sumber fusi karena informasi tersebut sudah terserap lewat IDR pada tahap pelatihan *backbone*.

### Alur Data Latih vs Inferensi

Perbedaan struktur jaringan antara fase pelatihan dan fase inferensi adalah inti efisiensi MobileSal, diringkas pada diagram berikut.

```
Fase pelatihan:
  RGB ─► backbone mobile ─┬─► CPR ─► peta saliency
                          └─► IDR ─► peta kedalaman prediksi
                                     (dibandingkan dgn depth asli)

Fase inferensi:
  RGB ─► backbone mobile ─────► CPR ─► peta saliency
         (cabang IDR dibuang, depth map tidak diproses)
```

Diagram ini menunjukkan bahwa struktur jaringan saat inferensi lebih sederhana daripada saat pelatihan: hanya satu aliran RGB yang diproses, sedangkan pengaruh kedalaman sudah tertanam pada bobot *backbone* melalui proses pelatihan dengan IDR.

## Eksperimen dan Hasil

Menurut naskah dan repositori kode resmi, MobileSal dievaluasi pada tujuh tolok ukur RGB-D SOD; di antaranya teridentifikasi NJU2K, NLPR, STEREO, SIP, SSD, dan DUTLF-D (DUT-RGBD), yang juga menjadi tolok ukur umum pada bab-bab RGB-D SOD lain dalam tinjauan ini. Metrik evaluasi yang dipakai mengikuti konvensi baku SOD: S-measure (kemiripan struktur antara peta saliency prediksi dan kebenaran lapangan), F-measure (rata-rata harmonik presisi dan *recall* pada peta saliency), E-measure (*enhanced-alignment measure*, mengukur kesejajaran piksel sekaligus statistik global citra), dan MAE (*Mean Absolute Error*, rata-rata selisih absolut antara peta prediksi dan kebenaran lapangan, semakin kecil semakin baik).

Model dibandingkan dengan metode RGB-D SOD berat seperti DMRA, CPFP, dan metode sejenis yang memakai *backbone* VGG/ResNet. Naskah melaporkan bahwa MobileSal mencapai kinerja yang bersaing dengan model-model tersebut pada mayoritas tolok ukur, sementara kecepatannya jauh lebih tinggi: 450 FPS pada resolusi 320×320 memakai implementasi PyTorch di GPU RTX 2080Ti, dan meningkat hingga sekitar 800 FPS dengan konversi ke TensorRT presisi FP16 (format angka titik-mengambang 16-bit yang mempercepat inferensi pada GPU modern). Jumlah parameter model tercatat 6,5 juta — jauh di bawah model RGB-D SOD berat yang umumnya berjumlah puluhan juta parameter. Perbandingan ini menunjukkan MobileSal menempati posisi efisiensi yang berbeda kelas: kecepatan inferensinya berorde ratusan FPS, sedangkan model dua-cabang konvensional pada klaster ini umumnya berjalan pada orde puluhan FPS atau lebih rendah.

Studi ablasi (pengujian pengaruh komponen dengan menghilangkannya satu per satu) yang dilaporkan menunjukkan bahwa penghapusan IDR menurunkan akurasi model dibandingkan versi lengkap, mengonfirmasi bahwa sinyal pemulihan kedalaman selama pelatihan memberi manfaat nyata terhadap kualitas fitur *backbone*, meskipun tidak menambah biaya inferensi. Angka S-measure, F-measure, dan MAE spesifik per dataset serta besaran penurunan akurasi pada ablasi IDR tidak berhasil diverifikasi secara pasti dari sumber yang dapat diakses untuk penulisan bab ini dan perlu dikonfirmasi langsung ke tabel pada naskah asli sebelum dikutip formal.

## Kelebihan dan Keterbatasan

Kelebihan utama MobileSal adalah rasio efisiensi terhadap akurasi yang tinggi: dengan parameter dan biaya komputasi yang jauh lebih rendah dari model RGB-D SOD berat, kecepatannya mencapai ratusan FPS sambil mempertahankan akurasi yang menurut naskah bersaing dengan model-model tersebut pada sebagian besar tolok ukur. Desain IDR juga elegan secara konseptual karena memindahkan biaya pemrosesan kedalaman sepenuhnya ke fase pelatihan, sehingga inferensi tidak memerlukan sensor kedalaman maupun cabang jaringan tambahan.

Dari sisi rekayasa, pendekatan ini memiliki ketergantungan struktural pada ketersediaan data RGB-D berpasangan yang berkualitas selama pelatihan, karena kualitas sinyal pemulihan kedalaman menentukan seberapa besar manfaat yang tertanam pada *backbone*. Secara konseptual, karena kedalaman tidak lagi dipakai saat inferensi, model tidak dapat memanfaatkan informasi kedalaman baru pada waktu uji meskipun tersedia — berbeda dari metode fusi eksplisit yang tetap dapat menyesuaikan diri terhadap kualitas kedalaman aktual pada tiap sampel uji. Efisiensi yang dicapai lewat *backbone* mobile juga umumnya menyertakan kompromi kapasitas representasi dibandingkan *backbone* berat, sehingga pada kasus adegan yang sangat rumit atau objek dengan tekstur ambigu, model kemungkinan tetap tertinggal dari model berat berkapasitas tinggi.

## Kaitan dengan Bab Lain

MobileSal berada pada klaster RGB-D SOD yang sama dengan CoNet (bab 166), DCF (bab 167), SPNet (bab 168), dan CAVER (bab 169), tetapi menempuh arah berbeda dari ketiganya. Bab-bab tersebut umumnya menambah kompleksitas modul fusi lintas-modal untuk menaikkan akurasi, sedangkan MobileSal menyederhanakan struktur inferensi lewat IDR agar kedalaman tidak perlu diproses ulang saat digunakan. Perbandingan ini relevan bagi pembaca yang ingin memilih pendekatan RGB-D SOD sesuai kendala perangkat: bab-bab fusi eksplisit lebih cocok ketika sumber daya komputasi memadai dan akurasi maksimal diutamakan, sedangkan MobileSal lebih relevan ketika target penerapan adalah perangkat mobile atau sistem *real-time* dengan anggaran komputasi ketat, misalnya robotika bergerak atau aplikasi kamera pada telepon pintar.

- [166 - 2020 - CoNet - RGB-D SOD](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md)
- [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md)
- [168 - 2021 - SPNet - RGB-D SOD](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md)
- [169 - 2023 - CAVER - RGB-D SOD](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md)

## Poin untuk Sitasi

Kutip dengan kunci `wu2022mobilesal`. Ringkasan yang aman dikutip: "MobileSal mengajukan *Implicit Depth Restoration* dan *Compact Pyramid Refinement* di atas *backbone* mobile untuk RGB-D SOD, mencapai 450 FPS pada resolusi 320×320 dengan 6,5 juta parameter sambil mempertahankan akurasi kompetitif terhadap model RGB-D SOD berat." Angka 450 FPS, konversi TensorRT FP16 (±800 FPS), dan 6,5 juta parameter berasal dari abstrak dan repositori kode resmi penulis (github.com/yuhuan-wu/MobileSal) sehingga cukup tepercaya untuk dikutip. Namun, angka S-measure/F-measure/MAE spesifik per dataset, daftar lengkap tujuh tolok ukur uji, serta besaran penurunan akurasi pada studi ablasi IDR **tidak berhasil diverifikasi langsung dari tabel naskah** dalam penulisan bab ini dan wajib dicek ke PDF asli (arXiv 2012.13095 atau versi TPAMI) sebelum dikutip dalam karya formal.
