# Automated Crop Yield Estimation for Apple Orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2013automated` |
| Judul asli | Automated Crop Yield Estimation for Apple Orchards |
| Penulis | Wang, Qi; Nuske, Stephen; Bergerman, Marcel; Singh, Sanjiv |
| Tahun | 2013 |
| Venue | Springer Tracts in Advanced Robotics |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wang2013automated.pdf](../pdf/wang2013automated.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-00065-7_50

## Gambaran Umum
Makalah ini (prosiding *International Symposium on Experimental Robotics*, Juni 2012) menyajikan sistem berbasis penglihatan komputer untuk estimasi hasil panen apel secara otomatis dengan cara menghitung buah. Sistem memakai sepasang kamera stereo (*stereo rig*) yang dipasang pada kendaraan kebun otonom, bekerja pada malam hari dengan pencahayaan buatan terkendali, dan memindai kedua sisi setiap baris pohon. Buah dideteksi pada setiap bingkai, diregistrasi lintas bingkai dan lintas sisi baris berdasarkan koordinat global, lalu dihitung sebagai estimasi hasil.

Sistem diuji di Sunrise Orchard, Washington State University, Rock Island, WA, pada September 2011, pada dua blok pohon sistem tanam *tall spindle*: Red Delicious (apel merah) dan Granny Smith (apel hijau). Acuan hitungan adalah hitungan manual oleh pekerja kebun profesional per seksi tiga pohon.

Hasil utama: galat estimasi -3,2% untuk blok apel merah (sekitar 480 pohon; baris 1-10 yang dijarangkan buahnya) dan 1,2% untuk blok apel hijau (sekitar 670 pohon) setelah kalibrasi linear dengan sampel manual 10 seksi. Tanpa kalibrasi, hitungan apel hijau kurang hitung rata-rata 29,8% per baris, dan baris tidak dijarangkan pada blok merah kurang hitung 41,3%.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil panen apel lazimnya didasarkan pada data historis, kondisi cuaca, dan hitungan manual pada beberapa lokasi sampel. Cara itu memakan waktu, padat tenaga kerja, dan sampelnya terbatas sehingga kurang mewakili sebaran hasil, terutama pada kebun yang variabilitas spasialnya tinggi. Penulis menyatakan belum ada penelitian yang menghasilkan estimasi hasil apel yang memuaskan; riset sebelumnya hanya menangani deteksi apel pada satu atau beberapa pemandangan kebun tanpa pencacahan berkelanjutan, atau memakai kepadatan bunga yang korelasinya dengan hasil berubah dari tahun ke tahun.

Penulis mengidentifikasi tiga tantangan: (1) variasi pencahayaan alami, (2) oklusi buah oleh daun, dahan, dan buah lain, dan (3) deteksi ganda apel yang sama pada citra berurutan, yang menyebabkan salah hitung bila registrasi gagal.

## Ide Utama
Setiap tantangan dijawab oleh satu komponen. Pencahayaan malam dengan lampu kilat cincin (*ring flash*) mengurangi variasi cahaya alami. Pemindaian berurutan dari kedua sisi baris memberi banyak sudut pandang pada tiap pohon sehingga oklusi berkurang. Posisi geografis tiap apel dihitung dari triangulasi stereo dan pose kendaraan, lalu deteksi yang berdekatan di koordinat global digabung sebagai satu apel untuk mencegah hitungan ganda.

Oklusi yang tersisa (apel yang tidak terlihat sama sekali) dikompensasi dengan faktor kalibrasi yang diperoleh dari regresi linear antara hitungan komputer dan hitungan manual pada sampel kecil.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Perangkat keras terdiri atas dua kamera Nikon D300s dengan lensa sudut lebar (panjang fokus 11 mm), dipasang pada batang aluminium berjarak sekitar 0,28 m dan dipicu serempak pada 1 Hz. Pencahayaan memakai lampu kilat cincin AlienBees ABR800 dengan energi 20 Ws; kamera diatur pada apertur f/6,3, kecepatan rana 1/250 s, dan ISO 400 untuk pohon pada jarak sekitar 2 m. Kendaraan kebun otonom Carnegie Mellon melaju mengikuti baris pohon pada 0,25 m/s, dan sistem penentu posisi presisi POS LV (Applanix) menyediakan koordinat kendaraan. Citra berukuran 1072 × 712 piksel. Pengolahan dilakukan luring dengan Matlab 2010a; kontrol akuisisi daring ditulis dalam Python.

### 2. Deteksi apel merah
Citra dikoreksi distorsinya, lalu piksel apel merah disegmentasi di ruang warna HSV: hue 0° sampai 9° atau 349° sampai 360°, dengan piksel latar berjenuh (*saturation*) atau nilai (*value*) di bawah atau sama dengan 0,1 dibuang.

### 3. Deteksi apel hijau
Hue apel hijau dan daun berada pada 49° sampai 75° (dari analisis 10 citra contoh). Apel dipisahkan dari daun dengan ambang saturasi 0,8 atau lebih. Karena pantulan spekular dari lampu kilat membuat bagian tengah apel hijau berkurang saturasinya, pantulan itu dideteksi dengan mencari maksimum lokal pada peta keabuan (tetangga 30% sisi pendek wilayah) dan memeriksa profil intensitas pada empat garis (0°, 45°, 90°, 135°; panjang 21 piksel). Skor kebulatan total $R$ dari delapan bagian garis; maksimum lokal dianggap pantulan spekular bila $R \ge 4$. Hasilnya digabung dengan piksel saturasi beserta tetangga 18 × 18 piksel.

### 4. Segmentasi apel individual
Diameter rata-rata $D$ diperkirakan dari wilayah yang relatif bulat (eksentrisitas $0 < E < 0{,}6$) setelah derau berluas kecil dibuang. Wilayah dengan sumbu mayor lebih dari $2D$ dianggap dua apel bersentuhan dan dipisah menjadi tepat dua apel (perangkat lunak saat ini hanya memisah menjadi dua karena tandan apel pada kebun komersial umumnya dijarangkan hingga dua buah). Dua wilayah yang pusatnya berjarak kurang dari $D$ dianggap satu apel yang terhalang sebagian.

### 5. Registrasi multi-citra
Posisi 3D tiap apel di kerangka kamera ditriangulasi dengan pencocokan blok (*block matching*) dua arah antara kamera bawah dan atas; deteksi yang tidak cocok timbal balik dibuang. Posisi ditransformasikan ke kerangka global (UTM dan elevasi). Satu apel dapat terlihat sampai tujuh kali dari satu sisi baris. Dari satu sisi, apel yang jaraknya kurang dari 0,05 m digabung dengan merata-ratakan posisinya; apel yang terdeteksi hanya sekali dan apel yang tingginya kurang dari 0,3 m (dianggap jatuh) dibuang sebagai derau.

### 6. Registrasi antar-sisi baris
Karena GPS bergeser (*drift*) pada ketinggian saat kendaraan kembali di sisi seberang dan triangulasi stereo cenderung menempatkan apel lebih dekat ke kamera, suku koreksi dihitung dari objek tetap di infrastruktur kebun (ujung tiang, patok, kawat; pita penanda tiap tiga pohon, posisinya saat ini dicatat manual pada citra). Setelah koreksi, apel dari kedua sisi yang berjarak kurang dari 0,16 m (sekitar dua kali diameter rata-rata apel) digabung.

## Eksperimen dan Hasil
Tiap blok seluas sekitar setengah acre: 15 baris apel merah dan 14 baris apel hijau, sekitar 48 pohon per baris. Setiap baris dibagi menjadi 16 seksi berisi tiga pohon, ditandai pita; acuan adalah hitungan manual pekerja kebun, dan algoritma dipaksa melaporkan hitungan per seksi dengan menandai pita pada citra secara manual. Hitungan dilaporkan total per seksi dan per baris, bukan per kelas.

| Kondisi | Galat estimasi | Catatan |
|---|---|---|
| Apel merah, baris 1-10 (dijarangkan), tanpa kalibrasi | -3,2% (blok gabungan); rerata per baris -2,9%, SD 7,1% | Tanpa kalibrasi |
| Apel merah, baris 11-15 (tidak dijarangkan), mentah | kurang hitung 41,3%; SD per baris 3,2% | Tandan besar, oklusi antarapel |
| Apel merah, baris 11-15, kalibrasi (faktor 1,7) | rerata per baris 0,4%, SD 5,5% | Kalibrasi sampel manual |
| Apel hijau, mentah | rerata per baris -29,8%, SD 8,1% | Oklusi daun |
| Apel hijau, kalibrasi (faktor 1,4) | rerata per baris 1,8%, SD 11,7%; blok total 1,2% | 10 seksi acak dari 224 |

Faktor kalibrasi apel hijau diperoleh dari regresi linear tanpa intersep pada 10 seksi acak; dari 100 pengulangan, rerata faktor 1,4 dengan SD 0,1. Peta hasil (*yield map*) resolusi tinggi per pohon juga dihasilkan dan dibandingkan secara visual dengan peta acuan (Gambar 14).

## Kelebihan dan Keterbatasan
Keterbatasan yang dinyatakan penulis: (1) perangkat lunak hanya memisah tandan menjadi dua apel, sehingga tandan lebih besar terhitung kurang; (2) apel berlebih cahaya (*overexposed*) atau bersunburn merah gagal lolos segmentasi hue hijau; (3) sebagian kecil deteksi positif palsu (anak daun muda, gulma, apel yang sangat dekat dengan kamera); (4) posisi pita penanda saat ini dicatat manual; (5) faktor kalibrasi bergantung pada sampel manual, dan pengaruh ukuran sampel, serta penggunaan ulang faktor dari tahun lain atau kebun lain, belum dipelajari; (6) penggabungan deteksi dari kedua sisi baris masih perlu ditingkatkan.

Menurut pembacaan ringkasan ini, bukti masih terbatas pada satu kebun, satu musim, dua varietas, dan sistem tanam berkanopi tipis; hasil blok hijau bergantung pada kalibrasi yang dicocokkan dengan data acuan blok yang sama, sehingga galat 1,2% bukan galat prediksi pada data yang belum dilihat. Metode registrasi bergantung pada geometri stereo dan posisi presisi, serta tidak memakai kemiripan tampilan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani apel yang terlihat lebih dari sekali pada dua tingkat. Pada tingkat pertama, deteksi berurutan dari satu sisi baris digabung bila jarak koordinat globalnya di bawah 0,05 m. Pada tingkat kedua, deteksi dari dua sisi baris digabung bila jarak di bawah 0,16 m setelah koreksi drift GPS dan bias stereo. Mekanismenya adalah pencocokan berbasis geometri (posisi 3D global), bukan pelacakan berbasis tampilan. Hitungan tidak dilaporkan per kelas, dan acuannya adalah hitungan manual di lapangan per seksi tiga pohon.

Untuk pencacahan tandan kelapa sawit multi-sisi, gagasan yang dapat dipindahkan adalah penggabungan dua tahap berbasis jarak pada koordinat bersama, pengoreksian bias sistematis antar-sisi memakai penanda tetap, dan kalibrasi hitungan terhadap sampel manual. Syarat kunci, yaitu posisi 3D yang presisi pada kerangka global, tidak dipenuhi oleh citra pohon sawit dari sisi yang diambil tanpa pose kamera presisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wang2013automated`.

Wang dkk. mengembangkan sistem estimasi hasil apel otomatis berbasis stereo yang memindai kedua sisi baris pohon pada malam hari dengan pencahayaan terkendali, mendeteksi apel dengan segmentasi warna HSV, dan mendaftarkan deteksi berulang berdasarkan koordinat global (ambang 0,05 m dari satu sisi dan 0,16 m antar-sisi) sebelum menghitungnya. Pada uji lapangan September 2011 di Washington, galat estimasi adalah -3,2% untuk blok Red Delicious (sekitar 480 pohon) dan 1,2% untuk blok Granny Smith (sekitar 670 pohon) setelah kalibrasi linear dengan sampel manual.

Catatan verifikasi data: Angka galat -3,2%, 1,2%, -2,9% (SD 7,1%), 41,3%, -29,8% (SD 8,1%), faktor kalibrasi 1,4 dan 1,7, serta galat setelah kalibrasi 1,8% dan 0,4% tertulis pada seksi 5.2 dan Kesimpulan. Ambang registrasi 0,05 m dan 0,16 m ada pada seksi 4; parameter kamera dan kendaraan pada seksi 2. Jumlah pohon (sekitar 480 dan 670) adalah perkiraan dari makalah. Jumlah apel absolut, jumlah citra, dan metrik presisi atau recall deteksi tidak dilaporkan dalam teks; nilai pada gambar (Gambar 9-11) tidak terbaca dari teks ekstraksi. Teks ekstraksi baik dan berbahasa Inggris.
