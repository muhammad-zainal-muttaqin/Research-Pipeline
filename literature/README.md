# Tinjauan Pustaka

Korpus tinjauan pustaka untuk riset tandan buah segar kelapa sawit. Ada dua
korpus:

1. **Korpus Scopus September 2026** (`scopus-2026-09/`), dasar naskah aktif
   `main6`: 5.889 rekaman unik, 933 kajian dinilai dari teks lengkap, 898
   kajian masuk peta, 248 kajian multi-pengamatan (C1) dikodekan menurut
   mekanisme asosiasi M0–M5. Angka terkini selalu di
   [`scopus-2026-09/ANGKA-NASKAH.md`](scopus-2026-09/ANGKA-NASKAH.md).
2. **Korpus lama**: 182 ringkasan makalah terverifikasi, 20 entri yang ditahan
   karena PDF sumber tidak tersedia, dan sintesis lintas makalah. Dipakai
   naskah 182 sumber (`main.tex`, `main-elsarticle.tex`) dan Ruang Baca situs
   bersama 898 entri `main6`.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Memeriksa korpus naskah `main6` | [`scopus-2026-09/`](scopus-2026-09/README.md): [`PROTOKOL.md`](scopus-2026-09/PROTOKOL.md), [`QUERY.md`](scopus-2026-09/QUERY.md), matriks bukti `topik/bukti/matriks_bukti.csv` |
| Mengerjakan verifikasi `main6` | [`scopus-2026-09/verifikasi/`](scopus-2026-09/verifikasi/README.md), lalu [`TUGAS.md`](scopus-2026-09/verifikasi/TUGAS.md) |
| Membaca ringkasan satu makalah | [`entries/`](entries/): cari di [`INDEX.md`](entries/INDEX.md) (urut nomor) atau [`INDEX-TAHUN.md`](entries/INDEX-TAHUN.md) (per tahun dan tema); untuk `main6`, [`scopus-2026-09/entri/`](scopus-2026-09/entri/) (788 berkas) |
| Membaca sintesis lintas makalah | [`synthesis.md`](synthesis.md): tayang juga di Ruang Baca situs |
| Mencari teks lengkap korpus lama | [`extracted/`](extracted/): satu berkas `.md` per makalah |
| Melihat entri yang ditahan | [`withheld/`](withheld/): 20 entri tanpa PDF sumber |
| Melihat bahan rujukan luar | [`references/`](references/): PDF baseline SawitMVC dan permintaan revisi dosen pembimbing |
| Melihat artikel contoh gaya tinjauan | [`example/`](example/): dirujuk `AGENTS.md` §12 |

## Isi folder

| Lokasi | Isi |
|---|---|
| `scopus-2026-09/` | Korpus `main6`: kueri, rekaman, penyaringan tiga tahap, matriks bukti, 898 ringkasan per kajian di `entri/`, kajian metodologi, PDF dan teks terekstrak, katalog PDF, lembar verifikasi |
| `entries/` | 182 ringkasan makalah (satu berkas per makalah), `INDEX.md`, `INDEX-TAHUN.md` |
| `withheld/` | 20 entri yang ditahan karena PDF sumber tidak tersedia |
| `synthesis.md` | Sintesis lintas makalah korpus lama |
| `extracted/` | Teks lengkap terekstrak dari PDF korpus lama |
| `pdf/` | PDF sumber korpus lama, **tidak masuk Git** karena terlalu besar |
| `references/` | PDF baseline SawitMVC (*Data in Brief* 2026); `revisi-dosen-2026-07-23/` berisi delapan permintaan revisi dosen (`Chat.txt`) dan laporan konvensi delapan tinjauan CEA |
| `example/` | Artikel contoh yang dirujuk panduan gaya |

Bahan pencarian OpenAlex Agustus 2026 (`search/`, `search-data/`) dihapus pada
18 November 2026 karena tidak dipakai naskah aktif. Isinya tetap dapat dibuka
di tag Git `arsip-pra-rapi-2026-11-18`.

## Catatan

- Nama berkas di `entries/` bersifat **load-bearing**: diparse oleh `site/build.js`.
  Format: `NNN - YYYY - Judul singkat - Tema.md`. Jangan mengubah nama berkas.
- Angka **182** adalah invarian korpus lama (lihat `AGENTS.md` §4). Angka
  `main6` hanya bersumber dari `scopus-2026-09/`.
