# SAM 2: SEGMENT ANYTHING IN IMAGES AND VIDEOS

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ravi2025sam` |
| Judul asli | SAM 2: SEGMENT ANYTHING IN IMAGES AND VIDEOS |
| Penulis | Ravi, N.; others |
| Tahun | 2025 |
| Venue | 13th International Conference on Learning Representations Iclr 2025 |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [ravi2025sam.pdf](../pdf/ravi2025sam.pdf)

## Gambaran Umum

Kajian ini memperkenalkan SAM 2 (*Segment Anything Model 2*), model dasar (*foundation model*) untuk segmentasi visual yang dapat diberi perintah (*promptable*) pada gambar dan video. Masalah yang diangkat adalah keterbatasan model segmentasi sebelumnya. Segment Anything (SA) hanya menangani gambar diam, sedangkan video memiliki tantangan tambahan. Objek dapat berubah penampilan akibat gerak, deformasi, oklusi, dan perubahan pencahayaan. Kualitas video juga umumnya lebih rendah, dan jumlah frame yang harus diproses sangat besar. Penulis menilai model dan dataset video yang ada belum mampu "segmen apa pun dalam video". Karena itu, penulis merumuskan tugas segmentasi visual yang dapat diberi perintah (*Promptable Visual Segmentation*, PVS). Tugas ini menerima titik, kotak (*bounding box*), atau masker pada frame mana pun, lalu menghasilkan masker spatio-temporal objek yang disebut *masklet*. Hasil prediksi dapat diperbaiki dengan perintah tambahan pada frame lain.

Data utama dikumpulkan melalui *data engine*, yaitu proses ketika model ikut bekerja bersama anotator untuk memberi anotasi interaktif pada data yang baru dan sulit. Dataset akhir bernama SA-V berisi 35,5 juta masker pada 50,9 ribu video. Penulis menyatakan jumlah masker ini 53 kali lebih banyak daripada dataset segmentasi video mana pun sebelumnya. SA-V mencakup objek utuh maupun bagian objek, termasuk objek kecil yang tertutup lalu muncul kembali. Penulis menyebut data ini tersebar secara geografis. Evaluasi keadilan menunjukkan selisih performa yang minimal berdasarkan gender yang dipersepsikan, serta variasi kecil di antara tiga kelompok usia yang dipersepsikan. Evaluasi dilakukan secara zero-shot pada 9 dataset untuk segmentasi interaktif, 17 dataset video, dan 37 dataset gambar. Dari 37 dataset gambar tersebut, 23 berasal dari SAM dan 14 merupakan dataset video tambahan. Kecepatan diukur pada satu GPU A100. Teks tidak menyebutkan sensor kamera atau platform pengambilan citra, karena kajian ini berfokus pada data gambar dan video umum.

Model menggunakan arsitektur transformer sederhana dengan memori streaming yang memproses frame satu per satu. Modul *memory attention* membaca memori tentang objek dari frame sebelumnya. Pada gambar, memori dibiarkan kosong sehingga model berperilaku seperti SAM. Pada segmentasi video interaktif, rata-rata J&F dengan perintah (Gambar 5) mengungguli SAM+XMem++ dan SAM+Cutie, dengan interaksi lebih dari 3 kali lebih sedikit. Pada semi-supervised VOS (Tabel 4), SAM 2 mencapai J&F 64,7 dengan 1 klik, dibanding 56,9 (SAM+XMem++) dan 56,7 (SAM+Cutie). Dengan 3 klik, nilainya 75,3, dibanding 68,4 dan 70,1. Dengan 5 klik, nilainya 77,6, dibanding 70,6 dan 72,2. Dengan kotak, nilainya 74,4, dibanding 67,6 dan 69,4. Dengan masker ground truth, nilainya 79,3, dibanding 72,7 dan 74,1. Pada segmentasi gambar (Tabel 5), SAM 2 mencapai mIoU 58,9 dengan 1 klik pada 23 dataset SAM, sedikit di atas SAM yang mencapai 58,1. Kecepatan SAM 2 adalah 130,1 FPS, sedangkan SAM 21,7 FPS. Dengan campuran data SA-1B dan video, rata-rata pada 23 dataset naik menjadi 61,4 menurut teks. Pada VOS, SAM 2 dengan encoder Hiera-B+ berjalan 43,8 FPS dan Hiera-L 30,2 FPS. Kedua kecepatan tersebut disebut berjalan secara real-time.

Penulis merilis model utama, dataset SA-V dengan lisensi CC BY 4.0, kode pelatihan dengan lisensi Apache 2.0, kode demo interaktif, serta demo daring. Penulis juga menyatakan bahwa hasil pada kajian ini memakai pengaturan baku Hiera-B+ dengan resolusi 1024 untuk sebagian besar evaluasi, dan model yang dilaporkan merupakan versi yang diperbaiki dari rilis awal.
