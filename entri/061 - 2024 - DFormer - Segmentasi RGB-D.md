# 061 - DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 061 dari 154 |
| Kunci BibTeX | `yin2024dformer` |
| Judul | DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation |
| Penulis | Yin, Bowen; Zhang, Xuying; Li, Zhong-Yu; Liu, Li; Cheng, Ming-Ming; Hou, Qibin |
| Tahun | 2024 |
| Venue / Jurnal | International Conference on Learning Representations (ICLR) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, pra-pelatihan RGB-D, representasi, efisien, backbone |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DFormer%3A%20Rethinking%20RGBD%20Representation%20Learning%20for%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DFormer%3A%20Rethinking%20RGBD%20Representation%20Learning%20for%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Backbone RGB-D yang memikirkan ulang pra-pelatihan representasi dengan meng-encode interaksi RGB-D sejak pra-pelatihan, menghasilkan segmentasi efisien dan akurat.

## Abstrak (Parafrase)
DFormer berargumen bahwa backbone RGB yang dipra-latih ImageNet tidak dirancang untuk kedalaman, sehingga fusi belakangan kurang optimal. DFormer memakai building block interaksi RGB-D dan melakukan pra-pelatihan RGB-D pada ImageNet, sehingga representasi sadar-RGBD terbentuk sejak awal. Hasilnya SOTA dengan komputasi lebih rendah.

## Latar Belakang & Konteks
Backbone pra-latih RGB tidak menyandikan interaksi RGB-D, sehingga metode fusi harus 'menambal' interaksi di tahap hilir, kurang optimal dan boros.

## Permasalahan yang Diangkat
- Backbone pra-latih RGB tak menyandikan kedalaman.
- Fusi ditambahkan di tahap hilir kurang optimal.
- Pra-pelatihan sadar-RGBD belum umum.
- Efisiensi parameter/komputasi diperlukan.
- Interaksi RGB-D perlu sejak awal.

## Tujuan & Pertanyaan Penelitian
- Meng-encode interaksi RGB-D sejak pra-pelatihan.
- Menyediakan backbone RGB-D efisien.
- Meningkatkan akurasi dengan komputasi lebih rendah.

## Tinjauan Terdahulu / Posisi Literatur
DFormer mengubah pra-pelatihan agar sadar-RGBD sejak awal.

Karya/konsep pembanding yang relevan:

- Backbone pra-latih RGB — yang dikritik.
- Pra-pelatihan ImageNet (RGB-D).
- Building block interaksi RGB-D.
- Segmentasi RGB-D.

## Metodologi & Arsitektur
Building block DFormer menyandikan interaksi RGB-D di dalam backbone; pra-pelatihan dilakukan pada ImageNet dengan kedalaman (mis. dari model depth); representasi hasil dipakai untuk segmentasi RGB-D dengan decoder ringan.

Komponen / langkah metodologis utama:

- Building block interaksi RGB-D dalam backbone.
- Pra-pelatihan RGB-D pada ImageNet.
- Representasi sadar-RGBD sejak awal.
- Efisien parameter/komputasi.
- Decoder ringan untuk segmentasi.
- Pelatihan end-to-end hilir.

## Kontribusi Utama
1. Menggeser fusi ke tahap pra-pelatihan.
2. Building block interaksi RGB-D.
3. SOTA dengan komputasi lebih rendah.
4. Arah baru representasi RGB-D.

## Rincian Eksperimen
Diuji pada NYUv2, SUN RGB-D (dan dataset RGB-D lain) dengan metrik mIoU dan perbandingan komputasi terhadap backbone RGB + fusi hilir.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | SOTA dengan komputasi lebih rendah |
| SUN RGB-D | mIoU | SOTA/kompetitif |
| Efisiensi | parameter/FLOPs | lebih hemat dari fusi hilir |

## Temuan Kunci
- Interaksi RGB-D sejak pra-pelatihan lebih optimal.
- Efisiensi parameter/komputasi meningkat.
- Representasi sadar-RGBD kuat.
- Menggeser paradigma fusi ke pra-pelatihan.

## Keunggulan
- Efisien & akurat.
- Pra-pelatihan sadar-RGBD.
- Arah baru representasi.

## Keterbatasan
- Butuh pra-pelatihan RGB-D (biaya awal).
- Bergantung kualitas kedalaman pra-latih.
- Adopsi memerlukan bobot pra-latih khusus.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DFormer mewakili arah mutakhir representasi RGB-D (fusi sejak pra-pelatihan) yang relevan bagi masa depan fusi RGB+Depth dalam tinjauan.

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
DFormer memikirkan ulang representasi RGB-D dengan meng-encode interaksi lintas-modal sejak pra-pelatihan ImageNet, menghasilkan backbone efisien dan akurat serta arah baru fusi RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yin2024dformer` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 061/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
