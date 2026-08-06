#!/usr/bin/env python3
"""F-006 (K2) — Kepala ordinal kumulatif CORN berpenjaga-peringkat untuk RF-DETR-L.

MENUNGGU GERBANG F-005. Berkas ini ditulis lebih dulu karena menulis kode tidak
memakai GPU dan K2 adalah tambalan paling berisiko di seri ini (menyentuh
`LWDETR.forward` DAN `SetCriterion`). Bila F-005 memalsukan K2, yang terbuang
hanya waktu tulis, bukan jam GPU.

## Jalur skor yang ditempeli — dibaca dari kode, bukan diasumsikan

RF-DETR memakai **IA-BCE** (`criterion.py:268-296`), bukan softmax CE. Skor
deteksi = `sigmoid(z[q,c])` per kelas INDEPENDEN, top-k `num_select=300` atas
grid datar Q x C (`postprocess.py:106`). Konsekuensinya:

  1. Tidak ada simpleks softmax. Residu ordinal harus berupa **offset logit
     aditif ber-mean nol antar 4 kelas** -- bukan pergeseran pada simpleks.
  2. Kepala mengeluarkan **5** logit; kanal indeks 4 mati (lihat SERI-F.md §5.2).
     Residu hanya disuntikkan ke kanal 0..3 (B1..B4).
  3. mAP COCO dihitung per kelas, jadi yang dapat digerakkan residu ber-mean nol
     adalah selisih logit antar kelas DI DALAM query yang sama. Itulah yang
     diukur F-005 sebagai gerbang.

## Konstruksi CORN

q1 = P(y>B1), q2 = P(y>B2 | y>B1), q3 = P(y>B3 | y>B2), lalu

    pi1 = 1-q1,  pi2 = q1(1-q2),  pi3 = q1 q2 (1-q3),  pi4 = q1 q2 q3

Sumbu ordinalnya nyata dan arahnya penting: **B1 = MATANG ... B4 = MENTAH**
(CLAUDE.md §"Arah kelas — jangan dibalik").

Residu: `r = log(pi)`, dipusatkan (mean nol antar 4 kelas), di-gate `alpha`
(NOL saat init), lalu **di-clip ke +-eps**. Urutan itu penting: clip di akhir
memberi jaminan penjaga-peringkat yang sesungguhnya, yaitu urutan hanya dapat
berubah bila selisih logit < 2*eps.

**Gate SKALAR, bukan per kelas.** Rancangan menulis `alpha_c`, menyiratkan per
kelas. Gate per kelas MERUSAK pemusatan, dan pemusatan itulah yang menjamin
residu tidak menggeser objectness keseluruhan (sehingga tidak mengubah deteksi
mana yang lolos top-k). Satu skalar juga bisa dilaporkan apa adanya setelah
latihan sebagai bukti "kepala ordinal terpakai".

## Kenapa suku CORN dilipat ke `loss_ce`, bukan jadi kunci loss sendiri

`weight_dict` dibangun saat konstruksi (`lwdetr.py:836-855`) lalu disalin ke
seluruh lapisan aux dengan sufiks `_0`, `_1`, ..., `_enc`. Menyisipkan kunci baru
pasca-konstruksi menuntut menebak sufiks mana yang dipakai di versi ini --
persis jenis kegagalan senyap yang sudah beberapa kali menjatuhkan hasil di repo
ini. Melipatnya ke `loss_ce` membuatnya PASTI masuk gradien tanpa plumbing.
Nilai mentahnya tetap dicatat di `_LOG` untuk diagnosis.

Suku CORN dan suku peringkat hanya dihitung pada **lapisan decoder terakhir**
(dikenali dari adanya kunci `aux_outputs`), bukan tiap lapisan aux: yang
disupervisi adalah kepala ordinal itu sendiri, bukan tiap tingkat penyempurnaan.

## Dua lengan suku peringkat

  pasangan   pasangan logistik pada pasangan SULIT (selisih < 2*eps)
  brs        Bucketed Rank & Sort, surogat AP ber-bucket

**Kejujuran sumber:** BRS di sini adalah implementasi dari MEKANISME yang
diuraikan laporan deep research, bukan salinan algoritma terpublikasi yang
terverifikasi. Sitasi kedua laporan belum dapat di-resolve (SERI-F.md §2), jadi
lengan ini TIDAK BOLEH dilaporkan sebagai "Bucketed Rank & Sort dari makalah X"
sampai rujukannya diverifikasi.

Pemakaian:
  python train/train_rfdetr_ordinal.py --uji-sambungan
  python train/train_rfdetr_ordinal.py --peringkat pasangan --seed 42 --output <dir>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"

# `python train/xxx.py` menaruh `train/` di sys.path[0], BUKAN akar
# `reproduce/experiments/`, sehingga `from train.train_rfdetr import ...` gagal
# dengan ModuleNotFoundError. Kegagalan itu terjadi SETELAH latihan selesai
# (saat mengumpulkan metrik), jadi ia membuang seluruh run tanpa menyentuh
# bobotnya — terjadi 6 Agustus 2026 pada F-007 dwt seed 42, 1,5 jam GPU.
# Pola sisipan ini sama dengan `analysis/cross_side_consistency.py:52`.
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import torch
import torch.nn as nn
import torch.nn.functional as F

N_KELAS = 4          # B1..B4; kanal ke-5 kepala RF-DETR mati (SERI-F.md §5.2)
EPS = 0.3
PERINGKAT = ["pasangan", "brs", "tanpa"]

_KEPALA: "KepalaOrdinal | None" = None
_LOG: dict = {}


class KepalaOrdinal(nn.Module):
    """Bungkus `class_embed`: logit nominal + residu ordinal CORN ber-clip.

    Membungkus `class_embed` (bukan menambal `LWDETR.forward`) membuat residu
    otomatis ikut ke SELURUH konsumen `pred_logits` -- matcher Hungarian,
    kriteria, dan postprocess -- sehingga latihan dan inferensi melihat jalur
    skor yang sama. Tidak ada tempat yang bisa lupa diperbarui.
    """

    def __init__(self, class_embed: nn.Module, hidden_dim: int, eps: float = EPS):
        super().__init__()
        self.class_embed = class_embed
        self.ordinal = nn.Linear(hidden_dim, N_KELAS - 1)
        nn.init.zeros_(self.ordinal.bias)
        nn.init.normal_(self.ordinal.weight, std=0.01)
        # alpha = 0 -> residu NOL -> identik baseline saat inisialisasi.
        self.alpha = nn.Parameter(torch.zeros(1))
        self.eps = eps
        self.q_logit_terakhir: torch.Tensor | None = None

    def forward(self, hs: torch.Tensor) -> torch.Tensor:
        z = self.class_embed(hs)                       # (..., C) dengan C = 5
        q_logit = self.ordinal(hs)                     # (..., 3)
        self.q_logit_terakhir = q_logit[-1] if q_logit.dim() == 4 else q_logit

        q = torch.sigmoid(q_logit).clamp(1e-4, 1 - 1e-4)
        q1, q2, q3 = q[..., 0], q[..., 1], q[..., 2]
        pi = torch.stack([1 - q1, q1 * (1 - q2), q1 * q2 * (1 - q3), q1 * q2 * q3], dim=-1)

        r = torch.log(pi.clamp_min(1e-6))
        r = r - r.mean(dim=-1, keepdim=True)           # terpusat: mean nol
        r = self.alpha * r                             # di-gate
        r = r.clamp(-self.eps, self.eps)               # di-CLIP -> penjaga peringkat

        z = z.clone()
        z[..., :N_KELAS] = z[..., :N_KELAS] + r.to(z.dtype)
        return z


def corn_loss(q_logit: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Loss CORN kondisional pada query yang tercocokkan.

    q1 disupervisi seluruh sampel; q2 hanya pada y>0; q3 hanya pada y>1. Itulah
    yang membedakan CORN dari CORAL: rantai kondisionalnya membuat pi selalu
    membentuk distribusi yang sah tanpa kendala monotonisitas terpisah.
    """
    total = q_logit.new_zeros(())
    n = 0
    masker = torch.ones_like(y, dtype=torch.bool)
    for k in range(N_KELAS - 1):
        if masker.sum() == 0:
            break
        target = (y[masker] > k).float()
        total = total + F.binary_cross_entropy_with_logits(
            q_logit[masker, k], target, reduction="sum")
        n += int(masker.sum())
        masker = masker & (y > k)
    return total / max(n, 1)


def peringkat_pasangan(z: torch.Tensor, y: torch.Tensor, eps: float) -> torch.Tensor:
    """Pasangan logistik pada pasangan SULIT saja.

    Pasangan sulit = selisih logit kelas-benar vs kelas-salah-tertinggi berada di
    dalam pita 2*eps, yaitu satu-satunya wilayah yang residu ber-clip mampu
    balikkan. Menghukum pasangan yang sudah terpisah jauh membuang gradien pada
    kasus yang toh tidak akan berubah.
    """
    if z.numel() == 0:
        return z.new_zeros(())
    z4 = z[:, :N_KELAS]
    benar = z4.gather(1, y.view(-1, 1)).squeeze(1)
    lain = z4.clone()
    lain.scatter_(1, y.view(-1, 1), float("-inf"))
    salah = lain.max(dim=1).values
    selisih = benar - salah
    sulit = selisih.abs() < 2 * eps
    if sulit.sum() == 0:
        return z.new_zeros(())
    return F.softplus(-selisih[sulit]).mean()


def peringkat_brs(z: torch.Tensor, y: torch.Tensor, n_bucket: int = 16) -> torch.Tensor:
    """Surogat peringkat ber-bucket (pembacaan atas mekanisme BRS).

    Skor di-bucket, lalu tiap positif dihukum menurut massa negatif yang berada
    di bucket LEBIH TINGGI daripada dirinya -- pendekatan diskret atas "berapa
    banyak negatif mendahului positif ini", yang merupakan inti kerugian AP.
    Bucketing menurunkan ongkos dari O(PN) menjadi O(N log N + P^2).

    BUKAN salinan algoritma terpublikasi yang terverifikasi -- lihat catatan
    kejujuran sumber di kepala berkas.
    """
    if z.numel() == 0:
        return z.new_zeros(())
    s = torch.sigmoid(z[:, :N_KELAS])
    pos = s.gather(1, y.view(-1, 1)).squeeze(1)
    neg = s.clone()
    neg.scatter_(1, y.view(-1, 1), 0.0)

    tepi = torch.linspace(0, 1, n_bucket + 1, device=s.device)[1:-1]
    b_pos = torch.bucketize(pos, tepi)
    b_neg = torch.bucketize(neg.reshape(-1), tepi)
    massa = torch.zeros(n_bucket, device=s.device, dtype=s.dtype)
    massa.scatter_add_(0, b_neg, neg.reshape(-1))
    kumulatif_atas = massa.flip(0).cumsum(0).flip(0)
    # Jumlah negatif yang mendahului tiap positif, sebagai fungsi bucketnya.
    mendahului = kumulatif_atas[b_pos]
    return (mendahului / (mendahului + pos.detach() + 1e-6) * (1 - pos)).mean()


def pasang_kriteria(peringkat: str, koef_corn: float, koef_peringkat: float,
                    eps: float = EPS) -> None:
    """Tambal `SetCriterion.loss_labels`: tambahkan CORN + suku peringkat."""
    from rfdetr.models.criterion import SetCriterion

    asli = SetCriterion.loss_labels

    def loss_labels_ordinal(self, outputs, targets, indices, num_boxes, log=True):
        losses = asli(self, outputs, targets, indices, num_boxes, log=log)
        # Hanya lapisan decoder TERAKHIR. Panggilan utama adalah satu-satunya
        # yang membawa kunci `aux_outputs`; panggilan aux/enc tidak.
        if _KEPALA is None or "aux_outputs" not in outputs:
            return losses
        q = _KEPALA.q_logit_terakhir
        if q is None:
            return losses

        idx_b = torch.cat([torch.full_like(src, i) for i, (src, _) in enumerate(indices)])
        idx_q = torch.cat([src for (src, _) in indices])
        y = torch.cat([t["labels"][j] for t, (_, j) in zip(targets, indices)])
        if y.numel() == 0:
            return losses
        y = y.clamp(0, N_KELAS - 1)

        qm = q[idx_b, idx_q]
        tambahan = koef_corn * corn_loss(qm, y)
        _LOG["corn"] = float(tambahan.detach())

        if peringkat != "tanpa":
            zm = outputs["pred_logits"][idx_b, idx_q]
            rk = (peringkat_pasangan(zm, y, eps) if peringkat == "pasangan"
                  else peringkat_brs(zm, y))
            tambahan = tambahan + koef_peringkat * rk
            _LOG["peringkat"] = float(rk.detach())

        losses["loss_ce"] = losses["loss_ce"] + tambahan
        return losses

    SetCriterion.loss_labels = loss_labels_ordinal
    print(f"kriteria ordinal terpasang: peringkat={peringkat}, "
          f"koef_corn={koef_corn}, koef_peringkat={koef_peringkat}")


def pasang_kepala(model, eps: float = EPS):
    """Bungkus `class_embed` model dengan kepala ordinal. Kembalikan kepalanya."""
    global _KEPALA
    inti = model.model.model if hasattr(model.model, "model") else model.model
    if isinstance(inti.class_embed, KepalaOrdinal):
        _KEPALA = inti.class_embed
        return _KEPALA
    hidden = inti.transformer.d_model if hasattr(inti.transformer, "d_model") else 256
    kepala = KepalaOrdinal(inti.class_embed, hidden, eps).to(
        next(inti.parameters()).device).to(next(inti.parameters()).dtype)
    inti.class_embed = kepala
    _KEPALA = kepala
    print(f"kepala ordinal terpasang (hidden={hidden}, eps={eps}, alpha=0 saat init)")
    return kepala


def uji_sambungan(model) -> dict:
    """(a) alpha=0 -> logit IDENTIK baseline. (b) alpha!=0 -> logit BERUBAH.

    Plus (c): dengan clip aktif, |residu| tidak boleh melampaui eps -- itu
    jaminan penjaga-peringkat yang membedakan K2 dari LDL/EMD.
    """
    inti = model.model.model if hasattr(model.model, "model") else model.model
    inti = inti.to("cpu").eval()
    kepala = pasang_kepala(model)
    kepala = kepala.to("cpu").eval()

    torch.manual_seed(0)
    hs = torch.randn(4, 2, 300, kepala.ordinal.in_features)   # (L,B,Q,D)
    with torch.no_grad():
        dasar = kepala.class_embed(hs)
        kepala.alpha.zero_()
        nol = kepala(hs)
        kepala.alpha.fill_(1.0)
        buka = kepala(hs)
        residu = (buka - dasar)[..., :N_KELAS]
        kepala.alpha.zero_()

    selisih_nol = float((nol - dasar).abs().max())
    selisih_buka = float((buka - dasar).abs().max())
    residu_maks = float(residu.abs().max())
    kanal_mati_tersentuh = float((buka - dasar)[..., N_KELAS:].abs().max())
    lulus_a = selisih_nol == 0.0
    lulus_b = selisih_buka > 1e-3
    lulus_c = residu_maks <= kepala.eps + 1e-6
    lulus_d = kanal_mati_tersentuh == 0.0
    return {
        "(a) selisih_saat_alpha_nol": selisih_nol,
        "(a) lulus_no_op": lulus_a,
        "(b) selisih_saat_alpha_satu": round(selisih_buka, 6),
        "(b) lulus_tersambung": lulus_b,
        "(c) residu_maks": round(residu_maks, 6),
        "(c) eps": kepala.eps,
        "(c) lulus_clip": lulus_c,
        "(d) kanal_mati_tersentuh": kanal_mati_tersentuh,
        "(d) lulus_kanal_mati_utuh": lulus_d,
        "param_tambahan": sum(p.numel() for p in kepala.ordinal.parameters()) + 1,
        "PUTUSAN": "LULUS" if all([lulus_a, lulus_b, lulus_c, lulus_d]) else "GAGAL",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--peringkat", default="pasangan", choices=PERINGKAT)
    ap.add_argument("--koef-corn", type=float, default=1.0)
    ap.add_argument("--koef-peringkat", type=float, default=0.5)
    ap.add_argument("--eps", type=float, default=EPS)
    ap.add_argument("--dataset", default="rfdetr_ds")
    ap.add_argument("--output", default=None)
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--resolution", type=int, default=1280)
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--grad-accum", type=int, default=2)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--uji-sambungan", action="store_true")
    args = ap.parse_args()

    from rfdetr import RFDETRLarge

    if args.uji_sambungan:
        model = RFDETRLarge(gradient_checkpointing=False, resolution=320, device="cpu")
        hasil = uji_sambungan(model)
        print(json.dumps(hasil, indent=2, ensure_ascii=False))
        keluaran = EVIDENCE_ROOT / "results" / "F-006" / "uji_sambungan.json"
        keluaran.parent.mkdir(parents=True, exist_ok=True)
        keluaran.write_text(json.dumps(hasil, indent=2, ensure_ascii=False))
        print(f"-> {keluaran}")
        return 0 if hasil["PUTUSAN"] == "LULUS" else 1

    output = Path(args.output or f"runs/f006_{args.peringkat}_seed{args.seed}")
    output.mkdir(parents=True, exist_ok=True)
    pasang_kriteria(args.peringkat, args.koef_corn, args.koef_peringkat, args.eps)
    model = RFDETRLarge(gradient_checkpointing=True, resolution=args.resolution)
    pasang_kepala(model, args.eps)
    model.train(
        dataset_dir=args.dataset, output_dir=str(output), epochs=args.epochs,
        batch_size=args.batch, grad_accum_steps=args.grad_accum,
        num_workers=args.workers, resolution=args.resolution, device="cuda",
        seed=args.seed, early_stopping=True, early_stopping_patience=8,
        early_stopping_min_delta=0.001,
        multi_scale=False, expanded_scales=False, run_test=True,
    )
    from train.train_rfdetr import collect_metrics
    hasil = collect_metrics(output / "metrics.csv", vars(args))
    hasil["alpha_akhir"] = float(_KEPALA.alpha.detach()) if _KEPALA else None
    hasil["log_suku"] = _LOG
    (output / "evaluation.json").write_text(json.dumps(hasil, indent=2, default=float))
    print(f"alpha akhir (seberapa besar kepala ordinal terpakai): {hasil['alpha_akhir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
