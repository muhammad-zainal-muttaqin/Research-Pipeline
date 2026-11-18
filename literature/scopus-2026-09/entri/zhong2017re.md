# Re-ranking person re-identification with k-reciprocal encoding

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhong2017re` |
| Judul asli | Re-ranking person re-identification with k-reciprocal encoding |
| Penulis | Zhong, Zhun; Zheng, Liang; Cao, Donglin; Li, Shaozi |
| Tahun | 2017 |
| Venue | Proceedings 30th IEEE Conference on Computer Vision and Pattern Recognition Cvpr 2017 |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhong2017re.pdf](../pdf/zhong2017re.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr.2017.389

## Gambaran Umum

Penelitian ini membahas tahap pengurutan ulang (re-ranking) pada person re-identification (re-ID, pencocokan orang lintas kamera), yang dipandang sebagai proses retrieval. Masalah utamanya adalah daftar peringkat awal sering memuat kecocokan palsu pada k teratas, sehingga pencocokan sejati terdorong ke peringkat bawah. Penulis mengajukan hipotesis bahwa citra dalam galeri yang termasuk tetangga terdekat saling balik (k-reciprocal nearest neighbors) dari citra probe lebih mungkin menjadi kecocokan sejati. Metode yang diusulkan sepenuhnya otomatis dan tanpa pengawasan, tidak memerlukan interaksi manusia maupun data berlabel, sehingga dapat diterapkan pada kumpulan data berskala besar dan pada hasil peringkat awal mana pun.

Data yang dipakai adalah empat kumpulan data re-ID berskala besar. Market-1501 memuat 32.668 kotak pembatas dari 1.501 identitas yang direkam dari enam titik pandang, dengan 12.936 citra untuk latihan dan 19.732 untuk pengujian serta 3.368 probe buatan tangan. CUHK03 memuat 14.096 citra dari 1.467 identitas yang direkam dari dua kamera, dengan anotasi kotak pembatas buatan manusia maupun hasil detector deformable part model (DPM). MARS adalah kumpulan data berbasis video dengan 1.261 identitas dan sekitar 20.000 sekuens dari enam kamera, dilengkapi 3.248 sekuens pengganggu. PRW adalah kumpulan data ujung-ke-ujung dengan 11.816 frame dari 932 identitas dan enam kamera, yang menuntut deteksi orang terlebih dahulu sebelum pencocokan. Fitur pembanding yang dipakai penulis adalah local maximal occurrence (LOMO), bag-of-words (BOW), serta fitur ID-discriminative embedding (IDE) yang dilatih pada CaffeNet dan ResNet-50.

Mekanisme asosiasinya terdiri atas tiga langkah. Pertama, himpunan tetangga saling balik dibobot dan dikodekan menjadi satu vektor k-reciprocal; dua citra dikatakan saling balik bila masing-masing berada di peringkat k teratas ketika citra lain dijadikan probe. Himpunan ini diperluas dengan menambahkan tetangga saling balik setengah-k dari setiap kandidat apakah tumpang tindihnya mencapai dua pertiga, agar positif sulit yang terlewat dapat dikembalikan. Kedua, jarak Jaccard dihitung dari perbandingan himpunan tetangga dua citra, yaitu satu dikurangi rasio irisan terhadap gabungan. Untuk menghindari perhitungan irisan dan gabungan himpunan yang mahal, himpunan dikodekan menjadi vektor berdimensi N dengan bobot Gaussian e^{−d(p,gi)} untuk anggota himpunan dan nol untuk bukan anggota; irisan dan gabungan dihitung berturut-turut sebagai norma-L1 dari min dan max elementwise. Local query expansion merata-ratakan vektor tetangga terdekat probe untuk memperkuat fitur, dengan ukuran k2 lebih kecil daripada k1. Ketiga, jarak akhir dirumuskan sebagai d* = (1−λ)dJ + λd, yang menggabungkan jarak Jaccard dan jarak Mahalanobis asli; λ = 0 memakai jarak Jaccard saja dan λ = 1 memakai jarak asli saja. Kompleksitasnya O(N²) untuk pasangan galeri dan O(N² log N) untuk peringkat, yang dapat dihitung di luar jaringan, sehingga untuk probe baru hanya diperlukan O(N) dan O(N log N).

Hasil diukur dengan metrik cumulated matching characteristics pada rank-1 dan mean average precision (mAP), dengan angka pembanding dari publikasi aslinya. Pada Market-1501 dengan k1 = 20, k2 = 6, dan λ = 0,3, metode IDE berbasis ResNet-50 naik dari 72,54 persen dan 46,00 persen menjadi 74,85 persen dan 59,87 persen, yaitu perbaikan 3,06 persen pada rank-1 dan 13,99 persen pada mAP; kombinasi terbaik IDE (R) + KISSME + usulan mencapai 77,11 persen dan 63,63 persen, mengungguli metode mutakhir Gated sebesar 65,88 persen dan 39,55 persen. Pada CUHK03 skema single-shot, perbaikan hanya sekitar 1 persen dan pada IDE bahkan hampir setara dengan hasil awal, karena setiap identitas hanya memiliki satu positif di galeri. Skema pembagian baru dengan beberapa ground truth per identitas memberi kenaikan misalnya IDE (R) + XQDA dari 32,0 persen dan 29,6 persen menjadi 38,1 persen dan 40,3 persen pada data berlabel. Pada MARS, IDE (R) + XQDA naik dari 70,51 persen dan 55,12 persen menjadi 73,94 persen dan 68,45 persen; pada PRW, IDE (C) naik dari 51,03 persen dan 25,09 persen menjadi 52,54 persen dan 31,51 persen.

Batasan yang dinyatakan penulis mencakup ketergantungan metode pada ketersediaan beberapa contoh positif per identitas di galeri, karena pada skema single-shot konteks yang diperoleh tidak cukup sehingga perbaikannya kecil. Penulis juga menyatakan efektivitas re-ranking sangat bergantung pada kualitas daftar peringkat awal. Parameter k1, k2, dan λ ditentukan berdasarkan kumpulan data, misalnya k1 = 7, k2 = 3, dan λ = 0,85 pada CUHK03 single-shot dibanding k1 = 20, k2 = 6, dan λ = 0,3 pada kumpulan data lain. Selain itu, perhitungan irisan dan gabungan himpunan memerlukan pengodean vektor agar praktis, dan kode sumber hanya tersedia atas permintaan. Penulis tidak menyatakan batasan lain secara eksplisit.

