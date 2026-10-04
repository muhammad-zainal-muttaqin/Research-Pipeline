# Cek 2 — Pemeriksaan Tangan Keputusan Terpenting

> Berkas ini dibuat ulang oleh `tools/scopus/verifikasi_cek_tangan.py` setiap kali
> skrip dijalankan (terakhir 2026-09-28). Jangan disunting
> tangan; ubah skripnya.

## Tujuan

Penyaringan dan pengodean korpus `main6` dilakukan satu peninjau dengan bantuan
model bahasa besar (`PROTOKOL.md` §6). Cek 2 memastikan keputusan yang paling
menentukan isi naskah benar-benar diperiksa manusia. **Setiap keputusan di cek
ini adalah keputusan peninjau.** Lembar hanya menampilkan keputusan dan kode
model beserta bukti untuk menilainya; kolom konfirmasi sengaja kosong dan tidak
pernah diisi skrip.

## Lembar kerja

Lembar tersedia dalam format `.csv` dan `.xlsx` di folder ini. Isi lembar `.xlsx` (ada daftar pilihan dan teks terbungkus). Jangan mengisi CSV dan XLSX sekaligus untuk baris yang sama; bila keduanya berbeda, skrip berhenti dan meminta Anda menyelaraskannya. Untuk mengosongkan isian, kosongkan di kedua berkas (skrip mengambil nilai yang tidak kosong).

| Kelompok | Lembar | Jumlah | Rencana | Diputuskan dari judul saja | Sudah dikonfirmasi |
|---|---|---:|---:|---:|---:|
| Kajian inti C1 | `cek_C1` | 187 | 187 | 42 | 0 |
| Kajian sawit C3 | `cek_C3` | 170 | 170 | 35 | 0 |
| Eksklusi tahap kelayakan | `cek_eksklusi` | 153 | 153 | 30 | 0 |

Rencana kelompok "judul saja": C1 42, C3 35.

Kolom penting:

- `hanya_judul = Y`: keputusan model dibuat dari judul dan sumber saja (baris di
  `abstrak_T00.txt` atau bertanda `(judul)`). Kolom `abstrak` biasanya kosong.
- `pdf_ada`, `path_teks`: teks lengkap ada di `literature/scopus-2026-09/pdf/<key>.pdf`
  dan `teks/<key>.txt`.
- `catatan_skrip`: diisi skrip (kode `?`, abstrak yang baru tersedia, sumber yang
  kini berbeda dari kolom `*_ai`, baris yang tidak lagi termasuk kelompoknya).
- Kolom berlatar kuning (`konfirmasi_*`, `kode_benar`, `seharusnya_C1_atau_C3`,
  `catatan`) adalah milik peninjau. Arti kode ada di lembar `keterangan`.

## Urutan kerja yang disarankan

1. **Rekaman yang diputuskan dari judul saja** (saring `hanya_judul = Y`) di
   `cek_C1` lalu `cek_C3`. Sebelum memutuskan, cari dulu abstrak atau teks
   lengkapnya (DOI, halaman penerbit, PDF lokal bila `pdf_ada = Y`). Bila tidak
   ada yang dapat dibaca, tulis di `catatan` sumber apa yang sudah dicoba.
2. **Sisa `cek_C1`**: apakah kajian sungguh menggabungkan beberapa pengamatan
   buah yang sama (video, beberapa pandang, pindaian berulang)? Isi
   `konfirmasi_C1`; lalu periksa mekanisme, akuisisi, dan per_kelas → `kode_benar`.
3. **Sisa `cek_C3`**: apakah kajian mencitrakan TBS kelapa sawit? Isi
   `konfirmasi_C3`; lalu periksa tugas, lokasi, modalitas, dan multipandang →
   `kode_benar`. Kode `?` (lihat `catatan_skrip`) diputuskan dari teks lengkap bila ada.
4. **`cek_eksklusi`**: apakah alasan E1–E7 benar (`konfirmasi_alasan`), dan apakah
   ada kajian C1 atau C3 yang hilang (`seharusnya_C1_atau_C3`). Dahulukan baris
   dengan `hanya_judul = Y` dan baris yang `sinyal_kata_kunci`-nya berisi `sawit`
   atau `multi-observasi` (petunjuk prioritas otomatis, bukan keputusan).

## Mencatat perubahan

Lembar cek hanya mencatat penilaian. Bila penilaian mengubah keputusan atau kode,
ubah juga berkas sumbernya, lalu catat setiap perubahan di log.

| Yang berubah | Berkas yang disunting |
|---|---|
| Keputusan penyaringan (C1/C2/C3/…/X, alasan E#) | baris `idx KODE [E#]` di `topik/penyaringan/abstrak_*.txt` |
| Kode mekanisme, akuisisi, per_kelas, hasil ringkas C1 | `topik/bukti/mekanisme_C1.txt` |
| Kode tugas, lokasi, modalitas, multipandang, per_kelas C3 | `topik/bukti/kode_C3.txt` |
| **Setiap** perubahan di atas | `verifikasi/log_perubahan.csv` |

Aturan penyuntingan berkas penyaringan:

- Saat ini setiap idx muncul tepat satu kali di seluruh `abstrak_*.txt`. Sunting
  baris itu di tempatnya; jangan menambah baris kedua di berkas lain. Bila suatu
  idx sampai muncul lebih dari sekali, `kode_bukti.py` memakai baris terakhir
  menurut urutan nama berkas (`abstrak_00` … `abstrak_08`, `B00` … `B03`, `T00`),
  sedangkan hitungan "judul saja" di `gambar_tinjauan.py` menghitung setiap baris,
  sehingga angka PRISMA menjadi salah.
- Dasar keputusan "judul" ditentukan oleh letak baris di `abstrak_T00.txt` atau
  tanda `(judul)`. Bila Anda memutuskan ulang setelah membaca abstrak, catat
  `kolom = dasar_keputusan` di log; memindahkan baris antarberkas mengubah angka
  254 di `PROTOKOL.md` dan naskah, jadi putuskan itu secara sadar.
- Rekaman yang menjadi C1 perlu baris baru di `mekanisme_C1.txt`; yang menjadi C3
  perlu baris baru di `kode_C3.txt`. Rekaman yang keluar dari C1/C3 dihapus
  barisnya dari berkas kode itu.

Format `log_perubahan.csv` (satu baris per sel yang berubah):

```
tanggal,berkas,idx_atau_key,kolom,nilai_lama,nilai_baru,alasan,oleh
2026-10-05,topik/penyaringan/abstrak_T00.txt,1234,kode,C2,C1,"abstrak: pelacakan video dengan garis hitung",MZM
```

`tanggal` ISO (YYYY-MM-DD); `berkas` relatif terhadap `literature/scopus-2026-09/`;
`kolom` misalnya `kode`, `alasan`, `mekanisme`, `akuisisi`, `tugas`, `lokasi`,
`multipandang`, `per_kelas`, `dasar_keputusan`; `oleh` inisial peninjau.

## Setelah ada perubahan

1. `python3 tools/scopus/kode_bukti.py` (matriks bukti), lalu
   `gambar_tinjauan.py` dan `tabel_lampiran.py`.
2. Perbarui angka di naskah `main6`, `PROTOKOL.md`, dan `AGENTS.md` §3
   (`AGENTS.md` §7).
3. Jalankan ulang skrip ini. Isian peninjau dipertahankan; kolom `*_ai` tetap
   menunjukkan nilai yang dinilai, dan `catatan_skrip` mencatat nilai sumber yang
   kini berbeda.

## Tenggat

**20 Oktober 2026**: kirim `log_perubahan.csv` sejauh yang sudah terisi kepada Fatma,
meskipun Cek 2 belum selesai seluruhnya.

## Peringatan dari eksekusi terakhir

- Tidak ada.
