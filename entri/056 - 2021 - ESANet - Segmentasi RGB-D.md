# 056 - Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 056 dari 154 |
| Kunci BibTeX | `seichter2021esanet` |
| Judul | Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis |
| Penulis | Seichter, Daniel; K{\"o |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Robotics and Automation (ICRA) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | segmentasi RGB-D, efisien, real-time, robotika, SE-attention |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Efficient%20RGB-D%20Semantic%20Segmentation%20for%20Indoor%20Scene%20Analysis
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Efficient%20RGB-D%20Semantic%20Segmentation%20for%20Indoor%20Scene%20Analysis&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 13525--13531 |

## Ringkasan Eksekutif
Arsitektur segmentasi RGB-D yang efisien (encoder ganda ResNet + attention) dioptimalkan untuk inferensi real-time pada robot indoor.

## Abstrak (Parafrase)
ESANet (Efficient Scene Analysis Network) menyeimbangkan akurasi dan efisiensi untuk analisis scene RGB-D real-time. Ia memakai dua encoder ResNet ringan dengan SE-attention untuk fusi, decoder efisien, dan dioptimasi untuk TensorRT sehingga cocok untuk robot indoor. Akurasinya kompetitif pada kecepatan jauh lebih tinggi.

## Latar Belakang & Konteks
Metode RGB-D akurat sering terlalu berat untuk robot dengan komputasi terbatas dan kebutuhan real-time; diperlukan keseimbangan akurasi-efisiensi.

## Permasalahan yang Diangkat
- Metode RGB-D akurat terlalu berat untuk robot.
- Kebutuhan real-time pada komputasi terbatas.
- Fusi RGB-D harus efisien.
- Deployment (TensorRT) perlu dipertimbangkan.
- Akurasi tak boleh dikorbankan berlebihan.

## Tujuan & Pertanyaan Penelitian
- Menyeimbangkan akurasi & efisiensi segmentasi RGB-D.
- Mengoptimalkan untuk inferensi real-time.
- Menyediakan model praktis untuk robot indoor.

## Tinjauan Terdahulu / Posisi Literatur
ESANet menyeimbangkan akurasi-efisiensi terhadap metode berat seperti SA-Gate/ACNet.

Karya/konsep pembanding yang relevan:

- SA-Gate/ACNet — pembanding akurat namun berat.
- ResNet ringan — backbone efisien.
- SE-attention — fusi ringan.
- TensorRT — optimasi deployment.

## Metodologi & Arsitektur
Dua encoder ResNet (RGB & depth) yang ringan; fusi memakai SE-attention untuk menimbang kanal; decoder efisien memulihkan resolusi; model dioptimasi TensorRT untuk inferensi cepat pada GPU embedded.

Komponen / langkah metodologis utama:

- Dual ResNet encoder ringan (RGB & depth).
- Fusi berbasis SE-attention.
- Decoder efisien.
- Optimasi TensorRT untuk deployment.
- Segmentasi per-piksel indoor.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Segmentasi RGB-D real-time untuk robot.
2. Encoder ganda ringan + SE-attention.
3. Akurasi kompetitif pada kecepatan tinggi.
4. Optimasi deployment (TensorRT).

## Rincian Eksperimen
Diuji pada NYUv2, SUN RGB-D, dan Cityscapes dengan metrik mIoU dan pengukuran kecepatan (FPS pada GPU embedded).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2/SUN RGB-D | mIoU/FPS | akurasi kompetitif, real-time |
| Cityscapes | mIoU | kompetitif |
| Kecepatan | FPS | real-time pada GPU embedded |

## Temuan Kunci
- Efisiensi memungkinkan segmentasi RGB-D real-time.
- SE-attention cukup untuk fusi ringan.
- Akurasi terjaga pada kecepatan tinggi.
- Deployment nyata layak (TensorRT).

## Keunggulan
- Real-time & efisien.
- Cocok untuk robot indoor.
- Akurasi kompetitif.

## Keterbatasan
- Akurasi sedikit di bawah metode terberat.
- Bergantung kualitas kedalaman.
- Optimasi terikat perangkat.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ESANet penting bagi tinjauan karena menautkan segmentasi RGB-D dengan robotika real-time — konteks yang sama dengan banyak sistem YOLO+RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [052 - 2018 - RedNet - Segmentasi RGB-D](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md)
- [053 - 2017 - RDFNet - Segmentasi RGB-D](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md)
- [054 - 2019 - ACNet - Segmentasi RGB-D](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [057 - 2021 - ShapeConv - Segmentasi RGB-D](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md)
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
ESANet menyediakan segmentasi RGB-D efisien dengan encoder ganda ringan dan SE-attention, dioptimasi untuk inferensi real-time pada robot indoor tanpa mengorbankan akurasi berlebihan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `seichter2021esanet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 056/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
