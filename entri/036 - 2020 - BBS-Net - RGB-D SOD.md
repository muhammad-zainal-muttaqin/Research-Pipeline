# 036 - BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 036 dari 154 |
| Kunci BibTeX | `fan2020bbsnet` |
| Judul | BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network |
| Penulis | Fan, Deng-Ping; Zhai, Yingjie; Borji, Ali; Yang, Jufeng; Shao, Ling |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, bifurcated backbone, depth-enhanced, cascaded refinement, fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=BBS-Net%3A%20RGB-D%20Salient%20Object%20Detection%20with%20a%20Bifurcated%20Backbone%20Strategy%20Network
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=BBS-Net%3A%20RGB-D%20Salient%20Object%20Detection%20with%20a%20Bifurcated%20Backbone%20Strategy%20Network&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 275--292 |

## Ringkasan Eksekutif
Jaringan RGB-D SOD yang memisahkan fitur multi-level menjadi kelompok via strategi bifurcated backbone dan memperkuatnya dengan modul depth-enhanced, dengan penyempurnaan bertahap.

## Abstrak (Parafrase)
BBS-Net (Bifurcated Backbone Strategy Network) membagi fitur backbone menjadi kelompok level-rendah dan level-tinggi, memprosesnya secara berbeda, lalu menyatukannya dengan Depth-Enhanced Module (DEM) yang memanfaatkan kedalaman untuk memperkuat fitur. Penyempurnaan bertingkat (cascaded refinement) meningkatkan kualitas peta saliency, mencapai SOTA pada beberapa metrik saat rilis.

## Latar Belakang & Konteks
Integrasi fitur lintas-level dan lintas-modal pada RGB-D SOD masih suboptimal: fitur level-rendah (detail) dan level-tinggi (semantik) memerlukan perlakuan berbeda, dan kedalaman perlu dimanfaatkan efektif.

## Permasalahan yang Diangkat
- Integrasi lintas-level fitur belum optimal.
- Fitur rendah (detail) & tinggi (semantik) perlu perlakuan berbeda.
- Pemanfaatan kedalaman sering dangkal.
- Fusi lintas-modal menyebarkan derau.
- Penyempurnaan saliency satu-lintasan terbatas.

## Tujuan & Pertanyaan Penelitian
- Memisahkan & memperlakukan fitur multi-level berbeda.
- Memperkuat fitur dengan kedalaman (DEM).
- Menyempurnakan saliency secara bertingkat.

## Tinjauan Terdahulu / Posisi Literatur
BBS-Net memperbaiki fusi RGB-D dan agregasi multi-level dengan strategi bifurkasi.

Karya/konsep pembanding yang relevan:

- RGB-D SOD berbasis CNN — dasar.
- Agregasi multi-level (mirip FPN).
- Depth enhancement — pemanfaatan kedalaman.
- Cascaded refinement — penyempurnaan bertahap.

## Metodologi & Arsitektur
Backbone (mis. ResNet) menghasilkan fitur multi-level yang dibifurkasi menjadi kelompok rendah/tinggi; Depth-Enhanced Module memakai kedalaman untuk merekalibrasi fitur; agregasi dan cascaded refinement menghasilkan peta saliency akhir.

Komponen / langkah metodologis utama:

- Bifurcated backbone (fitur rendah vs tinggi).
- Depth-Enhanced Module (DEM) rekalibrasi fitur.
- Agregasi multi-level terkelompok.
- Cascaded refinement bertingkat.
- Supervisi multi-skala.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Strategi bifurkasi untuk fitur multi-level.
2. DEM memanfaatkan kedalaman secara efektif.
3. Cascaded refinement meningkatkan kualitas.
4. SOTA pada beberapa metrik saat rilis.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar (NJU2K, NLPR, STERE, DES, SIP, dll.) dengan metrik S/F/E-measure dan MAE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | SOTA saat rilis |
| SIP/STERE | S/F/E, MAE | kompetitif/unggul |
| Ablation | bifurkasi/DEM | keduanya menyumbang gain |

## Temuan Kunci
- Perlakuan berbeda untuk fitur multi-level bermanfaat.
- Kedalaman efektif memperkuat fitur (DEM).
- Penyempurnaan bertingkat meningkatkan detail.
- Strategi bifurkasi banyak diadopsi.

## Keunggulan
- Arsitektur berpengaruh & banyak dirujuk.
- Pemanfaatan kedalaman efektif.
- Penyempurnaan bertingkat berkualitas.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Backbone CNN (konteks global terbatas).
- Kompleksitas cascaded refinement.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
BBS-Net adalah entri inti klaster RGB-D SOD; strategi bifurkasi dan pemanfaatan kedalaman relevan sebagai prinsip fusi RGB+Depth yang dibahas dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [040 - 2020 - HDFNet - RGB-D SOD](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)
- [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)
- [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)
- [043 - 2022 - SwinNet - RGB-D SOD](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)

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
BBS-Net memperkenalkan strategi bifurcated backbone dan Depth-Enhanced Module dengan cascaded refinement untuk RGB-D SOD, menjadi arsitektur berpengaruh dalam pemanfaatan kedalaman.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `fan2020bbsnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 036/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
