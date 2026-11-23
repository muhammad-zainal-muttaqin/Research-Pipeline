# ANN model for apple yield estimation based on feature of tree image

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cheng2015ann` |
| Judul asli | ANN model for apple yield estimation based on feature of tree image |
| Penulis | Cheng, H.; others |
| Tahun | 2015 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [cheng2015ann.pdf](../pdf/cheng2015ann.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2015.01.003

## Gambaran Umum

Kajian ini memperkirakan hasil panen apel per pohon sejak dini dari citra tajuk pohon. Penulis menyatakan bahwa pengambilan jumlah apel dari citra sudah banyak diteliti, tetapi cara menaksir hasil panen dari informasi citra masih perlu didalami. Dua pendekatan terdahulu yang dikutip adalah rumus berbasis jumlah dan diameter apel, serta jaringan saraf yang memerlukan citra dari beberapa periode sehingga hanya cocok mendekati panen. Kajian ini mencoba model untuk fase setengah matang dan fase matang.

Data berasal dari kebun apel milik Universitas Bonn, Jerman (tertulis Kein Altendorf), kultivar "Gala", bentuk tajuk spindel ramping, dengan 70 sampai 170 apel per pohon. Satu citra per pohon diambil dengan kamera digital Canon PowerShot SX110IS dari sisi barat, tegak lurus arah barisan, dengan kain putih sebagai latar. Pengambilan dilakukan saat apel setengah matang dan sekitar setengah bulan sebelum panen. Label berupa bobot panen hasil penimbangan semua apel tiap pohon. Tiap fase memiliki 145 sampel: 120 untuk membangun model dan 25 untuk uji.

Metode: area buah dan jumlah buah diperoleh dengan algoritma pengolahan citra dari rujukan [10], dan area daun dengan membuang latar lalu memisahkan daun dari ranting memakai K-means (pengelompokan piksel menurut nilai G dan H menjadi tiga kelompok). Empat fitur dihitung: rasio area buah terhadap citra, jumlah buah dibagi 170, rasio area buah kecil terhadap area buah, dan rasio area buah terhadap area daun. Fitur itu masuk ke jaringan saraf *backpropagation* (jaringan berlapis yang bobotnya diperbarui dari galat keluaran) tiga lapis, dilatih dengan algoritma Levenberg-Marquardt. Keluarannya hasil panen per pohon yang dinormalisasi dengan 50 kg.

Hasil pada 120 sampel pembangunan: koefisien korelasi R model 0,9287 (setengah matang) dan 0,9804 (matang). Pada 25 sampel uji, R 0,8766 dan 0,9606, galat akar kuadrat rata-rata (RMSE) 2,95 kg dan 2,03 kg, serta galat persentase absolut rata-rata (MAPE) 13,52% dan 8,46%. Metode rumus pembanding memberi R 0,8349 dan 0,8850, RMSE 3,82 kg dan 3,07 kg, serta MAPE 23,37% dan 18,52% pada sampel uji yang sama.

Keterbatasan yang dapat diperiksa: hanya satu sisi pohon dicitrakan sehingga apel di sisi lain atau di balik daun tidak terlihat. Data hanya dari satu kebun, satu kultivar, dan satu bentuk tajuk. Hanya 25 pohon per fase dipakai sebagai uji, dan cara pemisahan 120 dan 25 selain pengacakan tidak disebut. Pembanding hanya satu metode rumus. Teks hasil ekstraksi kehilangan tanda desimal, sehingga nilai di atas dicocokkan dengan abstrak dan selisih yang tertulis di teks.
