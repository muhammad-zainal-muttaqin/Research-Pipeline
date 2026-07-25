# REPRODUCE — cara mereproduksi setiap angka

Panduan untuk mereproduksi hasil di `docs/eksperimen/METRICS.md` / `docs/eksperimen/SR`. Jawaban jujur
atas "bisakah direproduksi dari info yang ada": **ya untuk eksperimen detektor**
(E-009…E-021, termasuk RF-DETR/RT-DETR/YOLO26l), dengan catatan di §4; **ya untuk
jalur DA3** (E-003…E-007) bila DA3 dipasang.

## 1. Lingkungan (versi persis)

| Paket | Versi | Sumber |
|---|---|---|
| Python | 3.12 | — |
| torch | 2.8.0+cu128 | image sistem |
| torchvision | 0.23.0+cu128 | image sistem |
| ultralytics | **8.4.103** | pip (`requirements.txt`) |
| numpy | 1.26.4 | pip |
| opencv | 4.11.0 | pip |
| pycocotools | **2.0.11** | pip |
| **rfdetr** (E-021) | **1.8.3** | pip |
| supervision (E-021) | 0.29.1 | pip |
| ultralytics-thop / matplotlib (E-021) | 2.0.20 / — | pip |
| GPU / CUDA | NVIDIA L4 / 12.8 | — |

`pip install -r requirements.txt`. Versi ultralytics **penting** (nama kolom
`results.csv` & API `.val()` bisa berubah). Versi **rfdetr penting**: default
library-nya (lr, ema, warmup, dll) menentukan training RF-DETR — konfigurasi
efektif lengkap juga terekam di `runs/rfdetr_l_e60_i1280/training_config.json`.

## 2. Data (tidak diarsipkan — publik)

| Dataset | Lokasi diharapkan | Sumber |
|---|---|---|
| SawitMVC (960×1280, anotasi) | `/workspace/SawitMVC/data/` | HuggingFace `ULM-DS-Lab/SawitMVC`, CC BY-NC 4.0 (`download.py`) |
| Sawit master (3024×4032) | `/workspace/Sawit/data/` | `download.py` di folder itu |

**Split** ada di repo (`splits_rgb/*.txt`) dan **memakai path absolut**
`/workspace/SawitMVC/data/images/...`. Di lingkungan baru, taruh data di path
sama, atau `sed -i 's#/workspace/SawitMVC#/path/baru#' splits_rgb/*.txt`. Split
per pohon 716/96/141 dengan **irisan nol** — jangan diacak ulang.

## 3. Peta skrip → SR → keluaran

| Skrip | Eksperimen | SR | Keluaran |
|---|---|---|---|
| `experiments/analysis/class_mismatch_stats.py` | E-001 | SR-001 | `experiments/results/E-001/class_mismatch.json` |
| `experiments/analysis/da3_video_test.py`, `experiments/analysis/da3_video_multi.py` | E-003, E-004 | SR-003 | `experiments/results/E-003*, experiments/results/E-004` |
| `experiments/analysis/da3_sides_test.py` | E-005 | SR-004 | `experiments/results/E-005` |
| `experiments/analysis/depth_bunch_signal.py` | E-006 | SR-005 | `experiments/results/E-006` |
| `experiments/analysis/geometric_linking.py` | E-007 | SR-006 | `experiments/results/E-007` |
| `experiments/analysis/box_size_analysis.py` | E-009 | SR-007 | `experiments/results/E-009` |
| `experiments/analysis/why_b4_fails.py` | E-010 | SR-007 | `experiments/results/E-010` |
| `experiments/analysis/contrast_boost_test.py` | E-011 | SR-008 | `experiments/results/E-011` |
| `experiments/analysis/class_separability.py` | E-012 | SR-009 | `experiments/results/E-012` |
| `experiments/eval/diag_bottleneck.py` | E-014 | SR-010 | `experiments/results/E-014/diag_bottleneck.json` |
| `experiments/build/match_raw.py` | E-015 | SR-002 | `experiments/results/E-015/raw_map.json` |
| `experiments/analysis/head_vs_crop.py`, `experiments/analysis/multiview_vote.py`, `experiments/eval/metric_variants.py` | E-016 | SR-011 (ditarik) | `experiments/results/E-016/head_vs_crop.json` dll |
| `experiments/train/train_agnostic.py`, `experiments/train/train_maturity_v2.py`, `experiments/analysis/two_stage.py` | E-017 | SR-012 | `results/two_stage_val_*.json` |
| `experiments/analysis/loc_ceiling.py` | E-018 | — | `experiments/results/E-018/loc_ceiling.json` |
| `experiments/train/train_4cls_hi.py` | E-019 | — | `runs/c4_e50_i1280_warna/` |
| `experiments/train/train_rtdetr.py`, `experiments/eval/eval_rtdetr.py` | E-020 | SR-013 | `runs/rtdetr_l_e60_i1280/`, `experiments/results/E-020/rtdetr_eval.json` |
| `experiments/build/build_rfdetr_ds.py`, `experiments/train/train_rfdetr.py` | E-021 | — | `runs/rfdetr_l_e60_i1280/` (evaluation.json, metrics.csv, **training_config.json**) |
| `experiments/train/train_yolo26l.py` | E-021 | — | `runs/yolo26l_e60_i1280/`, `experiments/results/E-021/yolo26l_eval.json` |
| `experiments/eval/eval_perkelas.py`, `experiments/eval/eval_rfdetr_perkelas.py` | E-021 | — | `experiments/results/E-021/perkelas_fair.json` |
| `experiments/eval/eval_all_pycoco.py` | E-021 | — | `experiments/results/E-021/perkelas_pycoco.json` (1-protokol) |
| `experiments/eval/eval_all_metrics.py` | E-021 | — | `experiments/results/E-021/metrics_full.json` (COCO 12-stat + P/R/F1) |
| `experiments/eval/eval_extras.py` | E-021 | — | `results/{confusion,bootstrap_ci,pr_curves}.json`, `figures/*.png` |
| `experiments/eval/eval_efficiency.py` | E-021 | — | `experiments/results/E-021/efficiency.json` |
| `experiments/train/train_fusion.py` | I-4 (RGBD) | — | `runs/rgbd_e60_i640_s42/` |
| `experiments/eval/eval_missing.py` | — | — | `experiments/results/lintas-eksperimen/eval_missing.json` (per-kelas RGBD & c4) |

Konfigurasi persis tiap run pelatihan ada di `runs/<run>/args.yaml` (ultralytics)
atau `runs/<run>/training_config.json` (RF-DETR); kurva per-epoch di
`runs/<run>/results.csv` / `metrics.csv`; keluaran konsol di `logs/`. Urutan E-021:
`experiments/build/build_rfdetr_ds.py` → `experiments/train/train_rfdetr.py` → `experiments/train/train_yolo26l.py` → `experiments/eval/eval_all_pycoco.py`
→ `experiments/eval/eval_all_metrics.py` → `experiments/eval/eval_extras.py` → `experiments/eval/eval_efficiency.py`. Ringkasan jebakan
teknis di [`CATATAN-TEKNIS-E021.md`](CATATAN-TEKNIS-E021.md).

## 4. Yang TIDAK akan bit-per-bit sama (jujur)

1. **Non-determinisme GPU.** Meski `seed=42`, operasi CUDA (cuDNN, atomics)
   tidak deterministik penuh. Angka akan **sangat dekat** (±0,005 mAP), bukan
   identik. `docs/eksperimen/METRICS.md` adalah angka run yang sebenarnya terjadi.
2. **Bobot terlatih tidak diarsipkan** (best 53–264 MB/run). Harus dilatih ulang
   dari skrip, atau — untuk **RF-DETR-L (model terbaik, E-021)** — diarsipkan ke
   penyimpanan objek dulu (belum dilakukan; lihat `docs/eksperimen/STATUS.md` §1). Bobot
   E-021: RF-DETR `checkpoint_best_ema.pth` (142 MB), RT-DETR `best.pt` (264 MB),
   YOLO26l `best.pt` (53 MB).
3. **Dataset turunan** (crops, master_ds, depth_da3, tiles) dibuat ulang dari
   skrip build (`experiments/build/build_crops_raw.py`, `experiments/build/build_master_ds.py`, `experiments/build/gen_depth_dataset.py`).
4. **Jalur DA3 (E-003…E-007)** butuh Depth Anything 3 dipasang terpisah
   (`requirements.txt`). Tanpa DA3, SR-003…SR-006 tak bisa direproduksi; tetapi
   angka + kesimpulannya terekam di SR-nya.

## 5. Untuk sekadar MELAPORKAN (bukan menjalankan ulang)

Cukup dari repo, tanpa GPU/data:
- **Angka:** `docs/eksperimen/METRICS.md` (per-kelas B1–B4, val+test, semua run; tabel
  1-protokol + metrik penuh + efisiensi + bootstrap + confusion E-021) +
  `results/*.json` (mentah: `metrics_full`, `perkelas_pycoco`, `bootstrap_ci`,
  `confusion`, `efficiency`, `pr_curves`).
- **Narasi & pembelaan tiap klaim:** `docs/eksperimen/SR` + `docs/eksperimen/EKSPERIMEN.md` (log
  kronologis E-001…E-021).
- **Figur:** `figures/*.png` (confusion, PR, F1-confidence — E-021).
- **Kurva pelatihan:** `runs/<run>/results.csv` / `metrics.csv`.
- **Konfigurasi:** `runs/<run>/args.yaml` (ultralytics) atau `training_config.json`
  (RF-DETR — seluruh hyperparameter efektif).

Semua klaim numerik dapat dilacak ke JSON/CSV sumbernya — itu memang prinsip repo.
