# COUNTING OF OIL PALM FRESH FRUIT BUNCHES USING COMPUTER VISION

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shiddiq2023counting` |
| Judul asli | COUNTING OF OIL PALM FRESH FRUIT BUNCHES USING COMPUTER VISION |
| Penulis | Shiddiq, Minarni |
| Tahun | 2023 |
| Venue | Journal of Oil Palm Research |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [shiddiq2023counting.pdf](../pdf/shiddiq2023counting.pdf)
- DOI resmi: https://doi.org/10.21894/jopr.2022.0029

## Gambaran Umum

Penelitian ini bertujuan membangun sistem penghitungan otomatis untuk tandan buah segar (TBS) sawit yang bergerak di atas konveyor. Penghitungan diperlukan untuk mengestimasi hasil panen dan kapasitas pabrik minyak sawit dalam ton per jam pada tahap pemilahan dan penilaian mutu. Penghitungan manual rusak oleh kondisi psikologis pekerja, sedangkan penghitungan mekanis dengan sensor elektronik tidak menyimpan informasi bentuk, ukuran, dan tekstur buah. Penulis mengusulkan metode penglihatan komputer yang mendeteksi dan melacak TBS pada frame video. Tingkat kematangan tidak termasuk dalam penilaian.

Sistem terdiri atas konveyor ember berlantai putih, kamera RGB Havit HV-V662 dengan sensor 1/3 inci dan lensa tetap, komputer jinjing, serta program penghitungan berbasis Python dan OpenCV. Kamera dipasang 150 cm di atas konveyor. Konveyor mampu menahan TBS lebih dari 40 kg; konveyor sabuk tidak dipakai karena variasi berat buah. Sampel berupa 117 TBS varietas Tenera dengan beragam ukuran dan berat. Sepuluh video direkam pada 20 frame per detik dengan resolusi 640×480 piksel, dengan jumlah TBS, jumlah TBS per ember, dan tanggal pengambilan yang berbeda. Pengambilan dilakukan di laboratorium dengan pencahayaan ruangan yang tidak dapat diatur, sehingga intensitas cahaya berkisar antara 40 dan 235 lux.

Detektor dibangun sendiri dengan menambahkan ciri warna. Citra RGB diubah ke ruang warna HSV; kanal saturasi dipilih, lalu diambang untuk menghasilkan citra biner. Operasi morfologi dilasi dan erosi merapikan komponen piksel, kemudian kontur dicari. Kontur dengan luas lebih dari 9.000 diterima sebagai TBS dan diberi kotak pembatas serta titik pusat. Pelacak berbasis titik pusat memakai HashMap dengan tiga tahap, yaitu pendaftaran, pembaruan, dan penghapusan. Jika jarak titik pusat kurang dari 50 piksel, objek dianggap sama dan ID-nya dipertahankan; ID dihapus setelah objek tidak terdeteksi selama sejumlah frame berturut-turut. Penghitungan dilakukan dengan iterasi ID. Kinerja dinilai dengan matriks konfusi melalui recall, precision, F-score, dan akurasi sebagai TP/(TP+FN+FP)×100%.

Penulis tidak melaporkan pembagian data latih dan uji; kesepuluh video dinilai terhadap jumlah aktual per video. Pada video 5, jumlah aktual 15 dan hasil sistem 15 dengan TP 15 serta tanpa FP dan FN, sehingga recall, precision, dan F-score bernilai 1 dengan akurasi 100% pada 190 lux. Video 8 juga mencapai akurasi 100% pada 200 lux. Akurasi turun menjadi 50% pada video 4 dengan 40 lux, 60% pada video 10 dengan 60 lux, 62,50% pada video 9 dengan 80 lux, dan 93,75% pada video 3 dengan 235 lux. Nilai F-score tertinggi terjadi pada video 5 dan 8. Abstrak menyebut akurasi dapat mencapai 100,00% dan rata-rata akurasi penghitungan untuk 10 video adalah 79,35%. Sistem bekerja baik pada intensitas cahaya sekitar 180–210 lux.

Penulis menyatakan sejumlah batasan. Akurasi bergantung pada warna permukaan TBS dan intensitas cahaya ruangan. Orientasi TBS di ember membuat bagian yang lebih gelap menghadap kamera; konversi HSV memiliki batas sehingga bagian gelap gagal terdeteksi. Dua TBS yang berdekatan memiliki titik pusat yang dekat dan dianggap satu objek, seperti yang terjadi ketika empat buah hanya terhitung tiga. Pada intensitas tinggi, satu TBS dapat memperoleh dua ID karena luas kontur melebihi 9.000. Kecepatan konveyor tidak disesuaikan dengan laju frame, dan kamera beresolusi 640×480 dengan sensor 1/3 inci serta paparan otomatis menghasilkan perbedaan warna antarperekaman. Penulis menganjurkan pencahayaan yang sesuai, kamera dengan spesifikasi lebih tinggi, penambahan ciri selain warna, serta penggunaan algoritma pembelajaran mendalam seperti YOLO.
