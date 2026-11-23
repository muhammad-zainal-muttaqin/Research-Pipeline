# Identification and yield estimation of mature fruits using modified watershed algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `prabhu2021identification` |
| Judul asli | Identification and yield estimation of mature fruits using modified watershed algorithm |
| Penulis | Prabhu, Akshatha; Lakshmi, Shree |
| Tahun | 2021 |
| Venue | 2021 2nd International Conference for Emerging Technology Incet 2021 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, tomato |

## Tautan Akses
- PDF: [prabhu2021identification.pdf](../pdf/prabhu2021identification.pdf)
- DOI resmi: https://doi.org/10.1109/incet51464.2021.9456198

## Gambaran Umum

Prabhu dan Lakshmi (2021) menyebut identifikasi dan penentuan lokasi buah sebagai pekerjaan yang rumit dan memakan waktu. Mereka mengajukan kerangka yang memisahkan buah dari latar, menentukan lokasinya, dan mencacahnya untuk estimasi hasil panen. Kerangka ini dirancang untuk buah matang dan dikaitkan dengan robot pemanen. Penulis juga menyebut buah yang tumpang tindih sebagai tantangan.

Data berupa 245 citra yang diambil dari sumber Google, bukan dari kebun yang dicitrakan penulis. Rinciannya 40 apel, 20 paprika, 40 ceri, 15 cabai, 30 delima, 30 raspberi, 30 stroberi, dan 40 tomat. Latarnya kompleks dan pencahayaannya beragam. Pemberi label tidak disebut. Citra acuan segmentasi dibuat dengan perangkat lunak Photoshop. Pembagian latih dan uji tidak disebut, karena metodenya berbasis aturan dan ambang.

Metode terdiri atas tiga tahap. Pertama, citra diubah ke ruang warna *L\*a\*b\** dan diberi ambang per kanal untuk menghapus latar. Kedua, *marker controlled watershed* (transformasi daerah aliran yang dibatasi penanda, untuk memisahkan buah yang bersentuhan) memisahkan buah yang tumpang tindih. Ketiga, deteksi tepi *Canny*, deteksi kontur, dan *circular Hough transform* (pemungutan suara untuk mendeteksi pola lingkaran) mencacah buah. Setiap citra dicacah sendiri.

Hasil segmentasi diukur dengan indeks Dice terhadap citra acuan: apel 82,1%, delima 80,2%, tomat 87,7%, ceri 82,4%, paprika 74,4%, cabai 70,3%, raspberi 73,2%, stroberi 71,5%. Untuk pencacahan, 196 dari 245 citra dicacah benar dibandingkan hitung tangan, dan teks menulis akurasinya 85,21%. Per jenis, 39 dari 40 citra apel, 39 dari 40 tomat, 39 dari 40 ceri, 26 dari 30 delima, 30 dari 40 stroberi, 20 dari 30 raspberi, dan 12 citra paprika benar. Abstrak dan simpulan menyebut 97,5% untuk apel dan tomat.

Keterbatasan dapat diperiksa dari teks. Tidak ada pembagian data uji terpisah dan tidak ada pembanding metode lain. Angka 196 dari 245 setara 80,0%, bukan 85,21% seperti tertulis. Dice dilaporkan untuk 5 citra per jenis pada Tabel I. Metode gagal pada buah yang tidak bulat dan pada buah tertutup. Pencacahan hanya pada satu citra, tanpa penggabungan antarcitra.
