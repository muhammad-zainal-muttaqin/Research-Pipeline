# Site

Pembuat situs statis "Ruang Baca Riset" — aplikasi web satu halaman yang
memuat seluruh korpus tinjauan pustaka agar dapat dibaca langsung di browser.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Membangun ulang situs | Jalankan `node site/build.js` dari akar repo |
| Melihat laporan tanpa menulis | Jalankan `node site/build.js --dry` |
| Membaca hasil build | Buka [`../index.html`](../index.html) di browser |

## Isi folder

| Berkas | Isi |
|---|---|
| `build.js` | Perakit situs (100 KB). Memindai `literature/entries/*.md` dan `literature/synthesis.md`, lalu menghasilkan `index.html` di akar repo. Tanpa dependensi luar — hanya `fs` dan `path` bawaan Node.js |
| `vendor/marked.min.js` | Parser Markdown (marked v12) yang di-vendor agar tidak perlu `npm install` |

## Catatan

- `index.html` di akar repo adalah **hasil build** (9+ MB) — jangan disunting
  langsung. Jalankan `build.js` setelah mengubah entri literatur, sintesis,
  atau laporan eksperimen.
- `build.js` juga memuat `experiments/LAPORAN-EKSPERIMEN.md` sebagai halaman
  terpisah di dalam situs.
