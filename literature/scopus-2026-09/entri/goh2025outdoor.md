# Outdoor RGB and Point Cloud Depth Dataset for Palm Oil Fresh Fruit Bunch Ripeness Classification and Localization

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `goh2025outdoor` |
| Judul asli | Outdoor RGB and Point Cloud Depth Dataset for Palm Oil Fresh Fruit Bunch Ripeness Classification and Localization |
| Penulis | Goh, Jin Yu; Mohamed Ali, Mohamed Sultan; Md Yunos, Yusri; Sheikh, Usman Ullah; Khan, Muhamad Salman |
| Tahun | 2025 |
| Venue | Scientific Data |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [goh2025outdoor.pdf](../pdf/goh2025outdoor.pdf)
- DOI resmi: https://doi.org/10.1038/s41597-025-04953-6

## Gambaran Umum

Kajian ini menyajikan dataset multi-modal untuk menilai kematangan dan lokasi tandan buah sawit (fresh fruit bunch, FFB) di kebun terbuka. Penulis menyatakan bahwa penilaian manual memiliki tingkat kesalahan 15-25% dan menurun ketika luas kebun melebihi 500 hektar per pemeriksa. Tinjauan pustaka penulis mendapati 87% dataset existing direkam di bawah pencahayaan buatan dan hanya 13% yang mencerminkan variasi lingkungan nyata, serta belum ada dataset publik yang memuat peta kedalaman atau awan titik dari pohon sawit di luar ruangan. Tujuan kajian adalah mengisi kekosongan itu dengan data RGB, peta kedalaman, dan awan titik yang direkam pada kondisi kebun sebenarnya.

Pengumpulan dilakukan di empat lokasi di Johor, Malaysia, dua di Batu Pahat dan dua di Yong Peng. Tanaman berjenis Elaeis guineensis berusia 3-7 tahun dengan kepadatan 138-148 pohon per hektar dan jarak tanam 8,8 meter dalam pola segitiga. Suhu tercatat 24-35 °C, kelembapan 65-95%, radiasi matahari 100-1200 W/m², dan curah hujan 0-25 mm per hari. Citra RGB diambil dengan sensor Sony IMX766V 50 MP beresolusi 8688 × 5792 piksel pada jarak 2 meter dari batang dengan sudut pandang 15°-60°. Peta kedalaman dan awan titik direkam dengan Intel RealSense D455f beresolusi 1280 × 720, laju 90 frame per detik, daya IR 350 mW per modul, dan rentang kerja 0,6-6,0 meter. Sinkronisasi memakai unit berbasis Nvidia Jetson Nano dengan penyangga waktu ±0,1 ppm dan phase-locked loop; selisih waktu yang dilaporkan 8,3 ms ± 0,1 ms. Dataset terdiri dari 400 citra RGB, 400 peta kedalaman, dan 400 awan titik.

Anotasi kematangan bersifat biner, yaitu matang dan belum matang, menurut kriteria Malaysian Palm Oil Board. Buah matang berwarna jingga tua hingga merah dengan buah lepas terlihat; buah belum matang berwarna ungu tua hingga hitam dengan sedikit atau tanpa buah lepas. Pekerja kebun terlatih membuat kontur poligon tertutup dengan perangkat lunak CVAT atau LabelMe dan menambahkan metadata berupa status oklusi serta kondisi pencahayaan dalam berkas JSON. Poligon dapat diubah menjadi kotak pembatas untuk YOLO atau Faster R-CNN, atau dipakai langsung untuk Mask R-CNN. Lokalisasi tiga dimensi memakai DBSCAN dengan parameter ε dan minPts yang dipilih memakai koefisien siluet, lalu setiap klaster diperiksa pakar, diberi identitas, dan dianotasi dengan koordinat sentroid, orientasi, serta skor kepercayaan. Kalibrasi intrinsik memakai papan checkerboard; kalibrasi ekstrinsik menghasilkan transformasi kaku dari kerangka kamera kedalaman ke kerangka RGB dengan galat pendaftaran rata-rata 1,8 cm pada jarak 3 meter, sedangkan Tabel 3 mencatat RMSE di bawah 2 cm.

Karena kajian ini adalah deskriptor data, tidak ada model klasifikasi atau deteksi yang dilatih dan diuji; angka yang dilaporkan adalah statistik dataset dan hasil validasi. Kesepakatan awal tiga pemeriksa adalah 87,5% pada 400 tandan, menjadi 100% setelah diskusi konsensus, dan 95,2% pada pemeriksaan ulang acak 40 tandan; abstrak menyebut angka 92,5%. Pemeriksaan kualitas citra memberi tingkat lolos 94,5% untuk eksposur, 92,3% untuk fokus, 96,7% untuk keseimbangan warna, 91,8% untuk kelengkapan tandan, dan 100% untuk integritas berkas. Pemeriksaan kedalaman dengan penggaris memakai toleransi ±10 cm pada jarak 1,5-2,0 m, ±15 cm pada 2,0-3,0 m, dan ±20 cm pada 3,0-4,0 m. Waktu pengambilan terbagi 35% pagi, 40% siang, dan 25% sore; kondisi langit 60% cerah dan 40% berawan. Tidak ada split latihan, validasi, atau uji yang dinyatakan.

Penulis menyatakan bahwa pencahayaan dan cuaca mengubah warna serta tekstur tandan dan memengaruhi paparan, kontras, serta mutu citra, sehingga menambah ketidakpastian klasifikasi kematangan otomatis. Penulis juga menyatakan bahwa prosedur validasi bersifat dasar dan dapat direplikasi, bukan uji kinerja model. Keterbatasan lain yang disebut adalah pemilihan lokasi terutama didasarkan pada aksesibilitas kebun.

