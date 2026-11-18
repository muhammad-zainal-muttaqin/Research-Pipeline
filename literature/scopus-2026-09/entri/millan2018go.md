# On-the-go grapevine yield estimation using image analysis and boolean model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `millan2018go` |
| Judul asli | On-the-go grapevine yield estimation using image analysis and boolean model |
| Penulis | Millan, Borja; Velasco-Forero, Santiago; Aquino, Arturo; Tardaguila, Javier |
| Tahun | 2018 |
| Venue | Journal of Sensors |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [millan2018go.pdf](../pdf/millan2018go.pdf)
- DOI resmi: https://doi.org/10.1155/2018/9634752

## Gambaran Umum

Penelitian ini bertujuan memperkirakan hasil panen anggur secara noninvasif, objektif, dan otomatis dari citra dengan memakai model Boolean. Penulis menyatakan segmentasi citra lapang terganggu oleh okklusi antarbuah maupun oleh organ tanaman lain, sehingga kualitas hasil menurun. Model Boolean dipilih karena dapat memperkirakan jumlah partikel dalam citra meskipun terjadi kesalahan segmentasi atau okklusi. Penulis menyatakan model ini belum pernah dipakai di pertanian untuk pendugaan buah dan hasil. Pendekatan ini diuji pada tiga keadaan: citra tandan, citra tanaman yang diambil manual, dan citra tanaman yang diambil secara *on-the-go* memakai kendaraan quad.

Kajian berlangsung pada September 2014 dan 2015 di kebun anggur komersial di Falces, Navarra, Spanyol, pada ketinggian 325 m. Pohon berupa *Vitis vinifera* dengan sistem teralis *vertical shoot positioning*, baris berarah utara–selatan, jarak 2 × 1 m, dan enam daun basal pertama dibuang manual setelah pembentukan buah. Tiga himpunan data dipakai. Pertama, 45 citra tandan dari empat varietas (Cabernet Sauvignon, Garnacha, Syrah, Tempranillo) diambil dengan kamera Nikon D5300 dan lensa makro Sigma 50 mm F2.8 pada latar kardus oranye, resolusi 6000 × 4000 piksel, 8 bit per kanal. Kedua, 45 citra tanaman dari empat varietas (Cabernet Sauvignon, Garnacha, Syrah, Touriga Nacional) dengan lensa Nikon 18–55 mm, latar panel putih, dan tripod pada jarak sekitar 120 cm. Ketiga, 64 citra tanaman dari tiga varietas (Cabernet Sauvignon, Syrah, Tempranillo) diambil pada malam 9 September 2015 memakai quad Trail Boss 330 yang melaju sekitar 7 km/jam, kamera Sony alpha 7-II dengan lensa 24–70 mm, penerangan panel LED 900 dan dua lampu LED Travor, serta pemicu kamera berbasis Arduino MEGA dan sensor induktif yang menghasilkan tumpang tindih sekitar 40%. Citra ketiga digabung manual menjadi 28 bagian yang masing-masing memuat tiga pohon. Acuan hitung berupa buah yang dipetik dihitung dan ditimbang, serta pohon atau bagian tiga pohon yang dipanen lalu ditimbang.

Model Boolean menghitung jumlah objek dalam daerah kajian sebagai −a_z/(a′ log q), dengan a_z luas daerah kajian, a′ luas rata-rata objek, dan q porositas yang didefinisikan sebagai (piksel daerah kajian − piksel daerah tersegmentasi)/piksel daerah kajian. Daerah kajian diperoleh otomatis dengan operasi morfologi *opening* memakai kernel lingkaran berjari-jari sama dengan ukuran buah rata-rata. Pembandingnya adalah penduga naif berupa piksel tandan tersegmentasi dibagi piksel luas buah rata-rata. Segmentasi tandan memakai klasifikasi jarak Mahalanobis atas vektor enam dimensi dari RGB dan HSV, dengan komponen H diubah agar warna biru berada di tengah rentang; jarak diubah menjadi peta probabilitas keanggotaan memakai distribusi Boltzmann dengan kT = 10. Jumlah kelas tiga untuk citra tandan dan enam untuk citra tanaman. Pada citra *on-the-go*, peta probabilitas warna dikalikan dengan tiga peta tambahan, yaitu kedekatan tandan, bentuk kabel, dan zona kemunculan linear, untuk mengurangi salah klasifikasi antara tandan dan kawat penopang. Jari-jari buah rata-rata diukur manual pada citra tandan dan ditetapkan per varietas untuk citra tanaman.

Pengujian sintetis dengan 100 simulasi per keadaan menunjukkan kesalahan penduga naif sebesar 1,7% dan 2,3% untuk 50 partikel, tetapi naik menjadi 24,9% dan 25,1% untuk 500 partikel, sedangkan model Boolean berturut-turut 2,4%, 2,7%, 2,1%, dan 2,1%. Pada 45 citra tandan, model Boolean menghasilkan RMSE 20,1 buah dan R² = 0,80 dengan kemiringan regresi 0,93, sedangkan penduga naif menghasilkan RMSE 60 buah dan R² = 0,71. Pada 45 citra tanaman hasil pengambilan manual, model Boolean menghasilkan RMSE 310,2 g dan R² = 0,81, sedangkan penduga naif menghasilkan RMSE 777,2 g dan R² = 0,82. Pada 28 bagian citra *on-the-go* yang masing-masing memuat tiga pohon, model Boolean menghasilkan RMSE 610,1 g dan R² = 0,78, dengan kesalahan 15,6%, sedangkan penduga naif menghasilkan RMSE 2472 g dan R² = 0,71. Penilaian segmentasi citra *on-the-go* terhadap topeng buatan manual menunjukkan *recall* 0,58 dan *precision* 0,71 tanpa penyaringan, menjadi 0,56 dan 0,79 setelah penyaringan.

Penulis menyatakan kesalahan segmentasi masih terjadi, antara lain bagian batang yang terklasifikasi sebagai tandan serta tumpang tindih kelas antara tandan dan kawat logam. Nilai *recall* yang rendah pada citra *on-the-go* dikaitkan dengan pencahayaan yang tidak seragam, dan penulis menyatakan perbaikan pencahayaan dapat meningkatkannya. Model Boolean menunjukkan hasil yang lebih seragam antarvarietas, tetapi penulis menyatakan diperlukan kajian lebih luas untuk membuktikan kemampuan generalisasinya. Penulis juga menyatakan data citra dan pengukuran lapang belum tersedia karena lembaga mereka sedang menyusun protokol berbagi data.

