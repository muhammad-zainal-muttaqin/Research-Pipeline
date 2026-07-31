#!/usr/bin/env python3
"""Konsistensi prediksi detektor pada tandan fisik yang sama antar-sisi.

Menggantikan ukuran yang dipalsukan di E-001. Rekam alasannya, supaya tidak
ditafsirkan keliru lagi:

  `class_mismatch` (E-001/SR-001) mengukur ketidaksepakatan ANOTATOR antar-sisi
  dan hasilnya NOL dari 7.328 bunch multi-sisi. Itu menjadikannya pemeriksa
  integritas data yang bersih, BUKAN pengukur ambiguitas kematangan — dan angka
  nol itu tidak mendukung maupun membantah klaim ambiguitas B2/B3.

  CLAUDE.md mencatat penggantinya: pakai identitas bunch lintas-sisi sebagai
  ORACLE, lalu ukur inkonsistensi PREDIKSI DETEKTOR pada bunch fisik yang sama.
  Ini mengukur ambiguitas tanpa bergantung pada label manusia sama sekali —
  kalau detektor memberi kelas berbeda pada objek fisik yang sama dilihat dari
  sisi berbeda, itu ambiguitas penampilan yang terukur langsung.

Oracle-nya tidak perlu dihitung: `json/<tree>.json` sudah menyediakan
`bunches[].appearances`, yaitu hasil transitive closure graf `_confirmedLinks`
— satu entri = satu tandan fisik, dengan kotak piksel per sisi.

Ukuran yang dilaporkan (semuanya pada tandan yang tampak dari >= 2 sisi):

  laju_inkonsisten  fraksi tandan fisik yang mendapat >= 2 kelas berbeda dari
                    detektor. Nol berarti detektor konsisten secara geometris.
  laju_terlewat     fraksi kemunculan yang tidak terdeteksi sama sekali; dicatat
                    terpisah supaya "konsisten karena tidak terdeteksi" tidak
                    tersamar sebagai "konsisten".

Pemakaian:

  python analysis/cross_side_consistency.py \
      --bobot runs/detect/runs_e022/yolo26n_rgb_seed42/weights/best.pt --modal rgb \
      --keluaran ../../evidence/experiments/results/E-024/konsistensi_rgb.json

Jalankan untuk lengan RGB dan RGB-D dengan checkpoint sepadan: selisih laju
inkonsisten antara keduanya menguji apakah kedalaman MENSTABILKAN identitas
lintas-sisi — pertanyaan yang tidak bisa dijawab oleh mAP agregat.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
DATA = Path("/workspace/SawitMVC-Depth/data")

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

KELAS = ["B1", "B2", "B3", "B4"]


def iou(a: list[float], b: list[float]) -> float:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
    inter = iw * ih
    if inter <= 0:
        return 0.0
    ua = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - inter
    return inter / ua if ua > 0 else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bobot", required=True)
    ap.add_argument("--modal", default="rgb", choices=["rgb", "rgbd", "derau", "tukar"])
    ap.add_argument("--split", default="test", choices=["val", "test"])
    ap.add_argument("--split-dir", default=str(EVIDENCE_ROOT / "splits_depth" / "seed42"))
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--conf", type=float, default=0.25)
    ap.add_argument("--iou-cocok", type=float, default=0.5,
                    help="IoU minimum agar prediksi dianggap kemunculan tandan itu")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--keluaran", default=None)
    args = ap.parse_args()

    from eval.eval_e022_pycoco import prediksi as prediksi_batch

    paths = [Path(x.strip()) for x in
             (Path(args.split_dir) / f"{args.split}.txt").read_text().splitlines() if x.strip()]
    pohon = sorted({p.stem.rsplit("_", 1)[0] for p in paths})
    peta_id = {p.stem: i for i, p in enumerate(paths)}

    # Prediksi seluruh citra split lewat jalur yang SAMA dengan evaluator E-022,
    # supaya komposisi kanal ke-4 dan praproses tidak berbeda diam-diam.
    dets = prediksi_batch(args.bobot, paths, peta_id, args.imgsz, args.modal, seed=args.seed)
    per_stem: dict[str, list[dict]] = defaultdict(list)
    balik = {v: k for k, v in peta_id.items()}
    for d in dets:
        if d["score"] >= args.conf:
            x, y, w, h = d["bbox"]
            per_stem[balik[d["image_id"]]].append(
                {"kotak": [x, y, x + w, y + h], "kelas": KELAS[d["category_id"] - 1],
                 "skor": d["score"]})

    n_bunch = n_multi = n_terukur = n_tidak_konsisten = 0
    n_kemunculan = n_terlewat = 0
    per_kelas_gt = Counter()
    per_kelas_gt_tidak_konsisten = Counter()
    pasangan_salah = Counter()

    for t in pohon:
        jf = DATA / "json" / f"{t}.json"
        if not jf.is_file():
            continue
        data = json.loads(jf.read_text())
        for b in data.get("bunches", []):
            n_bunch += 1
            app = b.get("appearances", [])
            if len(app) < 2:
                continue
            n_multi += 1
            terprediksi = []
            for a in app:
                n_kemunculan += 1
                stem = f"{t}_{a['side_index'] + 1}"
                kandidat = per_stem.get(stem, [])
                terbaik, skor_iou = None, args.iou_cocok
                for p in kandidat:
                    v = iou(a["bbox_pixel"], p["kotak"])
                    if v >= skor_iou:
                        terbaik, skor_iou = p, v
                if terbaik is None:
                    n_terlewat += 1
                else:
                    terprediksi.append(terbaik["kelas"])

            if len(terprediksi) < 2:
                continue          # tak cukup sisi terdeteksi untuk diuji
            n_terukur += 1
            gt = b.get("class", "?")
            per_kelas_gt[gt] += 1
            if len(set(terprediksi)) > 1:
                n_tidak_konsisten += 1
                per_kelas_gt_tidak_konsisten[gt] += 1
                for i in range(len(terprediksi)):
                    for j in range(i + 1, len(terprediksi)):
                        if terprediksi[i] != terprediksi[j]:
                            pasangan_salah["↔".join(sorted((terprediksi[i], terprediksi[j])))] += 1

    lap = {
        "bobot": args.bobot, "modal": args.modal, "split": args.split,
        "conf": args.conf, "iou_cocok": args.iou_cocok,
        "n_pohon": len(pohon), "n_bunch": n_bunch, "n_bunch_multi_sisi": n_multi,
        "n_bunch_terukur": n_terukur,
        "n_kemunculan": n_kemunculan, "n_kemunculan_terlewat": n_terlewat,
        "laju_terlewat": round(n_terlewat / n_kemunculan, 4) if n_kemunculan else None,
        "n_tidak_konsisten": n_tidak_konsisten,
        "laju_inkonsisten": round(n_tidak_konsisten / n_terukur, 4) if n_terukur else None,
        "per_kelas_gt_terukur": dict(per_kelas_gt),
        "per_kelas_gt_tidak_konsisten": dict(per_kelas_gt_tidak_konsisten),
        "pasangan_kelas_bertabrakan": dict(pasangan_salah.most_common()),
    }
    print(json.dumps(lap, indent=2, ensure_ascii=False))
    if args.keluaran:
        Path(args.keluaran).parent.mkdir(parents=True, exist_ok=True)
        Path(args.keluaran).write_text(json.dumps(lap, indent=2, ensure_ascii=False))
        print(f"-> {args.keluaran}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
