# 060 - Multimodal Token Fusion for Vision Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 060 dari 154 |
| Kunci BibTeX | `wang2022tokenfusion` |
| Judul | Multimodal Token Fusion for Vision Transformers |
| Penulis | Wang, Yikai; Chen, Xinghao; Cao, Lele; Huang, Wenbing; Sun, Fuchun; Wang, Yunhe |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | Transformer, token fusion, multimodal, pruning, RGB-D |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Multimodal%20Token%20Fusion%20for%20Vision%20Transformers
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Multimodal%20Token%20Fusion%20for%20Vision%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 12186--12195 |

## Ringkasan Eksekutif
Metode fusi multimodal untuk Vision Transformer yang menukar token tak-informatif satu modal dengan token proyeksi antar-modal secara efisien.

## Abstrak (Parafrase)
TokenFusion mendeteksi token yang tidak informatif pada satu modalitas lalu menggantinya dengan token hasil proyeksi dari modalitas lain, dengan residual positional alignment untuk menjaga struktur. Ini memungkinkan fusi multimodal (mis. RGB-D) pada Transformer secara selektif dan efisien tanpa mencampur semua token.

## Latar Belakang & Konteks
Fusi Transformer multimodal naif (menggabungkan semua token) mahal dan tak selektif, padahal sebagian token satu modal tidak informatif dan sebaiknya digantikan modal lain.

## Permasalahan yang Diangkat
- Fusi Transformer multimodal naif mahal.
- Penggabungan semua token tak selektif.
- Sebagian token satu modal tak informatif.
- Struktur posisi perlu dijaga saat pertukaran.
- Efisiensi fusi diperlukan.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi token tak-informatif.
- Menukarnya dengan token antar-modal.
- Menjaga struktur via positional alignment.

## Tinjauan Terdahulu / Posisi Literatur
TokenFusion mengembangkan pemangkasan dan pertukaran token pada ViT untuk fusi multimodal.

Karya/konsep pembanding yang relevan:

- Vision Transformer (ViT) — arsitektur dasar.
- Token pruning — deteksi token tak-penting.
- Multimodal fusion.
- Residual positional alignment.

## Metodologi & Arsitektur
Modul deteksi menandai token tak-informatif pada satu modal; token tersebut digantikan proyeksi token dari modal lain; residual positional alignment menjaga korespondensi spasial; berlaku untuk berbagai tugas multimodal termasuk segmentasi RGB-D.

Komponen / langkah metodologis utama:

- Deteksi token tak-informatif per-modal.
- Substitusi antar-modal (token swap).
- Residual positional alignment.
- Fusi selektif dan efisien.
- Berlaku lintas tugas multimodal.
- Pelatihan end-to-end.

## Kontribusi Utama
1. Mekanisme fusi token selektif & efisien.
2. Pertukaran token antar-modal.
3. Menjaga struktur posisi.
4. Efektif untuk RGB-D dan tugas multimodal lain.

## Rincian Eksperimen
Diuji pada tugas multimodal termasuk segmentasi RGB-D dan lainnya dengan metrik yang sesuai (mis. mIoU), plus ablation mekanisme pertukaran token.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| RGB-D segmentation | mIoU | efisien & akurat |
| Tugas multimodal lain | metrik terkait | generalisasi |
| Ablation | token swap | pertukaran selektif menyumbang gain |

## Temuan Kunci
- Sebagian token satu modal dapat digantikan modal lain.
- Fusi token selektif lebih efisien.
- Positional alignment penting.
- Generalisasi lintas tugas multimodal.

## Keunggulan
- Fusi token efisien.
- Selektif (bukan menggabung semua).
- Generalis lintas tugas.

## Keterbatasan
- Deteksi token tak-informatif bergantung heuristik.
- Transformer mahal untuk resolusi tinggi.
- Bergantung kualitas modal kedua.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
TokenFusion menawarkan mekanisme fusi token efisien untuk Transformer multimodal — relevan bagi tren fusi RGB+Depth berbasis Transformer dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)
- [057 - 2021 - ShapeConv - Segmentasi RGB-D](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md)
- [058 - 2023 - CMX - Segmentasi RGB-D](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)

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
TokenFusion menukar token tak-informatif satu modal dengan token antar-modal secara selektif dan efisien pada Vision Transformer, menyediakan fusi multimodal (termasuk RGB-D) yang hemat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2022tokenfusion` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 060/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
