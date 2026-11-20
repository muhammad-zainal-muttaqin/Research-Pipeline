# A Feasibility Study on Synthetic RGB-NIR Image Generation for Oil Palm Fresh Fruit Bunch Grading

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `suriani2026feasibility` |
| Judul asli | A Feasibility Study on Synthetic RGB-NIR Image Generation for Oil Palm Fresh Fruit Bunch Grading |
| Penulis | Suriani, Nor Surayahani; Mohd, Norzali Hj; Shah, Shaharil Mohd; Muji, Siti Zarina; Rashid, Fadilla Atyka Nor |
| Tahun | 2026 |
| Venue | International Journal of Advanced Computer Science and Applications |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [suriani2026feasibility.pdf](../pdf/suriani2026feasibility.pdf)
- DOI resmi: https://doi.org/10.14569/ijacsa.2026.0170272

## Gambaran Umum

Kajian ini menguji kelayakan pembangkitan citra near-infrared (NIR) sintetis dari citra RGB untuk penilaian kematangan tandan buah segar (TBS) kelapa sawit. Pencitraan NIR memberi petunjuk spektral yang sensitif terhadap kandungan air, struktur sel, dan akumulasi minyak, tetapi pemakaiannya di lapangan terkendala oleh biaya sensor, kompleksitas sistem, serta langkanya dataset RGB-NIR berpasangan. Penulis mengusulkan alternatif berupa model terjemahan citra berbasis U-Net yang menghasilkan representasi menyerupai NIR dari RGB, lalu menggabungkannya dengan kanal RGB untuk klasifikasi. Tujuan kajian adalah menilai apakah NIR sintetis meningkatkan akurasi tanpa menambah perangkat keras pencitraan, bukan menghasilkan standar grading baru atau mereproduksi pengukuran NIR sejati.

Tanaman yang dikaji adalah kelapa sawit. Data berupa 3.476 citra RGB yang diperoleh dari Pertubuhan Peladang Parit Raja di bawah kondisi luar ruangan alami. Pengambilan memakai kamera digital standar tanpa sensor NIR atau multispektral, dalam beberapa sesi panen untuk menangkap variasi pencahayaan, latar, orientasi tandan, dan okklusi. Setiap citra memuat satu TBS dan diberi label manual ke dalam empat kelas: *underripe*, *unripe*, *ripe*, dan *overripe*, dengan acuan kebenaran dari petani berpengalaman sesuai pedoman panen. Citra diubah ke resolusi tetap, intensitas piksel dinormalisasi, lalu dibagi secara berlapis menjadi data latih, validasi, dan uji. Rasio pembagian dan jumlah citra pada cawat uji tidak dinyatakan.

Mekanisme pembangkitan memakai U-Net dengan arsitektur encoder–decoder dan skip connection yang menerima citra RGB tiga kanal serta menghasilkan satu kanal NIR sintetis. Karena tidak ada citra NIR sejati, U-Net dilatih secara self-supervised dan dipandu prior, bukan dengan supervisi piksel-demi-piksel. Pelatihannya memakai batasan konsistensi rekonstruksi, regularisasi kehalusan, dan objektif pelestarian tepi agar representasi yang dihasilkan tetap koheren secara spasial dan tidak menimbulkan artefak. Prior spektral dari hubungan hiperspektral ke RGB/NIR disisipkan secara implisit untuk menekankan karakteristik pantulan yang berkaitan dengan kematangan, seperti homogenitas tekstur dan variasi intensitas. NIR sintetis kemudian dikonkatenasi dengan RGB menjadi masukan empat kanal. Lima model klasifikasi diuji dengan partisi, praproses, dan hyperparameters identik: CNN kustom, ResNet50, EfficientNet-B0, DenseNet-201, dan MobileNetV3.

Evaluasi memakai akurasi, presisi, *recall*, dan F1-score, dengan F1 makro sebagai metrik utama karena lebih tahan terhadap ketimpangan kelas dan lebih sensitif pada kategori kematangan yang ambigu. Semua model mengalami kenaikan kinerja saat NIR sintetis ditambahkan. Pada konfigurasi RGB saja, akurasi berturut-turut adalah CNN 75,8 persen, ResNet50 77,5 persen, EfficientNet-B0 85,3 persen, DenseNet-201 82,1 persen, dan MobileNetV3 80,3 persen; F1 makronya 70,1; 75,3; 80,5; 80,1; dan 82,5 persen. Pada konfigurasi RGB + NIR sintetis, akurasi menjadi 78,5; 78,1; 90,3; 85,4; dan 82,9 persen, dengan F1 makro 74,0; 75,7; 84,6; 80,9; dan 85,4 persen. EfficientNet-B0 mencatat akurasi tertinggi 90,3 persen, sedangkan MobileNetV3 mencatat F1 makro tertinggi 85,4 persen. Pada EfficientNet-B0, F1 per kelas untuk *unripe*, *underripe*, *ripe*, dan *overripe* adalah 95,65; 66,67; 94,12; dan 81,82 persen. Pada MobileNetV3, nilai yang sama adalah 91,67; 100; 83,33; dan 66,67 persen. Matriks kebingungan menunjukkan EfficientNet-B0 lebih tangguh pada tahap akhir kematangan, sedangkan MobileNetV3 lebih baik pada tahap awal.

Penulis menyatakan dua batasan utama. Tidak ada kebenaran NIR sejati, sehingga akurasi fisik citra sintetis tidak dapat divalidasi langsung; seluruh kesimpulan bertumpu pada kinerja klasifikasi hilir, bukan pada fidelitas spektral. Ketimpangan kelas dan ukuran sampel yang terbatas dapat memengaruhi variabilitas antarkelas, khususnya *underripe* dan *overripe*. Penulis menilai perbaikan F1 makro yang konsisten di berbagai arsitektur menunjukkan perolehan yang sistematis, bukan kebetulan, dan menyatakan validasi NIR sintetis terhadap informasi spektral serta penggunaan model generatif yang lebih canggih sebagai pekerjaan berikutnya.
