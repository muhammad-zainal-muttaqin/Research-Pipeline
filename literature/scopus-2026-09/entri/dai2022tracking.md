# Tracking and Counting Method for Tomato Fruits Scouting Robot in Greenhouse

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `dai2022tracking` |
| Judul asli | Tracking and Counting Method for Tomato Fruits Scouting Robot in Greenhouse |
| Penulis | Dai, Guanglin; Hu, Ling; Wang, Pengbo; Rong, Jiacheng |
| Tahun | 2022 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [dai2022tracking.pdf](../pdf/dai2022tracking.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-031-13844-7_6

## Gambaran Umum

Penelitian ini bertujuan mengembangkan metode penghitungan buah tomat untuk robot inspeksi di rumah kaca. Jumlah buah tomat berkaitan dengan informasi hasil panen, sehingga penghitungan otomatis diperlukan karena lingkungan rumah kaca panas dan berat untuk pekerjaan manual. Metode yang diusulkan melacak posisi tomat dalam citra memakai informasi perpindahan spasial robot, dengan penyaringan kedalaman tiga dimensi untuk menghilangkan gangguan tomat di latar belakang. Pendekatan ini dirancang agar dapat melacak tandan buah sekaligus menghitung buah tunggal di dalamnya.

Tanaman yang dipakai adalah tomat ceri kultivar "jiaxina" dari rumah kaca nijiawan, Distrik Xiangcheng, Kota Suzhou, Provinsi Jiangsu. Tomat ditanam dalam barisan dan buahnya tumbuh bergumpal dalam tandan; setelah perlakuan agronomi, buah matang berada pada rentang tinggi tetap dari tanah. Robot inspeksi terdiri dari kamera kedalaman Realsense D435i, tiang pengangkat, dan sasis berrel rumah kaca yang memakai sistem RFID untuk mengendalikan nyala mati fungsi inspeksi. Kamera dipasang tetap dengan sumbu tegak lurus bidang barisan, berjarak 500-650 mm dari barisan dan pada tinggi 1650 mm dari tanah. Citra yang diperoleh terdiri dari gambar RGB dan peta kedalaman yang sejajar, masing-masing berukuran 1280 × 720 piksel.

Deteksi memakai YOLOv5 dengan dua model terpisah, satu untuk tandan buah dan satu untuk buah tunggal. Data dikumpulkan dari Oktober hingga Desember 2021 dalam tiga rentang waktu, yaitu 06.00-08.00, 12.00-14.00, dan 16.00-17.00, yang mencakup kondisi cerah, berawan, dan hujan. Robot bergerak dengan kecepatan tetap 0,1 m/s dan menyimpan gambar sebanyak 5 frame per detik; dari sekitar 15.000 citra, 3000 citra dengan latar dan tingkat kematangan berbeda dipilih. Citra diberi anotasi dua kali dengan Labelme dan rasio latih, validasi, uji adalah 1:1:19. Setiap tandan yang terdeteksi diberi daftar informasi [frame, ID, x, y, w, h, a, D, s], berturut-turut nomor frame, jumlah tandan yang terdeteksi sejak awal, koordinat piksel dan ukuran kotak, jumlah buah tunggal dalam tandan, nilai rata-rata kedalaman buah, serta jarak tempuh kumulatif robot. Peta kedalaman dipakai untuk menyaring tomat latar belakang yang terdeteksi salah, dan daftar dengan koordinat x kurang dari 100 atau lebih dari 1180 dihapus agar tandan di tepi citra tidak menimbulkan kesalahan pelacakan.

Pelacakan menghilangkan label ganda dengan memprediksi posisi kotak buah pada frame sebelumnya memakai perpindahan robot dan transformasi koordinat kamera, lalu menghitung rasio irisan terhadap gabungan (IOU) terhadap semua kotak pada frame sebelumnya. Apabila IOU lebih dari 0,8, daftar yang bersangkutan dianggap duplikat dan dihapus; setiap daftar dibandingkan dengan seluruh daftar dalam 30 frame sebelumnya. Pada akhir inspeksi, jumlah daftar yang tersisa menjadi jumlah tandan dan jumlah nilai a menjadi jumlah buah tunggal. Uji pada tiga jalur rel dengan kecepatan 0,1 m/s menghasilkan akurasi penghitungan tandan sebesar 86,7%, 91,2%, dan 87,2% serta akurasi buah tunggal sebesar 84,8%, 88,3%, dan 84,2%; jumlah tandan aktual berturut-turut 30, 68, 86 dan yang terdeteksi 34, 75, 98, sedangkan jumlah buah tunggal aktual 356, 664, 704 dan yang terdeteksi 302, 586, 593. Perbandingan dengan DeepSORT pada aliran warna yang sama memberi akurasi tandan 61,2%-59,7% dan buah tunggal 74,3%-79,2%; penulis menyebut DeepSORT tidak memiliki penyaringan kedalaman sehingga memasukkan banyak tomat latar belakang ke dalam hitungan.

Penulis menyatakan akurasi penghitungan buah tunggal lebih rendah daripada tandan karena buah saling menutupi; pengenalan dari berbagai sudut masih terpengaruh oleh oklusi antarbuah. Jumlah tandan yang terdeteksi juga melebihi jumlah aktual karena sebuah tandan yang gagal dikenali dalam beberapa frame berturut-turut lalu dikenali kembali dihitung sebagai tandan baru, sehingga akurasi pengenalan pada satu frame menjadi penting. Penulis tidak menyebut metrik statistik lain, interval kepercayaan, atau split uji bernomor; pengujian didasarkan pada perbandingan dengan hitungan manual di tiga jalur. Pekerjaan berikutnya difokuskan pada peningkatan akurasi pengenalan tandan dan buah tunggal, khususnya penanganan oklusi, misalnya dengan model berbeda untuk tiap periode atau perubahan jaringan.
