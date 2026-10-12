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

## 2. Cek 2, lembar C3 — belum diisi

Lembar `cek-2-cek-tangan/cek_C3.xlsx` masih kosong (176 baris).

| Draf | Isi |
|---|---|
| `menunggu-acc/cek-2/cek_C3_haiku.csv` | Putaran pertama Haiku 5.5 atas 176 kajian: 149 dikonfirmasi C3, 20 ragu, 7 bukan C3 |
| `menunggu-acc/cek-2/cek_C3_haiku_ulang.csv` | Putaran ulang atas 64 kajian yang ragu atau ditolak: 54 dikonfirmasi C3, 6 ragu, 4 bukan C3 |

Yang diputuskan: apakah lembar C3 boleh diisi dari draf ini, dan bagaimana
memperlakukan baris yang tetap ragu.

## 3. Cek 2, lembar eksklusi — belum diisi

Lembar `cek-2-cek-tangan/cek_eksklusi.xlsx` masih kosong (143 baris).

| Draf | Isi |
|---|---|
| `menunggu-acc/cek-2/cek_eksklusi_haiku.csv` | Putaran pertama atas 143 rekaman: alasan eksklusi dikonfirmasi pada 78, ragu 37, ditolak 28; 9 rekaman diusulkan sebagai C1 atau C3 |
| `menunggu-acc/cek-2/cek_eksklusi_haiku_ulang.csv` | Putaran ulang atas 65 rekaman: 17 dikonfirmasi, 23 ragu, 25 ditolak; 4 rekaman tetap diusulkan sebagai C1 atau C3 |

Yang diputuskan: apakah lembar eksklusi boleh diisi dari draf ini, dan apakah
empat rekaman itu masuk korpus.

## 4. Draf lain di `menunggu-acc/cek-2/`

`cek_C1_haiku.csv` dan `cek_C1_haiku_ulang.csv` adalah dua putaran Haiku atas
lembar C1. Isinya sudah dipakai untuk butir 1 dan disimpan sebagai jejak.

## Di luar daftar ini

- `putaran-kedua/` sudah diterapkan ke data sumber pada 1–2 Oktober 2026. Sisa
  keputusan manusianya tercatat di `../SERAH-TERIMA.md`.
- Ringkasan kajian di `../../entri/` ditulis model untuk Ruang Baca dan belum
  diperiksa peninjau.
