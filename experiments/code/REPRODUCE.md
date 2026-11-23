# REPRODUCE - cara mereproduksi setiap angka

Panduan untuk mereproduksi hasil di `experiments/METRICS.md` / `experiments/SR`. Jawaban jujur
atas "bisakah direproduksi dari info yang ada": **ya untuk eksperimen detektor**
(E-009…E-021, termasuk RF-DETR/RT-DETR/YOLO26l), dengan catatan di §4; **ya untuk
jalur DA3** (E-003…E-007) bila DA3 dipasang.

## 1. Lingkungan (versi persis)

| Paket | Versi | Sumber |
|---|---|---|
| Python | 3.12 | - |
| torch | 2.8.0+cu128 | image sistem |
| torchvision | 0.23.0+cu128 | image sistem |
| ultralytics | **8.4.103** | pip (`requirements.txt`) |
| numpy | 1.26.4 | pip |
| opencv | 4.11.0 | pip |
| pycocotools | **2.0.11** | pip |
| **rfdetr** (E-021) | **1.8.3** | pip |
| supervision (E-021) | 0.29.1 | pip |
| ultralytics-thop / matplotlib (E-021) | 2.0.20 / - | pip |
| GPU / CUDA | NVIDIA L4 / 12.8 | - |

`pip install -r experiments/code/requirements.txt`. Versi ultralytics **penting** (nama kolom
`results.csv` & API `.val()` bisa berubah). Versi **rfdetr penting**: default
library-nya (lr, ema, warmup, dll) menentukan training RF-DETR - konfigurasi
efektif lengkap juga terekam di `experiments/runs/rfdetr_l_e60_i1280/training_config.json`.

## 2. Data (tidak diarsipkan - publik)

| Dataset | Lokasi diharapkan | Sumber |
|---|---|---|
| SawitMVC (960×1280, anotasi) | `/workspace/SawitMVC/data/` | HuggingFace `ULM-DS-Lab/SawitMVC`, CC BY-NC 4.0 (`download.py`) |
| Sawit master (3024×4032) | `/workspace/Sawit/data/` | `download.py` di folder itu |

**Split** ada di repo (`experiments/splits/rgb/*.txt`) dan **memakai path absolut**
`/workspace/SawitMVC/data/images/...`. Di lingkungan baru, taruh data di path
sama, atau `sed -i 's#/workspace/SawitMVC#/path/baru#' experiments/splits/rgb/*.txt`. Split
per pohon 716/96/141 dengan **irisan nol** - jangan diacak ulang.

## 3. Peta skrip → SR → keluaran

| Skrip | Eksperimen | SR | Keluaran |
|---|---|---|---|
| `analysis/class_mismatch_stats.py` | E-001 | SR-001 | `experiments/results/E-001/class_mismatch.json` |
| `analysis/da3_video_test.py`, `analysis/da3_video_multi.py` | E-003, E-004 | SR-003 | `experiments/results/E-003*, results/E-004` |
| `analysis/da3_sides_test.py` | E-005 | SR-004 | `experiments/results/E-005` |
| `analysis/depth_bunch_signal.py` | E-006 | SR-005 | `experiments/results/E-006` |
| `analysis/geometric_linking.py` | E-007 | SR-006 | `experiments/results/E-007` |
| `analysis/box_size_analysis.py` | E-009 | SR-007 | `experiments/results/E-009` |
| `analysis/why_b4_fails.py` | E-010 | SR-007 | `experiments/results/E-010` |
| `analysis/contrast_boost_test.py` | E-011 | SR-008 | `experiments/results/E-011` |
| `analysis/class_separability.py` | E-012 | SR-009 | `experiments/results/E-012` |
| `eval/diag_bottleneck.py` | E-014 | SR-010 | `experiments/results/E-014/diag_bottleneck.json` |
| `build/match_raw.py` | E-015 | SR-002 | `experiments/results/E-015/raw_map.json` |
| `analysis/head_vs_crop.py`, `analysis/multiview_vote.py`, `eval/metric_variants.py` | E-016 | SR-011 (ditarik) | `experiments/results/E-016/head_vs_crop.json` dll |
| `train/train_agnostic.py`, `train/train_maturity_v2.py`, `analysis/two_stage.py` | E-017 | SR-012 | `experiments/results/two_stage_val_*.json` |
| `analysis/loc_ceiling.py` | E-018 | - | `experiments/results/E-018/loc_ceiling.json` |
| `train/train_4cls_hi.py` | E-019 | - | `experiments/runs/c4_e50_i1280_warna/` |
| `train/train_rtdetr.py`, `eval/eval_rtdetr.py` | E-020 | SR-013 | `experiments/runs/rtdetr_l_e60_i1280/`, `experiments/results/E-020/rtdetr_eval.json` |
| `build/build_rfdetr_ds.py`, `train/train_rfdetr.py` | E-021 | - | `experiments/runs/rfdetr_l_e60_i1280/` (evaluation.json, metrics.csv, **training_config.json**) |
| `train/train_yolo26l.py` | E-021 | - | `experiments/runs/yolo26l_e60_i1280/`, `experiments/results/E-021/yolo26l_eval.json` |
| `eval/eval_perkelas.py`, `eval/eval_rfdetr_perkelas.py` | E-021 | - | `experiments/results/E-021/perkelas_fair.json` |
| `eval/eval_all_pycoco.py` | E-021 | - | `experiments/results/E-021/perkelas_pycoco.json` (1-protokol) |
| `eval/eval_all_metrics.py` | E-021 | - | `experiments/results/E-021/metrics_full.json` (COCO 12-stat + P/R/F1) |
| `eval/eval_extras.py` | E-021 | - | `experiments/results/{confusion,bootstrap_ci,pr_curves}.json`, `figures/*.png` |
| `eval/eval_efficiency.py` | E-021 | - | `experiments/results/E-021/efficiency.json` |
| `train/train_fusion.py` | I-4 (RGBD) | - | `experiments/runs/rgbd_e60_i640_s42/` |
| `eval/eval_missing.py` | - | - | `experiments/results/lintas-eksperimen/eval_missing.json` (per-kelas RGBD & c4) |

Konfigurasi persis tiap run pelatihan ada di `experiments/runs/<run>/args.yaml` (ultralytics)
atau `experiments/runs/<run>/training_config.json` (RF-DETR); kurva per-epoch di
`experiments/runs/<run>/results.csv` / `metrics.csv`; keluaran konsol di `experiments/logs/`. Urutan E-021:
`build/build_rfdetr_ds.py` → `train/train_rfdetr.py` → `train/train_yolo26l.py` → `eval/eval_all_pycoco.py`
→ `eval/eval_all_metrics.py` → `eval/eval_extras.py` → `eval/eval_efficiency.py`. Jebakan teknisnya
ada di §6.

## 4. Yang TIDAK akan bit-per-bit sama (jujur)

1. **Non-determinisme GPU.** Meski `seed=42`, operasi CUDA (cuDNN, atomics)
   tidak deterministik penuh. Angka akan **sangat dekat** (±0,005 mAP), bukan
   identik. `experiments/METRICS.md` adalah angka run yang sebenarnya terjadi.
2. **Bobot terlatih tidak diarsipkan** (best 53–264 MB/run). Harus dilatih ulang
   dari skrip, atau - untuk **RF-DETR-L (model terbaik, E-021)** - diarsipkan ke
   penyimpanan objek dulu (belum dilakukan). Bobot
   E-021: RF-DETR `checkpoint_best_ema.pth` (142 MB), RT-DETR `best.pt` (264 MB),
   YOLO26l `best.pt` (53 MB).
3. **Dataset turunan** (crops, master_ds, depth_da3, tiles) dibuat ulang dari
   skrip build (`build/build_crops_raw.py`, `build/build_master_ds.py`, `build/gen_depth_dataset.py`).
4. **Jalur DA3 (E-003…E-007)** butuh Depth Anything 3 dipasang terpisah
   (`requirements.txt`). Tanpa DA3, SR-003…SR-006 tak bisa direproduksi; tetapi
   angka + kesimpulannya terekam di SR-nya.

## 5. Untuk sekadar MELAPORKAN (bukan menjalankan ulang)

Cukup dari repo, tanpa GPU/data:
- **Angka:** `experiments/METRICS.md` (per-kelas B1–B4, val+test, semua run; tabel
  1-protokol + metrik penuh + efisiensi + bootstrap + confusion E-021) +
  `experiments/results/*.json` (mentah: `metrics_full`, `perkelas_pycoco`, `bootstrap_ci`,
  `confusion`, `efficiency`, `pr_curves`).
- **Narasi & pembelaan tiap klaim:** `experiments/SR` + `experiments/EKSPERIMEN.md` (log
  kronologis E-001…E-021).
- **Figur:** `figures/*.png` (confusion, PR, F1-confidence - E-021).
- **Kurva pelatihan:** `experiments/runs/<run>/results.csv` / `metrics.csv`.
- **Konfigurasi:** `experiments/runs/<run>/args.yaml` (ultralytics) atau `training_config.json`
  (RF-DETR - seluruh hyperparameter efektif).

Semua klaim numerik dapat dilacak ke JSON/CSV sumbernya - itu memang prinsip repo.

## 6. Jebakan teknis dan keputusan fairness E-021

Dicatat dari run 24–25 Juli 2026. Angka hasil keempat model ada di
[`../METRICS.md`](../METRICS.md). Log konsol run ini: `logs/logs-rfdetr-e60.txt`,
`logs-rfdetr-smoke.txt`, `logs-rfdetr-install.txt`, `logs-rfdetr-install2.txt`,
`logs-rfdetr-perkelas.txt`, `logs-yolo26l.txt`, `logs-pycoco-all.txt` (semuanya
di `experiments/logs/`).

### Jebakan RF-DETR (rfdetr 1.8.3)

1. **Resolusi harus kelipatan 32**, BUKAN 56. Constraint = patch_size(16) ×
   num_windows(2) = 32. Jadi 1280 valid (1280/32=40) dan cocok persis dengan
   RT-DETR. (Awalnya diduga 56 → salah; error: "resolution=1288 is not divisible
   by patch_size (16) * num_windows (2) = 32".)

2. **`multi_scale`/`expanded_scales` default melatih di 1440, BUKAN resolusi yang
   diminta.** Default `multi_scale=True`+`expanded_scales=True`, dan karena
   `do_random_resize_via_padding=False`, ia mengunci ke skala TERBESAR =
   resolusi×45/40 = 1440. **Untuk fairness @1280 WAJIB set
   `multi_scale=False, expanded_scales=False`.** Tanpa ini RF-DETR diam-diam dapat
   keunggulan resolusi. Cek log: baris "Using multi-scale training ... scales:
   [1440]" TIDAK boleh muncul.

3. **Tidak ada `.evaluate()` di rfdetr 1.8.3.** Pakai `run_test=True` di `.train()`
   → metrik test masuk `metrics.csv` (kolom `test/*`). Val dicatat tiap epoch
   (`val/mAP_50`, `val/mAP_50_95`, `val/AP/Bx`, plus varian `val/ema_*`).

4. **Per-kelas `val/AP/Bx` di metrics.csv & evaluation.json = AP50-95, BUKAN AP50.**
   Untuk AP50 per-kelas harus COCO-eval terpisah (`eval/eval_rfdetr_perkelas.py`).

5. **Checkpoint: `run_test` memakai `checkpoint_best_total.pth` untuk test**
   (memberi test 0,5837/0,2653), sedangkan checkpoint terbaik-val = EMA
   (`checkpoint_best_ema.pth`). Eval EMA konsisten val↔test memberi test
   0,6038/0,2770. Val pycocotools EMA (0,5695) cocok dengan evaluator internal
   rf-detr (0,5699) → pipeline tervalidasi. **Pakai EMA konsisten.**

6. **Resume:** `RFDETRLarge(..., resume="runs/.../last.ckpt")` (PTL ckpt_path).
   `train/train_rfdetr.py --resume` sudah mendukung.

### Jebakan performa GPU (NVIDIA L4, 23 GB, TDP 72 W)

7. **GPU kelaparan data dengan `num_workers` default 2** → util loncat 5%↔100%
   (rata-rata rendah), ~5 jam untuk 60 epoch. Naikkan ke 8. (128 core tersedia,
   tapi lihat #8.)

8. **JANGAN maksimalkan worker/batch membabi-buta.** batch16 × workers32 →
   **`/dev/shm` (26 GB) penuh → DataLoader worker di-SIGKILL** ("DataLoader worker
   (pid …) is killed by signal: Killed"). RAM host 503 GB tak relevan; batasnya
   shared-memory. **Sweet spot: batch 8 / grad-accum 2 (effective 16) / workers 8**
   → shm ~2-3 GB, GPU util ~67-100%, tanpa crash.

9. **L4 power-limited.** Pada beban penuh: util 100%, **power 70/72 W (~97%)**,
   P-State P0. "100% util tapi 70 W" itu NORMAL - L4 memang GPU hemat daya; 70 W =
   sudah mentok. **~10 mnt/epoch adalah lantai** untuk RF-DETR-L @1280 di L4;
   lebih cepat hanya dengan GPU lebih kuat atau resolusi lebih rendah (merusak
   fairness).

### Keputusan fairness

- **Resolusi 1280 identik** untuk RT-DETR & RF-DETR & YOLO26l (YOLO26m 640 = acuan
  ringan, bukan pembanding sekelas).
- **Split identik** 3000/404/588 (E-017), augmentasi aman-warna (hsv kecil, E-019),
  seed 42, dari bobot COCO. `build/build_rfdetr_ds.py` = adaptor dataset YOLO→RF-DETR via
  symlink (tanpa salin citra).
- **Effective batch 16** untuk RF-DETR; RT-DETR/YOLO26l pakai batch 4 default
  ultralytics (perbedaan batch antar-framework kurang kritis dibanding resolusi).
- **Patience beda tapi adil:** RF-DETR patience 8 (stop ep17), RT-DETR & YOLO26l
  patience 60 (penuh). SEMUA melaporkan checkpoint **terbaik-val** - patience hanya
  soal kapan berhenti melatih, bukan checkpoint mana yang dilaporkan.
- **Baseline YOLO param-adil = YOLO26l** (26,3 jt, config IDENTIK RT-DETR). Tetap
  di bawah kedua DETR → keunggulan DETR **bukan** efek kapasitas/resolusi.
- **Evaluator campur diselesaikan:** semua 4 model dievaluasi ulang lewat
  **1-protokol pycocotools** (`eval/eval_all_pycoco.py`) - perbedaan protokol vs
  ultralytics `.val()` <0,005 (terkonfirmasi silang).

## 7. Membangun ulang lingkungan depth (E-022 dan sesudahnya)

Sesi 31 Juli–1 Agustus berjalan di workspace sementara. **12,1 GB state berada di
luar git dan akan hilang** bila workspace direset; yang tersisa hanyalah 968
berkas ter-track. Daftar ini menjawab "apa yang harus dibangun ulang, dalam
urutan apa" supaya tidak ditemukan ulang satu per satu.

Ukuran di bawah adalah hasil `du -sh` sebenarnya, diukur 1 Agustus sesaat sebelum
pod di-terminate - bukan taksiran. Angka taksiran sebelumnya meleset pada tiga
baris (`runs_e022` 2,5 → 4,0 GB, `runs_e023` 1,1 → 0,3 GB, `.venv` 1,2 → 2,8 GB);
jumlah berkas ter-track juga dikoreksi 770 → 968 (`git ls-files | wc -l`).

| Hilang | Ukuran | Cara mendapatkan kembali |
|---|---:|---|
| `/workspace/SawitMVC/data` | 2,3 GB | HuggingFace `ULM-DS-Lab/SawitMVC` |
| `/workspace/SawitMVC-Depth/data` | 2,6 GB | HuggingFace `ULM-DS-Lab/SawitMVC-Depth` (**private**, butuh token baru) |
| `experiments/results/depth_png/` | 211 MB | `build/reproject_depth.py`, ~10 menit |
| `runs/detect/runs_e022/` (**35 checkpoint**) | 4,0 GB | latih ulang; tidak ada jalan pintas |
| `runs/detect/runs_e023/` (**15 checkpoint**) | 315 MB | `shell/e023_fusi.sh` + `shell/e023_seed2024.sh`; ~4 jam pada satu A4500. Kurva latihan, `args.yaml`, dan SHA-256 tiap `best.pt` SUDAH diarsipkan di `experiments/results/E-023/` - cukup untuk memverifikasi apakah hasil latih-ulang menghasilkan checkpoint yang sama |
| `experiments/code/.venv` | 2,8 GB | `python -m venv --system-site-packages` |

### Urutan dan jebakannya

**1. Dataset - layout wajib `data/`.** Unduhan HuggingFace mendarat dengan
`images/`, `labels/`, `json/` di **akar**, sedangkan seluruh skrip dan split
mengharapkan `<root>/data/…`. Pindahkan. Untuk SawitMVC-Depth, `MERGE_MAP.csv`
dan `MERGE_VERIFICATION.json` juga harus ada **di dalam** `data/`
(`build/make_splits_depth.py` membacanya dari sana) - sambungkan dengan symlink.
Verifikasi integritas sebelum dipakai: 6.336 artefak ber-SHA256 terhadap
`manifests/`.

**2. venv - opencv.** `requirements.txt` memakai `opencv-python==4.11.0.86`.
Varian *headless* tidak mengekspor `cv2.imshow` yang disentuh ultralytics saat
impor, dan `pip install albumentations` menariknya kembali (E-033); pasang ulang
pin itu sesudahnya. Pasang
juga `numpy==1.26.4` **setelah** ultralytics, karena ultralytics menariknya ke
numpy 2.x. torch diwarisi dari image sistem, jangan dipasang lewat pip.

**3. depth_png - rentang metrik dibekukan.** Jalankan
`build/reproject_depth.py --z-near 0.8 --z-far 15.0`, **bukan** nilai bawaan.
Pemeriksaan bahwa hasilnya benar: cakupan piksel valid rata-rata harus
**0,710** (nilai beku di `depth_meta.json` 0,71032). Jangan memakai
`pipeline/prepare_depth.py` untuk dataset ini.

**4. Split - sudah di git, tetapi path-nya absolut.** `experiments/splits/depth/seed{42,1,2}`
dan `experiments/splits/rgb/sawitmvc` memuat path absolut ke `/workspace/…`, baik di
`*.txt` maupun di `path:` tiap `data_*.yaml`. Bila repo di-clone ke lokasi lain,
keduanya harus disesuaikan. Path pada `data_*.yaml` **wajib absolut** -
ultralytics me-resolve entri relatif terhadap `DATASETS_DIR`, bukan terhadap
lokasi yaml.

**5. Checkpoint - tidak ada jalan pintas.** 35 bobot tidak diarsipkan (kebijakan
repo). Yang tersedia sebagai gantinya: `metrics_lengkap.json` memuat **SHA-256
dan ukuran byte** tiap `best.pt`. Setelah latih ulang, bandingkan hash-nya -
kalau angkanya berbeda, hash membedakan "checkpoint memang lain" dari "resep
tidak tereproduksi".

### Yang tidak perlu dibangun ulang

Seluruh hasil sudah terarsip dan aman di git: 21 JSON berpasangan E-022,
`metrics_lengkap.json` (25 run, mAP50/mAP50-95/AP per kelas/P/R/F1/provenans),
hasil E-024/E-026/E-028, split, dan semua entri E-025 sampai E-031. **Membaca
kesimpulan tidak menuntut satu pun run diulang** - yang menuntut latih ulang
hanyalah melanjutkan ke E-023.
