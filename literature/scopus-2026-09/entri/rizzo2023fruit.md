# Fruit ripeness classification: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rizzo2023fruit` |
| Judul asli | Fruit ripeness classification: A survey |
| Penulis | Rizzo, Matteo; Marcuzzo, Matteo; Zangari, Alessandro; Gasparetto, Andrea; Albarelli, Andrea |
| Tahun | 2023 |
| Venue | Artificial Intelligence in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [rizzo2023fruit.pdf](../pdf/rizzo2023fruit.pdf)
- DOI resmi: https://doi.org/10.1016/j.aiia.2023.02.004

## Gambaran Umum

Tinjauan ini mengkaji klasifikasi kematangan buah, yaitu tugas menetapkan tahap kematangan buah secara otomatis untuk menjamin mutu, keamanan pangan, dan waktu panen. Penentuan kematangan selama ini dilakukan secara visual oleh pakar lapang sehingga bersifat subjektif, melelahkan, memakan waktu, dan rawan salah. Karena buah terus matang selama penyimpanan dan transportasi, penilaian kematangan yang objektif diperlukan sepanjang rantai pasok. Penulis menyusun kerangka bidang ini dari pernyataan masalah formal dan biologi pematanan, melalui representasi fitur dan metode klasifikasi, sampai estimasi waktu panen optimal.

Penulis meninjau makalah ilmiah terbitan 2014–2022 dan mengelompokkan metode menjadi tiga golongan: statistik, pembelajaran mesin, dan pembelajaran mendalam. Berbagai tanaman menjadi kasus, antara lain pisang, tomat, apel, mangga, anggur, stroberi, blueberry, kurma, pepaya, mulberi, dan sawit. Representasi fitur yang dikaji meliputi warna (kolorimeter serta pencitraan warna dalam ruang CIELAB, RGB, HSI, dan HSV), senyawa volatil melalui hidung elektronik, spektroskopi tampak–inframerah dekat, fluoresensi klorofil, serta pencitraan spektral berupa pencitraan hiperspektral dan multispektral. Praproses data yang dibahas mencakup filter Savitzky–Golay, Standard Normal Variate, Multiple Scattering Correction, dan turunan spektra.

Untuk pengenalan dan asosiasi, tinjauan membedakan pengklasifikasi yang bekerja pada data mentah dengan pengklasifikasi yang bekerja pada fitur rekayasa. Pendekatan berbasis deteksi memakai Faster R-CNN dan Mask R-CNN untuk memisahkan buah dari latar sekaligus menaksir kematangan; Halstead dkk. melaporkan skor F1 77,3 dengan lapisan paralel berbanding 72,5 dengan kelas tambahan, sedangkan Ni dkk. memperoleh mAP 71,6% dan akurasi mask 90,4% pada blueberry. Kajian lain menggabungkan jaringan saraf tiruan dengan fitur rekayasa atau menggabungkan dua moda pencitraan melalui konkatenasi fitur. Angka hasil yang dikutip berasal dari kajian primer yang dirujuk tinjauan ini, misalnya akurasi 98% untuk tujuh tahap kematangan pisang (Mendoza dan Aguilera), 94,3% pada 250 citra tomat (Goel dan Sehgal), 97,75% dengan jaringan saraf tiruan untuk pisang (Mazen dan Nashat), 99,01%/97,25%/98,59% untuk klasifikasi jenis, kematangan, dan keputusan panen kurma (Altaheri dkk.), akurasi 0,89 dengan EfficientNetB0 untuk sawit (Suharjito dkk.), serta peningkatan skor F1 1,1% dengan ResAttDenseNet (Herman dkk.).

Penulis mencatat sejumlah batasan. Ukuran dataset menjadi penghalang utama karena model pembelajaran mendalam memerlukan data berlabel yang cukup besar dan baik; tidak semua peneliti merilis data dan kode sehingga keterulangan hasil tidak selalu terjamin. Dataset kerap dikumpulkan untuk satu tugas tertentu sehingga daya generalisasi model terbatas. Tinjauan juga menemui celah literatur pada pengukuran waktu inferensi yang dibutuhkan aplikasi waktu nyata di lapang. Selain itu, model pembelajaran mendalam tidak transparan sehingga sulit dijelaskan; penulis menyerukan keseimbangan antara akurasi dan interpretabilitas serta mengusulkan Transformers visi dan teknik penjelasan model sebagai arah penelitian lanjutan.
