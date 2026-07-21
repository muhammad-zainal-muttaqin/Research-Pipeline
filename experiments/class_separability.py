#!/usr/bin/env python3
"""E-012 — Plafon empiris diskriminasi kematangan dari penampilan (ide I-18).

SR-001 gagal mengukur ambiguitas B2/B3 lewat `class_mismatch` (nilainya nol
karena sudah dikonsolidasikan sebelum rilis). SR-007 menunjukkan B2 punya
kontras latar tinggi (dE 18,48) tetapi AP50 rendah (0,433) -- artinya masalahnya
bukan MELIHAT tandan, melainkan MEMBEDAKAN kelasnya.

Uji ini mengukur plafon itu tanpa bergantung pada detektor maupun label manusia
yang saling bertentangan: ambil potongan kotak kebenaran-dasar, hitung fitur
penampilan sederhana, latih pengklasifikasi, lalu lihat matriks kebingungannya.

Karena kotaknya berasal dari kebenaran-dasar, tahap deteksi dihilangkan
sepenuhnya. Yang tersisa murni pertanyaan: **dapatkah kematangan dibedakan dari
penampilan potongan itu saja?** Kalau B2 dan B3 tetap tertukar di sini, maka
ambiguitasnya melekat pada objeknya, bukan pada detektornya.

Pemakaian:  python class_separability.py --per-class 1500
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import cv2
import numpy as np

SRC = Path("/workspace/SawitMVC/data")
CLASSES = ["B1", "B2", "B3", "B4"]


def load_boxes(stem: str):
    f = SRC / "labels" / f"{stem}.txt"
    if not f.exists():
        return []
    out = []
    for line in f.read_text().strip().splitlines():
        p = line.split()
        if len(p) >= 5:
            out.append([int(p[0])] + [float(v) for v in p[1:5]])
    return out


def features(patch: np.ndarray) -> np.ndarray | None:
    """Fitur penampilan sederhana: warna, tekstur, dan gradien.

    Sengaja sederhana dan dapat ditafsirkan. Tujuannya bukan mengalahkan CNN,
    melainkan mengukur apakah sinyal dasarnya ADA.
    """
    if patch.size == 0 or min(patch.shape[:2]) < 8:
        return None
    p = cv2.resize(patch, (48, 48))
    lab = cv2.cvtColor(p, cv2.COLOR_BGR2LAB).astype(np.float32)
    hsv = cv2.cvtColor(p, cv2.COLOR_BGR2HSV).astype(np.float32)
    g = cv2.cvtColor(p, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(g, cv2.CV_32F, ksize=3)
    gx = cv2.Sobel(g, cv2.CV_32F, 1, 0, 3); gy = cv2.Sobel(g, cv2.CV_32F, 0, 1, 3)
    mag = cv2.magnitude(gx, gy)

    f = []
    for ch in (lab[:, :, 0], lab[:, :, 1], lab[:, :, 2],
               hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]):
        f += [ch.mean(), ch.std(), np.percentile(ch, 10), np.percentile(ch, 90)]
    f += [lap.var(), np.abs(lap).mean(), mag.mean(), mag.std(),
          float((mag > mag.mean() + mag.std()).mean())]
    # histogram hue kasar (penanda kematangan)
    h = cv2.calcHist([p], [0], None, [8], [0, 256]).ravel()
    f += (h / max(h.sum(), 1)).tolist()
    return np.array(f, dtype=np.float32)


def collect(split: str, per_class: int, seed=42):
    names = [Path(l).stem for l in (SRC / f"{split}.txt").read_text().split() if l.strip()]
    rng = np.random.default_rng(seed)
    rng.shuffle(names)
    X, y = [], []
    count = Counter()
    for stem in names:
        if all(count[c] >= per_class for c in range(4)):
            break
        im = cv2.imread(str(SRC / "images" / f"{stem}.jpg"))
        if im is None:
            continue
        H, W = im.shape[:2]
        for c, cx, cy, bw, bh in load_boxes(stem):
            if count[c] >= per_class:
                continue
            x0, y0 = int((cx-bw/2)*W), int((cy-bh/2)*H)
            x1, y1 = int((cx+bw/2)*W), int((cy+bh/2)*H)
            f = features(im[max(0, y0):y1, max(0, x0):x1])
            if f is None:
                continue
            X.append(f); y.append(c); count[c] += 1
    return np.array(X), np.array(y)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-class", type=int, default=1500)
    args = ap.parse_args()

    print("mengumpulkan potongan latih...")
    Xtr, ytr = collect("train", args.per_class)
    print("mengumpulkan potongan uji...")
    Xte, yte = collect("test", max(200, args.per_class // 4))
    print(f"latih {Xtr.shape}, uji {Xte.shape}")
    print("sebaran latih:", {CLASSES[k]: int(v) for k, v in sorted(Counter(ytr).items())})

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import confusion_matrix, accuracy_score

    clf = RandomForestClassifier(n_estimators=400, class_weight="balanced",
                                 random_state=42, n_jobs=-1)
    clf.fit(Xtr, ytr)
    pred = clf.predict(Xte)
    acc = accuracy_score(yte, pred)
    cm = confusion_matrix(yte, pred, labels=[0, 1, 2, 3])

    W = 72
    print("\n" + "=" * W)
    print("E-012 — DISKRIMINASI KEMATANGAN DARI POTONGAN KEBENARAN-DASAR")
    print("=" * W)
    print(f"  akurasi keseluruhan : {acc*100:.2f}%  (tebak acak 25%)")
    print(f"\n  matriks kebingungan (baris = sebenarnya, kolom = prediksi)")
    print("           " + "".join(f"{c:>8s}" for c in CLASSES) + f"{'recall':>9s}")
    for i, c in enumerate(CLASSES):
        row = cm[i]
        rec = row[i] / max(row.sum(), 1)
        print(f"  {c:8s} " + "".join(f"{v:8d}" for v in row) + f"{rec*100:8.1f}%")

    print("\n  KEBINGUNGAN PASANGAN (% dari kelas sebenarnya)")
    pairs = []
    for i in range(4):
        for j in range(4):
            if i != j and cm[i].sum():
                pairs.append((CLASSES[i], CLASSES[j], cm[i][j] / cm[i].sum() * 100))
    pairs.sort(key=lambda p: -p[2])
    for a, b, v in pairs[:6]:
        print(f"    {a} -> {b}: {v:5.1f}%")

    # apakah B2/B3 memang yang terburuk?
    b2b3 = cm[1][2] / max(cm[1].sum(), 1) * 100
    b3b2 = cm[2][1] / max(cm[2].sum(), 1) * 100
    print(f"\n  B2<->B3 dua arah: {b2b3:.1f}% dan {b3b2:.1f}%")

    imp = clf.feature_importances_
    print(f"\n  10 fitur terpenting (indeks): {np.argsort(imp)[::-1][:10].tolist()}")

    out = Path("/workspace/experiments/results/e012")
    out.mkdir(parents=True, exist_ok=True)
    (out / "separability.json").write_text(json.dumps({
        "accuracy": float(acc),
        "confusion": cm.tolist(),
        "recall": {CLASSES[i]: float(cm[i][i] / max(cm[i].sum(), 1)) for i in range(4)},
        "pair_confusion_pct": {f"{a}->{b}": float(v) for a, b, v in pairs},
    }, indent=1))
    print(f"\nlaporan -> {out / 'separability.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
