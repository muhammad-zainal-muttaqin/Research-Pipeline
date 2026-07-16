# 068 - Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 068 dari 154 |
| Kunci BibTeX | `ranftl2022midas` |
| Judul | Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer |
| Penulis | Ranftl, Ren{\'e |
| Tahun | 2022 |
| Venue / Jurnal | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth monokular, multi-dataset, scale-shift invariant, zero-shot, generalisasi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Towards%20Robust%20Monocular%20Depth%20Estimation%3A%20Mixing%20Datasets%20for%20Zero-Shot%20Cross-Dataset%20Transfer
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Towards%20Robust%20Monocular%20Depth%20Estimation%3A%20Mixing%20Datasets%20for%20Zero-Shot%20Cross-Dataset%20Transfer&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 44 |
| Nomor | 3 |
| Halaman | 1623--1637 |

## Ringkasan Eksekutif
Melatih depth monokular yang robust dengan mencampur banyak dataset memakai scale-and-shift invariant loss untuk transfer zero-shot lintas dataset.

## Abstrak (Parafrase)
MiDaS mengatasi keterbatasan generalisasi model depth single-dataset dengan mencampur banyak dataset heterogen (berbeda skala, sensor, anotasi). Kuncinya adalah scale-and-shift invariant loss yang menyelaraskan prediksi ke ground-truth tanpa mengharuskan skala absolut sama, memungkinkan pelatihan gabungan. Hasilnya generalisasi depth relatif zero-shot terbaik saat rilis, dipakai luas sebagai penyedia pseudo-depth.

## Latar Belakang & Konteks
Model depth yang dilatih pada satu dataset tidak general ke domain lain (indoor vs outdoor, sensor berbeda), sedangkan menggabungkan dataset terhambat perbedaan skala/anotasi.

## Permasalahan yang Diangkat
- Model single-dataset tak general lintas domain.
- Dataset depth berbeda skala/sensor/anotasi.
- Penggabungan naif terhambat perbedaan skala.
- Skala absolut sulit diselaraskan lintas dataset.
- Generalisasi zero-shot diperlukan.

## Tujuan & Pertanyaan Penelitian
- Melatih depth robust lintas banyak dataset.
- Menyelaraskan prediksi via scale-shift invariant loss.
- Mencapai generalisasi depth relatif zero-shot.

## Tinjauan Terdahulu / Posisi Literatur
MiDaS mengembangkan pelatihan multi-dataset untuk generalisasi depth.

Karya/konsep pembanding yang relevan:

- Depth monokular (Eigen/DPT) — dasar.
- Scale-and-shift invariant loss.
- Pencampuran multi-dataset.
- Zero-shot transfer.

## Metodologi & Arsitektur
Beberapa dataset depth heterogen digabung; scale-and-shift invariant loss menyelaraskan prediksi (menormalkan skala & shift) sebelum menghitung galat; strategi pencampuran menyeimbangkan dataset; backbone (ResNeXt/ViT/DPT) memprediksi depth relatif.

Komponen / langkah metodologis utama:

- Scale-and-shift invariant loss.
- Strategi pencampuran multi-dataset.
- Prediksi depth relatif (bukan metrik).
- Backbone fleksibel (CNN/DPT).
- Pelatihan gabungan lintas domain.
- Zero-shot cross-dataset transfer.

## Kontribusi Utama
1. Pelatihan multi-dataset untuk generalisasi.
2. Scale-shift invariant loss memungkinkan penggabungan.
3. Generalisasi depth relatif zero-shot terbaik saat rilis.
4. Dipakai luas sebagai penyedia pseudo-depth.

## Rincian Eksperimen
Diuji zero-shot pada 6+ dataset yang tak dilihat saat latih dengan metrik depth relatif, dibandingkan model single-dataset.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| 6+ dataset zero-shot | ranking/AbsRel | generalisasi terbaik saat rilis |
| Cross-dataset | transfer | robust lintas domain |
| Ablation | scale-shift loss | memungkinkan penggabungan dataset |

## Temuan Kunci
- Pencampuran multi-dataset kunci generalisasi.
- Scale-shift invariance memungkinkan penggabungan.
- Depth relatif general lintas domain.
- Fondasi penyedia pseudo-depth serbaguna.

## Keunggulan
- Generalisasi zero-shot kuat.
- Robust lintas domain.
- Dipakai luas.

## Keterbatasan
- Menghasilkan depth relatif (bukan metrik).
- Skala absolut butuh kalibrasi.
- Kualitas bergantung backbone.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
MiDaS adalah fondasi model depth serbaguna yang memungkinkan RGB->pseudo-RGB-D murah — sangat relevan bagi tema RGB+Depth tanpa sensor dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
- [066 - 2021 - AdaBins - Estimasi Kedalaman](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md)
- [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)
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
MiDaS melatih depth monokular robust dengan mencampur banyak dataset via scale-and-shift invariant loss, mencapai generalisasi zero-shot terbaik dan menjadi penyedia pseudo-depth serbaguna.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ranftl2022midas` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 068/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
