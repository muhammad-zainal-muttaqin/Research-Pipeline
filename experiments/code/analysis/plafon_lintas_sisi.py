#!/usr/bin/env python3
"""F-003 (P3) — Plafon keras distilasi lintas-sisi.

Gerbang untuk K3 (konsistensi query lintas-sisi). Pertanyaannya satu kalimat:

    Dari kemunculan tandan yang diprediksi SALAH, berapa fraksi yang punya
    kemunculan BENAR pada sisi lain dari tandan fisik yang sama?

Itu plafon keras. K3 bekerja dengan memindahkan keyakinan dari sisi yang benar
ke sisi yang salah lewat graf `_confirmedLinks`. Bila mayoritas galat salah di
SEMUA sisi, tidak ada yang bisa ditransfer, dan K3 gugur tanpa perlu dilatih.

## Kenapa ini tidak bisa dihitung dari E-028

`experiments/results/E-028/konsistensi_sawitmvc_rgb_seed42.json` hanya
menyimpan laju agregat (`laju_inkonsisten`, `per_kelas_gt_*`,
`pasangan_kelas_bertabrakan`) — tidak ada satu pun prediksi per-sisi. Diperiksa
langsung 6 Agustus 2026. Karena itu `cross_side_consistency.py` diberi flag
`--dump-tandan`, dan berkas ini membaca hasilnya.

## KAVEAT YANG WAJIB IKUT DILAPORKAN

Bobot yang tersedia untuk uji ini adalah **yolo26n**
(`runs_e022/yolo26n_sawitmvc_rgb_seed42`), bukan RF-DETR-L. Bobot RF-DETR-L
E-021 hilang saat pod di-terminate. Angka di sini karena itu menjawab
**"apakah ada ruang secara struktural"**, BUKAN "berapa besar ruangnya pada
model final". Detektor yang lebih kuat menggeser plafon ke dua arah sekaligus:
lebih sedikit galat (pembilang turun) tetapi juga lebih sedikit sisi terlewat
(penyebut naik). P3 definitif diulang setelah F-004.

## Yang memalsukan (ditulis sebelum melihat hasil)

K3 GUGUR bila fraksi galat-yang-dapat-diselamatkan < **0,30** — artinya
mayoritas galat salah di semua sisi dan graf identitas tidak punya informasi
untuk ditransfer.

Pemakaian:
  python analysis/cross_side_consistency.py --bobot ... --dump-tandan dump.json
  python analysis/plafon_lintas_sisi.py --dump dump.json
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"

KELAS = ["B1", "B2", "B3", "B4"]
AMBANG_LOLOS = 0.30


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="keluaran --dump-tandan")
    ap.add_argument("--keluaran", default=str(
        EVIDENCE_ROOT / "results" / "F-003" / "plafon_lintas_sisi.json"))
    args = ap.parse_args()

    d = json.loads(Path(args.dump).read_text())
    tandan = d["tandan"]

    n_tandan = 0
    n_kemunculan = 0
    n_terlewat = 0
    n_benar = 0
    n_salah = 0
    n_salah_dapat_diselamatkan = 0        # ada >=1 sisi BENAR pada tandan yang sama
    n_salah_semua_sisi = 0                # tidak ada sisi benar sama sekali
    n_terlewat_dapat_diselamatkan = 0     # sisi terlewat, tapi sisi lain benar

    per_kelas_salah = Counter()
    per_kelas_selamat = Counter()
    # Sebaran: berapa banyak sisi benar yang dimiliki tandan yang punya galat
    sebaran_pendukung = Counter()
    # Tandan yang seluruhnya tidak terdeteksi tidak boleh dihitung sebagai
    # "galat tak terselamatkan" -- itu kegagalan DETEKSI, bukan kelas.
    n_tandan_tanpa_deteksi = 0

    for b in tandan:
        gt = b["gt"]
        app = b["kemunculan"]
        n_tandan += 1
        n_kemunculan += len(app)

        pred = [a["prediksi"] for a in app]
        benar = [p for p in pred if p is not None and p == gt]
        salah = [p for p in pred if p is not None and p != gt]
        lewat = [p for p in pred if p is None]

        n_benar += len(benar)
        n_salah += len(salah)
        n_terlewat += len(lewat)

        if not any(p is not None for p in pred):
            n_tandan_tanpa_deteksi += 1
            continue

        if salah:
            sebaran_pendukung[len(benar)] += 1
            for p in salah:
                per_kelas_salah[gt] += 1
                if benar:
                    n_salah_dapat_diselamatkan += 1
                    per_kelas_selamat[gt] += 1
                else:
                    n_salah_semua_sisi += 1
        if lewat and benar:
            n_terlewat_dapat_diselamatkan += len(lewat)

    frak = (round(n_salah_dapat_diselamatkan / n_salah, 4) if n_salah else None)
    lolos = frak is not None and frak >= AMBANG_LOLOS

    def ci95(k: int, n: int, seed: int = 42):
        """CI95 bootstrap untuk sebuah proporsi.

        Tanpa ini, membandingkan titik estimasi dengan ambang memberi kesan
        presisi yang tidak dimiliki datanya -- kesalahan yang sama seperti
        mengutip satu seed sebagai temuan (E-027, E-033b).
        """
        if not n:
            return None
        import numpy as np
        rng = np.random.default_rng(seed)
        b = rng.binomial(n, k / n, 200000) / n
        lo, hi = np.percentile(b, [2.5, 97.5])
        return [round(float(lo), 4), round(float(hi), 4)]

    ci_kelas = ci95(n_salah_dapat_diselamatkan, n_salah)
    ci_hadir = ci95(n_terlewat_dapat_diselamatkan, n_terlewat)
    ambang_terpisah = ci_kelas is not None and not (ci_kelas[0] <= AMBANG_LOLOS <= ci_kelas[1])

    lap = {
        "eksperimen": "F-003",
        "pertanyaan": "dari kemunculan yang SALAH kelas, berapa yang punya kemunculan BENAR di sisi lain?",
        "sumber_dump": str(args.dump),
        "bobot": d["meta"]["bobot"],
        "PROKSI": "yolo26n, BUKAN RF-DETR-L. Menjawab 'ada ruang?', bukan 'berapa besar ruangnya'.",
        "split": d["meta"]["split"],
        "conf": d["meta"]["conf"],
        "iou_cocok": d["meta"]["iou_cocok"],
        "n_tandan_multi_sisi": n_tandan,
        "n_tandan_tanpa_deteksi_sama_sekali": n_tandan_tanpa_deteksi,
        "n_kemunculan": n_kemunculan,
        "n_kemunculan_benar": n_benar,
        "n_kemunculan_salah": n_salah,
        "n_kemunculan_terlewat": n_terlewat,
        "plafon_kelas": {
            "n_salah_dapat_diselamatkan": n_salah_dapat_diselamatkan,
            "n_salah_semua_sisi": n_salah_semua_sisi,
            "fraksi_dapat_diselamatkan": frak,
            "ci95": ci_kelas,
        },
        "plafon_deteksi_terlewat": {
            "n_terlewat_dapat_diselamatkan": n_terlewat_dapat_diselamatkan,
            "fraksi": (round(n_terlewat_dapat_diselamatkan / n_terlewat, 4)
                       if n_terlewat else None),
            "ci95": ci_hadir,
            "catatan": "K3 punya suku konsistensi KEHADIRAN; ini plafonnya, terpisah dari plafon kelas",
        },
        "per_kelas_gt": {
            k: {
                "n_salah": per_kelas_salah.get(k, 0),
                "n_dapat_diselamatkan": per_kelas_selamat.get(k, 0),
                "fraksi": (round(per_kelas_selamat.get(k, 0) / per_kelas_salah[k], 4)
                           if per_kelas_salah.get(k) else None),
            } for k in KELAS
        },
        "sebaran_sisi_benar_pada_tandan_bergalat": dict(sorted(sebaran_pendukung.items())),
        "gerbang": {
            "ambang_fraksi_dapat_diselamatkan": AMBANG_LOLOS,
            "terukur": frak,
            "ci95": ci_kelas,
            "ambang_di_luar_ci": ambang_terpisah,
            "putusan": "LOLOS" if lolos else "GUGUR",
            "arti": ("K3 boleh dilanjutkan: ada galat yang punya pasangan benar di sisi lain"
                     if lolos else
                     "K3 gugur: mayoritas galat salah di semua sisi, tidak ada yang bisa ditransfer"),
            "kualifikasi": (
                "Titik estimasi di bawah ambang, TETAPI CI95 memuat ambang: data ini "
                "tidak dapat memisahkan keduanya. Aturan pra-daftar tetap mengikat "
                "(putusan GUGUR), namun bukti pemalsuannya LEMAH, bukan tegas."
                if (not lolos and not ambang_terpisah) else
                "Titik estimasi dan CI95 sepakat terhadap ambang."
            ),
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
