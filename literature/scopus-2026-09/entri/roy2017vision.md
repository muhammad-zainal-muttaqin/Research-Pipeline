# Vision-Based Apple Counting and Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `roy2017vision` |
| Judul asli | Vision-Based Apple Counting and Yield Estimation |
| Penulis | Roy, Pravakar; Isler, Volkan |
| Tahun | 2017 |
| Venue | Springer Proceedings in Advanced Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [roy2017vision.pdf](../pdf/roy2017vision.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-50115-4_42

## Gambaran Umum
Makalah ini (prosiding *International Symposium on Experimental Robotics* 2016, terbit 2017) mengusulkan metode pencacahan apel pada kebun apel dari citra yang telah tersegmentasi dan teregistrasi. Masukan metode adalah citra gugus apel (*apple cluster*) tempat piksel bukan apel telah dihilangkan; keluarannya adalah jumlah dan lokasi apel individual pada tiap gugus. Kontribusi teknis utama adalah representasi gugus sebagai campuran Gaussian (*Gaussian Mixture Model*, GMM) dan kriteria baru untuk memilih jumlah komponen campuran berbasis prinsip *minimum description length* (MDL) yang diberi imbalan (*reward*) dan penalti.

Metode diuji pada empat dataset dari kamera genggam, kendaraan darat, dan pesawat nirawak (UAV). Akurasi algoritme pencacahan sendiri adalah 91,30% pada 442 citra gugus dari Dataset 3. Pada alur lengkap (segmentasi, registrasi, lalu pencacahan), akurasi 81,3492%, 85,87%, dan 84,72% dilaporkan untuk Dataset 1, 2, dan 4. Metode pembanding berupa pencocokan lingkaran serakah (*greedy circle fitting*) memperoleh 69,44% dan 76,34% pada Dataset 1 dan 2.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Keputusan pada kebun buah khusus, seperti jumlah pemetik, jumlah tempat penyimpanan, dan kontrak penjualan awal musim, bergantung pada estimasi jumlah buah. Penulis menyebut tiga kesulitan menghitung apel dari urutan citra berjalan: kompromi antara cakupan citra dan ukuran apel (pandang dekat memakan waktu, sudut lebar membuat apel kecil); apel muncul dalam gugus berbentuk acak dengan hampir semua apel saling tumpang tindih sehingga segmentasi individu sulit; dan oklusi daun dan ranting serta pantulan spekular membuat sebagian apel tidak dapat terdeteksi.

Penulis menyatakan bahwa kebanyakan sistem estimasi hasil robotik tidak berfokus pada pencacahan akurat, tetapi pada penaksir yang konsisten terhadap jumlah sebenarnya. Metode terdahulu yang dikutip: Wang dkk. (operasi morfologi dan pencocokan elips, tidak menangani lebih dari dua apel per gugus), Hung dkk. (transformasi Hough lingkaran), dan Linker dkk. (deteksi tepi buah, memerlukan citra resolusi sangat tinggi). Metode ini berhasil untuk apel tunggal tetapi dinilai gagal pada gugus kompleks.

## Ide Utama
Setiap apel dimodelkan sebagai satu distribusi Gaussian dua dimensi pada piksel biner gugus, dan gugus dimodelkan sebagai campuran Gaussian dengan $k$ komponen. Pusat komponen $\mu_i$ menjadi pusat apel, dengan jari-jari ekuatorial dan aksial $2\sigma_{x_i}$ dan $2\sigma_{y_i}$. Parameter diestimasi dengan algoritme *expectation maximization* (EM) yang diinisialisasi dengan K-means (implementasi MATLAB). Persoalan utamanya adalah memilih $k$ yang benar, yaitu jumlah apel $\kappa$.

Kriteria klasik seperti AIC dan MDL standar disebut tidak bekerja langsung, karena cenderung memilih $k$ lebih besar (contoh sintetis: lima lingkaran, tetapi kriteria AIC terendah pada $k=6$ dan menghasilkan delapan apel). Penulis mengusulkan skor heuristik: $\kappa = \arg\max_k R(G_k) - V(G_k)$. Imbalan $R_i$ terdiri atas empat suku: respons kernel Gaussian di pusat, kebulatan ($1-\epsilon^2 = (\sigma_{min}/\sigma_{max})^2$), cakupan piksel, dan penalti untuk Gaussian yang menutupi area luas dengan sedikit piksel. Penalti $V$ mengikuti MDL dengan konstanta $c' = 3/2$ (bukan $1/2$) karena imbalan memiliki tiga suku, dan faktor $3k$ karena tiap Gaussian memiliki tiga parameter.

## Cara Kerja Langkah demi Langkah
### 1. Prasyarat: segmentasi dan registrasi
Metode tidak mencakup segmentasi apel dan registrasi gugus antar-citra; kedua tahap itu dirujuk pada karya terdahulu penulis (segmentasi berbasis warna dan registrasi gugus apel antar citra). Registrasi memastikan gugus yang sama pada citra berbeda diselaraskan sehingga hitungan tidak ganda, tetapi mekanismenya tidak dijelaskan pada makalah ini.

### 2. Analisis komponen terhubung
Pada citra masukan dilakukan analisis komponen terhubung untuk memisahkan gugus yang disjoin. Jumlah apel total adalah penjumlahan hitungan per gugus.

### 3. Metode GMM
Citra gugus diubah ke biner, lokasi piksel bukan nol menjadi masukan GMM, dan EM dijalankan untuk berbagai $k$. Skor imbalan dikurangi penalti dihitung untuk setiap $k$ dan nilai maksimum dipilih. Pada contoh sintetis enam lingkaran acak, skor maksimum diperoleh pada $k=6$.

### 4. Metode pembanding serakah
Kernel Gaussian dengan berbagai ukuran pada rentang jari-jari yang diketahui dikonvolusikan pada citra untuk mencari pusat apel dengan respons maksimum. Apel berikutnya dipilih dengan memaksimalkan respons gabungan bersama apel yang sudah dipilih, dan urutan pemilihan mendefinisikan hierarki oklusi. Metode ini dipakai sebagai baseline yang setara dengan teknik Hough dan pencocokan elips.

## Eksperimen dan Hasil
Empat dataset dipakai: dua dari kamera genggam (Dataset 1 dan 2), satu dari kamera pada kendaraan darat (Dataset 3), dan satu dari UAV (Dataset 4). Dataset 3 (442 citra gugus, semuanya dihitung manual) dipakai untuk menguji algoritme pencacahan sendiri, dan hasil alur lengkap untuk Dataset 3 tidak tersedia saat pengiriman naskah. Dataset 1 berisi apel merah dan hijau pada satu blok enam pohon (464 citra), Dataset 2 terutama apel merah pada satu baris penuh (964 citra), dan Dataset 4 dari UAV mencakup enam pohon (655 citra). Jumlah apel hasil hitung manual pada ketiga dataset itu adalah 258, 952, dan 673, secara berurutan (teks menyebut "258 and 952, and 673" untuk Dataset 1, 2, dan 4).

| Dataset | Jumlah citra | Hitungan manual | Akurasi GMM (%) | Akurasi serakah (%) |
|---|---|---|---|---|
| 3 (hanya algoritme pencacahan, gugus tersegmentasi) | 442 | tidak dilaporkan | 91,30 | tidak dilaporkan |
| 1 (genggam, merah dan hijau) | 464 | 258 | 81,3492 | 69,44 |
| 2 (genggam, terutama merah) | 964 | 952 | 85,87 | 76,34 |
| 4 (UAV) | 655 | 673 | 84,72 | tidak dilaporkan |

Pada Dataset 3, untuk gugus berisi enam apel atau lebih, penghitungan kurang (*under counting*) mencapai 33,33%, tetapi jumlah gugus besar sangat sedikit sehingga penulis tidak menarik inferensi kuat. Untuk apel tunggal ditemukan penghitungan lebih sebesar 10%, yang dikaitkan dengan oklusi dan pantulan spekular. Penurunan akurasi Dataset 1 dikaitkan terutama dengan metode segmentasi yang tidak mendeteksi banyak apel hijau. Metode serakah turun karena memakai ambang keras untuk pengelompokan piksel dan gagal bila skala citra berubah banyak atau apel hanya tampak sebagian.

## Kelebihan dan Keterbatasan
Kelebihan: GMM dengan kriteria seleksi baru menangani gugus apel yang saling menumpuk dan menghasilkan lokasi serta jari-jari tiap apel; dievaluasi pada empat dataset dari tiga jenis platform; akurasi lebih tinggi daripada metode serakah yang setara dengan metode Hough dan pencocokan elips.

Keterbatasan yang dinyatakan penulis: hasil akhir bergantung pada tahap segmentasi dan registrasi sebelumnya (apel hijau yang tidak tersegmentasi tidak dihitung sama sekali); algoritme gagal bila tumpang tindih terlalu besar dan batas antar-buah tidak terdeteksi (EM gagal menemukan lokasi dan jari-jari yang benar walau $k$ benar); sulit memprediksi jumlah apel yang benar dari satu pandang pada kasus ini, sehingga penulis mengusulkan penglihatan aktif (*active vision*), yaitu mengamati gugus dari sudut lain dan menggabungkan informasinya pada pekerjaan mendatang.

Menurut pembacaan ringkasan ini, ada keterbatasan lain. Hasil pencacahan sendiri (91,30%) dan hasil alur lengkap dilaporkan pada dataset yang berbeda, sehingga keduanya tidak dapat dibandingkan langsung. Definisi akurasi, serta cara penghitungan manual, tidak dijelaskan pada teks yang tersedia. Hasil rinci per ukuran gugus hanya ada pada grafik (Gambar 6) yang tidak terbaca dari ekstraksi teks. Tidak ada perbandingan dengan detektor pembelajaran mendalam. Seleksi $k$ memakai konstanta dan bobot heuristik yang tidak divalidasi pada dataset selain yang dipakai penulis.

## Kaitan dengan Tinjauan main6
Makalah ini hanya menyentuh masalah buah yang terlihat lebih dari sekali secara tidak langsung. Penghitungan antar-citra bergantung pada tahap registrasi gugus apel antar-citra dari karya penulis sebelumnya, yang disebut tetapi tidak diuraikan di sini. Kontribusi inti makalah ini adalah pemisahan apel yang saling tumpang tindih di dalam satu gugus pada satu citra (pencacahan satu pandang, kode C2), bukan identitas lintas pandang. Penulis juga menyebut bahwa ambiguitas pada satu pandang paling baik diatasi dengan melihat gugus dari sudut lain dan menggabungkan informasi, tetapi hal itu dinyatakan sebagai pekerjaan masa depan dan belum dilakukan.

Hitungan dilaporkan sebagai total buah, tidak per kelas (apel merah dan hijau muncul pada Dataset 1, tetapi tidak dihitung terpisah). Acuan hitungan adalah hitung manual dari citra ("hand counted apples from the images"), bukan panen atau hitung lapangan. Hal yang dapat dipindahkan ke tandan sawit multisisi terbatas: gagasan memisahkan objek saling tumpang tindih lewat model campuran dengan kriteria seleksi komponen, serta pengamatan bahwa keputusan jumlah dari satu pandang tidak dapat dipastikan sehingga pandang tambahan diperlukan. Makalah tidak menyediakan mekanisme lintas pandang yang dapat langsung dipakai.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `roy2017vision`.

Roy dan Isler (2017) mengusulkan pencacahan apel dari citra gugus tersegmentasi dan teregistrasi dengan campuran Gaussian yang jumlah komponennya dipilih oleh kriteria berbasis MDL dengan imbalan dan penalti. Akurasi algoritme pencacahan adalah 91,30% pada 442 citra gugus, dan akurasi alur lengkap 81,35% sampai 85,87% pada tiga dataset kebun (kamera genggam dan UAV), dibanding 69,44% dan 76,34% untuk metode pencocokan lingkaran serakah pada dua dataset.

Catatan verifikasi data: 91,30% dan 442 citra pada Bagian 3 (paragraf pertama), 33,33% dan 10% pada paragraf yang sama; akurasi 81,3492%, 85,87%, 84,72% serta jumlah citra (464, 964, 655) dan hitungan manual (258, 952, 673) pada paragraf kedua Bagian 3; 69,44% dan 76,34% pada paragraf yang sama. Pemetaan hitungan manual pada Dataset 1, 2, dan 4 mengikuti urutan kalimat pada teks. Grafik pada Gambar 6 tidak terbaca dari ekstraksi teks, sehingga hasil per ukuran gugus tidak dilaporkan. Makalah tidak menjelaskan definisi akurasi, hitungan manual untuk Dataset 3, hasil alur lengkap untuk Dataset 3, dan rincian registrasi lintas-citra yang dirujuk pada karya terdahulu. Teks diawali halaman sampul ResearchGate, yang tidak mengubah isi makalah. Makalah ini berformat prosiding sehingga entri ini lebih pendek daripada artikel jurnal.
