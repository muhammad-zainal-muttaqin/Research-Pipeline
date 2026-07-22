# experiments/ — Arsip kode & hasil eksperimen

Snapshot **kode dan angka** dari `/workspace/experiments/` (di luar repo saat
eksperimen berjalan). Diselamatkan ke sini agar setiap perintah reproduksi di
`docs/SR/` dan `docs/EKSPERIMEN.md` tetap punya sumbernya meski folder kerja
aslinya dihapus.

## Yang ADA di sini

- **`*.py`** (33 skrip) — seluruh kode eksperimen E-001…E-020. Tiap SR menyebut
  skrip yang memproduksinya di bagian "Reproduksi".
- **`results/*.json`** — angka mentah di balik setiap tabel SR (mis.
  `diag_bottleneck.json` = E-014, `loc_ceiling.json` = E-018,
  `raw_map.json` = peta master E-015, `class_mismatch.json` = E-001).
- **`splits_rgb/*.txt`** — definisi split train/val/test **persis** yang dipakai
  (per pohon, irisan nol). Ini yang membuat angka dapat direproduksi bit-per-bit.
- **`runs/<run>/results.csv`** — kurva metrik **per-epoch** (P/R/mAP50/mAP50-95)
  untuk kelima run detektor, plus `args.yaml` (konfigurasi persis tiap run).
- **`logs/*.txt`** — keluaran konsol tiap eksperimen, **sudah dibersihkan** dari
  progress-bar (\r). Rekam mentah yang dicetak ultralytics.
- **`data_*.yaml`**, **`requirements.txt`**, **`run_queue*.sh`** — konfigurasi
  dataset, lingkungan, dan orkestrasi antrean pelatihan.

Tabel metrik lengkap semua run (per-kelas B1–B4, val+test) dirangkum di
[`../docs/METRICS.md`](../docs/METRICS.md).

## Yang TIDAK ada (sengaja — bisa dibuat ulang dari skrip di atas)

| Artefak | Ukuran | Cara membuat ulang |
|---|---|---|
| Bobot model (`runs/**/*.pt`) | ~2,2 GB | jalankan skrip `train_*.py` |
| Potongan tandan (`crops/`, `crops_raw/`) | ~1,3 GB | `build_crops.py`, `build_crops_raw.py` |
| Dataset master (`master_ds/`) | — | `build_master_ds.py` (butuh `results/raw_map.json`) |
| Pseudo-depth (`depth_da3/`) | ~765 MB | `gen_depth_dataset.py` |
| Ubin (`data_tiles/`) | ~1,5 GB | `tiling.py --build` |
| Visualisasi (`results/e003–e005/`) | ~100 MB | skrip DA3 terkait |
| Log mentah (`logs-*.txt`) | ~5 MB | keluaran ulang saat menjalankan |

## Prasyarat menjalankan

Skrip mengharap dataset SawitMVC di `/workspace/SawitMVC/data/` dan master
mentah di `/workspace/Sawit/data/` (lihat `CLAUDE.md`). Lingkungan: `pip install
-r requirements.txt` pada Python dengan CUDA (dikembangkan di NVIDIA L4).

Kode ini **bukan deliverable produksi** — untuk itu lihat `pipeline/`. Ini
catatan ilmiah: bukti bahwa angka di SR benar-benar berasal dari kode yang
dijalankan, bukan diketik.
