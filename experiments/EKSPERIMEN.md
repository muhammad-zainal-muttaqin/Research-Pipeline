# Catatan Eksperimen — SawitMVC

Log eksperimen yang **hanya bertambah** (*append-only*). Entri lama tidak diedit
untuk "memperbaiki" hasil; kalau kesimpulan berubah, tulis entri baru yang
merujuk entri lama.

> **Peta baca saat ini:** gunakan [README eksperimen](README.md) untuk status
> dan register, [METRICS.md](METRICS.md) untuk hasil final E-021, serta
> [arsip E-022](archive/E022-seed42-awal.md) bersama
> [AUDIT-E022.md](AUDIT-E022.md) untuk rekam dan koreksi E-022.

**Hasil negatif wajib dicatat.** Justru itu isi paling berharga di sini — ia
mencegah jalan buntu yang sama ditempuh dua kali, dan menjawab pertanyaan
reviewer "apa saja yang sudah dicoba".

> **Catatan migrasi jalur — 25 Juli 2026.** Repositori dirapikan: `docs/` dipecah
> per fungsi (`eksperimen/`, `naskah/`, `audit/`, `referensi/`), skrip
> `experiments/` dikelompokkan (`train/`, `eval/`, `build/`, `analysis/`,
> `shell/`, `config/`), dan `results/` diseragamkan per eksperimen
> (`results/E-0NN/`). **Yang disunting di entri lama hanya jalur berkas** —
> tidak ada satu pun angka, hipotesis, atau putusan yang berubah. Perintah
> reproduksi tetap ditulis relatif terhadap `experiments/` (cwd
> `/workspace/experiments`), sesuai [`experiments/code/REPRODUCE.md`](code/REPRODUCE.md) §2.
> Peta skrip baru: [`experiments/code/PETA-SKRIP.md`](code/PETA-SKRIP.md).

**Laporan per-ide ada di [`experiments/SR`](SR/)** — tiap SR merangkum satu ide dari
masalah → ide → solusi → hasil → putusan. Berkas ini adalah **log kronologis**
(E-NNN); SR adalah **pandangan per-ide**. Tiap entri E-NNN di bawah menyebut ide
dan SR yang memuatnya.

Kode eksperimen dijalankan di `/workspace/experiments/` (di luar repo). Snapshot
**kode + hasil JSON + split**-nya diarsipkan ke [`experiments/code/`](code/)
(kode) dan [`experiments/results/`](results/) (hasil, split, log)
di repo ini agar tiap perintah reproduksi tetap punya sumbernya; artefak besar
(bobot, dataset turunan) tidak diarsipkan karena bisa dibuat ulang dari skrip —
lihat [`experiments/code/README.md`](code/README.md).

> **Seri F — Formulasi, dibuka 6 Agustus 2026.** Mulai dari `F-001`, log ini
> memuat dua penomoran. **Seri E** adalah eksperimen diagnostik dan pembanding
> (praproses, titik fusi, sapuan kapasitas, varians seed/split). **Seri F**
> adalah perubahan **formulasi dan arsitektur** di atas RF-DETR-L — yaitu satu-
> satunya arah yang tersisa menurut pernyataan pengguna 21 Juli 2026 setelah
> teknik siap-pakai dan tuning habis dijalankan (CLAUDE.md §"Pernyataan pengguna").
> Isinya tiga komponen — K1 cabang frekuensi ber-gate init-nol, K2 kepala ordinal
> kumulatif berpenjaga-peringkat, K3 konsistensi query lintas-sisi — masing-masing
> didahului gerbang penyaring yang dapat menggugurkannya tanpa GPU. Aturan
> append-only, satu entri satu hipotesis falsifiable, dan kewajiban mencatat hasil
> negatif berlaku sama persis. Rangkuman per-ide: [SR-017](SR/SR-017-sintesis-deep-research.md).
>
> Nomor `E-033` sudah terpakai dua kali (rentang metrik depth, 6 Agustus 2026),
> jadi seri F **bukan** kelanjutan penomoran E — ia berjalan paralel.

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
| **I-14** | Detektor NMS-free (RT-DETR-L) | laporan (prioritas 1) | **DIKONFIRMASI** — detektor terbaik, +0,063 mAP50 test (E-020, [SR-013](SR/SR-013-rtdetr-nms-free.md)) |
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

**Cara** — `experiments/code/analysis/class_mismatch_stats.py` atas seluruh 953 JSON di
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

**Cara** — `experiments/code/analysis/da3_video_test.py`, checkpoint `depth-anything/da3-large`,
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

**Cara** — `experiments/code/analysis/da3_video_multi.py`, `depth-anything/da3-large`,
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

**Reproduksi** — `python analysis/da3_video_multi.py --videos 6 --frames 32`
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

**Cara** — `experiments/code/analysis/da3_sides_test.py`, `depth-anything/da3-large`,
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

**Reproduksi** — `python analysis/da3_sides_test.py --trees 20 --sides 4` dan
`python analysis/da3_sides_test.py --trees 30 --sides 8 --preview 1`.

---

## E-006 — Sinyal kedalaman di tingkat tandan (2026-07-21) · Ide I-9 · [SR-005](SR/SR-005-sinyal-depth-tandan.md)

**Hipotesis** — Tandan yang tertanam/bertumpuk berada pada lapisan kedalaman
berbeda dari sekitarnya, sehingga kedalaman dapat memisahkan apa yang warna
tidak bisa (naskah §14). Dipalsukan bila kotak tandan tidak menunjukkan kontras
kedalaman lebih besar daripada kotak acak berukuran sama.

**Cara** — `experiments/code/analysis/depth_bunch_signal.py`, 40 pohon (780 kotak
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

**Reproduksi** — `python analysis/depth_bunch_signal.py --trees 40 [--process-res 1008]`

---

## E-007 — Penautan lintas-sisi geometris (2026-07-21) · Ide I-6/I-7 · [SR-006](SR/SR-006-penautan-geometris.md)

**Hipotesis** — Pose kamera DA3 memungkinkan penautan tandan lintas-sisi secara
geometris (tandan sama = titik 3D sama), mengalahkan koreksi statistik k=1,8905.
Dipalsukan bila mode sadar-pose tidak lebih baik daripada penampilan/depth/k.

**Cara** — `experiments/code/analysis/geometric_linking.py`, 141 pohon split uji. Tangga
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

**Reproduksi** — `python analysis/geometric_linking.py --split test [--sweep]`

---

## E-009 — Ukuran kotak pada resolusi latih (2026-07-21) · Ide I-11/I-12

**Hipotesis** — B4 gagal (AP50 0,354) sebagian karena resolusi: pada
`imgsz=640`, citra 960×1280 diperkecil 2×, sehingga tandan kecil kehilangan
piksel sebelum masuk jaringan. Kalau benar, B4 akan jauh lebih kecil daripada
kelas lain dan banyak yang jatuh di bawah ambang "kecil" COCO.

**Cara** — `experiments/code/analysis/box_size_analysis.py`. Tanpa model sama sekali; hanya
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

**Reproduksi** — `python analysis/box_size_analysis.py`

---

## E-010 — Diagnosis kegagalan B4 (2026-07-21) · Ide I-11 · [SR-007](SR/SR-007-diagnosis-b4.md)

**Hipotesis** — Kegagalan B4 (AP50 0,354) punya penyebab yang dapat diukur
langsung dari data, tanpa model. Tiga tersangka diuji berdampingan: kontras
fotometrik rendah, kepadatan/crowding, dan tumpang tindih antar-kotak.

**Cara** — `experiments/code/analysis/why_b4_fails.py` atas 400 citra uji. Kontras diukur di
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

**Reproduksi** — `python analysis/why_b4_fails.py --images 400`

---

## E-011 — Praproses mana yang menaikkan keterpisahan B4? (2026-07-21) · Ide I-20 · [SR-008](SR/SR-008-kanal-tekstur.md)

**Hipotesis** — SR-007 menemukan B4 tersamar dalam warna tetapi bertekstur
tertinggi. Kalau begitu, praproses yang memperkuat kontras lokal atau tekstur
akan menaikkan keterpisahannya. Dipalsukan bila tidak ada praproses yang
menaikkan AUC B4 lebih dari 0,02 di atas acuan.

**Cara** — `experiments/code/analysis/contrast_boost_test.py`, 250 citra uji. Lima peta
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

**Reproduksi** — `python analysis/contrast_boost_test.py --images 250`

---

## E-012 — Plafon diskriminasi kematangan dari penampilan (2026-07-21) · Ide I-18 · [SR-009](SR/SR-009-ordinalitas-kelas.md)

**Hipotesis** — SR-001 gagal mengukur ambiguitas B2/B3 lewat `class_mismatch`.
SR-007 menunjukkan B2 punya kontras latar tinggi tetapi AP50 rendah, artinya
masalahnya membedakan kelas, bukan melihat tandan. Diuji langsung: dapatkah
kematangan dibedakan dari penampilan potongan kebenaran-dasar saja?

**Cara** — `experiments/code/analysis/class_separability.py`. Potongan diambil dari kotak
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
deployment" yang disebut `literature/references/deep-research-report.md`.

**Reproduksi** — `python analysis/class_separability.py --per-class 1500`

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

**Catatan penting** — `experiments/code/train/train_fusion.py` (I-4, sedang berjalan di GPU) TIDAK
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

**Cara** — `experiments/code/eval/diag_bottleneck.py`: bobot identik (`rgb_e60_i640_s42/best.pt`),
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

**Reproduksi** — `python eval/diag_bottleneck.py`

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

**Cara** — `experiments/code/build/match_raw.py`: tiap citra diperkecil lewat penskalaan DCT JPEG
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

**Reproduksi** — `python build/match_raw.py` (CPU, beberapa menit) → `experiments/results/E-015/raw_map.json`

---

## E-016 — Plafon kematangan, diukur tiga kali (2026-07-21) · Ide I-23 · [SR-011](SR/SR-011-plafon-kematangan.md)

**Konteks** — SR-010 memberi sasaran tajam: klasifikasi kematangan harus ≈83%
supaya mAP50 mencapai 0,60. E-016 menguji apakah angka itu bisa dicapai.

**Cara** — Tiga jalur bebas pada tugas identik (diberi kotak, tebak kelas):
head YOLO (`experiments/code/analysis/head_vs_crop.py`), CNN ConvNeXt-Tiny pada potongan master
3024×4032 (`experiments/code/build/build_crops_raw.py` + `experiments/code/train/train_maturity.py`), dan voting antar-sisi
dengan penautan kebenaran dasar (`experiments/code/analysis/multiview_vote.py`).

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

**Reproduksi** — `experiments/code/analysis/head_vs_crop.py`, `experiments/code/analysis/multiview_vote.py`, `experiments/code/eval/metric_variants.py`

---

## E-017 — Detektor dua tahap (2026-07-21) · Ide I-23 · [SR-012](SR/SR-012-dua-tahap.md)

**Konteks** — SR-010 memisahkan deteksi dari klasifikasi; SR-011 mengukur
plafon klasifikasi ~68%. I-23 menguji apakah memisahkan keduanya secara
arsitektural memberi mAP 4-kelas yang lebih baik daripada satu tahap.

**Cara** — Tahap 1: `experiments/code/train/train_agnostic.py`, yolo26m `single_cls=True`, imgsz 960,
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

**Reproduksi** — `experiments/code/train/train_agnostic.py`, `experiments/code/build/build_crops_raw.py`,
`experiments/code/train/train_maturity_v2.py --root crops_raw`, `experiments/code/analysis/two_stage.py --crop-source raw`

---

## E-018 — Plafon lokalisasi: apakah 0,60/0,30 mungkin secara geometris? (2026-07-21) · Ide I-24

**Konteks** — Pengguna menetapkan sasaran tegas: **mAP50 0,60 dan mAP50-95 0,30
pada 4 kelas penuh**, tanpa mendefinisikan ulang metrik. Sebelum menghabiskan
berjam-jam GPU, satu hal harus diketahui: apakah kotak anotasinya sendiri cukup
ketat untuk memungkinkannya? mAP50-95 merata-ratakan ambang IoU sampai 0,95 —
kalau kotak GT digambar longgar, tidak ada model yang bisa mencapainya.

**Cara** — `experiments/code/analysis/loc_ceiling.py`: untuk tiap kotak GT val, IoU tertinggi dengan
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

**Dampak** — Membuka **E-015 → dataset master**: `experiments/code/build/build_master_ds.py` menautkan
3.000/404/588 citra ke piksel master 3060×4080 (rasio 0,75, identik dengan MVC)
tanpa anotasi ulang dan tanpa menyalin 16 GB. Pada SawitMVC, `imgsz=1280` sudah
memakai seluruh piksel yang ada; master memungkinkan `imgsz` 1600–2048 berisi
detail nyata.

**Reproduksi** — `experiments/code/analysis/loc_ceiling.py`, `experiments/code/build/build_master_ds.py`

---

## E-019 — Detektor 4-kelas resolusi tinggi + augmentasi aman-warna (2026-07-21) · Ide I-24

**Konteks** — Setelah menarik klaim plafon (E-018), jalur paling langsung untuk
sasaran 0,60/0,30 diuji: serang tepat di klasifikasi kematangan, dari dalam
detektor 4-kelas satu tahap. Dua koreksi sekaligus — (a) augmentasi aman-warna
(`hsv_s` 0,7 → 0,15; kematangan adalah warna), (b) resolusi asli 1280 (dari 640).

**Cara** — `experiments/code/train/train_4cls_hi.py`, yolo26m diinisialisasi dari baseline yang sudah
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

**Reproduksi** — `python train/train_4cls_hi.py --imgsz 1280 --hsv-s 0.15`

---

## E-020 — RT-DETR sebagai detektor NMS-free (2026-07-21) · Ide I-14 · [SR-013](SR/SR-013-rtdetr-nms-free.md)

**Konteks** — Semua yang menempel plateau berasal dari keluarga YOLO, yang
memakai NMS. `literature/references/deep-research-report.md` menempatkan NMS-free sebagai prioritas 1:
NMS greedy dapat menekan kotak benar pada objek rapat/bertumpuk — persis tandan
di mahkota.

**Hipotesis** — Bila sebagian plafon deteksi berasal dari NMS, RT-DETR (Hungarian
satu-ke-satu, tanpa NMS) mengangkatnya, khususnya recall pada tandan bertumpuk.

**Cara** — `experiments/code/train/train_rtdetr.py`, RT-DETR-L (33,0 juta parameter), 1280, aman-warna,
60 epoch dari bobot COCO. Menguji hipotesis MEKANISME (bukan kapasitas), jadi
bebas dari jalur yolo26x.

**Cara (detail varian)** — RT-DETR-L (ultralytics 8.4.103, `rt-detr-l.yaml`):
backbone HGNetv2-L, encoder AIFI + RepC3, RTDETRDecoder (tanpa NMS),
**32.970.476 param**, 103,4 GFLOPs. Dihentikan ep52/60 setelah mosaic-off (ep50)
tak memberi lonjakan; `best.pt` = epoch fitness-terbaik (ep25).

**Hasil (best.pt, dievaluasi ulang bersih):**

| | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|
| VAL baseline | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| **VAL RT-DETR** | 0,5466 | 0,2543 | 0,7503 | 0,4413 | 0,5808 | 0,4138 |
| TEST baseline | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| **TEST RT-DETR** | **0,5794** | **0,2694** | 0,7891 | 0,4685 | 0,6391 | **0,4208** |

**Putusan — DIKONFIRMASI (arah), target belum tercapai.** Detektor 4-kelas
terbaik sejauh ini: unggul di keempat kelas pada kedua split, **+0,063 mAP50
test**, dan gain terbesar di **B4 (+0,0885)** — kelas paling padat/tersamar,
persis tanda tangan hipotesis NMS-free. Test tinggal −0,021 dari sasaran mAP50
0,60. **Koreksi prediksi:** selama pelatihan saya menduga plateau/DIPALSUKAN —
keliru, itu membaca last.pt yang overfit; best.pt jauh lebih baik.

**Dampak** — RT-DETR jadi tulang punggung baru menggantikan yolo26m. Lanjutan:
latih di piksel master (imgsz 1600–2048), dan RT-DETR-X (67,5 juta).

**Reproduksi** — `python train/train_rtdetr.py --weights rtdetr-l.pt --imgsz 1280`
lalu `python eval/eval_rtdetr.py`

---

## E-021 — RF-DETR-L: transformer NMS-free DINOv2 vs RT-DETR (2026-07-24) · Ide I-14 · lanjutan [E-020]

**Konteks** — E-020 mengonfirmasi arah NMS-free (RT-DETR-L) mengalahkan keluarga
YOLO. RF-DETR-L (backbone **DINOv2** pra-latih + kepala LW-DETR hasil NAS) adalah
transformer NMS-free generasi lebih baru. Pertanyaannya bukan kapasitas melainkan
apakah pada setelan **identik & adil** ia melampaui RT-DETR-L.

**Hipotesis** — RF-DETR-L layak jadi pembanding bila pada val identik ia
(a) melampaui yolo26m dan (b) mendekati/melampaui RT-DETR-L pada kedua metrik.
**DIPALSUKAN** bila run konvergen tertinggal dari RT-DETR-L pada kedua metrik.
Test hanya dilaporkan setelah checkpoint dipilih dari val.

**Cara** — `experiments/code/train/train_rfdetr.py` + `experiments/code/build/build_rfdetr_ds.py` (adaptor dataset YOLO tanpa
salin citra, split identik E-017 3000/404/588). RFDETRLarge (rfdetr 1.8.3,
**35,65 juta param**, DINOv2 patch-16 + 2-window), resolusi **1280 tepat**
(kelipatan 32; sama RT-DETR), dari bobot COCO `rf-detr-large-2026`, batch efektif
16 (batch 8 × grad-accum 2). Early-stopping patience 8 → berhenti ep17, checkpoint
terbaik **ep9 (EMA)**.

**Fairness (dijaga ketat)** — (1) Resolusi 1280 identik: default rf-detr
`multi_scale`+`expanded_scales` diam-diam mengunci ke skala TERBESAR (1440);
**dimatikan** agar benar-benar 1280. (2) Split, augmentasi aman-warna, effective
batch sekelas RT-DETR. (3) `.evaluate()` tak ada di rfdetr 1.8.3 → pakai
`run_test=True`; GPU L4 sempat kelaparan data (num_workers default 2) — dinaikkan
ke 8; batch16/workers32 meledak `/dev/shm` 26 GB → turun ke 8/8.

**Hasil (checkpoint ep9 EMA; per-kelas AP50 via COCO eval `experiments/code/eval/eval_rfdetr_perkelas.py`):**

| | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|
| VAL RT-DETR | 0,5466 | 0,2543 | 0,7503 | 0,4413 | 0,5808 | 0,4138 |
| **VAL RF-DETR** | **0,5695** | **0,2604** | 0,775 | 0,446 | 0,594 | **0,464** |
| TEST RT-DETR | 0,5794 | 0,2694 | 0,7891 | 0,4685 | 0,6391 | 0,4208 |
| **TEST RF-DETR** | **0,6038** | **0,2770** | 0,817 | 0,497 | 0,668 | 0,433 |

Sanity: val pycocotools saya (0,5695) cocok evaluator internal rf-detr (0,5699 EMA)
→ pipeline tervalidasi. `run_test` bawaan melaporkan test 0,5837/0,2653 memakai
checkpoint `best_total` (berbeda); angka di atas EMA konsisten val↔test.

**Putusan — DIKONFIRMASI.** RF-DETR-L melampaui RT-DETR-L (dan yolo26m) pada val
kedua metrik (+0,023 mAP50, +0,006 mAP50-95) dan pada test (+0,024 mAP50,
+0,008 mAP50-95). **Detektor 4-kelas terbaik baru.** Test mAP50 0,604 melewati
sasaran 0,60. Kelas tersulit tetap B4.

**Caveat kesetaraan (dicatat, sedang ditangani)** — yolo26m (21,9 jt, imgsz 640)
BUKAN pembanding sekelas RT-DETR-L (33,0 jt) / RF-DETR-L (35,7 jt @1280).
Pembanding YOLO adil = **YOLO26l (26,3 jt) @1280** config identik RT-DETR —
**BERJALAN** (`experiments/code/train/train_yolo26l.py`). Evaluator juga campur (yolo/rtdetr via
ultralytics `.val()`, rf-detr via pycocotools); unifikasi 1-protokol
`experiments/code/eval/eval_all_pycoco.py` → `experiments/results/E-021/perkelas_pycoco.json` **BERJALAN**.

**Dampak** — RF-DETR-L jadi detektor terbaik menggantikan RT-DETR-L (E-020).
Lanjutan: selesaikan YOLO26l + tabel 1-protokol; pertimbangkan latih di piksel
master.

**Reproduksi** — `python build/build_rfdetr_ds.py` → `python train_rfdetr.py --dataset
rfdetr_ds --epochs 60 --resolution 1280 --batch 8 --grad-accum 2 --workers 8` →
`python eval/eval_rfdetr_perkelas.py`. Metrik: `experiments/results/E-021/perkelas_fair.json`,
`experiments/runs/rfdetr_l_e60_i1280/evaluation.json` + `metrics.csv`.

**Lanjutan (2026-07-25) — dua caveat E-021 diselesaikan:** (1) Baseline YOLO
**param-adil YOLO26l** (26,3 jt, config IDENTIK RT-DETR: 1280/60ep/color-safe/
seed42/cos_lr/COCO) dilatih penuh — `experiments/code/train/train_yolo26l.py`, best val ep31. (2) Semua
4 model dievaluasi lewat **1-protokol pycocotools** (`experiments/code/eval/eval_all_pycoco.py` →
`experiments/results/E-021/perkelas_pycoco.json`), menghapus caveat evaluator campur. Hasil
1-protokol (mAP50/mAP50-95):

| Model | Param | VAL | TEST |
|---|---|---|---|
| YOLO26m | 21,9 jt | 0,5195 / 0,2411 | 0,5165 / 0,2452 |
| YOLO26l | 26,3 jt | 0,5270 / 0,2526 | 0,5300 / 0,2568 |
| RT-DETR-L | 33,0 jt | 0,5459 / 0,2555 | 0,5784 / 0,2707 |
| **RF-DETR-L** | 35,7 jt | **0,5695 / 0,2604** | **0,6038 / 0,2770** |

Ranking = urutan parameter di semua metrik/split. **YOLO26l (param-adil) tetap di
bawah kedua DETR** → keunggulan RF-DETR/RT-DETR **bukan efek kapasitas/resolusi**,
melainkan arsitektur NMS-free. Putusan E-021 makin kuat. Tabel penuh per-kelas:
[METRICS.md](METRICS.md) §1-protokol. Reproduksi: `python train/train_yolo26l.py` →
`python eval/eval_all_pycoco.py`.

**Laporan per-ide:** [SR-014](SR/SR-014-rfdetr-dinov2.md) (ditulis 25 Juli 2026).

---

## E-022 — Depth SENSOR Orbbec pada SawitMVC-Depth: registrasi + 4-kanal simultan (2026-07-29) · Ide I-4/I-8 · [SR-015](SR/SR-015-depth-sensor-4kanal.md)

> ### ⚠ PENCABUTAN SEBAGIAN — 2026-07-30
>
> **Seluruh kesimpulan arah-efek di entri ini bertumpu pada SATU seed (42) dan
> tidak bertahan saat direplikasi.** Replikasi 3 seed pada dua arsitektur
> (12 run YOLO26n + 9 run RT-DETR-L, 60 epoch, split per-pohon identik)
> menunjukkan:
>
> - **YOLO26n:** Δ(RGB-D − RGB) = +0,0252 / −0,0063 / −0,0013 pada seed
>   42/1337/2024. Rerata +0,0059, dan CI95 ketiganya melewati nol
>   (P(>0) = 0,851 / 0,436 / 0,406). Angka +0,0252 yang dilaporkan di bawah
>   adalah **seed paling menguntungkan dari tiga**, bukan efek yang dapat
>   dipertahankan. Pernyataan yang benar: **tidak dapat dibedakan dari nol.**
> - **B4 hanya punya 95 kotak** di dataset ini, dan AP B4 bergerak
>   0,0945 → 0,3147 hanya karena ganti seed. Seluruh Δ agregat yang
>   diperdebatkan di entri ini (±0,04) **lebih kecil daripada lantai derau
>   antar-seed pada satu kelas yang memegang 25% bobot macro-mAP.**
>
> **Dua lengan kontrol di bawah dibuat dengan kode cacat** dan angkanya tidak
> sah (lihat [AUDIT-E022.md](AUDIT-E022.md)):
> - lengan **depth pohon LAIN** mengambil donor lintas split — 192/980 citra
>   train memakai depth pohon **test**. Setelah diperbaiki, angkanya turun
>   0,3771 → 0,3301 (−0,0470). Klaim "registrasi tidak memberi apa pun"
>   **tidak lagi didukung**.
> - lengan **derau** memakai satu RNG bersama sehingga kanal ke-4 diacak ulang
>   tiap epoch — ia diam-diam mendapat augmentasi. Setelah diperbaiki derau
>   justru **naik** (RT-DETR-L 0,3552 → 0,3894), jadi temuan "derau
>   mengalahkan depth" bertahan dan bahkan diperkuat.
>
> Angka multi-seed protokol beku sedang diproduksi; entri ini akan
> **direstrukturisasi**, bukan ditambal. Sampai itu selesai, jangan mengutip
> arah-efek dari entri ini.
>
> ### ✅ RESTRUKTURISASI SELESAI — 2026-08-01
>
> Restrukturisasi yang dijanjikan di atas **sudah dilaksanakan**, dan sesuai
> aturan append-only ia berbentuk **entri-entri baru**, bukan suntingan pada
> entri ini. Angka di bawah dipertahankan utuh sebagai rekam seed-42; yang
> menggantikannya:
>
> | Entri | Menggantikan bagian mana |
> |---|---|
> | [E-025](EKSPERIMEN.md) | Selisih evaluator yang belum terjelaskan — terlacak: menskala dengan jumlah deteksi. `hasil.json` dilarang untuk perbandingan antar lengan |
> | [E-027](EKSPERIMEN.md) | Seluruh arah-efek YOLO26n. Matriks 12 run (4 modal × 3 seed): depth − RGB rerata **−0,0230**, dua seed signifikan NEGATIF |
> | [E-029](EKSPERIMEN.md) | Seluruh arah-efek RT-DETR-L. Matriks 9 run: klausa "depth terpakai pada kapasitas tinggi" **DICABUT PENUH** |
> | [E-030](EKSPERIMEN.md) | Klaim "kapasitas menentukan arah efek" — dipersempit: benar untuk kanal tanpa informasi, tidak untuk depth-vs-derau |
> | [E-031](EKSPERIMEN.md) | Keterbatasan "varians split belum diukur" — terukur 0,0488 pada lengan RGB |
>
> **Tidak ada angka di entri ini yang boleh dikutip.** Seluruhnya bertumpu pada
> satu seed, dua lengan kontrol berkode cacat, dan evaluator yang kini terlarang
> untuk perbandingan antar lengan. Untuk keadaan terkini mulai dari
> [STATUS.md](STATUS.md); untuk metrik terukur seluruh run lihat
> [METRIK-LENGKAP.md](METRIK-LENGKAP.md).

**Konteks** — Dataset baru `ULM-DS-Lab/SawitMVC-Depth` (352 pohon, 1.408 citra
RGB 1280×800, depth sensor Orbbec Y16 848×480 uint16le milimeter, 2.299 kotak
B1–B4) menyediakan hal yang selama ini kosong di STATUS.md §5: **depth SENSOR
sungguhan**, bukan pseudo-depth. Sampai E-021 hanya pseudo-depth yang pernah
diuji (E-006/SR-005, dipalsukan). Integritas 6.336 artefak diverifikasi
SHA-256 terhadap `manifests/`: 0 hilang, 0 tidak cocok.

**Peringatan pembanding, ditulis di depan** — angka apa pun di entri ini **tidak
sebanding** dengan test mAP50 0,6038 milik E-021. Dataset berbeda: prior kelas
terbalik (B3 52,3% → 14,0%; B1 11,0% → 36,1%), kotak ~2× lebih besar relatif,
orientasi berubah (960×1280 potret → 1280×800 lanskap), anotasi 18.540 → 2.299.
Satu-satunya klaim sah adalah **selisih RGB-D minus RGB di dalam dataset ini**
pada protokol identik.

### E-022a — Apakah depth benar-benar sudah tersejajar ke RGB?

**Hipotesis (H-022c)** — Buffer depth 848×480 sudah tersejajar ke bidang color
sebagaimana klaim sidecar `"alignedTo": "color"`, sehingga `cv2.resize` ke
1280×800 sudah cukup (asumsi yang dipakai `pipeline/prepare_depth.py`).
**Dipalsukan bila** geometri kalibrasi atau uji empiris menunjukkan buffer masih
di grid kamera depth.

**Cara** — `build/depth_calib.py` (parser kalibrasi per-berkas + reproyeksi),
`analysis/verify_depth_align.py` (uji berbasis kotak anotasi), `analysis/verify_depth_mi.py`
(mutual information agregat + kontrol pergeseran, bootstrap berpasangan 2000×).

**Hasil — DIPALSUKAN, tiga bukti independen:**

1. **Geometri kalibrasi.** Intrinsik depth (fx=fy=416,55, piksel persegi) bukan
   versi terskala intrinsik color: 610,87·848/1280 = 404,7 pada x tetapi
   610,87·480/800 = 366,5 pada y — tidak persegi, tidak konsisten.
2. **Tidak ada pita kosong struktural.** FOV vertikal color 66,4° > depth 59,9°.
   Bila depth sudah di-resample ke bidang color, ~34 baris atas dan ~28 baris
   bawah wajib kosong di setiap citra. Terukur: **0 baris dan 0 kolom** yang
   selalu-invalid.
3. **Mutual information.** MI(depth; abu-abu RGB) atas 150 citra:

   | Pemetaan | MI (bit) |
   |---|---|
   | H1 resize langsung | 0,2546 |
   | H2 affine-intrinsik | 0,2591 |
   | **H3 reproyeksi penuh** | **0,2852** |
   | H3 digeser +24 px (kontrol) | 0,2385 |
   | H3 digeser −24 px (kontrol) | 0,2320 |

   Selisih berpasangan **H3 − H1 = +0,0306 bit, CI95 [0,0260; 0,0354]** (tidak
   memuat 0), H3 menang di **84%** dari 150 citra. Kontrol pergeseran buatan
   menurunkan MI → metrik memang peka terhadap registrasi.

**Putusan — DIPALSUKAN.** Label `alignedTo: "color"` menyesatkan; buffer masih di
grid kamera depth pabrikan. Resize naif meleset **median 29,3 px, maksimum 61 px**
pada bidang 1280×800 — seukuran tandan B4 itu sendiri. Memakainya akan
menghasilkan hasil negatif palsu yang terbaca sebagai "depth tidak menolong",
persis skenario D3Net (entri 037).

**Dampak** — `pipeline/prepare_depth.py` **tidak boleh dipakai untuk dataset ini**.
Diganti `build/reproject_depth.py`: depth → titik 3D (intrinsik depth) → ekstrinsik →
intrinsik color + distorsi Brown-Conrady K6, forward-warp **ber-z-buffer** (tanpa
ini latar menimpa objek di tepi oklusi — justru sinyal yang dicari untuk B4),
tambal lubang **median 3×3** (operator ranking, bukan blur yang menghasilkan
kedalaman hantu melintasi batas objek).

Dua temuan pendamping yang mengubah konfigurasi:

- **Ada DUA unit kamera**, bukan satu: 660 berkas fx_depth=416,55 dan 748 berkas
  fx_depth=414,38, rotasi ekstrinsik 0,064° vs 0,562°. Kalibrasi **wajib dibaca
  per berkas**; hardcode satu set = separuh dataset salah proses, dan biasnya
  berkorelasi dengan perangkat sehingga bocor ke perbandingan antar-split.
- **Rentang metrik `fourch.py` (0,3–8,0 m) tidak cocok data ini.** 0,000% piksel
  valid di bawah 0,3 m (minimum absolut 313 mm) sementara 10,07% melebihi 8 m;
  entropi kanal hanya 6,19 dari 7,99 bit, level median 21/255. Dipilih ulang dari
  histogram **split train saja** (anti-kebocoran): **Z_NEAR=0,8 / Z_FAR=15,0**,
  entropi 7,62 bit, level median 74/255. Nilai >15 m dan 65535 (saturasi uint16)
  diperlakukan tidak valid. Angka ini dibekukan bersama bobot di
  `depth_png/depth_meta.json`.

### E-022b — Apakah depth sensor menaikkan mAP?

**Hipotesis (H-022)** — Pada SawitMVC-Depth, dengan split per-pohon identik, seed
identik, dan seluruh hiperparameter identik kecuali kehadiran kanal kedalaman,
detektor dengan masukan 4-kanal RGB+D sensor (ter-reproyeksi) mencapai test mAP50
lebih tinggi daripada baseline RGB-saja dengan **delta > +0,015**, dan CI 95%
bootstrap berpasangan **per-pohon** atas selisih itu tidak memuat 0.

**Yang memalsukan H-022** (salah satu cukup): (1) delta ≤ +0,015; (2) CI95 memuat
0; (3) delta lebih kecil daripada varians antar-seed pada lengan RGB sendiri;
(4) kontrol negatif kanal-4 = derau memberi kenaikan sebanding — maka kenaikan
berasal dari kapasitas tambahan di stem, bukan dari informasi kedalaman.

Ambang +0,015 dipilih karena reproduksi tidak bit-per-bit deterministik meski
seed=42 (deviasi wajar ±0,005 menurut `REPRODUCE.md`). Selisih ≤0,005 **tidak
boleh** dinarasikan sebagai perbaikan maupun penurunan.

**H-022b (sub-hipotesis mekanistik)** — kenaikan terkonsentrasi pada B4 dan citra
teroklusi, bukan B2/B3. Kegagalan B2/B3 sudah didiagnosis **fotometrik** (SR-007,
SR-009), jadi hasil naik di B4 tapi datar di B2/B3 adalah **konfirmasi teori**,
bukan kegagalan. **Peringatan daya uji: B4 hanya punya 148 kotak di SELURUH
dataset** (38 di test) — AP50 B4 bisa bergeser >0,1 karena beberapa kotak saja;
H-022b dilaporkan dengan CI dan tidak boleh jadi klaim utama.

**Cara** — Split per-pohon terstratifikasi `(device × unit-kamera) × kelas-dominan`,
irisan nol: train 245 pohon/980 citra/1.593 kotak · val 35/140/202 · test
72/288/504 (B4 95/15/38). Skrip: `build/make_splits_depth.py`, `build/reproject_depth.py`,
`train/train_depth4ch.py`, `eval/eval_e022_pycoco.py`.

Tiga pagar keadilan yang dipasang sengaja, semuanya jebakan senyap:

1. **HSV dimatikan di KEDUA lengan.** `RandomHSV.apply_image` melewati citra
   non-3-kanal secara diam (`ultralytics/data/augment.py:1461`) — tanpa pagar ini
   lengan RGB dapat augmentasi yang tidak didapat lengan RGB-D, dan selisihnya
   salah diatribusikan ke depth.
2. **Inflasi conv pertama** (`fourch.make_inflate_callback`): kanal 1–3 dari bobot
   pratlatih urutan BGR, kanal ke-4 = 0, model + EMA sama-sama ditambal. Tanpa ini
   conv pertama 4-kanal mulai acak dan lengan RGB-D kalah karena inisialisasi.
   Terverifikasi di log run.
3. **Modality dropout = 0** untuk lengan hipotesis. Dengan dropout 0,25 lengan
   RGB-D sebenarnya berlatih 25% tanpa depth; hasil datar lalu ditafsirkan "depth
   tidak menolong" padahal yang diuji bukan itu.

**Hasil — pasangan 1: YOLO26n (2,57 jt param, imgsz 640, 60 epoch)**

Angka lewat 1-protokol pycocotools, split test 72 pohon / 288 citra / 504 kotak:

| Lengan | mAP50 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|
| RGB | 0,3249 | 0,6598 | 0,4342 | 0,0889 | 0,1166 |
| RGB-D 4-kanal | **0,3501** | 0,6102 | 0,4394 | **0,2001** | **0,1506** |

**delta mAP50 = +0,0252 · CI95 bootstrap berpasangan per-pohon [−0,0215; +0,0632] ·
P(delta>0) = 0,851 · B=2000**

**Putusan pasangan 1 — H-022 DIPALSUKAN.** Kriteria falsifikasi butir (2) yang
ditulis sebelum melihat hasil berbunyi "CI 95% bootstrap berpasangan per-pohon
memuat 0". CI memuat 0, jadi meski titik estimasi +0,0252 melewati ambang
+0,015, buktinya belum dapat dibedakan dari nol. Sebabnya bukan misteri: test
hanya 72 pohon / 504 kotak, dan resample **per pohon** (yang benar secara
statistik, karena 4 sisi satu pohon tidak independen) memang melebarkan CI
dibanding resample per citra yang akan menipu.

**Arah per-kelas konsisten dengan H-022b** — kenaikan terkonsentrasi pada kelas
yang kegagalannya geometris: B3 +0,1112 dan B4 +0,0340, sementara B1 justru
TURUN 0,0496. B1 adalah kelas jingga-merah paling kontras, yang memang tidak
membutuhkan isyarat kedalaman. Tetapi B4 hanya punya 38 kotak di test — tidak
ada klaim yang boleh disandarkan padanya tanpa CI per-kelas tersendiri.

**Catatan metodologis yang penting untuk pasangan berikutnya:** dengan test
sekecil ini, CI satu pasangan akan selalu lebar. Bukti yang lebih kuat adalah
**konsistensi lintas arsitektur** — bila RT-DETR-L dan RF-DETR Nano memberi
delta positif dengan pola per-kelas yang sama (naik di B3/B4, datar atau turun
di B1), itu jauh lebih sulit dijelaskan oleh kebetulan daripada satu CI lebar.
Tiga pasangan + kontrol negatif kanal-derau adalah rancangan yang sedang
dijalankan.

**Hasil — sembilan run, 60 epoch, seed 42, konfigurasi identik per pasangan**

Angka lewat 1-protokol pycocotools (RF-DETR lewat `eval/eval_rfdetr_e022.py` dari
`checkpoint_best_ema.pth`; kedua lengannya memakai evaluator yang sama sehingga
selisihnya bersih). Test = 72 pohon / 288 citra / 504 kotak.

| Kanal ke-4 | YOLO26n (2,57 jt) | RT-DETR-L (33,0 jt) | RF-DETR Nano |
|---|---|---|---|
| tidak ada (RGB) | 0,3249 | **0,4076** | 0,4196 |
| depth sensor terregistrasi | 0,3501 | 0,3900 | **0,4635** |
| derau acak | 0,3686 | 0,3535 | (val EMA 0,5093) |
| depth pohon LAIN | 0,3721 | — | — |

Selisih berpasangan, bootstrap 2000x resample per **POHON**:

| Perbandingan | delta mAP50 | CI95 | P(>0) |
|---|---|---|---|
| YOLO26n depth − RGB | +0,0252 | [−0,0215; +0,0632] | 0,851 |
| RF-DETR Nano depth − RGB | +0,0439 | [+0,0000; +0,0918] | 0,975 |
| RT-DETR-L depth − RGB | −0,0177 | [−0,0669; +0,0203] | 0,225 |
| **YOLO26n DERAU − RGB** | **+0,0437** | **[+0,0051; +0,0875]** | 0,991 |
| YOLO26n depth − derau | −0,0186 | [−0,0694; +0,0191] | 0,194 |
| YOLO26n depth − tukar | −0,0220 | [−0,0506; +0,0085] | 0,080 |
| RT-DETR-L depth − derau | +0,0365 | [−0,0014; +0,0668] | 0,971 |
| RF-DETR Nano depth − derau | +0,0087 | [−0,0372; +0,0538] | 0,649 |

**Putusan H-022 — DIPALSUKAN, pada dua kriteria independen:**

- Butir (2): CI berpasangan memuat 0 untuk ketiga arsitektur. Delta terbesar
  (RF-DETR Nano +0,0439) berbatas bawah tepat +0,0000.
- Butir (4): **kontrol negatif menyamai.** Kanal ke-4 berisi DERAU memberi
  +0,0437 dengan CI yang **tidak** memuat nol — satu-satunya delta di seluruh
  E-022 yang signifikan, dan ia berasal dari kanal tanpa informasi apa pun.

**Kontrol registrasi (baru, tidak ada di rencana awal).** Kanal ke-4 diisi peta
depth ASLI milik pohon LAIN (`train_depth4ch.py --depth-tukar`): statistik dan
tekstur depth realistis, hanya keselarasan spasialnya dihancurkan. Hasil pada
YOLO26n: 0,3721 vs depth benar 0,3501, selisih −0,0220 CI [−0,0506; +0,0085].
**Tafsir yang benar: keduanya TIDAK DAPAT DIBEDAKAN** (CI memuat nol), dan pada
B1 depth benar justru signifikan lebih buruk (−0,0662 [−0,1089; −0,0199]).
Konsekuensinya keras: **reproyeksi penuh yang dibuktikan lebih selaras di E-022a
tidak membeli apa pun pada model kecil.**

**Putusan H-022b — TIDAK KONKLUSIF, tetapi mekanismenya terlihat pada model
besar.** Pada YOLO26n, kenaikan B4 direproduksi persis oleh depth-tertukar
(0,1671 vs 0,1506) sehingga tidak bisa disebut manfaat geometris. Namun pada
RT-DETR-L, depth mengalahkan kontrol deraunya sendiri secara signifikan justru
di kelas yang diprediksi teori: **B4 +0,1001 [+0,0062; +0,1618]** dan B1 +0,0698
[+0,0306; +0,1100]. Jadi kandungan informasi depth NYATA pada model besar,
tetapi tidak cukup menutup kerugian yang ditimbulkan kanal ke-4 itu sendiri.

Pola depth-vs-derau kini lengkap untuk ketiga arsitektur dan **konsisten**: pada
**dua** model kecil depth tidak dapat dibedakan dari derau secara keseluruhan
(YOLO26n −0,0186; RF-DETR Nano +0,0087, keduanya CI memuat nol) dan justru
signifikan **lebih buruk** di B1 (−0,0734 dan −0,0446). Hanya pada RT-DETR-L
33,0 jt parameter isi kanal menentukan: B1 +0,0698 dan B4 +0,1001, keduanya CI
tidak memuat nol. **Kandungan informasi depth baru terpakai pada kapasitas tinggi.**

**Temuan struktural: arah efek kanal ke-4 ditentukan KAPASITAS MODEL, bukan isi
kanal.** Pada 2,57 jt parameter kanal ke-4 menaikkan (dan isinya tidak penting —
derau dan depth-tertukar setara atau lebih baik daripada depth benar); pada
33,0 jt parameter kanal ke-4 menurunkan (dan isinya penting — depth jauh lebih
baik daripada derau). Tafsir paling hemat: pada model kecil yang undertrained di
1.593 kotak latih, kanal ke-4 bekerja sebagai regularisasi; pada model besar
berbobot pratlatih, ia mengganggu stem 3-kanal dan depth hanya memulihkan
sebagian kerugian itu.

**Dampak — arah lanjutan yang kini didukung bukti sendiri, bukan kutipan.**
Kegagalan ada pada **cara memasukkan** depth (konkatenasi di kanal masukan), bukan
pada kandungan depth-nya. Ini persis yang diprediksi korpus (FuseNet 4-kanal
31,95 IoU di bawah RGB 32,47 sementara fusi fitur 37,29; sapuan 28 titik fusi
Ophoff, `evidence-body.tex` §174). **E-023 yang diusulkan: fusi MENENGAH dua
cabang** pada RT-DETR-L/RF-DETR, karena di situlah depth sudah terbukti membawa
informasi B4. Kontrol derau dan kontrol tukar wajib diulang di sana.

**Keterbatasan yang tidak boleh dihaluskan:**

- **Satu seed, satu split.** Semua selisih di atas ~0,02–0,04 sementara deviasi
  antar-run wajar ±0,005 dan CI-nya 0,05–0,09 lebar. Varians split belum diukur;
  3-fold CV yang direncanakan tidak dijalankan.
- **B4 hanya 148 kotak di SELURUH dataset** (38 di test). Setiap klaim per-kelas
  B4 bersandar pada puluhan kotak.
- **Dataset 8x lebih kecil** dari SawitMVC. Daya uji untuk mendeteksi efek kecil
  memang rendah; "tidak terbukti" di sini bukan "terbukti tidak ada".
- RF-DETR RGB-D dan derau: `run_test` bawaan tidak pernah berjalan pada kedua
  lengan; evaluasi test dijalankan terpisah dari `checkpoint_best_ema.pth` lewat
  `eval/eval_rfdetr_e022.py` — bukan latih ulang.
  **Koreksi 2026-07-30:** versi sebelumnya menyatakan penyebabnya kuota disk
  habis dengan `checkpoint_59.ckpt` terpotong tepat 256 MB pada kedua lengan.
  **Klaim itu tidak dapat disubstansiasi dan sudah dihapus.** Pemeriksaan disk:
  `runs_e022/rfdetrnano_rgbd/` tidak memuat `.ckpt` sama sekali, dan
  `checkpoint_59.ckpt` hanya ada di `runs_e022/rfdetrnano_derau/` dalam ukuran
  utuh 488.105.861 byte — bukan 268.435.456. Penyebab sebenarnya tidak diketahui
  dan tidak boleh dinarasikan tanpa bukti.

**Reproduksi** — `build/depth_calib.py`, `analysis/verify_depth_mi.py` (gerbang registrasi),
`build/reproject_depth.py` (PNG kanonik + `depth_meta.json`), `build/make_splits_depth.py`,
`train/train_depth4ch.py` (ultralytics; `--depth-acak`, `--depth-tukar`),
`train/train_rfdetr_4ch.py` (rfdetr 4-kanal, 4 tambalan), `eval/eval_e022_pycoco.py`,
`eval/eval_e022_paired.py`, `eval/eval_rfdetr_e022.py`. Hasil: `results/E-022/*.json`.
Split persis: `splits_depth/seed42/`. Tabel seed-42 awal:
[archive/E022-seed42-awal.md](archive/E022-seed42-awal.md). Audit koreksi:
[AUDIT-E022.md](AUDIT-E022.md).

---

## E-024 — Inkonsistensi prediksi lintas-sisi sebagai ukuran ambiguitas (2026-07-31) · pengganti E-001

**Hipotesis** — `class_mismatch` dipalsukan di E-001 sebagai ukuran ambiguitas
kematangan: nol dari 7.328 bunch multi-sisi, yang menjadikannya pemeriksa
integritas anotasi, bukan pengukur ambiguitas. CLAUDE.md mencatat penggantinya:
pakai identitas bunch lintas-sisi sebagai **oracle**, lalu ukur inkonsistensi
**prediksi detektor** pada tandan fisik yang sama. Hipotesisnya: detektor
memberi kelas kematangan berbeda pada objek fisik yang sama dilihat dari sisi
berbeda, dan ketidaksepakatan itu menumpuk pada pasangan kelas bertetangga.
**Dipalsukan bila** laju inkonsisten mendekati nol (artinya penampilan sudah
menentukan kelas secara stabil) atau tersebar merata tanpa struktur.

**Cara** — `analysis/cross_side_consistency.py`. Oracle tidak dihitung ulang:
`json/<tree>.json` sudah menyediakan `bunches[].appearances`, yaitu transitive
closure graf `_confirmedLinks` — satu entri = satu tandan fisik dengan kotak
piksel per sisi. Prediksi dibuat lewat jalur yang sama dengan evaluator E-022
(`eval_e022_pycoco.prediksi`) supaya praproses dan komposisi kanal tidak
berbeda diam-diam. Kemunculan dicocokkan ke prediksi pada IoU >= 0,5, conf
>= 0,25. Checkpoint: `yolo26n_rgb_seed42` (60 epoch, split test SawitMVC-Depth
72 pohon).

**Hasil**

| Ukuran | Nilai |
|---|---:|
| Tandan fisik di split test | 310 |
| Tampak dari >= 2 sisi | 182 |
| Terukur (>= 2 sisi terdeteksi) | 82 |
| Kemunculan terlewat | 137 / 376 = **36,4%** |
| **Tidak konsisten** | 16 / 82 = **19,5%** |

Pasangan kelas yang bertabrakan: **B1↔B2 sebanyak 11**, **B2↔B3 sebanyak 6**.
Tidak ada tabrakan yang melibatkan B4. Sebaran per kelas GT yang terukur:
B1 50, B2 25, B3 7, **B4 nol** — seluruh tandan B4 multi-sisi gagal terdeteksi
di >= 2 sisi, sehingga tidak masuk pengukuran sama sekali.

**Putusan — DIKONFIRMASI, dengan daya uji terbatas.** Detektor memberi kelas
berbeda pada tandan fisik yang sama pada 19,5% kasus, sementara anotator
manusia tidak pernah (0/7.328 di E-001). Pemisahan itu bersih: ambiguitas
berada pada klasifikasi berbasis penampilan, bukan pada labelnya. Strukturnya
juga sesuai prediksi — tabrakan terkonsentrasi pada tetangga ordinal (B1↔B2,
B2↔B3), konsisten dengan ordinalitas kelas yang dikonfirmasi E-012/SR-009.

**Yang tidak boleh dihaluskan:**

- **n = 82** tandan terukur. Setiap butir persentase bersandar pada kurang dari
  satu tandan.
- **Laju terlewat 36,4%** dicatat justru supaya "konsisten" tidak tertukar
  dengan "tidak terdeteksi". Bunch yang hanya terdeteksi di satu sisi
  dikeluarkan dari pengukuran, bukan dihitung konsisten.
- **B4 nol** — kelas yang paling penting bagi pertanyaan riset ini sama sekali
  tidak terwakili. Untuk B4, ukuran ini belum memberi apa pun.
- Satu seed, satu arsitektur, satu ambang conf. Ambang 0,25 dipilih sebagai
  default umum, bukan hasil sapuan; sensitivitasnya belum diuji.
- Angka ini **bukan** metrik performa dan tidak sebanding dengan mAP mana pun.

**Dampak** — Menyediakan ukuran ambiguitas yang tidak bergantung label manusia,
dan karena itu dapat dipakai menguji apakah kedalaman **menstabilkan** identitas
lintas-sisi: jalankan skrip yang sama pada checkpoint RGB-D sepadan dan
bandingkan laju inkonsistennya. Itu pertanyaan yang tidak terjawab oleh mAP
agregat, dan kini punya alatnya. Lengan RGB-D menyusul setelah matriks G2
selesai.

**Reproduksi** — `analysis/cross_side_consistency.py --bobot <run>/weights/best.pt
--modal rgb`. Hasil: `experiments/results/E-024/konsistensi_rgb_seed42.json`.

---

## E-025 — Selisih evaluator E-022 terlacak: celah menskala dengan jumlah deteksi (2026-07-31) · menutup gerbang G1

**Konteks** — [AUDIT-E022.md](AUDIT-E022.md) §"Selisih evaluator yang belum
terjelaskan" mencatat celah sampai 0,028 antara `hasil.json` (jalur val internal
trainer) dan `eval_e022_paired.py` (pycocotools), **tidak simetris antar lengan**,
sehingga rerata Δ YOLO26n berubah tanda. Selama itu belum terlacak, tidak ada
angka E-022 yang berstatus final. Empat kandidat didaftar audit: pemilihan
checkpoint, ambang confidence, `max_det`, dan perbedaan daftar citra.

**Hipotesis** — Celah berasal dari `maxDets`: tidak satu pun skrip menyetel
`ev.params.maxDets`, jadi COCOeval memakai default `[1, 10, 100]` sementara
prediksi dibuat dengan `max_det=300`. **Dipalsukan bila** memaksa maxDets=300
tidak mengubah AP.

**Cara** — `eval/diag_evaluator_gap.py`, satu himpunan deteksi dipakai untuk
seluruh pengukuran sehingga tiap sumber celah terisolasi. Checkpoint dilatih
ulang di RTX A4500 (asal: L4), pasangan `yolo26n_rgb_seed42` dan
`yolo26n_rgbd_seed42`, 60 epoch, split test 72 pohon / 288 citra / 504 kotak.

**Hasil**

| | RGB | RGB-D |
|---|---:|---:|
| `hasil.json` mAP50 | 0,36119 | 0,35604 |
| pycocotools mAP50 | 0,34789 | 0,35830 |
| **celah (pycoco − hasil)** | **−0,01330** | **+0,00226** |
| deteksi total | 4.610 | 11.233 |
| rerata deteksi/citra | 16,0 | 39,0 |
| citra dengan >100 deteksi | 0 | 25 |

Konsekuensinya pada arah efek:

| Δ(RGB-D − RGB) | nilai |
|---|---:|
| menurut `hasil.json` | **−0,00515** |
| menurut pycocotools | **+0,01041** |

**Putusan — hipotesis maxDets DIPALSUKAN; celahnya terlacak ke jumlah deteksi.**

1. **maxDets bukan penyebabnya.** Memaksa `maxDets=300` menghasilkan mAP50 dan
   mAP50-95 yang **identik sampai lima desimal** pada kedua lengan. Kandidat ini
   diajukan di G1 lalu digugurkan oleh pengukuran, bukan oleh argumen.
2. **Checkpoint bukan penyebabnya** — terverifikasi, kedua jalur memuat
   `weights/best.pt` yang sama, dan daftar citra identik (satu `test.txt`).
3. **Celahnya menskala dengan jumlah deteksi.** Lengan RGB-D memancarkan
   **2,44× lebih banyak** deteksi (11.233 vs 4.610). Lengan yang deteksinya
   jarang justru **dinaikkan** oleh evaluator internal ultralytics (+0,0133),
   sedangkan lengan yang padat hampir tidak (−0,0023). Asimetrinya 0,0156 —
   cukup untuk **membalik tanda** Δ, dan itu persis yang dilaporkan audit.

**Sifat gejalanya tereproduksi, besarannya tidak.** Audit mencatat celah
+0,0184 dan +0,0282 pada lengan RGB-D di seed 1337/2024 (perangkat L4); di sini
+0,0023 pada seed 42 (A4500). Yang tereproduksi adalah **arah asimetri dan
pembalikan tanda Δ**, bukan angka absolutnya.

**Mekanisme internalnya belum dibuktikan** dan tidak boleh dinarasikan seolah
sudah: yang terukur adalah korelasi celah dengan kepadatan deteksi. Dugaan
paling hemat adalah perbedaan interpolasi kurva PR (ultralytics memakai trapz
atas kurva yang disisipi titik ujung; COCOeval memakai interpolasi 101 titik),
yang perlakuannya terhadap ekor berkeyakinan-rendah memang berbeda. Itu
hipotesis, bukan temuan.

**Dampak — aturan protokol yang mengikat seluruh E-022 dan lanjutannya:**

- **`hasil.json` TIDAK BOLEH dipakai untuk membandingkan antar lengan.**
  Celahnya bukan offset tetap; ia menskala dengan jumlah deteksi, dan jumlah
  deteksi berbeda secara sistematis antar lengan. Membandingkan lengan lewat
  `hasil.json` berarti membandingkan dua metrik yang berbeda.
- **pycocotools adalah protokol tunggal**, sebagaimana sudah berlaku untuk
  E-021. Seluruh evaluasi G2 memakai `eval/eval_e022_pycoco.py` dan
  `eval/eval_e022_paired.py`.
- `hasil.json` tetap berguna sebagai pemantau kemajuan **di dalam satu run**,
  tetapi bukan sebagai angka yang dilaporkan.
- Gerbang G1 **dibuka**: matriks multi-seed G2 boleh dilanjutkan, dengan
  evaluasi terikat protokol di atas.

**Catatan cacat skrip yang ditemukan saat pengerjaan** — versi pertama
`diag_evaluator_gap.py` membaca `ev.stats`, dan `COCOeval.summarize()`
menghitung `stats[0]` dengan `maxDets=100` yang di-hardcode lalu mencari indeks
100 di `params.maxDets`. Begitu maxDets diubah ke `[1,10,300]`, nilai itu tidak
ada dan pycocotools mengembalikan sentinel **−1.0 tanpa error** — persis jenis
kegagalan senyap yang mudah lolos sebagai hasil. Diperbaiki dengan menghitung
langsung dari `ev.eval["precision"]`. Angka di tabel atas berasal dari versi
yang sudah diperbaiki.

**Reproduksi** — `eval/diag_evaluator_gap.py --run <run> --modal <rgb|rgbd>`.
Hasil: `experiments/results/E-022/diag_evaluator_gap_{rgb,rgbd}.json`.

---

## E-026 — Apakah depth menstabilkan identitas lintas-sisi? (2026-07-31) · lanjutan [E-024]

**Hipotesis** — [E-024](#) menetapkan ukuran inkonsistensi prediksi lintas-sisi
yang tidak bergantung label manusia. Pertanyaan yang ia buka: kalau kegagalan
B2/B3 bersifat **fotometrik** (SR-007, SR-009), kedalaman seharusnya **tidak**
menolong; tetapi kalau sebagian ketidakstabilan berasal dari geometri —
tandan yang tampak berbeda karena sudut, oklusi, atau jarak — kanal kedalaman
seharusnya **menurunkan** laju inkonsisten. **Dipalsukan bila** laju
inkonsisten lengan RGB-D tidak dapat dibedakan dari lengan RGB.

**Cara** — `analysis/cross_side_consistency.py` pada pasangan checkpoint
sepadan `yolo26n_rgb_seed42` dan `yolo26n_rgbd_seed42` (60 epoch, seed 42,
konfigurasi identik kecuali kehadiran kanal kedalaman ter-reproyeksi). Split
test 72 pohon. Prediksi lewat jalur evaluator E-022 yang sama, conf 0,25,
IoU pencocokan 0,5. Bootstrap 10.000× atas selisih proporsi.

**Hasil**

| | RGB | RGB-D |
|---|---:|---:|
| Tandan terukur (>= 2 sisi terdeteksi) | 82 | 75 |
| **Laju inkonsisten** | **0,1951** (16/82) | **0,2000** (15/75) |
| Laju kemunculan terlewat | 0,3644 | 0,3883 |
| Tabrakan B1↔B2 | 11 | 8 |
| Tabrakan B2↔B3 | 6 | 6 |
| Tabrakan B1↔B3 | 0 | 1 |

**selisih (RGB-D − RGB) = +0,0049 · CI95 [−0,1194; +0,1314] · P(<0) = 0,457**

**Putusan — DIPALSUKAN.** Kanal kedalaman tidak menurunkan inkonsistensi
prediksi lintas-sisi. Titik estimasinya bahkan bergerak ke arah yang salah
(+0,0049), CI memuat nol dengan lebar, dan peluang depth membantu hanya 0,457 —
tidak dapat dibedakan dari lemparan koin. Laju terlewatnya juga sedikit lebih
buruk (0,3883 vs 0,3644), jadi lengan RGB-D tidak membeli apa pun di sini,
termasuk dalam hal deteksi dasar.

**Konsisten dengan diagnosis yang sudah ada, dan itu penting.** SR-007 dan
SR-009 mendiagnosis kegagalan B2/B3 sebagai **fotometrik**, dan CLAUDE.md
mencatat sejak awal bahwa depth **tidak** akan menolong di sana. Tabrakan yang
terukur di sini memang terkonsentrasi pada tetangga ordinal B1↔B2 dan B2↔B3 —
persis kelas yang kegagalannya fotometrik. **Hasil negatif ini adalah
konfirmasi teori, bukan kegagalan eksperimen**, dan harus dilaporkan begitu.

**Yang tidak boleh dihaluskan:**

- **n kecil** (82 dan 75 tandan), sehingga CI selebar ±0,12 memang wajar. Uji
  ini **tidak berdaya** mendeteksi efek kecil; "tidak terbukti" bukan "terbukti
  tidak ada".
- **B4 nol terwakili di kedua lengan.** Kelas yang justru paling geometris —
  dan karenanya paling mungkin dibantu depth — tidak masuk pengukuran sama
  sekali karena tidak pernah terdeteksi di >= 2 sisi. **Untuk B4, hipotesis ini
  belum diuji, bukan dipalsukan.** Ini batas terpenting entri ini.
- Satu seed, satu arsitektur kecil (2,57 jt param). E-022/SR-015 menemukan
  kandungan informasi depth baru terpakai pada kapasitas tinggi (RT-DETR-L
  33,0 jt); ukuran ini belum dijalankan di sana.
- Ambang conf 0,25 belum disapu; jumlah tandan terukur bergantung padanya.

**Dampak** — Menambah satu bukti independen pada kesimpulan E-022: fusi awal
4-kanal tidak membeli apa pun pada model kecil, kini juga terlihat pada ukuran
yang sama sekali berbeda dari mAP. Ukuran ini menjadi **instrumen tambahan
untuk G4/G6**: bila fusi menengah atau akhir benar-benar bekerja, laju
inkonsisten harus turun — dan bila tidak turun, kenaikan mAP apa pun di sana
patut dicurigai sebagai efek kapasitas. Jalankan juga pada RT-DETR-L begitu
matriks G2 selesai, karena di situlah depth terbukti membawa informasi B4.

**Reproduksi** — `analysis/cross_side_consistency.py --bobot <run>/weights/best.pt
--modal <rgb|rgbd>`. Hasil: `experiments/results/E-024/konsistensi_{rgb,rgbd}_seed42.json`.

---

## E-027 — Matriks multi-seed YOLO26n, protokol beku: depth MERUGIKAN (2026-08-01) · menutup G2 bagian YOLO26n

**Konteks** — [E-022](EKSPERIMEN.md) dicabut karena bertumpu satu seed, dan
[AUDIT-E022.md](AUDIT-E022.md) menyatakan matriks multi-seed "sedang diproduksi".
Matriks itu tidak pernah selesai maupun diarsipkan. Entri ini menyelesaikannya
untuk YOLO26n: 12 run (4 modal × 3 seed), 60 epoch, kode `_fix`, seluruhnya
dievaluasi lewat pycocotools sesuai aturan mengikat [E-027 pendahulunya, E-025].

**Hipotesis** — H-022 asli: kanal depth sensor ter-reproyeksi menaikkan test
mAP50 dengan delta > +0,015 dan CI bootstrap berpasangan per-pohon tidak memuat
nol. Dipalsukan pula bila kontrol derau memberi kenaikan sebanding.

**Cara** — `shell/matriks_g2.sh` (kolam slot paralel, dapat dilanjutkan,
dijaga `periksa_run`) lalu `shell/eval_g2.sh` (bootstrap 2000× per pohon,
protokol tunggal pycocotools). Split test 72 pohon / 288 citra / 504 kotak.
Perangkat RTX A4500; angka asal E-022 diproduksi di L4.

**Hasil — 12 perbandingan berpasangan**

| Perbandingan | seed 42 | seed 1337 | seed 2024 | rerata |
|---|---:|---:|---:|---:|
| depth − RGB | +0,0104 | **−0,0414** | **−0,0379** | **−0,0230** |
| DERAU − RGB | +0,0032 | +0,0011 | **−0,0443** | −0,0133 |
| depth − derau | +0,0072 | **−0,0425** | +0,0064 | −0,0096 |
| depth − tukar | +0,0190 | −0,0272 | −0,0042 | −0,0041 |

Angka tebal = CI95 bootstrap tidak memuat nol. mAP50 lengan RGB per seed:
0,3479 / 0,3428 / 0,3749 — **rentang antar-seed 0,0321 pada satu lengan yang
konfigurasinya identik.**

**Putusan — H-022 DIPALSUKAN, dan lebih keras daripada sebelumnya.**

1. **Depth merugikan, bukan sekadar netral.** Rerata −0,0230, dan pada DUA dari
   tiga seed CI-nya tidak memuat nol dengan tanda NEGATIF (seed 1337
   [−0,073; −0,015], seed 2024 [−0,069; −0,001]). Kesimpulan lama "tidak dapat
   dibedakan dari nol" terlalu lunak untuk YOLO26n.
2. **Seed 42 terkonfirmasi sebagai seed paling menguntungkan.** Ia satu-satunya
   yang positif (+0,0104), persis peringatan yang ditulis saat pencabutan
   E-022. Melaporkan seed tunggal di sini akan membalik kesimpulan.
3. **Temuan "derau mengalahkan depth" TIDAK TEREPRODUKSI.** Pada seed-42 lama
   derau memberi +0,0437 dengan CI tidak memuat nol — satu-satunya delta
   signifikan di seluruh E-022. Di matriks bersih ini derau justru netral
   sampai merugikan (+0,0032 / +0,0011 / −0,0443, rerata −0,0133). Klausa
   SR-015 yang bersandar pada temuan itu kehilangan pijakan.
4. **Registrasi tetap tidak membeli apa pun.** depth − tukar rerata −0,0041,
   CI memuat nol di dua dari tiga seed. Reproyeksi penuh yang terbukti lebih
   selaras di E-022a tetap tidak diterjemahkan menjadi mAP pada model kecil —
   konsisten dengan putusan lama.

**Yang tidak boleh dihaluskan:**

- **CI lintas-seed sangat lebar.** Dengan n=3, CI-t rerata depth−RGB adalah
  [−0,0949; +0,0490] — memuat nol meski seluruh titik estimasinya negatif.
  Yang kuat di sini adalah **arah yang konsisten dan dua CI per-seed yang
  signifikan**, bukan rerata tiga angkanya.
- **Lantai derau antar-seed 0,0321** pada lengan RGB saja. Seluruh delta yang
  diperdebatkan (±0,04) berada pada orde yang sama dengan varians seed. Ini
  menegaskan kembali peringatan pencabutan E-022, sekarang dengan angkanya.
- **Perangkat berbeda** dari run asal (A4500 vs L4). Besaran tidak dapat
  disamakan langsung dengan angka E-022 lama; yang dibandingkan adalah pola.
- Berlaku untuk **YOLO26n saja** (2,57 jt param). Matriks RT-DETR-L berjalan
  terpisah, dan G7 menyapu YOLO26m/l untuk memisahkan kapasitas dari
  arsitektur — klaim struktural SR-015 belum diuji ulang di sini.

**Dampak** — Bagian YOLO26n pada G2 selesai dan buktinya terarsip
(`paired_yolo26n_*_seed*.json`, 12 berkas), menutup celah keterlacakan yang
ditinggalkan audit. Untuk model kecil, arah bukti kini melawan fusi awal secara
lebih tegas: bukan "tidak terbukti membantu" melainkan "terukur merugikan pada
mayoritas seed". Itu memperkuat, bukan melemahkan, alasan menempuh fusi
menengah/akhir (G4/G6).

**Reproduksi** — `shell/matriks_g2.sh` lalu `shell/eval_g2.sh`. Hasil:
`experiments/results/E-022/paired_yolo26n_{depth_vs_rgb,derau_vs_rgb,depth_vs_derau,depth_vs_tukar}_seed{42,1337,2024}.json`.

---

## E-028 — Inkonsistensi lintas-sisi di SawitMVC: daya uji 6× dan B4 akhirnya terwakili (2026-08-01) · lanjutan [E-024]/[E-026] · [SR-016](SR/SR-016-konsistensi-lintas-sisi.md)

**Konteks** — [E-024](EKSPERIMEN.md) mengukur inkonsistensi prediksi lintas-sisi
sebesar 19,5% pada SawitMVC-Depth, dan [E-026](EKSPERIMEN.md) menemukan depth
tidak menstabilkannya. Keduanya menandai batas yang sama: hanya **82 tandan
terukur**, dan **B4 nol terwakili** karena tidak pernah terdeteksi di ≥ 2 sisi.
B4 adalah kelas yang kegagalannya geometris, jadi justru itu yang paling perlu
diukur. SawitMVC punya 18.540 kotak vs 2.299 dan 4–8 sisi per pohon.

**Hipotesis** — Ukuran yang sama pada dataset yang jauh lebih besar akan (a)
memberi CI yang cukup sempit untuk dipecah per kelas, dan (b) menempatkan
tabrakan pada tetangga ordinal, dengan **B2↔B3 sebagai pasangan dominan** —
karena SR-007 dan SR-009 mendiagnosis ambiguitas kematangan justru di sana.
**Dipalsukan bila** tabrakan tersebar tanpa struktur ordinal, atau B2↔B3 bukan
pasangan terbesar.

**Cara** — `analysis/cross_side_consistency.py --data-root /workspace/SawitMVC/data
--split-dir experiments/splits/rgb/sawitmvc`. Detektor `yolo26n` dilatih
di SawitMVC dengan resep **identik** lengan RGB SawitMVC-Depth (60 epoch, imgsz
640, batch 16, seed 42, HSV mati) supaya kedua laju sebanding. Split E-021
terarsip: 716/96/141 pohon, irisan nol. Test = 141 pohon.

**Hasil**

| | SawitMVC-Depth (E-024) | **SawitMVC (E-028)** |
|---|---:|---:|
| Tandan fisik | 310 | **1.404** |
| Tampak ≥ 2 sisi | 182 | **1.022** |
| Terukur | 82 | **511** (6,2×) |
| **Laju inkonsisten** | **0,1951** | **0,2329** |
| Laju terlewat | 0,3644 | 0,3336 |

Selisih +0,0378, CI95 bootstrap [−0,0585; +0,1276] — **kedua dataset tidak dapat
dibedakan** pada ukuran ini, meski prior kelas, resolusi, dan orientasinya
berbeda jauh.

Per kelas, dengan CI Wilson — **B4 akhirnya terwakili**:

| Kelas | Laju inkonsisten | CI95 |
|---|---:|---|
| B1 | 0,2346 (19/81) | [0,156; 0,338] |
| **B2** | **0,4340 (46/106)** | [0,344; 0,529] |
| B3 | 0,1552 (43/277) | [0,117; 0,203] |
| B4 | 0,2340 (11/47) | [0,136; 0,372] |

Pasangan kelas yang bertabrakan: **B2↔B3 sebanyak 79**, B1↔B2 32, B3↔B4 25,
B1↔B3 12. **Tidak ada satu pun B1↔B4** — tabrakan yang melompati tiga tingkat
ordinal.

**Putusan — DIKONFIRMASI.** Struktur ordinalnya jelas dan kuat: tabrakan
terkonsentrasi pada tetangga langsung, meluruh dengan jarak ordinal
(79 → 32/25 → 12 → 0), dan **B2↔B3 adalah pasangan dominan** persis seperti
yang diprediksi SR-007/SR-009. Ini diperoleh **tanpa memakai label kematangan
sebagai kebenaran**, hanya identitas fisik tandan — jadi ia menguatkan diagnosis
ambiguitas B2/B3 lewat jalur bukti yang sepenuhnya berbeda dari mAP per kelas.

**B2 adalah kelas paling ambigu, bukan B4.** Laju inkonsisten B2 (0,434) hampir
tiga kali B3 (0,155) dan CI-nya tidak beririsan. Itu temuan baru: sampai sekarang
B4 selalu diperlakukan sebagai kelas bermasalah karena AP50-nya terendah, tetapi
AP rendah mencampur *kegagalan deteksi* dengan *kebingungan kelas*. Ukuran ini
memisahkan keduanya, dan begitu dipisah, B4 justru **tidak lebih ambigu daripada
B1** (0,234 vs 0,235) — kesulitan B4 memang soal menemukannya, bukan
menamainya.

**Yang tidak boleh dihaluskan:**

- **SawitMVC tanpa depth.** E-028 hanya laju BASELINE. Pertanyaan "apakah depth
  menstabilkan" tetap hanya terjawab di SawitMVC-Depth, dan di sana sudah
  dipalsukan (E-026).
- **Laju terlewat 33,4%** — sepertiga kemunculan tidak masuk pengukuran.
  Detektor yang lebih kuat akan mengubah komposisi tandan terukur, dan arah
  perubahannya tidak dapat diprediksi dari sini.
- **B4 n=47**, CI-nya masih lebar [0,136; 0,372]. Cukup untuk menyatakan B4
  tidak menonjol ambigu, belum cukup untuk memberi angka presisi.
- Satu seed, satu arsitektur kecil, ambang conf 0,25 belum disapu.
- Angka ini bukan metrik performa dan tidak sebanding dengan mAP mana pun.

**Dampak** — Menyediakan pembanding baseline berdaya uji layak untuk G4/G6:
bila fusi menengah/akhir bekerja, laju inkonsisten harus turun dari 0,2329, dan
penurunannya harus terkonsentrasi di B2↔B3 kalau mekanismenya fotometrik atau
di B3↔B4 kalau geometris. Ukuran ini kini bisa membedakan keduanya — sesuatu
yang mAP agregat tidak pernah bisa.

**Reproduksi** — `shell/g8_sawitmvc.sh`. Hasil:
`experiments/results/E-028/konsistensi_sawitmvc_rgb_seed42.json`.

---

## E-029 — Matriks multi-seed RT-DETR-L: klausa "depth terpakai pada kapasitas tinggi" DICABUT (2026-08-01) · melengkapi G2

**Konteks** — [SR-015](SR/SR-015-depth-sensor-4kanal.md) menyisakan satu klausa
positif setelah pencabutan 30 Juli: *"kandungan informasi depth NYATA pada model
besar"*, bersandar pada RT-DETR-L seed-42 depth − derau **+0,0365** dengan
**B4 +0,1001 [+0,0062; +0,1618]** signifikan. Lengan derau pembandingnya dibuat
dengan kode cacat (RNG bersama, AUDIT-E022 #4). [E-027](EKSPERIMEN.md) sudah
menunjukkan temuan sejenis gugur pada YOLO26n. Entri ini mengujinya pada
arsitektur yang melahirkannya.

**Hipotesis** — Bila klausa itu benar, depth − derau pada RT-DETR-L harus tetap
positif **dan** signifikan setelah kode diperbaiki, dengan kenaikan terkonsentrasi
di B4. **Dipalsukan bila** CI memuat nol, atau efeknya lebih kecil daripada
sebaran antar-seed.

**Cara** — 9 run (3 modal × 3 seed), 60 epoch, kode `_fix`, protokol tunggal
pycocotools ([E-025]), bootstrap 2000× per pohon. Split test 72 pohon / 288
citra / 504 kotak. Perangkat A4500.

**Hasil**

| Perbandingan | seed 42 | seed 1337 | seed 2024 | rerata | sd |
|---|---:|---:|---:|---:|---:|
| depth − RGB | −0,0350 | +0,0091 | **+0,0702** | +0,0148 | 0,0431 |
| DERAU − RGB | **−0,0533** | −0,0063 | **+0,0667** | +0,0024 | 0,0494 |
| depth − derau | +0,0183 | +0,0153 | +0,0035 | **+0,0124** | **0,0064** |

Tebal = CI95 bootstrap tidak memuat nol. mAP50 lengan RGB per seed: 0,4282 /
0,4142 / 0,3523 — **rentang antar-seed 0,0759 pada satu lengan berkonfigurasi
identik.**

**Putusan — klausa SR-015 DICABUT.**

1. **depth − derau kehilangan signifikansi di ketiga seed.** +0,0183 / +0,0153 /
   +0,0035, semuanya CI memuat nol. Angka lama +0,0365 menyusut menjadi rerata
   **+0,0124**, dan B4 +0,1001 yang menjadi tulang punggung klausa itu tidak
   direproduksi.
2. **Sebaran antar-seed mengubur efeknya.** Lengan RGB saja berayun 0,0759
   antar seed — **enam kali** rerata depth − derau. Setiap klaim sebesar ±0,04
   pada dataset ini tidak dapat dipertahankan tanpa multi-seed.
3. **Arah depth − RGB tidak stabil**: −0,0350 (seed 42) sampai +0,0702 (seed
   2024), keduanya dengan CI yang tidak memuat nol tetapi **bertanda
   berlawanan**. Dua seed yang sama-sama "signifikan" menunjuk arah berbeda —
   demonstrasi paling telanjang mengapa seed tunggal tidak cukup.

**Satu pola yang bertahan, dan ini yang menarik.** Di antara ketiga kontras,
hanya **depth − derau** yang punya sd kecil (0,0064 versus 0,0431 dan 0,0494).
CI-t lintas-seed-nya [−0,0071; +0,0318] — nyaris tidak memuat nol meski n=3.
Tafsir yang hemat: **isi kanal ke-4 berpengaruh lebih konsisten daripada
keberadaan kanal itu sendiri.** Menambahkan kanal keempat mengguncang pelatihan
secara besar dan tak terarah; mengganti isinya dari derau ke depth memberi
perbaikan kecil tetapi berulang. Itu tidak menyelamatkan fusi awal — +0,0124
jauh di bawah ambang +0,015 yang ditetapkan H-022 — tetapi ia mendukung premis
E-023: informasi depth ada, salurannya yang salah.

**Yang tidak boleh dihaluskan:**

- **n = 3 seed.** CI-t depth − derau [−0,0071; +0,0318] tetap memuat nol.
  "Nyaris signifikan" bukan signifikan, dan tidak boleh dilaporkan sebagai
  temuan positif.
- Pola sd-kecil di atas adalah **pengamatan pasca-hoc**, bukan hipotesis yang
  ditulis sebelum melihat data. Ia layak diuji terpisah di E-023, bukan
  dijadikan kesimpulan di sini.
- Perangkat A4500, bukan L4 asal; besaran tidak sebanding langsung dengan angka
  E-022 lama, yang dibandingkan adalah pola.
- Berlaku untuk fusi AWAL 4-kanal pada RT-DETR-L. Fusi menengah/akhir belum
  diuji sama sekali.

**Dampak** — Bersama [E-027](EKSPERIMEN.md), seluruh klaim positif E-022 kini
tercabut pada kedua arsitektur: tidak ada satu pun kontras yang bertahan
signifikan lintas tiga seed. G2 selesai, dan basis buktinya bersih untuk
pertama kalinya. Arah G4/G6 (fusi menengah/akhir) tetap berdiri — bukan karena
fusi awal menjanjikan, melainkan karena ia sekarang dipalsukan secara meyakinkan
pada dua arsitektur dan tiga seed.

**Reproduksi** — `shell/matriks_g2.sh` lalu `ARCH=rtdetr-l shell/eval_g2.sh`.
Hasil: `experiments/results/E-022/paired_rtdetr-l_*_seed{42,1337,2024}.json`.

---

## E-030 — Sapuan kapasitas YOLO26 n→m→l: klaim "kapasitas" SR-015 harus dipersempit (2026-08-01) · G7

**Konteks** — SR-015 menyimpulkan *"arah efek kanal ke-4 ditentukan **kapasitas
model**, bukan isi kanal"*, berdasar lompatan YOLO26n (2,57 jt) → RT-DETR-L
(33,0 jt). Lompatan itu mengubah **kapasitas dan arsitektur sekaligus**, jadi
kata "kapasitas" belum terisolasi. Diminta pengguna 1 Agustus; YOLO26m (21,9 jt)
dan YOLO26l (26,3 jt) mengisi celah **di dalam satu keluarga arsitektur**.

**Hipotesis** — Bila kapasitas yang menentukan, pola depth-vs-derau harus
berubah secara monoton sepanjang 2,57 → 21,9 → 26,3 → 33,0 jt. **Dipalsukan
bila** YOLO26m dan YOLO26l berperilaku seperti YOLO26n meski kapasitasnya
mendekati RT-DETR-L — itu menunjukkan pembedanya arsitektur.

**Cara** — 6 run baru (2 arsitektur × 3 modal), seed 42, 60 epoch, imgsz 640,
batch 8, resep identik lengan E-022. Evaluasi protokol tunggal pycocotools
([E-025]), bootstrap 2000× per pohon. `shell/sapuan_kapasitas.sh`.

**Hasil — seluruh keluarga pada seed 42**

| Model | Param | depth − RGB | DERAU − RGB | depth − derau |
|---|---:|---:|---:|---:|
| YOLO26n | 2,57 jt | +0,0104 | +0,0032 | +0,0072 |
| YOLO26m | 21,9 jt | −0,0086 | +0,0184 | −0,0270 |
| **YOLO26l** | **26,3 jt** | +0,0054 | **−0,0325** | **+0,0379** |
| RT-DETR-L | 33,0 jt | −0,0350 | **−0,0533** | +0,0183 |

Tebal = CI95 tidak memuat nol. Metrik lengkap YOLO26l (seed 42): lengan rgbd
**unggul di keempat metrik sekaligus** — mAP50 0,3612 vs rgb 0,3557, mAP50-95
0,1299 vs 0,1207, precision 0,605 vs 0,569, recall 0,520 vs 0,482 — sementara
derau terburuk (0,3232, recall anjlok ke 0,385).

**Putusan — DIKONFIRMASI SEBAGIAN; klaim SR-015 harus DIPERSEMPIT.**

Yang bertahan: **kolom DERAU − RGB berubah tanda secara monoton menurut
kapasitas.** +0,0032 → +0,0184 → **−0,0325** → **−0,0533**, dan dua nilai
terbesar signifikan. Kanal ke-4 tanpa informasi **membantu** model kecil dan
**merugikan** model besar, persis mekanisme yang ditafsirkan SR-015 (regularisasi
pada model undertrained versus gangguan pada stem pratlatih). Titik baliknya kini
terukur: **antara 21,9 dan 26,3 jt parameter.**

Yang **tidak** bertahan: kolom depth − derau **tidak monoton** (+0,0072 →
−0,0270 → +0,0379 → +0,0183). YOLO26m menyimpang dari tren, dan tidak satu pun
dari keempatnya signifikan. Jadi kalimat "arah efek kanal ke-4 ditentukan
kapasitas" hanya benar untuk **kanal tanpa informasi**; untuk selisih
depth-versus-derau — bagian yang menyangkut apakah kedalaman membawa informasi —
kapasitas **tidak** menjelaskannya.

**Rumusan yang didukung bukti, menggantikan yang lama:**

> Kapasitas model menentukan apakah **menambahkan kanal keempat** menolong atau
> merugikan, dengan titik balik antara 21,9 dan 26,3 jt parameter. Kapasitas
> **tidak** menentukan apakah **mengisi kanal itu dengan kedalaman** lebih baik
> daripada mengisinya dengan derau.

**Yang tidak boleh dihaluskan:**

- **Satu seed.** E-027 dan E-029 sudah menunjukkan sebaran antar-seed 0,032–0,076
  pada dataset ini — lebih besar daripada sebagian besar selisih di tabel atas.
  Monotonisitas kolom DERAU − RGB **belum diuji multi-seed**, dan sampai itu
  dilakukan ia adalah pola yang menarik, bukan temuan mapan.
- Hanya kolom DERAU − RGB yang punya dua nilai signifikan; sembilan sel lainnya
  CI-nya memuat nol.
- Keunggulan empat-metrik YOLO26l rgbd bersandar pada satu run tunggal.
- Perangkat A4500; berlaku untuk fusi AWAL 4-kanal pada SawitMVC-Depth.

**Dampak** — Mengubah dasar pemilihan arsitektur untuk E-023. Alasan memakai
model besar bukan lagi "di situ depth terbukti membawa informasi" (dicabut
[E-029]), melainkan yang lebih spesifik: **pada model besar, kerugian menambah
kanal keempat paling parah** — dan justru itu yang seharusnya dihapus oleh fusi
menengah/akhir, karena keduanya tidak menyentuh stem 3-kanal berbobot pratlatih.
G7 dengan demikian mempertajam prediksi yang akan diuji G4/G6, bukan sekadar
menambah baris tabel.

**Reproduksi** — `shell/sapuan_kapasitas.sh`, lalu `ARCH=yolo26m|yolo26l
SEEDS=42 shell/eval_g2.sh`. Hasil: `experiments/results/E-022/paired_yolo26{m,l}_*_seed42.json`,
metrik lengkap di `metrics_lengkap.json`.

---

## E-031 — Varians SPLIT vs varians SEED (2026-08-01) · G5, menutup SR-015 §7

**Konteks** — [SR-015](SR/SR-015-depth-sensor-4kanal.md) §7 mencatat *"varians
split belum diukur; 3-fold CV yang direncanakan tidak dijalankan"* — satu-satunya
keterbatasan E-022 yang belum tersentuh setelah [E-027]/[E-029]/[E-030] menutup
varians seed.

Dua sumber varians ini sering tertukar, dan pemisahannya menentukan:

| | Yang divariasikan | Yang diukur |
|---|---|---|
| E-027 | RNG pelatihan, split tetap | keacakan optimisasi |
| **E-031** | **split**, RNG tetap 42 | ketergantungan pada pohon mana yang jatuh di test |

**Hipotesis** — Bila kesimpulan E-022 kokoh terhadap pemilihan pohon, Δ(RGB-D −
RGB) harus stabil lintas split. **Dipalsukan bila** rentang Δ antar-split
sebanding atau melebihi efek yang diperdebatkan sepanjang E-022 (±0,02–0,04).

**Cara** — Dua split baru (`splits_depth/seed1`, `seed2`) dari
`build/make_splits_depth.py`, stratifikasi dan rasio identik seed42: 245/35/72
pohon, irisan nol. YOLO26n rgb + rgbd per split, 60 epoch, **RNG pelatihan tetap
42**, resep identik. Evaluasi pycocotools, bootstrap 2000× per pohon, tiap model
dinilai pada test split-nya sendiri.

**Hasil**

| Split | RGB | RGB-D | Δ | CI95 |
|---|---:|---:|---:|---|
| seed42 | 0,3479 | 0,3583 | +0,0104 | [−0,0246; +0,0397] |
| seed1 | 0,3137 | 0,3204 | +0,0067 | [−0,0351; +0,0450] |
| seed2 | 0,2991 | 0,3384 | **+0,0393** | **[+0,0059; +0,0665]** |

| Sumber varians | Lengan RGB | Δ(RGB-D − RGB) |
|---|---:|---:|
| **Split** (E-031, RNG tetap) | rentang **0,0488** · sd 0,0205 | rentang 0,0326 · sd 0,0146 |
| **Seed** (E-027, split tetap) | rentang 0,0321 | rentang 0,0518 |

**Putusan — varians split NYATA dan lebih besar daripada varians seed pada
performa absolut.** Lengan RGB berayun **0,0488** antar split — lebih lebar
daripada 0,0321 antar seed, dan **hampir 5× lipat** ambang +0,015 yang
ditetapkan H-022 sebagai kriteria keberhasilan depth. Kesimpulan yang mengikat:
**tidak ada angka mAP absolut pada dataset ini yang bermakna tanpa menyebut
split-nya.**

**Tetapi arah Δ justru lebih stabil terhadap split daripada terhadap seed.**
Ketiga split memberi Δ **positif** (+0,0104 / +0,0067 / +0,0393, rerata +0,0188,
sd 0,0146), sementara ketiga seed memberi tanda **berlawanan** (+0,0104 /
−0,0414 / −0,0379, sd 0,0289). Rasio sd-nya 1 : 2. Itu berlawanan dengan dugaan
yang wajar — orang mengira pemilihan pohon lebih mengguncang daripada RNG.

**Tafsir yang hemat, dan batasnya.** Pola ini konsisten dengan gagasan bahwa
selisih berpasangan **saling menghapus** komponen kesulitan split (kedua lengan
menghadapi pohon test yang sama) tetapi **tidak** menghapus lintasan optimisasi
(kedua lengan punya lintasan berbeda meski seed sama, karena arsitekturnya
berbeda satu kanal). Kalau benar, maka **menambah seed lebih berharga daripada
menambah split** untuk menguji klaim depth — dan itu justru kebalikan dari yang
direncanakan sebagai "3-fold CV" di SR-015. **Ini hipotesis dari n=3 lawan n=3;
belum diuji, dan tidak boleh dipakai sebagai dasar merancang E-023 tanpa
verifikasi.**

**Yang tidak boleh dihaluskan:**

- **n = 3 split** dan **n = 3 seed**. Membandingkan dua sd dari sampel sekecil
  itu tidak punya daya uji; rasio 1 : 2 dapat berbalik dengan mudah.
- Hanya **satu arsitektur** (YOLO26n) dan **satu kontras** (depth vs RGB).
  Kontrol derau dan tukar tidak dijalankan lintas split.
- split2 satu-satunya yang CI-nya tidak memuat nol (+0,0393). Dengan tiga split,
  satu hasil signifikan adalah yang diharapkan muncul secara kebetulan pada
  α=0,05 kira-kira 14% waktu — **bukan bukti**.
- Perangkat A4500; fusi AWAL 4-kanal; SawitMVC-Depth.

**Dampak** — Menutup keterbatasan terakhir SR-015 §7. Aturan pelaporan yang kini
berlaku: **setiap angka mAP pada dataset ini wajib menyebut split**, karena
rentang antar-split (0,0488) melampaui hampir semua efek yang pernah
diperdebatkan di E-022. Untuk G4/G6, prioritas replikasi adalah **seed lebih
dulu, split kemudian** — dengan catatan bahwa dasar prioritas itu sendiri masih
hipotesis.

**Reproduksi** — `build/make_splits_depth.py --seed 1 --seed 2`, lalu
`train_depth4ch.py --split seed{1,2}`, lalu `eval_e022_paired.py --split-dir
splits_depth/seed{1,2}`. Hasil: `experiments/results/E-022/paired_yolo26n_depth_vs_rgb_split{1,2}.json`.

---

## E-032 — Titik fusi RGB-D: awal vs menengah vs akhir, semua dari nol (2026-08-01) · G4, G6

**Hipotesis** — E-022 menguji fusi hanya pada satu titik: konkatenasi 4-kanal di
masukan. Kalau kegagalannya disebabkan TITIK fusi (depth dipaksa masuk sebelum
jaringan sempat membentuk fitur), memindahkan fusi lebih dalam harus menolong.
Dua alternatif diuji sejajar: fusi MENENGAH (cabang depth ringan sampai P2/4,
digabung sebelum P3) dan fusi AKHIR (dua backbone penuh, digabung di P3/P4/P5).

**Metode** — 5 lengan x 3 seed = 15 run, seluruhnya YOLO26 skala n, 150 epoch,
imgsz 640, batch 16, split SawitMVC-Depth seed42, **tanpa bobot pratlatih**.

Dari nol untuk SEMUA lengan, termasuk baseline RGB. Bukan penghematan — justru
3x lebih mahal — melainkan karena arsitektur dua cabang lahir dari YAML kustom
dan tidak punya checkpoint COCO yang cocok. Membandingkan fusi-dari-nol dengan
lengan pratlatih akan mengukur ada-tidaknya pralatihan, bukan titik fusi.

150 epoch, bukan 60: dari nol dengan 980 citra latih, 60 epoch underfit dan
hasil rendahnya akan salah dibaca sebagai "fusi gagal".

Lengan `derau` (kanal ke-4 berisi derau) WAJIB per SR-015 §6 — tanpanya kenaikan
apa pun tidak dapat dipisahkan dari efek menambah kapasitas.

Evaluasi: pycocotools, bootstrap berpasangan 2000x pada tingkat POHON (72 pohon,
288 citra uji). `hasil.json` trainer tidak dipakai [E-025].

**Kriteria ditetapkan SEBELUM hasil dibaca** (`eval/ringkas_e023.py`):
berbeda dari baseline = 3/3 seed sepakat tanda DAN tidak ada CI yang memuat nol;
indikasi = tanda sepakat tetapi ada CI memuat nol; selain itu = tidak berbeda.

**Hasil — Δ mAP50 terhadap baseline RGB seed yang sama**

| lengan | seed 42 | seed 1337 | seed 2024 | rerata | rentang | putusan |
|---|---|---|---|---|---|---|
| awal  | -0,0120 | +0,0234 | -0,0017 | +0,0032 | 0,0354 | tidak berbeda |
| mid   | +0,0096 | +0,0212 | +0,0110 | +0,0139 | 0,0116 | **indikasi** |
| late  | -0,0056 | +0,0070 | +0,0102 | +0,0039 | 0,0158 | tidak berbeda |
| derau | -0,0130 | +0,0025 | -0,0081 | -0,0062 | 0,0155 | tidak berbeda |

Seluruh 12 CI95 memuat nol. Tidak ada satu pun lengan yang lolos ambang
"berbeda"; `mid` satu-satunya yang tandanya sepakat di tiga seed.

**Tiga pembacaan, berurut dari yang paling didukung bukti**

1. **Efek titik fusi lebih kecil daripada derau seed.** Rentang antar-seed
   `awal` (0,0354) melampaui SELURUH selisih titik yang terukur di tabel ini.
   Pada 2,57 jt param dengan 980 citra dari nol, memindahkan titik fusi tidak
   menghasilkan efek yang dapat dipisahkan dari pemilihan seed.

2. **Fusi AKHIR tidak menolong meski menambah parameter paling banyak** (3,00 jt
   vs 2,51 jt `mid` vs 2,57 jt `awal`). Ini menjawab G6: dua backbone penuh,
   ~17% parameter tambahan, nol perbaikan yang dapat dibedakan.

3. **`mid` konsisten positif tetapi belum boleh disebut temuan.** Rentangnya
   paling sempit (0,0116) dan reratanya tertinggi (+0,0139), unggul +0,0201 atas
   kontrol derau. Itu pola yang diharapkan bila fusi menengah benar-benar
   bekerja — tetapi ketiga CI-nya memuat nol, dan dengan 4 lengan diuji, satu
   lengan bertanda sepakat 3/3 secara kebetulan bukan kejadian langka.

**Keterbatasan**

- **Satu skala (n), satu arsitektur (YOLO26), satu split.** E-030 menunjukkan
  arah efek kanal ke-4 berubah dengan kapasitas; E-031 menunjukkan varians split
  (0,0488) melampaui hampir semua efek di sini. Kesimpulan ini terikat pada
  yolo26n/split-seed42 dan TIDAK boleh digeneralkan.
- **Semua lengan dari nol.** Tidak menjawab apakah fusi menengah menolong ketika
  cabang RGB dapat memakai bobot pratlatih — konfigurasi yang justru paling
  mungkin dipakai di praktik.
- **72 pohon.** CI selebar +-0,03 adalah konsekuensi langsung ukuran uji ini,
  bukan kelemahan metode.
- Baseline seed 42 (0,3164) jauh di atas seed 1337 (0,2944) dan 2024 (0,2952).
  Seluruh lengan tampak "naik" pada dua seed terakhir sebagian karena
  baselinenya rendah — alasan tambahan untuk tidak membaca kolom per seed
  sendirian.

**Dampak** — Menutup G4 dan G6. Untuk SR-015: klaim "kanal ke-4 tidak menolong
pada kapasitas kecil" kini berlaku juga ketika fusi dipindah ke P2/4 dan
P3/P4/P5, bukan hanya di masukan — jadi penjelasan "titik fusi salah" GUGUR
sebagai kandidat penyebab. Yang tersisa sebagai kandidat: kapasitas (E-030),
kualitas depth itu sendiri, dan ukuran data.

Arah yang layak berikutnya, dan hanya jika ada alasan lain untuk melanjutkan:
`mid` pada yolo26m/l, di mana E-030 menunjukkan isi kanal ke-4 mulai penting.

**Catatan operasional** — Penjaga "lewati bila berkas hasil sudah ada" TIDAK
mencegah peluncuran ganda: hasil ditulis di akhir, jadi driver meluncurkan
salinan kedua `awal_seed2024` 20 menit setelah yang pertama mulai. Membunuh
induknya juga tidak cukup — 12 pekerja ProcessPoolExecutor menjadi yatim dan
terus berjalan. Yang dibutuhkan kunci berbasis proses (`flock` pada penanda saat
MULAI), bukan pemeriksaan keberadaan hasil.

**Reproduksi** — `shell/e023_fusi.sh` (seed 42, 1337) dan `shell/e023_seed2024.sh`,
lalu `shell/eval_e023_par.sh`, lalu `eval/ringkas_e023.py`. Bukti:
`experiments/results/E-023/paired_{awal,mid,late,derau}_vs_rgb_seed{42,1337,2024}.json`;
kurva latihan + hash bobot 15 run di direktori yang sama.
## E-033 — Rentang metrik kanal depth: 0,3/8,0 (salah) vs 0,8/15,0 (terkalibrasi) (2026-08-06) · SR-015

**Hipotesis** — `fourch.Z_NEAR/Z_FAR` di jalur produksi masih 0,3/8,0, sedangkan
E-022 memilih 0,8/15,0 dari histogram split train. Rentang yang salah membuang
sebagian besar jangkauan kanal: pada 60 citra train terukur entropi **6,190 bit
vs 7,627 bit**, median level **23 vs 72** dari 255, dan **10,22% vs 0,40%**
piksel mentok di level 1. Kalau kerugian informasi sebesar itu berdampak pada
deteksi, lengan z08 harus mengalahkan lengan z03 secara konsisten.

Ini menguji satu kandidat penyebab yang MASIH TERBUKA di SR-015 §7b setelah
titik fusi dicoret: **kualitas kanal depth itu sendiri**.

**Yang akan memalsukan** (ditetapkan sebelum satu angka pun dibaca):
- **DIPALSUKAN** (rentang tidak berdampak) bila |Δ mAP50| ≤ 0,015 pada ketiga
  arsitektur, ATAU tanda Δ tidak konsisten antar arsitektur.
- **DIKONFIRMASI** bila tanda Δ konsisten (z08 > z03) pada ketiga arsitektur
  DAN sekurang-kurangnya satu CI95 tidak memuat nol.
- Selain itu = **INDIKASI**.

**Cara** — 3 arsitektur × 2 lengan = 6 run. Seed 42 saja, 30 epoch, **tanpa
early stopping** (`patience=epochs` untuk ultralytics, `early_stopping=False`
untuk rfdetr), split SawitMVC-Depth seed42 (980/140/288 citra, 72 pohon uji).

| arsitektur | bobot awal | batch | catatan |
|---|---|---|---|
| YOLO26n | `yolo26n.pt` | 16 | ultralytics 8.4.103 |
| RT-DETR-L | `rtdetr-l.pt` | 8 | batch 8 (bukan 16) agar dua lengan muat serentak; identik di kedua lengan |
| RF-DETR Nano | pratlatih rfdetr | 8 (grad-accum 2) | normalisasi kanal depth dari train saja |

**Kedua lengan hanya berbeda pada folder PNG depth.** Set z03 dibangkitkan
dengan `build/reproject_depth.py --z-near 0.3 --z-far 8.0`, yaitu jalur
reproyeksi yang PERSIS sama dengan set z08 — kontrolnya: cakupan piksel valid
rata-rata identik **0,71032** di kedua set, jadi geometri, z-buffer, dan tambal
lubangnya benar-benar sama dan yang berbeda hanya pengodean.

Pagar keadilan (identik di kedua lengan, diverifikasi dari `args.yaml`):
`hsv_h=hsv_s=hsv_v=0` (RandomHSV melewati citra 4-kanal secara diam), modality
dropout 0, inflasi conv pertama dari bobot pratlatih (model **dan** EMA),
`deterministic=True`, seed 42, imgsz/resolution 640.

**Cacat yang ditutup sebelum run** — `DEPTH_DIR` di-hardcode di
`train/train_rfdetr_4ch.py`, `eval/eval_e022_pycoco.py`,
`eval/eval_rfdetr_e022.py`, dan diwarisi `eval/eval_e022_paired.py`. Tanpa
`--depth-dir`, bobot z03 akan dinilai memakai depth z08 — ketidakcocokan
latih/uji yang senyap dan akan memalsukan efek besar yang sebetulnya artefak.
Keempat skrip kini menerima folder depth eksplisit per lengan.

Evaluasi: pycocotools protokol tunggal, bootstrap berpasangan 2000× pada tingkat
POHON. `hasil.json` trainer tidak dipakai untuk membandingkan lengan [E-025].

**Batas yang melekat pada rancangan ini, jangan dihaluskan:**
- **Satu seed.** E-032 mengukur rentang antar-seed **0,0354** pada lengan `awal`
  YOLO26n — lebih besar daripada seluruh efek yang pernah terukur di E-022.
  CI bootstrap di sini mengukur galat pencuplikan SET UJI, **bukan** varians
  seed. Δ yang "signifikan" di sini karenanya bukti yang lebih lemah daripada
  Δ signifikan di E-032.
- **30 epoch**, bukan 60 atau 150. Angka absolutnya tidak sebanding dengan
  E-022/E-027/E-030/E-032 maupun dengan E-021.
- **Tanpa lengan RGB.** Yang diuji murni kontras z08 vs z03; eksperimen ini
  tidak dapat menjawab apakah kanal depth menolong sama sekali.
- RT-DETR-L memakai batch 8, berbeda dari E-022 yang memakai 16. Sah untuk
  kontras di dalam arsitektur, tidak sah untuk dibandingkan lintas eksperimen.

**Hasil** — Δ = z08 − z03, pycocotools, bootstrap berpasangan 2000× per pohon
(72 pohon, 288 citra uji). `*` = CI95 tidak memuat nol.

| metrik | YOLO26n | RT-DETR-L | RF-DETR Nano |
|---|---|---|---|
| mAP50 z03 (rentang salah) | 0,3485 | 0,4021 | 0,4351 |
| mAP50 z08 (terkalibrasi) | 0,3707 | 0,4126 | 0,4539 |
| **Δ mAP50** | **+0,0222** | **+0,0105** | **+0,0188** |
| CI95 Δ mAP50 | [−0,0101; +0,0571] | [−0,0285; +0,0546] | [−0,0155; +0,0558] |
| frac. bootstrap positif | 0,905 | 0,712 | 0,848 |
| Δ B1 | −0,0029 | **−0,0648** * | +0,0071 |
| Δ B2 | +0,0067 | −0,0089 | −0,0367 |
| Δ B3 | **+0,0876** * | +0,0678 | +0,0659 |
| Δ B4 | −0,0026 | +0,0480 | +0,0390 |

Rerata Δ mAP50 **+0,0172**, rentang antar-arsitektur 0,0117.
Rerata Δ B3 **+0,0738**, rentang 0,0217.

**Putusan — INDIKASI.** Kriteria yang ditetapkan di muka tidak terpenuhi ke arah
mana pun:

- **Tidak DIPALSUKAN.** Tanda Δ mAP50 **positif pada ketiga arsitektur**, dan dua
  dari tiga melebihi ambang 0,015.
- **Tidak DIKONFIRMASI.** Tidak satu pun CI95 Δ mAP50 mengecualikan nol.

Pola sekunder yang paling tahan: **Δ B3 positif pada ketiganya**
(+0,0876 / +0,0678 / +0,0659; fraksi bootstrap positif 0,989 / 0,917 / 0,900),
signifikan pada YOLO26n. Rentang antar-arsitekturnya hanya 0,0217 — sempit untuk
tiga arsitektur yang mAP50 absolutnya berbeda 0,09.

**Kontra-pola yang tidak boleh disembunyikan:** RT-DETR-L kehilangan B1 secara
signifikan (−0,0648 [−0,1123; −0,0130], fraksi positif 0,004), sementara dua
arsitektur lain tidak (−0,0029 dan +0,0071). Jadi rentang yang benar **bukan**
menang di semua lini pada semua arsitektur; pada RT-DETR-L ia menggeser kinerja
dari B1 ke B3/B4. B2 juga campur (+0,0067 / −0,0089 / −0,0367).

**Mengapa ini belum boleh disebut temuan:** E-032 mengukur ayunan antar-seed
**0,0354** pada YOLO26n — **lebih besar daripada rerata Δ mAP50 +0,0172 di sini**.
Eksperimen ini satu seed, jadi CI bootstrapnya mengukur galat pencuplikan set uji
saja dan tidak dapat memisahkan efek rentang dari lotere inisialisasi. Yang
memberi bobot lebih pada Δ B3 bukan besarnya, melainkan **tanda yang sepakat di
tiga arsitektur berbeda** — replikasi lintas-arsitektur, bukan lintas-seed.
Perlu diingat pula B3 hanya ~14% kotak dengan AP50 dasar rendah (0,16–0,39),
jadi ia kelas paling berderau; konsistensi tandanya yang menarik, bukan
magnitudonya sendirian.

**Dampak**

1. **Untuk SR-015 §7b:** "kualitas kanal depth" tetap kandidat penyebab yang
   hidup, dan kini punya bukti terarah pertamanya — memperbaiki pengodean
   menggerakkan angka ke arah yang diprediksi pada tiga arsitektur sekaligus.
   Belum cukup untuk mengubah putusan SR-015; fusi awal tetap DIPALSUKAN.
2. **Untuk jalur produksi:** `pipeline/fourch.py` masih memakai
   `Z_NEAR/Z_FAR = 0,3/8,0` sebagai konstanta modul, tanpa flag CLI. Eksperimen
   ini memberi alasan empiris untuk membongkarnya: rentang wajib parameter
   eksplisit dan wajib ditulis ke `depth_meta.json` bersama bobot, sebagaimana
   jalur eksperimen sudah melakukannya.
3. **Uji lanjutan yang dibenarkan hasil ini:** ulangi kontras z08 vs z03 pada
   **3 seed** untuk satu arsitektur (YOLO26n, paling murah). Tanpa itu +0,0172
   tidak dapat dipisahkan dari derau seed, dan klaim apa pun akan mengulang
   kesalahan yang menjatuhkan E-022.

**Cacat lingkungan yang ditemukan saat menjalankan** (bukan hasil ilmiah, tetapi
menghabiskan waktu nyata dan akan berulang):

- `nohup … &` dari shell yang time-out ikut terbunuh bersama grup prosesnya —
  dua run RT-DETR mati senyap setelah mencetak "Starting training". Pakai
  `setsid`.
- venv `.venv` tidak lengkap dibangun ulang: `tqdm`, `huggingface_hub`,
  `pytorch_lightning`, `faster_coco_eval`, `albumentations` semuanya hilang dan
  masing-masing menggagalkan RF-DETR pada titik yang berbeda. `requirements.txt`
  tidak menyebut empat yang terakhir (semuanya dependensi tak langsung `rfdetr`).
- `pip install albumentations` menarik `opencv-python-headless 5.0.0.93` —
  persis jebakan yang dicatat STATUS.md §2. Dikembalikan ke `4.11.0.86`.

**Reproduksi** — `build/reproject_depth.py --z-near 0.3 --z-far 8.0 --tujuan
depth_png_z03_8` (set z08 sudah ada), lalu `train/train_depth4ch.py` (yolo26n,
rtdetr-l) dan `train/train_rfdetr_4ch.py --depth-dir …`, lalu
`eval/eval_e022_paired.py --depth-dir-a/--depth-dir-b` dan
`eval/eval_rfdetr_e022.py --depth-dir-a/--depth-dir-b`. Bukti:
`experiments/results/E-033/paired_{yolo26n,rtdetrl,rfdetrnano}.json`.

## E-033b — Replikasi 3 seed E-033: efek mAP50 TIDAK bertahan (2026-08-06) · SR-015

**Hipotesis** — E-033 memberi INDIKASI: Δ mAP50 (z08 − z03) positif pada tiga
arsitektur, rerata +0,0172, tetapi seluruh CI memuat nol dan seluruhnya satu
seed. E-032 mengukur ayunan antar-seed 0,0354 pada YOLO26n — lebih besar
daripada efek itu. Kalau efek rentang metrik nyata, tandanya harus bertahan
ketika seed diganti.

**Yang akan memalsukan** (kriteria E-032 dipakai apa adanya): tanda Δ tidak
sepakat pada 3 seed.

**Cara** — 4 run baru YOLO26n (seed 1337 dan 2024 × lengan z08/z03), resep
IDENTIK dengan E-033 seed 42: 30 epoch, tanpa early stopping, hsv=0, dropout=0,
inflasi conv pertama, split `seed42` (split tidak diubah — yang divariasikan
hanya seed inisialisasi). Evaluasi sama: pycocotools, bootstrap berpasangan
2000× per pohon.

**Hasil — Δ mAP50 dan per kelas, YOLO26n**

| metrik | seed 42 | seed 1337 | seed 2024 | rerata | rentang |
|---|---|---|---|---|---|
| **mAP50** | **+0,0222** | **−0,0052** | **−0,0012** | **+0,0053** | 0,0274 |
| mAP50-95 | +0,0050 | −0,0048 | −0,0095 | −0,0031 | 0,0146 |
| B1 | −0,0029 | **−0,0555** * | −0,0417 | −0,0333 | 0,0526 |
| B2 | +0,0067 | +0,0162 | −0,0149 | +0,0027 | 0,0310 |
| B3 | **+0,0876** * | +0,0216 | +0,0566 | +0,0553 | 0,0660 |
| B4 | −0,0026 | −0,0032 | −0,0049 | −0,0036 | 0,0023 |

`*` = CI95 tidak memuat nol.

mAP50 absolut: z03 = 0,3485 / 0,3213 / 0,3613 (rentang antar-seed **0,0400**);
z08 = 0,3707 / 0,3161 / 0,3601 (rentang **0,0546**). **Ayunan seed pada satu
lengan lebih besar daripada seluruh selisih antar-lengan yang pernah terukur.**

**Putusan — DIPALSUKAN untuk mAP50 agregat.** Tanda Δ mAP50 tidak sepakat
(+ / − / −). Angka +0,0222 pada seed 42 — dasar seluruh INDIKASI di E-033 —
adalah **pencilan seed**, bukan efek. Rerata turun dari +0,0222 menjadi +0,0053,
lebih kecil daripada ambang 0,015 yang ditetapkan di muka.

Ini persis mode kegagalan yang menjatuhkan E-022 dan kemudian dikoreksi E-027:
satu seed yang kebetulan bagus dibaca sebagai temuan. Kali ini tertangkap
sebelum masuk laporan.

**Yang TETAP berdiri — redistribusi antar kelas.** Dua pola tidak ikut runtuh,
dan keduanya konsisten lintas seed DAN lintas arsitektur:

| kelas | 3 seed YOLO26n | RT-DETR-L | RF-DETR Nano | rerata 5 pengukuran |
|---|---|---|---|---|
| **B3** | +0,0876 * / +0,0216 / +0,0566 | +0,0678 | +0,0659 | **+0,0599**, positif **5/5** |
| **B1** | −0,0029 / −0,0555 * / −0,0417 | −0,0648 * | +0,0071 | **−0,0316**, negatif **4/5** |

Jadi memperbaiki rentang metrik **memindahkan kinerja dari B1 ke B3**, dan
kedua efek itu saling meniadakan di agregat. Itu menjelaskan mengapa mAP50
tampak bergerak positif di E-033 pada tiga arsitektur namun tidak pernah
signifikan: yang bergerak bukan total, melainkan distribusinya.

Penjelasan yang konsisten dengan fisika pengodean, **belum diuji**: rentang
0,3/8,0 memampatkan seluruh adegan ke level 1–122 dengan 10,2% piksel mentok di
level 1, sehingga jarak menengah-jauh kehilangan resolusi. Rentang 0,8/15,0
memulihkan resolusi di sana tetapi menghabiskan lebih sedikit level untuk objek
dekat. B1 (matang, cenderung terlihat besar/dekat) dan B3 tidak berada pada
rentang jarak yang sama. Ini hipotesis pasca-hoc — jangan dikutip sebagai
temuan tanpa uji terstratifikasi menurut jarak.

**Dampak**

1. **INDIKASI E-033 dicabut untuk mAP50.** Jangan mengutip +0,0172 maupun
   +0,0222. Yang boleh dikutip: rentang metrik tidak memperbaiki mAP50 agregat
   pada 3 seed, dan menggeser B1 → B3.
2. **SR-015 §7b:** "kualitas kanal depth" tetap kandidat penyebab yang hidup,
   tetapi bukti terarah pertamanya ternyata **bukan** kenaikan agregat. Kalau
   jalur depth diteruskan, ukuran yang layak dipantau adalah AP per kelas
   terstratifikasi jarak, bukan mAP50.
3. **Jalur produksi:** alasan memperbaiki `fourch.Z_NEAR/Z_FAR` sekarang
   **bukan** "menaikkan mAP" — melainkan bahwa rentang yang salah mengubah
   perilaku per kelas secara sistematis dan diam-diam. Rentang tetap wajib jadi
   parameter eksplisit yang tercatat bersama bobot, tetapi jangan dijanjikan
   memberi kenaikan angka.
4. **Pelajaran proses:** 4 run YOLO26n paralel berebut `labels.cache` bersama di
   folder dataset (`/workspace/SawitMVC-Depth/data/labels.cache`); dua run mati
   dengan `FileNotFoundError`. Anggaran VRAM saja tidak cukup — run serentak
   juga berbagi berkas cache. Geser waktu peluncuran atau pisahkan cache.

**Reproduksi** — `train/train_depth4ch.py --arch yolo26n --modal rgbd --seed
{1337,2024} --depth-dir {depth_png,depth_png_z03_8} --epochs 30`, lalu
`eval/eval_e022_paired.py --depth-dir-a/--depth-dir-b`. Bukti:
`experiments/results/E-033/paired_yolo26n_seed{1337,2024}.json`.

## F-002 — (P2) Apakah frekuensi tinggi memisahkan tandan dari PELEPAH? (2026-08-06) · gerbang K1 · [SR-017](SR/SR-017-sintesis-deep-research.md)

**Hipotesis** — K1 (cabang frekuensi samping) bersandar pada anggapan bahwa
respons frekuensi tinggi menyoroti isi tandan. E-011 sudah mengukur sesuatu yang
mirip — Laplacian +0,0458 di atas kendali pada B4, mengungguli Sobel +0,0367 —
tetapi pembandingnya **cincin sekeliling**, yang memuat apa saja: langit, batang,
tanah, tandan tetangga.

Mode gagal yang dikhawatirkan lebih spesifik: pelepah sawit adalah struktur
berfrekuensi sangat tinggi (anak daun tipis berulang), dan B4 yang gelap
kehijauan justru kelas yang paling menyatu dengannya. Bila frekuensi tinggi
tidak memisahkan tandan dari **pelepah**, cabang K1 akan belajar menyalakan
pelepah, dan kenaikan apa pun yang muncul bukan dari mekanisme yang diklaim.

**Dipalsukan bila** tidak ada satu pun lengan frekuensi tinggi yang menaikkan
AUC tandan-vs-pelepah lebih dari **+0,02** di atas kendali kotak acak pada B4
(ambang diambil dari E-011 supaya kedua uji terbaca pada skala yang sama).

**Cara** — `experiments/code/analysis/freq_vs_pelepah.py`, 250 citra
`SawitMVC-test`, 1.114 kotak GT terukur (1 kotak sebagian ditolak karena wilayah
pelepahnya < 200 piksel). Wilayah pembanding didefinisikan ulang:

    pelepah = cincin sekeliling kotak  MINUS  seluruh kotak GT tandan lain

`asli`/`gradmag`/`laplacian` disalin persis dari `contrast_boost_test.py` agar
sebanding dengan E-011. Sub-band Haar satu tingkat (LH/HL/HH) ditulis langsung
dengan numpy — `pywt` tidak terpasang. Ketiga sub-band dihaluskan Gaussian
sigma=2 **identik** dengan perlakuan gradmag/laplacian di E-011; tanpa itu
perbandingan DWT vs Laplacian tercemar beda penghalusan, bukan beda kandungan
frekuensi. Kendali kotak acak berukuran sama diperlakukan identik.

**Hasil** — AUC pemisahan piksel isi-kotak vs pelepah:

| Lengan | B1 | B2 | B3 | B4 | kendali | B4−kendali |
|---|---|---|---|---|---|---|
| asli (luminans) | 0,6016 | 0,6127 | 0,5889 | 0,5849 | 0,5694 | +0,0155 |
| gradmag (Sobel) | 0,5790 | 0,5898 | 0,6052 | 0,6289 | 0,5681 | +0,0608 |
| **laplacian** | 0,5804 | 0,5934 | 0,6133 | 0,6423 | 0,5702 | **+0,0721** |
| dwt_lh | 0,5779 | 0,5918 | 0,6068 | 0,6325 | 0,5702 | +0,0623 |
| dwt_hl | 0,5750 | 0,5818 | 0,6018 | 0,6286 | 0,5652 | +0,0634 |
| **dwt_hh** | 0,5808 | 0,5927 | 0,6134 | 0,6403 | 0,5672 | **+0,0731** |
| dwt_energi | 0,5818 | 0,5921 | 0,6113 | 0,6403 | 0,5683 | +0,0720 |

**Putusan** — **LOLOS.** Lengan terbaik dwt_hh +0,0731, lebih dari tiga kali
ambang +0,02. Mode gagal yang dikhawatirkan **tidak terjadi**: pemisahan terhadap
pelepah justru LEBIH BESAR daripada terhadap cincin generik di E-011 (Laplacian
0,0721 vs 0,0458).

Dua pembacaan yang lebih penting daripada angka gerbangnya:

1. **Urutan kelas monoton B1 < B2 < B3 < B4 pada SETIAP lengan frekuensi
   tinggi**, dan terbalik pada luminans (di sana B4 justru paling rendah,
   0,5849). Arah ini persis yang diramalkan mekanismenya: makin mentah, makin
   gelap-kehijauan, makin menyatu dengan pelepah dalam intensitas — dan makin
   terpisah dalam tekstur. Ini mereplikasi pembalikan urutan E-011 pada
   pembanding yang lebih ketat.
2. **Laplacian dan DWT-HH praktis seri** (0,0721 vs 0,0731; selisih 0,0010).
   Pada dataset ini, sub-band DWT **tidak** membeli apa pun di atas Laplacian
   biasa yang jauh lebih murah. Konsekuensinya untuk F-007: lengan Laplacian
   bukan formalitas — ia pesaing sesungguhnya, dan **DWT wajib mengalahkannya**
   untuk membenarkan mesin tambahannya.

**Dampak** — K1 boleh dilanjutkan ke F-007. Lengan `laplacian` dinaikkan
statusnya dari pembanding menjadi kandidat setara. Uji ini **tidak** membuktikan
K1 akan menaikkan mAP; ia hanya menutup satu mode gagal yang dapat membatalkannya
secara murah. Keterpisahan piksel bukan AP.

**Reproduksi** — `python analysis/freq_vs_pelepah.py --images 250`. Bukti:
`experiments/results/F-002/freq_vs_pelepah.json`.

## F-003 — (P3) Plafon keras distilasi lintas-sisi (2026-08-06) · gerbang K3 · [SR-017](SR/SR-017-sintesis-deep-research.md)

**Hipotesis** — K3 memindahkan keyakinan dari sisi yang benar ke sisi yang salah
lewat graf `_confirmedLinks`. Mekanisme itu punya plafon keras yang dapat diukur
tanpa melatih apa pun: **dari kemunculan tandan yang diprediksi salah kelas,
berapa fraksi yang punya kemunculan BENAR pada sisi lain tandan fisik yang sama?**
Bila mayoritas galat salah di semua sisi, tidak ada yang bisa ditransfer.

**Dipalsukan bila** fraksi galat-yang-dapat-diselamatkan < **0,30**.

**Cara** — `analysis/cross_side_consistency.py --dump-tandan` (flag baru; jalur
agregatnya tidak diubah) lalu `analysis/plafon_lintas_sisi.py`. Bobot
`runs_e022/yolo26n_sawitmvc_rgb_seed42`, `SawitMVC-test`, conf 0,25, IoU cocok
0,5. Oracle identitas = `bunches[].appearances` dari `json/<pohon>.json`.

Pemeriksaan kebenaran modifikasi: jalur agregat mereproduksi E-028 **persis** —
511 tandan terukur, 119 tidak konsisten, laju **0,2329**.

**Kenapa perlu inferensi ulang** — `results/E-028/konsistensi_sawitmvc_rgb_seed42.json`
diperiksa langsung dan **hanya menyimpan laju agregat**; tidak ada satu pun
prediksi per-sisi. Ini menjawab §9 butir 3 rencana: P3 tidak dapat dihitung dari
berkas itu.

**Hasil** — 1.022 tandan multi-sisi, 2.230 kemunculan: 1.078 benar, 408 salah
kelas, 744 terlewat.

| Plafon | n | fraksi | CI95 |
|---|---|---|---|
| **Kelas** (galat kelas punya sisi benar) | 114 / 408 | **0,2794** | [0,2353; 0,3235] |
| **Kehadiran** (sisi terlewat punya sisi benar) | 368 / 744 | **0,4946** | [0,4583; 0,5309] |

Sebaran sisi benar pada tandan yang bergalat: **194 tandan punya NOL sisi benar**,
93 punya satu, 10 punya dua, 4 punya tiga. Dari 408 galat kelas, **294 (72%)
salah di SEMUA sisi**.

Per kelas GT (fraksi dapat diselamatkan): B1 0,5333 (16/30) · B3 0,4257 (43/101)
· B2 0,2573 (44/171) · **B4 0,1038 (11/106)**.

**Putusan** — **DIPALSUKAN untuk suku kelas, tetapi lemah.** Titik estimasi
0,2794 di bawah ambang pra-daftar 0,30, jadi aturan yang ditulis sebelum melihat
data mengikat dan K3 tidak diteruskan. **Tetapi CI95 [0,2353; 0,3235] memuat
0,30** — data ini tidak dapat memisahkan keduanya. Ini pemalsuan lemah, bukan
tegas, dan wajib dibaca demikian.

Yang justru tegas adalah dua hal lain:

1. **72% galat kelas salah di semua sisi.** Galat kelas bukan kecelakaan per
   pandangan; ia sifat tandannya. Itu konsisten dengan E-028 (B2 paling ambigu)
   dan dengan diagnosis (B) fotometrik di CLAUDE.md — ambiguitas B2↔B3 tidak
   diselesaikan dengan melihat dari sisi lain.
2. **B4 adalah kasus terburuk: 0,1038.** Dari 106 galat kelas B4, hanya 11 punya
   saudara yang benar. Harapan bahwa K3 menolong B4 **tertutup**, dan itu
   kebetulan kelas yang paling ingin ditolong.

**Temuan sampingan yang TIDAK menyelamatkan gerbang ini** — plafon **kehadiran**
0,4946, CI95 [0,4583; 0,5309], tegas di atas 0,30. Suku konsistensi kehadiran K3
(sisi terlewat ditolong sisi yang mendeteksi) punya ruang hampir dua kali lipat
suku kelas. Itu **mekanisme yang berbeda dengan plafon yang berbeda**, bukan
penyelamat gerbang yang gagal. Bila mau dikejar, ia harus didaftarkan sebagai
hipotesis tersendiri dengan ambangnya sendiri — bukan disisipkan ke K3 setelah
melihat hasil ini.

**KAVEAT PROKSI, wajib ikut dikutip** — bobot yang dipakai **yolo26n**, bukan
RF-DETR-L (bobot E-021 hilang saat pod di-terminate). Angka ini menjawab
"apakah ada ruang secara struktural", bukan "berapa besar ruangnya pada model
final". Detektor lebih kuat menggeser plafon ke dua arah sekaligus: galat
berkurang (pembilang turun) tetapi sisi terlewat juga berkurang (penyebut naik).
Arah netonya tidak dapat ditebak dari sini. P3 definitif menunggu F-004.

**Dampak** — **F-008 (K3) tidak dijalankan.** Anggaran seri turun ~13 jam GPU.
Seri berlanjut dengan K1 (F-002 LOLOS) dan K2 (menunggu F-005). Karena tinggal
dua komponen, syarat F-009 ("≥ 2 komponen lolos") sekarang menuntut **keduanya**
lolos.

**Reproduksi** —
`python analysis/cross_side_consistency.py --bobot ../../runs/detect/runs_e022/yolo26n_sawitmvc_rgb_seed42/weights/best.pt --split-dir results/splits_rgb/sawitmvc --data-root /workspace/SawitMVC/data --dump-tandan <dump>`
lalu `python analysis/plafon_lintas_sisi.py --dump <dump>`. Bukti:
`experiments/results/F-003/{plafon_lintas_sisi,konsistensi_ulang_yolo26n}.json`.

## F-001 — Pemulihan prasyarat seri F + probe VRAM RTX A4500 (2026-08-06) · [SR-017](SR/SR-017-sintesis-deep-research.md)

**Hipotesis** — Seri F seluruhnya berdiri di atas RF-DETR-L. Sebelum satu
komponen pun dirancang, tiga hal harus dipastikan: dataset RF-DETR dapat
dibangun ulang, bobot pratlatih dapat diperoleh kembali, dan **resep E-021 muat
di GPU yang sekarang**. Yang terakhir bukan formalitas: E-021 dilatih di NVIDIA
L4 23 GB, sedangkan mesin ini RTX A4500 **20,4 GB — 2,6 GB lebih kecil**.

**Dipalsukan bila** resep E-021 (batch 8 / grad-accum 2 @1280) OOM, sehingga
seluruh seri harus memakai konfigurasi berbeda dari baseline yang dibandingkan.

**Cara** — `build/build_rfdetr_ds.py` untuk dataset; konstruksi `RFDETRLarge()`
mengunduh bobot pratlatih; lalu `train/train_rfdetr.py --smoke` 1 epoch pada
resolusi 1280 dengan VRAM disampel tiap 2 detik.

**Temuan keadaan awal (diperiksa langsung di disk, bukan diasumsikan)**

| Hal | Keadaan |
|---|---|
| Bobot RF-DETR-L E-021 | **HILANG.** `find / -name "checkpoint*.pth"` menemukan 6 berkas, semuanya `rfdetrnano` milik E-033 |
| Bobot pratlatih | **HILANG.** Hanya `rf-detr-nano.pth` di `~/.roboflow/models/`; `rf-detr-large-2026.pth` diunduh ulang (130 MB, MD5 tervalidasi) |
| `rfdetr_ds` | **KOSONG** (0 citra). Dibangun ulang jadi 3000/404/588 symlink |
| `splits_rgb/sawitmvc` | **UTUH**, path absolutnya masih resolve |
| Kriteria klasifikasi | **IA-BCE** (`ia_bce_loss: true`), bukan softmax CE — lihat Dampak |

**Hasil** —

| Ukuran | Nilai |
|---|---|
| VRAM puncak, batch 8 @1280 | **10.331 MiB** dari 20.470 |
| Kelonggaran | 10.139 MiB |
| **Paralelisme maksimum** | **1** — 2 × 10.331 = 20.662 > 20.470 |
| Menit per epoch (latih + val) | **9,2** |
| Param model | 35,6 jt (E-021 mencatat 35,7 jt) |
| `scales: [1440]` di log | **tidak muncul** — jebakan `CATATAN-TEKNIS-E021.md` #2 terhindar |
| Smoke 1 epoch | val mAP50 0,4941 · test mAP50 0,5230 |

**Putusan** — **DIKONFIRMASI.** Resep E-021 muat apa adanya; tidak perlu turun
ke batch 4. Konfigurasi dikunci untuk SELURUH lengan seri F supaya perbandingan
baseline↔perlakuan tidak tercemar beda batch.

Angka smoke 1 epoch **bukan hasil** — ia hanya bukti pipeline hidup. Jangan
dikutip. E-021 mencapai val 0,5695 pada epoch terbaiknya (epoch 9 dari 19).

**Dampak** —

1. **Paralelisme 1 adalah kendala keras.** Kelonggaran 10,1 GB terlihat lega
   tetapi tidak cukup untuk run RF-DETR-L kedua. Ini persis jebakan yang dicatat
   CLAUDE.md ("3 × 6,6 = 19,7 dari 19,7 GiB"). Seluruh run seri F **berurutan**;
   yang dapat diparalelkan hanya pekerjaan CPU.
2. **Anggaran dihitung ulang dari angka terukur**, bukan diskalakan dari L4:
   ~9,2 mnt/epoch × ~19 epoch ≈ **3 jam per seed**, jadi F-004 ≈ **9 jam**.
3. **Kriteria klasifikasi RF-DETR terbaca langsung dari kode** — menjawab
   pertanyaan yang membuka seri ini. `criterion.py:268-296`: IA-BCE, bobot
   positif `t = σ(z)^α · IoU^(1−α)` dengan `α = 0,25`, di-clamp 0,01, di-detach.
   Skor deteksi = `σ(z)` per kelas **independen**, top-k `num_select=300` atas
   grid datar Q×C (`postprocess.py:106`). **Tidak ada simpleks softmax.**
   Konsekuensinya untuk K2: residu ordinal harus berupa offset logit aditif
   ber-mean nol antar 4 kelas, bukan pergeseran pada simpleks; dan karena mAP
   COCO dihitung per kelas, yang dapat digerakkan residu itu adalah selisih
   logit **antar kelas di dalam query yang sama** — itulah yang diukur F-005.

**Reproduksi** — `build/build_rfdetr_ds.py --splits results/splits_rgb/sawitmvc --labels /workspace/SawitMVC/data/labels --output rfdetr_ds`,
lalu `train/train_rfdetr.py --dataset rfdetr_ds --resolution 1280 --batch 8 --grad-accum 2 --workers 8 --smoke --output <dir>`.
Bukti: `experiments/results/F-001/prasyarat.json`.

## F-005 — (P1) Massa selisih logit antar-kelas di dalam query yang sama (2026-08-06) · gerbang K2 · [SR-017](SR/SR-017-sintesis-deep-research.md)

**Hipotesis** — K2 menambahkan residu ordinal ber-mean nol yang **di-clip ke ±ε**.
Clip itu memberi jaminan penjaga-peringkat: urutan hanya dapat berubah bila
selisih logit < 2ε. Jaminan itu membuktikan **keamanan, bukan potensi naik** — ia
tidak menjamin ada cukup kerugian AP yang tinggal di pasangan rapat untuk
direbut. Gerbang ini mengukur massanya.

Rumusannya diubah dari rencana asli, dan alasannya dibaca dari kode (F-001):
RF-DETR memakai IA-BCE dengan `sigmoid` per kelas independen dan top-k atas grid
datar Q×C — tidak ada simpleks softmax — sedangkan mAP COCO dihitung per kelas.
Maka yang dapat digerakkan residu ber-mean nol adalah selisih logit **antar kelas
di dalam query yang sama**:

$$\Delta = z_{q,c_\text{benar}} - z_{q,c_\text{teratas salah}}$$

**Dipalsukan bila** fraksi galat kelas dengan $|\Delta| < 2\varepsilon = 0{,}6$
**< 0,30**.

**Cara** — `analysis/massa_selisih_logit.py` atas
`results/F-004/logits_test_seed42.npz`, yaitu dump logit mentah seluruh query
dari **checkpoint konvergen** `runs_f004/rfdetrl_rgb_seed42/checkpoint_best_ema.pth`
(seed 42, best epoch 5, val mAP50 0,5708). `SawitMVC-test`, pencocokan query↔GT
pada IoU ≥ 0,5.

**Checkpoint konvergen itu syarat, bukan detail.** Ukuran ini sensitif terhadap
skala logit: model yang belum konvergen punya logit rapat sehingga fraksinya
bias TINGGI. Terukur langsung — pada checkpoint probe 1-epoch F-001 fraksinya
0,7666 dengan median |Δ| 0,3086; pada checkpoint konvergen turun ke 0,7113
dengan median melebar ke 0,3633. Arahnya persis seperti yang dikhawatirkan, dan
angka yang dipakai adalah yang konvergen.

**Hasil** — 2.612 kotak GT, hanya **27 (1,0%) tidak tertangkap query mana pun**;
918 salah kelas, 1.667 benar.

| | nilai |
|---|---|
| Galat kelas dalam pita \|Δ\| < 0,6 | **653 / 918 = 0,7113** |
| Kuantil \|Δ\| galat | p10 0,060 · p25 0,159 · **p50 0,363** · p75 0,662 · p90 1,135 |

Per kelas GT (fraksi dalam pita): **B3 0,8493** (355/418) · B1 0,7551 (74/98) ·
B4 0,6087 (98/161) · **B2 0,5228** (126/241).

Pasangan tertukar, seluruhnya **kelas bertetangga**: B3→B4 202 · B3→B2 199 ·
B2→B3 177 · B4→B3 147 · B1→B2 90 · B2→B1 57.

Paparan risiko (dilaporkan, **bukan penggugur**, dan ini didaftarkan sebelum
melihat data): **769 query yang sudah BENAR juga berada di dalam pita**, jadi
rasio untung-rugi **0,849** — yang benar-berisiko sedikit LEBIH BANYAK daripada
yang salah-dapat-diperbaiki.

**Putusan** — **LOLOS.** 0,7113 jauh di atas ambang 0,30. Potensi naik K2 tidak
tertutup secara matematis.

Tiga pembacaan yang tidak boleh dihaluskan:

1. **Ini bukan ramalan kenaikan mAP.** Gerbang ini hanya menyatakan bahwa
   ruangnya ada. Apakah kepala ordinal benar-benar mengarahkan residu ke sisi
   yang benar adalah pertanyaan F-006, bukan pertanyaan ini.
2. **Rasio untung-rugi 0,849 < 1.** Residu ber-clip menyentuh lebih banyak query
   benar daripada query salah. Kepala ordinal karena itu harus **informatif**,
   bukan sekadar aktif; residu yang mendekati acak berekspektasi merugikan. Inilah
   yang membuat gate α dan clip ±ε bukan hiasan melainkan syarat keselamatan.
3. **B2 justru yang paling sedikit dapat direbut (0,5228), bukan paling banyak.**
   Rancangan meramalkan K2 paling menolong B2↔B3. Massa terbesar ternyata di
   **B3** (0,8493). Galat B2 lebih sering jauh dari batas — yakin tetapi salah —
   dan itu konsisten dengan E-028 yang menempatkan B2 sebagai kelas paling ambigu
   (0,434). Bila F-006 memberi kenaikan, kenaikannya **diperkirakan di B3, bukan
   B2**; kenaikan di B2 justru perlu dijelaskan, bukan dirayakan.

**Dampak** — K2 boleh dilanjutkan ke F-006. Dengan K1 (F-002) dan K2 (F-005)
sama-sama lolos dan K3 gugur, **kedua komponen tersisa lolos gerbangnya**,
sehingga syarat F-009 ("≥ 2 komponen lolos") terpenuhi bila keduanya juga lolos
gerbang hasilnya nanti.

**Reproduksi** — `python analysis/massa_selisih_logit.py --npz results/F-004/logits_test_seed42.npz`.
Bukti: `experiments/results/F-005/massa_selisih_logit_seed42.json`.

## F-004 — Baseline RF-DETR-L 3 seed: varians seed jalur RGB akhirnya terukur (2026-08-06) · [SR-017](SR/SR-017-sintesis-deep-research.md)

**Hipotesis** — Seluruh seri F membandingkan perlakuan terhadap baseline
RF-DETR-L. Dua hal harus dipenuhi lebih dulu: (a) resep E-021 masih tereproduksi
setelah bobotnya hilang dan GPU-nya berganti, dan (b) **varians seed jalur RGB
harus diukur** — sampai kini nol terukur untuk RF-DETR pada SawitMVC. Ambang
+0,05 yang dipakai seluruh rencana diturunkan dari E-027 (0,0321) dan E-031
(0,0488), keduanya diukur pada **YOLO26n di SawitMVC-Depth**, bukan jalur ini.

**Dipalsukan bila** ketiga seed menyimpang jauh dari E-021, sehingga tidak ada
baseline sah untuk dibandingkan.

**Cara** — `shell/f004_baseline.sh`: `train/train_rfdetr.py` seed 42/1337/2024,
resep dikunci persis ke `training_config.json` E-021 (resolusi 1280, batch 8,
grad-accum 2, workers 8, epochs 60, early stopping patience 8 min-delta 0,001,
EMA, `multi_scale=False`, `expanded_scales=False`, `ia_bce_loss=True`).
Berurutan — dua run RF-DETR-L serentak = 20.662 MiB > 20.470 (F-001).
Total 5j40m (09:36:57 → 15:17:18), rata-rata 1j53m per seed.

**Hasil** —

| seed | val mAP50 (EMA) | val mAP50-95 | test mAP50 | test mAP50-95 | epoch terbaik | total epoch |
|---|---|---|---|---|---|---|
| 42 | 0,5708 | 0,2660 | 0,5997 | 0,2738 | 5 | 14 |
| 1337 | 0,5708 | 0,2635 | 0,5900 | 0,2700 | 5 | 16 |
| 2024 | 0,5796 | 0,2699 | 0,5951 | 0,2677 | 5 | 14 |
| **rerata** | **0,5738** | 0,2665 | **0,5949** | **0,2705** | — | — |

**Varians seed jalur RGB, RF-DETR-L, SawitMVC-test:**

| Metrik | SD | Rentang |
|---|---|---|
| test mAP50 | **0,0049** | 0,0097 |
| test mAP50-95 | 0,0031 | 0,0062 |
| val mAP50 | 0,0051 | 0,0088 |

Perbandingan reproduksi harus like-for-like: `evaluation.json` E-021 (jalur
`run_test`, checkpoint `best_total`) mencatat test mAP50 **0,5837**; F-004 lewat
jalur yang SAMA memberi rerata **0,5949**. Angka **0,6038** yang biasa dikutip
berasal dari evaluasi EMA-konsisten `eval_all_pycoco.py` yang terpisah, jadi
tidak sebanding dengan tabel di atas.

**Putusan** — **DIKONFIRMASI.** Resep tereproduksi pada GPU dan checkpoint baru;
ketiga seed konsisten. Baseline seri F sah.

**Dampak — dan ini yang paling penting dari entri ini.**

**Varians seed jalur RGB 6,5× LEBIH KECIL daripada yang diandaikan rencana**
(0,0049 vs 0,0321 milik E-027). Konsekuensinya bukan sekadar "ambang diturunkan",
melainkan bahwa **dua pertanyaan yang selama ini tercampur harus dipisah**:

1. **Keterdeteksian statistik.** Dengan SD 0,0049, efek jauh di bawah 0,05 kini
   dapat dibedakan dari derau. Ambang +0,05 setara ~10 SD — menuntutnya sebagai
   syarat *deteksi* berarti membuang efek nyata yang terukur. Untuk F-006/F-007/
   F-009, syarat deteksi yang sah adalah **CI bootstrap tingkat pohon tidak
   memuat nol pada 3 seed berpasangan**, bukan +0,05.
2. **Kebermaknaan praktis.** Ambang +0,05 **tetap berlaku** sebagai bar pengguna,
   dan asalnya bukan derau melainkan pernyataan 21 Juli 2026: "kenaikan 2–5% pun
   dianggap tidak cukup" (CLAUDE.md). Itu keputusan pengguna, bukan artefak
   pengukuran, dan **tidak boleh diturunkan diam-diam** dengan alasan varians
   ternyata kecil.

Maka tiap kontras seri F wajib melaporkan **keduanya**: apakah efeknya nyata, dan
apakah efeknya cukup besar. Efek +0,015 yang CI-nya jelas di atas nol adalah
temuan yang sah dan **wajib dilaporkan apa adanya** — sekaligus wajib dinyatakan
belum memenuhi bar praktis pengguna.

**Replikasi gerbang F-005 pada ketiga seed** (fraksi galat kelas dalam pita
\|Δ\| < 0,6):

| seed | fraksi | p50 \|Δ\| | untung-rugi | B3 | B2 |
|---|---|---|---|---|---|
| 42 | 0,7113 | 0,3633 | 0,849 | 0,8493 | 0,5228 |
| 1337 | 0,6384 | 0,4004 | 0,647 | 0,7760 | 0,5290 |
| 2024 | 0,7147 | 0,3589 | 0,971 | 0,7931 | 0,5375 |

Ketiganya LOLOS jauh di atas ambang 0,30, dan dua pola kualitatifnya bertahan di
seluruh seed: **B3 selalu punya massa lebih besar daripada B2** (kebalikan dari
ramalan rancangan bahwa K2 paling menolong B2↔B3), dan **rasio untung-rugi selalu
< 1** (0,647–0,971), artinya residu ber-clip menyentuh lebih banyak query yang
sudah benar daripada yang salah. K2 karena itu menuntut kepala ordinal yang
benar-benar informatif; residu mendekati acak berekspektasi merugikan.

**Reproduksi** — `bash shell/f004_baseline.sh`. Bukti:
`experiments/results/F-004/{evaluation,metrics,sha256}_seed*.{json,csv,txt}`,
`logits_test_seed*.npz`, dan `results/F-005/massa_selisih_logit_seed*.json`.

## F-007 — (K1a) Cabang frekuensi ber-gate: GATE TIDAK PERNAH TERBUKA (2026-08-06, DIHENTIKAN) · [SR-017](SR/SR-017-sintesis-deep-research.md)

**Status: DIHENTIKAN ATAS PERMINTAAN PENGGUNA** pada 2 dari 12 run. Entri ini
mencatat apa adanya; ia **bukan** hasil lengkap dan tidak boleh dikutip sebagai
uji K1 yang tuntas.

**Hipotesis** — F-002 menunjukkan respons frekuensi tinggi memisahkan isi tandan
dari pelepah pada B4 sebesar +0,0731 di atas kendali. Bila keterpisahan piksel
itu berarti, menyuntikkan fitur frekuensi lewat side encoder sempit sebelum
projector akan menaikkan mAP.

**Cara** — `train/train_rfdetr_freq.py`, cabang samping ber-gate skalar `gamma`
berinisialisasi **nol**, disuntik pada keluaran projector. Resep latih identik
F-004 (1280, batch 8, grad-accum 2, patience 8, EMA, dari `rf-detr-large-2026.pth`).
Rencana 4 lengan x 3 seed; **yang terlaksana hanya 2 lengan pada seed 42.**

**Hasil — dan yang menentukan bukan mAP-nya, melainkan gamma-nya.**

| lengan | epoch | VAL mAP50 (EMA) | TEST mAP50 | **gamma akhir** |
|---|---|---|---|---|
| baseline F-004 seed42 | 14 | 0,5708 | 0,5997 | — |
| dwt seed42 | 12 | 0,5667 | 0,5956 | **+0,0003** |
| laplacian seed42 | 10 (dihentikan) | 0,5698 | — | **−0,00006** |

**Putusan — DIPALSUKAN untuk mekanismenya, bukan sekadar nol hasil.**

`gamma` mulai di nol dan **tidak pernah bergerak dari nol**. Injeksinya
`keluar = fitur + gamma · proyeksi(samping)`; dengan gamma ~ 1e-4 sampai -6e-5,
kontribusi cabang frekuensi **secara efektif nol**. Model perlakuan pada dasarnya
**adalah** model baseline, dan selisih mAP yang terlihat (−0,004) adalah derau
latihan, bukan efek frekuensi.

Ini **bukan** kegagalan implementasi. Uji sambungan membuktikan cabangnya
tersambung: pada gamma dibuka paksa ke 1, keluaran backbone berubah 0,807–1,089;
pada gamma = 0 selisihnya tepat 0,0; parameter pratlatih termuat penuh (14 tak
termuat, semuanya cabang samping). Cabangnya berfungsi — optimizer yang memilih
tidak memakainya.

**Sebab paling mungkin: inisialisasi nol adalah PERANGKAP, bukan sekadar
pengaman.** Gradiennya membentuk kebuntuan ayam-telur:

- gradien ke side encoder = `gamma · dL/dkeluar` → **nol persis saat gamma = 0**,
  jadi side encoder tidak pernah belajar;
- gradien ke gamma = `dL/dkeluar · proyeksi(samping)`, sedangkan `proyeksi(samping)`
  masih **acak** pada inisialisasi → sinyalnya derau di sekitar nol, sehingga
  gamma hanya berjalan acak dan tidak tumbuh.

Rancangan menuntut `gamma = 0` supaya cabang menjadi *no-op* persis dan menjawab
keberatan E-030 (cabang tak berguna tidak boleh merusak baseline). Syarat itu
terpenuhi — tetapi **ongkosnya tidak diantisipasi**: no-op yang sempurna juga
berarti titik mati yang sempurna. Siapa pun yang mengulang gagasan ini harus
mengubah salah satu dari: inisialisasi gamma kecil-tapi-taknol, warmup gamma,
LR terpisah untuk gamma, atau melatih side encoder dengan tugas pendamping
(mis. probe center-heatmap yang ada di rancangan tetapi tidak jadi dipakai).

**Yang TIDAK dapat disimpulkan dari entri ini:**

- Apakah cabang frekuensi akan menolong bila gate-nya benar-benar terbuka —
  **tidak diuji**, karena gate tidak pernah terbuka.
- Perbandingan terhadap kontrol `freq_rendah` dan `fase_diacak` — **kedua lengan
  kontrol tidak pernah dijalankan**, jadi atribusi frekuensi-vs-kapasitas tetap
  terbuka. (Meski dengan gamma ~ 0, kapasitas tambahannya pun efektif tidak
  terpakai.)
- Replikasi seed — hanya seed 42. SD seed baseline 0,0049 (F-004), jadi selisih
  −0,004 berada **di dalam derau satu seed** dan tidak dapat diklaim ke arah mana pun.

**Dampak** — K1 dalam bentuk ini tidak menghasilkan kenaikan, dan alasannya
terdiagnosis: mekanismenya tidak aktif. Ini menurunkan prior untuk seluruh
keluarga "cabang samping ber-gate init-nol" di repo ini, termasuk rancangan
intra-blok yang ditangguhkan.

**Reproduksi** — `bash shell/f007_frekuensi.sh` (hapus dulu penanda
`.selesai` + `.DIHENTIKAN-PENGGUNA` di `runs/detect/runs_f007/*_seed{1337,2024}/`).
Bukti: `experiments/results/F-007/` — `evaluation_{dwt,laplacian}_seed42.json`,
`logits_test_{dwt,laplacian}_seed42.npz`, `uji_sambungan_*.json`, `sha256_*.txt`.
