# Ekstraksi Teks Lengkap `main6`

Folder ini menyimpan hasil membaca teks lengkap kajian korpus `main6`
(`../teks/<kunci>.txt`) oleh agen model bahasa. Hasilnya disimpan agar tidak
perlu dibaca ulang setiap sesi. Setiap subfolder memuat `prompt.txt`, yaitu
instruksi yang diberikan kepada agen kata demi kata, dan satu berkas hasil per
kajian.

**Hasil di sini adalah bahan kerja, bukan sumber naskah.** Setiap angka atau
klaim yang masuk naskah diperiksa ulang di `../teks/<kunci>.txt` pada nomor
baris yang disebut berkas hasil. Agen kadang salah membaca tabel yang
teksnya terburai; kesalahan yang sudah ditemukan ditulis di bagian `NOTES`
berkas hasil.

## Isi

| Subfolder | Pertanyaan yang dijawab | Kajian | Dipakai untuk |
|---|---|---|---|
| `perbandingan/` | Apakah kajian membandingkan dua cara menautkan atau menghitung pengamatan pada data uji yang sama, dan apa hasilnya? | Kajian metode multi-pengamatan (C1 tanpa makalah set data) | Tabel perbandingan pada data yang sama di Seksi 5 naskah (`tab:assoc`) |
| `tanaman-platform/` | Tanaman apa dan wahana kamera apa yang dipakai dalam eksperimen kajian itu sendiri? | Semua kajian C1 | Kolom tanaman dan platform Lampiran A dan gambar S4, menggantikan aturan kata kunci abstrak |
| `bacaan/` | Isi kajian inti: akuisisi, detektor, asosiasi, asumsi, sumber hitung ganda, penanganan kelas, rujukan hitung, hasil, kondisi gagal, kutipan | Kajian yang dibahas rinci di Seksi 4–8 | Penulisan ulang seksi bukti |

### `perbandingan/<kunci>.txt`

Satu berkas per kajian, dalam bahasa Inggris, dengan judul baku:

- `KEY`, `CROP AND DATA` (tanaman, data uji, jenis rujukan hitung);
- `SAME-DATA COMPARISON: yes` atau `no`;
- untuk setiap perbandingan `C1`, `C2`, ...: `TYPE`, `ARMS`, `RESULTS` (angka
  setiap lengan seperti tercetak), `WHERE` (tabel dan nomor baris),
  `QUOTE`, `AUTHORS' EXPLANATION`, `CONDITIONS`;
- `NOTES`: ketidakcocokan antara teks, tabel, dan abstrak.

Arti `TYPE`:

- `TRACKER`: pelacak berbeda, misalnya SORT, DeepSORT, ByteTrack.
- `COMPONENT`: jalur yang sama dengan dan tanpa satu komponen asosiasi,
  misalnya deskriptor tampilan, kompensasi gerak kamera, atau langkah 3D.
- `MECHANISM`: mekanisme asosiasi berbeda, misalnya penjumlahan, pelacakan,
  penggabungan 3D, atau faktor koreksi.
- `COUNTING-RULE`: aturan hitung berbeda, misalnya identitas unik, garis
  hitung, atau wilayah.
- `ACQUISITION`: desain akuisisi berbeda pada tanaman yang sama, misalnya
  satu sisi lawan dua sisi.

Sebuah perbandingan dicatat hanya bila ketiga syarat ini terpenuhi:

1. penulis sendiri menguji dua lengan atau lebih pada data uji yang sama;
2. lengan-lengannya berbeda dalam salah satu dari lima jenis di atas;
3. ada hasil kuantitatif untuk setiap lengan.

Perbandingan detektor saja dan angka yang dikutip dari makalah lain tidak
dicatat. Aturan ini sama dengan yang tertulis di subseksi *Appraisal and
synthesis* naskah.

### `tanaman-platform/hasil_<N>.tsv`

Satu baris per kajian, empat kolom yang dipisah TAB:

```
kunci   tanaman   platform   nomor baris pendukung
```

Nama tanaman dan platform memakai kosakata `TANAMAN` dan `PLATFORM` di
`tools/scopus/kode_bukti.py`. Nilai `not stated` berarti teks tidak menyebut
wahana kamera. Berkas `daftar_<N>.txt` berisi pembagian kunci per agen.

### `bacaan/<kunci>.txt`

Lembar bacaan dengan judul baku (lihat `bacaan/prompt.txt`). Lembar ini
dipakai untuk menulis ulang Seksi 4–8 pada November 2026.

## Posisi sekarang

18 November 2026:

- `perbandingan/`: korpus memuat 211 kajian metode C1. Empat di antaranya
  (`guo2023real`, `tu2026passion`, `wang2024camellia`,
  `zhu2022identification`) tidak punya teks karena fon PDF-nya tanpa
  pemetaan Unicode, dan perlu OCR. Dari 207 sisanya, 186 sudah punya berkas
  dan 111 memuat perbandingan pada data yang sama. Sisa 21 kajian sedang
  dikerjakan.
- `tanaman-platform/`: 81 dari 215 kajian C1 sudah tercatat.
- `bacaan/`: 49 kajian inti, selesai.

Angka ini dihitung ulang dengan perintah di bawah, bukan disalin.

## Cara memeriksa dan melanjutkan

Daftar kajian yang belum punya berkas `perbandingan/`:

```bash
python3 - <<'E'
import csv, os
d = "literature/scopus-2026-09"
for r in csv.DictReader(open(f"{d}/topik/bukti/matriks_bukti.csv")):
    if r["kode"] == "C1" and r["mekanisme"] != "DATA" \
            and not os.path.exists(f"{d}/ekstraksi/perbandingan/{r['key']}.txt"):
        print(r["key"])
E
```

Melanjutkan ekstraksi:

1. Beri agen `prompt.txt` subfolder itu beserta daftar kunci yang belum ada.
   Agen menulis satu berkas per kajian sebelum membaca kajian berikutnya dan
   melewati kunci yang berkasnya sudah ada.
2. Pakai Haiku, paling banyak empat agen sekaligus, masing-masing 8–14 kunci.
3. Batasi potongan baca 60–80 baris. Beberapa teks punya baris sangat panjang;
   dengan potongan 120–250 baris agen kehabisan konteks ("Autocompact is
   thrashing") dan berhenti.
4. Agen Haiku kadang berhenti dengan alasan "hanya teks". Lanjutkan dengan
   pesan bahwa pemanggilan alat diizinkan.
5. Berkas yang ditulis dari catatan, bukan dari teks, ditandai agen di
   `NOTES`. Periksa ulang sebelum dipakai.

## Langkah berikutnya

- Selesaikan 21 kajian `perbandingan/` yang tersisa, lalu perbarui
  `tab:assoc` dan teks Seksi 5 naskah.
- Selesaikan `tanaman-platform/`. Setiap baris yang berbeda dari kode kata
  kunci diperiksa di teks lengkap, lalu diisikan ke `topik/bukti/mekanisme_C1.txt`
  dan dicatat di `verifikasi/.teknis/log_perubahan.csv`.
