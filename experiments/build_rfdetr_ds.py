"""Bangun adaptor dataset YOLO untuk RF-DETR tanpa menyalin citra.

Mempertahankan split per-pohon E-017 (train/val/test = 3000/404/588) dengan
symlink ke citra dan label SawitMVC. RF-DETR mensyaratkan struktur direktori
train/images, valid/images, test/images dan belum menerima daftar *.txt milik
Ultralytics secara langsung.
"""
from __future__ import annotations

import argparse
from pathlib import Path

SPLITS = {"train": "train", "val": "valid", "test": "test"}
NAMES = ["B1", "B2", "B3", "B4"]


def link(src: Path, dst: Path) -> None:
    if not src.is_file():
        raise FileNotFoundError(src)
    if dst.is_symlink() and dst.resolve() == src.resolve():
        return
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    dst.symlink_to(src.resolve())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--splits", type=Path, default=Path("splits_rgb"))
    ap.add_argument("--labels", type=Path,
                    default=Path("/workspace/SawitMVC/data/labels"))
    ap.add_argument("--output", type=Path, default=Path("rfdetr_ds"))
    args = ap.parse_args()

    seen: set[str] = set()
    counts: dict[str, int] = {}
    for source_name, target_name in SPLITS.items():
        image_dir = args.output / target_name / "images"
        label_dir = args.output / target_name / "labels"
        image_dir.mkdir(parents=True, exist_ok=True)
        label_dir.mkdir(parents=True, exist_ok=True)

        paths = [Path(x.strip()) for x in (args.splits / f"{source_name}.txt").read_text().splitlines() if x.strip()]
        counts[source_name] = len(paths)
        for image in paths:
            if image.name in seen:
                raise ValueError(f"Nama citra muncul pada lebih dari satu split: {image.name}")
            seen.add(image.name)
            link(image, image_dir / image.name)
            link(args.labels / f"{image.stem}.txt", label_dir / f"{image.stem}.txt")

    yaml = (
        "names:\n" + "".join(f"  - {name}\n" for name in NAMES) +
        "nc: 4\n"
        "train: train/images\n"
        "val: valid/images\n"
        "test: test/images\n"
    )
    (args.output / "data.yaml").write_text(yaml)
    print(f"Dataset RF-DETR siap di {args.output.resolve()}: {counts}")


if __name__ == "__main__":
    main()
