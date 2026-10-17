# Serah-Terima Teknis Verifikasi `main6`

Diperbarui 17 Oktober 2026. Dokumen ini untuk agen dan penulis yang menjalankan
skrip. Peninjau mulai dari [README.md](README.md). Keputusan yang menunggu
peninjau hanya dicatat di [TUGAS.md](TUGAS.md); arti kode di
[ISTILAH.md](ISTILAH.md).

## 1. Aturan agar data tidak rusak

- Keluaran model ditulis ke `hasil-kerja-ai/menunggu-acc/<cek>/` dahulu. Setiap
  keputusan yang diminta dari peninjau ditambahkan ke `TUGAS.md` dengan pola
  butirnya. Butir dihapus setelah jawaban peninjau diterapkan (`AGENTS.md` §11).
- Isian model di lembar cek selalu ditandai di kolom `catatan` atau
  `catatan_peninjau`. Kolom manusia (`keputusan_manusia`, `final_*`, `benar`,
  `oleh`) tidak diisi model kecuali atas instruksi eksplisit peninjau, dan asal
  isiannya tetap ditulis.
- Putaran pertama dibaca dari salinan `hasil-kerja-ai/putaran-kedua/putaran_1/`;
  jangan dihapus. Perubahan kelompok putaran kedua hanya diterapkan bila
  penyanggah menyatakan `bertahan`; rekaman `perlu manusia` memakai nilai
  putaran pertama.
- Urutan penerapan putaran kedua tetap: `verifikasi_ai2_terapkan.py`, lalu
  `verifikasi_ai2_judul.py terapkan`. Yang pertama membangun ulang berkas kode
  dari salinan putaran 1; keduanya idempoten.
- Rekaman yang dimasukkan peninjau ditulis ke `topik/penyaringan/abstrak_F00.txt`
  (tidak ditimpa skrip `verifikasi_ai2*.py`) dan dicatat di `log_perubahan.csv`.
- Kode C1 dan C3 hanya diubah di `topik/bukti/mekanisme_C1.txt` dan
  `kode_C3.txt`, dengan baris di `log_perubahan.csv`.
- Naskah tidak memuat jalur folder atau kode internal; angka korpus hanya lewat
  makro `\nXxx`/`\pXxx`. Penyaringan ditulis sebagai satu peninjau dengan bantuan
  model, bukan dua peninjau independen.
- Jangan menyunting tangan: `main6-angka.tex`, `main6-appendix-*.tex`,
  `references6.bib`, `figures/main6/F*`, `ANGKA-NASKAH.md`, serta panduan cek
  yang dibuat skrip (`CEK-TANGAN.md`, `KODE-ULANG.md`, `CEK-FAKTA.md`,
  `PERMINTAAN-PDF.md`).
- Model untuk *workflow*: Sonnet 5.5, `effort: 'high'` (permintaan pengguna
  2 Oktober 2026).

## 2. Perintah bangun ulang

Jalankan berurutan dari akar repo setiap kali data atau kode berubah:

```bash
python tools/scopus/kode_bukti.py
python tools/scopus/gambar_tinjauan.py
python tools/scopus/tabel_lampiran.py
python tools/scopus/lampiran_kueri.py
python tools/scopus/angka_naskah.py --simpan      # ANGKA-NASKAH.md dan main6-angka.tex
python tools/scopus/buat_bib.py --rekaman literature/scopus-2026-09/topik/records_all.csv literature/scopus-2026-09/metodologi/records_MA*.csv literature/scopus-2026-09/topik/tambahan_metode_lain.csv --kunci literature/scopus-2026-09/topik/bukti/matriks_bukti.csv literature/scopus-2026-09/metodologi/terpilih.csv literature/scopus-2026-09/topik/tambahan_metode_lain.csv --cache literature/scopus-2026-09/crossref.jsonl --keluar manuscript/source/references6.bib
cd manuscript/source && tectonic main6.tex && mv main6.pdf ../output/papers/
```

| Cek | Skrip di `tools/scopus/` |
|---|---|
| 1 | `verifikasi_sampel.py` (tarik sampel), `verifikasi_kappa.py` (kesepakatan dan kappa) |
| 2 | `verifikasi_cek_tangan.py` (`--segarkan-ai` membuat ulang lembar dari korpus terkini) |
| 4 | `verifikasi_teks_lengkap.py` |
| 5 | `verifikasi_kode_ulang.py` (`--terapkan` memindahkan `final_*` ke `mekanisme_C1.txt`) |
| 6 | `verifikasi_cek_fakta.py` (isian dipertahankan per pasangan kalimat dan kunci; kalimat yang berubah menjadi baris `lama`) |
| Putaran kedua | `verifikasi_ai2.py`, `verifikasi_ai2_gabung.py`, `verifikasi_ai2_terapkan.py`, `verifikasi_ai2_judul.py` |

## 3. Pekerjaan teknis yang tersisa

1. Menerapkan jawaban peninjau atas butir `TUGAS.md`, lalu bangun ulang (bagian 2)
   dan perbarui teks naskah, `PROTOKOL.md`, dan `AGENTS.md` §3 bila angka berubah.
2. `verifikasi_kode_ulang.py --terapkan` setelah peninjau menyetujui butir 3.7.
   Uji keringnya lolos: 147 baris, 451 sel pada kolom verifikasi, tanpa
   perubahan kode.
3. Pemeriksaan ulang eksklusi tahap judul untuk kueri Q2 dan Q4–Q9 (sekitar
   3.300 rekaman) belum dikerjakan. Pakai `verifikasi_ai2_judul.py` dengan
   mengubah `KUERI_INTI`. Q1 dan Q3 sudah selesai (1.325 rekaman, 19 dimasukkan
   kembali; laporan `hasil-kerja-ai/putaran-kedua/ULANG-JUDUL.md`).
4. OCR empat PDF jurnal CSAM: `guo2023real`, `tu2026passion`,
   `wang2024camellia`, `zhu2022identification`.
5. Ekstrak ulang teks `kang2022accurate` setelah peninjau mengganti PDF-nya
   (butir 4.4).
6. Penulisan ulang gaya mengikuti `manuscript/guides/CATATAN-GAYA-TULIS-CONTOH.md`
   yang belum selesai: pembagian paragraf panjang, kolom hasil terpisah di tabel
   perbandingan, ringkasan sawit per subseksi. Aturan: jangan memperpanjang
   kalimat; satu kajian per kalimat; kutip dengan `\citet`.
7. Ringkasan Ruang Baca (`../entri/`): 176 dari 479 kajian ber-PDF; kepala entri
   dibuat `tools/scopus/entri_main6.py`. Isinya ditulis model dan belum
   diperiksa peninjau.

## 4. Riwayat dan asal-usul isian

### Cek 1

Dihitung 4 Oktober 2026: judul 256 dari 300 sepakat (kappa 0,57); abstrak 86
dari 165 (kappa 0,45); 5 judul kritis. Bu Fatma memutuskan kelima judul itu pada
5 Oktober 2026: empat dikeluarkan, idx 3661 (Qiu dkk., 2022) masuk sebagai C5,
sehingga tidak perlu menarik 300 judul tambahan. Keputusan diisikan ke
`ketidaksepakatan.csv` dan `sampel_judul.csv`; idx 3661 dimasukkan lewat
`abstrak_F00.txt`. Aturan stereo dan prioritas C1 ditambahkan ke `PROTOKOL.md`
bagian 4, `cek-1-sampel-buta/PANDUAN.md`, dan bagian metode naskah. Kode E1 untuk
idx 1338 dilengkapi peninjau pada 11 Oktober 2026 dan menunggu konfirmasi
Bu Fatma.

### Putaran kedua (1–2 Oktober 2026)

| Pekerjaan | Hasil | Berkas |
|---|---|---|
| Putaran kedua buta atas 510 rekaman kunci, sampel buta Cek 1, cek fakta | 115 paket | `hasil-kerja-ai/putaran-kedua/hasil/`, `RINGKASAN-BANDING.md` |
| Ajudikasi 227 rekaman yang berbeda dan uji sanggah | 16 kelompok berubah, 7 disanggah, 10 diserahkan ke manusia | `PERUBAHAN-AI2.md`, `keputusan_final.csv` |
| Penerapan ke data sumber | `abstrak_*.txt`, `mekanisme_C1.txt`, `kode_C3.txt`, `log_perubahan.csv` (oleh = AI-2) | `verifikasi_ai2_terapkan.py` |
| Cek 3 | Häni 2020 C2 → C1; Liu dan Ampatzidis 2026 sebagai rekaman metode lain | `topik/tambahan_metode_lain.csv` |
| Cek fakta putaran kedua | 31 klaim salah atau sebagian benar diperbaiki di naskah | `hasil/vf_*.json` |

### Isian model di lembar Cek 2 (11–13 Oktober 2026)

Semua isian dibuat atas instruksi peninjau dan ditandai di kolom `catatan`.

- **`cek_C1`.** 117 baris dari konfirmasi Haiku 5.5 dua putaran
  (`menunggu-acc/cek-2/cek_C1_haiku.csv`, `cek_C1_haiku_ulang.csv`); 47 baris
  dari penilaian buta per makalah (Opus 5.5 untuk 42 makalah, Haiku 5.5 *effort*
  high untuk 35; `cek_C1_buta.csv`); 32 baris sisa dinilai buta oleh tiga agen
  Opus 5.5 dan diperiksa agen Opus 5.5 keempat (`cek_C1_sisa_opus.csv`). Kasus
  rekonstruksi 3D dan gabungan statistik diputuskan model dari definisi
  protokol. Keadaan: 146 Y/Y, 42 usul koreksi kode, 5 bukan C1, 2 kosong
  (`safre2024advanced` tanpa PDF; `genemola2020lfuji` karena penilai dan
  pemeriksa tidak sepakat).
- **`cek_C3`.** 83 baris dikonfirmasi Haiku 5.5 dua putaran; 93 baris dinilai
  buta oleh dua agen Opus 5.5 dan diperiksa agen Opus 5.5 ketiga
  (`cek_C3_buta_opus.csv`; 6 dari teks lengkap, 74 dari abstrak, 13 dari judul).
  Usul gabungan di `usul_isian_cek_C3.csv`: 134 benar, 27 usul koreksi, 4 bukan
  C3, 11 perlu peninjau. Terisi 172 baris (165 lengkap, 7 hanya `konfirmasi_C3`).
- **`cek_eksklusi`.** 95 baris dikonfirmasi Haiku 5.5; 48 baris dinilai buta
  oleh agen Opus 5.5 dan diperiksa agen Opus 5.5 lain
  (`cek_eksklusi_buta_opus.csv`; 28 dari abstrak, 20 dari judul). Usul gabungan
  di `usul_isian_cek_eksklusi.csv`: 109 alasan benar, 4 alasan lain, 19 layak
  masuk, 11 perlu peninjau. Terisi 132 baris.
- **Sisa 38 baris** berstatus perlu peninjau dinilai ulang buta oleh satu agen
  Sonnet 5.5 tanpa pemeriksa (`sisa_perlu_peninjau_sonnet.csv`); abstrak
  diperoleh untuk 29 baris; 16 baris menjadi siap, 22 tetap perlu peninjau.
  Angka di atas sudah memuat hasil ini.
- Catatan pemeriksa atas ketidakseragaman penilaian (batas C1 pada pelacakan
  tanpa hitungan, E2 lawan E3 untuk buah di mesin pemanen, lokasi yang
  disimpulkan dari konteks) ada di kolom `verif_catatan` kedua berkas
  `*_buta_opus.csv`.

### Cek 3, 4, 5, dan 6

- **Cek 3.** Usul keputusan agen Sonnet 5.5 di `menunggu-acc/cek-3/`. Keenam
  belas makalah dikenal ada di peta dan dikutip. Dari sepuluh kandidat
  *snowballing*, empat memenuhi kriteria; enam tidak (tiga di luar rentang
  tahun, satu E1, satu E5, satu duplikat).
- **Cek 4.** 213 dari 214 kajian memiliki PDF (C1 194 dari 195);
  `safre2024advanced` tidak diperoleh dan dilaporkan lewat makro
  `\nMultiNoFullText` atas arahan Bu Fatma (5 Oktober 2026). 41 PDF dibeli. Teks
  diekstrak ke `../teks/` (476 berkas). Makro `\nFullText` menghitung PDF yang
  diperoleh (479 dari 1.001).
- **Cek 5.** Tiga agen Sonnet 5.5 berurutan mengodekan 190 dari 195 kajian dari
  teks lengkap (`menunggu-acc/cek-5/usul_kode_ulang_C1.csv`, `KEMAJUAN.md`;
  keyakinan 88 tinggi, 97 sedang, 5 rendah; 39 usul perubahan). Kolom `final_*`
  diisi pada 13 Oktober 2026 untuk 147 baris yang kodenya tidak berubah.
  Dibanding 42 usul koreksi Cek 2: 26 kajian mendapat usul di kedua cek, 16 hanya
  di Cek 2, 13 hanya di Cek 5; isi usul pada 26 kajian itu belum dicocokkan.
- **Cek 6.** Dua agen Sonnet 5.5 berurutan menilai 273 klaim dari lembar yang
  disusun dari naskah 29 September 2026 (`menunggu-acc/cek-6/usul_cek_fakta.csv`,
  `KEMAJUAN.md`): 206 benar, 57 salah atau sebagian benar, 10 tidak dapat
  diperiksa. Pada 16 Oktober 2026 lembar dibuat ulang dari naskah terkini: 203
  klaim, 292 baris. 61 baris mempertahankan isian model; 8 baris salah disalin
  dari baris lamanya (asal di `catatan`); 223 baris kosong; 202 isian lama
  disimpan sebagai baris `lama` berawalan `L-`. `peta_klaim_kosong.csv` memuat
  baris lama terdekat untuk tiap baris kosong (kemiripan ≥0,9: 34; 0,6–0,9: 55;
  0,3–0,6: 69; tanpa padanan: 65). Padanan id `KEMAJUAN.md` ke lembar baru:
  K020 → K021, K038-1 → K043-1, K112-2/4/5/6 → K136-2/4/5/6, K142 → K170,
  K184 → K200, K094-1 → K113-1; K006 dan K014 tetap.

### Naskah

Ditulis ulang pada 2 dan 5 Oktober 2026: bagian metode (kedua putaran), tabel
kelompok, tabel RQ, nama mekanisme tanpa M0–M5, perbaikan cek fakta, abstrak,
Declaration of AI. Dikompilasi 16 Oktober 2026: 34 halaman, tanpa rujukan atau
sitasi yang tidak terdefinisi. Angka korpus terkini selalu di
`../ANGKA-NASKAH.md`.
