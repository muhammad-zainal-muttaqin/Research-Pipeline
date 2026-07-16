# 141 - Indoor Segmentation and Support Inference from RGBD Images

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 141 dari 154 |
| Kunci BibTeX | `silberman2012nyu` |
| Judul | Indoor Segmentation and Support Inference from RGBD Images |
| Penulis | Silberman, Nathan; Hoiem, Derek; Kohli, Pushmeet; Fergus, Rob |
| Tahun | 2012 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Dataset |
| Kata kunci | dataset, RGB-D, indoor, segmentasi, Kinect |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-dataset)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Indoor%20Segmentation%20and%20Support%20Inference%20from%20RGBD%20Images
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Indoor%20Segmentation%20and%20Support%20Inference%20from%20RGBD%20Images&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 746--760 |

## Ringkasan Eksekutif
Dataset RGB-D indoor dengan anotasi segmentasi dan inferensi dukungan, dari kamera Kinect, menjadi benchmark standar segmentasi/depth RGB-D indoor.

## Abstrak (Parafrase)
NYU Depth v2 (Silberman dkk.) menyediakan 1449 citra RGB-D beranotasi padat (label segmentasi per-piksel dan relasi dukungan/support) plus video mentah, direkam dengan Kinect di lingkungan indoor. Ia menjadi benchmark standar untuk segmentasi semantik RGB-D dan estimasi kedalaman indoor.

## Latar Belakang & Konteks
Pemahaman scene indoor (segmentasi, relasi objek) membutuhkan data RGB-D beranotasi kaya yang sebelumnya tidak tersedia berskala.

## Permasalahan yang Diangkat
- Pemahaman scene indoor butuh data RGB-D kaya.
- Anotasi segmentasi padat mahal.
- Relasi dukungan objek perlu dilabeli.
- Benchmark RGB-D indoor kurang.
- Kinect memungkinkan akuisisi RGB-D murah.

## Tujuan & Pertanyaan Penelitian
- Menyediakan citra RGB-D beranotasi padat.
- Melabeli segmentasi & relasi dukungan.
- Menyediakan benchmark indoor standar.

## Tinjauan Terdahulu / Posisi Literatur
NYUv2 menyediakan benchmark RGB-D indoor.

Karya/konsep pembanding yang relevan:

- Kinect — sensor RGB-D.
- Segmentasi semantik indoor.
- Support inference — relasi objek.
- Benchmark depth/segmentasi.

## Metodologi & Arsitektur
1449 citra RGB-D dipilih dari video Kinect dan dianotasi padat (kelas objek per-piksel + relasi dukungan); video mentah juga disediakan; dipakai untuk segmentasi RGB-D, estimasi kedalaman, dan inferensi dukungan.

Komponen / langkah metodologis utama:

- 1449 citra RGB-D beranotasi padat.
- Label segmentasi per-piksel.
- Relasi dukungan (support inference).
- Video mentah Kinect.
- Lingkungan indoor.
- Benchmark standar.

## Kontribusi Utama
1. Dataset RGB-D indoor beranotasi kaya.
2. Label segmentasi + relasi dukungan.
3. Benchmark standar segmentasi/depth.
4. Fondasi riset RGB-D indoor.

## Rincian Eksperimen
Menyediakan benchmark NYUv2; dipakai untuk mengevaluasi segmentasi RGB-D (mIoU) dan depth (AbsRel/RMSE) pada banyak metode.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 segmentasi | mIoU | benchmark standar indoor |
| NYUv2 depth | AbsRel/RMSE | benchmark depth indoor |
| Anotasi | padat | segmentasi + dukungan |

## Temuan Kunci
- Data RGB-D beranotasi memungkinkan riset scene indoor.
- Kinect membuka akuisisi RGB-D murah.
- Relasi dukungan memperkaya pemahaman.
- Benchmark standar memacu riset.

## Keunggulan
- Benchmark fondasi.
- Anotasi kaya.
- Indoor RGB-D.

## Keterbatasan
- Skala relatif kecil (1449 beranotasi).
- Kedalaman Kinect berderau.
- Domain indoor saja.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
NYUv2 adalah dataset fondasi yang dipakai banyak entri Segmentasi RGB-D dan Estimasi Kedalaman dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Dataset** yang baik dibaca berdampingan:

- [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)
- [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)
- [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)
- [145 - 2020 - nuScenes - Dataset](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)
- [146 - 2014 - Microsoft COCO - Dataset](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Dataset** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Dataset)
Istilah penting untuk memahami makalah ini:

- **Benchmark** — Dataset+metrik standar untuk evaluasi adil.
- **Anotasi** — Label ground-truth (box, mask, pose, depth).
- **RGB-D** — Data warna berpasangan kedalaman.
- **Split train/val/test** — Pembagian data pelatihan/evaluasi.
- **Metrik** — Ukuran kinerja (mAP, mIoU, AbsRel).
- **Sensor** — Perangkat akuisisi (Kinect, LiDAR, stereo).
- **Skala** — Jumlah citra/instance.
- **Kelas/kategori** — Jenis objek yang dilabeli.
- **Kalibrasi** — Parameter intrinsik/ekstrinsik sensor.
- **Generalisasi** — Kemampuan lintas domain.

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
NYU Depth v2 menyediakan dataset RGB-D indoor beranotasi padat (segmentasi + relasi dukungan) dari Kinect, menjadi benchmark standar segmentasi dan estimasi kedalaman indoor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `silberman2012nyu` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 141/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
