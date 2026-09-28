# Tinjauan Pustaka

Korpus tinjauan pustaka untuk riset tandan buah segar kelapa sawit. Ada dua
korpus:

1. **Korpus Scopus September 2026** (`scopus-2026-09/`), dasar naskah aktif
   `main6`: 5.889 rekaman unik, 971 kajian masuk peta, 187 kajian
   multi-pengamatan dikodekan mekanisme M0–M5.
2. **Korpus lama**: 182 ringkasan makalah terverifikasi, 20 entri yang ditahan
   karena PDF sumber tidak tersedia, sintesis lintas makalah, dan bahan
   pencarian OpenAlex/Scopus Agustus 2026. Dipakai naskah `main`–`main5v3` dan
   Ruang Baca situs.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Memeriksa korpus naskah `main6` | [`scopus-2026-09/`](scopus-2026-09/README.md) — [`PROTOKOL.md`](scopus-2026-09/PROTOKOL.md), [`QUERY.md`](scopus-2026-09/QUERY.md), matriks bukti `topik/bukti/matriks_bukti.csv` |
| Membaca ringkasan satu makalah | [`entries/`](entries/) — cari di [`INDEX.md`](entries/INDEX.md) (urut nomor) atau [`INDEX-TAHUN.md`](entries/INDEX-TAHUN.md) (per tahun dan tema) |
| Membaca sintesis lintas makalah | [`synthesis.md`](synthesis.md) — tayang juga di Ruang Baca situs |
| Memahami protokol pencarian | [`search/PROTOCOL.md`](search/PROTOCOL.md) |
| Mencari teks lengkap dari PDF | [`extracted/`](extracted/) — satu berkas `.md` per makalah |
| Melihat entri yang ditahan | [`withheld/`](withheld/) — 20 entri tanpa PDF sumber |
| Melihat bahan rujukan luar | [`references/`](references/) — PDF baseline SawitMVC, laporan deep research, revisi dosen |

## Isi folder

| Lokasi | Isi |
|---|---|
| `scopus-2026-09/` | Korpus `main6`: kueri, rekaman, penyaringan, matriks bukti, kajian metodologi, 331 PDF akses terbuka dan teksnya |
| `entries/` | 182 ringkasan makalah (satu berkas per makalah), `INDEX.md`, `INDEX-TAHUN.md` |
| `withheld/` | 20 entri yang ditahan karena PDF sumber tidak tersedia |
| `synthesis.md` | Sintesis lintas makalah dari seluruh korpus |
| `search/` | Protokol pencarian (`PROTOCOL.md`), kueri Scopus, daftar periksa mandiri |
| `extracted/` | Teks lengkap terekstrak dari PDF (satu `.md` per makalah) |
| `pdf/` | PDF sumber — **tidak masuk Git** karena terlalu besar |
| `references/` | Bahan rujukan luar: PDF baseline SawitMVC (DiB 2026), laporan deep research, catatan revisi dosen |
| `search-data/` | Data mentah hasil pencarian OpenAlex (`openalex-counts.csv`, `raw/`) |

## Catatan

- Nama berkas di `entries/` bersifat **load-bearing** — diparse oleh `site/build.js`.
  Format: `NNN - YYYY - Judul singkat - Tema.md`. Jangan mengubah nama berkas.
- Angka **182** adalah invarian korpus lama. Mengubah jumlah entri berarti
  memperbarui `synthesis.md`, naskah lama, dan `audit/claim-audit-182.md`.
  Angka `main6` (971, 187, dst.) hanya bersumber dari `scopus-2026-09/`.
