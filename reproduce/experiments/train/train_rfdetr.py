"""E-021 — RF-DETR sebagai pembanding transformer NMS-free.

Hipotesis: RF-DETR-L (backbone DINOv2 + arsitektur hasil NAS) layak menjadi
pembanding bila pada split val identik ia melampaui YOLO26m 640
(0.5218/0.2407 mAP50/mAP50-95) dan mendekati atau melampaui RT-DETR-L 1280
(0.5466/0.2543), tanpa memilih konfigurasi dari test.

Hipotesis dipalsukan bila run konvergen tertinggal dari YOLO26m pada kedua
metrik. Test hanya dievaluasi setelah checkpoint terbaik dipilih dari val.
Tahap pertama sengaja memakai resolusi native RF-DETR-L (704) agar menguji
checkpoint sebagaimana dirancang dan tetap muat pada NVIDIA L4; run 1280 hanya
layak dilakukan bila tahap ini memberi sinyal positif.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from rfdetr import RFDETRLarge


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="rfdetr_ds")
    ap.add_argument("--output", default="runs/rfdetr_l_e30_r704")
    ap.add_argument("--epochs", type=int, default=30)
    ap.add_argument("--resolution", type=int, default=704)
    ap.add_argument("--batch", type=int, default=2)
    ap.add_argument("--grad-accum", type=int, default=8)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--resume", default=None,
                    help="Path ckpt PTL (mis. last.ckpt) untuk melanjutkan tanpa mengulang.")
    # Seri F butuh 3 seed berpasangan (F-004). Bawaannya 42 = seed yang dipakai
    # E-021, jadi menambah flag ini TIDAK mengubah reproduksi E-021.
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()

    if args.smoke:
        args.epochs = 1
        # `--output` eksplisit dihormati supaya probe VRAM F-001 bisa menulis ke
        # runs/ akar repo (yang di-gitignore) alih-alih mengotori snapshot kode.
        if args.output == ap.get_default("output"):
            args.output = "runs/rfdetr_l_smoke"

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    model = RFDETRLarge(gradient_checkpointing=True, resolution=args.resolution)
    model.train(
        dataset_dir=args.dataset,
        output_dir=str(output),
        epochs=args.epochs,
        batch_size=args.batch,
        grad_accum_steps=args.grad_accum,
        num_workers=args.workers,
        resume=args.resume,
        resolution=args.resolution,
        device="cuda",
        seed=args.seed,
        early_stopping=not args.smoke,
        early_stopping_patience=8,
        early_stopping_min_delta=0.001,
        # Fairness vs RT-DETR@1280: default rf-detr (multi_scale=True + expanded_scales)
        # mengunci ke skala TERBESAR (1280*45/40 = 1440), memberi keunggulan resolusi
        # tak adil. Dimatikan agar training benar-benar di resolusi 1280.
        multi_scale=False,
        expanded_scales=False,
        run_test=True,  # trainer.test() pada checkpoint terbaik -> kolom test/* di metrics.csv
    )

    # rfdetr 1.8.x tidak punya .evaluate(); val dicatat tiap epoch dan test dievaluasi
    # oleh run_test=True. Angka bersih dibaca dari metrics.csv (bukan ekor log).
    result = collect_metrics(output / "metrics.csv", vars(args))
    result_path = output / "evaluation.json"
    result_path.write_text(json.dumps(result, indent=2, default=float))
    print(f"Hasil evaluasi: {result_path}")
    v, t = result.get("val", {}), result.get("test", {})
    print(f"VAL  mAP50={v.get('mAP50')}  mAP50-95={v.get('mAP50_95')}")
    print(f"TEST mAP50={t.get('mAP50')}  mAP50-95={t.get('mAP50_95')}")


def collect_metrics(csv_path: Path, config: dict) -> dict:
    """Ekstrak val (epoch terbaik) dan test dari metrics.csv rf-detr.

    Checkpoint terbaik dipilih oleh val/ema_mAP_50_95 (default RFDETRLarge memakai
    EMA). Kelas: B1..B4. Test dilaporkan terpisah; konfigurasi tidak dipilih darinya.
    """
    import csv

    names = ["B1", "B2", "B3", "B4"]
    rows = list(csv.DictReader(csv_path.open()))

    def fnum(row: dict, key: str):
        raw = row.get(key, "")
        return float(raw) if raw not in ("", None) else None

    # Baris val = punya val/mAP_50_95 terisi; pilih epoch dengan EMA mAP tertinggi.
    val_rows = [r for r in rows if fnum(r, "val/mAP_50_95") is not None]
    result: dict = {"config": config}
    if val_rows:
        def key(r):
            return fnum(r, "val/ema_mAP_50_95") or fnum(r, "val/mAP_50_95") or -1.0
        best = max(val_rows, key=key)
        result["best_epoch"] = fnum(best, "epoch")
        result["val"] = {
            "mAP50": fnum(best, "val/mAP_50"),
            "mAP50_95": fnum(best, "val/mAP_50_95"),
            "ema_mAP50": fnum(best, "val/ema_mAP_50"),
            "ema_mAP50_95": fnum(best, "val/ema_mAP_50_95"),
            "precision": fnum(best, "val/precision"),
            "recall": fnum(best, "val/recall"),
            "per_kelas_AP": {n: fnum(best, f"val/AP/{n}") for n in names},
        }
    # Baris test (run_test=True) = punya test/mAP_50_95 terisi.
    test_rows = [r for r in rows if fnum(r, "test/mAP_50_95") is not None]
    if test_rows:
        t = test_rows[-1]
        result["test"] = {
            "mAP50": fnum(t, "test/mAP_50"),
            "mAP50_95": fnum(t, "test/mAP_50_95"),
            "precision": fnum(t, "test/precision"),
            "recall": fnum(t, "test/recall"),
            "per_kelas_AP": {n: fnum(t, f"test/AP/{n}") for n in names},
        }
    return result


if __name__ == "__main__":
    main()
