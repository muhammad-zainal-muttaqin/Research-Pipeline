"""Potong tandan pada resolusi asli (960x1280) untuk melatih pengklasifikasi
kematangan tahap-2.

Alasannya langsung dari E-014: head klasifikasi YOLO memutuskan kematangan dari
peta fitur citra yang sudah diperkecil ke 640 — tandan bermedian ~46 px di sana.
Potongan asli memberi 2-4x piksel lebih banyak pada objek yang sama, dan warna
serta tekstur permukaan buah adalah bukti kematangan.

Konteks 25% disertakan (buah dinilai relatif terhadap pelepah di sekitarnya).
"""
import argparse, os
from multiprocessing import Pool
from pathlib import Path
import cv2

NAMES = ["B1", "B2", "B3", "B4"]
PAD = 0.25


def one(job):
    img_path, out_root = job
    p = Path(img_path)
    lab = Path(str(p).replace("/images/", "/labels/")).with_suffix(".txt")
    if not lab.exists():
        return 0
    im = cv2.imread(str(p))
    if im is None:
        return 0
    H, W = im.shape[:2]
    n = 0
    for i, line in enumerate(lab.read_text().split("\n")):
        f = line.split()
        if len(f) < 5:
            continue
        c = int(f[0])
        cx, cy, bw, bh = (float(v) for v in f[1:5])
        pw, ph = bw * (1 + 2 * PAD) * W, bh * (1 + 2 * PAD) * H
        x0 = max(0, int(cx * W - pw / 2)); y0 = max(0, int(cy * H - ph / 2))
        x1 = min(W, int(cx * W + pw / 2)); y1 = min(H, int(cy * H + ph / 2))
        if x1 - x0 < 8 or y1 - y0 < 8:
            continue
        cv2.imwrite(str(out_root / NAMES[c] / f"{p.stem}_{i}.jpg"),
                    im[y0:y1, x0:x1], [cv2.IMWRITE_JPEG_QUALITY, 95])
        n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dst", default="crops")
    a = ap.parse_args()
    dst = Path(a.dst)
    total = {}
    for split in ["train", "val", "test"]:
        root = dst / split
        for nm in NAMES:
            (root / nm).mkdir(parents=True, exist_ok=True)
        imgs = [l.strip() for l in open(f"splits_rgb/{split}.txt") if l.strip()]
        with Pool(os.cpu_count()) as pool:
            counts = pool.map(one, [(i, root) for i in imgs], chunksize=16)
        total[split] = sum(counts)
        print(f"{split}: {len(imgs)} citra -> {total[split]} potongan", flush=True)
    for split in total:
        for nm in NAMES:
            print(f"  {split}/{nm}: {len(list((dst/split/nm).glob('*.jpg')))}")


if __name__ == "__main__":
    main()
