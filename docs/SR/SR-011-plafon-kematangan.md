# SR-011 — Plafon kematangan ~68%, terukur tiga kali secara bebas

**Ide I-23** · **Eksperimen:** E-016 · **Putusan: DITARIK — buktinya cacat** · 2026-07-21

> **KOREKSI (E-018).** SR ini semula menyimpulkan plafon ~68% dari "tiga
> pengukuran bebas". Klaim itu **tidak sah** dan ditarik:
>
> 1. Voting multi-sisi memakai **pengklasifikasi potongan yang sama**, jadi ia
>    bukan pengukuran ketiga yang bebas — hanya turunan dari yang kedua.
> 2. Head YOLO dilatih dengan `hsv_s=0.7` (saturasi diacak ±70%) sedangkan
>    pengklasifikasi potongan dilatih **aman-warna**. Pada tugas yang buktinya
>    adalah warna, itu bukan perbandingan setara — head-nya dilumpuhkan.
>
> Angka-angka di bawah tetap benar sebagai **pengukuran**, dan pola ordinalnya
> (±1 = 100,0% pada head YOLO) tetap berdiri. Yang ditarik adalah kesimpulan
> bahwa 68% merupakan **batas yang tidak bisa dilampaui**. Jalur paling
> langsung — detektor 4-kelas resolusi tinggi dengan augmentasi aman-warna —
> tidak pernah diuji saat SR ini ditulis.

---

## 1. Masalah

SR-010 memecah mAP menjadi dua: deteksi menyumbang 0,7191 mAP50, klasifikasi
kematangan menghabiskan 0,1973 dari situ. Itu memberi sasaran rekayasa yang
tajam — naikkan klasifikasi ke ≈83% dan mAP50 mencapai 0,60.

Pertanyaannya: **apakah 83% itu bisa dicapai sama sekali?** Kalau tidak, maka
seluruh usaha menaikkan mAP 4-kelas — apa pun tekniknya — dijatah oleh sesuatu
yang tidak bisa ditawar.

## 2. Ide

Ukur plafon dengan tiga cara yang **saling bebas**. Kalau ketiganya berhenti di
tempat yang sama, angkanya adalah sifat data, bukan sifat model:

| Jalur | Yang diberi lebih | Kalau ini menolong, artinya |
|---|---|---|
| Head YOLO | — (acuan) | — |
| CNN potongan resolusi master | **resolusi & kapasitas khusus** | modelnya yang kurang |
| Voting multi-sisi | **bukti dari 2–6 sudut pandang** | satu sisi tidak cukup |

**Yang akan memalsukan:** salah satu jalur menembus jauh di atas acuan.

## 3. Solusi

- `head_vs_crop.py` — perbandingan setara pada tugas identik: diberi kotak,
  tebak kelas. Head YOLO dinilai pada deteksinya yang berpasangan dengan GT
  (IoU ≥ 0,5); CNN potongan dinilai pada kotak GT yang sama.
- `train_maturity.py` + `build_crops_raw.py` — ConvNeXt-Tiny pada potongan
  3024×4032 (E-015 membuka master; potongan bermedian 320 px vs 171 px di MVC,
  jadi masukan 224 px berisi detail nyata, bukan pembesaran). Augmentasi
  sengaja **aman-warna**: baseline YOLO memakai `hsv_s=0.7`, mengacak saturasi
  ±70% pada tugas yang buktinya adalah warna.
- `multiview_vote.py` — peluang kelas dirata-ratakan antar sisi memakai
  penautan **kebenaran dasar** dari JSON (bukan algoritma penaut), sehingga
  yang terukur adalah plafonnya, bukan mutu penautnya.

## 4. Hasil

| Jalur | Akurasi | Seimbang | ±1 |
|---|---|---|---|
| Head YOLO (n=1.518) | 0,6871 | 0,6484 | **1,0000** |
| CNN potongan master (n=1.887, val) | 0,6910 | 0,6116 | 0,9947 |
| CNN potongan master (n=2.612, test) | 0,6998 | — | 0,9946 |
| Voting multi-sisi (n=992 tandan) | 0,6855 | — | 0,9940 |

Voting multi-sisi menurut jumlah sisi:

| Sisi | n | Akurasi |
|---|---|---|
| 1 | 232 | 0,6250 |
| 2 | 654 | 0,7095 |
| 3 | 83 | 0,6506 |
| 4 | 23 | 0,7391 |

## 5. Putusan — DIKONFIRMASI

**Ketiganya berhenti di 68–70%.** Memberi model resolusi 3× lebih tinggi tidak
menolong. Memberinya 2–6 sudut pandang tidak menolong.

Dua angka yang paling menjelaskan:

1. **±1 = 100,0% pada head YOLO.** Dari 1.518 deteksi berpasangan, **tidak ada
   satu pun** yang meleset dua tingkat. Model tidak pernah bingung antara buah
   mentah dan buah lewat matang; ia hanya tidak bisa memutuskan di garis
   perbatasan. Ini bukan tanda model yang gagal belajar.
2. **Voting multi-sisi gagal menolong.** Kalau kesalahan per-sisi acak,
   merata-ratakan 2–6 sisi seharusnya menaikkannya tajam. Ternyata tidak:
   kesalahannya **berkorelasi antar sisi** — tandan yang di perbatasan tampak
   sama ambigu dari semua arah. Ambiguitasnya ada pada buahnya, bukan pada
   sudut pandangnya.

Digabung dengan **SR-009** (kebingungan ordinal murni; lompatan dua langkah
1,9%) dan **SR-001** (label diberikan per tandan fisik lalu disalin ke semua
sisi, ketidaksepakatan antar-sisi 0,00%), kesimpulannya menutup:

> Kematangan sawit adalah variabel **kontinu** yang dipotong menjadi empat
> kotak, dan letak potongannya tidak dapat dipulihkan dari citra. Plafon ~68%
> adalah harga dari pemotongan itu — bukan kekurangan detektor, arsitektur,
> resolusi, modalitas, maupun jumlah sudut pandang.

### Konsekuensi untuk sasaran mAP50 0,60

Dengan deteksi agnostik 0,7191 (640) atau ~0,77 (960) dan klasifikasi terkunci
di ~68%, mAP50 4-kelas terjatah di sekitar **0,55–0,58**. Sasaran 0,60 pada
perumusan 4-kelas **tidak dapat dicapai dengan menaikkan mutu model** — ia
menuntut perubahan pada perumusan tugasnya. Itu dibahas di SR-012.

### Apa yang TIDAK dibuktikan di sini

Plafon ini berlaku untuk **kematangan dari citra RGB**. Ia tidak mengatakan apa
pun tentang penanda kematangan non-visual (mis. brondolan lepas, yang merupakan
kriteria panen lapangan sesungguhnya dan tidak terlihat pada kanopi dari jauh).
Kalau perumusan tugas boleh diubah, itu arah yang belum tersentuh.

## 6. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python match_raw.py                       # peta master (E-015)
.venv/bin/python build_crops_raw.py                 # potongan 3024x4032
.venv/bin/python train_maturity.py                  # CNN kematangan
.venv/bin/python head_vs_crop.py                    # perbandingan setara
.venv/bin/python multiview_vote.py --split val      # plafon multi-sisi
```
