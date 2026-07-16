# 035 - Depth-Induced Multi-Scale Recurrent Attention Network for Saliency Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 035 dari 154 |
| Kunci BibTeX | `piao2019dmra` |
| Judul | Depth-Induced Multi-Scale Recurrent Attention Network for Saliency Detection |
| Penulis | Piao, Yongri; Ji, Wei; Li, Jingjing; Zhang, Miao; Lu, Huchuan |
| Tahun | 2019 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, depth-induced, recurrent attention, multi-skala, saliency |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Depth-Induced%20Multi-Scale%20Recurrent%20Attention%20Network%20for%20Saliency%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Depth-Induced%20Multi-Scale%20Recurrent%20Attention%20Network%20for%20Saliency%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 7254--7263 |

## Ringkasan Eksekutif
Jaringan RGB-D salient object detection yang memakai pembobotan multi-skala terinduksi kedalaman dan recurrent attention untuk memandu deteksi objek menonjol, sekaligus merilis dataset DUT-RGBD.

## Abstrak (Parafrase)
DMRA (Depth-induced Multi-scale Recurrent Attention) memanfaatkan peta kedalaman untuk menghasilkan bobot multi-skala yang memandu fusi fitur RGB, lalu menerapkan recurrent attention untuk menyempurnakan peta saliency secara bertahap. Makalah juga memperkenalkan dataset DUT-RGBD. Pendekatan ini menegaskan peran kedalaman sebagai pemandu attention lintas-skala pada RGB-D SOD.

## Latar Belakang & Konteks
Fusi RGB-D naif memperlakukan kontribusi kedalaman seragam padahal isyarat kedalaman bervariasi antar-skala dan wilayah, sehingga penyempurnaan saliency kurang optimal.

## Permasalahan yang Diangkat
- Fusi RGB-D naif mengabaikan variasi kontribusi kedalaman.
- Isyarat kedalaman berbeda antar-skala/wilayah.
- Penyempurnaan saliency satu-lintasan kurang optimal.
- Dataset RGB-D SOD masih terbatas.
- Attention lintas-modal belum matang.

## Tujuan & Pertanyaan Penelitian
- Memanfaatkan kedalaman sebagai pemandu multi-skala.
- Menyempurnakan saliency secara bertahap (recurrent).
- Menyediakan dataset RGB-D SOD baru (DUT-RGBD).

## Tinjauan Terdahulu / Posisi Literatur
DMRA membangun di atas SOD berbasis CNN dan mekanisme attention, mengintegrasikan kedalaman sebagai pemandu.

Karya/konsep pembanding yang relevan:

- SOD berbasis CNN — dasar.
- Attention mechanism — penyempurna fitur.
- Recurrent refinement — iterasi saliency.
- Dataset RGB-D SOD sebelumnya (NJU2K, NLPR).

## Metodologi & Arsitektur
Modul depth-induced multi-scale weighting memakai peta kedalaman untuk menimbang fitur RGB lintas skala; recurrent attention module menyempurnakan peta saliency secara iteratif; jaringan dilatih end-to-end pada pasangan RGB-D.

Komponen / langkah metodologis utama:

- Depth-induced multi-scale weighting module.
- Recurrent attention untuk penyempurnaan bertahap.
- Fusi fitur RGB terpandu kedalaman.
- Pelatihan end-to-end RGB-D.
- Dataset DUT-RGBD baru.
- Decoder saliency multi-skala.

## Kontribusi Utama
1. Kedalaman sebagai pemandu attention multi-skala.
2. Recurrent attention menyempurnakan saliency.
3. Dataset DUT-RGBD untuk komunitas.
4. Hasil kompetitif pada benchmark RGB-D SOD.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD (NJU2K, NLPR, DUT-RGBD, dll.) dengan metrik S-measure, F-measure, E-measure, MAE, dibandingkan metode SOD sezaman.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | kompetitif saat rilis |
| DUT-RGBD | S/F/E, MAE | dataset baru diperkenalkan |
| Ablation | depth weighting | peningkatan dengan panduan kedalaman |

## Temuan Kunci
- Panduan kedalaman multi-skala meningkatkan saliency.
- Recurrent attention efektif menyempurnakan hasil.
- Dataset baru memperkaya evaluasi.
- Fusi terpandu lebih baik dari fusi naif.

## Keunggulan
- Memanfaatkan kedalaman secara adaptif.
- Penyempurnaan bertahap.
- Menyediakan dataset baru.

## Keterbatasan
- Bergantung kualitas peta kedalaman.
- Recurrent menambah biaya komputasi.
- Arsitektur CNN (konteks global terbatas).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DMRA adalah salah satu entri fondasi klaster RGB-D SOD dalam tinjauan; menegaskan prinsip bahwa kedalaman memandu attention, yang relevan bagi fusi RGB+Depth secara umum.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
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
DMRA menunjukkan kedalaman dapat memandu pembobotan multi-skala dan recurrent attention untuk RGB-D SOD, serta menyumbang dataset DUT-RGBD bagi komunitas.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `piao2019dmra` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 035/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
