# 065 - From Big to Small: Multi-Scale Local Planar Guidance for Monocular Depth Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 065 dari 154 |
| Kunci BibTeX | `lee2019bts` |
| Judul | From Big to Small: Multi-Scale Local Planar Guidance for Monocular Depth Estimation |
| Penulis | Lee, Jin Han; Han, Myung-Kyu; Ko, Dong Wook; Suh, Il Hong |
| Tahun | 2019 |
| Venue / Jurnal | arXiv preprint arXiv:1907.10326 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth monokular, supervised, local planar guidance, decoder, NYUv2/KITTI |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-estimasi-kedalaman)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1907.10326
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=From%20Big%20to%20Small%3A%20Multi-Scale%20Local%20Planar%20Guidance%20for%20Monocular%20Depth%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=From%20Big%20to%20Small%3A%20Multi-Scale%20Local%20Planar%20Guidance%20for%20Monocular%20Depth%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 1907.10326 |

## Ringkasan Eksekutif
Metode depth monokular tersupervisi yang memperkenalkan lapisan local planar guidance pada decoder untuk memandu fitur kembali ke resolusi penuh secara geometris.

## Abstrak (Parafrase)
BTS (From Big To Small) menambahkan lapisan Local Planar Guidance (LPG) pada beberapa tahap decoder yang secara eksplisit memodelkan bidang planar lokal untuk memandu upsampling fitur ke resolusi penuh. Ini memulihkan detail geometris lebih baik dibanding upsampling naif, mencapai SOTA supervised saat rilis di NYUv2 dan KITTI.

## Latar Belakang & Konteks
Upsampling decoder standar kehilangan detail geometri lokal, sehingga peta kedalaman kabur di batas dan permukaan miring.

## Permasalahan yang Diangkat
- Upsampling decoder standar kehilangan detail geometri.
- Batas & permukaan miring menjadi kabur.
- Fitur perlu dipandu kembali ke resolusi penuh.
- Struktur planar lokal kurang dimanfaatkan.
- Akurasi supervised perlu ditingkatkan.

## Tujuan & Pertanyaan Penelitian
- Memandu upsampling dengan bidang planar lokal.
- Memulihkan detail geometris resolusi penuh.
- Meningkatkan akurasi depth supervised.

## Tinjauan Terdahulu / Posisi Literatur
BTS mengembangkan decoder depth tersupervisi dengan panduan planar.

Karya/konsep pembanding yang relevan:

- Depth supervised (Eigen/BTS) — dasar.
- Encoder-decoder depth.
- Local planar assumption — geometri.
- Dataset NYUv2/KITTI.

## Metodologi & Arsitektur
Encoder (DenseNet/ResNeXt) mengekstrak fitur; Local Planar Guidance layers pada beberapa tahap decoder memparameterkan bidang planar lokal (koefisien) yang memandu upsampling ke resolusi penuh; loss depth tersupervisi.

Komponen / langkah metodologis utama:

- Encoder DenseNet/ResNeXt.
- Local Planar Guidance (LPG) layers.
- Parameterisasi bidang planar lokal.
- Upsampling terpandu ke resolusi penuh.
- Pelatihan supervised (ground-truth depth).
- Evaluasi NYUv2 & KITTI.

## Kontribusi Utama
1. Local Planar Guidance memandu upsampling geometris.
2. Detail geometris resolusi penuh dipulihkan.
3. SOTA supervised saat rilis.
4. Batas & permukaan lebih tajam.

## Rincian Eksperimen
Diuji pada NYUv2 dan KITTI dengan metrik depth standar, dibandingkan metode supervised sebelumnya, plus ablation LPG.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | AbsRel/RMSE | SOTA supervised saat rilis |
| KITTI | AbsRel/RMSE | SOTA/kompetitif |
| Ablation | LPG | panduan planar menyumbang gain |

## Temuan Kunci
- Panduan planar lokal memperbaiki rekonstruksi.
- Detail resolusi penuh dipulihkan.
- Batas objek lebih tajam.
- Supervised tetap kompetitif dengan LPG.

## Keunggulan
- Detail geometris tajam.
- SOTA supervised.
- Panduan planar efektif.

## Keterbatasan
- Butuh ground-truth depth (supervised).
- Encoder relatif berat.
- Asumsi planar lokal tak selalu berlaku.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
BTS menegaskan pentingnya panduan geometris pada decoder depth; melengkapi klaster Estimasi Kedalaman yang mendasari pseudo-depth RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [066 - 2021 - AdaBins - Estimasi Kedalaman](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md)
- [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)
- [068 - 2022 - MiDaS (Robust Monocular Depth) - Estimasi Kedalaman](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md)
- [069 - 2020 - PackNet - Estimasi Kedalaman](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md)
- [070 - 2021 - MonoIndoor - Estimasi Kedalaman](./070%20-%202021%20-%20MonoIndoor%20-%20Estimasi%20Kedalaman.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Estimasi Kedalaman** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Estimasi Kedalaman)
Istilah penting untuk memahami makalah ini:

- **Depth monokular** — Estimasi kedalaman dari satu citra RGB (ill-posed).
- **Supervised** — Dilatih dengan ground-truth depth.
- **Self-supervised** — Dilatih tanpa label depth via konsistensi stereo/video.
- **Disparitas** — Pergeseran piksel antar-pandangan stereo.
- **Skala metrik vs relatif** — Depth satuan nyata vs hanya urutan relatif.
- **AbsRel** — Absolute Relative error (makin kecil makin baik).
- **RMSE** — Root Mean Square Error peta depth.
- **delta<1.25** — Persentase piksel dengan error di bawah ambang.
- **Zero-shot** — Generalisasi ke dataset tak dilihat saat pelatihan.
- **Pseudo-depth** — Depth prediksi model, pengganti sensor depth.

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
BTS memperkenalkan Local Planar Guidance untuk memandu upsampling decoder secara geometris, memulihkan detail dan mencapai SOTA supervised pada depth monokular.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lee2019bts` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 065/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
