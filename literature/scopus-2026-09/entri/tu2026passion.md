# Passion Fruit Counting Method Based on Lightweight YOLO lln CLL and BoT SORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tu2026passion` |
| Judul asli | Passion Fruit Counting Method Based on Lightweight YOLO lln CLL and BoT SORT |
| Penulis | Tu, S.; others |
| Tahun | 2026 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | passion fruit |

## Tautan Akses
- PDF: [tu2026passion.pdf](../pdf/tu2026passion.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2026.10.021

## Gambaran Umum

Makalah ini mengusulkan kerangka penghitungan buah markisa yang ringan untuk mendukung pemanenan otomatis. Permasalahan yang diangkat adalah tumpang tindih antara buah dan daun atau ranting, perubahan pencahayaan, dan getaran kamera. Ketiga faktor itu menyebabkan kehilangan deteksi, deteksi palsu, dan penghitungan ganda.

Data dikumpulkan di kebun markisa di distrik Huadu dan Conghua, Guangzhou, pada Oktober 2021 dan Oktober 2022. Ponsel HUAWEI P50 dipasang 1,5 m di atas tanah dengan jarak 1 m ke objek, setiap video menjangkau sekitar 15 m area tanam. Dataset terdiri atas 21 video dengan total 37.800 frame, resolusi 1080×1920 pixel, laju 30 frame/s, dan durasi 1 menit per video. Tiap frame memuat 2 sampai 15 buah dengan rata-rata 10 buah. Empat jenis adegan dicakup, yaitu okklusi rapat oleh daun dan ranting, pencahayaan kuat sampai overeksposur, citra kabur akibat pergerakan perangkat, dan pencahayaan ideal sebagai acuan. Penandaan dilakukan dengan DarkLabel.

Tahap deteksi memakai YOLO11n-CLL, yaitu YOLO11n yang dimodifikasi dengan tiga perubahan. Blok C3k2_CG menyisipkan context-guided block pada backbone untuk memperkuat konteks. Mekanisme atensi large separable kernel ditambahkan untuk pemodelan ciri pada beberapa skala. Detection head ringan dengan convolution peningkat detail dipakai untuk membangun kembali tekstur buah yang tertutup. Tahap pelacakan memakai BoT-SORT dengan kompensasi gerak kamera, prediksi Kalman, dan asosiasi dua tahap: kotak berkeyakinan tinggi dicocokkan memakai ciri tampilan dan posisi, lalu jejak yang tersisa dicocokkan dengan kotak berkeyakinan rendah memakai IoU (Bagian 2.3). Penghitungan membandingkan tiga cara, yaitu penjumlahan nomor identitas, penghitungan garis, dan penghitungan berbasis wilayah.

YOLO11n-CLL mencapai mAP@0,5 sebesar 87,0% dengan ukuran model 5,0 MB. BoT-SORT memperoleh HOTA 62,4% dan MOTA 68,4%. Pada delapan video uji, penghitungan berbasis wilayah mencapai akurasi rata-rata 92,8%, lebih tinggi 8,8 poin persentase daripada penghitungan garis (84,0%) dan 29,9 poin persentase daripada penjumlahan nomor identitas (62,9%) (Tabel 6, h. 216). Acuannya adalah jumlah buah pada video beranotasi.

Pendahuluan menyebut hasil penulis sebelumnya untuk penghitungan wilayah pada markisa dengan akurasi 87,0% dan hasil AN dkk. dengan pendekatan wilayah ganda sebesar 90,43%. Makalah ini menguji kembali pendekatan wilayah pada empat kondisi kebun yang lebih beragam dan menyatakan bahwa penentuan wilayah hitung lebih dulu membantu menekan penghitungan ganda.
