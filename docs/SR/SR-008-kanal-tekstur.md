# SR-008 — Kanal tekstur sebagai modalitas keempat

**Ide I-20 / I-21** · **Eksperimen:** E-011 (+ E-012 menyusul)
**Putusan: DIKONFIRMASI (tekstur) / DIPALSUKAN (penajam kontras)** · 2026-07-21

---

## 1. Masalah

SR-007 menyisakan satu kesimpulan yang tidak nyaman: B4 **tersamar dalam dua
modalitas sekaligus**.

| Modalitas | Hasil pengukuran | Sumber |
|---|---|---|
| Kedalaman | kontras 0,26× kendali, AUC 0,602 | SR-005 |
| Warna / luminans | ΔE 11,55, **di bawah** kendali acak 12,92 | SR-007 |
| Kepadatan (bertumpuk) | IoU maks 0,029, **terendah** dari semua kelas | SR-007 |

Kalau ketiganya buntu, tidak ada arsitektur fusi yang akan menolong — masalahnya
bukan cara menggabungkan informasi, melainkan tidak adanya informasi untuk
digabungkan.

Tetapi SR-007 juga meninggalkan satu petunjuk: **B4 punya tekstur tertinggi**
(varians Laplacian 7.780, di atas semua kelas dan jauh di atas kendali 5.441).
Tandan B4 berduri dan berkerut.

## 2. Ide

Kalau tekstur adalah satu-satunya sinyal yang tersisa, maka transformasi yang
menonjolkan tekstur seharusnya menaikkan keterpisahan B4 — dan transformasi
yang hanya menaikkan kontras warna seharusnya tidak.

Dua hipotesis diadu, karena keduanya sama-sama masuk akal secara intuitif:

| Hipotesis | Praproses | Prediksi |
|---|---|---|
| "B4 kurang kontras" | CLAHE, unsharp mask | naik |
| "B4 kurang terlihat teksturnya" | gradien Sobel, Laplacian | naik |

Diuji **sebelum** melatih apa pun, mengikuti disiplin yang sama seperti E-006
dan E-010 — mengukur dulu, membakar GPU kemudian.

**Yang akan memalsukan:** tidak ada praproses yang menaikkan AUC B4 lebih dari
0,02 di atas acuan.

## 3. Solusi

`experiments/contrast_boost_test.py`, 250 citra uji, lima peta skalar.
Metrik: AUC pemisahan piksel isi-kotak vs cincin sekeliling, per kelas, dengan
**kendali kotak acak dihitung ulang untuk tiap praproses** — karena tiap
transformasi mengubah statistik citra secara keseluruhan, sehingga
membandingkan AUC mentah antar-praproses akan menyesatkan.

## 4. Hasil

| Praproses | B1 | B2 | B3 | **B4** | kendali | **B4 − kendali** |
|---|---|---|---|---|---|---|
| asli (luminans) | 0,5897 | 0,6003 | 0,5753 | 0,5573 | 0,5659 | **−0,0086** |
| CLAHE | 0,5680 | 0,5833 | 0,5621 | 0,5534 | 0,5614 | −0,0080 |
| unsharp | 0,5696 | 0,5772 | 0,5582 | 0,5447 | 0,5513 | −0,0066 |
| gradien Sobel | 0,5682 | 0,5768 | 0,5909 | 0,6041 | 0,5674 | +0,0367 |
| **Laplacian** | 0,5673 | 0,5818 | 0,5970 | **0,6153** | 0,5695 | **+0,0458** |

Perbaikan Laplacian atas acuan: **+0,0544 AUC**.

## 5. Putusan

**Hipotesis "kurang kontras" — DIPALSUKAN.** CLAHE (−0,0080) dan unsharp
(−0,0066) tidak menolong, bahkan sedikit **memperburuk** dibanding acuan
(−0,0086 → keduanya tetap negatif). Ini dugaan yang paling intuitif, dan
ternyata salah.

**Hipotesis "kurang terlihat teksturnya" — DIKONFIRMASI.** Kanal frekuensi
tinggi murni menaikkan keterpisahan B4 secara nyata: Sobel +0,0367, Laplacian
+0,0458.

**Bukti terkuatnya adalah pembalikan urutan kelas.** Pada luminans asli, B4
adalah kelas **paling tidak terpisah** (0,5573) dan bahkan di bawah kendali
acak. Pada kanal Laplacian, B4 menjadi kelas **paling terpisah dari semuanya**
(0,6153, di atas B1/B2/B3).

Ini bukan sekadar kenaikan angka; ini pembalikan peringkat yang konsisten
dengan penjelasan fisiknya. **B4 tak terlihat dalam intensitas, tetapi terlihat
dalam tekstur.**

### Batas klaim

AUC 0,6153 tetap jauh dari sempurna. Ini menunjukkan tekstur membawa sinyal
yang **nyata tetapi sederhana** — cukup untuk membenarkan pengujian arsitektur,
belum cukup untuk menjanjikan lompatan AP50. Pengujian sesungguhnya adalah
E-012, dan hasilnya bisa saja datar meski diagnosis ini benar: sinyal yang ada
di piksel belum tentu dapat dimanfaatkan detektor.

## 6. Dampak

**I-21 — kanal keempat berisi tekstur, bukan kedalaman.**

Ini lebih beralasan daripada RGB+D pada setiap titik pembandingnya:

| | RGB + kedalaman (I-4) | RGB + tekstur (I-21) |
|---|---|---|
| Dasar bukti | E-006 **memalsukan** pemisahan tandan | E-011 **mengonfirmasi** (+0,0458) |
| Efek pada B4 | AUC 0,602 (terendah antar-kelas) | AUC 0,6153 (**tertinggi** antar-kelas) |
| Biaya disk | 765 MB peta kedalaman | **nol** — dihitung saat pemuatan |
| Biaya prapemrosesan | DA3 pada 3.992 citra (~10 menit GPU) | Laplacian, milidetik per citra |
| Ketergantungan | model fondasi eksternal | hanya OpenCV |

Mesin 4-kanal yang dibangun untuk I-4 dipakai ulang dengan menukar isi kanal,
sehingga perbandingan RGB vs RGB+D vs RGB+T berjalan pada kondisi identik:
`yolo26m`, epochs 60, batch 32, imgsz 640, seed 42, split sama.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python contrast_boost_test.py --images 250
# keluaran: results/e011/contrast_boost.json

# pelatihan varian tekstur (E-012)
.venv/bin/python train_fusion.py --mode rgbt
```

E-011 tanpa GPU, beberapa menit.
