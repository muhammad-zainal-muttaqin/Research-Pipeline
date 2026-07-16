# 144 - Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 144 dari 154 |
| Kunci BibTeX | `geiger2012kitti` |
| Judul | Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite |
| Penulis | Geiger, Andreas; Lenz, Philip; Urtasun, Raquel |
| Tahun | 2012 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Dataset |
| Kata kunci | dataset, berkendara, stereo/LiDAR, deteksi 3D, benchmark |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Are%20We%20Ready%20for%20Autonomous%20Driving%3F%20The%20KITTI%20Vision%20Benchmark%20Suite
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Are%20We%20Ready%20for%20Autonomous%20Driving%3F%20The%20KITTI%20Vision%20Benchmark%20Suite&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 3354--3361 |

## Ringkasan Eksekutif
Benchmark visi berkendara otonom dengan data stereo, LiDAR, dan GPS untuk deteksi/tracking, odometry, dan depth — paling berpengaruh untuk persepsi berkendara.

## Abstrak (Parafrase)
KITTI (Geiger dkk.) menyediakan data berkendara dunia-nyata terkalibrasi: kamera stereo, LiDAR Velodyne, dan GPS/IMU, dengan tugas deteksi objek 2D/3D, tracking, visual odometry, dan estimasi kedalaman. Ia menjadi benchmark rujukan paling berpengaruh untuk persepsi berkendara otonom.

## Latar Belakang & Konteks
Riset berkendara otonom membutuhkan benchmark dunia-nyata multi-sensor terkalibrasi yang sebelumnya tidak tersedia.

## Permasalahan yang Diangkat
- Riset berkendara butuh benchmark dunia-nyata.
- Data multi-sensor terkalibrasi diperlukan.
- Tugas beragam (deteksi/odometry/depth).
- Ground-truth 3D (LiDAR) penting.
- Standarisasi evaluasi diperlukan.

## Tujuan & Pertanyaan Penelitian
- Menyediakan data berkendara multi-sensor terkalibrasi.
- Menyediakan tugas deteksi 2D/3D, odometry, depth.
- Menstandarkan evaluasi persepsi berkendara.

## Tinjauan Terdahulu / Posisi Literatur
KITTI menyediakan dataset berkendara terkalibrasi.

Karya/konsep pembanding yang relevan:

- Kamera stereo — RGB/depth.
- Velodyne LiDAR — point cloud.
- GPS/IMU — pose.
- Tugas deteksi/odometry/depth.

## Metodologi & Arsitektur
Kendaraan dilengkapi kamera stereo, LiDAR Velodyne, dan GPS/IMU merekam data berkendara; anotasi kotak 2D/3D dan ground-truth odometry/depth disediakan; benchmark untuk deteksi, tracking, odometry, dan estimasi kedalaman.

Komponen / langkah metodologis utama:

- Kamera stereo + Velodyne LiDAR + GPS/IMU.
- Anotasi kotak 2D/3D.
- Tugas deteksi/tracking.
- Visual odometry.
- Estimasi kedalaman (depth).
- Data berkendara terkalibrasi.

## Kontribusi Utama
1. Benchmark berkendara multi-sensor terkalibrasi.
2. Tugas beragam (deteksi 3D/odometry/depth).
3. Ground-truth LiDAR untuk 3D.
4. Paling berpengaruh untuk persepsi berkendara.

## Rincian Eksperimen
Menyediakan benchmark KITTI untuk deteksi 3D (AP 3D), odometry, dan depth, dirujuk hampir semua metode berkendara.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI deteksi 3D | AP 3D | benchmark rujukan |
| KITTI depth/odometry | metrik | benchmark standar |
| Sensor | stereo/LiDAR/GPS | terkalibrasi |

## Temuan Kunci
- Benchmark multi-sensor memacu riset berkendara.
- LiDAR memberi ground-truth 3D.
- Tugas beragam mendorong metode serbaguna.
- Standar evaluasi penting.

## Keunggulan
- Benchmark fondasi berkendara.
- Multi-sensor.
- Tugas beragam.

## Keterbatasan
- Skala lebih kecil dari dataset modern (nuScenes).
- Kondisi cuaca terbatas.
- Domain berkendara saja.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
KITTI adalah dataset fondasi paling berpengaruh untuk deteksi 3D, depth, dan pseudo-LiDAR yang dirujuk banyak entri dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Dataset** yang baik dibaca berdampingan:

- [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)
- [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)
- [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)
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
KITTI menyediakan benchmark berkendara otonom multi-sensor (stereo/LiDAR/GPS) untuk deteksi 2D/3D, odometry, dan depth, menjadi rujukan paling berpengaruh untuk persepsi berkendara.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `geiger2012kitti` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 144/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
