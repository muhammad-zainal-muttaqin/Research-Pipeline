# 030 - YOLO-Based Object Detection Models: A Review and Its Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ali2024yoloreview` |
| Judul asli | YOLO-based Object Detection Models: A Review and its Applications |
| Penulis | Ajantha Vijayakumar; Subramaniyaswamy Vairavasundaram (SASTRA Deemed University, India) |
| Tahun | 2024 |
| Venue | Multimedia Tools and Applications (Springer), vol. 83, hlm. 83535–83574 |
| Tema | Survei YOLO |

> **Catatan verifikasi identitas.** `references.bib` mencatat penulis sebagai "Ali, Md Latifur; Zhang, Zhili". Atribusi tersebut tidak ditemukan pada Crossref, OpenAlex, DBLP, maupun Semantic Scholar; keempatnya seragam mencatat Vijayakumar dan Vairavasundaram sebagai penulis makalah dengan judul dan DOI ini. Rincian pada bagian *Poin untuk Sitasi*.

## Tautan Akses
- **DOI (halaman penerbit):** https://doi.org/10.1007/s11042-024-18872-y
- **Google Scholar:** https://scholar.google.com/scholar?q=YOLO-Based%20Object%20Detection%20Models%3A%20A%20Review%20and%20Its%20Applications
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=YOLO-Based%20Object%20Detection%20Models%3A%20A%20Review%20and%20Its%20Applications&sort=relevance

## Gambaran Umum

Makalah ini adalah survei atas model deteksi objek keluarga YOLO (*You Only Look Once*) beserta aplikasinya. Alih-alih mengusulkan metode baru, penulis mengonsolidasikan tiga kelompok materi: (1) evolusi arsitektur YOLO dari versi pertama tahun 2016 sampai YOLOv8 tahun 2023; (2) komponen penunjang evaluasi, yaitu metrik kinerja, ketersediaan dataset, dan metode pasca-pemrosesan; (3) peta penerapan YOLO pada berbagai domain, antara lain transportasi, pengawasan, industri, medis, pertanian, dan citra udara.

Masalah yang dipecahkan bersifat organisatoris. Literatur YOLO terpencar di banyak tempat publikasi, sehingga pembaca baru sulit memperoleh gambaran utuh. Survei ini menyatukannya dalam satu dokumen 40 halaman dengan 107 rujukan. Hasil utamanya bukan angka eksperimen, melainkan kerangka baca terpadu; kebergunaannya terbukti dari adopsi komunitas — sampai Juli 2026 makalah ini disitasi lebih dari 400 kali menurut Crossref, OpenAlex, dan Semantic Scholar.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sejak YOLOv1 pada 2016 (bab 001), keluarga YOLO bertambah terus: YOLOv2/YOLO9000 (bab 002), YOLOv3 (bab 003), YOLOv4 (bab 004), YOLOX (bab 005), YOLOv6 (bab 006), YOLOv7 (bab 007), hingga YOLOv8. Setiap generasi mengubah arsitektur, resep pelatihan, atau keduanya. Di luar versi resmi, ratusan varian turunan dipublikasikan untuk tugas khusus seperti deteksi objek kecil, citra drone, dan inspeksi cacat produk.

Kondisi ini menimbulkan tiga kesulitan. Pertama, silsilah versi sukar ditelusuri karena sebagian rilis tidak melewati kanal publikasi formal; YOLOv5 dan YOLOv8, misalnya, dirilis sebagai perangkat lunak tanpa makalah konferensi. Kedua, tiap versi dievaluasi dengan metrik dan dataset yang berbeda-beda, sehingga perbandingan langsung antarmakalah tidak adil tanpa pemahaman metrik yang memadai. Ketiga, peneliti aplikasi tidak memiliki peta yang menunjukkan versi mana yang lazim dipakai pada domainnya. Survei-survei terdahulu (bab 026, bab 028, bab 034) sebagian terbit sebelum YOLOv8 dan sebagian membatasi cakupan. Makalah ini mengisi celah tersebut dengan cakupan sampai YOLOv8 sekaligus materi penunjangnya.

## Ide Utama

Gagasan inti sebuah survei adalah pemetaan, dan makalah ini memetakan ekosistem YOLO pada dua sumbu. Sumbu vertikal adalah silsilah model: versi demi versi, apa yang berubah pada setiap generasi. Sumbu horizontal adalah domain aplikasi: di mana setiap generasi dipakai. Kedua sumbu ditopang tiga blok penjelas — metrik evaluasi agar angka antarmakalah dapat ditimbang, dataset agar konteks pengujian jelas, dan pasca-pemrosesan sebagai tahap setelah jaringan mengeluarkan prediksi mentah. Masukan survei adalah literatur yang tersebar; keluarannya adalah satu dokumen terstruktur yang menjawab tiga pertanyaan pembaca: YOLO berevolusi bagaimana, kinerjanya diukur dengan apa, dan dipakai di mana.

## Cara Kerja Langkah demi Langkah

### Kerangka Pembanding: Pipeline Detektor Satu Tahap

Seluruh versi YOLO berbagi pola yang sama, sehingga dapat dibandingkan blok demi blok. Citra masukan dilewatkan ke tiga blok jaringan: *backbone* (jaringan konvolusi pengekstrak fitur visual), *neck* (penggabung fitur lintas skala agar objek besar dan kecil sama-sama terdeteksi), dan *head* (lapisan prediksi yang mengeluarkan koordinat *bounding box* — kotak pembatas objek — beserta kelasnya). Keluaran mentah kemudian dirapikan oleh tahap pasca-pemrosesan di luar jaringan. Skema perbandingan inilah yang dipakai survei untuk menempatkan tiap versi:

```
 CITRA       BACKBONE        NECK          HEAD         PASCAPROSES
┌────────┐  ┌───────────┐  ┌───────────┐  ┌──────────┐  ┌────────────┐
│640x640 │─>│ konvolusi │─>│ gabungkan │─>│ prediksi │─>│ NMS: buang │
│piksel  │  │bertingkat │  │ fitur     │  │ kotak +  │  │ kotak yang │
└────────┘  └───────────┘  │ lintas    │  │ kelas    │  │ tumpang    │
                           │ skala     │  └──────────┘  │ tindih     │
                           └───────────┘                └────────────┘
 evolusi versi: backbone Darknet -> CSPDarknet; head anchor -> anchor-free
```

Diagram menunjukkan alur data dari citra sampai daftar deteksi. Dua sumbu evolusi utama tercatat pada baris bawah: *backbone* berpindah dari Darknet polos ke varian CSP, dan *head* berpindah dari skema *anchor* ke skema *anchor-free*. Kedua istilah ini dijelaskan pada uraian versi di bawah.

### Sumbu Vertikal: Silsilah Versi 1 sampai 8

Survei menelusuri tiap versi dengan kerangka di atas. Rangkuman perubahannya adalah sebagai berikut; pembahasan primer tiap versi tersedia pada bab-bab fondasi tinjauan ini.

- **YOLOv1 (2016):** deteksi dirumuskan sebagai regresi tunggal pada grid S×S; mencapai 45 *frame* per detik (FPS) dengan 63,4% mAP pada PASCAL VOC 2007 (bab 001).
- **YOLOv2/YOLO9000 (2017):** memperkenalkan *anchor box* (kotak acuan berbentuk tetap yang menjadi titik awal prediksi ukuran objek), *batch normalization* (normalisasi statistik tiap lapis untuk menstabilkan pelatihan), dan pelatihan multi-resolusi (bab 002).
- **YOLOv3 (2018):** prediksi pada tiga skala fitur dengan backbone Darknet-53, memperbaiki deteksi objek kecil (bab 003).
- **YOLOv4 (2020):** backbone CSPDarknet53, varian *Cross Stage Partial* yang membelah aliran fitur untuk menekan biaya komputasi, disertai kumpulan teknik *bag of freebies* (cara menaikkan akurasi tanpa menambah biaya inferensi) (bab 004).
- **YOLOv5 (2020):** implementasi ulang berbasis PyTorch oleh Ultralytics; tanpa makalah resmi, penekanannya pada rekayasa dan kemudahan pelatihan.
- **YOLOv6 (2022):** desain untuk perangkat industri; beralih ke *anchor-free* (posisi objek diprediksi langsung tanpa kotak acuan) dan *decoupled head* (cabang prediksi kelas dan lokasi dipisah) (bab 006).
- **YOLOv7 (2022):** modul E-ELAN (*extended efficient layer aggregation network*, pola penggabungan fitur bertingkat yang lebih kaya) dan *trainable bag of freebies* (bab 007).
- **YOLOv8 (2023):** rilis Ultralytics; *anchor-free* dengan *decoupled head*, dalam satu kerangka yang melayani deteksi, segmentasi, dan estimasi pose.

Cakupan sampai YOLOv8 ini terverifikasi dari daftar rujukan makalah yang memuat YOLO9000, v3, v4, v5, v6, v7, dan v8, serta dari ringkasan indeks Semantic Scholar.

### Sumbu Penunjang: Metrik Evaluasi

Survei menjelaskan metrik agar pembaca dapat menimbang klaim antarmakalah. IoU (*Intersection over Union*) adalah rasio luas irisan terhadap luas gabungan antara kotak prediksi dan kotak kebenaran; deteksi lazim dianggap benar bila IoU mencapai 0,5. Presisi adalah proporsi deteksi yang benar dari seluruh deteksi model, sedangkan *recall* adalah proporsi objek yang ditemukan dari seluruh objek yang ada. AP (*Average Precision*) meringkas kurva presisi-*recall* per kelas, dan mAP adalah rata-rata AP seluruh kelas — metrik utama deteksi objek. FPS mengukur kecepatan; kisaran 30 FPS dianggap ambang *real-time*. Penjelasan metrik pada survei ini merujuk antara lain survei metrik Padilla dkk. (2020) yang tercatat dalam daftar rujukannya.

### Sumbu Penunjang: Dataset

Daftar rujukan menunjukkan survei membahas ketersediaan dataset standar: ImageNet (dataset klasifikasi berisi jutaan citra berlabel, dipakai untuk pralatih *backbone*), MS COCO (80 kelas deteksi dengan anotasi kotak dan segmentasi, tolok ukur utama YOLO modern), serta Open Images dan Objects365 (dataset skala besar untuk pralatih). Pemahaman dataset penting karena angka mAP hanya bermakna bila dibandingkan pada data yang sama.

### Sumbu Penunjang: Pasca-Pemrosesan

Satu objek biasanya diprediksi berkali-kali oleh titik-titik berbeda pada peta fitur. *Non-Maximum Suppression* (NMS) merampingkan duplikasi itu: kandidat diurutkan menurut skor, kandidat terbaik dipertahankan, dan kandidat lain yang IoU-nya terhadap kandidat terbaik melebihi ambang dibuang. Survei meninjau metode pasca-pemrosesan semacam ini — istilah *non-maximum* tercatat pada daftar rujukannya — karena pilihan ambang NMS memengaruhi angka akhir mAP dan *recall*.

### Sumbu Horizontal: Peta Aplikasi

Berdasarkan literatur yang dirujuknya, survei mengelompokkan penerapan YOLO pada sejumlah domain: transportasi dan lalu lintas (kendaraan, rambu), pengawasan dan keamanan (pejalan kaki, wajah), industri (deteksi cacat produk), medis (pencitraan), pertanian (tanaman), serta penginderaan jauh dan wahana udara (citra satelit dan drone). Pola yang sama berulang pada tiap domain: model dasar YOLO disetel halus pada data domain, dan pilihan versi ditentukan oleh timbal balik kecepatan-akurasi — model ringkas untuk perangkat tepi, model besar untuk akurasi maksimal.

## Eksperimen dan Hasil

Sebagai survei, makalah ini tidak melaporkan eksperimen baru; hasilnya berupa sintesis literatur. Tiga hasil terukur dapat diverifikasi dari luar naskah.

1. **Cakupan silsilah lengkap versi 1 sampai 8.** Dari 107 rujukan, daftar pustaka memuat seluruh versi resmi YOLO hingga v8. Interpretasi: pada terbitnya (Maret 2024), makalah ini termasuk sedikit survei yang mencakup YOLOv8 sekaligus materi penunjangnya.
2. **Adopsi komunitas yang tinggi.** Tercatat 418 sitasi pada Crossref, 415 pada OpenAlex, dan 425 pada Semantic Scholar per Juli 2026. Interpretasi: untuk survei berumur dua tahun, angka ini jauh di atas rata-rata dan menunjukkan makalah dipakai sebagai rujukan masuk oleh banyak studi aplikasi.
3. **Kesimpulan lintas domain.** Temuan yang ditarik dari literatur konsisten: tidak ada satu versi YOLO yang terbaik untuk semua tugas; kesesuaian ditentukan kebutuhan kecepatan, akurasi, dan ukuran objek khas domain — model yang unggul pada citra drone belum tentu sesuai untuk inspeksi lini produksi.

## Kelebihan dan Keterbatasan

Kelebihan makalah ini tiga hal. Pertama, keluasan cakupan: model, metrik, dataset, pasca-pemrosesan, dan aplikasi dibahas dalam satu dokumen 40 halaman. Kedua, ketepatan waktu: terbit Maret 2024 dengan cakupan sampai YOLOv8. Ketiga, kebergunaan praktis sebagai rujukan masuk, yang dibuktikan angka sitasi pada bagian sebelumnya.

Keterbatasannya juga jelas. Pertama, cakupan berhenti di YOLOv8; YOLOv9 (bab 008) dan YOLOv10 (bab 009) terbit pada tahun yang sama, sehingga silsilahnya segera tertinggal. Kedua, makalah berstatus akses tertutup — tidak tersedia salinan akses terbuka menurut Unpaywall — sehingga pembaca tanpa langganan hanya menjangkau metadata. Ketiga, secara konseptual, survei seluas ini mengorbankan kedalaman: pembahasan tiap versi bersifat ringkas dibanding makalah aslinya, sehingga angka kinerja tetap harus dirujuk ke bab-bab fondasi. Keempat, makalah berbentuk survei naratif; tidak ditemukan keterangan protokol telaah sistematis pada metadata yang dapat diakses, sehingga pemilihan literaturnya bergantung penilaian penulis.

## Kaitan dengan Bab Lain

Bab ini berada pada klaster Survei YOLO dan berfungsi sebagai peta induk. Ia melanjutkan survei-survei sebelumnya: [bab 028](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md) memotret perkembangan sampai versi-versi awal 2020-an, [bab 026](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md) meninjau sampai YOLOv8 dengan penekanan metrik, dan [bab 034](./034%20-%202023%20-%20Object%20Detection%20using%20YOLO%20%28Diwan%20dkk.%29%20-%20Survei%20YOLO.md) meninjau tantangan serta penerus arsitektur; [bab 033](./033%20-%202024%20-%20Review%20YOLOv8%20%28Sohan%20dkk.%29%20-%20Survei%20YOLO.md) memperdalam khusus YOLOv8. Versi-versi yang dipetakan bab ini dibahas primer pada bab fondasi: [bab 001](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md), [bab 002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md), [bab 003](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md), [bab 004](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md), [bab 006](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md), dan [bab 007](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md). Peta aplikasinya menjadi jembatan ke klaster-klaster terapan tinjauan ini — medis, industri, penginderaan jauh, pertanian — tempat varian turunan tiap versi dibahas satu per satu.

## Poin untuk Sitasi

Kunci BibTeX: `ali2024yoloreview`. Ringkasan yang aman dikutip: "Survei ini mengonsolidasikan evolusi model YOLO dari versi pertama hingga YOLOv8, beserta metrik evaluasi, dataset, metode pasca-pemrosesan, dan peta aplikasinya lintas domain (Multimedia Tools and Applications, vol. 83, hlm. 83535–83574, 2024)."

Catatan wajib sebelum sitasi formal:

1. **Atribusi penulis pada `references.bib` keliru.** Entri `ali2024yoloreview` mencatat "Ali, Md Latifur; Zhang, Zhili", tetapi Crossref, OpenAlex, DBLP, Semantic Scholar, dan Unpaywall seragam mencatat Ajantha Vijayakumar dan Subramaniyaswamy Vairavasundaram (SASTRA Deemed University) sebagai penulis makalah berjudul ini dengan DOI 10.1007/s11042-024-18872-y. Tidak ditemukan makalah lain berjudul sama karya Ali–Zhang pada basis data mana pun. Perbaiki `references.bib` sebelum menyitasi.
2. **Tubuh makalah berbayar.** Hanya metadata dan daftar rujukan yang dapat diverifikasi terbuka. Uraian bab ini disusun dari ringkasan Semantic Scholar dan analisis 107 rujukan; tabel dan angka di dalam naskah belum diverifikasi baris demi baris.
3. **Potensi duplikasi dengan entri 031** (`vijayakumar2024yolo`, judul tercatat "YOLO-Based Object Detection: A Systematic Review and Applications", penulis dan jurnal sama): makalah kedua berjudul demikian tidak ditemukan; kemungkinan besar merujuk karya yang sama. Periksa sebelum menyitasi keduanya sekaligus.
4. Angka sitasi (415–425) adalah potret akses Juli 2026 dan terus berubah.
