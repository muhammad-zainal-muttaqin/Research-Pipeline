# Innovative Flood Impact Monitoring and Harvest Analysis in Oil Palm Plantations Utilizing Geographic Information Systems and Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `puttinaovarat2025innovative` |
| Judul asli | Innovative Flood Impact Monitoring and Harvest Analysis in Oil Palm Plantations Utilizing Geographic Information Systems and Deep Learning |
| Penulis | Puttinaovarat, Supattra; Chai-Arayalert, Supaporn; Saetang, Wanida; Khaimook, Kanit; Plaiklang, Sasikarn; Horkaew, Paramate |
| Tahun | 2025 |
| Venue | Agriengineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [puttinaovarat2025innovative.pdf](../pdf/puttinaovarat2025innovative.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering7020044

## Gambaran Umum

Penelitian ini bertujuan mengembangkan metode dan aplikasi untuk memeriksa kebun kelapa sawit yang terdampak banjir saat panen. Banjir sering terjadi setiap tahun di wilayah selatan Thailand dan menggenangi kebun selama beberapa hari, sehingga tandan yang sudah matang tidak dapat dipanen. Survei lapangan untuk menilai kerugian memakan waktu, dan belum ada platform yang secara khusus menilai dampak banjir terhadap panen kelapa sawit. Penulis mengusulkan sistem yang memadukan *pembelajaran mendalam* dengan Sistem Informasi Geografis (SIG). Sistem ini mengklasifikasikan area yang terdampak banjir dan menentukan tingkat kematangan tandan pada pohon. Penulis juga menyatakan bahwa kajian terdahulu umumnya bergantung pada lingkungan terkendali dan dataset kecil, serta lebih banyak meneliti kematangan tandan setelah panen daripada kematangan tandan di pohon.

Data penelitian terdiri atas citra digital tandan kelapa sawit di pohon dan citra kebun yang terdampak banjir. Untuk klasifikasi kematangan, jumlah citra mencapai 9223, terdiri atas 4225 citra kelas matang dan 4998 citra kelas belum matang. Sebanyak 500 citra dipakai untuk validasi, dengan 250 citra per kelas. Untuk klasifikasi banjir, 6350 citra dipakai sebagai data latih, terbagi rata menjadi 3175 citra banjir dan 3175 citra tidak banjir. Data validasi banjir terdiri atas 1000 citra, dengan 500 citra per kelas. Data spasial untuk pemantauan banjir berasal dari sumber termasuk ESRI yang diakses melalui API. Penulis menyatakan bahwa dataset tersebut belum tersedia untuk umum.

Penelitian ini membandingkan tiga model pada tugas yang sama, yaitu *MobileNet*, *Random Forest* (RF), dan *Support Vector Machine* (SVM). MobileNet memproses citra secara langsung. RF dan SVM memakai fitur hasil ekstraksi dari *InceptionV3*, model pralatih yang dipakai untuk menghasilkan representasi fitur. Model CNN dengan MobileNet memakai 100 *epoch*, ukuran *batch* 32, laju pembelajaran 0,01, dan fungsi aktivasi ReLU. RF memakai 10 pohon, sedangkan SVM memakai kernel RBF dengan 100 iterasi. MobileNet memperoleh akurasi tertinggi sehingga dipilih sebagai model klasifikasi utama. Model ini kemudian diintegrasikan ke dalam aplikasi untuk pemantauan dan analisis secara real-time. Metode yang diusulkan mencapai akurasi klasifikasi banjir sebesar 96,80% sampai 98,29%. Untuk klasifikasi kematangan tandan di pohon, akurasinya berkisar antara 97,60% dan 99,75%. Evaluasi juga memakai *recall*, *precision*, dan *F-score* sebagai metrik.

Penulis menyatakan bahwa dataset penelitian belum dapat diakses publik, dan rencana untuk membukanya akan dipertimbangkan guna mendukung penelitian lanjutan.
