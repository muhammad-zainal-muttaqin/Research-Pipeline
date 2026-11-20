# A review on structural development and recognition–localization methods for end-effector of fruit–vegetable picking robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022review` |
| Judul asli | A review on structural development and recognition–localization methods for end-effector of fruit–vegetable picking robots |
| Penulis | Li, Ziyue; Yuan, Xianju; Wang, Chuyan |
| Tahun | 2022 |
| Venue | International Journal of Advanced Robotic Systems |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [li2022review.pdf](../pdf/li2022review.pdf)
- DOI resmi: https://doi.org/10.1177/17298806221104906

## Gambaran Umum

Tinjauan ini membahas dua hal pada robot pemetik buah dan sayur: struktur *end-effector* (bagian ujung lengan robot yang menyentuh dan memisahkan buah) dan metode pengenalan serta penentuan lokasi buah. Penulisnya Ziyue Li, Xianju Yuan, dan Chuyan Wang, dan naskahnya terbit di *International Journal of Advanced Robotic Systems*. Masalah yang diangkat adalah pemetikan yang lambat, keberhasilan panen yang bervariasi, dan buah yang rusak saat dipetik.

Struktur *end-effector* dikelompokkan menurut cara menggenggam: tipe hisap (*suction*), tipe jepit (*clamping*), dan tipe hisap-jepit (*sucking-clamping*). Tinjauan ini juga membahas manipulator *underactuated* (digerakkan oleh jumlah penggerak yang lebih sedikit daripada derajat kebebasannya) dan manipulator lunak (*soft*). Tabel 1 membandingkan beberapa instansi. Pada apel, tipe hisap di lapangan mencapai keberhasilan panen 80% dengan waktu siklus 8–10 detik, tipe jepit 77% dengan 15 detik, dan tipe tabung 82,14% dengan 4,5 detik. Pada stroberi, tipe hisap di rumah kaca mencapai 41,3%, dan tipe potong di laboratorium 70%. Pada tomat, tipe hisap-jepit di laboratorium mencapai 91% dengan 15 detik. Kondisi uji tiap baris berbeda (laboratorium, rumah kaca, lapangan), sehingga angka antarbaris tidak dibandingkan langsung.

Metode pengenalan dibagi menjadi tiga kelompok: fitur tunggal, fusi multi-fitur, dan pembelajaran mendalam. Pada fitur warna, operator R-G untuk apel dan Otsu yang diperbaiki untuk stroberi, tomat, delima, dan kesemek mencapai akurasi 95%. Pengklasifikasi AdaBoost menaikkan keberhasilan deteksi anggur dari 88,33% menjadi 96,56% dibanding K-means saja. Pengenalan kiwi lewat kaliks mencapai sekitar 93,7%, sedangkan metode tekstur untuk jeruk hijau mencapai 75,3%. Pada fitur bentuk, deteksi apel berbasis geometri konveks mencapai 94%. Penulis menyatakan bahwa akurasi warna bergantung pada kematangan, varietas, latar belakang, dan cahaya, sedangkan bentuk melemah karena buah tertutup cabang dan daun.

Keterbatasan yang dinyatakan penulis mencakup tiga hal. Pertama, cara memisahkan buah saat ini membatasi keserbagunaan dan efisiensi. Kedua, waktu siklus pemetikan panjang: kiwi 17 detik, mentimun 45 detik, dan terong 1 menit. Ketiga, manipulator lunak lemah terhadap gangguan dan daya genggam rendah, meski kekakuan yang dapat diatur (*variable stiffness*) disebut naik lebih dari enam kali saat tekanan naik dari 20 kPa ke 80 kPa. Daya dorong SMA (paduan memori bentuk) dan EAP (polimer elektroaktif) juga kecil. Penulis menyarankan integrasi bahan cerdas, kekakuan yang dapat diatur, prinsip bionik, dan operasi *underactuated*.
