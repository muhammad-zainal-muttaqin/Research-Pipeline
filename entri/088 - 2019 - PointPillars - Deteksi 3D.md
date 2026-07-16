# 088 - PointPillars: Fast Encoders for Object Detection from Point Clouds

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 088 dari 154 |
| Kunci BibTeX | `lang2019pointpillars` |
| Judul | PointPillars: Fast Encoders for Object Detection from Point Clouds |
| Penulis | Lang, Alex H.; Vora, Sourabh; Caesar, Holger; Zhou, Lubing; Yang, Jiong; Beijbom, Oscar |
| Tahun | 2019 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, pillar, BEV, real-time, LiDAR |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PointPillars%3A%20Fast%20Encoders%20for%20Object%20Detection%20from%20Point%20Clouds
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PointPillars%3A%20Fast%20Encoders%20for%20Object%20Detection%20from%20Point%20Clouds&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 12697--12705 |

## Ringkasan Eksekutif
Metode deteksi 3D yang meng-encode point cloud menjadi kolom vertikal (pillar) 2D sehingga dapat memakai CNN 2D cepat, mencapai deteksi 3D real-time.

## Abstrak (Parafrase)
PointPillars mengorganisasi point cloud menjadi pillar (kolom vertikal pada grid BEV); fitur tiap pillar dipelajari (PointNet mini) lalu disusun menjadi pseudo-image 2D yang diproses backbone 2D CNN dan head deteksi (SSD). Karena menghindari konvolusi 3D mahal, PointPillars sangat cepat (>60 FPS) dengan akurasi kompetitif, menjadi detektor 3D LiDAR populer.

## Latar Belakang & Konteks
Konvolusi 3D (VoxelNet) mahal dan lambat, menghambat deteksi 3D real-time yang dibutuhkan berkendara otonom.

## Permasalahan yang Diangkat
- Konvolusi 3D (VoxelNet) mahal & lambat.
- Deteksi 3D real-time sulit dicapai.
- Representasi voxel 3D boros komputasi.
- Point cloud tak terstruktur untuk CNN 2D.
- Kebutuhan efisiensi untuk berkendara.

## Tujuan & Pertanyaan Penelitian
- Meng-encode point cloud menjadi pillar 2D.
- Memakai CNN 2D cepat (hindari konvolusi 3D).
- Mencapai deteksi 3D real-time.

## Tinjauan Terdahulu / Posisi Literatur
PointPillars menyederhanakan VoxelNet ke representasi pillar.

Karya/konsep pembanding yang relevan:

- VoxelNet — voxel 3D (pembanding).
- PointNet — fitur pillar.
- SSD — head deteksi.
- BEV representation.

## Metodologi & Arsitektur
Point cloud dikelompokkan ke pillar pada grid BEV; PointNet mini mengekstrak fitur tiap pillar; fitur disusun menjadi pseudo-image 2D; backbone 2D CNN + SSD head menghasilkan deteksi 3D. Tanpa konvolusi 3D.

Komponen / langkah metodologis utama:

- Pillar feature encoding (kolom vertikal).
- PointNet mini per-pillar.
- Pseudo-image 2D (BEV).
- Backbone 2D CNN.
- SSD detection head.
- Deteksi 3D real-time.

## Kontribusi Utama
1. Representasi pillar menghindari konvolusi 3D mahal.
2. Deteksi 3D real-time (>60 FPS).
3. Akurasi kompetitif.
4. Fondasi banyak pipeline fusi berikutnya.

## Rincian Eksperimen
Diuji pada KITTI dan nuScenes dengan metrik AP 3D/BEV/NDS dan kecepatan, dibandingkan VoxelNet dan metode lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D | AP 3D | kompetitif |
| nuScenes | NDS | kuat |
| Kecepatan | FPS | >60 FPS (real-time) |

## Temuan Kunci
- Representasi pillar 2D sangat efisien.
- CNN 2D cukup untuk deteksi 3D BEV.
- Trade-off kecepatan-akurasi unggul.
- Menjadi backbone fusi populer.

## Keunggulan
- Real-time & efisien.
- Akurasi kompetitif.
- Populer & mudah diperluas.

## Keterbatasan
- Kehilangan detail vertikal (pillar).
- LiDAR-only (butuh fusi untuk tekstur).
- Objek kecil menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PointPillars adalah detektor 3D LiDAR real-time yang menjadi basis banyak pipeline fusi LiDAR-kamera dalam tinjauan (mis. PointPainting).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
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
PointPillars meng-encode point cloud menjadi pillar 2D untuk memakai CNN 2D cepat, mencapai deteksi 3D real-time dengan akurasi kompetitif dan menjadi fondasi banyak pipeline fusi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lang2019pointpillars` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 088/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
