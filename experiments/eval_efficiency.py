"""#3 Tabel efisiensi E-021 — parameter, GFLOPs, latensi/FPS (L4), ukuran bobot.

Untuk keputusan deployment: "worth it-kah RF-DETR yang lebih berat?". Latensi
diukur langsung di GPU (NVIDIA L4) — 10 warmup + 50 ukur pada 1 citra test,
pada resolusi latihan masing-masing. Hasil -> results/efficiency.json.
"""
import json
import time
from pathlib import Path

import torch

from eval_all_pycoco import build_gt, load, MODELS

WEIGHT_FILE = {
    "YOLO26m": "runs/rgb_e60_i640_s42/weights/best.pt",
    "YOLO26l": "runs/yolo26l_e60_i1280/weights/best.pt",
    "RT-DETR-L": "runs/rtdetr_l_e60_i1280/weights/best.pt",
    "RF-DETR-L": "runs/rfdetr_l_e60_i1280/checkpoint_best_ema.pth",
}


def n_params(model, kind):
    mods = []
    if kind in ("yolo", "rtdetr"):
        mods = [model.model]
    else:
        for a in ("model",):
            o = getattr(model, a, None)
            if isinstance(o, torch.nn.Module):
                mods = [o]; break
            for a2 in ("model", "module", "net"):
                o2 = getattr(o, a2, None)
                if isinstance(o2, torch.nn.Module):
                    mods = [o2]; break
    if not mods:
        return None
    return sum(p.numel() for p in mods[0].parameters())


def gflops_ultra(model, imgsz):
    try:
        from ultralytics.utils.torch_utils import get_flops
        return round(get_flops(model.model, imgsz), 1)
    except Exception:
        try:
            info = model.info(detailed=False, verbose=False)
            return round(info[3], 1) if info and len(info) >= 4 else None
        except Exception:
            return None


def latency(model, kind, img, imgsz, warm=10, runs=50):
    def once():
        if kind == "rfdetr":
            model.predict(img, threshold=0.5)
        else:
            model.predict(img, imgsz=imgsz, verbose=False)
    for _ in range(warm):
        once()
    torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(runs):
        once()
    torch.cuda.synchronize()
    ms = (time.perf_counter() - t0) / runs * 1000
    return round(ms, 2), round(1000 / ms, 1)


def main():
    _, paths = build_gt("test")
    img = str(paths[0])
    out = {}
    for key, kind, weights, imgsz, params in MODELS:
        if not Path(weights).exists():
            print(f"SKIP {key}"); continue
        print(f"\n== {key} ==")
        model = load(kind, weights, imgsz)
        npar = n_params(model, kind)
        gflops = gflops_ultra(model, imgsz) if kind in ("yolo", "rtdetr") else None
        wf = WEIGHT_FILE.get(key)
        wmb = round(Path(wf).stat().st_size / 1e6, 1) if wf and Path(wf).exists() else None
        ms, fps = latency(model, kind, img, imgsz)
        out[key] = {"params_juta": round(npar / 1e6, 2) if npar else params,
                    "GFLOPs": gflops, "imgsz": imgsz,
                    "bobot_MB": wmb, "latensi_ms_L4": ms, "FPS_L4": fps}
        print(f"  param={out[key]['params_juta']}jt GFLOPs={gflops} "
              f"bobot={wmb}MB latensi={ms}ms FPS={fps} @L4 (imgsz {imgsz})")
        del model
        torch.cuda.empty_cache()
    Path("results").mkdir(exist_ok=True)
    json.dump(out, open("results/efficiency.json", "w"), indent=2)
    print("\n-> results/efficiency.json")
    print("\nCatatan: GFLOPs RF-DETR = n/a (forward butuh NestedTensor; latensi &"
          " param tetap terukur). GFLOPs ultralytics dihitung pada imgsz masing-masing.")


if __name__ == "__main__":
    main()
