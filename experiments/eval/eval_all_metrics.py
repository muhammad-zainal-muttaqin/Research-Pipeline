"""Dump metrik LENGKAP 1-protokol untuk semua model (val+test).

Superset dari eval_all_pycoco.py. Untuk tiap model x split:
- 12 statistik COCO (AP@[.5:.95], AP50, AP75, AP S/M/L, AR@1/10/100, AR S/M/L)
- per-kelas: AP50, AP50-95, AR@[.5:.95]
- precision, recall, F1 @IoU0.5 pada ambang best-F1:
  * per-kelas (ambang per-kelas sendiri)
  * MACRO (rata-rata per-kelas)
  * MICRO (gabung semua kelas, satu ambang global)

Prediksi dilakukan sekali per model x split lalu dipakai bersama untuk COCOeval
dan P/R/F1. Hasil -> results/metrics_full.json. Reuse GT/predict dari
eval_all_pycoco.py agar identik dengan tabel 1-protokol.
"""
import json
from pathlib import Path

import numpy as np
from pycocotools.cocoeval import COCOeval

from eval_all_pycoco import (NAMES, SPLIT_DIR, MODELS, build_gt, load,
                             predict_ultra, predict_rfdetr)

OUT = Path("results/metrics_full.json")


def iou_xywh(a, boxes):
    ax, ay, aw, ah = a
    ax2, ay2 = ax + aw, ay + ah
    bx, by, bw, bh = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    bx2, by2 = bx + bw, by + bh
    ix1 = np.maximum(ax, bx); iy1 = np.maximum(ay, by)
    ix2 = np.minimum(ax2, bx2); iy2 = np.minimum(ay2, by2)
    iw = np.clip(ix2 - ix1, 0, None); ih = np.clip(iy2 - iy1, 0, None)
    inter = iw * ih
    union = aw * ah + bw * bh - inter
    return np.where(union > 0, inter / union, 0.0)


def match_class(preds, gts, iou_thr=0.5):
    """preds: list dict {score,bbox}; gts: Nx4 xywh. -> (scores, tp) urut skor desc, nGT."""
    if not preds:
        return np.array([]), np.array([]), len(gts)
    preds = sorted(preds, key=lambda p: -p["score"])
    scores = np.array([p["score"] for p in preds])
    gt = np.array([g for g in gts], dtype=float) if len(gts) else np.zeros((0, 4))
    used = np.zeros(len(gt), dtype=bool)
    tp = np.zeros(len(preds))
    for i, p in enumerate(preds):
        if len(gt) == 0:
            continue
        ious = iou_xywh(p["bbox"], gt)
        ious[used] = -1
        j = int(np.argmax(ious)) if len(ious) else -1
        if j >= 0 and ious[j] >= iou_thr:
            tp[i] = 1; used[j] = True
    return scores, tp, len(gt)


def prf_at_bestf1(scores, tp, ngt):
    """PR curve -> titik best-F1. return (P,R,F1,thr)."""
    if len(scores) == 0 or ngt == 0:
        return 0.0, 0.0, 0.0, 0.0
    order = np.argsort(-scores)
    tp = tp[order]; sc = scores[order]
    ctp = np.cumsum(tp); cfp = np.cumsum(1 - tp)
    prec = ctp / np.maximum(ctp + cfp, 1e-9)
    rec = ctp / ngt
    f1 = 2 * prec * rec / np.maximum(prec + rec, 1e-9)
    k = int(np.argmax(f1))
    return float(prec[k]), float(rec[k]), float(f1[k]), float(sc[k])


def per_class_coco(ev):
    p = ev.eval["precision"]  # [T,R,K,A,M]
    r = ev.eval["recall"]     # [T,K,A,M]
    out = {}
    for k, n in enumerate(NAMES):
        s95 = p[:, :, k, 0, 2]; s50 = p[0, :, k, 0, 2]
        arr = r[:, k, 0, 2]
        out[n] = {
            "AP50": round(float(s50[s50 > -1].mean()) if (s50 > -1).any() else 0.0, 4),
            "AP50_95": round(float(s95[s95 > -1].mean()) if (s95 > -1).any() else 0.0, 4),
            "AR": round(float(arr[arr > -1].mean()) if (arr > -1).any() else 0.0, 4),
        }
    return out


def full_metrics(gt, dt_list):
    ev = COCOeval(gt, gt.loadRes(dt_list), "bbox")
    ev.evaluate(); ev.accumulate(); ev.summarize()
    s = [round(float(x), 4) for x in ev.stats]
    coco = {"AP50_95": s[0], "AP50": s[1], "AP75": s[2], "AP_small": s[3],
            "AP_medium": s[4], "AP_large": s[5], "AR1": s[6], "AR10": s[7],
            "AR100": s[8], "AR_small": s[9], "AR_medium": s[10], "AR_large": s[11]}
    perkelas = per_class_coco(ev)

    # P/R/F1 @IoU0.5 best-F1 — per-kelas + macro + micro (matching per-gambar)
    # pre-index prediksi per (image_id, category) sekali (hindari O(N) filter berulang)
    dt_idx = {}
    for d in dt_list:
        dt_idx.setdefault((d["image_id"], d["category_id"]), []).append(d)
    prf = {}
    micro_scores, micro_tp, micro_ngt = [], [], 0
    P, R, F = [], [], []
    for k, n in enumerate(NAMES):
        cat = k + 1
        sc, tp, ng = match_per_image(dt_idx, gt, cat)
        p_, r_, f_, thr = prf_at_bestf1(sc, tp, ng)
        prf[n] = {"P": round(p_, 4), "R": round(r_, 4), "F1": round(f_, 4), "thr": round(thr, 4)}
        P.append(p_); R.append(r_); F.append(f_)
        micro_scores.append(sc); micro_tp.append(tp); micro_ngt += ng
    prf["macro"] = {"P": round(float(np.mean(P)), 4), "R": round(float(np.mean(R)), 4),
                    "F1": round(float(np.mean(F)), 4)}
    ms = np.concatenate(micro_scores) if micro_scores else np.array([])
    mt = np.concatenate(micro_tp) if micro_tp else np.array([])
    mp, mr, mf, mthr = prf_at_bestf1(ms, mt, micro_ngt)
    prf["micro"] = {"P": round(mp, 4), "R": round(mr, 4), "F1": round(mf, 4), "thr": round(mthr, 4)}
    return {"coco": coco, "per_kelas": perkelas, "prf": prf}


def match_per_image(dt_idx, gt, cat):
    """Match prediksi kelas `cat` ke GT per gambar (IoU0.5). dt_idx: {(img,cat):[det]}."""
    imgs = {im["id"] for im in gt.dataset["images"]}
    gt_by_img = {}
    for a in gt.dataset["annotations"]:
        if a["category_id"] == cat:
            gt_by_img.setdefault(a["image_id"], []).append(a["bbox"])
    all_sc, all_tp, ngt = [], [], 0
    for img in imgs:
        preds = dt_idx.get((img, cat), [])
        gts = gt_by_img.get(img, [])
        ngt += len(gts)
        sc, tp, _ = match_class(preds, gts)
        if len(sc):
            all_sc.append(sc); all_tp.append(tp)
    sc = np.concatenate(all_sc) if all_sc else np.array([])
    tp = np.concatenate(all_tp) if all_tp else np.array([])
    return sc, tp, ngt


def main():
    gts = {s: build_gt(sd) for s, sd in SPLIT_DIR.items()}
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for key, kind, weights, imgsz, params in MODELS:
        if not Path(weights).exists():
            print(f"SKIP {key}: bobot tak ada"); continue
        print(f"\n===== {key} ({params}jt, {kind}) =====")
        model = load(kind, weights, imgsz)
        entry = {"params_juta": params, "imgsz": imgsz, "evaluator": "pycocotools+IoU0.5-PRF"}
        for split, (gt, paths) in gts.items():
            dt = predict_rfdetr(model, paths) if kind == "rfdetr" else predict_ultra(model, paths, imgsz)
            entry[split] = full_metrics(gt, dt)
            c = entry[split]["coco"]; pr = entry[split]["prf"]
            print(f"  {split}: AP50={c['AP50']} AP50-95={c['AP50_95']} AP75={c['AP75']} "
                  f"AR100={c['AR100']} | micro P/R/F1={pr['micro']['P']}/{pr['micro']['R']}/{pr['micro']['F1']}")
        data[key] = entry
        OUT.parent.mkdir(exist_ok=True)
        OUT.write_text(json.dumps(data, indent=2))
        del model
    print(f"\n-> {OUT}")


if __name__ == "__main__":
    main()
