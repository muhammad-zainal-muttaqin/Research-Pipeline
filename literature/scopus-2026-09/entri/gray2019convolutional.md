# A convolutional neural network for detecting sea turtles in drone imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gray2019convolutional` |
| Judul asli | A convolutional neural network for detecting sea turtles in drone imagery |
| Penulis | Gray, Patrick C.; Fleishman, Abram B.; Klein, David J.; McKown, Matthew W.; B\'ezy, Vanessa S.; Lohmann, Kenneth J.; Johnston, David W. |
| Tahun | 2019 |
| Venue | Methods in Ecology and Evolution |
| Kode | T (Metode dari luar pertanian) |
| Tanaman | olive |

## Tautan Akses
- PDF: [gray2019convolutional.pdf](../pdf/gray2019convolutional.pdf)
- DOI resmi: https://doi.org/10.1111/2041-210x.13132

## Gambaran Umum

Gray dkk. (2019) di *Methods in Ecology and Evolution* menghitung penyu laut dari citra *unoccupied aerial system* (UAS, drone) dengan jaringan saraf konvolusi (*convolutional neural network*, CNN).

Citra dipotong menjadi jendela geser 100 × 100 piksel dengan tumpang tindih 30%. Setiap jendela berisi tiga kanal (Green, Red, dan NIR), dan CNN berukuran kecil (empat lapisan konvolusi dengan 64 kernel 3 × 3, serta *max pooling* 2 × 2) memutuskan apakah jendela itu berisi penyu. Pelatihan memakai 944 contoh penyu dengan *stochastic gradient descent*, laju belajar 0,01, dan momentum Nesterov 0,9 selama 20 *epoch*. Set validasi berisi 1.558 jendela, 153 di antaranya memuat penyu. Dari sisi penghitungan, model ini hanya memutuskan per jendela. Penghitungan per individu dilakukan manual: karena jendela tumpang tindih, satu penyu bisa terdeteksi lebih dari sekali, dan peninjau menghapus duplikat dengan mengurutkan deteksi menurut urutan foto dan memberi label baru pada duplikat (bagian 2.7).

Hasil utama dihitung pada ambang probabilitas 0,93, yang dipilih untuk memprioritaskan *recall*. Dari 2.971.554 jendela, model menandai 6.696 jendela. Hasil tinjauan manual menunjukkan 874 penyu pasti, 218 penyu mungkin, dan 5.402 bukan penyu. Dengan menganggap seluruh penyu di data sudah terdeteksi, *recall* 76,5% dan *precision* 16,3% (Tabel 1: 1.092 benar positif, 336 negatif palsu, 5.604 positif palsu). Penulis menyebut akurasi keseluruhan 99,83% tidak tepat sebagai ukuran karena sebagian besar jendela tidak memuat penyu. Dibanding hitungan manual pada sumber data yang sama, CNN menemukan 8%–9% lebih banyak penyu. Beban validasi manual turun menjadi 1,5% dari jumlah awal, dari 2.971.554 jendela menjadi sekitar 44.800 jendela yang ditinjau (1 jam untuk 6.696 jendela dan 11,8 jam untuk 44.799 jendela).

Batas kajian perlu dicatat. *Precision* 16,3% berarti sebagian besar deteksi adalah positif palsu, sehingga verifikasi manual tetap diperlukan. Penulis sendiri menyebut *precision* di data uji lebih rendah daripada di data validasi, yang mereka tafsirkan sebagai tanda *overfitting* ringan. Angka 0,05 sampai 0,93 juga bergantung pada asumsi bahwa penyu di bawah ambang 0,15 hampir tidak ada. Asumsi ini diterima tanpa pemeriksaan manual penuh pada jendela di bawah 0,05. Kajian tidak mengukur kinerja pada lintas-pandang (*cross-view*) atau deduplikasi otomatis. Penulis menyatakan pendekatan ini berlaku untuk spesies lain yang cukup besar terlihat dari udara di perairan pesisir atau laut. Bukti yang dapat ditransfer dari kajian ini adalah pola jendela-geser plus verifikasi manual.
