#!/usr/bin/env python3
"""Ringkas 12 kontras E-023 menjadi satu tabel + agregat lintas-seed.

Tiap kontras diuji berpasangan pada seed-nya sendiri. Menggabungkan ketiganya
memerlukan kehati-hatian: yang dilaporkan di sini adalah RERATA selisih titik
lintas seed dan RENTANG-nya, BUKAN CI gabungan. Tiga seed terlalu sedikit untuk
CI yang bermakna, dan menyajikan "CI lintas-seed" dari tiga angka akan terbaca
jauh lebih kuat daripada bukti yang sebenarnya ada.

Kriteria yang dipakai untuk menyebut sebuah lengan berbeda dari baseline:
seluruh tiga seed sepakat tandanya DAN tidak ada seed yang CI95-nya memuat nol.
Kalau hanya tandanya yang sepakat, itu dilaporkan sebagai indikasi, bukan
temuan — persis pelajaran E-022, yang tumbang karena satu seed dibaca sebagai
kesimpulan.
"""
from __future__ import annotations

import json
from pathlib import Path

DIR = Path(__file__).resolve().parents[3] / "experiments/results/E-023"
LENGAN = ["awal", "mid", "late", "derau"]
SEEDS = [42, 1337, 2024]


def muat(lengan: str, seed: int) -> dict | None:
    p = DIR / f"paired_{lengan}_vs_rgb_seed{seed}.json"
    return json.loads(p.read_text()) if p.is_file() else None


def main() -> int:
    baris = []
    kumpul: dict[str, list] = {a: [] for a in LENGAN}
    for lengan in LENGAN:
        for seed in SEEDS:
            d = muat(lengan, seed)
            if d is None:
                baris.append((lengan, seed, None, None, None, None, None))
                continue
            t, dl = d["titik"], d["delta"]["mAP50"]
            lo, hi = dl["ci95"]
            baris.append((lengan, seed, t["rgb"]["mAP50"], t["rgbd"]["mAP50"],
                          dl["titik"], (lo, hi), dl["frac_positif"]))
            kumpul[lengan].append((dl["titik"], lo, hi))

    print(f"{'lengan':7} {'seed':>5} {'rgb':>8} {'lengan':>8} {'delta':>9} "
          f"{'CI95':>22} {'frac+':>6}")
    for lengan, seed, rgb, arm, dt, ci, fp in baris:
        if dt is None:
            print(f"{lengan:7} {seed:>5} {'-':>8} {'-':>8} {'BELUM ADA':>9}")
            continue
        print(f"{lengan:7} {seed:>5} {rgb:>8.4f} {arm:>8.4f} {dt:>+9.4f} "
              f"[{ci[0]:+.4f}, {ci[1]:+.4f}] {fp:>6.3f}")

    print("\nAgregat lintas-seed (rerata selisih titik; RENTANG, bukan CI):")
    for lengan in LENGAN:
        v = kumpul[lengan]
        if len(v) < len(SEEDS):
            print(f"  {lengan:7} belum lengkap ({len(v)}/{len(SEEDS)} seed)")
            continue
        d = [x[0] for x in v]
        rer = sum(d) / len(d)
        sepakat = all(x > 0 for x in d) or all(x < 0 for x in d)
        nol_luar = all(not (lo <= 0 <= hi) for _, lo, hi in v)
        if sepakat and nol_luar:
            status = "BERBEDA dari baseline (3/3 seed sepakat, nol di luar CI)"
        elif sepakat:
            status = "indikasi saja — tanda sepakat tetapi ada CI yang memuat nol"
        else:
            status = "TIDAK berbeda — tanda pun tidak sepakat antar seed"
        print(f"  {lengan:7} rerata {rer:+.4f}  rentang [{min(d):+.4f}, {max(d):+.4f}]  {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
