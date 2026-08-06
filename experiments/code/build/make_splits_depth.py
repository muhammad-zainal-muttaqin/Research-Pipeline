#!/usr/bin/env python3
"""Bangun split per-pohon untuk SawitMVC-Depth (352 pohon, 1408 citra).

Aturan yang diwarisi dari split lama SawitMVC (E-017: 716/96/141 per pohon,
irisan train/val/test NOL) plus dua penyesuaian karena dataset ini ~1/8 lebih
kecil:

  1. Unit split = POHON (semua 4 sisi ikut ke split yang sama). Wajib —
     4 sisi pohon sama sangat berkorelasi.
  2. Stratifikasi ganda: (a) sesi tangkap = device x unit kamera (dibaca dari
     intrinsik pada depth/*.json, 4 strata), (b) kelas dominan pohon dari
     label YOLO. Kunci strata digabung; strata yang terlalu kecil (< n_min)
     dilebur ke kunci sesi saja lalu ke "GLOBAL".
  3. Beberapa seed: hasilkan split untuk tiap --seed agar varians split bisa
     diukur (dataset kecil -> varians tinggi).

Keluaran: <out>/seed<K>/{train,val,test}.txt (path citra absolut) +
data_rgb.yaml + data_rgbd4.yaml + stats.json (sebaran kotak per kelas/split).

Pemakaian:
  python make_splits_depth.py --root /workspace/SawitMVC-Depth/data \
      --out splits_depth --seed 42 --seed 1 --seed 2 --ratio 0.70 0.10 0.20
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import random
import re
from pathlib import Path

NAMES = ["B1", "B2", "B3", "B4"]


def baca_sesi(root: Path) -> dict[str, str]:
    """tree_id -> 'Device-N|unitFX' dari MERGE_MAP.csv + intrinsik sidecar depth."""
    dev = {r["new_tree_id"]: r["source_device"]
           for r in csv.DictReader(open(root / "MERGE_MAP.csv"))}
    sesi = {}
    for f in (root / "depth").glob("*_1.json"):
        t = f.name.rsplit("_", 1)[0]
        d = json.load(open(f))
        fx = re.search(r"mDepthIntrinsic=CameraIntrinsic\{mFx=([\d.]+)",
                       d["calibrationDump"]).group(1)
        sesi[t] = f"{dev.get(t, '?')}|fx{fx[:6]}"
    for t, v in dev.items():
        sesi.setdefault(t, f"{v}|fx?")
    return sesi


def baca_label(root: Path) -> tuple[dict, dict]:
    """tree_id -> Counter kelas; nama_citra -> jumlah kotak."""
    per_pohon = collections.defaultdict(collections.Counter)
    per_citra = {}
    for f in sorted((root / "labels").glob("*.txt")):
        t = f.stem.rsplit("_", 1)[0]
        n = 0
        for line in f.read_text().splitlines():
            if line.strip():
                per_pohon[t][int(line.split()[0])] += 1
                n += 1
        per_citra[f.stem] = n
        per_pohon[t]  # pastikan pohon tanpa kotak tetap muncul
    return per_pohon, per_citra


def kunci_strata(sesi: str, kelas: collections.Counter) -> str:
    dom = NAMES[kelas.most_common(1)[0][0]] if kelas else "kosong"
    return f"{sesi}|{dom}"


def bagi(pohon: list[str], kunci: dict, rasio, rng, n_min=6):
    """Split per-pohon terstratifikasi; strata kecil dilebur bertahap."""
    grup = collections.defaultdict(list)
    for t in pohon:
        grup[kunci[t]].append(t)
    # lebur strata kecil -> hanya bagian sesi -> GLOBAL
    lebur = collections.defaultdict(list)
    for k, v in grup.items():
        lebur[k if len(v) >= n_min else k.split("|")[0] + "|" + k.split("|")[1]].extend(v)
    final = collections.defaultdict(list)
    for k, v in lebur.items():
        final[k if len(v) >= n_min else "GLOBAL"].extend(v)

    out = {"train": [], "val": [], "test": []}
    for k in sorted(final):
        v = sorted(final[k])
        rng.shuffle(v)
        n = len(v)
        n_tr = round(rasio[0] * n)
        n_va = round(rasio[1] * n)
        out["train"] += v[:n_tr]
        out["val"] += v[n_tr:n_tr + n_va]
        out["test"] += v[n_tr + n_va:]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="/workspace/SawitMVC-Depth/data")
    ap.add_argument("--out", default="splits_depth")
    ap.add_argument("--seed", type=int, action="append", default=None)
    ap.add_argument("--ratio", type=float, nargs=3, default=[0.70, 0.10, 0.20])
    a = ap.parse_args()
    seeds = a.seed or [42]
    root = Path(a.root)

    if not (root / "labels").is_dir():
        print(f"BELUM ADA: {root/'labels'} — unduhan dataset belum selesai.")
        return 1

    sesi = baca_sesi(root)
    per_pohon, per_citra = baca_label(root)
    pohon = sorted(per_pohon)
    kunci = {t: kunci_strata(sesi.get(t, "?"), per_pohon[t]) for t in pohon}
    print(f"{len(pohon)} pohon, {len(per_citra)} citra berlabel, "
          f"{sum(sum(c.values()) for c in per_pohon.values())} kotak")

    for s in seeds:
        rng = random.Random(s)
        sp = bagi(pohon, kunci, a.ratio, rng)
        d = Path(a.out) / f"seed{s}"
        d.mkdir(parents=True, exist_ok=True)
        stats = {}
        for split, trees in sp.items():
            citra = sorted(p for t in trees
                           for p in (root / "images").glob(f"{t}_*.jpg"))
            (d / f"{split}.txt").write_text(
                "\n".join(str(p.resolve()) for p in citra) + "\n")
            c = collections.Counter()
            for t in trees:
                c.update(per_pohon[t])
            stats[split] = {"pohon": len(trees), "citra": len(citra),
                            "kotak": sum(c.values()),
                            **{NAMES[i]: c.get(i, 0) for i in range(4)}}
        # irisan wajib nol
        for x, y in (("train", "val"), ("train", "test"), ("val", "test")):
            assert not (set(sp[x]) & set(sp[y])), (x, y)
        for ch, nm in ((3, "data_rgb.yaml"), (4, "data_rgbd4.yaml")):
            (d / nm).write_text(
                f"path: {d.resolve()}\ntrain: train.txt\nval: val.txt\n"
                f"test: test.txt\nchannels: {ch}\nnc: 4\nnames:\n"
                + "".join(f"  {i}: {n}\n" for i, n in enumerate(NAMES)))
        json.dump(stats, open(d / "stats.json", "w"), indent=2)
        print(f"seed {s}: " + " ".join(
            f"{k}={v['pohon']}p/{v['citra']}c/{v['kotak']}b" for k, v in stats.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
