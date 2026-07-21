"""Tahap 2: pengklasifikasi kematangan pada potongan resolusi asli.

Keputusan desain yang berasal dari data, bukan dari resep bawaan:

1. AUGMENTASI AMAN-WARNA. Baseline YOLO memakai hsv_s=0.7, hsv_v=0.4 —
   saturasi diacak sampai +-70%. Kematangan sawit ADALAH warna (B1 gelap
   kehijauan -> B4 jingga-merah), jadi resep itu mengacak justru bukti yang
   harus dipelajari. Di sini: geometri diacak bebas, warna nyaris tidak.
2. TANPA BOBOT KELAS. mAP menilai tiap kelas lewat peringkat skornya, jadi
   kalibrasi lebih berharga daripada akurasi argmax yang dipaksa seimbang.
3. KELUARAN DISIMPAN SEBAGAI PROBABILITAS PENUH, bukan argmax — tahap
   penggabungan butuh skor untuk menghitung AP.
"""
import argparse, json, time
from pathlib import Path
import torch, torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms as T, models

NAMES = ["B1", "B2", "B3", "B4"]


def loaders(root, size, batch, workers=8):
    tr = T.Compose([
        T.RandomResizedCrop(size, scale=(0.65, 1.0), ratio=(0.8, 1.25)),
        T.RandomHorizontalFlip(), T.RandomVerticalFlip(),
        T.RandomApply([T.RandomRotation(20)], p=0.5),
        # hanya kecerahan ringan (cuaca/naungan); saturasi & hue DIBIARKAN
        T.ColorJitter(brightness=0.18, contrast=0.12, saturation=0.04, hue=0.012),
        T.ToTensor(),
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    ev = T.Compose([
        T.Resize(int(size * 1.14)), T.CenterCrop(size), T.ToTensor(),
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    d = {}
    for sp, tf, sh in [("train", tr, True), ("val", ev, False), ("test", ev, False)]:
        ds = datasets.ImageFolder(f"{root}/{sp}", tf)
        assert ds.classes == NAMES, ds.classes
        d[sp] = DataLoader(ds, batch_size=batch, shuffle=sh, num_workers=workers,
                           pin_memory=True, drop_last=sh, persistent_workers=True)
    return d


@torch.no_grad()
def evaluate(model, dl, dev):
    model.eval()
    P, Y = [], []
    for x, y in dl:
        with torch.autocast("cuda", torch.bfloat16):
            o = model(x.to(dev, non_blocking=True))
        P.append(o.float().softmax(1).cpu()); Y.append(y)
    P, Y = torch.cat(P), torch.cat(Y)
    pred = P.argmax(1)
    acc = (pred == Y).float().mean().item()
    pm1 = (pred - Y).abs().le(1).float().mean().item()
    cm = torch.zeros(4, 4, dtype=torch.long)
    for t, p in zip(Y, pred):
        cm[t, p] += 1
    per = {NAMES[i]: round((cm[i, i] / max(1, cm[i].sum())).item(), 4) for i in range(4)}
    return acc, pm1, per, cm, P, Y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="crops")
    ap.add_argument("--size", type=int, default=224)
    ap.add_argument("--batch", type=int, default=48)
    ap.add_argument("--epochs", type=int, default=18)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--out", default="runs/maturity")
    a = ap.parse_args()

    dev = "cuda"
    dl = loaders(a.root, a.size, a.batch)
    model = models.convnext_tiny(weights=models.ConvNeXt_Tiny_Weights.IMAGENET1K_V1)
    model.classifier[2] = nn.Linear(768, 4)
    model.to(dev).to(memory_format=torch.channels_last)

    opt = torch.optim.AdamW(model.parameters(), lr=a.lr, weight_decay=0.05)
    sched = torch.optim.lr_scheduler.OneCycleLR(
        opt, a.lr, epochs=a.epochs, steps_per_epoch=len(dl["train"]), pct_start=0.25)
    lossf = nn.CrossEntropyLoss(label_smoothing=0.05)

    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    best = 0.0
    for ep in range(1, a.epochs + 1):
        model.train(); t0 = time.time(); tot = 0.0
        for x, y in dl["train"]:
            x = x.to(dev, non_blocking=True).to(memory_format=torch.channels_last)
            y = y.to(dev, non_blocking=True)
            with torch.autocast("cuda", torch.bfloat16):
                loss = lossf(model(x), y)
            opt.zero_grad(set_to_none=True); loss.backward(); opt.step(); sched.step()
            tot += loss.item()
        acc, pm1, per, cm, _, _ = evaluate(model, dl["val"], dev)
        flag = ""
        if acc > best:
            best = acc; torch.save(model.state_dict(), out / "best.pt"); flag = " *"
        print(f"ep{ep:02d} loss={tot/len(dl['train']):.3f} val_acc={acc:.4f} "
              f"pm1={pm1:.4f} {per} {time.time()-t0:.0f}s{flag}", flush=True)

    model.load_state_dict(torch.load(out / "best.pt"))
    res = {"val_acc_terbaik": round(best, 4)}
    for sp in ["val", "test"]:
        acc, pm1, per, cm, _, _ = evaluate(model, dl[sp], dev)
        res[sp] = {"acc": round(acc, 4), "acc_pm1": round(pm1, 4),
                   "recall_per_kelas": per, "confusion": cm.tolist()}
    print(json.dumps(res, indent=1))
    json.dump(res, open(out / "hasil.json", "w"), indent=1)


if __name__ == "__main__":
    main()
