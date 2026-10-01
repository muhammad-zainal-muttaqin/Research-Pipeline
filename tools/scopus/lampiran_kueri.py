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


# Nama deskriptif tiap kueri; kunci Q hanya penghubung antara tabel kueri di naskah dan lampiran ini.
NAMA = {
    "Q1": "Multi-observation counting",
    "Q2": "Counting in titles",
    "Q3": "Oil-palm imaging",
    "Q4": "Class attributes with counting",
    "Q5": "Depth and 3D sensing",
    "Q6": "Reviews of association methods",
    "Q7": "Reviews of fruit detection and yield",
    "Q8a": "Methods outside agriculture: multi-object tracking",
    "Q8b": "Methods outside agriculture: multi-view detection and association",
    "Q8c": "Methods outside agriculture: structure from motion and SLAM",
    "Q8d": "Methods outside agriculture: object counting",
    "Q8e": "Methods outside agriculture: re-identification",
    "Q9": "Named foundational methods",
}


def main():
    q = json.load(open(TOPIK / "queries.json"))
    n = {r["qid"]: r for r in csv.DictReader(open(TOPIK / "counts.csv"))}
    out = ["%% Dibuat otomatis oleh tools/scopus/lampiran_kueri.py; jangan disunting manual."]
    for r in q:
        c = n[r["qid"]]
        kept = int(c["retrieved"])
        tot = int(c["total_results"])
        catatan = f"{tot:,} records" + ("" if kept == tot else f"; the {kept} most cited were retained")
        out.append(r"\par\medskip\noindent\textbf{%s. %s} (%s)\par\nobreak\smallskip"
                   % (r["qid"], NAMA[r["qid"]], catatan))
        out.append(r"{\noindent\scriptsize\ttfamily\raggedright " + esc(r["query"]) + r"\par}")
    OUT.write_text("\n".join(out) + "\n", newline="\n")
    print(len(q), "kueri ->", OUT)


if __name__ == "__main__":
    main()
