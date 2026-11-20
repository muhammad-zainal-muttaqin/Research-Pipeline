# VISUAL DETECTION OF OIL PALM MATURITY LEVERAGING SIMPLE EVOLVING CONNECTIONIST SYSTEM

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alkhowarizmi2026visual` |
| Judul asli | VISUAL DETECTION OF OIL PALM MATURITY LEVERAGING SIMPLE EVOLVING CONNECTIONIST SYSTEM |
| Penulis | Al-Khowarizmi, Al-Khowarizmi; Hutagalung, Fatma Sari; Maulana, Halim |
| Tahun | 2026 |
| Venue | Journal of Applied Engineering and Technological Science |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [alkhowarizmi2026visual.pdf](../pdf/alkhowarizmi2026visual.pdf)
- DOI resmi: https://doi.org/10.37385/kvqm6450

## Gambaran Umum

Penelitian ini mengatasi penentuan tingkat kematangan tandan buah sawit yang selama ini dilakukan secara manual oleh petani atau pekerja lapangan. Pengamatan manual dinyatakan subjektif, tidak konsisten, dan tidak efisien, serta dapat menurunkan mutu dan jumlah minyak bila tandan dipanen terlalu muda atau terlalu matang. Penulis mengusulkan sistem deteksi visual berbasis algoritma Simple Evolving Connectionist System (SECoS) untuk mengklasifikasikan kematangan dari citra, lalu menyalurkan hasilnya ke aplikasi Android bagi pekerja kebun. Tujuannya adalah merancang dan mengevaluasi sistem klasifikasi citra digital untuk kematangan tandan sawit.

Datanya adalah 300 citra tandan buah sawit yang diperoleh dari perkebunan mitra, terdiri atas enam label dengan 50 citra per label: empty bunch (tandan kosong), overripe (terlalu matang), ripe (matang), rotten (busuk), underripe (setengah matang), dan unripe (mentah). Pemisahan data latih dan data uji tidak dinyatakan secara eksplisit; 300 citra dipakai untuk pelatihan dan pengujian, dengan 50 citra per label pada pengujian. Arsitektur yang diusulkan terdiri atas tiga lapis, yaitu lapis masukan dengan fungsi transfer linear, lapis evolving sebagai lapis tersembunyi, dan lapis keluaran dengan fungsi aktivasi linear jenuh sederhana.

Mekanismenya adalah klasifikasi per citra, bukan pelokalan atau penghitungan satu per satu tandan. Citra melalui praproses dan ekstraksi ciri berupa histogram skala abu-abu yang mengubah data gambar menjadi nilai numerik; abstrak menyebut ciri warna, tekstur, dan bentuk, sedangkan bagian metode menyebut histogram skala abu-abu dan data citra biner. Aktivasi simpul ke-n pada lapis evolving dihitung sebagai An = 1 − Dn, dengan Dn jarak Euclidean ternormalisasi antara vektor masukan dan vektor bobot. Pelatihan menambah simpul baru bila aktivasi maksimum lebih kecil dari ambang sensitivitas atau bila galat keluaran melebihi ambang galat; jika tidak, bobot simpul pemenang diperbarui. Setiap vektor masukan diproses sekali tanpa epoch berulang, dan keputusan kelas diambil dengan fungsi argmax.

Hasil pelatihan menunjukkan rugi turun dari nilai awal yang tinggi menjadi mendekati 0,1 pada epoch ke-20, sementara akurasi latih naik dari sekitar 65% menjadi lebih dari 94%. Pengujian pada 300 citra menghasilkan nilai per label sebagai berikut: Ripe 94%, Overripe 93,2%, Rotten 92%, Underripe 91,8%, Empty Bunch 89%, dan Unripe 88%, dengan rata-rata 91,3%. Tabel 1 memberi kolom bertajuk MAPE (%), tetapi narasi menyebut nilai tersebut sebagai akurasi. Contoh tampilan aplikasi menunjukkan satu tandan diprediksi overripe dengan akurasi deteksi 60,9%, disertai waktu 20 Agustus 2025 pukul 14.17 dan koordinat 3,5595; 98,7007.

Batasan yang dinyatakan penulis mencakup belum optimalnya kategori Empty Bunch dan Unripe, yang dikaitkan dengan kemiripan visual antarkelas dan terbatasnya data latih untuk kelas tersebut. Penulis menyatakan pula bahwa jumlah dan keragaman citra perlu ditambah, serta mengusulkan teknik optimasi tambahan seperti mekanisme atensi atau transfer learning untuk kelas berkinerja rendah. Tidak dinyatakan metrik pelokalan, penghitungan tandan, perbandingan dengan detektor lain, atau protokol split yang terpisah.
