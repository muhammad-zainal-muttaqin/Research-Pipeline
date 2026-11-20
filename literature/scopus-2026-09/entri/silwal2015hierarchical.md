# A hierarchical approach of apple identification for robotic harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `silwal2015hierarchical` |
| Judul asli | A hierarchical approach of apple identification for robotic harvesting |
| Penulis | Silwal, A.; others |
| Tahun | 2015 |
| Venue | American Society of Agricultural and Biological Engineers Annual International Meeting 2015 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [silwal2015hierarchical.pdf](../pdf/silwal2015hierarchical.pdf)

## Gambaran Umum

Penelitian ini membahas kesulitan identifikasi buah apel pada sistem pemanen robotik. Buah yang tertutup sebagian atau berkelompok sulit dikenali dari satu citra. Masalah ini sering menjadi hambatan utama bagi pengembangan sistem pemanen robotik komersial. Penulis mengusulkan pendekatan hierarkis. Buah yang paling terlihat dipanen lebih dahulu. Setelah itu, tanaman dicitrakan ulang agar buah yang sebelumnya tertutup menjadi lebih terlihat. Tujuan kajian adalah mengevaluasi akurasi identifikasi dan akurasi panen dari pendekatan tersebut di lapangan.

Percobaan dilakukan di kebun komersial di Prosser, Washington, pada musim panen 2014. Tanaman yang diamati adalah apel Jazz yang dibentuk dalam arsitektur *tall spindle*, dengan jarak baris 2,74 m dan jarak antarpohon 1,17 m. Rata-rata tinggi pohon 427 cm dengan rata-rata 90 buah per pohon. Kamera CCD Prosilica GigeE 1290C dengan lensa 6 mm dipasang sekitar 1 m dari batang. Citra berukuran 1280 x 960 piksel. Buah berdiameter 6 sampai 8 cm terpetakan menjadi sekitar 35 sampai 70 piksel. Kamera ditempatkan dalam platform *over-the-row* beratap tertutup dengan lampu LED difus, sehingga citra siang dan malam sama-sama dipakai. Setiap sisi kanopi dicitrakan dalam enam bagian yang saling tumpang tindih. Total 740 citra diambil dari 240 bagian kanopi pada 20 pohon. Sebanyak 1827 buah tercatat melalui hitungan manual.

Metode yang dipakai menggabungkan *circular Hough transform* (CHT) dan *blob analysis* (BA). CHT mengenali buah yang terlihat jelas, sedangkan BA mendeteksi buah yang tertutup sebagian. Pada iterasi pertama, buah yang terdeteksi CHT dipanen lebih dahulu. Pada iterasi berikutnya, buah yang terdeteksi oleh CHT dan BA dipertimbangkan. Buah prioritas kemudian dipetik tangan oleh pekerja untuk menunjukkan konsep. Proses berhenti ketika algoritma tidak lagi menemukan buah. Hasilnya, algoritma mendeteksi 1789 dari 1827 buah, dengan akurasi identifikasi 98%. Kesalahan negatif palsu sebesar 2% (38 buah), dan positif palsu sebesar 7% (130 hitungan). Sekitar 80% buah dipanen dari satu sisi kanopi, dan sisanya dari sisi seberang. Waktu hitung rata-rata pada iterasi pertama sekitar 6 s per citra. Waktu ini turun di bawah 1 s untuk citra tanpa buah.

Penulis menyebut beberapa batasan. Sebagian kesalahan negatif terjadi karena buah tidak terlihat dari kedua sisi kanopi. Beberapa buah sepenuhnya hijau sehingga tidak dikenali algoritma. Positif palsu terutama berupa hitungan ganda untuk satu buah. Penulis menyarankan informasi lokasi 3D untuk mengurangi hitungan ganda tersebut. Kecepatan komputasi belum dioptimalkan, karena implementasi memakai Matlab R2014a tanpa optimasi. Penulis juga mengabaikan deteksi rintangan, sehingga semua buah yang teridentifikasi dianggap dapat dipanen. Pemanenan dalam penelitian ini dilakukan secara manual.
