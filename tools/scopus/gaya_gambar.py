"""Gaya bersama semua gambar naskah main6 dan main7.

Dipakai gambar_tinjauan.py dan gambar_galat_inventaris.py. Gambar disimpan
selebar tempatnya di halaman dan dimuat LaTeX tanpa skala
(`\\includegraphics{F..}` tanpa `width`), sehingga huruf FS (7 pt) tercetak
7 pt di semua gambar. `simpan()` menolak gambar yang lebih lebar daripada
batasnya: LEBAR_TEKS untuk naskah cas-dc (\\textwidth 494,5 pt), LEBAR_SUPP
untuk gambar yang juga dimuat bahan tambahan (A4, margin 2,5 cm).

Aturan warna:
- mekanisme asosiasi selalu WARNA_MEK (dan WARNA_GABUNGAN untuk gabungan);
- kelompok kajian selalu WARNA_KAT;
- satu deret yang ditekankan AKSEN, deret kedua AKSEN2, pembanding atau
  "tidak ada" ABU/ABU_MUDA;
- peta panas memakai PETA_WARNA;
- kotak diagram bertepi GARIS, isi putih, LATAR untuk kotak keluar atau
  sekunder, SOROT untuk kotak yang menjadi pokok gambar.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

LEBAR_TEKS = 6.84
LEBAR_SUPP = 6.30

FS = 7.0
FS_KECIL = 6.5
FS_JUDUL = 8.0

C = {"hitam": "#000000", "oranye": "#E69F00", "biru_muda": "#56B4E9",
     "hijau": "#009E73", "kuning": "#F0E442", "biru": "#0072B2",
     "merah": "#D55E00", "ungu": "#CC79A7", "abu": "#8C8C8C", "abu_muda": "#D9D9D9"}
TINTA = "#222222"
GARIS = "#333333"
REDUP = "#555555"
LATAR = "#F2F2F2"
SOROT = "#E3EEF8"
AKSEN = C["biru"]
AKSEN2 = C["oranye"]
ABU = C["abu"]
ABU_MUDA = C["abu_muda"]
PETA_WARNA = "Blues"

WARNA_MEK = {"M0": C["abu"], "M1": C["kuning"], "M2": C["ungu"],
             "M3": C["biru"], "M4": C["hijau"], "M5": C["merah"]}
WARNA_GABUNGAN = {"M2+M3": C["biru_muda"], "M3+M4": C["oranye"], "Other combinations": REDUP}
WARNA_KAT = {"C1": C["biru"], "C2": C["biru_muda"], "C3": C["merah"],
             "C4": C["oranye"], "C5": C["hijau"], "R": C["ungu"], "T": C["abu"]}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIXGeneral"],
    "mathtext.fontset": "stix",
    "font.size": FS,
    "text.color": TINTA,
    "axes.titlesize": FS_JUDUL,
    "axes.titlelocation": "left",
    "axes.titlepad": 4,
    "axes.labelsize": FS,
    "axes.labelcolor": TINTA,
    "axes.edgecolor": GARIS,
    "axes.linewidth": 0.6,
    "xtick.labelsize": FS,
    "ytick.labelsize": FS,
    "xtick.color": TINTA,
    "ytick.color": TINTA,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "legend.fontsize": FS,
    "legend.frameon": False,
    "pdf.fonttype": 42,
})


def campur(warna, t):
    """Warna padat sebesar t dicampur putih (pengganti alpha pada kotak yang tidak bertumpuk)."""
    r, g, b = to_rgb(warna)
    return (1 - t + t * r, 1 - t + t * g, 1 - t + t * b)


def kotak(ax, x, y, w, h, warna="white", lw=0.6, sudut=0.8, **kw):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0.25,rounding_size={sudut}",
                                linewidth=lw, edgecolor=GARIS, facecolor=warna, **kw))


def panah(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=8,
                                 linewidth=0.7, color=GARIS))


def simpan(fig, jalur, batas=LEBAR_TEKS, png=True):
    """Simpan PDF (dan PNG pratinjau) dengan batas putih kecil; tolak bila lebih lebar dari batas (inci)."""
    jalur = Path(jalur)
    jalur.parent.mkdir(parents=True, exist_ok=True)
    pad = 0.02
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    lebar = bb.width + 2 * pad
    assert lebar <= batas + 0.005, f"{jalur.name}: lebar {lebar:.2f} in melebihi {batas:.2f} in"
    fig.savefig(jalur.with_suffix(".pdf"), bbox_inches="tight", pad_inches=pad,
                metadata={"CreationDate": None})
    if png:
        fig.savefig(jalur.with_suffix(".png"), dpi=220, bbox_inches="tight", pad_inches=pad)
    plt.close(fig)
    return round(lebar, 2)
