# SR-015 — Depth SENSOR 4-kanal simultan: informasinya ada, cara memasukkannya salah

**Ide I-4/I-8** · **Eksperimen:** E-022, direplikasi [E-027]/[E-029] · **Putusan: DIPALSUKAN (fusi awal), diperkuat 3 seed × 2 arsitektur; klausa "mekanisme depth TERKONFIRMASI pada model besar" DICABUT PENUH 2026-08-01** · 2026-07-29

> **⚠ PENCABUTAN KLAUSA PUTUSAN — 2026-07-30.** Putusan "fusi awal DIPALSUKAN"
> **tetap berdiri** dan justru diperkuat replikasi 3 seed. Yang **dicabut**
> adalah klausa keduanya: "mekanisme depth terkonfirmasi pada model besar".
> Klausa itu bertumpu pada satu perbandingan seed-42 RT-DETR-L depth − derau
> (+0,0365, B1 +0,0698, B4 +0,1001) — dan lengan derau pembandingnya dibuat
> dengan kode cacat. Setelah diperbaiki, derau RT-DETR-L naik 0,3552 → 0,3894,
> sehingga selisih itu menyusut drastis. Pada seed1337 derau bahkan
> **mengalahkan** depth (0,4353 vs 0,4125) dengan B4 0,3147 vs 0,1206.
> B4 hanya punya 95 kotak; sebaran antar-seed-nya melebihi seluruh efek yang
> diklaim. Detail: [AUDIT-E022.md](../AUDIT-E022.md).

> **⚠ TAMBAHAN 2026-08-01 — pembanding derau juga tidak bertahan.** Matriks
> multi-seed YOLO26n protokol beku ([E-027](../EKSPERIMEN.md)) menunjukkan
> temuan "derau mengalahkan depth" **tidak tereproduksi**. Angka +0,0437 pada
> seed-42 lama — satu-satunya delta signifikan di seluruh E-022 dan dasar
> beberapa kalimat di bawah — menjadi +0,0032 / +0,0011 / −0,0443 (rerata
> −0,0133) setelah dijalankan ulang dengan kode `_fix`. Sebaliknya, putusan
> utama "fusi awal DIPALSUKAN" **makin kuat**: depth − RGB kini rerata −0,0230
> dengan dua dari tiga seed signifikan NEGATIF, jadi untuk YOLO26n depth bukan
> netral melainkan **merugikan**. Tabel di bawah dipertahankan sebagai rekam
> seed-42; jangan mengutip angka deraunya sebagai temuan.

> **⚠ PENCABUTAN PENUH KLAUSA KAPASITAS — 2026-08-01.** Matriks RT-DETR-L
> lengkap 3 seed ([E-029](../EKSPERIMEN.md)) mencabut klausa terakhir yang masih
> berdiri. depth − derau menjadi **+0,0183 / +0,0153 / +0,0035** (rerata
> +0,0124), **ketiganya CI memuat nol**, dan **B4 +0,1001 yang menjadi tulang
> punggung klausa itu tidak direproduksi**. Sebagai ukuran skalanya: lengan RGB
> saja berayun **0,0759** antar seed — enam kali rerata efek yang diklaim.
> Lebih telak lagi, depth − RGB bertanda **berlawanan** pada dua seed yang
> sama-sama signifikan (−0,0350 seed42 vs +0,0702 seed2024).
>
> Yang **tetap berdiri** adalah putusan utama SR ini: **fusi awal 4-kanal
> DIPALSUKAN**, kini pada dua arsitektur dan tiga seed, bukan lagi satu seed.
> Judul SR ("informasinya ada, cara memasukkannya salah") masih dapat
> dipertahankan, tetapi bagian "informasinya ada" kini bersandar pada
> pengamatan yang jauh lebih lemah: depth − derau satu-satunya kontras dengan
> sd kecil (0,0064), dan itu **pengamatan pasca-hoc** yang belum diuji sebagai
> hipotesis. Lihat [E-029](../EKSPERIMEN.md) §"Satu pola yang bertahan".

---

## 1. Masalah

`STATUS.md` §5 mencatat satu lubang yang tidak bisa ditutup dengan analisis:
**depth SENSOR belum pernah diuji.** Yang pernah diuji hanya pseudo-depth
(E-006/SR-005, dipalsukan) — dan pseudo-depth punya cacat bawaan yang dicatat di
`evidence-body.tex` §133: ia diturunkan dari RGB yang sama, jadi galatnya
berkorelasi dan ia prior struktural, bukan pengukuran independen.

Dataset `ULM-DS-Lab/SawitMVC-Depth` menutup lubang itu: 352 pohon, 1.408 citra
RGB 1280×800, dan depth sensor Orbbec Y16 848×480 uint16 milimeter per citra.
Pertanyaannya jadi bisa diuji langsung: **apakah depth dari sensor sungguhan
menaikkan mAP deteksi tandan?**

Diagnosa yang sudah disepakati membatasi harapan sejak awal (`CLAUDE.md`):
kegagalan deteksi terbelah dua — **(A) geometris** (B4 kecil/tertanam/tertutup
pelepah), di sinilah depth relevan; dan **(B) fotometrik** (ambiguitas kematangan
B2↔B3), di mana depth **tidak** akan menolong.

## 2. Ide

Masukan 4 kanal `[B,G,R,D]` — depth masuk **bersamaan** dengan RGB dalam satu
model, satu forward pass, satu loss. Bukan kaskade deteksi-lalu-proyeksi.
Kanal ke-4 diisi depth metrik terkuantisasi pada rentang TETAP (inverse depth),
tanpa normalisasi per-citra, dengan 0 = "tidak ada data".

**Yang akan memalsukan:** delta mAP50 ≤ +0,015 terhadap baseline RGB pada
protokol identik, atau CI 95% bootstrap berpasangan memuat 0, atau kontrol
negatif tanpa informasi memberi kenaikan sebanding.

## 3. Solusi — apa yang persis dikerjakan

**Prasyarat yang hampir merusak segalanya.** Sidecar setiap berkas depth
menyatakan `"alignedTo": "color"`. **Itu menyesatkan** — buffer 848×480 masih di
grid kamera depth pabrikan. Tiga bukti independen:

1. Intrinsik depth (fx=fy=416,55, piksel persegi) bukan versi terskala intrinsik
   color: 610,87·848/1280 = 404,7 pada x tetapi 610,87·480/800 = 366,5 pada y.
2. FOV vertikal color (66,4°) **lebih lebar** daripada depth (59,9°), sehingga
   depth yang sudah di-D2C wajib punya ~34 baris atas dan ~28 baris bawah kosong
   di setiap citra. Terukur: **0 baris dan 0 kolom** yang selalu-invalid.
3. Mutual information atas 150 citra: reproyeksi penuh 0,2852 bit vs resize
   langsung 0,2546 bit; selisih berpasangan **+0,0306 [+0,0260; +0,0354]**, menang
   di 84% citra. Kontrol pergeseran buatan ±24 px menurunkan MI ke ~0,23,
   membuktikan metriknya peka terhadap registrasi.

`cv2.resize` naif — yang diasumsikan `reproduce/pipeline/prepare_depth.py` — meleset
**median 29,3 px, maksimum 61 px** pada bidang 1280×800, seukuran tandan B4 itu
sendiri. Maka dibangun `build/reproject_depth.py`: depth → titik 3D (intrinsik depth) →
ekstrinsik → intrinsik color + distorsi Brown-Conrady K6, forward-warp
**ber-z-buffer** (tanpa ini latar menimpa objek di tepi oklusi — justru sinyal
yang dicari), tambal lubang **median 3×3** (operator ranking; blur menghasilkan
kedalaman hantu melintasi batas objek). Kalibrasi dibaca **per berkas** karena
dataset memuat **dua unit kamera** (fx_depth 416,55 vs 414,38; rotasi ekstrinsik
0,064° vs 0,562°).

Rentang metrik `fourch.py` (0,3–8,0 m) terbukti tidak cocok: 0,000% piksel valid
di bawah 0,3 m (minimum absolut 313 mm) sementara 10,07% melebihi 8 m, entropi
kanal hanya 6,19 dari 7,99 bit. Dipilih ulang dari histogram **split train saja**:
**Z_NEAR 0,8 / Z_FAR 15,0 m**, entropi 7,62 bit, level median 74/255.

**Tiga arsitektur, varian terkecil masing-masing**, 60 epoch, seed 42, 640 px,
split per-pohon 245/35/72 (irisan nol, stratifikasi device × unit-kamera ×
kelas-dominan). Tiga pagar keadilan: HSV dimatikan di **kedua** lengan
(`RandomHSV` melewati citra non-3-kanal secara diam, `augment.py:1461`); conv
pertama diinflasi dari bobot pratlatih (kanal RGB utuh, kanal ke-4 = 0, model
**dan** EMA); modality dropout 0.

RF-DETR 4-kanal dibuat tanpa fork paket — `rfdetr 1.8.3` sudah punya
`ModelConfig.num_channels`, ditambah empat tambalan: pemuat data, normalisasi
(mean/std kanal depth dari train saja), validasi kanal `PatchEmbeddings`, dan
penimpaan heuristik `_adapt_input_conv` yang secara bawaan mengubin bobot RGB ke
kanal ke-4 lalu mengalikan **seluruh** bobot dengan 0,75.

## 4. Hasil

| Kanal ke-4 | YOLO26n (2,57 jt) | RT-DETR-L (33,0 jt) | RF-DETR Nano |
|---|---|---|---|
| tidak ada (RGB) | 0,3249 | **0,4076** | 0,4196 |
| depth terregistrasi | 0,3501 | 0,3900 | **0,4635** |
| derau acak | 0,3686 | 0,3535 | — |
| depth pohon LAIN | 0,3721 | — | — |

Selisih berpasangan, bootstrap 2000× per **pohon**:

| Perbandingan | delta | CI95 |
|---|---|---|
| YOLO26n depth − RGB | +0,0252 | [−0,0215; +0,0632] |
| RF-DETR Nano depth − RGB | +0,0439 | [+0,0000; +0,0918] |
| RT-DETR-L depth − RGB | −0,0177 | [−0,0669; +0,0203] |
| **YOLO26n DERAU − RGB** | **+0,0437** | **[+0,0051; +0,0875]** |
| YOLO26n depth − derau | −0,0186 | [−0,0694; +0,0191] |
| YOLO26n depth − tukar | −0,0220 | [−0,0506; +0,0085] |
| **RT-DETR-L depth − derau** | **+0,0365** | [−0,0014; +0,0668] |
| RF-DETR Nano depth − derau | +0,0087 | [−0,0372; +0,0538] |

## 5. Putusan

**DIPALSUKAN untuk fusi 4-kanal awal.** Dua kriteria falsifikasi yang ditulis
sebelum run pertama sama-sama terpenuhi: CI memuat nol untuk ketiga arsitektur,
**dan** kontrol negatif menyamai — kanal berisi derau memberi satu-satunya delta
signifikan di seluruh E-022 (+0,0437, CI tidak memuat nol).

**Registrasi tidak membeli apa pun pada model kecil.** Depth dari pohon LAIN
setara dengan depth yang diregistrasi benar (−0,0220, CI memuat nol), dan pada B1
depth benar justru signifikan lebih buruk (−0,0662 [−0,1089; −0,0199]). Reproyeksi
yang terbukti lebih selaras di §3 tidak diterjemahkan menjadi mAP.

**Tetapi kandungan informasi depth NYATA pada model besar.** Pada RT-DETR-L, depth
mengalahkan kontrol deraunya sendiri secara signifikan justru pada kelas yang
diprediksi teori: **B4 +0,1001 [+0,0062; +0,1618]** dan B1 +0,0698 [+0,0306;
+0,1100]. Ini bukan hasil nol — ini hasil "informasinya ada, salurannya salah".

Pola ini konsisten pada **dua** model kecil: depth tidak dapat dibedakan dari
derau (YOLO26n −0,0186; RF-DETR Nano +0,0087) dan signifikan lebih buruk di B1
(−0,0734 dan −0,0446). Hanya di 33,0 jt parameter isi kanal menentukan.

**Arah efek kanal ke-4 ditentukan KAPASITAS MODEL, bukan isi kanal.** Pada 2,57 jt
parameter ia menaikkan dan isinya tidak penting (derau ≥ depth); pada 33,0 jt
parameter ia menurunkan dan isinya penting (depth ≫ derau). Tafsir paling hemat:
pada model kecil yang undertrained di 1.593 kotak latih, kanal ke-4 bekerja
sebagai regularisasi; pada model besar berbobot pratlatih, ia mengganggu stem
3-kanal dan depth hanya memulihkan sebagian kerugiannya.

## 6. Dampak

Kegagalan ada pada **cara memasukkan** depth, bukan pada depth-nya. Itu persis
prediksi korpus sendiri — FuseNet tumpukan 4-kanal 31,95 IoU **di bawah** RGB
32,47 sementara fusi fitur mencapai 37,29; sapuan 28 titik fusi Ophoff dkk.
menemukan fusi tengah-hingga-akhir konsisten mengungguli fusi awal
(`evidence-body.tex` §174). Bedanya sekarang: itu bukan lagi kutipan literatur
indoor, melainkan terukur pada FFB sawit dengan depth sensor.

**Lanjutan yang diusulkan (E-023): fusi MENENGAH dua cabang** pada RT-DETR-L atau
RF-DETR — arsitektur di mana depth sudah terbukti membawa informasi B4. Kontrol
derau dan kontrol tukar **wajib** diulang di sana; tanpa keduanya, kenaikan
apa pun tidak dapat dibedakan dari efek kapasitas.

## 7. Keterbatasan yang tidak boleh dihaluskan

- **Satu seed, satu split.** Selisih yang diukur 0,02–0,04 sementara CI-nya
  0,05–0,09 lebar dan deviasi antar-run wajar ±0,005. Varians split belum diukur;
  3-fold CV yang direncanakan tidak dijalankan.
- **B4 hanya 148 kotak di SELURUH dataset**, 38 di test. Setiap klaim B4 —
  termasuk temuan positif +0,1001 di atas — bersandar pada puluhan kotak.
- **Dataset 8× lebih kecil** dari SawitMVC (2.299 vs 18.540 kotak) dengan prior
  kelas terbalik. Daya ujinya rendah: "tidak terbukti" bukan "terbukti tidak ada".
- Angka di sini **tidak sebanding** dengan test mAP50 0,6038 milik E-021 —
  dataset, resolusi, orientasi, dan sebaran kelasnya berbeda.

## 8. Reproduksi

`build/depth_calib.py` → `analysis/verify_depth_mi.py` (gerbang registrasi) →
`build/reproject_depth.py` (PNG kanonik + `depth_meta.json`) → `build/make_splits_depth.py` →
`train/train_depth4ch.py` (ultralytics; `--depth-acak`, `--depth-tukar`) /
`train/train_rfdetr_4ch.py` (rfdetr 4-kanal) → `eval/eval_e022_pycoco.py`,
`eval/eval_e022_paired.py`, `eval/eval_rfdetr_e022.py`.

Hasil mentah: `evidence/experiments/results/E-022/*.json`. Split persis:
`evidence/experiments/splits_depth/seed42/`. Tabel seed-42 awal:
[`../archive/E022-seed42-awal.md`](../archive/E022-seed42-awal.md). Audit:
[`../AUDIT-E022.md`](../AUDIT-E022.md). Log kronologis:
[`../EKSPERIMEN.md`](../EKSPERIMEN.md) §E-022.
