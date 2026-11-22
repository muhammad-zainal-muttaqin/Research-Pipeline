# Advance Assessment and Counting of Ripe Cherry Tomato’s Via Yolo Model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `naseem2025advance` |
| Judul asli | Advance Assessment and Counting of Ripe Cherry Tomato’s Via Yolo Model |
| Penulis | Naseem, Minhaj; Ahmad, Bushra; Razzaq, Abdul Manan; QADRI, Salman; Ullah, Sami; Saeed, Shafqat; Jamil, Muhammad Ahsan |
| Tahun | 2025 |
| Venue | Journal of Computing and Biomedical Informatics |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [naseem2025advance.pdf](../pdf/naseem2025advance.pdf)

## Gambaran Umum

Makalah ini mendeteksi, menghitung, dan menilai kematangan tomat ceri (*cherry tomato*) yang tumbuh di rumah kaca. Penulis berargumen bahwa pengumpulan data fenotipe dan penghitungan buah secara manual melelahkan, sementara metode pengolahan citra klasik dinilai kurang memadai. Mereka mengusulkan deteksi berbasis *deep learning* dengan YOLO, dengan tujuan akhir pengelolaan hasil panen dan otomatisasi pemanenan.

Data dikumpulkan di rumah kaca dengan kamera resolusi tinggi yang diarahkan ke tanaman dari berbagai sudut dan jarak, dengan kondisi pencahayaan yang bervariasi. Teks menyebut minimal 500 citra dianotasi dengan kotak pembatas (*bounding box*) pada setiap tomat. Tabel 1 melaporkan 640 citra dan 3.456 instans: 280 citra dan 2.786 instans tidak matang (*unripe*), serta 185 citra dan 1.659 instans matang (*ripe*). Data dibagi 70% latih, 15% validasi, dan 15% uji. Teks tidak menyebut jenis sensor atau tipe kamera, jumlah tanaman, lokasi rumah kaca, atau apakah beberapa citra berasal dari tanaman atau tandan yang sama.

Metode yang dipakai adalah YOLOv8, yang dipilih karena keseimbangan kecepatan dan akurasinya. Teks menyatakan jumlah kelas diatur menjadi 1, tetapi di bagian lain juga disebut dua kelas, matang dan tidak matang, sehingga konfigurasi kelas tidak jelas. Augmentasi berupa rotasi, pembalikan, penskalaan, dan *color jittering* diterapkan. Citra diubah ukurannya menjadi 416×416 piksel dan nilai pikselnya dinormalisasi ke rentang [0, 1]. Hasil pada data uji dilaporkan sebagai presisi 92,6% dan recall 94,7% untuk deteksi, penghitungan, dan penilaian kematangan. Pada Tabel 1, mAP50 seluruh kelas adalah 0,16 dan mAP50-95 adalah 0,0823. Untuk kelas matang, mAP50 adalah 0,198 dan mAP50-95 adalah 0,107. Untuk kelas tidak matang, mAP50 adalah 0,123 dan mAP50-95 adalah 0,058. Kolom presisi pada tabel tidak terbaca jelas, dan nilainya tidak sejalan dengan presisi 92,6% di teks, sehingga tidak dipakai. Teks menyebut hasil penghitungan dibandingkan dengan jumlah kebenaran dasar, tetapi angka galat hitung tidak dilaporkan.

Teks tidak menyajikan perbandingan dengan metode klasik pada data yang sama, padahal penulis menyatakan hasilnya "comparatively better" dari metode klasik. Penulis juga tidak menjelaskan cara penghitungan presisi dan recall, misalnya apakah dihitung per citra atau per buah, serta ambang kepercayaan yang dipakai. Angka presisi dan recall dengan demikian sulit dibandingkan dengan angka mAP pada Tabel 1. Makalah ini juga tidak memuat bagian keterbatasan tersendiri.
