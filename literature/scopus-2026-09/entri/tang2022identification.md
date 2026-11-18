# Identification of the Yield of Camellia oleifera Based on Color Space by the Optimized Mean Shift Clustering Algorithm Using Terrestrial Laser Scanning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tang2022identification` |
| Judul asli | Identification of the Yield of Camellia oleifera Based on Color Space by the Optimized Mean Shift Clustering Algorithm Using Terrestrial Laser Scanning |
| Penulis | Tang, Jie; Jiang, Fugen; Long, Yi; Fu, Liyong; Sun, Hua |
| Tahun | 2022 |
| Venue | Remote Sensing |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | camellia |

## Tautan Akses
- PDF: [tang2022identification.pdf](../pdf/tang2022identification.pdf)
- DOI resmi: https://doi.org/10.3390/rs14030642

## Gambaran Umum

Penelitian ini bertujuan meningkatkan akurasi dan efisiensi pendugaan hasil panen tanaman minyak teh (Camellia oleifera) memakai data awan titik. Penentuan hasil secara tradisional dilakukan dengan pengukuran manual yang memakan waktu dan tenaga kerja. Penulis menyatakan bahwa atribut geometri yang diperoleh dari LiDAR saja masih membatasi akurasi identifikasi hasil, dan pengenalan berbasis citra memerlukan banyak data latih serta sensitif terhadap kondisi teduh atau terang berlebih. Kajian ini menguji penggunaan ruang warna RGB dan YUV untuk memisahkan awan titik buah, lalu membangun algoritme mean shift termodifikasi untuk mengekstraksi dan menghitung buah dari hasil pemindaian darat (terrestrial laser scanning, TLS).

Wilayah kajian berada di Kabupaten Changsha, Provinsi Hunan, Tiongkok tengah, dengan iklim monsun subtropis dan tanah merah asam. Varietas yang ditanam adalah seri Xianglin. Pengambilan data lapang dilakukan pada November 2019 pada lima petak contoh yang dipilih secara acak; sebanyak 79 pohon dicatat jumlah buahnya, dengan total 19.066 buah, rata-rata 241 buah per pohon, maksimum 593, minimum 38, dan jari-jari rata-rata buah 2,0 cm. Awan titik diperoleh dengan pemindai Faro Focus 3D X330 pada resolusi 1/4 dan mutu 4X. Setiap petak dipindai dari lima stasiun, yaitu satu di tengah dan empat di batas petak secara searah jarum jam, dengan bola standar untuk menyambung hasil antarstasiun. Data mentah dibersihkan di perangkat lunak FARO Scene sehingga hanya awan titik cabang, daun, dan buah yang dipertahankan.

Proses identifikasi terdiri dari empat tahap: akuisisi dan praproses awan titik, pemisahan awan titik buah, pengelompokan awan titik buah, dan evaluasi akurasi. Pemisahan memakai ambang nilai warna: pada RGB, buah matang dipisahkan dari daun dan cabang berdasarkan perbandingan nilai merah dan hijau; pada YUV, nilai kecerahan dan perbedaan warna dihitung dari RGB dan dipisahkan satu sama lain sehingga perubahan kecerahan tidak mengubah ciri warna target. Pengelompokan memakai mean shift termodifikasi. Titik sembarang dipilih sebagai pusat kelompok, titik dalam jari-jari 2 cm (sama dengan jari-jari buah terukur) dikumpulkan, rata-rata koordinatnya dijadikan pusat baru, dan dua kelompok digabung apabila jarak antarpusatnya tidak melebihi ambang konvergensi berupa jari-jari rata-rata buah. Langkah ini dimaksudkan mengatasi pemindaian yang tidak lengkap dan mengurangi deteksi ganda maupun terlewat. Algoritme pembanding adalah mean shift biasa, DBSCAN, dan maximum-minimum distance clustering.

Akurasi dinilai dengan laju deteksi rata-rata P, yaitu rata-rata dari jumlah buah terdeteksi dibagi jumlah buah aktual per pohon, serta varians D dari laju deteksi antarpohon. Pada ruang RGB, mean shift termodifikasi menghasilkan P sebesar 79,33% dengan 14.929 buah terdeteksi dan varians 0,0127, dibandingkan 70,29% untuk mean shift biasa, 75,42% untuk maximum-minimum distance, dan 24,80% untuk DBSCAN. Pada ruang YUV, mean shift termodifikasi menghasilkan P sebesar 81,73% dengan 15.210 buah terdeteksi dan varians 0,0134, dibandingkan 74,68%, 70,95%, dan 19,38% untuk ketiga metode pembanding. Laju deteksi metode usulan lebih tinggi 2,4% di ruang YUV daripada di ruang RGB. Kepadatan awan titik hasil pemisahan YUV lebih tinggi 51,94% daripada RGB; pada satu pohon contoh, jumlah titik buah yang terekstraksi berturut-turut adalah 8.839 dan 1.485. Abstrak mencantumkan angka peningkatan 9,02% dan 7,05% terhadap mean shift biasa pada RGB dan YUV, serta 54,53% dan 62,35% terhadap DBSCAN.

Penulis menyebut sejumlah sumber ketidakpastian. Kesalahan alat meliputi galat sensor laser akibat refraksi atmosfer, getaran atau pergeseran titik pusat pemindai, dan galat penyambungan awan titik; akuisisi dihindari pada cuaca dengan cahaya langsung kuat. Kanopi yang terlalu besar memperkuat efek naung dan penutupan daun sehingga bagian awan titik hilang; penulis menggunakan petak berisi sedikit pohon dan banyak stasiun pemindaian untuk menguranginya. Ruang RGB sensitif terhadap cahaya, sedangkan DBSCAN sensitif terhadap kepadatan dan kecenderungan buah bergerombol, dan maximum-minimum distance terganggu oleh pusat awal yang terlalu rapat. Penulis juga menyatakan LiDAR memiliki jangkauan terbatas dan tidak memiliki informasi spektral, sehingga menggabungkannya dengan data penginderaan jauh lain atau memakai metode pembelajaran mesin menjadi arah lanjutan; tidak ada uji statistik atau interval kepercayaan yang dilaporkan untuk perbedaan laju deteksi tersebut.

