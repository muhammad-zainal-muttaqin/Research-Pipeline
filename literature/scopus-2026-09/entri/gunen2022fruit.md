# Fruit Detection from Apple Orchard Using Point Cloud Data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gunen2022fruit` |
| Judul asli | Fruit Detection from Apple Orchard Using Point Cloud Data |
| Penulis | G\"unen, Mehmet Akif |
| Tahun | 2022 |
| Venue | El Cezeri Journal of Science and Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gunen2022fruit.pdf](../pdf/gunen2022fruit.pdf)
- DOI resmi: https://doi.org/10.31202/ecjse.962269

## Gambaran Umum

Penelitian ini mengatasi penentuan posisi spasial buah apel untuk pemantauan kesehatan, pemanenan otomatis, dan perkiraan hasil panen. Penulis mencatat bahwa kebun memiliki geometri kompleks sehingga solusi pertanian presisi lebih sulit diterapkan daripada pada tanaman semusim. Sebagian besar kajian deteksi buah bertumpu pada analisis citra, yang terhalang pencahayaan kompleks dan kondisi lingkungan berubah. Pendekatan berbasis citra juga memerlukan ambang batas yang ditentukan pengguna dan tidak menghasilkan posisi tiga dimensi, sedangkan pendekatan pembelajaran dalam memerlukan perangkat keras berkapasitas tinggi dan berjalan relatif lambat. Penulis mengusulkan kerangka kerja baru berbasis awan titik tiga dimensi hasil fotogrametri untuk menemukan posisi apel Fuji.

Data berasal dari himpunan apel Fuji (*Malus domestica* Borkh. cv. Fuji) yang dibuat Mola dkk. dengan fotogrametri *structure from motion*. Himpunan ini memuat 582 citra mentah dari berbagai sudut pandang dan lintasan serta awan titik tiga dimensi dari 11 pohon apel. Awan titik telah tergeoreferensi, disimpan dalam format .txt, dan diberi warna 8 bit pada rentang 0–255. Data referensi diberi label manual dengan perangkat lunak Cloud Compare. Seluruh himpunan terdiri atas 1.455 apel, dengan 3 pohon untuk latih (433 apel) dan 8 pohon untuk uji (1.022 apel). Karena pengolahan awan titik memerlukan beban dan biaya besar, himpunan latih yang diambil contohnya dibagi lagi menjadi sekitar 30% uji dan 70% latih. Penelitian ini hanya memakai data awan titik tiga dimensi; fitur warna tidak dipakai karena sangat bergantung pada kondisi pencahayaan dan pengaruh atmosfer.

Mekanisme kerangka kerja terdiri atas empat tahap. Pertama, jumlah tetangga terdekat optimal ditentukan secara adaptif untuk setiap titik memakai metrik omnivarian; penulis mencari k tetangga dari 100 hingga 3.500 dengan langkah 50, sehingga terdapat 69 kemungkinan jumlah tetangga, lalu memilih yang memberikan nilai omnivarian optimum. Kedua, dari tetangga terpilih diekstrak 30 fitur geometris dua dan tiga dimensi per titik (9 fitur 2D dan 21 fitur 3D) berdasarkan matriks kovarians dan nilai eigen, mencakup linearitas, kebidatan, kesferisan, omnivarian, anisotropi, entropi, jumlah nilai eigen, perubahan kelengkungan, nilai Z, jari-jari tetangga terdekat, kerapatan, dan vertikalitas. Ketiga, seleksi fitur memakai metode *minimum redundancy maximum relevance* (mRMR) untuk memilih fitur dengan redundansi terendah dan relevansi tertinggi terhadap label; fitur diurutkan berdasarkan bobot sehingga terbentuk enam himpunan fitur berisi 5, 10, 15, 20, 25, dan 30 fitur teratas. Keempat, klasifikasi memakai *support vector machine* dengan fungsi inti radial, parameter penalti C = 25, dan lebar inti 0,1. Seluruh pengolahan dijalankan dengan Matlab 2021a pada stasiun kerja Windows 7, GPU Quadro K5000 dan Tesla K20, prosesor 2,50 GHz, serta RAM 64 GB.

Metrik evaluasi dihitung dari matriks kebingungan dan mencakup akurasi, presisi, sensitivitas atau recall, spesifisitas, skor-F, dan G-mean. Akurasi untuk himpunan 5, 10, 15, 20, 25, dan 30 fitur berturut-turut 0,8925; 0,9300; 0,9485; 0,9566; 0,9581; dan 0,8027, sedangkan presisi berturut-turut 0,7340; 0,8642; 0,9002; 0,9258; 0,9320; dan 0,3343. Himpunan 25 fitur memberi kinerja tertinggi dengan akurasi 95,81% dan presisi 93,20%, disusul skor-F 0,7898, recall 0,6852, spesifisitas 0,9935, dan G-mean 0,8251. Himpunan 5 fitur memiliki akurasi tinggi tetapi recall sangat rendah (0,1004), sedangkan himpunan 30 fitur menurunkan akurasi dan presisi meski recall naik menjadi 0,7234; penulis mengaitkan hal ini dengan jumlah contoh kelas apel yang lebih sedikit daripada kelas lainnya. Uji McNemar pada taraf signifikansi 5% menolak hipotesis nol bahwa kedua himpunan fitur memiliki kinerja sama (p = 1,2218 × 10⁻¹¹³), sehingga perbedaan antarhimpunan dinyatakan signifikan secara statistik. Penulis juga menyatakan fitur dua dimensi sama pentingnya dengan fitur tiga dimensi.

Batasan yang dinyatakan penulis mencakup kebutuhan akan stasiun kerja berkapasitas tinggi untuk menjalankan proses dan ketidakmungkinan melakukan pemanenan robotik waktu nyata dengan awan titik hasil *structure from motion* pada kondisi teknologi saat ini. Penggunaan seluruh 30 fitur justru menurunkan kinerja karena data yang kurang representatif dan model menjadi lebih kompleks. Penulis tidak memakai informasi warna, sehingga pendekatan ini bergantung pada geometri semata. Penelitian lanjutan yang diusulkan adalah membandingkan berbagai pengklasifikasi untuk menentukan ukuran apel; potensi penentuan berat buah dari ukurannya disebutkan belum diuji.
