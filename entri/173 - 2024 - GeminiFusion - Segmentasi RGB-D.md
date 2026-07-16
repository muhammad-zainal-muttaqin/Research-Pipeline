# 173 - GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 173 dari 191 |
| Kunci BibTeX | `jia2024geminifusion` |
| Judul | GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer |
| Penulis | Jia, Ding; Guo, Jianyuan; Han, Kai; Wu, Han; Zhang, Chao; Xu, Chang; Chen, Xinghao |
| Tahun | 2024 |
| Venue / Jurnal | International Conference on Machine Learning (ICML) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | multimodal fusion, vision transformer, pixel-wise, RGB-X |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2406.01210
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=GeminiFusion%3A%20Efficient%20Pixel-wise%20Multimodal%20Fusion%20for%20Vision%20Transformer
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=GeminiFusion%3A%20Efficient%20Pixel-wise%20Multimodal%20Fusion%20for%20Vision%20Transformer&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2406.01210 |

## Ringkasan Eksekutif
GeminiFusion adalah modul fusi multimodal efisien untuk Vision Transformer yang menggabungkan informasi antar-modal secara per-piksel (pixel-wise), berlaku untuk RGB-D, RGB-thermal, dan kombinasi lain dengan biaya linear.

## Abstrak (Parafrase)
Penulis mengusung fusi intra- dan inter-modal per-piksel yang menyeimbangkan kedua aliran secara adaptif dengan bobot yang dipelajari, menghindari attention lintas-modal global yang mahal. GeminiFusion dapat disisipkan ke ViT untuk berbagai tugas RGB-X (segmentasi, deteksi) dan mencapai hasil SOTA/kompetitif dengan kompleksitas linear terhadap jumlah token.

## Latar Belakang & Konteks
Fusi multimodal berbasis attention global mahal; dibutuhkan fusi efisien yang tetap kuat untuk banyak kombinasi modalitas.

## Permasalahan yang Diangkat
- Cross-attention global mahal.
- Fusi tak seimbang antar-modal.
- Perlu modul serbaguna lintas tugas RGB-X.

## Tujuan & Pertanyaan Penelitian
- Fusi multimodal per-piksel efisien.
- Menyeimbangkan aliran modal adaptif.
- Serbaguna untuk banyak tugas.

## Tinjauan Terdahulu / Posisi Literatur
Berdialog dengan CMX/TokenFusion (fusi RGB-X) dan Omnivore; menekankan efisiensi linear per-piksel.

Karya/konsep pembanding yang relevan:

- CMX - fusi RGB-X berbasis Transformer.
- TokenFusion - pertukaran token multimodal.
- Omnivore - model multi-modalitas tunggal.
- DFormer - representasi RGBD.

## Metodologi & Arsitektur
Untuk tiap piksel, gabungkan fitur intra-modal dan inter-modal dengan bobot adaptif (learned gating), memakai operasi lokal yang linear; disisipkan pada beberapa layer ViT.

Komponen / langkah metodologis utama:

- Fusi intra + inter-modal per-piksel.
- Bobot adaptif (gating) yang dipelajari.
- Kompleksitas linear terhadap token.
- Plug-in ke ViT/backbone RGB-X.

## Kontribusi Utama
1. Modul fusi multimodal per-piksel efisien.
2. Kompleksitas linear.
3. Serbaguna lintas modal & tugas.
4. Hasil SOTA/kompetitif RGB-X.

## Rincian Eksperimen
Segmentasi RGB-D (NYUv2/SUNRGB-D), RGB-thermal, dan tugas RGB-X lain dengan mIoU; pembandingan efisiensi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2/SUNRGB-D | mIoU | SOTA/kompetitif |
| RGB-T/RGB-X | mIoU | konsisten lintas modal |
| Efisiensi | FLOPs | linear, lebih murah dari cross-attention global |

## Temuan Kunci
- Fusi per-piksel adaptif efektif dan murah.
- Satu modul melayani banyak modalitas.
- Keseimbangan modal penting.

## Keunggulan
- Efisien (linear).
- Serbaguna.
- Mudah diintegrasi ke ViT.

## Keterbatasan
- Fokus per-piksel bisa lemah pada konteks global.
- Bergantung kualitas modal kedua.
- Perlu penyetelan gating.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Modul fusi generik yang langsung relevan untuk menggabungkan depth ke backbone RGB pada deteksi/segmentasi RGB-D modern.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [171 - 2021 - SegFormer - Segmentasi RGB-D](./171%20-%202021%20-%20SegFormer%20-%20Segmentasi%20RGB-D.md)
- [172 - 2022 - EMSANet - Segmentasi RGB-D](./172%20-%202022%20-%20EMSANet%20-%20Segmentasi%20RGB-D.md)
- [174 - 2022 - Omnivore - Segmentasi RGB-D](./174%20-%202022%20-%20Omnivore%20-%20Segmentasi%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Segmentasi RGB-D** dalam peta tinjauan (17 klaster, 191 entri total).
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
GeminiFusion menawarkan fusi multimodal per-piksel yang efisien dan serbaguna, komponen praktis untuk arsitektur RGB-X.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `jia2024geminifusion` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 173/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
