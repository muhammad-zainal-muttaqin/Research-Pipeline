# 176 - ZoeDepth: Zero-Shot Transfer by Combining Relative and Metric Depth

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bhat2023zoedepth` |
| Judul asli | ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth |
| Penulis | Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter Wonka, Matthias Müller |
| Tahun | 2023 |
| Venue | arXiv preprint arXiv:2302.12288 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2302.12288
- **Google Scholar:** https://scholar.google.com/scholar?q=ZoeDepth%3A%20Zero-Shot%20Transfer%20by%20Combining%20Relative%20and%20Metric%20Depth
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ZoeDepth%3A%20Zero-Shot%20Transfer%20by%20Combining%20Relative%20and%20Metric%20Depth&sort=relevance

## Gambaran Umum

ZoeDepth mengusulkan model estimasi kedalaman monokular (dari satu citra RGB) yang menggabungkan dua sifat yang sebelumnya sulit didapat bersamaan: generalisasi lintas-domain dari model *depth* relatif, dan skala metrik (satuan nyata, misalnya meter) dari model *depth* metrik. Pendekatannya bertahap dua tahap: pra-pelatihan pada *depth* relatif memakai gabungan dua belas kumpulan data, diikuti penambahan kepala prediksi metrik ringan yang disebut *metric bins module* (modul bin metrik) dan disetel halus (*fine-tuning*) pada data berlabel metrik. Penulis melaporkan model gabungan mereka meningkatkan galat relatif absolut (REL) pada NYU Depth v2 sekitar 21% dibandingkan metode metrik terbaik sebelumnya, sekaligus mempertahankan generalisasi zero-shot (tanpa pelatihan ulang) ke delapan kumpulan data yang tidak pernah dilihat saat pelatihan.

Kontribusi utamanya adalah arsitektur yang memisahkan tanggung jawab: *backbone* (jaringan tulang punggung) belajar struktur *depth* umum dari data relatif yang melimpah dan beragam domain, sedangkan kepala metrik domain-spesifik menerjemahkan struktur itu menjadi jarak nyata. Model penuh, disebut ZoeD-M12-NK, dilatih pada gabungan domain indoor dan outdoor sekaligus tanpa penurunan akurasi berarti pada kedua domain — sebuah hasil yang menurut penulis belum dicapai model metrik sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi *depth* monokular terbagi menjadi dua aliran riset dengan tujuan berbeda. Aliran pertama, *depth* relatif, dipelopori model seperti MiDaS: dilatih pada campuran banyak kumpulan data dari sumber heterogen (foto internet, video, sintesis), sehingga menggeneralisasi baik ke domain baru, tetapi keluarannya hanya urutan kedalaman relatif antarpiksel — tanpa skala satuan nyata, sehingga tidak langsung dapat dipakai untuk pengukuran jarak atau rekonstruksi 3D yang presisi. Aliran kedua, *depth* metrik, dilatih langsung dengan target kedalaman berlabel meter pada satu kumpulan data spesifik (misalnya NYU Depth v2 untuk indoor atau KITTI untuk outdoor), sehingga akurat pada domain itu tetapi jatuh performanya secara tajam bila diuji pada domain lain — sebuah model yang dilatih pada ruangan kantor umumnya gagal menaksir jarak pada jalan raya.

Upaya sebelumnya seperti AdaBins dan LocalBins memperbaiki akurasi metrik lewat mekanisme *adaptive binning* (pembagian rentang kedalaman menjadi sejumlah bin yang lebar dan posisinya disesuaikan per citra), tetapi tetap dilatih dan dievaluasi dalam satu domain tunggal. Belum ada model yang menggabungkan kekuatan pra-pelatihan relatif skala besar dengan keluaran metrik yang akurat pada lebih dari satu domain sekaligus. ZoeDepth diposisikan untuk mengisi celah ini: menghasilkan satu model yang memprediksi kedalaman berskala metrik namun tetap general seperti model relatif.

## Ide Utama

Gagasan inti ZoeDepth adalah memisahkan pelatihan menjadi dua tahap yang saling melengkapi. Tahap pertama melatih *encoder-decoder* (jaringan penyandi-pengurai fitur) pada tugas *depth* relatif memakai gabungan dua belas kumpulan data, sehingga jaringan mempelajari representasi struktur kedalaman yang kaya dan tidak terikat satu domain. Tahap kedua menempelkan kepala prediksi tambahan — modul bin metrik — di atas *decoder* yang sudah terlatih itu, lalu menyetel halus keseluruhan jaringan dengan target *depth* metrik dari NYU Depth v2 dan/atau KITTI.

Modul bin metrik bekerja dengan memprediksi sejumlah pusat bin kedalaman (nilai kedalaman kandidat) untuk tiap citra, kemudian menghitung kedalaman akhir tiap piksel sebagai kombinasi bobot dari pusat-pusat bin tersebut. Bobot ini diperhalus lewat lapisan yang disebut *attractor* (penarik): lapisan ini menggeser posisi pusat bin awal secara bertahap berdasarkan fitur multi-skala dari *decoder*, sehingga posisi bin makin presisi menjelang lapisan akhir jaringan. Karena kedalaman bersifat berurutan (bin yang berdekatan mewakili jarak yang berdekatan pula), distribusi bobot bin dihitung memakai distribusi log-binomial, bukan *softmax* biasa — pilihan ini menjaga sifat berurutan antarbin alih-alih memperlakukannya sebagai kelas independen.

## Cara Kerja Langkah demi Langkah

### Tahap 1 — Pra-pelatihan Depth Relatif

Jaringan *backbone* memakai arsitektur bertipe MiDaS/DPT (*Dense Prediction Transformer*, arsitektur berbasis *transformer* untuk prediksi padat per piksel). Jaringan ini dilatih pada dua belas kumpulan data *depth* relatif yang digabung, mencakup citra indoor, outdoor, dan sintetis dengan label kedalaman berskala tak seragam. Tujuan tahap ini semata melatih jaringan mengenali struktur permukaan, tepi objek, dan urutan kedalaman — bukan nilai metrik absolut. Hasil tahap ini adalah *backbone* dengan bobot awal yang sudah terbukti menggeneralisasi ke domain visual yang luas, sama seperti model MiDaS pada umumnya.

### Tahap 2 — Modul Bin Metrik dan Attractor

Di atas *decoder* tahap pertama, ditempelkan kepala metrik ringan. Untuk setiap citra, kepala ini memprediksi satu himpunan awal pusat bin kedalaman, misalnya 64 pusat yang tersebar pada rentang kedalaman domain yang ditarget (0–10 meter untuk indoor, 0–80 meter untuk outdoor). Lapisan *attractor* kemudian menyempurnakan posisi pusat-pusat ini secara berjenjang mengikuti resolusi fitur yang membesar di *decoder*: pada resolusi rendah, pusat bin digeser secara kasar; pada resolusi tinggi, pergeseran menjadi halus dan spesifik-piksel. Kedalaman akhir tiap piksel dihasilkan dari jumlah berbobot pusat bin akhir, dengan bobot dihitung lewat distribusi log-binomial berdasarkan fitur piksel tersebut.

### Router Domain untuk Model Multi-Dataset

Ketika model dilatih pada lebih dari satu kumpulan data metrik sekaligus (varian ZoeD-M12-NK, dilatih pada NYU Depth v2 dan KITTI bersamaan), setiap citra masukan pertama melewati pengklasifikasi laten ringan yang menentukan citra tersebut kemungkinan berasal dari domain indoor atau outdoor, lalu merutekannya ke kepala metrik yang sesuai. Mekanisme ini memungkinkan satu jaringan *backbone* dibagi pakai lintas-domain sementara kepala metriknya tetap terspesialisasi, sehingga menghindari penurunan akurasi yang biasanya muncul saat satu kepala tunggal dipaksa menangani rentang kedalaman indoor dan outdoor yang berbeda jauh skalanya.

Diagram berikut merangkum alur dua tahap tersebut:

```
tahap 1: pra-latih relatif          tahap 2: fine-tune metrik
┌──────────────────────┐            ┌───────────────────────────┐
│ 12 dataset depth      │            │ backbone hasil tahap 1      │
│ relatif (indoor+      │  bobot     │  + modul bin metrik         │
│ outdoor+sintetis)     │ ────────► │  + lapisan attractor        │
└──────────────────────┘  awal      │  + router domain (opsional) │
                                     └──────────────┬──────────────┘
                                                     │
                                    citra masukan ──►│── router ──► kepala N (indoor)
                                                     │           atau kepala K (outdoor)
                                                     ▼
                                            peta depth metrik (meter)
```

Diagram ini menunjukkan bahwa bobot dari pra-pelatihan relatif menjadi titik awal, bukan target akhir; skala metrik hanya diperoleh setelah kepala bin dan *attractor* ditambahkan dan disetel halus pada data berlabel metrik.

### Varian Model

Penulis melaporkan beberapa varian sesuai kombinasi data pelatihan: model yang dilatih langsung pada data metrik tanpa pra-pelatihan relatif (misalnya ZoeD-N untuk NYU saja, ZoeD-K untuk KITTI saja, ZoeD-NK untuk keduanya), dan model dengan pra-pelatihan dua belas dataset relatif (ZoeD-M12-N, ZoeD-M12-K, ZoeD-M12-NK). Perbandingan antarvarian dipakai untuk mengisolasi kontribusi pra-pelatihan relatif terhadap akurasi metrik akhir.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada NYU Depth v2 (kumpulan data indoor dengan label kedalaman dari sensor RGB-D) dan KITTI (kumpulan data outdoor dari kendaraan berkamera dan LiDAR), memakai metrik standar estimasi *depth*: REL (galat relatif absolut, rata-rata selisih absolut antara prediksi dan kebenaran dibagi kebenaran — makin kecil makin baik), RMSE (*root mean square error*, akar rata-rata kuadrat galat), dan delta1 (persentase piksel dengan rasio prediksi-terhadap-kebenaran di bawah ambang 1,25).

Pada NYU Depth v2, penulis melaporkan peningkatan REL sekitar 21% dibandingkan metode metrik *state-of-the-art* sebelumnya (di antaranya NeWCRFs, dibahas pada bab 179). Angka ini menunjukkan galat relatif model menyusut sekitar seperlima dibandingkan pembanding terbaik pada domain yang sama — sebuah perbaikan besar untuk tugas yang sudah kompetitif.

Pengujian generalisasi dilakukan pada delapan kumpulan data yang tidak dilihat saat pelatihan metrik, mencakup domain indoor dan outdoor lain. Penulis melaporkan peningkatan zero-shot yang sangat besar pada sebagian dataset tersebut, termasuk klaim peningkatan REL hingga 976,4% pada dataset DIML Outdoor dibandingkan baseline metrik yang tidak memakai pra-pelatihan relatif. Angka sebesar ini kemungkinan mencerminkan kegagalan total model baseline pada domain di luar cakupan pelatihannya, bukan semata keunggulan absolut ZoeDepth; interpretasi tepatnya perlu dicek pada tabel lengkap naskah asli. Secara umum, temuan eksperimen menunjukkan bahwa pra-pelatihan relatif skala besar adalah faktor dominan di balik generalisasi zero-shot, sedangkan modul bin metrik dan *attractor* berkontribusi pada presisi metrik akhir setelah *fine-tuning*.

## Kelebihan dan Keterbatasan

Kelebihan utama ZoeDepth terletak pada penyatuan dua tujuan yang secara historis dianggap berkompromi: skala metrik dan generalisasi domain. Arsitekturnya modular — *backbone* relatif dapat dipakai ulang untuk domain metrik baru hanya dengan melatih kepala bin baru, tanpa mengulang pra-pelatihan besar. Router domain pada varian gabungan memungkinkan satu model melayani indoor dan outdoor tanpa kepala tunggal yang dipaksa menangani rentang skala yang jauh berbeda.

Dari sisi rekayasa, ketergantungan pada router domain berarti akurasi model gabungan bergantung pada seberapa tepat pengklasifikasi laten menebak domain citra; kesalahan rute berpotensi menghasilkan prediksi kedalaman pada skala yang salah. Secara konseptual, model tetap memerlukan data metrik berlabel dari domain yang ingin dicapai akurasi tingginya — generalisasi zero-shot yang dilaporkan baik untuk domain yang mirip NYU/KITTI, tetapi domain yang sangat berbeda (misalnya citra bawah air atau medis) kemungkinan tetap membutuhkan *fine-tuning* tambahan. Jumlah bin dan rentang kedalaman per domain juga merupakan hiperparameter yang ditentukan di muka, sehingga model kurang fleksibel terhadap rentang kedalaman ekstrem yang tidak diantisipasi saat perancangan kepala metrik.

## Kaitan dengan Bab Lain

ZoeDepth mewarisi *backbone* dan filosofi pra-pelatihan lintas-dataset dari garis model *depth* relatif seperti MiDaS, dan berbagi prinsip modul bin adaptif dengan AdaBins/LocalBins yang mendahuluinya. Pada klaster Estimasi Kedalaman dalam tinjauan ini, ZoeDepth berada di antara pendekatan *depth* relatif murni yang dibahas pada bab [175 - 2024 - Depth Anything V2](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md) — yang juga mengandalkan pra-pelatihan skala besar tetapi tanpa kepala metrik eksplisit — dan pendekatan metrik langsung seperti bab [179 - 2022 - NeWCRFs](./179%20-%202022%20-%20NeWCRFs%20-%20Estimasi%20Kedalaman.md), salah satu pembanding yang dilampaui pada NYU Depth v2. Bab [177 - 2023 - Metric3D](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md) mengangkat masalah serupa — metrik yang general lintas-kamera — dengan strategi berbeda (normalisasi geometri kamera alih-alih router domain). Bab [178 - 2024 - Marigold](./178%20-%202024%20-%20Marigold%20-%20Estimasi%20Kedalaman.md) mendekati generalisasi *depth* lewat model difusi, jalur arsitektur yang berbeda dari pendekatan diskriminatif berbasis bin pada ZoeDepth. Bagi pipeline RGB-D pada tinjauan ini, ZoeDepth relevan sebagai sumber pseudo-*depth* berskala metrik dari kamera RGB tunggal tanpa sensor kedalaman khusus.

## Poin untuk Sitasi

Kutip dengan kunci `bhat2023zoedepth`. Ringkasan yang aman dikutip: "ZoeDepth menggabungkan pra-pelatihan *depth* relatif pada dua belas kumpulan data dengan modul bin metrik dan lapisan *attractor* yang disetel halus pada data metrik (NYU Depth v2, KITTI), mencapai peningkatan REL sekitar 21% pada NYU Depth v2 dibanding metode metrik sebelumnya serta generalisasi zero-shot ke delapan kumpulan data tak terlihat." Angka 21% REL pada NYU Depth v2 dan klaim peningkatan hingga 976,4% REL pada DIML Outdoor perlu diverifikasi ulang terhadap tabel lengkap pada naskah asli sebelum dikutip dalam karya formal, termasuk nilai RMSE dan delta1 spesifik yang tidak dikutip di sini karena belum terkonfirmasi presisi angkanya dari sumber yang diakses.
