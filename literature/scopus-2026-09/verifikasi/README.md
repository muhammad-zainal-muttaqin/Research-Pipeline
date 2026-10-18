# Verifikasi Tinjauan `main6`

Tinjauan `main6` menyaring 6.491 artikel Scopus menjadi 1.000 artikel dengan
bantuan AI. Keputusan AI itu wajib diperiksa manusia sebelum naskah dikirim.
Folder ini berisi semua lembar pemeriksaannya, mengikuti rencana Bu Fatma
(29 September 2026, salinan di [`rencana/index.html`](rencana/index.html)).

## Posisi per 18 Oktober 2026

AI sudah mengisi usulan di hampir semua lembar. Usulan itu belum sah sebelum
Anda periksa.

| Pemeriksaan | Yang diperiksa | Keadaan | Tenggat |
|---|---|---|---|
| 1. Sampel acak | Kecocokan keputusan peninjau dan AI pada 300 judul dan 165 abstrak acak | Selesai. Lulus pada 5 Oktober; 118 perbedaan diputuskan pada 18 Oktober (8 keputusan berubah) | 6 Okt |
| 2. Periksa keputusan penting | Semua artikel C1 (195) dan C3 (176), serta artikel yang dikeluarkan | AI sudah mengisi lembar; aturan, koreksi label, dan 18 artikel yang layak masuk menunggu Anda | 20 Okt |
| 3. Makalah yang sudah dikenal | Apakah 16 makalah penting ikut tertangkap pencarian | Semuanya tertangkap; 4 kandidat tambahan perlu diputuskan | 20 Okt |
| 4. PDF lengkap | Ketersediaan PDF untuk 195 artikel C1 dan 19 artikel sawit yang menghitung atau memakai beberapa pandang | 213 dari 214 ada (yang tidak diperoleh dilaporkan di naskah); 1 PDF salah isi | 23 Okt |
| 5. Label ulang dari PDF | Label 195 artikel C1 dibaca ulang dari PDF | 147 cocok; 38 usul perubahan, 7 belum dilabel | 6 Nov |
| 6. Cek fakta naskah | Kecocokan setiap kalimat naskah dengan sumbernya | 69 dari 293 kalimat terisi; 9 kalimat salah perlu diganti | 13 Nov |

## Langkah berikutnya

Buka **[TUGAS.md](TUGAS.md)**. Isinya daftar keputusan, diurutkan dari yang
paling penting. Arti kode seperti C1 atau E5 ada di [ISTILAH.md](ISTILAH.md).

## Isi folder

| Folder | Isi | Petunjuk rinci |
|---|---|---|
| [`cek-1-sampel-buta/`](cek-1-sampel-buta/) | Sampel acak dan perbedaan keputusan | [PANDUAN.md](cek-1-sampel-buta/PANDUAN.md), hasil di [kesepakatan.md](cek-1-sampel-buta/kesepakatan.md), keputusan akhir di [ajudikasi_cek1.csv](cek-1-sampel-buta/ajudikasi/ajudikasi_cek1.csv) |
| [`cek-2-cek-tangan/`](cek-2-cek-tangan/) | Lembar C1, C3, dan eksklusi (`.xlsx` untuk diisi) | [CEK-TANGAN.md](cek-2-cek-tangan/CEK-TANGAN.md) |
| [`cek-3-makalah-dikenal/`](cek-3-makalah-dikenal/) | Laporan 16 makalah dikenal | [cek_makalah_dikenal.md](cek-3-makalah-dikenal/cek_makalah_dikenal.md) |
| [`cek-4-teks-lengkap/`](cek-4-teks-lengkap/) | Status PDF dan daftar permintaan PDF | [PERMINTAAN-PDF.md](cek-4-teks-lengkap/PERMINTAAN-PDF.md) |
| [`cek-5-kode-ulang/`](cek-5-kode-ulang/) | Lembar label ulang C1 dan sampel untuk Bu Fatma | [KODE-ULANG.md](cek-5-kode-ulang/KODE-ULANG.md) |
| [`cek-6-cek-fakta/`](cek-6-cek-fakta/) | Lembar cek fakta, satu baris per klaim | [CEK-FAKTA.md](cek-6-cek-fakta/CEK-FAKTA.md) |
| [`hasil-kerja-ai/menunggu-acc/`](hasil-kerja-ai/menunggu-acc/) | Draf AI yang menjadi bahan butir di `TUGAS.md`. Dibuka hanya bila butir merujuknya | — |

Boleh diabaikan: `hasil-kerja-ai/putaran-kedua/` (penyaringan ulang AI yang
sudah diterapkan), `arsip/` (cadangan lama), dan `cek-1-sampel-buta/.kunci/`
(kunci jawaban sampel buta). `log_perubahan.csv` mencatat setiap nilai yang
diubah dan diisi oleh skrip.

## Untuk agen

Catatan teknis, perintah bangun ulang, dan aturan agar data tidak rusak ada di
[SERAH-TERIMA.md](SERAH-TERIMA.md). Aturan kerja model ada di `AGENTS.md` §11.
