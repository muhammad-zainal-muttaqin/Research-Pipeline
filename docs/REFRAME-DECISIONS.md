# REFRAME-DECISIONS — Keputusan Reframe Naskah (23 Juli 2026)

Catatan keputusan atas 8 butir revisi dosen (`Revisi-23July2026/Chat.txt`).
Berkas ini **append-only** seperti `docs/EKSPERIMEN.md`: kalau keputusan berubah,
tulis blok baru bertanggal yang merujuk blok lama — jangan sunting blok lama.

Rencana eksekusi penuh (8 fase, kriteria selesai per langkah, tabel risiko) ada di
plan sesi: `~/.claude/plans/jadi-dosen-saya-memberikan-wobbly-sun.md`.

---

## Titik awal — apa yang dosen nilai

Dosen mereview commit **`ea1f277`**, ditandai tag **`versi-dinilai-dosen-2026-07-23`**.

Satu-satunya hal substantif yang belum ia lihat adalah §Pilot experimental findings
(~2.509 kata), yang baru masuk di commit `6332dc1`. Sisa perbedaan adalah sapuan
em-dash. **Kedelapan butir revisi berlaku sama persis pada versi kerja** — tidak ada
pekerjaan yang terbuang karena dosen menilai versi lama.

## Mengapa ini penulisan ulang, bukan penyuntingan

Terverifikasi dari repo pada 23 Juli 2026:

| Fakta | Angka |
|---|---|
| Entri bertema Pertanian di korpus | **3 / 182** (1,6%) |
| Entri menyinggung multi-view / tracking / SfM sama sekali | **9 / 182** — 5 di antaranya deteksi 3D mobil otonom |
| `references.bib`: `counting`, `oil palm`, `citrus`, `grape`, `re-identification`, `yield`, `Suharjito`, `Goh` | **0 masing-masing** |
| Blok sejarah di `evidence-body.tex` | **8.982 kata = 53,7%** naskah |
| Seksi yang mengerjakan tugas target (`evidence-body.tex:212–219`) | **699 kata = 4,2%** |
| Jejak protokol pencarian di repo | **tidak ada** — commit pertama (`4a7661d`, 16 Juli) sudah berisi 202 entri lengkap |
| Struktur naskah vs konvensi CEA | **16 seksi / 9 subseksi** vs median **7 / 22** |
| Record `references.bib` yang punya baris DOI | **2 / 202** |

`evidence-body.tex:16` menyatakan sendiri: *"This review is written as a chronological
history of the field"* — persis anti-pola yang butir 2 larang.

Estimasi: **~75% naskah ditulis ulang, ~90–120 studi baru dicari.** 6–10 minggu paruh waktu.

---

## Keputusan

### K1 — Basis data: satu langganan + dua terbuka

Satu database berlangganan yang tersedia (**Scopus atau WoS** — mana yang dimiliki ULM)
sebagai jangkar, ditambah **OpenAlex** dan **Google Scholar**. Protokol ditulis dalam
dua sintaks (`TITLE-ABS-KEY(...)` untuk Scopus, `TS=(...)` untuk WoS) supaya dapat
dijalankan di mana pun aksesnya tersedia.

**Deviasi dinyatakan terbuka di §2**, tidak disembunyikan. Preseden: dari 8 review CEA
2026 yang dibedah, P2 — paper paling metodologis rigor di sampel — hanya memakai WoS
Core Collection + snowballing, dan P7 hanya memakai Scopus.

> **Terbuka:** database mana persisnya yang tersedia belum dipastikan. Menentukan
> sintaks jangkar dan catatan deviasi mana yang dipakai di §2.2.

### K2 — §Pilot keluar jadi makalah pendamping

`evidence-body.tex:282–325` (§Pilot experimental findings and revised agenda, ~2.509 kata)
dicabut utuh dari naskah tinjauan. Kategori bukti keempat di `evidence-body.tex:53–55`
(paragraf yang memagari pilot) ikut dicabut karena kehilangan rujukannya.

Alasan: **0 dari 8** review CEA pembanding memuat eksperimen penulis sendiri. Naskah
campuran memancing pertanyaan "ini tinjauan atau paper eksperimen?".

**Bahan makalah pendamping sudah lengkap dan aman:**

| Bahan | Lokasi |
|---|---|
| Teks §Pilot | commit `6332dc1`, `evidence-body.tex:282–325` |
| Laporan eksperimen | `docs/LAPORAN-EKSPERIMEN.md` |
| Kode + hasil JSON + split | `experiments/` (E-001…E-020) |
| Log bertanggal | `docs/EKSPERIMEN.md` |
| Prosedur reproduksi | `REPRODUCE.md` |
| Catatan per-SR | `docs/SR/` |

**Efek K2 yang menyelamatkan tesis.** Angka **95,57% Class±1** (koreksi global
k = 1,8905 pada deteksi ground-truth) berasal dari **Tabel 4 makalah SawitMVC**,
*Data in Brief* 67 (2026) 112990, DOI `10.1016/j.dib.2026.112990` — literatur terbit,
bebas dikutip di §5.6. Yang pindah ke makalah pendamping hanya angka penautan eksplisit
milik sendiri (77,13% penampilan / 75,00% kedalaman / 69,50% pose-aware 3D).

Ketiadaannya justru **memperkuat** posisi tinjauan: tidak ada studi terbit yang menguji
penautan eksplisit di rezim ini — itulah gap-nya, dan makalah pendamping yang mengisinya.

### K3 — Framing butir 3: "kapan deduplikasi eksplisit layak dibayar"

Kontribusi utama dibingkai sebagai **pertanyaan ruang desain**, bukan advokasi
deduplikasi eksplisit.

Alasan: baseline terbit sendiri (SawitMVC Tabel 4) menunjukkan koreksi statistik
sederhana mencapai 95,57% Class±1 pada deteksi bersih. Makalah yang mengadvokasikan
deduplikasi geometris sambil menyajikan angka itu di halaman yang sama mudah dipatahkan.
Framing "kapan layak dibayar" konsisten dengan bukti, tidak bisa dibantah angka sendiri,
dan justru merupakan pertanyaan yang hanya bisa dijawab sebuah *design-space review*.

> **Terbuka:** perlu konfirmasi dosen bahwa ini memenuhi maksud "dedup multi-view
> sebagai kontribusi utama".

### K4 — Skala: 6–10 minggu, penulisan ulang penuh

6 set query, Register A ~120–160 studi, 8 seksi, Lampiran A1–A4. Plafon
`references.bib` **260** (rentang sampel CEA 59–286).

---

## Ruang desain yang dipilih

Dua sumbu, dari tiga rancangan independen yang dinilai:

**Sumbu 1 — mekanisme identitas.** M0 intra-view · M1 statistik (non-asosiasi) ·
M2 penampilan/re-ID · M3 gerak/temporal · M4 geometris (back-projection, SfM) ·
M5 multi-view terpelajar.

**Sumbu 2 — asumsi yang dituntut.** A1 tumpang tindih · A2 baseline · A3 kekakuan/
stasioneritas · A4 kalibrasi & skala metrik · A5 keterbedaan penampilan ·
A6 keteraturan duplikasi · A7 oracle identitas.

**Tesis:** pilihan mekanisme ditentukan oleh asumsi mana yang bertahan di rezim
akuisisi tertentu. Itu menjelaskan mengapa M1 menang di kebun sawit 4-sisi (A6 kuat,
A4 gagal) **tanpa** berarti M1 menang di mana-mana.

**Kelas sebagai atribut yang melekat pada identitas** (butir 6): hitungan per kelas
mustahil tanpa instans teridentifikasi. Kematangan = satu kasus; ukuran, mutu, penyakit,
kultivar = kasus lain. Dijaga metodologis lewat kriteria eksklusi (keluaran
non-per-instance dieksklusi), bukan lewat retorika.

**Judul:** *Counting Each Fruit Once: A Design-Space Review of Cross-View Identity for
Class-Wise Fruit Inventories*. Cadangan (usulan dosen): *Multi-View and Multimodal
Perception for Class-Wise Fruit Inventories: A Design-Space Review*.

---

## Garis integritas yang tidak boleh dilanggar

1. **Jangan pernah mengarang corong PRISMA yang berujung di 182.** Query dosen
   dijalankan sungguhan akan mengembalikan himpunan yang hampir tidak beririsan dengan
   korpus lama. Laporkan angka apa adanya, termasuk bila jumlah included jauh di atas
   atau di bawah 182. Reviewer cukup mengulang satu query untuk mematahkan angka palsu.

2. **Dua register asal-usul dilaporkan terpisah.** Register A = studi yang ditinjau
   (masuk corong, punya baris di tabel sintesis). Register B = sitasi latar (R-CNN,
   COCO, KITTI, DETR, NYU Depth v2 — dikutip untuk konteks, tidak masuk corong).
   Label `hand-search-snowballing` **hanya** boleh diberikan bila tautan sitasinya
   dapat disebut konkret dan diverifikasi ke `docs/extracted/`.

3. **Klaim kebaruan dibatasi ke hasil pencarian.** Tulis *"tidak ditemukan dalam
   pencarian yang dilaporkan di §2"*, bukan *"belum ada tinjauan pustaka yang mengangkat
   gap ini"*. Bila Q5 mengembalikan review yang sudah membahasnya, klaim dilemahkan
   apa adanya.

4. **`evidence-body.tex:29` wajib dicabut.** Kalimat itu saat ini secara eksplisit
   menolak PRISMA (*"...rather than a formal systematic review computing a pooled
   statistic under a retrospective PRISMA protocol"*). Menambah diagram alir tanpa
   mencabutnya menghasilkan naskah yang membantah metodenya sendiri di halaman yang sama.

5. **Angka `class_mismatch` nol tetap terlarang** sebagai bukti ambiguitas kelas
   (lihat `CLAUDE.md`). Itu properti konsistensi anotasi pasca-koreksi editorial
   pra-rilis, bukan pengukuran ambiguitas.

---

## Wajib dikonfirmasi ke dosen sebelum FASE 3

1. **Framing butir 3 (K3).** Apakah *"kapan deduplikasi eksplisit layak dibayar"*
   memenuhi maksud "dedup multi-view sebagai kontribusi utama"?

2. **Bentuk klaim kebaruan.** Apakah diterima klaim yang dibatasi ke hasil pencarian
   alih-alih klaim absolut?

3. **Bentuk tabel butir 8.** Apakah **~22 baris di badan + Lampiran A1–A4** memenuhi
   maksud "satu baris per studi di dalam makalah"? Batas teknis: float LaTeX tidak bisa
   pecah antar halaman, dan `longtable` gagal di IEEEtran dua kolom sementara mulus di
   elsarticle satu kolom — padahal satu `evidence-body.tex` di-`\input` kedua driver.
   182 baris di badan mustahil. Preseden: P2 (210 studi → 10 tabel apendiks),
   P8 (Tabel A.1–A.2).

4. **Rujukan butir 7.** Referensi **Suharjito** dan **Goh** yang persis mana (judul/DOI)?
   Nol hit di 202 record; satu-satunya "Goh" di repo adalah **Gabriel Goh**, co-author
   CLIP — false positive. Dan: apakah literatur sawit **berbahasa Indonesia**
   (Sinta/Garuda) masuk scope? Bila ya, itu jalur hand-search terpisah yang wajib
   berlabel sendiri di tabel provenance.

5. **Database (K1).** Bila ULM tidak berlangganan Scopus maupun WoS, apakah dosen
   menerima OpenAlex sebagai indeks utama dengan deviasi yang dinyatakan terbuka?
   Ia menulis "minimal SCOPUS/WOS".

---

## Utang teknis yang ditemukan sepanjang analisis (bukan bagian revisi)

Ditemukan saat memverifikasi butir 8, dicatat supaya tidak hilang:

- **Inkonsistensi jumlah klaster tema**, sudah ada sebelum revisi ini:
  `CLAUDE.md` menulis **14**, `TEMUAN.md:91` menulis **17**, nama berkas `entri/`
  menghasilkan **17**, `docs/evidence-matrix-182.csv` menghasilkan **18** (6 entri
  tanpa baris `| Tema |` jatuh ke kategori "Uncoded"). Tabel sintesis akan memaparkan
  ini di depan reviewer — harus direkonsiliasi sebelum FASE 4.
- **`docs/evidence-matrix-182.csv` tidak bisa diekspor apa adanya** ke tabel LaTeX:
  keempat kolom prosa terpotong pada 460 karakter (rata-rata 461, maks 462 — hampir
  semua sel putus di tengah kalimat), isinya Bahasa Indonesia, dan kolom
  `task`/`modality` hasil heuristik kata kunci yang ~24% barisnya jatuh ke kategori
  sampah (YOLOv1 diklasifikasikan "Computer-vision method or application").
- **`tools/build_evidence_matrix.py`** di-drive dari `PDF/benar/*.pdf` yang tidak ada
  di git, dan `fields = list(rows[0])` crash bila `rows` kosong.
- **SawitMVC belum jadi record BibTeX** — dikutip sebagai teks biasa di
  `evidence-body.tex:285`.
- **`he2021ffb6d`** (6D pose) akan lolos setiap grep "FFB" — jebakan audit otomatis.
- **Nama berkas figur memuat komoditas**: `F07-funnel-sawit`, `F08-pipeline-sawit`.
