# 051 - FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 051 dari 154 |
| Kunci BibTeX | `hazirbas2016fusenet` |
| Judul | FuseNet: Incorporating Depth into Semantic Segmentation via Fusion-Based CNN Architecture |
| Penulis | Hazirbas, Caner; Ma, Lingni; Domokos, Csaba; Cremers, Daniel |
| Tahun | 2016 |
| Venue / Jurnal | Proceedings of the Asian Conference on Computer Vision (ACCV) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, encoder ganda, fusi penjumlahan, SegNet, indoor |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=FuseNet%3A%20Incorporating%20Depth%20into%20Semantic%20Segmentation%20via%20Fusion-Based%20CNN%20Architecture
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=FuseNet%3A%20Incorporating%20Depth%20into%20Semantic%20Segmentation%20via%20Fusion-Based%20CNN%20Architecture&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 213--228 |

## Ringkasan Eksekutif
Pelopor segmentasi semantik RGB-D yang menyisipkan cabang kedalaman ke encoder-decoder SegNet dan menjumlahkan fitur kedalaman ke cabang RGB secara berkala.

## Abstrak (Parafrase)
FuseNet memperluas SegNet ke input RGB-D dengan arsitektur dua-encoder: satu untuk RGB, satu untuk kedalaman. Fitur kedalaman dijumlahkan ke cabang RGB secara berkala (element-wise addition) di beberapa level, menyalurkan isyarat geometri ke jalur utama. Satu decoder menghasilkan segmentasi. Fusi penjumlahan ini menaikkan akurasi dibanding RGB saja.

## Latar Belakang & Konteks
Kedalaman memuat isyarat geometri (bentuk, batas objek) yang berguna untuk segmentasi, tetapi cara mengintegrasikannya ke CNN segmentasi belum jelas pada saat itu.

## Permasalahan yang Diangkat
- Cara mengintegrasikan kedalaman ke CNN segmentasi belum jelas.
- Isyarat geometri kedalaman kurang dimanfaatkan.
- Fusi input naif (4-kanal) kurang efektif.
- Segmentasi indoor kompleks (banyak kelas/oklusi).
- Perlu arsitektur yang menjaga detail geometri.

## Tujuan & Pertanyaan Penelitian
- Mengintegrasikan kedalaman ke encoder-decoder segmentasi.
- Menyalurkan geometri ke jalur RGB secara berkala.
- Meningkatkan akurasi segmentasi indoor.

## Tinjauan Terdahulu / Posisi Literatur
FuseNet memperluas SegNet ke RGB-D dengan strategi fusi encoder ganda.

Karya/konsep pembanding yang relevan:

- SegNet — encoder-decoder dasar.
- Segmentasi RGB-D awal.
- Element-wise fusion (penjumlahan).
- Dataset NYUv2/SUN RGB-D.

## Metodologi & Arsitektur
Dua encoder (RGB & depth) berbasis VGG; fitur kedalaman dijumlahkan ke fitur RGB pada beberapa level encoder; decoder tunggal (dengan unpooling gaya SegNet) memulihkan resolusi dan menghasilkan peta segmentasi.

Komponen / langkah metodologis utama:

- Arsitektur dua-encoder (RGB & depth).
- Fusi penjumlahan fitur bertahap (multi-level).
- Decoder tunggal gaya SegNet (unpooling).
- Backbone VGG.
- Segmentasi per-piksel multi-kelas.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Pelopor strategi fusi encoder ganda RGB-D.
2. Fusi penjumlahan bertahap efektif.
3. Menaikkan akurasi dibanding RGB saja.
4. Dasar banyak arsitektur segmentasi RGB-D.

## Rincian Eksperimen
Diuji pada NYUv2 dan SUN RGB-D dengan metrik segmentasi (pixel accuracy, mIoU), dibandingkan RGB saja dan fusi input naif.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU/pixel acc | fusi depth > RGB saja |
| SUN RGB-D | mIoU | peningkatan dengan fusi |
| Ablation | fusi penjumlahan | lebih baik dari input 4-kanal |

## Temuan Kunci
- Fusi encoder ganda mengungguli input 4-kanal.
- Penjumlahan bertahap menyalurkan geometri.
- Kedalaman meningkatkan akurasi segmentasi.
- Dasar arsitektur RGB-D berikutnya.

## Keunggulan
- Pelopor & berpengaruh.
- Sederhana (penjumlahan).
- Meningkatkan akurasi.

## Keterbatasan
- Fusi penjumlahan sederhana (kurang adaptif).
- Backbone VGG (relatif berat).
- Bergantung kualitas kedalaman.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
FuseNet adalah entri fondasi klaster Segmentasi RGB-D; strategi fusi encoder ganda mendasari banyak metode fusi RGB+Depth yang dibahas dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
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
FuseNet mempelopori fusi encoder ganda untuk segmentasi semantik RGB-D dengan menjumlahkan fitur kedalaman ke cabang RGB, menjadi dasar banyak arsitektur segmentasi RGB-D berikutnya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `hazirbas2016fusenet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 051/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
