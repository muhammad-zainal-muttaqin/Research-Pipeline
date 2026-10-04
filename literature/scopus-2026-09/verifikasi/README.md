# Verifikasi Korpus `main6` — Peta Folder

Folder ini memuat semua bahan untuk memeriksa penyaringan dan pengodean korpus
`main6`, mengikuti rencana verifikasi Bu Fatma (29 September 2026; salinannya di
[`rencana/index.html`](rencana/index.html)). Status dan sisa pekerjaan:
[`SERAH-TERIMA.md`](SERAH-TERIMA.md).

Hampir semua berkas di sini **disiapkan skrip atau model**, bukan diisi manusia.
Kolom penilaian manusia sengaja dikosongkan dan hanya boleh diisi peninjau.

## Satu folder untuk satu cek

| Folder | Isi | Diisi oleh | Tenggat |
|---|---|---|---|
| [`cek-1-sampel-buta/`](cek-1-sampel-buta/PANDUAN.md) | Sampel acak 300 judul dan 165 rekaman tahap abstrak dengan keputusan peninjau dan keputusan AI; hasil di `kesepakatan.md` dan `ketidaksepakatan.csv` | Peninjau | 6 Oktober 2026 |
| [`cek-2-cek-tangan/`](cek-2-cek-tangan/CEK-TANGAN.md) | Lembar periksa tangan semua C1, C3, dan eksklusi tahap kelayakan | Peninjau | 20 Oktober 2026 |
| [`cek-3-makalah-dikenal/`](cek-3-makalah-dikenal/cek_makalah_dikenal.md) | Laporan 16 makalah yang sudah dikenal dan kandidat tambahan | Laporan model; keputusan penulis | 20 Oktober 2026 |
| [`cek-4-teks-lengkap/`](cek-4-teks-lengkap/PERMINTAAN-PDF.md) | Status PDF tiap kajian dan daftar permintaan PDF | Peninjau (status permintaan) | 6 dan 23 Oktober 2026 |
| [`cek-5-kode-ulang/`](cek-5-kode-ulang/KODE-ULANG.md) | Lembar kode ulang C1 dari teks lengkap; sampel 20 kajian untuk Bu Fatma | Peninjau; Bu Fatma | 6 November 2026 |
| [`cek-6-cek-fakta/`](cek-6-cek-fakta/CEK-FAKTA.md) | Satu baris per klaim naskah untuk dicek ke sumbernya | Peninjau | 13 November 2026 |

## Di luar keenam cek

| Lokasi | Isi |
|---|---|
| `hasil-kerja-ai/` | Seluruh keluaran putaran kedua penyaringan oleh model (paket kerja, hasil, banding, ajudikasi, laporan perubahan) dan salinan keputusan putaran pertama di `putaran_1/`. **Bukan penilaian manusia.** |
| `log_perubahan.csv` | Log lintas cek: satu baris untuk setiap nilai yang diubah pada berkas keputusan sumber (`tanggal, berkas, idx_atau_key, kolom, nilai_lama, nilai_baru, alasan, oleh`) |
| `rencana/` | Salinan rencana verifikasi Bu Fatma |
| `SERAH-TERIMA.md` | Apa yang sudah selesai, apa yang tersisa, dan aturan agar data tidak rusak |

## Skrip

Semua skrip ada di `tools/scopus/` dan menulis langsung ke folder cek yang sesuai.

| Cek | Skrip |
|---|---|
| 1 | `verifikasi_sampel.py` (tarik sampel), `verifikasi_kappa.py` (kesepakatan dan kappa) |
| 2 | `verifikasi_cek_tangan.py` |
| 4 | `verifikasi_teks_lengkap.py` |
| 5 | `verifikasi_kode_ulang.py` |
| 6 | `verifikasi_cek_fakta.py` |
| Hasil kerja AI | `verifikasi_ai2.py`, `verifikasi_ai2_gabung.py`, `verifikasi_ai2_terapkan.py`, `verifikasi_ai2_judul.py` |
