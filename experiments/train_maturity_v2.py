"""Pengklasifikasi kematangan v2 — dua koreksi yang berasal dari hasil v1.

v1 runtuh ke kelas mayoritas: B3 mengisi 52% potongan latih (7.333/14.040), dan
model membayar lebih murah dengan menebak B3 (recall B3 0,95 vs B2 0,23).
Untuk mAP hal ini merugikan: AP dihitung per kelas dari PERINGKAT skor, dan
peluang kelas minoritas yang tergencet prior membuat peringkatnya kacau.

Koreksi:
  1. PENCUPLIKAN BERIMBANG (WeightedRandomSampler) — tiap kelas muncul sama
     sering per epoch, sehingga model belajar batas antar kelas, bukan prior.
  2. POTONGAN RESOLUSI MASTER (opsional --root crops_raw) — pada SawitMVC
     potongan 224 px adalah hasil pembesaran; pada master 3024x4032 ia berisi
     detail permukaan buah yang sebenarnya.

Augmentasi tetap aman-warna: kematangan ADALAH warna.
"""
import argparse, json, time
from collections import Counter
from pathlib import Path
import torch, torch.nn as nn
from torch.utils.data import DataLoader, WeightedRandomSampler
from torchvision import datasets, transforms as T, models

NAMES = ["B1", "B2", "B3", "B4"]


def build(root, size, batch, workers=8, balanced=True):
    tr = T.Compose([
        T.RandomResizedCrop(size, scale=(0.65, 1.0), ratio=(0.8, 1.25)),
        T.RandomHorizontalFlip(), T.RandomVerticalFlip(),
        T.RandomApply([T.RandomRotation(20)], p=0.5),
        T.ColorJitter(brightness=0.18, contrast=0.12, saturation=0.04, hue=0.012),
        T.ToTensor(), T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    ev = T.Compose([T.Resize(int(size * 1.14)), T.CenterCrop(size), T.ToTensor(),
                    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    out = {}
    ds = datasets.ImageFolder(f"{root}/train", tr)
    assert ds.classes == NAMES, ds.classes
    if balanced:
        cnt = Counter(ds.targets)
        w = [1.0 / cnt[t] for t in ds.targets]
        smp = WeightedRandomSampler(w, num_samples=len(ds), replacement=True)
        out["train"] = DataLoader(ds, batch_size=batch, sampler=smp, num_workers=workers,
                                  pin_memory=True, drop_last=True, persistent_workers=True)
    else:
        out["train"] = DataLoader(ds, batch_size=batch, shuffle=True, num_workers=workers,
                                  pin_memory=True, drop_last=True, persistent_workers=True)
    for sp in ["val", "test"]:
        d = datasets.ImageFolder(f"{root}/{sp}", ev)
        out[sp] = DataLoader(d, batch_size=batch, shuffle=False, num_workers=workers,
                             pin_memory=True, persistent_workers=True)
    return out


@torch.no_grad()
def evaluate(model, dl, dev):
    model.eval(); P, Y = [], []
    for x, y in dl:
        with torch.autocast("cuda", torch.bfloat16):
            o = model(x.to(dev, non_blocking=True))
        P.append(o.float().softmax(1).cpu()); Y.append(y)
    P, Y = torch.cat(P), torch.cat(Y)
    pred = P.argmax(1)
    cm = torch.zeros(4, 4, dtype=torch.long)
    for t, p in zip(Y, pred):
        cm[t, p] += 1
    rec = {NAMES[i]: round((cm[i, i] / max(1, cm[i].sum())).item(), 4) for i in range(4)}
    # rerata recall seimbang: ukuran yang tidak bisa dicurangi dengan menebak B3
    bal = sum(rec.values()) / 4
    return {"acc": (pred == Y).float().mean().item(),
            "bal_acc": bal, "pm1": (pred - Y).abs().le(1).float().mean().item(),
            "recall": rec, "cm": cm.tolist()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="crops")
    ap.add_argument("--size", type=int, default=224)
    ap.add_argument("--batch", type=int, default=48)
    ap.add_argument("--epochs", type=int, default=22)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--out", default="runs/maturity_v2")
    ap.add_argument("--no-balance", action="store_true")
    a = ap.parse_args()

    dev = "cuda"
    dl = build(a.root, a.size, a.batch, balanced=not a.no_balance)
    model = models.convnext_tiny(weights=models.ConvNeXt_Tiny_Weights.IMAGENET1K_V1)
    model.classifier[2] = nn.Linear(768, 4)
    model.to(dev).to(memory_format=torch.channels_last)
    opt = torch.optim.AdamW(model.parameters(), lr=a.lr, weight_decay=0.05)
    sched = torch.optim.lr_scheduler.OneCycleLR(
        opt, a.lr, epochs=a.epochs, steps_per_epoch=len(dl["train"]), pct_start=0.2)
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
        m = evaluate(model, dl["val"], dev)
        flag = ""
        if m["bal_acc"] > best:
            best = m["bal_acc"]; torch.save(model.state_dict(), out / "best.pt"); flag = " *"
        print(f"ep{ep:02d} loss={tot/len(dl['train']):.3f} acc={m['acc']:.4f} "
              f"bal={m['bal_acc']:.4f} pm1={m['pm1']:.4f} {m['recall']} "
              f"{time.time()-t0:.0f}s{flag}", flush=True)

    model.load_state_dict(torch.load(out / "best.pt"))
    res = {"root": a.root, "bal_acc_terbaik": round(best, 4)}
    for sp in ["val", "test"]:
        m = evaluate(model, dl[sp], dev)
        res[sp] = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in m.items()}
    print(json.dumps(res, indent=1))
    json.dump(res, open(out / "hasil.json", "w"), indent=1)


if __name__ == "__main__":
    main()
