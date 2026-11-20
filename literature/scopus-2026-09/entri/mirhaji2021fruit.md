# Fruit detection and load estimation of an orange orchard using the YOLO models through simple approaches in different imaging and illumination conditions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mirhaji2021fruit` |
| Judul asli | Fruit detection and load estimation of an orange orchard using the YOLO models through simple approaches in different imaging and illumination conditions |
| Penulis | Mirhaji, Hamzeh; Soleymani, Mohsen; Asakereh, Abbas; Abdanan Mehdizadeh, Saman |
| Tahun | 2021 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [mirhaji2021fruit.pdf](../pdf/mirhaji2021fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2021.106533

## Gambaran Umum

Estimasi jumlah buah merupakan langkah penting dalam *Precision Agriculture* (PA). Data hasil panen membantu petani merencanakan pemasaran, tenaga kerja, dan peralatan, serta membantu perusahaan asuransi menaksir kerusakan kebun. Pada kebun dengan ratusan pohon, perhitungan manual memakan waktu, padat tenaga, sering tidak akurat, dan biasanya hanya bertumpu pada riwayat panen sebelumnya. Kajian Mirhaji dkk. (2021) ini berangkat dari masalah tersebut dengan menerapkan model deteksi berbasis *deep learning* dari keluarga YOLO untuk mendeteksi dan menghitung jeruk. Tujuannya ada empat: memilih versi YOLO terbaik (V2, V3, atau V4), menguji pengaruh tingkat cahaya saat pemotretan, membandingkan akurasi estimasi hasil antara pemotretan dua sisi dan empat sisi, serta membuat peta variasi potensi hasil kebun.

Data dikumpulkan pada 2018 di kebun jeruk varietas lokal Dezful seluas 4,8 hektare di Dezful, Khuzestan, Iran barat daya. Pohon ditanam pada 2010 dengan jarak 6 m × 6 m. Dua kamera RGB, yaitu Nikon COOLPIX S8100 dan Pentax K10D, dipakai dalam mode otomatis. Dari total 766 citra, 512 diambil saat berawan, 86 saat cerah, dan 168 pada malam hari dengan lampu LED 72 watt. Citra diambil dari empat sisi barisan pohon sebulan sebelum panen. Setiap citra dianotasi satu per satu dengan *bounding box* menggunakan LabelImg, dengan rata-rata 10 menit per citra. Dengan augmentasi menggunakan pustaka Albumentations, dataset menjadi 1.568 citra, dan 20% di antaranya dipakai untuk pengujian. Untuk menguji akurasi estimasi jumlah, penulis memilih 100 pohon secara acak, memotretnya dari empat sisi, lalu menghitung buahnya setelah panen. Bobot rata-rata jeruk diperoleh dari 20 buah yang ditimbang tiga kali.

Model dilatih dengan *transfer learning* menggunakan Google Colaboratory. Hasil terbaik diperoleh YOLO-V4 untuk deteksi jeruk pada citra uji, dengan *precision* 91,23%, *recall* 92,8%, *F1-score* 92%, dan *mean average precision* (mAP) 90,8%. Kinerja model pada siang dan malam hari tidak berbeda nyata, sehingga YOLO-V4 dipilih untuk estimasi hasil kebun. Estimasi dengan pemotretan dua sisi dan empat sisi menunjukkan perbedaan yang signifikan. Karena itu, penulis mengusulkan metode gabungan: pemotretan dua sisi untuk tajuk tipis dan empat sisi untuk tajuk rapat. Peta variasi hasil kebun menunjukkan sebaran hasil per pohon dengan galat +9,19%. Penulis menilai YOLO efektif sebagai metode sederhana dan praktis bagi peneliti dan praktisi pertanian.

Penulis menyatakan bahwa ketepatan estimasi hasil peka terhadap kondisi pemotretan dan struktur tajuk, sehingga hasil kajian ini terikat pada kondisi pemotretan tertentu. Kajian dilakukan pada satu kebun, satu varietas jeruk, dan satu musim panen, dengan dua jenis kamera. Galat pada peta hasil kebun tercatat sebesar +9,19%, yang berarti peta hasil ini masih mengandung simpangan dari jumlah sebenarnya. Pembaca perlu mempertimbangkan keterbatasan cakupan ini sebelum menerapkan metode tersebut pada kebun lain atau varietas lain.
