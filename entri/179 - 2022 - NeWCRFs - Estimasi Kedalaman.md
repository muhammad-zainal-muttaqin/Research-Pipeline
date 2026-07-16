# 179 - Neural Window Fully-Connected CRFs for Monocular Depth Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 179 dari 191 |
| Kunci BibTeX | `yuan2022newcrfs` |
| Judul | Neural Window Fully-Connected CRFs for Monocular Depth Estimation |
| Penulis | Yuan, Weihao; Gu, Xiaodong; Dai, Zuozhuo; Zhu, Siyu; Tan, Ping |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | monocular depth, neural window CRF, attention, supervised |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2203.01502
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Neural%20Window%20Fully-Connected%20CRFs%20for%20Monocular%20Depth%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Neural%20Window%20Fully-Connected%20CRFs%20for%20Monocular%20Depth%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2203.01502 |

## Ringkasan Eksekutif
NeWCRFs memadukan Conditional Random Fields (CRF) dengan Transformer berjendela untuk estimasi kedalaman monokular tersupervisi, menghitung energi CRF dalam jendela lokal via mekanisme mirip attention untuk hasil yang tajam dan akurat.

## Abstrak (Parafrase)
Penulis menghidupkan kembali CRF dalam kerangka deep learning modern. Alih-alih CRF global mahal, NeWCRFs menghitung CRF fully-connected dalam jendela lokal, diimplementasikan sebagai neural window attention. Dengan struktur multiskala top-down, model menghasilkan depth halus namun tajam pada batas, mencapai SOTA pada KITTI dan NYU v2 saat rilis.

## Latar Belakang & Konteks
CRF klasik memperbaiki batas prediksi dense tetapi mahal secara global. Menyatukannya dengan attention berjendela membuatnya efisien dan dapat dilatih end-to-end.

## Permasalahan yang Diangkat
- CRF global mahal.
- Batas depth sering kabur.
- Menyatukan CRF dengan deep net secara efisien.

## Tujuan & Pertanyaan Penelitian
- Menghitung CRF efisien via jendela lokal.
- Menghasilkan depth tajam dan akurat.
- Melatih end-to-end dengan attention.

## Tinjauan Terdahulu / Posisi Literatur
Berpijak pada BTS/AdaBins/DPT dan tradisi CRF untuk prediksi dense; kebaruan pada neural window CRF.

Karya/konsep pembanding yang relevan:

- BTS - local planar guidance.
- AdaBins - metric bins.
- DPT - Transformer dense.
- CRF klasik - penghalusan batas.

## Metodologi & Arsitektur
Encoder (mis. Swin) menghasilkan fitur multiskala; modul neural window fully-connected CRF menghitung energi pasangan dalam jendela via attention; dekoder top-down memadukan skala untuk depth akhir.

Komponen / langkah metodologis utama:

- Neural window fully-connected CRF.
- Implementasi mirip window attention.
- Struktur multiskala top-down.
- Encoder Transformer (Swin).

## Kontribusi Utama
1. CRF berjendela yang efisien dan dapat dilatih.
2. Depth tajam pada batas.
3. SOTA KITTI/NYU saat rilis.
4. Jembatan CRF-attention.

## Rincian Eksperimen
KITTI (outdoor) dan NYU Depth v2 (indoor) untuk metrik depth tersupervisi (RMSE/AbsRel/delta).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI | RMSE | SOTA saat rilis |
| NYU v2 | AbsRel/delta | akurat, batas tajam |
| Ablation CRF | metrik | CRF berjendela menaikkan hasil |

## Temuan Kunci
- CRF lokal efektif menajamkan batas depth.
- Attention berjendela mewujudkan CRF efisien.
- Multiskala penting untuk akurasi.

## Keunggulan
- Batas tajam.
- Akurasi tinggi.
- Efisien relatif CRF global.

## Keterbatasan
- Tersupervisi (butuh label depth).
- Backbone Transformer relatif berat.
- Fokus depth (bukan multitugas).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Estimasi depth akurat mendukung konstruksi input RGB-D dan lokalisasi 3D pada aplikasi berbasis kamera.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [175 - 2024 - Depth Anything V2 - Estimasi Kedalaman](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)
- [176 - 2023 - ZoeDepth - Estimasi Kedalaman](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)
- [177 - 2023 - Metric3D - Estimasi Kedalaman](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md)
- [178 - 2024 - Marigold - Estimasi Kedalaman](./178%20-%202024%20-%20Marigold%20-%20Estimasi%20Kedalaman.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Estimasi Kedalaman** dalam peta tinjauan (17 klaster, 191 entri total).
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
NeWCRFs menyatukan CRF dan attention berjendela untuk depth monokular yang tajam dan akurat, menyegarkan peran CRF di era deep learning.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yuan2022newcrfs` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 179/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
