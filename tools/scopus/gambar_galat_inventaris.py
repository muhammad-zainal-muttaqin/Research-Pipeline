#!/usr/bin/env python3
"""Buat figur vektor main7 dari contoh hipotetis galat inventaris, dengan gaya gaya_gambar.py.

Keluaran: manuscript/figures/main7/galat-inventaris.pdf.
Jalankan: python3 tools/scopus/gambar_galat_inventaris.py
"""

from collections import Counter
from pathlib import Path

from gaya_gambar import AKSEN2, C, FS, FS_JUDUL, FS_KECIL, GARIS, LATAR, LEBAR_TEKS, REDUP, SOROT, TINTA, simpan

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "manuscript/figures/main7/galat-inventaris.pdf"
WIDTH, HEIGHT = 176, 64
INK = TINTA
MUTED = REDUP
PANEL = LATAR
RULE = GARIS
ALERT = TINTA
CLASS_COLORS = {"Unripe": C["hijau"], "Ripe": AKSEN2}

FIELD = {
    "Unripe": ("A", "B", "C", "D", "E", "I", "J"),
    "Ripe": ("F", "G", "H"),
}
HIDDEN = {"I", "J"}
ESTIMATE = {
    "Unripe": ("A", "B", "B", "C"),
    "Ripe": ("D", "F", "G", "H"),
}


def total(records):
    return sum(len(fruits) for fruits in records.values())


def panel(ax, x, title, subtitle, records, footnote, hidden=(), marked=()):
    ax.add_patch(FancyBboxPatch(
        (x, 13.1), 56, 49.5, boxstyle="round,pad=0,rounding_size=1.6",
        facecolor=PANEL, edgecolor=RULE, linewidth=0.6,
    ))
    ax.text(x + 3.1, 57.5, title, color=INK, size=FS_JUDUL, va="center")
    ax.text(x + 52.7, 57.3, str(total(records)), color=INK, size=FS_JUDUL + 2,
            weight="bold", ha="right", va="center")
    ax.text(x + 3.1, 52.4, subtitle, color=MUTED, size=FS_KECIL, style="italic", va="center")
    ax.hlines(48.2, x + 3.1, x + 52.9, color=RULE, linewidth=0.4)

    for grade, y in (("Unripe", 38.3), ("Ripe", 26.2)):
        fruits = records[grade]
        color = CLASS_COLORS[grade]
        ax.text(x + 3.1, y + 5.45, f"{grade}  {len(fruits)}",
                color=INK, size=FS, weight="bold", va="center")
        for number, fruit in enumerate(fruits):
            cx = x + 5.65 + 6.15 * number
            concealed = fruit in hidden
            ax.add_patch(Circle(
                (cx, y), 2.36, linewidth=0.7, edgecolor=color,
                facecolor="white" if concealed else color,
                linestyle=(0, (2, 2)) if concealed else "solid",
            ))
            ax.text(cx, y, fruit, color=color if concealed else "white",
                    size=FS_KECIL, weight="bold", ha="center", va="center")
            if (grade, number) in marked:
                ax.add_patch(Circle((cx, y), 2.95, fill=False,
                                    edgecolor=ALERT, linewidth=1.0))

    ax.text(x + 3.1, 18.55, footnote, color=INK, size=FS_KECIL,
            va="center", linespacing=1.2)


def main():
    visible = {
        grade: tuple(fruit for fruit in fruits if fruit not in HIDDEN)
        for grade, fruits in FIELD.items()
    }
    true_grade = {fruit: grade for grade, fruits in visible.items() for fruit in fruits}
    seen = Counter()
    marked = set()
    repeated = set()
    relabelled = set()
    for grade, fruits in ESTIMATE.items():
        for number, fruit in enumerate(fruits):
            seen[fruit] += 1
            if seen[fruit] > 1:
                repeated.add(fruit)
                marked.add((grade, number))
            if true_grade[fruit] != grade:
                relabelled.add(fruit)
                marked.add((grade, number))
    missing = true_grade.keys() - seen.keys()

    lebar = LEBAR_TEKS - 0.1
    fig = plt.figure(figsize=(lebar, lebar * HEIGHT / WIDTH))
    ax = fig.add_axes((0, 0, 1, 1), xlim=(0, WIDTH), ylim=(0, HEIGHT))
    ax.set_axis_off()

    panel(ax, 1, "(a) Field reference", "All fruit on the plant", FIELD,
          f"{' and '.join(sorted(HIDDEN))} hidden in all views.", hidden=HIDDEN)
    panel(ax, 60, "(b) Visible reference", "Linked fruit in the images", visible,
          "One record per visible fruit.")
    panel(ax, 119, "(c) Predicted records", "Count and class returned", ESTIMATE,
          f"{', '.join(sorted(repeated))} repeated. {', '.join(sorted(missing))} missed.\n"
          f"{', '.join(sorted(relabelled))} assigned to the ripe class.", marked=marked)

    for x, label, reference in (
        (1, "Signed error against visible count", visible),
        (90, "Signed error against field count", FIELD),
    ):
        ax.add_patch(FancyBboxPatch(
            (x, 1.1), 85, 9.4, boxstyle="round,pad=0,rounding_size=1.3",
            facecolor=SOROT, edgecolor="none",
        ))
        error = total(ESTIMATE) - total(reference)
        ax.text(x + 3.1, 5.85, label, color=INK, va="center", size=FS)
        ax.text(x + 81.6, 5.85, f"{error:+d}".replace("-", "\u2212") if error else "0", color=INK,
                va="center", ha="right", size=FS_JUDUL + 2, weight="bold")

    print(OUT, simpan(fig, OUT, png=False))


if __name__ == "__main__":
    main()
