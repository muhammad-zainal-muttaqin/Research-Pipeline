# 059 - PGDENet: Progressive Guided Fusion and Depth Enhancement Network for RGB-D Indoor Scene Parsing

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 059 dari 154 |
| Kunci BibTeX | `zhou2022pgdenet` |
| Judul | PGDENet: Progressive Guided Fusion and Depth Enhancement Network for RGB-D Indoor Scene Parsing |
| Penulis | Zhou, Wujie; Yang, Enquan; Lei, Jingsheng; Yu, Lu |
| Tahun | 2023 |
| Venue / Jurnal | IEEE Transactions on Multimedia |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, depth enhancement, progressive guided fusion, indoor, scene parsing |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PGDENet%3A%20Progressive%20Guided%20Fusion%20and%20Depth%20Enhancement%20Network%20for%20RGB-D%20Indoor%20Scene%20Parsing
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PGDENet%3A%20Progressive%20Guided%20Fusion%20and%20Depth%20Enhancement%20Network%20for%20RGB-D%20Indoor%20Scene%20Parsing&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 25 |
| Halaman | 3483--3494 |

## Ringkasan Eksekutif
Arsitektur scene parsing RGB-D indoor yang memakai progressive guided fusion dan depth enhancement untuk memperbaiki kualitas fitur kedalaman sebelum digabung.

## Abstrak (Parafrase)
PGDENet (Progressive Guided fusion and Depth Enhancement Network) memperkuat fitur kedalaman yang berderau melalui modul depth enhancement, lalu menggabungkannya dengan RGB melalui progressive guided fusion bertahap. Peningkatan kualitas kedalaman pra-fusi meningkatkan akurasi scene parsing indoor.

## Latar Belakang & Konteks
Peta kedalaman mentah sering berderau/tidak lengkap, sehingga langsung memfusikannya menurunkan kualitas; kedalaman perlu ditingkatkan lebih dahulu.

## Permasalahan yang Diangkat
- Kedalaman mentah berderau/tidak lengkap.
- Fusi langsung menurunkan kualitas.
- Kedalaman perlu ditingkatkan pra-fusi.
- Panduan fusi perlu bertahap.
- Scene parsing indoor kompleks.

## Tujuan & Pertanyaan Penelitian
- Meningkatkan fitur kedalaman sebelum fusi.
- Menggabungkan modal via fusi terpandu progresif.
- Meningkatkan akurasi scene parsing indoor.

## Tinjauan Terdahulu / Posisi Literatur
PGDENet mengembangkan penguatan kedalaman dan fusi terpandu progresif.

Karya/konsep pembanding yang relevan:

- Segmentasi/scene parsing RGB-D — dasar.
- Depth enhancement — penguatan kedalaman.
- Progressive/guided fusion.
- Dataset NYUv2/SUN RGB-D.

## Metodologi & Arsitektur
Depth enhancement module memperbaiki/menguatkan fitur kedalaman; progressive guided fusion menggabungkan RGB dan kedalaman secara bertahap dengan panduan; decoder menghasilkan peta segmentasi indoor.

Komponen / langkah metodologis utama:

- Depth enhancement module (penguatan kedalaman).
- Progressive guided fusion bertahap.
- Penguatan kedalaman pra-fusi.
- Fusi terpandu multi-level.
- Decoder segmentasi.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Penguatan kedalaman sebelum fusi.
2. Fusi terpandu progresif.
3. Peningkatan akurasi scene parsing.
4. Menangani kedalaman berderau.

## Rincian Eksperimen
Diuji pada NYUv2 dan SUN RGB-D dengan metrik mIoU dan pixel accuracy, plus ablation depth enhancement.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | peningkatan atas baseline |
| SUN RGB-D | mIoU | kompetitif/unggul |
| Ablation | depth enhancement | penguatan kedalaman menyumbang gain |

## Temuan Kunci
- Penguatan kedalaman pra-fusi bermanfaat.
- Fusi terpandu progresif efektif.
- Kedalaman berderau dapat ditangani.
- Akurasi scene parsing meningkat.

## Keunggulan
- Menangani kedalaman berderau.
- Fusi terpandu progresif.
- Peningkatan konsisten.

## Keterbatasan
- Modul enhancement menambah komputasi.
- Bergantung kualitas kedalaman awal.
- Backbone relatif berat.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PGDENet menekankan peningkatan kualitas kedalaman pra-fusi — melengkapi tema keandalan kedalaman (D3Net/SA-Gate) yang berulang dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)
- [057 - 2021 - ShapeConv - Segmentasi RGB-D](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md)
- [058 - 2023 - CMX - Segmentasi RGB-D](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)

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
PGDENet memperkuat fitur kedalaman via depth enhancement lalu menggabungkannya dengan RGB melalui progressive guided fusion, meningkatkan akurasi scene parsing indoor RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhou2022pgdenet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 059/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
