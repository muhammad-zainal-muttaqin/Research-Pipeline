# experiments/ — Arsip kode & hasil eksperimen

Snapshot **kode dan angka** dari `/workspace/experiments/` (di luar repo saat
eksperimen berjalan). Diselamatkan ke sini agar setiap perintah reproduksi di
`docs/eksperimen/SR/` dan `docs/eksperimen/EKSPERIMEN.md` tetap punya sumbernya meski folder
kerja aslinya dihapus.

## Yang ADA di sini

| Folder | Isi |
|---|---|
| `train/` (10) | Skrip pelatihan model |
| `eval/` (12) | Skrip pengukuran dan diagnosis metrik |
| `build/` (7) | Penyiapan dataset turunan (potongan, master, pseudo-depth) |
| `analysis/` (16) | Uji hipotesis dan diagnosis, satu skrip per pertanyaan |
| `shell/` (8) | Orkestrasi antrean pelatihan |
| `config/` (2) | `data_rgb.yaml`, `data_rgbd4.yaml` |
| `results/` | JSON mentah, dikelompokkan per eksperimen — indeks di [`results/README.md`](results/README.md) |
| `runs/` | `args.yaml` / `training_config.json` + kurva per-epoch (`results.csv`, `metrics.csv`) |
| `logs/` | Keluaran konsol, sudah dibersihkan dari progress-bar (\r) |
| `figures/` | Confusion matrix, kurva PR, kurva F1-confidence (E-021) |
| `splits_rgb/` | Definisi split train/val/test **persis** per pohon, irisan nol — ini yang membuat angka dapat direproduksi |

**Peta lengkap skrip → eksperimen → keluaran ada di
[`PETA-SKRIP.md`](PETA-SKRIP.md).** Perintah reproduksi dan versi paket persis
di [`REPRODUCE.md`](REPRODUCE.md).

`requirements.txt` sengaja tetap di akar folder ini supaya
`pip install -r requirements.txt` berjalan apa adanya.

Tabel metrik lengkap semua run (per-kelas B1–B4, val+test) dirangkum di
[`docs/eksperimen/METRICS.md`](../docs/eksperimen/METRICS.md).

## Yang TIDAK ada (sengaja — bisa dibuat ulang dari skrip di atas)

| Artefak | Ukuran | Cara membuat ulang |
|---|---|---|
| Bobot model (`runs/**/*.pt`) | ~2,2 GB | jalankan skrip `train_*.py` |
| Potongan tandan (`crops/`, `crops_raw/`) | ~1,3 GB | `experiments/build/build_crops.py`, `experiments/build/build_crops_raw.py` |
| Dataset master (`master_ds/`) | — | `experiments/build/build_master_ds.py` (butuh `experiments/results/E-015/raw_map.json`) |
| Pseudo-depth (`depth_da3/`) | ~765 MB | `experiments/build/gen_depth_dataset.py` |
| Ubin (`data_tiles/`) | ~1,5 GB | `experiments/analysis/tiling.py --build` |
| Visualisasi (`results/E-003/`…`results/E-005/`) | ~100 MB | skrip DA3 terkait |
| Log mentah (`logs-*.txt`) | ~5 MB | keluaran ulang saat menjalankan |

## Prasyarat menjalankan

Skrip mengharap dataset SawitMVC di `/workspace/SawitMVC/data/` dan master
mentah di `/workspace/Sawit/data/` (lihat `CLAUDE.md`). Lingkungan: `pip install
-r requirements.txt` pada Python dengan CUDA (dikembangkan di NVIDIA L4).

Kode ini **bukan deliverable produksi** — untuk itu lihat `pipeline/`. Ini
catatan ilmiah: bukti bahwa angka di SR benar-benar berasal dari kode yang
dijalankan, bukan diketik.
