# Sustainable Yield Prediction in Agricultural Areas Based on Fruit Counting Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `saddik2023sustainable` |
| Judul asli | Sustainable Yield Prediction in Agricultural Areas Based on Fruit Counting Approach |
| Penulis | Saddik, Amine; Latif, Rachid; Abualkishik, Abedallah Zaid; El Ouardi, Abdelhafid; Elhoseny, Mohamed |
| Tahun | 2023 |
| Venue | Sustainability Switzerland |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple, other berries |

## Tautan Akses
- PDF: [saddik2023sustainable.pdf](../pdf/saddik2023sustainable.pdf)
- DOI resmi: https://doi.org/10.3390/su15032707

## Gambaran Umum

Kajian ini bertujuan meramalkan hasil pertanian melalui penghitungan buah dengan algoritma berkompleksitas rendah dan dapat berjalan waktu nyata. Penulis berangkat dari kelemahan pendekatan pembelajaran mesin dan pembelajaran mendalam yang memerlukan basis data besar, pelatihan yang lama, papan GPU, serta konsumsi daya tinggi. Usulan yang diajukan tidak memakai data latih dan tidak melatih model, melainkan memakai pemrosesan citra berbasis warna dan bentuk geometris.

Objek kajian adalah apel merah dan hijau, khususnya Red Delicious dan Golden Delicious, pada kebun di wilayah Fes-Meknes dekat Danau Daiit Aoua, Maroko, pada koordinat 33°38′41″ LU dan 5°02′04″ BB, dengan luas 44,12 ha. Data dikumpulkan dengan kamera RGB beresolusi 4608 × 3456 piksel dan 16 Mpx pada 3 September 2020 sekitar pukul 13.30. Karena metode ini tidak melalui pelatihan, tidak ada pembagian himpunan latih dan uji; evaluasi dilakukan pada data lapangan dan pada urutan 50 citra untuk mengukur waktu pemrosesan minimum, maksimum, dan rata-rata.

Algoritma terdiri atas tiga blok. Blok pertama membaca citra RGB dan menerapkan filter median untuk menghilangkan derau garam dan merica. Blok kedua mengubah RGB menjadi HSV, memilih piksel sesuai warna buah dengan ambang nilai hue, misalnya sekitar 0–20° atau 340–360° untuk merah, membentuk topeng biner, lalu mendeteksi buah memakai transformasi Hough pada bentuk lingkaran. Blok ketiga menghitung buah yang terdeteksi dengan perulangan. Implementasi memakai bahasa C/C++ dan pustaka OpenCV, lalu dijalankan pada dua perangkat, yaitu komputer meja dan sistem tertanam Raspberry Pi 3B+ dengan prosesor Broadcom Cortex-A53 1,4 GHz dan RAM 1 GB LPDDR2.

Hasil pengukuran menunjukkan komputer meja memproses satu citra dalam waktu minimum 14,2 ms, rata-rata 25,52 ms, dan maksimum 38 ms, atau 40 citra per detik. Raspberry Pi 3B+ membutuhkan 39,2 ms, 63,08 ms, dan 88 ms secara berturut-turut, atau 15 citra per detik. Pengukuran per blok menunjukkan blok pertama memakan 6,6 ms pada komputer meja dan 19,02 ms pada Raspberry; blok kedua 16,4 ms dan 34,05 ms; blok ketiga 2,5 ms dan 10,01 ms. Akurasi deteksi dilaporkan 98,45% pada komputer meja dan 95,04% pada Raspberry, dengan kisaran masing-masing 94,98–98,91% dan 91,05–98,77%. Tabel perbandingan mencantumkan akurasi metode usulan 95,04–97,22% pada Raspberry Pi dengan algoritma HSV-Hough dan 15 fps, dibandingkan beberapa kajian berbasis GPU yang mencapai 2–17 fps.

Batasan yang dinyatakan penulis adalah kamera RGB tidak dapat mengukur kedalaman, sehingga apel di belakang tidak dapat dihitung; penulis menyarankan putaran 360° mengelilingi tanaman agar semua buah terhitung dengan galat minimum. Penulis juga menyatakan komputer meja lebih cepat tetapi memiliki konsumsi daya dan berat yang tinggi untuk drone dan robot darat, sehingga Raspberry dipilih karena biaya dan dayanya rendah. Pekerjaan berikutnya diarahkan pada akselerasi dengan CPU-GPU atau CPU-FPGA serta penggunaan data cuaca dan riwayat hasil panen.

