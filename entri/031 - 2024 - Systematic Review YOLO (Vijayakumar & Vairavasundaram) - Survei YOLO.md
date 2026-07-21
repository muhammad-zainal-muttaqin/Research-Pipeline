# 031 - YOLO-Based Object Detection: A Systematic Review and Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vijayakumar2024yolo` |
| Judul asli | YOLO-based Object Detection Models: A Review and its Applications |
| Penulis | Ajantha Vijayakumar, Subramaniyaswamy Vairavasundaram |
| Tahun | 2024 |
| Venue | Multimedia Tools and Applications, Springer, vol. 83, hlm. 83535–83574 |
| Tema | Survei YOLO |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1007/s11042-024-18872-y
- **Halaman Springer:** https://link.springer.com/article/10.1007/s11042-024-18872-y
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLO-Based%20Object%20Detection%3A%20A%20Systematic%20Review%20and%20Applications
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLO-Based%20Object%20Detection%3A%20A%20Systematic%20Review%20and%20Applications&sort=relevance

## Gambaran Umum

Makalah ini adalah artikel survei atas keluarga detektor objek YOLO, diterbitkan di jurnal *Multimedia Tools and Applications* (Springer) pada Maret 2024. Cakupannya adalah seluruh iterasi YOLO sejak versi pertama yang dipublikasikan pada 2015 hingga YOLOv8 yang dirilis Januari 2023. Makalah ini tidak mengusulkan detektor baru; kontribusinya adalah penyusunan ulang literatur YOLO yang tersebar menjadi satu rujukan yang runtut.

Susunan telaahnya bergerak dari fondasi ke arsitektur lalu ke terapan: metrik kinerja deteksi, metode pasca-pemrosesan, ketersediaan dataset, dan teknik deteksi umum dijelaskan lebih dulu, kemudian desain arsitektur setiap versi, dan terakhir kontribusi tiap versi pada berbagai aplikasi. Hasil utamanya adalah gambaran terkonsolidasi atas pertukaran akurasi dan kecepatan pada silsilah YOLO, yang menjadi dasar pembaca memahami mengapa versi-versinya diadopsi luas.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek adalah tugas menemukan posisi setiap objek pada citra — dinyatakan sebagai kotak pembatas (*bounding box*) — sekaligus menentukan kelas objeknya. Sebelum YOLO, detektor paling akurat bekerja dalam dua tahap: tahap pertama mengusulkan kandidat wilayah (*region proposal*), tahap kedua mengklasifikasikan wilayah tersebut. Keluarga R-CNN ([bab 012](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md)), Fast R-CNN ([bab 013](./013%20-%202015%20-%20Fast%20R-CNN%20-%20Fondasi%20RGB.md)), dan Faster R-CNN ([bab 014](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)) mewakili garis ini. Abstrak survei ini menegaskan bahwa akurasi detektor dua tahap lebih baik daripada detektor satu tahap, yaitu detektor yang memprediksi kotak dan kelas langsung dari citra dalam satu kali evaluasi.

YOLO ([bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)) mengubah peta tersebut pada 2015 dengan membuktikan detektor satu tahap dapat berjalan *real-time* (umumnya dipahami sebagai laju minimal 30 citra per detik) dengan akurasi yang tetap kompetitif. Setelahnya, iterasi YOLO muncul hampir setiap tahun: versi kedua pada 2017, ketiga pada 2018, dan seterusnya hingga YOLOv8 pada Januari 2023. Setiap versi hadir dengan arsitektur, resep pelatihan, dan laporan aplikasi sendiri, terpencar di banyak venue publikasi.

Kondisi ini menimbulkan masalah kepraktisan: peneliti atau praktisi yang ingin memilih versi YOLO harus membaca belasan naskah primer untuk memahami perbedaan antarversi, cara pengukuran kinerjanya, dan bidang aplikasi yang telah dicoba. Survei ini ditulis untuk merangkum silsilah tersebut dalam satu telaah utuh.

## Ide Utama

Gagasan inti makalah ini adalah menyusun literatur YOLO yang tersebar ke dalam satu kerangka baca yang berurutan, dari alat ukur menuju arsitektur dan aplikasi. Masukannya adalah korpus publikasi tentang YOLO; keluarannya adalah sintesis terstruktur yang menjawab tiga pertanyaan pembaca: bagaimana kinerja detektor diukur, apa yang berubah pada setiap versi YOLO, dan di mana versi-versi itu dipakai.

Batas cakupannya tegas: silsilah dari versi pertama hingga YOLOv8, sehingga titik potong survei jatuh pada Januari 2023 dan seluruh versi yang lebih muda berada di luar telaah.

## Cara Kerja Langkah demi Langkah

Struktur telaah makalah, sesuai abstraknya, terdiri atas lima blok yang disajikan berurutan:

```
Struktur telaah survei (korpus: YOLO v1, 2015, s.d. YOLOv8, Jan 2023)

 masukan: literatur YOLO yang terpencar di banyak venue
            |
            v
 +----------------------------------------------------+
 | 1. Metrik evaluasi    | presisi, recall, IoU, mAP,  |
 |                       | FPS                         |
 | 2. Pasca-pemrosesan   | NMS dan teknik sejenis      |
 | 3. Dataset + teknik   | data latih; detektor satu   |
 |    deteksi umum       | tahap vs dua tahap          |
 | 4. Arsitektur versi   | v1 -> v2 -> v3 -> v4 -> v5  |
 |                       | -> YOLOX -> v6 -> v7 -> v8  |
 | 5. Pemetaan aplikasi  | kontribusi tiap versi ke    |
 |                       | bidang penerapan            |
 +----------------------------------------------------+
            |
            v
 keluaran: sintesis terstruktur silsilah YOLO + peta aplikasinya
```

Blok 1 sampai 3 membangun fondasi; blok 4 adalah inti survei; blok 5 menutup dengan peta terapan.

### Blok 1 — Metrik Evaluasi Deteksi

Survei dimulai dari alat ukur, karena seluruh perbandingan antarversi YOLO bergantung padanya. Metrik dasarnya adalah IoU (*Intersection over Union*): rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak kebenaran. Sebagai contoh, bila sebuah kotak prediksi dan kotak kebenaran beririsan seluas 60 satuan luas dan gabungan keduanya seluas 100 satuan, IoU-nya 0,6; prediksi lazim dihitung benar bila IoU-nya melampaui ambang 0,5 dan kelasnya tepat.

Di atas definisi benar-salah itu dibangun dua ukuran. Presisi adalah proporsi prediksi yang benar di antara seluruh prediksi. *Recall* adalah proporsi objek yang berhasil ditemukan di antara seluruh objek yang ada. *Average Precision* (AP) merangkum keseimbangan keduanya pada satu kelas, dan mAP (*mean Average Precision*) merata-ratakan AP seluruh kelas — inilah metrik akurasi utama yang dipakai di seluruh literatur YOLO. Sisi kecepatan diukur dalam FPS (*frame* per detik), yaitu jumlah citra yang diproses per detik. Pasangan mAP dan FPS selalu dilaporkan berdampingan pada tiap versi YOLO, karena posisi sebuah versi hanya bermakna bila keduanya disebut bersama.

### Blok 2 — Pasca-Pemrosesan

Detektor satu tahap mengeluarkan banyak kandidat kotak per objek, sehingga keluaran mentahnya harus dirapikan sebelum dipakai. Survei membahas metode pasca-pemrosesan yang umum, yang utamanya adalah NMS (*Non-Maximum Suppression*). Prosedurnya: urutkan seluruh kotak berdasarkan skor keyakinan (*confidence*, estimasi jaringan bahwa kotak berisi objek), ambil yang tertinggi, lalu buang semua kotak lain yang IoU-nya terhadap kotak terpilih melampaui ambang; ulangi untuk sisa kotak. Sebagai contoh, bila tiga kotak menutupi objek yang sama dengan skor 0,9, 0,8, dan 0,7 serta saling tumpang tindih, hanya kotak 0,9 yang dipertahankan. Tanpa tahap ini, satu objek akan dilaporkan berkali-kali.

### Blok 3 — Dataset dan Teknik Deteksi Umum

Blok ketiga memetakan data yang menjadi bahan latih dan uji detektor, serta teknik deteksi yang paling banyak dipakai. Dua tolok ukur yang menjadi standar pada literatur yang ditelaah adalah PASCAL VOC (20 kelas objek umum) dan MS COCO (80 kelas, dengan proporsi objek kecil yang jauh lebih besar, sehingga lebih berat). Sisi teknik mencakup pembagian detektor dua tahap dan satu tahap yang telah diuraikan pada latar belakang, beserta varian rancangan seperti detektor berbasis *anchor box* (kotak acuan berbagai ukuran dan rasio yang dipasang pada setiap posisi peta fitur, yang oleh jaringan diubah suai menjadi kotak akhir) dan detektor *anchor-free* (yang memprediksi posisi objek langsung tanpa kotak acuan).

### Blok 4 — Arsitektur Setiap Versi YOLO

Inti survei adalah telaah desain arsitektur tiap versi. Kosakata yang dipakai pada blok ini adalah pembagian detektor modern atas tiga bagian: *backbone* (jaringan pengekstrak fitur dari citra), *neck* (rangkaian penggabung fitur lintas resolusi), dan *head* (bagian yang mengeluarkan prediksi kotak dan kelas). Silsilah yang ditelaah, dari yang tertua hingga batas cakupan survei:

- **YOLOv1 (2016):** merumuskan deteksi sebagai regresi tunggal; citra dibagi grid S×S dan setiap sel langsung memprediksi kotak beserta kelasnya ([bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)).
- **YOLOv2/YOLO9000 (2017):** memperkenalkan *anchor box*, *batch normalization* (normalisasi keluaran tiap lapis untuk menstabilkan pelatihan), dan pelatihan gabungan deteksi-klasifikasi ([bab 002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)).
- **YOLOv3 (2018):** prediksi pada tiga skala resolusi agar objek kecil tertangkap ([bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)).
- **YOLOv4 (2020):** backbone CSPDarknet53 dengan kumpulan teknik pelatihan penambah akurasi tanpa biaya inferensi ([bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)).
- **YOLOv5 (2020):** implementasi PyTorch oleh Ultralytics yang menekankan kemudahan pemakaian dan pelatihan ulang.
- **PP-YOLO (2020):** penyempurnaan bertahap di atas YOLOv3 oleh Baidu ([bab 011](./011%20-%202020%20-%20PP-YOLO%20-%20Fondasi%20RGB.md)).
- **YOLOX (2021):** beralih ke rancangan *anchor-free* dengan kepala prediksi terpisah untuk klasifikasi dan regresi kotak ([bab 005](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)).
- **YOLOv6 (2022):** kerangka satu tahap yang dirancang untuk aplikasi industri ([bab 006](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)).
- **YOLOv7 (2022):** struktur lapisan baru E-ELAN dan resep pelatihan yang menjadikannya detektor *real-time* tercepat sekaligus terakurat pada masanya ([bab 007](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)).
- **YOLOv8 (Januari 2023):** rilis Ultralytics berikutnya, *anchor-free*, menyatukan deteksi, segmentasi, dan klasifikasi dalam satu kerangka; versi terbaru dalam cakupan survei.

### Blok 5 — Pemetaan Aplikasi

Survei ditutup dengan membahas ragam versi YOLO melalui kontribusinya pada berbagai aplikasi; premis yang dinyatakan abstraknya adalah bahwa banyak aplikasi mengadopsi versi YOLO karena kecepatan inferensinya. Sebaran terapan semacam itu terdokumentasi luas dalam literatur; korpus tinjauan ini sendiri memuat survei khusus YOLO untuk manufaktur ([bab 027](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)) dan untuk pertanian ([bab 029](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)), yang menunjukkan dua domain tempat silsilah ini dipakai. Taksonomi domain persis yang dipakai makalah ini tidak dapat diverifikasi dari abstrak dan dicatat pada bagian Poin untuk Sitasi.

## Eksperimen dan Hasil

Sebagai artikel survei, makalah ini tidak melaporkan eksperimen deteksi baru; hasilnya berupa sintesis atas literatur yang ditelaah. Empat hasil sintesis dapat dinyatakan dengan dukungan sumber.

Pertama, pernyataan eksplisit abstraknya: akurasi deteksi detektor dua tahap lebih baik daripada detektor satu tahap, tetapi YOLO mencapai akurasi tinggi dan waktu inferensi tinggi sekaligus dengan rancangan satu tahap. Pernyataan ini merangkum alasan keberadaan seluruh silsilah yang ditelaah: tiap versi YOLO adalah usaha mempersempit selisih akurasi itu tanpa mengorbankan kecepatan.

Kedua, besaran pertukaran tersebut dapat dilihat pada angka sumber primer yang menjadi objek survei. YOLOv1 mencapai 63,4% mAP pada 45 FPS di PASCAL VOC 2007, sementara Fast R-CNN pada saat yang sama mencapai 70,0% mAP pada sekitar 0,5 FPS. Interpretasinya: generasi pertama YOLO menukar sekitar 6,6 poin mAP dengan percepatan kurang lebih 90 kali lipat — pertukaran yang menjadikan deteksi *real-time* layak untuk aplikasi interaktif.

Ketiga, laju evolusi silsilahnya. Dari versi pertama pada 2015 hingga YOLOv8 pada Januari 2023 terdapat delapan rilis versi utama ditambah varian seperti PP-YOLO dan YOLOX dalam rentang delapan tahun, atau rata-rata lebih dari satu rilis berpengaruh per tahun. Konsekuensinya, survei atas silsilah ini cepat tertinggal dan berfungsi sebagai potret pada titik waktu tertentu, bukan peta final.

Keempat, skala telaahnya. Metadata penerbit mencatat 107 entri referensi, yang menunjukkan cakupan pustaka yang luas untuk sebuah survei naratif satu artikel.

## Kelebihan dan Keterbatasan

Kelebihan survei ini terletak pada tiga hal. Pertama, seluruh silsilah YOLO hingga YOLOv8 dihimpun dalam satu artikel jurnal yang telah melewati peninjauan sejawat. Kedua, telaah dimulai dari fondasi pengukuran — metrik, pasca-pemrosesan, dataset — sehingga pembaca yang belum mengenal deteksi objek dapat mengikuti bagian arsitektur. Ketiga, versi-versi dikaitkan dengan aplikasinya, bukan hanya dibandingkan di atas kertas.

Keterbatasannya juga tiga. Pertama, dari sisi cakupan, telaah berhenti pada YOLOv8, sehingga YOLOv9 ([bab 008](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md)), YOLOv10 ([bab 009](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md)), dan YOLOv11 ([bab 010](./010%20-%202024%20-%20YOLOv11%20%28Overview%29%20-%20Fondasi%20RGB.md)) berada di luar jangkauannya. Kedua, dari sisi metodologi, abstrak tidak menyebut protokol seleksi studi yang sistematis; secara konseptual, reprodusibilitas pemilihan literaturnya tidak dapat dinilai tanpa membaca teks lengkap, dan karakterisasinya sebagai tinjauan sistematis tidak didukung abstrak. Ketiga, dari sisi rekayasa, format survei memadatkan detail tiap versi, sehingga angka kinerja per versi tetap harus dirujuk ke naskah primer masing-masing sebelum dipakai sebagai dasar perbandingan.

## Kaitan dengan Bab Lain

Bab ini berdiri di atas bab-bab klaster Fondasi RGB: setiap versi yang ditelaahnya — dari YOLOv1 ([bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)) hingga YOLOv7 ([bab 007](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)) — memiliki bab tersendiri dalam korpus ini yang memuat detail teknis lebih dalam. Posisinya dalam klaster Survei YOLO sejajar dengan telaah naratif lain: survei Terven dkk. ([bab 026](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)), survei perkembangan YOLO oleh Jiang dkk. ([bab 028](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)), dan telaah dekade penuh YOLOv1–YOLOv12 oleh Sapkota dkk. ([bab 030](./030%20-%202025%20-%20Tinjauan%20Dekade%20YOLO%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)). Batas cakupannya di YOLOv8 beririsan dengan survei khusus YOLOv8 oleh Sohan dkk. ([bab 033](./033%20-%202024%20-%20Review%20YOLOv8%20%28Sohan%20dkk.%29%20-%20Survei%20YOLO.md)) dan diteruskan oleh tolok ukur evolusi YOLO dari Alif dan Hussain ([bab 032](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md)) yang membawa telaah hingga generasi YOLO11 dan YOLOv12.

## Poin untuk Sitasi

Kutip dengan kunci `vijayakumar2024yolo`. Ringkasan yang aman dikutip: "Vijayakumar dan Vairavasundaram (2024) menyurvei keluarga detektor objek YOLO dari versi pertama hingga YOLOv8; telaah dimulai dari metrik evaluasi, pasca-pemrosesan, dan ketersediaan dataset, kemudian membahas arsitektur setiap versi beserta kontribusinya pada berbagai aplikasi."

Catatan verifikasi sebelum sitasi formal:

- Judul terbit yang terverifikasi dari Crossref, DBLP, dan halaman penerbit adalah *"YOLO-based Object Detection Models: A Review and its Applications"* (DOI 10.1007/s11042-024-18872-y, vol. 83, hlm. 83535–83574, terbit daring 14 Maret 2024). Judul ini berbeda dari judul pada baris pertama berkas ini; bidang `title` di `references.bib` perlu dikoreksi.
- **Resolusi duplikasi dengan entri 030 (selesai).** Entri lama nomor 030 (`ali2024yoloreview`, atribusi penulis "Ali, Md Latifur; Zhang, Zhili") ternyata merujuk makalah yang sama persis dengan entri ini (DOI identik). Entri 030 telah diganti dengan sumber independen (Sapkota dkk. 2025, `sapkota2025yologenesis`), dan `references.bib` kini hanya memuat satu entri untuk DOI 10.1007/s11042-024-18872-y (`vijayakumar2024yolo`, kini dilengkapi field DOI).
- Karakterisasi makalah sebagai tinjauan sistematis berbasis PRISMA pada berkas lama tidak didukung abstrak; makalah menyebut dirinya survei lengkap. Jangan dikutip sebagai tinjauan sistematis tanpa memeriksa teks lengkap.
- Teks lengkap berbayar. Rincian isi per bagian, taksonomi domain aplikasi yang persis, dan tabel perbandingan antarversi di dalam makalah belum terverifikasi; hanya cakupan umum sesuai abstrak yang dipakai pada bab ini.
