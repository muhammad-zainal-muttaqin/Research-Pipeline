# Immature green citrus fruit detection and counting based on fast normalized cross correlation (FNCC) using natural outdoor colour images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2016immature` |
| Judul asli | Immature green citrus fruit detection and counting based on fast normalized cross correlation (FNCC) using natural outdoor colour images |
| Penulis | Li, Han; Lee, Won Suk; Wang, Ku |
| Tahun | 2016 |
| Venue | Precision Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [li2016immature.pdf](../pdf/li2016immature.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-016-9443-z

## Gambaran Umum

Makalah ini menyajikan metode untuk mendeteksi dan menghitung buah jeruk hijau muda (*immature green citrus fruit*) dari citra warna yang diambil di luar ruangan. Judul makalah menyebut *fast normalized cross correlation* (FNCC) sebagai metode utama. Data yang dipakai berasal dari kebun, sehingga buah sering tertutup daun dan ranting. Penulis menyatakan bahwa tujuannya adalah deteksi dan penghitungan buah dari citra alami.

Data terdiri atas 118 citra yang diambil pada Oktober 2010 di kebun jeruk Universitas Florida, Gainesville, dengan varietas Orlando Tangelo. Citra diambil dengan kamera Canon PowerShot SD880IS pada resolusi 3648×2736 piksel, lalu diperkecil menjadi 912×684 piksel. Citra dibagi menjadi 59 citra latih dan 59 citra validasi. Citra mencakup kondisi cerah dan berawan, serta bagian yang terkena sinar matahari dan yang teduh. Pemberi label tidak disebut.

Metode FNCC mencocokkan patch berukuran 30×30 piksel dengan templat buah dan mengukur kemiripannya. Ambang kemiripan 0,7 dipilih dari sembilan kandidat pada data latih. Komponen warna R, B, dan H dipilih dengan seleksi maju. Klasifikasi KNN (*k-nearest neighbour*) menandai area sebagai buah jika mengandung lebih dari 450 piksel buah. *Circular Hough transform* (CHT) mencari lingkaran dengan jari-jari 60 sampai 180 piksel, dengan maksimum 15 lingkaran per citra.

Pada 59 citra validasi terdapat 154 buah. Sebanyak 130 buah terdeteksi dengan benar, 24 buah terlewat, dan 25 positif palsu. Akurasi identifikasi buah yang benar adalah 84,4%. Tabel 1 melaporkan positif palsu 16,2% dan buah terlewat 15,6%. Penulis hanya menghitung buah yang tampak lebih dari setengahnya pada citra.

Keterbatasan yang dapat diperiksa dari teks: buah yang tertutup lebih dari setengah sulit dideteksi, dan penutupan oleh ranting serta kemiripan warna buah dengan daun menyebabkan buah terlewat (Gambar 12). Pengaruh pencahayaan disebut sebagai masalah yang belum ditangani. Hasil hanya dilaporkan pada set validasi, tanpa data uji terpisah. Pembagian per pohon dan acuan hitung tangan tidak disebut.
