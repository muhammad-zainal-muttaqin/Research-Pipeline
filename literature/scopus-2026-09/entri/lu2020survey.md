# A survey of public datasets for computer vision tasks in precision agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lu2020survey` |
| Judul asli | A survey of public datasets for computer vision tasks in precision agriculture |
| Penulis | Lu, Yuzhen; Young, Sierra |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [lu2020survey.pdf](../pdf/lu2020survey.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2020.105760

## Gambaran Umum

Kajian ini berangkat dari keterbatasan data citra publik untuk pertanian presisi. Kelangkaan *dataset* citra publik disebut sebagai hambatan utama bagi pembuatan prototipe dan evaluasi cepat algoritma *computer vision* dan pembelajaran mesin. Sejak 2015 sejumlah *dataset* telah dirilis, tetapi belum ada survei khusus yang membahasnya. Penulis menyebut tulisan ini sebagai tinjauan komprehensif pertama, meskipun tidak menyeluruh, atas *dataset* citra publik yang dikumpulkan di kondisi lapangan atau semi-lapangan. Tujuannya membantu peneliti memilih *dataset* yang sesuai dan menunjukkan di mana *dataset* baru masih dibutuhkan.

Kajian ini mencakup 34 *dataset* citra publik. Dataset tersebut dikelompokkan menjadi 15 untuk pengendalian gulma, 10 untuk deteksi buah, dan 9 untuk aplikasi lain. Tanaman yang tercakup meliputi wortel, kedelai, bit gula, serta bibit tanaman dan gulma. Sensor yang disebut meliputi RGB, multispektral, NIR, dan gabungan multimodal. Platformnya beragam, mulai dari kendaraan darat, kamera genggam, UAV, hingga bingkai kamera tetap. Jumlah citra sangat bervariasi. Dataset CWFI memuat 60 citra, Carrot-Weed 39 citra, dan plant seedlings 407 citra. Grass-Broadleaf memuat 15.336 *patch*, sedangkan Leaf counting memuat 9.372 citra. Synthetic SugarBeet Weeds memuat 8.518 citra sintetis. Sugar Beets 2016 memuat 283 citra multi-kelas beranotasi piksel dan sekitar 12.340 citra beranotasi tiga kelas. Pembagian data latih dan uji tidak dijelaskan dalam teks.

Penulis menyatakan beberapa batasan. Survei ini bersifat komprehensif tetapi tidak menyeluruh, dan hanya mencakup *dataset* yang tersedia publik. Beberapa *dataset* berukuran kecil. Dataset CWFI disebut relatif kecil, sedangkan dataset Plant seedlings tidak cocok untuk segmentasi atau deteksi gulma karena tidak memiliki anotasi gulma yang rinci. Dataset Synthetic SugarBeet Weeds dibuat dengan pembangkitan prosedural. Penulis menilai data sintetis ini paling tepat dipakai sebagai pelengkap *dataset* nyata yang jumlahnya terbatas.
