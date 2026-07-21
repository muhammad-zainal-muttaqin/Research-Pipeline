# Catatan Eksperimen — SawitMVC

Log eksperimen yang **hanya bertambah** (*append-only*). Entri lama tidak diedit
untuk "memperbaiki" hasil; kalau kesimpulan berubah, tulis entri baru yang
merujuk entri lama.

**Hasil negatif wajib dicatat.** Justru itu isi paling berharga di sini — ia
mencegah jalan buntu yang sama ditempuh dua kali, dan menjawab pertanyaan
reviewer "apa saja yang sudah dicoba".

Kode eksperimen ada di `/workspace/experiments/` (di luar repo ini; repo ini
mencatat apa yang dipelajari, bukan menampung artefak besar).

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
