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

**Kalau ada yang GAGAL, query itu belum layak dipakai** dan angka corongnya tidak boleh
masuk naskah. Perbaiki query, catat versi yang gagal di `PROTOCOL.md` §10 (jangan
dihapus), jalankan ulang.

Suharjito dan Goh **belum diuji** — rujukan persisnya masih menunggu konfirmasi dosen
(lihat `REFRAME-DECISIONS.md`, konfirmasi #4).

### 2.2 Rekap jumlah + batas yang tersentuh

```bash
cat docs/search/openalex-counts.csv
```

Kolom **`terpotong_oleh_batas`** adalah yang penting. Skrip berhenti di 5.000 record per
query sebagai penjaga runaway. Query mana pun yang bernilai `YA` **belum lengkap** — ia
harus dipersempit (query terlalu luas) atau batasnya dinaikkan sebelum angkanya dipakai
sebagai `n_raw` di corong PRISMA. Ini dicatat, bukan didiamkan.

### 2.3 Klaster tema — sudah terpecahkan, tinggal diputuskan

Inkonsistensi 14/17/18 yang saya laporkan kemarin **bukan tiga angka yang berbeda —
hanya satu yang benar**:

| Sumber | Angka | Status |
|---|---|---|
| Nama berkas `entri/*.md` (segmen terakhir) | **17** | benar, 182/182 berkas terparse |
| Baris `\| Tema \|` di dalam entri | **17** | sepakat dengan nama berkas |
| `docs/evidence-matrix-182.csv` | 18 | 17 + kategori palsu "Uncoded" |
| `CLAUDE.md` | 14 | **salah** |

Penyebab angka 18: **6 entri tidak punya baris `| Tema |`**, jadi jatuh ke "Uncoded".
Temanya bisa dipulihkan dari nama berkasnya sendiri:

| Entri | Tema dari nama berkas |
|---|---|
| `126 - 2019 - Automated Fruit Harvesting Robot (Onishi dkk.)` | Pertanian |
| `149 - 2018 - CBAM` | Fusi Multimodal |
| `151 - 2023 - Object Detection in 20 Years (Zou dkk.)` | Fusi Multimodal |
| `153 - 2021 - Survei RGB-D SOD (Zhou dkk.)` | Fusi Multimodal |
| `156 - 2024 - YOLO-World` | Fondasi RGB |
| `163 - 2022 - Swin Transformer V2` | Fondasi RGB |

> **Perbaikannya belum saya kerjakan** — menyentuh 6 berkas entri dan mengharuskan
> `node build.js` dijalankan ulang. Saya tidak mau menyunting entri tanpa Anda melihat
> dulu, karena kontrak berkas entri ketat (`docs/PANDUAN-PENULISAN.md` §2).
> **Keputusan Anda:** setuju tambahkan baris `| Tema |` ke 6 entri itu dan ubah
> `CLAUDE.md` 14 → 17? Kalau ya, ini pekerjaan 15 menit.

Verifikasi mandiri:
```bash
ls entri/*.md | sed 's/.* - //; s/\.md$//' | sort | uniq -c | sort -rn
```

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
