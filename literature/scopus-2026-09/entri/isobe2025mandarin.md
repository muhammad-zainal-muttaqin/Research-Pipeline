# Mandarin count estimation with 360-degree tree video and transformer-based deep learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `isobe2025mandarin` |
| Judul asli | Mandarin count estimation with 360-degree tree video and transformer-based deep learning |
| Penulis | Isobe, Daisuke; Buayai, Prawit; Mao, Xiaoyang |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [isobe2025mandarin.pdf](../pdf/isobe2025mandarin.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.100874

## Gambaran Umum
Makalah ini (*Smart Agricultural Technology* 10, 2025) mengusulkan sistem estimasi jumlah total jeruk mandarin kecil dan belum matang pada satu pohon dari video RGB 360 derajat yang direkam dengan tablet iPad sebelum penjarangan buah (*thinning*). Model berbasis Transformer menggabungkan fitur dari beberapa bingkai yang diambil dari berbagai sudut pandang, dan keluarannya adalah satu bilangan jumlah buah per pohon, termasuk buah yang tertutup daun. Sistem tidak mendeteksi atau melacak buah satu per satu.

Data dikumpulkan di Setoda, Onomichi, Prefektur Hiroshima, Jepang, pada 2022 dan 2023, dengan kultivar Early Satsuma Mandarin. Terdapat video 89 pohon dengan jumlah buah hasil hitung manual (300 sampai 1.200 buah per pohon) dan 73 pohon tanpa jumlah yang diketahui. Hasil terbaik, yaitu model dengan pelatihan awal *Masked Auto Encoder*, pemilihan bingkai berdasarkan jumlah bingkai, dan fungsi kerugian WeakL1Loss, mencapai MAE 189,56 buah dan MAPE 26,12% rata-rata pada validasi silang lima lipatan. Metode pembanding satu citra menghasilkan MAE 632,28 dan MAPE 104,18%, sedangkan metode dua citra (depan dan belakang) menghasilkan MAE 251,88 dan MAPE 43,70%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Jumlah buah per pohon diperlukan untuk menentukan tingkat penjarangan agar tidak terjadi pembuahan berlebih dan agar ukuran buah terjaga. Sebelum penjarangan, satu pohon dapat memuat beberapa ratus hingga beberapa ribu buah, sehingga hitung manual sulit dan memakan tenaga. Penulis menyatakan bahwa metode yang ada menghitung buah yang tampak dari arah tertentu (citra tunggal, video baris pohon dengan pelacakan, atau citra multi-sudut) dan belum menghitung buah yang sepenuhnya tertutup daun. Metode depan-belakang mensyaratkan seluruh pohon masuk dalam satu citra, hal yang tidak selalu mungkin, dan pohon mandarin berdaun lebat.

Selain itu, pelabelan jumlah buah per pohon mahal, sehingga data berlabel terbatas. Penulis menilai ViViT dan TubeViT terlalu mahal secara komputasi untuk masukan banyak bingkai, dan Video Swin Transformer mengandaikan pencuplikan bingkai yang rapat.

## Ide Utama
Jumlah total buah per pohon diregresikan secara menyeluruh (*end-to-end*) dari sekumpulan bingkai yang jarang dan beragam sudutnya. Penulis memperkirakan model dapat mempelajari hubungan antara jumlah buah sebenarnya dan ciri visual pohon (jumlah buah tampak, kerapatan daun). Identitas buah antarbingkai tidak dibangun sama sekali. Penulis secara eksplisit menolak pelacakan buah dan *structure-from-motion* karena sulit dipertahankan pada video yang mengitari objek dengan banyak oklusi.

Tiga elemen pendukung: (1) *Temporal Swin Transformer* yang hanya memakai jendela pada sumbu waktu untuk menghubungkan fitur antarbingkai; (2) pelatihan awal tanpa label dengan *Masked Auto Encoder* yang dapat memakai 73 pohon tanpa jumlah buah; (3) fungsi kerugian WeakL1Loss yang memberi toleransi galat.

## Cara Kerja Langkah demi Langkah

```
 Video 360 derajat -> F bingkai (dipilih) -> Mask2Former -> citra mask buah
                          |                                     |
                          +---- RGB + mask --> CNN (ConvNeXt V2 nano) per bingkai
                                                   |
                                      Temporal Swin Transformer (jendela 4, N=2)
                                                   |
                                          MLP -> jumlah buah per pohon
```

### 1. Akuisisi data
Video vertikal direkam dengan iPad Pro 11 inci (generasi ke-4) dan iPad Pro 12,9 inci (generasi ke-6) sambil mengitari pohon, dengan jarak sekitar 1 m dan seluruh pohon diupayakan masuk bingkai. Umur pohon 15 sampai 40 tahun. Jumlah buah per pohon dihitung manual sebagai acuan. Pohon dengan jumlah buah sangat rendah akibat pembuahan berselang (*alternate bearing*) dikeluarkan. Rentang jumlah 300 sampai 1.200, rerata 685,19, simpangan baku 253,79, koefisien variasi 0,37039. Jumlah total bingkai per video tidak dilaporkan.

### 2. Pemilihan bingkai
Dua cara dipakai. Pertama, pemilihan berdasarkan jumlah bingkai yang diminta: bingkai ke-$i$ adalah $\lfloor N/F \cdot i \rfloor + 1$ dengan $N$ jumlah bingkai video dan $F$ jumlah bingkai masukan. Kedua, pemilihan berdasarkan selisih kumulatif: selisih antarbingkai bersebelahan $Diff = 1 - \text{SSIM}$ diakumulasi, dan bingkai dipilih ketika akumulasi mencapai ambang $T_i = SUM \cdot i / F$. Nilai $F$ diuji pada 12, 24, dan 36.

### 3. Pembuatan mask buah
Model segmentasi instans Mask2Former dengan *backbone* Swin-S, dilatih awal pada MSCOCO dan di-*fine-tune* pada citra jeruk mandarin dengan anotasi khusus, menghasilkan citra mask buah untuk tiap bingkai. Jumlah citra anotasi untuk Mask2Former tidak dilaporkan.

### 4. Ekstraksi fitur per bingkai
CNN berbasis ConvNeXt V2 nano memproses citra RGB (kanal 80 dan 160, blok 2 dan 6; blok ketiga dan seterusnya dihilangkan). Citra mask diproses cabang terpisah berkeluaran 16 kanal.

### 5. Penggabungan lintas bingkai
Fitur tiap bingkai dipecah menjadi patch $P \times P$ dengan embedding posisi, lalu *Temporal Swin Transformer* menyusun token seluruh bingkai dalam satu jendela waktu (ukuran jendela 4, dua lapis, dengan jendela bergeser setengah ukuran) tanpa jendela spasial. Koneksi B2T dipakai untuk menstabilkan pelatihan. MLP dengan agregasi bertahap menghasilkan jumlah buah.

### 6. Fungsi kerugian dan pelatihan awal
WeakL1Loss didefinisikan $\max(L1 - \alpha \cdot \text{GT}, 0)$, yaitu kerugian nol bila galat berada dalam $\pm\alpha$ kali nilai acuan; nilai $\alpha$ tidak ditemukan pada teks yang dibaca. Pelatihan awal *Masked Auto Encoder* hanya menutup bagian citra RGB (bukan mask) dan merekonstruksi gambar dengan dekoder Inv-CNN dan FC, selama 150 epoch. Pelatihan estimasi jumlah berlangsung 30 epoch, dengan CNN dibekukan dan peluruhan laju belajar per lapis 0,85 pada tahap penyesuaian.

## Eksperimen dan Hasil
Evaluasi memakai validasi silang berlapis (*stratified K-fold*), dengan $G = 12$ dan $K = 5$; jumlah video per lipatan 18, 18, 19, 16, dan 18. Beberapa set $F$ bingkai diambil dari video yang sama dengan menggeser bingkai awal untuk menambah data latih. Metrik adalah MAE dan MAPE, dirata-ratakan antarlipatan.

Pengaruh jumlah bingkai (Tabel 5, tanpa pelatihan awal):

| Bingkai | MAE | MAPE (%) |
|---|---|---|
| 12 | 208,70 | 28,63 |
| 24 | 224,17 | 31,19 |
| 36 | 227,81 | 31,26 |

Hasil utama (Tabel 6, F = 12):

| Pemilihan bingkai | Tanpa MAE: L1 (MAE/MAPE) | Tanpa MAE: WeakL1 | Dengan MAE: L1 | Dengan MAE: WeakL1 |
|---|---|---|---|---|
| Berdasarkan jumlah bingkai | 208,70 / 28,63 | 223,88 / 30,81 | 194,02 / 27,08 | 189,56 / 26,12 |
| Kumulatif SSIM | 216,03 / 30,90 | 238,97 / 33,19 | 195,99 / 27,86 | 190,38 / 26,74 |

Perbandingan dengan metode lain (Tabel 7, diimplementasikan ulang pada data yang sama):

| Metode | MAE | MAPE (%) |
|---|---|---|
| Satu citra (Chen dkk.) | 632,28 | 104,18 |
| Dua citra depan-belakang (Koirala dkk.) | 251,88 | 43,70 |
| Metode usulan | 189,56 | 26,12 |

Uji-t dua sisi pada taraf kepercayaan 95% menunjukkan metode usulan signifikan lebih akurat daripada kedua metode pembanding, tetapi tidak ada perbedaan signifikan antarvarian metode usulan sendiri. Analisis per rentang jumlah buah (interval 100) dengan uji Kruskal-Wallis juga tidak menunjukkan perbedaan signifikan. Galat per pohon meningkat pada pohon berbuah banyak. Tiga contoh (Tabel 8): pohon A 364 buah dengan prediksi 423,134 (galat 59,134); pohon B 724 dengan prediksi 675,384 (galat 48,616); pohon C 1.175 dengan prediksi 864,808 (galat 310,192). Pada tiga pohon uji (Tabel 9), metode kumulatif SSIM lebih baik pada pohon D (60,11 berbanding 198,68) dan lebih buruk pada pohon F (204,77 berbanding 90,69), sedangkan pohon E hampir sama (87,05 dan 86,96).

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: hanya memerlukan video dari perangkat seluler, memperkirakan jumlah total termasuk buah tersembunyi, tidak memerlukan pelacakan atau rekonstruksi 3D, dan pelatihan awal tanpa label memanfaatkan video tanpa hitungan.

Keterbatasan menurut penulis: hasil bergantung pada bingkai yang dipilih; perubahan skala antarbingkai menyulitkan estimasi; galat tinggi pada pohon berbuah banyak; pohon harus dapat dikelilingi sehingga memerlukan ruang antarpohon; dan generalisasi ke wilayah dan tahun lain belum dikonfirmasi. Penulis juga menyatakan bahwa keunggulan pelatihan awal tidak signifikan secara statistik pada setiap interval.

Menurut pembacaan ringkasan ini, terdapat keterbatasan lain. Hanya 89 pohon berlabel dari satu wilayah, sehingga estimasi MAE 189,56 pada rerata 685 buah (sekitar 26%) bersifat kasar. Keluaran berupa bilangan per pohon tidak dapat diaudit per buah, sehingga tidak ada bukti bahwa buah yang sama tidak dihitung ganda atau bahwa buah tersembunyi benar-benar terhitung. Tidak ada pemisahan data uji tersendiri selain lipatan validasi silang (teks menyebut "validasi dan uji" tetapi hasil dirata-ratakan dari lipatan validasi). Fungsi kerugian WeakL1Loss justru memperburuk hasil tanpa pelatihan awal (MAE 223,88 dibanding 208,70).

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat dari beberapa sudut dengan mekanisme regresi menyeluruh: bingkai dari video 360 derajat dijadikan token, dan Transformer menggabungkan fitur antarbingkai menjadi jumlah per pohon. Identitas buah lintas bingkai tidak dibangun; pelacakan dan *structure-from-motion* ditolak secara eksplisit. Hitungan tidak dilaporkan per kelas. Acuan hitungnya adalah hitung manual lapangan jumlah buah per pohon sebelum penjarangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan pemilihan bingkai yang beragam sudutnya (jumlah bingkai tetap atau selisih kumulatif SSIM), pelatihan awal tanpa label dari pohon yang jumlahnya tidak diketahui, dan keluaran total per pohon sebagai pembanding terhadap pendekatan berbasis identitas. Namun, pendekatan ini tidak menghasilkan hitungan per kelas kematangan dan tidak menyediakan pencocokan antarsisi, sehingga tidak dapat langsung dipakai untuk inventaris per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `isobe2025mandarin`.

Isobe dkk. (2025) mengusulkan estimasi jumlah total jeruk mandarin kecil belum matang per pohon dari video 360 derajat yang direkam dengan tablet, memakai Temporal Swin Transformer atas fitur CNN dari 12 bingkai dan mask hasil Mask2Former, dengan pelatihan awal Masked Auto Encoder. Pada 89 pohon berlabel (300 sampai 1.200 buah) dengan validasi silang lima lipatan, model terbaik mencapai MAE 189,56 dan MAPE 26,12%, dibandingkan MAPE 104,18% (satu citra) dan 43,70% (dua citra) pada data yang sama.

Catatan verifikasi data: Angka MAE dan MAPE diambil dari Tabel 5, 6, dan 7; angka per pohon dari Tabel 8 dan 9; statistik jumlah buah (rerata 685,19, simpangan baku 253,79) dari Seksi 2.1; pengaturan pelatihan dari Tabel 2 sampai 4. Gambar 12 sampai 14 tidak dapat dibaca dari teks. Nilai $\alpha$ pada WeakL1Loss, jumlah bingkai per video, dan jumlah citra anotasi Mask2Former tidak ditemukan pada teks. Judul "Tabel 6" memuat nama kolom yang digabung pada ekstraksi; urutan kolom dipastikan dari nilai terbaik yang dinyatakan di teks (189,56 dan 26,12).
