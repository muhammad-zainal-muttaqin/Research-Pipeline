# E-023 — fusi awal vs menengah vs akhir, semuanya dari nol

Matriks penuh 15 run (5 lengan x 3 seed, yolo26n skala n, 150 epoch, split
SawitMVC-Depth seed42, tanpa bobot pratlatih). **Ke-15 run lengkap 150/150**,
selesai 2026-08-01 pukul 15:34 UTC. `late_seed42` dan `mid_seed42` sempat
diulang setelah bug topeng 4-kanal; versi yang diarsipkan di sini adalah hasil
ulangan yang bersih.

## Kenapa arsip ini ada

`runs/` masuk `.gitignore` (baris 97), jadi `results.csv`, `args.yaml`, dan
`hasil.json` di sana hanya hidup di disk kerja yang bersifat sementara. Sembilan
run yang sudah selesai mewakili sekitar sepuluh jam GPU; menahannya sampai
seluruh matriks tuntas berarti mempertaruhkan semuanya pada satu disk tanpa
cadangan. Yang disalin ke sini hanya berkas teks — total ~234 KB.

## Isi tiap folder run

| Berkas | Keterangan |
|---|---|
| `results.csv` | metrik per epoch dari trainer |
| `args.yaml` | hiperparameter efektif, apa adanya dari ultralytics |
| `hasil.json` | ringkasan akhir trainer — **lihat peringatan di bawah** |
| `best.pt.sha256` | hash bobot; bobotnya sendiri tidak diarsipkan (kebijakan repo) |

## Peringatan: `hasil.json` tidak boleh dipakai membandingkan antar lengan

Aturan E-025. Evaluator internal trainer menghasilkan selisih yang bergantung
pada jumlah deteksi yang dipancarkan model, dan pada E-022 hal itu membalik
TANDA selisih antar lengan (-0,00515 lewat evaluator internal vs +0,01041 lewat
pycocotools). Angka di `hasil.json` disalin ke sini hanya sebagai catatan
mentah pelatihan.

Perbandingan antar lengan E-023 akan dihitung ulang dengan pycocotools atas
seluruh 15 run sekaligus, dan itulah yang menjadi dasar entri E-032.

## Bobot tidak diarsipkan

Kebijakan repo tidak menyimpan `*.pt`. `best.pt.sha256` membuat hasil latih
ulang dapat dibandingkan: kalau hash berbeda, minimal diketahui bahwa
checkpoint-nya memang lain, bukan sekadar menduga hasilnya tidak tereproduksi.
Resep latihannya ada di `reproduce/experiments/shell/e023_fusi.sh` (seed 42 dan
1337) dan `e023_seed2024.sh` (seed 2024).

## Catatan penanda `.e023-tanda/`

Direktori penanda milik driver TIDAK sinkron dengan kenyataan dan tidak boleh
dipakai sebagai sumber kebenaran. `gagal-e023_derau_seed1337` adalah sisa
percobaan pertama yang kena OOM — penggantinya selesai 150/150 dengan bersih.
`mid_seed42` dan `late_seed42` tidak punya penanda karena diselesaikan lewat
jalur perbaikan terpisah. Jumlah epoch unik di `results.csv` adalah ukuran yang
dipakai, di sini maupun di skrip evaluasi.
