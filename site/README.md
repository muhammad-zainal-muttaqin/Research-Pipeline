# Site

Pembuat situs statis "Ruang Baca Riset" - aplikasi web satu halaman yang
memuat 970 entri dari dua korpus tinjauan pustaka (182 entri lama dan 788 entri
`main6`) agar dapat dibaca langsung di browser.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Membangun ulang situs | Jalankan `node site/build.js` dari akar repo |
| Melihat laporan tanpa menulis | Jalankan `node site/build.js --dry` |
| Membaca hasil build | Buka [`../index.html`](../index.html) di browser |

## Isi folder

| Berkas | Isi |
|---|---|
| `build.js` | Perakit situs (105 KB). Memindai `literature/entries/*.md`, `literature/scopus-2026-09/entri/*.md`, dan tiga dokumen spesial (`literature/synthesis.md`, `experiments/LAPORAN-EKSPERIMEN.md`, `literature/scopus-2026-09/KATALOG-PDF.md`), lalu menghasilkan `index.html` di akar repo. Tanpa dependensi luar - hanya `fs` dan `path` bawaan Node.js |
| `vendor/marked.min.js` | Parser Markdown (marked v12) yang di-vendor agar tidak perlu `npm install` |

## Catatan

- `index.html` di akar repo adalah **hasil build** (12 MB) - jangan disunting
  langsung. Jalankan `build.js` setelah mengubah entri korpus lama, entri
  `main6`, sintesis, katalog PDF `main6`, atau laporan eksperimen.
- Teks lengkap `literature/scopus-2026-09/teks/*.txt` diambil saat entri
  `main6` dibuka; hasil ekstraksi di `literature/scopus-2026-09/ekstraksi/`
  tidak dibaca `build.js`.
