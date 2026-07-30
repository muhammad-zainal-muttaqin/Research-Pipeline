#!/usr/bin/env python3
"""E-005 — DA3 multi-view pada 4/8 sisi foto asli SawitMVC.

Ini pertanyaan yang sebenarnya. E-004 membuktikan DA3 andal pada video orbit,
tetapi video punya baseline antar-frame kecil. Foto dataset diambil dari 4 posisi
berjarak ~90 derajat -- baseline lebar, tumpang tindih rendah, pada objek yang
menutupi dirinya sendiri. Keberhasilan pada video TIDAK menjamin apa pun di sini.

Yang diuji:
  (b) Apakah 4 pusat kamera tersusun melingkar dengan jarak sudut ~90 derajat?
      Ini dapat diperiksa objektif karena geometri pengambilan datanya diketahui:
      operator memutari pohon pada 4 posisi. Pohon 8-sisi memberi uji lebih ketat
      (~45 derajat) sekaligus pembanding baseline yang lebih rapat.
  (c) Apakah kedalaman memisahkan lapisan pada citra dataset (bukan video)?

Metrik utama: `angle_rmse_deg` -- simpangan RMS jarak sudut antar-sisi berurutan
terhadap 360/N derajat yang diharapkan. Kecil = geometri terekonstruksi benar.

Pemakaian:
  python da3_sides_test.py --trees 20
  python da3_sides_test.py --trees 20 --sides 8
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

IMAGES = Path("/workspace/SawitMVC/data/images")
JSON_DIR = Path("/workspace/SawitMVC/data/json")
OUT_DIR = Path("/workspace/experiments/results/e005")


def group_by_tree(images: Path) -> dict[str, list[Path]]:
    by = defaultdict(list)
    for p in sorted(images.glob("*.jpg")):
        m = re.match(r"^(.*)_(\d+)$", p.stem)
        if m:
            by[m.group(1)].append(p)
    for t in by:
        by[t].sort(key=lambda q: int(re.match(r"^.*_(\d+)$", q.stem).group(1)))
    return by


def camera_centers(ext: np.ndarray) -> np.ndarray:
    return np.stack([-E[:3, :3].T @ E[:3, 3] for E in ext])


def ring_metrics(C: np.ndarray) -> dict:
    """Seberapa dekat pusat kamera dengan cincin ber-spasi seragam?"""
    n = len(C)
    mu = C.mean(0)
    X = C - mu
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    proj = X @ Vt[:2].T
    A = np.c_[2 * proj, np.ones(n)]
    sol, *_ = np.linalg.lstsq(A, (proj ** 2).sum(1), rcond=None)
    cx, cy = sol[0], sol[1]
    r = float(np.sqrt(max(sol[2] + cx ** 2 + cy ** 2, 0)))
    d = np.linalg.norm(proj - [cx, cy], axis=1)

    ang = np.degrees(np.arctan2(proj[:, 1] - cy, proj[:, 0] - cx))
    order = np.argsort(ang)
    # jarak sudut antar-sisi berurutan (urut sesuai indeks sisi, bukan diurut)
    a = np.degrees(np.unwrap(np.radians(ang)))
    steps = np.diff(a)
    steps = (steps + 180) % 360 - 180          # ke [-180,180)
    expected = 360.0 / n
    # arah putar bisa searah atau berlawanan jarum jam
    err_pos = steps - expected
    err_neg = steps + expected
    err = err_pos if abs(err_pos).sum() <= abs(err_neg).sum() else err_neg

    return {
        "n": n,
        "radius": r,
        "circle_resid_mean_rel": float(abs(d - r).mean() / r) if r else None,
        "planarity_ratio": float(S[2] / S[0]) if S[0] else None,
        "steps_deg": steps.tolist(),
        "expected_step_deg": expected,
        "angle_rmse_deg": float(np.sqrt((err ** 2).mean())),
        "angle_maxerr_deg": float(abs(err).max()),
        "order_correct": bool(np.all(steps > 0) or np.all(steps < 0)),
        "sorted_order": order.tolist(),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trees", type=int, default=20)
    ap.add_argument("--sides", type=int, default=4, choices=[4, 8])
    ap.add_argument("--ckpt", default="depth-anything/da3-large")
    ap.add_argument("--process-res", type=int, default=504)
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--preview", type=int, default=2, help="jumlah pohon yang disimpan pratinjaunya")
    args = ap.parse_args()

    by_tree = group_by_tree(IMAGES)
    cand = [t for t, ps in by_tree.items() if len(ps) == args.sides]
    if not cand:
        print(f"[GAGAL] tidak ada pohon dengan {args.sides} sisi", file=sys.stderr)
        return 2
    random.Random(args.seed).shuffle(cand)
    trees = cand[: args.trees]
    print(f"pohon {args.sides}-sisi tersedia: {len(cand)}, diuji: {len(trees)}\n")

    import torch
    from depth_anything_3.api import DepthAnything3
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = DepthAnything3.from_pretrained(args.ckpt).to(device=dev).eval()

    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, t in enumerate(trees):
        paths = by_tree[t]
        with torch.inference_mode():
            pred = model.inference([str(p) for p in paths], process_res=args.process_res)
        depth = np.asarray(pred.depth)
        conf = np.asarray(pred.conf) if pred.conf is not None else None
        C = camera_centers(np.asarray(pred.extrinsics))
        m = ring_metrics(C)

        d = depth.reshape(len(depth), -1)
        p1, p50, p99 = np.percentile(d, [1, 50, 99], axis=1)
        dyn = float(np.mean((p99 - p1) / np.maximum(p50, 1e-9)))

        row = {"tree": t, "sides": len(paths), "dyn_range": dyn,
               "conf_mean": float(np.nanmean(conf)) if conf is not None else None, **m}
        rows.append(row)
        if (i + 1) % 5 == 0 or i == 0:
            print(f"  [{i+1}/{len(trees)}] {t}: rmse sudut {m['angle_rmse_deg']:.1f} deg, "
                  f"residual lingkaran {m['circle_resid_mean_rel']*100:.0f}%, "
                  f"urutan benar {m['order_correct']}")

        if i < args.preview:
            import cv2
            pv = []
            for k, p in enumerate(paths):
                rgb = cv2.imread(str(p))
                dm = depth[k].astype(np.float32)
                lo, hi = np.nanpercentile(dm, [2, 98])
                dn = np.clip((dm - lo) / max(hi - lo, 1e-9), 0, 1)
                dv = cv2.applyColorMap((dn * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
                dv = cv2.resize(dv, (rgb.shape[1], rgb.shape[0]))
                pv.append(np.vstack([rgb, dv]))
            canvas = np.hstack(pv)
            s = 1800 / canvas.shape[1]
            cv2.imwrite(str(args.out / f"preview_{t}.jpg"),
                        cv2.resize(canvas, None, fx=s, fy=s),
                        [cv2.IMWRITE_JPEG_QUALITY, 85])

    rmse = np.array([r["angle_rmse_deg"] for r in rows])
    resid = np.array([r["circle_resid_mean_rel"] for r in rows])
    plan = np.array([r["planarity_ratio"] for r in rows])
    okord = np.array([r["order_correct"] for r in rows])
    dyn = np.array([r["dyn_range"] for r in rows])
    exp_step = 360.0 / args.sides

    W = 74
    print("\n" + "=" * W)
    print(f"E-005 — DA3 PADA {args.sides} SISI FOTO ASLI ({len(rows)} pohon)")
    print("=" * W)
    print(f"  langkah sudut diharapkan          : {exp_step:.0f} derajat")
    print(f"  RMSE sudut  : rata2 {rmse.mean():.1f}  median {np.median(rmse):.1f}  "
          f"min {rmse.min():.1f}  maks {rmse.max():.1f}")
    print(f"  residual lingkaran (rata2)        : {resid.mean()*100:.0f}%")
    print(f"  rasio kerataan (rata2)            : {plan.mean():.3f}")
    print(f"  urutan sisi terekonstruksi benar  : {okord.sum()}/{len(rows)} "
          f"({okord.mean()*100:.0f}%)")
    print(f"  rentang dinamis kedalaman (rata2) : {dyn.mean():.2f}")

    # pembanding acak: seberapa bagus tebakan asal?
    rng = np.random.default_rng(0)
    rand_rmse = []
    for _ in range(2000):
        a = np.sort(rng.uniform(0, 360, args.sides))
        st = np.diff(np.r_[a, a[0] + 360])[:args.sides - 1]
        rand_rmse.append(np.sqrt(((st - exp_step) ** 2).mean()))
    rand_rmse = np.array(rand_rmse)
    print(f"\n  pembanding acak (sudut asal)      : RMSE rata2 {rand_rmse.mean():.1f}, "
          f"median {np.median(rand_rmse):.1f}")
    better = (rmse < np.median(rand_rmse)).mean()
    print(f"  pohon yang lebih baik dari acak   : {better*100:.0f}%")

    (args.out / f"report_{args.sides}sides.json").write_text(
        json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nlaporan -> {args.out / f'report_{args.sides}sides.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
