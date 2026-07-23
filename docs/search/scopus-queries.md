# Query Scopus — siap tempel

Versi satu baris dari `PROTOCOL.md` §4, untuk ditempel ke **Advanced document search**
Scopus. Isinya identik dengan yang dijalankan di lengan OpenAlex — hanya sintaksnya yang
berbeda. Jangan mengubah kata kunci di sini tanpa mengubah `PROTOCOL.md` juga; kalau
berubah, catat sebagai deviasi baru (D-7 dst.).

## Cara menjalankan

1. Buka **Advanced document search** (bukan kotak pencarian dasar).
2. Tempel satu query, jalankan.
3. Catat `n_raw` yang dilaporkan Scopus **sebelum** filter apa pun.
4. **Export → CSV**, centang minimal: *Citation information* + *Bibliographical
   information* + **DOI**. DOI wajib — ia kunci dedup lintas-sumber.
5. Simpan sebagai `docs/search/raw/scopus_Q<N>_<YYYY-MM-DD>.csv`.
6. Ulangi untuk ketujuh query.

**Catatan batas.** Ekspor CSV Scopus dibatasi 20.000 record; ketujuh query ini
seharusnya jauh di bawahnya. **Bila ada query yang melampaui batas, catat apa adanya
dan jangan dipotong diam-diam** — itulah kesalahan yang sudah terjadi sekali di lengan
OpenAlex (D-3).

**Perbedaan yang diharapkan dengan OpenAlex.** Angka Scopus kemungkinan besar **lebih
kecil**. `TITLE-ABS-KEY` mencocokkan frasa persis dan mendukung wildcard (`count*`),
sedangkan filter OpenAlex melakukan pencocokan token ber-*stemming* tanpa wildcard.
Selisih ini normal dan **tidak** menandakan salah satu arm bermasalah — ia justru
alasan kedua arm dijalankan. Laporkan keduanya terpisah di corong PRISMA.

---

## Q1 — Inventaris/penghitungan buah dari banyak observasi

```
TITLE-ABS-KEY(("fruit" OR "fresh fruit bunch" OR "FFB" OR "oil palm" OR "apple" OR "citrus" OR "mango" OR "grape" OR "berry" OR "bunch" OR "cluster" OR "crop") AND ("count*" OR "yield estimation" OR "load estimation" OR "fruit load" OR "inventory" OR "enumeration") AND ("multi-view" OR "multiple view*" OR "multi-camera" OR "video" OR "cross-view" OR "structure from motion" OR "SfM" OR "track*" OR "3D reconstruction" OR "image sequence")) AND PUBYEAR > 2014
```

## Q2 — Asosiasi lintas-view dan anti-duplikasi *(non-pertanian diizinkan)*

```
TITLE-ABS-KEY(("multi-view" OR "cross-view" OR "multi-camera" OR "multiple cameras" OR "overlapping view*" OR "multi-sensor") AND ("re-identification" OR "data association" OR "identity" OR "duplicate*" OR "deduplicat*" OR "double counting" OR "correspondence" OR "instance matching" OR "track*" OR "association") AND ("object detection" OR "instance segmentation" OR "counting" OR "instance" OR "pedestrian" OR "vehicle")) AND PUBYEAR > 2014
```

Set inilah yang mengisi §5.2–5.5, tempat korpus lama **nol**.

## Q3 — Multimodalitas dan geometri untuk tanaman

```
TITLE-ABS-KEY(("RGB-D" OR "depth camera" OR "stereo vision" OR "LiDAR" OR "point cloud" OR "monocular depth" OR "photogrammetry" OR "structure from motion") AND ("fruit" OR "orchard" OR "vineyard" OR "canopy" OR "plant" OR "tree crop" OR "plantation" OR "oil palm") AND ("detection" OR "segmentation" OR "localization" OR "counting" OR "phenotyping" OR "harvesting")) AND PUBYEAR > 2014
```

## Q4 — Kelas per-instans di luar kematangan

```
TITLE-ABS-KEY(("fruit" OR "produce" OR "crop" OR "bunch") AND ("maturity" OR "ripeness" OR "grading" OR "grade" OR "quality class*" OR "size class*" OR "defect" OR "disease" OR "cultivar" OR "variety") AND ("instance segmentation" OR "object detection" OR "per-instance" OR "individual fruit" OR "bounding box" OR "per-object")) AND PUBYEAR > 2014
```

## Q5 — Tinjauan terdahulu *(positioning, butir 3)*

```
TITLE(("review" OR "survey" OR "systematic review" OR "scoping review")) AND TITLE-ABS-KEY(("fruit detection" OR "fruit counting" OR "yield estimation" OR "oil palm" OR "orchard" OR "crop monitoring" OR "agricultural robot*" OR "precision agriculture") AND ("deep learning" OR "computer vision" OR "object detection" OR "machine vision")) AND PUBYEAR > 2014
```

**Query paling penting untuk butir 3.** Tiap review yang masuk dikodekan pada satu
pertanyaan: *apakah identitas/duplikasi lintas-view diperlakukan sebagai masalah kelas
satu?* Jawabannya jadi kolom terakhir Tabel 1. Bila ada yang menjawab "ya", klaim
kebaruan **dilemahkan apa adanya**.

## Q6 — Seed sawit *(butir 7; versi dipersempit D-5)*

```
TITLE-ABS-KEY(("oil palm" OR "elaeis guineensis" OR "fresh fruit bunch" OR "FFB") AND ("deep learning" OR "machine learning" OR "convolutional" OR "neural network" OR "computer vision" OR "image processing" OR "YOLO" OR "object detection" OR "remote sensing")) AND PUBYEAR > 2014
```

## Q7 — Penghitungan buah pandangan-tunggal *(butir 7; ditambahkan D-2/D-4)*

```
TITLE-ABS-KEY(("fruit" OR "apple" OR "citrus" OR "mango" OR "grape" OR "berry" OR "bunch" OR "oil palm" OR "orchard" OR "vineyard") AND ("counting" OR "count" OR "yield estimation" OR "load estimation" OR "fruit load" OR "crop load") AND ("deep learning" OR "convolutional" OR "object detection" OR "YOLO" OR "instance segmentation" OR "machine vision")) AND PUBYEAR > 2014
```

---

## Jalur penulis terpisah *(butir 7)*

Dicatat sebagai jalur tersendiri di corong PRISMA, **bukan** digabung ke Q6:

```
AUTHOR-NAME("Suharjito")
```
```
AUTHOR-NAME("Goh, J.Y.") OR AUTHOR-NAME("Goh, Jin Yu")
```

**Peringatan.** "Goh" nama yang sangat umum — batasi ke subjek *Agricultural and
Biological Sciences* / *Computer Science*, dan buang false positive secara manual.
Kandidat yang sudah tervalidasi lewat Q6 OpenAlex ada di `PROTOCOL.md` D-5 (Suharjito
11 karya, Jin Yu Goh 8 karya) — pakai itu sebagai pembanding hasil Scopus.

---

## Uji known-item — jalankan setelah ketujuh ekspor selesai

Sama seperti lengan OpenAlex (`PROTOCOL.md` §6). Ketiganya harus kembali di **setidaknya
satu** query:

| Item | DOI |
|---|---|
| Gené-Molá 2020, deteksi buah + SfM | `10.1016/j.compag.2019.105165` |
| Koirala 2019, MangoYOLO | `10.1007/s11119-019-09642-0` |
| Indriani 2026, SawitMVC | `10.1016/j.dib.2026.112990` |

Bila ada yang **tidak** kembali, itu bukan alasan menyetel ulang query diam-diam —
catat sebagai deviasi bernomor lebih dulu, seperti D-1 dan D-2.

---

## Catatan integritas

Angka Scopus **tidak boleh** disetel agar mendekati angka OpenAlex, dan tidak boleh
disetel agar jumlah included berujung di 182. Kedua arm dilaporkan apa adanya, terpisah,
di corong PRISMA.
