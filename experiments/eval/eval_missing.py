"""Generate per-kelas B1-B4 (val + test) untuk run yang belum punya JSON:
c4_e50 (3-kanal) dan rgbd (4-kanal). Inferensi pada best.pt yang sudah ada —
BUKAN latih ulang. Dijalankan sebelum workspace di-terminate agar tak ada
metrik yang hilang.
"""
import json, sys
from ultralytics import YOLO
NAMES = ["B1", "B2", "B3", "B4"]
out = {}

def run(tag, weights, data, imgsz, patch=None):
    if patch:
        import train_fusion
        train_fusion.patch_loader_for_4ch("rgbd")
    m = YOLO(weights)
    r = {}
    for sp in ["val", "test"]:
        v = m.val(data=data, split=sp, imgsz=imgsz, batch=4, plots=False, verbose=False)
        r[sp] = {"mAP50": round(float(v.box.map50), 4),
                 "mAP50-95": round(float(v.box.map), 4),
                 "precision": round(float(v.box.mp), 4),
                 "recall": round(float(v.box.mr), 4),
                 "per_kelas_AP50": {NAMES[i]: round(float(v.box.ap50[i]), 4) for i in range(4)}}
        print(f"[{tag}/{sp}] mAP50={r[sp]['mAP50']} mAP50-95={r[sp]['mAP50-95']} "
              f"per-kelas={r[sp]['per_kelas_AP50']}")
    out[tag] = r

# E-019: c4_e50 (3-kanal, augmentasi aman-warna, 1280)
run("c4_e50_i1280_warna", "runs/c4_e50_i1280_warna/weights/best.pt",
    "data_rgb.yaml", 1280)

# I-4: rgbd 4-kanal (early fusion, pseudo-depth DA3)
try:
    run("rgbd_e60_i640_s42", "runs/rgbd_e60_i640_s42/weights/best.pt",
        "data_rgbd4.yaml", 640, patch="rgbd")
except Exception as e:
    print(f"[rgbd] GAGAL val 4-kanal: {e}")
    out["rgbd_e60_i640_s42"] = {"error": str(e),
        "catatan": "aggregate per-epoch tetap ada di runs/rgbd_e60_i640_s42/results.csv"}

json.dump(out, open("results/eval_missing.json", "w"), indent=1)
print("-> results/eval_missing.json")
