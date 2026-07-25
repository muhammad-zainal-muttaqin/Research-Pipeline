# SR-001 — Mengukur plafon ambiguitas kematangan B2/B3

**Ide:** manfaatkan flag `class_mismatch` sebagai batas atas empiris
**Eksperimen:** E-001 · **Putusan: DIPALSUKAN** · 2026-07-21

---

## 1. Masalah

Baseline DiB menunjukkan dua kelas kematangan jauh lebih buruk daripada yang
lain: **B2 AP50 = 0,433** dan B3 = 0,599, sementara B1 mencapai 0,739. Naskah
menyebut ini ambiguitas yang sulit direduksi di batas B2/B3.

Persoalannya: klaim itu bersandar pada **hasil model**. Kalau model salah
membedakan B2 dan B3, itu bisa berarti dua hal yang sangat berbeda —
(a) modelnya kurang baik, atau (b) kelasnya memang tidak terpisah secara visual.
Keduanya menuntut tindakan berbeda. Tanpa memisahkan keduanya, kita bisa
menghabiskan waktu memperbaiki sesuatu yang memang tidak bisa diperbaiki, atau
sebaliknya menyerah pada sesuatu yang sebenarnya bisa.

## 2. Ide

Dataset memuat pengukuran yang jauh lebih langsung daripada hasil model. Tiap
tandan fisik dilihat dari 2–6 sisi, dan tiap kemunculan diberi label kelas
sendiri. Karena **satu tandan fisik pasti punya satu kematangan**, setiap
perbedaan label antar-sisi adalah kesalahan pelabelan pada salah satu sisi.

Flag `class_mismatch` di JSON per-pohon menyala tepat pada kondisi itu.

Kalau anotator manusia — yang melihat citra beresolusi penuh, tanpa batas waktu,
diawasi ahli agronomi — masih tidak konsisten pada tandan yang sama, maka
tingkat ketidaksepakatan itu adalah **batas atas empiris akurasi klasifikasi
per-sisi**. Model tidak bisa diharapkan melampaui konsistensi manusianya.

**Yang akan memalsukan:** tingkat ketidaksepakatan mendekati nol, atau
ketidaksepakatan tidak terkonsentrasi di pasangan B2↔B3.

## 3. Solusi

`experiments/class_mismatch_stats.py` membaca seluruh **953 JSON**, lalu
menghitung:

- jumlah flag `class_mismatch` yang menyala,
- perbedaan label antar-sisi yang dihitung ulang **langsung dari data**
  (tidak percaya begitu saja pada flag),
- matriks kebingungan label-sisi terhadap kelas konsensus tandan,
- pecahan per split, varietas, jumlah sisi kemunculan, dan kelas.

## 4. Hasil

| Besaran | Nilai |
|---|---|
| Tandan unik | 9.823 |
| Tandan tampak dari ≥2 sisi | 7.328 (74,6%) |
| **Label antar-sisi berbeda** | **0 (0,00%)** |
| **Flag `class_mismatch` menyala** | **0** |
| Konsistensi label sisi vs konsensus | 18.540 / 18.540 = **100,00%** |

**Verifikasi bahwa nol itu bukan bug.** Angka turunan parser dicocokkan dengan
angka publikasi dan cocok persis:

| Besaran | Parser | Publikasi |
|---|---|---|
| Tandan unik | 9.823 | 9.823 ✓ |
| Total kemunculan | 18.540 | 18.540 ✓ |
| Tampak dari 2 / 3 / 4 / 5 / 6 sisi | 6.264 / 834 / 147 / 71 / 12 | idem ✓ |

## 5. Putusan — DIPALSUKAN

`class_mismatch` **bukan** pengukur ambiguitas kematangan. Ia pemeriksa
integritas data, dan hasilnya bersih.

Penyebabnya tertulis di naskah DiB §4.3: *"Completed annotations were reviewed in
full by a single reviewer, who applied corrections before export."* Perbedaan
antar-sisi sudah dikonsolidasikan sebelum rilis, sehingga besaran yang ingin
diukur **tidak lagi teramati** pada versi publik dataset.

**Peringatan salah kutip.** Angka nol ini **tidak** mendukung dan **tidak**
membantah klaim ambiguitas B2/B3 — ia tidak mengukurnya sama sekali. Menyajikan
"konsistensi anotator 100%" sebagai bukti mutu terhadap ambiguitas akan
menyesatkan. Satu hal yang sah disimpulkan: dataset ini bersih dan konsisten
secara internal.

## 6. Dampak dan pengganti

Jalur ini ditutup. Penggantinya tidak bergantung pada label manusia sama sekali:

> Pakai graf `_confirmedLinks` sebagai **oracle identitas**, lalu ukur
> **inkonsistensi prediksi detektor** pada tandan fisik yang sama antar-sisi.
> Tandan yang sama harus mendapat kelas yang sama; setiap kali model berubah
> pikiran antar-sisi, itu ambiguitas yang terukur.

Bonusnya, ukuran yang sama bisa dipakai menguji apakah depth menstabilkan
prediksi. Membutuhkan detektor terlatih, jadi dijalankan bersama I-4/I-5.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python class_mismatch_stats.py
# keluaran: results/class_mismatch.json
```

Waktu jalan: beberapa detik. Tidak butuh GPU.
