# 043 - SwinNet: Swin Transformer Drives Edge-Aware RGB-D and RGB-T Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 043 dari 154 |
| Kunci BibTeX | `liu2021swinnet` |
| Judul | SwinNet: Swin Transformer Drives Edge-Aware RGB-D and RGB-T Salient Object Detection |
| Penulis | Liu, Zhengyi; Tan, Yacheng; He, Qian; Xiao, Yun |
| Tahun | 2022 |
| Venue / Jurnal | IEEE Transactions on Circuits and Systems for Video Technology |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, RGB-T SOD, Swin Transformer, edge-aware, cross-modal |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=SwinNet%3A%20Swin%20Transformer%20Drives%20Edge-Aware%20RGB-D%20and%20RGB-T%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=SwinNet%3A%20Swin%20Transformer%20Drives%20Edge-Aware%20RGB-D%20and%20RGB-T%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 32 |
| Nomor | 7 |
| Halaman | 4486--4497 |

## Ringkasan Eksekutif
Kerangka SOD yang memakai backbone Swin Transformer dengan modul edge-aware dan fusi lintas-modal untuk RGB-D dan RGB-T, menyatukan dua modalitas kedua dalam satu desain.

## Abstrak (Parafrase)
SwinNet memakai backbone Swin Transformer dua-aliran untuk menangkap konteks global, dengan modul spatial alignment dan channel re-calibration untuk fusi lintas-modal, serta edge-aware guidance untuk mempertajam batas objek. Kerangka ini bekerja untuk RGB-D maupun RGB-T (thermal) dan mencapai SOTA pada banyak dataset.

## Latar Belakang & Konteks
Backbone CNN membatasi konteks global sehingga batas objek sering kabur, dan metode biasanya khusus satu jenis modalitas kedua (depth ATAU thermal).

## Permasalahan yang Diangkat
- Backbone CNN membatasi konteks global.
- Batas objek sering kabur pada SOD.
- Metode sering khusus depth ATAU thermal.
- Fusi lintas-modal perlu penyelarasan spasial/kanal.
- Kebutuhan desain umum lintas modalitas kedua.

## Tujuan & Pertanyaan Penelitian
- Memakai backbone Transformer untuk konteks global.
- Menyatukan RGB-D dan RGB-T dalam satu kerangka.
- Mempertajam batas via edge-aware guidance.

## Tinjauan Terdahulu / Posisi Literatur
SwinNet menggabungkan Swin Transformer dan panduan tepi untuk fusi lintas-modal.

Karya/konsep pembanding yang relevan:

- Swin Transformer — backbone.
- RGB-D & RGB-T SOD — target.
- Edge/boundary guidance.
- Cross-modal fusion (alignment/recalibration).

## Metodologi & Arsitektur
Dua backbone Swin memproses RGB dan modal kedua (depth/thermal); spatial alignment module menyelaraskan fitur lintas-modal, channel re-calibration menimbang kanal; edge-aware guidance memandu penajaman batas; decoder menghasilkan saliency.

Komponen / langkah metodologis utama:

- Backbone Swin Transformer dua-aliran.
- Spatial alignment lintas-modal.
- Channel re-calibration.
- Edge-aware guidance (penajaman batas).
- Fusi lintas-modal terpandu.
- Bekerja untuk RGB-D & RGB-T.

## Kontribusi Utama
1. Backbone Transformer untuk konteks global.
2. Desain umum RGB-D & RGB-T.
3. Edge-aware guidance mempertajam batas.
4. SOTA pada banyak dataset.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD dan RGB-T SOD dengan metrik S/F/E-measure dan MAE, dibandingkan metode CNN/Transformer.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| RGB-D SOD | S/F/E, MAE | SOTA pada banyak dataset |
| RGB-T SOD | S/F/E, MAE | SOTA pada banyak dataset |
| Ablation | edge/align | keduanya menyumbang gain |

## Temuan Kunci
- Backbone Transformer meningkatkan konteks global.
- Satu desain menangani depth & thermal.
- Edge-aware guidance penting untuk batas.
- Penyelarasan spasial/kanal krusial.

## Keunggulan
- Backbone Transformer edge-aware.
- Umum lintas modalitas kedua.
- SOTA luas.

## Keterbatasan
- Transformer mahal komputasi.
- Bergantung kualitas modal kedua.
- Penyelarasan menambah kompleksitas.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
SwinNet mencontohkan penerapan Swin (entri 025) pada fusi lintas-modal RGB-D/RGB-T; relevan bagi tren Transformer pada tinjauan RGB+Depth.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [040 - 2020 - HDFNet - RGB-D SOD](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)
- [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)
- [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 154 entri total).
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
SwinNet memanfaatkan backbone Swin Transformer dengan edge-aware guidance dan fusi lintas-modal untuk RGB-D dan RGB-T SOD, menyatukan dua modalitas kedua dalam satu desain SOTA.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `liu2021swinnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 043/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
