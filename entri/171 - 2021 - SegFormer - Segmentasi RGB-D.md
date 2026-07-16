# 171 - SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 171 dari 191 |
| Kunci BibTeX | `xie2021segformer` |
| Judul | SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers |
| Penulis | Xie, Enze; Wang, Wenhai; Yu, Zhiding; Anandkumar, Anima; Alvarez, Jose M.; Luo, Ping |
| Tahun | 2021 |
| Venue / Jurnal | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | semantic segmentation, transformer, hierarchical encoder, efficient |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2105.15203
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=SegFormer%3A%20Simple%20and%20Efficient%20Design%20for%20Semantic%20Segmentation%20with%20Transformers
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=SegFormer%3A%20Simple%20and%20Efficient%20Design%20for%20Semantic%20Segmentation%20with%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2105.15203 |

## Ringkasan Eksekutif
SegFormer menyatukan Transformer hierarkis tanpa positional encoding dengan dekoder MLP ringan, menghasilkan segmentasi semantik yang akurat, efisien, dan robust - menjadi baseline populer termasuk untuk cabang RGB pada segmentasi RGB-D.

## Abstrak (Parafrase)
Penulis merancang encoder Transformer hierarkis (MiT) yang menghasilkan fitur multiskala tanpa positional encoding (memakai Mix-FFN), sehingga robust terhadap perubahan resolusi. Dekodernya hanya MLP sederhana yang mengagregasi fitur multiskala. SegFormer mencapai akurasi tinggi pada ADE20K/Cityscapes dengan efisiensi dan ketahanan terhadap korupsi yang baik.

## Latar Belakang & Konteks
Segmentasi berbasis Transformer awal (SETR) berat dan butuh positional encoding yang rapuh terhadap resolusi. Dibutuhkan desain efisien dan robust.

## Permasalahan yang Diangkat
- Positional encoding rapuh lintas resolusi.
- Dekoder segmentasi berat.
- Trade-off akurasi-efisiensi.

## Tujuan & Pertanyaan Penelitian
- Encoder Transformer hierarkis bebas positional encoding.
- Dekoder ringan.
- Segmentasi akurat dan efisien.

## Tinjauan Terdahulu / Posisi Literatur
Kontras dengan SETR (Transformer berat) dan CNN (DeepLab); menekankan Mix-FFN dan dekoder MLP.

Karya/konsep pembanding yang relevan:

- SETR - Transformer segmentasi awal.
- DeepLabv3+ - CNN dilatasi.
- PVT - Transformer piramidal.
- Swin - Transformer berjendela.

## Metodologi & Arsitektur
MiT encoder menghasilkan fitur 4 skala; Mix-FFN menyisipkan konvolusi 3x3 untuk info posisi implisit; dekoder MLP menyatukan fitur multiskala ke prediksi per-piksel.

Komponen / langkah metodologis utama:

- Encoder hierarkis MiT (B0-B5).
- Mix-FFN (tanpa positional encoding).
- Efficient self-attention (reduksi sequence).
- Dekoder All-MLP ringan.

## Kontribusi Utama
1. Encoder Transformer segmentasi efisien & robust.
2. Dekoder MLP sederhana.
3. Skalabilitas B0-B5.
4. Baseline luas dipakai.

## Rincian Eksperimen
ADE20K, Cityscapes, COCO-Stuff untuk mIoU; uji robustnes terhadap korupsi (Cityscapes-C).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ADE20K | mIoU | SOTA/efisien saat rilis |
| Cityscapes | mIoU | akurasi tinggi |
| Robustnes | mIoU | lebih tahan korupsi |

## Temuan Kunci
- Positional encoding tak wajib bila ada Mix-FFN.
- Dekoder ringan cukup dengan encoder kuat.
- Transformer segmentasi bisa robust.

## Keunggulan
- Efisien dan robust.
- Skalabel.
- Dekoder sederhana.

## Keterbatasan
- Varian besar tetap berat.
- Attention resolusi tinggi mahal.
- RGB-only (perlu adaptasi untuk depth).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Encoder/backbone segmentasi yang sering dijadikan cabang RGB pada model segmentasi RGB-D (mis. keluarga CMX/DFormer terkait).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [172 - 2022 - EMSANet - Segmentasi RGB-D](./172%20-%202022%20-%20EMSANet%20-%20Segmentasi%20RGB-D.md)
- [173 - 2024 - GeminiFusion - Segmentasi RGB-D](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md)
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
SegFormer menyediakan tulang punggung segmentasi Transformer yang efisien dan robust, fondasi banyak metode RGB dan RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `xie2021segformer` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 171/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
