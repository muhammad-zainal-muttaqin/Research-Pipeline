# 097 - TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 097 dari 154 |
| Kunci BibTeX | `bai2022transfusion` |
| Judul | TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers |
| Penulis | Bai, Xuyang; Hu, Zeyu; Zhu, Xinge; Huang, Qingqiu; Chen, Yilun; Fu, Hongbo; Tai, Chiew-Lan |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, Transformer, LiDAR-kamera, robust, attention |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=TransFusion%3A%20Robust%20LiDAR-Camera%20Fusion%20for%203D%20Object%20Detection%20with%20Transformers
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=TransFusion%3A%20Robust%20LiDAR-Camera%20Fusion%20for%203D%20Object%20Detection%20with%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1090--1099 |

## Ringkasan Eksekutif
Detektor 3D berbasis Transformer yang memfusikan LiDAR dan kamera secara robust: query dari LiDAR lalu attention lunak ke fitur citra, tahan misalignment/kalibrasi.

## Abstrak (Parafrase)
TransFusion memakai decoder Transformer dua-tahap untuk fusi LiDAR-kamera: object query diinisialisasi dari fitur LiDAR (tahap 1), lalu attention lunak (soft-association) mengambil informasi dari fitur citra secara adaptif per-query (tahap 2). Karena asosiasi dipelajari (bukan proyeksi keras), TransFusion tahan terhadap misalignment kalibrasi dan degradasi sensor, SOTA robust pada nuScenes/Waymo.

## Latar Belakang & Konteks
Fusi keras (hard association via proyeksi) LiDAR-kamera rapuh terhadap kesalahan kalibrasi dan kondisi buruk (kamera gelap/kabur), menurunkan kinerja.

## Permasalahan yang Diangkat
- Fusi keras (proyeksi) rapuh terhadap kalibrasi.
- Kondisi buruk (gelap/kabur) merusak fusi keras.
- Asosiasi LiDAR-kamera perlu adaptif.
- Degradasi satu sensor menurunkan kinerja.
- Robustness fusi diperlukan.

## Tujuan & Pertanyaan Penelitian
- Memfusikan LiDAR-kamera via attention lunak.
- Membuat asosiasi dipelajari (bukan proyeksi keras).
- Meningkatkan robustness terhadap degradasi.

## Tinjauan Terdahulu / Posisi Literatur
TransFusion membawa Transformer ke fusi 3D.

Karya/konsep pembanding yang relevan:

- DETR — decoder Transformer (query).
- Fusi LiDAR-kamera — target.
- Soft association — attention lunak.
- Dataset nuScenes/Waymo.

## Metodologi & Arsitektur
Tahap 1: object query diinisialisasi dari fitur LiDAR (BEV) dan menghasilkan deteksi awal. Tahap 2: cross-attention dari query ke fitur citra (soft, adaptif lokasi) menambah informasi tekstur; image guidance membantu query sulit. Robust terhadap misalignment.

Komponen / langkah metodologis utama:

- Decoder Transformer dua-tahap.
- Object query dari fitur LiDAR (BEV).
- Soft cross-attention ke fitur citra.
- Asosiasi LiDAR-kamera dipelajari (adaptif).
- Image-guided query initialization.
- Robust terhadap kalibrasi/degradasi.

## Kontribusi Utama
1. Fusi LiDAR-kamera berbasis attention lunak.
2. Robust terhadap misalignment/degradasi sensor.
3. Query dari LiDAR + attention ke citra.
4. SOTA robust pada nuScenes/Waymo.

## Rincian Eksperimen
Diuji pada nuScenes dan Waymo dengan metrik NDS/mAP, termasuk skenario degradasi sensor (kalibrasi buruk, kamera hilang).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| nuScenes | NDS/mAP | SOTA saat rilis |
| Waymo | mAP | kuat |
| Degradasi sensor | robustness | tahan misalignment/kehilangan |

## Temuan Kunci
- Attention lunak lebih robust dari proyeksi keras.
- Asosiasi dipelajari menangani misalignment.
- Query dari LiDAR memberi dasar geometris kuat.
- Robustness penting untuk keselamatan.

## Keunggulan
- Robust terhadap degradasi.
- Fusi berbasis attention.
- SOTA robust.

## Keterbatasan
- Transformer menambah komputasi.
- Bergantung fitur LiDAR untuk query.
- Kompleksitas dua-tahap.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
TransFusion menegaskan fusi berbasis attention yang tahan-gangguan — prinsip robustness fusi yang relevan bagi fusi RGB+Depth dalam tinjauan.

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
TransFusion memakai decoder Transformer dengan query dari LiDAR dan soft attention ke citra, menghasilkan fusi LiDAR-kamera yang robust terhadap misalignment dan degradasi sensor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `bai2022transfusion` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 097/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
