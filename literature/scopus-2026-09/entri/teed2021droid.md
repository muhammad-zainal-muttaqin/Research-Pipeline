# DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `teed2021droid` |
| Judul asli | DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras |
| Penulis | Teed, Z.; others |
| Tahun | 2021 |
| Venue | Advances in Neural Information Processing Systems |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [teed2021droid.pdf](../pdf/teed2021droid.pdf)

## Gambaran Umum

Simultaneous Localization and Mapping (*SLAM*) bertujuan membangun peta lingkungan sekaligus menentukan posisi kamera di dalam peta tersebut. Kajian ini menyoroti masalah ketahanan sistem SLAM. Kegagalan sering terjadi karena hilangnya jejak fitur, divergensi optimisasi, dan akumulasi *drift*. Penulis mengusulkan DROID-SLAM, sistem SLAM visual berbasis pembelajaran dalam yang dirancang akurat sekaligus tangguh.

DROID-SLAM memperbarui pose kamera dan kedalaman per piksel secara iteratif. Pembaruan dilakukan melalui lapisan *Dense Bundle Adjustment* yang dapat diturunkan. Sistem ini dilatih hanya dengan masukan monokular pada data sintetis TartanAir. Model yang sama kemudian diuji pada video monokular, stereo, dan RGB-D dari empat kumpulan data. Kumpulan data tersebut adalah TartanAir, EuRoC yang direkam dari pesawat mikro tanpa awak, TUM-RGBD, dan ETH-3D. Untuk ETH-3D, video dapat mencapai 5000 bingkai. Penulis memakai uji resmi TartanAir dan tidak merinci jumlah citra untuk setiap pembagian data pada kumpulan lainnya.

Pada TartanAir monokular, sistem tidak mengalami kegagalan katastrofik. Kesalahannya turun 62% dibandingkan hasil terbaik sebelumnya pada jalur monokular dan 60% pada jalur stereo. Pada skor uji TartanAir, nilai DROID-SLAM adalah 0,129 untuk monokular dan 0,047 untuk stereo. Nilai terbaik lain yang dibandingkan adalah 0,340 untuk monokular dan 0,119 untuk stereo. Pada ETH-3D RGB-D, sistem berhasil melacak 30 dari 32 kumpulan data, sedangkan metode terbaik berikutnya hanya 19 dari 32. Pada EuRoC monokular, kesalahan turun 82% di antara metode tanpa kegagalan. Dibandingkan ORB-SLAM3 pada 10 dari 11 urutan yang berhasil, penurunannya 43%. Pada EuRoC stereo, penurunannya 71%. Pada TUM-RGBD, kesalahan turun 83% di antara metode tanpa kegagalan. Dari sisi kecepatan, sistem berjalan sekitar 20 bingkai per detik pada EuRoC dan 30 bingkai per detik pada TUM-RGBD. Pada TartanAir, kecepatannya 8 bingkai per detik. Kecepatan ini 16 kali lebih cepat daripada dua pengirim teratas yang bergantung pada COLMAP.

Penulis menyatakan beberapa batasan. Kebutuhan memori dan sumber daya komputasi menjadi kendala utama. Bagian *frontend* dapat berjalan pada GPU dengan memori 8 GB. Bagian *backend* lebih berat karena harus menyimpan peta fitur dari seluruh citra. Hasil EuRoC, TartanAir, dan ETH-3D memerlukan GPU dengan memori 24 GB. Pada TartanAir, gerak kamera yang cepat membuat sistem belum mampu berjalan secara waktu nyata. Penulis berharap kebutuhan ini dapat dikurangi dengan memangkas komputasi yang berlebihan dan memakai representasi yang lebih efisien.
