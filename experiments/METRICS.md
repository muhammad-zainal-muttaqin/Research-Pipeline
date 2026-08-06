# Metrik final yang boleh dikutip

Halaman ini hanya memuat metrik performa final. Saat ini, satu-satunya hasil
yang memenuhi status tersebut adalah perbandingan empat kelas E-021 pada
SawitMVC. Angka E-022 tidak ada di halaman ini karena belum mendukung klaim
peningkatan deteksi; lihat [audit E-022](AUDIT-E022.md) dan
[arsip seed-42](archive/E022-seed42-awal.md).

## E-021: perbandingan final satu protokol

Keempat model dievaluasi lewat pipeline `pycocotools` yang identik: prediksi
dengan ambang rendah, ground truth yang sama, lalu `COCOeval`. Konfigurasi
dipilih pada val; angka test hanya dilaporkan. Split per pohon adalah
716/96/141, setara 3.000/404/588 citra train/val/test dengan irisan nol.

| Model | Parameter | Resolusi | Val mAP50 | Val mAP50-95 | Test mAP50 | Test mAP50-95 |
|---|---:|---:|---:|---:|---:|---:|
| YOLO26m | 21,9 jt | 640 | 0,5195 | 0,2411 | 0,5165 | 0,2452 |
| YOLO26l | 26,3 jt | 1280 | 0,5270 | 0,2526 | 0,5300 | 0,2568 |
| RT-DETR-L | 33,0 jt | 1280 | 0,5459 | 0,2555 | 0,5784 | 0,2707 |
| **RF-DETR-L** | **35,7 jt** | **1280** | **0,5695** | **0,2604** | **0,6038** | **0,2770** |

Klaim yang dapat dikutip: **RF-DETR-L adalah detektor empat kelas terbaik pada
E-021, dengan test mAP50 0,6038 dan mAP50-95 0,2770.** Baseline YOLO26l yang
sekelas parameter tetap berada di bawah kedua model DETR dalam empat metrik
utama.

## Sumber dan reproduksi

- JSON kanonik: [`evidence/experiments/results/E-021/perkelas_pycoco.json`](../../evidence/experiments/results/E-021/perkelas_pycoco.json).
- Skrip evaluator: [`reproduce/experiments/eval/eval_all_pycoco.py`](../../reproduce/experiments/eval/eval_all_pycoco.py).
- Metrik lengkap per kelas, AP, AR, precision, recall, F1, bootstrap, serta
  efisiensi: [`evidence/experiments/results/E-021/`](../../evidence/experiments/results/E-021/).
- Catatan konfigurasi dan jebakan run: [`CATATAN-TEKNIS-E021.md`](../../reproduce/experiments/CATATAN-TEKNIS-E021.md).
- Perintah lengkap: [`REPRODUCE.md`](../../reproduce/experiments/REPRODUCE.md).

## Batas penggunaan

- Hasil ini berlaku untuk SawitMVC dan split E-021, bukan untuk SawitMVC-Depth.
- Hasil E-022 hanya boleh dibaca bersama [auditnya](AUDIT-E022.md); jangan
  menggunakannya sebagai bukti bahwa depth sensor meningkatkan mAP.
