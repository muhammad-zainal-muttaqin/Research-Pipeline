# Overlapped apple fruit yield estimation using pixel classification and hough transform

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kanwal2019overlapped` |
| Judul asli | Overlapped apple fruit yield estimation using pixel classification and hough transform |
| Penulis | Kanwal, Zartash; Basit, Abdul; Jawad, Muhammad; Ullah, Ihsan; Ali, Anwar |
| Tahun | 2019 |
| Venue | International Journal of Advanced Computer Science and Applications |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [kanwal2019overlapped.pdf](../pdf/kanwal2019overlapped.pdf)
- DOI resmi: https://doi.org/10.14569/ijacsa.2019.0100271

## Gambaran Umum

Penelitian ini bertujuan menghitung buah apel yang saling tumpang tindih di kebun luar ruang dengan metode visual yang cepat dan tanpa pembelajaran mesin. Penulis menyebutkan bahwa perkiraan hasil buah konvensional memakai data historis, kondisi cuaca, dan sampel manual sehingga memakan waktu, memerlukan banyak tenaga kerja, dan kurang akurat. Tantangan penglihatan mesin di kebun meliputi perubahan pencahayaan, variasi warna, buah yang bertumpukan, latar yang berantakan, serta naungan daun dan cabang. Penulis mengusulkan kombinasi klasifikasi piksel untuk segmentasi warna dan analisis kelengkungan memakai *Hough circle transform* agar buah yang bertumpukan dapat dihitung satu per satu.

Materi pengujian berupa 36 citra apel dari kebun yang berbeda dengan pencahayaan, warna, dan latar yang beragam, termasuk buah yang saling menutupi. Varietas, lokasi kebun, dan spesifikasi kamera tidak dinyatakan. Pengujian dibagi dua: percobaan I menampilkan hasil kualitatif pada dua himpunan citra, dan percobaan II memakai video kebun apel dengan lima frame serta acuan hitung berupa 46 buah yang dihitung manual. Penulis tidak melaporkan pembagian data latih dan data uji.

Alur metode dimulai dari pembacaan citra RGB dan perataan Gauss untuk menekan derau, lalu konversi ke ruang warna HSV. Komponen V dibuang karena sensitif terhadap perubahan cahaya, sehingga pengolahan berjalan pada citra HS. Ambang warna dengan batas bawah (0, 23, 30) dan batas atas (23, 255, 255) diterapkan untuk memisahkan daerah apel dari daun, cabang, dan batang, menghasilkan citra biner yang dipakai sebagai mask. Operator morfologi *erode* menghilangkan gumpalan derau kecil, diikuti *dilate* untuk menutup gumpalan yang terbuka akibat okklusi; perataan Gauss diulang sebelum *Hough circle transform* mencari pusat lingkaran dengan pemungutan suara dalam ruang parameter x₀ = x − r cos θ dan y₀ = y − r sin θ pada rentang jari-jari tertentu. Jumlah pusat lingkaran yang terdeteksi menjadi jumlah apel; penulis menyatakan metode ini dapat berjalan langsung pada kendaraan darat atau udara kecil.

Pada percobaan I, tiga frame pertama berturut-turut memuat 5, 10, dan 6 buah; metode menghitung benar 5, 9, dan 5 buah. Dua frame dari aliran video memuat 13 dan 12 buah; metode menghitung benar 12 dan 12 buah. Pada percobaan II, dari 46 buah pada lima frame, metode yang diusulkan mendeteksi 43 buah dengan tingkat *true positive* 93,48%, sedangkan metode berbasis kontur yang dijadikan pembanding hanya mendeteksi 19 buah dengan tingkat 41,31%. Tingkat *false positive* metode yang diusulkan sebesar 4,35% dan metode pembanding 2,17%. Penulis menyatakan analisis kelengkungan menghasilkan lebih banyak lingkaran salah, sedangkan metode kontur menggabungkan empat buah yang bertumpukan menjadi satu. Batasan yang dinyatakan penulis mencakup ketidakmampuan mengenali apel yang terlalu jauh dan kecil karena rentang parameter jari-jari, ketergantungan pada model warna yang harus dilatih ulang untuk buah bulat lain, serta perlunya metode estimasi kelengkungan yang lebih tepat dan perbandingan dengan metode pembelajaran mendalam pada pekerjaan berikutnya.

