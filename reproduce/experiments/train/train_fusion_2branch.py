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

## Dukungan RT-DETR (`--arch rtdetr-l`)

`bangun_yaml()` sudah diverifikasi juga menurunkan `rtdetr-l.yaml` (satu-satunya
skala yang tersedia di YAML dasar RT-DETR adalah `l` — panggil dengan
`--skala l`). Dua hal yang BERBEDA dari yolo26 dan sudah ditangani secara
eksplisit, bukan lewat konstanta yang dipakai bersama:

1. **Titik fusi berbeda posisi.** Untuk yolo26, akhir stage P2/4 ada di lapisan
   backbone indeks 2. Untuk rtdetr-l, backbone dimulai `HGStem` (0, sudah
   P2/4) lalu `HGBlock` stage1 (1, masih P2/4) baru `DWConv` yang turun ke
   P3/8 (2) — akhir stage P2/4 yang sesungguhnya untuk rtdetr-l adalah indeks
   1, BUKAN 2. P3/P4/P5 juga di indeks berbeda: (3, 7, 9), bukan (4, 6, 10).
   Nilai ini sekarang parameter `ARSITEKTUR[...]`, bukan konstanta hardcode.

2. **`HGStem`/`HGBlock` menaruh lebar keluaran (`c2`) di `args[1]`, bukan
   `args[0]`.** `parse_model` membacanya `c1, cm, c2 = ch[f], args[0], args[1]`
   — berbeda dari `Conv`/`C3k2`/`DWConv` yang memakai `args[0]` langsung
   sebagai `c2`. Memakai `args[0]` mentah di titik fusi rtdetr-l akan
   mengambil kanal TENGAH (`cm`), bukan `c2` — model tetap terbangun dan
   forward pass tetap sukses TANPA error (dikonfirmasi lewat eksekusi CPU),
   hanya lebar proyeksi fusinya salah. Inilah persis kegagalan senyap yang
   jadi alasan desain PETA INDEKS di berkas ini, hanya bersembunyi satu lapis
   lebih dalam (di lebar kanal `args`, bukan di indeks `from`). Ditangani oleh
   `lebar_keluar()`/`sunting_lebar()` di bawah, yang membaca TIPE modul di
   titik potong sebelum menafsirkan `args`.

3. **`YOLO(yaml)` TIDAK otomatis mengalihkan ke RT-DETR untuk YAML custom** —
   koreksi terhadap dugaan awal bahwa `ultralytics/models/yolo/model.py:80-83`
   ("`if "RTDETR" in self.model.model[-1]._get_name()`") membuat baris
   `model = YOLO(...)` bekerja apa adanya untuk RT-DETR. Cek itu berjalan
   SETELAH model dibangun, tapi pembangunannya sendiri butuh `self.task`
   sudah terisi lebih dulu, dan `guess_model_task` menebak task dari nama
   modul head lewat substring `"detect"` — `"rtdetrdecoder"` tidak
   mengandungnya, jadi task jatuh ke `None` dan `_smart_load` melempar
   `NotImplementedError` SEBELUM cek RTDETR itu sempat jalan. Dikonfirmasi
   gagal identik untuk `rtdetr-l.yaml` BAWAAN ultralytics tanpa modifikasi
   apa pun — bukan cacat khusus YAML turunan berkas ini. Solusinya memakai
   kelas `ultralytics.RTDETR` langsung (ia mem-pass `task="detect"` eksplisit
   ke `Model.__init__`, melewati tebakan itu sama sekali) — lihat
   `ARSITEKTUR["rtdetr-l"]["kelas_model"]` dan pemilihan kelas di `main()`.

`rtdetr-resnet50.yaml`/`resnet101.yaml` TIDAK didukung dan TIDAK akan
ditambahkan lewat pola yang sama: `ResNetLayer` tidak menurunkan `c1` dari
`ch[f]` sama sekali (`parse_model` punya cabang khusus untuknya yang tidak
pernah menimpa `args[0]`) — `c1` di YAML-nya adalah literal hardcode yang
menyambung manual angka-per-angka ke `c2` lapisan sebelumnya. Premis "modul
auto-derive lebar dari `ch[f]`" yang mendasari topeng+peta-indeks tidak
berlaku untuk backbone ini; memakainya butuh menulis ulang penanganan
channel-args di sepanjang rantai `ResNetLayer`, bukan penyesuaian indeks.
Dikonfirmasi lewat eksekusi: construct berhasil (nn.Module tidak memeriksa
kecocokan kanal saat dibangun) tapi forward pass gagal keras dengan
`RuntimeError: ... expected input[...] to have 16 channels, but got 4`.
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
    dan 1. Dengan menutup, pembukuan parser benar apa adanya sementara tiap
    cabang tetap hanya menerima informasi modalitasnya: bobot pada kanal yang
    ditutup selalu dikali nol, tidak menerima gradien, tidak menyumbang keluaran.

    Topeng dihitung DARI BENTUK MASUKAN, bukan dari buffer tetap 4-kanal.
    Alasannya konkret: `YOLO(yaml)` membangun model sekali dengan `ch=3` untuk
    menghitung stride sebelum pelatihan menggantinya dengan `ch=4` dari
    `data.yaml`. Buffer tetap membuat lintasan pertama itu gagal dengan
    "size of tensor a (3) must match tensor b (4)" — dan gagalnya di dalam
    konstruktor, sebelum satu epoch pun berjalan.
    """

    def __init__(self, c1=None, c2=None):
        super().__init__()

    def forward(self, x):
        c = x.shape[1]
        if c <= 3:
            # Lintasan penghitung stride (3 kanal): tidak ada kanal kedalaman
            # untuk dipisahkan. Cabang RGB melihat citra apa adanya; cabang
            # kedalaman melihat nol — bentuknya tetap benar, dan nilai ini
            # tidak pernah dipakai untuk belajar.
            return x if self.KANAL.start == 0 else torch.zeros_like(x)
        topeng = torch.zeros(1, c, 1, 1, dtype=x.dtype, device=x.device)
        topeng[:, self.KANAL] = 1.0
        return x * topeng


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


# --------------------------------------------------- lebar kanal per-tipe-modul
# `parse_model` (ultralytics/nn/tasks.py) tidak menaruh c2 di `args[0]` untuk
# SEMUA modul. `HGStem`/`HGBlock` memakai `c1, cm, c2 = ch[f], args[0], args[1]`
# — c2 ada di args[1], args[0] adalah kanal TENGAH (cm). Modul lain yang dipakai
# backbone (`Conv`, `C3k2`, `DWConv`, ...) memakai args[0] langsung sebagai c2.
# Dua fungsi di bawah membaca TIPE modul di titik potong sebelum menafsirkan
# args, supaya fusi mid/late pada backbone HGNetv2 (rtdetr-l) tidak diam-diam
# memproyeksikan ke lebar kanal yang salah (lihat KAVEAT RT-DETR di kepala
# berkas — bug ini lolos tanpa error di construct maupun forward pass).
_MODUL_CM_C2 = frozenset({"HGStem", "HGBlock"})


def lebar_keluar(modul: str, a: list) -> int:
    """Kanal keluaran (c2) sebuah lapisan backbone, dari args mentah YAML-nya."""
    return a[1] if modul in _MODUL_CM_C2 else a[0]


def sunting_lebar(modul: str, a2: list, lebar_bagi: int) -> None:
    """Susutkan lebar kanal `a2` in-place untuk cabang depth yang diringankan.

    Untuk `HGStem`/`HGBlock`, kanal tengah (`cm`, args[0]) DAN keluaran (`c2`,
    args[1]) sama-sama disusutkan — keduanya lebar riil, bukan hanya c2.
    Untuk modul lain, hanya args[0] (yaitu c2) yang disusutkan.
    """
    if modul in _MODUL_CM_C2:
        for idx in (0, 1):
            if idx < len(a2) and isinstance(a2[idx], int):
                a2[idx] = max(8, a2[idx] // lebar_bagi)
    elif a2 and isinstance(a2[0], int):
        a2[0] = max(16, a2[0] // lebar_bagi)


# ------------------------------------------------------------- pembangun YAML
def bangun_yaml(dasar: Path, fusi: str, nc: int, skala: str,
                 titik_mid: int, titik_late: tuple[int, ...]) -> dict:
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
            if lebar_bagi > 1:
                sunting_lebar(m, a2, lebar_bagi)
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
        TITIK = titik_mid               # akhir tahap P2/4 pada backbone dasar
        # Urutan penambahan menentukan urutan EKSEKUSI: cabang depth, lalu
        # cabang RGB sampai titik fusi, lalu fusi, baru sisa cabang RGB.
        dep = salin_cabang(i_dep, lebar_bagi=4, sampai=TITIK)
        rgb = salin_cabang(i_rgb, sampai=TITIK)
        lebar = lebar_keluar(bb[TITIK][2], bb[TITIK][3])
        f_out = fusi_di(rgb[TITIK], dep[TITIK], lebar)
        rgb = salin_cabang(f_out, mulai=TITIK + 1, lokal=rgb)
        peta.update(rgb)

    elif fusi == "late":
        rgb = salin_cabang(i_rgb)
        dep = salin_cabang(i_dep, lebar_bagi=2)
        peta.update(rgb)
        for p in titik_late:            # P3, P4, P5 pada backbone dasar
            lebar = lebar_keluar(bb[p][2], bb[p][3])
            peta[p] = fusi_di(rgb[p], dep[p], lebar)
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

    # Skala DIBEKUKAN sebagai satu-satunya entri `scales`, bukan lewat kunci
    # `scale`. Alasannya cacat nyata di ultralytics, bukan preferensi gaya:
    # `yaml_model_load` menimpa `d["scale"]` TANPA SYARAT dengan hasil
    # `guess_model_scale(path)`, yang menebak skala dari NAMA BERKAS lewat regex
    # `yolo(e-)?[v]?\d+([nslmx])`. Nama berkas turunan kita tidak cocok pola itu,
    # sehingga tebakannya string kosong dan `parse_model` jatuh ke
    # `next(iter(scales.keys()))` — kunci PERTAMA — sambil hanya mencetak
    # peringatan. Akibatnya `--skala l` akan diam-diam membangun model `n`:
    # 2,5 jt param, bukan 26 jt, tanpa error.
    #
    # Dengan menyisakan satu entri saja, jalur fallback itu justru menjadi benar
    # menurut konstruksi — apa pun yang ditebak dari nama berkas, satu-satunya
    # skala yang tersedia adalah yang diminta.
    if "scales" in d:
        if skala not in d["scales"]:
            raise SystemExit(f"skala '{skala}' tidak ada di YAML dasar; "
                             f"tersedia: {sorted(d['scales'])}")
        d["scales"] = {skala: d["scales"][skala]}
    d["scale"] = skala
    return d


# -------------------------------------------------------- arsitektur dasar
# Titik fusi (indeks lapisan backbone) TIDAK bisa dibagi antar arsitektur
# lewat konstanta tunggal — posisinya bergantung struktur backbone masing-
# masing YAML dasar. Diverifikasi lewat pembacaan langsung YAML + forward
# pass CPU (lihat KAVEAT RT-DETR di kepala berkas), bukan diasumsikan simetris
# dengan yolo26.
ARSITEKTUR: dict[str, dict] = {
    "yolo26": {
        "path": "26/yolo26.yaml",
        # akhir stage P2/4: bb[2] adalah C3k2 tepat setelah conv turun ke P2/4.
        "titik_mid": 2,
        "titik_late": (4, 6, 10),   # P3, P4, P5
    },
    "rtdetr-l": {
        "path": "rt-detr/rtdetr-l.yaml",
        # akhir stage P2/4: bb[0]=HGStem (sudah P2/4), bb[1]=HGBlock stage1
        # (masih P2/4) — bb[2] SUDAH DWConv turun ke P3/8. Titik yang benar
        # untuk fusi P2/4 adalah 1, bukan 2 seperti yolo26.
        "titik_mid": 1,
        "titik_late": (3, 7, 9),    # P3, P4, P5 — sama seperti rujukan head
                                     # rtdetr-l.yaml asli ([[21, 24, 27], ...]
                                     # dibaca dari backbone indeks 3/7/9)
        "skala_wajib": "l",         # satu-satunya skala di YAML dasar RT-DETR
        # `YOLO(yaml)` TIDAK otomatis mengalihkan ke RT-DETR untuk YAML custom
        # (terverifikasi juga gagal untuk rtdetr-l.yaml BAWAAN tanpa modifikasi
        # apa pun): `guess_model_task` menebak task dari nama modul head lewat
        # substring "detect", dan "rtdetrdecoder" tidak mengandungnya -> task
        # jatuh ke None -> `NotImplementedError`. Kelas `RTDETR` mem-pass
        # `task="detect"` eksplisit ke `Model.__init__`, menghindari tebakan
        # itu sama sekali. WAJIB dipakai untuk arsitektur ini.
        "kelas_model": "RTDETR",
    },
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fusi", required=True, choices=["mid", "late"])
    ap.add_argument("--arch", default="yolo26", choices=sorted(ARSITEKTUR),
                    help="arsitektur dasar (menentukan titik fusi & YAML default)")
    ap.add_argument("--dasar", default=None,
                    help="path YAML dasar; default diturunkan dari --arch. "
                         "Titik fusi tetap dari --arch walau path ditimpa.")
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

    arch_cfg = ARSITEKTUR[args.arch]
    if "skala_wajib" in arch_cfg and args.skala != arch_cfg["skala_wajib"]:
        raise SystemExit(
            f"--arch {args.arch} hanya punya skala '{arch_cfg['skala_wajib']}' "
            f"di YAML dasar; panggil dengan --skala {arch_cfg['skala_wajib']} "
            f"(dapat: --skala {args.skala})"
        )

    daftarkan_modul()
    from ultralytics.utils import ROOT as ULTRA_ROOT
    if arch_cfg.get("kelas_model") == "RTDETR":
        from ultralytics import RTDETR as KelasModel
    else:
        from ultralytics import YOLO as KelasModel

    dasar = Path(args.dasar) if args.dasar else \
        Path(ULTRA_ROOT) / "cfg" / "models" / arch_cfg["path"]
    spec = bangun_yaml(dasar, args.fusi, nc=4, skala=args.skala,
                       titik_mid=arch_cfg["titik_mid"],
                       titik_late=arch_cfg["titik_late"])

    keluar = Path(f"cfg_fusi_{args.fusi}_{args.arch}_{args.skala}.yaml")
    keluar.write_text(yaml.safe_dump(spec, sort_keys=False))
    print(f"YAML dua cabang -> {keluar}  ({len(spec['backbone'])} lapisan backbone)")
    if args.hanya_bangun:
        return 0

    nama = args.name or f"fusi{args.fusi}_{args.arch}_{args.modal}_seed{args.seed}"
    data = SPLIT / args.split / "data_rgbd4.yaml"

    fourch.patch_loader(args.depth_dir, dropout=args.dropout)
    model = KelasModel(str(keluar))

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
