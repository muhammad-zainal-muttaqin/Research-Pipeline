# 091 - Multi-View 3D Object Detection Network for Autonomous Driving

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 091 dari 154 |
| Kunci BibTeX | `chen2017mv3d` |
| Judul | Multi-View 3D Object Detection Network for Autonomous Driving |
| Penulis | Chen, Xiaozhi; Ma, Huimin; Wan, Ji; Li, Bo; Xia, Tian |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, multi-view, LiDAR-kamera, BEV, fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Multi-View%203D%20Object%20Detection%20Network%20for%20Autonomous%20Driving
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Multi-View%203D%20Object%20Detection%20Network%20for%20Autonomous%20Driving&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1907--1915 |

## Ringkasan Eksekutif
Pelopor fusi multi-view yang menggabungkan bird's-eye-view LiDAR, front-view LiDAR, dan citra RGB via fusi berbasis region untuk deteksi 3D kendaraan.

## Abstrak (Parafrase)
MV3D (Multi-View 3D) menghasilkan proposal 3D dari representasi bird's-eye-view (BEV) LiDAR, lalu memfusikan fitur dari tiga tampilan — BEV LiDAR, front-view LiDAR, dan citra RGB — melalui deep fusion berbasis region untuk deteksi 3D kendaraan. Ini mempelopori arah fusi LiDAR-kamera pada berkendara otonom.

## Latar Belakang & Konteks
Satu modalitas tak cukup untuk deteksi 3D akurat: LiDAR presisi geometris namun jarang, RGB kaya tekstur namun tanpa kedalaman; keduanya perlu dipadukan.

## Permasalahan yang Diangkat
- Satu modalitas tak cukup untuk deteksi 3D akurat.
- LiDAR jarang, RGB tanpa kedalaman.
- Menyelaraskan multi-view sulit.
- Proposal 3D berkualitas dibutuhkan.
- Fusi region-wise belum matang.

## Tujuan & Pertanyaan Penelitian
- Menghasilkan proposal 3D dari BEV LiDAR.
- Memfusikan fitur multi-view (LiDAR+RGB).
- Meningkatkan deteksi 3D kendaraan.

## Tinjauan Terdahulu / Posisi Literatur
MV3D pelopor fusi multi-view LiDAR-kamera.

Karya/konsep pembanding yang relevan:

- LiDAR BEV/front-view — representasi.
- RGB image — tekstur.
- Faster R-CNN — proposal/fusi region.
- Deep fusion — penggabungan fitur.

## Metodologi & Arsitektur
BEV LiDAR menghasilkan proposal 3D; fitur dari BEV, front-view LiDAR, dan RGB di-crop per-region (ROI) lalu difusikan secara deep (region-wise) berulang; head menghasilkan deteksi 3D. Fokus kelas kendaraan.

Komponen / langkah metodologis utama:

- Proposal 3D dari BEV LiDAR.
- Tiga tampilan: BEV LiDAR, front-view LiDAR, RGB.
- Deep fusion region-wise (ROI).
- Penggabungan fitur berulang.
- Deteksi box 3D kendaraan.
- Berbasis Faster R-CNN.

## Kontribusi Utama
1. Pelopor fusi multi-view LiDAR-kamera.
2. Proposal dari BEV LiDAR efektif.
3. Deep fusion region-wise.
4. Mendasari arah fusi 3D berkendara.

## Rincian Eksperimen
Diuji pada KITTI 3D (kendaraan) dengan metrik AP 3D/BEV, dibandingkan metode single-modal.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D (mobil) | AP 3D | pelopor fusi, kompetitif saat rilis |
| KITTI BEV | AP BEV | kuat |
| Ablation | multi-view | fusi > single-modal |

## Temuan Kunci
- Fusi multi-view mengungguli single-modal.
- BEV LiDAR baik untuk proposal 3D.
- Deep fusion region-wise efektif.
- Penyelarasan multi-view penting.

## Keunggulan
- Pelopor fusi 3D.
- Multi-view efektif.
- Mendasari arah riset.

## Keterbatasan
- Fokus kelas kendaraan.
- Objek kecil lemah.
- Fusi region-wise relatif berat.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
MV3D mendasari arah fusi LiDAR-kamera dalam klaster Deteksi 3D; menegaskan prinsip memadukan geometri dan tekstur yang relevan bagi fusi RGB+Depth.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
- [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)
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
MV3D mempelopori fusi multi-view LiDAR-kamera dengan proposal BEV dan deep fusion region-wise untuk deteksi 3D kendaraan, mendasari arah fusi sensor pada berkendara otonom.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `chen2017mv3d` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 091/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
