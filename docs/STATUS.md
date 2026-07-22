# STATUS — titik berhenti & cara melanjutkan

**Terakhir diperbarui:** 2026-07-22 · **Status:** dijeda dengan rapi, siap dilanjutkan.

Metrik lengkap semua run (per-kelas B1–B4, val+test) di [`METRICS.md`](METRICS.md).

Dokumen ini adalah **titik masuk tunggal** saat pekerjaan dilanjutkan. Baca ini
dulu, lalu `docs/SR/README.md` (cerita per-ide) dan `docs/EKSPERIMEN.md` (log
kronologis E-001…E-020).

---

## 1. Di mana kita sekarang

**Sasaran** (ditetapkan pengguna, tidak dapat ditawar dengan pembingkaian ulang):
**mAP50 0,60 dan mAP50-95 0,30 pada 4 kelas penuh (B1–B4)**, angka COCO apa
adanya, pilih di val / lapor di test, tanpa hack.

**Hasil terbaik saat ini — RT-DETR-L (NMS-free), lihat [SR-013](SR/SR-013-rtdetr-nms-free.md):**

| | mAP50 | mAP50-95 | ke target |
|---|---|---|---|
| TEST | **0,5794** | **0,2694** | mAP50 −0,021 · mAP50-95 −0,031 |
| VAL | 0,5466 | 0,2543 | mAP50 −0,053 · mAP50-95 −0,046 |

Terdekat yang pernah dicapai. **Belum tembus target**, tetapi test tinggal
−0,021 dari mAP50 0,60. RT-DETR-L unggul di **keempat kelas** dibanding baseline
yolo26m, dengan gain terbesar di **B4** (+0,089 test) — kelas terpadat/tersamar.

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
- **`experiments/`** — arsip 35 skrip + 29 JSON hasil + split, seluruh E-001…E-020.

---

## 4. Jalur lanjutan yang belum tersentuh (prioritas turun)

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
- **Depth sensor Gemini** — `pipeline/` menunggu data fisik. Depth SENSOR
  (metrik, pengukuran independen) belum pernah diuji; hanya pseudo-depth (E-006).

---

## 6. Reproduksi & lingkungan

Kode di `experiments/` (arsip repo) dan `/workspace/experiments/` (kerja).
Dataset: `/workspace/SawitMVC/data/` (960×1280) dan `/workspace/Sawit/data/`
(master 3024×4032). `pip install -r experiments/requirements.txt`, CUDA (L4).
Split per pohon 716/96/141, **irisan nol** — jaga ini.

Panduan reproduksi langkah demi langkah (skrip→SR→keluaran, versi persis, celah
jujur): [`../experiments/REPRODUCE.md`](../experiments/REPRODUCE.md).
