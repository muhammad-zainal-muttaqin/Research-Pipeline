# Automated yield prediction in vineyard using RGB images acquired by a UAV prototype platform

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `orlandi2025automated` |
| Judul asli | Automated yield prediction in vineyard using RGB images acquired by a UAV prototype platform |
| Penulis | Orlandi, Giorgia; Matese, Alessandro; Ulrici, Alessandro; Calvini, Rosalba; Berton, Andrea; Di Gennaro, Salvatore Filippo |
| Tahun | 2025 |
| Venue | Oeno One |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [orlandi2025automated.pdf](../pdf/orlandi2025automated.pdf)
- DOI resmi: https://doi.org/10.20870/oeno-one.2025.59.1.8133

## Gambaran Umum

Kajian ini mengembangkan metode cepat dan otomatis untuk memperkirakan hasil panen anggur dari citra udara pada kebun dengan kemiringan dan kondisi berbeda. Cara konvensional berupa penilaian visual atau sampling destruktif bersifat subjektif, memakan waktu, dan sering gagal menangkap keragaman spasial dalam kebun. Tujuannya adalah membangun alur kerja berbasis citra digital dari UAV yang dapat mengoreksi distorsi geometri, mendeteksi tandan, dan mengubah luas tandan menjadi estimasi hasil per pohon tanpa pelatihan supervised pada citra.

Tanaman yang dikaji adalah anggur kultivar Sangiovese. Penelitian berlangsung pada musim tanam 2021 dan 2022 di empat kebun dekat Siena, Italia, dengan luas 6.200–20.000 m², kemiringan 0% sampai 10%, dan sistem penopang Guyot atau cordon tunggal. Survei multispektral awal dengan DJI Phantom 4 Multispectral pada akhir Juli 2021 menghasilkan peta NDVI untuk memetakan zona vigour tinggi dan rendah. Setiap kebun dibagi menjadi empat petak kecil, dua di zona vigour tinggi dan dua di zona rendah; setiap petak berisi sembilan pohon berurutan, diberi empat label sian 12 × 10 cm di sudut dan label merah 10 × 10 cm pada batang pohon ke-1, ke-4, ke-7, dan ke-10. Citra RGB diambil dengan prototipe multirotor Helyx-Zero buatan khusus yang dilengkapi Raspberry Pi Zero 2W dan baterai LiPo 3S 3000 mAh, pada ketinggian terbang 5 m dengan sensor dimiringkan 45° terhadap vertikal. Pengambilan dilakukan pada 2–3 September 2021 (T1), 22–23 September 2021 (T2), dan 9 September 2022. Dari setiap petak dihasilkan tiga ROI; pada 2021 setiap sesi menghasilkan 96 citra ROI, berkurang menjadi 84 setelah dua petak di V_d terserang jamur abu-abu *Botrytis cinerea* dikeluarkan, sedangkan pada 2022 dihasilkan 36 citra ROI. Kalibrasi memakai 24 tandan terpilih di dua kebun pada 2021, dengan bobot hasil panen diukur secara destruktif.

Pengolahan citra terdiri atas tiga tahap berbasis pendekatan colourgrams di MATLAB. Tahap koreksi distorsi memakai label sian yang tersegmentasi dengan ambang relative red 0,15 dan transformasi geometri proyektif untuk mendapatkan faktor konversi Kn dalam cm² per piksel. Tahap kedua memotong citra menjadi tiga ROI memakai label merah yang tersegmentasi dengan ambang relative green 0,25. Tahap ketiga mendeteksi anggur merah matang dengan ambang relative blue 0,40, diikuti morphological closing, penutupan lubang, dan penghapusan objek di bawah 100 piksel. Jumlah piksel tandan dikalikan Kn untuk memperoleh luas tandan. Estimasi hasil dihitung dari model regresi linear antara luas tandan dari citra dan bobot tandan dari pengukuran lapang, dengan persamaan y = 2,9279x − 50,578. Validasi dilakukan terpisah dari kalibrasi, terhadap hasil panen destruktif per petak pada tiga kampanye pengamatan.

Model kalibrasi memiliki R² 0,85. Pada himpunan uji 2021, sesi T1 dan T2 masing-masing menghasilkan R² 0,85 dengan RMSE 1,29 dan 1,24 kg per tiga pohon, atau rata-rata 0,42 kg per pohon. Pada 2022, estimasi menghasilkan R² 0,89 dan RMSE 1,21 kg per tiga pohon, sekitar 0,40 kg per pohon. Pengukuran lapang menunjukkan hasil rata-rata 0,49–2,80 kg per pohon tergantung kebun dan zona vigour. Pembahasan membandingkan angka ini dengan kajian lain, antara lain Torres-Sánchez dkk. dengan R² 0,82 dan Hacking dkk. dengan R² 0,88 serta RMSE 0,44 kg per pohon.

Penulis menyatakan dua batas fisik yang tidak terhindarkan, yaitu tandan hijau dan penutup daun, karena itu kajian dibatasi pada anggur merah matang dan menerapkan defoliasi sebagian pada sisi kanopi timur laut. Ambang warna juga perlu disesuaikan dengan kondisi pencahayaan, terroir, dan cuaca setempat. Pemasangan label sian dan merah di lapang masih diperlukan untuk koreksi distorsi dan pemotongan ROI, meskipun label merah dapat dihilangkan bila jarak tanam sudah diketahui. Pengembangan berikutnya mencakup pengenalan objek lingkungan seperti tiang kebun dengan pembelajaran mesin agar tidak memasang label, validasi pada kultivar lain, penggunaan pembelajaran mesin atau deep learning untuk segmentasi piksel tandan, serta penerapan pada tanaman lain seperti apel.
