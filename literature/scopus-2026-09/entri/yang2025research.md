# Research progress on binocular stereo vision technology and its applications in smart agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2025research` |
| Judul asli | Research progress on binocular stereo vision technology and its applications in smart agriculture |
| Penulis | Yang, X.; others |
| Tahun | 2025 |
| Venue | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [yang2025research.pdf](../pdf/yang2025research.pdf)
- DOI resmi: https://doi.org/10.11975/j.issn.1002-6819.202410177

## Gambaran Umum

Yang dkk. (2025) menulis tinjauan tentang teknik penglihatan stereo binokular (*binocular stereo vision*) dan penerapannya dalam pertanian cerdas. Teknik ini memakai dua kamera yang telah dikalibrasi untuk memperoleh kedalaman dan awan titik 3D dari suatu adegan. Penulis menyebut tiga masalah yang ditinjau: penentuan posisi 3D buah untuk pemetikan dan navigasi kebun, pengukuran parameter pertumbuhan tanaman, serta pengenalan penyakit dan penyemprotan. Penulis juga membahas alur teknisnya, yaitu kalibrasi kamera, koreksi epipolar, dan pencocokan stereo.

Cakupan tinjauan dijelaskan terbatas. Pencarian dilakukan pada Oktober 2024 di China National Knowledge Infrastructure (CNKI), Wanfang, Web of Science, EI (*Engineering Village*), dan Elsevier ScienceDirect. Kata kunci teknis adalah "binocular vision", "stereo vision", dan "binocular stereo vision". Kata kunci aplikasi adalah lokasi, pemetikan, pengukuran, dan hama atau penyakit. Periode yang disaring adalah 2004 sampai 2024 pada bidang rekayasa pertanian. Jumlah kajian yang masuk tidak disebut; daftar pustaka memuat 113 rujukan.

Isi tinjauan terbagi menjadi alur teknis dan penerapan. Alur teknis mencakup kalibrasi, koreksi epipolar, dan pencocokan stereo, yaitu mencari titik yang sama pada citra kiri dan kanan untuk menghitung selisih posisi (*disparity*). Pencocokan dibagi menjadi cara berbasis fitur dan cara berbasis pembelajaran mendalam. Pada pemetikan, penulis membedakan dua pola. Pola pertama menyegmentasi buah lebih dulu menjadi daerah minat (*region of interest*, ROI) lalu menghitung *disparity* hanya di ROI. Pola kedua mendeteksi buah dan menghitung *disparity* bersamaan, lalu menggabungkan keduanya.

Hasil yang dikutip dari kajian lain berupa galat lokalisasi, bukan hitungan buah. Dengan YOLOv3 pada citra kiri, nanas pada jarak 1,7 sampai 2,7 m mendapat galat absolut rerata 24,414 mm dan galat relatif rerata 1,17% (Liu dkk.). Pada jeruk berjarak 200 sampai 500 mm, galat absolut rerata titik petik adalah 8,63 mm dan galat relatif rerata 2,76% (Hou dkk.). Untuk stroberi, galat gabungan sumbu X, Y, dan Z adalah 3,1 mm dengan YOLOv3 dan 3,9 mm dengan Mask R-CNN (Hu dkk.). Pada jeruk berjarak 1,5 m, galat dalam rentang minus 20 sampai 20 mm mencapai 82,5% pada cahaya rendah atau normal dan 72% pada cahaya kuat (Bao dkk.).

Penulis menyebut empat keterbatasan teknik ini. Keseimbangan antara kecepatan dan ketelitian sulit dicapai. Sebagian besar penerapan diuji di lingkungan percobaan atau cuaca cerah. Set data stereo berlabel yang besar dan terbuka tidak tersedia. Pencocokan stereo tidak punya standar evaluasi yang seragam, sehingga algoritme sulit dibandingkan. Dari teks tinjauan ini, tidak ada bagian yang membahas penghitungan buah, identitas buah lintas pandang, atau kelapa sawit. Tinjauan ini tidak menggabungkan angka antarkajian dan tidak menilai mutu kajian yang dimasukkan.
