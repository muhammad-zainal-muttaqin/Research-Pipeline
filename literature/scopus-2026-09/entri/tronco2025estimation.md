# Estimation of fruit number in coffee trees by maturity level, based on color space weighting, using a new segmentation algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tronco2025estimation` |
| Judul asli | Estimation of fruit number in coffee trees by maturity level, based on color space weighting, using a new segmentation algorithm |
| Penulis | Tronco, Mario Luiz; Pedrazza, Ingrid Lorena Argote; Pedrino, Emerson Carlos; Valencio, Carlos Roberto |
| Tahun | 2025 |
| Venue | IEEE Latin America Transactions |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | cherry, coffee, olive |

## Tautan Akses
- PDF: [tronco2025estimation.pdf](../pdf/tronco2025estimation.pdf)
- DOI resmi: https://doi.org/10.1109/tla.2025.11072497

## Gambaran Umum

Penelitian ini bertujuan mengestimasi jumlah buah kopi pada cabang pohon berdasarkan tingkat kematangannya. Penulis menilai bahwa pencacahan langsung di pohon sulit dilakukan karena buah sering tertutup daun dan cabang (*occlusion*), sementara kondisi pencahayaan di lapangan tidak terkendali. Pengambilan buah dari cabang untuk dihitung bersifat merusak, sehingga penulis mencari cara tanpa-invasif. Penulis mengajukan dua pertanyaan: apakah kamera berbiaya rendah dapat menjaga kualitas citra, dan apakah algoritma visi komputer dapat menghitung serta mengklasifikasikan biji kopi dengan akurasi di atas 80%. Ambang 80% ditetapkan secara empiris berdasarkan statistik hitung buah secara manual.

Data yang digunakan berasal dari tanaman kopi Arabika. Citra diambil langsung di lapangan dari cabang pohon menggunakan sistem akuisisi yang dikembangkan berdasarkan karakteristik fenologi tanaman kopi. Penulis memakai kamera berbiaya rendah. Set data pertama berisi 1.500 citra buah kopi dari varietas *Coffea arabica* dan *Coffea canephora* yang diseragamkan menjadi 300x300 piksel. Set data kedua berisi sampel biji kopi dalam empat kelas, yaitu ceri, hijau-kekuningan, hijau, dan kismis, dengan masing-masing 600 citra berukuran 50x50 piksel. Evaluasi penghitungan dilakukan pada seluruh 1.500 sampel. Hitung manual per kelas adalah 2.892 untuk hijau, 2.172 untuk hijau-kekuningan, 6.053 untuk ceri, dan 2.295 untuk kismis.

Metode yang diusulkan merupakan algoritma tepi (*edge detection*) baru. Algoritma ini memakai analisis statistik ruang warna untuk memisahkan buah dari latar belakang, lalu melakukan segmentasi. Setiap buah kemudian diproyeksikan sebagai elips, dan jumlah buah dihitung dari titik pusat (*centroid*) elips tersebut. Hasil hitung dibandingkan dengan hitung manual per kelas menggunakan matriks konfusi, dengan *true positive* dan *false positive* dihitung secara terpisah untuk tiap kelas dan latar belakang. Akurasi yang dicapai adalah 83% untuk hijau, 79% untuk hijau-kekuningan, 86% untuk ceri, dan 80% untuk kismis. Pada tingkat total, algoritma menghitung 12.023 buah, sedangkan hitung manual mencatat 13.412 buah. Penulis juga membandingkan metodenya dengan dua penelitian terdahulu, yaitu Ramos dkk. (2017 dan 2018) serta Bazame dkk. (2021), dalam tabel presisi, sensitivitas, dan *F1-score*.

Penulis menyatakan bahwa metode ini menawarkan alternatif tanpa-invasif yang menjaga keutuhan pohon. Kelas ceri dianggap paling penting karena menandakan buah siap petik, dan akurasinya 86% dinilai cukup andal untuk perencanaan panen. Penulis juga mencatat bahwa hasil ini masih berupa akurasi pada sampel, bukan validasi pada kondisi nyata. Langkah lanjutan yang direncanakan adalah membangun model matematika yang mengorelasikan hasil hitung otomatis dengan hitung manual dalam periode tertentu. Model tersebut diharapkan menjadi dasar estimasi hasil panen, sekaligus menguji akurasi dan keandalan algoritma dalam penerapan lapangan.
