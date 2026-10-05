# Serah-Terima Verifikasi `main6` (diperbarui 5 Oktober 2026)

Dokumen ini memungkinkan agen atau penulis lain melanjutkan pekerjaan tanpa membaca percakapan sebelumnya.
Rencana asal: `rencana/index.html` (Bu Fatma, 29 September 2026). Semua keputusan di bawah dibuat model bahasa
besar (putaran kedua, "AI-2") dan **belum diperiksa manusia**. Isian manusia (`keputusan_manusia`, `final_*`,
`benar`, `oleh`) di lembar Cek 1-6 tidak pernah ditulis AI-2.

## 0. Status cek manusia per 5 Oktober 2026

| Cek | Status | Berkas |
|---|---|---|
| 1 Sampel buta | Dihitung 4 Oktober 2026: judul 256 dari 300 sepakat (kappa 0,57); abstrak 86 dari 165 (kappa 0,45); 5 judul kritis. Bu Fatma memutuskan kelima judul itu pada 5 Oktober 2026: empat dieksklusi dan idx 3661 (Qiu dkk., 2022) masuk korpus sebagai C5, sehingga Cek 1 lulus tanpa penarikan 300 judul tambahan. Sudah dikerjakan pada 5 Oktober 2026: kelima keputusan diisikan ke `ketidaksepakatan.csv` dan `sampel_judul.csv`; idx 3661 dimasukkan lewat `topik/penyaringan/abstrak_F00.txt` (berkas suntingan tangan yang tidak ditimpa skrip `verifikasi_ai2*.py`) dan dicatat di `log_perubahan.csv`; angka, gambar, makro, dan `references6.bib` dibangun ulang; dua aturan kode (stereo dan prioritas C1) ditambahkan ke `PROTOKOL.md` bagian 4, `PANDUAN.md` Cek 1, dan bagian metode naskah. Belum dikerjakan: kompilasi `main6.pdf` (`tectonic` tidak terpasang di laptop peninjau), kode eksklusi untuk idx 1338 (belum diberikan Bu Fatma), keputusan atas 118 ketidaksepakatan lain, dan pemeriksaan empat kajian C1 yang mungkin terkena aturan stereo (`zhang2021method`, `xie2023fruit`, `hu2026calibration`, `vulpi2022rgb`). | `cek-1-sampel-buta/kesepakatan.md`, `ketidaksepakatan.csv` |
| 2 Cek tangan | Belum dimulai. Lembar `cek_C1` (187) dan `cek_C3` (170) masih mengikuti korpus sebelum putaran kedua (kini C1 195, C3 176); bangkitkan ulang dengan `verifikasi_cek_tangan.py` sebelum diisi. | `cek-2-cek-tangan/` |
| 3 Makalah dikenal | Laporan model tersedia; keputusan penulis belum diambil. | `cek-3-makalah-dikenal/` |
| 4 Teks lengkap | 213 dari 214 kajian memiliki PDF (C1 194 dari 195); satu kajian belum, yaitu `safre2024advanced` (ISHS, dikode dari judul). Sebanyak 41 PDF diperoleh lewat pembelian pada 5 Oktober 2026. Teks PDF yang masuk pada 3-5 Oktober 2026 belum diekstrak ke `teks/`, sehingga angka teks lengkap naskah tetap 331. | `cek-4-teks-lengkap/` |
| 5 Kode ulang | Belum dimulai. Lembar `kode_ulang_C1` (187) perlu dibangkitkan ulang. | `cek-5-kode-ulang/` |
| 6 Cek fakta | Belum dimulai oleh peninjau. | `cek-6-cek-fakta/` |

## 1. Sudah selesai

| Pekerjaan | Hasil | Berkas |
|---|---|---|
| Putaran kedua buta atas 510 rekaman kunci (C1, C3, eksklusi), sampel buta Cek 1, cek fakta Cek 6 | 115 paket | `hasil-kerja-ai/hasil/`, `hasil-kerja-ai/RINGKASAN-BANDING.md` |
| Ajudikasi 227 rekaman yang berbeda + uji sanggah tiap perubahan kelompok | 16 kelompok berubah, 7 disanggah, 10 diserahkan ke manusia | `hasil-kerja-ai/PERUBAHAN-AI2.md`, `hasil-kerja-ai/keputusan_final.csv` |
| Penerapan ke data sumber (idempoten) | `penyaringan/abstrak_*.txt`, `mekanisme_C1.txt`, `kode_C3.txt`, `log_perubahan.csv` (oleh = AI-2) | `tools/scopus/verifikasi_ai2_terapkan.py` |
| Cek 3: Häni 2020 C2 -> C1; Liu dan Ampatzidis 2026 sebagai rekaman metode lain | kotak "other methods" di F01, `liu2026shaping` di `references6.bib` | `topik/tambahan_metode_lain.csv` |
| Naskah `main6` ditulis ulang: bagian metode (kedua putaran), tabel kelompok, tabel RQ, nama mekanisme (tanpa M0-M5), perbaikan cek fakta, abstrak, Declaration of AI | 33 halaman, semua angka korpus berupa makro | `manuscript/source/main6-body.tex`, `main6-angka.tex` |
| Alat | `tools/scopus/angka_naskah.py` (angka dan makro), `verifikasi_ai2*.py`, `verifikasi_ai2_judul.py` | |

Perintah bangun ulang, berurutan, setiap kali data berubah:

```bash
python tools/scopus/kode_bukti.py
python tools/scopus/gambar_tinjauan.py
python tools/scopus/tabel_lampiran.py
python tools/scopus/lampiran_kueri.py
python tools/scopus/angka_naskah.py --simpan      # ANGKA-NASKAH.md dan main6-angka.tex
python tools/scopus/buat_bib.py --rekaman literature/scopus-2026-09/topik/records_all.csv literature/scopus-2026-09/metodologi/records_MA*.csv literature/scopus-2026-09/topik/tambahan_metode_lain.csv --kunci literature/scopus-2026-09/topik/bukti/matriks_bukti.csv literature/scopus-2026-09/metodologi/terpilih.csv literature/scopus-2026-09/topik/tambahan_metode_lain.csv --cache literature/scopus-2026-09/crossref.jsonl --keluar manuscript/source/references6.bib
cd manuscript/source && tectonic main6.tex && mv main6.pdf ../output/papers/
```

Jangan menyunting tangan: `main6-angka.tex`, `main6-appendix-*.tex`, `references6.bib`, `figures/main6/F*`, `ANGKA-NASKAH.md`.

## 2. Sisa pekerjaan, berurutan menurut prioritas

1. **Pemeriksaan ulang eksklusi tahap judul Q1 dan Q3: SELESAI dan diterapkan** (1.325 rekaman, 19 dimasukkan kembali setelah uji sanggah:
   C1 6, C2 4, C3 6, C5 1, T 2; 12 usul disanggah). Laporan: `hasil-kerja-ai/ULANG-JUDUL.md`. **Urutan penerapan harus tetap:**
   `verifikasi_ai2_terapkan.py` lebih dulu, lalu `verifikasi_ai2_judul.py terapkan` (yang pertama membangun ulang berkas kode dari salinan
   putaran 1 sehingga yang kedua harus menyusul; keduanya idempoten).
   **Yang masih perlu dikerjakan:** eksklusi tahap judul dari kueri lain (Q2, Q4-Q9; sekitar 3.300 rekaman) belum diperiksa ulang;
   gunakan skrip yang sama dengan mengubah `KUERI_INTI` bila ingin diperluas. Angka naskah terkini (5 Oktober 2026): korpus Scopus 1.001
   (C1 195, C2 238, C3 176, C4 49, C5 135, R 120, T 88) + 1 metode lain; sebagian teks naskah yang menyebut angka tetap
   (bukan makro) sudah dicocokkan dengan data pada 2 Oktober 2026 (14 perbandingan, 5 dari 11 tinjauan, 8 studi akuisisi: benar).
2. **Penulisan ulang gaya** mengikuti `manuscript/guides/CATATAN-GAYA-TULIS-CONTOH.md`: sudah diterapkan pada seluruh
   bagian; yang belum: pembagian paragraf panjang lain, tabel perbandingan memisahkan kolom hasil, ringkasan oil-palm per
   subseksi. Aturan: jangan memperpanjang kalimat; satu kajian per kalimat; kutip dengan `\citet`.
3. **Cek fakta**: 31 klaim N atau SEBAGIAN sudah diperbaiki di naskah dari verifikasi kedua (`hasil-kerja-ai/hasil/vf_*.json`). 11 klaim
   TAK-TERPERIKSA dan klaim berstatus Y oleh satu pemeriksa saja perlu mata manusia. Lembar manusia: `cek-6-cek-fakta/cek_fakta.csv`.
4. **Cek manusia (tidak dapat dikerjakan agen)**: Cek 1 (`cek-1-sampel-buta/`: `sampel_judul.csv`, `sampel_abstrak.csv`; kappa di
   `kesepakatan.md`), Cek 2 (`cek-2-cek-tangan/`), Cek 4 (PDF, `cek-4-teks-lengkap/PERMINTAAN-PDF.md`), Cek 5
   (`cek-5-kode-ulang/sampel_fatma_C1.csv`). Kerjakan 10 rekaman `perlu manusia` dan 7 `sengketa` lebih dulu: `hasil-kerja-ai/PERUBAHAN-AI2.md` bagian B dan C.
5. **Keputusan penulis**: isi CRediT, Funding, Declaration of competing interest, Acknowledgment (tidak boleh dikarang);
   tahun sitasi `liu2026shaping` (2026 atau 2027); batas kata abstrak jurnal; kebijakan AI jurnal;
   ejaan Oxford -ize dipertahankan.
6. (SELESAI 2 Oktober 2026) `AGENTS.md` bagian 3, `PROTOKOL.md`, dan `CATATAN-FORMAT-CONTOH.md` sudah diperbarui dengan angka baru (lihat `ANGKA-NASKAH.md`): korpus Scopus
   1.000 (bukan 971), C1 195, C2 238, C3 176, C4 49, C5 134, R 120, T 88, ditambah 1 rekaman metode lain; `references6.bib`
   1.061 rekord.

## 3. Aturan agar tidak merusak data

- Putaran pertama dibaca dari salinan `hasil-kerja-ai/putaran_1/`; jangan dihapus. `terapkan` dapat dijalankan ulang kapan saja.
- Perubahan kelompok hanya diterapkan bila penyanggah menyatakan `bertahan`. Rekaman `perlu manusia` tetap memakai nilai putaran pertama.
- Naskah tidak memuat jalur folder atau kode internal; angka korpus hanya lewat makro `\nXxx`/`\pXxx`.
- Penyaringan adalah satu peninjau dengan model; jangan menulis "dua peninjau independen".
- Model untuk *workflow*: Sonnet 5.5, `effort: 'high'` (permintaan pengguna 2 Oktober 2026).
