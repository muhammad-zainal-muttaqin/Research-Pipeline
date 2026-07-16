# 024 - An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 024 dari 154 |
| Kunci BibTeX | `dosovitskiy2021vit` |
| Judul | An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale |
| Penulis | Dosovitskiy, Alexey; Beyer, Lucas; Kolesnikov, Alexander; Weissenborn, Dirk; Zhai, Xiaohua; Unterthiner, Thomas; Dehghani, Mostafa; Minderer, Matthias; Heigold, Georg; Gelly, Sylvain; others |
| Tahun | 2021 |
| Venue / Jurnal | International Conference on Learning Representations (ICLR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | ViT, Transformer, patch embedding, klasifikasi citra, pra-pelatihan |

> **Catatan integritas.** Ringkasan disusun dari pemahaman atas makalah ini; bagian *Abstrak* adalah **parafrase**, bukan kutipan verbatim. Angka/klaim spesifik dapat berbeda dari naskah asli — **verifikasi lewat tautan akses** sebelum dikutip dalam karya formal.

## Daftar Isi
1. [Metadata Ringkas](#metadata-ringkas)
2. [Tautan Akses](#tautan-akses-klik-untuk-viewunduh)
3. [Identitas Publikasi](#identitas-publikasi)
4. [Ringkasan Eksekutif](#ringkasan-eksekutif)
5. [Abstrak (Parafrase)](#abstrak-parafrase)
6. [Latar Belakang & Konteks](#latar-belakang--konteks)
7. [Permasalahan yang Diangkat](#permasalahan-yang-diangkat)
8. [Tujuan & Pertanyaan Penelitian](#tujuan--pertanyaan-penelitian)
9. [Tinjauan Terdahulu / Posisi Literatur](#tinjauan-terdahulu--posisi-literatur)
10. [Metodologi & Arsitektur](#metodologi--arsitektur)
11. [Kontribusi Utama](#kontribusi-utama)
12. [Rincian Eksperimen](#rincian-eksperimen)
13. [Temuan Kunci](#temuan-kunci)
14. [Keunggulan](#keunggulan)
15. [Keterbatasan](#keterbatasan)
16. [Relevansi terhadap Tema Tinjauan](#relevansi-terhadap-tema-tinjauan)
17. [Hubungan dengan Entri Lain](#hubungan-dengan-entri-lain)
18. [Glosarium Istilah](#glosarium-istilah-tema-fondasi-rgb)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=An%20Image%20Is%20Worth%2016x16%20Words%3A%20Transformers%20for%20Image%20Recognition%20at%20Scale
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=An%20Image%20Is%20Worth%2016x16%20Words%3A%20Transformers%20for%20Image%20Recognition%20at%20Scale&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Menerapkan Transformer murni pada patch citra sebagai token, membuktikan bahwa dengan pra-pelatihan skala besar Transformer mengungguli CNN pada klasifikasi citra.

## Abstrak (Parafrase)
ViT memecah citra menjadi patch 16x16 yang diperlakukan sebagai token, ditambah positional embedding, lalu diproses Transformer encoder standar (seperti pada NLP) untuk klasifikasi. Tanpa bias induktif konvolusi, ViT memerlukan data pra-pelatihan sangat besar (ImageNet-21k/JFT-300M); dengan skala data cukup, ViT mengungguli CNN state-of-the-art dengan komputasi pra-pelatihan lebih hemat.

## Latar Belakang & Konteks
Konvolusi lama diasumsikan wajib untuk visi karena bias induktif (lokalitas, translasi). Belum terbukti apakah Transformer murni, yang sukses di NLP, dapat unggul pada citra tanpa konvolusi.

## Permasalahan yang Diangkat
- Diasumsikan konvolusi wajib untuk pemrosesan citra.
- Transformer murni kekurangan bias induktif visual.
- Butuh cara memperlakukan citra sebagai urutan token.
- Skalabilitas terhadap data/komputasi belum diketahui.
- Generalisasi tanpa lokalitas dipertanyakan.

## Tujuan & Pertanyaan Penelitian
- Membuktikan Transformer murni efektif untuk citra.
- Menunjukkan pentingnya skala data pra-pelatihan.
- Menyediakan backbone alternatif tanpa konvolusi.

## Tinjauan Terdahulu / Posisi Literatur
ViT mengadaptasi Transformer NLP ke citra dan membandingkannya dengan ResNet/BiT pada berbagai skala data.

Karya/konsep pembanding yang relevan:

- Transformer (NLP) — arsitektur dasar.
- ResNet/BiT — pembanding CNN.
- Patch embedding — tokenisasi citra.
- Self-attention — mekanisme inti.

## Metodologi & Arsitektur
Citra dipecah menjadi patch non-overlap, diproyeksikan linear menjadi token, ditambah embedding posisi dan token [CLS]; Transformer encoder (multi-head self-attention + MLP) memprosesnya; head klasifikasi pada token [CLS]. Pra-pelatihan pada data besar lalu fine-tune.

Komponen / langkah metodologis utama:

- Patch embedding (patch 16x16 -> token).
- Positional embedding + token [CLS].
- Transformer encoder standar (MHSA + MLP).
- Pra-pelatihan skala besar (ImageNet-21k/JFT).
- Fine-tuning pada tugas hilir.
- Minim bias induktif konvolusi.

## Kontribusi Utama
1. Transformer murni mengungguli CNN dengan data cukup.
2. Menegaskan skala data sebagai faktor kunci.
3. Membuka era backbone Transformer untuk visi.
4. Mendasari ViT-varian untuk deteksi/segmentasi.

## Rincian Eksperimen
Diuji pada ImageNet, CIFAR, VTAB dsb. dengan variasi ukuran model dan skala data pra-pelatihan, dibandingkan CNN (BiT/ResNet).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ImageNet | akurasi top-1 | ViT-L/H unggul saat dipra-latih JFT-300M |
| Komputasi | pra-latih | lebih hemat dari CNN pada akurasi setara |
| Skala kecil | akurasi | tanpa data besar, kalah dari CNN |

## Temuan Kunci
- Skala data pra-pelatihan menentukan keunggulan ViT.
- Transformer murni layak untuk citra.
- Tanpa data besar, bias induktif CNN masih unggul.
- Attention global memberi representasi kuat.

## Keunggulan
- Backbone kuat dengan data cukup.
- Skalabel dan sederhana konseptual.
- Fondasi banyak model visi modern.

## Keterbatasan
- Butuh data pra-pelatihan sangat besar.
- Komputasi attention besar untuk resolusi tinggi.
- Kurang efisien untuk prediksi padat tanpa modifikasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ViT mengubah lanskap backbone visi dan mendasari backbone Transformer (Swin, VST) yang dipakai pada RGB-D SOD/segmentasi dalam tinjauan ini.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
- [007 - 2023 - YOLOv7 - Fondasi RGB](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)
- [008 - 2024 - YOLOv9 - Fondasi RGB](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fondasi RGB** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Fondasi RGB)
Istilah penting untuk memahami makalah ini:

- **Bounding box** — Kotak pembatas yang melingkupi objek; (x,y,w,h) atau (x1,y1,x2,y2).
- **Anchor box** — Kotak acuan berukuran/rasio tetap tempat jaringan meregresi offset objek.
- **Anchor-free** — Deteksi tanpa anchor; memprediksi pusat/keypoint atau jarak ke sisi box.
- **mAP** — mean Average Precision; rata-rata AP lintas kelas/ambang IoU.
- **IoU** — Intersection over Union; rasio irisan/gabungan dua box.
- **NMS** — Non-Maximum Suppression; membuang deteksi berlebih yang tumpang tindih.
- **Backbone** — Jaringan ekstraksi fitur (ResNet, CSPDarknet) di awal detektor.
- **Neck** — Modul agregasi fitur multi-skala (FPN, PAN, BiFPN).
- **Head** — Bagian akhir yang menghasilkan prediksi kelas dan box.
- **One-stage vs two-stage** — Satu-tahap (YOLO/SSD) langsung; dua-tahap (Faster R-CNN) pakai proposal.
- **FLOPs** — Floating-point operations; ukuran biaya komputasi.
- **Attention/Transformer** — Mekanisme membobot relasi antar-token/fitur secara global.

## Checklist Verifikasi Manual
Centang saat memeriksa berkas ini terhadap makalah asli:

- [ ] Judul, tahun, dan venue di berkas ini cocok dengan makalah asli (buka tautan).
- [ ] Nama penulis sesuai (perhatikan entri yang memakai 'others'/dkk.).
- [ ] Klaim metode/arsitektur di bagian Metodologi sesuai isi makalah.
- [ ] Dataset yang disebut pada bagian Eksperimen benar dipakai makalah.
- [ ] Metrik & angka hasil (bila tercantum) sesuai tabel makalah asli.
- [ ] Daftar Kontribusi mencerminkan klaim penulis, bukan tafsir berlebih.
- [ ] Bagian Keterbatasan wajar (sebagian dapat berupa inferensi, bukan pernyataan penulis).
- [ ] Tautan arXiv/DOI/Scholar benar mengarah ke makalah yang dimaksud.
- [ ] Relevansi terhadap tema (YOLO/RGB/RGB-D) masuk akal untuk kebutuhan Anda.
- [ ] Jenis publikasi (jurnal/konferensi/preprint) sesuai kebutuhan sitasi Anda.
- [ ] Tahun publikasi berada pada rentang fokus tinjauan (2019-2026) atau merupakan karya fondasi yang dirujuk.
- [ ] Kode/sumber terbuka (bila ada) tersedia dan dapat direproduksi.

## Pertanyaan Telaah Kritis
Gunakan pertanyaan berikut untuk menilai kualitas dan kecocokan makalah bagi riset Anda:

- Apa gap/celah spesifik yang membedakan makalah ini dari karya sebelumnya?
- Apakah klaim kinerja didukung ablation study (uji komponen) yang memadai?
- Seberapa adil baseline pembanding (dataset, resolusi, dan anggaran komputasi setara)?
- Apakah metrik yang dipakai tepat untuk tugasnya (mis. mAP untuk deteksi, mIoU untuk segmentasi, AbsRel untuk depth)?
- Bagaimana generalisasi metode ke domain/dataset lain di luar yang diuji?
- Apakah biaya komputasi (parameter, FLOPs, FPS) dilaporkan dan realistis untuk penerapan Anda?

## Kesimpulan
ViT membuktikan Transformer murni pada patch citra mengungguli CNN dengan pra-pelatihan skala besar, membuka era backbone Transformer untuk deteksi dan tugas RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `dosovitskiy2021vit` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 024/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
