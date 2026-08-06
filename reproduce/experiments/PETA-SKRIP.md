# PETA-SKRIP — 62 skrip, dikelompokkan menurut peran

Jawaban atas "skrip mana yang menghasilkan angka ini". Setiap baris menyebut
eksperimen penghasilnya dan tempat angkanya mendarat. Perintah reproduksi persis
beserta versi paket ada di [`REPRODUCE.md`](REPRODUCE.md).

Kolom **Eksperimen** memakai penomoran log di
[`../../docs/experiments/EKSPERIMEN.md`](../../docs/experiments/EKSPERIMEN.md); **SR**
merujuk laporan solusi di [`../../docs/experiments/SR/`](../../docs/experiments/SR/).

## Rute tugas

| Tugas | Jalur minimum | Hasil atau batas |
|---|---|---|
| Menghasilkan metrik E-021 | `build/build_rfdetr_ds.py` → `train/train_rfdetr.py` → `eval/eval_all_pycoco.py` | [`perkelas_pycoco.json`](../../evidence/experiments/results/E-021/perkelas_pycoco.json); baca [METRICS.md](../../docs/experiments/METRICS.md) sebelum melaporkan angka. |
| Mengaudit E-022 | [AUDIT-E022.md](../../docs/experiments/AUDIT-E022.md) → `analysis/verify_depth_mi.py` → `eval/eval_e022_paired.py` | Angka seed-42 bersifat historis. Bandingkan dengan [arsip E-022](../../docs/experiments/archive/E022-seed42-awal.md). |
| Menyiapkan depth sensor untuk pipeline produksi | [`../pipeline/prepare_depth.py`](../pipeline/prepare_depth.py) dengan `--mode gemini` | Untuk depth yang **sudah** disejajarkan ke RGB oleh SDK sensor. Depth SawitMVC-Depth ditangani `build/reproject_depth.py` (lihat catatan dua jalur di bawah). |

## `train/` — pelatihan model (12)

| Skrip | Eksperimen | Keluaran |
|---|---|---|
| `train_agnostic.py` | E-017 | detektor kelas-agnostik, `runs/agn_e25_i960_s42/` |
| `train_maturity.py` | E-016 | kepala kematangan ConvNeXt-Tiny pada potongan |
| `train_maturity_v2.py` | E-017 | kepala kematangan tahap dua |
| `train_ordinal.py` | E-012 | varian kepala ordinal (kematangan kontinu) |
| `train_fusion.py` | I-4 (RGBD) | `runs/rgbd_e60_i640_s42/` — 4 kanal RGB+depth |
| `train_4cls_hi.py` | E-019 | `runs/c4_e50_i1280_warna/` — 1280 aman-warna |
| `train_x.py` | E-013 | uji kapasitas yolo26x |
| `train_rtdetr.py` | E-020 | `runs/rtdetr_l_e60_i1280/` — RT-DETR-L NMS-free |
| `train_rfdetr.py` | E-021, **F-001/F-004** | `runs/rfdetr_l_e60_i1280/`; `runs_f004/rfdetrl_rgb_seed*` (flag `--seed` ditambah untuk seri F; bawaan 42 = E-021, jadi reproduksi E-021 tidak berubah) |
| `train_rfdetr_freq.py` | **F-007** (K1a) | `runs_f007/{dwt,laplacian,freq_rendah,fase_diacak}_seed*`; `--uji-sambungan` → `results/F-007/uji_sambungan_*.json` |
| `train_rfdetr_ordinal.py` | **F-006** (K2) | `runs_f006/*`; `--uji-sambungan` → `results/F-006/uji_sambungan.json` |
| `train_yolo26l.py` | E-021 | `runs/yolo26l_e60_i1280/` — baseline param-adil |

## `eval/` — pengukuran (14)

| Skrip | Eksperimen | Keluaran |
|---|---|---|
| `eval_baseline_test.py` | acuan | `results/lintas-eksperimen/baseline_test.json` |
| `eval_missing.py` | — | `results/lintas-eksperimen/eval_missing.json` |
| `diag_bottleneck.py` | E-014 | `results/E-014/diag_bottleneck.json` — agnostik vs 4-kelas |
| `metric_variants.py` | E-016 | `results/E-016/metric_variants.json`, `metric_pm1.json` |
| `eval_rtdetr.py` | E-020 | `results/E-020/rtdetr_eval.json` |
| `eval_perkelas.py`, `eval_rfdetr_perkelas.py` | E-021 | `results/E-021/perkelas_fair.json` |
| `eval_all_pycoco.py` | E-021 | `results/E-021/perkelas_pycoco.json` — **tabel 1-protokol** |
| `eval_all_metrics.py` | E-021 | `results/E-021/metrics_full.json` — COCO 12-stat + P/R/F1 |
| `eval_extras.py` | E-021 | `results/E-021/{confusion,bootstrap_ci,pr_curves}.json` + `figures/*.png`. **Resample CITRA, 2.000 replikat** — unit salah untuk seri F, lihat `bootstrap_pohon.py` |
| `dump_logits_rfdetr.py` | **F-004** | `results/F-004/logits_test_seed*.npz` — logit MENTAH seluruh query; masukan F-005 dan `bootstrap_pohon.py` |
| `bootstrap_pohon.py` | **rezim seri F** | CI95 persentil + BCa, resample **POHON**, 10.000 replikat; kontras berpasangan bila dua npz diberi |
| `eval_efficiency.py` | E-021 | `results/E-021/efficiency.json` — latensi & FPS di L4 |
| `stratified_eval.py` | — | evaluasi terstratifikasi; keluaran tidak diarsipkan |

## `build/` — penyiapan data (7)

| Skrip | Eksperimen | Keluaran |
|---|---|---|
| `match_raw.py` | E-015 | `results/E-015/raw_map.json` — pemetaan raw ↔ MVC berbasis isi |
| `build_master_ds.py` | E-015 | dataset master 3024×4032 (butuh `raw_map.json`) |
| `build_crops.py`, `build_crops_raw.py` | E-016 | potongan tandan untuk kepala kematangan |
| `make_depth.py`, `gen_depth_dataset.py` | I-4 | pseudo-depth untuk masukan 4 kanal |
| `build_rfdetr_ds.py` | E-021 | adaptor dataset YOLO → RF-DETR tanpa salin citra |

## `analysis/` — diagnosis & uji hipotesis (19)

| Skrip | Eksperimen | SR | Keluaran |
|---|---|---|---|
| `class_mismatch_stats.py` | E-001 | SR-001 | `results/E-001/class_mismatch.json` |
| `da3_video_test.py`, `da3_video_multi.py` | E-003, E-004 | SR-003 | `results/E-003/`, `E-003b/`, `E-004/` |
| `da3_sides_test.py` | E-005 | SR-004 | `results/E-005/` |
| `depth_bunch_signal.py` | E-006 | SR-005 | `results/E-006/` |
| `geometric_linking.py` | E-007 | SR-006 | `results/E-007/` |
| `box_size_analysis.py` | E-009 | SR-007 | `results/E-009/box_sizes.json` |
| `why_b4_fails.py` | E-010 | SR-007 | `results/E-010/why_b4.json` |
| `contrast_boost_test.py` | E-011 | SR-008 | `results/E-011/contrast_boost.json` |
| `freq_vs_pelepah.py` | **F-002** (P2) | SR-017 | `results/F-002/freq_vs_pelepah.json` — gerbang K1; tandan vs **pelepah**, bukan cincin |
| `plafon_lintas_sisi.py` | **F-003** (P3) | SR-017 | `results/F-003/plafon_lintas_sisi.json` — gerbang K3 |
| `massa_selisih_logit.py` | **F-005** (P1) | SR-017 | `results/F-005/massa_selisih_logit.json` — gerbang K2 |
| `class_separability.py` | E-012 | SR-009 | `results/E-012/separability.json` |
| `head_vs_crop.py`, `multiview_vote.py` | E-016 | SR-011 (ditarik) | `results/E-016/` |
| `two_stage.py` | E-017 | SR-012 | `results/E-017/two_stage_val_*.json` |
| `loc_ceiling.py` | E-018 | — | `results/E-018/loc_ceiling.json` — plafon lokalisasi |
| `tiling.py` | — | — | ubin citra (SAHI-like); dataset turunan |
| `conv8.py` | — | — | utilitas konversi |

## `shell/` — orkestrasi (10)

`run_queue.sh`…`run_queue4.sh`, `run_final.sh`, `chain_x.sh` menjalankan antrean
pelatihan berurutan; `progress_report.sh` mencetak ringkasan berjalan;
`stop_at_52.sh` menghentikan run RT-DETR pada epoch 52 (lihat E-020).
Skrip ini bergantung pada tata letak `/workspace/` dan bukan bagian dari jalur
reproduksi minimal.

Seri F menambah dua driver:

| Skrip | Eksperimen | Isi |
|---|---|---|
| `f004_baseline.sh` | F-004 | RF-DETR-L 3 seed berurutan + dump logit + SHA-256 tiap checkpoint |
| `f007_frekuensi.sh` | F-007 | 4 lengan × 3 seed = 12 run berurutan; `--periksa` = validasi prasyarat tanpa melatih |

**Keduanya BERURUTAN, dan itu bukan pilihan.** VRAM puncak RF-DETR-L @1280
batch 8 = 10.331 MiB dari 20.470 (F-001); dua run serentak = 20.662 MiB → OOM.
`f007_frekuensi.sh` karena itu punya **penjaga proses** yang menolak start bila
sudah ada `train_rfdetr*` berjalan — ditambahkan setelah menjalankan skrip itu
"sekadar untuk memeriksa" sempat menyalakan run sungguhan di atas F-004
(insiden 6 Agustus 2026, lihat [SERI-F.md](../../docs/experiments/SERI-F.md) §5.4).

## `config/` — konfigurasi dataset (2)

`data_rgb.yaml` (3 kanal) dan `data_rgbd4.yaml` (4 kanal RGB+depth) — berkas
dataset ultralytics. `requirements.txt` sengaja tetap di akar `experiments/`
supaya `pip install -r requirements.txt` tetap berjalan apa adanya.

## E-022 — depth SENSOR Orbbec 4-kanal (dataset SawitMVC-Depth)

Dijalankan pada dataset **berbeda** (`/workspace/SawitMVC-Depth/data`), jadi
angkanya tidak sebanding dengan E-001…E-021. Urutan jalan:

| Skrip | Fungsi | Keluaran |
|---|---|---|
| [`build/depth_calib.py`](build/depth_calib.py) | Parser kalibrasi sidecar + reproyeksi depth→bidang color (z-buffer, Brown-Conrady K6) | modul, dipakai skrip lain |
| [`analysis/verify_depth_mi.py`](analysis/verify_depth_mi.py) | **Gerbang wajib**: MI 4 kandidat pemetaan + kontrol pergeseran ±24 px | `results/E-022/mi.json` |
| [`analysis/verify_depth_align.py`](analysis/verify_depth_align.py) | Uji berbasis kotak anotasi (hasilnya tidak konklusif — dicatat apa adanya) | `results/E-022/align.json` |
| [`build/make_splits_depth.py`](build/make_splits_depth.py) | Split per-pohon terstratifikasi (device × unit-kamera × kelas-dominan) | `splits_depth/seed42/` |
| [`build/reproject_depth.py`](build/reproject_depth.py) | 1.408 PNG depth kanonik; Z_NEAR/Z_FAR dipilih dari histogram **train saja** | `depth_png/` + `results/E-022/depth_meta.json` |
| [`train/train_depth4ch.py`](train/train_depth4ch.py) | Latih ultralytics 4-kanal; `--depth-acak` (kontrol derau), `--depth-tukar` (kontrol registrasi) | `runs_e022/…/hasil.json` |
| [`train/train_rfdetr_4ch.py`](train/train_rfdetr_4ch.py) | RF-DETR 4-kanal lewat 4 tambalan (tanpa fork paket) | `runs_e022/rfdetrnano_*/` |
| [`eval/eval_e022_pycoco.py`](eval/eval_e022_pycoco.py) | 1-protokol pycocotools; mode kanal `rgbd`/`derau`/`tukar` | `results/E-022/pycoco_*.json` |
| [`eval/eval_e022_paired.py`](eval/eval_e022_paired.py) | Bootstrap berpasangan 2000× **per pohon** + CI per-kelas | `results/E-022/paired_*.json` |
| [`eval/eval_rfdetr_e022.py`](eval/eval_rfdetr_e022.py) | idem untuk RF-DETR dari `checkpoint_best_ema.pth` | `results/E-022/paired_rfdetrnano*.json` |
| [`shell/`](shell/) | `driver_e022.sh`, `queue_e022*.sh`, `antre_*.sh` — orkestrasi antrean | — |

**Dua jalur depth, masing-masing punya kasusnya sendiri.** `build/reproject_depth.py`
melayani SawitMVC-Depth: buffer `.raw` masih di grid kamera depth, jadi butuh
reproyeksi penuh (keputusan diambil di E-022a, meleset median 29 px bila hanya
di-resize). `../pipeline/prepare_depth.py` melayani keluaran Gemini yang sudah
di-align SDK di lapangan, dan hanya menerima `.png/.tif/.tiff` — ia tidak akan
memproses `.raw` dataset ini walau dipanggil. Lihat
[SR-015](../../docs/experiments/SR/SR-015-depth-sensor-4kanal.md).

## Bukti hasil

| Folder | Isi |
|---|---|
| [`results/`](../../evidence/experiments/results/) | JSON mentah, dikelompokkan per eksperimen |
| [`runs/`](../../evidence/experiments/runs/) | Konfigurasi + kurva per-epoch tiap run (`args.yaml`, `results.csv`, `metrics.csv`, `training_config.json`) |
| [`logs/`](../../evidence/experiments/logs/) | Keluaran konsol, sudah dibersihkan dari progress-bar |
| [`figures/`](../../evidence/experiments/figures/) | Confusion matrix, kurva PR, kurva F1-confidence (E-021) |
| [`splits_rgb/`](../../evidence/experiments/splits_rgb/) | Definisi split per pohon 716/96/141, irisan nol |
| [`splits_depth/`](../../evidence/experiments/splits_depth/) | Split per pohon 245/35/72 untuk SawitMVC-Depth (E-022), irisan nol |
