# Keluaran Model yang Menunggu Persetujuan Peninjau

Diperbarui 13 Oktober 2026. Aturan kerjanya ada di `AGENTS.md` §11: model menulis
ke `menunggu-acc/` dahulu, dan berkas baru dipindah ke folder cek (struktur
rencana Bu Fatma) setelah peninjau menyetujuinya. Butir yang sudah disetujui
dihapus dari daftar ini.

## Isian 13 Oktober 2026

Atas instruksi peninjau, usul model yang berstatus siap sudah diisikan ke lembar
di folder cek. Setiap isian ditandai di kolom catatan sebagai isian model yang
belum dibaca peninjau. Drafnya tetap disimpan di `menunggu-acc/` sebagai jejak.
Keputusan pada tiap butir di bawah tetap terbuka.

| Lembar | Terisi | Tersisa untuk peninjau |
|---|---:|---|
| `cek-2-cek-tangan/cek_C3` (176) | 165 lengkap, 7 hanya `konfirmasi_C3` | 4 baris berjudul saja; `kode_benar` pada 7 baris |
| `cek-2-cek-tangan/cek_eksklusi` (143) | 132 | 11 baris yang memerlukan teks lengkap |
| `cek-5-kode-ulang/kode_ulang_C1.csv` (195) | 147 (`final_*`; kode tidak berubah) | 39 usul perubahan kode, 4 berkeyakinan rendah, 5 belum dikode; drafnya ada di kolom `draf_ai_*` |
| `cek-6-cek-fakta/cek_fakta.csv` (273) | 263 | 10 klaim yang tidak dapat diperiksa |

Belum dijalankan: `verifikasi_kode_ulang.py --terapkan` (uji keringnya lolos: 147
baris, 451 sel pada kolom verifikasi, tanpa perubahan kode), perbaikan naskah
dari Cek 6, dan penerapan usul koreksi kode ke `topik/bukti/`.

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
| C3 benar, kode benar | 134 |
| C3 benar, ada usul koreksi kode | 27 |
| Bukan C3 | 4 |
| Perlu peninjau | 11 |

Angka ini sudah memuat penilaian ulang Sonnet 5.5 (butir 3a).

| Yang diputuskan | Baris |
|---|---|
| Menyetujui usul isian 165 baris berstatus `siap` untuk diisikan ke lembar | saring `status = siap` |
| Empat kajian yang dinilai bukan C3: tiga diusulkan C1 karena aturan prioritas, satu dikeluarkan dengan E6 | no 15 `daud2023detection`, no 116 `daud2022loose`, no 126 `aji2021automatic`, no 12 `narendran2024palm` |
| Empat baris yang hanya berjudul; perlu teks lengkap | no 7, 11, 21, 31 |
| Tujuh baris yang dipastikan C3 dari abstrak, tetapi kode rincinya berbeda antarpenilai (tugas, lokasi, modalitas, atau per kelas) | no 33, 35, 46, 114, 131, 132, 176 |
| Menerima atau menolak 27 usul koreksi kode; yang diterima diterapkan ke `topik/bukti/kode_C3.txt` | saring `usul_kode_benar = N` |

## 3. Cek 2, lembar eksklusi — usul isian siap, lembar belum diisi

Lembar `cek-2-cek-tangan/cek_eksklusi.xlsx` masih kosong (143 baris). Usul
isiannya ada di `menunggu-acc/cek-2/usul_isian_cek_eksklusi.csv`. Dasarnya: 95
baris dikonfirmasi Haiku 5.5; 48 baris sisanya dinilai buta oleh satu agen Opus
5.5 dan diperiksa ulang oleh agen Opus 5.5 lain (`cek_eksklusi_buta_opus.csv`).
Dari 48 baris itu, 28 dinilai dari abstrak dan 20 dari judul saja.

| Usul | Baris |
|---|---:|
| Alasan eksklusi benar | 109 |
| Tetap dikeluarkan dengan alasan lain | 4 |
| Dinilai layak masuk korpus | 19 |
| Perlu peninjau | 11 |

Angka ini sudah memuat penilaian ulang Sonnet 5.5 (butir 3a).

| Yang diputuskan | Baris |
|---|---|
| **Sembilan belas rekaman yang dinilai layak masuk** (C5 8, C2 4, C1 3, R 2, C3 1, C4 1). Memasukkannya mengubah angka korpus, gambar, dan naskah | saring `usul_catatan` yang memuat "layak masuk" |
| Sebelas baris yang buktinya tetap tidak cukup; perlu teks lengkap | saring `status = perlu peninjau` |
| Empat alasan eksklusi yang diusulkan diganti | no 7, 48, 101, 134 |
| Menyetujui usul isian 109 baris yang alasannya dikonfirmasi | saring `usul_konfirmasi_alasan = Y` |

Catatan pemeriksa atas ketidakseragaman penilaian (batas C1 pada pelacakan tanpa
hitungan, E2 lawan E3 untuk buah di mesin pemanen, lokasi yang disimpulkan dari
konteks) tertulis di kolom `verif_catatan` kedua berkas `*_buta_opus.csv`.

## 3a. Cek 2, sisa 38 baris yang buktinya belum cukup

Agen Sonnet 5.5 mencari abstrak 38 baris berstatus `perlu peninjau` dari butir 2
dan 3, lalu menilainya ulang tanpa melihat penilaian sebelumnya
(`menunggu-acc/cek-2/sisa_perlu_peninjau_sonnet.csv`). Abstrak diperoleh untuk 29
baris. Hasil ini sudah digabungkan ke `usul_isian_cek_*.csv` pada 13 Oktober 2026
dengan `dasar` "penilaian ulang Sonnet 5.5 (satu penilai, tanpa pemeriksa)":
16 baris menjadi `siap` dari penilai tunggal ini, dan 22 baris tetap
`perlu peninjau`.

| Putusan | Baris |
|---|---:|
| C3, bukti cukup | 9 |
| C3, hanya dari judul | 4 |
| C2 (layak masuk): `golder2026automated`, `kahya2025predicting` | 2 |
| Dikeluarkan (E5 9, E1 1, E2 1, E3 1) | 12 |
| Tetap tidak dapat diputuskan; perlu teks lengkap | 11 |

Yang diputuskan: **kebijakan E7**. Sepuluh rekaman berasal dari jurnal berbahasa
Mandarin dengan abstrak Inggris. Penilai Opus menebak E7; agen Sonnet menilainya
menurut isi (E5, E2, E3), karena empat PDF jurnal berbahasa Mandarin sudah masuk
peta. Alasannya harus seragam dengan rekaman yang sudah masuk.

## 3b. Cek 3 — usul keputusan

Draf: `menunggu-acc/cek-3/usul_keputusan_cek3.md` dan `.csv` (agen Sonnet 5.5).
Keenam belas makalah dikenal ada di peta dan dikutip di naskah.

| Yang diputuskan | Rincian |
|---|---|
| Empat kandidat *snowballing* yang memenuhi kriteria: Payne 2014, Apolo-Apolo 2020, Kwon 2024 (C2), Choi 2015 (C5) | Usul model: tidak ditambahkan, karena penelusuran rujukan hanya memeriksa 57 dari 635 judul |
| Kalimat `main6-body.tex` baris 75 ("ten candidates ... none met the criteria") | Hanya benar untuk kriteria multipengamatan; diusulkan diubah |
| Enam kandidat lain tidak masuk | Tiga di luar rentang tahun, satu E1, satu E5, satu duplikat |
| Lima kode mekanisme makalah dikenal yang diubah model pada 1 Oktober 2026 | Stein, Zhang, Lee, Fusaro, Indriani; belum diperiksa manusia |
| Tahun `liu2026shaping` di `.bib` | Masih 2027 |

## 3c. Cek 6 — usul cek fakta (273 klaim)

Draf: `menunggu-acc/cek-6/usul_cek_fakta.csv` dan `KEMAJUAN.md` (dua agen Sonnet
5.5 berurutan). Lembar `cek-6-cek-fakta/cek_fakta.csv` belum diisi. Putusan: 206
benar, 57 salah atau sebagian benar, 10 tidak dapat diperiksa.

| Yang diputuskan | Rincian |
|---|---|
| **Sembilan klaim yang masih salah di naskah terkini**; usul kalimat pengganti ada di `KEMAJUAN.md` | K006, K014, K020, K038-1, K112-2, K112-4, K112-5, K142, K184 |
| Hamdani 2026 menghitung buah di dalam tandan, bukan tandan; Hutapea 2024 tidak memuat hasil pencacahan | Memengaruhi kalimat "nine counting studies" dan mungkin kode kedua kajian |
| Kueri Q9 tidak memuat batas bidang subjek | Kalimat metode dan `PROTOKOL.md` bagian 2 perlu disesuaikan |
| Sepuluh klaim yang tidak dapat diperiksa | saring `usul_benar` kosong |
| Lembar `cek_fakta.csv` usang: 48 klaim salah hanya di lembar, sedangkan naskah terkini sudah benar | Buat ulang lembar dengan `verifikasi_cek_fakta.py` sebelum diisi |
| `pdf/kang2022accurate.pdf` dan teksnya memuat makalah lain dari penulis yang sama | Unduh ulang PDF yang benar (Cek 4) |

## 3d. Cek 5 — usul kode ulang C1 (190 dari 195 kajian)

Draf: `menunggu-acc/cek-5/usul_kode_ulang_C1.csv` dan `KEMAJUAN.md` (tiga agen
Sonnet 5.5 berurutan, dari teks lengkap). Kolom `final_*` di
`cek-5-kode-ulang/kode_ulang_C1.csv` belum diisi. Keyakinan: 88 tinggi, 97
sedang, 5 rendah.

| Yang diputuskan | Rincian |
|---|---|
| **Menerima atau menolak 39 usul perubahan kode** (mekanisme, akuisisi, atau per kelas); yang diterima diterapkan ke `topik/bukti/mekanisme_C1.txt` | saring `sama_dengan_kode_ai = N`; daftar di `KEMAJUAN.md` |
| Lima kajian yang belum dikode: empat PDF jurnal berbahasa Mandarin dengan lapisan teks rusak, satu tanpa PDF | no 29, 44, 48, 58; no 65 `safre2024advanced` |
| Aturan kode akuisisi untuk *pipeline* foto ke awan titik (agen memberi D, S, dan V secara tidak seragam) | `xiao20243d`, `sun2020three`, `torressanchez2021grape`, `hobart2025fruit` |
| Tujuh kajian yang status C1-nya dinilai lemah | `kutyrev2025uav`, `ahmad2024enabling`, `torressanchez2021grape`, `zineelabidine2021assigning`, `zaenker2021viewpoint`, `zaenker2023graph`, `marangoz2022fruit` |
| Tiga pasang kajian dengan data atau hasil yang tumpang tindih | `roy2019vision` dan `dong2020semantic`; `osman2021yield` dan `osman2021yieldb`; `nuske2014automated` dan `nuske2014modeling` |
| Lima kode berkeyakinan rendah | saring `keyakinan = rendah` |

Dibanding 42 usul koreksi kode di butir 1 (Cek 2): 26 kajian mendapat usul
perubahan di kedua cek, 16 hanya di Cek 2, dan 13 hanya di Cek 5. Isi usul pada
26 kajian itu belum dicocokkan. Kelima kajian yang dinilai bukan C1 di Cek 2
tetap diberi kode di sini. Lembar kerja di folder cek sudah
dibuat ulang skrip menjadi 195 baris dan tidak memuat isian.

## 4. Draf lain di `menunggu-acc/cek-2/`

`cek_C1_haiku.csv` dan `cek_C1_haiku_ulang.csv` adalah dua putaran Haiku atas
lembar C1. Isinya sudah dipakai untuk butir 1 dan disimpan sebagai jejak.

## Di luar daftar ini

- `putaran-kedua/` sudah diterapkan ke data sumber pada 1–2 Oktober 2026. Sisa
  keputusan manusianya tercatat di `../SERAH-TERIMA.md`.
- Ringkasan kajian di `../../entri/` ditulis model untuk Ruang Baca dan belum
  diperiksa peninjau.
