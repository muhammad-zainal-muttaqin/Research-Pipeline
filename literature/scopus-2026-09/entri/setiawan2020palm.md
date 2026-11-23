# Palm Oil Fresh Fruit Bunch Grading System Using Multispectral Image Analysis in HSV

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `setiawan2020palm` |
| Judul asli | Palm Oil Fresh Fruit Bunch Grading System Using Multispectral Image Analysis in HSV |
| Penulis | Setiawan, Agung W.; Prasetya, Oktavian E. |
| Tahun | 2020 |
| Venue | 2020 IEEE International Conference on Informatics Iot and Enabling Technologies Iciot 2020 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [setiawan2020palm.pdf](../pdf/setiawan2020palm.pdf)
- DOI resmi: https://doi.org/10.1109/iciot48696.2020.9089431

## Gambaran Umum

Kajian ini menguji apakah citra multispektral pada 19 panjang gelombang dapat membedakan tingkat kematangan tandan buah segar sawit varietas *nigrescens*. Penulis menyebut bahwa produktivitas pabrik sawit Indonesia rendah dan bahwa penilaian kematangan bergantung pada manusia. Tujuan kajian adalah menemukan panjang gelombang terbaik untuk sistem penilaian objektif berbasis ruang warna HSV (*hue*, *saturation*, *value*).

Data berupa 24 tandan: 14 mentah, 9 matang, dan 1 terlalu matang. Setiap tandan difoto dengan 19 sumber cahaya LED dalam rentang 615 sampai 940 nm, sehingga totalnya 456 citra (266, 171, dan 19). Teks menyebut pemotretan dilakukan dalam kondisi tertutup dan gelap. Teks tidak menyebut tanaman, lokasi pemotretan, atau cara penentuan label per tandan.

Latar belakang dihapus dengan konversi keabuan, ambang 50, dan masking. Citra RGB diubah ke HSV, lalu rerata nilai piksel tiap kanal dihitung. Perbandingan dilakukan pada rerata *hue* (H), *saturation* (S), dan *value* (V). Tidak ada model klasifikasi yang dilatih, sehingga penilaian bersifat visual dari sebaran nilai rerata.

Hasil utama: pada 940 nm, sebaran rerata nilai *hue* tandan matang kecil (sekitar 11 sampai 14), dan tumpang tindih antara mentah dan terlalu matang lebih kecil dibanding panjang gelombang lain. Teks tidak melaporkan akurasi, presisi, atau galat klasifikasi untuk panjang gelombang mana pun. Kesimpulan penulis bahwa 940 nm membedakan dua kelas dengan jelas tidak disertai angka uji.

Keterbatasan yang dapat diperiksa: tidak ada pembagian latih dan uji. Hanya satu tandan terlalu matang. Pemilihan 940 nm bergantung pada perbandingan visual grafik. Teks menyatakan bahwa penghapusan latar belakang memberi hasil serupa, dan penulis menyarankan tidak memakainya.
