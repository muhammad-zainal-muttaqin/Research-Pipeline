"""Bangun dataset YOLO yang menunjuk ke piksel MASTER 3024x4032.

Dimungkinkan oleh E-015 (peta isi 3.992/3.992). Rasio aspek kedua tingkat
identik (0,75), jadi koordinat YOLO ternormalisasi berlaku persis — label
disalin apa adanya, tidak ada anotasi ulang.

Kenapa ini berbeda dari sekadar menaikkan imgsz pada SawitMVC: pada 960x1280,
melatih di imgsz 1280 sudah memakai seluruh piksel yang ada. Menaikkannya lebih
jauh hanya memperbesar interpolasi. Master menyediakan piksel yang BENAR-BENAR
ada — 3,15x lipat linear — sehingga imgsz 1536/2048 berisi detail nyata.

Citra di-symlink (tanpa menyalin 16 GB); label disalin karena kecil.
"""
import argparse
import json
import shutil
from pathlib import Path

RAW = Path("/workspace/Sawit/data")
MVC_LAB = Path("/workspace/SawitMVC/data/labels")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", default="results/raw_map.json")
    ap.add_argument("--dst", default="master_ds")
    a = ap.parse_args()

    peta = json.load(open(a.map))["peta"]
    dst = Path(a.dst)
    (dst / "images").mkdir(parents=True, exist_ok=True)
    (dst / "labels").mkdir(parents=True, exist_ok=True)

    total = {}
    for split in ["train", "val", "test"]:
        lines, miss = [], 0
        for l in open(f"splits_rgb/{split}.txt"):
            name = Path(l.strip()).name
            if not l.strip():
                continue
            e = peta.get(name)
            lab = MVC_LAB / f"{Path(name).stem}.txt"
            if e is None or not lab.exists():
                miss += 1
                continue
            link = dst / "images" / name              # nama MVC dipertahankan
            if not link.exists():
                link.symlink_to(RAW / e["raw"])
            tgt = dst / "labels" / f"{Path(name).stem}.txt"
            if not tgt.exists():
                shutil.copy(lab, tgt)
            # JANGAN link.resolve(): itu menelusuri symlink ke folder master,
            # sehingga pasangan /images/ <-> /labels/ yang dipakai ultralytics
            # untuk menemukan label ikut hilang.
            lines.append(str((dst / "images").resolve() / name))
        (dst / f"{split}.txt").write_text("\n".join(lines) + "\n")
        total[split] = (len(lines), miss)
        print(f"{split}: {len(lines)} citra ({miss} terlewat)", flush=True)

    (dst / "data.yaml").write_text(
        f"path: {dst.resolve()}\n"
        "train: train.txt\nval: val.txt\ntest: test.txt\n"
        "channels: 3\nnc: 4\nnames:\n  0: B1\n  1: B2\n  2: B3\n  3: B4\n")
    print(f"data.yaml -> {dst/'data.yaml'}")


if __name__ == "__main__":
    main()
