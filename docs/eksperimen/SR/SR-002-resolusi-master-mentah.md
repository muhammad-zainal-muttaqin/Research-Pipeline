# SR-002 — Master mentah 3024×4032 sebagai jalan keluar untuk B4

**Ide:** kalau resolusi bagian dari bottleneck, latih pada piksel penuh
**Eksperimen:** E-002 · **Putusan: TERBLOKIR → DIBUKA oleh E-015** · 2026-07-21

> **PEMBARUAN (E-015, 2026-07-21).** Blokade di SR ini — nama berkas master
> mentah tidak unik global sehingga pemetaan raw ↔ anotasi mustahil dari nama —
> **sudah dibuka.** `match_raw.py` memetakan 3.992/3.992 citra lewat isi
> (tanda tangan citra ternormalkan), nol ambigu, skor terendah 0,9985. Master
> 3024×4032 kini dapat dipakai tanpa anotasi ulang; `build_master_ds.py`
> merakit dataset YOLO yang menunjuk ke piksel master. Lihat E-015 dan E-018.

---

## 1. Masalah

**B4 adalah kelas terburuk: AP50 = 0,354.** Definisinya di dataset — *"small,
deeply positioned, black to green"* — menjelaskan kenapa: tandan B4 kecil,
tertanam dalam di ketiak pelepah, dan berwarna gelap seperti latarnya.

SawitMVC adalah versi **terkompresi** ke 960×1280. Baseline DiB melatih pada
`imgsz=640`, artinya citra diperkecil lagi. Untuk objek sekecil B4, detail yang
membedakan tandan dari bayangan pelepah bisa hilang sama sekali.

Ini **bukan pertanyaan tuning.** Melatih `imgsz=1280` pada sumber 960×1280 hanya
memperbesar piksel yang detailnya sudah hilang saat kompresi. Melatih pada
sumber 3024×4032 memberi detail yang benar-benar baru. Dua eksperimen berbeda.

## 2. Ide

Master mentah `Sawit` adalah dataset yang sama sebelum dikompresi. Kalau rasio
aspeknya identik, koordinat YOLO **ternormalisasi** dari SawitMVC berlaku persis
di raw tanpa anotasi ulang — anotasi mahal itu bisa dipakai ulang gratis pada
resolusi 9,9× lebih besar.

## 3. Solusi

Inventarisasi langsung `/workspace/Sawit/data`: hitung berkas, resolusi, rasio
aspek, tabrakan nama, dan properti video.

## 4. Hasil

| | Sawit (raw) | SawitMVC |
|---|---|---|
| Resolusi | **3024 × 4032** | 960 × 1280 |
| Rasio aspek | 0,75 | 0,75 — **identik** |
| JPG | 3.992 (16 GB) | 3.992 (2,3 GB) |
| Video | **45 MP4** 1920×1080 | — |
| Anotasi | tidak ada | lengkap |

Premis utamanya **benar**: rasio aspek identik → label transferable, luas piksel
9,9×.

**Tetapi ada penghalang yang menggagalkan pelaksanaannya:**

Nama berkas raw **tidak unik secara global**. Dari 3.992 berkas hanya **1.352
nama unik** — **936 nama kembar** antar folder `Kelompok N`. Contoh:
`LONSUM_A21A_044_3.jpg` ada di `Kelompok 2` *dan* `Kelompok 5`, dan itu **dua
pohon fisik berbeda**. Ditambah penomoran raw 3 digit (`_001_`) vs MVC 4 digit
(`_0001_`), pemetaan raw ↔ anotasi **tidak dapat dilakukan dari nama berkas**.

Video juga hanya bernama cap waktu (`VID_20260205_090556.mp4`), semuanya dari
`Kelompok 6`, tanpa ID pohon.

## 5. Putusan — TIDAK KONKLUSIF (terblokir)

Idenya sehat dan premisnya terverifikasi, tetapi tidak dapat dijalankan sampai
pemetaan raw ↔ anotasi tersedia. Ini **kegagalan pelaksanaan, bukan kegagalan
hipotesis** — hipotesis resolusinya sendiri belum diuji sama sekali.

## 6. Dampak

Dua hal:

1. **Eksperimen resolusi penuh ditunda.** Pemetaan dapat direkonstruksi lewat
   pencocokan berbasis isi (perceptual hash / *downscale-and-compare*), karena
   MVC secara harfiah diturunkan dari raw sehingga padanan 1:1 pasti ada dan
   dapat diverifikasi. Alternatif yang jauh lebih baik: tabel pemetaan dari tim
   pengumpul data.
2. **Video menjadi aset tak terduga.** Risiko terbesar rencana DA3 multi-view
   adalah *baseline* ~90° antar sisi. Ratusan frame mengelilingi satu pohon
   memberi *baseline* kecil — kondisi ideal untuk geometri multi-view. Urutan
   uji diubah karena temuan ini: video lebih dulu (→ SR-003).

## 7. Reproduksi

```bash
# resolusi & rasio aspek
python3 -c "from PIL import Image; print(Image.open('/workspace/Sawit/data/Damimas/Kelompok 1/DAMIMAS_A21B_001_1.jpg').size)"

# tabrakan nama
cd /workspace/Sawit/data && python3 - <<'PY'
from collections import defaultdict
from pathlib import Path
d = defaultdict(list)
for p in Path(".").rglob("*.jpg"): d[p.name].append(str(p.parent))
print("berkas", sum(len(v) for v in d.values()), "| nama unik", len(d),
      "| kembar", sum(1 for v in d.values() if len(v) > 1))
PY
```
