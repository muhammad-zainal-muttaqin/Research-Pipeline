# Cek 3 — Makalah yang Sudah Dikenal

Disusun 29 September 2026 untuk langkah Cek 3 rencana verifikasi Bu Fatma.
Berkas ini hanya laporan dan usulan. Tidak ada berkas data, skrip, `.bib`,
atau naskah yang diubah.

Sumber pemeriksaan: `topik/bukti/matriks_bukti.csv` (971 baris),
`topik/records_all.csv` (5.889 rekaman unik), `manuscript/source/references6.bib`
(1.031 entri), `manuscript/source/main6-body.tex`, dan
`main6-appendix-c1.tex`. Metadata makalah yang hilang diperiksa lewat Crossref
REST API, OpenAlex, dan halaman ScienceDirect pada 29 September 2026.

## A. Enam belas makalah yang dikenal

Semua 16 makalah (18 kunci, karena "Gené-Molá 2020" dan "Lai 2023 & Goh 2025
reviews" masing-masing mewakili dua makalah) **ada di peta dan di
`references6.bib`**. Satu catatan penting: **Häni 2020 ada di peta (C2) dan di
`.bib`, tetapi tidak dikutip di teks `main6` maupun di Lampiran A**, jadi
pernyataan "semua 16 ada di draf" hanya benar untuk 15.

| # | Makalah (rencana) | Kunci BibTeX | Kode | Mekanisme / akuisisi | `idx` | Dikutip di badan naskah | Lampiran A |
|---|---|---|---|---|---:|---|---|
| 1 | Stein dkk. 2016 | `stein2016image` | C1 | M4 / V | 766 | ya (6×) | ya |
| 2 | Liu dkk. 2018 | `liu2018robust` | C1 | M3+M4 / V | 723 | ya | ya |
| 3 | Liu dkk. 2019 | `liu2019monocular` | C1 | M3+M4 / V | 699 | ya | ya |
| 4a | Gené-Mola dkk. 2020 (LiDAR, aliran udara) | `genemola2020fruit` | C1 | M4 / S | 672 | ya | ya |
| 4b | Gené-Mola dkk. 2020 (Mask R-CNN + SfM) | `genemola2020fruitb` | C1 | M4 / D | 4032 | ya | ya |
| 5 | Gené-Mola dkk. 2023 | `genemola2023video` | C1 | M3+M2 / V | 449 | ya | ya |
| 6 | Zhang dkk. 2022 (jeruk, OrangeSort) | `zhang2022deep` | C1 | M3+M2 / V | 535 | ya | ya |
| 7 | Lee dkk. 2026 | `lee2026lidarcamera` | C1 | M3+M4 / V | 53 | ya | ya |
| 8 | Rapado-Rincón dkk. 2023 | `rapadorincon2023development` | C1 | M4+M3 / V | 421 | ya | ya |
| 9 | Fusaro dkk. 2026 | `fusaro2026horticultural` | C1 | M5 / T | 37 | ya | ya |
| 10 | Indriani dkk. 2026 (SawitMVC) | `indriani2026sawitmvc` | C1 | DATA / D, per kelas | 24 | ya (6×) | ya |
| 11 | Lai dkk. 2022 | `lai2022real` | C3 | — | 1883 | ya | tidak (bukan C1) |
| 12 | Shiddiq dkk. 2023 | `shiddiq2023counting` | C3 | — | 434 | ya | tidak (bukan C1) |
| 13 | Goh dkk. 2025 (dataset RGB-D) | `goh2025outdoor` | C3 | — | 1509 | ya | tidak (bukan C1) |
| 14 | Suharjito dkk. 2025 (dataset sensus) | `suharjito2025oil` | C3 | — | 117 | ya | tidak (bukan C1) |
| 15a | Lai dkk. 2023 (review) | `lai2023oil` | R | — | 1796 | ya (+ Tabel IV) | tidak |
| 15b | Goh dkk. 2025 (review) | `goh2025fresh` | R | — | 1563 | ya (+ Tabel IV) | tidak |
| 16 | Häni dkk. 2020 | `hani2020comparative` | C2 | — | 1278 | **tidak** | tidak |

Kode diambil dari `matriks_bukti.csv`; nama kode: C1 multipengamatan, C2
penghitungan satu pandang, C3 kelapa sawit, R review. Akuisisi: V video
sepanjang lintasan, D pandangan diskret, S pindaian 3D, T kunjungan ulang.

Hal yang perlu diputuskan manusia (tidak diubah di sini):

1. **Häni 2020 (C2).** Judulnya membandingkan metode deteksi dan penghitungan
   untuk pemetaan hasil apel; dari ingatan penulis berkas ini, studi itu juga
   menggabungkan hitungan dari dua sisi baris. Bila benar, kode C1 (M4 atau M1)
   lebih tepat. **Periksa di teks lengkap pada Cek 5.** Bila tetap C2, putuskan
   apakah perlu dikutip di naskah; saat ini hanya ada di bahan tambahan.
2. **Kunci ganda yang mudah tertukar.** "Liu 2018" juga cocok dengan
   `liu2018tomato` (C2), "Liu 2019" dengan `liu2019improved` (C5), dan
   "Zhang 2022" dengan lima kunci lain (`zhang2022yield` C1 M1, dsb.). Tabel di
   atas memakai kunci yang dikutip naskah pada konteks yang sesuai.
3. **Gené-Mola 2020** punya empat rekaman C1: dua makalah metode (4a, 4b) dan
   dua makalah dataset (`genemola2020fuji`, `genemola2020lfuji`, kode DATA).

## B. Makalah yang hilang: Liu dan Ampatzidis (tinjauan prediksi hasil jeruk)

### B1. Metadata terverifikasi

| Butir | Nilai | Sumber |
|---|---|---|
| Judul | *Shaping the future of citrus yield prediction with multimodal data fusion and machine learning: a systematic review* | Crossref |
| Penulis | Shiyu Liu; Yiannis Ampatzidis (ORCID 0000-0002-3660-3298, penulis korespondensi) | Crossref, OpenAlex |
| Afiliasi | University of Florida, IFAS, Southwest Florida Research and Education Center | OpenAlex |
| Jurnal | *Computers and Electronics in Agriculture* (Elsevier), ISSN 0168-1699 | Crossref |
| Volume, nomor artikel | **256**, 112418 | Crossref |
| DOI | **10.1016/j.compag.2026.112418** | Crossref |
| PII | S0168169926010161 | pengalihan doi.org |
| Terbit daring | 14 September 2026 (Crossref `created`; OpenAlex `publication_date`) | Crossref, OpenAlex |
| Terbitan cetak | **Januari 2027** (`published-print` dan `issued` = 2027-01) | Crossref |
| Jumlah rujukan | 104 (Crossref; 74 ber-DOI); OpenAlex mencatat 80 karya terhubung | Crossref, OpenAlex |
| Kata kunci | Artificial intelligence; Citrus; Hybrid modeling; Remote sensing; UAV; Yield forecasting | ScienceDirect |
| OpenAlex ID | W7212557116 | OpenAlex |
| Status akses terbuka | **Belum pasti.** OpenAlex: *hybrid*, CC BY-NC-ND. Crossref hanya memuat lisensi TDM Elsevier dan STM ASF (tanpa lisensi CC). Halaman ScienceDirect yang diambil otomatis tidak menampilkan label *Open access*. Periksa di peramban; bila tertutup, masukkan ke daftar permintaan PDF Cek 4. | ketiganya |

Abstrak (dari ScienceDirect, verbatim):

> Accurate yield forecasting enables growers and the citrus industry to optimize
> resource allocation, mitigate economic risks, and enhance supply chain
> efficiency. However, existing studies remain fragmented, with substantial
> variation in input features, data acquisition platforms, preprocessing
> strategies, and predictive algorithms, limiting comparability and the
> development of common best practices. This review systematically synthesizes
> the state of the art in citrus yield prediction from four perspectives: (i)
> input features influencing yield; (ii) data acquisition platforms and feature
> extraction methods; (iii) prediction models and analytical approaches; and
> (iv) complementary yield-related methods, including estimation, monitoring,
> and measurement. Comparative analysis of published studies highlights
> consistent trends, such as the importance of fruit counts and canopy spectral
> indices for short-term predictions, the critical but underexplored role of
> mid-term forecasting in bridging imaging and climate-based data regimes, the
> reliance on climatic and soil variables in long-term forecasting, and the
> increasing use of machine learning to capture complex, nonlinear
> interactions. Despite notable progress, critical challenges remain, including
> limited availability of long-term and large-scale datasets, occlusion and
> variability in image-based methods, and poor model transferability across
> orchards, varieties, and growing regions. To address these barriers, future
> research should prioritize standardized and harmonized feature sets, robust
> multi-source data integration, interpretable and hybrid modeling frameworks
> that incorporate biological knowledge, and scalable pipelines capable of
> supporting operational decision-making. By consolidating fragmented
> knowledge, this review provides both the current state of citrus yield
> prediction and a roadmap for advancing toward reliable, transferable, and
> sustainable forecasting systems.

Sorotan (*highlights*) di halaman penerbit: "First systematic review dedicated
to citrus yield prediction with AI and sensing" dan empat butir lain. Judul
seksi yang tampak: *Methodology of literature selection*; *Related methods:
yield estimation, monitoring, and measuring*; *Input features for citrus yield
prediction*; *Data acquisition and feature extraction*; *Yield prediction
methods*; *Technology readiness and deployment analysis*; *Discussion*;
*Expanding the input feature space*; *Conclusion*.

**Tentang klaim "membahas pelacakan, ID switch, dan hitung ganda".** Abstrak,
sorotan, dan kata kunci tidak menyebut *tracking*, *ID switch*, atau *double
counting*; yang disebut hanya "occlusion and variability in image-based
methods". Daftar rujukannya memuat SORT (Bewley 2016), DeepSORT (Wojke 2017),
pelacakan jeruk Zhang dkk. 2022 (`zhang2022deep`), dan Santos dkk. 2024
(pelacakan jeruk dengan relokalisasi 3D, DOI 10.1016/j.compag.2024.109199),
sehingga kemungkinan besar pelacakan dibahas di seksi *Related methods*. Klaim
itu **harus diverifikasi dari teks lengkap** sebelum ditulis di naskah.

### B2. Mengapa pencarian 28 September tidak menemukannya

Ada dua sebab, dan yang kedua lebih menentukan daripada "terlalu baru":

1. Rekaman mungkin belum terindeks Scopus pada 28 September (terbit daring
   14 September).
2. **Artikel ini masuk volume 256 yang bertanggal Januari 2027.** Di
   `records_all.csv`, volume CEA 255 bertanggal 2026-12-01 dan tahun Scopus-nya
   2026, jadi volume 256 hampir pasti bertahun **2027** di Scopus. Semua kueri
   memakai `PUBYEAR > 2011 AND PUBYEAR < 2027`, sehingga menjalankan ulang
   kueri yang sama pun tidak akan menemukannya. Q7 (review buah) sebenarnya
   cocok dengan judul dan abstraknya (*citrus*, *yield prediction*, *machine
   learning*, `DOCTYPE(re)`), jadi yang menahannya adalah batas tahun, bukan
   kata kunci.

Akibatnya bagi naskah: rujukan ini kemungkinan tercetak sebagai
"Comput. Electron. Agric. 256 (2027) 112418", bukan 2026. Naskah perlu satu
kalimat yang menjelaskan bahwa rekaman dari metode lain boleh berada di luar
batas tahun kueri karena terbit daring sebelum tanggal pencarian.

### B3. Usulan entri BibTeX

Kunci mengikuti pola repo (nama keluarga penulis pertama + tahun + kata
pertama judul yang bukan kata tugas). `liu2026shaping` belum dipakai di
`.bib` maupun di matriks. Tahun 2026 dipakai di kunci karena itu tahun terbit
daring; isi `year` menunggu keputusan (lihat pertanyaan untuk Fatma).

```bibtex
@article{liu2026shaping,
  title = {Shaping the future of citrus yield prediction with multimodal data fusion and machine learning: a systematic review},
  author = {Liu, Shiyu and Ampatzidis, Yiannis},
  journal = {Computers and Electronics in Agriculture},
  year = {2027},
  volume = {256},
  pages = {112418},
  doi = {10.1016/j.compag.2026.112418}
}
```

Entri ini **jangan ditempel tangan ke `references6.bib`** karena berkas itu
dibuat ulang oleh `buat_bib.py`. Cara yang sesuai pipeline ada di B5.

### B4. Usulan baris untuk `tab:position`

Format kolom tabel: *Review & Scope & Organizing variable & Stated method &
Identity across views as organizing variable*. Baris diturunkan **dari abstrak,
sorotan, dan judul seksi saja**; semua sel harus dicek ulang ke teks lengkap.
Letakkan setelah baris Rong dkk. 2026 (urutan tahun), sebelum *This review*.

```latex
Liu and Ampatzidis 2027 \cite{liu2026shaping} & Citrus yield prediction: input features, acquisition platforms and feature extraction, prediction models, and related estimation, monitoring, and measurement methods & Input feature, data platform, and model; forecast horizon (short, mid, long term) & Systematic review; search details not stated in the abstract & No\\
```

Catatan untuk sel terakhir: bila teks lengkap ternyata membahas pelacakan dan
hitung ganda sebagai subtopik, jawabannya tetap *No* (pelacakan bukan variabel
pengorganisasi), tetapi kalimat pengantar Seksi 9 ("although several discuss
occlusion and extrapolation from partial counts") bisa ditambah "and one
discusses tracking-based counting \cite{liu2026shaping}". Kalimat pendahuluan
yang mengelompokkan review "by yield-estimation route
\cite{anderson2021technologies,he2022fruit}" juga dapat menambah kutipan ini.

### B5. Cara menambahkannya sesuai pipeline (deskripsi, belum dikerjakan)

Hasil pemeriksaan skrip:

- **`buat_bib.py` sudah mendukung berkas data tambahan.** Argumen `--rekaman`
  dan `--kunci` menerima banyak CSV; rekaman digabung menurut kolom `eid`, lalu
  setiap `key` di CSV `--kunci` yang `eid`-nya ada di rekaman masuk ke `.bib`.
  Satu CSV baru yang memuat kolom `records_all.csv` **ditambah** kolom `key`
  dapat dipakai sekaligus sebagai `--rekaman` dan `--kunci`. Tidak ada perubahan
  kode yang perlu.
- **`kode_bukti.py` dan `matriks_bukti.csv` sebaiknya tidak disentuh.**
  Matriks dibangun dari `kandidat_abstrak.csv` dan keputusan
  `penyaringan/abstrak_*.txt`, yaitu alur Scopus. Memasukkan rekaman metode
  lain ke sana akan mencampur dua alur PRISMA dan mengubah angka 971 dan R 119
  yang harus dapat dihitung ulang dari Scopus.
- **`gambar_tinjauan.py` belum punya kotak "metode lain".** `gambar_prisma()`
  hanya menggambar satu kolom (Scopus) dengan kotak eksklusi di kanan
  (x = 56–98 pada kanvas 0–100). Perlu perubahan kode kecil, bukan berkas data
  saja; karena itu **tidak dikerjakan di sini** (skrip bersama, dan agen lain
  sedang bekerja).

Langkah yang diusulkan:

1. Buat berkas baru `literature/scopus-2026-09/topik/tambahan_metode_lain.csv`
   (belum dibuat; isi siap-simpan di bawah). `eid` memakai ID semu karena belum
   ada EID Scopus; ganti dengan EID asli bila rekaman sudah terindeks. Kolom
   `year` mengikuti keputusan Fatma (2026 terbit daring atau 2027 volume).

   ```csv
   idx,eid,doi,title,first_author,year,cover_date,source,source_type,doc_type,volume,issue,pages,article_number,cited_by,open_access,issn,eissn,affil_country,qids,dup_eids,key,kode,metode,tanggal_identifikasi,catatan
   L1,lain-0001,10.1016/j.compag.2026.112418,Shaping the future of citrus yield prediction with multimodal data fusion and machine learning: a systematic review,Liu S.,2027,2027-01-01,Computers and Electronics in Agriculture,Journal,Review,256,,,112418,0,,01681699,,United States,,,liu2026shaping,R,daftar makalah dikenal (Cek 3),2026-09-29,terbit daring 2026-09-14; volume Januari 2027 di luar PUBYEAR<2027
   ```

2. Tambahkan berkas itu ke perintah BibTeX di `literature/scopus-2026-09/README.md`:
   `--rekaman ... literature/scopus-2026-09/topik/tambahan_metode_lain.csv`
   dan `--kunci ... literature/scopus-2026-09/topik/tambahan_metode_lain.csv`.
   Bila Crossref tidak terjangkau saat skrip berjalan, `buat_bib.py` memakai
   cadangan `Liu, S. and others`; jalankan dari jaringan yang bisa mencapai
   `api.crossref.org` agar daftar penulis lengkap masuk `crossref.jsonl`.
   Field `scopuseid` akan berisi `lain-0001`; itu wajar untuk rekaman non-Scopus.
3. Ubah `gambar_prisma()` agar membaca CSV itu bila ada: kanvas diperlebar
   (mis. `figsize=(9.2, 5.6)`, `xlim` 0–130), kolom kanan berjudul
   *Identification of studies via other methods* dengan kotak *Records
   identified from: check of known papers (n = 1)* → *Reports assessed for
   eligibility (n = 1)* → *Reports excluded (n = 0)*, lalu panah ke kotak
   inklusi yang menulis *Studies included, n = 971 + 1 = 972* (atau
   *971 from Scopus; 1 from other methods*). Jumlah per kelompok di kotak itu
   (R 119) tetap angka Scopus kecuali Fatma memutuskan lain.
4. Setelah skrip dijalankan ulang: perbarui kalimat Seksi 2.7 (*Result of the
   search*), keterangan Gambar 1, Tabel IV, dan angka `.bib` (1.031 → 1.032;
   dikutip 271 → 272) di `PROTOKOL.md` dan `AGENTS.md` §3.

## C. Persiapan *snowballing* (opsional Cek 3)

Rincian ada di `kandidat_snowballing.csv`. Ringkasan cara kerja:

- Lima review terdahulu yang paling dekat dengan penghitungan buah lintas
  pengamatan dipilih dari kelompok R dan Tabel IV: Gongal dkk. 2015
  (`gongal2015sensors`), Koirala dkk. 2019 (`koirala2019deepb`), Anderson dkk.
  2021 (`anderson2021technologies`), He dkk. 2022 (`he2022fruit`), dan Rong
  dkk. 2026 (`rong2026research`). Daftar rujukan Liu dan Ampatzidis juga
  diperiksa sebagai tambahan.
- Daftar rujukan diambil dari Crossref (110, 83, 124, 95, 119, dan 104 entri).
  Judul yang mengisyaratkan penghitungan dari beberapa pengamatan (dua sisi,
  citra berurutan, video, pelacakan, 3D, SfM, LiDAR + kamera) dicocokkan ke
  `records_all.csv` menurut DOI, lalu menurut judul (difflib ≥ 0,8).
- Hasil: 57 judul diperiksa (termasuk sembilan kontrol yang memang sudah
  dikutip naskah, misalnya Song 2014, Wang 2013, Gongal 2016); **45 sudah ada
  di `records_all.csv`** (kueri Scopus menangkapnya) dan **12 tidak ada**. Dua
  dari 12 dibuang karena jelas citra tunggal (Chen dan Lee 2014; Sengupta dan
  Lee 2014), sehingga **10 masuk CSV**. Dari 10 itu hanya tiga yang kuat dan
  berada dalam rentang tahun: Payne dkk. 2014 (mangga, citra malam dua sisi),
  Apolo-Apolo dkk. 2020 (*Eur. J. Agron.*, jeruk dari UAV), dan Gongal dkk. 2014
  (prosiding ASABE, sistem over-the-row dua sisi). Empat lemah (satu di
  antaranya praprint arXiv), dan tiga terbit sebelum 2012 (hanya catatan).
- Temuan sampingan: dua rekaman kuat yang lolos pencarian tetapi tidak
  tertangkap kueri memakai frasa "Estimating ... yield" atau "estimation of the
  yield", bukan `"yield estimat*"`. Ini celah frasa kueri yang layak disebut di
  keterbatasan bila Fatma setuju.

Rekaman yang **sudah ada** di `records_all.csv` tetapi kodenya patut dicek pada
Cek 2 atau Cek 5 (bukan keputusan, hanya penanda):

| Rekaman | Status sekarang | Alasan dicek |
|---|---|---|
| Underwood dkk. 2016, *Mapping almond orchard canopy volume, flowers, fruit and yield using lidar and vision sensors* (10.1016/j.compag.2016.09.014) | **X di tahap judul** | LiDAR + kamera sepanjang baris, buah per pohon; mungkin C1 atau C5 |
| Zhou dkk. 2025, *Agrosense* (10.1007/s11119-025-10268-8) | X di tahap judul | sistem pemantauan kebun tingkat pohon; Agrosense v2 justru C2 |
| Payne dkk. 2013 (10.1016/j.compag.2012.11.009); Koirala dkk. 2019 MangoYOLO (10.1007/s11119-019-09642-0); Anderson dkk. 2019 (10.1007/s11119-018-9614-1); Qureshi dkk. 2017 (10.1007/s11119-016-9458-5); Koirala dkk. 2021 (10.3390/agronomy11020347) | C2 | hitungan dari dua sisi pohon dijumlah lalu dikalibrasi; menurut definisi C1 naskah ("combine several observations of the same fruit") ini M0/M1 dengan pandangan diskret |
| Linker 2017 (10.1007/s11119-016-9467-4) dan Linker 2018 (10.1016/j.biosystemseng.2018.01.003) | C2 | kelanjutan Linker 2015 (`linker2015estimation`, C1 M1, enam citra per pohon); pengodean belum konsisten |
| Bellocchio dkk. 2020 (10.1109/LRA.2020.2966398) | C2 | memakai konsistensi spasial antar-pandang |
| Vasconez dkk. 2020 (10.1016/j.compag.2020.105348) | C2 | penghitungan pada video; perlu cek apakah memakai pelacakan |
| Häni dkk. 2020 (10.1002/rob.21902) | C2 | lihat bagian A |

Tambahan kecil: di `matriks_bukti.csv`, akuisisi C1 metode adalah V 135, D 37,
S 5, T 3, dan **1 (satu pandang) 2**. Naskah Seksi 3.4 hanya menyebut empat
angka pertama (jumlah 180 dari 182).
