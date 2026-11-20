# ON-PLANT SIZE AND WEIGHT ESTIMATION OF TOMATO FRUITS USING DEEP NEURAL NETWORKS AND RGB-D IMAGING

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hong2024plant` |
| Judul asli | ON-PLANT SIZE AND WEIGHT ESTIMATION OF TOMATO FRUITS USING DEEP NEURAL NETWORKS AND RGB-D IMAGING |
| Penulis | Hong, Suk-Ju; Kim, Sungjay; Lee, ChangHyup; Park, Seongmin; Kim, Kyoung-Chul; Lee, Ahyeong; Kim, Ghiseok |
| Tahun | 2024 |
| Venue | Journal of the Asabe |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [hong2024plant.pdf](../pdf/hong2024plant.pdf)
- DOI resmi: https://doi.org/10.13031/ja.15746

## Gambaran Umum

Hong dkk. (2024) mengukur ukuran dan berat tomat yang masih tumbuh di tanaman memakai citra RGB-D (citra warna dan kedalaman) dan jaringan saraf dalam (*deep neural network*). Kajian ini dimuat di *Journal of the ASABE* 67(2): 439–450.

Data dikumpulkan di rumah kaca hidroponik Institut Nasional Sains Hortikultura dan Herbal, Wanju, Korea Selatan, dengan varietas tomat Dafnis. Kamera Intel RealSense D435i merekam citra RGB-D beresolusi 1280 × 720 piksel pada 17 dan 29 Juni, 19 dan 26 Oktober, serta 9 dan 16 November 2022, pukul 11.00 sampai 14.00. Data segmentasi berisi 533 citra pada jarak 0,3–0,7 m. Ukuran acuan diukur dengan jangka sorong (*Vernier calipers*). Rentang ukuran terukur adalah lebar 53,78–91,27 mm, tinggi 46,86–78,3 mm, dan berat 78,29–339,26 g.

Tahap pertama membandingkan beberapa model segmentasi instans. Mask R-CNN dengan backbone Swin-T memberi AP50:95 tertinggi pada data uji, yaitu 77,3%. Angka itu lebih tinggi daripada Mask R-CNN ResNet-101 (69,5%), YOLACT (69,1%), dan RTMDet-Ins-x (73,4%). Tahap kedua menghitung area tomat dari hasil segmentasi. Area dan kedalaman median dimasukkan ke regresi linear untuk memprediksi berat. Korelasi berat dan volume tercatat R² 0,998, yang menurut penulis terjadi karena tomat sebagian besar berisi air. Hanya berat yang dimodelkan.

Hasil gabungan seluruh tanggal: lebar RMSE 4 mm (MAPE 4,28%), tinggi RMSE 5,12 mm (MAPE 6,42%), dan berat RMSE 19,69 g (MAPE 9,44%). Validasi memakai tujuh lipatan antartanggal. Galat tinggi per tanggal berkisar RMSE 3,25–8,32 mm, dan galat tinggi lebih besar daripada galat lebar pada setiap tanggal. Galat tinggi tertinggi terjadi pada 19 Oktober (RMSE 8,32 mm), yang menurut penulis dipengaruhi kondisi cahaya.

Keterbatasan yang dinyatakan penulis: RTMDet-Ins membutuhkan 42 ms per citra, sedangkan makalah asalnya melaporkan 5,31 ms. Kesalahan prediksi terbesar terjadi pada tomat kecil yang berjarak jauh. Kajian ini tidak menghitung jumlah buah.
