# Looking behind occlusions: A study on amodal segmentation for robust on-tree apple fruit size estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2023looking` |
| Judul asli | Looking behind occlusions: A study on amodal segmentation for robust on-tree apple fruit size estimation |
| Penulis | Gen\'e-Mola, Jordi; Ferrer-Ferrer, Mar; Gregorio, Eduard; Blok, Pieter M.; Hemming, Jochen; Morros, Josep-Ramon; Rosell-Polo, Joan R.; Vilaplana, Ver\'onica; Ruiz-Hidalgo, Javier |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2023looking.pdf](../pdf/genemola2023looking.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.107854

## Gambaran Umum

Kajian ini, oleh Gené-Mola dkk. (2023), mengusulkan metode untuk mendeteksi apel dan sekaligus mengukur diameternya dari citra RGB-D. Masalah yang diangkat adalah penghitungan buah di kebun yang sering tertutup daun dan buah lain, sehingga buah yang terlihat hanya sebagian. Metode yang diusulkan memakai segmentasi instans *amodal*, yaitu model yang memprediksi bentuk buah utuh termasuk bagian yang tertutup, bukan hanya bagian yang terlihat.

Data terdiri atas 3.925 citra RGB-D berukuran 1.024 x 1.024 piksel, diambil dengan kamera Canon EOS 60D. Citra memuat 15.335 instans apel, yaitu 5.837 instans pada tahap BBCH77 (diameter rata-rata 54,0 mm) dan 9.498 instans pada tahap BBCH85 (diameter rata-rata 77,4 mm). Pembagian acak menghasilkan 2.304 citra latih, 814 validasi, dan 807 uji. Kasus uji lapangan memakai apel Elstar di Randwijk, Belanda, dengan lima pohon, empat tanggal pengambilan, dan empat tahap BBCH (75, 77, 78, 85). Ukuran sebenar diperoleh dari 15 sampel per pohon yang diukur dengan jangka sorong.

Metode dibangun di atas Mask R-CNN dengan cabang mask amodal tambahan, backbone ResNet-101 dengan FPN, dan pra-latih COCO melalui Detectron2. Model dilatih dengan SGD, momentum 0,9, learning rate 0,02, dan batch 4 pada GPU GTX 1080 Ti 11 GB. Bobot iterasi 3.000 dipilih berdasarkan loss validasi terendah. Diameter piksel dikonversi ke milimeter dengan model kamera pinhole memakai depth image. Nilai visibilitas tiap buah dipakai sebagai ukuran kepercayaan untuk menyaring pengukuran.

Pada data uji, deteksi mencapai F1 0,86 dengan presisi 0,92 dan recall 0,80, serta AP 0,47 untuk gabungan kedua tahap. AP BBCH85 adalah 0,51 (F1 0,87), sedangkan AP BBCH77 adalah 0,44 (F1 0,84). Untuk diameter, MAE gabungan 4,5 mm dan R2 0,80 pada semua buah. Bila dibatasi pada buah dengan visibilitas di atas 60 persen, MAE turun menjadi 2,93 mm dengan R2 0,91, dengan MBE gabungan −0,19 mm dan MAPE 4,19 persen. Penulis mencatat kecenderungan meremehkan diameter (MBE negatif). Pada studi kasus per pohon, MAE gabungan 4,17 mm dan R2 0,91.

Penulis menyebut keterbatasan utama pada data depth yang dihasilkan melalui fotogrametri, yang membatasi efisiensi akuisisi data. Penulis juga menyebut kerja lanjut dengan sensor RGB-D komersial dan buah non-bulat seperti pir.
