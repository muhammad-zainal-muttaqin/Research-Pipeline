# Intelligent color vision system for ripeness classification of oil palm fresh fruit bunch

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fadilah2012intelligent` |
| Judul asli | Intelligent color vision system for ripeness classification of oil palm fresh fruit bunch |
| Penulis | Fadilah, Norasyikin; Mohamad-Saleh, Junita; Abdul Halim, Zaini; Ibrahim, Haidi; Syed Ali, Syed Salim |
| Tahun | 2012 |
| Venue | Sensors Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [fadilah2012intelligent.pdf](../pdf/fadilah2012intelligent.pdf)
- DOI resmi: https://doi.org/10.3390/s121014179

## Gambaran Umum

Penelitian ini bertujuan membangun algoritma klasifikasi kematangan tandan buah segar (TBS) kelapa sawit secara otomatis berdasarkan penglihatan warna dalam kondisi cahaya alami. Kematangan saat panen menentukan jumlah minyak yang dihasilkan. Cara petani mengamati buah lepas di tanah atau soket buah di tandan dianggap tidak akurat karena buah dapat jatuh di bawah pohon lain, tersangkut pelepah, hanyut saat hujan, atau dimakan hewan; caranya juga memakan waktu dan tenaga. Penulis juga menyatakan penilaian warna oleh manusia bersifat subjektif dan rawan salah. Kajian sebelumnya menunjukkan komponen merah saja tidak cukup membedakan kelas belum matang dan matang, sedangkan nilai *hue* lebih kebal terhadap perubahan intensitas cahaya. Tujuan khususnya adalah menguji reduksi data dengan *principal component analysis* (PCA) dan memakai jaringan saraf tiruan sebagai sistem klasifikasi.

Bahan berupa 80 TBS tipe DxP Yangambi dari Felda Agricultural Services Sdn. Bhd. (FASSB). Jumlahnya sama untuk setiap kelas kematangan. Seorang pengawas mutu terlatih FASSB membagi tandan menjadi empat kelas, yaitu belum matang (*unripe*), kurang matang (*underripe*), matang (*ripe*), dan terlalu matang (*overripe*); TBS busuk, kosong, dan terinfeksi dibuang. Paling banyak empat citra diambil dari bagian berbeda pada setiap tandan, sehingga terkumpul 208 citra berukuran 480 × 640 piksel dalam format RGB 24-bit. Kamera yang dipakai adalah Vivotek IP8332 Network Bullet Camera (0 Lux, 1,0 megapiksel, F1.8) yang dipilih karena mampu menyesuaikan pencahayaan luar ruangan. Citra diproses dengan Matlab Image Processing Toolbox dan Neural Network Toolbox. Data dibagi secara acak menjadi 120 citra latih, 28 citra validasi, dan 60 citra uji independen; penulis menyatakan jumlah uji dibatasi 60 karena ketersediaan TBS terbatas.

Mekanisme deteksi terdiri dari tiga tahap. Citra RGB dikonversi ke ruang warna L*a*b*, lalu dikelompokkan dengan K-means menjadi tiga klaster untuk memisahkan area buah dari area spikelet. Lima nilai rata-rata warna pembeda dijadikan penanda; setiap piksel diberi kelas berdasarkan jarak Euclidean terkecil, sehingga terbentuk topeng biner dengan buah berlabel 1 dan spikelet berlabel 0. Selanjutnya, piksel buah diubah ke model warna HSI dan dihitung nilai *hue*-nya. Histogram *hue* berisi 100 bin menjadi vektor ciri, tetapi hanya 59 bin yang mewakili warna buah yang dipakai sebagai masukan. Klasifikasinya memakai jaringan *multilayer perceptron* (MLP) tiga lapis dengan 15 neuron tersembunyi yang ditentukan secara eksperimen. Enam kombinasi fungsi transfer diuji, yaitu logsig, tansig, dan purelin, dengan satu, dua, atau empat neuron keluaran serta skema pengkodean kelas yang berbeda. Dua strategi dibandingkan: metode MA memakai seluruh 59 fitur, sedangkan metode MB memakai PCA untuk menghilangkan komponen yang saling berkorelasi dan menyisakan sejumlah komponen utama. Akurasi dihitung sebagai persentase klasifikasi benar terhadap jumlah data uji; data validasi dipakai untuk menghentikan pelatihan ketika kinerja tidak membaik lagi.

Pada metode MA, kombinasi CC dengan fungsi logsig pada lapis tersembunyi dan keluaran serta empat neuron keluaran memberi akurasi tertinggi 91,67%; kombinasi lain berkisar 85,00–90,00%. Pada metode MB, kombinasi CC dengan lima komponen utama awalnya memberi 91,67%. Penulis mendapati akurasi turun di bawah 70% ketika jumlah komponen terlalu banyak, misalnya 55 komponen, karena korelasi data mengganggu pembelajaran, serta juga turun ketika hanya dua komponen karena informasi tidak cukup. Pencarian lanjutan pada kisaran 5–15 komponen menunjukkan kombinasi CD dengan enam dan dua belas komponen utama mencapai akurasi 93,33%, yaitu nilai tertinggi. Ringkasannya, metode pertama dengan 59 fitur *hue* menghasilkan 91,67%, sedangkan metode kedua dengan enam fitur menghasilkan 93,33%, atau meningkat 1,66%. Penulis melaporkan bahwa reduksi fitur juga memperkecil arsitektur jaringan, mengurangi kebutuhan memori, dan mempercepat klasifikasi. Sebagai pembanding, kajian dengan pencahayaan laboratorium terkontrol dapat mencapai 100%, pendekatan neuro-fuzzy di luar ruangan melaporkan 73,3%, sedangkan pendekatan yang diusulkan mencapai 93,33% pada citra luar ruangan.

Penulis menyatakan jumlah TBS yang dapat diperoleh terbatas sehingga ukuran himpunan uji dibatasi. Acuan kelas berasal dari penilaian pengawas mutu terlatih, bukan dari pengukuran kandungan minyak di laboratorium, dan tandan yang busuk, kosong, atau terinfeksi tidak disertakan. Penulis juga mencatat bahwa sebagian besar kajian sebelumnya memakai kondisi laboratorium dan pencahayaan terkontrol, sedangkan sistem ini dirancang untuk cahaya alami di luar ruangan. Dengan hasil tersebut, penulis mengusulkan klasifier ini dapat berfungsi sebagai sensor warna untuk mempercepat penentuan kematangan TBS pada proses pemanenan.
