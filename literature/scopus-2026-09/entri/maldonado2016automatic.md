# Automatic green fruit counting in orange trees using digital images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `maldonado2016automatic` |
| Judul asli | Automatic green fruit counting in orange trees using digital images |
| Penulis | Maldonado, Walter; Barbosa, Jos\'e Carlos |
| Tahun | 2016 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [maldonado2016automatic.pdf](../pdf/maldonado2016automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2016.07.023

## Gambaran Umum

Kajian ini menghitung buah dari foto digital dengan metode pengolahan citra klasik, bukan jaringan saraf dalam. Sistem memproses setiap foto secara terpisah. Tahap awal mengubah model warna, menerapkan *thresholding*, dan melakukan equalisasi histogram untuk memperjelas kontras. Setelah itu, sistem menghitung fitur tekstur bas-relief memakai filter *Laplace*, *Sobel*, dan *Gaussian blur*. Sebuah pengklasifikasi *support vector machine* (SVM, metode klasifikasi yang mencari batas pemisah terbaik antar-kelas) menentukan apakah suatu wilayah termasuk buah atau bukan. Hasil hitungan kemudian dibandingkan dengan hitungan manual oleh pemeriksa menggunakan regresi linear.

Ukuran kecocokan utama adalah R² (koefisien determinasi, yaitu proporsi variasi hitungan manual yang dijelaskan oleh hitungan algoritma). Nilainya berkisar dari 0,19 pada pohon Pêra umur 3–5 tahun hingga 0,74 pada pohon Natal umur 11 tahun ke atas. Kecocokan bergantung pada varietas dan umur pohon. Dari sisi waktu, rerata waktu hitung manual adalah 64,9 dan rerata waktu algoritma 9,79 (teks tidak menegaskan satuan waktunya dalam bagian yang diperiksa; median 63,2 dan 9,80). Rerata false positive keseluruhan adalah 14,68 ± 0,52 pada n = 1182 citra. Kelompok citra dengan kualitas "very good" (281 citra) memiliki false positive sekitar 3%.

Setiap titik pada grafik regresi menunjukkan jumlah dua citra dari pohon yang sama, baik hasil algoritma maupun hasil pemeriksa, sehingga satu titik mewakili satu pohon. Dua citra itu dijumlahkan untuk membentuk hitungan per pohon. Teks tidak menyatakan bahwa sebuah buah diidentifikasi kembali antar-foto, sehingga buah yang sama dapat terhitung lebih dari sekali dalam dua citra.

Dataset terdiri atas 1182 citra dari 591 pohon. Keterbatasan ini perlu diperiksa sebelum angka dikutip.
