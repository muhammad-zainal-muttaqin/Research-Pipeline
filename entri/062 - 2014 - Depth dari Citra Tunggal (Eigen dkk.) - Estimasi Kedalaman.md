# 062 - Depth Map Prediction from a Single Image Using a Multi-Scale Deep Network

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 062 dari 154 |
| Kunci BibTeX | `eigen2014depth` |
| Judul | Depth Map Prediction from a Single Image Using a Multi-Scale Deep Network |
| Penulis | Eigen, David; Puhrsch, Christian; Fergus, Rob |
| Tahun | 2014 |
| Venue / Jurnal | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth monokular, multi-scale CNN, scale-invariant loss, pelopor, NYUv2 |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Map%20Prediction%20from%20a%20Single%20Image%20Using%20a%20Multi-Scale%20Deep%20Network
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Depth%20Map%20Prediction%20from%20a%20Single%20Image%20Using%20a%20Multi-Scale%20Deep%20Network&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 2366--2374 |

## Ringkasan Eksekutif
Karya pelopor yang memprediksi peta kedalaman dari satu citra RGB memakai dua jaringan skala (global kasar + lokal halus), membuka bidang depth monokular berbasis deep learning.

## Abstrak (Parafrase)
Eigen dkk. mengusulkan pendekatan CNN pertama yang efektif untuk estimasi kedalaman monokular: jaringan skala-global memprediksi struktur kedalaman kasar seluruh citra, lalu jaringan skala-lokal memperhalusnya. Scale-invariant loss menangani ambiguitas skala global. Karya ini menetapkan baseline dan memicu bidang depth monokular deep learning.

## Latar Belakang & Konteks
Estimasi kedalaman dari satu citra bersifat ill-posed (banyak scene 3D memberi citra 2D sama) dan sebelumnya bergantung isyarat manual/asumsi geometris yang rapuh.

## Permasalahan yang Diangkat
- Depth monokular ill-posed (ambigu secara inheren).
- Metode sebelumnya bergantung isyarat manual.
- Skala global sulit ditentukan dari satu citra.
- Struktur kasar & detail halus perlu keduanya.
- Belum ada pendekatan CNN efektif.

## Tujuan & Pertanyaan Penelitian
- Memprediksi kedalaman dari satu citra via CNN.
- Menangani struktur kasar dan detail halus.
- Mengatasi ambiguitas skala (scale-invariant loss).

## Tinjauan Terdahulu / Posisi Literatur
Karya ini pelopor pendekatan CNN untuk depth monokular.

Karya/konsep pembanding yang relevan:

- Metode geometris/isyarat manual — pendahulu.
- CNN — arsitektur baru untuk depth.
- Scale-invariant loss — penanganan skala.
- Dataset NYUv2/KITTI.

## Metodologi & Arsitektur
Jaringan skala-global (coarse) memprediksi kedalaman kasar seluruh citra; jaringan skala-lokal (fine) memperhalus detail; pelatihan memakai scale-invariant loss yang tidak menghukum kesalahan skala global secara berlebihan.

Komponen / langkah metodologis utama:

- Jaringan coarse (global) untuk struktur kasar.
- Jaringan fine (local) untuk detail halus.
- Scale-invariant loss.
- Prediksi peta kedalaman padat.
- Pelatihan supervised (ground-truth depth).
- Evaluasi NYUv2 & KITTI.

## Kontribusi Utama
1. Pendekatan CNN pertama yang efektif untuk depth monokular.
2. Arsitektur coarse-to-fine dua-skala.
3. Scale-invariant loss menangani ambiguitas.
4. Menetapkan baseline dan memicu bidang.

## Rincian Eksperimen
Diuji pada NYUv2 (indoor) dan KITTI (outdoor) dengan metrik depth (AbsRel, RMSE, akurasi ambang), menetapkan baseline deep learning.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | AbsRel/RMSE | baseline depth monokular DL |
| KITTI | AbsRel/RMSE | baseline outdoor |
| Ablation | coarse+fine | dua-skala meningkatkan akurasi |

## Temuan Kunci
- CNN dapat memprediksi kedalaman dari satu citra.
- Coarse-to-fine menangkap struktur & detail.
- Scale-invariant loss penting untuk skala global.
- Membuka bidang depth monokular DL.

## Keunggulan
- Pelopor & berpengaruh.
- Coarse-to-fine efektif.
- Menangani ambiguitas skala.

## Keterbatasan
- Akurasi rendah menurut standar modern.
- Butuh ground-truth depth (supervised).
- Detail halus terbatas.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini adalah akar klaster Estimasi Kedalaman dalam tinjauan; memahami depth monokular penting bagi 'pseudo-depth' yang memungkinkan RGB->RGB-D tanpa sensor.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
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
Eigen dkk. mempelopori estimasi kedalaman monokular berbasis CNN dengan arsitektur coarse-to-fine dan scale-invariant loss, membuka bidang yang mendasari pseudo-depth untuk pipeline RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `eigen2014depth` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 062/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
