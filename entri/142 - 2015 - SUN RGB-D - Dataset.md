# 142 - SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 142 dari 154 |
| Kunci BibTeX | `song2015sunrgbd` |
| Judul | SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite |
| Penulis | Song, Shuran; Lichtenberg, Samuel P.; Xiao, Jianxiong |
| Tahun | 2015 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Dataset |
| Kata kunci | dataset, RGB-D, indoor, deteksi 3D, scene understanding |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=SUN%20RGB-D%3A%20A%20RGB-D%20Scene%20Understanding%20Benchmark%20Suite
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=SUN%20RGB-D%3A%20A%20RGB-D%20Scene%20Understanding%20Benchmark%20Suite&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 567--576 |

## Ringkasan Eksekutif
Benchmark pemahaman scene RGB-D indoor berskala dengan anotasi 2D/3D (box 3D, layout, segmentasi) dari empat sensor.

## Abstrak (Parafrase)
SUN RGB-D (Song dkk.) menyediakan ~10 ribu citra RGB-D indoor dengan anotasi kaya: kotak 3D beorientasi, layout ruangan, dan segmentasi, direkam dari empat jenis sensor RGB-D. Ia menjadi benchmark standar untuk deteksi objek 3D indoor dan pemahaman scene.

## Latar Belakang & Konteks
Benchmark RGB-D indoor untuk deteksi 3D dan pemahaman scene masih terbatas skala dan kelengkapan anotasi.

## Permasalahan yang Diangkat
- Benchmark RGB-D indoor terbatas skala.
- Anotasi 3D (box/layout) mahal.
- Deteksi 3D indoor butuh data kaya.
- Ragam sensor perlu dicakup.
- Pemahaman scene menyeluruh diperlukan.

## Tujuan & Pertanyaan Penelitian
- Menyediakan citra RGB-D indoor berskala.
- Melabeli box 3D, layout, segmentasi.
- Menyediakan benchmark deteksi 3D/scene indoor.

## Tinjauan Terdahulu / Posisi Literatur
SUN RGB-D menyediakan dataset RGB-D beranotasi kaya berskala.

Karya/konsep pembanding yang relevan:

- Sensor RGB-D (empat jenis).
- Anotasi box 3D & layout.
- Segmentasi semantik.
- Deteksi 3D indoor.

## Metodologi & Arsitektur
~10k citra RGB-D dari empat sensor dianotasi dengan kotak 3D beorientasi, layout ruangan, dan segmentasi; menyediakan tugas deteksi 3D, estimasi layout, dan segmentasi; benchmark dengan protokol evaluasi.

Komponen / langkah metodologis utama:

- ~10k citra RGB-D indoor.
- Anotasi kotak 3D beorientasi.
- Anotasi layout ruangan.
- Segmentasi semantik.
- Empat jenis sensor RGB-D.
- Benchmark deteksi 3D/scene.

## Kontribusi Utama
1. Dataset RGB-D indoor berskala & kaya.
2. Anotasi 2D/3D lengkap (box 3D/layout/segmentasi).
3. Multi-sensor.
4. Benchmark standar deteksi 3D indoor.

## Rincian Eksperimen
Menyediakan benchmark SUN RGB-D untuk deteksi 3D (mAP 3D), segmentasi (mIoU), dan estimasi layout.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| SUN RGB-D deteksi 3D | mAP 3D | benchmark standar indoor |
| Segmentasi | mIoU | benchmark segmentasi |
| Anotasi | 2D/3D | box 3D/layout/segmentasi |

## Temuan Kunci
- Data RGB-D kaya memungkinkan deteksi 3D indoor.
- Anotasi 3D penting untuk pemahaman scene.
- Multi-sensor meningkatkan generalisasi.
- Benchmark standar memacu riset.

## Keunggulan
- Benchmark fondasi 3D indoor.
- Anotasi lengkap.
- Multi-sensor.

## Keterbatasan
- Kedalaman sensor bervariasi kualitas.
- Domain indoor saja.
- Anotasi 3D terbatas presisi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
SUN RGB-D adalah dataset fondasi utama untuk deteksi 3D dan segmentasi indoor yang dirujuk banyak entri dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Dataset** yang baik dibaca berdampingan:

- [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)
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
SUN RGB-D menyediakan benchmark RGB-D indoor berskala dengan anotasi box 3D, layout, dan segmentasi dari empat sensor, menjadi standar deteksi objek 3D dan pemahaman scene indoor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `song2015sunrgbd` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 142/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
