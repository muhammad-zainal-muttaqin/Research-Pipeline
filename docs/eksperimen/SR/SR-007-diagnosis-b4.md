# SR-007 — Kenapa B4 gagal? Diagnosis berbasis pengukuran

**Ide I-11 (analisis terstratifikasi)** · **Eksperimen:** E-009, E-010
**Putusan: DIKONFIRMASI (kontras) / DIPALSUKAN (kepadatan, ukuran)** · 2026-07-21

---

## 1. Masalah

B4 adalah kelas terburuk: **AP50 = 0,354**, hampir separuh B1 (0,739). Setiap
ide perbaikan sejauh ini menebak penyebabnya:

- "B4 kecil" → maka perbesar resolusi
- "B4 bertumpuk" → maka pakai kedalaman untuk memisahkan lapisan
- "B4 gelap" → maka tingkatkan kontras

Ketiganya masuk akal, dan **ketiganya belum pernah diukur.** Menebak penyebab
lalu membangun solusi di atasnya adalah cara tercepat membakar jam GPU untuk
sesuatu yang tidak menyerang masalah sebenarnya. SR-005 sudah memberi satu
pelajaran mahal ke arah itu.

## 2. Ide

Ukur penyebabnya langsung dari kotak kebenaran-dasar, **tanpa model sama
sekali**. Kalau diagnosisnya tidak bergantung pada detektor, ia tidak bisa
dibantah dengan "mungkin modelnya saja yang kurang bagus".

Tiga tersangka diuji berdampingan, ditambah kendali kotak acak (karena kotak
apa pun pada citra kanopi akan menunjukkan kontras tertentu):

| Tersangka | Cara mengukur |
|---|---|
| Ukuran | luas kotak setelah diskalakan ke `imgsz=640`, terhadap ambang COCO |
| Kontras fotometrik | ΔE CIELAB antara isi kotak dan cincin sekelilingnya |
| Kepadatan / tumpang tindih | jumlah tetangga dalam 1,5× diagonal; IoU maks |

## 3. Solusi

`experiments/box_size_analysis.py` (E-009) dan `experiments/why_b4_fails.py`
(E-010, 400 citra uji, kendali kotak acak, ruang warna CIELAB, varians
Laplacian sebagai ukuran tekstur).

## 4. Hasil

### E-009 — ukuran

| Kelas | Lebar×tinggi median (px @640) | Luas median | % kecil | % sedang |
|---|---|---|---|---|
| B1 | 63 × 69 | 4.361 | 2,6% | 82,6% |
| B2 | 57 × 64 | 3.626 | 4,4% | 86,0% |
| B3 | 52 × 56 | 2.886 | 8,8% | 85,1% |
| **B4** | **46 × 46** | **2.147** | **16,4%** | 81,2% |

### E-010 — kontras, tekstur, kepadatan

| Kelas | ΔE | Tekstur | Tetangga | IoU maks | %IoU>0,1 | AP50 DiB |
|---|---|---|---|---|---|---|
| B1 | **19,15** | 5.015 | 3,23 | 0,042 | 10,3% | 0,739 |
| B2 | 18,48 | 5.726 | 2,92 | 0,041 | 11,5% | 0,433 |
| B3 | 13,93 | 6.892 | 2,81 | 0,033 | 7,7% | 0,599 |
| **B4** | **11,55** | **7.780** | **2,58** | **0,029** | **6,4%** | **0,354** |
| *acak (kendali)* | *12,92* | *5.441* | — | — | — | — |

## 5. Putusan

**Tersangka "ukuran" — melemah.** B4 memang terkecil, tetapi **81,2% kotaknya
masih tergolong sedang** menurut COCO, dengan median 46×46 px. Ukuran itu tidak
problematis bagi detektor modern. Hanya 16,4% yang benar-benar kecil.

**Tersangka "kepadatan" — DIPALSUKAN.** B4 justru punya tetangga **paling
sedikit** (2,58 vs 3,23 pada B1) dan tumpang tindih **paling rendah**
(IoU 0,029; hanya 6,4% di atas 0,1). Hipotesis "B4 gagal karena bertumpuk" —
yang selama ini menjadi motivasi utama jalur kedalaman — **salah**.

**Tersangka "kontras" — DIKONFIRMASI, dan lebih parah dari dugaan.** ΔE B4
adalah **11,55, di bawah kendali kotak acak (12,92)**. Tandan B4 secara harfiah
lebih sulit dibedakan dari latarnya daripada tambalan acak pada citra yang sama.
Ia **tersamar**, bukan sekadar kurang kontras.

**Temuan tambahan: B2 gagal karena sebab yang berbeda.** Kontras latarnya tinggi
(18,48, hampir setara B1) tetapi AP50-nya rendah (0,433). Jadi masalah B2 bukan
*melihat* tandan, melainkan *membedakannya dari B3*. Ini memberi bukti terukur
untuk pemisahan yang dirumuskan di awal proyek:

| Mode kegagalan | Kelas | Bukti |
|---|---|---|
| Fotometrik — tersamar dari latar | **B4** | ΔE 11,55 < kendali 12,92 |
| Fotometrik — tertukar antar-kelas | **B2** | ΔE 18,48 tinggi, AP50 tetap 0,433 |
| Geometrik — bertumpuk | *tidak ada* | IoU maks ≤0,042 di semua kelas |

## 6. Dampak — gambaran yang menyatu

Digabung dengan SR-005, tiga pengukuran independen memberi satu kesimpulan yang
konsisten tentang B4:

1. **Tidak terpisah dalam kedalaman** (SR-005: kontras 0,26× kendali, AUC 0,602)
2. **Tidak terpisah dalam warna** (SR-007: ΔE di bawah kendali)
3. **Tidak bertumpuk** (SR-007: IoU maks 0,029, terendah dari semua kelas)

Ini menjelaskan plafon yang dialami tim dengan cara yang tidak bisa dijelaskan
oleh "modelnya kurang bagus": **B4 memang objek yang tersamar dalam dua modalitas
sekaligus.**

Satu-satunya sinyal yang tersisa adalah **tekstur**, dan di situ B4 justru
**tertinggi** (7.780, di atas semua kelas lain dan jauh di atas kendali 5.441).
Tandan B4 berduri dan berkerut; itulah yang membedakannya, bukan warna maupun
jarak.

**Konsekuensi untuk rencana:**

- **I-12 (ubin) tetap layak, tetapi dengan dasar pemikiran yang berbeda.**
  Bukan karena "objeknya kecil" (E-009 melemahkan itu), melainkan karena
  **tekstur frekuensi-tinggi adalah hal pertama yang hancur saat citra
  diperkecil 2×**. Ekspektasi ini dicatat sebelum hasil ubin keluar.
- **I-16 (copy-paste/augmentasi) turun prioritas** untuk B4: masalahnya bukan
  jumlah contoh, melainkan keterlihatan.
- **Ide baru yang dibenarkan diagnosis ini (I-20):** praproses penajam kontras
  lokal (mis. CLAHE) atau kanal gradien/tekstur eksplisit, yang menyerang tepat
  pada satu-satunya sinyal yang tersisa.
- **B2 butuh perlakuan berbeda dari B4.** Menggabungkan keduanya sebagai
  "kelas sulit" akan menyesatkan: satu perlu keterlihatan, satu perlu
  diskriminasi antar-kelas.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python box_size_analysis.py          # E-009
.venv/bin/python why_b4_fails.py --images 400  # E-010
# keluaran: results/e009/box_sizes.json, results/e010/why_b4.json
```

Tanpa GPU, tanpa model. Beberapa menit.
