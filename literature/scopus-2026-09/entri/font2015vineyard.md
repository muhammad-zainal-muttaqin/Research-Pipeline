# Vineyard yield estimation based on the analysis of high resolution images obtained with artificial illumination at night

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `font2015vineyard` |
| Judul asli | Vineyard yield estimation based on the analysis of high resolution images obtained with artificial illumination at night |
| Penulis | Font, Davinia; Tresanchez, Marcel; Mart\'\inez, Dani; Moreno, Javier; Clotet, Eduard; Palac\'\in, Jordi |
| Tahun | 2015 |
| Venue | Sensors Switzerland |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [font2015vineyard.pdf](../pdf/font2015vineyard.pdf)
- DOI resmi: https://doi.org/10.3390/s150408284

## Gambaran Umum

Penelitian ini mengestimasi hasil panen kebun anggur dari citra beresolusi tinggi yang diambil dengan pencahayaan buatan pada malam hari. Tujuannya adalah menghindari variasi warna dan perubahan pencahayaan siang hari yang menyulitkan segmentasi buah. Penulis menilai lima metode segmentasi berbasis piksel untuk mendeteksi anggur merah, kemudian mengubah luas dan volume tandan menjadi perkiraan berat. Dua prosedur estimasi hasil diuji: luas tandan dalam piksel dikonversi langsung menjadi berat, dan luas tandan diubah menjadi volume benda putar lalu dikonversi menjadi berat.

Datanya adalah anggur meja merah varietas Flame Seedless dari kebun di Bakersfield, California. Citra diambil dengan kamera monokular Nikon D300s berlensa 18–55 mm pada panjang fokus 20 mm, bukaan F11, ISO200, waktu paparan 1/250 s, dan tanpa kompensasi paparan, menghasilkan berkas JPEG RGB 4288 × 2848 piksel berkedalaman 24 bit. Pencahayaan berasal dari cincin flash 10 Ws yang diarahkan 45° ke langit-langit dan dipasang pada kendaraan yang bergerak dengan kecepatan tetap sekitar 2 m dari kedua sisi tanaman; citra diambil pada interval tetap tanpa tumpang tindih. Rata-rata diameter satu buah matang adalah 109 piksel dan rata-rata luas satu tandan 250.000 piksel. Pengambilan dilakukan pada masa panen. Tidak ada split latih-uji formal yang dinyatakan; penulis memakai 29 tandan untuk kalibrasi, 40 citra berisi 97 tandan untuk penilaian segmentasi, dan 25 tandan untuk estimasi hasil.

Mekanisme segmentasi mencakup ambang batas (pada lapis R, G, B, abu-abu I, dan H), jarak Mahalanobis, pengklasifikasi Bayes, model warna linier, dan segmentasi histogram, masing-masing dalam ruang warna RGB dan HSV dengan komponen H digeser 180° agar merah berada di tengah. Dua templat acuan, yaitu buah dan latar, dipilih manual oleh operator; model warna linier memakai tiga templat buah dan enam templat latar. Akurasi diukur dengan membandingkan hasil otomatis terhadap pelabelan kontur manual (~600 titik): galat dihitung sebagai jumlah piksel yang berbeda (XOR) dibagi jumlah piksel tandan pada pelabelan manual, lalu ditingkatkan dengan rangkaian morfologi berupa erosi, dilasi, dan pengisian lubang. Kalibrasi dilakukan di laboratorium dengan menimbang 29 tandan secara manual, memotretnya pada latar putih, memsegmentasinya dengan metode Otsu disertai 10 erosi dan dilasi, lalu meregresikan berat terhadap luas (koefisien korelasi 0,9557) dan terhadap volume benda putar dengan penampang π·((e(k) − s(k))/2)² per baris (0,9635).

Pada 97 tandan tanpa oklusi, kelima metode mendeteksi 100% tandan. Galat luas terbaik diperoleh dari ambang batas pada lapis H, yaitu 13,55%, turun menjadi 10,01% setelah penyaringan morfologi HF + 4E + 4D. Metode lainnya menghasilkan galat setelah penyaringan sebagai berikut: Mahalanobis RGB 13,29% dan HSV 10,50%; Bayes RGB 13,24% dan HSV 10,29%; model warna linier RGB 10,99% dan HSV 14,78%; histogram RGB 13,37% dan HSV 12,27%. Untuk 25 tandan, galat berat individu berkisar 18,8% sampai −16,5% memakai luas dan 15,1% sampai −21,1% memakai volume. Berat total hasil estimasi luas adalah 18,382 kg terhadap berat terukur 15,835 kg (galat +16,0%); estimasi volume menghasilkan 13,183 kg (galat −16,7%; abstrak menuliskan −17%). Rata-rata kedua metode menghasilkan 15,782 kg (galat −0,3%), yang penulis sebut sebagai kemungkinan kebetulan numerik.

Batasan yang dinyatakan penulis mencakup perlunya validasi lebih lanjut pada pengukuran kebun berskala besar; oklusi apa pun mengurangi luas, volume, dan berat yang diperkirakan; kalibrasi bersifat manual dan dilakukan di laboratorium; serta kurva kalibrasi sangat sensitif terhadap galat ukuran tandan. Semua metode bersifat bergantung warna dan disetel untuk varietas matang berwarna merah di bawah pencahayaan terkendali, sehingga varietas lain atau tingkat kematangan lain dapat memberi hasil berbeda. Pemilihan templat awal menghambat penerapan praktis metode Mahalanobis, Bayes, dan histogram. Penulis juga menyatakan hasil 16% dan −17% belum menentukan metode mana yang lebih cocok, estimasi volume sensitif terhadap tumpang tindih dan oklusi, dan penggunaan waktu nyata serta uji ketahanan terhadap penyakit dan tahap kematangan menjadi pekerjaan lanjutan.

