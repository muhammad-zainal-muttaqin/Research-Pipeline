# Pipeline YOLO 4-Kanal (RGB + Kedalaman) — Sawit FFB

Pipeline produksi untuk deteksi tandan dengan kamera *depth sensor* (Orbbec
Gemini dan sejenisnya). Satu bobot model melayani dua mode uji di lapangan:

| Mode | Kanal ke-4 | Kapan |
|---|---|---|
| RGB + depth | peta kedalaman kanonik | kamera Gemini terpasang |
| RGB saja | nol | kamera biasa / depth gagal |

Kuncinya **modality dropout**: saat pelatihan, sebagian citra sengaja diberi
kanal depth kosong (bawaan 25%), sehingga model belajar bekerja dengan dan
tanpa kedalaman. Tidak perlu dua model, tidak perlu logika ganti model di
aplikasi.

## Berkas

| Berkas | Fungsi |
|---|---|
| `fourch.py` | Inti: kontrak pengodean depth, patch pemuat 4-kanal + dropout, inflasi bobot pratlatih, kelas `Sawit4CH` untuk aplikasi |
| `prepare_depth.py` | Sensor uint16 mm → PNG kanonik uint8 (`--mode gemini`); pseudo-depth relatif (`--mode relative`) |
| `train_4ch.py` | Pelatihan → `best.pt` |
| `infer_4ch.py` | Inferensi citra/folder, dengan atau tanpa depth, keluar `detections.json` |

Butuh `ultralytics >= 8.4` dan `opencv-python`. Tidak ada dependensi lain.

## Kontrak kanal kedalaman — WAJIB sama saat latih dan uji

PNG uint8 satu kanal, senama dengan citranya (`foto_001.jpg` ↔ `foto_001.png`),
sejajar (*registered*) ke RGB lewat fitur *depth-to-color alignment* SDK sensor.

- `0` = tidak valid / tidak ada data (lubang sensor, atau seluruh frame saat
  mode RGB).
- `1..255` = *inverse depth* pada rentang metrik **tetap** 0,3–8 m:
  dekat → 255, jauh → 1.

Rentang metrik itu dibekukan bersama bobot (`fourch.Z_NEAR/Z_FAR`). Jangan
menormalkan per-citra pada data sensor — itu membuang jarak absolut dan membuat
nilai piksel tidak sebanding antar-frame.

## Alur kerja

```bash
# 1. konversi depth mentah sensor -> kanonik
python prepare_depth.py --src depth_mentah/ --dst depth_kanonik/ --mode gemini

# 2. latih (data.yaml lihat templat di bawah)
python train_4ch.py --data data_4ch.yaml --depth-dir depth_kanonik/ \
    --epochs 60 --batch 32 --name gemini_v1

# 3. uji lapangan
python infer_4ch.py --weights runs4ch/gemini_v1/weights/best.pt \
    --source foto_uji/ --depth-dir depth_kanonik/     # dengan depth
python infer_4ch.py --weights runs4ch/gemini_v1/weights/best.pt \
    --source foto_uji/                                # RGB saja
```

Templat `data_4ch.yaml` (layout dataset sama persis dengan SawitMVC):

```yaml
path: /path/absolut/dataset
train: train.txt        # daftar path citra, absolut atau relatif ke path
val: val.txt
test: test.txt
channels: 4             # <- ini yang membuat ultralytics membangun model 4-kanal
nc: 4
names:
  0: B1
  1: B2
  2: B3
  3: B4
```

Folder depth **tidak** disebut di yaml — ia diberikan lewat `--depth-dir` dan
dicocokkan per nama berkas. Citra tanpa PNG depth tetap ikut dilatih dengan
kanal nol (identik dengan mode RGB lapangan).

## Integrasi ke aplikasi yang sudah ada

Ganti pemanggilan YOLO lama dengan tiga baris:

```python
from fourch import Sawit4CH, encode_metric_depth

det = Sawit4CH("best.pt")                      # sekali, saat aplikasi mulai
hasil = det.predict(frame_bgr)                                 # kamera biasa
hasil = det.predict(frame_bgr, encode_metric_depth(depth_mm))  # Gemini
# hasil = {"deteksi": [{kelas, nama, skor, kotak_xyxy}...],
#          "hitung": {"B1": n, ...}, "pakai_depth": bool}
```

`Sawit4CH` juga menerima bobot 3-kanal lama — ia mendeteksi jumlah kanal dari
bobotnya dan menyusun masukan yang sesuai, jadi penggantian model tidak
mengubah kode aplikasi.

Ekspor ke ONNX/TensorRT bila diperlukan: `YOLO("best.pt").export(format="onnx")`
— masukan menjadi tensor `(1, 4, H, W)`; komposisi kanal (`fourch.compose`)
tetap dilakukan aplikasi sebelum memanggil model.

## Detail teknis yang sudah diverifikasi

- Ultralytics 8.4 membalik urutan kanal BGR→RGB **hanya untuk 3 kanal** — pada
  4 kanal, urutan `[B,G,R,D]` konsisten antara jalur latih dan prediksi
  (diverifikasi di `engine/predictor.py` dan `data/augment.py`).
- Transfer bobot bawaan ultralytics melewati conv pertama karena bentuknya
  beda (3→4 kanal). `train_4ch.py` mengisinya lewat callback: bobot RGB
  pratlatih disalin **dalam urutan BGR**, kanal depth mulai dari nol — model
  mulai persis dari perilaku RGB pratlatih.
- Pemuat 4-kanal tidak menggandakan dataset di disk; kanal depth ditempel di
  memori saat pemuatan.

## Peringatan jujur — pseudo-depth vs depth sensor

Bobot yang dilatih dengan pseudo-depth DA3 (`--mode relative`) memakai
kedalaman **relatif per-citra**; distribusinya berbeda dari inverse-depth
metrik sensor. Jangan mencampur keduanya dalam satu bobot produksi: begitu
data Gemini asli terkumpul, **latih ulang** (atau setel-halus) dengan
`--mode gemini`. Perlu diketahui pula: eksperimen E-006 memalsukan hipotesis
bahwa *pseudo*-depth memisahkan tandan dari latarnya — depth sensor asli
adalah pengukuran fisik independen yang belum diuji, dan pipeline ini yang
membuatnya bisa diuji begitu datanya ada.
