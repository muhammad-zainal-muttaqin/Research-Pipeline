# Multi-vision-based Localization and Pose Estimation of Occluded Apple Fruits for Harvesting Robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022multi` |
| Judul asli | Multi-vision-based Localization and Pose Estimation of Occluded Apple Fruits for Harvesting Robots |
| Penulis | Li, Tao; Xie, Feng; Feng, Qingchun; Qiu, Quan |
| Tahun | 2022 |
| Venue | Proceedings 2022 37th Youth Academic Annual Conference of Chinese Association of Automation Yac 2022 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [li2022multi.pdf](../pdf/li2022multi.pdf)
- DOI resmi: https://doi.org/10.1109/yac57282.2022.10023577

## Gambaran Umum

Penulis menangani masalah memosisikan dan menentukan pose cengkeram apel yang tertutup bagi robot pemanen. Mereka menyebut sekitar 62% apel pada 100 pohon kerdil padat yang mereka hitung pada musim panen tertutup sebagian. Kamera stereo juga memiliki tingkat pengisian (*filling rate*) kurang dan derau, sehingga titik pusat bagian buah yang terlihat meleset dari titik pusat buah utuh.

Data pelatihan ada dua. Pertama, set MinneApple terbuka berisi 1.000 citra dengan lebih dari 41 ribu apel berlabel. Kedua, set kumpulan sendiri dari dua kebun di Haidian dan Changping, Beijing, direkam dengan kamera RGB-D RealSense D435i: 1.000 citra dengan lebih dari 12 ribu instans berlabel berikut kotak pembatas, dengan oklusi oleh daun, cabang, dan buah lain. Pemberi label tidak disebut. Set latih dan validasi dibagi 4:1; set uji terpisah tidak disebut.

Metodenya jaringan konvolusi multitugas (*multi-task*) yang sekaligus mendeteksi kotak pembatas utuh buah dan menyegmentasi bagian yang terlihat. Dari hasil itu dibentuk frustum 3D (volume pandang dari kotak 2D) untuk menaksir titik pusat bagian terlihat, lalu bentuk buah direkonstruksi. Dua kamera stereo pada robot, dekat dan jauh, menghasilkan estimasi masing-masing. Keduanya digabung dengan bobot (λa = 0,7 untuk kamera dekat, λb = 0,3) menjadi satu titik pusat dan satu pose cengkeram per buah.

Pada evaluasi jaringan, pelatihan ujung ke ujung memberi *recall* 74,4%, AP 67,3%, akurasi 92,0%, dan IoU 71,0%. Model multitugas berjalan 35,1 ms, sedangkan deteksi saja mencapai AP 71,2% (27,6 ms) dan segmentasi saja IoU 75,9% (25,7 ms). Lokalisasi dievaluasi pada 50 pasang bingkai RGB-D, dan pose pada 50 percobaan cengkeram di 10 tanaman apel. Tabel III memuat galat median titik pusat sekitar 5,73 mm, 8,25 mm, dan 6,43 mm untuk tiga konfigurasi; kolom mana milik metode penulis tidak dapat dipastikan dari teks terekstrak (belum diperiksa pada PDF).

Keterbatasan: tidak ada pencacahan buah dan tidak ada tautan identitas buah antarpandang; dua kamera dipakai untuk menaksir satu buah target. Acuan galat posisi tidak dijelaskan dengan rinci. Teks tidak menyebut hasil keberhasilan cengkeram dalam angka. Hanya apel di dua kebun yang diuji.
