# 169 - CAVER: Cross-Modal View-Mixed Transformer for Bi-Modal Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 169 dari 191 |
| Kunci BibTeX | `pang2023caver` |
| Judul | CAVER: Cross-Modal View-Mixed Transformer for Bi-Modal Salient Object Detection |
| Penulis | Pang, Youwei; Zhao, Xiaoqi; Zhang, Lihe; Lu, Huchuan |
| Tahun | 2023 |
| Venue / Jurnal | IEEE Transactions on Image Processing |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, RGB-T, transformer, view-mixed attention |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-sod)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=CAVER%3A%20Cross-Modal%20View-Mixed%20Transformer%20for%20Bi-Modal%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=CAVER%3A%20Cross-Modal%20View-Mixed%20Transformer%20for%20Bi-Modal%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 32 |
| Halaman | 892--904 |

## Ringkasan Eksekutif
CAVER adalah Transformer lintas-modal untuk salient object detection dwi-modal (RGB-D dan RGB-T) yang memadukan pandangan antar-modalitas melalui view-mixed attention efisien, menyatukan penanganan depth dan thermal dalam satu kerangka.

## Abstrak (Parafrase)
Penulis mengusung cross-modal view-mixed transformer yang memperlakukan fusi RGB-D dan RGB-T secara seragam. Modul attention memandang fitur lintas-modal sebagai token campuran dan menggunakan operasi patch-wise yang efisien untuk pertukaran informasi, ditambah dekoder progresif. CAVER mencapai kinerja SOTA pada benchmark RGB-D maupun RGB-T SOD.

## Latar Belakang & Konteks
Metode SOD dwi-modal sering dirancang khusus RGB-D atau RGB-T; kerangka terpadu berbasis Transformer masih jarang dan mahal.

## Permasalahan yang Diangkat
- Metode terpisah untuk RGB-D vs RGB-T.
- Attention lintas-modal mahal.
- Fusi multiskala kurang efisien.

## Tujuan & Pertanyaan Penelitian
- Menyatukan SOD RGB-D dan RGB-T.
- Merancang attention lintas-modal efisien.
- Mencapai SOTA dwi-modal.

## Tinjauan Terdahulu / Posisi Literatur
Berpijak pada Transformer SOD (VST, SwinNet) dan fusi RGB-T; menekankan keseragaman penanganan modalitas kedua.

Karya/konsep pembanding yang relevan:

- VST - visual saliency transformer.
- SwinNet - Swin untuk RGB-D/RGB-T SOD.
- BBS-Net - fusi bercabang.
- Transformer lintas-modal umum.

## Metodologi & Arsitektur
Encoder ganda mengekstrak fitur RGB dan modal kedua; view-mixed attention module menukar informasi lintas-modal secara efisien; dekoder progresif menyatukan skala untuk peta saliency.

Komponen / langkah metodologis utama:

- Encoder dua-aliran (RGB + depth/thermal).
- View-mixed attention efisien.
- Fusi lintas-modal patch-wise.
- Dekoder progresif multiskala.

## Kontribusi Utama
1. Kerangka Transformer terpadu RGB-D/RGB-T SOD.
2. View-mixed attention efisien.
3. SOTA di kedua tugas.
4. Desain modular lintas-modal.

## Rincian Eksperimen
Benchmark RGB-D SOD dan RGB-T SOD (mis. VT821/VT1000/VT5000 untuk RGB-T) dengan S/F/E-measure dan MAE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| RGB-D SOD | S/E-measure | SOTA/kompetitif |
| RGB-T SOD | F-measure/MAE | SOTA saat rilis |
| Efisiensi | params/FLOPs | lebih ringan dari Transformer fusi naif |

## Temuan Kunci
- Satu kerangka dapat menangani depth dan thermal.
- Attention efisien menjaga biaya rendah.
- Fusi lintas-modal terpadu efektif.

## Keunggulan
- Terpadu dan efisien.
- SOTA dwi-modal.
- Modular.

## Keterbatasan
- Tetap butuh dua encoder.
- Bergantung kualitas modal kedua.
- Transformer relatif berat untuk edge.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Menyatukan fusi depth dan thermal, relevan untuk persepsi multimodal (RGB-D/RGB-T) pada kondisi pencahayaan menantang.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [166 - 2020 - CoNet - RGB-D SOD](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md)
- [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md)
- [168 - 2021 - SPNet - RGB-D SOD](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md)
- [170 - 2022 - MobileSal - RGB-D SOD](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SOD)
Istilah penting untuk memahami makalah ini:

- **SOD** — Salient Object Detection; menyorot objek paling menonjol.
- **Peta kedalaman** — Citra yang tiap pikselnya menyatakan jarak ke kamera.
- **Fusi lintas-modal** — Penggabungan fitur RGB dan depth.
- **Early/middle/late fusion** — Fusi di input, fitur tengah, atau keputusan akhir.
- **Attention lintas-modal** — Membobot kontribusi RGB vs depth secara adaptif.
- **S-measure** — Structure-measure; kemiripan struktur peta saliency.
- **E-measure** — Enhanced-alignment measure; kesejajaran piksel-global.
- **F-measure** — Harmonik precision-recall pada peta saliency.
- **MAE** — Mean Absolute Error peta saliency vs ground truth.
- **Depth berkualitas rendah** — Depth berderau yang dapat merusak fusi.
- **Backbone Transformer** — Encoder attention (mis. Swin) untuk konteks global.

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
CAVER menghadirkan Transformer lintas-modal terpadu yang efisien untuk SOD dwi-modal, menjembatani RGB-D dan RGB-T.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `pang2023caver` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 169/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
