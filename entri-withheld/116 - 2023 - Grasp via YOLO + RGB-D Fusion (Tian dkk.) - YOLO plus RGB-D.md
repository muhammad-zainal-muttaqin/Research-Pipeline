# 116 - A Robot Grasp Detection Method Based on YOLO and RGB-D Feature Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tian2023grasp` |
| Judul asli | A Robot Grasp Detection Method Based on YOLO and RGB-D Feature Fusion |
| Penulis | Tian, Hao; Song, Kechen; Li, Song; Ma, Shaoning; Yan, Yunhui |
| Tahun | 2023 |
| Venue | Journal of Intelligent & Robotic Systems |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Robot%20Grasp%20Detection%20Method%20Based%20on%20YOLO%20and%20RGB-D%20Feature%20Fusion
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=A%20Robot%20Grasp%20Detection%20Method%20Based%20on%20YOLO%20and%20RGB-D%20Feature%20Fusion&sort=relevance

## Gambaran Umum

Makalah ini mengusulkan metode deteksi *grasp* (konfigurasi genggaman robot pada suatu objek) yang menggabungkan arsitektur detektor bergaya YOLO dengan fusi fitur RGB-D: citra warna (RGB) dan peta kedalaman (*depth map*, citra yang setiap pikselnya berisi jarak permukaan objek ke kamera) diproses bersama untuk memprediksi posisi dan orientasi genggaman yang layak dieksekusi lengan robot. Tujuannya adalah memindahkan paradigma "satu evaluasi jaringan untuk seluruh citra" — ciri khas YOLO pada deteksi objek (bab 001) — ke tugas deteksi *grasp*, sehingga kecepatan satu tahap tetap terjaga sambil memanfaatkan informasi geometri dari kanal kedalaman yang tidak tersedia pada citra RGB semata.

Berkas sumber untuk entri ini terbatas pada metadata bibliografis (judul, penulis, tahun, venue) tanpa tautan arXiv atau DOI yang dapat diakses langsung, dan pencarian daring lanjutan tidak berhasil menemukan salinan naskah lengkap atau abstrak resmi yang dapat difetch. Akibatnya, uraian pada bab ini membatasi diri pada apa yang dapat disimpulkan secara aman dari judul dan konvensi umum kelas metode sejenis (deteksi *grasp* berbasis fusi RGB-D dengan tulang punggung detektor satu tahap), sementara seluruh angka kinerja, rincian dataset, dan konfigurasi arsitektur spesifik ditandai sebagai belum terverifikasi pada bagian *Poin untuk Sitasi*.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi *grasp* robotik memprediksi di mana dan dengan sudut berapa sebuah *gripper* (penjepit) harus menutup untuk mengangkat suatu objek tanpa terlepas atau merusaknya. Sejak Jiang dkk. (2011) merumuskan representasi genggaman sebagai kotak berorientasi lima parameter — posisi pusat, sudut rotasi, lebar bukaan *gripper*, dan tinggi pelat kontak — sebagian besar metode berikutnya memprediksi parameter ini dari citra masukan dengan jaringan konvolusi. Generasi awal metode ini, misalnya jaringan dua tahap yang menyaring ribuan kandidat kotak sebelum mengklasifikasikannya, mewarisi kelemahan yang sama dengan detektor objek dua tahap yang dibahas pada bab 012–014: proses bertahap membuat latensi tinggi, sehingga sulit dipakai pada lini produksi atau manipulasi *real-time*.

Sumber informasi kedua yang lazim dipakai untuk mengatasi ambiguitas visual adalah kanal kedalaman. Citra RGB saja rentan tertipu tekstur permukaan, bayangan, dan pantulan cahaya, sedangkan peta kedalaman memberi ukuran geometri objek secara langsung — jarak tepi objek terhadap latar, kemiringan permukaan, dan ketebalan bagian yang bisa dijepit. Masalahnya, RGB dan *depth* memiliki statistik yang sangat berbeda: RGB kaya tekstur dan warna, sedangkan *depth* dari sensor konsumen (seperti Kinect atau RealSense) sering memiliki lubang data (*noise*) di tepi objek dan permukaan reflektif. Menggabungkan keduanya secara naif — misalnya sekadar menumpuk sebagai kanal keempat — sering gagal memanfaatkan komplementaritas kedua modalitas ini secara optimal. Klaster YOLO plus RGB-D pada tinjauan ini (bab 112–119) mengumpulkan berbagai jawaban atas masalah fusi ini pada konteks yang berbeda-beda; makalah Tian dkk. memposisikan jawabannya spesifik pada tugas deteksi *grasp*.

## Ide Utama

Gagasan inti makalah, sejauh dapat disimpulkan dari judulnya, adalah mengganti tahap pengklasifikasian kandidat genggaman yang terpisah dengan satu jaringan bergaya YOLO yang meregresi parameter *grasp* langsung dari citra, sebagaimana YOLO meregresi kotak objek langsung dari citra pada deteksi umum. Perbedaannya terletak pada masukan: alih-alih hanya RGB, jaringan menerima pasangan RGB dan *depth* yang fiturnya digabungkan lewat modul fusi sebelum mencapai lapisan prediksi. Dengan demikian, kecepatan satu tahap (satu kali evaluasi jaringan per citra) dipertahankan, sementara akurasi geometri genggaman ditingkatkan oleh informasi kedalaman yang tidak dimiliki metode RGB tunggal.

Prinsip ini konsisten dengan pola umum pada metode fusi RGB-D untuk deteksi maupun *grasp*: kedua modalitas diproses dengan cabang fitur masing-masing sebelum digabungkan pada satu titik dalam jaringan — dikenal sebagai fusi awal (*early fusion*, penggabungan sebelum ekstraksi fitur), fusi tengah (*mid fusion*, penggabungan pada peta fitur pertengahan), atau fusi akhir (*late fusion*, penggabungan pada tahap keputusan). Titik fusi spesifik yang dipakai makalah ini tidak dapat dipastikan tanpa akses ke naskah penuh, sehingga disebutkan di sini sebagai kerangka konseptual, bukan klaim rinci tentang implementasinya.

## Cara Kerja Langkah demi Langkah

### Representasi Genggaman

Konvensi yang lazim dipakai pada deteksi *grasp* planar (genggaman searah sumbu vertikal, dua dimensi) menyatakan setiap genggaman sebagai lima angka: g = (x, y, θ, w, h). Sebagai ilustrasi hipotetis: pada citra 640×480 piksel, sebuah genggaman dapat dinyatakan sebagai pusat (320, 240), sudut rotasi 30 derajat terhadap sumbu horizontal, lebar bukaan *gripper* 80 piksel, dan tinggi pelat kontak 40 piksel. Format ini setara secara struktural dengan kotak pembatas pada deteksi objek biasa, hanya ditambah satu parameter sudut — kesamaan struktural inilah yang membuat kerangka detektor satu tahap seperti YOLO dapat diadaptasi untuk tugas *grasp* dengan mengganti kepala prediksi (bagian akhir jaringan yang menghasilkan angka keluaran).

### Dua Cabang Ekstraksi Fitur dan Modul Fusi

Pola arsitektural yang umum pada kelas metode ini memakai dua cabang paralel: satu cabang konvolusi memproses citra RGB, satu cabang lain memproses peta kedalaman yang telah dinormalisasi ke rentang nilai piksel yang sebanding. Keluaran kedua cabang pada satu atau beberapa tingkat resolusi kemudian digabungkan oleh modul fusi, yang dapat berupa penjumlahan kanal, penyambungan kanal (*concatenation*) diikuti konvolusi 1×1 untuk mereduksi dimensi, atau mekanisme perhatian (*attention*) yang memberi bobot berbeda pada tiap modalitas sesuai keandalannya di lokasi tertentu. Diagram berikut merangkum alur data yang konsisten dengan judul makalah dan konvensi umum kelas metode ini:

```
citra RGB (3 kanal)          peta depth (1 kanal)
        |                            |
  cabang fitur RGB              cabang fitur depth
  (blok konvolusi)               (blok konvolusi)
        |                            |
        +-------------+  +-----------+
                      |  |
                modul fusi RGB-D
           (gabung kanal / spasial)
                      |
             head gaya YOLO (grid SxS)
                      |
   per sel grid: x, y, sudut, lebar, tinggi, skor
```

Fitur gabungan diteruskan ke bagian jaringan yang meniru kepala prediksi YOLO: citra dibagi menjadi grid sel, dan setiap sel bertanggung jawab memprediksi parameter genggaman bila pusat suatu genggaman jatuh di dalamnya — mekanisme pembagian tanggung jawab yang sama seperti dijelaskan pada bab 001 untuk deteksi objek, hanya keluarannya berupa lima parameter *grasp* dan satu skor keyakinan alih-alih kelas objek.

### Pelatihan dan Inferensi

Pelatihan jaringan semacam ini umumnya memakai fungsi *loss* regresi (galat kuadrat atau galat absolut) antara parameter genggaman prediksi dan anotasi kebenaran, ditambah galat klasifikasi bila jaringan turut memprediksi kelas objek. Pada inferensi, citra RGB dan *depth* dilewatkan bersamaan melalui jaringan dalam satu evaluasi, menghasilkan satu atau beberapa kandidat genggaman per objek yang kemudian disaring dengan mekanisme penekanan duplikat, serupa *Non-Maximum Suppression* pada YOLO, sebelum genggaman dengan skor tertinggi dieksekusi oleh lengan robot. Rincian hiperparameter, ukuran *backbone* (tulang punggung ekstraksi fitur), dan pengaturan pelatihan spesifik pada makalah ini tidak dapat dipastikan dari sumber yang tersedia.

## Eksperimen dan Hasil

Kelas metode deteksi *grasp* berbasis RGB-D umumnya dievaluasi pada dua jenis pengujian: akurasi deteksi pada dataset benchmark berlabel genggaman (misalnya dataset yang berisi pasangan citra RGB-D dengan anotasi kotak genggaman), dan validasi fisik berupa tingkat keberhasilan (*success rate*) saat lengan robot benar-benar mengeksekusi genggaman yang diprediksi. Berdasarkan judul dan venue makalah, dapat diperkirakan bahwa Tian dkk. mengikuti pola evaluasi yang sama, namun dataset yang dipakai, metrik akurasi, dan angka spesifik lain tidak dapat dikonfirmasi karena naskah penuh maupun abstrak resminya tidak berhasil ditemukan melalui pencarian yang dilakukan untuk bab ini. Interpretasi kuantitatif — misalnya seberapa besar fusi RGB-D menaikkan akurasi dibanding RGB tunggal, atau seberapa cepat model berjalan dibanding metode dua tahap — karena itu belum dapat dituliskan secara bertanggung jawab di sini dan harus diambil langsung dari tabel hasil pada naskah asli sebelum dikutip.

## Kelebihan dan Keterbatasan

Kelebihan yang dapat disimpulkan secara konseptual dari desainnya: pendekatan satu tahap mewarisi keunggulan kecepatan YOLO dibanding metode *grasp* dua tahap, sementara fusi RGB-D berpotensi memperbaiki akurasi orientasi dan skala genggaman dibanding metode RGB tunggal, karena kedalaman memberi ukuran geometri langsung yang tidak dapat diperoleh dari warna dan tekstur saja.

Dari sisi rekayasa, terdapat sejumlah keterbatasan struktural yang lazim menyertai kelas metode ini dan yang secara spesifik berlaku bila makalah ini menggunakan representasi genggaman planar lima parameter: pertama, representasi tersebut mengasumsikan genggaman searah sumbu vertikal terhadap permukaan objek, sehingga tidak mencakup genggaman enam derajat kebebasan (6-DoF, posisi dan orientasi bebas dalam ruang tiga dimensi) yang dibutuhkan untuk objek dengan geometri kompleks atau posisi miring. Kedua, kualitas peta kedalaman dari sensor konsumen — lubang data pada tepi objek transparan atau reflektif — dapat menurunkan kualitas fusi bila jaringan tidak dirancang tahan terhadap derau ini. Ketiga, sebagaimana metode fusi RGB-D lain pada klaster ini, pemilihan titik fusi (awal, tengah, atau akhir) melibatkan kompromi antara kekayaan interaksi antarmodalitas dan biaya komputasi tambahan, dan kompromi spesifik yang diambil makalah ini tidak dapat dinilai tanpa akses ke naskah lengkap.

## Kaitan dengan Bab Lain

Bab ini mewarisi format keluaran satu tahap yang diperkenalkan YOLO pada bab 001, diadaptasi dari deteksi kelas objek menjadi regresi parameter genggaman. Di dalam klaster YOLO plus RGB-D, bab ini berdampingan dengan bab [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md), yang juga menyasar prediksi genggaman namun memakai representasi titik awan (*point cloud*) alih-alih peta kedalaman dua dimensi, dan bab [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md), yang mengeksplorasi titik fusi RGB-D pada detektor YOLO secara lebih umum tanpa spesifik ke tugas *grasp*. Perbandingan ketiganya berguna untuk melihat bagaimana pertanyaan "di mana dan bagaimana menggabungkan RGB dengan kedalaman" dijawab berbeda-beda bergantung pada representasi keluaran yang ditargetkan.

## Poin untuk Sitasi

Kutip dengan kunci `tian2023grasp`. Ringkasan yang aman dikutip terbatas pada metadata bibliografis: "Tian, Song, Li, Ma, dan Yan mengusulkan metode deteksi *grasp* robotik yang memfusikan fitur RGB dan kedalaman dalam kerangka bergaya YOLO, dipublikasikan di Journal of Intelligent & Robotic Systems (2023)." Seluruh hal berikut BELUM terverifikasi terhadap naskah asli dan wajib dicek sebelum dikutip dalam karya formal: (1) tautan arXiv/DOI langsung ke naskah tidak ditemukan pada berkas sumber maupun pencarian lanjutan, sehingga isi abstrak dan metodologi rinci pada bab ini adalah simpulan dari judul dan konvensi umum kelas metode sejenis, bukan kutipan dari naskah; (2) rincian volume 107, nomor 3, dan halaman 38 yang tercatat pada berkas lama belum dikonfirmasi ke basis data penerbit; (3) dataset evaluasi, metrik akurasi, kecepatan inferensi, dan hasil uji robot fisik sepenuhnya belum terkonfirmasi; (4) titik fusi RGB-D (awal/tengah/akhir) dan representasi genggaman (planar lima parameter atau varian lain) yang dipakai makalah masih berupa inferensi, bukan fakta yang terverifikasi.
