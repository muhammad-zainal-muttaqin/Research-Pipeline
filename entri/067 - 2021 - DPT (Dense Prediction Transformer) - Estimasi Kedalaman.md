# 067 - Vision Transformers for Dense Prediction

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 067 dari 154 |
| Kunci BibTeX | `ranftl2021dpt` |
| Judul | Vision Transformers for Dense Prediction |
| Penulis | Ranftl, Ren{\'e |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth, Transformer, dense prediction, ViT backbone, zero-shot |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Vision%20Transformers%20for%20Dense%20Prediction
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Vision%20Transformers%20for%20Dense%20Prediction&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 12179--12188 |

## Ringkasan Eksekutif
Backbone Vision Transformer untuk prediksi padat (kedalaman, segmentasi) yang merakit token menjadi representasi mirip-citra multi-skala, unggul terutama pada depth relatif.

## Abstrak (Parafrase)
DPT (Dense Prediction Transformer) memakai ViT sebagai encoder untuk prediksi padat: token dari berbagai lapisan Transformer dirakit kembali (reassemble) menjadi peta fitur mirip-citra pada beberapa resolusi, lalu difusikan oleh decoder konvolusi. Karena attention global di setiap tahap, DPT menjaga resolusi/konteks lebih baik dari CNN, mencapai SOTA depth monokular dan segmentasi.

## Latar Belakang & Konteks
Konvolusi kehilangan resolusi dan konteks global saat downsampling, membatasi prediksi padat; ViT menawarkan konteks global namun perlu diadaptasi untuk output padat.

## Permasalahan yang Diangkat
- Konvolusi kehilangan resolusi/konteks global.
- Downsampling merusak detail prediksi padat.
- ViT menghasilkan token, bukan peta padat.
- Perlu merakit token ke representasi citra.
- Konteks global penting untuk depth/segmentasi.

## Tujuan & Pertanyaan Penelitian
- Mengadaptasi ViT untuk prediksi padat.
- Merakit token menjadi fitur multi-skala.
- Meningkatkan akurasi depth/segmentasi.

## Tinjauan Terdahulu / Posisi Literatur
DPT mengadaptasi ViT untuk dense prediction (depth, segmentasi).

Karya/konsep pembanding yang relevan:

- ViT — backbone Transformer.
- Encoder-decoder dense prediction.
- Reassemble tokens — perakitan fitur.
- MiDaS — pelatihan multi-dataset (terkait).

## Metodologi & Arsitektur
Encoder ViT memproses token patch; token dari beberapa lapisan di-reassemble menjadi peta fitur mirip-citra pada resolusi berbeda; decoder konvolusi memfusikan dan mengupsample; head menghasilkan depth/segmentasi. Dilatih pada data besar (mirip MiDaS) untuk zero-shot.

Komponen / langkah metodologis utama:

- Encoder ViT (token patch).
- Reassemble tokens menjadi fitur multi-skala.
- Decoder konvolusi fusi + upsample.
- Head depth/segmentasi.
- Pelatihan multi-dataset (zero-shot depth).
- Konteks global di tiap tahap.

## Kontribusi Utama
1. Backbone Transformer untuk prediksi padat.
2. Reassemble tokens menjaga resolusi/konteks.
3. SOTA depth monokular & segmentasi saat rilis.
4. Kuat untuk depth relatif zero-shot.

## Rincian Eksperimen
Diuji pada depth monokular (termasuk zero-shot) dan segmentasi (ADE20K) dengan metrik terkait, dibandingkan CNN state-of-the-art.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Depth monokular | AbsRel/rank | SOTA, unggul zero-shot relatif |
| ADE20K | mIoU | SOTA segmentasi saat rilis |
| Zero-shot | generalisasi | depth relatif kuat lintas dataset |

## Temuan Kunci
- ViT sebagai backbone dense prediction efektif.
- Konteks global di tiap tahap meningkatkan akurasi.
- Reassemble tokens penting untuk resolusi.
- Kuat untuk depth relatif zero-shot.

## Keunggulan
- Backbone Transformer kuat.
- SOTA depth & segmentasi.
- Generalisasi zero-shot.

## Keterbatasan
- Transformer mahal komputasi.
- Butuh data pra-latih besar.
- Depth metrik butuh kalibrasi tambahan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DPT adalah backbone kunci untuk depth relatif (dipakai MiDaS/Depth Anything); relevan bagi penyediaan pseudo-depth berkualitas untuk RGB-D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
- [066 - 2021 - AdaBins - Estimasi Kedalaman](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md)
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
DPT mengadaptasi ViT untuk prediksi padat dengan merakit token menjadi fitur multi-skala, mencapai SOTA depth monokular dan segmentasi serta kuat pada depth relatif zero-shot.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ranftl2021dpt` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 067/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
