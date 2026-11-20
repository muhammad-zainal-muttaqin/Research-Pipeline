# Perception scheme for fruits detection in trees for autonomous agricultural robot applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kadmiry2016perception` |
| Judul asli | Perception scheme for fruits detection in trees for autonomous agricultural robot applications |
| Penulis | Kadmiry, Bourhane; Chee Kit Wong |
| Tahun | 2016 |
| Venue | International Conference Image and Vision Computing New Zealand |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [kadmiry2016perception.pdf](../pdf/kadmiry2016perception.pdf)
- DOI resmi: https://doi.org/10.1109/ivcnz.2015.7761534

## Gambaran Umum

Kajian ini, ditulis oleh Kadmiry, Wong, dan Burger (2016), mengusulkan skema persepsi untuk robot pertanian otonom yang menghitung dan memetakan buah jeruk (tangerine) pada satu pohon. Robot memegang pasangan kamera RGB Basler ACE acA1300-30gc dan kamera time-of-flight (ToF) PDM CamCube 3.0 dengan sensor 200×200 piksel, rentang 0,3–7,5 m, dan 40 fps. Kedua kamera dikalibrasi memakai 30 citra papan catur, lalu jarak ToF dikoreksi dengan model polinomial.

Algoritmanya mengambil citra berurutan saat robot berputar mengelilingi pohon. Setiap buah yang terdeteksi disimpan sebagai simpul dalam graf dengan koordinat global, sehingga buah yang sama dari sudut pandang berbeda tidak dihitung dua kali. Deteksi memakai tiga metode sekaligus, yaitu deteksi blob, transformasi Hough lingkaran, dan deteksi kontur. Hasil dari ketiganya digabung agar tiap calon buah lebih andal. Pencocokan titik invarian dengan ICP memperkirakan rotasi pohon antarbingkai, dan buah yang sudah ada di graf dikenali kembali agar tidak dihitung ulang.

Di dalam ruangan, graf terbentuk 90–100% setelah satu sampai dua putaran mengelilingi pohon. Di luar ruangan, cahaya dan latar belakang yang berubah membuat deteksi lebih sulit, sehingga graf baru stabil setelah tiga sampai lima putaran, dengan jumlah simpul 75–90%. Kajian ini juga menunjukkan bahwa penyaringan warna dengan ruang HSV tetap berfungsi di luar ruangan setelah ekualisasi histogram, meski pengaturan ambang dan ukuran filter masih ditentukan secara manual.

Simpulan kajian menyebut jumlah buah yang tepat diperoleh dengan variansi sekitar 15%. Kajian tidak menyertakan tabel per pohon, sehingga jumlah pohon uji, jumlah buah sebenarnya, dan cara menghitung variansi tidak dapat ditelusuri dari teks. Penulis menyebut hasil ini bukti kelayakan; penyempurnaan parameter dan pembelajaran berbasis inferensi induktif serta penguatan masih direncanakan.
