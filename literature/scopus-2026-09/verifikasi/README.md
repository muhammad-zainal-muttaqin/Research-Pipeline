# Verifikasi Tinjauan `main6`

Tinjauan `main6` menyaring 6.491 artikel Scopus menjadi 1.013 artikel dengan
bantuan AI. Lima artikel lain berasal dari luar pencarian, sehingga totalnya 1.018.
Folder ini berisi lembar pemeriksaannya, mengikuti rencana Bu Fatma
(29 September 2026, salinan di [`rencana/index.html`](rencana/index.html)).

## Posisi per 19 Oktober 2026

Semua pemeriksaan selesai, kecuali dua butir yang hanya dapat dikerjakan manusia
([TUGAS.md](TUGAS.md)). Pada 19 Oktober 2026 peninjau menyatakan telah memeriksa
dan menyetujui seluruh perubahan buatan AI di
[`log_perubahan.csv`](log_perubahan.csv).

| Pemeriksaan | Yang diperiksa | Hasil |
|---|---|---|
| 1. Sampel acak | Keputusan peninjau dan AI pada 300 judul dan 165 abstrak acak | Kappa 0,57 (judul) dan 0,45 (abstrak). 123 perbedaan sudah diputuskan: 5 oleh Bu Fatma, 118 oleh AI dan disetujui peninjau |
| 2. Keputusan penting | Semua artikel C1, C3, dan yang dikeluarkan di tahap kelayakan | 203 baris C1, 177 baris C3, dan 145 eksklusi diperiksa |
| 3. Makalah yang sudah dikenal | Apakah 16 makalah penting tertangkap pencarian | Semuanya tertangkap; 5 kajian dari luar pencarian ditambahkan |
| 4. PDF lengkap | Ketersediaan PDF 199 artikel C1 dan 19 artikel sawit inti | 217 dari 218 ada; satu artikel C1 tanpa PDF (Safre dkk. 2024) dilaporkan di naskah |
| 5. Label ulang dari PDF | Label 199 artikel C1 | 196 dibaca dari teks lengkap, 3 dari abstrak; 98 label berubah |
| 6. Cek fakta naskah | Kecocokan setiap klaim naskah dengan kajian yang dikutip | 303 pasangan klaim dan kajian sesuai sumber |

Label C1 belum dikode buta oleh manusia, sehingga kesepakatan yang dilaporkan
untuk label C1 adalah antarmodel (butir F.4 di [TUGAS.md](TUGAS.md)).

## Langkah berikutnya

Buka [TUGAS.md](TUGAS.md).

## Isi folder

| Folder atau berkas | Isi |
|---|---|
| [`log_perubahan.csv`](log_perubahan.csv) | Setiap perubahan keputusan dan label, dengan alasan dan pengubahnya |
| [`cek-1-sampel-buta/`](cek-1-sampel-buta/) | Sampel acak, laporan kesepakatan, dan keputusan atas setiap perbedaan |
| [`cek-2-cek-tangan/`](cek-2-cek-tangan/) | Lembar periksa artikel C1, C3, dan yang dikeluarkan |
| [`cek-3-makalah-dikenal/`](cek-3-makalah-dikenal/) | Laporan 16 makalah dikenal dan penelusuran daftar pustaka |
| [`cek-4-teks-lengkap/`](cek-4-teks-lengkap/) | Status PDF dan daftar PDF yang diminta ke Bu Fatma |
| [`cek-5-kode-ulang/`](cek-5-kode-ulang/) | Label artikel C1 dari teks lengkap dan sampel untuk Bu Fatma |
| [`cek-6-cek-fakta/`](cek-6-cek-fakta/) | Lembar cek fakta, satu baris per pasangan klaim dan kajian |

`.teknis/` berisi data mentah yang dibaca skrip; peninjau tidak perlu
membukanya. Aturan kerja agen ada di `AGENTS.md` §11.
