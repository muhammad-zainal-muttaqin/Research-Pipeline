# Detection the Ripeness of Oil Palm Fresh Fruit Bunch Using Pretrained and Improved Models of YOLOv8

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jumrat2026detection` |
| Judul asli | Detection the Ripeness of Oil Palm Fresh Fruit Bunch Using Pretrained and Improved Models of YOLOv8 |
| Penulis | Jumrat, Saysunee; Saeleung, Pattanapong; Pianroj, Yutthapong; Chotikawanid, Piyanart; Punvichai, Teerasak; Chitcharoen, Doungrat; Muangprathub, Jirapond |
| Tahun | 2026 |
| Venue | Journal of Advances in Information Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [jumrat2026detection.pdf](../pdf/jumrat2026detection.pdf)
- DOI resmi: https://doi.org/10.12720/jait.17.6.1028-1040

## Gambaran Umum

Kajian ini mengatasi klasifikasi kematangan tandan buah segar (TBS) kelapa sawit yang selama ini dilakukan secara manual. Petani menilai kematangan melalui warna dan jumlah buah yang rontok, sementara profesional di pabrik mengamati tandan di area pembuangan. Cara ini memakan waktu, menimbulkan biaya tenaga kerja, dan bergantung pada penilaian subjektif. Tujuan kajian adalah membangun sistem deteksi dan klasifikasi kematangan TBS berbasis YOLOv8 dengan memanfaatkan model terlatih (*pretrained*) dan penyempurnaan (*fine-tuning*) untuk meningkatkan akurasi sekaligus menekan waktu inferensi.

Tanaman yang dikaji adalah kelapa sawit, dengan tiga kelas kematangan sesuai praktik grading industri: mentah (*raw*), setengah matang (*half-ripe*), dan matang (*ripe*). Data dikumpulkan oleh Thaksin Palm Company di Thailand di bawah kondisi industri nyata memakai kamera RGB standar pada beragam jarak dan sudut serta pencahayaan alami. Dataset berisi 427 citra bersih setelah proses pembersihan, terdiri atas 146 citra mentah, 127 citra setengah matang, dan 154 citra matang. Anotasi kotak pembatas dilakukan manual memakai Roboflow oleh tenaga terlatih, lalu ditinjau ulang agar konsisten. Data dibagi dengan rasio 7:2:1 untuk latih, validasi, dan uji. Augmentasi diterapkan hanya pada data latih, meliputi pembalikan horizontal (probabilitas 0,5), transformasi *grayscale* (25 persen), derau Gaussian (rerata 0, varians 0,01), dan blur Gaussian (kernel 5×5, probabilitas 0,3), sehingga menghasilkan 891 citra latih, 84 citra validasi, dan 46 citra uji.

Mekanisme deteksi memakai YOLOv8 sebagai model deteksi satu tahap (*single-stage*) yang memprediksi kotak pembatas dan probabilitas kelas langsung dari keseluruhan citra dalam satu lintasan. Lima varian terlatih (n, s, m, l, x) diuji dengan pelatihan 100 epoch memakai optimizer Adam, laju pembelajaran awal 0,001, jadwal penurunan kosinus, dan ukuran batch 16. Model terbaik (YOLOv8x) disempurnakan lebih lanjut melalui pembekuan selektif pada 10, 13, 16, dan 19 blok *backbone*, sementara *neck* dan *detection head* tetap dilatih. Selama *fine-tuning*, laju pembelajaran diturunkan menjadi 0,0001. Penulis tidak mengubah arsitektur YOLOv8; istilah "YOLOv8 yang ditingkatkan" merujuk pada strategi pelatihan, bukan perubahan struktur jaringan.

Evaluasi memakai metrik presisi, *recall*, F1-score, mAP50, dan mAP50–95, serta waktu deteksi per citra. Model YOLOv8x19 (19 blok *backbone* dibekukan) memberi kinerja terbaik dengan presisi 0,966, *recall* 0,968, F1-score 0,967, mAP50 0,988, dan mAP50–95 0,773, diukur pada cawat uji 46 citra. Waktu inferensinya 16,2 ms per citra (sekitar 61,7 FPS), lebih singkat 13,1 ms dibandingkan YOLOv8x penuh (29,3 ms). Pengukuran terpisah pada 45 citra uji mencatat inferensi 32,8 ms, praproses 1,8 ms, dan pascaproses 1,3 ms, dengan total 35,9 ms (rerata 32 ms per citra). Matriks kebingungan menunjukkan klasifikasi 100 persen benar untuk kelas mentah dan matang serta 89 persen untuk kelas setengah matang.

Penulis menyatakan sejumlah batasan. Kesalahan klasifikasi paling sering terjadi antara kelas setengah matang dan matang karena kemiripan warna dan tekstur pada tahap kematangan antara, terutama saat pencahayaan berubah. Okklusi sebagian tandan dan kekacauan latar belakang juga menyebabkan prediksi keliru, khususnya ketika beberapa tandan muncul dalam satu citra. Penulis menilai fitur visual RGB saja mungkin tidak cukup untuk membedakan transisi kematangan yang halus. Ukuran dataset yang terbatas membatasi paparan model terhadap pola visual langka atau ambigu, sehingga menurunkan ketahanan pada skenario tandan tumpang tindih maupun pencahayaan tidak merata.
