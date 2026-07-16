# 166 - Accurate RGB-D Salient Object Detection via Collaborative Learning

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 166 dari 191 |
| Kunci BibTeX | `ji2020conet` |
| Judul | Accurate RGB-D Salient Object Detection via Collaborative Learning |
| Penulis | Ji, Wei; Li, Jingjing; Zhang, Miao; Piao, Yongri; Lu, Huchuan |
| Tahun | 2020 |
| Venue / Jurnal | European Conference on Computer Vision (ECCV) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, collaborative learning, edge, depth |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-sod)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Accurate%20RGB-D%20Salient%20Object%20Detection%20via%20Collaborative%20Learning
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Accurate%20RGB-D%20Salient%20Object%20Detection%20via%20Collaborative%20Learning&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
CoNet mendeteksi objek salien RGB-D melalui collaborative learning yang membagi tugas menjadi cabang edge, saliency, dan depth yang saling membantu, sehingga depth hanya dipakai sebagai penunjang saat pelatihan.

## Abstrak (Parafrase)
Penulis mengusulkan kerangka pembelajaran kolaboratif dengan tiga cabang - knowledge collector untuk saliency, edge, dan depth - yang berbagi fitur. Depth diperlakukan sebagai sinyal pembelajaran pendukung sehingga saat inferensi model dapat lebih robust terhadap depth berkualitas rendah. Pendekatan ini mencapai akurasi tinggi pada benchmark RGB-D SOD.

## Latar Belakang & Konteks
Fusi RGB-D untuk SOD rentan pada depth berderau. Alih-alih fusi langsung, CoNet memakai depth sebagai penopang pembelajaran.

## Permasalahan yang Diangkat
- Depth berkualitas rendah merusak fusi langsung.
- Batas objek salien sering kabur.
- Perlu pemanfaatan depth yang robust.

## Tujuan & Pertanyaan Penelitian
- Memanfaatkan depth secara kolaboratif, bukan fusi naif.
- Mempertajam batas objek salien.
- Meningkatkan robustnes terhadap depth buruk.

## Tinjauan Terdahulu / Posisi Literatur
Berbeda dari fusi dua-aliran (JL-DCF, BBS-Net) dengan menekankan pembagian tugas kolaboratif dan peran edge.

Karya/konsep pembanding yang relevan:

- BBS-Net - strategi backbone bercabang.
- JL-DCF - joint learning densely-cooperative.
- Edge-aware SOD - pemanfaatan tepi.
- D3Net - penyaringan depth.

## Metodologi & Arsitektur
Cabang bersama mengekstrak fitur; collaborators memprediksi saliency, edge, dan depth; hasil edge dan depth memandu penyempurnaan peta saliency melalui interaksi fitur.

Komponen / langkah metodologis utama:

- Tiga cabang: saliency, edge, depth.
- Berbagi backbone dan interaksi fitur.
- Depth sebagai supervisi pendukung.
- Panduan tepi untuk batas tajam.

## Kontribusi Utama
1. Kerangka collaborative learning RGB-D SOD.
2. Pemakaian depth yang robust.
3. Peningkatan ketajaman batas.
4. Hasil kompetitif pada banyak dataset.

## Rincian Eksperimen
Benchmark RGB-D SOD standar (NJU2K, NLPR, STERE, SIP, DES) dengan metrik S-measure, F-measure, E-measure, MAE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S-measure/MAE | kompetitif dengan SOTA saat rilis |
| SIP/STERE | F/E-measure | batas objek lebih tajam |
| Ablation depth | metrik | depth kolaboratif > fusi naif |

## Temuan Kunci
- Depth sebagai penunjang lebih robust dari fusi langsung.
- Edge meningkatkan kualitas batas.
- Pembelajaran multitugas saling menguatkan.

## Keunggulan
- Robust terhadap depth buruk.
- Batas tajam.
- Multitugas efisien.

## Keterbatasan
- Kompleksitas pelatihan multitugas.
- Bergantung kualitas anotasi edge.
- Skema kolaborasi perlu penyetelan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Memberi strategi memanfaatkan depth secara aman pada tugas RGB-D, relevan untuk fusi kedalaman yang tahan-derau.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md)
- [168 - 2021 - SPNet - RGB-D SOD](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md)
- [169 - 2023 - CAVER - RGB-D SOD](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md)
- [170 - 2022 - MobileSal - RGB-D SOD](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SOD)
Istilah penting untuk memahami makalah ini:

- **SOD** — Salient Object Detection; menyorot objek paling menonjol.
- **Peta kedalaman** — Citra yang tiap pikselnya menyatakan jarak ke kamera.
- **Fusi lintas-modal** — Penggabungan fitur RGB dan depth.
- **Early/middle/late fusion** — Fusi di input, fitur tengah, atau keputusan akhir.
- **Attention lintas-modal** — Membobot kontribusi RGB vs depth secara adaptif.
- **S-measure** — Structure-measure; kemiripan struktur peta saliency.
- **E-measure** — Enhanced-alignment measure; kesejajaran piksel-global.
- **F-measure** — Harmonik precision-recall pada peta saliency.
- **MAE** — Mean Absolute Error peta saliency vs ground truth.
- **Depth berkualitas rendah** — Depth berderau yang dapat merusak fusi.
- **Backbone Transformer** — Encoder attention (mis. Swin) untuk konteks global.

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
CoNet menawarkan pemanfaatan depth kolaboratif yang robust untuk RGB-D SOD, alternatif menarik atas fusi dua-aliran.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ji2020conet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 166/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
