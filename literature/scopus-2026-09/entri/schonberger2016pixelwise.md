# Pixelwise view selection for unstructured multi-view stereo

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `schonberger2016pixelwise` |
| Judul asli | Pixelwise view selection for unstructured multi-view stereo |
| Penulis | Sch\"onberger, Johannes L.; Zheng, Enliang; Frahm, Jan-Michael; Pollefeys, Marc |
| Tahun | 2016 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [schonberger2016pixelwise.pdf](../pdf/schonberger2016pixelwise.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-46487-9_31

## Gambaran Umum

Kajian ini membahas rekonstruksi padat tiga dimensi dari kumpulan citra tak terstruktur, yaitu citra yang diambil dari sudut dan kondisi pencahayaan yang tidak diatur. Masalah utamanya adalah memperoleh model padat yang akurat, lengkap, dan efisien dari citra semacam itu. Pada metode *Multi-View Stereo* (MVS) terdahulu, pemilihan citra sumber sering dilakukan secara heuristik. Misalnya, sebagian metode memilih kluster kamera lebih dahulu lalu hanya memakai beberapa citra terbaik per piksel. Pilihan semacam ini dapat menurunkan kelengkapan dan ketelitian hasil. Penulis mengusulkan *pixelwise view selection*, yaitu pemilihan citra sumber untuk setiap piksel dengan memanfaatkan prior fotometrik dan geometrik.

Pengujian memakai beberapa set data. Pengujian komponen menggunakan *South Building* yang berisi 128 citra beresolusi 7 MP, dengan 127 citra sumber untuk setiap citra referensi. Tolok ukur Middlebury memakai model Dino dan Temple yang ditangkap pada 640x480 dengan variasi Full, Ring, dan Sparse. Model Full memuat sekitar 300 citra. Tolok ukur Strecha memakai citra beresolusi tinggi dengan *ground truth*, yaitu model Fountain dan Herzjesu. Set data terakhir adalah 100 juta foto Internet dari Heinly dan rekan, dan penulis memproses 41 ribu citra dari set tersebut. Seluruh komputasi memakai implementasi CUDA pada GPU Nvidia Titan X. Untuk set foto Internet, penulis memakai satu mesin dengan 4 GPU Titan X.

Metode ini memperluas kerangka optimasi Zheng dan rekan dengan beberapa kontribusi. Kontribusinya meliputi estimasi normal per piksel di dalam skema sampling *PatchMatch*, prior geometrik berdasarkan sudut triangulasi, sudut datang, dan resolusi citra, suku kehalusan temporal untuk variabel oklusi, serta suku konsistensi geometrik multi-tampilan. Pada Strecha Fountain, akurasi pada ambang 2 cm naik dari 0,769 menjadi 0,827, dan pada ambang 10 cm naik dari 0,929 menjadi 0,975. Pada Herzjesu, akurasi pada ambang 2 cm naik dari 0,650 menjadi 0,691, dan pada ambang 10 cm naik dari 0,844 menjadi 0,931. Pada Middlebury, metode ini berada di peringkat 1 untuk Dino Full (seri) dan Dino Sparse. Untuk Temple, peringkatnya 4 pada Full dan 8 pada Ring. Pada set foto Internet, pemrosesan memerlukan sekitar 70 detik per tampilan dan 4,2 hari, setelah 6 hari untuk *Structure-from-Motion* (SfM) awal.

Penulis mencatat beberapa batasan. Metode bekerja paling baik pada resolusi tinggi karena estimasi normal membutuhkan ukuran *patch* yang besar. Pada Temple, hasilnya tidak selalu menempati peringkat teratas. Pada set foto Internet, batas memori GPU tercapai sekitar 200 citra, sehingga penulis hanya memilih citra sumber yang paling terhubung berdasarkan jumlah titik jarang yang sama. Penulis juga menyebut bahwa setiap komponen penting untuk mencapai akurasi dan kelengkapan keseluruhan, sehingga manfaat metode bergantung pada kombinasi komponen tersebut.
