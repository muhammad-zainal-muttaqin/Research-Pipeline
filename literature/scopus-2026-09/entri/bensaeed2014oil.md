# Oil palm fruit grading using a hyperspectral device and machine learning algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bensaeed2014oil` |
| Judul asli | Oil palm fruit grading using a hyperspectral device and machine learning algorithm |
| Penulis | Bensaeed, O M; Shariff, A M; Mahmud, A B; Shafri, H; Alfatni, M |
| Tahun | 2014 |
| Venue | Iop Conference Series Earth and Environmental Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [bensaeed2014oil.pdf](../pdf/bensaeed2014oil.pdf)
- DOI resmi: https://doi.org/10.1088/1755-1315/20/1/012017

## Gambaran Umum

Penelitian ini mengatasi masalah gradasi tandan buah segar (TBS) kelapa sawit berdasarkan tingkat kematangan sebelum buah diolah. Di industri sawit Malaysia, kematangan menentukan mutu dan daya jual minyak. Cara konvensional mengandalkan pengalaman pekerja, yaitu memotong buah untuk melihat warna mesokarp dan menghitung buah yang lepas dari tandan. Cara ini memakan waktu, padat karya, dan rawan penilaian bias serta kesalahan manusia. Penulis menyatakan sebagian besar kajian sebelumnya dilakukan di laboratorium dan masih terbatas pada pemindai hiperspektral dalam ruangan. Tujuan penelitian ini adalah membangun sistem otomatis gradasi TBS memakai teknik pemindai hiperspektral, mencari panjang gelombang yang membedakan tiga kelas kematangan, serta menguji dan memvalidasi prototipe pada kumpulan buah yang dikumpulkan dari lapangan.

Data berupa 469 buah dari tiga tipe, yaitu nigrescens, virescens, dan oleifera, yang diambil segar dari lahan Malaysian Palm Oil Board (MPOB) di Kluang, Johor, Malaysia. Pakar manusia mengelompokkan setiap buah ke dalam tiga kelas: belum matang (*underripe*), matang (*ripe*), dan terlalu matang (*overripe*). Rinciannya adalah virescens 151 sampel (36 belum matang, 41 matang, 74 terlalu matang), nigrescens 159 sampel (46, 47, 66), dan oleifera 159 sampel (52, 44, 63). Standar MPOB mengaitkan gradasi dengan persentase buah lepas, dari tandan tanpa buah lepas sampai lebih dari 90% buah lepas serta tandan busuk. Perekaman memakai kamera hiperspektral Imperx IPX-2 M 30 beresolusi 1600 × 1200 piksel, kedalaman 12 bit per piksel, dan 824 pita spektral pada rentang 400–1000 nm. Waktu eksposur ditetapkan 15 ms dan kamera ditempatkan 1,1 m di atas objek. Kalibrasi spektral dan spasial menghasilkan distorsi dalam satu piksel sehingga tidak diperlukan koreksi. Reflektan dinormalisasi terhadap ubin putih dan gelap dengan faktor skala 10.000. Citra diproses di ENVI 4.7; sekitar 35.000 piksel per citra dipilih sebagai daerah minat dan difilter dengan *low-pass* 11 × 11. Data dibagi secara acak menjadi data latih dan data uji dengan rasio 75:25, lalu dianalisis di Matlab.

Mekanisme deteksi memanfaatkan perubahan pigmen selama pematangan. Kandungan klorofil menurun dan karoten meningkat, sehingga cekungan penyerapan klorofil di sekitar 675 nm hilang ketika buah matang. Nigrescens memperlihatkan tiga pita serapan luas di sekitar 460, 675, dan 970 nm, sedangkan virescens dan oleifera di sekitar 520, 670, dan 970 nm. Pita 750–910 nm membedakan ketiga kelas kematangan. Penulis juga memakai pohon klasifikasi dengan metode pertumbuhan CHAID untuk memilih pita, lalu mengklasifikasikan melalui jaringan saraf tiruan *multilayer feed-forward* (ANN-MLP) tiga lapis dengan fungsi transfer log-sigmoid. Arsitektur yang dipakai adalah [50 30 1] untuk nigrescens, [60 20 1] untuk virescens, dan [35 15 1] untuk oleifera. Kelas diberi label −1 untuk belum matang, 0 untuk matang, dan 1 untuk terlalu matang. Pelatihan menggunakan kesalahan kuadrat jumlah maksimum 10e-4 selama 10e6 epoch. Kinerja dinilai dengan akurasi klasifikasi terhadap penilaian pakar, nilai *mean square error* (MSE) dan efisiensi, serta kurva *receiver operating characteristic* dan luas di bawah kurva (AUC) yang mencakup sensitivitas, spesifisitas, serta hasil positif dan negatif palsu.

Hasil seleksi pita menunjukkan pita 710–940 nm memberi akurasi pengujian terbaik. Panjang gelombang 830 nm paling baik untuk nigrescens dan virescens, sedangkan 880 nm paling baik untuk oleifera. Dengan metode CHAID, akurasi 83,3% diperoleh pada rentang 770–870 nm untuk virescens dan 830–890 nm untuk nigrescens; tumpang tindih keduanya ada di 830 nm. Pada model ANN-MLP, MSE pelatihan berturut-turut untuk nigrescens, virescens, dan oleifera adalah 9,7276 × 10⁻⁴, 1,09 × 10⁻⁶, dan 9,7476 × 10⁻⁵ dengan efisiensi 0,9999. Pada data uji, MSE berturut-turut 0,00184, 0,00156, dan 0,00173 dengan efisiensi 0,8574, 0,7812, dan 0,8245. Nilai AUC adalah 94,54 untuk nigrescens, 98,67 untuk virescens, 97,89 untuk oleifera, dan 95,73 untuk gabungan seluruh data. Bagian simpulan menyebut angka akurasi 94,54%, 98,67%, dan 97,89% per tipe serta 98,67% untuk gabungan seluruh data, sehingga angka gabungan di bagian itu tidak sama dengan nilai AUC yang dilaporkan di bagian hasil. Abstrak menyatakan akurasi lebih dari 95% untuk ketiga tipe buah.

Penulis menyatakan masih ada keterbatasan pada penggunaan pemindai hiperspektral dalam ruangan untuk membedakan kematangan, sehingga prototipe yang dibangun memakai perangkat keras yang digunakan di dalam ruangan. Penulis juga mencatat tipe oleifera lebih sulit dibedakan, terutama antara buah belum matang dan matang, sehingga karakternya tidak sama dengan nigrescens dan virescens. Selain itu, setiap pilihan teknologi membawa pertimbangan teknis, ekonomi, dan risiko tersendiri. Penulis mengusulkan riset lanjutan di bidang hiperspektral dan menyatakan prototipe ini dapat membantu perusahaan sawit memilih sistem pemeriksaan yang sesuai dengan kebutuhannya.

