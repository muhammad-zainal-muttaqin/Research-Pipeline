# 096 - Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 096 dari 154 |
| Kunci BibTeX | `you2020pseudolidarpp` |
| Judul | Pseudo-LiDAR++: Accurate Depth for 3D Object Detection in Autonomous Driving |
| Penulis | You, Yurong; Wang, Yan; Chao, Wei-Lun; Garg, Divyansh; Pleiss, Geoff; Hariharan, Bharath; Campbell, Mark; Weinberger, Kilian Q. |
| Tahun | 2020 |
| Venue / Jurnal | International Conference on Learning Representations (ICLR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, stereo depth, koreksi LiDAR sparse, jarak jauh, kamera |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-deteksi-3d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Pseudo-LiDAR%2B%2B%3A%20Accurate%20Depth%20for%203D%20Object%20Detection%20in%20Autonomous%20Driving
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Pseudo-LiDAR%2B%2B%3A%20Accurate%20Depth%20for%203D%20Object%20Detection%20in%20Autonomous%20Driving&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Penyempurnaan Pseudo-LiDAR yang memperbaiki akurasi depth (terutama jarak jauh) via jaringan stereo khusus dan koreksi memakai sedikit titik LiDAR murah.

## Abstrak (Parafrase)
Pseudo-LiDAR++ mengatasi kelemahan Pseudo-LiDAR pada objek jauh dengan: (1) stereo depth network yang dioptimalkan untuk objek (bukan piksel), dan (2) depth correction memakai LiDAR sparse (mis. 4-beam murah) untuk mengoreksi bias jarak. Hasilnya mendekati akurasi LiDAR penuh dengan biaya jauh lebih rendah.

## Latar Belakang & Konteks
Depth stereo tidak akurat pada jarak jauh, membatasi Pseudo-LiDAR untuk objek jauh yang penting bagi berkendara aman.

## Permasalahan yang Diangkat
- Depth stereo tak akurat pada jarak jauh.
- Objek jauh penting untuk berkendara aman.
- Pseudo-LiDAR terbatas oleh error depth jauh.
- LiDAR penuh mahal.
- Bias skala depth perlu dikoreksi.

## Tujuan & Pertanyaan Penelitian
- Meningkatkan akurasi depth objek jauh.
- Mengoreksi depth dengan LiDAR sparse murah.
- Mendekati akurasi LiDAR penuh secara ekonomis.

## Tinjauan Terdahulu / Posisi Literatur
Pseudo-LiDAR++ menyempurnakan Pseudo-LiDAR.

Karya/konsep pembanding yang relevan:

- Pseudo-LiDAR — pendahulu.
- Stereo depth network — dioptimasi objek.
- Sparse LiDAR (4-beam) — koreksi.
- Dataset KITTI.

## Metodologi & Arsitektur
Stereo depth network dilatih dengan loss berorientasi objek (bukan piksel) untuk akurasi objek jauh; graph-based depth correction memakai titik LiDAR sparse (4-beam) untuk mengoreksi/menyelaraskan depth; point cloud hasil diproses detektor 3D.

Komponen / langkah metodologis utama:

- Stereo depth network dioptimasi objek.
- Loss berorientasi objek (bukan piksel).
- Depth correction via LiDAR sparse (4-beam).
- Graph-based propagation koreksi.
- Point cloud pseudo-LiDAR yang ditingkatkan.
- Detektor 3D LiDAR hilir.

## Kontribusi Utama
1. Akurasi depth objek jauh membaik.
2. Koreksi LiDAR sparse murah efektif.
3. Mendekati akurasi LiDAR penuh.
4. Deteksi 3D kamera ekonomis membaik.

## Rincian Eksperimen
Diuji pada KITTI 3D dengan metrik AP 3D, membandingkan stereo-only, dengan koreksi LiDAR sparse, dan LiDAR penuh.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D (stereo) | AP 3D | peningkatan atas Pseudo-LiDAR |
| + LiDAR sparse | AP 3D | mendekati LiDAR penuh |
| Biaya | sensor | jauh lebih murah dari LiDAR penuh |

## Temuan Kunci
- Loss berorientasi objek memperbaiki depth jauh.
- LiDAR sparse murah cukup untuk koreksi.
- Celah kamera-vs-LiDAR menyempit.
- Ekonomis untuk deteksi 3D akurat.

## Keunggulan
- Depth jauh membaik.
- Koreksi murah efektif.
- Mendekati LiDAR penuh.

## Keterbatasan
- Masih butuh sedikit LiDAR (versi terkoreksi).
- Bergantung kualitas stereo.
- Kompleksitas koreksi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Pseudo-LiDAR++ mempersempit celah kamera vs LiDAR untuk deteksi 3D ekonomis — relevan bagi tema memanfaatkan kedalaman murah dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
- [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)
- [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md)
- [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md)
- [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md)
- [094 - 2020 - 3D-CVF - Deteksi 3D](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Deteksi 3D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Deteksi 3D)
Istilah penting untuk memahami makalah ini:

- **Deteksi 3D** — Prediksi kotak 3D beorientasi (x,y,z,l,w,h,yaw).
- **LiDAR** — Sensor laser menghasilkan point cloud akurat.
- **BEV** — Bird's-Eye View; proyeksi tampak-atas.
- **Voxel/pillar** — Diskretisasi point cloud ke sel 3D / kolom.
- **Fusi LiDAR-kamera** — Penggabungan geometri LiDAR dan tekstur kamera.
- **Frustum** — Volume 3D dibatasi deteksi 2D pada citra.
- **Pseudo-LiDAR** — Point cloud dari depth kamera.
- **KITTI/nuScenes** — Benchmark deteksi 3D berkendara.
- **AP 3D / NDS** — Metrik deteksi 3D (NDS khusus nuScenes).
- **Kalibrasi sensor** — Penyelarasan koordinat antar-sensor.

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
Pseudo-LiDAR++ memperbaiki depth objek jauh via stereo network berorientasi objek dan koreksi LiDAR sparse, mendekati akurasi LiDAR penuh untuk deteksi 3D dengan biaya jauh lebih rendah.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `you2020pseudolidarpp` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 096/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
