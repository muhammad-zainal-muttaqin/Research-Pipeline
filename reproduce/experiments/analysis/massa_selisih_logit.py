#!/usr/bin/env python3
"""F-005 (P1) — Massa selisih logit antar-kelas di dalam query yang sama.

Gerbang untuk K2 (kepala ordinal kumulatif berpenjaga-peringkat).

## Kenapa rumusannya bukan "pasangan berskor rapat"

Rencana aslinya menulis P1 sebagai "berapa galat peringkat relevan-AP yang
berselisih < 2*eps". Rumusan itu mengandaikan skor tunggal per deteksi pada
satu daftar terurut. Jalur skor RF-DETR tidak begitu (dibaca langsung dari kode,
F-001):

  - kriteria IA-BCE, `sigmoid` per kelas INDEPENDEN (`criterion.py:268-296`);
  - skor = `sigmoid(z[q,c])`, top-k `num_select=300` atas grid datar Q x C
    (`postprocess.py:106`) -- satu query bisa memancarkan sampai 4 deteksi;
  - mAP COCO dihitung PER KELAS lalu dirata-rata, jadi peringkat hanya penting
    DI DALAM kelas.

Residu K2 ber-mean nol antar 4 kelas dan di-clip +-eps. Yang benar-benar dapat
digerakkannya karena itu adalah selisih logit antar-kelas pada query yang SAMA:

    delta = z[q, c_benar] - z[q, c_teratas_salah]

Urutan hanya dapat dibalik bila |delta| < 2*eps. Dengan eps = 0,3 (nilai yang
dipakai rencana), ambangnya **0,6 logit**.

## Yang memalsukan (ditulis sebelum F-004 selesai dilatih)

K2 GUGUR bila fraksi galat kelas yang berada di dalam pita |delta| < 0,6
**< 0,30**. Di bawah itu, potensi naik K2 tertutup secara matematis: bukti
penjaga-peringkat menjamin urutan tidak rusak, tetapi tidak menjamin ada cukup
kerugian AP yang tinggal di pasangan rapat untuk direbut.

## PERINGATAN: ukuran ini SENSITIF TERHADAP SKALA LOGIT

Pita 2*eps = 0,6 dinyatakan dalam satuan LOGIT, dan skala logit bergantung pada
kematangan latihan serta kalibrasi. Model yang belum konvergen punya logit yang
rapat, sehingga fraksi "di dalam pita" menjadi **bias TINGGI**.

Terukur langsung: pada checkpoint probe F-001 (1 epoch saja) fraksi dalam pita
0,7666 dengan median |delta| hanya 0,3086 -- angka yang akan "meloloskan"
gerbang ini secara palsu. Model yang konvergen memisahkan kelas lebih lebar,
jadi fraksi sesungguhnya akan LEBIH RENDAH.

**Jalankan HANYA pada checkpoint terbaik-val F-004 yang sudah konvergen.**
Angka dari checkpoint mana pun yang belum konvergen tidak sah sebagai putusan
gerbang, dan `ckpt` selalu ikut dicatat di keluaran supaya ini dapat diperiksa.

## Yang DILAPORKAN tetapi TIDAK menggugurkan

Fraksi query yang kelasnya sudah BENAR namun berada di dalam pita yang sama
(`n_benar_dalam_pita`). Itu paparan risiko: residu yang sama dapat merusaknya.
Ini sengaja BUKAN syarat gerbang -- kepala ordinal yang terlatih dan informatif
akan mendorong query benar makin benar, bukan mengacak. Menjadikannya
penggugur berarti menghukum K2 untuk alasan yang tidak sahih. Ia dilaporkan
supaya rasio untung-rugi terlihat, bukan supaya menutup jalan.

Pemakaian:
  python analysis/massa_selisih_logit.py --npz results/F-004/logits_test_seed42.npz
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
DS = Path(__file__).resolve().parents[1] / "rfdetr_ds"

import numpy as np

KELAS = ["B1", "B2", "B3", "B4"]
SPLIT_DIR = {"val": "valid", "test": "test"}
EPS = 0.3
PITA = 2 * EPS          # 0,6 logit
AMBANG_LOLOS = 0.30
IOU_COCOK = 0.5


def gt_boxes(stem: str, w: int, h: int) -> list[tuple[int, float, float, float, float]]:
    """Kotak GT dalam xyxy piksel dari label YOLO."""
    lf = DS / SPLIT_DIR["test"] / "labels" / f"{stem}.txt"
    out = []
    if not lf.is_file():
        return out
    for line in lf.read_text().splitlines():
        if not line.strip():
            continue
        c, cx, cy, bw, bh = map(float, line.split())
        out.append((int(c), (cx - bw / 2) * w, (cy - bh / 2) * h,
                    (cx + bw / 2) * w, (cy + bh / 2) * h))
    return out


def iou_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """IoU antara (N,4) dan (M,4), keduanya xyxy."""
    ix1 = np.maximum(a[:, None, 0], b[None, :, 0])
    iy1 = np.maximum(a[:, None, 1], b[None, :, 1])
    ix2 = np.minimum(a[:, None, 2], b[None, :, 2])
    iy2 = np.minimum(a[:, None, 3], b[None, :, 3])
    iw = np.clip(ix2 - ix1, 0, None)
    ih = np.clip(iy2 - iy1, 0, None)
    inter = iw * ih
    aa = (a[:, 2] - a[:, 0]) * (a[:, 3] - a[:, 1])
    bb = (b[:, 2] - b[:, 0]) * (b[:, 3] - b[:, 1])
    union = aa[:, None] + bb[None, :] - inter
    return np.where(union > 0, inter / np.maximum(union, 1e-9), 0.0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--npz", required=True, help="keluaran eval/dump_logits_rfdetr.py")
    ap.add_argument("--iou", type=float, default=IOU_COCOK)
    ap.add_argument("--pita", type=float, default=PITA)
    ap.add_argument("--keluaran", default=str(
        EVIDENCE_ROOT / "results" / "F-005" / "massa_selisih_logit.json"))
    args = ap.parse_args()

    d = np.load(args.npz, allow_pickle=True)
    logits, boxes, ukuran = d["logits"].astype(np.float32), d["boxes"], d["ukuran"]
    nama = [str(x) for x in d["nama"]]

    delta_salah: list[float] = []      # |z_benar - z_teratas_salah| pada query BERGALAT
    delta_benar: list[float] = []      # margin pada query yang sudah BENAR
    per_kelas_salah: dict[str, list[float]] = {k: [] for k in KELAS}
    bingung = Counter()                # (gt -> prediksi) pada query bergalat
    n_gt = 0
    n_tak_tercocok = 0

    for i, stem in enumerate(nama):
        h, w = int(ukuran[i][0]), int(ukuran[i][1])
        gts = gt_boxes(stem, w, h)
        if not gts:
            continue
        g = np.array([[x0, y0, x1, y1] for _, x0, y0, x1, y1 in gts], np.float32)
        kelas_gt = [c for c, *_ in gts]
        ious = iou_matrix(g, boxes[i].astype(np.float32))   # (n_gt, Q)

        for j in range(len(gts)):
            n_gt += 1
            q = int(np.argmax(ious[j]))
            if ious[j, q] < args.iou:
                # GT tidak tertangkap query mana pun -> kegagalan DETEKSI,
                # bukan kelas. K2 tidak menyentuh kasus ini.
                n_tak_tercocok += 1
                continue
            z = logits[i, q]                    # 4 logit query itu
            c = kelas_gt[j]
            z_benar = float(z[c])
            lain = [k for k in range(len(KELAS)) if k != c]
            k_top = max(lain, key=lambda k: z[k])
            z_salah = float(z[k_top])
            margin = z_benar - z_salah
            if margin < 0:
                delta_salah.append(-margin)
                per_kelas_salah[KELAS[c]].append(-margin)
                bingung[f"{KELAS[c]}->{KELAS[k_top]}"] += 1
            else:
                delta_benar.append(margin)

    ds = np.array(delta_salah)
    db = np.array(delta_benar)
    n_salah = len(ds)
    n_dalam_pita = int((ds < args.pita).sum())
    frak = round(n_dalam_pita / n_salah, 4) if n_salah else None
    n_benar_dalam_pita = int((db < args.pita).sum())

    def kuantil(a):
        if not len(a):
            return None
        return {f"p{p}": round(float(np.percentile(a, p)), 4)
                for p in (10, 25, 50, 75, 90)}

    lolos = frak is not None and frak >= AMBANG_LOLOS
    lap = {
        "eksperimen": "F-005",
        "pertanyaan": "dari GT yang tertangkap query tetapi SALAH kelas, berapa yang |delta| < 2*eps?",
        "rumusan_delta": "z[q, c_benar] - z[q, c_teratas_salah], query yang sama",
        "sumber": str(args.npz),
        "ckpt": str(d["ckpt"][0]),
        "split": str(d["split"][0]),
        "eps": EPS,
        "pita_2eps": args.pita,
        "iou_cocok": args.iou,
        "n_gt": n_gt,
        "n_gt_tak_tercocok": n_tak_tercocok,
        "catatan_tak_tercocok": "kegagalan DETEKSI, di luar jangkauan K2",
        "n_query_salah_kelas": n_salah,
        "n_query_benar_kelas": int(len(db)),
        "massa": {
            "n_salah_dalam_pita": n_dalam_pita,
            "fraksi_salah_dalam_pita": frak,
            "kuantil_delta_salah": kuantil(ds),
        },
        "paparan_risiko_dilaporkan_bukan_penggugur": {
            "n_benar_dalam_pita": n_benar_dalam_pita,
            "fraksi_benar_dalam_pita": (round(n_benar_dalam_pita / len(db), 4)
                                        if len(db) else None),
            "rasio_untung_rugi": (round(n_dalam_pita / n_benar_dalam_pita, 4)
                                  if n_benar_dalam_pita else None),
            "catatan": "kepala ordinal terlatih mendorong query benar makin benar; "
                       "angka ini konteks, bukan syarat gerbang",
        },
        "per_kelas_gt": {
            k: {
                "n_salah": len(v),
                "n_dalam_pita": int((np.array(v) < args.pita).sum()) if v else 0,
                "fraksi": (round(float((np.array(v) < args.pita).mean()), 4) if v else None),
            } for k, v in per_kelas_salah.items()
        },
        "pasangan_bingung": dict(bingung.most_common(8)),
        "gerbang": {
            "ambang_fraksi_dalam_pita": AMBANG_LOLOS,
            "terukur": frak,
            "putusan": "LOLOS" if lolos else "GUGUR",
            "arti": ("K2 boleh dilanjutkan: cukup galat kelas berada di pita yang "
                     "dapat dibalik residu ber-clip"
                     if lolos else
                     "K2 gugur: potensi naiknya tertutup secara matematis"),
        },
    }
    print(json.dumps(lap, indent=2, ensure_ascii=False))
    keluaran = Path(args.keluaran)
    keluaran.parent.mkdir(parents=True, exist_ok=True)
    keluaran.write_text(json.dumps(lap, indent=2, ensure_ascii=False))
    print(f"\n-> {keluaran}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
