# CEK-SAYA — Daftar Periksa Sesi Otonom 23 Juli 2026

Kerja yang dilakukan tanpa Anda, dan **persis apa yang harus Anda verifikasi sendiri**.
Semua di branch `reframe-design-space`. `main` tidak disentuh sejak `ea6819b`.

Buang seluruhnya kalau tidak cocok:

```bash
git checkout main                                  # branch reframe ditinggalkan
git branch -D reframe-design-space                 # atau hapus sekalian
git checkout main && git reset --hard ea1f277      # kembali ke versi yang dosen nilai
```

---

## Ringkas: apa yang berubah

| Berkas | Isi | Risiko |
|---|---|---|
| `tools/openalex_search.py` | Skrip pencarian Q1–Q6 lewat OpenAlex | Rendah — kode, bisa dijalankan ulang |
| `docs/search/raw/openalex_Q*.csv` | Hasil mentah per query | Rendah — data mentah, tidak ditafsirkan |
| `docs/search/raw/known-item-test_*.csv` | Hasil uji known-item | **Perlu dicek** — ini gerbang mutu query |
| `docs/search/openalex-counts.csv` | Rekap n per query | **Perlu dicek** |
| `docs/CEK-SAYA.md` | Berkas ini | — |

**Tidak ada satu kata pun prosa naskah yang saya tulis.** `evidence-body.tex`,
`main.tex`, `main-elsarticle.tex`, `references.bib` **tidak disentuh sama sekali**.
Alasannya di `REFRAME-DECISIONS.md`: keluaran FASE 1 adalah masukan untuk §5, dan
gerbang R2 harus dilewati dulu.

---

## 1. Temuan terpenting: gerbang R2 lolos

Risiko terbesar rencana ini adalah **R2** — §5 (3.400 kata, inti naskah) berdiri di
atas literatur yang **nol di korpus lama** (0 entri re-ID/MOT/MVDet). Rencana
menetapkan gerbang: bila Q2 menghasilkan <30 studi setelah penyaringan, sumbu asumsi
diciutkan dari 7 jadi 3–4 dan klaim kontribusi diturunkan — **sebelum** menulis.

**Q2 mengembalikan 1.991 record mentah.** Bahkan dengan tingkat lolos penyaringan yang
pesimistis, ini jauh di atas ambang. Ruang desain versi penuh (M0–M5 × A1–A7) layak
dipertahankan.

> **Yang harus Anda cek:** buka `docs/search/raw/openalex_Q2_2026-07-23.csv`, baca 20
> judul acak. Pertanyaannya bukan "apakah banyak" tapi **"apakah ini benar tentang
> memutuskan dua deteksi di dua pandangan adalah objek yang sama"**. Kalau yang muncul
> ternyata mayoritas *multi-view learning* (metode pembelajaran mesin dengan banyak
> "view" fitur, bukan banyak sudut kamera), query harus diperketat dan angka 1.991 itu
> menyesatkan. Ini **satu-satunya cek yang tidak bisa saya gantikan** — ia butuh
> penilaian domain.

## 2. Yang harus Anda verifikasi

### 2.1 Uji known-item — gerbang mutu query

```bash
cat docs/search/raw/known-item-test_2026-07-23.csv
```

Tiga item wajib kembali lewat query yang diharapkan:

| Item | DOI | Harus ditemukan oleh |
|---|---|---|
| Gené-Molá 2020, deteksi buah + SfM | `10.1016/j.compag.2019.105165` | Q1 dan/atau Q3 |
| Koirala 2019, MangoYOLO | `10.1007/s11119-019-09642-0` | Q1 dan/atau Q4 |
| Indriani 2026, SawitMVC | `10.1016/j.dib.2026.112990` | Q1 |

**Hasil sebenarnya — uji ini menangkap dua masalah nyata:**

| Item | Hasil | Keterangan |
|---|---|---|
| Gené-Molá 2020 | ditemukan **Q3** | Sebenarnya LOLOS. Skrip salah menilai karena memakai `all()` padahal §6 menulis "dan/atau". Sudah diperbaiki → `PROTOCOL.md` D-1. |
| Koirala 2019 MangoYOLO | **tidak ditemukan Q1 maupun Q4** | **Celah nyata.** Lihat di bawah. |
| Indriani 2026 SawitMVC | ditemukan **Q1, Q2, Q4** | LOLOS. |

**Celah yang ditemukan (`PROTOCOL.md` D-2), dan ini penting.** MangoYOLO lolos dari
kedua query karena alasan yang sah: Q1 mensyaratkan klausa multi-view/video/tracking,
sedangkan MangoYOLO adalah deteksi citra-tunggal; Q4 mensyaratkan klausa atribut kelas,
sedangkan MangoYOLO mengerjakan penghitungan, bukan penilaian mutu.

Artinya **set query saat ini tidak menjaring baseline penghitungan buah
pandangan-tunggal** — literatur yang dibutuhkan dua kali: sebagai kelas pembanding
M0/M1 di §5, dan untuk memenuhi butir 7 dosen (penghitungan apel/jeruk/anggur).
Rancangan **Q7** sudah saya tulis di `PROTOCOL.md` D-2, **belum dijalankan**.

> **Keputusan Anda:** setujui Q7 lalu saya jalankan, atau Anda ingin merumuskan
> ulang klausanya dulu?

Suharjito dan Goh **belum diuji** — rujukan persisnya masih menunggu konfirmasi dosen
(lihat `REFRAME-DECISIONS.md`, konfirmasi #4).

### 2.2 Rekap jumlah + batas yang tersentuh

```bash
cat docs/search/openalex-counts.csv
```

Hasil sebenarnya:

| Query | Isi | n_api | diunduh | Status |
|---|---|---|---|---|
| Q1 | inventaris buah multi-view | 1.849 | 1.851 | lengkap |
| **Q2** | **asosiasi lintas-view** | **1.991** | 1.991 | lengkap — **gerbang R2 lolos** |
| Q3 | multimodalitas/geometri tanaman | 6.423 | 5.000 | **terpotong** |
| Q4 | kelas per-instans | 2.757 | 2.757 | lengkap |
| Q5 | tinjauan terdahulu | 1.143 | 1.143 | lengkap |
| Q6 | seed sawit | **15.609** | 5.000 | **terpotong, terlalu luas** |

Dua query menyentuh penjaga runaway 5.000 (`PROTOCOL.md` D-3):

- **Q3** (6.423) — selisihnya kecil; cukup naikkan batas.
- **Q6** (15.609) — **terlalu luas**. Literatur "oil palm" mencakup agronomi, biologi,
  dan ekonomi minyak sawit yang sebagian besar bukan visi komputer. Butuh klausa keempat
  yang mensyaratkan istilah pencitraan/pembelajaran mesin.

**`n_raw` untuk Q3 dan Q6 belum sah** untuk corong PRISMA sampai ini dibereskan.
Angka Q1, Q2, Q4, Q5 lengkap dan bisa dipakai.

### 2.3 Klaster tema — SAYA KELIRU, ini koreksinya

**Laporan saya sebelumnya salah dan saya cabut.** Saya menulis bahwa angka 14 di
`CLAUDE.md` "salah" dan bahwa 6 entri "kehilangan baris `| Tema |`". Keduanya keliru.

**Yang benar — 14 dan 17 mengukur hal berbeda, dan repo sudah mendokumentasikannya**
di `docs/PLAN.md` §"Catatan rekonsiliasi sumber" baris 50–53 dan
`figures/C02-distribusi-tema.md` §2:

| Angka | Artinya | Sumber |
|---|---|---|
| **14** | klaster taksonomi **naskah LaTeX**, menggabungkan beberapa label berkas | `TEMUAN.md`, `CLAUDE.md` |
| **17** | label tema yang dipakai `build.js` dan situs, dibaca dari **nama berkas** | `entri/*.md` |

`docs/PLAN.md:52` menyatakannya harfiah: *"keduanya tidak bertentangan, aplikasi
mengikuti label nama berkas."* Audit itu sudah pernah dikerjakan; saya melewatkannya.
**Jangan menyamakan keduanya.** `CLAUDE.md` sekarang saya beri baris penjelas, angkanya
tidak diubah.

**Yang benar-benar rusak, dan sudah diperbaiki.** Bukan tema yang hilang — melainkan
**label kolomnya tidak seragam**. Enam entri memakai `| Tema klaster |` atau
`| Tema Klaster |` alih-alih `| Tema |`:

| Entri | Label lama |
|---|---|
| `126 - Automated Fruit Harvesting Robot (Onishi dkk.)` | `Tema Klaster` |
| `149 - CBAM` · `151 - Object Detection in 20 Years` · `153 - Survei RGB-D SOD` | `Tema klaster` |
| `156 - YOLO-World` · `163 - Swin Transformer V2` | `Tema klaster` |

Akibatnya `tools/build_evidence_matrix.py` — yang membaca baris `| Tema |` — tidak
menemukannya dan melempar keenamnya ke kategori palsu **"Uncoded"**, sehingga CSV
melaporkan 18 tema. `build.js` **tidak** terpengaruh: ia membaca tema dari nama berkas
(`build.js:111`), jadi situs selalu benar.

Sudah dinormalkan ke `| Tema |`. Hasil sesudahnya: **182/182 entri punya baris
`| Tema |`, 17 tema unik, tidak ada lagi "Uncoded".**

Verifikasi mandiri:
```bash
# 17 label dari nama berkas
ls entri/*.md | sed 's/.* - //; s/\.md$//' | sort | uniq -c | sort -rn
# nol varian label yang tersisa
grep -rl "Tema [Kk]laster" entri/ ; echo "(kosong = bersih)"
```

`docs/evidence-matrix-182.csv` **belum diregenerasi** — `build_evidence_matrix.py`
butuh `PDF/benar/` yang tidak ada di git. CSV lama masih memuat "Uncoded" sampai skrip
itu dijalankan di mesin yang punya PDF-nya.

---

## 3. Yang sengaja TIDAK saya kerjakan, dan kenapa

| Tidak dikerjakan | Alasan |
|---|---|
| Prosa §3/§5/§6 | Butuh korpus hasil FASE 1 yang baru selesai malam ini. Menulis lebih dulu = mengarang. |
| Membongkar `evidence-body.tex` | R3: naskah setengah-sejarah-setengah-ruang-desain lebih lemah dari kedua kerangka murni. Pembongkaran harus satu tarikan, bersamaan dengan penggantinya. |
| Menyunting 6 entri (klaster tema) | Kontrak berkas entri ketat; butuh persetujuan Anda. |
| Query Scopus/WoS | Tidak ada akses dari mesin ini. Lengan berlangganan tetap harus Anda jalankan. |
| Uji known-item Suharjito/Goh | Rujukan persisnya belum diketahui — menunggu dosen. |
| Pengayaan DOI 202 record | Belum sempat; prasyarat FASE 1.5, aman dikerjakan kapan saja. |
| Perbaikan `tools/build_evidence_matrix.py` | Belum sempat; tidak memblokir apa pun sampai FASE 4. |

---

## 4. Langkah berikutnya, berurut

1. **Cek §1 dan §2.1 di atas.** Kalau uji known-item gagal atau isi Q2 ternyata salah
   sasaran, semua yang di bawah ini tertunda.
2. **Kirim 4 konfirmasi ke dosen** (`REFRAME-DECISIONS.md` §"Wajib dikonfirmasi") —
   ini punya waktu tunggu terpanjang, kirim lebih dulu.
3. **Jalankan lengan Scopus/WoS** dengan query yang sama dari `PROTOCOL.md`, ekspor ke
   `docs/search/raw/`, lalu dedup antar-sumber.
4. Baru setelah itu: penyaringan judul–abstrak → `prisma-counts.csv` → FASE 2.

---

## Catatan integritas

Belum ada satu angka pun dari sesi ini yang layak masuk naskah. Semuanya masih
`n_raw` — belum disaring, belum dedup antar-sumber, dan lengan berlangganan belum
dijalankan. Angka corong PRISMA baru sah setelah FASE 1.5.

Dan yang paling penting, dari `REFRAME-DECISIONS.md`: **jangan pernah menyetel protokol
agar jumlah included berujung di 182.** Korpus lama dan hasil pencarian ini memang
hampir tidak beririsan — itu fakta yang dilaporkan, bukan masalah yang ditutupi.
