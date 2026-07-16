# 049 - Cross-Modal Hierarchical Interaction Network for RGB-D Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 049 dari 154 |
| Kunci BibTeX | `chen2023cmhi` |
| Judul | Cross-Modal Hierarchical Interaction Network for RGB-D Salient Object Detection |
| Penulis | Bi, Hangbo; Wu, Ruimin; Liu, Ziqi; Zhu, Huihui; Zhang, Cong; Xiang, Tian-Zhu |
| Tahun | 2023 |
| Venue / Jurnal | Pattern Recognition |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, interaksi hierarkis, cross-modal, multi-level, Pattern Recognition |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Cross-Modal%20Hierarchical%20Interaction%20Network%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Cross-Modal%20Hierarchical%20Interaction%20Network%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 136 |
| Halaman | 109194 |

## Ringkasan Eksekutif
Jaringan RGB-D SOD yang menyusun pertukaran informasi lintas-modal bertingkat (hierarkis) untuk memanfaatkan hierarki fitur RGB dan kedalaman.

## Abstrak (Parafrase)
Makalah ini (di Pattern Recognition) mengusulkan cross-modal hierarchical interaction network yang menyusun interaksi RGB-D secara bertingkat sesuai hierarki fitur (rendah ke tinggi), sehingga detail dan semantik dipertukarkan pada level yang sesuai. Agregasi bertingkat menghasilkan saliency yang lebih konsisten.

## Latar Belakang & Konteks
Interaksi lintas-modal yang datar (satu level) mengabaikan hierarki fitur, padahal detail (level rendah) dan semantik (level tinggi) memerlukan interaksi berbeda.

## Permasalahan yang Diangkat
- Interaksi lintas-modal datar mengabaikan hierarki fitur.
- Detail & semantik perlu interaksi berbeda.
- Agregasi antar-level belum optimal.
- Konsistensi saliency sulit dijaga.
- Fusi statis kurang kaya.

## Tujuan & Pertanyaan Penelitian
- Menyusun interaksi lintas-modal hierarkis.
- Mempertukarkan fitur pada level yang sesuai.
- Mengagregasi hasil secara bertingkat.

## Tinjauan Terdahulu / Posisi Literatur
Makalah mengembangkan interaksi lintas-modal hierarkis untuk RGB-D SOD.

Karya/konsep pembanding yang relevan:

- RGB-D SOD berbasis fusi — dasar.
- Hierarki fitur multi-level (FPN-like).
- Cross-modal interaction.
- Agregasi bertingkat.

## Metodologi & Arsitektur
Modul interaksi hierarkis mempertukarkan fitur RGB-D pada tiap level hierarki (rendah->tinggi); agregasi bertingkat menyatukan hasil; decoder menghasilkan saliency dengan supervisi multi-level.

Komponen / langkah metodologis utama:

- Modul interaksi hierarkis RGB-D.
- Pertukaran fitur per-level hierarki.
- Agregasi bertingkat.
- Konteks multi-level.
- Decoder saliency.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Interaksi lintas-modal hierarkis (per-level).
2. Agregasi bertingkat konsisten.
3. Detail & semantik dipertukarkan tepat level.
4. Peningkatan konsisten pada benchmark.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar dengan metrik S/F/E-measure dan MAE (dipublikasikan di Pattern Recognition).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | peningkatan konsisten |
| STERE/SIP | S/F/E, MAE | kompetitif |
| Ablation | hierarchical interaction | interaksi bertingkat menyumbang gain |

## Temuan Kunci
- Interaksi hierarkis mengungguli interaksi datar.
- Detail & semantik dipertukarkan pada level tepat.
- Agregasi bertingkat meningkatkan konsistensi.
- Hierarki fitur penting untuk fusi.

## Keunggulan
- Interaksi hierarkis lintas-modal.
- Agregasi bertingkat.
- Peningkatan konsisten.

## Keterbatasan
- Interaksi bertingkat menambah komputasi.
- Bergantung kualitas kedalaman.
- Backbone CNN (konteks terbatas).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Makalah ini memperkuat argumen interaksi hierarkis lintas-modal, prinsip desain fusi RGB+Depth yang relevan bagi tinjauan.

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
Cross-Modal Hierarchical Interaction Network menyusun pertukaran informasi RGB-D bertingkat sesuai hierarki fitur, meningkatkan konsistensi saliency dan memperkuat argumen interaksi hierarkis.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `chen2023cmhi` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 049/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
