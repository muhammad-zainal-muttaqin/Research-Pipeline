# Catatan Eksperimen — SawitMVC

Log eksperimen yang **hanya bertambah** (*append-only*). Entri lama tidak diedit
untuk "memperbaiki" hasil; kalau kesimpulan berubah, tulis entri baru yang
merujuk entri lama.

**Hasil negatif wajib dicatat.** Justru itu isi paling berharga di sini — ia
mencegah jalan buntu yang sama ditempuh dua kali, dan menjawab pertanyaan
reviewer "apa saja yang sudah dicoba".

**Laporan per-ide ada di [`docs/SR/`](SR/)** — tiap SR merangkum satu ide dari
masalah → ide → solusi → hasil → putusan. Berkas ini adalah **log kronologis**
(E-NNN); SR adalah **pandangan per-ide**. Tiap entri E-NNN di bawah menyebut ide
dan SR yang memuatnya.

Kode eksperimen dijalankan di `/workspace/experiments/` (di luar repo). Snapshot
**kode + hasil JSON + split**-nya diarsipkan ke [`../experiments/`](../experiments/)
di repo ini agar tiap perintah reproduksi tetap punya sumbernya; artefak besar
(bobot, dataset turunan) tidak diarsipkan karena bisa dibuat ulang dari skrip —
lihat [`experiments/README.md`](../experiments/README.md).

Format tiap entri:

```
## E-NNN — Judul   (YYYY-MM-DD)
**Hipotesis** — apa yang diuji, dan apa yang akan memalsukannya
**Cara** — data, konfigurasi, skrip
**Hasil** — angka apa adanya
**Putusan** — DIKONFIRMASI / DIPALSUKAN / TIDAK KONKLUSIF, plus alasannya
**Dampak** — apa yang berubah pada rencana
```

Status: `DIKONFIRMASI` · `DIPALSUKAN` · `TIDAK KONKLUSIF` · `BERJALAN`

---

## Peta Ide Solusi

Sebelas ide, semuanya berlabuh pada korpus 182 sumber. I-1…I-6 adalah jalur DA3
inti; I-7…I-11 diambil dari agenda riset naskah sendiri (`evidence-body.tex`
§208, §234–262, §265, §174) sebagai cadangan bila jalur inti mentok. Eksperimen
di bawah menyebut ide yang diujinya.

| Ide | Isi | Sumber |
|---|---|---|
| **I-1** | DA3 multi-view pada video orbit | entri 198 |
| **I-2** | DA3 multi-view pada 4 sisi foto asli | entri 198 |
| **I-3** | Bangkitkan pseudo-depth untuk 3.992 gambar | entri 175/198 |
| **I-4** | YOLO 4-kanal (early fusion) vs baseline RGB | Expandable YOLO, §174 |
| **I-5** | Fusi middle/late dua cabang | Ophoff dkk., §174 |
| **I-6** | Penautan bunch lintas-sisi secara geometris (ganti k/SVR) | §208 |
| **I-7** | **Asosiasi sadar-pose berjenjang** — tangga ablasi §208: hanya penampilan → depth tanpa pose → sadar-pose → bergerbang mutu. Melaporkan empat mode gagal counting secara terpisah: terlewat, tergabung, terpecah, terduplikasi. | §208 |
| **I-8** | **Gerbang mutu depth + fallback RGB** — pakai peta `conf` DA3 sebagai gerbang; bila depth buruk, jatuh ke RGB dan laporkan kondisi terdegradasi. Naskah menyatakan tegas: bila fallback RGB menyamai fusi saat depth buruk, itu **temuan deployment, bukan hasil negatif**. | §174, §265; SA-Gate 055, D3Net 037 |
| **I-9** | **Sampel depth terkendala instans** — ambil statistik kedalaman di dalam kotak tiap bunch (bukan seluruh citra) sebagai fitur geometris per-instans: ukuran relatif, pemisahan lapisan, jarak ke tetangga. Masuk ke penghitung menggantikan fitur 13-dimensi SVR. | F08; FocusDepth entri 202 |
| **I-10** | **Kaskade deteksi-lalu-proyeksi** — deteksi 2D dulu sebagai penyaring kasar, baru proyeksikan ke 3D pada himpunan titik yang sudah diperkecil. Alternatif terhadap fusi di input, dan lebih murah di perangkat lapangan. | FusionVision, YOLOv8-URE, §174 |
| **I-11** | **Analisis terstratifikasi ukuran/oklusi/iluminasi** — bukan sekadar AP tunggal, tetapi AP per strata, supaya terlihat **di mana** depth benar-benar membayar. Inilah yang memutuskan hipotesis (A) geometris vs (B) fotometrik. | Tabel hierarki metrik, §234–262 |

Ide berikut (I-12…I-24) lahir **dari hasil eksperimen di atas**, bukan dari
korpus — masing-masing menutup atau membuka arah menurut apa yang terukur. Ini
yang membedakannya dari daftar awal: bukan agenda pustaka, melainkan konsekuensi
data.

| Ide | Isi | Lahir dari | Status |
|---|---|---|---|
| **I-12** | Pelatihan berbasis ubin (tiling) resolusi tinggi | laporan | ekspektasi diturunkan (E-009); tak dijalankan tuntas |
| **I-13** | Loss berimbang kelas / focal | laporan | belum |
| **I-14** | Detektor NMS-free (RT-DETR) | laporan (prioritas 1) | **BERJALAN** (E-020, [SR-013](SR/SR-013-rtdetr-nms-free.md)) |
| **I-15** | Neck multiskala lebih kuat (BiFPN) | laporan | belum |
| **I-16** | Copy-paste / augmentasi sintetis | laporan | prioritas turun untuk B4 (SR-007) |
| **I-17** | Kalibrasi ambang per strata | laporan | belum |
| **I-18** | Kepala multi-tugas (deteksi + kematangan) | laporan | → menjelma I-22 |
| **I-19** | Kalibrasi depth metrik (Metric3D/ZoeDepth) | laporan | belum (perlu bila klaim jarak) |
| **I-20** | Praproses penajam kontras untuk B4 | E-010/SR-007 | **DIPALSUKAN** (E-011) |
| **I-21** | Kanal keempat berisi tekstur, bukan depth | E-011/SR-008 | dijalankan lalu dihentikan (E-014) |
| **I-22** | Loss ordinal / kepala regresi kematangan | E-012/SR-009 | belum (probe dihentikan di E-014) |
| **I-23** | Detektor dua tahap (deteksi agnostik + kepala kematangan) | E-014/SR-010 | **DIPALSUKAN** (E-017, [SR-012](SR/SR-012-dua-tahap.md)) |
| **I-24** | Detektor 4-kelas resolusi tinggi + augmentasi aman-warna | E-014/E-016 | diuji (E-019); menempel baseline |

---

## Baseline acuan (bukan eksperimen)

Angka publikasi dari Data in Brief 67 (2026) 112990, diverifikasi langsung dari
PDF di `docs/`. Semua eksperimen di bawah dibandingkan terhadap ini.

- Deteksi YOLO26m (test): AP50 overall **0,531** — B1 0,739 / B2 0,433 /
  B3 0,599 / **B4 0,354**
- Counting (test, 141 pohon), Class ±1 Acc: GT+SVR **96,81%** vs
  YOLO26m+SVR **75,35%**
- Baseline ini **sengaja tidak di-tuning** oleh penulis (`imgsz=640`, SVR default).
  Plafon hasil tuning tim adalah angka terpisah — jangan dicampur.

---

## E-001 — `class_mismatch` sebagai ukuran ambiguitas kematangan (2026-07-21)

**Hipotesis** — Flag `class_mismatch` pada JSON per-pohon menyala saat anotator
memberi kelas berbeda pada bunch fisik yang sama dilihat dari sisi berbeda.
Karena bunch yang sama pasti punya kematangan yang sama, tingkat ketidaksepakatan
itu adalah **batas atas empiris** akurasi klasifikasi per-sisi, dan diperkirakan
menumpuk di B2↔B3 sehingga mendukung klaim "ambiguitas B2/B3 sulit direduksi".
Dipalsukan bila tingkat ketidaksepakatan mendekati nol atau tidak terkonsentrasi
di B2/B3.

**Cara** — `experiments/class_mismatch_stats.py` atas seluruh 953 JSON di
`SawitMVC/data/json/`. Menghitung flag, ketidaksepakatan label per-sisi terhadap
kelas konsensus bunch, matriks kebingungan, dan pecahan per split/varietas/jumlah
sisi/kelas.

**Hasil** —

| Besaran | Nilai |
|---|---|
| Bunch unik | 9.823 |
| Bunch tampak dari ≥2 sisi | 7.328 (74,6%) |
| Label antar-sisi berbeda | **0 (0,00%)** |
| Flag `class_mismatch` menyala | **0** |
| Konsistensi label sisi vs konsensus | 18.540 / 18.540 = 100,00% |

Verifikasi silang parser terhadap angka publikasi — cocok persis: 9.823 bunch,
18.540 kemunculan, sebaran kemunculan 6.264 / 834 / 147 / 71 / 12 untuk 2–6 sisi.
Jadi angka nol bukan bug parser.

**Putusan** — **DIPALSUKAN.** Flag ini bukan pengukur ambiguitas kematangan,
melainkan pemeriksa integritas data yang hasilnya bersih. Ketidaksepakatan sudah
diselesaikan sebelum rilis; DiB §4.3: *"Completed annotations were reviewed in
full by a single reviewer, who applied corrections before export."*

**Penting untuk tidak salah kutip:** angka nol ini **tidak** mendukung maupun
membantah klaim ambiguitas B2/B3 — besaran itu tidak lagi teramati pada rilis
ini. Jangan menyajikannya sebagai "konsistensi anotator 100%" seolah bukti mutu
anotasi terhadap ambiguitas.

**Dampak** — Jalan ini ditutup. Pengganti: pakai graf `_confirmedLinks` sebagai
*oracle identitas*, lalu ukur **inkonsistensi prediksi detektor** pada bunch
fisik yang sama antar-sisi. Itu mengukur ambiguitas tanpa bergantung label
manusia, dan ukuran yang sama dapat menguji apakah depth menstabilkannya.
Butuh detektor terlatih → dijalankan bersama eksperimen utama.

---

## E-002 — Inventarisasi master mentah `Sawit` (2026-07-21)

**Hipotesis** — Master mentah 3024×4032 dapat langsung dipakai untuk eksperimen
resolusi penuh memakai anotasi SawitMVC yang sudah ada, karena keduanya dataset
yang sama.

**Cara** — Pemeriksaan langsung `/workspace/Sawit/data`: hitung berkas, resolusi,
rasio aspek, tabrakan nama, properti video.

**Hasil** —

- Raw: 3.992 JPG **3024×4032** (16 GB) + **45 MP4** 1920×1080, ~21 dtk
  (~618 frame), semuanya dari `Video/Kelompok 6`.
- Rasio aspek raw dan MVC **identik (0,75)** → koordinat YOLO ternormalisasi
  berlaku persis di kedua resolusi, tanpa anotasi ulang. Luas piksel 9,9×.
- **Penghalang:** nama berkas raw tidak unik secara global — 3.992 berkas hanya
  1.352 nama unik, **936 nama kembar** antar folder `Kelompok N`
  (mis. `LONSUM_A21A_044_3.jpg` di Kelompok 2 *dan* 5 = dua pohon berbeda).
  Penomoran raw 3 digit vs MVC 4 digit. Video hanya bernama cap waktu, tanpa
  ID pohon.

**Putusan** — **TIDAK KONKLUSIF.** Premisnya benar (aspek identik, label
transferable), tetapi pemetaan raw ↔ anotasi tidak dapat dilakukan dari nama
berkas. Perlu pencocokan berbasis isi (perceptual hash / *downscale-and-compare*)
yang hasilnya wajib diverifikasi, atau tabel pemetaan dari tim pengumpul data.

**Dampak** — Eksperimen resolusi penuh diblokir sampai pemetaan tersedia.
Sebaliknya, **video menjadi aset tak terduga**: risiko terbesar rencana DA3
multi-view adalah baseline ~90° antar sisi; ratusan frame mengelilingi satu pohon
memberi baseline kecil, kondisi ideal untuk geometri multi-view. Urutan uji
diubah — DA3 pada video lebih dulu.

---

## E-003 — DA3 multi-view pada video orbit pohon (2026-07-21)

**Hipotesis** — Depth Anything 3 (entri 198) dapat merekonstruksi geometri pohon
yang konsisten dari video orbit, sehingga kedalaman antar-pandangan dapat
diandalkan untuk memisahkan bunch bertumpuk dan, lebih jauh, untuk menautkan
bunch lintas-sisi secara geometris alih-alih statistik (k ≈ 1,89 / SVR).
Dipalsukan bila rekonstruksi gagal konvergen, pose kamera tidak membentuk orbit
yang masuk akal, atau peta kedalaman kanopi tidak memisahkan lapisan.

**Cara** — `experiments/da3_video_test.py`, checkpoint `depth-anything/da3-large`,
`process_res=504`, GPU L4. Video `VID_20260205_090556.mp4` (1280×720, 1.315
frame, 43,6 dtk) dari `Sawit/data/Video/Kelompok 6`. Frame diambil berjarak sama,
dua kerapatan: 16 dan 48 frame. Diagnosa: (b) PCA pusat kamera → kecocokan
lingkaran pada bidang orbit; (c) rentang dinamis kedalaman + inspeksi visual
pratinjau RGB|depth|conf.

**Hasil** —

Kecepatan: 16 frame dalam **2,2 dtk** (0,14 dtk/frame). Keluaran `Prediction`
memuat `depth` (N,H,W), `conf` per piksel, `extrinsics` (N,3,4), `intrinsics`.
`is_metric` kosong → kedalaman **relatif**, bukan metrik.

(b) Pose kamera, 48 frame:

| Besaran | Nilai |
|---|---|
| Cakupan sudut | 319,7° |
| Residual lingkaran (rata-rata / maks) | 8,2% / 28,0% dari radius |
| Simpangan dari bidang (RMS) | 9,1% |
| Rasio kerataan S3/S1 | 0,111 |

Deret langkah sudut menunjukkan pola yang tegas: **indeks 0–30 halus dan searah**
(−2° s.d. −16° per frame), lalu **indeks 31–47 kacau** (−77°, +54°, −44°, +89°,
−76°). Pola batas yang sama muncul pada sampling 16 frame (halus f00–f12, kacau
f13–f15). Perpindahan pusat kamera di bagian kacau mencapai ~96% radius orbit
per langkah, padahal frame-nya tampak serupa.

(c) Kedalaman: rentang dinamis (p99−p1)/p50 = **1,97**; secara visual pelepah
terpisah satu per satu dari latar, dan **tandan buah terlihat** (gugusan B1
merah pada frame 8) dengan kanopi terpisah dari langit/tanah. Peta `conf`
tinggi tepat pada pohon dan rendah pada langit — sinyal gating mutu yang
diminta SA-Gate (055) / D3Net (037) tersedia langsung dari model.

**Putusan** — **DIKONFIRMASI SEBAGIAN.** Rekonstruksi berjalan, cepat, dan pada
~2/3 pertama video menghasilkan orbit mulus searah dengan kedalaman berlapis
yang jelas. Tetapi keandalan pose **tidak seragam sepanjang video**: sepertiga
akhir gagal.

Dua sub-hipotesis atas penyebab kegagalan ekor ini diuji dan **keduanya
dipalsukan**: (i) "operator berhenti/melayang sehingga baseline kecil" — salah,
perpindahan di ekor justru 2,2× lebih besar dari badan orbit; (ii) "baseline
antar-frame terlalu lebar akibat sampling jarang" — salah, merapatkan 16→48
frame tidak menggeser batas kegagalan. Kegagalan terlokalisasi pada **isi video
di sepertiga akhir**, dan penyebabnya belum diketahui.

**Dampak** — Jalur depth berbasis geometri layak diteruskan, tetapi **wajib
disertai penyaring keandalan pose**, bukan diasumsikan berlaku untuk seluruh
masukan. Langkah lanjutan: (1) cari penyebab kegagalan sepertiga akhir dengan
memeriksa isi frame di sana; (2) uji pada beberapa video lain — n=1 tidak cukup
untuk generalisasi; (3) uji pada kasus 4-sisi yang sebenarnya, karena
keberhasilan pada video **belum** membuktikan apa pun untuk baseline ~90°.

**Catatan keterbatasan yang harus dibawa ke entri berikutnya:**

- **n = 1 video.** Belum ada bukti generalisasi.
- Frame diekstrak `cv2` yang **mengabaikan metadata rotasi**, sehingga masukan
  miring 90°. DA3 tetap bekerja, tetapi ini variabel tak terkontrol yang harus
  diperbaiki sebelum angka apa pun dikutip.
- "Kedalaman berlapis" masih kualitatif plus proksi rentang dinamis; **belum
  terhubung ke metrik deteksi apa pun**. Belum ada klaim bahwa ini menaikkan
  AP50 B4.
- Video ini rekaman jarak dekat ke mahkota; foto dataset diambil 2–3 m dari
  batang. Transfer antar-geometri **belum diuji**.

---

## E-004 — DA3 pada banyak video, rotasi diperbaiki (2026-07-21) · Ide I-1

**Hipotesis** — Kegagalan sepertiga akhir pada E-003 bukan batas DA3, melainkan
akibat (i) masukan miring 90° karena `cv2` mengabaikan metadata rotasi, dan/atau
(ii) sifat khas video tunggal itu. Bila benar, memperbaiki rotasi dan menguji
banyak video akan menghasilkan orbit mulus pada mayoritas video. Dipalsukan bila
sebagian besar video tetap gagal, atau kegagalan tersebar merata.

**Cara** — `experiments/da3_video_multi.py`, `depth-anything/da3-large`,
`process_res=504`, 6 video pertama `Kelompok 6`, 32 frame per video. Ekstraksi
frame lewat **ffmpeg** (menerapkan display matrix; terkonfirmasi video memuat
`displaymatrix: rotation of -90.00 degrees`) menggantikan `cv2`. Metrik utama
`smooth_frac` = pecahan frame di dalam sapuan orbit searah terpanjang (langkah
searah, besar ≤40°).

**Hasil** —

| Video | smooth_frac | Sapuan mulus | Residual lingkaran | Kerataan |
|---|---|---|---|---|
| 090556 | 41% | 149° | 2,4% | 0,098 |
| 091514 | **100%** | 331° | 3,6% | 0,020 |
| 092017 | 97% | 335° | 3,3% | 0,049 |
| 092548 | **100%** | 362° | 4,1% | 0,041 |
| 093119 | **100%** | 379° | 5,7% | 0,025 |
| 094046 | **100%** | 385° | 7,0% | 0,034 |

Ringkasan: `smooth_frac` rata-rata **90%**, median **100%**; **5 dari 6** video
mencapai sapuan ≥270°. Residual lingkaran 2,4–7,0% dari radius, rasio kerataan
0,020–0,098 — pusat kamera benar-benar terletak pada satu bidang melingkar.
Rentang dinamis kedalaman 2,70–3,63.

Uji sebab pada frame di luar segmen mulus: **ketajaman justru lebih tinggi**
(7.725 vs 6.526; rasio 0,84), kecerahan hampir sama (rasio 1,05), gerak hampir
sama (rasio 0,94). Jadi blur, pencahayaan, dan gerak **bukan** penyebabnya.

**Putusan** — **DIKONFIRMASI.** DA3 merekonstruksi orbit pohon sawit secara andal
pada 5 dari 6 video, dengan sapuan mendekati lingkaran penuh dan geometri yang
konsisten. E-003 mengukur satu video yang kebetulan bermasalah, dan `n=1` memang
tidak layak digeneralisasi — koreksi ini persis alasan keterbatasan itu dicatat.

Sebab kegagalan video 090556 **masih belum diketahui**; tiga kandidat (baseline
kecil, sampling jarang, blur/pencahayaan/gerak) sudah dipalsukan. Jangan
mengarang penjelasan untuk sisa 1 video ini.

**Dampak** — Ide I-1 selesai dan positif. Pose kamera dan kedalaman relatif dari
DA3 cukup andal untuk dijadikan fondasi I-6 (penautan geometris) dan I-7
(asosiasi sadar-pose). Tetapi keandalannya **tidak universal** (1 dari 6 gagal),
sehingga gerbang mutu I-8 bukan hiasan melainkan syarat.

**Reproduksi** — `python da3_video_multi.py --videos 6 --frames 32`
(pembanding tanpa koreksi rotasi: tambahkan `--no-rotate`).

---

## E-005 — DA3 pada 4 dan 8 sisi foto asli (2026-07-21) · Ide I-2

**Hipotesis** — Keberhasilan DA3 pada video (E-004) belum membuktikan apa pun
untuk foto dataset: 4 posisi berjarak ~90° adalah *baseline* lebar dengan
tumpang tindih rendah pada objek yang menutupi dirinya sendiri. Diuji apakah DA3
tetap merekonstruksi geometri yang benar. Dipalsukan bila susunan pusat kamera
tidak lebih baik daripada tebakan acak, atau urutan sisi salah.

Geometri sebenarnya diketahui (operator memutari pohon pada 4 atau 8 posisi),
sehingga tersedia kebenaran acuan objektif: langkah sudut antar-sisi berurutan
seharusnya 90° (4 sisi) atau 45° (8 sisi).

**Cara** — `experiments/da3_sides_test.py`, `depth-anything/da3-large`,
`process_res=504`. 20 pohon 4-sisi dan 30 pohon 8-sisi, dipilih acak `seed=42`
dari 908 dan 45 pohon yang tersedia. Metrik: RMSE simpangan langkah sudut
terhadap nilai harapan, residual kecocokan lingkaran, rasio kerataan PCA, dan
kebenaran urutan melingkar. Pembanding: 2.000 simulasi sudut acak seragam.

**Hasil** —

| | 4 sisi (20 pohon) | 8 sisi (30 pohon) |
|---|---|---|
| Langkah sudut diharapkan | 90° | 45° |
| **RMSE sudut** (rata2 / median) | **17,3° / 12,6°** | **8,5° / 7,4°** |
| RMSE pembanding acak | 57,5° | 34,4° |
| **Urutan sisi benar** | **20/20 (100%)** | **30/30 (100%)** |
| Residual lingkaran | 4% | 5% |
| Rasio kerataan | 0,014 | 0,026 |
| Rentang dinamis kedalaman | 3,74 | 4,95 |
| Lebih baik dari acak | 100% | 100% |

Galat relatif keduanya konsisten: 17,3/90 = 19% dan 8,5/45 = 19%.

**Putusan** — **DIKONFIRMASI.** Risiko *wide baseline* yang dikhawatirkan tidak
terwujud. DA3 memulihkan susunan melingkar keempat/kedelapan sisi dengan urutan
benar pada **seluruh 50 pohon**, jauh di atas pembanding acak, dengan pusat
kamera yang hampir sebidang (kerataan 0,014–0,026).

**Peringatan dari inspeksi visual — jangan diabaikan:** pada pratinjau
(`results/e005/preview_*.jpg`), kedalaman memisahkan **pelepah** dari latar
dengan sangat bersih, tetapi di area mahkota tempat tandan berada peta tampak
**halus dan menyatu dengan batang**. Jadi geometri tingkat-pohon terbukti,
sementara pemisahan tingkat-tandan **belum terbukti** — padahal justru itu yang
menentukan B4. Angka RMSE sudut di atas **tidak boleh** dikutip seolah menjawab
pertanyaan tandan.

**Dampak** — Ide I-2 selesai dan positif pada tingkat pohon. Fondasi untuk I-6
dan I-7 tersedia. Namun sebelum melatih apa pun, pertanyaan tandan harus diuji
kuantitatif (→ E-006, ide I-9): apakah kedalaman di dalam kotak tandan berbeda
dari sekitarnya? Kalau tidak, fusi depth tidak akan menolong B4 berapa pun
arsitekturnya, dan itu harus diketahui sebelum jam GPU dibakar.

**Reproduksi** — `python da3_sides_test.py --trees 20 --sides 4` dan
`python da3_sides_test.py --trees 30 --sides 8 --preview 1`.

---

## E-006 — Sinyal kedalaman di tingkat tandan (2026-07-21) · Ide I-9 · [SR-005](SR/SR-005-sinyal-depth-tandan.md)

**Hipotesis** — Tandan yang tertanam/bertumpuk berada pada lapisan kedalaman
berbeda dari sekitarnya, sehingga kedalaman dapat memisahkan apa yang warna
tidak bisa (naskah §14). Dipalsukan bila kotak tandan tidak menunjukkan kontras
kedalaman lebih besar daripada kotak acak berukuran sama.

**Cara** — `experiments/depth_bunch_signal.py`, 40 pohon (780 kotak
kebenaran-dasar), kedalaman DA3 multi-view per pohon. Untuk tiap kotak:
bandingkan kedalaman di dalam kotak vs cincin sekelilingnya. **Kendali: 2 kotak
acak berukuran sama per kotak asli** (1.560 kendali) — perlu karena peta
kedalaman apa pun punya struktur, sehingga kotak apa pun menunjukkan kontras
tertentu. AUC lewat statistik-U Mann–Whitney; signifikansi lewat 2.000
permutasi. Dijalankan pada `process_res` 504 dan 1008.

**Hasil** —

| | kontras (504) | AUC (504) | kontras (1008) | AUC (1008) |
|---|---|---|---|---|
| Kotak tandan asli | 0,0089 | 0,6078 | 0,0096 | 0,6079 |
| Kotak acak kendali | 0,0341 | 0,5998 | 0,0364 | 0,5991 |
| **Selisih** | **−0,0252 (0,26×)** | +0,0080 | **−0,0268 (0,26×)** | +0,0088 |

p permutasi: 0,0245 (504), 0,0110 (1008). Per kelas pada 1008, **B4 justru
ber-AUC terendah: 0,6022**.

**Putusan** — **DIPALSUKAN.** Tandan tidak menonjol dalam kedalaman; kontrasnya
0,26× kotak acak, dan rasio itu **identik** pada dua resolusi sehingga bukan
artefak resolusi. Tandan tumbuh tertanam di ketiak pelepah, pada jarak praktis
sama dengan mahkota sekitarnya. Selisih AUC +0,009 signifikan secara statistik
(n besar) tetapi **ukuran efeknya dapat diabaikan** — jangan disajikan sebagai
"depth membawa sinyal".

**Dampak** — Versi "kedalaman sebagai pemisah tandan tingkat piksel" gugur, dan
**I-4 (4-kanal early fusion) diprediksi gagal** — prediksi ini dicatat *sebelum*
dijalankan agar tidak bisa dirasionalisasi belakangan. Yang **tidak** gugur:
geometri tingkat-pohon (E-004, E-005) tetap kokoh, sehingga I-6/I-7 justru
menjadi jalur paling menjanjikan karena memakai pose lintas-pandangan yang
terbukti, bukan kontras lokal yang baru dipalsukan.

**Reproduksi** — `python depth_bunch_signal.py --trees 40 [--process-res 1008]`

---

## E-007 — Penautan lintas-sisi geometris (2026-07-21) · Ide I-6/I-7 · [SR-006](SR/SR-006-penautan-geometris.md)

**Hipotesis** — Pose kamera DA3 memungkinkan penautan tandan lintas-sisi secara
geometris (tandan sama = titik 3D sama), mengalahkan koreksi statistik k=1,8905.
Dipalsukan bila mode sadar-pose tidak lebih baik daripada penampilan/depth/k.

**Cara** — `experiments/geometric_linking.py`, 141 pohon split uji. Tangga
ablasi §208: (A) hanya penampilan, (B) depth tanpa pose, (C) sadar-pose 3D,
(D) koreksi global k. Identitas = komponen terhubung union-find. Ambang disapu
(9 nilai untuk pose, 7 untuk lainnya).

**Hasil** — Validasi perangkat: jumlah mentah dan koreksi k direproduksi
**persis** dari DiB Tabel 4 (50,00/6,38/2,142/+2,142 dan 95,57/86,52/0,356/+0,009).

| Mode | Ambang terbaik | Class±1 | Tree±1 | MAE |
|---|---|---|---|---|
| A. penampilan | 0,1 | 77,13% | 32,62% | 0,876 |
| B. depth tanpa pose | 0,01 | 75,00% | 29,08% | 0,966 |
| C. sadar-pose (3D) | 1,0 | **69,50%** | 22,70% | 1,367 |
| D. koreksi global k | — | **95,57%** | 86,52% | 0,356 |

**Putusan** — **DIPALSUKAN.** Ketiganya kalah telak dari koreksi k, dan yang
geometris justru paling buruk. Sapuan ambang menutup kemungkinan salah setelan.
Batas klaim: kedalaman DA3 **relatif** bukan metrik, sehingga proyeksi balik
terdistorsi — eksperimen ini memalsukan **implementasi**, dan hanya melemahkan
idenya. Uji adil menuntut kedalaman metrik terkalibrasi (I-19).

**Dampak** — Koreksi k sangat kuat (95,57%) karena tandan per pohon sedikit
(median 10) dan duplikasi teratur (1,887). Ruang perbaikan di tahap counting
tipis. Bersama E-006, arah dipersempit tegas: sisa perbaikan harus dari
**detektor**. Prioritas berikutnya I-12 (ubin), I-13 (loss berimbang), I-15.

**Reproduksi** — `python geometric_linking.py --split test [--sweep]`

---

## E-009 — Ukuran kotak pada resolusi latih (2026-07-21) · Ide I-11/I-12

**Hipotesis** — B4 gagal (AP50 0,354) sebagian karena resolusi: pada
`imgsz=640`, citra 960×1280 diperkecil 2×, sehingga tandan kecil kehilangan
piksel sebelum masuk jaringan. Kalau benar, B4 akan jauh lebih kecil daripada
kelas lain dan banyak yang jatuh di bawah ambang "kecil" COCO.

**Cara** — `experiments/box_size_analysis.py`. Tanpa model sama sekali; hanya
mengukur geometri kotak kebenaran-dasar (train+test) setelah diskalakan ke
`imgsz=640`. Dijalankan **sebelum** hasil pelatihan ubin keluar, supaya
ekspektasinya tercatat lebih dulu.

**Hasil** —

| Kelas | n | Lebar×tinggi median (px) | Luas median | % kecil | % sedang | % besar |
|---|---|---|---|---|---|---|
| B1 | 1.831 | 63 × 69 | 4.361 | 2,6% | 82,6% | 14,8% |
| B2 | 3.112 | 57 × 64 | 3.626 | 4,4% | 86,0% | 9,6% |
| B3 | 8.742 | 52 × 56 | 2.886 | 8,8% | 85,1% | 6,1% |
| **B4** | 2.968 | **46 × 46** | **2.147** | **16,4%** | 81,2% | 2,5% |

**Putusan** — **SEBAGIAN MENDUKUNG, TETAPI MELEMAHKAN I-12.** Benar bahwa B4
paling kecil: luasnya ~separuh B1 dan 6× lebih sering masuk kategori "kecil"
COCO. Tetapi **81,2% kotak B4 masih tergolong sedang**, dengan median 46×46 px
— ukuran yang tidak problematis bagi detektor modern. Hanya 16,4% yang benar-
benar kecil.

**Dampak** — Ekspektasi terhadap I-12 (pelatihan berbasis ubin) **diturunkan
sebelum hasilnya keluar**. Ubin 2×2 akan memangkas proporsi "kecil" B4 dari
16,4% menjadi 0,2%, tetapi kalau resolusi bukan penyebab dominan, perbaikannya
akan tipis. Penyebab B4 yang lebih mungkin: **oklusi dan kontras rendah** —
tandan hitam tertanam di ketiak pelepah yang juga gelap. Itu mengarah ke ide
lain: augmentasi sadar-oklusi (I-16) dan analisis terstratifikasi oklusi (I-11),
bukan sekadar resolusi.

**Reproduksi** — `python box_size_analysis.py`

---

## E-010 — Diagnosis kegagalan B4 (2026-07-21) · Ide I-11 · [SR-007](SR/SR-007-diagnosis-b4.md)

**Hipotesis** — Kegagalan B4 (AP50 0,354) punya penyebab yang dapat diukur
langsung dari data, tanpa model. Tiga tersangka diuji berdampingan: kontras
fotometrik rendah, kepadatan/crowding, dan tumpang tindih antar-kotak.

**Cara** — `experiments/why_b4_fails.py` atas 400 citra uji. Kontras diukur di
ruang CIELAB antara isi kotak dan cincin sekelilingnya (ΔE, ΔLuminans, ΔWarna),
plus varians Laplacian sebagai ukuran tekstur. Kepadatan = jumlah kotak lain
yang pusatnya dalam 1,5× diagonal. **Kendali kotak acak** dipakai seperti E-006.

**Hasil** —

| Kelas | ΔE | ΔLuminans | Tekstur | Tetangga | IoU maks | %IoU>0,1 | AP50 DiB |
|---|---|---|---|---|---|---|---|
| B1 | **19,15** | 17,75 | 5.015 | 3,23 | 0,042 | 10,3% | 0,739 |
| B2 | 18,48 | 17,39 | 5.726 | 2,92 | 0,041 | 11,5% | 0,433 |
| B3 | 13,93 | 12,77 | 6.892 | 2,81 | 0,033 | 7,7% | 0,599 |
| **B4** | **11,55** | 9,93 | **7.780** | **2,58** | **0,029** | **6,4%** | **0,354** |
| *acak (kendali)* | *12,92* | *11,71* | *5.441* | — | — | — | — |

**Putusan** — **DIKONFIRMASI untuk kontras; kepadatan DIPALSUKAN.**

1. **B4 tersamar.** Kontrasnya (ΔE 11,55) **di bawah kotak acak** (12,92) —
   tandan B4 secara harfiah lebih sulit dibedakan dari latarnya daripada
   tambalan acak pada citra yang sama.
2. **Kepadatan bukan penyebab.** B4 justru punya tetangga paling sedikit (2,58)
   dan tumpang tindih paling rendah (IoU 0,029). Hipotesis "B4 gagal karena
   bertumpuk" dipalsukan.
3. **B2 gagal karena sebab berbeda.** Kontras latarnya tinggi (18,48) tetapi
   AP50 rendah — masalahnya bukan melihat tandan, melainkan membedakannya dari
   B3. Ini pemisahan (A) geometris vs (B) fotometrik yang dirumuskan di awal,
   kini **terukur**, bukan diasumsikan.

**Dampak** — Menyatukan tiga temuan menjadi satu gambaran yang koheren:
B4 **tidak** terpisah dalam kedalaman (E-006), **tidak** terpisah dalam warna
(E-010), dan **tidak** bertumpuk (E-010). Satu-satunya sinyal tersisa adalah
**tekstur**, dan justru di situ B4 tertinggi (7.780, tertinggi dari semua kelas).

Itu memberi dasar pemikiran **baru dan lebih kuat** untuk I-12: tekstur adalah
hal pertama yang hancur saat citra diperkecil 2×. Jadi ubin tetap layak diuji,
tetapi alasannya bukan "objeknya kecil" (E-009 melemahkan itu) melainkan
"petunjuk yang menentukan adalah frekuensi tinggi". Ekspektasi ini dicatat
**sebelum** hasil ubin keluar.

**Reproduksi** — `python why_b4_fails.py --images 400`

---

## E-011 — Praproses mana yang menaikkan keterpisahan B4? (2026-07-21) · Ide I-20 · [SR-008](SR/SR-008-kanal-tekstur.md)

**Hipotesis** — SR-007 menemukan B4 tersamar dalam warna tetapi bertekstur
tertinggi. Kalau begitu, praproses yang memperkuat kontras lokal atau tekstur
akan menaikkan keterpisahannya. Dipalsukan bila tidak ada praproses yang
menaikkan AUC B4 lebih dari 0,02 di atas acuan.

**Cara** — `experiments/contrast_boost_test.py`, 250 citra uji. Lima peta
skalar diuji (luminans asli, CLAHE, unsharp mask, besar gradien Sobel,
Laplacian). Metrik: AUC pemisahan piksel isi-kotak vs cincin, per kelas, dengan
**kendali kotak acak untuk tiap praproses**. Yang dinilai adalah selisih
terhadap kendali, bukan AUC mentah.

**Hasil** —

| Praproses | B1 | B2 | B3 | B4 | kendali | B4−kendali |
|---|---|---|---|---|---|---|
| asli (luminans) | 0,5897 | 0,6003 | 0,5753 | 0,5573 | 0,5659 | **−0,0086** |
| CLAHE | 0,5680 | 0,5833 | 0,5621 | 0,5534 | 0,5614 | −0,0080 |
| unsharp | 0,5696 | 0,5772 | 0,5582 | 0,5447 | 0,5513 | −0,0066 |
| gradien Sobel | 0,5682 | 0,5768 | 0,5909 | 0,6041 | 0,5674 | +0,0367 |
| **Laplacian** | 0,5673 | 0,5818 | 0,5970 | **0,6153** | 0,5695 | **+0,0458** |

Perbaikan Laplacian atas acuan: **+0,0544 AUC**.

**Putusan** — **DIKONFIRMASI untuk tekstur; DIPALSUKAN untuk penajam kontras.**
CLAHE dan unsharp — dugaan awal yang paling intuitif — justru sedikit
memperburuk. Yang berhasil adalah kanal **frekuensi tinggi murni**.

Yang paling menentukan: **urutan kelas berbalik**. Pada luminans asli B4 paling
tidak terpisah (0,5573, di bawah kendali); pada kanal Laplacian B4 menjadi
**kelas paling terpisah dari semuanya** (0,6153). B4 tak terlihat dalam
intensitas, tetapi terlihat dalam tekstur.

**Dampak** — Melahirkan **I-21: kanal keempat berisi tekstur, bukan kedalaman.**
Ini jauh lebih beralasan daripada RGB+D karena bersandar pada satu-satunya
sinyal yang terbukti membedakan B4 (E-006 memalsukan kedalaman, E-010
memalsukan warna dan kepadatan). Mesin 4-kanal dari I-4 dapat dipakai ulang
dengan menukar isi kanalnya.

**Reproduksi** — `python contrast_boost_test.py --images 250`

---

## E-012 — Plafon diskriminasi kematangan dari penampilan (2026-07-21) · Ide I-18 · [SR-009](SR/SR-009-ordinalitas-kelas.md)

**Hipotesis** — SR-001 gagal mengukur ambiguitas B2/B3 lewat `class_mismatch`.
SR-007 menunjukkan B2 punya kontras latar tinggi tetapi AP50 rendah, artinya
masalahnya membedakan kelas, bukan melihat tandan. Diuji langsung: dapatkah
kematangan dibedakan dari penampilan potongan kebenaran-dasar saja?

**Cara** — `experiments/class_separability.py`. Potongan diambil dari kotak
kebenaran-dasar sehingga **tahap deteksi dihilangkan sepenuhnya**. Fitur
sederhana dan dapat ditafsirkan (statistik LAB/HSV, varians Laplacian, besar
gradien, histogram hue = 37 dimensi). RandomForest 400 pohon, seimbang kelas,
6.000 potongan latih (1.500/kelas), 1.377 potongan uji.

**Hasil** —

Akurasi keseluruhan **52,87%** (tebak acak 25%).

| Sebenarnya | B1 | B2 | B3 | B4 | Recall |
|---|---|---|---|---|---|
| B1 | **177** | 44 | 15 | 16 | 70,2% |
| B2 | 64 | **159** | 106 | 46 | 42,4% |
| B3 | 7 | 90 | **156** | 122 | 41,6% |
| B4 | 8 | 43 | 88 | **236** | 62,9% |

Kebingungan pasangan terbesar: B3→B4 32,5%, B2→B3 28,3%, B3→B2 24,0%,
B4→B3 23,5%. Sebaliknya B3→B1 hanya **7 dari 375**.

**Putusan** — **DIKONFIRMASI: kebingungannya ORDINAL.** Kesalahan hampir
seluruhnya terjadi antar kelas bersebelahan pada rantai B1→B2→B3→B4, dan
nyaris tidak pernah melompat. Ini tanda khas satu **variabel kontinu**
(tingkat kematangan) yang dipotong menjadi empat kotak; batas kelasnya adalah
garis buatan pada rangkaian yang mulus.

**Batas klaim — penting.** Angka 52,87% diperoleh dari fitur buatan tangan yang
sengaja sederhana. Ini **batas BAWAH** keterpisahan, bukan plafon sebenarnya —
CNN hampir pasti lebih baik. Yang transferable dari eksperimen ini adalah
**struktur kebingungannya**, bukan angka absolutnya. Jangan mengutip 52,87%
sebagai "plafon akurasi kematangan".

**Dampak** — Melahirkan **I-22: loss ordinal / kepala regresi kematangan**,
yang menghukum kesalahan ke kelas tetangga lebih ringan daripada kesalahan
melompat. Menarik: metrik counting DiB (`Class ±1 Acc`) **sudah** mengakui
sifat ordinal ini, tetapi pelatihan detektornya memakai klasifikasi kategoris
biasa yang memperlakukan B2→B3 sama buruknya dengan B1→B4. Ada ketidakcocokan
antara objektif pelatihan dan metrik evaluasi — persis "mismatch objective-ke-
deployment" yang disebut `deep-research-report.md`.

**Reproduksi** — `python class_separability.py --per-class 1500`

---

## E-013 — Pipeline produksi 4-kanal untuk sensor depth (2026-07-21) · `pipeline/`

**Konteks** — Arah baru dari pengguna: kamera lapangan berikutnya adalah
Orbbec Gemini (depth sensor sungguhan, bukan pseudo-depth). Dibutuhkan
pipeline matang: latih 4-kanal → bobot → inferensi lapangan yang menerima
RGB saja ATAU RGB+depth, tanpa mengubah aplikasi yang sudah ada.

**Hipotesis (rekayasa, falsifiable)** — Satu bobot bisa melayani dua mode uji
bila dilatih dengan *modality dropout* (kanal depth diganti nol dengan peluang
p saat latih; nol = "tidak ada data" di seluruh pipeline).

**Cara** — Kode di `pipeline/` (repo ini): `fourch.py` (kontrak pengodean
depth metrik inverse 0,3–8 m; patch pemuat; inflasi conv pertama; kelas
`Sawit4CH`), `prepare_depth.py`, `train_4ch.py`, `infer_4ch.py`. Uji asap CPU:
16 citra, 1 epoch, yolo26n — memverifikasi jalur kode, bukan kualitas model.

**Hasil** —
1. Latih→bobot→inferensi dua mode jalan ujung-ke-ujung. Bobot RGBD epoch-11
   (pelatihan GPU yang sedang berjalan) menghasilkan deteksi nyata lewat
   `Sawit4CH` pada kedua mode.
2. **Temuan yang bisa menggigit siapa pun yang memakai callback ultralytics:**
   `on_pretrain_routine_end` menyala SETELAH `ModelEMA(self.model)` disalin
   (`trainer.py` baris 383 vs 394), dan `best.pt` menyimpan EMA — jadi
   modifikasi bobot lewat callback itu **tidak masuk ke bobot tersimpan**
   kecuali `trainer.ema.ema` ikut ditambal. Diverifikasi: setelah menambal
   keduanya, norma kanal depth di `best.pt` = 0,0 persis dan bobot RGB = persis
   pratlatih (urutan BGR).
3. Urutan kanal konsisten: pembalikan BGR→RGB ultralytics hanya berlaku untuk
   3 kanal (`predictor.py:167`, `augment.py:2395`) — model 4-kanal melihat
   `[B,G,R,D]` di jalur latih maupun prediksi.

**Catatan penting** — `train_fusion.py` (I-4, sedang berjalan di GPU) TIDAK
memakai inflasi ini — conv pertamanya mulai acak. Bila RGBD/RGBT layak diulang,
ulangi lewat `pipeline/train_4ch.py` agar mulai dari bobot pratlatih penuh.

**Reproduksi** — lihat `pipeline/README.md`; uji asap: dataset mini 16 citra +
`train_4ch.py --epochs 1 --imgsz 320 --device cpu`.

---

## E-014 — Deteksi atau klasifikasi? (2026-07-21) · Ide I-23 · [SR-010](SR/SR-010-hambatan-klasifikasi.md)

**Konteks** — Sembilan ide diuji, mAP tidak bergerak. Pengguna melaporkan
berbulan-bulan mencoba teknik dari pustaka (termasuk SAHI) tanpa hasil. Sebelum
menjadwalkan ide ke-sepuluh, satu asumsi yang tidak pernah diperiksa harus
diperiksa: benarkah yang kurang itu kemampuan **menemukan** tandan?

**Hipotesis** — mAP menggabungkan dua kemampuan berbeda. Bila mAP kelas-agnostik
jauh di atas mAP 4-kelas pada bobot yang sama, maka kerugian ada di klasifikasi
kematangan, dan seluruh antrean ide berbasis deteksi salah alamat.

**Cara** — `diag_bottleneck.py`: bobot identik (`rgb_e60_i640_s42/best.pt`),
val identik (404 citra), hanya bendera `single_cls` yang berbeda.

**Hasil** —

| Evaluasi | mAP50 | mAP50-95 | P | R |
|---|---|---|---|---|
| 4 kelas | 0,5218 | 0,2407 | 0,5307 | 0,5484 |
| Kelas-agnostik | **0,7191** | **0,3197** | 0,6950 | 0,6365 |

AP50 per kelas: B1 0,7354 · B2 0,4076 · B3 0,5561 · B4 0,3881.

**Putusan — DIKONFIRMASI.** 38% mAP50 yang mungkin diraih hilang di klasifikasi.
Efektivitas klasifikasi terukur 0,5218/0,7191 = **72,6%**. mAP50-95 agnostik
0,3197 sudah melewati sasaran 0,30.

**Dampak** — Antrean lama (ubin I-12, RGBT I-21, ordinal I-22, RGBD I-4)
dihentikan; I-4 berhenti di epoch 25/60 dengan mAP50 terbaik 0,5135 vs baseline
0,5214 — kurva datar, tanpa sinyal. Seluruh GPU dialihkan ke **I-23: detektor
dua tahap** (deteksi agnostik resolusi 960 + pengklasifikasi kematangan pada
potongan resolusi asli). Melahirkan pula **I-24**: augmentasi baseline memakai
`hsv_s=0.7` — mengacak saturasi ±70% pada tugas yang buktinya adalah warna.

**Reproduksi** — `python diag_bottleneck.py`

---

## E-015 — Master mentah 3024×4032 terbuka (2026-07-21) · Ide I-2/I-23 · [SR-002](SR/SR-002-resolusi-master-mentah.md)

**Konteks** — SR-002 berstatus TIDAK KONKLUSIF (terblokir) sejak awal: nama
berkas master mentah tidak unik secara global (3.992 berkas, hanya 1.352 nama
unik, 936 nama kembar antar folder `Kelompok N`), sehingga pemetaan raw ↔
anotasi tidak bisa dilakukan lewat nama. E-014 membuat blokade ini mendadak
mahal: kalau hambatan mAP ada di penilaian kematangan, dan kematangan dinilai
dari permukaan buah, maka resolusi permukaan buah adalah sumber daya yang
paling langsung relevan — dan ia terkunci.

**Hipotesis** — Kedua tingkat adalah citra yang sama pada skala berbeda, jadi
pencocokan berbasis ISI menyelesaikan pemetaan tanpa tabel dari tim.

**Cara** — `match_raw.py`: tiap citra diperkecil lewat penskalaan DCT JPEG
(`IMREAD_REDUCED_*_8`), disamakan orientasinya ke potret, diringkas jadi vektor
abu-abu 32×40 yang dinormalkan (rerata 0, norma 1). Kecocokan = hasil kali titik
tertinggi, diverifikasi tiga lapis: skor > 0,90, jarak ke peringkat kedua
> 0,02, dan pemetaan dipaksa satu-ke-satu.

**Hasil** —

| Besaran | Nilai |
|---|---|
| Citra MVC | 3.992 |
| Citra master mentah | 3.992 |
| **Cocok** | **3.992 (100%)** |
| Ditolak karena skor lemah | 0 |
| Ditolak karena ambigu | 0 |
| Skor kecocokan **terendah** | 0,9985 |
| Selisih median ke peringkat kedua | 0,353 |

Contoh: `DAMIMAS_A21B_0001_1.jpg` → `Damimas/Kelompok 1/DAMIMAS_A21B_001_1.jpg`
(perhatikan penomoran 4 digit vs 3 digit yang membuat pencocokan nama gagal).

**Putusan — SR-002 TIDAK LAGI TERBLOKIR.** Skor terendah 0,9985 dengan selisih
median 0,353 tidak menyisakan ruang keraguan: tidak ada satu pun pasangan yang
"nyaris cocok". Karena rasio aspek kedua tingkat identik (0,75), koordinat YOLO
ternormalisasi berlaku persis — **tidak perlu anotasi ulang**.

**Dampak** — Potongan tandan bisa diambil pada 3024×4032, tempat tandan
bermedian ~220–300 px, bukan ~70–95 px seperti di SawitMVC. Pada MVC, potongan
masukan 224 px sebenarnya hasil **pembesaran** — tidak ada detail baru, hanya
interpolasi. Di master, 224 px berisi detail permukaan buah yang sebenarnya.
Ini menjadi masukan tahap 2 dari I-23.

**Reproduksi** — `python match_raw.py` (CPU, beberapa menit) → `results/raw_map.json`

---

## E-016 — Plafon kematangan, diukur tiga kali (2026-07-21) · Ide I-23 · [SR-011](SR/SR-011-plafon-kematangan.md)

**Konteks** — SR-010 memberi sasaran tajam: klasifikasi kematangan harus ≈83%
supaya mAP50 mencapai 0,60. E-016 menguji apakah angka itu bisa dicapai.

**Cara** — Tiga jalur bebas pada tugas identik (diberi kotak, tebak kelas):
head YOLO (`head_vs_crop.py`), CNN ConvNeXt-Tiny pada potongan master
3024×4032 (`build_crops_raw.py` + `train_maturity.py`), dan voting antar-sisi
dengan penautan kebenaran dasar (`multiview_vote.py`).

**Hasil** —

| Jalur | Akurasi | ±1 |
|---|---|---|
| Head YOLO (n=1.518) | 0,6871 | **1,0000** |
| CNN potongan master, val | 0,6910 | 0,9947 |
| CNN potongan master, test | 0,6998 | 0,9946 |
| Voting multi-sisi (992 tandan) | 0,6855 | 0,9940 |

Voting menurut jumlah sisi: 1 sisi 0,6250 · 2 sisi 0,7095 · 3 sisi 0,6506 ·
4 sisi 0,7391.

Varian perumusan metrik pada prediksi baseline yang sama (COCO):

| Perumusan | mAP50 | mAP50-95 |
|---|---|---|
| 4 kelas | 0,5153 | 0,2384 |
| Kelas-agnostik | 0,7125 | 0,3178 |
| B2+B3 digabung | 0,5829 | 0,2669 |
| Toleransi ±1 (deteksi digandakan) | 0,3467 | 0,1653 |
| Toleransi ±1 (GT digandakan) | 0,5029 | 0,2235 |

**Putusan — DIKONFIRMASI, plafonnya nyata.** Resolusi 3× tidak menolong; 2–6
sudut pandang tidak menolong. Head YOLO meleset lebih dari satu tingkat pada
**nol** dari 1.518 deteksi. Voting multi-sisi gagal karena kesalahannya
**berkorelasi antar sisi** — ambiguitas melekat pada buahnya.

**Temuan sampingan yang penting** — **mAP tidak dapat mewakili toleransi
ordinal.** Kedua cara memaksakannya justru menurunkan angka: menggandakan
deteksi meledakkan positif palsu, menggandakan GT meledakkan yang harus
ditemukan. Metrik deployment DiB `Class ±1 Acc` adalah metrik **penghitungan**,
dan tidak punya padanan di ruang metrik deteksi. Pelaporan yang jujur karena
itu harus memisahkan dua angka: AP deteksi kelas-agnostik, dan akurasi
kematangan (dengan ±1) — persis dekomposisi SR-010.

**Reproduksi** — `head_vs_crop.py`, `multiview_vote.py`, `metric_variants.py`

---

## E-017 — Detektor dua tahap (2026-07-21) · Ide I-23 · [SR-012](SR/SR-012-dua-tahap.md)

**Konteks** — SR-010 memisahkan deteksi dari klasifikasi; SR-011 mengukur
plafon klasifikasi ~68%. I-23 menguji apakah memisahkan keduanya secara
arsitektural memberi mAP 4-kelas yang lebih baik daripada satu tahap.

**Cara** — Tahap 1: `train_agnostic.py`, yolo26m `single_cls=True`, imgsz 960,
diinisialisasi dari baseline RGB yang sudah konvergen. Tahap 2: ConvNeXt-Tiny
pada potongan master 3024×4032 (E-015). Skor gabungan = skor objek × peluang
kelas, tiap kotak menyumbang ke keempat kelas — cara skor detektor dua-tahap
klasik, bukan penyetelan angka. Evaluasi memakai pycocotools (bukan
implementasi sendiri); konsistensi evaluator diverifikasi terhadap ultralytics
pada baseline (0,5153/0,2384 vs 0,5218/0,2407).

**Integritas** — Split per pohon 716/96/141, irisan train-val, train-test, dan
val-test semuanya **nol**. Konfigurasi dipilih pada val; test hanya dilaporkan.

**Hasil tahap 1** — Dipotong pada epoch 6 dari 25 karena anggaran waktu; epoch
6 kebetulan yang terbaik.

| Deteksi kelas-agnostik | mAP50 | mAP50-95 |
|---|---|---|
| Baseline 4-kelas dievaluasi agnostik (640) | 0,7191 | 0,3197 |
| **Tahap 1 khusus agnostik (960, 6 epoch)** | **0,7730** | **0,3320** |

**Hasil tahap 2** — Dua rezim pelatihan, dua mode gagal yang berlawanan:

| Pengklasifikasi | val acc | val seimbang | Catatan |
|---|---|---|---|
| v1 (potongan MVC, tanpa penyeimbang) | 0,6910 | 0,6116 | runtuh ke B3 (B2 recall 0,317, B4 0,386) |
| v2 (potongan master, pencuplikan berimbang) | 0,5350 | 0,6656 | terlalu jauh mengoreksi (B3 recall 0,318) |
| Head YOLO (acuan) | 0,6871 | 0,6484 | — |

Augmentasi tahap 2 sengaja **aman-warna**: baseline YOLO memakai `hsv_s=0.7`
yang mengacak saturasi ±70% pada tugas yang buktinya adalah warna.

**Reproduksi** — `train_agnostic.py`, `build_crops_raw.py`,
`train_maturity_v2.py --root crops_raw`, `two_stage.py --crop-source raw`

---

## E-018 — Plafon lokalisasi: apakah 0,60/0,30 mungkin secara geometris? (2026-07-21) · Ide I-24

**Konteks** — Pengguna menetapkan sasaran tegas: **mAP50 0,60 dan mAP50-95 0,30
pada 4 kelas penuh**, tanpa mendefinisikan ulang metrik. Sebelum menghabiskan
berjam-jam GPU, satu hal harus diketahui: apakah kotak anotasinya sendiri cukup
ketat untuk memungkinkannya? mAP50-95 merata-ratakan ambang IoU sampai 0,95 —
kalau kotak GT digambar longgar, tidak ada model yang bisa mencapainya.

**Cara** — `loc_ceiling.py`: untuk tiap kotak GT val, IoU tertinggi dengan
deteksi mana pun (kelas diabaikan, conf 0,05). Pecahan GT yang tercapai pada
tiap ambang COCO memberi batas atas mAP bila kelas dan peringkat skornya
sempurna.

**Hasil** —

| | Baseline 640 | Agnostik 960 (6 epoch) |
|---|---|---|
| GT tercapai IoU≥0,50 | 0,8834 | 0,8786 |
| GT tercapai IoU≥0,75 | 0,4494 | 0,3975 |
| GT tercapai IoU≥0,90 | **0,0376** | 0,0254 |
| Median IoU terbaik | 0,7303 | 0,7110 |
| **Plafon mAP50 (kelas sempurna)** | **0,8834** | 0,8786 |
| **Plafon mAP50-95 (kelas sempurna)** | **0,4702** | 0,4448 |

**Putusan — SASARAN BERADA DI DALAM PLAFON.** mAP50 0,60 = 68% dari 0,8834;
mAP50-95 0,30 = 64% dari 0,4702. Posisi saat ini 59% dan 51%. Yang dituntut
adalah menutup celah klasifikasi dan peringkat skor, **bukan** menembus batas
ketelitian anotasi.

**Peringatan yang jujur** — hanya 3,76% kotak GT tercapai pada IoU≥0,90 dan
median IoU 0,73. Batas tandan memang kabur (buah menyatu dengan pelepah), jadi
mAP50-95 akan selalu jauh lebih berat daripada mAP50 di dataset ini.

**Koreksi terhadap E-016** — klaim "tiga pengukuran bebas" di SR-011 **cacat
dan ditarik**: voting multi-sisi memakai pengklasifikasi potongan yang sama
(jadi bukan pengukuran ketiga yang bebas), dan head YOLO dilatih dengan
`hsv_s=0.7` sedangkan pengklasifikasi potongan dilatih aman-warna — jadi
perbandingannya tidak setara. Angka 68% tetap dilaporkan apa adanya, tetapi
**tidak boleh dibaca sebagai plafon**. Jalur langsungnya — detektor 4-kelas
resolusi tinggi dengan augmentasi aman-warna — belum pernah diuji sampai E-019.

**Dampak** — Membuka **E-015 → dataset master**: `build_master_ds.py` menautkan
3.000/404/588 citra ke piksel master 3060×4080 (rasio 0,75, identik dengan MVC)
tanpa anotasi ulang dan tanpa menyalin 16 GB. Pada SawitMVC, `imgsz=1280` sudah
memakai seluruh piksel yang ada; master memungkinkan `imgsz` 1600–2048 berisi
detail nyata.

**Reproduksi** — `loc_ceiling.py`, `build_master_ds.py`

---

## E-019 — Detektor 4-kelas resolusi tinggi + augmentasi aman-warna (2026-07-21) · Ide I-24

**Konteks** — Setelah menarik klaim plafon (E-018), jalur paling langsung untuk
sasaran 0,60/0,30 diuji: serang tepat di klasifikasi kematangan, dari dalam
detektor 4-kelas satu tahap. Dua koreksi sekaligus — (a) augmentasi aman-warna
(`hsv_s` 0,7 → 0,15; kematangan adalah warna), (b) resolusi asli 1280 (dari 640).

**Cara** — `train_4cls_hi.py`, yolo26m diinisialisasi dari baseline yang sudah
konvergen, 50 epoch, kosinus, `close_mosaic=15`.

**Hasil** — Puncak val **mAP50 0,5263 (epoch 9) · mAP50-95 0,2361 (epoch 7)**.
Pada epoch yang sama detektor ini unggul dari baseline (ep 10: 0,5062 vs 0,4777),
tetapi puncaknya hanya menempel baseline (0,5218/0,2407) dan menurun setelahnya —
fase pasca-mosaic (epoch 35+) tidak memberi lompatan. Dihentikan pada epoch 41.

**Putusan — MENEMPEL BASELINE, tak cukup.** Diagnosis: memulai dari bobot 640
yang sudah konvergen lalu memaksanya ke 1280 mengganggu model, dan 50 epoch tak
cukup untuk pulih dari cekungan lokal itu. Bukan bukti augmentasi/resolusi tak
membantu — bukti bahwa **fine-tuning dari checkpoint resolusi lain adalah strategi
yang salah**; run berikut (yolo26x, RT-DETR) mulai bersih dari COCO.

**Reproduksi** — `python train_4cls_hi.py --imgsz 1280 --hsv-s 0.15`

---

## E-020 — RT-DETR sebagai detektor NMS-free (2026-07-21) · Ide I-14 · [SR-013](SR/SR-013-rtdetr-nms-free.md)

**Konteks** — Semua yang menempel plateau berasal dari keluarga YOLO, yang
memakai NMS. `deep-research-report.md` menempatkan NMS-free sebagai prioritas 1:
NMS greedy dapat menekan kotak benar pada objek rapat/bertumpuk — persis tandan
di mahkota.

**Hipotesis** — Bila sebagian plafon deteksi berasal dari NMS, RT-DETR (Hungarian
satu-ke-satu, tanpa NMS) mengangkatnya, khususnya recall pada tandan bertumpuk.

**Cara** — `train_rtdetr.py`, RT-DETR-L (33,0 juta parameter), 1280, aman-warna,
60 epoch dari bobot COCO. Menguji hipotesis MEKANISME (bukan kapasitas), jadi
bebas dari jalur yolo26x.

**Status — BERJALAN** (diluncurkan 2026-07-21, ~8–10 jam pada L4). Hasil dan
putusan diisi di SR-013 saat selesai.

**Reproduksi** — `python train_rtdetr.py --weights rtdetr-l.pt --imgsz 1280`
