# Modeling and calibrating visual yield estimates in vineyards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nuske2014modeling` |
| Judul asli | Modeling and calibrating visual yield estimates in vineyards |
| Penulis | Nuske, Stephen; Gupta, Kamal; Narasimhan, Srinivasa; Singh, Sanjiv |
| Tahun | 2014 |
| Venue | Springer Tracts in Advanced Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [nuske2014modeling.pdf](../pdf/nuske2014modeling.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-642-40686-7_23

## Gambaran Umum

Penelitian ini bertujuan memprediksi hasil panen kebun anggur secara otomatis dan tidak destruktif serta memodelkan hubungan antara ukuran citra dan berat panen. Carabiaya peninjauan hasil panen selama ini bersifat destruktif, mahal, dan terlalu jarang untuk menangkap keragaman spasial. Penulis mengusulkan pengambilan citra dari kendaraan yang bergerak di antara barisan tanaman, deteksi buah pada citra, dan kalibrasi hasil hitungan buah terhadap berat panen.

Data berupa anggur dari tiga kultivar dan dua lokasi, yaitu Traminette dan Riesling di Fredonia, New York (September 2010, 10 hari menjelang panen, masing-masing 88 dan 124 pohon), serta Chardonnay di Modesto, California (Juni 2011, 90 hari menjelang panen, 648 pohon). Eksperimen lapang mencakup 860 pohon sepanjang 2,5 km dengan berat buah per pohon hasil panen manual sebagai kebenaran. Untuk menguji penutupan diri dalam tandan, penulis memotret 56 tandan Thompson Seedless di laboratorium dari beberapa arah pada jarak tetap, lalu menimbang dan menghitung jumlah buahnya. Peralatan terdiri atas kamera warna Nikon D300s menghadap samping, cincin lampu AlienBees ARB800, kamera stereo PointGrey BumbleBee2 menghadap sepanjang barisan, dan kotak sinkronisasi, semuanya dipasang pada rangka aluminium di bak traktor Kawasaki Mule. Posisi kamera dilacak dengan odometri visual dan dikoreksi dengan deteksi tiang penyangga yang berjarak tetap; penulis menganggap zona buah berada pada satu bidang pada kedalaman tiang dan memangkas citra yang tumpang tindih untuk menghindari penghitungan ganda.

Deteksi buah memakai transformasi simetri radial untuk mencari titik berbentuk buah pada rentang jari-jari yang ditentukan, lalu klasifikasi warna dan tekstur untuk membedakan buah dari daun yang warnanya serupa. Model hasil panen dinyatakan sebagai berat panen sama dengan jumlah buah dikalikan berat buah rata-rata. Jumlah buah yang terdeteksi dikoreksi oleh fungsi yang membagi hitungan itu dengan faktor-faktor bias: penutupan oleh buah dalam tandan yang sama, penutupan oleh tandan lain, penutupan oleh daun dan tunas, bias deteksi berupa buah terlewat atau salah terdeteksi, serta bias pendaftaran citra yang menyebabkan penghitungan ganda atau terlewat. Penulis juga menguji dua ukuran alternatif untuk tandan, yaitu luas *convex hull* dan model elipsoid, sebagai pengganti hitungan buah tampak. Dua cara kalibrasi diuji: sampel tangan destruktif pada saat pengambilan citra (15 pohon pada satu barisan) dan data panen tahun sebelumnya yang dinormalisasi terhadap berat buah, lalu diterapkan pada data tahun berikutnya.

Nilai r² dan galat kuadrat rata-rata pada data laboratorium berturut-turut sebesar 0,95 dan 9,3% untuk hitungan buah manual, 0,88 dan 15,4% untuk buah tampak, 0,85 dan 17% untuk model elipsoid, serta 0,92 dan 13,7% untuk *convex hull*. Pengukuran bias menunjukkan 46% buah tampak pada data laboratorium; bias deteksi sebesar 0,74, 0,75, dan 0,65 berturut-turut untuk Riesling, Traminette, dan Chardonnay; bias pendaftaran 1,0 pada data 2010 dan 1,03 pada Chardonnay 2011; serta gabungan penutupan oleh tanaman dan tandan sebesar 0,29, 0,24, dan 0,31. Pada prediksi hasil panen Chardonnay, galat absolut rata-rata per pohon berkisar 17–19%, galat per barisan 7–8%, dan galat total panen 3% dengan kalibrasi sampel tangan serta 4% dengan kalibrasi data Traminette 2010; kalibrasi data Riesling 2010 meramalkan lebih rendah 4,5%, sedangkan ekstrapolasi sampel tangan saja meramalkan lebih rendah 13%. Abstrak menyebut estimasi dalam 4% memakai data panen sebelumnya dan 3% memakai sampel tangan; tidak dinyatakan split latih/uji.

Penulis menyatakan beberapa batasan. Tidak semua buah tampak karena penutupan oleh buah lain, tandan, daun, dan tunas, sehingga hitungan citra harus dikalibrasi. Algoritme melaporkan 25–35% lebih sedikit buah daripada yang tampak, atau sekitar 10% lebih sedikit pada data Chardonnay yang diambil 90 hari menjelang panen. Pendaftaran otomatis pada data 2011 cenderung menghitung lebih banyak buah sebesar 3%. Ukuran *convex hull* dan elipsoid belum dipakai di lapang karena penulis belum memiliki metode memisahkan tandan yang berdekatan. Bias penutupan oleh tanaman dan tandan tidak diukur secara eksperimen, melainkan diturunkan tidak langsung dengan menganggap laju penutupan diri sama seperti di laboratorium; model elipsoid juga melanggar asumsi kerapatan seragam dan bentuk elipsoid. Penulis mengarahkan kerja berikutnya pada penghitungan tandan sebelum buah terbentuk dan perluasan pengujian ke lebih banyak kultivar serta sistem teralis.

