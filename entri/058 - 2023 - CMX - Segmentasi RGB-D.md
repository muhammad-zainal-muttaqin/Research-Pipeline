# 058 - CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 058 dari 154 |
| Kunci BibTeX | `zhang2023cmx` |
| Judul | CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers |
| Penulis | Zhang, Jiaming; Liu, Huayao; Yang, Kailun; Hu, Xinxin; Liu, Ruiping; Stiefelhagen, Rainer |
| Tahun | 2023 |
| Venue / Jurnal | IEEE Transactions on Intelligent Transportation Systems |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-X, Transformer, cross-modal rectification, fusi, general |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-segmentasi-rgb-d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=CMX%3A%20Cross-Modal%20Fusion%20for%20RGB-X%20Semantic%20Segmentation%20with%20Transformers
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=CMX%3A%20Cross-Modal%20Fusion%20for%20RGB-X%20Semantic%20Segmentation%20with%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 24 |
| Nomor | 12 |
| Halaman | 14679--14694 |

## Ringkasan Eksekutif
Kerangka Transformer untuk segmentasi RGB-X (X = depth/thermal/LiDAR/dll.) dengan koreksi fitur lintas-modal dan modul fusi berbasis attention.

## Abstrak (Parafrase)
CMX menggeneralisasi fusi lintas-modal untuk segmentasi RGB-X (modal kedua apa pun) memakai backbone Transformer (SegFormer). Cross-Modal Feature Rectification Module (CM-FRM) mengoreksi fitur kedua modal secara timbal-balik, dan Feature Fusion Module (FFM) berbasis attention menyatukannya. CMX SOTA pada banyak benchmark RGB-D/RGB-T/RGB-LiDAR.

## Latar Belakang & Konteks
Fusi RGB-X perlu generik lintas modal kedua (bukan khusus kedalaman), namun kebanyakan metode dirancang untuk satu modalitas dan tak mudah dialihkan.

## Permasalahan yang Diangkat
- Fusi sering khusus satu modalitas kedua.
- Perlu kerangka generik lintas RGB-X.
- Backbone CNN membatasi konteks global.
- Koreksi fitur lintas-modal diperlukan.
- Fusi berbasis attention belum umum untuk RGB-X.

## Tujuan & Pertanyaan Penelitian
- Menyediakan fusi generik lintas RGB-X.
- Mengoreksi fitur lintas-modal (CM-FRM).
- Menyatukan modal via fusi berbasis attention.

## Tinjauan Terdahulu / Posisi Literatur
CMX menggeneralisasi fusi lintas-modal dengan backbone Transformer (SegFormer).

Karya/konsep pembanding yang relevan:

- SegFormer — backbone Transformer.
- Segmentasi RGB-D/RGB-T/RGB-LiDAR.
- Cross-modal rectification.
- Attention-based fusion.

## Metodologi & Arsitektur
Dua backbone SegFormer memproses RGB dan modal X; CM-FRM mengoreksi fitur kedua modal secara timbal-balik (channel & spatial); FFM berbasis attention menyatukan fitur; decoder menghasilkan segmentasi. Generik untuk depth/thermal/LiDAR/event.

Komponen / langkah metodologis utama:

- Backbone SegFormer dua-aliran (RGB & X).
- Cross-Modal Feature Rectification Module (CM-FRM).
- Feature Fusion Module (FFM) berbasis attention.
- Generik lintas modal kedua (RGB-X).
- Konteks global via Transformer.
- Pelatihan end-to-end.

## Kontribusi Utama
1. Fusi RGB-X universal berbasis Transformer.
2. CM-FRM mengoreksi fitur lintas-modal.
3. FFM attention menyatukan modal.
4. SOTA lintas banyak benchmark/modalitas.

## Rincian Eksperimen
Diuji pada banyak dataset RGB-D, RGB-T, RGB-LiDAR, RGB-event dengan metrik mIoU, membuktikan generalisasi lintas modalitas.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| RGB-D (NYUv2/SUN) | mIoU | SOTA saat rilis |
| RGB-T | mIoU | SOTA lintas dataset |
| RGB-LiDAR/Event | mIoU | generalisasi lintas modalitas |

## Temuan Kunci
- Kerangka fusi RGB-X yang benar-benar generik.
- Koreksi timbal-balik lintas-modal penting.
- Backbone Transformer meningkatkan konteks.
- Generalisasi lintas banyak modalitas kedua.

## Keunggulan
- Generik lintas modalitas.
- Backbone Transformer kuat.
- SOTA luas.

## Keterbatasan
- Dua backbone Transformer mahal.
- Bergantung kualitas modal kedua.
- Kompleksitas rectification+fusion.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
CMX adalah kerangka fusi RGB-X universal yang sangat relevan bagi tinjauan RGB+Depth: menegaskan fusi Transformer generik lintas modalitas kedua.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)
- [057 - 2021 - ShapeConv - Segmentasi RGB-D](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md)
- [059 - 2023 - PGDENet - Segmentasi RGB-D](./059%20-%202023%20-%20PGDENet%20-%20Segmentasi%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Segmentasi RGB-D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Segmentasi RGB-D)
Istilah penting untuk memahami makalah ini:

- **Segmentasi semantik** — Pelabelan kelas per-piksel.
- **Scene parsing** — Pemahaman menyeluruh isi scene via segmentasi.
- **Encoder-decoder** — Arsitektur mengecilkan lalu memulihkan resolusi.
- **Fusi RGB-D** — Penggabungan cabang warna dan kedalaman.
- **mIoU** — mean Intersection-over-Union; metrik segmentasi utama.
- **Gating** — Gerbang penyaring/penimbang fitur sebelum digabung.
- **Cross-modal** — Antar-modalitas (RGB dan depth/thermal/LiDAR).
- **NYUv2** — Dataset RGB-D indoor standar.
- **SUN RGB-D** — Dataset RGB-D indoor berskala.
- **Pixel accuracy** — Persentase piksel terlabel benar.

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
CMX menghadirkan fusi RGB-X universal berbasis Transformer dengan cross-modal rectification dan attention fusion, mencapai SOTA lintas RGB-D/RGB-T/RGB-LiDAR dan menggeneralisasi fusi lintas modalitas.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2023cmx` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 058/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
