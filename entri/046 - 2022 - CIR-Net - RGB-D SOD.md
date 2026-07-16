# 046 - CIR-Net: Cross-Modality Interaction and Refinement for RGB-D Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 046 dari 154 |
| Kunci BibTeX | `cong2022cirnet` |
| Judul | CIR-Net: Cross-Modality Interaction and Refinement for RGB-D Salient Object Detection |
| Penulis | Cong, Runmin; Lin, Qinwei; Zhang, Chen; Li, Chongyi; Cao, Xiaochun; Huang, Qingming; Zhao, Yao |
| Tahun | 2022 |
| Venue / Jurnal | IEEE Transactions on Image Processing |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, cross-modality interaction, refinement, progresif, fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=CIR-Net%3A%20Cross-Modality%20Interaction%20and%20Refinement%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=CIR-Net%3A%20Cross-Modality%20Interaction%20and%20Refinement%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 31 |
| Halaman | 6800--6815 |

## Ringkasan Eksekutif
Metode RGB-D SOD yang menyusun interaksi lintas-modal progresif dan penyempurnaan (cross-modality interaction and refinement) untuk memaksimalkan komplementaritas RGB dan kedalaman.

## Abstrak (Parafrase)
CIR-Net (Cross-modality Interaction and Refinement) membangun interaksi lintas-modal bertahap: fitur RGB dan kedalaman saling memandu melalui progressive attention-guided integration, lalu convergence aggregation dan refinement menyempurnakan hasil. Pendekatan progresif ini melampaui interaksi satu arah/dangkal dan mencapai SOTA saat rilis.

## Latar Belakang & Konteks
Interaksi RGB-D yang satu arah atau dangkal membatasi eksploitasi komplementaritas kedua modal, sehingga fitur gabungan kurang optimal.

## Permasalahan yang Diangkat
- Interaksi RGB-D satu arah/dangkal membatasi komplementaritas.
- Fitur gabungan kurang optimal tanpa interaksi bertahap.
- Penyempurnaan hasil belum memadai.
- Konvergensi fitur lintas-modal sulit.
- Fusi statis kurang kaya.

## Tujuan & Pertanyaan Penelitian
- Menyusun interaksi lintas-modal progresif.
- Menyempurnakan fitur via convergence & refinement.
- Memaksimalkan komplementaritas RGB-D.

## Tinjauan Terdahulu / Posisi Literatur
CIR-Net mengembangkan interaksi lintas-modal bertahap untuk RGB-D SOD.

Karya/konsep pembanding yang relevan:

- RGB-D SOD berbasis fusi — dasar.
- Attention-guided integration.
- Progressive/iterative refinement.
- Cross-modality interaction.

## Metodologi & Arsitektur
Progressive attention-guided integration membuat RGB dan kedalaman saling memandu bertahap; convergence aggregation menyatukan fitur lintas-modal; modul refinement menyempurnakan peta saliency; supervisi multi-level.

Komponen / langkah metodologis utama:

- Progressive attention-guided integration.
- Interaksi lintas-modal bertahap (dua arah).
- Convergence aggregation lintas-modal.
- Refinement menyempurnakan saliency.
- Supervisi multi-level.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Interaksi lintas-modal progresif dua-arah.
2. Convergence aggregation + refinement.
3. Eksploitasi komplementaritas maksimal.
4. SOTA pada benchmark saat rilis.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar dengan metrik S/F/E-measure dan MAE, plus ablation interaksi progresif.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | SOTA saat rilis |
| STERE/SIP | S/F/E, MAE | kompetitif/unggul |
| Ablation | progressive interaction | interaksi bertahap menyumbang gain |

## Temuan Kunci
- Interaksi progresif dua-arah mengungguli satu-arah.
- Convergence + refinement meningkatkan kualitas.
- Komplementaritas RGB-D dieksploitasi maksimal.
- Penyempurnaan bertahap penting.

## Keunggulan
- Interaksi progresif dua-arah.
- Penyempurnaan efektif.
- SOTA saat rilis.

## Keterbatasan
- Interaksi bertahap menambah komputasi.
- Bergantung kualitas kedalaman.
- Backbone CNN (konteks terbatas).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
CIR-Net menegaskan interaksi-penyempurnaan progresif untuk fusi RGB-D — prinsip desain yang relevan bagi seluruh klaster RGB+Depth dalam tinjauan.

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
CIR-Net menyusun interaksi lintas-modal progresif dua-arah dengan convergence aggregation dan refinement untuk RGB-D SOD, memaksimalkan komplementaritas dan mencapai SOTA.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `cong2022cirnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 046/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
