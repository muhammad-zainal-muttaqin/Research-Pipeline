#!/usr/bin/env python3
"""Membuat Lampiran B naskah main6: string kueri Scopus lengkap dari topik/queries.json."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOPIK = ROOT / "literature/scopus-2026-09/topik"
OUT = ROOT / "manuscript/source/main6-appendix-queries.tex"
ESC = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%",
       "$": r"\$", "#": r"\#", "_": r"\_", "~": r"\textasciitilde{}", "^": r"\^{}"}


def esc(s):
    return "".join(ESC.get(c, c) for c in s)


def main():
    q = json.load(open(TOPIK / "queries.json"))
    n = {r["qid"]: r for r in csv.DictReader(open(TOPIK / "counts.csv"))}
    out = ["%% Dibuat otomatis oleh tools/scopus/lampiran_kueri.py; jangan disunting manual."]
    for r in q:
        c = n[r["qid"]]
        kept = int(c["retrieved"])
        tot = int(c["total_results"])
        catatan = f"{tot:,} records" + ("" if kept == tot else f"; the {kept} most cited were retained")
        out.append(r"\paragraph*{%s (%s)}" % (r["qid"], catatan))
        out.append(r"{\footnotesize\ttfamily\raggedright " + esc(r["query"]) + r"\par}")
    OUT.write_text("\n".join(out) + "\n")
    print(len(q), "kueri ->", OUT)


if __name__ == "__main__":
    main()
