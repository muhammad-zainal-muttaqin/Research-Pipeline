# Passion fruit detection and counting based on multiple scale faster R-CNN using RGB-D images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tu2020passion` |
| Judul asli | Passion fruit detection and counting based on multiple scale faster R-CNN using RGB-D images |
| Penulis | Tu, Shuqin; Pang, Jing; Liu, Haofeng; Zhuang, Nan; Chen, Yong; Zheng, Chan; Wan, Hua; Xue, Yueju |
| Tahun | 2020 |
| Venue | Precision Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | passion fruit |

## Tautan Akses
- PDF: [tu2020passion.pdf](../pdf/tu2020passion.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-020-09709-3

## Gambaran Umum

Penulis menyatakan bahwa buah markisa hijau kecil sulit dideteksi di bawah cahaya berubah dan oklusi, dan bahwa penghitungan hasil memerlukan deteksi buah kecil. Penelitian ini mengusulkan MS-FRCNN, yaitu *Faster R-CNN* dengan fitur multiskala, pada citra RGB dan depth. *Faster R-CNN* adalah detektor dua tahap yang mengusulkan area kandidat lalu mengklasifikasikannya.

Data berupa 2.275 citra RGB-D dari Kinect v2 di dua kebun markisa, Heyuan (2016) dan Conghua (2017). Sebanyak 1.900 citra dipakai untuk latih dan validasi setelah augmentasi, 100 citra untuk uji tambahan, dan 275 citra untuk penghitungan dengan 7.032 buah beranotasi. Anotasi dibuat manual dengan Labelme. Teks tidak menyebut pembagian per pohon.

Metode mengambil fitur dari conv3, conv4, dan conv5 untuk RPN dan *RoI pooling*. RPN adalah jaringan yang mengusulkan kotak kandidat. Detektor RGB dan depth dilatih terpisah, lalu digabung linier dengan λ = 0,4.

Hasil fusi RGB-D pada Tabel 3: presisi 0,962, recall 0,931, dan F1 0,946. Faster R-CNN VGG-16 mencapai F1 0,885. Pada 275 citra penghitungan, MS-FRCNN memperoleh 6.205 benar, 827 terlewat, 409 salah, dan F1 0,909 (Tabel 5). Detektor depth saja pada ResNet-101 mencapai F1 0,841.

Keterbatasan yang dapat diperiksa dari teks: teks menyebut 1.008 buah pada 100 citra uji tambahan, tetapi Tabel 3 memakai 1.020 buah tanpa penjelasan asal jumlah itu. Detektor depth lebih lemah karena derau sinar matahari. Teks mengakui F1 turun menjadi 0,755 pada buah yang tumpang tindih.
