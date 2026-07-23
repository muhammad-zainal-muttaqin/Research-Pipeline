# PROTOCOL — Protokol Pencarian Literatur

**Status: DRAF, BELUM DIJALANKAN.** Setiap angka corong di `prisma-counts.csv` masih
kosong. Jangan mengutip apa pun dari berkas ini ke naskah sebelum FASE 1.2–1.5 selesai.

Tinjauan: *Counting Each Fruit Once: A Design-Space Review of Cross-View Identity for
Class-Wise Fruit Inventories*.
Keputusan yang melatarbelakangi: [`../REFRAME-DECISIONS.md`](../REFRAME-DECISIONS.md).

---

## 1. Jenis tinjauan dan standar pelaporan

**Structured design-space review** dengan pencarian berbasis basis data yang dilaporkan
mengikuti alur PRISMA 2020 **untuk tahap pencarian dan seleksi saja**. Ini bukan
*systematic review* dengan penilaian mutu bukti formal dan bukan meta-analisis: tidak
ada statistik gabungan yang dihitung, karena studi yang ditinjau memakai objek, sensor,
dan metrik yang tidak sebanding.

Protokol tidak diregistrasi sebelumnya. Dari 8 review *Computers and Electronics in
Agriculture* 2026 yang dibedah (`Revisi-23July2026/`), **0/8** meregistrasi protokol,
**5/8** menyebut PRISMA, tetapi **8/8** menyebut basis data dan **8/8** menyatakan
kriteria seleksi. Bar venue ada di "transparan dan dapat direproduksi", bukan Cochrane.

## 2. Basis data

| Peran | Sumber | Catatan |
|---|---|---|
| Jangkar | **Scopus** *atau* **Web of Science Core Collection** | Mana yang tersedia lewat langganan institusi. Query ditulis dalam dua sintaks. |
| Pelengkap | **OpenAlex** (REST API, terbuka) | Dipakai juga untuk pengayaan DOI record lama (FASE 1.4). |
| Pelengkap | **Google Scholar** | Hanya untuk *forward/backward snowballing* dan penemuan literatur abu-abu; **tidak** dipakai sebagai sumber corong utama karena hasilnya tidak dapat diekspor secara stabil. |

**Deviasi yang harus dinyatakan di §2.2 naskah:** hanya satu dari Scopus/WoS yang
dipakai. Preseden di sampel venue: P2 (paper paling rigor) hanya WoS; P7 hanya Scopus.

**Catatan sintaks yang wajib dilaporkan:** `TS=` pada WoS mencakup *Keywords Plus*
(istilah yang dihasilkan otomatis dari judul referensi), sedangkan `TITLE-ABS-KEY` pada
Scopus tidak. Recall WoS karena itu lebih besar untuk query yang sama. Perbedaan ini
dicatat, bukan dihaluskan.

**Rentang tahun:** 2015–2026 (`PUBYEAR > 2014` / `PY=2015-2026`), mengikuti contoh dosen.
Karya fondasi sebelum 2015 boleh dikutip sebagai **Register B** (sitasi latar) tetapi
tidak masuk corong.

**Tanggal pencarian** dicatat per query di `raw/<db>_<qid>_<YYYY-MM-DD>.csv`.

---

## 3. Set query

**Tujuh set** (Q1–Q6 asli; **Q7 ditambahkan 2026-07-23**, lihat D-2/D-4), masing-masing
menjawab satu bagian ruang desain. Q1 mempertahankan struktur contoh dosen agar
keterkaitannya terlihat.

Versi siap-tempel satu baris untuk kotak Scopus ada di
[`scopus-queries.md`](scopus-queries.md).

### Q1 — Inventaris/penghitungan buah dari banyak observasi *(inti pertanian)*

**Scopus**
```
TITLE-ABS-KEY(
  ("fruit" OR "fresh fruit bunch" OR "FFB" OR "oil palm" OR "apple" OR "citrus"
   OR "mango" OR "grape" OR "berry" OR "bunch" OR "cluster" OR "crop")
  AND
  ("count*" OR "yield estimation" OR "load estimation" OR "fruit load"
   OR "inventory" OR "enumeration")
  AND
  ("multi-view" OR "multiple view*" OR "multi-camera" OR "video" OR "cross-view"
   OR "structure from motion" OR "SfM" OR "track*" OR "3D reconstruction"
   OR "image sequence")
)
AND PUBYEAR > 2014
```

**Web of Science** — ganti `TITLE-ABS-KEY(` → `TS=(`, `AND PUBYEAR > 2014` →
`AND PY=(2015-2026)`. Berlaku untuk Q1–Q6.

### Q2 — Asosiasi lintas-view dan anti-duplikasi *(mekanisme, non-pertanian diizinkan)*

```
TITLE-ABS-KEY(
  ("multi-view" OR "cross-view" OR "multi-camera" OR "multiple cameras"
   OR "overlapping view*" OR "multi-sensor")
  AND
  ("re-identification" OR "data association" OR "identity" OR "duplicate*"
   OR "deduplicat*" OR "double counting" OR "correspondence" OR "instance matching"
   OR "track*" OR "association")
  AND
  ("object detection" OR "instance segmentation" OR "counting" OR "instance"
   OR "pedestrian" OR "vehicle")
)
AND PUBYEAR > 2014
```

Set inilah yang mengisi §5.2–5.5, tempat korpus lama **nol**. Bila hasilnya kurus,
lihat gerbang keputusan R2 di plan (ciutkan sumbu asumsi 7 → 3–4 **sebelum** menulis).

### Q3 — Multimodalitas dan geometri untuk tanaman

```
TITLE-ABS-KEY(
  ("RGB-D" OR "depth camera" OR "stereo vision" OR "LiDAR" OR "point cloud"
   OR "monocular depth" OR "photogrammetry" OR "structure from motion")
  AND
  ("fruit" OR "orchard" OR "vineyard" OR "canopy" OR "plant" OR "tree crop"
   OR "plantation" OR "oil palm")
  AND
  ("detection" OR "segmentation" OR "localization" OR "counting" OR "phenotyping"
   OR "harvesting")
)
AND PUBYEAR > 2014
```

### Q4 — Kelas per-instans di luar kematangan *(butir 6)*

```
TITLE-ABS-KEY(
  ("fruit" OR "produce" OR "crop" OR "bunch")
  AND
  ("maturity" OR "ripeness" OR "grading" OR "grade" OR "quality class*"
   OR "size class*" OR "defect" OR "disease" OR "cultivar" OR "variety")
  AND
  ("instance segmentation" OR "object detection" OR "per-instance" OR "individual fruit"
   OR "bounding box" OR "per-object")
)
AND PUBYEAR > 2014
```

### Q5 — Tinjauan terdahulu *(positioning, butir 3)*

```
TITLE(("review" OR "survey" OR "systematic review" OR "scoping review"))
AND TITLE-ABS-KEY(
  ("fruit detection" OR "fruit counting" OR "yield estimation" OR "oil palm"
   OR "orchard" OR "crop monitoring" OR "agricultural robot*" OR "precision agriculture")
  AND
  ("deep learning" OR "computer vision" OR "object detection" OR "machine vision")
)
AND PUBYEAR > 2014
```

**Aturan pemakaian hasil Q5.** Tiap review yang masuk dikodekan pada satu pertanyaan:
*apakah identitas/duplikasi lintas-view diperlakukan sebagai masalah kelas satu?*
Jawabannya jadi kolom terakhir Tabel 1. Bila ada yang menjawab "ya", klaim kebaruan
**dilemahkan apa adanya** — jangan disembunyikan.

### Q6 — Seed sawit *(butir 7)*

> **Direvisi 2026-07-23 (D-5).** Klausa kedua yang lama (`yield` / `plantation` /
> `harvest*`) adalah istilah agronomi dan menjaring literatur agronomi, biologi, dan
> ekonomi minyak sawit — 15.609 record di OpenAlex. Diganti klausa pencitraan/ML yang
> **wajib**. Versi lama disimpan verbatim di D-5, tidak dihapus.

```
TITLE-ABS-KEY(
  ("oil palm" OR "elaeis guineensis" OR "fresh fruit bunch" OR "FFB")
  AND
  ("deep learning" OR "machine learning" OR "convolutional" OR "neural network"
   OR "computer vision" OR "image processing" OR "YOLO" OR "object detection"
   OR "remote sensing")
)
AND PUBYEAR > 2014
```

### Q7 — Penghitungan buah pandangan-tunggal / estimasi hasil *(butir 7)*

> **Ditambahkan 2026-07-23 (D-2, dijalankan di D-4).** Q1 mensyaratkan klausa
> multi-view dan Q4 mensyaratkan klausa atribut kelas, sehingga keduanya melewatkan
> baseline penghitungan citra-tunggal (terbukti: Koirala 2019 MangoYOLO lolos dari
> keduanya). Literatur ini dibutuhkan dua kali — sebagai kelas pembanding M0/M1 di §5,
> dan untuk memenuhi butir 7 (penghitungan apel/jeruk/anggur).

```
TITLE-ABS-KEY(
  ("fruit" OR "apple" OR "citrus" OR "mango" OR "grape" OR "berry" OR "bunch"
   OR "oil palm" OR "orchard" OR "vineyard")
  AND
  ("counting" OR "count" OR "yield estimation" OR "load estimation" OR "fruit load"
   OR "crop load")
  AND
  ("deep learning" OR "convolutional" OR "object detection" OR "YOLO"
   OR "instance segmentation" OR "machine vision")
)
AND PUBYEAR > 2014
```

Ditambah pencarian penulis terpisah, dicatat sebagai jalur tersendiri:
`AUTHOR-NAME("Suharjito")` dan `AUTHOR-NAME("Goh")` dibatasi ke subjek pertanian /
ilmu komputer. **Peringatan:** "Goh" adalah nama yang sangat umum, dan satu-satunya
"Goh" di repo saat ini adalah **Gabriel Goh** (co-author CLIP) — false positive.
Rujukan persisnya harus dikonfirmasi ke dosen sebelum jalur ini dijalankan.

**Terbuka:** apakah literatur sawit berbahasa Indonesia (Sinta/Garuda) masuk scope.
Bila ya, itu jalur hand-search terpisah dengan label provenance sendiri.

---

## 4. Kriteria inklusi

| Kode | Kriteria |
|---|---|
| **IC1** | Artikel riset yang telah ditinjau sejawat, atau praregistrasi/preprint dengan teks penuh tersedia dan hasil kuantitatif. |
| **IC2** | Memuat komponen persepsi visual yang menghasilkan keluaran **per-instans** (deteksi, segmentasi instans, pelacakan), **atau** membahas mekanisme asosiasi/identitas lintas-observasi. |
| **IC3** | Terbit 2015–2026. |
| **IC4** | Berbahasa Inggris atau Indonesia. |
| **IC5** | Hasil dapat diverifikasi dari teks penuh: dataset, protokol evaluasi, dan metrik dilaporkan. |

## 5. Kriteria eksklusi

| Kode | Kriteria |
|---|---|
| **EC1** | Keluaran bukan per-instans (klasifikasi tingkat-citra, regresi jumlah global) **dan** tidak membahas identitas/duplikasi lintas-observasi. |
| **EC2** | Tidak ada evaluasi kuantitatif. |
| **EC3** | Teks penuh tidak dapat diperoleh. *(Aturan repo melarang mengutip dari abstrak saja.)* |
| **EC4** | Duplikat, atau versi lebih awal dari record yang sudah masuk. |
| **EC5** | Bukan artikel riset: editorial, abstrak konferensi, poster, paten, buku teks. |
| **EC6** | Di luar rentang tahun. |

Setiap eksklusi pada tahap teks penuh dicatat dengan **satu kode alasan**. Eksklusi pada
tahap judul–abstrak dicatat sebagai agregat per kode.

---

## 6. Uji known-item *(FASE 1.2 — WAJIB sebelum ekspor)*

Query dianggap lolos hanya bila mengembalikan keempat item berikut. Kalau tidak, query
diperbaiki dan **versi yang gagal dicatat beserta alasannya di berkas ini**, bukan dihapus.

| Item | Rujukan | Query yang harus menemukannya |
|---|---|---|
| Gené-Molá dkk. 2020, deteksi buah + SfM | *Comput. Electron. Agric.* 169:105165 | Q1 dan/atau Q3 |
| Koirala dkk. 2019, MangoYOLO | *Precis. Agric.* 20(6):1107–1135 | Q1 dan/atau Q4 |
| Suharjito **dan** Goh | *(judul/DOI menunggu konfirmasi dosen)* | Q6 |
| Indriani dkk. 2026, SawitMVC | `10.1016/j.dib.2026.112990` | Q1 |

Alasan uji ini murah tapi menyelamatkan: ia memeriksa bahwa query benar-benar mencakup
ruang desain sebelum ribuan record disaring, dan ia satu-satunya cara memastikan butir 7
dosen benar-benar terjaring.

---

## 7. Prosedur penyaringan

1. **Ekspor mentah** per (database × query) → `raw/<db>_<qid>_<YYYY-MM-DD>.csv`, di-commit.
2. **Deduplikasi dalam-query**, lalu **antar-sumber**: kunci utama **DOI ternormalisasi**
   (huruf kecil, buang prefiks `https://doi.org/`); untuk record tanpa DOI, kunci
   cadangan = judul ternormalisasi (huruf kecil, buang tanda baca dan spasi) + tahun.
   Kecocokan judul di bawah ambang diperiksa manual — **jangan otomatiskan sepenuhnya**.
3. **Saringan judul–abstrak** (tahap 1) → terapkan EC1, EC5, EC6.
4. **Saringan teks penuh** (tahap 2) → terapkan IC1–IC5 dan EC2, EC3, EC4.
5. **Snowballing** maju dan mundur dari studi yang masuk, dilabeli terpisah.
6. Setiap tahap dicatat sebagai baris di `prisma-counts.csv` (append-only).

Penyaring tunggal. Karena tidak ada penyaring kedua, **tidak ada kappa antar-penilai yang
dilaporkan** dan itu dinyatakan sebagai keterbatasan di §7.4 — bukan dibiarkan implisit.
Preseden: P4 di sampel venue menyatakan hal serupa secara terbuka.

### Skema `prisma-counts.csv`

```
query_id, database, date_run, n_raw, n_dedup_within, n_dedup_across, n_screened,
n_excl_EC1, n_excl_EC2, n_excl_EC3, n_excl_EC4, n_excl_EC5, n_excl_EC6,
n_fulltext_sought, n_retrieved, n_included
```

Diagram alir di naskah **dibangkitkan dari CSV ini**, tidak digambar tangan — mengikuti
pola `build.js` → `index.html` yang sudah dipakai repo.

---

## 8. Dua register asal-usul

Korpus lama (202 record) **dikumpulkan sebelum protokol ini ada** — commit pertama
(`4a7661d`, 16 Juli 2026) sudah memuatnya lengkap. Tidak ada yang bisa direkonstruksi;
hanya bisa diproduksi baru. Karena itu asal-usul dilaporkan dalam dua register terpisah.

| Register | Isi | Perlakuan |
|---|---|---|
| **A** | Studi yang **ditinjau** | Masuk corong; punya baris di tabel sintesis dan di `evidence-matrix-v2.csv`. |
| **B** | Sitasi **latar** (R-CNN, COCO, KITTI, DETR, NYU Depth v2, dst.) | Dikutip untuk konteks; **tidak** masuk corong; tidak punya baris tabel sintesis. |

Tiap dari 202 record lama diberi **satu** label di `provenance-202.csv`:
`db-search` · `hand-search-snowballing` · `background-citation` · `dropped`.

> **Aturan keras.** Label `hand-search-snowballing` hanya boleh diberikan bila tautan
> sitasinya dapat **disebut konkret** — record ini disitasi oleh studi included X, atau
> menyitasi Y — dan diverifikasi ke `docs/extracted/`. Melabeli record lama sebagai
> "hand-search" tanpa tautan yang bisa ditunjuk adalah rasionalisasi retrospektif, bukan
> pelaporan.

**Jangan pernah menyetel protokol ini agar jumlah included berujung di 182.** Query yang
dijalankan sungguhan akan mengembalikan himpunan yang hampir tidak beririsan dengan
korpus lama (`references.bib` punya **0** judul ber-"counting", "oil palm", "citrus",
"grape", "re-identification", "yield"). Laporkan angkanya apa adanya.

---

## 9. Form ekstraksi

Satu baris per studi Register A di `docs/evidence-matrix-v2.csv`:

```
study_id, bibtex_key, authors_year, crop_or_domain, observation_regime,
modality, identity_mechanism, class_attribute_family, evaluation_context,
unique_instance_gt, metrics_reported, dedup_handled, evidence_status,
assumptions_required, violated_conditions
```

| Kolom | Nilai yang diizinkan |
|---|---|
| `observation_regime` | `single-view` · `multi-view-discrete` · `video-continuous` · `multi-camera-rig` · `aerial` |
| `identity_mechanism` | `M0` intra-view · `M1` statistik · `M2` penampilan/re-ID · `M3` gerak/temporal · `M4` geometris · `M5` multi-view terpelajar |
| `class_attribute_family` | `maturity` · `size` · `quality-defect` · `disease` · `cultivar` · `none` |
| `unique_instance_gt` | `y` · `n` — apakah studi punya ground truth instans unik lintas-observasi |
| `dedup_handled` | `explicit` · `implicit` · `no` · `n-a` |
| `evidence_status` | `direct` (pertanian/buah) · `transferable` (domain lain, menjawab pertanyaan mekanisme) · `absent` |
| `assumptions_required` | subset dari A1–A7 |
| `violated_conditions` | subset dari P1–P5 (kondisi kanopi yang melanggar asumsi domain asal) |

**Wajib dinyatakan sebagai keterbatasan di §7.4:** `assumptions_required` dan
`violated_conditions` adalah **inferensi peninjau**, bukan ekstraksi harfiah dari teks
studi. Sebagian besar studi tidak menyatakan asumsinya secara eksplisit.

---

## 10. Log deviasi

Setiap perubahan protokol setelah pencarian dimulai dicatat di sini, bertanggal, dengan
alasannya. **Versi query yang gagal dicatat, tidak dihapus.**

### D-1 — 2026-07-23 — bug logika uji known-item *(diperbaiki)*

Versi pertama `tools/openalex_search.py` menilai kelolosan dengan `all()`, sehingga
menuntut item ditemukan oleh **semua** query yang tercantum. §6 menulis "dan/atau",
yang berarti **satu** sudah cukup. Akibatnya Gené-Molá 2020 dilaporkan GAGAL padahal
Q3 menemukannya. Diperbaiki jadi `any()`. Angka pencarian tidak terpengaruh.

### D-2 — 2026-07-23 — celah nyata: penghitungan buah pandangan-tunggal tidak terjaring

Uji known-item menemukan **Koirala 2019 MangoYOLO** (`10.1007/s11119-019-09642-0`)
tidak dikembalikan oleh Q1 maupun Q4, meski record-nya ada di OpenAlex.

Penyebabnya sah, bukan salah ketik:

- **Q1** mensyaratkan klausa ketiga (`multi-view` OR `video` OR `tracking` OR …).
  MangoYOLO adalah deteksi citra-tunggal — tidak memuat satu pun istilah itu.
- **Q4** mensyaratkan klausa atribut kelas (`maturity` OR `grading` OR …). MangoYOLO
  mengerjakan penghitungan/estimasi muatan, bukan penilaian mutu.

Artinya set query saat ini **tidak menjaring baseline penghitungan buah
pandangan-tunggal** — padahal literatur itu dibutuhkan dua kali: sebagai kelas
pembanding M0/M1 di §5, dan untuk memenuhi butir 7 dosen (penghitungan apel/jeruk/anggur).

**Tindakan yang diperlukan (belum dijalankan):** tambahkan **Q7 — penghitungan buah
pandangan-tunggal / estimasi hasil**, tanpa klausa multi-view:

```
TITLE-ABS-KEY(
  ("fruit" OR "apple" OR "citrus" OR "mango" OR "grape" OR "berry" OR "bunch"
   OR "oil palm" OR "orchard" OR "vineyard")
  AND
  ("counting" OR "count" OR "yield estimation" OR "load estimation" OR "fruit load"
   OR "crop load")
  AND
  ("deep learning" OR "convolutional" OR "object detection" OR "YOLO"
   OR "instance segmentation" OR "machine vision")
)
AND PUBYEAR > 2014
```

Uji known-item Q7 harus mengembalikan Koirala 2019 sebelum dipakai.

### D-3 — 2026-07-23 — dua query menyentuh batas penjaga

`n_dilaporkan_api` melampaui batas unduh 5.000:

| Query | n_api | diunduh | Tindakan |
|---|---|---|---|
| Q3 multimodalitas/geometri tanaman | 6.423 | 5.000 | Naikkan batas, atau persempit klausa modalitas. Selisihnya kecil. |
| Q6 seed sawit | **15.609** | 5.000 | **Terlalu luas.** Literatur "oil palm" mencakup agronomi, biologi, dan ekonomi minyak sawit — sebagian besar bukan visi komputer. Perlu klausa keempat yang mensyaratkan istilah pencitraan/pembelajaran mesin. |

Angka `n_raw` untuk Q3 dan Q6 **belum sah** untuk corong PRISMA sampai ini dibereskan.

### D-4 — 2026-07-23 — Q7 dijalankan, celah D-2 tertutup

Q7 ditambahkan ke `tools/openalex_search.py` dan dijalankan. **n_raw = 1.317
(1.318 diunduh), tidak tersentuh batas.**

Uji known-item diulang dengan logika `any()` yang benar (D-1) dan pembacaan lintas-
seluruh-ekspor. **Ketiganya LOLOS:**

| Item | Ditemukan oleh |
|---|---|
| Gené-Molá 2020 | Q3 |
| Koirala 2019 MangoYOLO | **Q7** |
| Indriani 2026 SawitMVC | Q1, Q2, Q4, Q7 |

Skrip juga diperbaiki agar jalan sebagian (`python tools/openalex_search.py Q7`) tidak
menghapus rekap query lain: `openalex-counts.csv` dibaca-gabung, dan uji known-item
membaca DOI dari seluruh ekspor di disk, bukan hanya query yang baru dijalankan.

### D-5 — 2026-07-23 — Q6 dipersempit dari 15.609 → 1.177

**Versi yang gagal (disimpan, tidak dihapus):**

```
("oil palm" OR "elaeis guineensis" OR "fresh fruit bunch")
AND ("detection" OR "classification" OR "counting" OR "ripeness" OR "maturity"
     OR "yield" OR "grading" OR "harvesting" OR "plantation")
```

Mengembalikan **15.609** record. Penyebabnya klausa kedua: `yield`, `plantation`, dan
`harvesting` adalah istilah agronomi, sehingga query menjaring literatur agronomi,
biologi, dan ekonomi minyak sawit yang sebagian besar tidak memakai citra sama sekali.

**Versi yang dipakai:**

```
("oil palm" OR "elaeis guineensis" OR "fresh fruit bunch")
AND ("deep learning" OR "machine learning" OR "convolutional" OR "neural network"
     OR "computer vision" OR "image processing" OR "YOLO" OR "object detection"
     OR "remote sensing")
```

**n_raw = 1.177, tidak tersentuh batas.**

Tiga varian diprobe sebelum memilih, dicatat supaya pilihannya transparan:

| Varian | n |
|---|---|
| sawit AND klausa-tugas AND klausa-pencitraan | 704 |
| sawit AND klausa-tugas AND pencitraan tanpa `remote sensing` | 574 |
| **sawit AND klausa-pencitraan** *(dipakai)* | **1.177** |

Varian tiga-klausa dibuang meski lebih kecil: klausa tugas menambah eksklusi yang sulit
dipertanggungjawabkan ke reviewer, sementara "sawit AND pencitraan/ML" menyatakan
maksud Q6 secara langsung. Untuk query yang tugasnya menjaring literatur yang korpus
lama **sama sekali tidak punya**, recall lebih tinggi lebih berharga daripada biaya
penyaringan. `remote sensing` dipertahankan karena penghitungan pohon sawit dari
UAV/satelit adalah rezim observasi udara yang relevan bagi tinjauan ini.

**Validasi butir 7 — Q6 baru menjaring keduanya.** Ini menjawab konfirmasi #4 ke dosen
sebagian: identitas "Suharjito" dan "Goh" kini punya kandidat konkret.

| Penulis | Karya di Q6 | Contoh yang menonjol |
|---|---|---|
| **Suharjito** (BINUS) | 11 | *Oil palm FFB ripeness classification on mobile devices* (2021); *Hyperparameter optimization of YOLOv4-tiny for palm oil FFB* (2023); ***Video based oil palm ripeness detection model using deep learning*** (2023) |
| **Jin Yu Goh** (UTM) | 8 | ***Fresh Fruit Bunch Ripeness Classification Methods: A Review*** (2024); ***Outdoor RGB and Point Cloud Depth Dataset for Palm Oil FFB*** (2025) |

Dua di antaranya mengubah lanskap dan harus ditangani di naskah, bukan sekadar
disitasi:

1. **Goh 2024 adalah tinjauan terdahulu persis di topik ini.** Ia wajib masuk Tabel 1
   positioning (butir 3), dan klaim kebaruan harus diuji terhadapnya lebih dulu.
2. **Goh 2025 adalah dataset RGB-D FFB sawit yang publik.** Pernyataan di
   `CLAUDE.md` — "tidak ada satu pun benchmark RGB-D pada FFB sawit di korpus 182" —
   tetap benar **sebagai pernyataan tentang korpus**, tetapi tidak lagi benar sebagai
   pernyataan tentang literatur. Setiap kalimat naskah yang menyiratkan yang kedua
   harus diperbaiki.

### D-6 — 2026-07-23 — Q3 dijalankan tuntas; duplikat paginasi ditemukan dan dibuang

**Bagian pertama — batas dinaikkan, Q3 selesai.** `BATAS_PER_QUERY` dinaikkan dari
5.000 ke 12.000 di `tools/openalex_search.py` dan `Q3` dijalankan ulang sendirian.
Query-nya **tidak diubah** — yang berubah hanya penjaga runaway, jadi ini bukan
deviasi rancangan pencarian, melainkan pencabutan pemotongan artifisial.

```
[Q3] multimodalitas dan geometri untuk tanaman ...
    n_dilaporkan=6423  n_diunduh=6424  terpotong=tidak
```

**Bagian kedua — temuan yang tidak diduga.** Verifikasi pasca-unduh menunjukkan
`n_diunduh` (6.424) **melebihi** `n_dilaporkan` API (6.423). Pemeriksaan `openalex_id`
memastikan sebabnya: **paginasi kursor OpenAlex sesekali mengembalikan record yang
sama dua kali** bila indeks bergeser saat pengambilan berlangsung. Terjadi di tiga
query:

| Query | baris terunduh | unik | duplikat |
|---|---|---|---|
| Q1 | 1.851 | **1.849** | 2 |
| Q2 | 1.991 | 1.991 | 0 |
| **Q3** | 6.424 | **6.422** | 2 |
| Q4 | 2.757 | 2.757 | 0 |
| Q5 | 1.143 | 1.143 | 0 |
| Q6 | 1.177 | 1.177 | 0 |
| Q7 | 1.318 | **1.317** | 1 |

Bukan galat besar (5 record dari 16.661 baris terunduh = 0,03%), tetapi **materiil secara
metodologis**: `n_raw` yang masuk corong PRISMA harus jumlah **unik**, bukan jumlah
baris terunduh. Melaporkan 6.424 lalu kehilangan 2 saat dedup akan tampak seperti
dedup lintas-sumber padahal duplikatnya berasal dari satu query.

**Tindakan:**

1. `jalankan()` di `tools/openalex_search.py` kini dedup berdasarkan `openalex_id`
   sebelum menulis, dan mencetak `[dedup-dalam-query]` bila ada yang dibuang.
2. Ketujuh ekspor yang sudah ada di disk dinormalkan (tanpa unduh ulang); kolom
   `n_diunduh` di `openalex-counts.csv` kini berarti **jumlah unik**.

Setelah dedup, Q1 (1.849) dan Q7 (1.317) **cocok persis** dengan `n_dilaporkan` API.
Q3 menyisakan selisih 1 (6.422 unik vs 6.423 dilaporkan) — `meta.count` OpenAlex
adalah taksiran indeks, jadi selisih satu record pada 6.400 tidak dapat direkonsiliasi
dari sisi klien. **Dilaporkan apa adanya, tidak dibulatkan.**

**Sisa terbuka lengan OpenAlex: tidak ada.** Ketujuh query lengkap, nol terpotong.

| Tanggal | Deviasi | Status |
|---|---|---|
| 2026-07-23 | D-1 logika uji known-item | diperbaiki |
| 2026-07-23 | D-2 celah pandangan-tunggal → Q7 | **tertutup** (lihat D-4) |
| 2026-07-23 | D-3 Q3 & Q6 tersentuh batas | **tertutup** — Q6 di D-5, Q3 di D-6 |
| 2026-07-23 | D-4 Q7 dijalankan, known-item lolos | selesai |
| 2026-07-23 | D-5 Q6 dipersempit 15.609 → 1.177 | selesai |
| 2026-07-23 | D-6 Q3 tuntas (6.422) + dedup paginasi | selesai |
| 2026-07-23 | D-7 pembatasan `SUBJAREA` di lengan Scopus | berjalan |

### D-7 — 2026-07-23 — pembatasan bidang subjek pada lengan Scopus

**Temuan.** Q1 dijalankan di Scopus tanpa pembatasan: **3.403** record, **792 di
antaranya Medicine** (23%). Hasil teratas adalah makalah pediatri tentang praktik tidur
bayi, dan bibliometrik glaukoma — nol hubungan dengan buah.

**Sebabnya kata bermakna ganda**, bukan kesalahan rancangan query:

| Istilah | Tertangkap juga |
|---|---|
| `"cluster"` | *cluster randomized trial* |
| `"inventory"` | *Beck Depression Inventory* |
| `"berry"` | *berry aneurysm* |
| `"track*"` | *eye-tracking* |
| `"count*"` | *blood count*, *cell count* |
| `"crop"` | *cropped image* |

**Keputusan.** Istilahnya **tidak dibuang** — Q1 sengaja mempertahankan struktur contoh
dosen (§4). Yang dibatasi bidang subjeknya, ditulis **di dalam query** sebagai
`SUBJAREA(...)`, bukan lewat centang sidebar. Centang tidak tersimpan di string query
sehingga tidak dapat direproduksi orang lain — bertentangan dengan butir 1 revisi.

Hasil Q1 setelah dibatasi ke AGRI+COMP+ENGI: **1.853**.

**`MULT` ditambahkan setelah pemeriksaan.** *Data in Brief* terindeks Multidisciplinary,
dan di situlah SawitMVC (`10.1016/j.dib.2026.112990`) berada. Membatasi hanya ke
AGRI+COMP+ENGI akan mengeksklusi makalah dataset proyek ini sendiri. `EART`+`ENVI`
ditambahkan pada Q3 dan Q6 karena penginderaan jauh dan fotogrametri terindeks di sana.

**Kewajiban pelaporan.** Pembatasan subjek adalah eksklusi yang dideklarasikan, jadi
**dua angka dicatat per query**: `n_tanpa_subjarea` dan `n_final`. Selisihnya harus
terlihat di corong PRISMA, tidak boleh lenyap.

**Prediksi asisten yang salah, dicatat.** Sebelum lengan Scopus dijalankan, asisten
memperkirakan angka Scopus akan **lebih kecil** dari OpenAlex karena `TITLE-ABS-KEY`
mencocokkan frasa persis. Nyatanya lebih besar (3.403 vs 1.849): `TITLE-ABS-KEY` juga
menyisir *indexed keywords* Scopus, bukan hanya judul+abstrak. Kemiripan angka
pasca-pembatasan (1.853 vs 1.849) adalah **kebetulan**, bukan validasi silang.

Query final ada di [`scopus-queries.md`](scopus-queries.md).
