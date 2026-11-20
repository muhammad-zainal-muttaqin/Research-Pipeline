# Adaptive region growing for automated oil palm fruit quality recognition

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `amosh2013adaptive` |
| Judul asli | Adaptive region growing for automated oil palm fruit quality recognition |
| Penulis | Amosh, LaylaWantgli Shrif; Sheikh Abdullah, Siti Norul Huda; Che Mohd, Che Radiziah; Jameson, Jinjuli |
| Tahun | 2013 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [amosh2013adaptive.pdf](../pdf/amosh2013adaptive.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-02958-0_18

## Gambaran Umum

Kajian ini (Amosh dkk., 2013, *Adaptive Region Growing for Automated Oil Palm Fruit Quality Recognition*, prosiding IVIC 2013, LNCS 8237) membahas segmentasi citra warna untuk mengenali mutu tandan buah segar (TBS) kelapa sawit. Tujuannya memperbaiki algoritma *seed region growing*, yaitu metode segmentasi yang memulai dari titik benih (*seed*) lalu memperluas wilayah berdasarkan kemiripan warna piksel tetangga. Metode konvensional membutuhkan benih yang dipilih manual atau berjumlah tetap, yang menambah beban komputasi dan waktu implementasi.

Usulan yang disebut n-Seed Region Growing (n-SRG) memilih jumlah benih secara adaptif. Data terdiri atas 80 citra dengan dua kelas kematangan, yaitu matang (*ripe*) dan mentah (*unripe*). Penulis melaporkan bahwa metode mereka mengungguli *k-means clustering* dengan akurasi rata-rata 86% dan 80%, berurutan. Angka ini tercatat di abstrak. Unit pengukuran (piksel atau citra), pembagian data latih dan uji, serta protokol perbandingan dengan k-means tidak dinyatakan dalam abstrak.

Pendahuluan memberi konteks ekonomi. Minyak sawit diperoleh dari mesokarp buah, dan keputusan panen sering keliru karena petani pemanen kurang berpengalaman menilai tingkat kematangan. Penulis juga mencatat bahwa penelitian otomatisasi penilaian mutu buah sawit di Malaysia masih terbatas.

Tabel 1 memuat dua kajian sebelumnya di bidang yang sama. Alfatni dkk. (2008) memakai citra RGB, saturasi, dan intensitas untuk tiga kelas (matang, mentah, dan lewat matang), dengan akurasi 90%. May dkk. (2011) memakai logika fuzzy dan warna RGB untuk tiga kelas kematangan, dengan akurasi 86,67%. Angka-angka itu tidak dapat dibandingkan langsung dengan 86% dan 80% dalam kajian ini, karena jumlah kelas, jumlah citra, dan unit pengukurannya berbeda atau belum diketahui.

Kajian ini mengolah segmentasi warna untuk klasifikasi kematangan dari citra TBS. Kajian tidak menghitung jumlah buah, tidak memakai beberapa tampilan (multi-view), dan tidak memakai data kedalaman.

Keterbatasan yang tampak dari abstrak dan pendahuluan: jumlah 80 citra tergolong kecil untuk dua kelas, dan tidak ada informasi tentang kondisi pencahayaan, sudut pemotretan, atau pemisahan data latih dan uji.
