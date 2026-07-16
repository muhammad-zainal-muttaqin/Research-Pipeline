# 057 - ShapeConv: Shape-Aware Convolutional Layer for Indoor RGB-D Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 057 dari 154 |
| Kunci BibTeX | `cao2021shapeconv` |
| Judul | ShapeConv: Shape-Aware Convolutional Layer for Indoor RGB-D Semantic Segmentation |
| Penulis | Cao, Jinming; Leng, Hanchao; Lischinski, Dani; Cohen-Or, Daniel; Tu, Changhe; Li, Yangyan |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, shape-aware, konvolusi, geometri, plug-and-play |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-segmentasi-rgb-d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ShapeConv%3A%20Shape-Aware%20Convolutional%20Layer%20for%20Indoor%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ShapeConv%3A%20Shape-Aware%20Convolutional%20Layer%20for%20Indoor%20RGB-D%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 7088--7097 |

## Ringkasan Eksekutif
Lapisan konvolusi sadar-bentuk yang memisahkan komponen nilai-dasar dan bentuk dari patch kedalaman untuk memperkuat fitur geometris pada segmentasi RGB-D.

## Abstrak (Parafrase)
ShapeConv (Shape-aware Convolutional layer) mendekomposisi patch kedalaman menjadi komponen base (nilai rata-rata) dan shape (variasi relatif), lalu memproses keduanya dengan bobot terpisah yang dapat dipelajari. Ini secara eksplisit memodelkan bentuk geometris, meningkatkan segmentasi RGB-D, dan bersifat plug-and-play menggantikan konvolusi standar.

## Latar Belakang & Konteks
Konvolusi standar tidak secara eksplisit memodelkan bentuk pada patch kedalaman, padahal informasi bentuk (kelengkungan, kemiringan) penting untuk segmentasi geometris.

## Permasalahan yang Diangkat
- Konvolusi standar tak eksplisit memodelkan bentuk.
- Informasi bentuk pada kedalaman kurang dimanfaatkan.
- Fitur geometris perlu diperkuat.
- Butuh solusi plug-and-play.
- Segmentasi indoor menuntut isyarat geometri.

## Tujuan & Pertanyaan Penelitian
- Memodelkan bentuk secara eksplisit dari patch kedalaman.
- Memisahkan komponen base dan shape.
- Menyediakan lapisan plug-and-play.

## Tinjauan Terdahulu / Posisi Literatur
ShapeConv memodifikasi operasi konvolusi untuk data kedalaman.

Karya/konsep pembanding yang relevan:

- Konvolusi standar — yang dimodifikasi.
- Segmentasi RGB-D.
- Shape/geometry modeling.
- Plug-and-play layer.

## Metodologi & Arsitektur
Patch kedalaman didekomposisi menjadi base-component (nilai dasar) dan shape-component (variasi relatif); masing-masing dikalikan bobot terlatih terpisah lalu digabung sebelum konvolusi; menggantikan konvolusi standar di jaringan segmentasi.

Komponen / langkah metodologis utama:

- Dekomposisi base-component & shape-component.
- Bobot terlatih terpisah untuk tiap komponen.
- Pemodelan bentuk eksplisit.
- Plug-and-play menggantikan konvolusi.
- Diterapkan lintas backbone.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Pemodelan bentuk eksplisit pada patch kedalaman.
2. Lapisan plug-and-play lintas backbone.
3. Peningkatan konsisten segmentasi RGB-D.
4. Memperkuat fitur geometris.

## Rincian Eksperimen
Diuji pada NYUv2 dan SUN RGB-D dengan berbagai backbone, metrik mIoU, plus ablation komponen shape.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | peningkatan konsisten lintas backbone |
| SUN RGB-D | mIoU | peningkatan konsisten |
| Ablation | shape-component | pemodelan bentuk menyumbang gain |

## Temuan Kunci
- Pemodelan bentuk eksplisit meningkatkan segmentasi.
- Plug-and-play memudahkan adopsi.
- Konsisten lintas backbone.
- Fitur geometris diperkuat.

## Keunggulan
- Plug-and-play & sederhana.
- Peningkatan konsisten.
- Memodelkan geometri eksplisit.

## Keterbatasan
- Menambah sedikit parameter/komputasi.
- Bergantung kualitas kedalaman.
- Manfaat bervariasi antar-dataset.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ShapeConv menunjukkan pemanfaatan geometri kedalaman pada level operasi — wawasan yang melengkapi strategi fusi RGB+Depth lain dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)
- [058 - 2023 - CMX - Segmentasi RGB-D](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)
- [059 - 2023 - PGDENet - Segmentasi RGB-D](./059%20-%202023%20-%20PGDENet%20-%20Segmentasi%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Segmentasi RGB-D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Segmentasi RGB-D)
Istilah penting untuk memahami makalah ini:

- **Segmentasi semantik** — Pelabelan kelas per-piksel.
- **Scene parsing** — Pemahaman menyeluruh isi scene via segmentasi.
- **Encoder-decoder** — Arsitektur mengecilkan lalu memulihkan resolusi.
- **Fusi RGB-D** — Penggabungan cabang warna dan kedalaman.
- **mIoU** — mean Intersection-over-Union; metrik segmentasi utama.
- **Gating** — Gerbang penyaring/penimbang fitur sebelum digabung.
- **Cross-modal** — Antar-modalitas (RGB dan depth/thermal/LiDAR).
- **NYUv2** — Dataset RGB-D indoor standar.
- **SUN RGB-D** — Dataset RGB-D indoor berskala.
- **Pixel accuracy** — Persentase piksel terlabel benar.

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
ShapeConv memisahkan komponen base dan shape dari patch kedalaman untuk memodelkan bentuk secara eksplisit, meningkatkan segmentasi RGB-D sebagai lapisan plug-and-play.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `cao2021shapeconv` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 057/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
