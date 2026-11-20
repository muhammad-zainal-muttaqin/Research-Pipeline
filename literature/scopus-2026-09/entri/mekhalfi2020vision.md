# Vision system for automatic on-tree kiwifruit counting and yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mekhalfi2020vision` |
| Judul asli | Vision system for automatic on-tree kiwifruit counting and yield estimation |
| Penulis | Mekhalfi, Mohamed Lamine; Nicol\`o, Carlo; Ianniello, Ivan; Calamita, Federico; Goller, Rino; Barazzuol, Maurizio; Melgani, Farid |
| Tahun | 2020 |
| Venue | Sensors Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [mekhalfi2020vision.pdf](../pdf/mekhalfi2020vision.pdf)
- DOI resmi: https://doi.org/10.3390/s20154214

## Gambaran Umum

Penelitian ini mengembangkan sistem visi komputer otomatis dan noninvasif untuk menghitung buah kiwi di pohon dan mengestimasi hasil panen seluruh kebun. Penulis menyatakan estimasi hasil sebelum panen diperlukan untuk merencanakan transportasi, tenaga kerja, dan pemasaran, serta menyatakan bahwa literatur belum menyediakan sistem otomatis untuk kiwi pada skala kebun. Sistem ini mengakuisisi citra dengan sensor optik pada minitractor, lalu menjalankan perakitan citra, praproses, dan penghitungan buah untuk menghasilkan jumlah buah dan estimasi hasil.

Uji coba dilakukan di dua kebun kiwi komersial milik Consorzio Frutteto di Cesena, Italia, dengan luar masing-masing sekitar 200 m × 50 m dan 150 m × 65 m serta jarak tanam 2 m. Prototipe dipasang pada batang horizontal di belakang minitractor melalui three-point hitch, terdiri atas modul GPS Arduino untuk mencatat lokasi setiap 5 s, lampu LED 48 W dengan fluks 3.800 lm, gimbal Feiyu G6 Plus untuk menstabilkan kamera, dan kamera Sony Alpha 5100 beresolusi 24 MP. Tractor bergerak sekitar 2 km/jam dengan kamera menghadap ke atas ke kanopi pada jarak sekitar 60 cm dan laju tiga foto per detik. Untuk penilaian penghitungan, penulis memilih 50 citra; estimasi hasil dihitung dari seluruh citra kedua kebun.

Alur penghitungan dimulai dengan perakitan citra memakai fitur SURF yang dijelaskan dengan vektor 64-bin, pencocokan jarak Euclidean, estimasi matriks homografi dengan RANSAC, dan warping, sehingga menghasilkan satu citra tanpa pengulangan. Praproses mengubah citra RGB ke LAB, menerapkan binarisasi Otsu pada kanal A, penyaringan median 25 × 25 piksel, dan dilatasi morfologi untuk menekan daun latar sebelum mask diterapkan pada citra asli. Deteksi tidak mencari seluruh buah yang beragam ukuran, orientasi, dan oklusinya, melainkan ujung buah kiwi berupa bintik gelap di bagian bawah yang umum terlihat ketika kamera menghadap ke atas. Detektor memakai algoritme Viola–Jones dengan fitur Haar, citra integral, pelatihan AdaBoost, dan kaskade classifier. Estimasi berat diperoleh dengan mengalikan jumlah buah dan berat rata-rata 97,95 g, yang diukur dari 20 buah dengan ukuran beragam yang diambil dari beberapa lokasi.

Metrik evaluasi adalah galat persentase rata-rata (APE) sebesar 100/N × |EC − AC|/AC, dengan EC sebagai jumlah estimasi dan AC sebagai jumlah aktual. Dengan praproses, APE terbaik 12,35% dicapai pada enam kaskade; tanpa praproses, APE terbaik 13,02% dicapai pada delapan kaskade. Rata-rata APE lintas jumlah kaskade adalah 23,62% dengan praproses berbanding 38% tanpa praproses. Tingkat penolakan 20% memberi APE 12,36%, lebih rendah daripada 20,16% pada 10%, 24,23% pada 30%, 38,12% pada 40%, dan 41,48% pada 50%. Terhadap hasil panen aktual yang ditimbang setelah panen, sistem memberikan estimasi berlebih sebesar 15% pada kebun pertama dan 6% pada kebun kedua. Waktu pemrosesan adalah sekitar 1,6 s per citra berukuran 2000 × 3000 piksel pada prosesor AMD Ryzen 3007.

Penulis menyatakan sistem ini telah digunakan secara komersial selama sekitar dua tahun dan menghemat waktu dibandingkan estimasi manual. Keterbatasan yang dinyatakan adalah akuisisi citra pada kebun sangat besar memakan waktu dan penghitungan dilakukan di komputer di luar lokasi, bukan secara langsung di lapangan. Penulis juga menyatakan galat pada perakitan citra dan praproses dapat bertambah dan berdampak pada jumlah buah. Pendekatan ini dikatakan dapat diperluas ke tanaman lain apabila ada ciri yang unik dan konsisten pada sekumpulan buah yang besar, seperti tekstur ujung buah kiwi.
