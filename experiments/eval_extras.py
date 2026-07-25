"""Analisis tambahan E-021 (#1 confusion, #2 bootstrap CI, #4 kurva PR/F1).

Semua dari bobot & prediksi yang ada (tanpa training ulang). Split TEST (588,
split yang dilaporkan). Prediksi 1x per model lalu dipakai bersama.

- #1 Confusion matrix 5x5 (B1-B4 + latar) @IoU0.5, conf>=0.25, class-agnostic
  matching -> results/confusion.json (+ figures/confusion_<model>.png)
- #2 Bootstrap 95% CI mAP50 (2000 resample gambar) per model + selisih
  berpasangan RF-DETR - RT-DETR (uji signifikansi) -> results/bootstrap_ci.json
- #4 Kurva PR & F1-confidence (micro) semua model -> results/pr_curves.json
  + figures/pr_micro_test.png, figures/f1_conf_test.png

mAP50 di sini dihitung 101-titik COCO dari matching IoU0.5; divalidasi terhadap
pycocotools (harus cocok ~<0.005).
"""
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from eval_all_pycoco import NAMES, build_gt, load, predict_ultra, predict_rfdetr, MODELS

SPLIT = "test"
SDIR = "test"
FIG = Path("figures"); FIG.mkdir(exist_ok=True)
B = 2000
RNG = np.random.default_rng(42)
ORDER = ["YOLO26m", "YOLO26l", "RT-DETR-L", "RF-DETR-L"]


def iou_xywh(a, boxes):
    ax, ay, aw, ah = a; ax2, ay2 = ax + aw, ay + ah
    bx, by, bw, bh = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    ix1 = np.maximum(ax, bx); iy1 = np.maximum(ay, by)
    ix2 = np.minimum(ax2, bx + bw); iy2 = np.minimum(ay2, by + bh)
    iw = np.clip(ix2 - ix1, 0, None); ih = np.clip(iy2 - iy1, 0, None)
    inter = iw * ih; union = aw * ah + bw * bh - inter
    return np.where(union > 0, inter / union, 0.0)


def ap50(scores, tp, ngt):
    """AP COCO 101-titik @IoU0.5 dari (score,tp)."""
    if ngt == 0:
        return float("nan")
    if len(scores) == 0:
        return 0.0
    o = np.argsort(-scores); tp = tp[o]
    ctp = np.cumsum(tp); cfp = np.cumsum(1 - tp)
    rec = ctp / ngt; prec = ctp / np.maximum(ctp + cfp, 1e-9)
    prec = np.maximum.accumulate(prec[::-1])[::-1]  # monotonic (vektor, bukan loop)
    rthr = np.linspace(0, 1, 101)
    idx = np.searchsorted(rec, rthr, side="left")
    p = np.where(idx < len(prec), prec[np.clip(idx, 0, len(prec) - 1)], 0.0)
    p[idx >= len(prec)] = 0.0
    return float(p.mean())


def build_per_image(gt, dt_list):
    """Per (img,cls): (scores,tp) IoU0.5 + nGT. Untuk AP/PR/bootstrap."""
    imgs = [im["id"] for im in gt.dataset["images"]]
    gt_ic = {}
    for a in gt.dataset["annotations"]:
        gt_ic.setdefault((a["image_id"], a["category_id"]), []).append(a["bbox"])
    dt_ic = {}
    for d in dt_list:
        dt_ic.setdefault((d["image_id"], d["category_id"]), []).append(d)
    per = {}  # (img,cls) -> (scores,tp)
    ngt = {}  # (img,cls) -> n
    for img in imgs:
        for k in range(1, 5):
            gts = gt_ic.get((img, k), [])
            ngt[(img, k)] = len(gts)
            preds = sorted(dt_ic.get((img, k), []), key=lambda p: -p["score"])
            if not preds:
                per[(img, k)] = (np.array([]), np.array([])); continue
            gtb = np.array(gts, float) if gts else np.zeros((0, 4))
            used = np.zeros(len(gtb), bool); tp = np.zeros(len(preds))
            sc = np.array([p["score"] for p in preds])
            for i, p in enumerate(preds):
                if len(gtb) == 0:
                    continue
                io = iou_xywh(p["bbox"], gtb); io[used] = -1
                j = int(np.argmax(io)) if len(io) else -1
                if j >= 0 and io[j] >= 0.5:
                    tp[i] = 1; used[j] = True
            per[(img, k)] = (sc, tp)
    return imgs, per, ngt


def pr_micro(imgs, per, ngt):
    """PR + F1-conf micro (gabung semua kelas)."""
    sc = np.concatenate([per[(i, k)][0] for i in imgs for k in range(1, 5) if len(per[(i, k)][0])] or [np.array([])])
    tp = np.concatenate([per[(i, k)][1] for i in imgs for k in range(1, 5) if len(per[(i, k)][1])] or [np.array([])])
    N = sum(ngt[(i, k)] for i in imgs for k in range(1, 5))
    o = np.argsort(-sc); sc = sc[o]; tp = tp[o]
    ctp = np.cumsum(tp); cfp = np.cumsum(1 - tp)
    rec = ctp / max(N, 1); prec = ctp / np.maximum(ctp + cfp, 1e-9)
    f1 = 2 * prec * rec / np.maximum(prec + rec, 1e-9)
    return rec, prec, sc, f1


def confusion(gt, dt_list, conf=0.25):
    """5x5 class-agnostic @IoU0.5. cm[t][p]: t=GT kelas(0-3) atau 4=latar(FP),
    p=pred kelas(0-3) atau 4=latar(miss)."""
    gt_i = {}
    for a in gt.dataset["annotations"]:
        gt_i.setdefault(a["image_id"], []).append((a["category_id"] - 1, a["bbox"]))
    dt_i = {}
    for d in dt_list:
        if d["score"] >= conf:
            dt_i.setdefault(d["image_id"], []).append((d["category_id"] - 1, d["score"], d["bbox"]))
    cm = np.zeros((5, 5), int)
    for im in {x["id"] for x in gt.dataset["images"]}:
        gts = gt_i.get(im, []); preds = sorted(dt_i.get(im, []), key=lambda x: -x[1])
        gtb = np.array([b for _, b in gts], float) if gts else np.zeros((0, 4))
        used = np.zeros(len(gtb), bool)
        for pc, _, pb in preds:
            if len(gtb) == 0:
                cm[4][pc] += 1; continue
            io = iou_xywh(pb, gtb); io[used] = -1
            j = int(np.argmax(io)) if len(io) else -1
            if j >= 0 and io[j] >= 0.5:
                cm[gts[j][0]][pc] += 1; used[j] = True
            else:
                cm[4][pc] += 1  # FP (predicted, no GT)
        for j, u in enumerate(used):
            if not u:
                cm[gts[j][0]][4] += 1  # GT missed
    return cm


def plot_confusion(cm, name):
    lab = NAMES + ["latar"]
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    im = ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(5)); ax.set_yticks(range(5))
    ax.set_xticklabels(lab); ax.set_yticklabels(lab)
    ax.set_xlabel("Prediksi"); ax.set_ylabel("Ground truth")
    ax.set_title(f"Confusion @IoU0.5 conf0.25 — {name} (TEST)")
    for i in range(5):
        for j in range(5):
            ax.text(j, i, cm[i, j], ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black", fontsize=9)
    fig.tight_layout(); fig.savefig(FIG / f"confusion_{name}.png", dpi=130); plt.close(fig)


def main():
    gt, paths = build_gt(SDIR)
    dets = {}
    confmat = {}
    prdata = {}
    per_all = {}
    for key, kind, weights, imgsz, params in MODELS:
        if not Path(weights).exists():
            print(f"SKIP {key}"); continue
        cache = Path(f"results/_cache_dets_test_{key}.json")
        if cache.exists():
            print(f"\n== {key}: pakai cache prediksi ==")
            dt = json.loads(cache.read_text())
        else:
            print(f"\n== {key}: predict TEST ==")
            model = load(kind, weights, imgsz)
            dt = predict_rfdetr(model, paths) if kind == "rfdetr" else predict_ultra(model, paths, imgsz)
            cache.write_text(json.dumps(dt))
            del model
        dets[key] = dt
        imgs, per, ngt = build_per_image(gt, dt)
        per_all[key] = (imgs, per, ngt)
        # #1 confusion
        cm = confusion(gt, dt)
        confmat[key] = cm.tolist(); plot_confusion(cm, key)
        # validasi mAP50
        m50 = np.nanmean([ap50(np.concatenate([per[(i, k)][0] for i in imgs if len(per[(i, k)][0])] or [np.array([])]),
                               np.concatenate([per[(i, k)][1] for i in imgs if len(per[(i, k)][1])] or [np.array([])]),
                               sum(ngt[(i, k)] for i in imgs)) for k in range(1, 5)])
        print(f"  mAP50(check)={m50:.4f}  (bandingkan pycocotools)")
        # #4 PR/F1 micro
        rec, prec, sc, f1 = pr_micro(imgs, per, ngt)
        bi = int(np.argmax(f1))
        prdata[key] = {"recall": rec[::max(1, len(rec)//300)].tolist(),
                       "precision": prec[::max(1, len(prec)//300)].tolist(),
                       "conf": sc[::max(1, len(sc)//300)].tolist(),
                       "f1": f1[::max(1, len(f1)//300)].tolist(),
                       "best_f1": round(float(f1[bi]), 4), "best_conf": round(float(sc[bi]), 4)}

    # simpan confusion + pr
    json.dump({"split": SPLIT, "iou": 0.5, "conf": 0.25, "labels": NAMES + ["latar"],
               "matrix_rows_gt_cols_pred": confmat}, open("results/confusion.json", "w"), indent=2)
    json.dump({"split": SPLIT, "curves": prdata}, open("results/pr_curves.json", "w"), indent=2)

    # #4 figur gabungan
    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    for m in ORDER:
        if m in prdata:
            ax.plot(prdata[m]["recall"], prdata[m]["precision"], label=m, lw=1.8)
    ax.set_xlabel("Recall"); ax.set_ylabel("Precision"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title("Kurva PR micro (TEST) @IoU0.5"); ax.legend(); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(FIG / "pr_micro_test.png", dpi=130); plt.close(fig)

    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    for m in ORDER:
        if m in prdata:
            ax.plot(prdata[m]["conf"], prdata[m]["f1"], label=m, lw=1.8)
    ax.set_xlabel("Confidence"); ax.set_ylabel("F1"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title("F1 vs confidence micro (TEST)"); ax.legend(); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(FIG / "f1_conf_test.png", dpi=130); plt.close(fig)

    # #2 bootstrap mAP50 CI (test) + paired diff RF - RT
    print("\n== bootstrap mAP50 (2000x) ==")
    imgs = per_all[list(per_all)[0]][0]  # daftar image id (sama untuk semua model)
    n = len(imgs)
    boot = {m: np.zeros(B) for m in per_all}
    idxs = RNG.integers(0, n, size=(B, n))
    for b in range(B):
        samp = [imgs[i] for i in idxs[b]]
        for m, (_, per, ngt) in per_all.items():
            aps = []
            for k in range(1, 5):
                scs = [per[(i, k)][0] for i in samp if len(per[(i, k)][0])]
                tps = [per[(i, k)][1] for i in samp if len(per[(i, k)][1])]
                sc = np.concatenate(scs) if scs else np.array([])
                tp = np.concatenate(tps) if tps else np.array([])
                ng = sum(ngt[(i, k)] for i in samp)
                aps.append(ap50(sc, tp, ng))
            boot[m][b] = np.nanmean(aps)
    ci = {}
    for m, arr in boot.items():
        ci[m] = {"mAP50_mean": round(float(arr.mean()), 4),
                 "ci95_low": round(float(np.percentile(arr, 2.5)), 4),
                 "ci95_high": round(float(np.percentile(arr, 97.5)), 4)}
        print(f"  {m}: {ci[m]['mAP50_mean']} [{ci[m]['ci95_low']}, {ci[m]['ci95_high']}]")
    if "RF-DETR-L" in boot and "RT-DETR-L" in boot:
        diff = boot["RF-DETR-L"] - boot["RT-DETR-L"]
        p_win = float((diff > 0).mean())
        ci["RF_minus_RT"] = {"mean": round(float(diff.mean()), 4),
                             "ci95_low": round(float(np.percentile(diff, 2.5)), 4),
                             "ci95_high": round(float(np.percentile(diff, 97.5)), 4),
                             "P(RF>RT)": round(p_win, 4)}
        print(f"  RF-DETR - RT-DETR: {ci['RF_minus_RT']['mean']} "
              f"[{ci['RF_minus_RT']['ci95_low']}, {ci['RF_minus_RT']['ci95_high']}] P(RF>RT)={p_win:.3f}")
    json.dump({"split": SPLIT, "metric": "mAP50", "B": B, "seed": 42, "ci": ci},
              open("results/bootstrap_ci.json", "w"), indent=2)
    print("\n-> results/confusion.json, pr_curves.json, bootstrap_ci.json + figures/")


if __name__ == "__main__":
    main()
