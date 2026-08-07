# -*- coding: utf-8 -*-
"""Grafik detektor RGB pada dataset SawitMVC lama, satu protokol pycocotools.

Sumber angka: experiments/results/E-021/perkelas_pycoco.json (split test,
588 citra). Tabel yang sama ada di experiments/EKSPERIMEN.md baris 1045-1050.
"""
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
NAVY, TEAL, GREY, RED = "#1F3A5F", "#2E8B8B", "#9AA5B1", "#C0392B"


def koma(v, n=4):
    return f"{v:.{n}f}".replace(".", ",")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 4.3),
                               gridspec_kw={"width_ratios": [1.22, 1.0],
                                            "wspace": 0.30})

# --- kiri: empat detektor, satu protokol, split test
model = ["YOLO26m\n21,9 jt", "YOLO26l\n26,3 jt",
         "RT-DETR-L\n33,0 jt", "RF-DETR-L\n35,7 jt"]
mapv = [0.5165, 0.5300, 0.5784, 0.6038]
warna = [GREY, GREY, "#4E7FA5", NAVY]
b = ax1.bar(model, mapv, color=warna, width=0.60, edgecolor="white")
for r, v in zip(b, mapv):
    ax1.annotate(koma(v), (r.get_x() + r.get_width() / 2, v),
                 xytext=(0, 6), textcoords="offset points",
                 ha="center", fontsize=14, fontweight="bold",
                 color=NAVY if v == max(mapv) else "#3C4956")
ax1.axhline(0.60, color=TEAL, linewidth=1.4, linestyle="--", zorder=0)
ax1.annotate("sasaran 0,60", (-0.44, 0.617), ha="left", fontsize=11.5, color=TEAL)
ax1.set_ylim(0, 0.72)
ax1.set_yticks([0, 0.2, 0.4, 0.6])
ax1.set_yticklabels([koma(v, 1) for v in [0, 0.2, 0.4, 0.6]], fontsize=11)
ax1.set_ylabel("mAP50 pada split uji", fontsize=12)
ax1.tick_params(axis="x", labelsize=12)
ax1.set_title("Empat detektor warna, satu alat ukur yang sama",
              fontsize=14, pad=9)

# --- kanan: RF-DETR-L per kelas kematangan
kelas = ["B1\nmatang", "B2", "B3", "B4\nmentah"]
ap = [0.8171, 0.4970, 0.6678, 0.4333]
warna2 = [TEAL, TEAL, TEAL, RED]
b2 = ax2.bar(kelas, ap, color=warna2, width=0.58, edgecolor="white")
for r, v in zip(b2, ap):
    ax2.annotate(koma(v), (r.get_x() + r.get_width() / 2, v),
                 xytext=(0, 6), textcoords="offset points",
                 ha="center", fontsize=14, fontweight="bold",
                 color=RED if v == min(ap) else "#3C4956")
ax2.set_ylim(0, 0.98)
ax2.set_yticks([0, 0.2, 0.4, 0.6, 0.8])
ax2.set_yticklabels([koma(v, 1) for v in [0, 0.2, 0.4, 0.6, 0.8]], fontsize=11)
ax2.set_ylabel("AP50 per kelas", fontsize=12)
ax2.tick_params(axis="x", labelsize=12)
ax2.set_title("Rincian detektor terbaik. B4 tetap paling sulit.",
              fontsize=14, pad=9)

fig.savefig(os.path.join(OUT, "chart_rgb.png"), dpi=200, bbox_inches="tight")
plt.close(fig)

from PIL import Image
im = Image.open(os.path.join(OUT, "chart_rgb.png"))
print("chart_rgb.png", im.size, "rasio", round(im.size[0] / im.size[1], 3))
