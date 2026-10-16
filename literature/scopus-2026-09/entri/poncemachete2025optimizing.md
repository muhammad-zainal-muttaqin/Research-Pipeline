# Optimizing Fruit Yield Prediction: Evaluating Multiobject Tracking Algorithms for Calamansi Fruit Detection Using Yolov8m

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `poncemachete2025optimizing` |
| Judul asli | Optimizing Fruit Yield Prediction: Evaluating Multiobject Tracking Algorithms for Calamansi Fruit Detection Using Yolov8m |
| Penulis | Ponce-Machete, Regine A.; Fajardo, Arnel |
| Tahun | 2025 |
| Venue | 2025 17th International Conference on Computer and Automation Engineering Iccae 2025 |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [poncemachete2025optimizing.pdf](../pdf/poncemachete2025optimizing.pdf)
- DOI resmi: https://doi.org/10.1109/iccae64891.2025.10980575

## Gambaran Umum
Makalah prosiding ICCAE 2025 ini membandingkan tiga pelacak multi-objek (*multi-object tracking*, MOT), yaitu SORT, DeepSORT, dan ByteTrack, yang dipasangkan dengan detektor YOLOv8m untuk mencacah buah kalamansi (*Citrofortunella microcarpa*) dari video yang direkam drone. Data diambil di kebun komersial kalamansi di Naujan, Oriental Mindoro, Filipina. Detektor dilatih untuk dua kelas, yaitu bunga dan buah.

Hasil utama: YOLOv8m mencapai presisi 0,839, *recall* 0,794, F1 0,815, dan mAP@0,5 0,875. ByteTrack memberi hasil pelacakan terbaik dengan MOTA 59,671%, HOTA 65,424%, dan IDF1 73,72%, dibandingkan DeepSORT (51,57; 51,20; 61,961) dan SORT (41,59; 31,42; 44,52). Penulis menyimpulkan bahwa kombinasi YOLOv8m dan ByteTrack mengurangi hitungan ganda secara signifikan. Makalah tidak melaporkan akurasi jumlah akhir terhadap hitungan acuan (manual atau panen), sehingga klaim pengurangan hitungan ganda tidak diukur langsung.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengukuran hasil panen standar berupa hitung manual dan identifikasi visual dinilai subjektif, rumit, dan rentan galat manusia. Penghitungan buah juga terhambat oklusi. Salah satu strategi yang dikutip penulis adalah memperoleh data dari banyak pandangan sehingga buah yang tertutup dari satu sudut terlihat dari sudut lain, tetapi cara itu dapat menghasilkan hitungan berlebih karena buah yang sama terhitung dari berbagai sudut citra. Karena itu penulis menggabungkan akuisisi gerak kontinu oleh drone dengan pelacakan multi-objek agar buah tidak terhitung ganda.

## Ide Utama
Buah dideteksi pada setiap bingkai video, lalu pelacak memberi ID unik dan mempertahankannya antarbingkai. Hitungan per kelas diperoleh dengan menghitung ID yang belum pernah dihitung untuk kelas itu. Kontribusi makalah adalah membandingkan tiga pelacak pada data kalamansi dengan metrik MOT, bukan merancang pelacak baru.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Kebun seluas 5 hektare dengan lebih dari 3.000 pohon kalamansi; data diambil dari 300 pohon pada Januari sampai Februari 2024 pada pukul 08.00 sampai 11.00 dan 14.00 sampai 16.00. Video RGB direkam dengan drone DJI Air 2S yang tertulis "DJI Air 25" pada teks, berkamera 20 MP, beresolusi video 5472×3078 pada 25 fps. Drone menjaga jarak 1 sampai 1,5 meter dari target dengan kamera menghadap ke atas atau ke bawah, melayang atau bergerak perlahan mengitari pohon, dan pada ketinggian minimal 4 sampai 8 meter di atas pohon tertinggi. Bingkai video dikonversi menjadi citra melalui Roboflow. Jumlah citra, jumlah bidikan, dan pembagian data tidak dilaporkan.

### 2. Detektor
YOLOv8n, YOLOv8s, dan YOLOv8m diuji, dan YOLOv8m dipilih karena unggul pada banyak metrik. Parameter pelatihan: 100 epoch, *batch* 32, ukuran citra 640, optimizer SGD, laju belajar awal 0,01, kesabaran (*patience*) 20. Anotasi memakai Roboflow dengan dua kelas, bunga dan buah. YOLOv8m juga dibandingkan dengan Roboflow 3.0.

### 3. Pelacakan
SORT memakai filter Kalman dan algoritma Hungarian pada model gerak. DeepSORT menambahkan fitur penampakan dari jaringan identifikasi ulang (*re-identification*). ByteTrack memakai deteksi berkeyakinan tinggi dan rendah untuk menangani objek yang padat atau situasi kompleks.

### 4. Pencacahan
Tiap objek terlacak memiliki ID dan label kelas. Sistem memeriksa apakah ID itu sudah dihitung untuk kelasnya; bila belum, hitungan ditambah satu. Setiap objek unik terhitung sekali per kelas pada seluruh bingkai.

## Eksperimen dan Hasil
Detektor dinilai dengan presisi, *recall*, F1, dan mAP@0,5, sedangkan pelacak dinilai dengan MOTA, HOTA, dan IDF1.

| Model deteksi | Presisi | *Recall* | F1 | mAP@0,5 |
|---|---|---|---|---|
| Roboflow 3.0 | 0,774 | 0,668 | 0,717 | 0,724 |
| YOLOv8m | 0,839 | 0,794 | 0,815 | 0,875 |

| Pelacak | MOTA | HOTA | IDF1 |
|---|---|---|---|
| SORT | 41,59 | 31,42 | 44,52 |
| DeepSORT | 51,57 | 51,20 | 61,961 |
| ByteTrack | 59,671 | 65,424 | 73,72 |

Penulis menyatakan ByteTrack mempertahankan efisiensi komputasi yang sebanding dengan SORT, tetapi tidak melaporkan waktu inferensi atau kecepatan bingkai. Penulis juga memuat analisis biaya perangkat keras: drone (DJI Mini 2 SE sampai Phantom 4 RTK) dengan kisaran 18.590 sampai 182.064 dan laptop (Acer Aspire 6 sampai MSI Stealth 15M) dengan kisaran 38.949 sampai 64.950; mata uang tidak disebut pada teks, diduga peso tetapi tidak dinyatakan.

## Kelebihan dan Keterbatasan
Kelebihan: perbandingan tiga pelacak memakai metrik MOT standar (MOTA, HOTA, IDF1) pada data lapangan kebun komersial, dan hitungan dipisah per kelas (bunga dan buah).

Keterbatasan yang dinyatakan penulis: model hanya mampu mendeteksi buah dan bunga kalamansi karena data pelatihan bersifat khusus; penulis juga mencatat bahwa fitur penampakan DeepSORT tidak banyak membantu pelacakan buah (kesimpulan menulis "SORT", tetapi konteksnya menyangkut DeepSORT terhadap SORT).

Menurut pembacaan ringkasan ini: (a) hitungan total terhadap acuan hitung manual atau panen tidak dilaporkan, sehingga pengurangan hitungan ganda tidak terukur; (b) jumlah video, panjang video, dan jumlah anotasi untuk evaluasi MOT tidak dilaporkan; (c) MOTA di bawah 60% menunjukkan banyak kesalahan pelacakan, dan implikasinya terhadap akurasi hitungan tidak dibahas; (d) tabel hasil pelacakan diberi judul "Training Parameters" dan teks menyebutnya Tabel II, yang menunjukkan kesalahan penomoran; (e) klaim "pelopor" pada kesimpulan tidak didukung perbandingan dengan literatur.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dengan mekanisme pelacakan (SORT, DeepSORT, ByteTrack berbasis deteksi YOLOv8m dan penghitungan ID unik). Penulis menyebut pendekatan multi-pandang berisiko menghitung ganda, tetapi tidak menerapkan penyatuan identitas lintas sisi pohon; yang diuji adalah gerak kontinu drone. Hitungan dipisah per kelas hanya antara bunga dan buah, bukan per tingkat kematangan. Acuan evaluasi pelacakan adalah anotasi untuk metrik MOT (jenis anotasinya tidak diuraikan), bukan hasil panen atau hitung lapangan.

Untuk pencacahan tandan sawit multi-sisi, kontribusi yang dapat dipindahkan terbatas pada perbandingan metrik pelacakan (HOTA dan IDF1 menilai kualitas asosiasi identitas, bukan sekadar deteksi) dan pola penghitungan ID unik per kelas. Metrik tersebut berguna sebagai ukuran konsistensi identitas bila diterapkan pada urutan citra sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `poncemachete2025optimizing`.

Ponce-Machete dan Fajardo (2025) membandingkan SORT, DeepSORT, dan ByteTrack berbasis detektor YOLOv8m pada video drone kebun kalamansi di Filipina. YOLOv8m mencapai mAP@0,5 0,875, dan ByteTrack memberi MOTA 59,671%, HOTA 65,424%, serta IDF1 73,72%, lebih tinggi daripada DeepSORT dan SORT. Akurasi jumlah akhir terhadap hitungan acuan tidak dilaporkan.

Catatan verifikasi data: Angka deteksi tertulis pada Tabel II (bagian II-B) dan angka pelacakan pada tabel hasil pelacakan (teks menyebut Tabel II, tabel dicetak sebagai Tabel III dengan judul keliru "Training Parameters"). Parameter pelatihan terdapat pada Tabel I. Angka biaya pada Tabel IV tidak disertai mata uang. Jumlah citra, video, pohon yang dianotasi untuk evaluasi, dan pembagian data tidak dapat diverifikasi dari teks. Penulisan model drone pada teks ("DJI Air 25") diduga salah ketik dan dicatat apa adanya. Teks ekstraksi terbaca utuh.
