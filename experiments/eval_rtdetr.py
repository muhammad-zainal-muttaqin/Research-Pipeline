"""Evaluasi akhir RT-DETR pada bobot terbaik — val DAN test, per-kelas.

Dijalankan setelah pelatihan selesai. Memberi angka bersih untuk tabel SR-013,
bukan mengandalkan ekor log yang bisa terpotong. Test dilaporkan terpisah;
konfigurasi tidak dipilih dari test.
"""
import json
from pathlib import Path
from ultralytics import RTDETR

W = "runs/rtdetr_l_e60_i1280/weights/best.pt"
NAMES = ["B1", "B2", "B3", "B4"]
BASE = {"B1": 0.7354, "B2": 0.4076, "B3": 0.5561, "B4": 0.3881}  # baseline yolo26m 4-kelas

out = {}
m = RTDETR(W)
for split in ["val", "test"]:
    r = m.val(data="data_rgb.yaml", split=split, imgsz=1280, batch=2,
              plots=False, verbose=False)
    per = {NAMES[i]: round(float(r.box.ap50[i]), 4) for i in range(4)}
    out[split] = {
        "mAP50": round(float(r.box.map50), 4),
        "mAP50-95": round(float(r.box.map), 4),
        "precision": round(float(r.box.mp), 4),
        "recall": round(float(r.box.mr), 4),
        "per_kelas_AP50": per,
    }
    print(f"\n=== {split.upper()} ===")
    print(f"mAP50={out[split]['mAP50']}  mAP50-95={out[split]['mAP50-95']}  "
          f"P={out[split]['precision']}  R={out[split]['recall']}")
    print(f"{'kelas':6} {'RT-DETR':>8} {'baseline':>9} {'selisih':>8}")
    for k in NAMES:
        d = per[k] - BASE[k]
        print(f"{k:6} {per[k]:8.4f} {BASE[k]:9.4f} {d:+8.4f}")

Path("results").mkdir(exist_ok=True)
json.dump(out, open("results/rtdetr_eval.json", "w"), indent=1)
print("\n-> results/rtdetr_eval.json")
