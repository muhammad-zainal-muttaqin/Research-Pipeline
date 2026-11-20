# Mass Estimation of Soft Fruit via Oscillatory Plant Dynamics

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wagner2024mass` |
| Judul asli | Mass Estimation of Soft Fruit via Oscillatory Plant Dynamics |
| Penulis | Wagner, Nikolaus; Cielniak, Grzegorz |
| Tahun | 2024 |
| Venue | IEEE International Conference on Automation Science and Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [wagner2024mass.pdf](../pdf/wagner2024mass.pdf)
- DOI resmi: https://doi.org/10.1109/case59546.2024.10711606

## Gambaran Umum

Tinjauan hasil panen memerlukan perkiraan massa, bukan hanya jumlah buah. Metode pencacahan berbasis citra umumnya tidak memperhitungkan berat tiap buah. Metode berbasis volume juga memerlukan informasi kepadatan buah, yang sulit diperoleh secara cepat dan tanpa merusak tanaman. Kajian ini mengusulkan cara non-destruktif untuk memperkirakan massa stroberi individual dengan memanfaatkan sifat dinamis tanaman. Gerakan osilasi jangka pendek yang teramati melalui video *RGB-D* dimodelkan sebagai *damped harmonic oscillator*. Dari parameter model tersebut, massa buah dihitung menggunakan hubungan antara gaya eksitasi, simpangan awal, dan frekuensi eigen.

Data dikumpulkan dari 295 sampel video stroberi dengan dua varietas, yaitu Driscoll's Zara dan Driscoll's Katrina. Pengambilan data dilakukan pada Agustus 2023 di kampus Riseholme, Universitas Lincoln, Inggris. Buah yang digantung di sisi bedengan tabletop dalam polytunnel dipilih karena bebas bergerak. Sensor yang digunakan meliputi sensor gaya Pasco PS-2189 dengan resolusi 0,002 N, timbangan presisi G&G LS200 dengan resolusi 0,01 g, dan kamera Microsoft Azure Kinect dengan citra 1920 x 1080 piksel, 30 Hz, serta resolusi kedalaman 1 mm dari sensor *time-of-flight*. Kamera ditempatkan sekitar 1 m dari buah. Massa referensi berkisar antara 0,75 g hingga 35,57 g. Kekakuan berkisar antara 0,25 N/m hingga 5,86 N/m, dan frekuensi eigen antara 1,23 Hz hingga 6,06 Hz. Pembagian data latih dan uji tidak dilaporkan dalam bagian yang dibaca.

Metode ini menggabungkan stimulus terkendali, pelacakan, dan pemodelan. Buah dideteksi dengan *Mask R-CNN* yang dilatih pada data stroberi di semua tahap kematangan. Pelacakan dilakukan dengan *Simple Online Realtime Tracking* (SORT). Frekuensi eigen ditentukan melalui *Harmonic Inversion*, yang dinyatakan lebih cocok daripada *Fast Fourier Transform* karena resolusi frekuensinya tidak terbatas seperti FFT. Hasil utama menunjukkan median galat 1,16 g pada seluruh sampel. Korelasi antara massa referensi dan estimasi metode ini kuat, dengan koefisien determinasi yang tidak dilaporkan dalam bagian yang dibaca. Sebagai pembanding, metode berbasis volume memperoleh R² = 0,56, dengan galat yang lebih besar pada sebagian besar kategori. Pada buah matang penuh, galat median kedua metode setara, tetapi galat rata-rata metode berbasis osilasi lebih rendah. Bila kekakuan rata-rata seluruh sampel digunakan sebagai pengganti pengukuran gaya, galat rata-rata massa tetap di bawah 25 persen.

Penulis menyatakan bahwa metode ini bergantung pada gerak buah yang dapat diamati. Bila pelacakan gagal karena oklusi atau tabrakan selama gerak, hasilnya menurun. Kondisi terbaik dicapai untuk buah terisolasi yang terlihat jelas tanpa halangan dedaunan. Metode ini juga memerlukan interaksi fisik dengan buah untuk memberi stimulus. Interaksi tersebut dapat merusak tanaman, meskipun penulis mengusulkan penggabungan dengan metode volume untuk memperoleh kepadatan dari sampel kecil. Anotasi data dalam kajian ini masih semi-otomatis dengan koreksi manual. Penulis menyatakan bahwa proses ini dapat dibuat sepenuhnya otomatis. Penulis juga mencatat bahwa data hanya mencakup buah terisolasi, sedangkan stroberi di lapangan sering tumbuh berkelompok. Generalisasi metode ke skenario dan tanaman lain belum jelas, karena pengujian hanya dilakukan pada satu kondisi.
