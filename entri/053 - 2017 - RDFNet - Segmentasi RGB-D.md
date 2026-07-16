# 053 - RDFNet: RGB-D Multi-Level Residual Feature Fusion for Indoor Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 053 dari 154 |
| Kunci BibTeX | `park2017rdfnet` |
| Judul | RDFNet: RGB-D Multi-Level Residual Feature Fusion for Indoor Semantic Segmentation |
| Penulis | Park, Seong-Jin; Hong, Ki-Sang; Lee, Seungyong |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Computer Vision (ICCV) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, multi-modal feature fusion, residual, multi-level, RefineNet |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RDFNet%3A%20RGB-D%20Multi-Level%20Residual%20Feature%20Fusion%20for%20Indoor%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RDFNet%3A%20RGB-D%20Multi-Level%20Residual%20Feature%20Fusion%20for%20Indoor%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4980--4989 |

## Ringkasan Eksekutif
Arsitektur segmentasi RGB-D yang memperluas fusi residual multi-level (MMF) untuk menggabungkan fitur RGB dan kedalaman di banyak tingkat.

## Abstrak (Parafrase)
RDFNet memperluas RefineNet ke input RGB-D dengan Multi-modal Feature Fusion (MMF) block yang menggabungkan fitur RGB dan kedalaman secara residual di beberapa level. Ini memanfaatkan komplementaritas multi-skala kedua modal untuk segmentasi indoor yang lebih akurat.

## Latar Belakang & Konteks
Fusi RGB-D satu level kurang memanfaatkan komplementaritas yang bervariasi antar-skala; segmentasi indoor menuntut detail sekaligus semantik.

## Permasalahan yang Diangkat
- Fusi RGB-D satu-level kurang memanfaatkan komplementaritas.
- Komplementaritas bervariasi antar-skala.
- Segmentasi indoor butuh detail + semantik.
- Fusi residual multi-level belum dieksplorasi penuh.
- Kedalaman perlu difusikan bertingkat.

## Tujuan & Pertanyaan Penelitian
- Memfusikan RGB & kedalaman residual di banyak level.
- Memanfaatkan komplementaritas multi-skala.
- Meningkatkan akurasi segmentasi indoor.

## Tinjauan Terdahulu / Posisi Literatur
RDFNet memperluas RefineNet dengan blok fusi multi-modal residual.

Karya/konsep pembanding yang relevan:

- RefineNet — arsitektur segmentasi multi-path.
- Residual fusion — penggabungan residual.
- Segmentasi RGB-D.
- Multi-level feature fusion.

## Metodologi & Arsitektur
Multi-modal Feature Fusion (MMF) block menggabungkan fitur RGB dan kedalaman secara residual pada tiap level; jalur RefineNet menyatukan fitur multi-skala; decoder menghasilkan segmentasi.

Komponen / langkah metodologis utama:

- Multi-modal Feature Fusion (MMF) block residual.
- Fusi RGB-D bertingkat (multi-level).
- Jalur RefineNet multi-skala.
- Backbone residual (ResNet).
- Segmentasi per-piksel indoor.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Fusi residual multi-level RGB-D (MMF).
2. Pemanfaatan komplementaritas multi-skala.
3. Peningkatan akurasi segmentasi indoor.
4. Perluasan RefineNet ke RGB-D.

## Rincian Eksperimen
Diuji pada NYUv2 dan SUN RGB-D dengan metrik mIoU dan pixel accuracy, dibandingkan FuseNet dan metode segmentasi lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | peningkatan atas RGB/fusi sederhana |
| SUN RGB-D | mIoU | kompetitif/unggul saat rilis |
| Ablation | MMF | fusi residual multi-level menyumbang gain |

## Temuan Kunci
- Fusi residual multi-level efektif untuk RGB-D.
- Komplementaritas multi-skala dimanfaatkan.
- RefineNet dapat diperluas ke RGB-D.
- Detail & semantik terjaga.

## Keunggulan
- Fusi multi-level residual.
- Memanfaatkan multi-skala.
- Akurat untuk indoor.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Backbone relatif berat.
- Kompleksitas multi-path.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
RDFNet menegaskan efektivitas fusi residual multi-level RGB-D untuk scene parsing; prinsip multi-skala yang relevan bagi fusi RGB+Depth dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
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
RDFNet memperluas RefineNet dengan Multi-modal Feature Fusion residual untuk menggabungkan RGB dan kedalaman di banyak level, meningkatkan akurasi segmentasi indoor RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `park2017rdfnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 053/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
