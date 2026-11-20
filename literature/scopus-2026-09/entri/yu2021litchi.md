# A litchi fruit recognition method in a natural environment using RGB-D images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yu2021litchi` |
| Judul asli | A litchi fruit recognition method in a natural environment using RGB-D images |
| Penulis | Yu, Lianyi; Xiong, Juntao; Fang, Xueqing; Yang, Zhengang; Chen, Yunqi; Lin, Xiaoyun; Chen, Shufang |
| Tahun | 2021 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [yu2021litchi.pdf](../pdf/yu2021litchi.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2021.01.015

## Gambaran Umum

Kajian ini bertujuan mengenali buah leci secara akurat di kebun yang alami. Pengenalan buah leci sulit karena buah tumbuh berkelompok seperti untaian dan sering berpadu dengan latar yang rumit, terutama dedaunan. Leci hijau, yaitu varietas Feizixiao, hampir sama warnanya dengan daun, apalagi saat tersorot cahaya dari belakang. Permukaan kulit leci juga tidak rata sehingga pantulan cahaya berubah-ubah. Metode yang hanya memakai warna atau tekstur dinilai kurang tangguh dalam kondisi tersebut. Jaringan saraf dalam memang unggul, tetapi penulis mencatat kebutuhan komputasi dan penyimpanannya lebih besar. Karena itu, penulis mengusulkan metode yang memanfaatkan informasi kedalaman dari kamera *RGB-D* untuk mendukung perkiraan hasil panen dan pekerjaan robot pemetik.

Data dikumpulkan dengan sistem pencitraan yang dilengkapi kamera RGB-D. Dari 220 kelompok citra yang terkumpul, 200 kelompok dipilih, yaitu 100 kelompok Nuomici dan 100 kelompok Feizixiao. Citra warna berukuran 1920 × 1080 piksel dan citra kedalaman berukuran 512 × 424 piksel. Jarak pemotretan ditetapkan antara 50 dan 150 cm. Untuk pelatihan klasifikasi, setiap percobaan memakai 50 kelompok citra. Dari citra tersebut dipotong 2000 blok citra, terdiri atas 400 sampel positif yang memuat buah utuh dan 600 sampel negatif yang memuat daun, cabang, tanah, dan latar lain. Untuk evaluasi, 80 kelompok citra diberi label manual pada seluruh citra, masing-masing 40 kelompok per percobaan. Himpunan uji terdiri atas 100 kelompok citra RGB-D yang telah diregistrasi.

Metode bekerja dalam beberapa tahap. Pertama, segmentasi kedalaman membuang area di luar jangkauan efektif lengan pemetik. Kedua, *random forest* biner dilatih dengan fitur warna dan tekstur. Pelatihan dihentikan ketika akurasi mencapai 95 persen atau lebih. Ketiga, citra diskalakan pada beberapa skala dan diproses dengan *sliding window* berukuran tetap. Setiap blok diklasifikasikan, lalu buah ditentukan dengan *non-maximum suppression* untuk menekan deteksi ganda. Hasil pengenalan pada himpunan uji adalah 89,92 persen untuk leci hijau dan 94,50 persen untuk leci merah. Dengan demikian, metode ini mengenali kedua varietas dengan akurasi di atas 89 persen tanpa jaringan saraf dalam.
