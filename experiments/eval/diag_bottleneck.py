"""Diagnosis penentu: berapa banyak kerugian mAP berasal dari KLASIFIKASI,
bukan dari deteksi? Bandingkan mAP 4-kelas vs mAP kelas-agnostik (single_cls)
pada bobot yang sama. Kalau agnostik jauh lebih tinggi, maka detektornya sudah
menemukan tandan dan yang gagal adalah penilaian kematangan."""
import json, sys
from ultralytics import YOLO

W = "runs/rgb_e60_i640_s42/weights/best.pt"
out = {}
for tag, kw in [("4kelas", {}), ("agnostik", {"single_cls": True})]:
    m = YOLO(W).val(data="data_rgb.yaml", split="val", imgsz=640, batch=8,
                    device=0, verbose=False, plots=False, **kw)
    out[tag] = {"mAP50": round(float(m.box.map50), 4),
                "mAP50-95": round(float(m.box.map), 4),
                "P": round(float(m.box.mp), 4), "R": round(float(m.box.mr), 4)}
    if not kw:
        out[tag]["per_kelas_AP50"] = {n: round(float(v), 4) for n, v in
                                      zip(["B1","B2","B3","B4"], m.box.ap50)}
print(json.dumps(out, indent=1))
json.dump(out, open("results/diag_bottleneck.json","w"), indent=1)
