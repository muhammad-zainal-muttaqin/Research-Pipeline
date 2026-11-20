# Video-Based 3D Reconstruction: A Review of Photogrammetry and Visual SLAM Approaches

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `javadi2026video` |
| Judul asli | Video-Based 3D Reconstruction: A Review of Photogrammetry and Visual SLAM Approaches |
| Penulis | Javadi Moghadam, Ali; Kiani, Abbas; Naeimaei, Reza; Malihi, Shirin; Brilakis, Ioannis |
| Tahun | 2026 |
| Venue | Journal of Imaging |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [javadi2026video.pdf](../pdf/javadi2026video.pdf)
- DOI resmi: https://doi.org/10.3390/jimaging12030128

## Gambaran Umum

Artikel ini adalah tinjauan pustaka tentang rekonstruksi tiga dimensi (3D) berbasis video, dengan fokus pada fotogrametri dan *visual simultaneous localization and mapping* (V-SLAM). Masalah utamanya adalah kesenjangan antara rekonstruksi fotogrametrik yang akurat tetapi lambat dan sistem V-SLAM yang cepat tetapi kurang akurat, serta besarnya redundansi citra dalam video yang membebani komputasi. Penulis menyusun tinjauan ini untuk mengelompokkan metode, menjelaskan peran pemilihan citra kunci (*keyframe*), dan merumuskan arah penelitian. Meskipun berasal dari luar pertanian, mekanisme rekonstruksi dan asosiasi yang dibahas dapat ditransfer ke permasalahan identitas lintas pandang.

Data yang dianalisis berupa catatan SCOPUS untuk artikel jurnal hingga akhir 2024, ditambah sekitar 80 kajian yang ditelaah lebih rinci. Video diperlakukan sebagai kumpulan banyak citra dengan kontinuitas waktu dan laju 20–60 citra per detik. Metode dikelompokkan menjadi empat kategori: alur kerja berbasis fotogrametri, sistem V-SLAM untuk pemetaan daring, pendekatan berbasis pembelajaran atau hibrida, serta rekonstruksi spatiotemporal empat dimensi (4D). Pemilihan citra kunci menjadi komponen lintas kategori yang menentukan akurasi sekaligus efisiensi.

Mekanisme rekonstruksi bersifat bertahap. *Structure from Motion* (SfM) mendeteksi dan mencocokkan titik ciri, memverifikasi geometri, membangun pose kamera dan awan titik jarang melalui triangulasi, lalu menyempurnakannya dengan *bundle adjustment* yang meminimalkan galat proyeksi ulang. *Multi-View Stereo* (MVS) kemudian membangun peta kedalaman dan menggabungkannya menjadi awan titik padat serta mesh bertekstur. V-SLAM bekerja secara daring melalui pelacakan ciri, optimasi pose, dan penutupan loop untuk menekan pergeseran. Pemilihan citra kunci memakai kriteria geometris, kualitas citra,_data sensor seperti IMU dan GPS, atau model pembelajaran yang memprediksi kegunaan suatu citra.

Angka hasil dan acuan hitung yang disajikan mencakup temuan bibliometrik penulis maupun angka dari kajian yang ditinjau. Analisis SCOPUS penulis menunjukkan total sekitar 6.863 publikasi jurnal, dengan rincian SfM 4.607, V-SLAM 1.115, MVS 933, dan videogrammetri 208. Dari kajian lain, video 8K meningkatkan kerapatan awan titik dan akurasi rekonstruksi hingga 90% dibandingkan video HD dari drone yang sama, meningkatkan *ground sampling distance* sekitar empat kali pada ketinggian terbang sama, tetapi menaikkan kebutuhan memori, daya komputasi, dan waktu olah rata-rata lebih dari dua puluh kali. Untuk video 25 citra per detik, mengekstrak hanya sekitar 7–10% citra sudah cukup menghasilkan rekonstruksi akurat. DynPL-SLAM memiliki kecepatan olah sekitar 18,6% lebih tinggi daripada ORB-SLAM3, sedangkan ORB-SLAM2 mengungguli metode langsung dan ICP pada struktur tertutup tanpa memerlukan pemrosesan GPU. NeuralRecon mengungguli metode mutakhir dalam kualitas dan kecepatan, tetapi tidak memenuhi ketelitian geometris untuk aplikasi fotogrametri.

Batasan yang dikemukakan penulis mencakup tiga tantangan utama, yaitu adegan dinamis, pergeseran jangka panjang, serta rekonstruksi padat secara waktu nyata. Pemilihan citra kunci dan keandalan ciri menjadi titik hambat karena citra buram, berulang, atau bertekstur rendah menambah pencilan dan mengganggu stabilitas optimasi. Metode berbasis pembelajaran memerlukan sumber daya komputasi besar dan data latih banyak, serta generalisasi di luar sebaran latih masih belum memadai untuk keperluan metrologi. Metode berbasis Gaussian juga memiliki kendala waktu nyata, sehingga lebih cocok untuk aplikasi luring. Penulis menutup dengan perlunya protokol evaluasi terstandar yang melaporkan akurasi, ketahanan, kelengkapan, waktu jalan, dan mode kegagalan secara bersamaan.
