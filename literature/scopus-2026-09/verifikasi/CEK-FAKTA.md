# Cek 6: Cek Fakta Naskah `main6`

Setiap kalimat yang melaporkan hasil sebuah kajian harus cocok dengan makalah
yang dikutipnya. Lembar kerjanya adalah `cek_fakta.csv`: satu baris untuk
setiap pasangan klaim dan kajian yang dikutip. Lembar ini dibuat oleh
`tools/scopus/verifikasi_cek_fakta.py` dari `main6-body.tex` dan abstrak di
`main6.tex`. Tenggatnya **13 November 2026**, setelah kode C1 diperbarui (Cek 5).

## 1. Kolom

| Kolom | Isi | Diisi oleh |
|---|---|---|
| `id` | `K001`; akhiran `-2`, `-3` bila satu kalimat mengutip beberapa kajian | skrip |
| `prioritas` | Urutan kerja (bagian 2) | skrip |
| `bagian` | Seksi naskah; untuk baris tabel disertai label tabel | skrip |
| `jenis` | `baris_tabel`, `kalimat`, `abstrak`, atau `angka_korpus` | skrip |
| `kalimat` | Klaim sebagaimana tertulis di naskah; kutipan ditulis `[key]` | skrip |
| `key`, `kajian` | Kunci BibTeX dan penulis (tahun) makalah yang dikutip | skrip |
| `pdf_ada`, `teks_lokal` | Apakah PDF ada di `pdf/`, dan jalur teksnya di `teks/` | skrip |
| `halaman` | Halaman, tabel, atau gambar tempat klaim itu ditemukan | manusia |
| `benar` | `Y` atau `N` | manusia |
| `perbaikan` | Kata atau angka yang benar, bila `N` | manusia |
| `catatan`, `oleh`, `tanggal` | Keterangan, pemeriksa, tanggal periksa | manusia |

AI boleh membantu mencari halaman, tetapi nilai `halaman` dan `benar` hanya
diisi setelah pemeriksa membuka sumbernya sendiri.

## 2. Urutan kerja

| Prioritas | Isi |
|---|---|
| 1 | Tabel 2 dan 3 rencana: `tab:acq` (8 kajian akuisisi) dan `tab:assoc` (13 perbandingan pada data yang sama). Sejak tabel RQ (`tab:rqmap`) ditambahkan, keduanya bernomor III dan IV di PDF |
| 2 | Abstrak dan angka di Pendahuluan |
| 3 | Kalimat berkutipan di seksi akuisisi, mekanisme, atribut kelas, depth, dan sawit |
| 4 | Tabel tinjauan terdahulu: cakupan dan metode yang dinyatakan setiap tinjauan |
| 5 | Kalimat berkutipan di seksi lain |
| S | Angka hasil skrip (misalnya "113 of 182 use M3"): tidak dicek ke makalah; cukup dicocokkan dengan keluaran `kode_bukti.py` setelah dijalankan ulang pada Cek 5 |

Untuk baris `abstrak` dan klaim umum, periksa berapa kajian yang mendukungnya.
Contohnya, "appearance features did not improve tracking" bertumpu pada dua
kajian, jadi abstrak harus menyebutkannya.

## 3. Menjalankan ulang

```bash
python tools/scopus/verifikasi_cek_fakta.py
```

Jalankan ulang setelah naskah disunting. Isian manusia dipertahankan menurut
pasangan (`kalimat`, `key`). Baris berisi isian yang kalimatnya sudah berubah
tetap disimpan di bawah dengan prioritas `lama`. Setiap perbaikan pada naskah
juga dicatat di `log_perubahan.csv`.
