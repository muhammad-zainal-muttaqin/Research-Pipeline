# Advancements and Challenges in Deep Learning-Based Person Re-Identification: A Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2025advancements` |
| Judul asli | Advancements and Challenges in Deep Learning-Based Person Re-Identification: A Review |
| Penulis | Zhao, Liang; Han, Yuyan; Chen, Zhihao |
| Tahun | 2025 |
| Venue | Electronics Switzerland |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhao2025advancements.pdf](../pdf/zhao2025advancements.pdf)
- DOI resmi: https://doi.org/10.3390/electronics14224398

## Gambaran Umum

Artikel tinjauan ini mengkaji *person re-identification* (Re-ID), yaitu pencocokan individu lintas jaringan kamera yang terpisah dalam sistem pengawasan. Masalah utamanya adalah penurunan kinerja yang tajam pada kondisi dunia nyata yang tidak terkendali, seperti oklusi berat, variasi pose, perbedaan sudut pandang antarkamera, ketidaksejajaran spasial, dan citra beresolusi rendah. Penulis juga mencatat tiga celah pada tinjauan sebelumnya, yaitu pemahaman yang terbatas tentang struktur kolaborasi komunitas riset, fokus yang sempit pada benchmark konvensional, serta belum adanya taksonomi terpadu yang membedakan metode unimodal dan multimodal. Kebaruan yang diklaim terdiri atas analisis jaringan kolaborasi global, taksonomi 20 dataset benchmark dalam enam kategori modalitas, dan kerangka hierarkis yang mengelompokkan 82 metode mutakhir ke dalam 15 subkelas teknis.

Data yang dianalisis bukan tanaman—tanaman, data pertanian, dan mekanisme deteksi atau asosiasi pada tanaman tidak dinyatakan. Korpusnya terdiri atas 2067 artikel ilmiah yang terdiri dari 225 makalah konferensi dan 1842 artikel jurnal, diambil dari Web of Science serta venue CVPR, ICCV, dan ECCV untuk rentang Januari 2019 hingga Agustus 2024. Penyeleksian mengikuti pedoman PRISMA 2020 dan 2023: setelah penghapusan duplikat dan penyaringan, diperoleh 88 artikel teknis dan 5 tinjauan penting, dengan kriteria eksklusi divalidasi oleh tiga pakar (Fleiss' κ = 0,82). Analisis bibliometrik memakai Gephi 0.9.7 untuk jaringan penulis dan BibExcel untuk statistik kata kunci. Mekanisme asosiasi yang ditinjau mencakup pembelajaran fitur diskriminatif, *metric learning*, normalisasi lintas domain, pencocokan multiview, penyisipan fitur lintas modalitas (teks–gambar, video, inframerah–tampak), serta pendekatan berbasis Transformer dan model bahasa besar.

Penulis menyusun taksonomi dataset berdasarkan modalitas dan mendefinisikan metrik evaluasi. Dataset citra mencakup CUHK-01 (3884 citra, 971 identitas), Market-1501 (32.668 kotak, 1501 identitas), DukeMTMC-reID (36.411 citra, 1812 identitas), dan MSMT17 (126.441 citra, 4101 identitas); dataset video mencakup MARS (20.715 *tracklet*, 1261 identitas) dan LPW (7694 *tracklet*, 2731 identitas); dataset teks mencakup CUHK-PEDES (40.206 citra, 13.003 identitas); dataset inframerah–tampak mencakup SYSU-MM01 (45.863 citra, 491 identitas) dan LLCM (46.767 citra, 1064 identitas). Metrik yang dipakai adalah CMC/Rank-k dan mAP, dengan rumus pada persamaan (1)–(7); mAP dinilai paling tepat untuk retrieval berskala besar karena memperhitungkan urutan hasil. Penulis menegaskan bahwa seluruh angka kinerja pada tabel dikutip langsung dari publikasi asli, sehingga perbedaan kecil pada rincian implementasi tetap mungkin.

Beberapa angka hasil dapat dijadikan acuan. Secara bibliometrik, pertumbuhan tahunan majemuk artikel jurnal mencapai 42,7% berbanding 28,3% untuk makalah konferensi; jaringan kolaborasi terdiri atas 5413 simpul dan 15.455 sisi dengan koefisien klasterisasi 0,81, indeks modularitas 0,67, diameter 14, serta distribusi derajat mengikuti hukum pangkat (γ = 2,1; R² = 0,92). Secara kinerja, metode rekonstruksi 3D multiview Yu dkk. mencatat Rank-1 95,7% dan mAP 90,2% pada Market-1501 serta Rank-1 91,4% pada DukeMTMC-reID (Tabel 9); TCRL mencatat Rank-1 77,3% pada iLIDS-VID (Tabel 22); KADDL mencatat Rank-10 97,2% pada PRID-2011 (Tabel 23). Penulis juga melaporkan penurunan kinerja 41,6% dari siang ke malam dan 58,9% dari perkotaan ke pedesaan, 68% waktu inferensi terbuang pada wilayah non-diskriminatif, serta akurasi Rank-1 hanya 32,6% pada kueri atribut komposisional.

Batasan yang ditekankan penulis mencakup bias anotasi, tukar-menukar akurasi dan skalabilitas, serta konflik privasi–utilitas dalam penerapan nyata. Tinjauan ini juga menyoroti defisit validasi ekologis karena lebih dari 78% metode masih dioptimalkan untuk skenario benchmark terbatas, kerentanan arsitektural berupa penurunan kinerja 58% di bawah serangan topologi, ketiadaan batas generalisasi formal pada 89% metode, dan hanya 12% kajian yang membahas privasi. Arah masa depan yang diusulkan meliputi pembelajaran representasi kausal, integrasi neuro-simbolik, sistem yang berevolusi sendiri melalui pembelajaran berkelanjutan, serta tata kelola privasi memakai *differential privacy* dan *federated learning*.

