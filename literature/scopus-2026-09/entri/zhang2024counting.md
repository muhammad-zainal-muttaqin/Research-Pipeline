# Counting tomatoes with different maturities using ultra-depth masking and improved YOLOv8

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2024counting` |
| Judul asli | Counting tomatoes with different maturities using ultra-depth masking and improved YOLOv8 |
| Penulis | Zhang, R.; others |
| Tahun | 2024 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [zhang2024counting.pdf](../pdf/zhang2024counting.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202407205

## Gambaran Umum

Penelitian ini bertujuan menghitung buah tomat menurut tingkat kematangan di rumah kaca dari video yang direkam saat kamera bergerak menyusuri baris tanaman. Penulis menyebut dua masalah. Pertama, buah di kejauhan kecil dan berulang kali tertutup, sehingga pelacak (*tracker*) sulit mengikuti buah yang sama dan menghasilkan hitungan ganda. Kedua, saat kamera menyusuri satu baris, buah pada baris di belakangnya ikut terlihat dan identitasnya mudah salah ditetapkan. Hitungan yang akurat dipakai untuk pendugaan hasil dan penentuan waktu petik.

Data direkam pada Oktober 2023 di satu rumah kaca di Shenyang, pada tanaman tomat yang digantung dan sedang berbuah lebat. Kamera Intel RealSense D435 beresolusi 1.920×1.080 piksel dipasang pada robot beroda setinggi sekitar 1,2 m dan merekam 30 bingkai/s. Terkumpul 145 video, kira-kira 300 bingkai per video, dengan dua arah pandang yang jumlahnya mirip (tegak lurus dan sejajar baris). Pemeriksa menghitung buah per kematangan secara manual untuk setiap video. Sebanyak 70 video (Va) dipakai menguji hitungan. Dari 75 video lainnya (Vb) diambil 1.900 bingkai, diberi kotak dengan labelImg, lalu dibagi 4:1 menjadi latih dan uji. Tiga kelas kematangan memiliki proporsi 13% matang, 16% setengah matang, dan 71% mentah. Siapa pemberi label tidak disebut.

Metode berurutan dalam tiga langkah. Detektor YOLOT, yaitu YOLOv8n yang dimodifikasi dengan operator konvolusi *involution* (kernel dihasilkan dari fitur tiap piksel) dan fungsi kerugian WIoU (*loss* kotak yang tahan terhadap selisih anotasi), mendeteksi buah di tiap bingkai. Model *Depth Anything* menaksir kedalaman relatif dari citra tunggal. Deteksi yang kedalaman titik tengahnya melebihi ambang ω = rerata kedalaman + ρ kali simpangan baku kedalaman citra itu dibuang ("penyamaran kedalaman ekstrem"). Pelacak BoT-SORT memberi identitas pada deteksi yang tersisa, dan jumlah identitas unik per kelas menjadi hasil hitungan.

Pada set uji deteksi, YOLOT mencapai mAP50 91,0%, mAP50-95 60,2%, dan *recall* 90,2%, dibanding YOLOv8n 87,8%, 58,2%, dan 86,5%. Pada 70 video, ketepatan hitung rata-rata (ACP, yaitu satu dikurangi rerata galat relatif terhadap hitungan manual) sebesar 93,80% dengan MAE 4,33 dan RMSE 4,93 pada ρ = −0,5. Selisih dengan tanpa penyamaran adalah 12,63 poin persentase. Gabungan YOLOv8n dan BoT-SORT mendapat ACP 86,12% dengan MAE 9,68. ACP per kematangan adalah 91,40% (matang), 92,93% (setengah matang), dan 95,54% (mentah). Kecepatan 23 bingkai/s. Arah pandang tegak lurus menghasilkan ACP 94,00% dan arah sejajar 91,41%.

Keterbatasan yang dapat diperiksa dari teks: seluruh data berasal dari satu rumah kaca dan satu musim. Pembagian latih dan uji detektor dilakukan pada bingkai dengan rasio 4:1, dan teks tidak menyatakan apakah bingkai satu video terpisah antarsplit. Nilai ρ = −0,5 dipilih dari hasil pada video Va yang sama dengan video evaluasi hitungan, dan teks tidak menyebut set validasi terpisah. Hitungan acuan adalah hitungan manual, tanpa keterangan jumlah pemeriksa. Kelas matang hanya 13% dari label, dan penulis mengakui hal ini menurunkan ACP kelas tersebut.
