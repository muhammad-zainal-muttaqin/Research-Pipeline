#!/usr/bin/env python3
"""Ukur ketidaksepakatan kelas kematangan antar-sisi pada SawitMVC.

Motivasi: baseline DiB melaporkan B2 (AP50 0,433) dan B3 (0,599) sebagai sumber
kekeliruan kelas, dan naskah menyebutnya ambiguitas yang sulit direduksi. Klaim
itu selama ini bersandar pada hasil model. Dataset sebenarnya memuat pengukuran
yang jauh lebih langsung: bunch fisik yang sama dilihat dari beberapa sisi, dan
`class_mismatch` menyala ketika anotator memberi kelas berbeda pada bunch yang
sama.

Karena bunch yang sama pasti punya kematangan yang sama, setiap ketidaksepakatan
adalah kesalahan pelabelan pada salah satu sisi. Tingkat ketidaksepakatan itu
karena itu menjadi **batas atas empiris** bagi akurasi klasifikasi per-sisi:
model tidak dapat diharapkan melampaui konsistensi anotator manusianya sendiri.

Keluaran: ringkasan ke stdout + <out>/class_mismatch.json untuk dikutip.

Pemakaian:
  python class_mismatch_stats.py
  python class_mismatch_stats.py --json-dir ... --out ...
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

JSON_DIR = Path("/workspace/SawitMVC/data/json")
OUT_DIR = Path("/workspace/experiments/results")
CLASSES = ["B1", "B2", "B3", "B4", "other"]


def pct(n: int, d: int) -> float:
    return 100.0 * n / d if d else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json-dir", type=Path, default=JSON_DIR)
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    args = ap.parse_args()

    files = sorted(args.json_dir.glob("*.json"))
    if not files:
        print(f"[GAGAL] tidak ada JSON di {args.json_dir}")
        return 2

    n_trees = 0
    n_bunches = 0
    n_multi = 0            # bunch yang tampak dari >=2 sisi (mismatch baru mungkin di sini)
    n_flag = 0             # class_mismatch == True
    n_flag_multi = 0
    n_flag_single = 0      # flag menyala walau hanya 1 sisi -> anomali data

    by_split = defaultdict(lambda: {"multi": 0, "mismatch": 0})
    by_variety = defaultdict(lambda: {"multi": 0, "mismatch": 0})
    by_appearance = defaultdict(lambda: {"multi": 0, "mismatch": 0})
    # ketidaksepakatan per kelas konsensus
    by_consensus = defaultdict(lambda: {"multi": 0, "mismatch": 0})

    # pasangan kelas yang bertabrakan (tak berarah)
    pair_counts = Counter()
    # label per-sisi vs kelas konsensus bunch: batas atas akurasi per-sisi
    view_total = Counter()      # kelas konsensus -> jumlah kemunculan sisi
    view_agree = Counter()      # kelas konsensus -> kemunculan yang labelnya cocok
    view_conf = Counter()       # (konsensus, label sisi) -> jumlah

    anomalies = []

    for fp in files:
        try:
            d = json.loads(fp.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            anomalies.append({"file": fp.name, "error": str(exc)})
            continue

        n_trees += 1
        split = d.get("split", "?")
        variety = (d.get("metadata") or {}).get("variety", "?")

        for b in d.get("bunches", []):
            n_bunches += 1
            consensus = b.get("class")
            flag = bool(b.get("class_mismatch", False))
            apps = b.get("appearances", []) or []
            n_app = b.get("appearance_count", len(apps))

            labels = [a.get("class_name") for a in apps if a.get("class_name")]
            multi = len(labels) >= 2

            if flag:
                n_flag += 1
                if multi:
                    n_flag_multi += 1
                else:
                    n_flag_single += 1
                    anomalies.append({
                        "file": fp.name, "bunch_id": b.get("bunch_id"),
                        "issue": "class_mismatch=True tetapi <2 label sisi",
                        "labels": labels,
                    })

            # konsistensi label sisi vs konsensus, dihitung untuk semua bunch
            if consensus:
                for lab in labels:
                    view_total[consensus] += 1
                    view_conf[(consensus, lab)] += 1
                    if lab == consensus:
                        view_agree[consensus] += 1

            if not multi:
                continue

            n_multi += 1
            disagree = len(set(labels)) > 1

            for bucket, key in (
                (by_split, split), (by_variety, variety),
                (by_appearance, min(n_app, 6)), (by_consensus, consensus or "?"),
            ):
                bucket[key]["multi"] += 1
                if disagree:
                    bucket[key]["mismatch"] += 1

            if disagree:
                uniq = sorted(set(labels))
                for i in range(len(uniq)):
                    for j in range(i + 1, len(uniq)):
                        pair_counts[(uniq[i], uniq[j])] += 1
                # konsistensi flag vs data mentah
                if not flag:
                    anomalies.append({
                        "file": fp.name, "bunch_id": b.get("bunch_id"),
                        "issue": "label sisi berbeda tetapi class_mismatch=False",
                        "labels": labels,
                    })

    # ---------------------------------------------------------------- laporan
    W = 74
    print("=" * W)
    print("KETIDAKSEPAKATAN KELAS ANTAR-SISI — SawitMVC")
    print("=" * W)
    print(f"pohon                                : {n_trees}")
    print(f"bunch unik                           : {n_bunches}")
    print(f"bunch tampak dari >=2 sisi           : {n_multi} ({pct(n_multi, n_bunches):.1f}%)")
    print(f"  -> label antar-sisi berbeda        : {n_flag_multi} "
          f"({pct(n_flag_multi, n_multi):.2f}% dari yang multi-sisi)")
    print(f"flag class_mismatch menyala (total)  : {n_flag}")
    if n_flag_single:
        print(f"  [!] menyala tanpa 2 label sisi     : {n_flag_single}")

    print("\n" + "-" * W)
    print("PASANGAN KELAS YANG BERTABRAKAN")
    print("-" * W)
    tot_pair = sum(pair_counts.values())
    if tot_pair == 0:
        print("  (tidak ada)")
    for (a, b), c in pair_counts.most_common():
        bar = "#" * int(round(40 * c / max(pair_counts.values())))
        print(f"  {a} <-> {b:6s} {c:5d}  ({pct(c, tot_pair):5.1f}%)  {bar}")

    print("\n" + "-" * W)
    print("BATAS ATAS EMPIRIS AKURASI KELAS PER-SISI")
    print("(label satu sisi vs kelas konsensus bunch; kalau anotator sendiri")
    print(" tidak konsisten pada bunch yang sama, model tak bisa melampauinya)")
    print("-" * W)
    print(f"  {'kelas':6s} {'kemunculan':>11s} {'sepakat':>9s} {'batas atas':>11s}")
    for c in CLASSES:
        if view_total[c]:
            print(f"  {c:6s} {view_total[c]:11d} {view_agree[c]:9d} "
                  f"{pct(view_agree[c], view_total[c]):10.2f}%")
    tt, ta = sum(view_total.values()), sum(view_agree.values())
    print(f"  {'TOTAL':6s} {tt:11d} {ta:9d} {pct(ta, tt):10.2f}%")

    print("\n" + "-" * W)
    print("KE MANA LABEL SISI MELESET (baris = konsensus, kolom = label sisi)")
    print("-" * W)
    present = [c for c in CLASSES if view_total[c]]
    print("           " + "".join(f"{c:>9s}" for c in present))
    for r in present:
        row = "".join(f"{view_conf[(r, c)]:9d}" for c in present)
        print(f"  {r:8s} {row}")

    def dump(title, bucket, order=None):
        print("\n" + "-" * W)
        print(title)
        print("-" * W)
        keys = order or sorted(bucket)
        for k in keys:
            if k not in bucket:
                continue
            v = bucket[k]
            print(f"  {str(k):12s} multi={v['multi']:6d}  beda={v['mismatch']:5d}  "
                  f"({pct(v['mismatch'], v['multi']):5.2f}%)")

    dump("PER SPLIT", by_split, ["train", "val", "test"])
    dump("PER VARIETAS", by_variety)
    dump("PER JUMLAH SISI KEMUNCULAN", by_appearance)
    dump("PER KELAS KONSENSUS", by_consensus, CLASSES)

    if anomalies:
        print("\n" + "-" * W)
        print(f"ANOMALI: {len(anomalies)} (flag tidak sinkron dengan label sisi)")
        print("-" * W)
        for a in anomalies[:5]:
            print("  ", a)
        if len(anomalies) > 5:
            print(f"   ... {len(anomalies) - 5} lainnya (lengkap di JSON keluaran)")

    args.out.mkdir(parents=True, exist_ok=True)
    out = {
        "trees": n_trees,
        "bunches": n_bunches,
        "multiview_bunches": n_multi,
        "disagreeing_bunches": n_flag_multi,
        "disagreement_rate_pct": pct(n_flag_multi, n_multi),
        "flag_total": n_flag,
        "flag_without_two_labels": n_flag_single,
        "pairs": {f"{a}|{b}": c for (a, b), c in pair_counts.items()},
        "view_level_ceiling_pct": {
            c: pct(view_agree[c], view_total[c]) for c in CLASSES if view_total[c]
        },
        "view_level_counts": {c: view_total[c] for c in CLASSES if view_total[c]},
        "confusion": {f"{r}|{c}": v for (r, c), v in view_conf.items()},
        "by_split": {k: dict(v) for k, v in by_split.items()},
        "by_variety": {k: dict(v) for k, v in by_variety.items()},
        "by_appearance_count": {str(k): dict(v) for k, v in by_appearance.items()},
        "by_consensus_class": {k: dict(v) for k, v in by_consensus.items()},
        "anomalies": anomalies,
    }
    path = args.out / "class_mismatch.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nhasil lengkap -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
