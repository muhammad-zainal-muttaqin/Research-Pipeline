# -*- coding: utf-8 -*-
"""Grafik untuk dek reports-simple. Angka bersumber dari reports-simple.tex dan CLAUDE.md."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 13,
    "axes.spines.top": False, "axes.spines.right": False,
})

NAVY, TEAL, GREY, RED, AMBER = "#1F3A5F", "#2E8B8B", "#9AA5B1", "#C0392B", "#D68910"


def koma(v, n=4):
    return f"{v:+.{n}f}".replace(".", ",")


# --- Grafik 1: matriks fusi E-032 (rasio lebar 12 : 4,6) ---------------------
arms = ["Fusi awal", "Fusi menengah", "Fusi akhir", "Derau acak"]
seeds = {
    "seed 42":   [-0.0120, +0.0096, -0.0056, -0.0130],
    "seed 1337": [+0.0234, +0.0212, +0.0070, +0.0025],
    "seed 2024": [-0.0017, +0.0110, +0.0102, -0.0081],
}
means = [+0.0032, +0.0139, +0.0039, -0.0062]
SEEDC = ["#A8C4D8", "#4E7FA5", "#1F3A5F"]

fig, ax = plt.subplots(figsize=(12, 4.6))
x = np.arange(len(arms)); w = 0.24
for i, (lbl, vals) in enumerate(seeds.items()):
    ax.bar(x + (i - 1) * w, vals, w, label=lbl, color=SEEDC[i],
           edgecolor="white", linewidth=1.0, zorder=3)
ax.axhspan(-0.0321, 0.0321, color=AMBER, alpha=0.12, zorder=0)
ax.axhline(0, color="black", linewidth=1.5, zorder=4)
for xi, m in zip(x, means):
    ax.annotate("rerata " + koma(m), (xi, -0.0378), ha="center",
                fontsize=12.5, fontweight="bold",
                color=RED if m < 0 else NAVY, zorder=6)
ax.axvline(2.5, color="#BBBBBB", linewidth=1.2, linestyle="--", zorder=1)
ax.annotate("kelompok kendali", xy=(3.0, 0.0350), ha="center",
            fontsize=12, color=RED, fontweight="bold")
ax.annotate("pita ragam antar-seed pada model yang sama ($\\pm$0,0321)",
            xy=(-0.44, 0.0288), fontsize=11.5, color="#8A6D0B", ha="left")
ax.set_xticks(x); ax.set_xticklabels(arms, fontsize=14)
ticks = [-0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03]
ax.set_yticks(ticks)
ax.set_yticklabels([koma(v, 2) for v in ticks])
ax.set_ylabel("Perubahan mAP50 terhadap RGB-saja", fontsize=12)
ax.set_ylim(-0.044, 0.041)
ax.legend(loc="lower left", frameon=False, ncol=3, fontsize=12,
          bbox_to_anchor=(0.0, -0.03))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "chart_fusi.png"), dpi=200)
plt.close(fig)

# --- Grafik 2: depth dibandingkan derau acak (rasio 11 : 3,4) ---------------
fig, ax = plt.subplots(figsize=(11, 3.4))
lbl = ["Fusi awal", "Fusi menengah", "Fusi akhir", "Derau acak"]
val = [+0.0032, +0.0139, +0.0039, -0.0062]
bar_c = [TEAL, TEAL, TEAL, RED]
bars = ax.barh(lbl, val, color=bar_c, height=0.58, edgecolor="white")
for rect, v in zip(bars, val):
    ax.annotate(koma(v), (v, rect.get_y() + rect.get_height() / 2),
                xytext=(10 if v > 0 else -10, 0), textcoords="offset points",
                va="center", ha="left" if v > 0 else "right",
                fontsize=14, fontweight="bold")
ax.axvline(0, color="black", linewidth=1.5)
ax.set_xlim(-0.021, 0.025)
xt = [-0.02, -0.01, 0, 0.01, 0.02]
ax.set_xticks(xt); ax.set_xticklabels([koma(v, 2) for v in xt])
ax.set_xlabel("Rerata perubahan mAP50 terhadap RGB-saja", fontsize=12)
ax.tick_params(axis="y", labelsize=14)
ax.invert_yaxis()
fig.tight_layout()
fig.savefig(os.path.join(OUT, "chart_derau.png"), dpi=200)
plt.close(fig)

# --- Grafik 3: dua dataset, satuan sama (kotak YOLO) -----------------------
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(12.6, 4.4))
gs = gridspec.GridSpec(2, 3, height_ratios=[1.0, 1.30], hspace=0.72, wspace=0.34,
                       figure=fig)

pairs = [
    ("Jumlah pohon", [953, 352], "pohon"),
    ("Kotak per citra", [4.64, 1.63], "kotak/citra"),
    ("Total kotak anotasi", [18540, 2299], "kotak"),
]
names = ["SawitMVC\n(RGB, lama)", "SawitMVC-Depth\n(RGB-D, di sini)"]
for j, (title, vals, unit) in enumerate(pairs):
    ax = fig.add_subplot(gs[0, j])
    b = ax.bar(names, vals, color=[GREY, NAVY], width=0.55, edgecolor="white")
    for r, v in zip(b, vals):
        txt = f"{v:,.0f}".replace(",", ".") if v >= 100 else f"{v:.2f}".replace(".", ",")
        ax.annotate(txt, (r.get_x() + r.get_width() / 2, v),
                    xytext=(0, 5), textcoords="offset points",
                    ha="center", fontsize=13, fontweight="bold")
    ax.set_title(title, fontsize=13.5, pad=7)
    ax.set_ylabel(unit, fontsize=10.5)
    ax.tick_params(axis="x", labelsize=10)
    ax.tick_params(axis="y", labelsize=10)
    ax.set_ylim(0, max(vals) * 1.32)

# Sebaran kelas, dihitung dari berkas label kedua dataset.
lama_n  = [2032, 3500, 9701, 3307]      # total 18.540
depth_n = [829, 1001, 321, 148]         # total 2.299
lama  = [v / sum(lama_n) * 100 for v in lama_n]
depth = [v / sum(depth_n) * 100 for v in depth_n]

ax = fig.add_subplot(gs[1, :])
x = np.arange(4); w = 0.36
b1 = ax.bar(x - w / 2, lama, w, color=GREY, edgecolor="white",
            label="SawitMVC lama (18.540 kotak)")
b2 = ax.bar(x + w / 2, depth, w, color=NAVY, edgecolor="white",
            label="SawitMVC-Depth (2.299 kotak)")
for bars, pct, cnt in ((b1, lama, lama_n), (b2, depth, depth_n)):
    for r, p, n in zip(bars, pct, cnt):
        cx = r.get_x() + r.get_width() / 2
        ax.annotate(f"{p:.1f}".replace(".", ",") + "%", (cx, p),
                    xytext=(0, 15), textcoords="offset points",
                    ha="center", fontsize=12.5, fontweight="bold")
        ax.annotate(f"{n:,}".replace(",", ".") + " kotak", (cx, p),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", fontsize=10.5, color="#5A6672")
ax.set_xticks(x)
ax.set_xticklabels(["B1\nmatang", "B2", "B3", "B4\nmentah"], fontsize=13)
ax.set_ylabel("porsi kotak dalam\ndatasetnya sendiri", fontsize=10.5)
ax.set_yticks([0, 20, 40, 60])
ax.set_yticklabels(["0%", "20%", "40%", "60%"], fontsize=10)
ax.set_ylim(0, 100)
ax.legend(frameon=False, fontsize=11.5, ncol=2, loc="upper left",
          bbox_to_anchor=(0.0, 1.03))
ax.set_title("Sebaran kelas terbalik. B4 pada dataset depth hanya 148 kotak.",
             fontsize=13.5, pad=7)
fig.savefig(os.path.join(OUT, "chart_dataset.png"), dpi=200, bbox_inches="tight")
plt.close(fig)

from PIL import Image
for f in ["chart_fusi.png", "chart_derau.png", "chart_dataset.png"]:
    im = Image.open(os.path.join(OUT, f))
    print(f, im.size, "rasio", round(im.size[0] / im.size[1], 3))
