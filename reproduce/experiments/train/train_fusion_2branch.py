#!/usr/bin/env python3
"""G4/G6 (E-023): fusi MENENGAH dan AKHIR dua cabang RGB + kedalaman.

Kenapa ini ada, dalam satu kalimat: E-022 memalsukan fusi AWAL (konkatenasi di
kanal masukan), dan SR-015 menyimpulkan kegagalannya ada pada **cara memasukkan**
depth, bukan pada kandungan depth-nya — pada RT-DETR-L depth mengalahkan kontrol
deraunya sendiri justru di B4 (+0,1001 [+0,0062; +0,1618]), tetapi kanal ke-4
merusak stem 3-kanal berbobot pratlatih lebih besar daripada yang dipulihkannya.

Dua titik fusi diuji, keduanya diprediksi korpus sendiri (sapuan 28 titik fusi
Ophoff dkk., `evidence-body.tex` §174; FuseNet 4-kanal 31,95 IoU DI BAWAH RGB
32,47 sementara fusi fitur 37,29):

  --fusi mid   cabang depth ringan berjalan sampai P2/4, lalu difusikan ke
               cabang RGB sebelum P3. Stem RGB tetap 3-kanal, jadi bobot
               pratlatih masuk UTUH — inilah bedanya dengan fusi awal.

  --fusi late  kedua cabang menjalankan seluruh backbone secara terpisah, dan
               fusi terjadi pada ketiga peta fitur P3/P4/P5 sebelum head.
               Paling mahal, tetapi paling tidak mengganggu jalur RGB.

Arsitektur dibangun dengan MENURUNKAN YAML dasar ultralytics, bukan menyalinnya:
indeks `from` digeser secara terprogram. Menyalin-tempel YAML lalu menomori
ulang dengan tangan adalah sumber kesalahan senyap — model tetap terlatih,
hanya menyambung ke lapisan yang salah, dan tidak ada yang error.

Pagar keadilan sama persis dengan `train_depth4ch.py` (HSV mati di semua lengan,
modality dropout 0) supaya perbandingan mid/late/awal/RGB tetap satu protokol.
Kontrol derau dan tukar WAJIB diulang di sini — SR-015 §6: tanpa keduanya,
kenaikan apa pun tidak dapat dibedakan dari efek kapasitas.

## KAVEAT YANG BELUM TERSELESAIKAN — baca sebelum menjalankan E-023

Arsitektur ini lahir dari YAML kustom, sehingga **tidak ada bobot COCO
pratlatih** yang cocok untuknya. Seluruh lengan E-022 berangkat dari bobot
pratlatih (dan `fourch.make_inflate_callback` dipasang khusus supaya lengan
RGB-D tidak kalah karena inisialisasi). Melatih fusi menengah/akhir dari nol
lalu membandingkannya dengan lengan E-022 yang pratlatih **bukan perbandingan
yang sah** — selisihnya akan didominasi oleh ada-tidaknya pralatihan, bukan
oleh titik fusi.

Dua jalan keluar, dan pilihannya harus ditetapkan SEBELUM run pertama:

1. **Muat sebagian**: salin bobot pratlatih ke cabang RGB berdasarkan kecocokan
   nama/bentuk lapisan, biarkan cabang depth dan lapisan fusi mulai acak.
   Paling dekat dengan protokol E-022, tetapi kecocokan namanya harus
   diverifikasi lapis per lapis, bukan diasumsikan.
2. **Semua dari nol**: latih ulang JUGA baseline RGB dan lengan fusi awal tanpa
   pralatihan, sehingga seluruh matriks E-023 berada pada pijakan yang sama.
   Lebih mahal, tetapi perbandingannya bersih tanpa perlu memverifikasi apa pun.

Sampai keputusan itu diambil dan dicatat, skrip ini **belum boleh menghasilkan
angka yang dikutip**. Yang sudah tervalidasi di sini hanyalah bahwa kedua
arsitektur terbangun benar dan cabang kedalamannya benar-benar tersambung
(uji: mengubah HANYA kanal depth mengubah keluaran sebesar 6,8 dan 8,6 pada
mid dan late).
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
import time
from pathlib import Path

import torch
import torch.nn as nn
import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "experiments"
PIPELINE_ROOT = REPO_ROOT / "reproduce" / "pipeline"

sys.path.insert(0, str(PIPELINE_ROOT))
import fourch  # noqa: E402

SPLIT = EVIDENCE_ROOT / "splits_depth"


# ----------------------------------------------------------------- modul baru
class _Topeng(nn.Module):
    """Menutup kanal yang bukan milik cabang ini, TANPA mengubah jumlah kanal.

    Kenapa menutup dan bukan memotong: `parse_model` menghitung lebar kanal
    keluaran dari daftar tipe modul yang dikenalnya, dan modul kustom jatuh ke
    cabang `c2 = ch[f]` — artinya pemotongan kanal TIDAK terlihat oleh parser,
    dan kedua cabang akan dibangun seolah menerima 4 kanal padahal menerima 3
    dan 1. Itu gagal saat forward, dan memperbaikinya menuntut menambal parser.

    Dengan menutup, jumlah kanal tetap 4 sehingga pembukuan parser benar apa
    adanya, sementara cabang tetap hanya menerima informasi modalitasnya:
    bobot pada kanal yang ditutup selalu dikalikan nol, jadi tidak menerima
    gradien dan tidak menyumbang apa pun ke keluaran. Secara matematis setara
    dengan konvolusi berkanal-sedikit, hanya menyisakan sedikit bobot menganggur.
    """

    def __init__(self, c1=None, c2=None):
        super().__init__()
        m = torch.zeros(1, 4, 1, 1)
        m[:, self.KANAL] = 1.0
        self.register_buffer("topeng", m)

    def forward(self, x):
        return x * self.topeng.to(x.dtype)


class AmbilRGB(_Topeng):
    """Cabang RGB: kanal 0..2 lolos, kanal kedalaman ditutup."""

    KANAL = slice(0, 3)


class AmbilDepth(_Topeng):
    """Cabang kedalaman: hanya kanal ke-4 yang lolos."""

    KANAL = slice(3, 4)


def daftarkan_modul() -> None:
    """Sisipkan modul kustom ke namespace parser ultralytics.

    `parse_model` mencari nama modul di `globals()` modul `ultralytics.nn.tasks`,
    jadi modul kustom harus ada di sana sebelum YAML diurai.

    Hanya DUA modul yang ditambahkan, dan keduanya bebas parameter. Fusi sendiri
    TIDAK memakai modul kustom: ia dirakit dari `Concat` + `Conv` 1x1 bawaan
    ultralytics. Alasannya bukan gaya — `parse_model` menghitung lebar kanal
    keluaran lewat daftar tipe modul yang dikenalnya, dan modul multi-masukan di
    luar daftar itu jatuh ke cabang `c2 = ch[f]` yang langsung gagal untuk `f`
    berupa senarai. Memakai modul bawaan menghindari menambal parser.
    """
    from ultralytics.nn import tasks

    for m in (AmbilRGB, AmbilDepth):
        setattr(tasks, m.__name__, m)
        tasks.__dict__[m.__name__] = m


# ------------------------------------------------------------- pembangun YAML
def bangun_yaml(dasar: Path, fusi: str, nc: int, skala: str) -> dict:
    """Turunkan YAML dua cabang dari YAML dasar ultralytics.

    Memakai PETA INDEKS eksplisit (lama -> baru), bukan aritmetika offset.
    Aritmetika offset adalah tempat kesalahan senyap bersarang: model tetap
    terbangun dan tetap terlatih, hanya menyambung ke lapisan yang salah, dan
    tidak ada yang error. Peta eksplisit membuat setiap rujukan dapat diperiksa.
    """
    d = yaml.safe_load(dasar.read_text())
    bb, head = d["backbone"], d["head"]
    n_bb = len(bb)

    L: list = []
    peta: dict[int, int] = {}          # indeks lama (global) -> indeks baru

    def tambah(f, r, m, a) -> int:
        L.append([f, r, m, list(a)])
        return len(L) - 1

    # --- pembuka: simpan masukan 4-kanal, lalu pisahkan dua modalitas --------
    i_in = tambah(-1, 1, "nn.Identity", [])
    i_rgb = tambah(i_in, 1, "AmbilRGB", [])
    i_dep = tambah(i_in, 1, "AmbilDepth", [])

    def salin_cabang(masuk: int, lebar_bagi: int = 1, mulai: int = 0,
                     sampai: int | None = None,
                     lokal: dict[int, int] | None = None) -> dict[int, int]:
        """Salin sebagian backbone dasar sebagai satu cabang.

        `mulai`/`sampai` memungkinkan cabang dipotong di titik fusi lalu
        dilanjutkan SETELAH lapisan fusi ditambahkan — urutan itu wajib, karena
        ultralytics mengeksekusi lapisan secara berurutan dan `from` hanya boleh
        merujuk lapisan yang sudah ada sebelumnya.
        """
        lokal = dict(lokal or {})
        for i, (f, r, m, a) in enumerate(bb):
            if i < mulai or (sampai is not None and i > sampai):
                continue
            if i == mulai:
                f2 = masuk
            elif isinstance(f, int):
                f2 = f if f < 0 else lokal[f]
            else:
                f2 = [x if (isinstance(x, int) and x < 0) else lokal[x] for x in f]
            a2 = list(a)
            if lebar_bagi > 1 and a2 and isinstance(a2[0], int):
                a2[0] = max(16, a2[0] // lebar_bagi)
            lokal[i] = tambah(f2, r, m, a2)
        return lokal

    def fusi_di(idx_a: int, idx_b: int, lebar: int) -> int:
        """Concat + proyeksi 1x1 kembali ke `lebar`.

        Konkatenasi lalu proyeksi, bukan penjumlahan: penjumlahan memaksa kedua
        modalitas berbagi ruang fitur sejak awal, sedangkan proyeksi membiarkan
        jaringan sendiri menentukan bobot tiap modalitas — dan bobot itu dapat
        diperiksa setelah latihan, sehingga klaim "depth dipakai" bisa
        diverifikasi alih-alih diasumsikan.
        """
        c = tambah([idx_a, idx_b], 1, "Concat", [1])
        return tambah(c, 1, "Conv", [lebar, 1, 1])

    if fusi == "mid":
        TITIK = 2                       # akhir tahap P2/4 pada backbone dasar
        # Urutan penambahan menentukan urutan EKSEKUSI: cabang depth, lalu
        # cabang RGB sampai titik fusi, lalu fusi, baru sisa cabang RGB.
        dep = salin_cabang(i_dep, lebar_bagi=4, sampai=TITIK)
        rgb = salin_cabang(i_rgb, sampai=TITIK)
        f_out = fusi_di(rgb[TITIK], dep[TITIK], bb[TITIK][3][0])
        rgb = salin_cabang(f_out, mulai=TITIK + 1, lokal=rgb)
        peta.update(rgb)

    elif fusi == "late":
        rgb = salin_cabang(i_rgb)
        dep = salin_cabang(i_dep, lebar_bagi=2)
        peta.update(rgb)
        for p in (4, 6, 10):            # P3, P4, P5 pada backbone dasar
            peta[p] = fusi_di(rgb[p], dep[p], bb[p][3][0])
    else:
        raise SystemExit(f"fusi tidak dikenal: {fusi}")

    # --- head: geser rujukan absolutnya lewat peta ---------------------------
    awal_head = len(L)
    peta_head: dict[int, int] = {}
    for j, (f, r, m, a) in enumerate(head):
        lama = n_bb + j
        if isinstance(f, int):
            f2 = f if f < 0 else (peta_head.get(f) or peta[f])
        else:
            f2 = [x if (isinstance(x, int) and x < 0)
                  else (peta_head.get(x) or peta[x]) for x in f]
        peta_head[lama] = tambah(f2, r, m, a)

    d["backbone"] = L[:awal_head]
    d["head"] = L[awal_head:]
    d["nc"] = nc
    d["ch"] = 4
    d["scale"] = skala
    return d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fusi", required=True, choices=["mid", "late"])
    ap.add_argument("--dasar", default=None, help="YAML dasar; default yolo26.yaml")
    ap.add_argument("--skala", default="n")
    ap.add_argument("--modal", default="rgbd", choices=["rgbd", "derau", "tukar"])
    ap.add_argument("--depth-dir", default=str(EVIDENCE_ROOT / "depth_png"))
    ap.add_argument("--split", default="seed42")
    ap.add_argument("--epochs", type=int, default=60)
    ap.add_argument("--imgsz", type=int, default=640)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--dropout", type=float, default=0.0)
    ap.add_argument("--project", default="runs_e023")
    ap.add_argument("--name", default=None)
    ap.add_argument("--hanya-bangun", action="store_true",
                    help="tulis YAML lalu keluar, tanpa melatih")
    args = ap.parse_args()

    daftarkan_modul()
    from ultralytics import YOLO
    from ultralytics.utils import ROOT as ULTRA_ROOT

    dasar = Path(args.dasar) if args.dasar else \
        Path(ULTRA_ROOT) / "cfg" / "models" / "26" / "yolo26.yaml"
    spec = bangun_yaml(dasar, args.fusi, nc=4, skala=args.skala)

    keluar = Path(f"cfg_fusi_{args.fusi}_{args.skala}.yaml")
    keluar.write_text(yaml.safe_dump(spec, sort_keys=False))
    print(f"YAML dua cabang -> {keluar}  ({len(spec['backbone'])} lapisan backbone)")
    if args.hanya_bangun:
        return 0

    nama = args.name or f"fusi{args.fusi}_{args.modal}_seed{args.seed}"
    data = SPLIT / args.split / "data_rgbd4.yaml"

    fourch.patch_loader(args.depth_dir, dropout=args.dropout)
    model = YOLO(str(keluar))

    mulai = time.time()
    model.train(
        data=str(data), epochs=args.epochs, imgsz=args.imgsz, batch=args.batch,
        seed=args.seed, workers=args.workers, project=args.project, name=nama,
        exist_ok=True, patience=args.epochs, plots=False, deterministic=True, val=True,
        hsv_h=0.0, hsv_s=0.0, hsv_v=0.0,       # pagar keadilan #1
    )
    durasi = time.time() - mulai

    save_dir = Path(model.trainer.save_dir)
    m = model.val(data=str(data), split="test", imgsz=args.imgsz, batch=args.batch,
                  project=args.project, name=f"{nama}_test", exist_ok=True)
    hasil = {
        "run": nama, "fusi": args.fusi, "skala": args.skala, "modal": args.modal,
        "epochs": args.epochs, "imgsz": args.imgsz, "batch": args.batch,
        "seed": args.seed, "durasi_detik": round(durasi, 1),
        "catatan_evaluator": "angka ini hanya pemantau; perbandingan antar lengan "
                             "WAJIB lewat eval_e022_pycoco/paired (lihat E-025)",
        "test": {"mAP50": float(m.box.map50), "mAP50_95": float(m.box.map)},
    }
    (save_dir / "hasil.json").write_text(json.dumps(hasil, indent=2))
    print(json.dumps(hasil["test"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
