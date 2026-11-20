# ChatGPT and general-purpose AI count fruits in pictures surprisingly well without programming or training

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mengsuwan2024chatgpt` |
| Judul asli | ChatGPT and general-purpose AI count fruits in pictures surprisingly well without programming or training |
| Penulis | Mengsuwan, Konlavach; Rivera-Palacio, Juan C.; Ryo, Masahiro |
| Tahun | 2024 |
| Venue | Smart Agricultural Technology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | cherry, coffee |

## Tautan Akses
- PDF: [mengsuwan2024chatgpt.pdf](../pdf/mengsuwan2024chatgpt.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2024.100688

## Gambaran Umum

Studi ini menguji apakah model kecerdasan buatan serba guna dapat mencacah buah kopi (ceri kopi) dari foto tanpa pemrograman dan tanpa pelatihan khusus. Pencacahan buah merupakan tugas dasar digitalisasi pertanian, dan praktik standarnya bergantung pada anotasi data dan pelatihan model. Penulis membandingkan GPT-4 V (ChatGPT) dalam dua mode, yaitu *zero-shot* (tanpa contoh) dan *few-shot* (dengan contoh dan umpan balik), dengan model *foundation* untuk penghitungan objek bernama T-Rex. Sebagai pembanding terlatih, dipakai YOLOv8. Studi ini bersifat eksploratif dan disajikan sebagai catatan aplikasi.

Data yang dipakai adalah 100 foto cabang pohon kopi yang diambil di kebun petani lokal di Kolombia pada musim panen 2022. Foto diambil dengan ponsel pintar (Samsung, Xiaomi, dan Motorola) dalam cahaya alami antara pukul 06.00 dan 18.00, dengan variasi awan dan bayangan. Resolusi citra berkisar 1 sampai 18 megapiksel, dengan rerata 11,27 megapiksel. Jumlah ceri per citra dihitung manual dan berkisar 1 sampai 80 buah. Seratus citra ini hanya dipakai untuk uji. YOLOv8 dilatih pada 436 citra dengan 35.694 objek ceri berlabel dari studi sebelumnya. Setiap citra diperlakukan sebagai satu pandang, tanpa penautan antarfoto.

Metode dinilai dengan koefisien determinasi R² terhadap jumlah manual. Hasilnya: YOLOv8 mencapai R² 0,900, dan T-Rex mencapai R² 0,923 setelah penulis menggambar tiga kotak batas secara manual pada setiap citra sebagai petunjuk. GPT-4 V mencapai R² 0,360 pada mode zero-shot dan R² 0,460 setelah diberi umpan balik bahwa jumlahnya terlalu rendah atau terlalu tinggi. Kedua mode GPT-4 V cenderung meremehkan jumlah dan tidak menyebut angka di atas 45 pada citra mana pun. Waktu untuk 100 citra adalah sekitar 0,83 jam untuk T-Rex, 1,75 jam dan 3,25 jam untuk GPT-4 V (zero-shot dan few-shot), dan sekitar 161 jam untuk YOLOv8. Angka YOLOv8 itu mencakup anotasi, pelatihan selama 75 menit, dan prediksi 30 milidetik per citra. Penulis juga mencatat bahwa jumlah citra anotasi YOLOv8 tidak konsisten antarbagian. Bagian metode menyebut 436 citra dan 35.694 objek, sedangkan bagian hasil menyebut 500 citra dan 30.000 ceri.

Penulis menyatakan batasan berikut. Studi ini eksploratif dan hanya menguji 100 citra, sehingga perlu validasi yang lebih luas. Hasil GPT-4 V sulit diulang karena model tidak memungkinkan pengaturan *random seed* dan parameter lain. Akun GPT-4 V mengalami batas penggunaan empat kali, dengan batas 40 pesan per tiga jam pada Maret 2024. T-Rex memerlukan penggambaran kotak secara manual, dan penulis tidak menguji jenis objek lain. Evaluasi hanya memakai R², bukan mAP, karena tujuan studi adalah estimasi jumlah dan bukan deteksi.
