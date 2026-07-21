# SR-010 — Yang gagal bukan deteksi, melainkan penilaian kematangan

**Ide I-23** · **Eksperimen:** E-014 · **Putusan: DIKONFIRMASI** · 2026-07-21

---

## 1. Masalah

Setelah sembilan ide diuji, mAP baseline tidak bergerak: mAP50 0,5218 dan
mAP50-95 0,2407 pada val. Setiap ide berikutnya — ubin, kanal keempat, fusi,
neck, augmentasi — mengasumsikan hal yang sama tanpa pernah mengujinya: bahwa
yang kurang adalah **kemampuan menemukan tandan**.

Asumsi itu tidak pernah diperiksa. Selama ia tidak diperiksa, setiap perbaikan
diarahkan ke tempat yang belum tentu rusak — dan itu menjelaskan kenapa
berbulan-bulan usaha menghasilkan nol: obatnya benar, penyakitnya bukan itu.

## 2. Ide

mAP menggabungkan dua kemampuan yang berbeda menjadi satu angka: **menemukan
kotak** dan **memberinya kelas yang benar**. Keduanya bisa dipisahkan tanpa
melatih apa pun — cukup evaluasi bobot yang sama dua kali:

| Evaluasi | Yang diukur |
|---|---|
| 4 kelas | menemukan **dan** menilai kematangan |
| kelas-agnostik (`single_cls=True`) | menemukan saja |

Selisihnya adalah harga yang dibayar murni untuk klasifikasi. Ini pengukuran
langsung, bukan inferensi dari matriks kebingungan, dan biayanya dua menit.

**Yang akan memalsukan:** mAP agnostik hanya sedikit di atas mAP 4-kelas —
artinya detektor memang gagal menemukan tandan, dan seluruh antrean ide
berbasis deteksi memang beralasan.

## 3. Solusi

`experiments/diag_bottleneck.py`. Bobot yang dievaluasi identik
(`runs/rgb_e60_i640_s42/weights/best.pt`, yolo26m, imgsz 640, 60 epoch,
seed 42), split val identik (404 citra, 1.887 kotak). Satu-satunya yang berubah
adalah bendera `single_cls` pada pemanggilan `val()`.

## 4. Hasil

| Evaluasi | mAP50 | mAP50-95 | P | R |
|---|---|---|---|---|
| 4 kelas | 0,5218 | 0,2407 | 0,5307 | 0,5484 |
| **Kelas-agnostik** | **0,7191** | **0,3197** | 0,6950 | 0,6365 |
| **Selisih** | **+0,1973** | **+0,0790** | | |

AP50 per kelas pada evaluasi 4-kelas:

| Kelas | AP50 |
|---|---|
| B1 | 0,7354 |
| B2 | 0,4076 |
| B3 | 0,5561 |
| B4 | 0,3881 |

## 5. Putusan — DIKONFIRMASI

**38% dari mAP50 yang mungkin diraih hilang di klasifikasi, bukan di deteksi.**
Detektor yang sama menemukan 0,7191 mAP50 tandan bila tidak diminta menyebutkan
kematangannya. Begitu diminta, skornya jatuh ke 0,5218.

Tiga konsekuensi yang langsung mengubah prioritas:

1. **Antrean ide berbasis deteksi kehilangan dasarnya.** Ubin (I-12), neck
   multiskala (I-15), copy-paste (I-16), kanal keempat (I-4/I-21) semuanya
   menyerang tahap yang menyumbang 0,7191 — bukan tahap yang menyumbang
   kerugian 0,1973. Batas atas perbaikan mereka kecil menurut konstruksi.
2. **Target yang diminta ternyata sudah setengah tercapai.** mAP50-95
   kelas-agnostik **0,3197 sudah melewati sasaran 0,30**, dan mAP50 agnostik
   0,7191 jauh melewati sasaran 0,60. Angkanya bukan mustahil — ia terkunci di
   balik satu masalah yang selama ini disalahalamatkan.
3. **Efektivitas klasifikasi saat ini terukur: 0,5218 / 0,7191 = 72,6%.**
   Itu memberi sasaran rekayasa yang tajam: untuk mAP50 0,60 dengan detektor
   yang ada, klasifikasi kematangan harus mencapai ≈ 83%.

### Kecocokan dengan temuan sebelumnya

Bukan temuan yang berdiri sendiri — ia menutup rantai yang sudah terbentuk:

- **SR-009** menemukan kebingungan kematangan bersifat ordinal, tanda variabel
  kontinu yang dipotong empat. SR-010 mengukur **berapa harganya** dalam mAP.
- **SR-007** menemukan B4 gagal karena kontras rendah, bukan ukuran. Di sini
  B4 (AP50 0,3881) dan B2 (0,4076) memang dua yang terburuk — keduanya soal
  penilaian permukaan buah, bukan soal menemukan objeknya.
- **SR-001** menemukan label antar-sisi konsisten 100% pada 7.328 tandan
  multi-sisi. Angka nol-sempurna itu hampir pasti berarti label diberikan
  **per tandan fisik lalu disalin ke semua sisi** — sehingga pada sisi yang
  tertutup atau membelakangi cahaya, kotaknya membawa kelas yang pikselnya
  sendiri tidak mendukung. Sebagian dari kerugian 0,1973 itu memang tidak bisa
  direbut per-sisi.

### Kecurigaan yang lahir dari sini

Konfigurasi baseline memakai augmentasi bawaan ultralytics: `hsv_s=0.7`,
`hsv_v=0.4` — saturasi diacak sampai ±70% tiap batch. Kematangan sawit **adalah
warna** (B1 gelap kehijauan → B4 jingga-merah). Resep default itu mengacak
tepat bukti yang harus dipelajari model. Ini bukan hipotesis yang mahal diuji,
dan diuji terpisah (E-015).

## 6. Arah yang dibenarkan

**I-23 — detektor dua tahap.** Tahap 1 mendeteksi tandan secara kelas-agnostik
(sudah terukur 0,7191/0,3197, dan dilatih ulang pada resolusi 960 untuk
menaikkan lokalisasi yang menentukan mAP50-95). Tahap 2 menilai kematangan dari
**potongan resolusi asli**, bukan dari peta fitur citra yang sudah diperkecil ke
640 — pada 640 tandan bermedian 46–63 px, sedangkan potongan asli memberi
2–4× piksel lebih banyak pada objek yang sama.

Ini bukan penyetelan hiperparameter dan bukan modul yang ditempel: ia memindah
keputusan kematangan ke tempat yang punya bukti untuk mengambilnya.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python diag_bottleneck.py
# keluaran: results/diag_bottleneck.json
```

Butuh GPU, dua menit.
