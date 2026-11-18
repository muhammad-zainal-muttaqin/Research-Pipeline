# Machine vision systems in precision agriculture for crop farming

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mavridou2019machine` |
| Judul asli | Machine vision systems in precision agriculture for crop farming |
| Penulis | Mavridou, Efthimia; Vrochidou, Eleni; Papakostas, George A.; Pachidis, Theodore; Kaburlasos, Vassilis G. |
| Tahun | 2019 |
| Venue | Journal of Imaging |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [mavridou2019machine.pdf](../pdf/mavridou2019machine.pdf)
- DOI resmi: https://doi.org/10.3390/jimaging5120089

## Gambaran Umum

Tinjauan ini menyajikan perkembangan terkini penerapan visi mesin pada pertanian presisi, terutama budidaya tanaman. Pertanian presisi didefinisikan sebagai cara mengelola usaha tani dengan memantau, mengukur, dan merespons keragaman tanaman guna mengoptimalkan hasil atas masukan sembari menjaga sumber daya. Visi mesin dipandang mampu menggantikan pekerjaan manual yang melelahkan dan rawan salah, sedangkan algoritma pembelajaran mesin memungkinkan analisis data dalam jumlah besar secara cepat. Kajian ini dimaksudkan sebagai panduan bagi peneliti dan praktisi, dengan cakupan enam bidang, yaitu deteksi tanaman dan buah, dukungan panen meliputi pengkelasan mutu, deteksi kematangan, penghitungan buah, dan prakiraan hasil, perlindungan kesehatan tanaman meliputi deteksi gulma, serangga, penyakit, dan kekurangan hara, jenis kamera, sistem kemudi kendaraan berbasis visi, serta robot pertanian seluler otonom.

Tinjauan disusun mengikuti prosedur Kitchenham dan pendekatan Benitti. Pencarian memakai Google Scholar dengan kata kunci "machine vision in agriculture" dan "agricultural robots" untuk publikasi setelah tahun 2017 dalam bahasa Inggris. Pencarian awal menghasilkan 229 makalah, sebagian dibuang karena metodologi tidak jelas, daftar pustaka tidak memadai, atau penerbit bereputasi rendah. Studi yang dipertahankan harus melaporkan penggunaan visi mesin pada budidaya tanaman atau robot pertanian berbasis visi dalam rentang waktu tersebut. Penulis menyatakan bahwa fokus penyusunan adalah pada hasil tinjauan, bukan pada prosedur pelaksanaannya. Kajian ini juga merupakan bagian dari proyek nasional pengembangan robot pemanen anggur otonom.

Mekanisme yang dirangkum berpusat pada segmentasi citra untuk memisahkan tanaman atau buah dari latar dan tanaman. Ciri yang dipakai meliputi warna, tekstur, bentuk, dan ukuran; sejumlah metode memakai ambang Otsu pada ruang warna HSV atau YCbCr, pencocokan warna, atau pendekatan berbasis superpiksel. Teknik pembelajaran mencakup jaringan saraf tiruan yang dioptimasi dengan algoritma genetika, pemetaan saliensi dengan pencocokan kurva Gauss, kombinasi SLIC, CNN, PCA, dan SVM, pengklasifikasi ANN-HS, MLP, CLAHE, transformasi Hough, model Chan-Vese, operator Sobel, serta pembelajaran mendalam. Kamera yang dibahas mencakup citra tampak dan inframerah. Sistem kemudi memakai peta barisan tanaman, Hough transform, GPS diferensial, dan fusi data odometri; robot panen memadukan segmentasi, pelacakan buah, penentuan posisi tiga dimensi, dan beberapa lengan pemetik.

Tabel 1 dan pembahasan memuat sejumlah angka kinerja. Deteksi apel hijau dengan pemetaan saliensi dan pencocokan kurva Gauss mencapai akurasi 91,84%. Deteksi bunga apel dengan SLIC dan CNN menghasilkan skor-F 93,40% pada himpunan Apple A serta 80,20%, 82,20%, dan 79,90% pada himpunan Apple B, Apple C, dan peach. Identifikasi anggur dengan ANN dan algoritma genetika mencatat akurasi 99,40%; segmentasi daun mangga dengan Otsu mencatat presisi 99,50%, *recall* 97,10%, dan skor-F 98,30%; segmentasi enam jenis tanaman dengan ANN-HS mencatat akurasi 99,69%; dan klasifikasi biji gandum dengan Otsu serta MLP mencatat akurasi 99,92%. Deteksi kekurangan hara pada daun kopi hanya mencapai skor-F 64,9%. Pada sistem robot, penyemprotan di dalam ruangan mencapai akurasi sub-sentimeter, robot kiwi memiliki empat lengan yang masing-masing diprogram memetik satu buah per detik, dan navigasi dengan RTK-DGPS mencapai presisi centimeter; kinerja robot di lapangan umumnya lebih rendah daripada di dalam ruangan. Angka-angka ini dihitung pada himpunan uji masing-masing studi dengan indikator yang tercantum di tabel tinjauan.

Penulis membahas sejumlah keterbatasan. Segmentasi terganggu oleh perubahan pencahayaan, buah yang saling bertumpang tindih, buah yang tersembunyi di balik daun dan cabang, serta kemiripan warna antara target dan latar. Banyak metode bergantung pada ambang yang harus ditentukan ulang untuk setiap citra, sehingga kinerjanya tidak stabil ketika kondisi berubah. Algoritma seperti Panicle-SEG dan segmentasi daun kapas berjalan lebih cepat tetapi masih belum sesuai untuk aplikasi waktu nyata. Pengujian lapangan menunjukkan penurunan kinerja akibat permukaan tanah yang tidak rata, kesalahan ukur buatan manusia, selip roda pada tanah lunak dan lembap, gulma, serta angin. Penulis menyatakan bahwa lingkungan pertanian bersifat semi-terstruktur sekaligus tidak stabil: unsur tetap seperti barisan tanaman dapat dioptimalkan, tetapi tugas reaktif seperti menghadapi gulma, daun, cuaca buruk, dan pencahayaan harus dijalankan secara waktu nyata. Pengembangan arsitektur robot yang mampu mengoordinasikan perilaku reaktif masih diperlukan, dan metode pembelajaran mendalam memerlukan data serta daya komputasi dalam jumlah besar.

