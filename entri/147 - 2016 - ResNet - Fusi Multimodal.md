# 147 - Deep Residual Learning for Image Recognition

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 147 dari 154 |
| Kunci BibTeX | `he2016resnet` |
| Judul | Deep Residual Learning for Image Recognition |
| Penulis | He, Kaiming; Zhang, Xiangyu; Ren, Shaoqing; Sun, Jian |
| Tahun | 2016 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fusi Multimodal |
| Kata kunci | backbone, residual, skip connection, jaringan dalam, ImageNet |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Residual%20Learning%20for%20Image%20Recognition
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Deep%20Residual%20Learning%20for%20Image%20Recognition&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 770--778 |

## Ringkasan Eksekutif
Memperkenalkan koneksi residual (skip connection) yang memungkinkan pelatihan jaringan sangat dalam tanpa degradasi, menjadi backbone paling fundamental dalam visi.

## Abstrak (Parafrase)
ResNet (He dkk.) memperkenalkan residual learning: alih-alih memetakan langsung, tiap blok mempelajari residu terhadap identitas melalui skip connection. Ini mengatasi masalah degradasi pada jaringan sangat dalam, memungkinkan arsitektur hingga 152 lapis, dan memenangi ILSVRC/COCO 2015. ResNet menjadi backbone paling banyak dipakai.

## Latar Belakang & Konteks
Menambah kedalaman jaringan seharusnya meningkatkan kapasitas, namun secara empiris jaringan sangat dalam justru mengalami degradasi akurasi (bukan hanya overfitting).

## Permasalahan yang Diangkat
- Jaringan sangat dalam mengalami degradasi akurasi.
- Vanishing/exploding gradient menghambat pelatihan.
- Pemetaan identitas sulit dipelajari langsung.
- Kapasitas kedalaman belum termanfaatkan.
- Arsitektur dalam sulit dioptimalkan.

## Tujuan & Pertanyaan Penelitian
- Memungkinkan pelatihan jaringan sangat dalam.
- Mengatasi degradasi via residual learning.
- Menyediakan backbone kuat serbaguna.

## Tinjauan Terdahulu / Posisi Literatur
ResNet menjawab masalah degradasi arsitektur dalam.

Karya/konsep pembanding yang relevan:

- CNN dalam (VGG/GoogLeNet) — pembanding.
- Residual learning — gagasan inti.
- Skip/identity connection.
- ImageNet/COCO — benchmark.

## Metodologi & Arsitektur
Tiap blok residual menghitung F(x)+x, di mana skip connection membawa input x langsung ke output sehingga jaringan hanya perlu mempelajari residu F(x); ini memudahkan optimasi dan aliran gradien; arsitektur ResNet-18/34/50/101/152.

Komponen / langkah metodologis utama:

- Residual learning (F(x)+x).
- Skip/identity connection.
- Blok residual (bottleneck untuk model besar).
- Arsitektur hingga 152 lapis.
- Batch normalization.
- Pra-latih ImageNet.

## Kontribusi Utama
1. Residual learning memungkinkan jaringan sangat dalam.
2. Skip connection memperbaiki aliran gradien.
3. Memenangi ILSVRC/COCO 2015.
4. Backbone paling fundamental & serbaguna.

## Rincian Eksperimen
Diuji pada ImageNet (klasifikasi) dan COCO (deteksi/segmentasi), dengan analisis kedalaman (18-152), memenangi berbagai tantangan 2015.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ImageNet | top-1/top-5 | SOTA 2015, memenangi ILSVRC |
| COCO | AP | backbone pemenang deteksi/segmentasi |
| Kedalaman | 18-152 | degradasi teratasi |

## Temuan Kunci
- Residual learning mengatasi degradasi kedalaman.
- Skip connection memperbaiki gradien.
- Kedalaman ekstrem menjadi layak dilatih.
- Backbone serbaguna untuk banyak tugas.

## Keunggulan
- Backbone fundamental & serbaguna.
- Melatih jaringan sangat dalam.
- Berpengaruh luas.

## Keterbatasan
- Model besar (152) mahal.
- Bukan spesifik RGB-D.
- Digantikan sebagian oleh Transformer pada tugas tertentu.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ResNet adalah backbone yang mendasari hampir semua detektor dan jaringan RGB-D dalam tinjauan; skip connection juga menginspirasi banyak desain (DarkNet-53, dll.).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fusi Multimodal** yang baik dibaca berdampingan:

- [148 - 2017 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)
- [149 - 2018 - CBAM - Fusi Multimodal](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md)
- [150 - 2021 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)
- [153 - 2021 - Survei RGB-D SOD (Zhou dkk.) - Fusi Multimodal](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)
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
ResNet memperkenalkan residual learning dengan skip connection untuk melatih jaringan sangat dalam tanpa degradasi, menjadi backbone paling fundamental yang mendasari banyak detektor dan jaringan RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `he2016resnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 147/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
