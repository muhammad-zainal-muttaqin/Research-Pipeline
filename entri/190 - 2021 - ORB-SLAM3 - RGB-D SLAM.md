# 190 - ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 190 dari 191 |
| Kunci BibTeX | `campos2021orbslam3` |
| Judul | ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM |
| Penulis | Campos, Carlos; Elvira, Richard; G{\'o |
| Tahun | 2021 |
| Venue / Jurnal | IEEE Transactions on Robotics |
| Tema klaster | RGB-D SLAM |
| Kata kunci | visual-inertial SLAM, multi-map, RGB-D, loop closure |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-slam)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2007.11898
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ORB-SLAM3%3A%20An%20Accurate%20Open-Source%20Library%20for%20Visual%2C%20Visual-Inertial%2C%20and%20Multimap%20SLAM
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ORB-SLAM3%3A%20An%20Accurate%20Open-Source%20Library%20for%20Visual%2C%20Visual-Inertial%2C%20and%20Multimap%20SLAM&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 37 |
| Nomor | 6 |
| Halaman | 1874--1890 |
| arXiv | 2007.11898 |

## Ringkasan Eksekutif
ORB-SLAM3 adalah sistem SLAM serba-lengkap yang menyatukan mode visual, visual-inertial, dan multi-map (Atlas) untuk kamera monokular, stereo, dan RGB-D, dengan penempatan-ulang (relocalization) dan penggabungan peta yang tangguh.

## Abstrak (Parafrase)
Penulis memperluas ORB-SLAM2 dengan integrasi inersia erat (tightly-coupled visual-inertial) berbasis Maximum-a-Posteriori sejak inisialisasi, serta sistem multi-map Atlas yang mempertahankan dan menggabungkan banyak submap saat tracking hilang. Mendukung model kamera pinhole dan fisheye, ORB-SLAM3 mencapai akurasi SOTA dan robustnes tinggi pada berbagai dataset dan modalitas termasuk RGB-D.

## Latar Belakang & Konteks
Kehilangan tracking dan penggabungan sesi peta adalah tantangan SLAM praktis; integrasi inersia meningkatkan robustnes pada gerak cepat.

## Permasalahan yang Diangkat
- Tracking hilang memutus peta.
- Inisialisasi visual-inertial sulit.
- Menggabungkan multi-sesi/peta.

## Tujuan & Pertanyaan Penelitian
- Menyatukan visual, VI, dan multi-map.
- Inisialisasi VI berbasis MAP yang cepat.
- Robust relocalization + map merging.

## Tinjauan Terdahulu / Posisi Literatur
Kelanjutan ORB-SLAM2; berdialog dengan VINS-Mono/Fusion (visual-inertial).

Karya/konsep pembanding yang relevan:

- ORB-SLAM2 - SLAM fitur mono/stereo/RGB-D.
- VINS-Fusion - visual-inertial.
- DSO - direct sparse odometry.
- Bundle adjustment - optimasi peta.

## Metodologi & Arsitektur
Front-end fitur ORB; inisialisasi visual-inertial MAP; Atlas menyimpan banyak submap aktif/non-aktif; place recognition untuk relocalization dan penggabungan peta; optimasi bundle adjustment/pose graph.

Komponen / langkah metodologis utama:

- Visual-inertial tightly-coupled (MAP init).
- Sistem multi-map Atlas.
- Place recognition tangguh (relocalize/merge).
- Dukungan pinhole & fisheye, mono/stereo/RGB-D.

## Kontribusi Utama
1. SLAM terpadu VI + multi-map.
2. Inisialisasi VI cepat berbasis MAP.
3. Map merging antar-sesi.
4. Akurasi/robustnes SOTA lintas modalitas.

## Rincian Eksperimen
EuRoC, TUM-VI, dan dataset RGB-D untuk ATE (akurasi trajektori) dan uji robustnes.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| EuRoC (VI) | ATE | SOTA saat rilis |
| TUM-VI | ATE | akurat & robust |
| RGB-D | ATE | kompetitif |

## Temuan Kunci
- Integrasi inersia meningkatkan robustnes.
- Multi-map menyelamatkan tracking hilang.
- Satu sistem melayani banyak modalitas/sensor.

## Keunggulan
- Serbaguna (mono/stereo/RGB-D/VI).
- Robust relocalize/merge.
- Akurasi tinggi, open-source.

## Keterbatasan
- Fitur (rentan tekstur miskin/dinamis).
- Objek bergerak tak ditangani eksplisit.
- Penyetelan parameter kompleks.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Fondasi SLAM RGB-D modern; menjadi basis banyak sistem SLAM semantik/dinamis yang menambah deteksi (mis. YOLO) untuk lingkungan dinamis.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [191 - 2021 - DROID-SLAM - RGB-D SLAM](./191%20-%202021%20-%20DROID-SLAM%20-%20RGB-D%20SLAM.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SLAM** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SLAM)
Istilah penting untuk memahami makalah ini:

- **SLAM** — Simultaneous Localization and Mapping.
- **RGB-D SLAM** — SLAM kamera warna+kedalaman (skala metrik).
- **Lingkungan dinamis** — Scene dengan objek bergerak.
- **Loop closure** — Pengenalan tempat untuk koreksi drift.
- **Bundle adjustment** — Optimasi bersama pose dan titik peta.
- **ATE/RPE** — Absolute/Relative Trajectory/Pose Error.
- **Semantic SLAM** — SLAM memanfaatkan label semantik.
- **Fitur ORB** — Fitur cepat rotasi-invarian.
- **TUM RGB-D** — Benchmark SLAM RGB-D standar.
- **Deteksi objek dinamis** — Menandai objek bergerak (YOLO/Mask R-CNN).

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
ORB-SLAM3 menyatukan visual, visual-inertial, dan multi-map dalam satu sistem tangguh, tonggak SLAM RGB-D serbaguna.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `campos2021orbslam3` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 190/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
