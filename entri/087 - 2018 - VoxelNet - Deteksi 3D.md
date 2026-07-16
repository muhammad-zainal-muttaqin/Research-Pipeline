# 087 - VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 087 dari 154 |
| Kunci BibTeX | `zhou2018voxelnet` |
| Judul | VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection |
| Penulis | Zhou, Yin; Tuzel, Oncel |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, point cloud, voxel, VFE, LiDAR |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=VoxelNet%3A%20End-to-End%20Learning%20for%20Point%20Cloud%20Based%203D%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=VoxelNet%3A%20End-to-End%20Learning%20for%20Point%20Cloud%20Based%203D%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4490--4499 |

## Ringkasan Eksekutif
Metode deteksi objek 3D end-to-end yang mempelajari fitur dari point cloud mentah via voxel feature encoding lalu RPN 3D.

## Abstrak (Parafrase)
VoxelNet membagi point cloud menjadi voxel 3D dan mempelajari fitur tiap voxel dengan Voxel Feature Encoding (VFE) berbasis PointNet, menghasilkan representasi volumetrik yang diproses konvolusi 3D dan RPN untuk deteksi objek 3D. Ini adalah pipeline end-to-end pertama yang belajar fitur langsung dari point cloud mentah tanpa fitur buatan tangan.

## Latar Belakang & Konteks
Fitur point cloud buatan tangan (statistik lokal) membatasi akurasi deteksi 3D; diperlukan pembelajaran fitur end-to-end dari data mentah.

## Permasalahan yang Diangkat
- Fitur point cloud buatan tangan membatasi akurasi.
- Point cloud tak terstruktur sulit untuk CNN grid.
- Perlu representasi volumetrik yang dipelajari.
- Deteksi 3D end-to-end belum ada.
- Kepadatan titik tidak seragam.

## Tujuan & Pertanyaan Penelitian
- Mempelajari fitur voxel dari point cloud mentah.
- Menyediakan pipeline deteksi 3D end-to-end.
- Menggabungkan VFE dan RPN 3D.

## Tinjauan Terdahulu / Posisi Literatur
VoxelNet menggabungkan PointNet (per-voxel) dan RPN untuk deteksi 3D.

Karya/konsep pembanding yang relevan:

- PointNet — fitur per-titik.
- RPN — proposal (Faster R-CNN).
- Konvolusi 3D.
- Dataset KITTI.

## Metodologi & Arsitektur
Point cloud dipartisi menjadi voxel; VFE layers (PointNet mini) mengekstrak fitur tiap voxel; konvolusi 3D memproses tensor voxel; RPN menghasilkan deteksi 3D (box beorientasi). Dilatih end-to-end.

Komponen / langkah metodologis utama:

- Partisi point cloud menjadi voxel 3D.
- Voxel Feature Encoding (VFE) berbasis PointNet.
- Konvolusi 3D pada tensor voxel.
- Region Proposal Network 3D.
- Deteksi box 3D beorientasi.
- Pelatihan end-to-end.

## Kontribusi Utama
1. Pembelajaran fitur voxel end-to-end dari point cloud.
2. VFE menggantikan fitur buatan tangan.
3. Pipeline deteksi 3D terpadu.
4. Baseline penting deteksi 3D LiDAR.

## Rincian Eksperimen
Diuji pada KITTI 3D (mobil/pejalan/pesepeda) dengan metrik AP 3D/BEV, dibandingkan metode berbasis fitur tangan.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D | AP 3D | baseline end-to-end LiDAR |
| KITTI BEV | AP BEV | kompetitif saat rilis |
| Ablation | VFE | fitur dipelajari > fitur tangan |

## Temuan Kunci
- Fitur voxel dipelajari mengungguli fitur tangan.
- Voxelisasi memungkinkan konvolusi 3D.
- End-to-end menyederhanakan pipeline.
- Konvolusi 3D mahal (motivasi PointPillars).

## Keunggulan
- Pelopor deteksi 3D end-to-end.
- VFE efektif.
- Baseline penting.

## Keterbatasan
- Konvolusi 3D mahal (lambat).
- Voxelisasi kehilangan detail.
- Hanya LiDAR (belum fusi).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
VoxelNet adalah fondasi deteksi 3D berbasis point cloud dalam tinjauan; menetapkan representasi voxel yang menghubungkan geometri kedalaman dan deteksi 3D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
- [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)
- [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md)
- [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md)
- [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md)
- [094 - 2020 - 3D-CVF - Deteksi 3D](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md)
- [095 - 2019 - Pseudo-LiDAR - Deteksi 3D](./095%20-%202019%20-%20Pseudo-LiDAR%20-%20Deteksi%203D.md)

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
VoxelNet mempelajari fitur voxel dari point cloud mentah via VFE dan RPN 3D, menjadi pipeline deteksi 3D end-to-end pelopor yang menggantikan fitur buatan tangan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhou2018voxelnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 087/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
