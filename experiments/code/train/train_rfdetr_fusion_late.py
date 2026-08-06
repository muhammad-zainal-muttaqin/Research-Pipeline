#!/usr/bin/env python3
"""E-023 untuk RF-DETR: fusi AKHIR dua cabang RGB + kedalaman.

## Kenapa hanya fusi AKHIR, dan bukan fusi MENENGAH (baca sebelum menjalankan)

Tahap pemetaan sebelum berkas ini menyimpulkan: backbone RF-DETR (`rfdetr` 1.8.3)
BUKAN CNN berjenjang seperti YOLO26 (lihat `train_fusion_2branch.py`) — ia satu
ViT DINOv2 beraliran tunggal (`WindowedDinov2WithRegistersEncoder`, 12 lapisan,
resolusi token KONSTAN). "P3/P4/P5" RF-DETR adalah keluaran SINTETIS dari
`MultiScaleProjector` yang meng-upsample/downsample 4 lapisan ViT yang beresolusi
SAMA (indeks token ke-3/6/9/12) — bukan tahap spasial P2/P3/P4 seperti pada CNN.
Konsekuensinya: definisi "fusi menengah = sebelum P2/4" yang dipakai
`train_fusion_2branch.py --fusi mid` TIDAK punya padanan struktural di sini.
Mendefinisikan ulang "menengah" untuk RF-DETR (di lapisan transformer keberapa,
bagaimana token CLS/register ditangani, bagaimana jadwal windowed-attention
disinkronkan antar dua cabang) adalah proyek desain sendiri — lihat
`RANCANGAN-rfdetr-fusi-mid.md` di folder ini. Fusi MENENGAH ditangguhkan;
fusi AKHIR (titik ini) punya padanan struktural yang bersih dan diimplementasikan
di bawah.

## Titik fusi

Tepat setelah `Backbone.forward` (encoder DINOv2 + `MultiScaleProjector`),
sebelum posisi embedding + transformer LWDETR membaca `srcs`/`masks`
(`rfdetr/models/lwdetr.py:465`, `self.backbone(samples)`). Dua cabang menjalankan
SELURUH backbone (encoder + projector) secara terpisah, lalu fusi terjadi per
skala proyektor (mis. P4) lewat Concat + Conv1x1 — pola PERSIS `--fusi late`
di `train_fusion_2branch.py`, dipindahkan ke arsitektur yang berbeda:

  RGB (3ch, DINOv2 pratlatih jika --pretrained) --> Backbone RGB --> [P4_rgb]
  Depth (1ch, ACAK — lihat KAVEAT)              --> Backbone Depth --> [P4_dep]
                                                        |
                                        Concat(dim=kanal) + Conv1x1 --> [P4_fusi]
                                                        |
                                        posisi embedding + transformer LWDETR

Arsitektur dirakit dengan MENAMBAL fungsi pembangun `build_backbone` milik
rfdetr (`daftarkan_pembangun_fusi`), bukan menyalin `LWDETR`/`build_model`.
Alasannya sama dengan `daftarkan_modul()` di `train_fusion_2branch.py`: titik
tambal itu satu-satunya tempat semua argumen arsitektur (skala proyektor,
`out_feature_indexes`, ukuran patch, jumlah window, ...) sudah terkumpul
konsisten — menyalin `build_model` berarti dua sumber kebenaran yang bisa
menyimpang diam-diam saat rfdetr naik versi.

## KAVEAT YANG BELUM TERSELESAIKAN — baca sebelum melatih

1. **Tidak ada bobot DINOv2 pratlatih 1-kanal.** Patch-embed cabang depth
   (`nn.Conv2d(1, hidden, patch, patch)`) SELALU acak — beda dari
   `train_rfdetr_4ch.py` (fusi awal) yang bisa mewarisi 3 kanal pratlatih dan
   menginflasi kanal ke-4 dengan nol. Di sini seluruh cabang depth (bukan cuma
   satu conv) tidak pratlatih. Ini KONSEKUENSI ARSITEKTUR, bukan bug: pratlatihan
   DINOv2 adalah alasan utama RF-DETR-L unggul di E-021 (test mAP50 0,6038), dan
   membandingkan lengan ini head-to-head dengan RGB pratlatih penuh **bukan
   perbandingan yang sah** sampai strategi pratlatihan diputuskan — pilihan yang
   sama seperti KAVEAT `train_fusion_2branch.py` baris 42-50, diterapkan di sini.
2. **Cabang depth TIDAK bisa dipersempit** seperti `lebar_bagi=4` pada YOLO26
   (`train_fusion_2branch.py:216`). Keluarga config DINOv2 di paket ini hanya
   punya JSON untuk `small/base/large` (`rfdetr/models/backbone/dinov2.py`);
   tidak ada `tiny`. Maka cabang depth memakai encoder DINOv2 SAMA UKURAN dengan
   RGB (mis. `dinov2_windowed_small`, 384-d, 12 lapisan) — dua kali ongkos forward
   dibanding YOLO26 late fusion, yang cabang depth-nya sengaja dibuat murah.
3. **`.train()` (jalur PyTorch Lightning di rfdetr 1.8.3) belum diverifikasi
   TIDAK membangun ulang backbone dari config di titik lain** selain
   `build_model`. `daftarkan_pembangun_fusi()` menambal fungsi yang dipanggil
   `build_model`/`build_model_from_config`, sehingga SEHARUSNYA bertahan
   melewati pembangunan ulang apa pun yang lewat jalur resmi itu — tapi ini
   BELUM diuji dengan menjalankan `.train()` sungguhan (GPU dipakai penuh
   pelatihan lain saat berkas ini ditulis; `--latih` di baris perintah TIDAK
   dijalankan). Perlakukan `--latih` sebagai TIDAK TERVERIFIKASI sampai
   diuji ulang saat GPU tersedia.

Sampai kaveat 1 diputuskan, berkas ini **belum boleh menghasilkan angka yang
dikutip**. Yang sudah tervalidasi (`--hanya-bangun`, CPU): arsitektur dua cabang
terbangun benar dan cabang depth benar-benar tersambung (uji: mengubah HANYA
kanal depth mengubah keluaran fusi).
"""
from __future__ import annotations

import argparse
import json
import time

import torch
import torch.nn as nn

VARIAN = {
    "nano": "RFDETRNanoConfig", "small": "RFDETRSmallConfig",
    "medium": "RFDETRMediumConfig", "large": "RFDETRLargeConfig",
}


# ----------------------------------------------------------------- modul baru
def _tambal_kanal_tunggal(cabang, kanal: int) -> None:
    """Ganti conv patch-embed DINOv2 dari 3 kanal menjadi `kanal`, IN PLACE.

    Tidak ada mekanisme bawaan rfdetr untuk membangun `DinoV2` dengan
    `num_channels` != 3 (parameter itu memang tidak diekspos ke `DinoV2.__init__`
    maupun `Backbone.__init__` — hanya dibaca dari JSON config, selalu 3).
    Menukar `nn.Conv2d` di `patch_embeddings.projection` setelah konstruksi, lalu
    menyelaraskan `patch_embeddings.num_channels` dan `config.num_channels`
    (dipakai `Dinov2WithRegistersPatchEmbeddings.forward` untuk memvalidasi
    bentuk masukan, `dinov2_with_windowed_attn.py:307-311`), adalah satu-satunya
    jalan tanpa menambal kelas config itu sendiri. `bias` disalin apa adanya
    dari conv lama (DINOv2 patch-embed defaultnya tanpa bias, tapi tidak
    diasumsikan — dibaca dari conv yang sesungguhnya dibangun).
    """
    patch_embed = cabang.encoder.encoder.embeddings.patch_embeddings
    lama = patch_embed.projection
    baru = nn.Conv2d(kanal, lama.out_channels, kernel_size=lama.kernel_size,
                      stride=lama.stride, padding=lama.padding,
                      bias=lama.bias is not None)
    patch_embed.projection = baru
    patch_embed.num_channels = kanal
    cabang.encoder.encoder.config.num_channels = kanal


class FusionBackboneRGBD(nn.Module):
    """Dua cabang backbone (RGB 3ch, depth 1ch) + Concat/Conv1x1 per skala.

    Antarmuka `forward` meniru `Backbone.forward` PERSIS (`(out, cross_attn_out)`
    dengan `out` = senarai `NestedTensor` per skala proyektor), sehingga modul
    ini bisa langsung menggantikan `Backbone` sebagai elemen pertama `Joiner`
    tanpa menyentuh `Joiner`, posisi embedding, atau transformer sama sekali.
    """

    def __init__(self, rgb, kedalaman, out_channels: int):
        super().__init__()
        if rgb.projector_scale != kedalaman.projector_scale:
            raise ValueError("kedua cabang harus punya projector_scale yang sama")
        self.rgb = rgb
        self.kedalaman = kedalaman
        n_skala = len(rgb.projector_scale)
        # Concat lalu proyeksi 1x1, bukan penjumlahan — alasan sama dengan
        # `fusi_di` di `train_fusion_2branch.py`: proyeksi membiarkan jaringan
        # sendiri menimbang tiap modalitas, dan bobotnya bisa diperiksa
        # setelah latihan (klaim "depth dipakai" dapat diverifikasi).
        self.fusi = nn.ModuleList(
            nn.Conv2d(2 * out_channels, out_channels, kernel_size=1)
            for _ in range(n_skala)
        )
        self._export = False

    def forward(self, tensor_list):
        from rfdetr.utilities.tensors import NestedTensor

        x = tensor_list.tensors
        if x.shape[1] != 4:
            raise ValueError(f"FusionBackboneRGBD butuh masukan 4 kanal [R,G,B,D], dapat {x.shape[1]}")
        rgb_in = NestedTensor(x[:, :3], tensor_list.mask)
        dep_in = NestedTensor(x[:, 3:4], tensor_list.mask)

        rgb_out, _ = self.rgb(rgb_in)
        dep_out, _ = self.kedalaman(dep_in)

        out = []
        for r, d, conv in zip(rgb_out, dep_out, self.fusi):
            gabung = torch.cat([r.tensors, d.tensors], dim=1)
            out.append(NestedTensor(conv(gabung), r.mask))
        return out, None


def bangun_backbone_fusi(
    encoder, vit_encoder_num_layers, pretrained_encoder, window_block_indexes,
    drop_path, out_channels, out_feature_indexes, projector_scale, use_cls_token,
    hidden_dim, position_embedding, freeze_encoder, layer_norm, target_shape,
    rms_norm, backbone_lora, force_no_pretrain, gradient_checkpointing,
    load_dinov2_weights, patch_size, num_windows, positional_encoding_size,
    dual_projector=False,
):
    """Pengganti `rfdetr.models.backbone.build_backbone`, tanda tangan IDENTIK.

    Dipanggil oleh `build_model`/`build_model_from_config` setelah
    `daftarkan_pembangun_fusi()` menambalnya — argumen di sini adalah persis
    argumen yang biasanya diteruskan ke `Backbone` tunggal RF-DETR
    (`rfdetr/models/backbone/__init__.py:61`).
    """
    from rfdetr.models.backbone import Joiner
    from rfdetr.models.backbone.backbone import Backbone
    from rfdetr.models.position_encoding import build_position_encoding

    if dual_projector:
        raise NotImplementedError("dual_projector belum didukung fusi akhir dua cabang")

    kw_bersama = dict(
        window_block_indexes=window_block_indexes, drop_path=drop_path,
        out_channels=out_channels, out_feature_indexes=out_feature_indexes,
        projector_scale=projector_scale, use_cls_token=use_cls_token,
        layer_norm=layer_norm, target_shape=target_shape, rms_norm=rms_norm,
        backbone_lora=backbone_lora, gradient_checkpointing=gradient_checkpointing,
        patch_size=patch_size, num_windows=num_windows,
        positional_encoding_size=positional_encoding_size,
    )

    # `load_dinov2_weights` yang diteruskan `build_model` dihitung dari
    # `args.pretrain_weights is None` — bukan apa yang kita mau di sini (ada
    # tidaknya CHECKPOINT RF-DETR penuh, bukan niat memuat DINOv2 hub untuk
    # cabang RGB). Dikendalikan lewat `_MUAT_PRATLATIH_RGB` yang disetel
    # `daftarkan_pembangun_fusi`, bukan lewat argumen ini.
    rgb = Backbone(encoder, pretrained_encoder, freeze_encoder=freeze_encoder,
                    load_dinov2_weights=_MUAT_PRATLATIH_RGB, **kw_bersama)

    # Cabang depth: TIDAK PERNAH bisa memuat bobot DINOv2 pratlatih (yang ada
    # di hub adalah 3-kanal) — lihat KAVEAT 1 di kepala berkas. Selalu acak.
    kedalaman = Backbone(encoder, pretrained_encoder=None, freeze_encoder=False,
                          load_dinov2_weights=False, **kw_bersama)
    _tambal_kanal_tunggal(kedalaman, kanal=1)

    fusi = FusionBackboneRGBD(rgb, kedalaman, out_channels)
    pos_embed = build_position_encoding(hidden_dim, position_embedding)
    return Joiner(fusi, pos_embed)


_MUAT_PRATLATIH_RGB = False


def daftarkan_pembangun_fusi(muat_pratlatih_rgb: bool = False) -> None:
    """Tambal `build_backbone` di namespace `rfdetr.models.lwdetr`.

    `lwdetr.py` mengimpor nama itu lewat `from rfdetr.models.backbone import
    build_backbone` — artinya `lwdetr.build_backbone` adalah rujukan terpisah
    di namespace modul `lwdetr`, dan menambal DI SANA (bukan di
    `rfdetr.models.backbone.build_backbone`) adalah satu-satunya cara tambalan
    ini benar-benar dipakai `build_model`.
    """
    global _MUAT_PRATLATIH_RGB
    _MUAT_PRATLATIH_RGB = muat_pratlatih_rgb
    import rfdetr.models.lwdetr as lwdetr_mod
    lwdetr_mod.build_backbone = bangun_backbone_fusi
    print(f"pembangun fusi akhir terdaftar (RGB pratlatih={muat_pratlatih_rgb}, "
          f"depth SELALU acak — lihat KAVEAT 1)")


# ------------------------------------------------------------------ pengujian
def uji_forward_cpu(model, resolusi: int) -> dict:
    """Bangun tensor 4 kanal acak, jalankan forward CPU, dan buktikan cabang
    depth benar-benar tersambung (uji tukar E-023: mengubah HANYA kanal depth
    mengubah keluaran)."""
    model.eval()
    torch.manual_seed(0)
    x = torch.randn(1, 4, resolusi, resolusi)
    with torch.no_grad():
        keluar_a = model(x)
        x_beda_depth = x.clone()
        x_beda_depth[:, 3] = torch.randn_like(x_beda_depth[:, 3])
        keluar_b = model(x_beda_depth)

    selisih = (keluar_a["pred_boxes"] - keluar_b["pred_boxes"]).abs().sum().item()
    return {
        "bentuk_pred_logits": list(keluar_a["pred_logits"].shape),
        "bentuk_pred_boxes": list(keluar_a["pred_boxes"].shape),
        "selisih_abs_saat_depth_diubah": selisih,
        "depth_tersambung": selisih > 1e-6,
    }


def main() -> int:
    """Bangun model + uji forward CPU. Tidak ada jalur lain: `--latih` menolak
    jalan (lihat KAVEAT 3) sampai diverifikasi ulang saat GPU tersedia."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--varian", default="large", choices=list(VARIAN))
    ap.add_argument("--resolution", type=int, default=224,
                     help="kecil secara sengaja untuk uji CPU; produksi pakai 704 (large)")
    ap.add_argument("--num-classes", type=int, default=4)
    ap.add_argument("--pretrained", action="store_true",
                     help="muat DINOv2 pratlatih di cabang RGB (unduh dari HF hub; "
                          "lambat di CPU, dimatikan secara default untuk uji cepat)")
    ap.add_argument("--latih", action="store_true",
                     help="BELUM TERVERIFIKASI (lihat KAVEAT 3) — menolak jalan kecuali dipaksa")
    args = ap.parse_args()

    if args.latih:
        raise SystemExit(
            "--latih ditolak: jalur pelatihan (.train() PTL) belum diverifikasi menghormati "
            "tambalan build_backbone (KAVEAT 3), dan GPU sedang dipakai penuh pelatihan lain "
            "saat berkas ini ditulis. Uji ulang saat GPU tersedia sebelum menghapus pagar ini."
        )

    daftarkan_pembangun_fusi(muat_pratlatih_rgb=args.pretrained)

    import rfdetr.config as cfg_mod
    from rfdetr.models.lwdetr import build_model_from_config

    KelasConfig = getattr(cfg_mod, VARIAN[args.varian])
    mc = KelasConfig(
        resolution=args.resolution, num_classes=args.num_classes,
        # `pretrain_weights` di sini adalah checkpoint RF-DETR PENUH (bukan
        # hanya DINOv2) — tidak relevan untuk arsitektur dua cabang ini, jadi
        # selalu None. Pratlatihan cabang RGB dikendalikan terpisah lewat
        # `--pretrained` di atas (lihat `daftarkan_pembangun_fusi`).
        pretrain_weights=None,
    )

    mulai = time.time()
    model = build_model_from_config(mc)
    durasi_bangun = time.time() - mulai

    n_total = sum(p.numel() for p in model.parameters())
    n_rgb = sum(p.numel() for p in model.backbone[0].rgb.parameters())
    n_dep = sum(p.numel() for p in model.backbone[0].kedalaman.parameters())
    n_fusi = sum(p.numel() for p in model.backbone[0].fusi.parameters())

    hasil_uji = uji_forward_cpu(model, args.resolution)

    ringkas = {
        "varian": args.varian, "resolution": args.resolution,
        "num_classes": args.num_classes, "pretrained_rgb": args.pretrained,
        "durasi_bangun_detik": round(durasi_bangun, 2),
        "param_total": n_total, "param_cabang_rgb": n_rgb,
        "param_cabang_kedalaman": n_dep, "param_lapisan_fusi": n_fusi,
        **hasil_uji,
    }
    print(json.dumps(ringkas, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
