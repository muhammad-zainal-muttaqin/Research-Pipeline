"""Potongan tandan dari master mentah 3024x4032, memakai peta isi dari
match_raw.py.

Alasan: E-014 menempatkan hambatan pada penilaian kematangan. Kematangan
dinilai dari permukaan buah — warna dan tekstur. Pada SawitMVC (960x1280)
tandan bermedian ~70-95 px, sehingga potongan 224 px sebenarnya hasil
PEMBESARAN: tidak ada detail baru, hanya interpolasi. Pada master mentah
tandan yang sama ~220-300 px, jadi potongan 224 px berisi detail nyata.

Koordinat YOLO ternormalisasi berlaku langsung: rasio aspek kedua tingkat
identik (0,75), jadi tidak perlu anotasi ulang.
"""
import argparse, json, os
from multiprocessing import Pool
from pathlib import Path
import cv2

NAMES = ["B1", "B2", "B3", "B4"]
PAD = 0.25
RAW = Path("/workspace/Sawit/data")


def one(job):
    mvc_path, raw_rel, out_root = job
    p = Path(mvc_path)
    lab = Path(str(p).replace("/images/", "/labels/")).with_suffix(".txt")
    if not lab.exists():
        return 0
    im = cv2.imread(str(RAW / raw_rel))
    if im is None:
        return 0
    H, W = im.shape[:2]
    if H < W:                                  # samakan orientasi ke potret
        im = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
        H, W = im.shape[:2]
    n = 0
    for i, line in enumerate(lab.read_text().split("\n")):
        f = line.split()
        if len(f) < 5:
            continue
        c = int(f[0]); cx, cy, bw, bh = (float(v) for v in f[1:5])
        pw, ph = bw * (1 + 2 * PAD) * W, bh * (1 + 2 * PAD) * H
        x0 = max(0, int(cx * W - pw / 2)); y0 = max(0, int(cy * H - ph / 2))
        x1 = min(W, int(cx * W + pw / 2)); y1 = min(H, int(cy * H + ph / 2))
        if x1 - x0 < 24 or y1 - y0 < 24:
            continue
        cr = im[y0:y1, x0:x1]
        # simpan maksimal 320 px sisi panjang: cukup di atas 224 px masukan,
        # tetapi menjaga dataset tetap ringan dibaca
        s = 320 / max(cr.shape[:2])
        if s < 1:
            cr = cv2.resize(cr, (int(cr.shape[1] * s), int(cr.shape[0] * s)),
                            interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(out_root / NAMES[c] / f"{p.stem}_{i}.jpg"), cr,
                    [cv2.IMWRITE_JPEG_QUALITY, 95])
        n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", default="results/raw_map.json")
    ap.add_argument("--dst", default="crops_raw")
    a = ap.parse_args()
    peta = json.load(open(a.map))["peta"]
    dst = Path(a.dst)
    for split in ["train", "val", "test"]:
        root = dst / split
        for nm in NAMES:
            (root / nm).mkdir(parents=True, exist_ok=True)
        imgs = [l.strip() for l in open(f"splits_rgb/{split}.txt") if l.strip()]
        jobs = [(i, peta[Path(i).name]["raw"], root) for i in imgs
                if Path(i).name in peta]
        with Pool(os.cpu_count()) as pool:
            counts = pool.map(one, jobs, chunksize=8)
        print(f"{split}: {len(jobs)}/{len(imgs)} citra terpetakan -> "
              f"{sum(counts)} potongan", flush=True)


if __name__ == "__main__":
    main()
