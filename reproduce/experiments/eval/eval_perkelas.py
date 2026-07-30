"""Kumpulkan per-kelas AP50 DAN AP50-95 (val+test) untuk model ultralytics.

Melengkapi tabel perbandingan adil: rtdetr_eval.json lama hanya menyimpan AP50
per-kelas; di sini diambil keduanya agar konsisten dengan model lain. Hasil
diakumulasi ke results/perkelas_fair.json supaya tak perlu run ulang.
"""
import json
from pathlib import Path

from ultralytics import YOLO, RTDETR

NAMES = ["B1", "B2", "B3", "B4"]
OUT = Path("results/perkelas_fair.json")

# (kunci, kelas ultralytics, bobot, imgsz, param_juta, resolusi_label)
MODELS = [
    ("YOLO26m", YOLO, "runs/rgb_e60_i640_s42/weights/best.pt", 640, 21.9),
    ("RT-DETR-L", RTDETR, "runs/rtdetr_l_e60_i1280/weights/best.pt", 1280, 33.0),
]


def eval_model(cls, weights, imgsz):
    m = cls(weights)
    out = {}
    for split in ["val", "test"]:
        r = m.val(data="data_rgb.yaml", split=split, imgsz=imgsz, batch=2,
                  plots=False, verbose=False)
        out[split] = {
            "mAP50": round(float(r.box.map50), 4),
            "mAP50_95": round(float(r.box.map), 4),
            "per_kelas_AP50": {NAMES[i]: round(float(r.box.ap50[i]), 4) for i in range(4)},
            "per_kelas_AP50_95": {NAMES[i]: round(float(r.box.ap[i]), 4) for i in range(4)},
        }
    return out


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for key, cls, weights, imgsz, params in MODELS:
        print(f"== {key} ({params} jt, imgsz {imgsz}) ==")
        res = eval_model(cls, weights, imgsz)
        res["params_juta"] = params
        res["imgsz"] = imgsz
        data[key] = res
        for split in ["val", "test"]:
            s = res[split]
            print(f"  {split}: mAP50={s['mAP50']} mAP50-95={s['mAP50_95']}")
            for n in NAMES:
                print(f"    {n}: AP50={s['per_kelas_AP50'][n]:.4f}  AP50-95={s['per_kelas_AP50_95'][n]:.4f}")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2))
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
