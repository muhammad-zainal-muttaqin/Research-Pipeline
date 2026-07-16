# 145 - nuScenes: A Multimodal Dataset for Autonomous Driving

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 145 dari 154 |
| Kunci BibTeX | `caesar2020nuscenes` |
| Judul | nuScenes: A Multimodal Dataset for Autonomous Driving |
| Penulis | Caesar, Holger; Bankiti, Varun; Lang, Alex H.; Vora, Sourabh; Liong, Venice Erin; Xu, Qiang; Krishnan, Anush; Pan, Yu; Baldan, Giancarlo; Beijbom, Oscar |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Dataset |
| Kata kunci | dataset, berkendara, multimodal, 360, fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=nuScenes%3A%20A%20Multimodal%20Dataset%20for%20Autonomous%20Driving
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=nuScenes%3A%20A%20Multimodal%20Dataset%20for%20Autonomous%20Driving&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 11621--11631 |

## Ringkasan Eksekutif
Dataset berkendara otonom multimodal berskala (kamera 360, LiDAR, radar) dengan anotasi 3D penuh dan metrik NDS, benchmark utama fusi sensor.

## Abstrak (Parafrase)
nuScenes (Caesar dkk.) menyediakan 1000 scene berkendara dengan 6 kamera (cakupan 360 derajat), LiDAR, dan 5 radar, beranotasi 3D penuh (kotak 3D, atribut, tracking). Ia memperkenalkan metrik nuScenes Detection Score (NDS) dan menjadi benchmark utama untuk fusi LiDAR-kamera-radar (mis. BEVFusion, TransFusion).

## Latar Belakang & Konteks
KITTI terbatas skala dan cakupan sensor; diperlukan benchmark multimodal lebih besar dengan cakupan 360 derajat dan radar untuk fusi modern.

## Permasalahan yang Diangkat
- KITTI terbatas skala & cakupan sensor.
- Cakupan 360 derajat diperlukan.
- Radar belum tercakup luas.
- Fusi multimodal butuh data besar.
- Metrik komprehensif diperlukan.

## Tujuan & Pertanyaan Penelitian
- Menyediakan dataset multimodal berskala 360 derajat.
- Menyediakan anotasi 3D penuh + tracking.
- Memperkenalkan metrik NDS.

## Tinjauan Terdahulu / Posisi Literatur
nuScenes menyediakan dataset multimodal komprehensif.

Karya/konsep pembanding yang relevan:

- 6 kamera (360) + LiDAR + 5 radar.
- Anotasi 3D penuh.
- Metrik NDS.
- Fusi multimodal (BEVFusion/TransFusion).

## Metodologi & Arsitektur
1000 scene direkam dengan 6 kamera (360), 1 LiDAR, dan 5 radar; anotasi kotak 3D, atribut, dan tracking disediakan; metrik NDS menggabungkan mAP dan galat translasi/skala/orientasi; benchmark deteksi/tracking/fusi.

Komponen / langkah metodologis utama:

- 1000 scene, 6 kamera (360) + LiDAR + 5 radar.
- Anotasi kotak 3D + atribut + tracking.
- Metrik nuScenes Detection Score (NDS).
- Cakupan 360 derajat.
- Data multimodal berskala.
- Benchmark fusi/deteksi/tracking.

## Kontribusi Utama
1. Dataset multimodal berskala 360 derajat.
2. Anotasi 3D penuh + tracking.
3. Metrik NDS komprehensif.
4. Benchmark utama fusi multimodal modern.

## Rincian Eksperimen
Menyediakan benchmark nuScenes untuk deteksi 3D (NDS/mAP), tracking, dan segmentasi BEV; dirujuk metode fusi modern.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| nuScenes deteksi 3D | NDS/mAP | benchmark fusi utama |
| Tracking | AMOTA | benchmark tracking |
| Sensor | kamera 360/LiDAR/radar | multimodal |

## Temuan Kunci
- Multimodal 360 memungkinkan fusi komprehensif.
- Radar menambah modalitas ketiga.
- NDS metrik komprehensif.
- Skala besar memacu metode fusi modern.

## Keunggulan
- Benchmark fusi modern.
- Multimodal 360.
- Metrik NDS.

## Keterbatasan
- Akuisisi/anotasi mahal.
- Domain berkendara saja.
- Radar sparse/berderau.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
nuScenes adalah dataset fondasi modern untuk fusi multimodal berkendara yang dirujuk entri fusi 3D (BEVFusion/TransFusion) dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Dataset** yang baik dibaca berdampingan:

- [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)
- [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)
- [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)
- [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)
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
nuScenes menyediakan dataset berkendara multimodal berskala (kamera 360/LiDAR/radar) dengan anotasi 3D penuh dan metrik NDS, menjadi benchmark utama fusi sensor modern.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `caesar2020nuscenes` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 145/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
