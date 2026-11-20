# Active Perception Fruit Harvesting Robots — A Systematic Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `magalhaes2022active` |
| Judul asli | Active Perception Fruit Harvesting Robots — A Systematic Review |
| Penulis | Magalh\~aes, Sandro Augusto; Moreira, Ant\'onio Paulo; Santos, Filipe Neves dos; Dias, Jorge |
| Tahun | 2022 |
| Venue | Journal of Intelligent and Robotic Systems Theory and Applications |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [magalhaes2022active.pdf](../pdf/magalhaes2022active.pdf)
- DOI resmi: https://doi.org/10.1007/s10846-022-01595-3

## Gambaran Umum

Studi ini adalah tinjauan sistematis tentang persepsi aktif (*active perception*) pada robot panen buah. Persepsi aktif berarti robot memilih sudut pandang atau gerakan kamera untuk melihat buah yang tertutup daun dan cabang.

Temuan utama penulis adalah sebagian besar riset deteksi buah masih bekerja di ruang dua dimensi (2D), baik dengan visi komputer klasik maupun pembelajaran mendalam (*deep learning*). Penulis menyimpulkan bahwa literatur tidak mendukung efektivitas sensor 2D saja untuk panen yang berhasil. Sebagian besar studi yang memakai sensor 2D menambahkan sensor kedalaman, seperti LiDAR atau ToF (*time of flight*), dan penulis mengutip dua studi sebagai contoh. Pendekatan klasik dan pembelajaran mendalam terbagi rata di literatur. Pendekatan klasik dinilai lebih mudah dilacak, tetapi lebih lambat karena dijalankan berurutan. Pembelajaran mendalam unggul dalam ketepatan, tetapi membutuhkan GPU atau perangkat keras khusus dan waktu latih yang lama.

Untuk tahap panen, sebagian besar studi memakai *visual servoing*, yaitu lengan robot dikendalikan langsung dari umpan balik kamera. Penulis mencatat batas pendekatan ini pada keteramatan (*observability*) saat buah tertutup. Sebagian studi karena itu memakai beberapa sudut pandang dengan perencanaan dinamis. Penulis menyebut empat langkah berikutnya: pemilihan sudut pandang untuk augmentasi data, penggunaan sensor haptik bersama visi, pemilihan pose genggam yang tidak merusak tanaman, dan pencarian aktif di area yang tertutup. Empat celah riset yang disebut adalah pemilihan sudut pandang yang aktif dan dinamis, penilaian sifat buah, deteksi titik potong tangkai, dan basis data prosedur panen.

Dari sisi cakupan tanaman, Tabel 5 pada studi ini menghitung publikasi per jenis buah. Apel tercatat 58 publikasi, tomat 23, dan paprika 21. Penulis menyebut bahwa paprika dan tomat umumnya ditanam di rumah kaca. Sebagian besar studi apel masih berhenti pada algoritma deteksi dan belum sampai ke panen. Penulis tidak memeriksa kelapa sawit sebagai jenis buah.

Studi ini tidak menghitung buah pada pohon dan tidak memuat eksperimen penghitungan. Keterbatasan yang dinyatakan penulis sendiri: kecepatan algoritma deteksi tidak dianalisis dalam tinjauan ini, padahal penulis menilai aspek itu relevan.
