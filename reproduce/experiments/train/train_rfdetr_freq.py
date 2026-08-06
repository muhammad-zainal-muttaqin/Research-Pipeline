#!/usr/bin/env python3
"""F-007 (K1a) — Cabang frekuensi samping ber-gate init-nol untuk RF-DETR-L.

Gerbangnya sudah lolos: F-002 mengukur bahwa respons frekuensi tinggi memisahkan
isi tandan dari PELEPAH pada B4 sebesar +0,0731 (dwt_hh) di atas kendali kotak
acak, tiga kali lipat ambang +0,02. Berkas ini menguji apakah keterpisahan
piksel itu berubah menjadi mAP.

## Titik suntik: SEBELUM projector, bukan intra-blok

Rencana aslinya menyuntik di ~1/3 dan ~2/3 blok transformer DINOv2 DAN sebelum
projector. Bagian intra-blok DITANGGUHKAN, dan alasannya sudah terekam di repo
ini: backbone RF-DETR bukan CNN berjenjang melainkan satu ViT DINOv2 beraliran
tunggal dengan resolusi token KONSTAN; "P3/P4/P5"-nya adalah keluaran SINTETIS
`MultiScaleProjector` dari 4 lapisan ViT yang beresolusi sama. Mendefinisikan
"menengah" di sana (di lapisan berapa, bagaimana token register ditangani,
bagaimana jadwal windowed-attention disinkronkan) adalah proyek desain sendiri —
lihat `train_rfdetr_fusion_late.py:5-19` dan `RANCANGAN-rfdetr-fusi-mid.md`.

Titik sebelum projector punya padanan struktural yang bersih dan SUDAH terbukti
tersambung pada arsitektur ini.

## Penyimpangan dari rancangan, ditulis terbuka

Rancangan meminta **deformable cross-attention** (fitur backbone sebagai query,
fitur samping sebagai key/value). Yang diimplementasikan di sini adalah **fusi
aditif ber-gate**. Alasannya bukan kemalasan melainkan ongkos: pada resolusi
1280 dengan patch 16, keluaran projector P4 berukuran 80x80 = 6.400 token;
attention penuh 6.400x6.400 per kepala tidak sepadan untuk menguji pertanyaan
yang lebih dasar, yaitu **apakah informasi frekuensi tinggi yang disuntik
sebelum projector menolong sama sekali**. Bila lengan ini lolos, varian
attention yang lebih kaya baru layak dibayar. Bila tidak lolos, attention
kemungkinan besar hanya menambah parameter pada sinyal yang memang tidak
terpakai — dan itu justru yang dikhawatirkan E-030.

## Empat lengan — dua di antaranya KONTROL WAJIB

  dwt          sub-band Haar frekuensi tinggi (LH, HL, HH)   <- yang diusulkan
  laplacian    |Laplacian| tiga skala                        <- pesaing E-011/F-002
  freq_rendah  sub-band Haar LL tiga skala        [KONTROL]  <- frekuensi RENDAH
  fase_diacak  sub-band tinggi, fase diacak di Fourier [KONTROL]

Kedua kontrol berparameter SAMA PERSIS dengan lengan perlakuan (3 kanal masuk,
side encoder identik). Tanpa keduanya, kenaikan signifikan pun tidak membuktikan
bahwa **frekuensi** penyebabnya — bisa saja sekadar kapasitas tambahan. Ini
disiplin lengan `derau`/`tukar` yang sama seperti E-027 dan E-032.

`fase_diacak` adalah kontrol yang lebih ketat daripada `freq_rendah`: ia
mempertahankan spektrum amplitudo (jadi "jumlah frekuensi tinggi"-nya sama)
tetapi menghancurkan keselarasan spasial dengan tandan. Bila `dwt` hanya
menyamai `fase_diacak`, yang bekerja adalah kapasitas, bukan struktur.

## Sifat yang WAJIB dijaga: gamma = 0 saat inisialisasi

Cabang samping mulai sebagai *no-op* PERSIS. Itu menjawab keberatan E-030:
cabang yang tak berguna tidak boleh menjadi sumber derau yang menurunkan
baseline, karena kalau begitu yang diukur adalah kerusakan, bukan manfaat.
`--uji-sambungan` membuktikan dua arah: (a) pada init keluaran identik baseline,
(b) setelah gate dibuka paksa keluaran berubah. Bila (b) gagal, cabangnya tidak
tersambung dan seluruh runnya sia-sia — mode gagal senyap yang sudah beberapa
kali terjadi di repo ini.

Pemakaian:
  python train/train_rfdetr_freq.py --uji-sambungan --lengan dwt
  python train/train_rfdetr_freq.py --lengan dwt --seed 42 --output <dir>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"

import torch
import torch.nn as nn
import torch.nn.functional as F

LENGAN = ["dwt", "laplacian", "freq_rendah", "fase_diacak"]


# --------------------------------------------------------------- peta frekuensi
def _haar(x: torch.Tensor):
    """DWT Haar satu tingkat pada tensor (B,1,H,W). Kembalikan (LL, LH, HL, HH)."""
    a = x[..., 0::2, 0::2]
    b = x[..., 0::2, 1::2]
    c = x[..., 1::2, 0::2]
    d = x[..., 1::2, 1::2]
    return (a + b + c + d) / 2, (a + b - c - d) / 2, (a - b + c - d) / 2, (a - b - c + d) / 2


def peta_frekuensi(rgb: torch.Tensor, lengan: str) -> torch.Tensor:
    """Hasilkan masukan 3 kanal untuk side encoder dari batch RGB (B,3,H,W).

    Seluruh lengan mengeluarkan TEPAT 3 kanal pada resolusi penuh supaya jumlah
    parameter side encoder identik antar lengan — syarat kontrol berparameter
    sama (rezim §5.5).
    """
    B, _, H, W = rgb.shape
    # Luminans (BT.601), sejalan dengan `analysis/freq_vs_pelepah.py`.
    g = (0.299 * rgb[:, 0] + 0.587 * rgb[:, 1] + 0.114 * rgb[:, 2]).unsqueeze(1)

    if lengan == "dwt":
        _, lh, hl, hh = _haar(g)
        bands = [lh.abs(), hl.abs(), hh.abs()]

    elif lengan == "laplacian":
        k = torch.tensor([[0., 1., 0.], [1., -4., 1.], [0., 1., 0.]],
                         device=g.device, dtype=g.dtype).view(1, 1, 3, 3)
        bands = []
        cur = g
        for _ in range(3):
            bands.append(F.conv2d(cur, k, padding=1).abs())
            cur = F.avg_pool2d(cur, 2)
        # samakan ukuran ke skala terkecil supaya bisa ditumpuk
        kecil = bands[-1].shape[-2:]
        bands = [F.adaptive_avg_pool2d(b, kecil) for b in bands]

    elif lengan == "freq_rendah":
        # KONTROL: sub-band LL (frekuensi RENDAH) tiga tingkat.
        bands = []
        cur = g
        for _ in range(3):
            ll, _, _, _ = _haar(cur)
            bands.append(ll)
            cur = ll
        kecil = bands[-1].shape[-2:]
        bands = [F.adaptive_avg_pool2d(b, kecil) for b in bands]

    elif lengan == "fase_diacak":
        # KONTROL: sub-band tinggi yang SAMA dengan lengan `dwt`, tetapi fasenya
        # diacak di ranah Fourier. Amplitudo spektrum dipertahankan; keselarasan
        # spasial dengan tandan dihancurkan.
        _, lh, hl, hh = _haar(g)
        bands = []
        for b in (lh, hl, hh):
            f = torch.fft.rfft2(b.float())
            fase = torch.rand_like(f.real) * (2 * torch.pi)
            bands.append(torch.fft.irfft2(f.abs() * torch.exp(1j * fase),
                                          s=b.shape[-2:]).to(b.dtype).abs())
    else:
        raise ValueError(f"lengan tidak dikenal: {lengan}")

    return torch.cat(bands, dim=1)


# ------------------------------------------------------------------ side encoder
class SideEncoder(nn.Module):
    """Encoder konvolusi sempit: 3 kanal -> `out_channels` pada grid projector.

    Sempit disengaja. Yang diuji adalah apakah SINYAL-nya berguna, bukan apakah
    parameter tambahan berguna — dan E-030 sudah menunjukkan bahwa menambah
    kapasitas saja bisa menggerakkan angka.

    `GroupNorm` pada keluaran tiap tahap adalah "normalisasi energi" yang diminta
    rancangan: magnitudo tepi bergantung pencahayaan, dan tanpa normalisasi citra
    yang terang akan mendominasi batch.
    """

    def __init__(self, out_channels: int, lebar: int = 32):
        super().__init__()
        c1, c2, c3 = lebar, lebar * 2, lebar * 4

        def blok(ci, co, stride):
            return nn.Sequential(
                nn.Conv2d(ci, co, 3, stride=stride, padding=1, bias=False),
                nn.GroupNorm(8, co),
                nn.GELU(),
            )

        self.tahap = nn.Sequential(
            blok(3, c1, 2),       # /2
            blok(c1, c2, 2),      # /4
            blok(c2, c3, 2),      # /8
        )
        self.keluar = nn.Conv2d(c3, out_channels, 1)

    def forward(self, x, ukuran_target):
        h = self.tahap(x)
        h = self.keluar(h)
        if h.shape[-2:] != ukuran_target:
            h = F.interpolate(h, size=ukuran_target, mode="bilinear", align_corners=False)
        return h


def _kelas_frekuensi_backbone():
    """Bangun kelas `FrekuensiBackbone` sebagai TURUNAN `Backbone`.

    Dibuat lewat fungsi supaya `rfdetr` hanya diimpor saat dipakai.

    ## Kenapa TURUNAN, bukan pembungkus — pelajaran mahal 6 Agustus 2026

    Versi pertama MEMBUNGKUS `Backbone` sebagai `self.dasar`. Itu mengubah nama
    parameter dari `backbone.0.encoder...` menjadi `backbone.0.dasar.encoder...`,
    sehingga `load_pretrain_weights` **gagal mencocokkan 264 parameter** dan
    SELURUH backbone DINOv2 berangkat dari inisialisasi ACAK. rfdetr hanya
    mencetak WARNING, latihan tetap jalan, dan angkanya terlihat "wajar" —
    sampai dibandingkan: train/loss awal 11,56 vs baseline 9,28, dan val mAP50
    epoch 0 sebesar 0,1308 vs 0,4714.

    Kalau itu tidak ketahuan, 22 jam GPU akan menghasilkan perbandingan yang
    TIDAK SAH: lengan perlakuan berbackbone acak melawan baseline pratlatih.
    Selisihnya akan didominasi ada-tidaknya pralatihan, bukan cabang frekuensi —
    persis mode gagal yang sudah dicatat `STATUS.md` §"Penghalang" untuk E-023.

    Sebagai turunan, nama parameter warisan TIDAK berubah, bobot pratlatih
    termuat penuh, dan `get_named_param_lr_pairs` bawaan `Backbone` (yang
    mematok kunci `backbone.0.encoder`) bekerja apa adanya — sehingga peluruhan
    LR per lapisan pun tidak perlu ditulis ulang.
    """
    from rfdetr.models.backbone.backbone import Backbone

    class FrekuensiBackbone(Backbone):
        """`Backbone` + cabang frekuensi ber-gate, disuntik SEBELUM transformer.

        Injeksi: `keluar = fitur + gamma * proyeksi(samping)` dengan `gamma`
        skalar ber-inisialisasi NOL.

        **Kenapa gate SKALAR, bukan per-kanal.** Rancangan menulis `alpha_c`,
        menyiratkan gate per kanal. Skalar dipilih karena yang harus dijamin
        adalah sifat *no-op saat init*, dan karena satu angka per titik suntik
        dapat dilaporkan apa adanya setelah latihan — sehingga klaim "cabang
        frekuensi terpakai" dapat diverifikasi, bukan diasumsikan.

        `get_named_param_lr_pairs` TIDAK ditulis ulang: versi bawaan `Backbone`
        mematok kunci `backbone.0.encoder`, dan karena kelas ini turunan (bukan
        pembungkus) nama parameternya tetap cocok. Parameter cabang samping
        otomatis jatuh ke `other_params` dengan `args.lr` penuh — benar untuk
        modul berinisialisasi acak.
        """

        def __init__(self, *args, lengan: str = "dwt", lebar: int = 32, **kwargs):
            super().__init__(*args, **kwargs)
            self.lengan = lengan
            out_channels = kwargs["out_channels"]
            n_skala = len(self.projector_scale)
            self.samping = SideEncoder(out_channels, lebar)
            self.proyeksi = nn.ModuleList(
                nn.Conv2d(out_channels, out_channels, 1) for _ in range(n_skala))
            # gamma = 0 -> cabang samping adalah no-op PERSIS saat inisialisasi.
            self.gamma = nn.Parameter(torch.zeros(n_skala))
            for m in self.proyeksi:
                nn.init.zeros_(m.bias)

        def forward(self, tensor_list):
            from rfdetr.utilities.tensors import NestedTensor

            keluar_dasar, cross = super().forward(tensor_list)
            hf = peta_frekuensi(tensor_list.tensors[:, :3], self.lengan)

            out = []
            for i, feat in enumerate(keluar_dasar):
                f = feat.tensors
                s = self.samping(hf.to(f.dtype), f.shape[-2:])
                out.append(NestedTensor(f + self.gamma[i] * self.proyeksi[i](s), feat.mask))
            return out, cross

    return FrekuensiBackbone


# ------------------------------------------------------------------- pendaftaran
_LENGAN = "dwt"
_LEBAR = 32


def bangun_backbone_freq(
    encoder, vit_encoder_num_layers, pretrained_encoder, window_block_indexes,
    drop_path, out_channels, out_feature_indexes, projector_scale, use_cls_token,
    hidden_dim, position_embedding, freeze_encoder, layer_norm, target_shape,
    rms_norm, backbone_lora, force_no_pretrain, gradient_checkpointing,
    load_dinov2_weights, patch_size, num_windows, positional_encoding_size,
    dual_projector=False,
):
    """Pengganti `build_backbone`, tanda tangan IDENTIK.

    Membangun TURUNAN `Backbone`, bukan pembungkus — lihat
    `_kelas_frekuensi_backbone` untuk alasannya (264 parameter pratlatih gagal
    termuat pada versi pembungkus).
    """
    from rfdetr.models.backbone import Joiner
    from rfdetr.models.position_encoding import build_position_encoding

    if dual_projector:
        raise NotImplementedError("dual_projector belum didukung cabang frekuensi")

    Kelas = _kelas_frekuensi_backbone()
    bb = Kelas(
        encoder, pretrained_encoder, freeze_encoder=freeze_encoder,
        load_dinov2_weights=load_dinov2_weights,
        window_block_indexes=window_block_indexes, drop_path=drop_path,
        out_channels=out_channels, out_feature_indexes=out_feature_indexes,
        projector_scale=projector_scale, use_cls_token=use_cls_token,
        layer_norm=layer_norm, target_shape=target_shape, rms_norm=rms_norm,
        backbone_lora=backbone_lora, gradient_checkpointing=gradient_checkpointing,
        patch_size=patch_size, num_windows=num_windows,
        positional_encoding_size=positional_encoding_size,
        lengan=_LENGAN, lebar=_LEBAR,
    )
    return Joiner(bb, build_position_encoding(hidden_dim, position_embedding))


def daftarkan(lengan: str, lebar: int = 32) -> None:
    """Tambal `build_backbone` DI NAMESPACE `rfdetr.models.lwdetr`.

    `lwdetr.py` mengimpor nama itu lewat `from rfdetr.models.backbone import
    build_backbone`, jadi `lwdetr.build_backbone` adalah rujukan terpisah;
    menambal di `rfdetr.models.backbone` TIDAK berpengaruh.
    """
    global _LENGAN, _LEBAR
    if lengan not in LENGAN:
        raise ValueError(f"lengan harus salah satu dari {LENGAN}")
    _LENGAN, _LEBAR = lengan, lebar
    import rfdetr.models.lwdetr as lwdetr_mod
    lwdetr_mod.build_backbone = bangun_backbone_freq
    print(f"cabang frekuensi terdaftar: lengan={lengan}, lebar={lebar}, gamma=0 saat init")


# ---------------------------------------------------------------- uji sambungan
def uji_sambungan(model, resolusi: int) -> dict:
    """Buktikan DUA arah sekaligus. Wajib lulus sebelum run 3-seed diantre.

    (a) gamma = 0  -> keluaran IDENTIK dengan backbone dasar (no-op persis)
    (b) gamma != 0 -> keluaran BERUBAH (cabang benar-benar tersambung)

    Yang gagal senyap adalah (b): cabang yang tidak tersambung tetap melatih
    tanpa error dan menghasilkan angka yang tampak wajar.
    """
    from rfdetr.utilities.tensors import NestedTensor

    inti = model.model.model if hasattr(model.model, "model") else model.model
    inti = inti.to("cpu").eval()
    # Cari modulnya, jangan menebak jalur atribut: `Joiner` sendiri sebuah
    # `nn.Sequential`, dan rfdetr membungkusnya lagi di beberapa tempat.
    # Menelusuri `.modules()` tahan terhadap perubahan nesting antar versi.
    Kelas = _kelas_frekuensi_backbone()
    bungkus = next((m for m in inti.modules() if type(m).__name__ == "FrekuensiBackbone"), None)
    if bungkus is None:
        raise RuntimeError("FrekuensiBackbone tidak ditemukan di model — tambalan tidak terpakai")

    torch.manual_seed(0)
    x = torch.randn(1, 3, resolusi, resolusi)
    nt = NestedTensor(x, torch.zeros(1, resolusi, resolusi, dtype=torch.bool))

    with torch.no_grad():
        from rfdetr.models.backbone.backbone import Backbone
        dasar_out, _ = Backbone.forward(bungkus, nt)
        dasar_ref = [t.tensors.clone() for t in dasar_out]

        bungkus.gamma.zero_()
        nol_out, _ = bungkus(nt)
        selisih_nol = max(float((a.tensors - b).abs().max())
                          for a, b in zip(nol_out, dasar_ref))

        bungkus.gamma.fill_(1.0)
        buka_out, _ = bungkus(nt)
        selisih_buka = max(float((a.tensors - b).abs().max())
                           for a, b in zip(buka_out, dasar_ref))
        bungkus.gamma.zero_()

    n_samping = sum(p.numel() for p in bungkus.samping.parameters())
    n_proj = sum(p.numel() for p in bungkus.proyeksi.parameters())
    lulus_a = selisih_nol < 1e-5
    lulus_b = selisih_buka > 1e-3

    # (c) JALUR OPTIMIZER. Ditambahkan setelah run pertama mati di
    # `configure_optimizers` — bukan di forward — sehingga uji yang hanya
    # menjalankan forward meloloskannya. Yang diperiksa dua hal:
    #   1. `get_param_dict` benar-benar bisa dipanggil (metode ada), dan
    #   2. peluruhan LR per lapisan DINOv2 tetap hidup (bukan lr datar),
    #      karena delegasi yang salah mengembalikan dict kosong TANPA error.
    from rfdetr.training.param_groups import get_param_dict

    class _Args:
        out_feature_indexes = [3, 6, 9, 12]
        lr, lr_encoder = 1e-4, 1.5e-4
        lr_vit_layer_decay, lr_component_decay = 0.8, 0.7
        weight_decay = 1e-4

    try:
        pasangan = bungkus.get_named_param_lr_pairs(_Args(), prefix="backbone.0")
        n_encoder = len(pasangan)
        lr_unik = sorted({round(v["lr"], 10) for v in pasangan.values()})
        param_dicts = get_param_dict(_Args(), inti)
        n_grup = len(param_dicts)
        galat_optim = None
    except Exception as e:  # noqa: BLE001 - dilaporkan apa adanya
        n_encoder, lr_unik, n_grup, galat_optim = 0, [], 0, f"{type(e).__name__}: {e}"

    lulus_c = galat_optim is None and n_encoder > 0 and len(lr_unik) > 1

    # (d) BOBOT PRATLATIH BENAR-BENAR TERMUAT — pemeriksaan yang TIDAK ADA pada
    # versi pertama, dan justru itulah sebabnya cacat terbesar seri ini lolos.
    # Versi pembungkus mengubah nama parameter sehingga 264 bobot gagal
    # dicocokkan; rfdetr hanya mencetak WARNING dan latihan tetap jalan dengan
    # backbone ACAK. Di sini dihitung langsung: berapa parameter model yang
    # TIDAK punya pasangan di checkpoint pratlatih.
    import os

    ckpt_path = os.path.expanduser("~/.roboflow/models/rf-detr-large-2026.pth")
    tak_termuat, contoh_tak_termuat, galat_ckpt = -1, [], None
    try:
        sd = torch.load(ckpt_path, map_location="cpu", weights_only=False)
        kunci_ckpt = set((sd.get("model") or sd).keys())
        nama_model = [n for n, _ in inti.named_parameters()]
        hilang = [n for n in nama_model if n not in kunci_ckpt]
        tak_termuat = len(hilang)
        contoh_tak_termuat = hilang[:4]
    except Exception as e:  # noqa: BLE001
        galat_ckpt = f"{type(e).__name__}: {e}"

    # Ambang: hanya parameter cabang samping (+ _kp_active_mask milik baseline)
    # yang boleh tidak termuat. Baseline F-001 mencatat tepat 1.
    n_baru = (sum(p.numel() > 0 for p in bungkus.samping.parameters())
              + sum(p.numel() > 0 for p in bungkus.proyeksi.parameters()) + 1)
    lulus_d = galat_ckpt is None and 0 <= tak_termuat <= n_baru + 1
    return {
        "lengan": bungkus.lengan,
        "resolusi": resolusi,
        "(a) selisih_saat_gamma_nol": selisih_nol,
        "(a) lulus_no_op": lulus_a,
        "(b) selisih_saat_gamma_satu": selisih_buka,
        "(b) lulus_tersambung": lulus_b,
        "(c) n_param_encoder_ber-LR-lapisan": n_encoder,
        "(c) n_nilai_LR_unik": len(lr_unik),
        "(c) n_grup_optimizer": n_grup,
        "(c) galat": galat_optim,
        "(c) lulus_jalur_optimizer": lulus_c,
        "(d) param_tak_termuat_dari_pratlatih": tak_termuat,
        "(d) ambang_wajar": n_baru + 1,
        "(d) contoh": contoh_tak_termuat,
        "(d) galat": galat_ckpt,
        "(d) lulus_pratlatih_termuat": lulus_d,
        "param_side_encoder": n_samping,
        "param_proyeksi": n_proj,
        "param_tambahan_total": n_samping + n_proj + bungkus.gamma.numel(),
        "PUTUSAN": "LULUS" if all([lulus_a, lulus_b, lulus_c, lulus_d]) else "GAGAL",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lengan", default="dwt", choices=LENGAN)
    ap.add_argument("--lebar", type=int, default=32)
    ap.add_argument("--dataset", default="rfdetr_ds")
    ap.add_argument("--output", default=None)
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--resolution", type=int, default=1280)
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--grad-accum", type=int, default=2)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--uji-sambungan", action="store_true",
                    help="Bangun model di CPU, buktikan (a) dan (b), lalu keluar.")
    args = ap.parse_args()

    daftarkan(args.lengan, args.lebar)
    from rfdetr import RFDETRLarge

    if args.uji_sambungan:
        # Resolusi kecil supaya muat di CPU; sifat yang diuji tidak bergantung
        # resolusi (kelipatan 32 = patch_size 16 x num_windows 2).
        res = 320
        model = RFDETRLarge(gradient_checkpointing=False, resolution=res, device="cpu")
        hasil = uji_sambungan(model, res)
        print(json.dumps(hasil, indent=2, ensure_ascii=False))
        keluaran = EVIDENCE_ROOT / "results" / "F-007" / f"uji_sambungan_{args.lengan}.json"
        keluaran.parent.mkdir(parents=True, exist_ok=True)
        keluaran.write_text(json.dumps(hasil, indent=2, ensure_ascii=False))
        print(f"-> {keluaran}")
        return 0 if hasil["PUTUSAN"] == "LULUS" else 1

    output = Path(args.output or f"runs/f007_{args.lengan}_seed{args.seed}")
    output.mkdir(parents=True, exist_ok=True)
    model = RFDETRLarge(gradient_checkpointing=True, resolution=args.resolution)
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
    (output / "evaluation.json").write_text(json.dumps(hasil, indent=2, default=float))
    v, t = hasil.get("val", {}), hasil.get("test", {})
    print(f"VAL  mAP50={v.get('mAP50')}  mAP50-95={v.get('mAP50_95')}")
    print(f"TEST mAP50={t.get('mAP50')}  mAP50-95={t.get('mAP50_95')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
