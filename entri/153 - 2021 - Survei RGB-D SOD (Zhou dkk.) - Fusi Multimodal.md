# 153 - RGB-D Salient Object Detection: A Survey

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 153 dari 154 |
| Kunci BibTeX | `zhou2021rgbdsurvey` |
| Judul | RGB-D Salient Object Detection: A Survey |
| Penulis | Zhou, Tao; Fan, Deng-Ping; Cheng, Ming-Ming; Shen, Jianbing; Shao, Ling |
| Tahun | 2021 |
| Venue / Jurnal | Computational Visual Media |
| Tema klaster | Fusi Multimodal |
| Kata kunci | survei, RGB-D SOD, fusi, dataset, metrik |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-fusi-multimodal)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RGB-D%20Salient%20Object%20Detection%3A%20A%20Survey
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RGB-D%20Salient%20Object%20Detection%3A%20A%20Survey&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 7 |
| Nomor | 1 |
| Halaman | 37--69 |

## Ringkasan Eksekutif
Tinjauan komprehensif RGB-D salient object detection: model, dataset, metrik, dan analisis strategi fusi — peta kanonik bidang RGB-D SOD.

## Abstrak (Parafrase)
Zhou dkk. meninjau secara menyeluruh RGB-D salient object detection: mengklasifikasikan strategi fusi (early/middle/late), meninjau model, dataset, dan metrik (S-measure, E-measure, F-measure, MAE), serta membahas tantangan. Ini adalah peta kanonik bidang RGB-D SOD yang berguna untuk mengklasifikasikan metode fusi.

## Latar Belakang & Konteks
Bidang RGB-D SOD berkembang cepat dengan banyak model dan strategi fusi; dibutuhkan sintesis terstruktur.

## Permasalahan yang Diangkat
- Bidang RGB-D SOD berkembang cepat.
- Strategi fusi (early/middle/late) beragam.
- Model & dataset banyak.
- Metrik evaluasi perlu dirangkum.
- Perlu peta bidang koheren.

## Tujuan & Pertanyaan Penelitian
- Mengklasifikasikan strategi fusi RGB-D SOD.
- Meninjau model, dataset, dan metrik.
- Membahas tantangan dan arah.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini mengagregasi metode & benchmark RGB-D SOD.

Karya/konsep pembanding yang relevan:

- RGB-D SOD models (BBS-Net/JL-DCF/dll.).
- Strategi fusi (early/middle/late).
- Dataset RGB-D SOD.
- Metrik (S/E/F-measure, MAE).

## Metodologi & Arsitektur
Metodologi survei: taksonomi strategi fusi (kapan modal digabung), tinjauan model dan dataset, ikhtisar metrik, dan analisis tantangan (kualitas kedalaman, efisiensi).

Komponen / langkah metodologis utama:

- Taksonomi strategi fusi (early/middle/late).
- Tinjauan model RGB-D SOD.
- Ikhtisar dataset RGB-D SOD.
- Ikhtisar metrik (S/E/F-measure, MAE).
- Analisis tantangan (kualitas kedalaman).
- Sintesis literatur.

## Kontribusi Utama
1. Peta kanonik bidang RGB-D SOD.
2. Taksonomi strategi fusi yang jelas.
3. Ikhtisar model/dataset/metrik.
4. Rujukan klasifikasi metode fusi.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa kompilasi & analisis komparatif metode RGB-D SOD dari literatur.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Metode RGB-D SOD | S/E/F, MAE | kompilasi komparatif |
| Strategi fusi | taksonomi | early/middle/late |
| Dataset | ikhtisar | NJU2K/NLPR/SIP/dll. |

## Temuan Kunci
- Strategi fusi menentukan kinerja RGB-D SOD.
- Kualitas kedalaman tantangan utama.
- Metrik terstandar memudahkan perbandingan.
- Middle fusion sering unggul.

## Keunggulan
- Peta kanonik RGB-D SOD.
- Taksonomi fusi jelas.
- Rujukan bidang.

## Keterbatasan
- Bersifat survei.
- Fokus SOD.
- Cepat usang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini menaungi seluruh klaster RGB-D SOD dalam tinjauan dan menyediakan kerangka klasifikasi fusi (early/middle/late) yang dipakai luas.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fusi Multimodal** yang baik dibaca berdampingan:

- [147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)
- [148 - 2017 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)
- [149 - 2018 - CBAM - Fusi Multimodal](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md)
- [150 - 2021 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)
- [154 - 2022 - Survei Dataset RGB-D (Lopes dkk.) - Fusi Multimodal](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fusi Multimodal** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Fusi Multimodal)
Istilah penting untuk memahami makalah ini:

- **Multimodal** — Menggabungkan >1 modalitas data.
- **Backbone** — Jaringan ekstraksi fitur fundamental.
- **Residual/skip** — Jalan pintas memudahkan pelatihan jaringan dalam.
- **Attention (CBAM/SE)** — Modul penimbang fitur kanal-spasial.
- **PointNet** — Jaringan pemroses point cloud mentah.
- **Early/late/deep fusion** — Tingkat penggabungan modalitas.
- **Survei** — Sintesis literatur lintas metode.
- **Generalisasi lintas-sensor** — Ketahanan terhadap kombinasi sensor.
- **Kalibrasi/penyelarasan** — Penyelarasan spasial-temporal antar-modal.
- **Representasi bersama** — Ruang fitur gabungan lintas-modal.

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
Zhou dkk. meninjau RGB-D salient object detection secara komprehensif, mengklasifikasikan strategi fusi (early/middle/late) dan merangkum model/dataset/metrik, menjadi peta kanonik bidang.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhou2021rgbdsurvey` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 153/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
