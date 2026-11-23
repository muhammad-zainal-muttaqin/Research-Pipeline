# Detection and Counting of Mango Fruits in Occluded Condition Using Image Analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hutagalung2018detection` |
| Judul asli | Detection and Counting of Mango Fruits in Occluded Condition Using Image Analysis |
| Penulis | Hutagalung, Andriyono; Nugroho, Hertog; Suheryadi, Adi; Yunanto, Prasti Eko |
| Tahun | 2018 |
| Venue | Proceedings of 2017 5th International Conference on Instrumentation Communications Information Technology and Biomedical Engineering Icici Bme 2017 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [hutagalung2018detection.pdf](../pdf/hutagalung2018detection.pdf)
- DOI resmi: https://doi.org/10.1109/icici-bme.2017.8537729

## Gambaran Umum

Penelitian ini bertujuan mendeteksi dan menghitung buah mangga hijau pada tajuk daun hijau, termasuk buah yang saling menutupi (*occlusion*). Penulis menyebut kendala pencahayaan yang berubah, buah yang bertumpuk, dan warna buah yang mirip latar belakang. Estimasi hasil sebelum panen disebut berguna bagi petani untuk mengatur air dan pupuk.

Data berupa 150 citra mangga, dibagi 30 citra latih dan 120 citra uji. Citra uji memuat 705 buah, 283 berbentuk tunggal dan 422 berkelompok. Kamera yang dipakai adalah DSLR 21 MP, dan citra diubah ukurannya menjadi 480x320 piksel (di bagian lain ditulis 340x480). Lokasi kebun, jumlah pohon, dan pemberi label tidak disebut. Pembagian latih dan uji tidak dinyatakan per pohon.

Metode berjalan dalam empat tahap. Tahap pertama adalah segmentasi dengan ambang histogram per kanal merah, hijau, dan biru, yang dihitung dari rerata histogram citra latih, lalu operasi morfologi. Tahap kedua memberi bobot pada setiap *blob* (daerah biner yang terhubung) memakai *distance transform* (jarak tiap piksel ke tepi daerah). Tahap ketiga mencari titik puncak kandidat pusat buah dari topografi gradien bobot. Tahap keempat memakai *hierarchical clustering* (pengelompokan bertingkat) dengan ambang jarak rerata ditambah simpangan baku, sehingga jumlah kelompok tidak perlu ditentukan.

Pada 705 buah uji, 646 terdeteksi benar (*recall* 91,63%, presisi 97,88%, laju salah 2,12%). Buah tunggal: *recall* 97,53%, presisi 99,28%, laju salah 0,72%, F1 98,40%. Buah berkelompok atau tertutup: *recall* 87,68%, presisi 96,86%, laju salah 3,14%, F1 92,04%. Pembanding adalah satu kajian terdahulu pada 50 citra berisi 187 buah dengan *recall* 96,26% untuk buah yang tampak jelas.

Keterbatasan yang tertera: metode gagal pada pencahayaan berlebih dan pada malam hari, dan beberapa ambang ditentukan secara empiris dari praeksperimen. Kesalahan berupa objek bukan buah yang terdeteksi dan satu buah yang terhitung lebih dari satu. Tabel III memuat angka yang tidak konsisten (442 buah berkelompok di tabel, 422 di teks). Tidak ada data uji dari kebun atau pohon terpisah, dan acuan hitung (hitung tangan atau label citra) tidak dijelaskan.
