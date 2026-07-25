# SR-004 — DA3 multi-view pada 4 dan 8 sisi foto asli

**Ide I-2** · **Eksperimen:** E-005 · **Putusan: DIKONFIRMASI** · 2026-07-21

---

## 1. Masalah

SR-003 membuktikan DA3 andal pada video orbit. Tetapi video **bukan** data yang
sebenarnya kita punya. Dataset berisi foto dari **4 posisi berjarak ~90°**
(908 pohon) atau 8 posisi ~45° (45 pohon).

Perbedaan itu bukan sepele. Rekonstruksi multi-view mengandalkan tumpang tindih
antar-pandangan. Pada 90°:

- *baseline* lebar, tumpang tindih rendah,
- objeknya menutupi dirinya sendiri (pelepah menghalangi sisi jauh),
- kanopi sawit nyaris simetris berputar sehingga rawan *visual aliasing*.

Kalau geometri gagal di sini, seluruh jalur geometris (I-6, I-7) gugur —
karena video hanya tersedia untuk 45 pohon dari `Kelompok 6`, sedangkan foto
tersedia untuk seluruh 953 pohon.

## 2. Ide

Uji DA3 langsung pada 4 dan 8 sisi foto, dengan **kebenaran acuan objektif**
yang tersedia gratis: geometri pengambilan datanya diketahui. Operator memutari
pohon pada posisi berjarak sama, jadi langkah sudut antar-sisi berurutan
**seharusnya 90°** (4 sisi) atau **45°** (8 sisi).

Ini uji yang jujur karena acuannya tidak berasal dari model mana pun.

Pohon 8-sisi memberi uji ganda: lebih ketat (45°) sekaligus pembanding
*baseline* yang lebih rapat.

**Yang akan memalsukan:** susunan pusat kamera tidak lebih baik daripada tebakan
acak, atau urutan melingkar sisi salah.

## 3. Solusi

`experiments/da3_sides_test.py`. Untuk tiap pohon: jalankan DA3 multi-view atas
seluruh sisinya sekaligus, hitung pusat kamera dari `extrinsics`
(C = −Rᵀt), proyeksikan ke bidang orbit lewat PCA, cocokkan lingkaran, lalu
ukur:

- **RMSE sudut** — simpangan langkah sudut terhadap nilai harapan,
- residual kecocokan lingkaran, rasio kerataan PCA,
- kebenaran **urutan melingkar** sisi,
- rentang dinamis kedalaman.

Pembanding: **2.000 simulasi sudut acak seragam**, supaya "bagus" punya makna
kuantitatif, bukan kesan.

Sampel: 20 pohon 4-sisi dan 30 pohon 8-sisi, acak `seed=42`.

## 4. Hasil

| | 4 sisi (20 pohon) | 8 sisi (30 pohon) |
|---|---|---|
| Langkah sudut diharapkan | 90° | 45° |
| **RMSE sudut** (rata2 / median) | **17,3° / 12,6°** | **8,5° / 7,4°** |
| RMSE pembanding acak | 57,5° | 34,4° |
| **Urutan sisi benar** | **20/20 (100%)** | **30/30 (100%)** |
| Residual lingkaran | 4% | 5% |
| Rasio kerataan | 0,014 | 0,026 |
| Rentang dinamis kedalaman | 3,74 | 4,95 |
| Lebih baik dari acak | 100% | 100% |

Galat relatifnya konsisten antar-konfigurasi: 17,3/90 = **19%** dan
8,5/45 = **19%**.

## 5. Putusan — DIKONFIRMASI

Risiko *wide baseline* yang dikhawatirkan **tidak terwujud**. DA3 memulihkan
susunan melingkar sisi dengan urutan benar pada **seluruh 50 pohon**, jauh di
atas pembanding acak, dengan pusat kamera hampir sebidang.

### Peringatan yang menyertai putusan ini

Inspeksi visual (`results/e005/preview_*.jpg`) menunjukkan kedalaman memisahkan
**pelepah** dari latar dengan sangat bersih — tetapi di area mahkota tempat
tandan berada, peta tampak **halus dan menyatu dengan batang**.

Jadi yang terbukti adalah **geometri tingkat-pohon**. Pemisahan
**tingkat-tandan** belum terbukti sama sekali, padahal itulah yang menentukan
nasib B4. Angka RMSE sudut di atas **tidak boleh** dikutip seolah menjawab
pertanyaan tandan.

## 6. Dampak

- Jalur geometris berlaku untuk **seluruh 953 pohon**, bukan hanya 45 pohon
  bervideo. I-6 dan I-7 layak dikerjakan.
- Peringatan visual di atas langsung memicu **SR-005**: uji kuantitatif apakah
  kedalaman membawa sinyal di tingkat tandan — dijalankan **sebelum** jam GPU
  dibakar untuk pelatihan fusi.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python da3_sides_test.py --trees 20 --sides 4
.venv/bin/python da3_sides_test.py --trees 30 --sides 8 --preview 1
# keluaran: results/e005/report_4sides.json, report_8sides.json, preview_*.jpg
```

Lingkungan: GPU NVIDIA L4, `depth-anything/da3-large`, `process_res=504`.
