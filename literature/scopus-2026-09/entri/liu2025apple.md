# The apple detection method based on multimodal features

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2025apple` |
| Judul asli | The apple detection method based on multimodal features |
| Penulis | Liu, Xiaoyang; Hu, Chongyang; Huang, Xupeng; Sun, Chenxin; Zhu, Rongjin; Wang, Cheng; Zhang, Yuxiang; Shen, Qian; Zhou, Hongbiao; Ruan, Chengzhi |
| Tahun | 2025 |
| Venue | Plos One |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [liu2025apple.pdf](../pdf/liu2025apple.pdf)
- DOI resmi: https://doi.org/10.1371/journal.pone.0334911

## Gambaran Umum
Kajian ini bertujuan meningkatkan akurasi deteksi apel dalam lingkungan kompleks yang ditandai oleh perubahan pencahayaan, oklusi, dan latar yang berantakan. Penulis menilai metode konvensional yang mengandalkan citra RGB atau perbaikan inkremental pada arsitektur pembelajaran mendalam sering tidak mencapai akurasi memuaskan. Pendekatan yang diusulkan menitikberatkan pada fusi fitur multimodal pada lapisan masukan, bukan perubahan arsitektur yang radikal. Empat modalitas digabungkan, yaitu citra RGB, peta fitur warna dan tepi, peta fitur kedalaman, serta awan titik. Fitur warna dan tepi menangkap sifat kromatik buah dan batas geometrik struktur pohon, peta kedalaman menjadi kanal tersendiri, sedangkan koordinat awan titik menjadi tiga kanal tambahan.

Data dikumpulkan dengan kamera kedalaman Intel RealSense D455 di kebun apel Matou, Kota Huai'an, Provinsi Jiangsu, Tiongkok; sebagian citra memakai model apel tiruan yang menyerupai apel asli dari segi tampilan dan tekstur. Citra warna beresolusi 848 × 480 dalam format RGB8, citra kedalaman berformat Z16 dengan rentang 0–4 m, dan awan titik disusun dari akumulasi 30 frame yang diambil hampir bersamaan agar merujuk pada adegan tiga dimensi yang sama. Awan titik mengalami reduksi derau memakai *voxel down sampling* dan deteksi pencilan lokal, dengan ambang berupa jarak rata-rata ditambah dua kali simpanan baku dari 30 tetangga terdekat; bagian kosong diisi dengan nol, lalu dilakukan transformasi koordinat agar sesuai dengan skala dunia nyata. Keselarasan citra warna dan awan titik diverifikasi dengan pemetaan proyeksi tiga dimensi ke dua dimensi memakai parameter intrinsik dan ekstrinsik kamera, pencerminan horizontal, serta koreksi offset. Dari hasil penyaringan diperoleh 572 citra yang membentuk himpunan data DA1, dibagi menjadi latih, validasi, dan uji dengan perbandingan 70%, 10%, dan 20%; augmentasi meliputi rotasi, penskalaan, pemotongan, penyesuaian warna, dan penambahan derau. Anotasi memakai LabelImg dengan mengabaikan buah yang tertutup lebih dari 80% luasnya.

Mekanisme pengolahan fitur dimulai dari operator selisih merah-hijau (R−G) untuk menonjolkan buah merah terhadap langit, ranting, dan daun, serta operator Laplacian pada citra skala abu-abu untuk mengekstrak tepi; penulis tidak memakai fitur tekstur karena citra kebun berpandangan luas sehingga tekstur kurang jelas dan bentuk buah yang hampir bulat sulit dinyatakan secara langsung. Peta selisih warna dan peta tepi dinormalisasi, lalu digabung dengan bobot 6:4 menjadi peta fitur buah utama (F). Himpunan DA2 dibentuk dengan menggabungkan kanal R, G, B, F, kedalaman (D), dan koordinat awan titik (XYZ) menjadi delapan kanal. Lapisan masukan YOLOv5 diubah dari tiga menjadi delapan kanal; kernel berukuran 6 × 6 dan 32 filter dipertahankan, hanya jumlah lapisan kernel yang disesuaikan. Sembilan ukuran kotak jangkar awal dioptimalkan dengan k-means 30 iterasi dan algoritma genetik. Metrik yang dipakai adalah presisi P = TP/(TP+FP), recall R = TP/(TP+FN), dan F1 = 2PR/(P+R).

Hasil pendahuluan pada data DA2 menunjukkan YOLOv5 sebagai kerangka dasar terbaik dengan P 88,4%, R 98%, F1 92,95%, dan 13,6 juta parameter, dibanding YOLOv3 (79,7%/99%/88,31%), YOLOv6 (84,9%/97%/90,55%), dan YOLOv8 (86,7%/97%/91,56%). Penambahan satu fitur meningkatkan kinerja, dengan RGB+XYZ memberi hasil tertinggi pada kelompok itu (91,2%/97%/94,01%). Fusi langsung R−G dan tepi menghasilkan 91,9%/97%/94,38%, sedangkan fitur buah utama yang sudah dibobotkan menghasilkan 92,9%/96%/94,42%. Kombinasi RGB+(R−G)+E+D justru menurun menjadi 88,6%/97%/92,61% karena fitur kromatisitas dan tepi tumpang tindih dengan informasi RGB serta kedalaman memberi sinyal yang bertentangan. Konfigurasi terbaik adalah RGB+XYZ+D+F dengan delapan kanal, mencatat P 95,8%, R 96%, dan F1 95,9%; pada konfigurasi delapan kanal yang sama, SSD+VGG16 mencatat 86,6%/78%/82,08% dan Faster RCNN+VGG16 88,2%/81%/84,45%. Abstrak menyebut perbaikan presisi sebesar 7,4% dan 6,3% berturut-turut dibandingkan dasar RGB saja dan RGB+kedalaman, yang sesuai dengan selisih terhadap 88,4% dan 89,5%. Pelatihan memakai SGD, batch 4, laju awal 0,01, momentum 0,937, regularisasi L2 0,0005, pemanasan 3 epoch, dan maksimal 200 epoch pada i5-11400H, RAM 16 GB, serta GPU RTX 3050 12 GB.

Bagian batasan khusus tidak dinyatakan secara terpisah. Penulis hanya menyatakan bahwa masih ada ruang perbaikan dan mengusulkan strategi fusi fitur yang lebih efisien serta penerapan pada cakupan skenario otomasi pertanian yang lebih luas. Selain itu, penulis mencatat fitur tekstur tidak dipakai, kotak jangkar awal belum dievaluasi sebelum dioptimalkan, dan buah dengan oklusi lebih dari 80% tidak dianotasi.
