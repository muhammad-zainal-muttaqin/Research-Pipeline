# STATUS — titik berhenti & cara melanjutkan

**Terakhir diperbarui:** 2026-07-30 · **Status:** aktif — **dataset baru
`SawitMVC-Depth` (depth SENSOR Orbbec) sudah diuji: E-022 / [SR-014](SR/SR-014-depth-sensor-4kanal.md).**
Fusi 4-kanal awal **DIPALSUKAN**, tetapi kandungan informasi depth terkonfirmasi
pada model besar (B4 +0,1001 vs kontrol derau). Detektor terbaik di SawitMVC lama
tetap RF-DETR-L (E-021, test mAP50 0,6038).

Metrik lengkap semua run (per-kelas B1–B4, val+test) di [`METRICS.md`](METRICS.md).

Dokumen ini adalah **titik masuk tunggal** saat pekerjaan dilanjutkan. Baca ini
dulu, lalu `docs/SR/README.md` (cerita per-ide) dan `docs/EKSPERIMEN.md` (log
kronologis E-001…E-022).

---

## 1. Di mana kita sekarang

**Sasaran** (ditetapkan pengguna, tidak dapat ditawar dengan pembingkaian ulang):
**mAP50 0,60 dan mAP50-95 0,30 pada 4 kelas penuh (B1–B4)**, angka COCO apa
adanya, pilih di val / lapor di test, tanpa hack.

**Hasil terbaik saat ini — RF-DETR-L (NMS-free, DINOv2), lihat [E-021](EKSPERIMEN.md):**

| | mAP50 | mAP50-95 | ke target |
|---|---|---|---|
| TEST | **0,6038** | **0,2770** | mAP50 **+0,004 (LEWAT)** · mAP50-95 −0,023 |
| VAL | 0,5695 | 0,2604 | mAP50 −0,031 · mAP50-95 −0,040 |

**Sasaran mAP50 0,60 pada test TERLEWATI** (0,6038) untuk pertama kali;
mAP50-95 masih −0,023. RF-DETR-L melampaui RT-DETR-L pada kedua metrik di kedua
split (test +0,024 mAP50 / +0,008 mAP50-95). Checkpoint ep9 (EMA), early-stop
ep17. Angka via COCO eval independen (val cocok evaluator internal rf-detr).

Pembanding sebelumnya — **RT-DETR-L** (E-020/[SR-013](SR/SR-013-rtdetr-nms-free.md)):
test 0,5794/0,2694, val 0,5466/0,2543.

**Perbandingan adil SELESAI (2026-07-25):** YOLO26l @1280 (baseline param-adil
26,3 jt, config identik RT-DETR) terlatih penuh 60 epoch, dan seluruh 4 model
dievaluasi lewat **1-protokol pycocotools** (`results/perkelas_pycoco.json`).
Ranking monotonik menurut parameter: YOLO26m < YOLO26l < RT-DETR-L < RF-DETR-L.
YOLO26l tetap di bawah kedua DETR → keunggulan RF-DETR bukan efek
kapasitas/resolusi. Tabel penuh di [`METRICS.md`](METRICS.md) §1-protokol.
**Semua jebakan teknis + peta berkas + log run ini** terkonsolidasi di
[`experiments/CATATAN-TEKNIS-E021.md`](../experiments/CATATAN-TEKNIS-E021.md) —
baca sebelum menjalankan ulang RF-DETR/RT-DETR/YOLO26.

**Bobot terbaik:** `/workspace/experiments/runs/rtdetr_l_e60_i1280/weights/best.pt`
(264 MB, di luar repo). Reproduksi: `experiments/train_rtdetr.py` +
`experiments/eval_rtdetr.py`. **Kandidat untuk diarsipkan ke penyimpanan objek**
(HuggingFace Hub / Drive / GitHub Release+LFS) — belum dilakukan.

---

## 2. Peta keputusan — apa yang sudah pasti (jangan diulang)

| Temuan | Konsekuensi | Bukti |
|---|---|---|
| Tahap **counting** sudah jenuh (95,57% dgn deteksi sempurna) | masalah ada di **detektor** | SR-006, E-007 |
| Kerugian mAP ada di **klasifikasi kematangan**, bukan deteksi | ide berbasis-deteksi (ubin/fusi/neck) batas atasnya kecil | SR-010, E-014 |
| **B4 gagal karena tersamar** (kontras rendah, B4 mentah = hijau gelap seperti pelepah), bukan kecil/bertumpuk | SAHI/ubin tak menolong | SR-007 |
| **Kematangan itu kontinu** (kebingungan ordinal, lompatan 2-langkah 1,9%) | mismatch objektif-vs-metrik | SR-009 |
| **Depth pseudo** tidak memisahkan tandan | fusi RGB-D early tak membantu (depth SENSOR belum diuji) | SR-005, E-014 |
| **Detektor dua tahap** lebih buruk dari satu tahap | head YOLO sudah kalibrasi bersama + konteks | SR-012 |
| **NMS sebagian dari plafon** — RT-DETR-L +0,063 mAP50 test | ganti detektor ke NMS-free = jalur produktif | **SR-013** |
| **Depth SENSOR 4-kanal awal tidak menaikkan mAP** — kanal berisi DERAU justru satu-satunya delta signifikan (+0,0437) | fusi awal ditutup; arah = fusi menengah | **SR-014**, E-022 |
| **Arah efek kanal ke-4 ditentukan kapasitas model** — menaikkan di 2,6 jt param, menurunkan di 33 jt | jangan menyimpulkan dari model kecil saja | E-022 |
| **Sidecar depth `alignedTo: "color"` MENYESATKAN** (Orbbec) | wajib reproyeksi intrinsik+ekstrinsik, bukan resize | E-022a |
| SR-011 "plafon kematangan 68%" **DITARIK** (bukti cacat) | jangan kutip sebagai plafon | E-018 |
| Plafon **geometris** anotasi = mAP50 0,8834 / mAP50-95 0,4702 | **sasaran ADA di dalam batas fisik** | E-018 |

Dipalsukan / ditutup: SR-001, SR-005, SR-006, SR-012 (dipalsukan); SR-011
(ditarik). Jangan diulang tanpa alasan baru.

---

## 3. Aset yang sudah siap pakai (hasil kerja yang tidak hilang)

- **`pipeline/`** — pipeline produksi YOLO 4-kanal (RGB+depth) untuk kamera
  Gemini. Modality dropout: satu bobot untuk RGB-saja atau RGB+depth. Siap saat
  data sensor Gemini terkumpul. Belum ada bobot terlatih.
- **Dataset master 3060×4080** — `experiments/build_master_ds.py` merakit dataset
  YOLO yang menunjuk ke piksel master penuh (dari peta isi E-015, 3.992/3.992).
  Belum dipakai melatih apa pun. Ini kunci jalur lanjutan #1 di bawah.
- **RT-DETR-L best.pt** — model terbaik (lihat §1).
- **`experiments/`** — arsip skrip + JSON hasil + split, seluruh E-001…E-022.
- **Jalur 4-kanal untuk TIGA kerangka** (E-022): ultralytics YOLO & RT-DETR lewat
  `pipeline/fourch.py` + `experiments/train_depth4ch.py`, dan **rfdetr** lewat
  `experiments/train_rfdetr_4ch.py` (4 tambalan, tanpa fork paket). Termasuk dua
  kontrol negatif siap pakai: `--depth-acak` (derau) dan `--depth-tukar` (registrasi).
- **`experiments/reproject_depth.py`** — konverter depth Orbbec → PNG kanonik
  sejajar RGB (reproyeksi intrinsik+ekstrinsik, z-buffer). Menggantikan
  `pipeline/prepare_depth.py` untuk data sensor.

---

## 4. Jalur lanjutan yang belum tersentuh (prioritas turun)

> **Prioritas baru per 2026-07-30 (dari E-022):** **E-023 — fusi MENENGAH dua
> cabang RGB+D** pada RT-DETR-L atau RF-DETR. Alasannya bukan kutipan literatur
> lagi: pada RT-DETR-L, depth mengalahkan kontrol deraunya sendiri secara
> signifikan di B4 (+0,1001 CI [+0,0062; +0,1618]), jadi informasinya terbukti ada
> — yang gagal adalah salurannya (konkatenasi di kanal masukan merusak stem
> pratlatih 3-kanal). Kontrol derau **dan** kontrol depth-tertukar wajib diulang di
> E-023; tanpa keduanya kenaikan apa pun tidak dapat dibedakan dari efek kapasitas.


Semua GPU-bound, dijeda karena berhenti di sini. Perintah siap jalan.

1. **RT-DETR-L pada piksel master 3060×4080** (imgsz 1600–2048).
   *Kenapa:* menyerang lokalisasi = penentu mAP50-95 (sasaran terjauh); RT-DETR
   sekarang cuma di 1280. **Taruhan terbaik menutup −0,021 terakhir.**
   ```bash
   cd /workspace/experiments
   .venv/bin/python train_rtdetr.py --weights rtdetr-l.pt \
       --imgsz 1600 --epochs 60   # arahkan data ke master_ds/data.yaml
   ```
   Catatan: `train_rtdetr.py` saat ini menunjuk `data_rgb.yaml`; ganti ke
   `master_ds/data.yaml` (dibuat oleh `build_master_ds.py`).

2. **RT-DETR-X** (67,5 juta param) — kapasitas di atas mekanisme NMS-free.
   ```bash
   .venv/bin/python train_rtdetr.py --weights rtdetr-x.pt --imgsz 1280 --batch 3
   ```

3. **I-22 loss ordinal** pada RT-DETR — menyerang mismatch objektif ordinal
   (SR-009) yang belum pernah benar-benar diuji pada detektor terbaik.

4. **I-13 focal/loss berimbang**, **I-15 neck BiFPN** — prioritas lebih rendah;
   keluarga tuning yang sudah berkali gagal, tapi belum di atas RT-DETR.

---

## 5. Ide yang butuh keputusan pengguna (bukan sekadar teknis)

- **Brondolan lepas** sebagai penanda kematangan. Kriteria panen lapangan
  sesungguhnya, tidak terlihat dari kanopi pada jarak foto ini. Mengubah
  **perumusan tugas**, bukan tuning. Belum disentuh; perlu persetujuan.
- ~~**Depth sensor Gemini** — `pipeline/` menunggu data fisik.~~ **SUDAH DIUJI
  (2026-07-29, E-022/SR-014)** pada dataset `ULM-DS-Lab/SawitMVC-Depth` (352 pohon,
  1.408 citra RGB-D, sensor Orbbec). Lubang §5 ini tertutup. Yang perlu keputusan
  sekarang: apakah melanjutkan ke **E-023 fusi menengah** (didukung bukti sendiri —
  lihat SR-014 §6) atau menambah data B4 lebih dulu.
- **`pipeline/prepare_depth.py` tidak boleh dipakai untuk data Orbbec.** Ia
  berasumsi depth sudah tersejajar ke RGB; untuk dataset ini asumsi itu SALAH dan
  menghasilkan kanal ke-4 yang meleset median 29 px. Pakai
  `experiments/reproject_depth.py`. Rentang metrik `fourch.Z_NEAR/Z_FAR` (0,3–8,0 m)
  juga tidak cocok untuk sensor ini — untuk SawitMVC-Depth dipakai 0,8/15,0 m.

---

## 6. Reproduksi & lingkungan

Kode di `experiments/` (arsip repo) dan `/workspace/experiments/` (kerja).
Dataset: `/workspace/SawitMVC/data/` (960×1280) dan `/workspace/Sawit/data/`
(master 3024×4032). `pip install -r experiments/requirements.txt`, CUDA (L4).
Split per pohon 716/96/141, **irisan nol** — jaga ini.

Panduan reproduksi langkah demi langkah (skrip→SR→keluaran, versi persis, celah
jujur): [`../experiments/REPRODUCE.md`](../experiments/REPRODUCE.md).
