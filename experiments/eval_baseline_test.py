"""Angka TEST baseline yolo26m untuk perbandingan adil test-vs-test dengan RT-DETR."""
import json
from ultralytics import YOLO
NAMES=["B1","B2","B3","B4"]
m=YOLO("runs/rgb_e60_i640_s42/weights/best.pt")
out={}
for sp in ["val","test"]:
    r=m.val(data="data_rgb.yaml",split=sp,imgsz=640,batch=8,plots=False,verbose=False)
    out[sp]={"mAP50":round(float(r.box.map50),4),"mAP50-95":round(float(r.box.map),4),
             "per_kelas":{NAMES[i]:round(float(r.box.ap50[i]),4) for i in range(4)}}
    print(sp.upper(),json.dumps(out[sp]))
json.dump(out,open("results/baseline_test.json","w"),indent=1)
