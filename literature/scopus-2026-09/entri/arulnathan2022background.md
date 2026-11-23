# Background Subtraction for Accurate Palm Oil Fruitlet Ripeness Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arulnathan2022background` |
| Judul asli | Background Subtraction for Accurate Palm Oil Fruitlet Ripeness Detection |
| Penulis | Arulnathan, David Nathan; Koay, Brenda Chia Wen; Lai, Weng Kin; Ong, Thai Kiat; Lim, Li Li |
| Tahun | 2022 |
| Venue | 2022 IEEE International Conference on Automatic Control and Intelligent Systems I2cacis 2022 Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm, mango, strawberry |

## Tautan Akses
- PDF: [arulnathan2022background.pdf](../pdf/arulnathan2022background.pdf)
- DOI resmi: https://doi.org/10.1109/i2cacis54679.2022.9815275

## Gambaran Umum

Kajian ini menguji pengaruh penghapusan latar (*background subtraction*) terhadap ketepatan klasifikasi kematangan buah lepas (*fruitlet*) kelapa sawit ke tiga kelas: mentah (*unripe*), matang (*ripe*), dan terlalu matang (*overripe*). Penulis menyebut penilaian kematangan di Malaysia masih dilakukan manual berdasarkan warna dan jumlah brondolan yang jatuh. Penulis ingin mengetahui apakah penghapusan latar membantu klasifikasi otomatis. Pendekatan jaringan saraf konvolusi (*convolutional neural network*, CNN) dibandingkan dengan pendekatan berbasis fitur.

Sampel dipanen dari kebun Genting Plantation di Tebong, Melaka, dan diproses di laboratorium dalam 8 jam. Terdapat 42 sampel per kelas (mentah, matang, terlalu matang). Setiap sampel difoto dengan latar sederhana, lalu massa dan volumenya diukur. Citra diperbanyak (*augmentation*) dengan rotasi 60 derajat dan pembalikan acak menjadi 378 citra per kelas. Citra diubah ke 64 atau 128 piksel. Pembagian data 80% latih dan 20% uji. Pemberi label tidak disebut.

Tiga perlakuan latar dibandingkan: latar putih asli, latar hijau, dan latar hitam (latar dihapus) lewat metode semi-manual. Metode semi-manual berarti pengguna menandai piksel latar, lalu piksel bernilai serupa dilabeli sebagai latar. Metode Otsu (pemisahan ambang otomatis dari histogram) dipakai pada klasifier Bayes naif. CNN berisi dua lapis konvolusi, satu lapis padat, dan *dropout* 50% dengan 225.091 parameter. Sebanyak 336 konfigurasi dicoba dengan variasi ukuran piksel, lapis padat, ukuran *batch*, dan ukuran lapis konvolusi. Klasifier Bayes naif (*Naive Bayes*, pengklasifikasi probabilistik yang mengasumsikan fitur saling bebas) memakai tiga statistik (rerata, ragam, median) dari empat blok histogram, yaitu 12 fitur, dan 14 fitur bila massa dan volume ditambahkan.

CNN terbaik dengan latar asli mencapai akurasi rerata 96,93% (mentah 100,00%; terlalu matang 96,05%; matang 94,74%). Latar hijau memberi 90,79% dan latar hitam 87,72%. Pada latar hitam, kelas terlalu matang hanya 64,47%. Klasifier Bayes naif memberi 58,51% (asli), 64,59% (semi-manual), dan 65,67% (Otsu) dengan 12 fitur. Dengan 14 fitur, hasilnya 79,56%, 87,28%, dan 88,15%. Penulis menyimpulkan penghapusan latar tidak menaikkan akurasi CNN, tetapi menaikkan akurasi Bayes naif.

Keterbatasan dapat diperiksa dari teks. Objeknya buah lepas yang difoto di laboratorium dengan latar polos, bukan tandan di pohon, dan tidak ada pencacahan. Hanya 42 sampel asli per kelas. Augmentasi dilakukan sebelum pembagian 80/20 menurut uraian, sehingga citra turunan dari sampel yang sama dapat berada di data latih dan uji. Tidak ada pembagian per sampel yang disebut. Hasil CNN dipilih dari ratusan konfigurasi dengan data uji yang sama, dan tidak ada data validasi terpisah. Pemberi label dan jumlah ulangan tidak disebut.
