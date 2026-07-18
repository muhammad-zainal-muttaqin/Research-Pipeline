# PLAN — Penulisan Tinjauan Pustaka (`main.tex`, IEEEtran)

> Rencana kerja untuk menulis **ulang total** naskah tinjauan pustaka dari 202 entri
> di `entri/`, dalam bentuk **artikel jurnal LaTeX** (`main.tex`, kelas `IEEEtran`),
> disusun sebagai **sintesis tematik** yang menyempit (*funnel*) menuju celah riset:
> **YOLO dengan modifikasi arsitektur RGB → RGB-D untuk *counting* dan klasifikasi
> buah sawit**. Tinjauan tetap luas atas seluruh 202 literatur; angle sawit menjadi
> muara, bukan pembatas cakupan.
>
> Dokumen ini adalah **rencana**, bukan naskahnya. Naskah (`main.tex` + `figures/`)
> ditulis pada fase eksekusi (§6). `PLAN.md` (rencana web *reading room* `index.html`)
> berbeda dan tidak disentuh.

---

## 1. Tujuan & Hasil Akhir

| Aspek | Target |
|---|---|
| Berkas utama | `main.tex` (`IEEEtran`) + `main-elsarticle.tex` (Elsevier), keduanya `\input{body}` |
| Bibliografi | `references.bib` (202 entri, sudah ada) via `\bibliographystyle{IEEEtran}` |
| Figur | Folder `figures/` — sumber mermaid + brief siap-Gemini + hasil `*.pdf/png` |
| Gaya | Sintesis tematik akademik, *funnel* ke gap sawit |
| Cakupan | **Seluruh 202 entri disitasi** minimal sekali (0 sitasi menggantung, 0 sitasi yatim) |
| Bahasa | Indonesia baku PUEBI, nada buku teks, anti-slop |
| Kompilasi | Overleaf / *runner* remote — **tanpa `pdflatex` lokal** (GateGuard aktif) |
| Panjang sasaran | ± 9.000–12.000 kata isi + 8 figur konsep + 2 chart + 3 tabel |

**Non-goal:** bukan anotasi 202 entri satu per satu; bukan mengubah `entri/`,
`references.bib`, `TEMUAN.md`, atau `PLAN.md`.

---

## 2. Pilihan Kelas Dokumen

**Rekomendasi utama: `IEEEtran` (mode `journal`).** Alasan: format paling lazim untuk
karya deteksi objek/visi komputer (YOLO, DETR, RGB-D SOD banyak terbit di venue IEEE),
satu berkas `main.tex`, dua kolom, integrasi `references.bib` bersih, dan gaya
artikel-tinjauan cocok untuk IEEE Access.

**Alternatif satu-baris (ganti bila venue berubah):** Elsevier `elsarticle`
(`\documentclass[review]{elsarticle}`) — sesuai *Computers and Electronics in
Agriculture*, venue alami untuk aplikasi panen sawit. Struktur isi & figur di rencana
ini tidak berubah; hanya preamble dan gaya bibliografi yang disesuaikan.

**Realisasi — arsitektur isi-bersama (dua driver, satu isi).** Agar versi IEEE dan
Elsevier tidak pernah menyimpang (kritis untuk integritas 202 sitasi), isi naskah
diekstrak ke satu berkas bersama `body.tex` (12 `\section`, seluruh `\cite`, tabel,
figur). Dua *driver* tipis memakainya:
- `main.tex` — preamble `IEEEtran` + frontmatter IEEE + `\input{body}` + `\bibliographystyle{IEEEtran}`.
- `main-elsarticle.tex` — preamble `elsarticle` + `\begin{frontmatter}` Elsevier + `\input{body}` + `\bibliographystyle{elsarticle-num}`.

Agar `body.tex` netral-kelas: baris pembuka bab memakai makro `\dropstart{H}{uruf}`
(bukan `\IEEEPARstart` langsung), dan tiap driver mendefinisikannya sesuai kelas
(IEEE → drop cap; Elsevier → cetak biasa). Makro `\figplace` juga didefinisikan di
tiap driver. Edit isi cukup di `body.tex` sekali → kedua venue ikut.

**Kerangka `main.tex`:**

```
\documentclass[journal]{IEEEtran}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}
\usepackage[bahasa]{babel}
\usepackage{graphicx,float,booktabs,longtable,array,multirow,amsmath,amssymb}
\usepackage{url}\usepackage[hidelinks]{hyperref}
% opsional chart reproducible: \usepackage{pgfplots}\pgfplotsset{compat=1.18}
\begin{document}
\title{...}\author{...}\markboth{...}{...}\maketitle
\begin{abstract}...\end{abstract}
\begin{IEEEkeywords} YOLO, RGB-D, deteksi objek, fusi lintas-modal, panen sawit \end{IEEEkeywords}
% 12 \section (lihat §4)
\bibliographystyle{IEEEtran}\bibliography{references}
\end{document}
```

Naskah lama `tinjauan-pustaka.tex` **digantikan** oleh `main.tex`; berkas lama
dibiarkan (arsip), tidak dihapus tanpa konfirmasi.

---

## 3. Prinsip Penulisan

1. **Funnel.** Umum (fondasi deteksi RGB) → menyempit (fusi RGB-D, deteksi buah) →
   gap spesifik sawit → posisi riset penulis. Setiap bagian ditutup satu kalimat
   penghubung ke tujuan sawit agar benang merah terjaga.
2. **Sintesis, bukan anotasi.** Disusun per tema. Karya representatif tiap tema
   dibahas mendalam (mekanisme + angka kunci + interpretasi); karya lain diringkas
   dalam kalimat pengelompok atau baris tabel — **tetapi semuanya tetap `\cite`**.
3. **Kejujuran akademik.** Hanya fakta yang terverifikasi di bab sumber. Angka yang
   perlu cek volume/halaman/DOI ditandai di catatan (warisi "Catatan integritas"
   `TEMUAN.md`). Tidak mengarang angka/dataset/hasil.
4. **Bahasa.** Indonesia baku PUEBI; istilah asing dicetak miring pada kemunculan
   pertama (*bounding box*, *backbone*, *cross-modal attention*); desimal koma
   (`63,4\%`); nada impersonal. Poles akhir dengan skill `stop-slop-id` (hapus frasa
   pengisi & hiperbola). Mengadaptasi semangat `PANDUAN-PENULISAN.md` (bukan template
   10-bagiannya, yang khusus untuk bab `entri/`).
5. **Sumber isi.** Untuk tiap bagian, tarik dari bab `entri/` yang relevan: ambil
   inti dari "Gambaran Umum", klaim aman dari "Poin untuk Sitasi", dan angka dari
   "Eksperimen dan Hasil". Sintesiskan, jangan salin-tempel.

---

## 4. Struktur Naskah — 12 Bagian

Kolom "Entri" merujuk nomor berkas di `entri/`; pemetaan lengkap & saling lepas di
Lampiran A. Kolom "Figur" merujuk daftar di §5.

| # | `\section` | Isi inti | Entri | Figur |
|---|---|---|---|---|
| 1 | Pendahuluan | Konteks sawit & pertanian presisi; keterbatasan RGB murni; janji RGB-D; tujuan & pertanyaan tinjauan; metodologi penelusuran; struktur naskah | 146, 151 | F1, F7 |
| 2 | Fondasi Deteksi Objek RGB | Dua-tahap (R-CNN→Faster) → satu-tahap (SSD, RetinaNet) → anchor-free (FCOS, CenterNet) → transformer (DETR & turunan, ViT, Swin, ConvNeXt) | 12–25, 147, 149, 155, 157–165, 193–194 | F3 |
| 3 | Evolusi & Survei YOLO | v1→YOLO26: anchor-free, bebas-NMS, atensi; ringkasan survei; argumen YOLO sebagai kandidat *backbone* sawit | 1–11, 26–34, 156, 192 | F2 |
| 4 | Estimasi Kedalaman & Sumber *Depth* | Monokular klasik→fondasi (MiDaS, DPT, Depth Anything, metrik); *pseudo-depth* murah membuka RGB-D tanpa sensor khusus di kebun | 62–72, 175–179, 198–202 | — |
| 5 | Fusi RGB–Depth: Prinsip & Strategi | Taksonomi fusi awal/menengah/akhir; atensi lintas-modal; bukti dari RGB-D SOD & segmentasi RGB-D; dataset RGB-D inti | 35–61, 141–143, 153, 166–174, 196–197 | F4, F6 |
| 6 | Persepsi 3D & Geometri | Pose 6D, *grasp* robotik, deteksi 3D LiDAR–kamera, RGB-D SLAM; relevansi: lokalisasi 3D buah untuk panen robotik | 73–99, 107–111, 144–145, 148, 180–188, 190–191 | — |
| 7 | Pelajaran Fusi Multimodal Lain | Pedestrian RGB-T (ketidakseimbangan & penyelarasan modalitas); survei multimodal; transfer pelajaran ke RGB-D | 100–106, 150, 152, 154, 189 | — |
| 8 | Integrasi YOLO + RGB-D | Dua pola: perluasan kanal masukan vs deteksi-lalu-proyeksi; bukti keuntungan oklusi & lokalisasi 3D — **inti tinjauan** | 112–119 | F5 |
| 9 | Aplikasi YOLO Lintas Domain | Pertanian/buah (utama), medis, industri, *remote sensing*; menyempit ke deteksi & lokalisasi buah RGB-D | 120–140, 195 | C1, C2 |
| 10 | Sintesis & Celah Riset | Rangkuman lintas-tema; identifikasi gap sawit; posisi & kontribusi riset penulis | lintas-tema | F7, F8 |
| 11 | Tantangan Terbuka & Arah Masa Depan | Kualitas/penyelarasan depth di lapangan; efisiensi *edge*; *pseudo-depth* fondasi; ketahanan hilang-modalitas; dataset sawit RGB-D | lintas-tema | — |
| 12 | Kesimpulan | Jawaban ringkas atas pertanyaan tinjauan; jembatan ke riset lanjutan | — | — |

**Tabel dalam naskah:** (T1) taksonomi tematik 14 klaster; (T2) evolusi YOLO v1→YOLO26
(tahun, kebaruan, catatan); (T3) strategi fusi RGB-D (awal/menengah/akhir: mekanisme,
kelebihan, keterbatasan, contoh karya).

---

## 5. Sistem Figur (Konsisten Tema, Siap-Gemini)

Semua figur berbagi **satu tema visual** agar seragam. Alurnya: tulis spesifikasi tema
sekali → tiap figur punya *brief* + sumber mermaid → kirim ke Gemini → simpan hasil →
sisipkan ke `main.tex`.

### 5.1 Berkas tema tunggal — `figures/THEME.md`

Satu sumber kebenaran gaya yang **dirujuk semua brief**:

- **Palet** (selaras `PLAN.md` §13): aksen merah bata `#A03028`; tinta `#1A1D21`;
  kertas `#FAF9F6`; hairline `#E6E3DA`; satu *jewel-tone* per tema (17 hue di
  `PLAN.md` §13, mis. Fondasi RGB `#2B6CB0`, Fusi `#8B5CB4`, Kedalaman `#A6740E`).
- **Tipografi:** judul figur serif (Newsreader/Georgia); label sans; angka/kode mono.
- **Kaidah:** garis *hairline* 1–1,5 pt; tanpa bayangan berat/gradasi mencolok; sudut
  membulat halus; latar kertas; orientasi lanskap; rasio, tebal garis, ukuran node,
  dan margin seragam antar-figur; tanpa emoji.
- **Ekspor:** PDF vektor (utama, untuk LaTeX) atau PNG ≥300 dpi; nama `figures/FNN-slug.pdf`.

### 5.2 Daftar figur

Konsep (diagram) dan chart (data). Nomor figur = urutan kemunculan.

| ID | Judul | Jenis | Sumber data/konten |
|---|---|---|---|
| F1 | Taksonomi 4 poros / 14 klaster | pohon / *mind-map* | `TEMUAN.md` §4 |
| F2 | Garis waktu evolusi YOLO v1→YOLO26 | *timeline* | entri 1–11, 156, 192 |
| F3 | Silsilah detektor RGB (dua-tahap→satu-tahap→anchor-free→DETR) | pohon | entri 12–25, 155–165 |
| F4 | Tiga strategi fusi RGB-D (awal/menengah/akhir) | diagram blok | §5 + T3 |
| F5 | Dua pola YOLO+RGB-D (perluasan kanal vs deteksi-lalu-proyeksi) | diagram alur | entri 112–119 |
| F6 | Skema atensi lintas-modal | diagram blok | entri 55, 46, 58 |
| F7 | Funnel: survei umum → gap sawit | *funnel* | §10 |
| F8 | Pipeline usulan: YOLO RGB-D untuk *counting*/klasifikasi sawit | diagram alur | §10 |
| C1 | Distribusi entri per tahun (2012–2026) | *bar chart* | `entri/INDEX.md` |
| C2 | Distribusi entri per tema (17 tema) | *bar chart* | nama berkas `entri/` |

### 5.3 Brief per figur — `figures/FNN-slug.md`

Tiap brief memuat, urut:

1. **Tujuan & tempat** — figur ini menjelaskan apa, dirujuk di `\section` mana.
2. **Konten faktual** — daftar node & edge (untuk diagram) atau pasangan angka (untuk
   chart), diambil dari sumber di tabel §5.2. Tidak ada angka karangan.
3. **Rujukan tema** — "ikuti `figures/THEME.md`" (palet, tipografi, kaidah).
4. **Prompt siap-tempel Gemini** — instruksi menghasilkan figur (SVG/PDF vektor
   resolusi tinggi) memakai palet & kaidah tema, beserta konten faktual butir 2.
5. **Sumber mermaid** — kode mermaid sebagai spesifikasi kebenaran struktur sekaligus
   *fallback* bila figur Gemini belum siap (mermaid dapat dirender langsung).

Contoh kerangka prompt Gemini (diisi per figur):

```
Buat figur vektor (SVG/PDF) untuk artikel jurnal IEEE, orientasi lanskap.
Tema WAJIB konsisten: latar kertas #FAF9F6; garis & teks tinta #1A1D21; aksen
#A03028; pemisah hairline #E6E3DA; tanpa bayangan/gradasi; sudut membulat halus;
label sans, angka mono. Konten (struktur pasti — jangan tambah/kurangi node):
<tempel konten faktual butir 2>. Tata letak rapi, spasi seragam, kontras AA.
```

### 5.4 Integrasi LaTeX

Sisipkan via `\includegraphics` dalam `figure` (satu kolom) atau `figure*` (rentang
dua kolom IEEEtran untuk figur lebar seperti F3/F5), dengan `\caption` + `\label`.
Chart C1/C2 boleh alternatif native `pgfplots` bila ingin reproducible tanpa Gemini.

---

## 6. Alur Kerja Penulisan (Fase Eksekusi)

1. **Verifikasi pemetaan** entri→bagian (Lampiran A) terhadap `references.bib`: pastikan
   tiap nomor 001–202 punya kunci BibTeX dan masuk tepat satu bagian.
2. **Preamble `main.tex`** + judul, penulis, abstrak, `IEEEkeywords`.
3. **Draf per bagian §4** secara berurutan: baca bab sumber → sintesis → sisip
   `\cite{kunci}`. Bagian 8 (YOLO+RGB-D) dan 10 (gap sawit) ditulis paling cermat.
4. **Tabel T1–T3** disusun dari `TEMUAN.md` dan bab sumber.
5. **Figur:** tulis `figures/THEME.md` → tiap `figures/FNN-*.md` (brief + mermaid) →
   generate via Gemini → simpan → `\includegraphics`.
6. **Bagian 10 sebagai muara:** rangkum temuan lintas-tema → nyatakan gap (belum ada
   dataset/metode sawit RGB-D beranotasi; tandan buah tertumpuk & oklusi pelepah;
   cahaya matahari kuat mendegradasi *depth* sensor; kebutuhan *counting* akurat pada
   tandan padat) → posisi & kontribusi riset penulis.
7. **Poles anti-slop** seluruh naskah (`stop-slop-id`); rapikan konsistensi istilah.

---

## 7. Integritas Sitasi & Verifikasi

Karena `pdflatex` lokal tidak tersedia (GateGuard), verifikasi utama berbasis teks:

- **0 sitasi menggantung:** setiap kunci di `\cite{...}` dalam `body.tex`
  (yang diinput oleh `main.tex` dan `main-elsarticle.tex`) ada di `references.bib`.
- **0 sitasi yatim:** setiap kunci `@...{key,` di `references.bib` dirujuk ≥1× di
  `body.tex` → menjamin **202 entri terbahas**.
- **Cek berbasis `grep` (lokal, tanpa kompilasi):** ekstrak kunci `\cite` dari
  `body.tex` dan kunci `@` dari `references.bib`, bandingkan dua himpunan (selisih dua
  arah harus kosong).
- **Kompilasi PDF:** dilakukan pengguna via **Overleaf** (unggah `main.tex` +
  `references.bib` + `figures/`) atau *runner* remote. Urutan: `pdflatex` → `bibtex`
  → `pdflatex` → `pdflatex`.
- **Cek figur:** tiap figur di §5.2 punya berkas *brief* + sumber mermaid, dan semua
  *brief* merujuk `figures/THEME.md`.

---

## 8. Berkas yang Dibuat/Diubah

- **Dibuat:** `body.tex` (isi bersama, 202 `\cite`, 0 menggantung/0 yatim terverifikasi);
  `main.tex` (driver IEEEtran); `main-elsarticle.tex` (driver Elsevier cadangan);
  `figures/THEME.md`; `figures/F01-*.md` … `figures/C02-*.md` (10 *brief* dengan mermaid +
  prompt Gemini; chart C01/C02 punya *fallback* pgfplots); `figures/*.pdf|png` (hasil generate,
  masih perlu digenerate via Gemini).
- **Dipakai apa adanya (tidak diubah):** `references.bib`, `entri/*`, `TEMUAN.md`,
  `PLAN.md`, `PANDUAN-PENULISAN.md`.
- **Diarsipkan:** `tinjauan-pustaka.tex` (digantikan `main.tex`; tidak dihapus tanpa
  konfirmasi).

---

## 9. Risiko & Catatan

- Sintesis tematik menjaga panjang tetap wajar; hindari melebar jadi 202 anotasi.
- Metadata bibliografi (volume/halaman/DOI) perlu verifikasi akhir sebelum submit formal.
- Figur Gemini harus dicek terhadap sumber mermaid agar struktur tetap faktual (tidak
  ada node/relasi tambahan yang mengubah makna).
- `PANDUAN-PENULISAN.md` melarang gambar hanya untuk bab web `entri/`; `main.tex`
  (LaTeX) bebas memuat figur.
- Bila venue berubah ke Elsevier, ganti preamble ke `elsarticle` dan gaya bib; isi &
  figur tetap.

---

## Lampiran A — Pemetaan Entri → Bagian (partisi lengkap 001–202)

Setiap entri muncul **tepat satu kali**; total 202 (jaminan 0 yatim).

- **§1 Pendahuluan:** 146, 151
- **§2 Fondasi RGB:** 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 147, 149,
  155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 193, 194
- **§3 Evolusi & Survei YOLO:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 26, 27, 28, 29, 30,
  31, 32, 33, 34, 156, 192
- **§4 Estimasi Kedalaman:** 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 175, 176, 177,
  178, 179, 198, 199, 200, 201, 202
- **§5 Fusi RGB–Depth:** 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
  51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 141, 142, 143, 153, 166, 167, 168, 169,
  170, 171, 172, 173, 174, 196, 197
- **§6 Persepsi 3D & Geometri:** 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
  87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 107, 108, 109, 110, 111, 144, 145,
  148, 180, 181, 182, 183, 184, 185, 186, 187, 188, 190, 191
- **§7 Fusi Multimodal Lain:** 100, 101, 102, 103, 104, 105, 106, 150, 152, 154, 189
- **§8 YOLO + RGB-D:** 112, 113, 114, 115, 116, 117, 118, 119
- **§9 Aplikasi Lintas Domain:** 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
  131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 195
- **§10–§12:** menyintesis lintas-tema (tanpa entri "milik" eksklusif).

Verifikasi hitung: 2 + 28 + 22 + 21 + 42 + 46 + 11 + 8 + 22 = **202**.
