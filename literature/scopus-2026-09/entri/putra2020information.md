# Using information from images for plantation monitoring: A review of solutions for smallholders

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `putra2020information` |
| Judul asli | Using information from images for plantation monitoring: A review of solutions for smallholders |
| Penulis | Putra, Bayu Taruna Widjaja; Soni, Peeyush; Marhaenanto, Bambang; Pujiyanto; Sisbudi Harsono, Soni; Fountas, Spyros |
| Tahun | 2020 |
| Venue | Information Processing in Agriculture |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | coffee |

## Tautan Akses
- PDF: [putra2020information.pdf](../pdf/putra2020information.pdf)
- DOI resmi: https://doi.org/10.1016/j.inpa.2019.04.005

## Gambaran Umum

Kajian ini merupakan tinjauan kritis tentang pemanfaatan informasi citra untuk pemantauan perkebunan dalam kerangka *decision support system* (DSS). Penulis menyoroti kebutuhan petani kecil di negara berkembang akan teknologi yang murah untuk memantau tanaman seperti kopi, kakao, dan tanaman tahunan lainnya. Masalah yang diangkat adalah mahalnya kamera hiperspektral serta keterbatasan infrastruktur jaringan dan akses internet. Penulis juga mencatat bahwa petani sering melakukan pengukuran secara manual dan mencatat hasilnya dengan tidak tepat. Tujuan tinjauan ini adalah menguraikan konsep dasar dan praktik terbaik penggunaan citra dari satu *digital camera*, serta mengusulkan protokol yang dapat dipakai petani kecil untuk membangun sistem pemantauan kegiatan kebun yang terintegrasi.

Sebagai tinjauan, artikel ini tidak memuat dataset baru, jumlah citra, atau pembagian data latih dan data uji. Cakupannya meliputi kamera digital konsumen, sensor RGB dan *near-infrared* (NIR), *unmanned aerial vehicle* (UAV) berbiaya rendah, serta *remote sensing* berbasis darat. Penulis menekankan kondisi perkebunan dengan pohon peneduh yang rapat, sistem agroforestri, dan lahan sempit. Pembahasan disusun dalam beberapa bagian, yaitu sifat citra dan informasi tambahan pada *header* citra seperti waktu dan koordinat, kerangka sistem, pemanfaatan sensor posisi, implementasi kerangka, serta tantangan dan prospek. Artikel ini tidak berfokus pada satu lokasi perkebunan tertentu.

Metode yang digunakan adalah tinjauan literatur kritis. Hasil utamanya berupa kerangka sistem yang memakai kode QR untuk menautkan citra ke posisi setiap tanaman dan merekam data deret waktu kesehatan tanaman. Penulis mengacu pada Liu dkk. yang menyatakan bahwa kode QR tetap dapat digunakan pada berbagai kondisi pencahayaan. Pada bidang hasil panen, Ramos dkk. mengembangkan sistem visi jarak dekat untuk menghitung dan mengidentifikasi buah kopi yang dapat dan tidak dapat dipanen. Sistem itu dinilai memberikan hasil yang dapat diterima, tetapi masih memerlukan kajian lebih mendalam. Penghitungan buah mangga juga dibahas oleh Zandbergen dan Barbeau. Untuk hama dan penyakit, kamera konsumen dilaporkan mampu membantu mengenali ratusan jenis hama dan penyakit pada tanaman. Tinjauan ini tidak melaporkan angka kuantitatif dari eksperimen baru, sehingga nilai akurasi atau presisi hanya dapat dirujuk dari studi lain.

Penulis menyatakan beberapa batasan. Metode penghitungan buah memerlukan parameter tambahan, seperti *F-stop* dan informasi dari *depth of field* (DOF), agar jarak pengukuran dapat diperluas. Kondisi pencahayaan kebun dinyatakan sangat bervariasi. Pengukuran tinggi dan diameter pohon masih sering dilakukan secara manual, sedangkan alat khusus bermerek masih mahal bagi petani kecil. Penulis juga menekankan bahwa pengolahan citra membutuhkan pengetahuan teknologi informasi, serta aspek ekonomi dan perilaku petani perlu dipertimbangkan sebelum merekomendasikan solusi. Penulis mendorong lembaga publik dan para pakar berperan dalam memperbaiki infrastruktur dasar, terutama untuk pengolahan citra dan video.
