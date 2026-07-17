# 028 - A Review of YOLO Algorithm Developments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jiang2022yoloreview` |
| Judul asli | A Review of Yolo Algorithm Developments |
| Penulis | Peiyuan Jiang, Daji Ergu, Fangyao Liu, Ying Cai, Bo Ma |
| Tahun | 2022 |
| Venue | Procedia Computer Science, vol. 199, hlm. 1066–1073 (prosiding ITQM 2021, *International Conference on Information Technology and Quantitative Management*) |
| Tema | Survei YOLO |

## Tautan Akses
- **DOI (akses terbuka):** https://doi.org/10.1016/j.procs.2022.01.135
- **Semantic Scholar:** https://www.semanticscholar.org/paper/0c5c842529ec2f1ad6213f1827456ae77761d523
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Review%20of%20YOLO%20Algorithm%20Developments

## Gambaran Umum

Makalah ini adalah survei naratif singkat (delapan halaman) yang mengikhtisarkan algoritma YOLO (*You Only Look Once*) dan versi-versi lanjutannya sampai tahun 2021. YOLO adalah detektor objek satu tahap: lokasi dan kelas objek pada citra diprediksi dalam satu lintasan jaringan saraf, bukan melalui dua tahap terpisah. Masalah yang dipecahkan makalah ini bersifat kebahasaan-literatur: rangkaian versi YOLO berkembang cepat dan makalah primernya tersebar, sehingga pembaca baru sulit memetakan apa yang berubah dari satu versi ke versi berikutnya. Hasil utama makalah adalah analisis persamaan dan perbedaan antarversi YOLO, perbandingan antara YOLO dan detektor berbasis jaringan saraf konvolusi (CNN) pada umumnya, serta kesimpulan bahwa penyempurnaan YOLO masih berlangsung. Makalah ini juga membingkai YOLO sebagai penunjang ekstraksi fitur pada berita bergambar di bidang keuangan dan bidang lain.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek adalah tugas menemukan posisi objek pada citra sekaligus menentukan kelasnya, dan menjadi dasar bagi banyak aplikasi visi komputer. Antara 2016 dan 2021, rangkaian versi YOLO bertambah dengan cepat: YOLOv1 (2016) memperkenalkan deteksi satu tahap berbasis grid, YOLO9000/YOLOv2 (2017) menambahkan kotak jangkar dan *batch normalization*, YOLOv3 (2018) memperkenalkan prediksi multi-skala, dan YOLOv4 (2020) merangkai sejumlah teknik pelatihan dan arsitektur menjadi detektor yang lebih akurat. Perkembangan ini diuraikan dalam bab-bab fondasi tinjauan ini, misalnya [bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md) untuk YOLOv1 dan [bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md) untuk YOLOv4.

Kondisi tersebut menimbulkan tiga kesulitan praktis. Pertama, makalah primer tiap versi tersebar di venue berbeda dan masing-masing mengubah beberapa komponen sekaligus, sehingga sulit diperoleh gambaran utuh tanpa membaca semuanya. Kedua, survei deteksi objek yang sudah ada, misalnya tinjauan model deteksi berbasis CNN, menempatkan YOLO hanya sebagai satu metode di antara banyak metode, bukan sebagai rangkaian yang dievolusikan. Ketiga, komunitas di luar visi komputer inti, termasuk bidang teknologi informasi dan manajemen kuantitatif yang menjadi wadah publikasi makalah ini, membutuhkan ringkasan yang padat untuk menilai kelayakan YOLO bagi aplikasinya. Makalah Jiang dkk. mengisi celah tersebut dengan sebuah tinjauan khusus terhadap perkembangan YOLO.

## Ide Utama

Gagasan inti makalah ini sederhana: seluruh perkembangan YOLO dapat dipahami sebagai satu garis perubahan yang konsisten, dan garis itu dapat disajikan dalam satu dokumen perbandingan. Masukannya adalah literatur YOLO yang sudah terbit; keluarannya adalah sintesis yang menjawab tiga pertanyaan — apa yang dipertahankan semua versi, apa yang diubah tiap versi, dan bagaimana posisi YOLO terhadap pendekatan deteksi berbasis CNN lainnya. Makalah tidak mengusulkan metode baru dan tidak menjalankan eksperimen baru; kontribusinya adalah pemadatan dan pembandingan literatur. Kesimpulan sentral yang ditarik penulis adalah bahwa penyempurnaan YOLO bersifat berkelanjutan, bukan rangkaian yang sudah selesai.

## Cara Kerja Langkah demi Langkah

### Titik Tolak: Prinsip Dasar YOLO

Survei dimulai dari prinsip kerja YOLO yang menjadi dasar semua versi. Citra masukan dibagi menjadi grid berukuran S×S sel. Setiap sel bertanggung jawab memprediksi objek yang titik pusatnya jatuh di dalam sel tersebut. Setiap sel menghasilkan sejumlah prediksi *bounding box*, yaitu kotak pembatas berparameter (x, y, w, h) yang menyatakan pusat, lebar, dan tinggi objek, beserta skor *confidence* yang menyatakan seberapa yakin model bahwa kotak itu berisi objek. Selain itu setiap sel memprediksi probabilitas kelas objek. Sebagai contoh numerik, pada citra 448×448 piksel dengan grid 7×7, setiap sel mencakup wilayah 64×64 piksel, dan seluruh prediksi dari 49 sel dihitung dalam satu lintasan maju jaringan konvolusi. Karena satu objek dapat diprediksi oleh beberapa sel, dihasilkan kotak-kotak yang tumpang tindih; tahap *non-maximum suppression* (NMS) kemudian membuang kotak duplikat yang memiliki *intersection over union* (IoU) tinggi terhadap kotak berskor lebih besar, di mana IoU adalah rasio luas irisan terhadap luas gabungan dua kotak. Alur lengkapnya dapat digambarkan sebagai berikut.

```
citra masukan (mis. 448 x 448 piksel)
        |
        v
+------------------------------------------+
| jaringan konvolusi (backbone):           |
| ekstraksi fitur seluruh citra            |
| dalam satu lintasan                      |
+------------------------------------------+
        |
        v
peta fitur dibagi grid S x S sel
(grid 7 x 7 -> tiap sel 64 x 64 piksel)
        |
        v
tiap sel memprediksi:
- sejumlah bounding box (x, y, w, h)
  beserta skor confidence
- probabilitas kelas objek
        |
        v
non-maximum suppression (NMS):
kotak duplikat ber-IoU tinggi dibuang
        |
        v
hasil: kotak akhir + label kelas + skor
```

Diagram di atas memperlihatkan ciri yang membedakan YOLO: seluruh tahap, dari ekstraksi fitur hingga prediksi kotak, terjadi dalam satu jaringan, sehingga kecepatan inferensinya tinggi.

### Dimensi Perbandingan Antarversi

Bagian inti survei membandingkan versi-versi YOLO pada beberapa dimensi yang berulang. Dimensi pertama adalah *backbone*, yaitu jaringan konvolusi ekstraksi fitur yang membentuk peta fitur dari citra; tiap versi mengganti atau memperkuat backbone-nya. Dimensi kedua adalah kotak jangkar (*anchor box*), yaitu sekumpulan bentuk kotak acuan yang dipakai model sebagai titik awal regresi ukuran objek; mekanisme ini diperkenalkan pada YOLOv2 dan dipertahankan versi-versi sesudahnya. Dimensi ketiga adalah prediksi multi-skala, yaitu pembacaan peta fitur pada beberapa resolusi sekaligus agar objek kecil dan besar terdeteksi; mekanisme ini menjadi ciri YOLOv3. Dimensi keempat adalah komposisi teknik pelatihan dan arsitektur tambahan yang dirangkai pada YOLOv4. Perbandingan pada dimensi-dimensi ini menghasilkan temuan bahwa tiap versi mempertahankan kerangka dasar grid satu tahap, sementara akurasi dinaikkan bertahap melalui perubahan komponen, dengan konsekuensi pergeseran imbangan antara kecepatan dan akurasi.

### Perbandingan YOLO dengan Detektor CNN Dua Tahap

Survei juga membandingkan YOLO dengan keluarga detektor CNN dua tahap seperti R-CNN. Detektor dua tahap bekerja dengan mengusulkan sejumlah kandidat wilayah objek (*region proposal*) pada tahap pertama, lalu mengklasifikasikan tiap wilayah pada tahap kedua. Struktur ini umumnya lebih akurat tetapi lebih lambat karena komputasi diulang untuk setiap kandidat wilayah. YOLO menghapus tahap usulan wilayah dan memprediksi langsung dari grid, sehingga unggul pada kecepatan dan cocok untuk pemrosesan waktu nyata, dengan kelemahan yang dicatat literatur berupa kesulitan pada objek kecil dan objek yang berdekatan, karena satu sel hanya memprediksi sedikit kotak.

### Pengenalan Target, Pemilihan Fitur, dan Aplikasi

Bagian lanjutan survei merangkum metode pengenalan target dan pemilihan fitur (*feature selection*), yaitu cara memilih ciri citra yang paling informatif untuk membedakan objek. Penulis membingkai rangkuman ini sebagai dukungan literatur bagi aplikasi pemrosesan berita bergambar di bidang keuangan dan bidang lain, sesuai konteks konferensi tempat makalah diterbitkan. Contoh aplikasi yang tercermin dalam daftar rujukannya meliputi deteksi kepala gandum, deteksi pelat nomor kendaraan, deteksi buah apel di kebun, deteksi kendaraan pada citra udara, dan penggabungan data LiDAR dengan kamera.

### Prosedur Survei

Secara metodologis makalah ini adalah survei naratif, bukan tinjauan sistematis: tidak dilaporkan protokol pencarian basis data, kriteria inklusi, atau jumlah artikel yang disaring. Daftar rujukannya hanya memuat delapan dokumen, dan seluruhnya adalah literatur sekunder — survei deteksi objek lain dan makalah terapan YOLO — tanpa satu pun makalah primer YOLO. Angka kinerja yang dibahas di dalamnya merupakan kompilasi dari publikasi lain, bukan hasil pengukuran ulang pada pengaturan yang seragam.

## Eksperimen dan Hasil

Makalah ini tidak memuat eksperimen baru; hasilnya berupa temuan analitis. Pertama, seluruh versi YOLO berbagi kerangka yang sama — grid, prediksi kotak per sel, dan satu lintasan jaringan — sehingga persamaannya lebih mendasar daripada perbedaannya. Kedua, perbedaan antarversi terletak pada komponen yang diganti bertahap: backbone, kotak jangkar, prediksi multi-skala, dan teknik pelatihan, yang secara kumulatif menaikkan akurasi sambil mempertahankan kecepatan tinggi. Interpretasinya, evolusi YOLO bersifat inkremental dan berorientasi imbangan kecepatan-akurasi, bukan pergantian paradigma. Ketiga, dibandingkan detektor CNN dua tahap, YOLO menang pada kecepatan dan kalah pada sebagian aspek akurasi, terutama objek kecil; ini menegaskan posisi YOLO sebagai pilihan untuk aplikasi waktu nyata. Keempat, penulis menyimpulkan penyempurnaan YOLO masih berlangsung, yang terbukti konsisten dengan munculnya versi-versi baru setelah makalah ini terbit.

Satu bukti eksternal tentang dampak makalah: per Juli 2026, OpenAlex mencatat 2.639 sitasi dan Semantic Scholar mencatat 2.458 sitasi untuk makalah ini. Angka sebesar itu untuk survei delapan halaman menunjukkan makalah ini dipakai luas sebagai rujukan pengantar YOLO, walaupun jumlah sitasi bukan ukuran kedalaman teknis.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini adalah kepadatannya: dalam delapan halaman, pembaca memperoleh peta rangkaian versi YOLO, perbandingan dengan pendekatan CNN lain, dan penunjukan aplikasi. Status akses terbukanya memudahkan penyebaran, dan fokusnya pada satu rangkaian versi membuatnya lebih mudah dibaca daripada survei deteksi objek umum.

Keterbatasannya juga jelas. Dari sisi metodologi survei, delapan rujukan yang seluruhnya literatur sekunder adalah basis yang sangat sempit; temuannya dengan demikian merupakan ringkasan tingkat tinggi yang tidak diverifikasi terhadap makalah primer, dan tidak ada angka kinerja yang diukur ulang pada pengaturan seragam. Dari sisi cakupan, pembahasan berhenti pada versi yang tersedia sampai 2021, sehingga versi-versi sesudahnya tidak tercakup dan sebagian isinya cepat tertinggal. Secara konseptual, karena tidak ada protokol tinjauan sistematis, pemilihan bahan bergantung pada penulis dan rawan bias pemilihan. Keterbatasan-keterbatasan ini merupakan analisis penulis bab, bukan pernyataan penulis makalah.

## Kaitan dengan Bab Lain

Bab ini bergantung pada bab-bab fondasi yang menguraikan tiap versi YOLO secara rinci: [bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), [bab 002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md), [bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md), dan [bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md). Keempatnya menyediakan detail teknis yang oleh survei ini hanya diringkas.

Dalam klaster Survei YOLO, bab ini adalah entri paling awal dan paling ringkas; pembaca yang membutuhkan cakupan lebih baru atau lebih dalam dapat melanjutkan ke [bab 026](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md) yang meninjau versi lebih lengkap, [bab 027](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md) untuk aplikasi manufaktur, [bab 029](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md) untuk aplikasi pertanian, serta [bab 032](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md) yang mengevaluasi evolusi YOLO secara eksperimental — melengkapi sifat naratif survei Jiang dkk.

## Poin untuk Sitasi

- **Kunci BibTeX:** `jiang2022yoloreview`
- **Ringkasan yang aman dikutip:** Jiang dkk. (2022) menyajikan tinjauan naratif atas perkembangan algoritma YOLO dan versi-versi lanjutannya, membandingkan persamaan dan perbedaan antarversi serta posisi YOLO terhadap detektor berbasis CNN, dan menyimpulkan bahwa penyempurnaan YOLO masih berlangsung. Makalah diterbitkan di Procedia Computer Science vol. 199 (prosiding ITQM 2021), hlm. 1066–1073, dengan status akses terbuka.
- **Catatan verifikasi:** teks lengkap di ScienceDirect tidak dapat diakses saat penulisan bab ini (dibatasi anti-bot); narasi disusun dari abstrak terverifikasi (OpenAlex), metadata (DOI, volume, halaman), dan daftar rujukan (Semantic Scholar). Sebelum sitasi formal, verifikasi ke naskah asli: (1) cakupan versi yang dibahas persisnya, khususnya apakah YOLOv5 ikut ditinjau; (2) ada tidaknya tabel atau angka perbandingan kuantitatif spesifik; (3) butir keterbatasan di bab ini adalah analisis penulis bab, bukan pernyataan makalah. Jumlah sitasi bersifat dinamis dan dicatat per Juli 2026.
