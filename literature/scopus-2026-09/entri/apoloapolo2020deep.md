# Deep learning techniques for estimation of the yield and size of citrus fruits using a UAV

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `apoloapolo2020deep` |
| Judul asli | Deep learning techniques for estimation of the yield and size of citrus fruits using a UAV |
| Penulis | Apolo-Apolo, O.E.; Mart\'\inez-Guanter, J.; Egea, G.; Raja, P.; P\'erez-Ruiz, M. |
| Tahun | 2020 |
| Venue | European Journal of Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [apoloapolo2020deep.pdf](../pdf/apoloapolo2020deep.pdf)
- DOI resmi: https://doi.org/10.1016/j.eja.2020.126030

## Gambaran Umum

Estimasi hasil panen jeruk yang akurat dan dini penting bagi produsen dan koperasi agar dapat memperkirakan volume stok, menghindari kekosongan stok, dan merencanakan kegiatan panen. Estimasi visual yang selama ini dipakai bersifat subjektif karena bergantung pada pengalaman teknisi, dengan galat antara hasil aktual dan prakiraan sebesar 15–25%. Pengukuran manual ukuran buah juga memakan waktu dan rentan terhadap kesalahan pencatatan. Sebagian besar metode berbasis pencacahan buah sebelumnya menggunakan foto dari permukaan tanah, yang dinilai mahal dan tidak layak untuk kebun jeruk yang luas.

Penelitian ini bertujuan mengembangkan metode pengolahan citra otomatis untuk mendeteksi, mencacah, dan menaksir ukuran buah jeruk pada setiap pohon dengan *deep learning*. Penelitian juga membangun model hasil panen kebun berdasarkan jumlah buah yang terdeteksi. Penulis memakai *Unmanned Aerial Vehicle* (UAV) sebagai alternatif yang murah dan cepat diterapkan, dengan citra RGB sebagai masukan.

Data dikumpulkan selama tiga musim panen berturut-turut dari 20 pohon di kebun jeruk komersial. Citra diambil dengan UAV dari kedua sisi pohon, dan total 300 citra beresolusi tinggi diperoleh selama periode penelitian. Citra tersebut dirotasi 90, 180, dan 270 derajat serta diubah ukurannya menjadi 600 × 600 piksel, sehingga jumlah citra untuk pelatihan menjadi 900. Setiap buah pada citra pelatihan diberi label secara manual menggunakan LabelImg. Untuk pengujian deteksi, penulis memakai 40 citra UAV dari 20 pohon tersebut. Pohon dipanen secara manual dan ukuran buah diukur dengan timbangan berketelitian gram. Data hasil panen total kebun dari 2011 hingga 2018 memiliki rata-rata 158.740,12 kg per musim. Model hasil panen memakai pasangan dua tahun untuk pelatihan dan satu tahun sisanya untuk pengujian.

Pendekatan deteksi memakai *Faster R-CNN* yang dilatih melalui *transfer learning* dari model yang sebelumnya dilatih pada COCO. *Standard error* (SE) antara pencacahan visual dan hasil deteksi model sebesar 6,59%. Ukuran buah diperkirakan dengan kalibrasi menggunakan penggaris kayu sebagai objek acuan. Untuk estimasi hasil per pohon, model *Long Short-Term Memory* (LSTM) menghasilkan SE 4,53% dan simpangan baku 0,97 kg. Untuk total hasil kebun, estimasi teknisi memiliki SE 13,74%, sedangkan model menghasilkan SE 7,22% dengan simpangan baku 4.083,58 kg. Hasil ini menunjukkan model lebih dekat ke hasil aktual daripada estimasi teknisi.

Penulis menyatakan bahwa hasil ini menjanjikan dan mungkin berlaku pula untuk jenis buah lain, tetapi penelitian ini hanya menguji jeruk. Penulis juga mengakui bahwa penghitungan buah dari citra tidak mencerminkan seluruh hasil panen, karena pada tajuk yang besar citra hanya merekam sebagian dari total hasil. Hubungan jumlah buah dan hasil panen juga tidak linear, sebab dipengaruhi iklim, pemupukan, dan penyakit. Tantangan lain yang disebut penulis adalah buah yang tertutup daun, perubahan cahaya, serta perbedaan ukuran, bentuk, dan posisi buah. Penulis menilai diperlukan model yang mampu menangani kondisi tersebut.
