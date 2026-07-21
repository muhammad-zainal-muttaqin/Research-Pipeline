"""Berapa banyak yang bisa direbut dengan menggabungkan sisi?

Deployment menghitung per POHON, bukan per foto: aplikasi melihat 4-8 sisi
pohon yang sama, dan satu tandan fisik muncul di 2-6 sisi (SR-001: 7.328 dari
9.823 tandan). Kematangan tandan itu satu, jadi kesalahan per-sisi yang bersifat
ordinal (SR-009: 99% meleset satu langkah) sebagian bisa saling meniadakan.

Yang diukur di sini adalah PLAFON: penautan antar-sisi diambil dari kebenaran
dasar JSON, bukan dari algoritma penaut (SR-006 memalsukan penautan geometris).
Kalau plafonnya kecil, tidak ada gunanya membangun penaut sama sekali. Kalau
besar, itu justru yang layak dikerjakan berikutnya.
"""
import argparse, glob, json
from collections import defaultdict
from pathlib import Path

import cv2, numpy as np, torch, torch.nn as nn
from torchvision import transforms as T, models

NAMES = ["B1", "B2", "B3", "B4"]
PAD = 0.25


def bunch_index(split):
    """(nama_citra, box_index) -> (tree_id, bunch_id, kelas)"""
    idx = {}
    for f in glob.glob("/workspace/SawitMVC/data/json/*.json"):
        d = json.load(open(f))
        if d.get("split") != split:
            continue
        b2c, b2id = {}, {}
        for b in d.get("bunches", []):
            bid = b.get("bunch_id", b.get("id"))
            for ap in b.get("appearances", b.get("views", [])):
                key = (ap.get("image") or ap.get("filename") or
                       ap.get("side") or "", ap.get("box_index"))
                b2id[key] = bid
        for side, im in d["images"].items():
            fn = im["filename"]
            for an in im["annotations"]:
                k = (fn, an["box_index"])
                bid = (b2id.get((fn, an["box_index"])) or
                       b2id.get((side, an["box_index"])))
                idx[k] = {"tree": d["tree_id"], "bunch": bid,
                          "kelas": an["class_id"], "bbox": an["bbox_pixel"]}
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cls", default="runs/maturity/best.pt")
    ap.add_argument("--split", default="val")
    ap.add_argument("--size", type=int, default=224)
    ap.add_argument("--crops", default="crops")
    a = ap.parse_args()

    idx = bunch_index(a.split)
    linked = sum(1 for v in idx.values() if v["bunch"] is not None)
    print(f"anotasi {a.split}: {len(idx)} kotak, {linked} tertaut ke bunch_id")
    if linked == 0:
        print("PERINGATAN: bunch_id tidak terbaca dari JSON — periksa skema")
        return

    dev = "cuda"
    m = models.convnext_tiny(weights=None)
    m.classifier[2] = nn.Linear(768, 4)
    m.load_state_dict(torch.load(a.cls, map_location="cpu"))
    m.to(dev).eval()
    tf = T.Compose([T.ToTensor(),
                    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # klasifikasikan setiap potongan kebenaran-dasar (kotak sempurna: yang
    # diukur murni penilaian kematangan, bukan deteksi)
    per_bunch = defaultdict(list)
    per_view = []
    files = {}
    for split_dir in [a.crops]:
        for nm in NAMES:
            for p in Path(f"{split_dir}/{a.split}/{nm}").glob("*.jpg"):
                stem = p.stem
                i = stem.rfind("_")
                files[(stem[:i] + ".jpg", int(stem[i + 1:]))] = p
    keys = [k for k in files if k in idx and idx[k]["bunch"] is not None]
    print(f"potongan cocok: {len(keys)}")

    B = 128
    for s in range(0, len(keys), B):
        chunk = keys[s:s + B]
        ims = []
        for k in chunk:
            im = cv2.imread(str(files[k]))
            im = cv2.resize(im, (a.size, a.size), interpolation=cv2.INTER_AREA)
            ims.append(tf(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)))
        with torch.no_grad(), torch.autocast("cuda", torch.bfloat16):
            pr = m(torch.stack(ims).to(dev)).float().softmax(1).cpu().numpy()
        for k, p in zip(chunk, pr):
            g = idx[k]
            per_view.append((int(np.argmax(p)), g["kelas"]))
            per_bunch[(g["tree"], g["bunch"])].append((p, g["kelas"]))

    pv = np.array(per_view)
    acc_view = float((pv[:, 0] == pv[:, 1]).mean())
    pm1_view = float((np.abs(pv[:, 0] - pv[:, 1]) <= 1).mean())

    ok = tot = ok1 = 0
    by_n = defaultdict(lambda: [0, 0])
    for (tree, bid), lst in per_bunch.items():
        truth = lst[0][1]
        avg = np.mean([p for p, _ in lst], axis=0)
        pred = int(np.argmax(avg))
        tot += 1; ok += pred == truth; ok1 += abs(pred - truth) <= 1
        n = min(len(lst), 4)
        by_n[n][0] += pred == truth; by_n[n][1] += 1

    res = {"split": a.split,
           "per_sisi": {"n": len(pv), "akurasi": round(acc_view, 4),
                        "akurasi_pm1": round(pm1_view, 4)},
           "per_tandan_gabungan": {"n": tot, "akurasi": round(ok / tot, 4),
                                   "akurasi_pm1": round(ok1 / tot, 4)},
           "menurut_jumlah_sisi": {str(k): {"n": v[1], "akurasi": round(v[0] / v[1], 4)}
                                   for k, v in sorted(by_n.items())}}
    print(json.dumps(res, indent=1))
    json.dump(res, open(f"results/multiview_{a.split}.json", "w"), indent=1)


if __name__ == "__main__":
    main()
