# -*- coding: utf-8 -*-
"""Panel contoh citra: satu citra utuh beranotasi + empat potongan tandan B1-B4.

Citra dipilih dengan aturan yang sama untuk kedua dataset: dari seluruh citra yang
memuat keempat kelas, diambil kandidat peringkat tengah menurut kotak terkecilnya.
  SawitMVC lama  : 573 kandidat -> DAMIMAS_A21B_0641_3.jpg (960x1280)
  SawitMVC-Depth :   8 kandidat -> DAMIMAS_A21B_0023_2.jpg (1280x800)
"""
import os
import cv2
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.family": "DejaVu Sans"})

WARNA = ["#E8552D", "#F1C40F", "#2E86DE", "#8E44AD"]   # B1..B4
NAMA = ["B1 matang", "B2", "B3", "B4 mentah"]

TARGET = {
    "mvc": dict(
        img=r"D:\Work\Assisten-Dosen\Baseline-SawitMVC\SawitMVC-YOLO\images\train\DAMIMAS_A21B_0641_3.jpg",
        lab=r"D:\Work\Assisten-Dosen\Baseline-SawitMVC\SawitMVC-YOLO\labels\train\DAMIMAS_A21B_0641_3.txt",
        judul="SawitMVC lama, kamera ponsel, 960 x 1280",
        out="panel_mvc.png"),
    "depth": dict(
        img=r"D:\Work\Assisten-Dosen\PalmAnnotate-Kotlin\Dataset-28-29July2026\images\DAMIMAS_A21B_0023_2.jpg",
        lab=r"D:\Work\Assisten-Dosen\PalmAnnotate-Kotlin\Dataset-28-29July2026\labels\DAMIMAS_A21B_0023_2.txt",
        judul="SawitMVC-Depth, kamera Orbbec, 1280 x 800",
        out="panel_depth.png"),
}


def baca(cfg):
    im = cv2.cvtColor(cv2.imread(cfg["img"]), cv2.COLOR_BGR2RGB)
    H, W = im.shape[:2]
    kotak = []
    for ln in open(cfg["lab"]):
        q = ln.split()
        if len(q) < 5:
            continue
        c = int(q[0])
        cx, cy, w, h = [float(v) for v in q[1:5]]
        kotak.append((c, (cx - w / 2) * W, (cy - h / 2) * H, w * W, h * H))
    return im, kotak


def terbesar(kotak, c):
    kk = [k for k in kotak if k[0] == c]
    return max(kk, key=lambda k: k[3] * k[4]) if kk else None


def buat(key):
    cfg = TARGET[key]
    im, kotak = baca(cfg)
    H, W = im.shape[:2]

    fig = plt.figure(figsize=(12.4, 4.9))
    gs = gridspec.GridSpec(2, 3, width_ratios=[1.55, 1, 1], wspace=0.12,
                           hspace=0.30, figure=fig)

    ax = fig.add_subplot(gs[:, 0])
    ax.imshow(im)
    for c, x, y, w, h in kotak:
        ax.add_patch(Rectangle((x, y), w, h, fill=False, lw=2.2,
                               edgecolor=WARNA[c]))
        ax.text(x, y - 6, NAMA[c].split()[0], fontsize=11, fontweight="bold",
                color="white", va="bottom",
                bbox=dict(facecolor=WARNA[c], edgecolor="none", pad=1.6))
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(cfg["judul"], fontsize=13, pad=8)

    pos = [(0, 1), (0, 2), (1, 1), (1, 2)]
    for i in range(4):
        k = terbesar(kotak, i)
        r, cpos = pos[i]
        ax = fig.add_subplot(gs[r, cpos])
        if k is None:
            ax.axis("off"); continue
        _, x, y, w, h = k
        pad = 0.16 * max(w, h)
        x1, y1 = int(max(0, x - pad)), int(max(0, y - pad))
        x2, y2 = int(min(W, x + w + pad)), int(min(H, y + h + pad))
        crop = im[y1:y2, x1:x2]
        ax.imshow(crop, interpolation="nearest")
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_edgecolor(WARNA[i]); sp.set_linewidth(3.0)
        ax.set_title("%s  ·  %d x %d px" % (NAMA[i], int(w), int(h)),
                     fontsize=11.5, color=WARNA[i], fontweight="bold", pad=4)

    fig.savefig(os.path.join(HERE, cfg["out"]), dpi=190, bbox_inches="tight")
    plt.close(fig)
    from PIL import Image
    p = os.path.join(HERE, cfg["out"])
    print(cfg["out"], Image.open(p).size)


for k in TARGET:
    buat(k)
