# 071 - Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 071 dari 154 |
| Kunci BibTeX | `yang2024depthanything` |
| Judul | Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data |
| Penulis | Yang, Lihe; Kang, Bingyi; Huang, Zilong; Xu, Xiaogang; Feng, Jiashi; Zhao, Hengshuang |
| Tahun | 2024 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth fondasi, data tak-berlabel, pseudo-label, zero-shot, DINOv2 |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Anything%3A%20Unleashing%20the%20Power%20of%20Large-Scale%20Unlabeled%20Data
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Depth%20Anything%3A%20Unleashing%20the%20Power%20of%20Large-Scale%20Unlabeled%20Data&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 10371--10381 |

## Ringkasan Eksekutif
Model depth monokular fondasi yang dilatih pada puluhan juta citra tak-berlabel via pseudo-labeling dan regularisasi fitur, menghasilkan depth relatif zero-shot yang sangat robust.

## Abstrak (Parafrase)
Depth Anything membangun model depth fondasi dengan memanfaatkan ~62 juta citra tak-berlabel: sebuah data engine menghasilkan pseudo-label depth (dari model guru), lalu model siswa dilatih dengan augmentasi kuat dan regularisasi fitur dari model pra-latih (DINOv2) untuk mempertahankan semantik. Hasilnya depth relatif zero-shot yang sangat robust dan menjadi basis fine-tuning metrik.

## Latar Belakang & Konteks
Skala data berlabel depth terbatas membatasi generalisasi; memperluas data via pseudo-label menjanjikan namun rawan degradasi kualitas.

## Permasalahan yang Diangkat
- Data berlabel depth terbatas membatasi generalisasi.
- Pseudo-label naif rawan menurunkan kualitas.
- Semantik fitur perlu dipertahankan.
- Robustness lintas domain diperlukan.
- Skala data harus ditingkatkan drastis.

## Tujuan & Pertanyaan Penelitian
- Memanfaatkan data tak-berlabel masif (pseudo-label).
- Mempertahankan semantik via regularisasi fitur.
- Menghasilkan depth relatif zero-shot robust.

## Tinjauan Terdahulu / Posisi Literatur
Depth Anything mengembangkan MiDaS/DPT dengan data tak-berlabel masif.

Karya/konsep pembanding yang relevan:

- MiDaS/DPT — dasar depth relatif.
- Pseudo-labeling — data engine.
- DINOv2 — regularisasi fitur semantik.
- Zero-shot depth relatif.

## Metodologi & Arsitektur
Data engine memberi pseudo-label depth pada ~62M citra tak-berlabel memakai model guru; model siswa (encoder DINOv2/ViT + decoder DPT) dilatih dengan augmentasi kuat (CutMix) dan feature alignment ke DINOv2 agar semantik terjaga; menghasilkan depth relatif; dapat di-fine-tune untuk depth metrik.

Komponen / langkah metodologis utama:

- Data engine pseudo-label 62M citra tak-berlabel.
- Encoder ViT (DINOv2) + decoder DPT.
- Augmentasi kuat (CutMix) untuk robustness.
- Feature alignment ke DINOv2 (semantik).
- Depth relatif zero-shot.
- Fine-tune untuk depth metrik.

## Kontribusi Utama
1. Model depth fondasi dari data tak-berlabel masif.
2. Pseudo-labeling + regularisasi fitur efektif.
3. Zero-shot depth relatif sangat robust.
4. Basis fine-tuning depth metrik.

## Rincian Eksperimen
Diuji zero-shot pada banyak benchmark depth (indoor & outdoor) dengan metrik depth relatif/metrik, dibandingkan MiDaS/DPT dan model lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Banyak benchmark | zero-shot | SOTA depth relatif zero-shot |
| Fine-tune metrik | AbsRel | kuat setelah fine-tune |
| Ablation | data/alignment | keduanya menyumbang gain |

## Temuan Kunci
- Data tak-berlabel masif meningkatkan generalisasi.
- Regularisasi fitur menjaga semantik.
- Augmentasi kuat penting untuk robustness.
- Membuka pseudo-depth murah & berkualitas.

## Keunggulan
- Depth fondasi robust.
- Zero-shot kuat.
- Basis fine-tune metrik.

## Keterbatasan
- Depth relatif (metrik butuh fine-tune).
- Pelatihan skala besar mahal.
- Bergantung kualitas pseudo-label guru.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Depth Anything adalah model depth termutakhir yang membuat RGB->pseudo-RGB-D murah dan berkualitas — sangat relevan bagi masa depan YOLO+RGB-D tanpa sensor depth.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
- [066 - 2021 - AdaBins - Estimasi Kedalaman](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md)
- [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)
- [068 - 2022 - MiDaS (Robust Monocular Depth) - Estimasi Kedalaman](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md)
- [069 - 2020 - PackNet - Estimasi Kedalaman](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md)

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
Depth Anything melatih model depth fondasi pada ~62 juta citra tak-berlabel via pseudo-labeling dan regularisasi fitur DINOv2, menghasilkan depth relatif zero-shot yang sangat robust.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yang2024depthanything` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 071/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
