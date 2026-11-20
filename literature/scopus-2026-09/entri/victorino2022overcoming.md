# Overcoming the challenge of bunch occlusion by leaves for vineyard yield estimation using image analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `victorino2022overcoming` |
| Judul asli | Overcoming the challenge of bunch occlusion by leaves for vineyard yield estimation using image analysis |
| Penulis | Victorino, Gon\ccalo; Braga, Ricardo Pereira; Santos-Victor, Jos\'e; Lopes, Carlos Manuel |
| Tahun | 2022 |
| Venue | Oeno One |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [victorino2022overcoming.pdf](../pdf/victorino2022overcoming.pdf)
- DOI resmi: https://doi.org/10.20870/oeno-one.2022.56.1.4863

## Gambaran Umum

Estimasi hasil panen yang akurat penting bagi seluruh rantai produksi anggur, mulai dari perencanaan logistik panen hingga pengelolaan stok anggur di ruang produksi. Metode konvensional mengambil sampel tandan pada fase *berry lag* (BBCH 79), lalu menghitung dan menimbang hasilnya. Cara ini bersifat destruktif, padat tenaga kerja, dan dapat keliru bila sampel tidak mewakili kebun. Di sisi lain, citra dapat dikumpulkan secara masif dan dikaitkan dengan posisi geografis. Tantangan utama analisis citra adalah oklusi, yaitu tandan yang tertutup daun sehingga tidak terlihat oleh kamera. Penelitian ini bertujuan mengatasi tantangan tersebut. Penulis memakai fitur kanopi dari citra 2D, yaitu *canopy porosity* dan luas tandan yang terlihat, sebagai proksi untuk memperkirakan proporsi tandan yang terpapar, yang disebut *bunch exposure* (BE). Dengan cara ini, hasil panen dapat diestimasi secara otomatis tanpa gangguan pada kanopi.

Data penelitian dikumpulkan dari tiga varietas anggur, yaitu Arinto, Encruzado, dan Syrah. Citra diambil pada segmen tanaman sepanjang 1 m, pada dua tahap fenologi, yaitu *veraison* dan kematangan penuh (harvest). Tanaman diamati dalam kondisi tidak didefoliasi dan sebagian didefoliasi. Pengukuran dilakukan secara *proximal sensing*, yakni dari jarak dekat ke tanaman. Sebanyak 70 % dari seluruh data dipakai sebagai data latih, dan sisanya sebagai data validasi. Grafik pada data latih memuat 97 pengamatan pada *veraison* dan 107 pengamatan pada harvest. Menurut varietas, jumlahnya 57 untuk Arinto, 73 untuk Encruzado, dan 74 untuk Syrah. Persentase tandan terlihat berkisar antara 16 sampai 64 %. Penulis tidak menyebutkan jumlah total citra pada bagian yang dikutip di atas.

Model BE dibangun dengan regresi berganda yang memakai *canopy porosity* dan luas tandan terlihat sebagai prediktor. Model ini menjelaskan BE dengan R2 0,70 sampai 0,84 pada data latih, dan 10 sampai 43 % lebih kuat daripada prediktor tunggal. Model gabungan semua varietas dan tahap fenologi dipilih untuk estimasi BE dan menghasilkan R2 = 0,80 pada data validasi. Model ini tidak menunjukkan perbedaan metrik validasi antara *veraison* dan harvest. Nilai BE kemudian dipakai untuk menghitung total luas tandan (tBA). Galat tBA rendah, yaitu di bawah 10 %, kecuali pada Arinto yang memiliki daun dan tandan besar. Estimasi hasil dari tBA menghasilkan galat 0,2 % pada data gabungan validasi. Konversi luas ke massa yang sederhana kurang akurat pada Syrah. Pada tahap harvest dan pada kedua tahap Arinto, galat absolut massa buah melampaui 10 %. Sebagian besar kumpulan data lain memiliki galat absolut di bawah 5 %.

Penulis menyatakan beberapa batasan. Model BE hanya memperhitungkan oklusi oleh daun, bukan oklusi antartandan. Konversi luas tandan ke massa bersifat linear dan belum memperhitungkan pertumbuhan buah dari *veraison* sampai panen. Untuk estimasi hasil, massa pada *veraison* masih perlu dikalikan faktor pertumbuhan berbasis data historis. Penulis juga menyebut bahwa perbedaan kemiringan antartahap fenologi menunjukkan konversi luas ke massa belum universal. Karena itu, penulis menilai diperlukan fitur citra tambahan atau data kebun lain untuk model yang lebih umum. Kanopi yang sangat rapat dengan sedikit tandan terlihat tetap menjadi tantangan. Penulis menyebut bahwa sensor seperti ultrasonik atau perangkat yang dapat melihat tembus daun mungkin diperlukan, tetapi belum praktis di lapangan.
