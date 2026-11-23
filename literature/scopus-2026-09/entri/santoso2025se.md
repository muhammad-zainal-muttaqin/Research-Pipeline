# SE-SMOTE: Latent-Space Oversampling for Long-Tailed Oil Palm Fruit Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `santoso2025se` |
| Judul asli | SE-SMOTE: Latent-Space Oversampling for Long-Tailed Oil Palm Fruit Classification |
| Penulis | Santoso, Lucky; Kamal, Imam Mustafa; Adni Navastara, Dini; Irfan Subakti, Misbakhul Munir |
| Tahun | 2025 |
| Venue | 2025 15th International Conference on Information and Communication Technology and System AI for the Now and Next Delivering Solutions and Driving Vision Icts 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [santoso2025se.pdf](../pdf/santoso2025se.pdf)
- DOI resmi: https://doi.org/10.1109/icts67612.2025.11369614

## Gambaran Umum

Kajian ini menangani ketidakseimbangan kelas pada klasifikasi kematangan tandan buah segar (TBS) kelapa sawit. Penulis menyatakan pemanen dilatih memetik tandan setengah matang, sehingga kelas itu mendominasi data, sedangkan tandan matang penuh paling sedikit. Akibatnya jaringan saraf konvolusi (*CNN*) cenderung memprediksi kelas mayoritas. Penulis mengusulkan SE-SMOTE, yaitu pengambilan sampel berlebih (*oversampling*) di ruang laten yang dibentuk lebih dahulu agar kelasnya terpisah.

Data berupa citra buah sawit dari satu kebun di Kalimantan, Indonesia, yang dirujuk ke set data Kamal dkk. Citra diubah menjadi 64x64 piksel. Ada lima kelas: belum matang, setengah matang, matang penuh, terlalu matang, dan busuk. Penulis menyusun lima skenario rasio ketidakseimbangan (IR) 10, 30, 50, 70, dan 100. Pada IR 100 jumlah sampel ialah 1.405 (setengah matang), 444, 140, 44, dan 14 (matang penuh), total 2.047. Pemberi label tidak disebut. Pembagian 80% latih dan 20% uji dilakukan terstratifikasi dengan beberapa benih acak.

Metode SE-SMOTE berjalan dua tahap. Tahap pertama melatih *super-encoder*, yaitu *autoencoder* (jaringan yang memampatkan lalu merekonstruksi citra) dengan cabang pemisah (*separator*) berupa perceptron berlapis banyak yang memprediksi kelas dari vektor laten. Fungsi kerugiannya menjumlahkan galat rekonstruksi dan entropi silang kelas dengan bobot alfa dan beta yang dicari coba-coba. Tahap kedua memakai SMOTE, yaitu interpolasi linear antara sampel minoritas dan tetangga terdekatnya, pada vektor laten dari *encoder*. Hasilnya melatih lima pengklasifikasi: KNN, SVM, regresi logistik, XGBoost, dan *random forest*.

Metrik utama ialah F1 rata-rata makro. Pada IR 100, SE-SMOTE mencapai 0,621, EOS 0,594, dan DeepSMOTE 0,275 (peningkatan relatif 4,5% dan 125,8%). Pada IR 10, SE-SMOTE 0,852 dan DeepSMOTE 0,382. SE-SMOTE sedikit di atas EOS pada IR 10, sedikit di bawahnya pada IR 30 sampai 70, dan di atasnya pada IR 100. Pada IR 100 galat baku antarbenih untuk sejumlah sel mencapai sekitar 0,1 atau lebih.

Keterbatasan: penulis menyatakan validasi hanya pada satu set data. Pengujian memakai pembagian acak 80/20 terstratifikasi, tanpa pembagian per pohon yang disebut. Tidak ada deteksi, pencacahan, atau citra beberapa pandang. Sampel diperkecil secara buatan untuk membentuk IR, sehingga bukan distribusi alami set data. Bobot alfa dan beta ditentukan coba-coba. Citra 64x64 piksel kecil dibanding citra tandan asli.
