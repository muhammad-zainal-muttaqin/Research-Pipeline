# Tinjauan Pustaka

Korpus tinjauan pustaka untuk riset deteksi tandan buah segar kelapa sawit.
Berisi 182 ringkasan makalah terverifikasi, 20 entri yang ditahan karena PDF
sumber tidak tersedia, sintesis lintas makalah, dan seluruh bahan pendukung
pencarian literatur.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Membaca ringkasan satu makalah | [`entries/`](entries/) — cari di [`INDEX.md`](entries/INDEX.md) (urut nomor) atau [`INDEX-TAHUN.md`](entries/INDEX-TAHUN.md) (per tahun dan tema) |
| Membaca sintesis lintas makalah | [`synthesis.md`](synthesis.md) — tayang juga di Ruang Baca situs |
| Memahami protokol pencarian | [`search/PROTOCOL.md`](search/PROTOCOL.md) |
| Mencari teks lengkap dari PDF | [`extracted/`](extracted/) — satu berkas `.md` per makalah |
| Melihat entri yang ditahan | [`withheld/`](withheld/) — 20 entri tanpa PDF sumber |
| Melihat bahan rujukan luar | [`references/`](references/) — PDF baseline SawitMVC, laporan deep research, revisi dosen |

## Isi folder

| Lokasi | Isi |
|---|---|
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
- Angka **182** adalah invarian yang dijaga di seluruh repo. Mengubah jumlah entri
  berarti memperbarui `synthesis.md`, naskah, dan `audit/claim-audit-182.md`.
