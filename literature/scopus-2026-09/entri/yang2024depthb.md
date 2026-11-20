# Depth Anything V2

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024depthb` |
| Judul asli | Depth Anything V2 |
| Penulis | Yang, L.; others |
| Tahun | 2024 |
| Venue | Advances in Neural Information Processing Systems |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [yang2024depthb.pdf](../pdf/yang2024depthb.pdf)

## Gambaran Umum

Kajian ini membahas estimasi kedalaman monokular, yaitu memperkirakan jarak setiap piksel dari satu citra RGB. Kedalaman yang akurat dibutuhkan untuk rekonstruksi 3D, navigasi, dan mengemudi otonom. Model sebelumnya terbagi dua, yaitu model diskriminatif yang cepat tetapi kurang detail, dan model generatif berbasis *Stable Diffusion* yang detail tetapi lambat. Penulis ingin membangun model fondasi yang menggabungkan kelebihan keduanya, yakni hasil yang tangguh pada tata letak kompleks, detail halus, efisiensi, dan kemampuan dialihkan ke tugas hilir.

Data pelatihan utama berupa citra sintetis yang berlabel presisi, menggantikan citra nyata berlabel yang dipakai pada versi pertama. Model guru dilatih pada citra sintetis dengan ukuran batch 64 selama 160K iterasi, lalu model siswa yang lebih kecil dilatih melalui citra nyata berlabel pseudo dalam skala besar. Citra dilatih pada resolusi 518×518. Penulis juga membangun benchmark evaluasi baru, DA-2K, yang berisi 1K citra dengan 2K pasangan piksel. Benchmark ini mencakup delapan skenario penerapan MDE dan citra berresolusi tinggi. Kajian ini tidak menyebut tanaman, buah, atau platform lapangan. Latensi diukur pada GPU V100.

Hasil utama menunjukkan model Depth Anything V2 lebih cepat dan lebih ringan dibanding model berbasis *Stable Diffusion*. Pada Gambar 1, model terkecil (*Ours-Small*) memerlukan 60 ms dengan 25 juta parameter, sedangkan model lain tercatat 213 ms dengan 335 juta parameter, dan 2,1 detik hingga 5,2 detik untuk model berbasis difusi. Model berskala terbesar memiliki sekitar 1,3 miliar parameter. Pada uji zero-shot relatif (Tabel 2), skor metrik *AbsRel* dan δ1 Depth Anything V2 disebut lebih baik dari MiDaS dan sebanding dengan V1. Penulis menyatakan bahwa metrik tersebut belum mencerminkan keunggulan detail halus dan ketahanan model. Pada benchmark DA-2K (Tabel 3), akurasi model Depth Anything V2 berkisar dari 86,8% sampai 97,4%. Penulis mengklaim model paling ringan sudah melampaui seluruh model komunitas yang dibandingkan.

Penulis menyatakan beberapa batasan. Pertama, DA-2K tidak dimaksudkan menggantikan benchmark yang ada, karena pengukuran kedalaman jarang tidak cukup untuk rekonstruksi adegan padat. Kedua, citra sintetis memiliki pergeseran distribusi terhadap citra nyata dan cakupan adegan yang terbatas, sehingga pelatihan memerlukan citra nyata pseudo-berlabel. Ketiga, label kedalaman pada benchmark seperti NYU-D dan KITTI dinilai bising, terbatas keragamannya, dan beresolusi rendah sekitar 500×500. Penulis menegaskan bahwa temuan pada benchmark tersebut belum tentu dapat dialihkan ke citra beresolusi tinggi.
