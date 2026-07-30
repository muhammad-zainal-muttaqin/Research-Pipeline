"""Buka blokade SR-002: petakan 3.992 citra master mentah (3024x4032) ke citra
SawitMVC (960x1280) berdasarkan ISI, bukan nama berkas.

SR-002 terblokir karena nama berkas mentah tidak unik global (936 nama kembar
antar folder Kelompok). Tetapi kedua tingkat adalah citra yang SAMA pada skala
berbeda, jadi pencocokan isi menyelesaikannya tanpa tabel dari tim.

Tanda tangan: citra diperkecil (JPEG DCT scaling, murah) -> abu-abu 32x40 ->
dinormalkan (rerata 0, norma 1). Kecocokan = hasil kali titik tertinggi.
Diverifikasi: (a) skor > ambang, (b) pemenang jauh di atas peringkat kedua,
(c) pemetaan satu-ke-satu.
"""
import json, os
from multiprocessing import Pool
from pathlib import Path
import cv2, numpy as np

MVC = Path("/workspace/SawitMVC/data/images")
RAW = Path("/workspace/Sawit/data")
GH, GW = 40, 32


def sig(path):
    im = cv2.imread(str(path), cv2.IMREAD_REDUCED_GRAYSCALE_8)
    if im is None:
        im = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if im is None:
        return None
    if im.shape[0] < im.shape[1]:          # samakan orientasi ke potret
        im = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
    v = cv2.resize(im, (GW, GH), interpolation=cv2.INTER_AREA).astype(np.float32).ravel()
    v -= v.mean()
    n = np.linalg.norm(v)
    return v / n if n > 1e-6 else None


def sig_job(p):
    return str(p), sig(p)


def collect(paths, tag):
    with Pool(os.cpu_count()) as pool:
        out = pool.map(sig_job, paths, chunksize=8)
    keep = [(p, s) for p, s in out if s is not None]
    print(f"{tag}: {len(keep)}/{len(paths)} tanda tangan", flush=True)
    return [p for p, _ in keep], np.stack([s for _, s in keep])


def main():
    mvc_paths = sorted(MVC.glob("*.jpg"))
    raw_paths = sorted(p for p in RAW.rglob("*.jpg"))
    print(f"MVC {len(mvc_paths)} | RAW {len(raw_paths)}", flush=True)
    mp_, M = collect(mvc_paths, "MVC")
    rp_, R = collect(raw_paths, "RAW")

    S = M @ R.T                                    # (nMVC, nRAW)
    order = np.argsort(-S, axis=1)
    best, second = order[:, 0], order[:, 1]
    bs = S[np.arange(len(mp_)), best]
    ss = S[np.arange(len(mp_)), second]

    pairs, ambigu, lemah = {}, 0, 0
    taken = {}
    for i, p in enumerate(mp_):
        if bs[i] < 0.90:
            lemah += 1; continue
        if bs[i] - ss[i] < 0.02:
            ambigu += 1; continue
        j = int(best[i])
        if j in taken and bs[taken[j]] >= bs[i]:
            continue
        taken[j] = i
        pairs[Path(p).name] = {"raw": str(Path(rp_[j]).relative_to(RAW)),
                               "skor": round(float(bs[i]), 4),
                               "margin": round(float(bs[i] - ss[i]), 4)}
    stat = {"mvc": len(mp_), "raw": len(rp_), "cocok": len(pairs),
            "lemah": lemah, "ambigu": ambigu,
            "skor_min": round(float(min(v["skor"] for v in pairs.values())), 4) if pairs else None,
            "margin_median": round(float(np.median([v["margin"] for v in pairs.values()])), 4) if pairs else None}
    print(json.dumps(stat, indent=1))
    Path("results").mkdir(exist_ok=True)
    json.dump({"stat": stat, "peta": pairs}, open("results/raw_map.json", "w"), indent=1)


if __name__ == "__main__":
    main()
