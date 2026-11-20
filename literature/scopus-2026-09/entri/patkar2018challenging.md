# Challenging İssues in automated oil palm fruit grading

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `patkar2018challenging` |
| Judul asli | Challenging İssues in automated oil palm fruit grading |
| Penulis | Patkar, Gaurang S; Anjaneyulu, G.S.G.N; P.V.S.S.R, Chandra Mouli |
| Tahun | 2018 |
| Venue | Iaes International Journal of Artificial Intelligence |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [patkar2018challenging.pdf](../pdf/patkar2018challenging.pdf)
- DOI resmi: https://doi.org/10.11591/ijai.v7.i3.pp111-118

## Gambaran Umum

Artikel ini adalah tinjauan pustaka tentang masalah dalam penilaian mutu (grading) buah kelapa sawit secara otomatis. Masalah utamanya adalah cara penilaian manual yang lambat dan rawan kesalahan manusia, sehingga dikembangkan sistem penglihatan mesin berbasis pemrosesan citra dan logika fuzzy. Penulis menyusun tinjauan ini untuk mengumpulkan metode yang dipakai peneliti sebelumnya dan mengidentifikasi persoalan yang belum mendapat perhatian. Karena berupa tinjauan, artikel ini tidak menyajikan eksperimen baru; angka yang dilaporkan berasal dari kajian yang ditinjau.

Data dan metode yang ditinjau berfokus pada buah dan tandan buah segar (TBS) *Elaeis guineensis*. Penulis menjelaskan struktur buah (eksokarp, mesokarp pengandung minyak, dan endokarp), tiga varietas (Dura, Tenera, dan Pisifera), serta empat tahap kematangan, yaitu mentah (*unripe*), belum matang (*underripe*), matang (*ripe*), dan terlalu matang (*overripe*). Kajian yang ditinjau memakai model warna RGB, HSI, HSV, dan L*a*b*, serta teknik logika fuzzy, jaringan saraf tiruan, analisis komponen utama (PCA), pembelajaran Hebb, fotogrametri, pengukuran jarak pada histogram warna, dan operator deteksi tepi. Sumber data berupa citra buah yang diambil di kebun, antara lain dengan kamera Nikon Coolpix 4500 dan sistem visi Keyence, serta data statistik dari Godrej Agrovet Pvt. Ltd., Goa.

Mekanisme deteksi yang dominan adalah klasifikasi kematangan berbasis warna: fitur warna diekstrak dari citra, lalu dipetakan ke kategori kematangan dengan logika fuzzy atau pengklasifikasi jaringan saraf. Beberapa kajian mengaitkan kandungan minyak mesokarp dengan nilai warna, khususnya kanal merah; kajian lain membandingkan model warna atau menguji jarak pada histogram warna. Penulis juga mencatat pendekatan deteksi tepi untuk menilai mutu buah yang diadopsi dari kajian buah mangga.

Terkait angka hasil dan metrik, artikel ini tidak melaporkan angka atau metrik dari percobaan sendiri. Angka yang dikutip dari kajian yang ditinjau mencakup estimasi regresi 0,86 untuk hubungan antara kandungan minyak jaringan mesokarp dan pita warna merah (Choong dkk.), serta temuan bahwa komponen merah pada kategori mentah dan belum matang hampir sama (Ghazali dkk.), yang bertentangan dengan hasil tersebut. Penulis menyatakan bahwa jaringan saraf yang dilatih dengan fitur hasil reduksi PCA memiliki akurasi klasifikasi lebih tinggi daripada jaringan dengan fitur lengkap, dan bahwa *Fuzzy Moving K-means* mengklasifikasi citra lebih tepat daripada tiga algoritme lain, tanpa menyebutkan nilai akurasi numeriknya.

Batasan yang dikemukakan penulis mencakup sebelas masalah yang belum ditangani kajian terdahulu: model warna bergantung pada kondisi lingkungan yang tidak dapat diprediksi; spesifikasi kamera memengaruhi kompleksitas algoritme; letak kamera perlu dipilih karena warna buah tidak seragam dari pangkal ke ujung; kompleksitas waktu algoritme tidak pernah dinyatakan; sebagian besar kajian dilakukan di lingkungan terkendali sehingga rentan terhadap perubahan pencahayaan; belum ada kajian yang mengklasifikasikan varietas Dura, Tenera, dan Pisifera; deteksi penyakit dan hama belum dilakukan; warna eksokarp berbeda antarwilayah sehingga tidak dapat digeneralisasi; beberapa kajian hanya memakai tiga kategori padahal ada empat; persentase asam lemak bebas (FFA) belum dipertimbangkan; dan jumlah buah yang rontok belum diteliti sebagai penentu kategori. Penulis menyimpulkan perlunya model umum yang menggabungkan faktor-faktor tersebut agar sistem penilaian dapat diterapkan dalam berbagai kondisi.
