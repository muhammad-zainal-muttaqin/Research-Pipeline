# Novel Feature Extraction for Oil Palm Bunches Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024novel` |
| Judul asli | Novel Feature Extraction for Oil Palm Bunches Classification |
| Penulis | Hui Hui Wang; Yin Chai Wang; Bui Lin Wee; Shiang Wei Sim |
| Tahun | 2024 |
| Venue | Journal of Advanced Research in Applied Sciences and Engineering Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [wang2024novel.pdf](../pdf/wang2024novel.pdf)
- DOI resmi: https://doi.org/10.37934/araset.34.1.350360

## Gambaran Umum

Penelitian ini mengatasi klasifikasi kematangan tandan buah segar kelapa sawit yang selama ini dilakukan oleh grader manusia. Penilaian manual dinyatakan rentan kesalahan dan subjektif, memakan waktu, serta menghadapi kekurangan tenaga ahli. Tujuan penelitian adalah mengklasifikasikan tandan ke dalam empat kategori, yaitu unripe, under ripe, ripe, dan over ripe, dengan fokus pada ekstraksi fitur warna. Pendekatan ini tidak memerlukan fase pelatihan model.

Data terdiri atas 50 sampel tandan sawit yang menghasilkan 100 citra.Untuk setiap tandan, dua citra diambil secara bersamaan dari sisi depan dan belakang pada sudut berbeda, lalu disimpan dalam format JPEG. Penilaian acuan dilakukan oleh grader dari Sarawak Land Consolidation & Rehabilitation Authority (SALCRA) sebelum analisis citra: 30 tandan masuk kategori ripe, 10 under ripe, dan masing-masing 5 overripe serta unripe. Seluruh 50 sampel ini dipakai sebagai dasar perbandingan dengan keluaran metode yang diusulkan.

Alur metode terdiri atas enam tahap: akuisisi citra, praproses, pemrosesan warna, segmentasi, klasifikasi, serta evaluasi. Praproses menghilangkan latar dengan topeng biner hasil konversi citra ke biner dan operasi morfologi dilasi, erosi, dan rekonstruksi. Fitur diambil dari ruang warna HSV; komponen saturasi dipilih sebagai penentu kematangan karena menutupi area terbesar pada tandan. Nilai ambang saturasi ditetapkan dari 30 sampel uji awal, dengan rentang 0,65–1,0 pada penjelasan metode dan 0,68–1,0 pada bagian eksperimen.

Mekanisme penghitungan membandingkan luas wilayah matang yang tertutup topeng terhadap luas keseluruhan tandan dalam persentase. Persentase dihitung sebagai (total luas wilayah buah yang tertutup topeng)/(luas total tandan) dikali 100, untuk sisi depan dan belakang, lalu dirata-ratakan. Kategori ditentukan dari persentase luas tertutup: unripe ≤20, under ripe 21–45, ripe 46–65, dan over ripe >65. Akurasi dihitung sebagai jumlah klasifikasi benar dibagi jumlah total sampel uji. Hasil yang dilaporkan adalah 86% (abstrak menyebut 85%), dengan tujuh dari 50 sampel salah klasifikasi, yaitu nomor 6, 13, 16, 25, 41, 43, dan 44. Metrik yang dipakai hanya akurasi klasifikasi; split atau cawat uji tidak dinyatakan.

Penulis menyebut beberapa batasan. Sebagian besar kesalahan terjadi pada kategori ripe dan overripe karena bagian akar tandan ikut tertutup warna merah-oranye atau merah-kuning sehingga luas topeng bergeser. Perbedaan persentase yang besar antara sisi depan dan belakang pada sampel 6 dan 25 dikaitkan dengan akuisisi citra di lingkungan tak terkontrol dan intensitas cahaya. Penulis mengusulkan pengambilan citra dengan tandan berputar agar seluruh sisi tercakup. Selain itu, penulis menyatakan hasil beberapa sampel perlu dinilai ulang oleh grader karena nilai persentasenya berada dekat batas kategori.
