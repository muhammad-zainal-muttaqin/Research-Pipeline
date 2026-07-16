# 052 - RedNet: Residual Encoder-Decoder Network for Indoor RGB-D Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 052 dari 154 |
| Kunci BibTeX | `jiang2018rednet` |
| Judul | RedNet: Residual Encoder-Decoder Network for Indoor RGB-D Semantic Segmentation |
| Penulis | Jiang, Jindong; Zheng, Lunan; Luo, Fei; Zhang, Zhijun |
| Tahun | 2018 |
| Venue / Jurnal | arXiv preprint arXiv:1806.01054 |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, residual encoder-decoder, pyramid supervision, indoor, fusi |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1806.01054
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RedNet%3A%20Residual%20Encoder-Decoder%20Network%20for%20Indoor%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RedNet%3A%20Residual%20Encoder-Decoder%20Network%20for%20Indoor%20RGB-D%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 1806.01054 |

## Ringkasan Eksekutif
Arsitektur segmentasi semantik RGB-D indoor yang memakai residual encoder-decoder dengan fusi kedalaman dan supervisi piramida.

## Abstrak (Parafrase)
RedNet (Residual Encoder-Decoder Network) memakai encoder-decoder berbasis ResNet dengan fusi fitur kedalaman ke cabang RGB dan pyramid supervision (supervisi pada beberapa skala decoder) untuk segmentasi indoor RGB-D. Desain residual menstabilkan pelatihan jaringan dalam dan menghasilkan akurasi kompetitif saat rilis.

## Latar Belakang & Konteks
Segmentasi indoor RGB-D memerlukan arsitektur dalam yang stabil dilatih dan memanfaatkan kedalaman; encoder-decoder tanpa residual sulit dilatih dalam.

## Permasalahan yang Diangkat
- Segmentasi indoor RGB-D butuh jaringan dalam stabil.
- Encoder-decoder tanpa residual sulit dilatih dalam.
- Kedalaman perlu difusikan efektif.
- Supervisi hanya di akhir kurang optimal.
- Detail batas objek sulit dipulihkan.

## Tujuan & Pertanyaan Penelitian
- Memakai residual encoder-decoder yang stabil.
- Memfusikan kedalaman ke cabang RGB.
- Menerapkan pyramid supervision.

## Tinjauan Terdahulu / Posisi Literatur
RedNet menggabungkan ResNet encoder dan skema fusi RGB-D untuk segmentasi indoor.

Karya/konsep pembanding yang relevan:

- ResNet — encoder residual.
- Encoder-decoder segmentasi.
- Fusi RGB-D (mirip FuseNet).
- Deep/pyramid supervision.

## Metodologi & Arsitektur
Encoder ResNet memproses RGB dan kedalaman; fitur kedalaman difusikan ke cabang RGB; decoder residual memulihkan resolusi dengan skip connection; pyramid supervision menerapkan loss pada beberapa skala decoder.

Komponen / langkah metodologis utama:

- Encoder-decoder residual (ResNet).
- Fusi fitur kedalaman ke RGB.
- Skip connection encoder-decoder.
- Pyramid supervision (multi-skala).
- Segmentasi per-piksel indoor.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Residual encoder-decoder yang stabil dilatih.
2. Fusi kedalaman efektif.
3. Pyramid supervision meningkatkan akurasi.
4. Kompetitif pada segmentasi indoor saat rilis.

## Rincian Eksperimen
Diuji pada SUN RGB-D dan NYUv2 dengan metrik mIoU dan pixel accuracy, dibandingkan RGB saja dan metode fusi lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| SUN RGB-D | mIoU/pixel acc | kompetitif saat rilis |
| NYUv2 | mIoU | peningkatan dengan fusi kedalaman |
| Ablation | pyramid supervision | supervisi multi-skala menyumbang gain |

## Temuan Kunci
- Residual penting untuk melatih jaringan segmentasi dalam.
- Fusi kedalaman meningkatkan akurasi.
- Pyramid supervision membantu konvergensi/akurasi.
- Skip connection memulihkan detail.

## Keunggulan
- Stabil dilatih (residual).
- Fusi kedalaman efektif.
- Pyramid supervision bermanfaat.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Backbone relatif berat.
- Fusi tetap relatif sederhana.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
RedNet menegaskan residual + fusi kedalaman untuk segmentasi indoor; melengkapi FuseNet sebagai fondasi klaster Segmentasi RGB-D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
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
RedNet memakai residual encoder-decoder dengan fusi kedalaman dan pyramid supervision untuk segmentasi indoor RGB-D, menghasilkan arsitektur dalam yang stabil dan akurat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `jiang2018rednet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 052/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
