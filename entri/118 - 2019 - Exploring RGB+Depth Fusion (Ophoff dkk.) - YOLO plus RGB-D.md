# 118 - Exploring RGB+Depth Fusion for Real-Time Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ophoff2019multimodal` |
| Judul asli | Exploring RGB+Depth Fusion for Real-Time Object Detection |
| Penulis | Tanguy Ophoff, Kristof Van Beeck, Toon Goedemé |
| Tahun | 2019 |
| Venue | Sensors (MDPI), volume 19, nomor 4, artikel 866 |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **DOI (akses terbuka):** https://doi.org/10.3390/s19040866
- **PMC (naskah lengkap gratis):** https://pmc.ncbi.nlm.nih.gov/articles/PMC6412390/
- **Google Scholar:** https://scholar.google.com/scholar?q=Exploring%20RGB%2BDepth%20Fusion%20for%20Real-Time%20Object%20Detection

## Gambaran Umum

Makalah ini meneliti pertanyaan yang sebelumnya dijawab secara ad hoc di berbagai karya penerapan: pada lapis mana sebaiknya citra kedalaman (*depth map*) digabungkan dengan citra RGB di dalam sebuah detektor objek satu tahap agar akurasi meningkat tanpa mengorbankan kemampuan berjalan *real-time* di perangkat terbatas. Ophoff, Van Beeck, dan Goedemé membangun satu arsitektur dua cabang di atas YOLOv2 (bab 002) yang dapat digabungkan (*fusion*) pada 28 titik berbeda — dari sebelum lapis pertama sampai setelah lapis terakhir — lalu melatih dan menguji seluruh 28 varian tersebut pada tiga kumpulan data RGB-D.

Temuan utamanya adalah penggabungan pada lapis pertengahan hingga akhir jaringan secara konsisten mengungguli penggabungan pada lapis awal maupun model RGB tunggal, dengan kenaikan *average precision* (AP, presisi rata-rata pada satu ambang IOU) berkisar 1 hingga lebih dari 8 poin tergantung kumpulan data. Makalah ini adalah salah satu bukti empiris paling sistematis di klaster YOLO plus RGB-D mengenai pertanyaan "di mana harus memfusi", karena mengujinya secara eksaustif alih-alih memilih satu titik fusi berdasarkan intuisi arsitektur seperti kebanyakan karya lain di klaster ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sensor kedalaman konsumen seperti Kinect dan kamera *stereo* menghasilkan peta kedalaman (matriks jarak per piksel dari kamera ke permukaan objek) yang, secara prinsip, membawa informasi geometris yang tidak dimiliki citra RGB murni: batas objek yang tegas terhadap latar belakang, invariansi terhadap pencahayaan, dan ukuran fisik objek yang dapat diturunkan langsung dari jarak. Namun cara menggabungkan kedua modalitas ini ke dalam satu jaringan konvolusi belum memiliki jawaban baku pada 2019.

Literatur sebelum makalah ini umumnya membedakan tiga strategi fusi berdasarkan *kapan* kedua aliran data digabung. *Early fusion* menumpuk kanal RGB dan kedalaman sebagai satu masukan sejak awal, sehingga jaringan memproses keduanya sebagai satu tensor sejak lapis pertama. *Late fusion* membiarkan dua jaringan terpisah memproses RGB dan kedalaman secara independen sampai hampir ke keluaran, baru kemudian menggabungkan keputusan atau fitur tingkat tinggi. Di antara keduanya ada *mid fusion*, yang menggabungkan fitur pada lapis pertengahan setelah masing-masing cabang sempat mengekstrak fitur tingkat rendah sendiri-sendiri. Setiap karya penerapan yang menggunakan RGB-D biasanya memilih salah satu dari ketiganya berdasarkan preferensi desain, bukan perbandingan terkontrol. Akibatnya, tidak ada panduan kuantitatif tentang titik fusi mana yang sebenarnya optimal, dan apakah jawabannya berubah menurut jenis data (dalam ruangan versus luar ruangan) atau jenis objek yang dideteksi.

## Ide Utama

Gagasan inti makalah adalah menjadikan posisi fusi sebagai parameter yang dapat digeser bebas di sepanjang jaringan, lalu menguji seluruh posisi yang mungkin alih-alih menetapkannya di muka. Jaringan dasar (YOLOv2, berisi 27 lapis konvolusi) diduplikasi menjadi dua cabang identik: satu menerima citra RGB, satu menerima peta kedalaman sebagai masukan satu kanal. Kedua cabang berjalan paralel dan independen sampai satu titik potong yang disebut lapis fusi (*fuse layer*). Pada titik itu, fitur dari kedua cabang digabungkan menjadi satu, dan hasil gabungan tersebut diteruskan ke sisa jaringan tunggal hingga keluaran deteksi.

Karena YOLOv2 memiliki 27 lapis, terdapat 28 posisi potong yang mungkin: fusi bisa terjadi sebelum lapis 1 (setara *early fusion* murni), di lapis pertengahan mana pun, atau setelah lapis 27 (setara *late fusion*, hampir di keluaran). Dengan melatih satu model penuh untuk tiap posisi, penulis memperoleh 28 titik data yang menggambarkan bagaimana akurasi berubah sebagai fungsi dari letak fusi — bukan hanya membandingkan tiga kategori kasar (awal/tengah/akhir) seperti kebanyakan studi lain.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dua Cabang

Kedua cabang (RGB dan kedalaman) memakai struktur konvolusi yang identik dengan YOLOv2, hanya berbeda pada jumlah kanal masukan: tiga kanal (merah, hijau, biru) untuk cabang RGB, satu kanal untuk cabang kedalaman. Sebelum titik fusi, kedua cabang tidak berbagi bobot maupun aktivasi; masing-masing mengekstrak fiturnya sendiri dari modalitasnya masing-masing.

### Lapis Fusi

Pada posisi potong yang ditentukan, lapis fusi menerima dua peta fitur (satu dari tiap cabang) yang berukuran spasial sama tetapi punya jumlah kanal sendiri-sendiri. Lapis ini pertama menggabungkan (*concatenate*) kedua peta fitur di sepanjang dimensi kanal, sehingga jumlah kanal totalnya menjadi dua kali lipat kanal satu cabang. Kemudian sebuah konvolusi 1×1 (konvolusi dengan jendela satu piksel, berfungsi mencampur informasi antar-kanal tanpa mengubah ukuran spasial) diterapkan untuk memampatkan kembali jumlah kanal ke ukuran semula, sebesar jumlah kanal yang dipakai jaringan tunggal pada lapis tersebut. Dengan cara ini, arsitektur sesudah titik fusi tetap identik dengan YOLOv2 baku, sehingga sisa jaringan (termasuk kepala deteksi) tidak perlu diubah.

Skema arsitektur dua cabang dengan titik fusi yang dapat digeser digambarkan berikut:

```
citra RGB   -> [lapis 1]...[lapis k]  \
                                        > gabung + konv 1x1 -> [lapis k+1]...[lapis 27] -> deteksi
citra depth -> [lapis 1]...[lapis k]  /

   k = 0   : fusi sebelum lapis 1  (setara early fusion)
   k ~ 8-18: fusi tengah jaringan   (mid fusion, diuji 28 posisi)
   k = 27  : fusi setelah lapis terakhir (setara late fusion)
```

Diagram ini menunjukkan bahwa satu-satunya yang berubah antar-eksperimen adalah nilai k, yaitu jumlah lapis yang dilalui kedua cabang sebelum digabung; seluruh bobot dan hiperparameter lain memakai pengaturan baku YOLOv2, kecuali lama pelatihan yang disesuaikan dengan ukuran tiap kumpulan data.

### Kumpulan Data Uji

Perbandingan dilakukan pada tiga kumpulan data RGB-D dengan karakteristik berbeda. Pertama, kumpulan data pejalan kaki dalam ruangan berbasis EPFL yang dilabel ulang oleh penulis, direkam dengan kamera Kinect. Kedua, KITTI, kumpulan data luar ruangan berbasis kamera *stereo* pada kendaraan, mencakup kelas mobil, pengendara sepeda, dan pejalan kaki — kumpulan data ini jauh lebih menantang karena variasi jarak, oklusi, dan pencahayaan luar ruangan. Ketiga, kumpulan data industri "GD Screws": citra sekrup pada papan sirkuit yang direkam dengan pemindai *sheet-of-light* (metode penangkapan kedalaman presisi tinggi berbasis garis laser), dipakai untuk menguji kasus deteksi objek kecil dan homogen di lingkungan terkendali.

### Prosedur Pelatihan dan Evaluasi

Untuk tiap kumpulan data, penulis melatih model dasar RGB-tunggal, model dasar kedalaman-tunggal, dan 28 varian fusi, lalu mengukur AP pada tiap model. Hiperparameter pelatihan mengikuti pengaturan baku YOLOv2; yang disesuaikan hanyalah durasi pelatihan, mengingat ukuran kumpulan data yang jauh berbeda (KITTI beranggotakan ribuan citra, sedangkan GD Screws hanya puluhan citra). Perbandingan dilakukan secara adil karena seluruh varian memakai jumlah parameter dan anggaran pelatihan yang sebanding, sehingga selisih akurasi dapat diatribusikan pada posisi fusi, bukan pada perbedaan kapasitas model.

## Eksperimen dan Hasil

Pada kumpulan data pejalan kaki (EPFL), model RGB-tunggal mencapai AP sekitar 60%, model kedalaman-tunggal sedikit di bawahnya, sedangkan varian fusi terbaik mencapai sekitar 63%, atau naik sekitar 3 poin AP dibandingkan baseline RGB. Pada kumpulan data KITTI, kesenjangannya jauh lebih besar: model RGB-tunggal mencapai mAP moderat 45,64%, sedangkan varian fusi terbaik mencapai 54,25% — kenaikan sekitar 8,6 poin. Selisih sebesar ini mengindikasikan bahwa informasi kedalaman paling bermanfaat justru pada skenario yang paling menantang, yaitu luar ruangan dengan variasi jarak objek yang besar, karena kedalaman membantu memisahkan objek dari latar yang secara visual serupa. Pada kumpulan data GD Screws, baseline RGB sudah tinggi (sekitar 96%, karena lingkungan terkendali dan objek homogen), sehingga ruang perbaikan sempit; fusi terbaik hanya menaikkan AP sekitar 1 poin, meskipun pada metrik AP bergaya COCO (yang merata-ratakan beberapa ambang IOU sekaligus, sehingga lebih ketat terhadap presisi lokalisasi) kenaikannya lebih terasa.

Pola yang konsisten di ketiga kumpulan data adalah kurva AP terhadap posisi fusi berbentuk seperti busur: fusi pada lapis paling awal memberi perbaikan kecil atau bahkan menurunkan akurasi, sedangkan fusi pada rentang pertengahan hingga menjelang akhir jaringan memberi hasil terbaik, sebelum sedikit menurun lagi mendekati lapis paling akhir. Penulis menafsirkan pola ini berasal dari sifat fitur pada tiap kedalaman jaringan: fitur tingkat rendah (tepi, kontras lokal) dari cabang RGB dan cabang kedalaman tidak selalu selaras secara langsung, sehingga menggabungkannya terlalu dini memberi sedikit manfaat; sebaliknya, fitur tingkat menengah hingga tinggi (bentuk, keberadaan objek) sudah cukup abstrak sehingga informasi geometris dari kedalaman dapat melengkapi informasi tekstur dari RGB secara efektif. Posisi lapis persis yang optimal berbeda sedikit antar-kumpulan data, sehingga makalah tidak mengklaim satu nomor lapis tunggal yang universal, melainkan rentang pertengahan-hingga-akhir sebagai prinsip umum. Makalah tidak melaporkan angka kecepatan (FPS) hasil pengukuran langsung dari eksperimen fusi; klaim kemampuan *real-time* didasarkan pada sifat arsitektur dasar YOLOv2, yang telah dikenal mampu berjalan *real-time* pada perangkat tersemat seperti NVIDIA Jetson TX2.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah metodologinya yang eksaustif: alih-alih membandingkan tiga kategori kasar (awal/tengah/akhir), penulis menguji seluruh 28 titik potong yang mungkin pada arsitektur yang sama, sehingga kesimpulan "mid-hingga-late fusion lebih baik" didukung kurva empiris penuh, bukan sampel titik yang jarang. Desain lapis fusi (gabung kanal lalu konvolusi 1×1) juga sederhana dan mudah diterapkan ulang pada jaringan satu tahap lain, karena tidak mengubah struktur jaringan sesudah titik fusi.

Dari sisi rekayasa, keterbatasan yang tampak adalah bobot awal cabang kedalaman diambil dari bobot ImageNet yang dilatih untuk citra RGB tiga kanal, sedangkan tidak ada padanan ImageNet untuk citra kedalaman satu kanal; penyesuaian ini berpotensi membuat cabang kedalaman kurang optimal sejak awal pelatihan dibandingkan bila tersedia bobot awal yang memang dilatih pada data kedalaman. Secara konseptual, hiperparameter pelatihan (selain durasi) disamakan dengan pengaturan baku RGB agar perbandingan adil, tetapi ini berarti konfigurasi fusi tidak benar-benar dioptimalkan sendiri — kenaikan akurasi yang dilaporkan mungkin merupakan batas bawah dari potensi sebenarnya. Cakupan pengujian juga terbatas pada tiga kumpulan data dan satu arsitektur dasar (YOLOv2), sehingga generalisasi temuan ke detektor satu tahap yang lebih baru atau ke jenis sensor kedalaman lain (misalnya LiDAR jarak jauh) tidak diuji langsung oleh makalah ini.

## Kaitan dengan Bab Lain

Cabang RGB dan cabang kedalaman pada makalah ini sama-sama diturunkan langsung dari arsitektur YOLOv2 yang dibahas pada [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md); pemilihan YOLOv2 sebagai basis mencerminkan kebutuhan kecepatan *real-time* yang sudah menjadi ciri sejak makalah tersebut. Dalam klaster YOLO plus RGB-D, temuan bab ini — bahwa titik fusi optimal berada pada lapis pertengahan-hingga-akhir, bukan pada masukan mentah — memberi dasar empiris bagi desain fusi di karya penerapan lain, misalnya [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md) yang memperluas kanal masukan YOLO untuk RGB-D, dan [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md) yang menerapkan fusi RGB-D untuk tugas *grasping* robotik. Bab-bab penerapan lain di klaster yang memakai kedalaman sebagai kanal tambahan pada dasarnya sedang menjawab, secara implisit, pertanyaan yang diukur eksplisit oleh makalah ini.

## Poin untuk Sitasi

Kutip dengan kunci `ophoff2019multimodal`. Ringkasan aman dikutip: "Ophoff, Van Beeck, dan Goedemé (2019) menguji 28 posisi fusi RGB-kedalaman pada arsitektur dua cabang berbasis YOLOv2 dan menemukan bahwa penggabungan pada lapis pertengahan-hingga-akhir jaringan secara konsisten memberi akurasi deteksi terbaik dibandingkan fusi pada lapis awal atau model RGB tunggal, dengan kenaikan AP yang bervariasi antara sekitar 1 dan lebih dari 8 poin tergantung kumpulan data." Angka AP spesifik per kumpulan data (EPFL sekitar 60% menjadi sekitar 63%; KITTI 45,64% menjadi 54,25%; GD Screws sekitar 96% menjadi sekitar 97%) diperoleh dari ringkasan sumber sekunder atas naskah PMC dan berpotensi meleset dari tabel asli pada beberapa desimal; nomor lapis persis yang optimal untuk tiap kumpulan data (rentang 8 hingga 21 pada sumber yang berbeda) juga tidak konsisten antar-ringkasan yang diperoleh dan wajib diverifikasi langsung ke tabel hasil pada naskah asli (DOI 10.3390/s19040866) sebelum dikutip dengan presisi lapis tertentu.
