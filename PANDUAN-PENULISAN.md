# PANDUAN PENULISAN BAB — Tinjauan Pustaka YOLO / RGB / RGB-D

Dokumen ini adalah **satu-satunya acuan gaya** untuk menulis ulang setiap berkas di
`entri/`. Setiap penulis (termasuk subagent) wajib membaca dokumen ini sampai selesai
sebelum menulis. Tujuan penulisan ulang: mengubah lembar telaah yang telegrafik
menjadi **bab bergaya buku teks** — runtut, lengkap, dan dapat dipahami pembaca yang
belum mengenal topiknya.

---

## 1. Peran dan Alur Kerja

Satu penulis menangani **satu berkas entri** (satu makalah). Urutan kerja wajib:

1. Baca `PANDUAN-PENULISAN.md` ini sampai selesai.
2. Baca berkas entri lama yang ditugaskan. Ambil darinya: kunci BibTeX, identitas
   makalah (judul, penulis, tahun, venue), tema klaster, dan tautan akses. **Isi
   pembahasannya jangan dipertahankan** — tulis ulang sepenuhnya.
3. Riset sumber primer:
   - Buka tautan arXiv/DOI pada berkas lama (FetchURL); baca abstrak dan, bila
     tersedia, halaman HTML makalah.
   - Bila klaim/angka penting belum jelas, cari dengan WebSearch (situs resmi,
     repositori kode, halaman proyek, dokumentasi model).
   - Catat hanya fakta yang terverifikasi dari sumber; jangan mengarang angka.
4. Distil: tentukan masalah, gagasan inti, mekanisme kerja, hasil utama, dan
   keterbatasan makalah.
5. Tulis ulang berkas (overwrite penuh) mengikuti struktur dan kaidah di bawah.
6. Laporkan ke pemanggil: jumlah kata, bagian yang tidak dapat diverifikasi dari
   sumber, dan penyimpangan dari panduan (bila ada).

---

## 2. Kontrak Teknis (WAJIB — pelanggaran merusak build web)

- **Nama berkas tidak berubah.** Format: `NNN - YYYY - Judul singkat - Tema.md`.
- **Baris pertama berkas tidak berubah**, misalnya
  `# 003 - YOLOv3: An Incremental Improvement`.
- Tabel metadata **wajib memuat baris** `| Kunci BibTeX | \`kunci\` |` — baris ini
  diparse oleh `build.js`.
- Heading hanya memakai `##` dan `###` (dipakai untuk TOC web). Jangan memakai `#`
  selain baris judul pertama.
- **Gambar/foto dilarang** (repo tidak memuat berkas gambar; aplikasi web tidak merendernya).
- **Diagram ASCII dianjurkan** untuk menjelaskan arsitektur atau mekanisme yang sulit dipahami dari teks saja — maksimal 1–2 diagram per bab, ditulis dalam fenced code block (tiga backtick tanpa tag bahasa) agar dirender sebagai blok monospace. Kaidah diagram: lebar maksimal ±78 kolom; karakter ASCII dan gambar kotak sederhana (─ │ ┌ ┐ └ ┘ ├ ┤ ▼ ▲ ●); isi harus faktual (alur data, ukuran tensor, perbandingan pipeline), bukan dekorasi; setiap diagram diawali satu kalimat pengantar dan dijelaskan isinya pada teks sesudahnya.
- Tabel GFM diperbolehkan bila benar-benar diperlukan (maksimal satu per bab).
- Tautan antar-entri memakai tautan relatif Markdown dengan spasi di-encode `%20`,
  mengikuti pola yang sudah ada di berkas lama, misalnya
  `./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md`.
- **Jangan menyentuh berkas lain** selain berkas yang ditugaskan.

---

## 3. Struktur Bab (wajib, urut)

Sepuluh bagian `##` berikut, dengan judul persis seperti tertulis:

1. `## Metadata Ringkas` — tabel dua kolom: Kunci BibTeX, Judul asli, Penulis,
   Tahun, Venue, Tema.
2. `## Tautan Akses` — bullet tautan (arXiv/DOI/Scholar) dari berkas lama.
3. `## Gambaran Umum` — 1–2 paragraf: apa makalah ini, masalah apa yang dipecahkan,
   apa hasil utamanya. Ditulis sehingga pembaca yang hanya membaca bagian ini tetap
   mendapat inti bab.
4. `## Latar Belakang: Masalah yang Ingin Dipecahkan` — kondisi bidang sebelum
   makalah ini ada; kekurangan pendekatan sebelumnya yang spesifik; mengapa masalah
   itu penting. Rujuk bab terdahulu bila relevan.
5. `## Ide Utama` — gagasan inti makalah dalam bentuk paling sederhana yang benar
   secara teknis. Jelaskan intuisi mekanis (apa masuk, apa keluar, apa yang berubah),
   bukan metafora.
6. `## Cara Kerja Langkah demi Langkah` — bagian terpanjang (±40–50% isi bab).
   Uraikan mekanisme secara berurutan; gunakan `###` per komponen/tahap. Setiap
   istilah teknis dijelaskan saat pertama muncul. Gunakan contoh numerik konkret.
   Bila arsitekturnya sukar dipahami dari teks (mis. aliran data antar-komponen,
   perbandingan dengan pipeline pendahulu), sertakan satu diagram ASCII.
7. `## Eksperimen dan Hasil` — apa yang diuji, pada data apa, dibandingkan dengan
   apa; angka hasil utama beserta interpretasinya.
8. `## Kelebihan dan Keterbatasan` — prosa seimbang; keterbatasan yang merupakan
   analisis penulis bab (bukan pernyataan penulis makalah) ditandai dengan frasa
   seperti "dari sisi rekayasa, ..." atau "secara konseptual, ...".
9. `## Kaitan dengan Bab Lain` — narasi kesinambungan: bab ini mewarisi apa dari
   bab mana, dan memengaruhi bab mana; sertakan tautan relatif. Minimal merujuk
   satu bab sebelumnya dalam silsilahnya bila ada.
10. `## Poin untuk Sitasi` — kunci BibTeX; ringkasan 2–3 kalimat yang aman dikutip
    dalam tinjauan pustaka; catatan angka/klaim yang perlu diverifikasi ke naskah
    asli sebelum sitasi formal (wajib untuk makalah sangat baru).

---

## 4. Kaidah Bahasa (syarat utama)

- **Bahasa Indonesia baku dan kaku sesuai PUEBI.** Perhatikan: penulisan imbuhan
  (`di-` awalan pasif vs `di` kata depan), kata baku (sistem, metode, praktik,
  hingga→sampai), dan tanda baca. Angka desimal memakai koma (`63,4%`).
- **Istilah asing dicetak miring** pada kemunculan pertama dan selanjutnya boleh
  tetap miring: *bounding box*, *confidence*, *backbone*. Istilah yang sudah
  diserap ditulis sesuai kaidah serapan (mis. *citra*, *piksel*, *filter* →
  *tapis* bila konteksnya pemrosesan citra; boleh tetap *filter* bila merujuk
  nama teknis baku).
- **Dilarang metafora, perumpamaan, dan kalimat mewah.** Tidak ada "ibarat",
  "bagaikan", "bak", "laksana". Kejelasan dicapai melalui struktur penjelasan:
  definisi → mekanisme → contoh numerik → interpretasi.
- **Dilarang frasa pengisi dan hiperbola ("AI slop")**, antara lain: "di era
  modern ini", "perkembangan pesat", "revolusioner", "terobosan", "menariknya",
  "perlu dicatat bahwa", "penting untuk dipahami", "dunia deteksi objek",
  "seperti yang kita ketahui", pujian kosong pada makalah. Setiap kalimat wajib
  memuat informasi.
- Nada buku teks: impersonal, langsung, tepat. Tidak memakai "kita"/"Anda"
  kecuali sangat terpaksa; gunakan konstruksi pasif atau nominal ("model ini
  memprediksi...", bukan "kita akan melihat model memprediksi...").
- Kalimat efektif: satu gagasan per kalimat; hindari kalimat majemuk lebih dari
  dua anak kalimat.

## 5. Kaidah Isi

- Panjang **1200–1800 kata** (tidak termasuk tabel metadata dan tautan).
- Alur naratif runtut: masalah → gagasan → cara kerja → bukti → penilaian.
  Bullet hanya untuk enumerasi murni (daftar komponen, daftar hasil); penjelasan
  konsep wajib berbentuk paragraf.
- **Setiap istilah teknis dijelaskan saat pertama muncul**, dalam 1–2 kalimat
  definisi langsung. Tidak boleh ada jargon yang dipakai tanpa penjelasan —
  termasuk nama metode lain yang dirujuk (mis. bila menyebut FPN, jelaskan satu
  kalimat apa itu FPN).
- **Contoh numerik konkret** untuk memperjelas mekanisme, misalnya: "pada citra
  448×448 dan grid 7×7, setiap sel mencakup wilayah 64×64 piksel".
- **Setiap angka hasil diberi interpretasi**, misalnya: "63,4% mAP berada di bawah
  Fast R-CNN (70,0%), tetapi kecepatannya 45 FPS dibandingkan ±0,5 FPS".
- **Tidak ada pengulangan**: satu fakta dibahas sekali di satu bagian; bagian lain
  cukup merujuknya secara singkat.
- Bab harus **mandiri** (semua istilah dijelaskan di tempat) **tetapi terhubung**
  (bagian 4 dan 9 merujuk bab lain secara naratif dengan tautan).
- Kejujuran akademik: klaim yang tidak berhasil diverifikasi dari sumber primer
  diberi tanda di bagian *Poin untuk Sitasi*; narasi utama hanya memuat hal yang
  diyakini benar. Jangan mengarang angka, nama dataset, atau hasil.

## 6. Checklist Sebelum Melapor

- [ ] Baris pertama dan nama berkas tidak berubah; baris `| Kunci BibTeX |` ada.
- [ ] Sepuluh bagian `##` lengkap dan urut; heading hanya `##`/`###`.
- [ ] 1200–1800 kata.
- [ ] Tidak ada boilerplate administratif lama (checklist verifikasi, glosarium
      generik, catatan integritas, daftar isi panjang).
- [ ] Semua istilah teknis terjelaskan saat pertama muncul; tidak ada jargon telanjang.
- [ ] Tidak ada metafora/perumpamaan; tidak ada frasa pengisi; ejaan PUEBI.
- [ ] Setiap angka hasil memiliki interpretasi; tidak ada fakta diulang antar-bagian.
- [ ] Bagian *Kaitan dengan Bab Lain* berisi narasi + tautan relatif yang benar.
- [ ] Bagian arsitektur/mekanisme yang kompleks dibantu diagram ASCII yang faktual.
- [ ] Tanpa gambar/foto; diagram ASCII dalam fenced code block, lebar ≤78 kolom.
- [ ] Laporan akhir menyebut jumlah kata dan klaim yang belum terverifikasi.

---

## 7. Contoh Bab Jadi

Contoh bab yang sudah memenuhi seluruh kaidah: `entri/001 - 2016 - You Only Look
Once (YOLOv1) - Fondasi RGB.md`. Baca berkas tersebut sebagai acuan bentuk akhir —
perhatikan panjang bagian, cara istilah diperkenalkan, dan cara angka diinterpretasi.
Tirukan polanya pada bab yang ditugaskan, dengan isi yang sepenuhnya dari makalah
tugas Anda.
