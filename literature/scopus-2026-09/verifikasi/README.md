# Verifikasi Tinjauan `main6`

Tinjauan `main6` menyaring 6.491 artikel Scopus menjadi 1.013 artikel dengan
bantuan AI. Lima artikel lain berasal dari luar pencarian, sehingga totalnya 1.018.
Folder ini berisi semua lembar pemeriksaannya, mengikuti rencana Bu Fatma
(29 September 2026, salinan di [`rencana/index.html`](rencana/index.html)).

## Posisi per 19 Oktober 2026

Peninjau menyerahkan keputusan butir verifikasi kepada model. Semua butir sudah
diputuskan dan diterapkan, kecuali dua yang hanya dapat dikerjakan manusia
([TUGAS.md](TUGAS.md)). Isian model di lembar ditandai di kolom `catatan` atau
`catatan_peninjau`.

| Pemeriksaan | Yang diperiksa | Keadaan |
|---|---|---|
| 1. Sampel acak | Kecocokan keputusan peninjau dan AI pada 300 judul dan 165 abstrak acak | Selesai. 118 perbedaan diputuskan pada 18 Oktober (8 keputusan berubah) |
| 2. Periksa keputusan penting | Semua artikel C1, C3, dan yang dikeluarkan | Selesai. Aturan baru ditetapkan; 87 rekaman dibaca ulang buta; 26 keputusan berubah |
| 3. Makalah yang sudah dikenal | Apakah 16 makalah penting ikut tertangkap pencarian | Selesai. Semuanya tertangkap; 4 kajian dari daftar pustaka ditambahkan |
| 4. PDF lengkap | Ketersediaan PDF artikel C1 dan sawit inti | Selesai. Dua artikel C1 tanpa teks lengkap, dilaporkan di naskah |
| 5. Label ulang dari PDF | Label 199 artikel C1 | Selesai. Semua dikode ulang buta; label akhir di `final_*` |
| 6. Cek fakta naskah | Kecocokan setiap kalimat naskah dengan sumbernya | Selesai. 214 kalimat (305 pasangan kalimat dan kajian); 65 pasangan yang tidak tepat sudah diperbaiki di naskah |

Yang belum dilakukan: kode buta oleh manusia (F.4). Kesepakatan yang dilaporkan
untuk label C1 adalah antarmodel, bukan antarmanusia.

## Langkah berikutnya

Buka **[TUGAS.md](TUGAS.md)**. Rincian keputusan model per butir ada di
[tugas-model/README.md](hasil-kerja-ai/putaran-kedua/tugas-model/README.md). Arti
kode seperti C1 atau E5 ada di [ISTILAH.md](ISTILAH.md).

## Isi folder

| Folder | Isi | Petunjuk rinci |
|---|---|---|
| [`cek-1-sampel-buta/`](cek-1-sampel-buta/) | Sampel acak dan perbedaan keputusan | [PANDUAN.md](cek-1-sampel-buta/PANDUAN.md), hasil di [kesepakatan.md](cek-1-sampel-buta/kesepakatan.md), keputusan akhir di [ajudikasi_cek1.csv](cek-1-sampel-buta/ajudikasi/ajudikasi_cek1.csv) |
| [`cek-2-cek-tangan/`](cek-2-cek-tangan/) | Lembar C1, C3, dan eksklusi | [CEK-TANGAN.md](cek-2-cek-tangan/CEK-TANGAN.md) |
| [`cek-3-makalah-dikenal/`](cek-3-makalah-dikenal/) | Laporan 16 makalah dikenal | [cek_makalah_dikenal.md](cek-3-makalah-dikenal/cek_makalah_dikenal.md) |
| [`cek-4-teks-lengkap/`](cek-4-teks-lengkap/) | Status PDF dan daftar permintaan PDF | [PERMINTAAN-PDF.md](cek-4-teks-lengkap/PERMINTAAN-PDF.md) |
| [`cek-5-kode-ulang/`](cek-5-kode-ulang/) | Lembar label ulang C1 dan sampel untuk Bu Fatma | [KODE-ULANG.md](cek-5-kode-ulang/KODE-ULANG.md) |
| [`cek-6-cek-fakta/`](cek-6-cek-fakta/) | Lembar cek fakta, satu baris per klaim | [CEK-FAKTA.md](cek-6-cek-fakta/CEK-FAKTA.md) |
| [`hasil-kerja-ai/`](hasil-kerja-ai/) | Keluaran model: `putaran-kedua/` sudah diterapkan; `menunggu-acc/` untuk draf baru | [tugas-model/README.md](hasil-kerja-ai/putaran-kedua/tugas-model/README.md) |

Boleh diabaikan: `hasil-kerja-ai/putaran-kedua/draf-cek/` (draf model 11–18
Oktober yang sudah diputuskan), `arsip/` (cadangan lama), dan
`cek-1-sampel-buta/.kunci/` (kunci jawaban sampel buta). `log_perubahan.csv`
mencatat setiap nilai yang diubah dan diisi oleh skrip.

## Untuk agen

Catatan teknis, perintah bangun ulang, dan aturan agar data tidak rusak ada di
[SERAH-TERIMA.md](SERAH-TERIMA.md). Aturan kerja model ada di `AGENTS.md` §11.
