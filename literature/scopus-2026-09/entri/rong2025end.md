# An end-to-end maturity prediction and hierarchical counting method for cherry tomatoes

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rong2025end` |
| Judul asli | An end-to-end maturity prediction and hierarchical counting method for cherry tomatoes |
| Penulis | Rong, Jiacheng; Li, Xianjun; Zheng, Wanli; Chen, Tongqiang; Yuan, Ting; Wang, Pengbo; Li, Wei |
| Tahun | 2025 |
| Venue | Biosystems Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [rong2025end.pdf](../pdf/rong2025end.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2025.104191

## Gambaran Umum

Pemanenan dan inspeksi tomat ceri di pertanian vertikal menuntut penilaian kematangan buah secara otomatis. Masalahnya, pencahayaan yang berubah-ubah dan oklusi oleh batang serta daun menyulitkan penilaian visual. Metode berbasis warna dan pengolahan citra klasik juga peka terhadap silau dan tata letak rumah kaca. Penelitian ini mengusulkan *Lightweight Cherry Tomato Multi-Task Detection* (CT-MTD), yaitu model *deep learning* multi-tugas yang ringan untuk memperkirakan kematangan sekaligus mendeteksi oklusi. Model tersebut kemudian dipakai dalam metode pencacahan tomat per tingkat kematangan untuk robot inspeksi.

Citra dikumpulkan di Ni-hui Agricultural Base dari Mei hingga Juli 2024. Kamera Intel RealSense D435i dan Microsoft Azure Kinect DK dipasang pada robot inspeksi dan menghasilkan citra beresolusi 1920*1080 piksel. Dari citra tersebut dibuat 600 sampel citra kelompok tomat yang telah dilokalisasi, lalu setiap sampel diberi label tingkat kematangan dan status oklusi. Data dibagi menjadi data latih, validasi, dan uji dengan rasio 7:1,5:1,5. Pengujian pencacahan dilakukan di dua rumah kaca. Rumah kaca S1 di Suzhou memiliki kepadatan tanam rendah, sedangkan rumah kaca S2 di Fengyang memiliki kepadatan tinggi dan direkam dalam video pada Juni 2024 dengan jarak kamera ke buah yang sedikit berbeda.

Model memakai *backbone* MobileViT bersama, dengan *Coordinate Attention* sebelum setiap cabang. Cabang regresi memperkirakan kematangan, sedangkan cabang klasifikasi mendeteksi oklusi. Pada hasil utama, model mencapai RMSE 0,048 untuk estimasi kematangan. Untuk deteksi oklusi, model mencapai akurasi 0,817 dan skor *F1* 0,778. Pada pencacahan, sistem menggabungkan pelacakan buah antarframe video dengan model kematangan untuk menghitung tomat dan mengelompokkannya ke dalam lima rentang kematangan. Akurasi total pencacahan adalah 90,2 % di S1 dan 87,1 % di S2. Akurasi rata-rata pencacahan per tingkat kematangan adalah 86,3 % di S1 dan 80,2 % di S2. Akurasi pada rentang kematangan 80–100 % di S1 mencapai 97,2 %. Akurasi pada rentang 40–60 % di S2 hanya 61,4 %. Penulis membandingkan hasilnya dengan Dai et al. (2022), yang mencapai akurasi 84–86 % dalam skenario rumah kaca yang umum. Penulis menyatakan bahwa hasil mereka sebanding, bahkan kadang lebih tinggi, yaitu 87 %–90 %, pada kondisi dengan distribusi buah yang lebih padat.

Penulis menyatakan beberapa batasan. Pertama, eksperimen belum mencakup kondisi malam hari, padahal kondisi ini penting untuk pemantauan rumah kaca secara terus-menerus. Kedua, model belum menghasilkan estimasi hasil panen secara langsung. Model baru menjadi langkah awal dengan mengumpulkan distribusi kematangan, dan estimasi hasil memerlukan model bobot buah serta pola pertumbuhan historis. Ketiga, keandalan algoritma bergantung pada data latih yang besar dan beragam agar mencakup variasi kondisi rumah kaca di dunia nyata. Penulis juga menyarankan studi ablasi yang membandingkan pendekatan regresi dan klasifikasi, serta kemungkinan pendekatan hibrida yang memanfaatkan kekuatan keduanya.
