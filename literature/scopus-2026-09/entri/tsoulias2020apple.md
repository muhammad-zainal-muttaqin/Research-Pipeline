# Apple shape detection based on geometric and radiometric features using a LiDAR laser scanner

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tsoulias2020apple` |
| Judul asli | Apple shape detection based on geometric and radiometric features using a LiDAR laser scanner |
| Penulis | Tsoulias, Nikos; Paraforos, Dimitrios S.; Xanthopoulos, George; Zude-Sasse, Manuela |
| Tahun | 2020 |
| Venue | Remote Sensing |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [tsoulias2020apple.pdf](../pdf/tsoulias2020apple.pdf)
- DOI resmi: https://doi.org/10.3390/rs12152481

## Gambaran Umum

Penelitian ini mengusulkan metode segmentasi, lokalisasi, dan pengukuran ukuran apel di pohon memakai data awan titik LiDAR. Penulis menyatakan sistem pemantauan hasil buah selama ini banyak bergantung pada fitur warna yang peka terhadap perubahan cahaya, sehingga diskriminasi buah menjadi sulit. Tujuan penelitian adalah mengklasifikasikan titik tiga dimensi apel berdasarkan reflektansi dan fitur geometri, mengembangkan algoritma segmentasi untuk mengukur diameter buah pada pohon yang didefoliasi, dan mengevaluasi metode tersebut pada pohon berdaun di beberapa tahap pertumbuhan.

Data dikumpulkan pada musim tanam 2019 di stasiun percobaan ATB di Marquardt, Jerman, pada apel *Malus × domestica* Borkh. ‘Gala’ dengan batang bawah M9. Kebun seluas 0,37 ha memakai bentuk tall slender spindle dengan jarak antarpohon 0,95 m dan tinggi maksimum 3,3 m, serta empat kawat horizontal sebagai batas zona tinggi. Pemindaian dilakukan pada 42, 72, 104, dan 120 hari setelah pembungaan penuh (DAFB); pada setiap tanggal, dua pohon dipindai dalam keadaan berdaun (TL) lalu setelah defoliasi (TD), sehingga total delapan pohon. Setelah pemindaian, buah dihitung manual di pohon dan diameternya diukur di laboratorium setelah panen. Sensor LiDAR Sick LMS-511 dipasang vertikal 1,6 m di atas tanah pada rangka traktor dengan resolusi sudut 0,1667°, laju 25 Hz, sudut sapuan 190°, dan kecepatan traktor 0,13 m/s. Intensitas hamburan balik dikalibrasi dengan target putih barium sulfat dan uretan hitam menjadi RToF persen pada 905 nm. Unit pengukur inersia XSENS MTi-G-710 dan penerima RTK-GNSS Trimble AgGPS 542 dipakai untuk koreksi orientasi dan georujukan titik.

Mekanisme deteksi memakai fitur radiometrik RToF dan fitur geometri turunan dekomposisi matriks kovarians pada tetangga terdekat. Fitur linearitas L = (λ1 − λ2)/λ1 dipakai untuk memisahkan daun dan bagian kayu, sedangkan fitur kelengkungan C = λ3/(λ1 + λ2 + λ3) dipakai untuk membedakan titik apel; kedua nilai diskalakan 0–100. Kalibrasi pada dua pohon TD di DAFB120 menghasilkan ambang Rth = 76,1%, Cth = 73,2%, dan Lth = 15,5%, yang diterapkan kembali pada data TL. Clustering memakai DBSCAN dengan radius tetangga sama dengan diameter rata-rata hasil ukuran manual per zona kawat dan minimum sepuluh tetangga, lalu k-means untuk menentukan pusat buah. Bola dengan jari-jari sama dengan diameter perkiraan ditempatkan di setiap pusat untuk menyertakan titik tepi; klaster yang berisi dua atau tiga buah dipartisi berulang, dan bola yang jarak pusatnya di bawah diameter minimum digabung. Untuk evaluasi TL, klaster TD menjadi acuan hitung: pusat TL yang tumpang tindih lebih dari 50% dengan pusat TD dihitung sebagai benar positif, sedangkan klaster berdiameter di bawah diameter minimum dihitung sebagai positif palsu.

Hasil kalibrasi menunjukkan ambang Rth 76,1%, Cth 73,2%, dan Lth 15,5%. Diameter hasil LiDAR pada pohon TD memiliki R²adj = 0,95 dengan RMSE 9,5% pada DAFB120; nilai R²adj tertinggi per zona adalah 0,95 di ΔW4-3 pada DAFB104 dengan RMSE 4,1%. Jumlah buah yang terdeteksi pada pohon berdaun terhadap acuan TD berturut-turut adalah 88,6% pada DAFB42, 85,4% pada DAFB72, 88,5% pada DAFB104, dan 94,8% pada DAFB120. Kinerja tertinggi terjadi di zona ΔW4-3 pada DAFB120 dengan presisi 88,2%, recall 91,0%, dan skor F1 89,5%. Selisih posisi pusat buah TL terhadap TD memberikan RMSE terbaik 5,7% pada DAFB120 dan terburuk 19,9% pada DAFB42; selisih diameter memberi RMSE 9,5% pada DAFB120. Validasi silang memakai ambang dari DAFB120 pada enam pohon dari tiga tanggal sebelumnya. Waktu pemrosesan adalah 13 s per pohon pada komputer dengan prosesor Intel Core i7-8750H dan memori 16 GB.

Penulis menyatakan bagian kayu di zona bawah memiliki nilai RToF dan C yang mirip apel sehingga menambah positif palsu, sementara oklusi daun dan cabang menyebabkan buah terlewat. Radius DBSCAN yang tetap berdasarkan ukuran buah di DAFB120 menyebabkan ketidaksesuaian pada buah yang lebih kecil di tahap awal, dan bentuk apel yang tidak tepat berbola menimbulkan galat pada estimasi diameter. Penulis juga menyatakan bebuahan per pohon memengaruhi ukuran buah dan akhirnya menurunkan proporsi deteksi, lalu menyarankan pengujian pada kultivar lain dengan bentuk kurang bulat dan sifat permukaan berbeda.

