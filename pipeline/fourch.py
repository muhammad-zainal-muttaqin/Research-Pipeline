#!/usr/bin/env python3
"""Inti pipeline YOLO 4-kanal (RGB + kedalaman) untuk deteksi tandan sawit.

Dirancang untuk kamera stereo/ToF (mis. Orbbec Gemini) yang memberi peta
kedalaman metrik sejajar dengan RGB. Satu bobot model melayani DUA mode uji:

  - RGB + depth  : kanal ke-4 diisi peta kedalaman kanonik
  - RGB saja     : kanal ke-4 diisi nol

Ini dimungkinkan oleh *modality dropout* saat pelatihan: sebagian citra latih
sengaja diberi kanal depth kosong, sehingga model tidak pernah bergantung mati
pada kanal itu. Nilai nol dengan demikian punya arti tunggal di seluruh
pipeline: "tidak ada data kedalaman".

KONTRAK KANAL KEDALAMAN (wajib sama saat latih dan saat uji lapangan):
  - PNG uint8, satu kanal, ukuran sama dengan RGB, sejajar (registered) ke RGB.
  - 0            = tidak valid / tidak ada data.
  - 1..255       = kedalaman terbalik (inverse depth) pada rentang metrik tetap
                   [Z_NEAR, Z_FAR] meter: dekat -> 255, jauh -> 1.
  Konversi dari sensor: pakai prepare_depth.py, jangan menormalkan per-citra —
  normalisasi per-citra membuang informasi jarak absolut dan membuat nilai
  piksel tidak sebanding antar-frame.
"""
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np

# Rentang metrik kanonik. Gemini 2 andal kira-kira 0,15–10 m; pohon difoto
# 2–6 m. Rentang ini DIBEKUKAN bersama bobot model — mengubahnya berarti
# melatih ulang.
Z_NEAR = 0.3   # meter
Z_FAR = 8.0    # meter

CLASSES = ["B1", "B2", "B3", "B4"]

# flag pemuatan internal (nilai yang mustahil dipakai cv2)
_TRAIN_FLAG = -997   # dengan modality dropout
_EVAL_FLAG = -999    # tanpa dropout

_STATE = {"depth_dir": None, "dropout": 0.0}


# ---------------------------------------------------------------- pengodean
def encode_metric_depth(depth_mm: np.ndarray) -> np.ndarray:
    """uint16 milimeter (keluaran umum sensor) -> kanal kanonik uint8.

    Piksel 0 pada masukan (lubang sensor) tetap 0 pada keluaran.
    """
    z = depth_mm.astype(np.float32) / 1000.0
    valid = z > 0
    z = np.clip(z, Z_NEAR, Z_FAR)
    inv = (1.0 / z - 1.0 / Z_FAR) / (1.0 / Z_NEAR - 1.0 / Z_FAR)
    out = np.round(1 + inv * 254).astype(np.uint8)
    out[~valid] = 0
    return out


def encode_relative_depth(d: np.ndarray) -> np.ndarray:
    """Peta kedalaman RELATIF (mis. Depth Anything) -> kanal kanonik uint8.

    Hanya untuk pralatihan dengan pseudo-depth; skala absolutnya tidak berarti.
    Nilai disebar ke 1..255 per-citra (0 dicadangkan untuk "tidak ada data").
    """
    d = d.astype(np.float32)
    lo, hi = float(d.min()), float(d.max())
    if hi - lo < 1e-6:
        return np.zeros(d.shape[:2], np.uint8)
    return (1 + (d - lo) / (hi - lo) * 254).astype(np.uint8)


def compose(bgr: np.ndarray, depth8: np.ndarray | None) -> np.ndarray:
    """Susun masukan 4-kanal [B,G,R,D]. depth8=None -> kanal nol (mode RGB)."""
    if depth8 is None:
        depth8 = np.zeros(bgr.shape[:2], np.uint8)
    elif depth8.shape[:2] != bgr.shape[:2]:
        depth8 = cv2.resize(depth8, (bgr.shape[1], bgr.shape[0]),
                            interpolation=cv2.INTER_NEAREST)
    return np.dstack([bgr, depth8])


def load_depth_for(image_path: str | Path, depth_dir: str | Path | None) -> np.ndarray | None:
    """Cari PNG kedalaman kanonik berdasarkan nama berkas citra."""
    if depth_dir is None:
        return None
    p = Path(depth_dir) / f"{Path(image_path).stem}.png"
    if not p.exists():
        return None
    return cv2.imread(str(p), cv2.IMREAD_GRAYSCALE)


# ---------------------------------------------------------------- pelatihan
def patch_loader(depth_dir: str | Path | None, dropout: float = 0.25) -> None:
    """Ajari pemuat data ultralytics membaca 4 kanal, tanpa menyalin dataset.

    Citra dibaca dari JPEG asli; kanal kedalaman ditempel di memori. Pada
    dataset LATIH (augment=True) kanal depth diganti nol dengan peluang
    `dropout` — inilah yang membuat satu bobot bisa dipakai dengan atau tanpa
    depth di lapangan. Dataset VALIDASI selalu memakai depth apa adanya.
    """
    _STATE["depth_dir"] = Path(depth_dir) if depth_dir else None
    _STATE["dropout"] = float(dropout)

    import random
    import ultralytics.data.base as base
    from ultralytics.data.base import BaseDataset

    if getattr(base, "_fourch_patched", False):
        return

    orig_init = BaseDataset.__init__

    def patched_init(self, *a, **kw):
        orig_init(self, *a, **kw)
        if getattr(self, "channels", 3) == 4:
            self.cv2_flag = _TRAIN_FLAG if getattr(self, "augment", False) else _EVAL_FLAG

    BaseDataset.__init__ = patched_init

    orig_imread = base.imread

    def imread_4ch(filename, flags=cv2.IMREAD_COLOR):
        if flags not in (_TRAIN_FLAG, _EVAL_FLAG):
            return orig_imread(filename, flags)
        bgr = cv2.imread(str(filename), cv2.IMREAD_COLOR)
        if bgr is None:
            return None
        d8 = load_depth_for(filename, _STATE["depth_dir"])
        if flags == _TRAIN_FLAG and random.random() < _STATE["dropout"]:
            d8 = None
        return compose(bgr, d8)

    base.imread = imread_4ch
    base._fourch_patched = True


def make_inflate_callback(pretrained: str | Path):
    """Callback ultralytics: isi conv pertama 4-kanal dari bobot pratlatih 3-kanal.

    Tanpa ini, conv pertama mulai dari inisialisasi acak (transfer bobot
    ultralytics melewati tensor yang bentuknya beda). Bobot RGB pratlatih
    disalin dengan urutan DIBALIK ke BGR — jalur 4-kanal ultralytics TIDAK
    membalik kanal (pembalikan BGR->RGB hanya berlaku untuk 3 kanal), jadi
    masukan model adalah [B,G,R,D]. Kanal depth diinisialisasi nol: model mulai
    persis dari perilaku RGB pratlatih dan belajar memakai depth secara
    bertahap.
    """
    import torch
    import torch.nn as nn

    def fill(module, w3) -> bool:
        for m in module.modules():
            if isinstance(m, nn.Conv2d) and m.in_channels == 4:
                with torch.no_grad():
                    m.weight[:, :3] = w3[:, [2, 1, 0]].to(m.weight.device)  # RGB -> BGR
                    m.weight[:, 3] = 0.0
                return True
        return False

    def cb(trainer):
        sd = torch.load(str(pretrained), map_location="cpu", weights_only=False)
        src = (sd.get("model") or sd).float().state_dict()
        w3 = next(v for v in src.values()
                  if v.ndim == 4 and v.shape[1] == 3)  # conv pertama pratlatih
        ok = fill(trainer.model, w3)
        # EMA disalin SEBELUM callback ini menyala (trainer.py: ModelEMA lalu
        # on_pretrain_routine_end), dan best.pt menyimpan EMA — wajib ditambal juga.
        ema = getattr(getattr(trainer, "ema", None), "ema", None)
        if ema is not None:
            ok = fill(ema, w3) and ok
        if ok:
            print("fourch: conv pertama diisi dari bobot pratlatih (BGR), kanal depth = 0 (model + EMA)")
        else:
            print("fourch: PERINGATAN — conv 4-kanal tidak ditemukan, inflasi dilewati")

    return cb


# ---------------------------------------------------------------- inferensi
class Sawit4CH:
    """Pembungkus inferensi untuk aplikasi lapangan.

    Ganti pemanggilan YOLO lama di aplikasi dengan:

        det = Sawit4CH("best.pt")
        hasil = det.predict(frame_bgr)                    # RGB saja
        hasil = det.predict(frame_bgr, depth8=peta_uint8) # RGB + Gemini

    `depth8` adalah kanal kanonik (lihat kontrak di atas); dari frame mentah
    sensor (uint16 mm) panggil dulu `encode_metric_depth`.
    """

    def __init__(self, weights: str | Path, device=None, conf: float = 0.25,
                 imgsz: int = 640):
        from ultralytics import YOLO
        self.model = YOLO(str(weights))
        self.device = device
        self.conf = conf
        self.imgsz = imgsz
        self.four_channel = self._detect_channels() == 4

    def _detect_channels(self) -> int:
        import torch.nn as nn
        for m in self.model.model.modules():
            if isinstance(m, nn.Conv2d):
                return m.in_channels
        return 3

    def predict(self, bgr: np.ndarray, depth8: np.ndarray | None = None,
                conf: float | None = None):
        """-> daftar dict {kelas, nama, skor, kotak_xyxy} + hitungan per kelas."""
        inp = compose(bgr, depth8) if self.four_channel else bgr
        r = self.model.predict(inp, imgsz=self.imgsz, verbose=False,
                               conf=conf if conf is not None else self.conf,
                               device=self.device)[0]
        dets = [{
            "kelas": int(c),
            "nama": CLASSES[int(c)] if int(c) < len(CLASSES) else str(int(c)),
            "skor": round(float(s), 4),
            "kotak_xyxy": [round(float(v), 1) for v in b],
        } for b, s, c in zip(r.boxes.xyxy.cpu().numpy(),
                             r.boxes.conf.cpu().numpy(),
                             r.boxes.cls.cpu().numpy())]
        hitung = {n: 0 for n in CLASSES}
        for d in dets:
            hitung[d["nama"]] = hitung.get(d["nama"], 0) + 1
        return {"deteksi": dets, "hitung": hitung, "pakai_depth": depth8 is not None}
