# Optimization of Artificial Neural Networks using Genetic Algorithm for Palm Fruit Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `said2025optimization` |
| Judul asli | Optimization of Artificial Neural Networks using Genetic Algorithm for Palm Fruit Ripeness Classification |
| Penulis | Wan Said, Wan Zailah; Mardini, Mohamed Ayman; Mohd Tahir, Noor Idayu; Mohd Sahar, Norsuzlin; Tariqul Islam, Mohammad; Mohamid Salih, Noorazlina; Zanil, Mohd Fauzi |
| Tahun | 2025 |
| Venue | Journal of Advanced Research Design |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [said2025optimization.pdf](../pdf/said2025optimization.pdf)
- DOI resmi: https://doi.org/10.37934/ard.127.1.6783

## Gambaran Umum

Kelapa sawit merupakan sumber utama minyak nabati, sehingga ketepatan penentuan tingkat kematangan buah sebelum pengolahan menjadi penting bagi produsen dan eksportir di Malaysia. Penilaian kematangan tandan buah segar (TBS) saat ini dilakukan secara manual dengan mata. Cara ini memakan waktu dan rentan terhadap kesalahan. Kajian ini mengusulkan pendekatan pembelajaran mesin untuk memilah buah kelapa sawit berdasarkan citra. Tujuannya adalah meningkatkan efisiensi dan ketepatan klasifikasi, yang pada akhirnya mendukung pengendalian mutu dan produktivitas.

Data dikumpulkan dari dua sumber. Sumber pertama adalah pengambilan citra langsung di Felda Rasau Kerteh, Terengganu. Sumber kedua adalah set data berlisensi dari platform Roboflow. Citra diklasifikasikan ke dalam tiga kelas, yaitu *unripe*, *ripe*, dan *overripe*, berdasarkan warna, bentuk, dan kilap kulit buah. Penulis menyebutkan bahwa Dewan Minyak Sawit Malaysia (MPOB) membedakan empat tahap kematangan, tetapi kajian ini memakai tiga kelas tersebut. Citra diproses di MATLAB R2023b. Setiap citra diubah ukurannya menjadi 128 x 128 piksel, dinormalisasi, diubah menjadi skala abu-abu, lalu dibinerkan dengan ambang global metode Otsu dan operasi morfologi. Jumlah citra per kelas dan pembagian data latih serta data uji tidak tercantum dalam bagian yang dibaca.

Metode yang digunakan adalah ANN yang bobot dan jumlah neuron tersembunyinya dioptimasi dengan GA. GA mencari jumlah neuron tersembunyi dari 1 sampai 30. Ukuran populasi 100, jumlah generasi 50, dan peluang persilangan serta mutasi masing-masing 0,05. Pada tahap pelatihan, penulis membandingkan tiga algoritma pelatihan ANN. Levenberg-Marquardt menghasilkan akurasi 74,96%. Bayesian regularization menghasilkan akurasi 86,19%. Scaled conjugate gradient menghasilkan akurasi 74,97%. Bayesian regularization disebut paling baik. Akurasi uji awal ANN adalah 77%. Setelah optimasi GA, akurasi naik menjadi 87%, atau peningkatan 10%. Penulis juga mengukur sensitivitas dan spesifisitas, tetapi nilainya tidak tercantum dalam bagian yang dibaca. Kajian ini tidak menghitung jumlah buah per tandan atau per tanaman.

Penulis tidak menyatakan batasan penelitian secara eksplisit dalam bagian yang dibaca. Dari uraian latar belakang, penulis menyebut bahwa sistem klasifikasi berbasis citra sebelumnya peka terhadap perubahan intensitas cahaya, sehingga kurang cocok untuk kondisi pencahayaan yang tidak konsisten. Kajian ini juga bersifat klasifikasi kematangan pada citra, bukan pencacahan buah dengan kebenaran dasar penghitungan. Pengujian pada kondisi lapangan belum dilaporkan dalam bagian yang dibaca.
