# A review on methods for automatic counting of objects in digital images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `barbedo2012review` |
| Judul asli | A review on methods for automatic counting of objects in digital images |
| Penulis | Garcia Arnal Barbedo, Jayme |
| Tahun | 2012 |
| Venue | IEEE Latin America Transactions |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [barbedo2012review.pdf](../pdf/barbedo2012review.pdf)
- DOI resmi: https://doi.org/10.1109/tla.2012.6362356

## Gambaran Umum

Barbedo (2012) menulis tinjauan tentang metode penghitungan otomatis objek dalam citra digital. Penghitungan objek seperti sel, orang, serangga, dan lainnya sering dilakukan secara manual, sehingga prosesnya panjang dan melelahkan. Karena itu, sejumlah metode penghitungan otomatis telah diusulkan selama dua dekade terakhir. Penulis menilai bahwa literatur ini tersebar di banyak jurnal dan konferensi, sehingga solusi yang berguna untuk satu bidang mudah terlewat oleh peneliti di bidang lain. Tinjauan ini bertujuan menyatukan alat dan teknik utama tersebut.

Cakupan tinjauan ini luas dan tidak dibatasi pada satu komoditas. Penulis mengelompokkan teknik berdasarkan fungsinya, bukan berdasarkan rujukan, dengan format *tutorial*. Dalam Tabel I, aplikasi yang dicakup meliputi sel, bakteri, pohon, serangga, buah, struktur tanah, koloni jamur, serbuk sari, bulir, kromosom, cacat kayu, ikan, bijian, parasit malaria, penginderaan jauh, dan elemen ovarium. Sel dan bakteri menjadi kelompok aplikasi terbanyak yang dirujuk. Bagian awal tinjauan membahas faktor-faktor yang menentukan tingkat kesulitan, seperti kontras objek dengan latar, tingkat pengelompokan objek, tekstur, serta variasi ukuran dan bentuk. Teks ini juga menjelaskan bahwa banyak metode berupa rangkaian alat yang sama pentingnya, sehingga klasifikasi berdasarkan satu aspek dianggap terbatas.

Tinjauan ini mengelompokkan teknik ke dalam delapan kategori. Kategori pertama adalah operasi morfologi, yaitu *dilatasi* dan *erosi* sebagai operasi dasar, kemudian *closing*, *opening*, dan penipisan (*skeletonization*). Dilatasi biasanya dipakai untuk menutup lubang dan menyambungkan bagian yang seharusnya menyatu, sedangkan erosi dipakai untuk memisahkan objek yang saling menempel dan menghapus objek kecil yang tidak relevan. Kategori lain yang dibahas mencakup segmentasi dengan *watershed*, pengurangan latar belakang, dan deskriptor citra seperti *SIFT* dan *SURF*. Penulis mencatat bahwa *SIFT* dan *SURF* telah banyak dipakai di bidang pengolahan citra, tetapi penggunaannya dalam penghitungan objek masih sangat terbatas. Penulis hanya mengetahui satu metode yang secara eksplisit memanfaatkan jenis deskriptor ini, yaitu pendekatan Lempitsky dan Zisserman yang memperkirakan kepadatan citra, lalu mengintegralkannya di suatu wilayah untuk menghasilkan jumlah objek. Tinjauan ini tidak memuat angka akurasi, presisi, atau metrik kuantitatif lain dari metode-metode tersebut. Data kuantitatif yang tersedia hanya berupa jumlah kategori teknik, yaitu delapan, dan rentang nomor rujukan hingga [132].

Hasil utama tinjauan ini bersifat kualitatif. Penulis menyimpulkan bahwa artikel ini dapat berfungsi sebagai pengantar bagi pemula sekaligus sebagai kumpulan referensi dan gagasan bagi peneliti yang sudah berpengalaman. Setiap teknik dijelaskan secara ringkas, dan rincian lebih lanjut dirujuk ke sumber asli. Tabel I dimaksudkan untuk memudahkan pembaca menemukan rujukan berdasarkan aplikasi. Dengan demikian, nilai utama tinjauan ini terletak pada pemetaan lintas bidang, bukan pada perbandingan performa antarmetode.

Penulis secara eksplisit menyebut beberapa batasan. Pertama, keterbatasan ruang membuat tidak mungkin mencantumkan seluruh alat dan teknik yang pernah dipakai, sehingga dilakukan seleksi terhadap yang paling relevan. Kedua, penjelasan setiap teknik dibuat singkat demi keringkasan, sehingga pembaca perlu merujuk ke sumber asli untuk detail implementasi. Ketiga, pengelompokan ke dalam delapan kategori dinyatakan sebagai pilihan yang tidak sempurna, karena sebagian besar metode terdiri atas kombinasi beberapa teknik. Keempat, tinjauan ini tidak membandingkan performa metode secara kuantitatif, sehingga pembaca tidak dapat menentukan metode terbaik untuk kasus tertentu dari teks ini saja.
