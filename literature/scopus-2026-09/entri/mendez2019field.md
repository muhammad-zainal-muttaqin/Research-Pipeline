# In-field estimation of orange number and size by 3D laser scanning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mendez2019field` |
| Judul asli | In-field estimation of orange number and size by 3D laser scanning |
| Penulis | M\'endez, Valeriano; P\'erez-Romero, Antonio; Sola-Guirado, Rub\'en; Miranda-Fuentes, Antonio; Manzano-Agugliaro, Francisco; Zapata-Sierra, Antonio; Rodr\'\iguez-Lizana, Antonio |
| Tahun | 2019 |
| Venue | Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [mendez2019field.pdf](../pdf/mendez2019field.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy9120885

## Gambaran Umum

Estimasi beban buah sebelum panen diperlukan untuk merencanakan logistik panen dan keputusan pemasaran, tetapi penghitungan manual mahal, memakan waktu, dan rawan galat. Penelitian ini bertujuan menguji kemampuan algoritma K-means mendeteksi buah pada model tiga dimensi pohon jeruk yang dipangkas dan tidak dipangkas, serta menilai kemampuan prakiraan panen dibandingkan hasil panen lapangan yang diukur langsung.

Penelitian dilakukan pada 26 dan 28 Desember 2017 di kebun jeruk irigasi seluas 14 ha di Puebla de la Parrilla, Hornachuelos, Córdoba, Spanyol. Tanaman yang digunakan adalah jeruk 'Salustiana' (Citrus sinensis (L.) Osbeck) dengan jarak tanam 6 × 4 m. Sebanyak 24 pohon dibagi menjadi dua blok, masing-masing 12 pohon: blok pertama dipangkas pada Maret 2017 dan blok kedua tidak dipangkas sehingga memiliki kerapatan daun dan volume tajuk lebih besar. Setiap pohon dipanen terpisah untuk menghitung jumlah buah sebenarnya, dan sampel 10 buah per pohon diambil pada berbagai ketinggian dan arah mata angin untuk mengukur berat serta diameter (N = 160). Akuisisi memakai pemindai laser Leica ScanStation P20 dengan kamera terintegrasi, akurasi posisi 3 mm pada jarak 50 m, dan laju hingga satu juta titik per detik. Sembilan titik kontrol berupa sekrup baja diukur dengan GPS Leica 1200 mode RTK dalam sistem ETRS89 untuk menggabungkan awan titik. Setiap pohon memerlukan empat posisi pemindaian; waktu rata-rata 5 menit untuk jalur luar, 13,72 menit untuk sapuan penuh di jalur tengah, dan 15 menit tambahan untuk penyambungan antar-pemindaian, sehingga satu zona memakan waktu 8 jam.

Deteksi buah diawali dengan segmentasi warna berdasarkan filter RGB langsung (R ≥ 180, G ≥ 50, B ≤ 105) atau kromatisitas merah r = R/(R+G+B) dengan ambang r ≥ 0,5. Awan titik hasil segmentasi diproses dengan prosedur ISODATA, yaitu K-means dengan jumlah gugus yang berubah selama proses: pembentukan KD-Tree, matriks ketetanggaan dengan jarak maksimum rn < 20 mm, pengelompokan awal titik bertetangga, penyesuaian bentuk dengan batasan radius buah rmin = 30 mm dan rmax = 45 mm, penyeimbangan titik memakai K-means, serta penghapusan bentuk dengan jumlah titik ns < 9. Jumlah bentuk yang tersisa menjadi hitungan buah, dan jari-jari bentuk dipakai sebagai ukuran buah.

Pada delapan pohon yang dipangkas dan dipindai sebelum matahari terbenam, jumlah buah lapangan berkisar 278–470 per pohon sedangkan algoritma memberi 209–351, sehingga terjadi undercounting 11%–40%. Regresi jumlah buah lapangan terhadap jumlah buah model memberi R² = 0,63, Pearson r = 0,79 (p = 0,019), dan galat baku residu 59 buah. Pada sepuluh pohon tidak dipangkas, jumlah buah lapangan berkisar 268–488 sedangkan model memberi 59–413 (penurunan 22%–79%); hubungannya tidak signifikan dengan R² = 0,18, r = 0,43 (p = 0,18), dan RMSE 82 buah. Pohon yang dipindai setelah matahari terbenam hanya menghasilkan 25–67 buah karena filter warna tidak dapat diterapkan. Berat buah rata-rata 197,53 ± 4,22 g. Panen aktual delapan pohon adalah 549 kg, sedangkan prakiraan memakai regresi adalah 563 kg (selisih 2,5%); simulasi 2.000 kali memberi 563 kg dengan rentang 557–569,3 kg dan selang kepercayaan 96% sebesar 559,7–566,8 kg. Diameter menurut algoritma adalah 72,15 ± 22,62 mm dibandingkan 72,68 ± 5,728 mm di lapangan, tanpa perbedaan signifikan (p = 0,35). Berat buah berkorelasi dengan diameter (r = 0,89 dan 0,87 pada sumbu horizontal serta 0,78 pada sumbu Z; p < 10⁻¹⁰), dan persamaan berat = 26,729 + 0,000406 × (Diameterₐ × Diameter_b × Diameter_c) memberi R² = 0,88 (p < 10⁻¹⁰). Acuan hitung adalah regresi linier antara jumlah buah hasil panen lapangan dan jumlah buah dari K-means, dengan R², korelasi Pearson, dan RMSE sebagai metrik. Split latih-uji tidak dinyatakan; pengujian dibedakan atas kelompok pohon dipangkas (n = 8), tidak dipangkas (n = 10), dan pohon yang dipindai setelah matahari terbenam.

Penulis menyatakan penggunaan langsung algoritma tanpa regresi tidak menghasilkan angka yang tepat, sehingga hubungan antara hitungan lapangan dan hitungan model harus ditetapkan terlebih dahulu. Oklusi oleh daun, cabang, dan buah lain mengurangi kepadatan titik di dalam tajuk dan menyebabkan undercounting; kepadatan daun pada pohon tidak dipangkas memperparah masalah ini. Pencahayaan menjadi batasan tersendiri karena pemindaian setelah matahari terbenam menghilangkan informasi warna yang menjadi dasar filter. Akuisisi dengan pemindai laser tergolong lambat dan mahal, dan pemindai laser yang dipasang pada UAV tidak merekam informasi RGB yang dianggap wajib bagi deteksi buah otomatis. Penulis juga menyatakan ukuran buah berubah secara nonlinear menjelang panen, sehingga diperlukan deret pengukuran berulang jika informasi ukuran dipakai untuk keputusan pemasaran.
