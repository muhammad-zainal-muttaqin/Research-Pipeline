# Query Scopus — siap tempel (FINAL)

Versi satu baris dari `PROTOCOL.md` §4, untuk ditempel ke **Advanced document search**
Scopus. Jangan mengubah kata kunci di sini tanpa mengubah `PROTOCOL.md` juga; kalau
berubah, catat sebagai deviasi baru.

> **Direvisi 2026-07-23 (D-7).** Ditambahkan pembatasan `SUBJAREA(...)`. Alasan dan
> buktinya di bagian berikut.

## Kenapa ada `SUBJAREA(...)`

Q1 tanpa pembatasan mengembalikan **3.403** record, dan **792 di antaranya Medicine**.
Sebabnya kata bermakna ganda di query: `"cluster"` menangkap *cluster randomized
trial*, `"inventory"` menangkap *Beck Depression Inventory*, `"berry"` menangkap *berry
aneurysm*, `"track*"` menangkap *eye-tracking*, `"count*"` menangkap *blood count*.
Hasil teratas Q1 sebelum dibatasi adalah makalah pediatri tentang tidur bayi.

Istilahnya **tidak dibuang** — Q1 sengaja mempertahankan struktur contoh dosen. Yang
dibatasi bidang subjeknya. Setelah dibatasi ke AGRI+COMP+ENGI: **1.853** record.

Pembatasan ini ditulis **di dalam query**, bukan lewat centang sidebar. Centang tidak
ikut tersimpan di string query, sehingga tidak dapat direproduksi orang lain — padahal
reproducibility adalah inti butir 1 revisi dosen.

### `MULT` wajib ada — jangan dihapus

`MULT` = *Multidisciplinary*. Di situlah **Data in Brief** terindeks, dan di situlah
**SawitMVC** berada (`10.1016/j.dib.2026.112990`). Membatasi hanya ke AGRI+COMP+ENGI
akan mengeksklusi makalah dataset proyek ini sendiri.

Kode yang dipakai:

| Kode | Bidang | Dipakai di |
|---|---|---|
| `AGRI` | Agricultural and Biological Sciences | semua |
| `COMP` | Computer Science | semua |
| `ENGI` | Engineering | semua |
| `MULT` | Multidisciplinary | semua — **wajib** |
| `EART` | Earth and Planetary Sciences | Q3, Q6 *(penginderaan jauh, fotogrametri)* |
| `ENVI` | Environmental Science | Q3, Q6 |

## Cara menjalankan

1. Buka **Advanced document search**.
2. Tempel satu query, jalankan.
3. Catat **dua angka**: `n_tanpa_subjarea` (jalankan sekali tanpa klausa `SUBJAREA`)
   dan `n_final`. Keduanya masuk `prisma-counts.csv` — pembatasan subjek adalah
   eksklusi yang dideklarasikan, jadi jumlah yang dibuangnya harus terlihat.
4. **Export → CSV**, centang minimal *Citation information* + *Bibliographical
   information* + **DOI**. DOI wajib — ia kunci dedup lintas-sumber.
5. Simpan sebagai `docs/search/raw/scopus_Q<N>_<YYYY-MM-DD>.csv`.

**Catatan batas.** Ekspor CSV Scopus dibatasi 20.000 record. Bila ada query yang
melampauinya, **catat apa adanya dan jangan dipotong diam-diam** — itu kesalahan yang
sudah terjadi sekali di lengan OpenAlex (D-3).

**Perbandingan dengan OpenAlex.** Prediksi awal bahwa Scopus akan lebih kecil **salah**:
Q1 Scopus tanpa pembatasan 3.403 vs OpenAlex 1.849. Sebabnya `TITLE-ABS-KEY` juga
menyisir *indexed keywords* Scopus, bukan hanya judul+abstrak. Setelah `SUBJAREA`,
Q1 = 1.853 — kebetulan hampir sama dengan OpenAlex. Kemiripan ini **kebetulan**, bukan
validasi; kedua arm tetap dilaporkan terpisah.

---

## Q1 — Inventaris/penghitungan buah dari banyak observasi

```
TITLE-ABS-KEY(("fruit" OR "fresh fruit bunch" OR "FFB" OR "oil palm" OR "apple" OR "citrus" OR "mango" OR "grape" OR "berry" OR "bunch" OR "cluster" OR "crop") AND ("count*" OR "yield estimation" OR "load estimation" OR "fruit load" OR "inventory" OR "enumeration") AND ("multi-view" OR "multiple view*" OR "multi-camera" OR "video" OR "cross-view" OR "structure from motion" OR "SfM" OR "track*" OR "3D reconstruction" OR "image sequence")) AND PUBYEAR > 2014 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT))
```

## Q2 — Asosiasi lintas-view dan anti-duplikasi *(non-pertanian diizinkan)*

```
TITLE-ABS-KEY(("multi-view" OR "cross-view" OR "multi-camera" OR "multiple cameras" OR "overlapping view*" OR "multi-sensor") AND ("re-identification" OR "data association" OR "identity" OR "duplicate*" OR "deduplicat*" OR "double counting" OR "correspondence" OR "instance matching" OR "track*" OR "association") AND ("object detection" OR "instance segmentation" OR "counting" OR "instance" OR "pedestrian" OR "vehicle")) AND PUBYEAR > 2014 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(AGRI) OR SUBJAREA(MULT))
```

Set inilah yang mengisi §5.2–5.5, tempat korpus lama **nol**. Sengaja mengizinkan
literatur non-pertanian (pejalan kaki, kendaraan) — itu bukan kebocoran, itu maksudnya.

## Q3 — Multimodalitas dan geometri untuk tanaman

```
TITLE-ABS-KEY(("RGB-D" OR "depth camera" OR "stereo vision" OR "LiDAR" OR "point cloud" OR "monocular depth" OR "photogrammetry" OR "structure from motion") AND ("fruit" OR "orchard" OR "vineyard" OR "canopy" OR "plant" OR "tree crop" OR "plantation" OR "oil palm") AND ("detection" OR "segmentation" OR "localization" OR "counting" OR "phenotyping" OR "harvesting")) AND PUBYEAR > 2014 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MULT))
```

## Q4 — Kelas per-instans di luar kematangan

```
TITLE-ABS-KEY(("fruit" OR "produce" OR "crop" OR "bunch") AND ("maturity" OR "ripeness" OR "grading" OR "grade" OR "quality class*" OR "size class*" OR "defect" OR "disease" OR "cultivar" OR "variety") AND ("instance segmentation" OR "object detection" OR "per-instance" OR "individual fruit" OR "bounding box" OR "per-object")) AND PUBYEAR > 2014 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT))
```

## Q5 — Tinjauan terdahulu *(positioning, butir 3)*

```
TITLE(("review" OR "survey" OR "systematic review" OR "scoping review")) AND TITLE-ABS-KEY(("fruit detection" OR "fruit counting" OR "yield estimation" OR "oil palm" OR "orchard" OR "crop monitoring" OR "agricultural robot*" OR "precision agriculture") AND ("deep learning" OR "computer vision" OR "object detection" OR "machine vision")) AND PUBYEAR > 2014 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT))
```

**Query paling penting untuk butir 3.** Tiap review yang masuk dikodekan pada satu
pertanyaan: *apakah identitas/duplikasi lintas-view diperlakukan sebagai masalah kelas
satu?* Jawabannya jadi kolom terakhir Tabel 1. Bila ada yang menjawab "ya", klaim
kebaruan **dilemahkan apa adanya**.

## Q6 — Seed sawit *(butir 7; versi dipersempit D-5)*

```
TITLE-ABS-KEY(("oil palm" OR "elaeis guineensis" OR "fresh fruit bunch" OR "FFB") AND ("deep learning" OR "machine learning" OR "convolutional" OR "neural network" OR "computer vision" OR "image processing" OR "YOLO" OR "object detection" OR "remote sensing")) AND PUBYEAR > 2014 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MULT))
```

## Q7 — Penghitungan buah pandangan-tunggal *(butir 7; ditambahkan D-2/D-4)*

```
TITLE-ABS-KEY(("fruit" OR "apple" OR "citrus" OR "mango" OR "grape" OR "berry" OR "bunch" OR "oil palm" OR "orchard" OR "vineyard") AND ("counting" OR "count" OR "yield estimation" OR "load estimation" OR "fruit load" OR "crop load") AND ("deep learning" OR "convolutional" OR "object detection" OR "YOLO" OR "instance segmentation" OR "machine vision")) AND PUBYEAR > 2014 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT))
```

---

## Jalur penulis terpisah *(butir 7)*

Dicatat sebagai jalur tersendiri di corong PRISMA, **bukan** digabung ke Q6:

```
AUTHOR-NAME("Suharjito") AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT))
```
```
(AUTHOR-NAME("Goh, J.Y.") OR AUTHOR-NAME("Goh, Jin Yu")) AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT))
```

**Peringatan.** "Goh" nama yang sangat umum, dan satu-satunya "Goh" di repo saat ini
adalah **Gabriel Goh** (co-author CLIP) — false positive. Buang manual. Kandidat yang
sudah tervalidasi lewat Q6 OpenAlex ada di `PROTOCOL.md` D-5 (Suharjito 11 karya,
Jin Yu Goh 8 karya) — pakai itu sebagai pembanding.

---

## Uji known-item — WAJIB sebelum ekspor

Pembatasan `SUBJAREA` adalah tempat paling mudah kehilangan makalah tanpa sadar. Setelah
menjalankan tiap query, tempel DOI ini ke **Search within results**:

| Item | DOI | Diharapkan di |
|---|---|---|
| Gené-Molá 2020, deteksi buah + SfM | `10.1016/j.compag.2019.105165` | Q1 dan/atau Q3 |
| Koirala 2019, MangoYOLO | `10.1007/s11119-019-09642-0` | Q7 |
| Indriani 2026, SawitMVC | `10.1016/j.dib.2026.112990` | Q1 — **penguji `MULT`** |

Cukup **satu** query menemukannya. Bila ada yang hilang, **jangan diam-diam melonggarkan
`SUBJAREA` sampai ketemu** — catat sebagai deviasi bernomor lebih dulu, seperti D-1
dan D-2.

---

## Catatan integritas

Angka Scopus **tidak boleh** disetel agar mendekati angka OpenAlex, dan tidak boleh
disetel agar jumlah included berujung di 182. Kedua arm dilaporkan apa adanya, terpisah,
di corong PRISMA — termasuk berapa yang dibuang oleh pembatasan `SUBJAREA`.

Sisa noise setelah pembatasan **normal dan tidak perlu diperketat lagi**. Tahap
pencarian pada tinjauan sistematis memang dirancang recall-tinggi presisi-rendah;
penyaringan judul–abstrak yang membuang sisanya, tercatat sebagai `n_excl_EC*`.
Memperketat query sekarang justru membuang makalah sah tanpa jejak.
