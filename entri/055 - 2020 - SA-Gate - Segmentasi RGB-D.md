# 055 - Bi-Directional Cross-Modality Feature Propagation with Separation-and-Aggregation Gate for RGB-D Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 055 dari 154 |
| Kunci BibTeX | `chen2020sagate` |
| Judul | Bi-Directional Cross-Modality Feature Propagation with Separation-and-Aggregation Gate for RGB-D Semantic Segmentation |
| Penulis | Chen, Xiaokang; Lin, Kwan-Yee; Wang, Jingbo; Wu, Wayne; Qian, Chen; Li, Hongsheng; Zeng, Gang |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, separation-and-aggregation, bidireksional, gating, propagasi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Bi-Directional%20Cross-Modality%20Feature%20Propagation%20with%20Separation-and-Aggregation%20Gate%20for%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Bi-Directional%20Cross-Modality%20Feature%20Propagation%20with%20Separation-and-Aggregation%20Gate%20for%20RGB-D%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 561--577 |

## Ringkasan Eksekutif
Arsitektur segmentasi RGB-D yang memakai separation-and-aggregation gate untuk menyaring lalu menyatukan fitur RGB dan kedalaman secara dua-arah.

## Abstrak (Parafrase)
SA-Gate (Separation-and-Aggregation Gate) menyaring fitur RGB dan kedalaman (separation) untuk menekan derau sebelum menyatukannya (aggregation), lalu melakukan propagasi lintas-modal dua-arah (bi-directional multi-step propagation). Pendekatan 'saring dulu, baru gabung' ini mencapai SOTA pada NYUv2 dan Cityscapes saat rilis.

## Latar Belakang & Konteks
Fusi naif mencampur derau dari kedalaman berkualitas rendah; fitur perlu disaring sebelum digabung, dan informasi harus mengalir dua-arah antar-modal.

## Permasalahan yang Diangkat
- Fusi naif mencampur derau kedalaman.
- Fitur perlu disaring sebelum digabung.
- Aliran informasi antar-modal sering satu-arah.
- Segmentasi outdoor/indoor menuntut robustness.
- Penyelarasan fitur lintas-modal sulit.

## Tujuan & Pertanyaan Penelitian
- Menyaring fitur sebelum agregasi (gating).
- Menyatukan fitur RGB-D secara bidireksional.
- Meningkatkan robustness terhadap derau kedalaman.

## Tinjauan Terdahulu / Posisi Literatur
SA-Gate mengembangkan gating lintas-modal bidireksional untuk segmentasi RGB-D.

Karya/konsep pembanding yang relevan:

- Segmentasi RGB-D — dasar.
- Gating mechanism — penyaring fitur.
- Bi-directional propagation.
- Dataset NYUv2/Cityscapes.

## Metodologi & Arsitektur
Separation part menyaring fitur RGB dan kedalaman untuk menekan derau; aggregation part menyatukan fitur tersaring; bi-directional multi-step propagation menyalurkan informasi dua-arah antar-modal di beberapa langkah; decoder menghasilkan segmentasi.

Komponen / langkah metodologis utama:

- Separation-and-Aggregation Gate (SA-Gate).
- Penyaringan fitur sebelum agregasi.
- Bi-directional multi-step propagation.
- Aliran informasi dua-arah antar-modal.
- Backbone ResNet.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Prinsip 'saring dulu, baru gabung' (SA-Gate).
2. Propagasi bidireksional lintas-modal.
3. Robust terhadap derau kedalaman.
4. SOTA NYUv2 & Cityscapes saat rilis.

## Rincian Eksperimen
Diuji pada NYUv2 dan Cityscapes dengan metrik mIoU, plus ablation separation/aggregation dan propagasi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | SOTA saat rilis |
| Cityscapes | mIoU | SOTA saat rilis |
| Ablation | SA-Gate | gating & propagasi menyumbang gain |

## Temuan Kunci
- Menyaring sebelum menyatukan mengurangi derau.
- Propagasi bidireksional memperkaya fitur.
- Robust lintas domain (indoor/outdoor).
- Penyelarasan lintas-modal penting.

## Keunggulan
- Gating penyaring derau.
- Propagasi bidireksional.
- SOTA luas.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Kompleksitas propagasi multi-step.
- Backbone relatif berat.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
SA-Gate menegaskan pentingnya menyaring keandalan sebelum fusi — prinsip sentral fusi RGB+Depth yang berulang dalam tinjauan (bandingkan D3Net, S2MA).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
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
SA-Gate memperkenalkan separation-and-aggregation gate dengan propagasi bidireksional untuk segmentasi RGB-D, menegaskan pentingnya menyaring fitur sebelum menyatukannya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `chen2020sagate` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 055/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
