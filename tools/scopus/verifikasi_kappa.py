#!/usr/bin/env python3
"""Menghitung kesepakatan peninjau manusia dan penyaring AI untuk Cek 1.

Skrip membaca ``sampel_judul.csv`` (300 judul) dan ``sampel_abstrak.csv`` (165
rekaman) di ``verifikasi/cek-1-sampel-buta/``. Keputusan di lembar ditulis bersama
artinya; ``verifikasi_istilah.kode`` mengembalikannya ke kode mentah. Sampel judul
ditarik dari 5.723 judul (benih 20260929), sampel abstrak dari 1.143 rekaman
(benih 20261004). ``angka_naskah.py`` memakai ``muat``, ``kappa``, dan ``tiga``.

    python3 tools/scopus/verifikasi_kappa.py
"""
import csv
import math
import sys
from collections import Counter
from pathlib import Path

from verifikasi_istilah import JUDUL, kode

ROOT = Path(__file__).resolve().parents[2]
VER = ROOT / "literature/scopus-2026-09/verifikasi/cek-1-sampel-buta"

KODE_8 = ["C1", "C2", "C3", "C4", "C5", "R", "T", "X"]
KODE_ABSTRAK = KODE_8[:-1] + [f"X-E{i}" for i in range(1, 8)]
KODE_JUDUL = ["Yes", "Yes-C1", "Yes-C3", "No"]
JUDUL_MANUSIA = {JUDUL[k]: k for k in KODE_JUDUL}
JUDUL_AI = {JUDUL["lanjut"]: "lanjut", JUDUL["eksklusi"]: "eksklusi"}


def baca(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def kappa(x, y):
    """Kappa Cohen; selang 95% memakai galat baku pendekatan sederhana (indikatif)."""
    n = len(x)
    sepakat = sum(a == b for a, b in zip(x, y))
    po = sepakat / n
    pe = sum((x.count(c) / n) * (y.count(c) / n) for c in set(x) | set(y))
    k = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    se = math.sqrt(po * (1 - po) / (n * (1 - pe) ** 2)) if pe < 1 else float("nan")
    return {"n": n, "sepakat": sepakat, "po": po, "kappa": k, "bawah": k - 1.96 * se, "atas": k + 1.96 * se}


def angka(x, d=2):
    """Desimal koma dan tanda minus U+2212."""
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def f_sepakat(s):
    return f"{s['sepakat']} dari {s['n']} ({angka(s['po'] * 100, 1)}%)"


def f_kappa(s):
    return f"{angka(s['kappa'])} [{angka(s['bawah'])}; {angka(s['atas'])}]"


def gabung(k):
    return "X" if k.startswith("X") else k


def biner(k):
    return "eksklusi" if k.startswith("X") else "masuk"


def tiga(data):
    m, a = [d["manusia"] for d in data], [d["ai"] for d in data]
    return (kappa(m, a), kappa([gabung(v) for v in m], [gabung(v) for v in a]),
            kappa([biner(v) for v in m], [biner(v) for v in a]))


def muat():
    masalah = []
    judul = []
    for r in baca(VER / "sampel_judul.csv"):
        m = JUDUL_MANUSIA.get(r["keputusan_manusia"].strip(), "")
        ai = JUDUL_AI.get(r["keputusan_ai"].strip(), "")
        if m not in KODE_JUDUL or ai not in ("lanjut", "eksklusi"):
            masalah.append(f"sampel_judul.csv idx {r['idx']}: manusia '{m}', AI '{ai}'")
            continue
        judul.append({**r, "manusia": m, "ai": ai, "hm": "lanjut" if m.startswith("Yes") else "eksklusi"})
    abstrak = []
    for r in baca(VER / "sampel_abstrak.csv"):
        m, ai = kode(r["keputusan_manusia"]), kode(r["keputusan_ai"])
        if m not in KODE_ABSTRAK or ai not in KODE_ABSTRAK:
            masalah.append(f"sampel_abstrak.csv idx {r['idx']}: manusia '{m}', AI '{ai}'")
            continue
        abstrak.append({**r, "manusia": m, "ai": ai, "di100": r["termasuk_subsampel_acak_100"].strip() == "ya"})
    if masalah:
        sys.exit("Keputusan kosong atau tidak sah:\n" + "\n".join(masalah))
    return judul, abstrak


def main():
    judul, abstrak = muat()
    rj = kappa([d["hm"] for d in judul], [d["ai"] for d in judul])
    ra = tiga(abstrak)
    rs = tiga([d for d in abstrak if d["di100"]])
    kritis_j = [d for d in judul if d["ai"] == "eksklusi" and d["manusia"] in ("Yes-C1", "Yes-C3")]
    kritis_a = [d for d in abstrak if d["ai"].startswith("X") and d["manusia"] in ("C1", "C3")]

    print(f"Judul: {f_sepakat(rj)}, kappa {f_kappa(rj)}, PABAK {angka(2 * rj['po'] - 1)}, kritis {len(kritis_j)}")
    for nama, s in zip(("kode penuh", "eksklusi digabung", "biner"), ra):
        print(f"Abstrak, {nama}: {f_sepakat(s)}, kappa {f_kappa(s)}")
    print(f"Abstrak, subsampel 100, kode penuh: {f_sepakat(rs[0])}, kappa {f_kappa(rs[0])}; kritis {len(kritis_a)}")

if __name__ == "__main__":
    main()
