# Seeing the Fruit for the Leaves: Robotically Mapping Apple Fruitlets in a Commercial Orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `qureshi2023seeing` |
| Judul asli | Seeing the Fruit for the Leaves: Robotically Mapping Apple Fruitlets in a Commercial Orchard |
| Penulis | Qureshi, Ans; Smith, David; Gee, Trevor; Nejati, Mahla; Shahabi, Jalil; Lim, JongYoon; Ahn, Ho Seok; McGuinness, Ben; Downes, Catherine; Jangali, Rahul; Black, Kale; Lim, Hin; Duke, Mike; MacDonald, Bruce; Williams, Henry |
| Tahun | 2023 |
| Venue | IEEE International Conference on Intelligent Robots and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [qureshi2023seeing.pdf](../pdf/qureshi2023seeing.pdf)
- DOI resmi: https://doi.org/10.1109/iros55552.2023.10341502

## Gambaran Umum

Makalah ini menyajikan sistem penglihatan dari robot penjarangan buah apel muda (*fruitlet*) bernama Archie Snr, yang dikembangkan di Aotearoa Selandia Baru untuk mengatasi kekurangan tenaga kerja musiman. Robot mengangkangi struktur tajuk 2D setinggi 3,4 m dan memindai tiap cabang dari dua sisi dengan kamera stereo pada lengan UR5. Tujuannya adalah memetakan buah muda pada tiap cabang dan menghitung beban buah (*crop load*) per pohon sebagai dasar rekomendasi penjarangan.

Evaluasi dilakukan di kebun apel komersial di Hastings, Selandia Baru, pada musim penjarangan 2022, dengan pohon dewasa pada sistem tanam 2D. Sepuluh cabang dipindai dari dua sisi dan dibandingkan dengan hitungan manual seluruh buah muda pada tiap cabang. Hasil utama: akurasi hitungan pemindaian dua sisi 81,17%, dibandingkan 73,7% pada pemindaian satu sisi, dan estimasi diameter buah muda dengan RMSE 5,9% dari ukuran sebenarnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Industri apel dan pir Selandia Baru bernilai ekspor 917 juta dolar dan mengalami kekurangan pekerja terampil. Penjarangan buah muda saat ini memakai hitungan manual pada pohon terpilih untuk memperkirakan beban, dan perkiraan itu mengarahkan pekerja secara tidak konsisten. Mitra hortikultura penulis memperkirakan kenaikan mutu 10 sampai 30% bila beban tiap pohon diukur akurat dan aturan penjarangan khusus pohon diterapkan.

Tantangannya adalah daun lebat yang menyembunyikan buah muda sebagian atau seluruhnya dari satu sudut pandang, dan buah muda yang tumbuh bergerombol saling menutupi. Penulis menyebut tinjauan pustaka terdahulu: model prediksi musiman berbasis data besar tidak cukup presisi pada tingkat kebun atau pohon; menambah sudut pandang membantu melihat buah tersembunyi tetapi menuntut pelacakan objek yang akurat karena buah tampak serupa, dan bila tidak dikendalikan menyebabkan penghitungan ganda. Salah satu studi terdahulu (Stein dkk., mangga) memakai 37 citra di sekitar pohon dengan proyeksi epipolar dan LIDAR, dengan galat 1,36% pada 16 pohon terhadap hitungan panen, tetapi penghitungan ganda dikatakan diimbangi oleh buah tersembunyi yang tidak terdeteksi. Karya terdahulu penulis memakai platform satu sisi dengan akurasi 84% dan presisi 87%, tetapi hanya dievaluasi terhadap buah yang terlihat pada pemindaian, bukan jumlah sebenarnya pada pohon.

## Ide Utama

Gagasannya adalah memindai kedua sisi cabang dari platform yang mengangkangi pohon, mendeteksi buah muda di tiap pandangan dengan segmentasi instans, mengekstrak bola 3D dari kedalaman stereo, dan menggabungkan hasil dari banyak titik pandang menjadi peta 3D tanpa duplikat. Peta dua sisi disejajarkan secara geometris dengan papan Charuco sebagai titik acuan bersama. Pengangkangan dipilih untuk tiga alasan: menghilangkan silau saat matahari rendah (dan memungkinkan operasi malam hari dengan pencahayaan internal), menghilangkan dampak angin yang mengganggu registrasi, dan menjangkau buah muda yang tidak terlihat dari satu sisi.

## Cara Kerja Langkah demi Langkah

```
 stereo (UR5, 40 titik pandang/sisi) ─> Mask R-CNN (masker 2D)
        └─> HSMnet (kedalaman) ──────────────┤
                                             v
        masker + kedalaman -> titik 3D -> sphere fitting RANSAC
                                             v
   gabung dengan buah muda terdahulu (posisi, ukuran dirata-rata)
                                             v
     peta per sisi + penyejajaran Charuco -> peta dua sisi
```

### 1. Platform dan akuisisi

Archie Snr membawa dua lengan UR5 pada rel linear di kedua sisi, masing-masing berisi sepasang kamera stereo Basler acA2440-35uc (USB 3.0, resolusi 2056 × 2464, lensa Kowa F1,8 dengan panjang fokus 5 mm). Garis dasar stereo 100 mm, jarak kerja 300 sampai 600 mm (kamera ditempatkan 300 sampai 400 mm dari pusat cabang), dan resolusi kedalaman 1,10 mm per piksel galat pencocokan pada jarak 0,4 m (disparitas 362 piksel). Sinkronisasi memakai pemicu perangkat keras 20 Hz. Kalibrasi tangan-mata memakai OpenCV dan Charuco untuk kamera dan ViSP untuk pasangan UR5 dan stereo. Satu pemindaian cabang terdiri dari empat lintasan busur berjarak 15 mm sepanjang lebar cabang, tiap busur 10 titik, sehingga 40 titik pandang pada tiap sisi sepanjang 900 mm cabang. Papan Charuco di dasar pohon menjadi acuan bersama kedua sisi.

### 2. Deteksi buah muda

Deteksi memakai segmentasi instans pada kerangka Detectron2. Dataset latih terdiri dari 638 instans buah muda pada 38 citra dari beberapa kebun dengan variasi pencahayaan, dianotasi dengan Supervisely. Model akhir adalah Mask R-CNN dengan tulang punggung ResNeXt-101 dan mencapai mAP 0,5. Anotasi dijaga agar masker tidak mencakup daun atau latar, karena masker yang tercemar menghasilkan deteksi 3D yang salah.

### 3. Inferensi stereo

Kedalaman diperoleh dengan HSMnet (jaringan stereo hierarkis untuk citra resolusi tinggi) model pralatih, dipilih karena galat rerata terendah pada Middlebury v3 untuk citra resolusi tinggi per pertengahan 2021 (avgerr 2,07). Pelatihan khusus tidak mungkin karena tidak ada kedalaman acuan. Satu-satunya modifikasi adalah jendela terpotong di sekitar maksimum lokal pada regresi kedalaman berbobot untuk mengurangi derau di diskontinuitas.

### 4. Ekstraksi dan penggabungan buah muda

Masker 2D diselaraskan dengan kedalaman untuk memperoleh awan titik tiap buah muda. Bola dicocokkan dengan RANSAC dalam dua tahap: titik tengah dari rerata koordinat dan diameter dari rerata jarak titik sebagai nilai awal; titik di luar bola dan titik dengan kedalaman di bawah kedalaman minimum awan titik tidak dianggap inlier. Jumlah titik dibatasi sebelum RANSAC. Setiap buah muda diberi ID hitungan dan digabung dengan buah muda yang dihasilkan pada iterasi berikutnya untuk menghindari duplikasi; pada tiap penggabungan, posisi dan ukuran dirata-rata.

## Eksperimen dan Hasil

Pengujian dilakukan pada kebun apel komersial Hastings selama dua minggu pada musim penjarangan 2022 dengan pohon dewasa berumur lima tahun pada struktur 2D yang tidak dipangkas atau diubah. Platform dikemudikan manual ke depan segmen cabang, siang hari dengan pencahayaan bervariasi. Sebanyak 10 cabang dipindai dan dibandingkan dengan acuan: tiap buah muda pada cabang dihitung manual dan diameternya diukur dengan jangka sorong pada titik terlebar. Kultivar apel tidak dilaporkan. Akurasi dihitung sebagai $1 - |hitungan - acuan| / acuan$ dikali 100.

Ringkasan Tabel I (rerata atas 10 cabang):

| Skema | Akurasi (%) | Presisi | Recall | F1 |
|---|---|---|---|---|
| Satu sisi (rerata sisi A dan B) | 73,7 | 0,907 | 0,924 | 0,913 |
| Dua sisi (gabungan) | 81,167 | 0,803 | 0,926 | 0,856 |

Nilai per cabang pada Tabel I memperlihatkan variasi besar. Misalnya, pada cabang 1 acuan 52 buah muda, sisi A menghitung 29 dan sisi B 35, sedangkan gabungan menghitung 63 (akurasi 78,84%). Pada cabang 3 (acuan 61), sisi A 45 dan sisi B 30, gabungan 59 (96,72%). Pada cabang 5 (acuan 46), sisi A 42 dan sisi B 45, gabungan 59 (71,73%). Pada cabang 6 (acuan 59), gabungan 78 (67,79%), dan pada cabang 10 (acuan 50), gabungan 70 (60%). Hasil gabungan di atas acuan menunjukkan penghitungan berlebih. Estimasi ukuran: diameter terhitung 100 buah muda dibandingkan dengan acuan menghasilkan RMSE 5,9% (Gambar 7), dengan bias ke arah buah muda yang lebih besar karena pendekatan jarak titik rerata pada RANSAC.

Menurut penulis, *recall* tinggi pemindaian satu sisi (92,4%) menunjukkan keefektifan pendekatan multipandang karena buah yang tersembunyi dari satu pandangan terdeteksi dari pandangan lain. Akurasi terhadap hitungan sebenarnya hanya 73,7% karena satu sisi tidak dapat melihat semua buah di balik daun (penghitungan kurang). Penggabungan dua sisi menaikkan akurasi dari 73,7% menjadi 81,17%, tetapi presisi turun dari 90,7% menjadi 80,3% akibat positif palsu tambahan dari sisi lain.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: evaluasi dilakukan terhadap hitungan sebenarnya seluruh buah muda pada cabang (bukan hanya yang terlihat), pemindaian dua sisi terbukti menaikkan akurasi, pengangkangan tajuk mengendalikan silau dan angin, serta sistem memperkirakan ukuran buah muda sekaligus.

Keterbatasan yang dinyatakan penulis: pensejajaran dua sisi bertumpu pada estimasi posisi papan Charuco dan perlu diperbaiki karena menimbulkan hitungan berlebih; pencocokan berbasis ambang ukuran bola meredam penghitungan berlebih tetapi menimbulkan penghitungan kurang; penaksiran diameter bias ke buah muda yang lebih besar. Penulis menyatakan penelitian lanjutan akan mengurangi hitungan berlebih dan bias ukuran.

Menurut pembacaan ringkasan ini, evaluasi hanya mencakup 10 cabang di satu kebun, satu musim, tanpa uji pada tingkat pohon utuh, sehingga klaim penghitungan beban per pohon belum didukung data. Menurut pembacaan ringkasan ini, mAP detektor 0,5 dari hanya 38 citra latih tergolong rendah, dan teks tidak menjelaskan bagaimana mAP itu diukur atau berapa data validasinya. Menurut pembacaan ringkasan ini, makalah tidak memuat ablasi untuk ambang penggabungan, sehingga kontribusi tiap komponen terhadap penghitungan ganda tidak dapat dipisahkan, dan kesimpulan menyebut angka presisi dan recall satu sisi (92,4% keduanya) yang tidak sama dengan Tabel I (presisi 0,907).

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dan menyebut penghitungan ganda sebagai persoalan. Mekanismenya adalah rekonstruksi 3D dari stereo berlapis registrasi: tiap buah muda dimodelkan sebagai bola 3D, buah baru digabung dengan buah muda yang sudah ada pada peta (posisi dan ukuran dirata-rata), dan peta dua sisi diselaraskan memakai papan Charuco bersama. Penggabungan memakai kedekatan 3D, bukan kemiripan tampilan. Persoalan inti tinjauan, yaitu identitas lintas dua sisi, terlihat jelas: penggabungan dua sisi menaikkan *recall* tetapi menurunkan presisi karena hitungan berlebih akibat pensejajaran yang tidak sempurna.

Hitungan tidak dilaporkan per kelas (satu kelas, buah muda apel). Acuan hitungan adalah hitungan manual lapangan pada cabang yang sama (bukan panen atau anotasi citra), dan diameter diukur dengan jangka sorong. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah desain evaluasi terhadap hitungan sebenarnya pada kedua sisi, pemakaian titik acuan bersama untuk menyejajarkan sisi, dan pelaporan presisi dan *recall* terpisah untuk membedakan hitungan berlebih dari hitungan kurang. Keterbatasan pemindahan: sistem memerlukan platform pengangkang, struktur tajuk 2D yang pipih, dan kamera stereo pada jarak dekat, sedangkan tajuk kelapa sawit tinggi dan tiga dimensi.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `qureshi2023seeing`.

Ringkasan yang aman dikutip: Qureshi dkk. (2023) memaparkan sistem penglihatan robot penjarangan apel yang mengangkangi tajuk 2D dan memindai cabang dari dua sisi dengan stereo, segmentasi instans Mask R-CNN, dan pencocokan bola RANSAC, dengan penggabungan buah muda antartitik pandang. Pada 10 cabang di kebun komersial, akurasi hitungan terhadap hitungan manual naik dari 73,7% (satu sisi) menjadi 81,17% (dua sisi), dengan presisi turun dari 0,907 menjadi 0,803 dan estimasi diameter dengan RMSE 5,9%.

Catatan verifikasi data: Angka akurasi, presisi, *recall*, dan F1 dibaca dari Tabel I (baris rerata), dan RMSE 5,9% dari Bagian VI (Gambar 7 tidak terbaca). Jumlah label (638 instans pada 38 citra) dan mAP 0,5 berasal dari Bagian IV-A. Teks ekstraksi arXiv:2308.07512v1 terbaca baik, dengan tabel berurutan kolom per baris. Ada ketidakkonsistenan di makalah: kesimpulan menyebut presisi dan *recall* satu sisi 92,4%, sedangkan Tabel I memberi presisi 0,907 dan *recall* 0,924, dan Bagian VII menyebut presisi 90,7%; ringkasan ini memakai Tabel I. Akurasi satu sisi tertera sebagai rerata nilai per sisi dengan pembanding hitungan sebenarnya seluruh cabang. Kultivar dan jumlah pohon tidak dilaporkan.
