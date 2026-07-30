#!/usr/bin/env python3
"""E-003 — Uji DA3 multi-view pada video orbit pohon sawit.

Hipotesis: DA3 (entri 198) dapat merekonstruksi geometri pohon yang konsisten
dari video orbit. Kalau berhasil, kedalaman antar-pandangan dapat diandalkan
untuk memisahkan bunch bertumpuk, dan penautan bunch lintas-sisi dapat dikerjakan
secara geometris alih-alih statistik (k ~ 1,89 / SVR).

Yang memalsukan hipotesis ini:
  (a) rekonstruksi gagal / error,
  (b) pusat kamera tidak membentuk orbit yang masuk akal (residual besar,
      cakupan sudut sempit, atau tersebar acak),
  (c) peta kedalaman kanopi datar -- tidak memisahkan lapisan depan/belakang.

Skrip ini sengaja hanya mendiagnosis, bukan membangun apa pun di atas hasilnya.

Pemakaian:
  python da3_video_test.py --frames 16
  python da3_video_test.py --video "/path/ke/VID.mp4" --frames 24 --ckpt depth-anything/da3-large
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import cv2
import numpy as np

VIDEO_DIR = Path("/workspace/Sawit/data/Video/Kelompok 6")
OUT_DIR = Path("/workspace/experiments/results/e003")


# --------------------------------------------------------------------------
def extract_frames(video: Path, k: int, out_dir: Path) -> list[Path]:
    """Ambil k frame berjarak sama dari video."""
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise RuntimeError(f"tidak bisa membuka video: {video}")
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"video : {video.name}")
    print(f"        {w}x{h}, {total} frame, {fps:.1f} fps, {total/max(fps,1):.1f} dtk")

    idx = np.linspace(0, total - 1, k).round().astype(int)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, fi in enumerate(idx):
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(fi))
        ok, frame = cap.read()
        if not ok:
            print(f"  [!] frame {fi} gagal dibaca, dilewati")
            continue
        p = out_dir / f"f{i:03d}_{fi:05d}.jpg"
        cv2.imwrite(str(p), frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        paths.append(p)
    cap.release()
    print(f"        -> {len(paths)} frame diekstrak")
    return paths


# --------------------------------------------------------------------------
def camera_centers(extrinsics: np.ndarray) -> np.ndarray:
    """Pusat kamera di koordinat dunia dari matriks world-to-camera.

    DA3 mengembalikan (N,3,4); bentuk (N,4,4) juga diterima. Baris ke-4 (kalau
    ada) diabaikan karena hanya [0,0,0,1].
    """
    C = []
    for E in extrinsics:
        R, t = E[:3, :3], E[:3, 3]
        C.append(-R.T @ t)
    return np.stack(C)


def analyse_orbit(C: np.ndarray) -> dict:
    """Apakah pusat kamera membentuk orbit? Diagnosa, bukan penilaian lulus/gagal.

    Langkah: pusatkan -> PCA -> ambil 2 komponen utama sebagai bidang orbit ->
    ukur simpangan dari bidang, lalu kecocokan lingkaran pada bidang itu.
    """
    n = len(C)
    if n < 3:
        return {"ok": False, "reason": "kurang dari 3 kamera"}

    mu = C.mean(0)
    X = C - mu
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    plane = Vt[:2]                       # dua arah dominan = bidang orbit
    normal = Vt[2]
    proj = X @ plane.T                   # (N,2) koordinat pada bidang
    off_plane = X @ normal               # simpangan dari bidang

    # lingkaran terbaik pada bidang (kuadrat terkecil linear)
    A = np.c_[2 * proj, np.ones(n)]
    b = (proj ** 2).sum(1)
    sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    cx, cy = sol[0], sol[1]
    r = float(np.sqrt(max(sol[2] + cx ** 2 + cy ** 2, 0)))

    d = np.linalg.norm(proj - [cx, cy], axis=1)
    resid = d - r

    ang = np.unwrap(np.arctan2(proj[:, 1] - cy, proj[:, 0] - cx))
    span = float(np.degrees(abs(ang[-1] - ang[0])))
    steps = np.degrees(np.diff(ang))
    monotonic = bool(np.all(steps > 0) or np.all(steps < 0))

    scale = float(np.linalg.norm(X, axis=1).mean())
    return {
        "ok": True,
        "n_cameras": n,
        "radius": r,
        "radius_rel": r / scale if scale else 0.0,
        "circle_resid_mean_rel": float(abs(resid).mean() / r) if r else None,
        "circle_resid_max_rel": float(abs(resid).max() / r) if r else None,
        "off_plane_rms_rel": float(np.sqrt((off_plane ** 2).mean()) / r) if r else None,
        "angular_span_deg": span,
        "step_deg_mean": float(abs(steps).mean()),
        "step_deg_std": float(steps.std()),
        "monotonic_sweep": monotonic,
        "pca_singular_values": S.tolist(),
        "planarity_ratio": float(S[2] / S[0]) if S[0] else None,
    }


def depth_layering(depth: np.ndarray, conf: np.ndarray | None) -> dict:
    """Apakah peta kedalaman memisahkan lapisan, atau datar?

    Kanopi sawit yang benar-benar terekonstruksi harus punya sebaran kedalaman
    lebar dan struktur lokal; peta yang datar/terpotong menandakan kegagalan.
    """
    out = {}
    d = depth.reshape(len(depth), -1)
    finite = np.isfinite(d)
    stats = []
    for i in range(len(d)):
        v = d[i][finite[i]]
        if v.size == 0:
            stats.append(None)
            continue
        p1, p50, p99 = np.percentile(v, [1, 50, 99])
        stats.append({
            "min": float(v.min()), "max": float(v.max()),
            "p1": float(p1), "p50": float(p50), "p99": float(p99),
            "std": float(v.std()),
            "dyn_range_ratio": float((p99 - p1) / p50) if p50 else None,
        })
    good = [s for s in stats if s]
    out["per_frame"] = stats
    out["dyn_range_ratio_mean"] = float(np.mean([s["dyn_range_ratio"] for s in good
                                                 if s["dyn_range_ratio"] is not None]))
    out["p50_across_frames_std"] = float(np.std([s["p50"] for s in good]))
    if conf is not None:
        out["conf_mean"] = float(np.nanmean(conf))
        out["conf_frac_low"] = float(np.mean(conf < np.nanpercentile(conf, 20)))
    return out


def save_previews(images: list[Path], depth: np.ndarray, conf: np.ndarray | None,
                  out_dir: Path, every: int) -> None:
    """RGB | depth | conf berdampingan untuk inspeksi mata."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(0, len(images), every):
        rgb = cv2.imread(str(images[i]))
        d = depth[i].astype(np.float32)
        lo, hi = np.nanpercentile(d, [2, 98])
        dn = np.clip((d - lo) / max(hi - lo, 1e-9), 0, 1)
        dv = cv2.applyColorMap((dn * 255).astype(np.uint8), cv2.COLORMAP_TURBO)
        dv = cv2.resize(dv, (rgb.shape[1], rgb.shape[0]))
        panels = [rgb, dv]
        if conf is not None:
            c = conf[i].astype(np.float32)
            cn = np.clip((c - np.nanmin(c)) / max(np.nanmax(c) - np.nanmin(c), 1e-9), 0, 1)
            cv_ = cv2.applyColorMap((cn * 255).astype(np.uint8), cv2.COLORMAP_VIRIDIS)
            panels.append(cv2.resize(cv_, (rgb.shape[1], rgb.shape[0])))
        canvas = np.hstack(panels)
        s = 1600 / canvas.shape[1]
        canvas = cv2.resize(canvas, None, fx=s, fy=s)
        cv2.imwrite(str(out_dir / f"{images[i].stem}_rgb_depth_conf.jpg"), canvas,
                    [cv2.IMWRITE_JPEG_QUALITY, 88])


# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", type=Path, default=None)
    ap.add_argument("--frames", type=int, default=16)
    ap.add_argument("--ckpt", default="depth-anything/da3-large")
    ap.add_argument("--out", type=Path, default=OUT_DIR)
    ap.add_argument("--process-res", type=int, default=504)
    ap.add_argument("--preview-every", type=int, default=4)
    ap.add_argument("--export-glb", action="store_true")
    args = ap.parse_args()

    video = args.video
    if video is None:
        vids = sorted(VIDEO_DIR.glob("*.mp4"))
        if not vids:
            print(f"[GAGAL] tidak ada video di {VIDEO_DIR}", file=sys.stderr)
            return 2
        video = vids[0]

    args.out.mkdir(parents=True, exist_ok=True)
    frames = extract_frames(video, args.frames, args.out / "frames")
    if len(frames) < 3:
        print("[GAGAL] frame terlalu sedikit", file=sys.stderr)
        return 2

    import torch
    from depth_anything_3.api import DepthAnything3

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\nmemuat {args.ckpt} -> {dev}")
    model = DepthAnything3.from_pretrained(args.ckpt).to(device=dev)
    model.eval()

    kw = {}
    if args.export_glb:
        kw = {"export_dir": str(args.out / "glb"), "export_format": "glb"}

    print(f"inferensi multi-view atas {len(frames)} frame (process_res={args.process_res})...")
    import time
    t0 = time.time()
    with torch.inference_mode():
        pred = model.inference([str(p) for p in frames],
                               process_res=args.process_res, **kw)
    dt = time.time() - t0
    print(f"selesai dalam {dt:.1f} dtk ({dt/len(frames):.2f} dtk/frame)\n")

    depth = np.asarray(pred.depth)
    conf = np.asarray(pred.conf) if pred.conf is not None else None
    ext = np.asarray(pred.extrinsics) if pred.extrinsics is not None else None

    W = 74
    print("=" * W)
    print("HASIL E-003 — DA3 MULTI-VIEW PADA VIDEO ORBIT")
    print("=" * W)
    print(f"video          : {video.name}")
    print(f"frame          : {len(frames)}")
    print(f"depth shape    : {depth.shape}")
    print(f"is_metric      : {pred.is_metric}")
    print(f"conf tersedia  : {conf is not None}")
    print(f"extrinsics     : {None if ext is None else ext.shape}")

    report = {
        "video": video.name, "n_frames": len(frames), "ckpt": args.ckpt,
        "process_res": args.process_res, "seconds": dt,
        "depth_shape": list(depth.shape), "is_metric": pred.is_metric,
    }

    print("\n" + "-" * W)
    print("(b) APAKAH POSE KAMERA MEMBENTUK ORBIT?")
    print("-" * W)
    if ext is None:
        print("  extrinsics tidak dikembalikan -> tidak dapat dinilai")
    else:
        C = camera_centers(ext)
        orb = analyse_orbit(C)
        report["orbit"] = orb
        report["camera_centers"] = C.tolist()
        if orb.get("ok"):
            print(f"  radius orbit (relatif sebaran)   : {orb['radius_rel']:.3f}")
            print(f"  residual lingkaran rata-rata     : {orb['circle_resid_mean_rel']*100:.1f}% dari radius")
            print(f"  residual lingkaran maksimum      : {orb['circle_resid_max_rel']*100:.1f}%")
            print(f"  simpangan dari bidang (RMS)      : {orb['off_plane_rms_rel']*100:.1f}%")
            print(f"  cakupan sudut                    : {orb['angular_span_deg']:.1f} derajat")
            print(f"  langkah sudut per frame          : {orb['step_deg_mean']:.1f} +/- {orb['step_deg_std']:.1f}")
            print(f"  sapuan satu arah (monotonik)     : {orb['monotonic_sweep']}")
            print(f"  rasio kerataan (S3/S1)           : {orb['planarity_ratio']:.3f}")

    print("\n" + "-" * W)
    print("(c) APAKAH KEDALAMAN MEMISAHKAN LAPISAN?")
    print("-" * W)
    lay = depth_layering(depth, conf)
    report["layering"] = lay
    print(f"  rentang dinamis (p99-p1)/p50, rata2 : {lay['dyn_range_ratio_mean']:.3f}")
    print(f"  simpangan median antar-frame        : {lay['p50_across_frames_std']:.4f}")
    if conf is not None:
        print(f"  kepercayaan rata-rata               : {lay['conf_mean']:.4f}")
    s0 = next(s for s in lay["per_frame"] if s)
    print(f"  contoh frame 0: min={s0['min']:.3f} p1={s0['p1']:.3f} "
          f"p50={s0['p50']:.3f} p99={s0['p99']:.3f} max={s0['max']:.3f}")

    save_previews(frames, depth, conf, args.out / "preview", args.preview_every)
    print(f"\npratinjau RGB|depth|conf -> {args.out / 'preview'}")

    (args.out / "report.json").write_text(
        json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"laporan -> {args.out / 'report.json'}")
    print("\nCATATAN: angka di atas adalah diagnosa, bukan putusan otomatis.")
    print("Pratinjau wajib dilihat mata sebelum menyimpulkan apa pun.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
