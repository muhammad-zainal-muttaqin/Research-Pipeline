# Automated Ripeness Detection of Oil Palm Fruit Using a Hybrid GLCM-HSV-KNN Model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mirfan2025automated` |
| Judul asli | Automated Ripeness Detection of Oil Palm Fruit Using a Hybrid GLCM-HSV-KNN Model |
| Penulis | Mirfan; Billy Eden William Asrul; Mila Jumarlis; Juliani, Juliani |
| Tahun | 2025 |
| Venue | Jurnal Resti |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [mirfan2025automated.pdf](../pdf/mirfan2025automated.pdf)
- DOI resmi: https://doi.org/10.29207/resti.v9i5.6683

## Gambaran Umum

Penelitian ini bertujuan membangun sistem otomatis untuk menentukan tingkat kematangan buah kelapa sawit. Kematangan buah menentukan kualitas dan jumlah minyak yang dihasilkan saat panen. Penyortiran tandan buah segar (TBS) di perusahaan sawit umumnya dilakukan secara manual dengan menilai warna dan tekstur. Cara ini bergantung pada penilaian subjektif pekerja, rentan terhadap kelelahan, dan memakan waktu pada area perkebunan yang luas.

Data berupa citra buah kelapa sawit (*Elaeis guineensis*) yang diambil langsung dari perkebunan di Sulawesi Barat, Indonesia. Citra diambil dengan kamera digital Canon EOS 700D berSensor 18 megapiksel. Pemotretan dilakukan dalam pencahayaan semi-terkendali dengan latar belakang netral. Jarak dan sudut pemotretan dibuat seragam. Dataset berjumlah 600 citra yang terbagi rata ke empat kelas kematangan, yaitu *Overripe*, *Ripe*, *Half-Ripe*, dan *Unripe*, masing-masing 150 citra. Pelabelan dilakukan secara manual oleh pakar perkebunan. Setiap citra ditinjau minimal oleh dua pakar, dan perbedaan penilaian diselesaikan melalui diskusi. Dataset dibagi 80% untuk latih dan 20% untuk uji.

Metode meliputi pemotongan, pengubahan ukuran menjadi 128x128 piksel, dan konversi warna dari RGB ke *Hue Saturation Value* (HSV). Fitur warna diambil dari nilai rata-rata H, S, dan V. Fitur tekstur diambil dengan *Gray Level Co-occurrence Matrix* (GLCM), yaitu kontras, korelasi, energi, dan homogenitas. Kedua fitur kemudian diklasifikasikan dengan *K-Nearest Neighbor* (KNN). Hasil terbaik diperoleh pada K=3 dengan akurasi 85%, presisi 85%, dan recall 88%. Nilai K=3 dinyatakan lebih baik daripada K=5 dan K=7, tetapi nilai untuk kedua K tersebut tidak disebutkan dalam teks. Penulis menyimpulkan bahwa kombinasi HSV, GLCM, dan KNN efektif mengklasifikasikan empat tingkat kematangan. Penulis juga menilai sistem ini dapat meningkatkan ketepatan panen dan konsistensi pengolahan minyak sawit.

Penulis menyatakan bahwa metode ini layak diintegrasikan ke dalam sistem klasifikasi otomatis untuk mendukung keputusan panen. Cakupan data perlu dicermati. Citra diambil di satu wilayah, dengan pencahayaan semi-terkendali dan latar belakang netral. Kondisi tersebut berbeda dengan pencahayaan lapangan yang tidak stabil. Kajian sebelumnya yang dikutip penulis melaporkan penurunan akurasi pada kondisi cahaya alami. Oleh karena itu, hasil 85% pada penelitian ini berlaku untuk kondisi pemotretan yang dijelaskan dalam teks.
