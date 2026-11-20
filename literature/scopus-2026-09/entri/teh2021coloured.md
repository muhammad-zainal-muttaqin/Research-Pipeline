# Coloured Edge Maps for Oil Palm Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `teh2021coloured` |
| Judul asli | Coloured Edge Maps for Oil Palm Ripeness Classification |
| Penulis | Teh, W.Y.; others |
| Tahun | 2021 |
| Venue | 32nd British Machine Vision Conference Bmvc 2021 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [teh2021coloured.pdf](../pdf/teh2021coloured.pdf)

## Gambaran Umum

Kajian ini membahas kesulitan klasifikasi tingkat kematangan tandan buah segar (TBS) kelapa sawit dengan komputer vision. Penentuan kematangan secara visual sulit, karena perbedaan rona antara buah matang dan belum matang sangat kecil. Akibatnya, model berbasis warna mudah keliru ketika citra diambil dengan kondisi pencahayaan baru. Penulis menyebutkan bahwa waktu panen yang tidak tepat dapat menurunkan hasil minyak, sehingga otomatisasi klasifikasi dinilai dapat mempercepat proses panen dan menekan biaya industri.

Penelitian ini bertujuan menilai efektivitas dan karakteristik kinerja *coloured edge maps* sebagai fitur masukan CNN. Penulis membandingkan empat teknik ekstraksi tepi, yaitu *Laplacian of Gaussian* (LoG), *Sobel*, *Prewitt*, dan *Kirsch*, dengan citra berwarna penuh menggunakan YCbCr sebagai pembanding. Model dilatih untuk tiga kelas kematangan, termasuk kelas *underripe*. Setiap model dilatih dengan satu jenis fitur masukan, sehingga total ada lima model. Arsitektur yang dipakai adalah *EfficientNetB0* yang telah dilatih sebelumnya pada ImageNet, lalu disesuaikan melalui *transfer learning*. Lapisan keluaran diganti dengan *global average pooling* dan tiga neuron dengan fungsi aktivasi *softmax*.

Pelatihan dilakukan dalam dua tahap. Tahap pertama membekukan lapisan dasar selama 25 epoch dengan laju pembelajaran 1×10⁻⁴. Tahap kedua membuka seluruh lapisan selama 120 epoch dengan laju pembelajaran 1×10⁻⁵, dengan ukuran batch 16 dan optimasi Adam. Evaluasi dilakukan pada 25 batch yang masing-masing berisi 50 citra uji, dengan augmentasi citra. Pada kondisi pencahayaan normal, model Sobel mencapai rata-rata akurasi 91,4 persen dan model YCbCr 91,5 persen. Model Kirsch mencapai 90,8 persen, sedangkan model LoG paling rendah dengan 85,5 persen. Ketika citra versi abu-abu diuji, seluruh metode mengalami penurunan performa yang signifikan. Hal ini menunjukkan bahwa informasi warna sisa pada tepi memang berkontribusi pada klasifikasi. Pada pengujian dengan pencahayaan yang diubah, akurasi citra berwarna penuh turun 19,89 persen, sedangkan rata-rata penurunan pada metode *coloured edge maps* hanya 4,97 persen.

Penulis menyatakan beberapa batasan. Ukuran data relatif kecil menurut standar *deep learning*, sehingga risiko *overfitting* tetap menjadi perhatian meskipun telah dilakukan beberapa langkah mitigasi. Penulis juga mengakui bahwa model terbaik mereka masih sedikit lebih rendah dibanding hasil penelitian sebelumnya yang memakai kernel kelapa sawit individual. Penulis berpendapat pendekatan dengan TBS utuh lebih praktis untuk pengumpulan data dan lebih andal sebagai ukuran tingkat kematangan. Kode penelitian dijanjikan akan tersedia secara publik.
