# Keluaran Model yang Menunggu Persetujuan Peninjau

Diperbarui 12 Oktober 2026. Aturan kerjanya ada di `AGENTS.md` §11: model menulis
ke `menunggu-acc/` dahulu, dan berkas baru dipindah ke folder cek (struktur
rencana Bu Fatma) setelah peninjau menyetujuinya. Butir yang sudah disetujui
dihapus dari daftar ini.

## 1. Cek 2, lembar C1 — sudah terisi, menunggu empat keputusan

Lembar `cek-2-cek-tangan/cek_C1.xlsx` sudah diisi dari penilaian model atas
instruksi peninjau (11 dan 12 Oktober 2026), sebelum aturan di atas berlaku. Asal
tiap isian tertulis di kolom `catatan`. Keadaan: 146 baris C1 dengan kode benar,
42 baris C1 dengan usul koreksi kode, 5 baris bukan C1, 2 baris kosong.

| Yang diputuskan | Baris | Bahan |
|---|---|---|
| Apakah rekonstruksi 3D dan gabungan statistik termasuk C1 (aturan Bu Fatma belum ada; model memutuskan "ya" dari definisi protokol) | 23 baris; saring `catatan` yang memuat "aturan Fatma" | `menunggu-acc/cek-2/cek_C1_sisa_opus.csv` |
| Apakah artikel data tanpa metode hitung termasuk C1 | no 167 (terisi Y) dan no 168 (kosong) | sama |
| Apakah pelacakan tanpa hitungan lintas-*frame* termasuk C1 | no 129 `arizasentis2023object` | sama |
| Apakah regresi kalibrasi dikode M1 | no 163, 165, 184 | sama |
| Menerima atau menolak 42 usul koreksi kode; yang diterima diterapkan ke `topik/bukti/mekanisme_C1.txt` dan dicatat di `log_perubahan.csv` | saring `kode_benar = N` | `menunggu-acc/cek-2/cek_C1_buta.csv`, `cek_C1_sisa_opus.csv` |
| Menerima atau menolak 5 kajian yang dinilai bukan C1 | no 35, 103, 140, 161, 194 | sama |

No 17 `safre2024advanced` tetap kosong karena tidak ada PDF.

## 2. Cek 2, lembar C3 — usul isian siap, lembar belum diisi

Lembar `cek-2-cek-tangan/cek_C3.xlsx` masih kosong (176 baris). Usul isiannya ada
di `menunggu-acc/cek-2/usul_isian_cek_C3.csv` (kolom `usul_*`, `status`, `dasar`).
Dasarnya: 83 baris dikonfirmasi Haiku 5.5 dalam dua putaran; 93 baris sisanya
dinilai buta oleh dua agen Opus 5.5 dan diperiksa ulang oleh agen Opus 5.5 ketiga
(`cek_C3_buta_opus.csv`). Dari 93 baris itu, 6 dinilai dari teks lengkap, 74
dari abstrak, dan 13 dari judul saja.

| Usul | Baris |
|---|---:|
| C3 benar, kode benar | 132 |
| C3 benar, ada usul koreksi kode | 27 |
| Bukan C3 | 4 |
| Perlu peninjau | 13 |

| Yang diputuskan | Baris |
|---|---|
| Menyetujui usul isian 163 baris berstatus `siap` untuk diisikan ke lembar | saring `status = siap` |
| Empat kajian yang dinilai bukan C3: tiga diusulkan C1 karena aturan prioritas, satu dikeluarkan dengan E6 | no 15 `daud2023detection`, no 116 `daud2022loose`, no 126 `aji2021automatic`, no 12 `narendran2024palm` |
| Sembilan baris yang buktinya tidak cukup (tujuh hanya berjudul); perlu abstrak atau teks lengkap | saring `status = perlu peninjau` |
| Empat baris yang kode rincinya berbeda antara penilai dan pemeriksa (lokasi, modalitas, atau tugas) | sama |
| Menerima atau menolak 27 usul koreksi kode; yang diterima diterapkan ke `topik/bukti/kode_C3.txt` | saring `usul_kode_benar = N` |

## 3. Cek 2, lembar eksklusi — usul isian siap, lembar belum diisi

Lembar `cek-2-cek-tangan/cek_eksklusi.xlsx` masih kosong (143 baris). Usul
isiannya ada di `menunggu-acc/cek-2/usul_isian_cek_eksklusi.csv`. Dasarnya: 95
baris dikonfirmasi Haiku 5.5; 48 baris sisanya dinilai buta oleh satu agen Opus
5.5 dan diperiksa ulang oleh agen Opus 5.5 lain (`cek_eksklusi_buta_opus.csv`).
Dari 48 baris itu, 28 dinilai dari abstrak dan 20 dari judul saja.

| Usul | Baris |
|---|---:|
| Alasan eksklusi benar | 98 |
| Tetap dikeluarkan dengan alasan lain | 3 |
| Dinilai layak masuk korpus | 17 |
| Perlu peninjau | 25 |

| Yang diputuskan | Baris |
|---|---|
| **Tujuh belas rekaman yang dinilai layak masuk** (C5 8, C1 3, C2 2, R 2, C3 1, C4 1). Memasukkannya mengubah angka korpus, gambar, dan naskah | saring `usul_catatan` yang memuat "layak masuk" |
| Dua puluh lima baris yang buktinya tidak cukup (20 hanya berjudul). Sepuluh di antaranya ditebak E7 dari nama jurnal dan perlu dipastikan bahasanya | saring `status = perlu peninjau` |
| Tiga alasan eksklusi yang diusulkan diganti | no 48, 101, 134 |
| Menyetujui usul isian 98 baris yang alasannya dikonfirmasi | saring `usul_konfirmasi_alasan = Y` |

Catatan pemeriksa atas ketidakseragaman penilaian (batas C1 pada pelacakan tanpa
hitungan, E2 lawan E3 untuk buah di mesin pemanen, lokasi yang disimpulkan dari
konteks) tertulis di kolom `verif_catatan` kedua berkas `*_buta_opus.csv`.

## 4. Draf lain di `menunggu-acc/cek-2/`

`cek_C1_haiku.csv` dan `cek_C1_haiku_ulang.csv` adalah dua putaran Haiku atas
lembar C1. Isinya sudah dipakai untuk butir 1 dan disimpan sebagai jejak.

## Di luar daftar ini

- `putaran-kedua/` sudah diterapkan ke data sumber pada 1–2 Oktober 2026. Sisa
  keputusan manusianya tercatat di `../SERAH-TERIMA.md`.
- Ringkasan kajian di `../../entri/` ditulis model untuk Ruang Baca dan belum
  diperiksa peninjau.
