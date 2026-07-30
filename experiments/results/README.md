# results/ — indeks JSON hasil

Angka mentah di balik setiap tabel di
[`../../docs/eksperimen/METRICS.md`](../../docs/eksperimen/METRICS.md) dan setiap
putusan di [`../../docs/eksperimen/SR/`](../../docs/eksperimen/SR/). Dikelompokkan
per eksperimen; nama berkas sengaja **tidak diubah** supaya sitasi lama tetap
dapat ditelusuri lewat pencarian nama.

| Folder | Berkas | Eksperimen | Isi | Dikutip di |
|---|---|---|---|---|
| `E-001/` | `class_mismatch.json` | E-001 | Statistik `class_mismatch` — 0 dari 7.328 bunch multi-sisi | SR-001 (**dipalsukan**) |
| `E-003/`, `E-003b/` | `report.json` | E-003 | DA3 pada video orbit | SR-003 |
| `E-004/` | `report_rot.json` | E-004 | DA3 video, uji rotasi | SR-003 |
| `E-005/` | `report_4sides.json`, `report_8sides.json` | E-005 | DA3 pada 4/8 sisi foto | SR-004 |
| `E-006/` | `report_res504.json`, `report_res1008.json` | E-006 | Kedalaman sebagai pemisah tandan, dua resolusi | SR-005 (**dipalsukan**) |
| `E-007/` | `report_test.json`, `sweep.json` | E-007 | Penautan tandan lintas-sisi secara geometris | SR-006 (**dipalsukan**) |
| `E-009/` | `box_sizes.json` | E-009 | Sebaran ukuran kotak per kelas | SR-007 |
| `E-010/` | `why_b4.json` | E-010 | Diagnosis kegagalan B4 — kontras, bukan kepadatan | SR-007 |
| `E-011/` | `contrast_boost.json` | E-011 | Lima peta penajam kontras (CLAHE, unsharp, dll.) | SR-008 |
| `E-012/` | `separability.json` | E-012 | Keterpisahan kelas kematangan | SR-009 |
| `E-014/` | `diag_bottleneck.json` | E-014 | Agnostik vs 4-kelas — lokasi hambatan | SR-010 |
| `E-015/` | `raw_map.json` | E-015 | Pemetaan 3.992 citra raw ↔ MVC berbasis isi, nol ambigu | SR-002 |
| `E-016/` | `head_vs_crop.json`, `multiview_val.json`, `metric_variants.json`, `metric_pm1.json` | E-016 | Kepala kematangan, voting antar-sisi, varian metrik | SR-011 (**ditarik**, lihat E-018) |
| `E-017/` | `two_stage_val_A.json`, `_B`, `_mini_rawtest`, `_smoke` | E-017 | Detektor dua tahap | SR-012 (**dipalsukan**) |
| `E-018/` | `loc_ceiling.json` | E-018 | Plafon lokalisasi mAP50 0,8834 / mAP50-95 0,4702 | METRICS §deteksi kelas-agnostik |
| `E-020/` | `rtdetr_eval.json` | E-020 | RT-DETR-L, per-kelas val + test | SR-013 |
| `E-021/` | `perkelas_fair.json` | E-021 | Per-kelas AP50 + AP50-95 semua model | METRICS §val, §test |
| `E-021/` | `perkelas_pycoco.json` | E-021 | **Tabel 1-protokol** keempat model | METRICS §1-protokol |
| `E-021/` | `metrics_full.json` | E-021 | COCO 12-stat, per-kelas AR, P/R/F1 macro & micro | METRICS §metrik lengkap |
| `E-021/` | `confusion.json` | E-021 | Confusion matrix test, IoU 0,5, conf ≥ 0,25 | METRICS §confusion |
| `E-021/` | `bootstrap_ci.json` | E-021 | Bootstrap 2000× — selisih RF−RT signifikan | METRICS §signifikansi |
| `E-021/` | `pr_curves.json` | E-021 | Kurva PR micro & F1-confidence | METRICS §kurva PR |
| `E-021/` | `efficiency.json` | E-021 | Param, GFLOPs, latensi, FPS di NVIDIA L4 | METRICS §efisiensi |
| `E-021/` | `yolo26l_eval.json` | E-021 | YOLO26l baseline param-adil | METRICS §1-protokol |
| `E-022/` | `mi.json` | E-022a | Mutual information 4 kandidat pemetaan depth→RGB + kontrol pergeseran | METRICS §E-022 registrasi |
| `E-022/` | `align.json` | E-022a | Uji berbasis kotak anotasi (terbukti terlalu lemah, dicatat apa adanya) | SR-015 §3 |
| `E-022/` | `depth_meta.json` | E-022 | Kontrak kanal depth yang dibekukan (Z_NEAR 0,8 / Z_FAR 15,0, aturan invalid) | SR-015 §3 |
| `E-022/` | `pycoco_yolo26n.json` | E-022b | 1-protokol pycocotools YOLO26n RGB & RGB-D | METRICS §E-022 |
| `E-022/` | `paired_yolo26n.json` | E-022b | Selisih berpasangan RGB-D − RGB + CI per-kelas | METRICS §E-022 |
| `E-022/` | `paired_rtdetrl.json` | E-022b | idem, RT-DETR-L | METRICS §E-022 |
| `E-022/` | `paired_rfdetrnano.json` | E-022b | idem, RF-DETR Nano | METRICS §E-022 |
| `E-022/` | `paired_derau.json` | E-022b | **Kontrol negatif**: kanal ke-4 derau − RGB | METRICS §E-022 |
| `E-022/` | `paired_yolo26n_depth_vs_derau.json` | E-022b | Isolasi kandungan informasi depth (YOLO26n) | METRICS §E-022 |
| `E-022/` | `paired_rtdetrl_depth_vs_derau.json` | E-022b | idem, RT-DETR-L (B4 +0,1001 signifikan) | METRICS §E-022 |
| `E-022/` | `paired_rfdetrnano_depth_vs_derau.json` | E-022b | idem, RF-DETR Nano | METRICS §E-022 |
| `E-022/` | `paired_yolo26n_depth_vs_tukar.json` | E-022b | **Kontrol registrasi**: depth benar − depth pohon lain | METRICS §E-022 |

## `lintas-eksperimen/`

Berkas yang tidak dapat diatribusikan ke satu eksperimen tunggal. Tidak ditebak —
didaftar apa adanya.

| Berkas | Isi | Catatan |
|---|---|---|
| `baseline_test.json` | Baseline yolo26m pada test | Titik acuan yang mendahului penomoran E-0NN |
| `eval_missing.json` | Per-kelas untuk run RGBD dan c4 | Pelengkap metrik yang belum terekam saat run aslinya |
| `smoke_rgb.json` | Keluaran uji asap `stratified_eval.py` | Tidak dirujuk dokumen mana pun; disimpan agar skripnya tetap punya jejak |

Peta skrip penghasil tiap berkas ada di [`../PETA-SKRIP.md`](../PETA-SKRIP.md).
