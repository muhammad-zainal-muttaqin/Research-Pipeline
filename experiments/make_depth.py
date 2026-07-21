#!/usr/bin/env python3
"""Bangkitkan peta pseudo-depth untuk SawitMVC.

Tiga backend, sengaja dibuat dapat dibandingkan langsung karena korpus tidak
memuat satu pun benchmark RGB-D pada FFB sawit -- pilihan backend adalah
hipotesis yang harus diuji, bukan diasumsikan:

  dav2    Depth Anything V2 (entri 175) via transformers. Monokular murni,
          satu citra satu peta. Baseline yang paling matang.
  da3mono DA3Mono (entri 198) via paket depth-anything-3. Monokular, tetapi
          memprediksi depth langsung alih-alih disparitas.
  da3mv   DA3 multi-view (entri 198). Seluruh sisi satu pohon dimasukkan
          bersama sehingga kedalaman antar-sisi konsisten, plus pose kamera.
          Ini satu-satunya backend yang berpotensi menyelesaikan penautan
          bunch lintas-sisi secara geometris, dan satu-satunya yang berisiko
          gagal karena baseline lebar / tumpang tindih rendah antar sisi.

Keluaran per citra:
  <out>/depth/NAMA.png       peta kedalaman uint16, ternormalisasi per citra
  <out>/manifest.jsonl       satu baris per citra: rentang mentah + statistik mutu

Normalisasi per citra membuang skala absolut. Itu memang disengaja untuk
backend monokular (keluarannya toh affine-invariant), tetapi untuk da3mv
skala antar-sisi justru bermakna -- karena itu da3mv menormalisasi per POHON,
bukan per citra, dan menyimpan pose kamera. Lihat --norm.

Nilai mentah min/max selalu dicatat di manifest sehingga normalisasi dapat
dibalik tanpa menjalankan ulang model.

Pemakaian:
  python make_depth.py --backend dav2 --limit 40 --preview      # uji cepat
  python make_depth.py --backend da3mv --trees 8 --preview      # uji multi-view
  python make_depth.py --backend dav2                           # seluruh dataset
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from PIL import Image

# --------------------------------------------------------------------------
# Lokasi
# --------------------------------------------------------------------------
DATA_ROOT = Path("/workspace/SawitMVC/data")
IMAGES_DIR = DATA_ROOT / "images"
DEFAULT_OUT = Path("/workspace/experiments/depth")

# DAMIMAS_A21B_0003_1.jpg -> tree "DAMIMAS_A21B_0003", side 1
NAME_RE = re.compile(r"^(?P<tree>.+)_(?P<side>\d+)$")

UINT16_MAX = 65535


def parse_name(stem: str) -> tuple[str, int]:
    m = NAME_RE.match(stem)
    if not m:
        raise ValueError(f"nama berkas di luar pola NAMA_POHON_SISI: {stem}")
    return m.group("tree"), int(m.group("side"))


# --------------------------------------------------------------------------
# Backend
# --------------------------------------------------------------------------
class DepthAnythingV2:
    """Monokular via transformers. Keluaran: disparitas relatif (besar = dekat)."""

    multiview = False
    default_ckpt = "depth-anything/Depth-Anything-V2-Large-hf"

    def __init__(self, ckpt: str, device: str, dtype: torch.dtype):
        from transformers import AutoImageProcessor, AutoModelForDepthEstimation

        self.processor = AutoImageProcessor.from_pretrained(ckpt)
        self.model = AutoModelForDepthEstimation.from_pretrained(
            ckpt, torch_dtype=dtype
        ).to(device).eval()
        self.device = device

    @torch.inference_mode()
    def predict(self, paths: list[Path]) -> list[np.ndarray]:
        images = [Image.open(p).convert("RGB") for p in paths]
        sizes = [(im.height, im.width) for im in images]
        inputs = self.processor(images=images, return_tensors="pt").to(self.device)
        inputs = {k: (v.to(self.model.dtype) if v.is_floating_point() else v)
                  for k, v in inputs.items()}
        pred = self.model(**inputs).predicted_depth  # (B, h, w)
        if pred.ndim == 3:
            pred = pred.unsqueeze(1)
        out = []
        for i, (h, w) in enumerate(sizes):
            d = torch.nn.functional.interpolate(
                pred[i : i + 1].float(), size=(h, w),
                mode="bicubic", align_corners=False,
            )[0, 0]
            out.append(d.cpu().numpy())
        return out


class DepthAnything3:
    """DA3 via paket depth-anything-3.

    Satu kelas melayani dua mode: `multiview=False` memproses tiap citra
    sendiri-sendiri, `multiview=True` memasukkan seluruh sisi satu pohon dalam
    satu panggilan sehingga DA3 dapat menegakkan konsistensi antar-pandangan.
    """

    default_ckpt_mono = "depth-anything/da3mono-large"
    default_ckpt_mv = "depth-anything/da3-large"

    def __init__(self, ckpt: str, device: str, dtype: torch.dtype, multiview: bool):
        from depth_anything_3.api import DepthAnything3 as _DA3

        self.multiview = multiview
        self.model = _DA3.from_pretrained(ckpt).to(device=device)
        self.model.eval()
        self.device = device
        self.last_cameras: dict | None = None

    @torch.inference_mode()
    def predict(self, paths: list[Path]) -> list[np.ndarray]:
        pred = self.model.inference([str(p) for p in paths])

        depth = getattr(pred, "depth", None)
        if depth is None:
            raise RuntimeError(
                "keluaran DA3 tidak memuat atribut `depth`; periksa versi paket "
                f"depth-anything-3. Atribut tersedia: {dir(pred)}"
            )
        depth = np.asarray(depth)
        if depth.ndim == 2:  # satu citra
            depth = depth[None]

        # Pose hanya bermakna pada mode multi-view.
        self.last_cameras = None
        if self.multiview:
            ext = getattr(pred, "extrinsics", None)
            intr = getattr(pred, "intrinsics", None)
            if ext is not None and intr is not None:
                self.last_cameras = {
                    "extrinsics": np.asarray(ext).tolist(),
                    "intrinsics": np.asarray(intr).tolist(),
                }
        return [depth[i] for i in range(depth.shape[0])]


def build_backend(name: str, ckpt: str | None, device: str, dtype: torch.dtype):
    if name == "dav2":
        return DepthAnythingV2(ckpt or DepthAnythingV2.default_ckpt, device, dtype)
    if name == "da3mono":
        return DepthAnything3(
            ckpt or DepthAnything3.default_ckpt_mono, device, dtype, multiview=False
        )
    if name == "da3mv":
        return DepthAnything3(
            ckpt or DepthAnything3.default_ckpt_mv, device, dtype, multiview=True
        )
    raise ValueError(f"backend tidak dikenal: {name}")


# --------------------------------------------------------------------------
# Normalisasi & mutu
# --------------------------------------------------------------------------
def quality_stats(raw: np.ndarray) -> dict:
    """Statistik mentah untuk gating mutu depth.

    D3Net (entri 037) dan SA-Gate (entri 055) menunjukkan depth yang buruk
    justru merusak prediksi, jadi peta ini perlu dapat ditolak, bukan hanya
    dipakai. Angka di sini adalah bahan mentah untuk aturan penolakan itu --
    ambangnya ditentukan belakangan dari data, bukan ditebak sekarang.
    """
    finite = np.isfinite(raw)
    vals = raw[finite]
    if vals.size == 0:
        return {"ok": False, "reason": "seluruh piksel non-finite"}
    lo, hi = float(vals.min()), float(vals.max())
    rng = hi - lo
    grad = np.abs(np.diff(vals.reshape(-1)[: 1_000_000]))
    return {
        "ok": bool(rng > 0),
        "raw_min": lo,
        "raw_max": hi,
        "raw_mean": float(vals.mean()),
        "raw_std": float(vals.std()),
        # proporsi piksel yang menempel di kedua ujung rentang: nilai tinggi
        # menandakan peta datar/terpotong, gejala khas kegagalan di area
        # terang atau langit
        "frac_at_min": float((vals <= lo + 0.01 * rng).mean()) if rng > 0 else 1.0,
        "frac_at_max": float((vals >= hi - 0.01 * rng).mean()) if rng > 0 else 1.0,
        "frac_nonfinite": float((~finite).mean()),
        "mean_abs_grad": float(grad.mean()) if grad.size else 0.0,
    }


def to_uint16(raw: np.ndarray, lo: float, hi: float) -> np.ndarray:
    raw = np.nan_to_num(raw, nan=lo, posinf=hi, neginf=lo)
    if hi <= lo:
        return np.zeros(raw.shape, dtype=np.uint16)
    norm = (raw - lo) / (hi - lo)
    return np.clip(norm * UINT16_MAX, 0, UINT16_MAX).astype(np.uint16)


def save_png16(arr: np.ndarray, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(arr, mode="I;16").save(path, optimize=True)


def save_preview(rgb_path: Path, depth_u16: np.ndarray, path: Path) -> None:
    """RGB | depth berdampingan, untuk inspeksi mata pada kanopi sawit."""
    rgb = Image.open(rgb_path).convert("RGB")
    d8 = (depth_u16.astype(np.float32) / UINT16_MAX * 255).astype(np.uint8)
    dep = Image.fromarray(d8, mode="L").convert("RGB").resize(rgb.size)
    canvas = Image.new("RGB", (rgb.width * 2, rgb.height))
    canvas.paste(rgb, (0, 0))
    canvas.paste(dep, (rgb.width, 0))
    path.parent.mkdir(parents=True, exist_ok=True)
    canvas.resize((canvas.width // 2, canvas.height // 2)).save(path, quality=88)


# --------------------------------------------------------------------------
# Pemilihan berkas
# --------------------------------------------------------------------------
def load_split_map(data_root: Path) -> dict[str, str]:
    """tree_id -> split, dari split_manifest.csv bila tersedia."""
    path = data_root / "split_manifest.csv"
    if not path.exists():
        return {}
    import csv

    with path.open(newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        return {}
    tcol = next((c for c in rows[0] if c.lower() in ("tree_id", "tree")), None)
    scol = next((c for c in rows[0] if c.lower() == "split"), None)
    if not tcol or not scol:
        return {}
    return {r[tcol]: r[scol] for r in rows}


def collect(images_dir: Path, split: str | None, split_map: dict[str, str],
            trees_limit: int | None, image_limit: int | None
            ) -> dict[str, list[Path]]:
    by_tree: dict[str, list[Path]] = defaultdict(list)
    for p in sorted(images_dir.glob("*.jpg")):
        tree, side = parse_name(p.stem)
        if split and split_map.get(tree) != split:
            continue
        by_tree[tree].append(p)
    for tree in by_tree:
        by_tree[tree].sort(key=lambda p: parse_name(p.stem)[1])

    trees = sorted(by_tree)
    if trees_limit:
        trees = trees[:trees_limit]
    out = {t: by_tree[t] for t in trees}

    if image_limit:
        kept, n = {}, 0
        for t, ps in out.items():
            if n >= image_limit:
                break
            take = ps[: image_limit - n]
            kept[t] = take
            n += len(take)
        out = kept
    return out


# --------------------------------------------------------------------------
# Utama
# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--backend", choices=["dav2", "da3mono", "da3mv"], default="dav2")
    ap.add_argument("--ckpt", default=None, help="checkpoint HF, kosongkan untuk default backend")
    ap.add_argument("--images", type=Path, default=IMAGES_DIR)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--split", default=None, choices=["train", "val", "test"])
    ap.add_argument("--trees", type=int, default=None, help="batasi jumlah pohon")
    ap.add_argument("--limit", type=int, default=None, help="batasi jumlah citra")
    ap.add_argument("--batch", type=int, default=4, help="ukuran batch (diabaikan pada da3mv)")
    ap.add_argument("--norm", choices=["image", "tree"], default=None,
                    help="lingkup normalisasi; default: tree untuk da3mv, image untuk sisanya")
    ap.add_argument("--preview", action="store_true", help="tulis pratinjau RGB|depth")
    ap.add_argument("--preview-every", type=int, default=1)
    ap.add_argument("--fp32", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    if not args.images.is_dir():
        print(f"[GAGAL] direktori citra tidak ada: {args.images}", file=sys.stderr)
        return 2

    norm_scope = args.norm or ("tree" if args.backend == "da3mv" else "image")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float32 if (args.fp32 or device == "cpu") else torch.float16

    split_map = load_split_map(args.images.parent)
    if args.split and not split_map:
        print("[GAGAL] --split diminta tetapi split_manifest.csv tidak ditemukan "
              "(unduhan mungkin belum selesai)", file=sys.stderr)
        return 2

    by_tree = collect(args.images, args.split, split_map, args.trees, args.limit)
    n_img = sum(len(v) for v in by_tree.values())
    if n_img == 0:
        print("[GAGAL] tidak ada citra terpilih", file=sys.stderr)
        return 2

    depth_dir = args.out / "depth"
    prev_dir = args.out / "preview"
    manifest_path = args.out / "manifest.jsonl"
    cams_path = args.out / "cameras.json"
    args.out.mkdir(parents=True, exist_ok=True)

    done: set[str] = set()
    if manifest_path.exists() and not args.overwrite:
        with manifest_path.open(encoding="utf-8") as fh:
            for line in fh:
                try:
                    done.add(json.loads(line)["image"])
                except Exception:
                    pass

    print(f"backend={args.backend}  device={device}  dtype={dtype}")
    print(f"pohon={len(by_tree)}  citra={n_img}  sudah ada={len(done)}  norm={norm_scope}")
    print(f"keluaran -> {args.out}")

    model = build_backend(args.backend, args.ckpt, device, dtype)

    cameras: dict[str, dict] = {}
    if cams_path.exists() and not args.overwrite:
        cameras = json.loads(cams_path.read_text(encoding="utf-8"))

    t0 = time.time()
    n_done = n_skip = n_fail = 0
    mf = manifest_path.open("a", encoding="utf-8")

    for tree, paths in by_tree.items():
        todo = [p for p in paths if p.name not in done]
        if not todo:
            n_skip += len(paths)
            continue

        # Mode multi-view wajib melihat seluruh sisi sekaligus; kalau sebagian
        # sudah jadi, tetap hitung ulang satu pohon penuh agar konsisten.
        groups = [paths] if model.multiview else [
            todo[i : i + args.batch] for i in range(0, len(todo), args.batch)
        ]

        for group in groups:
            try:
                raws = model.predict(group)
            except Exception as exc:  # satu kegagalan tidak boleh menghentikan seluruh proses
                n_fail += len(group)
                print(f"[GAGAL] {tree} {[p.name for p in group]}: {exc}", file=sys.stderr)
                continue

            stats = [quality_stats(r) for r in raws]

            if norm_scope == "tree":
                oks = [s for s in stats if s.get("ok")]
                if not oks:
                    n_fail += len(group)
                    continue
                lo = min(s["raw_min"] for s in oks)
                hi = max(s["raw_max"] for s in oks)
                bounds = [(lo, hi)] * len(raws)
            else:
                bounds = [
                    (s.get("raw_min", 0.0), s.get("raw_max", 0.0)) if s.get("ok")
                    else (0.0, 0.0)
                    for s in stats
                ]

            for i, (path, raw, st, (lo, hi)) in enumerate(
                zip(group, raws, stats, bounds)
            ):
                u16 = to_uint16(raw, lo, hi)
                save_png16(u16, depth_dir / f"{path.stem}.png")
                if args.preview and (n_done % args.preview_every == 0):
                    save_preview(path, u16, prev_dir / f"{path.stem}.jpg")

                tree_id, side = parse_name(path.stem)
                rec = {
                    "image": path.name,
                    "tree": tree_id,
                    "side": side,
                    "backend": args.backend,
                    "norm_scope": norm_scope,
                    "norm_lo": lo,
                    "norm_hi": hi,
                    "shape": list(raw.shape),
                    **st,
                }
                mf.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_done += 1

            mf.flush()

        if model.multiview and getattr(model, "last_cameras", None):
            cameras[tree] = {
                "images": [p.name for p in paths],
                **model.last_cameras,
            }
            cams_path.write_text(
                json.dumps(cameras, ensure_ascii=False, indent=1), encoding="utf-8"
            )

        el = time.time() - t0
        rate = n_done / el if el > 0 else 0
        print(f"  {tree}: total {n_done}/{n_img} citra  "
              f"({rate:.2f} citra/s, gagal={n_fail})", flush=True)

    mf.close()
    el = time.time() - t0
    print(f"\nselesai: {n_done} ditulis, {n_skip} dilewati, {n_fail} gagal "
          f"dalam {el/60:.1f} menit")
    if model.multiview:
        print(f"pose kamera {len(cameras)} pohon -> {cams_path}")
    print(f"manifest -> {manifest_path}")
    if n_fail:
        print("\nPERINGATAN: ada kegagalan. Periksa stderr sebelum memakai keluaran ini.")
    return 1 if (n_fail and n_done == 0) else 0


if __name__ == "__main__":
    sys.exit(main())
