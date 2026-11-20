# Yield estimation of pomegranate using image processing techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `behera2019yield` |
| Judul asli | Yield estimation of pomegranate using image processing techniques |
| Penulis | Behera, S.K.; others |
| Tahun | 2019 |
| Venue | International Journal of Innovative Technology and Exploring Engineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | pomegranate |

## Tautan Akses
- PDF: [behera2019yield.pdf](../pdf/behera2019yield.pdf)

## Gambaran Umum

Kajian ini membahas estimasi jumlah buah delima (*Punica granatum*) langsung dari citra yang diambil di pohon. Tujuannya menghitung buah secara otomatis dari foto, sebagai alternatif penghitungan manual yang lambat dan bergantung pada pengamat. Data yang dilaporkan adalah 20 citra pohon delima di lapangan. Jumlah buah hasil hitung manual untuk setiap citra tercantum pada Tabel 1. Naskah tidak menyebut pembagian data latih dan data uji, sehingga seluruh 20 citra tampaknya dipakai untuk mengevaluasi metode.

Metode dibangun dalam dua alur. Alur pertama memisahkan buah dari latar belakang dengan *color thresholding* berbasis ruang warna HSI (naskah menulisnya "HIS"), lalu menerapkan *Circular Hough Transform* (CHT) untuk menemukan objek berbentuk lingkaran sebagai buah. Alur kedua mengganti tahap pemisahan dengan *K-means clustering*, yang juga diikuti CHT. Jumlah buah hasil kedua alur dibandingkan dengan jumlah manual melalui regresi linier, dengan koefisien determinasi (R2) sebagai ukuran kecocokan.

Hasilnya, alur HSI dan CHT memperoleh R2 0,6888 (Fig. 3), sedangkan alur K-means dan CHT memperoleh R2 0,7652 (Fig. 4). Selisih 0,0764 poin R2 ini menjadi dasar kesimpulan penulis bahwa pendekatan K-means lebih baik. Angka tersebut mengukur kecocokan jumlah per citra, bukan akurasi per buah. Naskah tidak melaporkan presisi, recall, atau mAP. Dengan dua nilai R2 dari 20 citra, perbedaan ini tidak disertai uji signifikansi dan belum diuji pada data terpisah.

Keterbatasan kajian yang dapat diperiksa dari teks adalah sebagai berikut. Pertama, jumlah citra kecil (20) dan tidak ada data uji terpisah. Kedua, evaluasi hanya memakai R2 pada tingkat jumlah per citra, sehingga kesalahan pada tingkat objek, yaitu buah yang terlewat atau terhitung ganda dalam satu citra yang kebetulan berjumlah sama, tidak terlihat. Ketiga, teks yang dibaca tidak memuat bagian keterbatasan tersendiri, sehingga kondisi yang membuat metode gagal, misalnya pencahayaan, daun yang menutupi buah, atau buah yang saling bertumpuk, tidak dibahas penulis. Keempat, angka lain yang muncul dalam pendahuluan berasal dari studi lain pada komoditas berbeda dan tidak dipakai sebagai hasil kajian ini.

Secara keseluruhan, kajian ini menunjukkan bahwa penghitungan buah delima berbasis warna dan lingkaran dapat dicocokkan dengan jumlah manual pada 20 citra, dengan R2 tertinggi 0,7652 pada alur K-means. Bukti ini terbatas pada jumlah citra yang kecil dan satu sudut pandang per pohon, sehingga belum cukup untuk menilai ketahanan metode pada kondisi lapangan yang lebih beragam.
