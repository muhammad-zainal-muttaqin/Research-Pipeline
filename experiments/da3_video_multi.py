#!/usr/bin/env python3
"""E-004 — DA3 multi-view pada BANYAK video, dengan rotasi diperbaiki.

Menuntaskan tiga keterbatasan E-003:
  1. n=1 video            -> jalankan pada banyak video
  2. frame miring 90 deg  -> ekstraksi lewat ffmpeg yang menerapkan display
                             matrix (cv2 mengabaikannya)
  3. sebab kegagalan ekor -> ukur "segmen mulus terpanjang" dan korelasikan
                             dengan mutu frame (ketajaman, kecerahan, gerak)

Metrik kunci: `smooth_frac` = pecahan frame yang termasuk dalam sapuan orbit
searah terpanjang. Inilah angka yang menentukan apakah pose DA3 dapat dipercaya
pada masukan lapangan, dan inilah yang harus dibandingkan antar-video.

Pemakaian:
  python da3_video_multi.py --videos 6 --frames 32
  python da3_video_multi.py --videos 6 --frames 32 --no-rotate   # pembanding
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

VIDEO_DIR = Path("/workspace/Sawit/data/Video/Kelompok 6")
OUT_DIR = Path("/workspace/experiments/results/e004")


def ffmpeg_exe() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def probe_rotation(video: Path) -> str:
    """Baca metadata rotasi dari keluaran stderr ffmpeg (tanpa ffprobe)."""
    p = subprocess.run([ffmpeg_exe(), "-i", str(video)],
                       capture_output=True, text=True)
    err = p.stderr
    for line in err.splitlines():
        if "rotate" in line.lower() or "displaymatrix" in line.lower():
            return line.strip()
    return "(tidak ada metadata rotasi)"


def extract_frames(video: Path, k: int, out_dir: Path, rotate: bool) -> list[Path]:
    """Ambil k frame berjarak sama.

    rotate=True  -> ffmpeg, menerapkan display matrix (orientasi benar)
    rotate=False -> cv2, mengabaikannya (mereplikasi E-003, sebagai pembanding)
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.jpg"):
        old.unlink()

    cap = cv2.VideoCapture(str(video))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    cap.release()
    if total <= 0:
        return []
    idx = np.linspace(0, total - 1, k).round().astype(int)

    paths = []
    if rotate:
        # satu panggilan ffmpeg per frame: presisi seek, rotasi otomatis
        for i, fi in enumerate(idx):
            t = fi / fps
            p = out_dir / f"f{i:03d}_{fi:05d}.jpg"
            cmd = [ffmpeg_exe(), "-nostdin", "-loglevel", "error",
                   "-ss", f"{t:.3f}", "-i", str(video),
                   "-frames:v", "1", "-q:v", "2", "-y", str(p)]
            subprocess.run(cmd, capture_output=True)
            if p.exists():
                paths.append(p)
    else:
        cap = cv2.VideoCapture(str(video))
        for i, fi in enumerate(idx):
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(fi))
            ok, fr = cap.read()
            if ok:
                p = out_dir / f"f{i:03d}_{fi:05d}.jpg"
                cv2.imwrite(str(p), fr, [cv2.IMWRITE_JPEG_QUALITY, 95])
                paths.append(p)
        cap.release()
    return paths


# --------------------------------------------------------------------------
def camera_centers(ext: np.ndarray) -> np.ndarray:
    return np.stack([-E[:3, :3].T @ E[:3, 3] for E in ext])


def orbit_angles(C: np.ndarray) -> tuple[np.ndarray, dict]:
    mu = C.mean(0)
    X = C - mu
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    proj = X @ Vt[:2].T
    A = np.c_[2 * proj, np.ones(len(proj))]
    sol, *_ = np.linalg.lstsq(A, (proj ** 2).sum(1), rcond=None)
    cx, cy = sol[0], sol[1]
    r = float(np.sqrt(max(sol[2] + cx ** 2 + cy ** 2, 0)))
    ang = np.degrees(np.unwrap(np.arctan2(proj[:, 1] - cy, proj[:, 0] - cx)))
    d = np.linalg.norm(proj - [cx, cy], axis=1)
    meta = {
        "radius": r,
        "circle_resid_mean_rel": float(abs(d - r).mean() / r) if r else None,
        "planarity_ratio": float(S[2] / S[0]) if S[0] else None,
    }
    return ang, meta


def longest_smooth_run(ang: np.ndarray, max_step: float = 40.0) -> tuple[int, int]:
    """Rentang terpanjang dengan langkah searah dan besarnya wajar.

    Sapuan orbit yang benar bergerak satu arah dengan langkah kecil-sedang.
    Langkah yang berbalik arah atau melompat besar menandakan pose tak andal.
    """
    steps = np.diff(ang)
    if len(steps) == 0:
        return 0, 0
    best = (0, 0, 0)  # (panjang, mulai, akhir)
    for sign in (+1, -1):
        i = 0
        while i < len(steps):
            if sign * steps[i] > 0 and abs(steps[i]) <= max_step:
                j = i
                while (j + 1 < len(steps) and sign * steps[j + 1] > 0
                       and abs(steps[j + 1]) <= max_step):
                    j += 1
                if (j - i + 2) > best[0]:
                    best = (j - i + 2, i, j + 1)
                i = j + 1
            else:
                i += 1
    return best[1], best[2]


def frame_quality(paths: list[Path]) -> dict:
    """Ketajaman (varians Laplacian), kecerahan, dan gerak antar-frame."""
    sharp, bright, motion = [], [], []
    prev = None
    for p in paths:
        im = cv2.imread(str(p), cv2.IMREAD_GRAYSCALE)
        if im is None:
            sharp.append(np.nan); bright.append(np.nan); motion.append(np.nan); continue
        small = cv2.resize(im, (320, 180))
        sharp.append(float(cv2.Laplacian(small, cv2.CV_64F).var()))
        bright.append(float(small.mean()))
        motion.append(float(np.abs(small.astype(np.float32) -
                                   prev.astype(np.float32)).mean()) if prev is not None else np.nan)
        prev = small
    return {"sharpness": sharp, "brightness": bright, "motion": motion}


# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--videos", type=int, default=6)
    ap.add_argument("--frames", type=int, default=32)
    ap.add_argument("--ckpt", default="depth-anything/da3-large")
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    ap.add_argument("--process-res", type=int, default=504)
    ap.add_argument("--no-rotate", action="store_true",
                    help="pakai cv2 (abaikan rotasi) untuk mereplikasi E-003")
    args = ap.parse_args()

    vids = sorted(VIDEO_DIR.glob("*.mp4"))[: args.videos]
    if not vids:
        print(f"[GAGAL] tidak ada video di {VIDEO_DIR}", file=sys.stderr)
        return 2
    rotate = not args.no_rotate
    args.out.mkdir(parents=True, exist_ok=True)

    import torch
    from depth_anything_3.api import DepthAnything3
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"memuat {args.ckpt} -> {dev}   (rotasi diperbaiki: {rotate})\n")
    model = DepthAnything3.from_pretrained(args.ckpt).to(device=dev).eval()

    print(f"metadata rotasi video pertama: {probe_rotation(vids[0])}\n")

    rows = []
    for vi, v in enumerate(vids):
        tag = f"{'rot' if rotate else 'norot'}_{v.stem}"
        frames = extract_frames(v, args.frames, args.out / "frames" / tag, rotate)
        if len(frames) < 5:
            print(f"[{vi+1}/{len(vids)}] {v.name}: frame gagal, dilewati")
            continue

        with torch.inference_mode():
            pred = model.inference([str(p) for p in frames],
                                   process_res=args.process_res)
        depth = np.asarray(pred.depth)
        conf = np.asarray(pred.conf) if pred.conf is not None else None
        ext = np.asarray(pred.extrinsics)

        C = camera_centers(ext)
        ang, meta = orbit_angles(C)
        i0, i1 = longest_smooth_run(ang)
        run_len = i1 - i0 + 1
        smooth_frac = run_len / len(ang)
        span_smooth = float(abs(ang[i1] - ang[i0]))

        d = depth.reshape(len(depth), -1)
        p1, p50, p99 = np.percentile(d, [1, 50, 99], axis=1)
        dyn = float(np.mean((p99 - p1) / np.maximum(p50, 1e-9)))

        q = frame_quality(frames)
        row = {
            "video": v.name, "rotate": rotate, "n_frames": len(frames),
            "smooth_start": int(i0), "smooth_end": int(i1),
            "smooth_len": int(run_len), "smooth_frac": smooth_frac,
            "smooth_span_deg": span_smooth,
            "total_span_deg": float(abs(ang[-1] - ang[0])),
            "dyn_range": dyn,
            "conf_mean": float(np.nanmean(conf)) if conf is not None else None,
            **meta,
            "angles": ang.tolist(),
            "quality": q,
        }
        rows.append(row)
        print(f"[{vi+1}/{len(vids)}] {v.name}")
        print(f"      segmen mulus : frame {i0}-{i1} dari {len(ang)} "
              f"({smooth_frac*100:.0f}%), sapuan {span_smooth:.0f} deg")
        print(f"      residual lingkaran {meta['circle_resid_mean_rel']*100:.1f}%  "
              f"kerataan {meta['planarity_ratio']:.3f}  rentang-dinamis {dyn:.2f}")

    if not rows:
        print("[GAGAL] tidak ada hasil")
        return 1

    sf = np.array([r["smooth_frac"] for r in rows])
    sp = np.array([r["smooth_span_deg"] for r in rows])
    W = 74
    print("\n" + "=" * W)
    print(f"RINGKASAN {len(rows)} VIDEO  (rotasi diperbaiki: {rotate})")
    print("=" * W)
    print(f"  smooth_frac      : rata2 {sf.mean()*100:.0f}%  "
          f"median {np.median(sf)*100:.0f}%  min {sf.min()*100:.0f}%  maks {sf.max()*100:.0f}%")
    print(f"  sapuan mulus     : rata2 {sp.mean():.0f} deg  "
          f"median {np.median(sp):.0f} deg  maks {sp.max():.0f} deg")
    print(f"  video >=180 deg  : {int((sp>=180).sum())}/{len(rows)}")
    print(f"  video >=270 deg  : {int((sp>=270).sum())}/{len(rows)}")

    # apakah kegagalan selalu di ekor?
    ends = np.array([r["smooth_end"] / (r["n_frames"] - 1) for r in rows])
    starts = np.array([r["smooth_start"] / (r["n_frames"] - 1) for r in rows])
    print(f"\n  posisi awal segmen mulus (0=awal video) : rata2 {starts.mean():.2f}")
    print(f"  posisi akhir segmen mulus (1=akhir video): rata2 {ends.mean():.2f}")
    print("  -> kalau akhir jauh di bawah 1,00, kegagalan memang menumpuk di ekor")

    # korelasi mutu frame dengan berada di dalam/di luar segmen mulus
    ins, outs = {"sharpness": [], "brightness": [], "motion": []}, {"sharpness": [], "brightness": [], "motion": []}
    for r in rows:
        for k in ins:
            arr = np.array(r["quality"][k], dtype=float)
            mask = np.zeros(len(arr), bool)
            mask[r["smooth_start"]: r["smooth_end"] + 1] = True
            ins[k] += arr[mask][~np.isnan(arr[mask])].tolist()
            outs[k] += arr[~mask][~np.isnan(arr[~mask])].tolist()
    print("\n  mutu frame di DALAM vs LUAR segmen mulus:")
    for k in ins:
        a = np.mean(ins[k]) if ins[k] else float("nan")
        b = np.mean(outs[k]) if outs[k] else float("nan")
        print(f"    {k:11s} dalam={a:8.2f}   luar={b:8.2f}   rasio={a/b if b else float('nan'):.2f}")

    out_path = args.out / f"report_{'rot' if rotate else 'norot'}.json"
    out_path.write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nlaporan -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
