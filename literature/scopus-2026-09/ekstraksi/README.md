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

Tanaman dan wahana kamera semua kajian C1 yang dulu diekstrak di folder ini
kini menjadi data sumber di `../topik/bukti/tanaman_platform_C1.txt`
(disetujui peninjau 20 November 2026) dan dibaca `kode_bukti.py`.

- `perbandingan/`: korpus memuat 232 kajian metode C1. Empat kajian yang dulu
  tanpa teks (`guo2023real`, `tu2026passion`, `wang2024camellia`,
  `zhu2022identification`) sudah diekstrak dengan OCR karena fon FzBookMaker.
  Teks Mandarin terbaca, sebagian tanda baca mungkin meleset. 210 kajian
  sudah punya berkas; 22 kajian C1 yang masuk pada 20 November 2026 belum.
- `bacaan/`: 48 kajian inti, selesai.

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

- Perbarui `tab:assoc` dan teks Seksi 5 naskah dari 127 kajian di `perbandingan/` yang
  memuat perbandingan pada data yang sama.
- Ekstrak `perbandingan/` untuk 22 kajian C1 yang belum punya berkas (perintah di atas).
