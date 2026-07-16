# 054 - ACNet: Attention Based Network to Exploit Complementary Features for RGBD Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 054 dari 154 |
| Kunci BibTeX | `hu2019acnet` |
| Judul | ACNet: Attention Based Network to Exploit Complementary Features for RGBD Semantic Segmentation |
| Penulis | Hu, Xinxin; Yang, Kailun; Fei, Lei; Wang, Kaiwei |
| Tahun | 2019 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Image Processing (ICIP) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, attention, tiga-cabang, complementary features, fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ACNet%3A%20Attention%20Based%20Network%20to%20Exploit%20Complementary%20Features%20for%20RGBD%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ACNet%3A%20Attention%20Based%20Network%20to%20Exploit%20Complementary%20Features%20for%20RGBD%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1440--1444 |

## Ringkasan Eksekutif
Arsitektur segmentasi RGB-D yang memakai tiga cabang (RGB, kedalaman, fusi) dengan attention untuk menimbang kontribusi fitur secara adaptif.

## Abstrak (Parafrase)
ACNet (Attention Complementary Network) memakai tiga cabang paralel: RGB, kedalaman, dan cabang fusi. Attention Complementary Module (ACM) menimbang fitur dari RGB dan kedalaman sebelum diagregasi ke cabang fusi, sehingga kontribusi tiap modal disesuaikan secara spasial. Pendekatan ini mencapai SOTA saat rilis pada segmentasi indoor.

## Latar Belakang & Konteks
Bobot kontribusi RGB vs kedalaman bervariasi secara spasial (mis. daerah bertekstur vs daerah datar), sehingga fusi tanpa pembobotan adaptif kurang optimal.

## Permasalahan yang Diangkat
- Kontribusi RGB vs kedalaman bervariasi spasial.
- Fusi tanpa pembobotan adaptif kurang optimal.
- Fitur komplementer perlu diseleksi.
- Segmentasi indoor kompleks.
- Agregasi tiga sumber fitur sulit.

## Tujuan & Pertanyaan Penelitian
- Menimbang fitur RGB & kedalaman via attention.
- Mengagregasi ke cabang fusi khusus.
- Menyesuaikan kontribusi modal secara spasial.

## Tinjauan Terdahulu / Posisi Literatur
ACNet menggabungkan attention channel dan arsitektur tiga-cabang untuk RGB-D segmentation.

Karya/konsep pembanding yang relevan:

- Attention (channel) — pembobotan fitur.
- Arsitektur tiga-cabang.
- Segmentasi RGB-D.
- Complementary feature selection.

## Metodologi & Arsitektur
Tiga cabang (RGB, depth, fusi) berbasis ResNet; Attention Complementary Module menimbang fitur RGB dan kedalaman lalu menambahkannya ke cabang fusi di beberapa level; decoder menghasilkan segmentasi.

Komponen / langkah metodologis utama:

- Tiga cabang paralel (RGB, depth, fusi).
- Attention Complementary Module (ACM).
- Pembobotan fitur adaptif per-modal.
- Agregasi ke cabang fusi.
- Backbone ResNet.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Attention menimbang kontribusi modal adaptif.
2. Arsitektur tiga-cabang dengan cabang fusi.
3. Seleksi fitur komplementer.
4. SOTA pada segmentasi indoor saat rilis.

## Rincian Eksperimen
Diuji pada NYUv2 dan SUN RGB-D dengan metrik mIoU dan pixel accuracy, plus ablation ACM.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | SOTA saat rilis |
| SUN RGB-D | mIoU | kompetitif/unggul |
| Ablation | ACM | attention menyumbang gain |

## Temuan Kunci
- Attention pentimbang modal efektif untuk RGB-D.
- Cabang fusi khusus membantu agregasi.
- Kontribusi modal disesuaikan spasial.
- Fitur komplementer diseleksi.

## Keunggulan
- Attention adaptif.
- Tiga-cabang dengan fusi.
- SOTA saat rilis.

## Keterbatasan
- Tiga cabang menambah komputasi.
- Bergantung kualitas kedalaman.
- Kompleksitas arsitektur.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ACNet menunjukkan attention untuk menimbang kontribusi modal — mekanisme kunci fusi RGB+Depth yang berulang di banyak entri tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)
- [057 - 2021 - ShapeConv - Segmentasi RGB-D](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md)
- [058 - 2023 - CMX - Segmentasi RGB-D](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)
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
ACNet memakai tiga cabang dengan Attention Complementary Module untuk menimbang kontribusi RGB dan kedalaman secara adaptif, mencapai SOTA pada segmentasi indoor RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `hu2019acnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 054/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
