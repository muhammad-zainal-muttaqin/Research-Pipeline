# Oil palm fresh fruit bunch ripeness classification using artificial neural network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fadilah2012oil` |
| Judul asli | Oil palm fresh fruit bunch ripeness classification using artificial neural network |
| Penulis | Fadilah, Norasyikin; Saleh, Junita Mohamad; Ibrahim, Haidi; Halim, Zaini Abdul |
| Tahun | 2012 |
| Venue | Icias 2012 2012 4th International Conference on Intelligent and Advanced Systems A Conference of World Engineering Science and Technology Congress Estcon Conference Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [fadilah2012oil.pdf](../pdf/fadilah2012oil.pdf)
- DOI resmi: https://doi.org/10.1109/icias.2012.6306151

## Gambaran Umum

Makalah konferensi ini mengklasifikasikan tandan buah segar (TBS) kelapa sawit ke dalam empat kelas kematangan, yaitu belum matang (*unripe*), kurang matang (*underripe*), matang (*ripe*), dan terlalu matang (*overripe*), dengan jaringan saraf tiruan dari histogram *hue*. Penulis menyebut cara panen yang berlaku, yaitu menghitung buah lepas di tanah atau soket buah lepas di tandan, tidak akurat. Buah lepas dapat jatuh di bawah pohon lain, tersangkut di pelepah, hanyut oleh hujan, atau dimakan hewan.

Bahannya 80 TBS bahan tanam DxP Yangambi dari Felda Agricultural Services Sdn. Bhd. (FASSB). Tandan dipanen lalu langsung dikumpulkan di ruang terbuka. Seorang pengawas mutu terlatih FASSB membagi tandan ke empat kelas. Kamera warna digital diletakkan 35 cm dari tandan, dan paling banyak empat citra diambil dari bagian berbeda setiap tandan. Ukuran citra 480 × 640 piksel, RGB 24-bit. Citra dibagi acak menjadi 160 citra latih, 28 citra validasi, dan 120 citra uji independen. Pembagian dilakukan per citra, bukan per tandan, sehingga citra dari tandan yang sama dapat muncul di data latih dan data uji.

Area buah dipisahkan dari duri (*spikelet*) dengan pengelompokan K-means tiga klaster di ruang warna L*a*b*, karena ambang abu-abu biasa tidak dapat memisahkan keduanya. Piksel buah diubah ke model warna HSI, lalu histogram *hue*-nya dipakai sebagai vektor ciri. Ada 59 nilai *hue* yang mewakili warna buah. Pengklasifikasinya *multilayer perceptron* (MLP) tiga lapis dengan jumlah neuron tersembunyi 1 sampai 15. Empat kombinasi fungsi transfer (logsig atau tansig di lapis tersembunyi, logsig di keluaran) dan jumlah neuron keluaran (4 atau 2) diuji. Data validasi dipakai untuk menghentikan pelatihan, dan model terbaik dipilih menurut akurasi pada data uji.

Akurasi tertinggi adalah 86,67% untuk kombinasi CD (tansig di lapis tersembunyi, logsig dengan dua neuron keluaran). Kombinasi lain mencapai 85,83% (CA), 85,00% (CB), dan 84,17% (CC). Akurasi naik tajam setelah neuron tersembunyi kedua dan ketiga. Per kelas, akurasi tertinggi pada kelas terlalu matang dan terendah pada kelas kurang matang. Penulis menjelaskan bahwa warna tandan kurang matang dapat mendekati kelas belum matang atau matang, dan penilai manusia juga kadang salah pada kelas ini.

Kajian ini memakai 80 tandan dan penilai yang sama dengan laporan jurnal Fadilah dkk. 2012 di *Sensors* (`fadilah2012intelligent`). Laporan jurnal itu memakai 208 citra dengan pembagian 120/28/60, menambahkan reduksi ciri dengan PCA, dan melaporkan akurasi 93,33%. Karena pembagian data dan hasilnya berbeda, kedua laporan dihitung sebagai dua kajian. Pemilihan model menurut akurasi uji berarti angka 86,67% bukan perkiraan tak bias untuk data baru.
