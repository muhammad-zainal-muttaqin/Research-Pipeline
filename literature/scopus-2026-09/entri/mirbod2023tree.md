# On-tree apple fruit size estimation using stereo vision with deep learning-based occlusion handling

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mirbod2023tree` |
| Judul asli | On-tree apple fruit size estimation using stereo vision with deep learning-based occlusion handling |
| Penulis | Mirbod, Omeed; Choi, Daeun; Heinemann, Paul H.; Marini, Richard P.; He, Long |
| Tahun | 2023 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [mirbod2023tree.pdf](../pdf/mirbod2023tree.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2022.12.008

## Gambaran Umum

Ukuran buah apel berperan penting dalam pengelolaan kebun, terutama pada penjarangan buah dengan bahan kimia, penilaian mutu, dan prediksi hasil. Pengukuran manual memakai jangka sorong atau cincin ukur. Cara ini padat karya, bergantung pada penilaian manusia dalam memilih sampel, dan rawan galat. Penelitian ini bertujuan membangun sistem visi mesin yang dapat mengukur ukuran apel secara akurat di lapangan, pada berbagai tahap kematangan, dari platform yang bergerak. Dasar masalahnya adalah penjarangan kimiawi dan pengelolaan beban panen memerlukan galat dalam satuan milimeter.

Tanaman yang diteliti adalah apel (*Malus domestica*) pada pohon berbentuk spindel yang tingginya mencapai 4,3 m. Sistem memakai sepasang kamera stereo beresolusi 8,9 MP dengan lensa 8 mm, serta lampu *strobe* LED yang disinkronkan dengan kamera untuk mengurangi pengaruh cahaya siang yang berubah-ubah dan kabur gerak. Sistem dapat ditarik kendaraan atau didorong manual di sepanjang baris kebun. Uji lapangan dilakukan setiap bulan dari Juni hingga Oktober, dengan diameter buah yang diukur berkisar 22 sampai 82 mm. Sebelum uji lapangan, percobaan terkendali di laboratorium dengan cahaya lampu fluoresen 600 lux menguji seberapa besar pengaruh bentuk buah terhadap ukuran berbasis citra.

Metode utamanya memakai dua model jaringan saraf dalam, yaitu *Faster R-CNN* dan *Mask R-CNN*, untuk mendeteksi buah yang layak diukur. Buah yang tertutup sebagian dilengkapi dengan ekstrapolasi area yang tertutup. Bentuk hasil segmentasi kemudian diubah menjadi luas permukaan dan diameter dalam satuan metrik, memakai resolusi spasial dan informasi kedalaman dari kamera stereo. Penulis menurunkan hubungan jarak kerja, panjang fokus lensa, dan resolusi sensor untuk memilih lensa 8 mm, sehingga satu milimeter di dunia nyata terwakili minimal oleh satu piksel pada jarak kerja maksimum sekitar 2,4 m. Hasil lapangan menunjukkan galat rerata absolut diameter 1,1 sampai 4,2 mm selama lima bulan. Galat rata-rata terhadap pengukuran diameter sebenarnya adalah 4,8%. Simpangan baku galat berada pada rentang 0,7 sampai 1,9 mm.

Penulis menyimpulkan bahwa pemilihan *neural network* untuk memilih buah dan ekstrapolasi area yang tertutup dapat menjadi alternatif untuk menangani oklusi buah dalam pencitraan pertanian serta meningkatkan akurasi pengukuran ukuran. Pembahasan lebih rinci mengenai keterbatasan penelitian tidak termuat dalam ringkasan ini.
