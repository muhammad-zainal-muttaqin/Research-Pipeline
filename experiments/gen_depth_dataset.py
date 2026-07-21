#!/usr/bin/env python3
"""I-3 — Bangkitkan pseudo-depth untuk seluruh 3.992 citra SawitMVC.

Kedalaman dihasilkan **per pohon dengan DA3 multi-view**, bukan per citra
sendiri-sendiri. Alasannya adalah inti kontribusi entri 198: kedalaman
antar-sisi menjadi konsisten, sehingga nilai yang sama berarti jarak yang sama
di seluruh sisi pohon itu. Normalisasi karenanya dilakukan **per pohon**, bukan
per citra -- kalau per citra, justru keunggulan itu yang dibuang.

Keluaran:
  depth/NAMA.png       uint16, ternormalisasi per pohon, seukuran citra asli
  conf/NAMA.png        uint8, peta kepercayaan DA3 (untuk gerbang mutu I-8)
  manifest.jsonl       rentang mentah + statistik mutu per citra
  cameras.json         pose & intrinsik kamera per pohon (untuk I-6/I-7)

Pemakaian:
  python gen_depth_dataset.py                  # seluruh dataset
  python gen_depth_dataset.py --trees 20       # uji cepat
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

IMAGES = Path("/workspace/SawitMVC/data/images")
OUT = Path("/workspace/experiments/depth_da3")
U16 = 65535


def group_by_tree(images: Path) -> dict[str, list[Path]]:
    by = defaultdict(list)
    for p in sorted(images.glob("*.jpg")):
        m = re.match(r"^(.*)_(\d+)$", p.stem)
        if m:
            by[m.group(1)].append(p)
    for t in by:
        by[t].sort(key=lambda q: int(re.match(r"^.*_(\d+)$", q.stem).group(1)))
    return dict(by)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", type=Path, default=IMAGES)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--ckpt", default="depth-anything/da3-large")
    ap.add_argument("--process-res", type=int, default=504)
    ap.add_argument("--trees", type=int, default=None)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--shard", type=int, default=0,
                    help="indeks irisan proses ini (0-based)")
    ap.add_argument("--num-shards", type=int, default=1,
                    help="jumlah proses paralel; tiap proses mengambil pohon "
                         "dengan indeks == shard (mod num_shards)")
    args = ap.parse_args()

    by_tree = group_by_tree(args.images)
    trees = sorted(by_tree)
    if args.trees:
        trees = trees[: args.trees]
    if args.num_shards > 1:
        trees = [t for i, t in enumerate(trees) if i % args.num_shards == args.shard]
    n_img = sum(len(by_tree[t]) for t in trees)

    d_dir, c_dir = args.out / "depth", args.out / "conf"
    d_dir.mkdir(parents=True, exist_ok=True)
    c_dir.mkdir(parents=True, exist_ok=True)
    sfx = "" if args.num_shards == 1 else f".s{args.shard}"
    mf_path = args.out / f"manifest{sfx}.jsonl"
    cam_path = args.out / f"cameras{sfx}.json"

    # Pelewatan berbasis keberadaan berkas, bukan manifest: aman dipakai
    # beberapa proses sekaligus dan tetap benar bila proses sebelumnya mati
    # di tengah jalan.
    def tree_done(paths):
        return all((d_dir / f"{p.stem}.png").exists() for p in paths)

    import torch
    from depth_anything_3.api import DepthAnything3
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = DepthAnything3.from_pretrained(args.ckpt).to(device=dev).eval()

    cameras = {}
    if cam_path.exists() and not args.overwrite:
        cameras = json.loads(cam_path.read_text(encoding="utf-8"))

    print(f"[shard {args.shard}/{args.num_shards}] pohon: {len(trees)}  citra: {n_img}")
    print(f"keluaran -> {args.out}\n")

    mf = mf_path.open("a", encoding="utf-8")
    t0 = time.time()
    n_done = n_skip = n_fail = 0

    for ti, t in enumerate(trees):
        paths = by_tree[t]
        if not args.overwrite and tree_done(paths):
            n_skip += len(paths)
            continue
        try:
            with torch.inference_mode():
                pred = model.inference([str(p) for p in paths],
                                       process_res=args.process_res)
        except Exception as exc:
            n_fail += len(paths)
            print(f"[GAGAL] {t}: {exc}", file=sys.stderr)
            continue

        depth = np.asarray(pred.depth, dtype=np.float32)
        conf = np.asarray(pred.conf, dtype=np.float32) if pred.conf is not None else None

        # --- normalisasi PER POHON: inilah yang menjaga konsistensi antar-sisi
        fin = np.isfinite(depth)
        if not fin.any():
            n_fail += len(paths)
            continue
        lo = float(np.percentile(depth[fin], 0.5))
        hi = float(np.percentile(depth[fin], 99.5))
        if hi <= lo:
            n_fail += len(paths)
            continue

        for k, p in enumerate(paths):
            im = cv2.imread(str(p))
            H, W = im.shape[:2]
            d = np.nan_to_num(depth[k], nan=lo, posinf=hi, neginf=lo)
            d = cv2.resize(d, (W, H), interpolation=cv2.INTER_CUBIC)
            u16 = np.clip((d - lo) / (hi - lo), 0, 1)
            cv2.imwrite(str(d_dir / f"{p.stem}.png"), (u16 * U16).astype(np.uint16))

            if conf is not None:
                c = cv2.resize(conf[k], (W, H), interpolation=cv2.INTER_CUBIC)
                c8 = np.clip((c - np.nanmin(conf)) /
                             max(np.nanmax(conf) - np.nanmin(conf), 1e-9), 0, 1)
                cv2.imwrite(str(c_dir / f"{p.stem}.png"), (c8 * 255).astype(np.uint8))

            v = d[np.isfinite(d)]
            mf.write(json.dumps({
                "image": p.name, "tree": t, "side": k + 1,
                "norm_lo": lo, "norm_hi": hi,
                "raw_min": float(v.min()), "raw_max": float(v.max()),
                "raw_mean": float(v.mean()), "raw_std": float(v.std()),
                "frac_at_min": float((u16 <= 0.01).mean()),
                "frac_at_max": float((u16 >= 0.99).mean()),
                "conf_mean": float(np.nanmean(conf[k])) if conf is not None else None,
            }, ensure_ascii=False) + "\n")
            n_done += 1
        mf.flush()

        if pred.extrinsics is not None:
            cameras[t] = {
                "images": [p.name for p in paths],
                "extrinsics": np.asarray(pred.extrinsics).tolist(),
                "intrinsics": np.asarray(pred.intrinsics).tolist(),
            }

        if (ti + 1) % 25 == 0:
            el = time.time() - t0
            rate = n_done / el if el else 0
            eta = (n_img - n_done - n_skip) / rate / 60 if rate else 0
            print(f"  {ti+1}/{len(trees)} pohon | {n_done} citra | "
                  f"{rate:.1f} citra/dtk | ETA {eta:.1f} menit", flush=True)
            cam_path.write_text(json.dumps(cameras, ensure_ascii=False),
                                encoding="utf-8")

    mf.close()
    cam_path.write_text(json.dumps(cameras, ensure_ascii=False), encoding="utf-8")
    el = time.time() - t0
    print(f"\nselesai: {n_done} ditulis, {n_skip} dilewati, {n_fail} gagal, "
          f"{el/60:.1f} menit")
    print(f"pose kamera {len(cameras)} pohon -> {cam_path}")
    return 1 if (n_fail and not n_done) else 0


if __name__ == "__main__":
    raise SystemExit(main())
