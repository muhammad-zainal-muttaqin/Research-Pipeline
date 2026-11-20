# A survey of recent advances in CNN-based single image crowd counting and density estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sindagi2018survey` |
| Judul asli | A survey of recent advances in CNN-based single image crowd counting and density estimation |
| Penulis | Sindagi, Vishwanath A.; Patel, Vishal M. |
| Tahun | 2018 |
| Venue | Pattern Recognition Letters |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [sindagi2018survey.pdf](../pdf/sindagi2018survey.pdf)
- DOI resmi: https://doi.org/10.1016/j.patrec.2017.07.007

## Gambaran Umum

 tinjauan ini membahas penghitungan orang dan estimasi peta kepadatan pada citra tunggal, dengan fokus pada pendekatan berbasis convolutional neural network (CNN, jaringan saraf konvolusional). Masalah utamanya adalah mengubah citra kerumunan menjadi jumlah orang dan peta kepadatan, yang sulit karena occlusions (tertutupnya objek), kepadatan tidak seragam, serta variasi skala dan perspektif di dalam satu citra maupun antarcitra. Penulis menyatakan metode penghitungan kerumunan dapat dialihkan ke tugas lain, seperti mikroskopi sel, penghitungan kendaraan, dan survei lingkungan, sehingga relevan sebagai bukti yang dapat ditransfer ke penghitungan objek pertanian.

Bahan yang ditinjau terdiri atas pendekatan tradisional dan pendekatan CNN. Pendekatan tradisional dibagi menjadi deteksi (jendela geser dengan fitur buatan seperti Haar, HOG, edgelet, dan shapelet), regresi (pemetaan fitur citra lokal ke jumlah, misalnya LBP, HOG, GLCM dengan regresi linear, ridge, atau Gaussian process), dan estimasi kepadatan (pemetaan fitur ke peta kepadatan yang integralnya memberi jumlah pada suatu wilayah). Penulis mengkategorikan metode CNN berdasarkan sifat jaringan menjadi CNN dasar, model sadar-skala, model sadar-konteks, dan kerangka multi-tugas, serta berdasarkan cara inferensi menjadi inferensi berbasis patch dan inferensi berbasis citra utuh. Tinjauan ini memakai lima kumpulan data utama: UCSD (2.000 frame, 49.885 instance), Mall (2.000 frame, 62.325), UCF CC 50 (50 citra, 63.974), WorldExpo '10 (3.980 frame, 199.923), dan ShanghaiTech (1.198 citra, 330.165; terbagi Part A dan Part B).

Mekanisme deteksi dan asosiasi yang dijelaskan berpusat pada pembangkitan peta kepadatan. Lempitsky dkk. mempelajari pemetaan linear fitur patch ke peta kepadatan sebagai optimasi cembung; Pham dkk. memakai regresi random forest tidak linear; Zhang dkk. (MCNN) memakai tiga kolom dengan ukuran receptive field berbeda dan menentukan parameter sebaran kernel Gaussian dari jarak rata-rata kepala ke tetangganya, sehingga normalisasi perspektif tidak memerlukan peta perspektif. Varian lain mencakup Hydra-CNN dengan tiga kepala berskala berbeda, Switching CNN yang memilih regresor terbaik per patch, Mixture of CNNs dengan gerbang pemilih pakar, dan model citra utuh yang menggabungkan GoogLeNet dengan decoder long short-term memory (LSTM) untuk menghitung jumlah lokal lalu global. Zhang dkk. juga melakukan adaptasi lintas adegan dengan menyetel ulang jaringan memakai sampel yang mirip dengan adegan target tanpa label tambahan.

Angka hasil dilaporkan dari makalah aslinya dengan metrik mean absolute error (MAE) dan mean squared error (MSE), yang didefinisikan sebagai rata-rata selisih absolut dan akar rata-rata selisih kuadrat antara jumlah sebenarnya dan jumlah estimasi. Secara umum metode CNN mengungguli pendekatan tradisional pada kelima kumpulan data, dengan perbaikan terbesar pada model sadar-skala dan sadar-konteks. MCNN mencapai hasil terbaik pada UCSD, WorldExpo '10, dan ShanghaiTech (MAE 1,07 pada UCSD; 173,2 pada ShanghaiTech-A dan 41,3 pada ShanghaiTech-B), CNN-boosting Walach dan Wolf terbaik pada Mall, serta kombinasi jumlah lokal-global Shang dkk. dan Hydra-CNN terbaik pada UCF CC 50. Walach dan Wolf melaporkan penurunan galat 20–30 persen dibanding metode mutakhir saat itu; metode citra utuh lebih efisien dan lebih akurat daripada metode berbasis patch. Seluruh angka pada tabel perbandingan diambil langsung dari publikasi masing-masing, bukan dihitung ulang oleh penulis.

Batasan yang dinyatakan penulis mencakup cakupan yang tidak mencakup seluruh literatur penghitungan kerumunan, hanya himpunan perwakilan dari metode terbaru. Kumpulan data masih timpang: UCF CC 50 terlalu kecil untuk melatih jaringan dalam, sedangkan ShanghaiTech didominasi citra berkepadatan rendah. Transfer learning dan adaptasi domain untuk adegan baru masih jarang diteliti dan mahal karena memerlukan anotasi baru. Metode berbasis patch kehilangan konteks global, sedangkan model sadar-skala dibatasi oleh jumlah kolom dan ukuran receptive field yang dipilih berdasarkan data. Selain itu, regenerasi peta kepadatan dari peta yang di-downsample dengan loss Euclidean menghasilkan peta berkualitas rendah meskipun jumlahnya akurat, sehingga merugikan tugas lanjutan seperti deteksi dan pelacakan; penulis juga mencatat kebutuhan metode real-time untuk video dan penggabungan pendekatan citra tunggal dengan video.
