# 100 - Multispectral Pedestrian Detection: Benchmark Dataset and Baseline

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 100 dari 154 |
| Kunci BibTeX | `hwang2015kaist` |
| Judul | Multispectral Pedestrian Detection: Benchmark Dataset and Baseline |
| Penulis | Hwang, Soonmin; Park, Jaesik; Kim, Namil; Choi, Yukyung; Kweon, In So |
| Tahun | 2015 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pedestrian RGB-T |
| Kata kunci | RGB-T, dataset, thermal, siang-malam, benchmark |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pedestrian-rgb-t)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Multispectral%20Pedestrian%20Detection%3A%20Benchmark%20Dataset%20and%20Baseline
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Multispectral%20Pedestrian%20Detection%3A%20Benchmark%20Dataset%20and%20Baseline&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1037--1045 |

## Ringkasan Eksekutif
Dataset pelopor deteksi pejalan multispektral (RGB + thermal terkalibrasi) dan baseline yang memungkinkan deteksi siang-malam, memicu riset fusi RGB-T.

## Abstrak (Parafrase)
KAIST memperkenalkan dataset deteksi pejalan multispektral: pasangan citra RGB (tampak) dan LWIR (thermal) yang terselaraskan spasial-temporal, direkam siang dan malam. Baseline ACF multispektral menunjukkan komplementaritas kedua modal. Dataset ini menjadi benchmark standar dan memicu gelombang riset fusi RGB-thermal.

## Latar Belakang & Konteks
Deteksi pejalan berbasis RGB gagal pada malam hari/cahaya buruk, padahal thermal andal dalam gelap; namun belum ada benchmark RGB-thermal berpasangan yang terkalibrasi.

## Permasalahan yang Diangkat
- Deteksi pejalan RGB gagal pada malam/cahaya buruk.
- Thermal andal gelap namun kurang tekstur.
- Belum ada benchmark RGB-thermal berpasangan.
- Penyelarasan RGB-thermal sulit.
- Riset fusi multispektral terhambat data.

## Tujuan & Pertanyaan Penelitian
- Menyediakan dataset RGB-thermal berpasangan.
- Menyediakan baseline multispektral.
- Memungkinkan deteksi pejalan siang-malam.

## Tinjauan Terdahulu / Posisi Literatur
KAIST menyediakan benchmark RGB-thermal berpasangan.

Karya/konsep pembanding yang relevan:

- Deteksi pejalan RGB (Caltech) — pembanding.
- Thermal/LWIR imaging.
- ACF — baseline detektor.
- Kalibrasi RGB-thermal.

## Metodologi & Arsitektur
Sistem kamera RGB+LWIR terselaraskan (beam splitter) merekam pasangan citra siang dan malam; anotasi kotak pejalan disediakan; baseline ACF multispektral menggabungkan fitur RGB dan thermal; benchmark dengan protokol evaluasi.

Komponen / langkah metodologis utama:

- Dataset RGB+LWIR terselaraskan (siang & malam).
- Anotasi kotak pejalan.
- Baseline ACF multispektral.
- Protokol evaluasi (miss rate).
- Kalibrasi spasial-temporal.
- Benchmark standar.

## Kontribusi Utama
1. Dataset RGB-thermal berpasangan pertama berskala.
2. Baseline multispektral menunjukkan komplementaritas.
3. Memungkinkan deteksi siang-malam.
4. Memicu riset fusi RGB-T.

## Rincian Eksperimen
Menyediakan benchmark KAIST dengan metrik miss rate; baseline dan banyak metode berikutnya dievaluasi di sini.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KAIST | miss rate | benchmark standar RGB-T |
| Baseline ACF | MR | komplementaritas RGB+thermal |
| Siang/malam | robustness | deteksi lintas kondisi cahaya |

## Temuan Kunci
- Thermal melengkapi RGB pada gelap.
- Fusi multispektral menurunkan miss rate.
- Penyelarasan berpasangan memungkinkan fusi.
- Benchmark memacu riset.

## Keunggulan
- Dataset fondasi RGB-T.
- Memungkinkan siang-malam.
- Memicu riset fusi.

## Keterbatasan
- Beberapa misalignment/anotasi perlu perbaikan (versi bersih menyusul).
- Domain khusus (pejalan).
- Thermal kurang tekstur.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
KAIST adalah dataset fondasi klaster Pedestrian RGB-T dalam tinjauan; menegaskan komplementaritas modal (paralel dengan RGB+Depth) dan memicu metode fusi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pedestrian RGB-T** yang baik dibaca berdampingan:

- [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md)
- [102 - 2020 - MBNet - Pedestrian RGB-T](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)
- [103 - 2021 - GAFF - Pedestrian RGB-T](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md)
- [104 - 2020 - Cyclic Fuse-and-Refine (CFR) - Pedestrian RGB-T](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md)
- [105 - 2022 - CMPD (Uncertainty-Guided Cross-Modal) - Pedestrian RGB-T](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md)
- [106 - 2021 - RGB-D Fusion for Detection (Farahnakian & Heikkonen) - Pedestrian RGB-T](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pedestrian RGB-T** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pedestrian RGB-T)
Istilah penting untuk memahami makalah ini:

- **Multispektral** — Citra beberapa pita (RGB + thermal).
- **RGB-T** — Pasangan citra warna dan termal.
- **Thermal/LWIR** — Inframerah panjang; andal saat gelap.
- **Illumination-aware** — Bobot modal menyesuaikan kondisi cahaya.
- **Modality imbalance** — Ketimpangan keandalan antar-modal.
- **Miss rate (MR)** — Metrik deteksi pejalan (makin kecil makin baik).
- **KAIST** — Dataset pejalan multispektral standar.
- **CVC-14** — Dataset pejalan siang-malam RGB-thermal.
- **Feature alignment** — Penyelarasan spasial fitur antar-modal.
- **Cross-modal attention** — Attention pemandu fusi RGB-thermal.

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
KAIST memperkenalkan dataset pejalan multispektral RGB-thermal berpasangan siang-malam dengan baseline, menjadi benchmark fondasi yang memicu riset fusi RGB-T.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `hwang2015kaist` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 100/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
