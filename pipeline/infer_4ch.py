#!/usr/bin/env python3
"""Inferensi lapangan: satu bobot, dengan atau tanpa kedalaman.

Contoh:
  # RGB + depth (kamera Gemini, PNG kanonik senama citra)
  python infer_4ch.py --weights best.pt --source foto/ --depth-dir depth/

  # RGB saja (kamera biasa)
  python infer_4ch.py --weights best.pt --source foto/

Keluaran: citra beranotasi + detections.json (kotak, kelas, skor, hitungan
per kelas per citra) di --save-dir.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import cv2

import fourch

WARNA = {0: (80, 200, 80), 1: (0, 200, 255), 2: (0, 120, 255), 3: (60, 60, 230)}


def gambar(bgr, dets):
    out = bgr.copy()
    for d in dets:
        x0, y0, x1, y1 = (int(v) for v in d["kotak_xyxy"])
        c = WARNA.get(d["kelas"], (255, 255, 255))
        cv2.rectangle(out, (x0, y0), (x1, y1), c, 2)
        cv2.putText(out, f'{d["nama"]} {d["skor"]:.2f}', (x0, max(12, y0 - 4)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, c, 1, cv2.LINE_AA)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights", required=True)
    ap.add_argument("--source", required=True, help="satu citra atau folder")
    ap.add_argument("--depth-dir", default=None,
                    help="folder PNG kedalaman kanonik; kosongkan untuk mode RGB")
    ap.add_argument("--conf", type=float, default=0.25)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--device", default=None)
    ap.add_argument("--save-dir", default="hasil_inferensi")
    args = ap.parse_args()

    src = Path(args.source)
    imgs = sorted(p for p in (src.iterdir() if src.is_dir() else [src])
                  if p.suffix.lower() in (".jpg", ".jpeg", ".png"))
    if not imgs:
        print("tidak ada citra di sumber")
        return 1

    det = fourch.Sawit4CH(args.weights, device=args.device, conf=args.conf,
                          imgsz=args.imgsz)
    save = Path(args.save_dir)
    save.mkdir(parents=True, exist_ok=True)
    mode = "RGB+D" if args.depth_dir else "RGB saja"
    print(f"model 4-kanal: {det.four_channel} | mode masukan: {mode} | {len(imgs)} citra")

    laporan = {}
    for p in imgs:
        bgr = cv2.imread(str(p))
        if bgr is None:
            continue
        d8 = fourch.load_depth_for(p, args.depth_dir)
        if args.depth_dir and d8 is None:
            print(f"  {p.name}: PNG kedalaman tidak ada -> jatuh ke mode RGB")
        r = det.predict(bgr, depth8=d8)
        laporan[p.name] = r
        cv2.imwrite(str(save / p.name), gambar(bgr, r["deteksi"]))
        print(f"  {p.name}: {sum(r['hitung'].values())} tandan {r['hitung']}")

    (save / "detections.json").write_text(json.dumps(laporan, indent=1))
    print(f"\nkeluaran -> {save}/ (+ detections.json)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
