# An extensive review on agricultural robots with a focus on their perception systems

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `thakur2023extensive` |
| Judul asli | An extensive review on agricultural robots with a focus on their perception systems |
| Penulis | Thakur, Abhishek; Venu, Sangeeth; Gurusamy, Muralimohan |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [thakur2023extensive.pdf](../pdf/thakur2023extensive.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108146

## Gambaran Umum

Tinjauan ini membahas robot pertanian dengan penekanan pada sistem persepsinya. Pertanian menghadapi kekurangan tenaga kerja, kelelahan pekerja, dan kondisi kerja yang berat. Penulis menyebut bahwa menurut perkiraan Organisasi Pangan dan Pertanian (FAO), produksi pangan perlu meningkat hingga 70 persen, sejalan dengan populasi dunia yang diperkirakan mencapai 9,1 miliar pada 2050. Dalam konteks ini, *machine vision* dipandang sebagai komponen utama yang memungkinkan mesin bekerja terus-menerus dengan efisiensi tinggi.

Tinjauan ini tidak berfokus pada satu kumpulan data. Cakupannya adalah sistem *machine vision* dalam pertanian, yang terdiri dari tiga tahap utama: akuisisi citra, pemrosesan citra, dan klasifikasi citra. Sistem tersebut memakai satu atau beberapa kamera, sumber cahaya, mikrokontroler atau mikroprosesor, lalu algoritme pengambilan keputusan. Hasilnya dapat dipakai sebagai sinyal untuk menggerakkan robot, manipulator, atau kendaraan. Penulis membahas penerapan pada penyiangan, penyemprotan pestisida, panen, penyemaian, penghitungan buah, penyortiran, dan pemetaan jalur kendaraan otonom. Sensor yang dibahas meliputi kamera monokular, sistem stereo binokular, dan pencitraan penginderaan jauh.

Pada kamera monokular, penulis mencontohkan Zhao dkk. (2005) yang mengganti kamera hitam-putih dengan kamera RGB dan melaporkan akurasi 90 persen dalam mengidentifikasi apel berdasarkan warna dan tekstur. Chen dkk. (2020) memakai kamera RGB monokular dengan VGG-16 yang memiliki 16 lapis untuk memposisikan paprika, dengan rata-rata kesalahan 18,3 persen dalam piksel terhadap posisi pusat buah. Pada sistem stereo binokular, Xiang dkk. (2014) memakai citra stereo untuk memperoleh peta kedalaman tomat yang bergerombol, lalu memisahkan area yang saling tumpang tindih. Wang dkk. (2016) menerapkan stereo untuk melokalisasi leci. Roy dan Isler (2016) memakai sistem monokular untuk memperoleh jumlah dan ukuran apel dalam kluster padat. Tinjauan ini tidak menyajikan perbandingan kuantitatif terpadu antarmetode.

Penulis menegaskan bahwa kamera monokular merupakan teknik berbiaya rendah, tetapi hanya memberikan informasi dua dimensi. Menurut Zhao dkk. (2016), pendekatan ini juga berisiko terdampak perubahan iluminasi. Stereo binokular memberikan representasi yang lebih rinci karena menambahkan sumbu ketiga untuk mengukur kedalaman, dimensi, dan geometri objek. Penulis juga menyebut penginderaan jauh sebagai cara mengukur radiasi elektromagnetik yang dipantulkan atau dipancarkan suatu benda. Untuk pencitraan hiperspektral, penulis mencatat keterbatasan berupa kompleksitasnya.

Batasan yang dinyatakan penulis terutama terkait iluminasi. Deteksi jeruk sulit dilakukan secara efektif karena iluminasi yang bervariasi dan pantulan cahaya dari buah tetangga serta gangguan latar belakang. Monokular hanya memberikan informasi dua dimensi dan rentan terhadap perubahan iluminasi. Penulis juga menyatakan bahwa tinjauan ini menyoroti celah penelitian yang masih terbuka. Dengan demikian, kajian ini memberikan landasan konseptual tentang sensor dan tahapan pengolahan citra untuk pertanian, tetapi tidak menyajikan hasil eksperimen baru.
