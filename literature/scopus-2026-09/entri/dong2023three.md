# Three-dimensional quantification of apple phenotypic traits based on deep learning instance segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dong2023three` |
| Judul asli | Three-dimensional quantification of apple phenotypic traits based on deep learning instance segmentation |
| Penulis | Dong, Xuhua; Kim, Woo-Young; Zheng, Yu; Oh, Ju-Youl; Ehsani, Reza; Lee, Kyeong-Hwan |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [dong2023three.pdf](../pdf/dong2023three.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108156

## Gambaran Umum

Dong dkk. (2023) menyoroti bahwa sifat fenotipik buah apel, seperti jumlah, distribusi tiga dimensi, dan volume, menentukan hasil panen, tetapi sulit diukur secara manual, terutama di kebun berskala besar. Metode berbasis citra 2D menimbulkan masalah *double counting* karena objek yang sama sulit dikenali pada citra yang berbeda, dan volume buah sulit diestimasi ketika tertutup daun maupun cabang. Penulis mengusulkan metode untuk mengekstraksi buah apel secara individual dan memetakan posisi serta volumenya dalam tiga dimensi.

Data dikumpulkan dari tiga sistem pembentukan tanaman apel (*training system*) di kebun berskala besar, yaitu MAAS, VAAS, dan VWAS. Citra multi-sudut diambil menggunakan sistem multi-kamera pada pesawat nirawak (UAV) dengan teknik *oblique photogrammetry*. Dari citra tersebut dibangun awan titik (*point cloud*) tiga dimensi dengan algoritma *structure-from-motion*. Segmentasi instans (*instance segmentation*) dilakukan dengan *generalized sparse convolutional neural network*, fungsi kerugian diskriminatif berbobot (*weighted discriminative loss*), dan pengelompokan berbasis kepadatan yang bervariasi (HDBSCAN 3D). Setelah itu, bentuk buah yang tidak utuh dipulihkan menggunakan model bola yang dipasang pada awan titik untuk menghitung volume.

Hasil kuantitatif menunjukkan bahwa estimasi jumlah buah memiliki koefisien determinasi (R²) 0,84 sampai 0,99 dengan *weighted mean absolute percentage error* (WMAPE) 3,41% sampai 12,75%. Hasil terbaik terdapat pada lapangan MAAS dengan R² 0,99 dan WMAPE 3,41%. Untuk VAAS, R² tercatat 0,84 (WMAPE 12,75%), sedangkan VWAS memperoleh R² 0,92 (WMAPE 8,63%). Estimasi volume memiliki R² 0,84 sampai 0,90 dengan WMAPE 4,74% sampai 7,03%. Dibandingkan metode diameter bola yang lazim dipakai, metode usulan menurunkan WMAPE dari 9,18% menjadi 5,06% di MAAS, dari 8,50% menjadi 7,03% di VAAS, dan dari 7,70% menjadi 4,74% di VWAS. Nilai R² volume juga meningkat di semua lapangan, yaitu dari 0,65 menjadi 0,88 (MAAS), 0,78 menjadi 0,84 (VAAS), dan 0,86 menjadi 0,90 (VWAS). Pada tahap segmentasi, rata-rata F1-score mencapai 0,906, sedangkan hasil reproduksi metode Lahoud dkk. (2019) pada data yang sama hanya 0,497.

Penulis mengakui beberapa batasan. Pertama, kinerja pengenalan menurun akibat oklusi berat di lapangan VAAS, sehingga penulis menyarankan penambahan sudut pandang, misalnya dengan mengombinasikan drone dan kendaraan darat, untuk mengurangi naungan daun. Kedua, R² estimasi volume masih di bawah 0,90 pada hampir semua lapangan karena bentuk buah yang tidak utuh dan beragam memengaruhi akurasi algoritma. Ketiga, penulis menyatakan bahwa penelitian ini hanya menguji satu jenis tanaman, yaitu apel, meskipun metode tersebut diharapkan dapat diterapkan pada buah lain. Penulis menyimpulkan bahwa metode ini layak dipakai di kondisi lapangan nyata untuk analisis hasil panen dan operasi robot pemanen.
