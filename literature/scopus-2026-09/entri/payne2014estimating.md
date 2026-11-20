# Estimating mango crop yield using image analysis using fruit at 'stone hardening' stage and night time imaging

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `payne2014estimating` |
| Judul asli | Estimating mango crop yield using image analysis using fruit at 'stone hardening' stage and night time imaging |
| Penulis | Payne, A.; Walsh, K.; Subedi, P.; Jarvis, D. |
| Tahun | 2014 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [payne2014estimating.pdf](../pdf/payne2014estimating.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2013.11.011

## Gambaran Umum

Kajian ini membahas estimasi hasil panen mangga secara otomatis dengan analisis citra. Petani dan pengelola kebun biasanya memperkirakan jumlah buah pada pohon melalui penghitungan manual terhadap sebagian kecil pohon. Cara ini memakan waktu dan hanya mewakili sampel kecil. Penelitian ini merupakan lanjutan dari studi sebelumnya yang dilakukan pada buah mendekati panen. Fokusnya adalah buah pada tahap *stone hardening*, yaitu sekitar enam minggu sebelum panen, ketika sebagian besar buah yang rontok sudah terjadi dan jumlah buah relatif tetap hingga panen. Pada tahap ini buah masih banyak yang berwarna hijau, sehingga algoritma sebelumnya yang bergantung pada warna merah kulit tidak lagi memadai.

Data dikumpulkan di dua perkebunan mangga (*Mangifera indica*), yaitu di Queensland utara tropis pada musim 2011 dan di wilayah Wide Bay Queensland selatan pada musim 2012. Citra diambil menggunakan kamera Canon 50D dengan lensa 28–135 mm, dalam format RAW RGB beresolusi 4752 × 3168 piksel. Kamera dipasang pada rangka dengan empat lampu LED 6 × 3 W, dan pemotretan dilakukan pada malam hari dengan eksposur minus dua stop. Kamera dipasang sekitar 2 m dari batang pohon di antara barisan tanaman, dari kendaraan yang bergerak di sepanjang baris. Set kalibrasi terdiri atas 100 citra dari 50 pohon pada 2011, dengan rerata 83,5 ± 36,9 buah per pohon. Set validasi 1 berisi 10 pohon dari set kalibrasi yang difoto ulang pada malam lain. Set validasi 2 berisi satu sisi dari 74 pohon tambahan. Set validasi 3 berisi kedua sisi dari 21 pohon pada 2012, dengan rerata 92,5 ± 50,4 buah per pohon. Jumlah buah total per pohon dihitung manual di lapangan pada siang hari, sedangkan jumlah buah per citra dihitung dengan fitur hitung pada Photoshop.

Metode awal dari studi sebelumnya menghasilkan tingkat kesalahan lebih dari 30 persen, dengan deteksi palsu pada tangkai bunga, cabang, dan batang, serta banyak buah hijau yang tidak terdeteksi. Penulis lalu memodifikasi algoritma dengan tiga perubahan utama. Penyaring selisih ternormalisasi dihapus. Penyaring varians 3 × 3 dan penyaring rerata berbatas dipertahankan dan ditambahkan. Penyaring Hessian ditambahkan untuk memisahkan struktur seperti tabung, seperti batang dan tangkai, dari buah yang berbentuk oval. Pada set kalibrasi 2011, algoritma yang diperbaiki mendeteksi 78,3 persen buah, dengan tingkat kesalahan 10,6 persen dan R² 0,63 terhadap hitungan manual. Hubungan antara jumlah total pohon dan jumlah hitungan manual per citra adalah R² 0,51 pada set kalibrasi dan R² 0,92 pada set validasi 3. Penerapan pada set validasi 2011 dan 2012 memberikan hasil yang beragam. Variasi karakteristik daun antarset menjadi sumber masalah utama.

Penulis mengakui beberapa batasan. Hasil pada set validasi belum konsisten, sehingga penulis menyarankan kinerja algoritma diuji ulang pada pohon dengan berbagai kondisi tumbuh. Pencahayaan malam hari lebih konsisten dibanding siang hari, tetapi penulis menekankan bahwa pencahayaan harus kuat, merata, dan tidak terarah pada seluruh tajuk. Penulis juga menyebut bahwa tajuk pohon perlu relatif datar agar pencitraan dari setiap barisan efektif. Buah yang jauh dari kamera ikut terhitung, dan penulis menyarankan kamera tiga dimensi dengan segmentasi kedalaman untuk menyingkirkannya. Penulis mengusulkan agar beberapa metode deteksi dipakai sebagai *toolkit* dalam sistem deteksi mangga yang juga menerima masukan dari pengguna.
