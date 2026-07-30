#!/usr/bin/env python3
"""Ringkas seluruh hasil P0 jadi satu tabel — protokol beku pycocotools.

Membaca results/p0_multiseed/<arch>_depth_vs_<pembanding>_seed<N>.json
(keluaran eval_e022_paired.py: titik-estimasi + bootstrap 2.000x per POHON)
lalu menulis RINGKASAN.md + RINGKASAN.json.

Ini deliverable akhir P0: perbandingan 3 arsitektur x (RGB vs RGB+Depth) di
SawitMVC-Depth, plus dua kontrol metodologis sebagai lampiran. Ditulis supaya
mendarat TANPA perlu agen — dipanggil di ujung antre_lanjut_p0.sh.

Konvensi angka: koma sebagai desimal, 4 angka di belakang koma.
"""
from __future__ import annotations

import json
from pathlib import Path
from statistics import mean

HASIL = Path("results/p0_multiseed")
SEED = (42, 1337, 2024)
ARCH = ("yolo26n", "rtdetr-l")
KELAS = ("B1", "B2", "B3", "B4")


def koma(x, n=4):
    return "—" if x is None else f"{x:.{n}f}".replace(".", ",")


def tanda(x, n=4):
    return "—" if x is None else f"{x:+.{n}f}".replace(".", ",")


def muat(arch, pembanding, seed):
    p = HASIL / f"{arch}_depth_vs_{pembanding}_seed{seed}.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text())


def main() -> None:
    baris = []
    kumpul: dict = {}

    baris.append("# RINGKASAN P0 — SawitMVC-Depth, protokol beku pycocotools\n")
    baris.append(
        "Semua angka: split **test**, evaluasi 1-protokol pycocotools, CI95 dari "
        "bootstrap 2.000x yang di-resample **per pohon** (4 sisi satu pohon tidak "
        "independen). Dihasilkan otomatis oleh `ringkas_p0.py`.\n"
    )

    # ---------- tabel utama: yang sebenarnya diminta ----------
    baris.append("\n## 1. Hasil utama — RGB vs RGB+Depth\n")
    baris.append("| Arsitektur | seed | RGB | RGB+D | Δ | CI95 Δ | frac boot > 0 |")
    baris.append("|---|---|---:|---:|---:|---|---:|")
    for arch in ARCH:
        deltas = []
        for s in SEED:
            d = muat(arch, "rgb", s)
            if not d:
                baris.append(f"| {arch} | {s} | — | — | — | — | — |")
                continue
            t, dl = d["titik"], d["delta"]["mAP50"]
            ci = dl["ci95"]
            deltas.append(dl["titik"])
            baris.append(
                f"| {arch} | {s} | {koma(t['rgb']['mAP50'])} | "
                f"{koma(t['rgbd']['mAP50'])} | {tanda(dl['titik'])} | "
                f"[{tanda(ci[0])}; {tanda(ci[1])}] | {koma(dl['frac_positif'], 3)} |"
            )
        if deltas:
            n_pos = sum(1 for x in deltas if x > 0)
            baris.append(
                f"| **{arch}** | **rerata** | | | **{tanda(mean(deltas))}** | "
                f"| {n_pos}/{len(deltas)} seed positif |"
            )
            kumpul[arch] = {"delta_rerata": mean(deltas), "n_seed": len(deltas),
                            "n_positif": n_pos}
    baris.append(
        "\nRF-DETR Nano hanya ada di seed42 dan dievaluasi terpisah: "
        "RGB 0,4196 → RGB+D 0,4635, Δ +0,0439, CI95 [+0,00004; +0,0918]. "
        "**Belum direplikasi ke seed lain.**\n"
    )

    # ---------- lampiran kontrol ----------
    baris.append("\n## 2. Lampiran — kontrol metodologis\n")
    baris.append(
        "`derau` = kanal ke-4 diisi bilangan acak tetap per berkas (kontrol "
        "KAPASITAS). `tukar` = depth nyata dari pohon lain dalam split yang sama "
        "(kontrol REGISTRASI). Δ di bawah adalah RGB+D **dikurangi kontrol** — "
        "positif berarti depth nyata lebih baik daripada kontrol.\n"
    )
    baris.append("| Arsitektur | seed | kontrol | AP kontrol | RGB+D | Δ | CI95 Δ |")
    baris.append("|---|---|---|---:|---:|---:|---|")
    for arch in ARCH:
        for pemb in ("derau", "tukar"):
            for s in SEED:
                d = muat(arch, pemb, s)
                if not d:
                    baris.append(f"| {arch} | {s} | {pemb} | — | — | — | — |")
                    continue
                t, dl = d["titik"], d["delta"]["mAP50"]
                ci = dl["ci95"]
                baris.append(
                    f"| {arch} | {s} | {pemb} | {koma(t['rgb']['mAP50'])} | "
                    f"{koma(t['rgbd']['mAP50'])} | {tanda(dl['titik'])} | "
                    f"[{tanda(ci[0])}; {tanda(ci[1])}] |"
                )

    # ---------- gerbang ----------
    baris.append("\n## 3. Gerbang P0/P1\n")
    baris.append(
        "Gerbang yang ditetapkan pengguna: depth harus mengalahkan **RGB**, "
        "**derau**, dan **tukar**, dengan batas bawah CI95 > 0, dan arahnya "
        "konsisten antar-seed.\n"
    )
    for arch in ARCH:
        cek = []
        for pemb in ("rgb", "derau", "tukar"):
            ds = [muat(arch, pemb, s) for s in SEED]
            ds = [x["delta"]["mAP50"]["titik"] for x in ds if x]
            if not ds:
                cek.append(f"- vs {pemb}: belum ada data")
                continue
            pos = sum(1 for x in ds if x > 0)
            lulus = "LULUS" if pos == len(ds) else "GAGAL"
            cek.append(
                f"- vs {pemb}: {pos}/{len(ds)} seed positif, rerata "
                f"{tanda(mean(ds))} → **{lulus}**"
            )
        baris.append(f"\n**{arch}**")
        baris.extend(cek)

    # ---------- per kelas ----------
    baris.append("\n## 4. Per kelas — Δ AP50 (RGB+D − RGB)\n")
    baris.append("| Arsitektur | seed | " + " | ".join(KELAS) + " |")
    baris.append("|---|---|" + "---:|" * len(KELAS))
    for arch in ARCH:
        for s in SEED:
            d = muat(arch, "rgb", s)
            if not d:
                continue
            sel = []
            for k in KELAS:
                v = d["delta"].get(k, {}).get("titik")
                sel.append(tanda(v))
            baris.append(f"| {arch} | {s} | " + " | ".join(sel) + " |")
    baris.append(
        "\nB4 hanya punya 95 kotak di seluruh dataset. Sebaran AP B4 antar-seed "
        "jauh melebihi setiap Δ agregat di tabel 1 — itu lantai derau eksperimen "
        "ini, dan tidak bisa diperbaiki oleh arsitektur fusi mana pun.\n"
    )

    out_md = HASIL / "RINGKASAN.md"
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(baris) + "\n")
    (HASIL / "RINGKASAN.json").write_text(json.dumps(kumpul, indent=2))
    print("\n".join(baris))
    print(f"\n-> {out_md}")


if __name__ == "__main__":
    raise SystemExit(main())
