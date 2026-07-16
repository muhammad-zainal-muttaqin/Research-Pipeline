# 089 - PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 089 dari 154 |
| Kunci BibTeX | `shi2019pointrcnn` |
| Judul | PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud |
| Penulis | Shi, Shaoshuai; Wang, Xiaogang; Li, Hongsheng |
| Tahun | 2019 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, point cloud, dua-tahap, proposal per-titik, KITTI |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PointRCNN%3A%203D%20Object%20Proposal%20Generation%20and%20Detection%20from%20Point%20Cloud
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PointRCNN%3A%203D%20Object%20Proposal%20Generation%20and%20Detection%20from%20Point%20Cloud&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 770--779 |

## Ringkasan Eksekutif
Detektor 3D dua-tahap yang menghasilkan proposal bottom-up langsung dari point cloud per-titik lalu menyempurnakannya di koordinat kanonik.

## Abstrak (Parafrase)
PointRCNN mendeteksi objek 3D dalam dua tahap tanpa voxelisasi kasar: tahap pertama mensegmentasi titik foreground dan menghasilkan proposal 3D per-titik (bottom-up) dari point cloud mentah (PointNet++); tahap kedua mengubah proposal ke koordinat kanonik dan menyempurnakan box. Ini mencapai SOTA LiDAR-only pada KITTI saat rilis.

## Latar Belakang & Konteks
Deteksi 3D memerlukan proposal berkualitas, namun voxelisasi kasar kehilangan detail dan pendekatan anchor 3D boros; proposal langsung dari titik lebih presisi.

## Permasalahan yang Diangkat
- Voxelisasi kasar kehilangan detail geometri.
- Anchor 3D boros dan sulit disetel.
- Proposal 3D berkualitas sulit dihasilkan.
- Point cloud jarang & tak seragam.
- Penyempurnaan box perlu konteks lokal.

## Tujuan & Pertanyaan Penelitian
- Menghasilkan proposal 3D per-titik (bottom-up).
- Menyempurnakan box di koordinat kanonik.
- Meningkatkan presisi deteksi 3D LiDAR-only.

## Tinjauan Terdahulu / Posisi Literatur
PointRCNN menggabungkan PointNet++ dan RPN dua-tahap untuk deteksi 3D.

Karya/konsep pembanding yang relevan:

- PointNet++ — fitur point cloud hierarkis.
- Faster R-CNN — paradigma dua-tahap.
- Foreground segmentation — proposal.
- Canonical refinement — penyempurnaan.

## Metodologi & Arsitektur
Tahap 1: PointNet++ mensegmentasi titik foreground dan tiap titik foreground menghasilkan proposal 3D (bottom-up). Tahap 2: titik dalam proposal ditransformasi ke koordinat kanonik untuk penyempurnaan box (regresi + klasifikasi confidence).

Komponen / langkah metodologis utama:

- Segmentasi foreground per-titik (PointNet++).
- Proposal 3D bottom-up per-titik.
- Transformasi ke koordinat kanonik.
- Penyempurnaan box tahap-2.
- LiDAR-only (point cloud mentah).
- Pelatihan dua-tahap.

## Kontribusi Utama
1. Proposal 3D bottom-up per-titik yang presisi.
2. Penyempurnaan di koordinat kanonik.
3. SOTA LiDAR-only pada KITTI saat rilis.
4. Menghindari voxelisasi kasar.

## Rincian Eksperimen
Diuji pada KITTI 3D dengan metrik AP 3D/BEV, dibandingkan VoxelNet dan metode berbasis voxel/anchor.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D | AP 3D | SOTA LiDAR-only saat rilis |
| KITTI BEV | AP BEV | kuat |
| Ablation | canonical refinement | penyempurnaan menyumbang gain |

## Temuan Kunci
- Proposal berbasis titik lebih presisi dari voxel/anchor.
- Koordinat kanonik memudahkan penyempurnaan.
- Segmentasi foreground kunci proposal.
- Point cloud mentah mempertahankan detail.

## Keunggulan
- Presisi (berbasis titik).
- Dua-tahap kuat.
- SOTA LiDAR-only.

## Keterbatasan
- Dua-tahap relatif lambat.
- LiDAR-only (tanpa tekstur).
- PointNet++ mahal pada scene besar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PointRCNN memperkuat klaster Deteksi 3D dengan pendekatan berbasis titik; menghubungkan geometri kedalaman/point cloud dengan deteksi objek 3D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
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
PointRCNN mendeteksi objek 3D dua-tahap dengan proposal bottom-up per-titik dan penyempurnaan di koordinat kanonik, mencapai SOTA LiDAR-only pada KITTI tanpa voxelisasi kasar.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `shi2019pointrcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 089/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
