# 092 - Joint 3D Proposal Generation and Object Detection from View Aggregation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 092 dari 154 |
| Kunci BibTeX | `ku2018avod` |
| Judul | Joint 3D Proposal Generation and Object Detection from View Aggregation |
| Penulis | Ku, Jason; Mozifian, Melissa; Lee, Jungwook; Harakeh, Ali; Waslander, Steven L. |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, fusi proposal, BEV, efisien memori, LiDAR-kamera |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Joint%203D%20Proposal%20Generation%20and%20Object%20Detection%20from%20View%20Aggregation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Joint%203D%20Proposal%20Generation%20and%20Object%20Detection%20from%20View%20Aggregation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1--8 |

## Ringkasan Eksekutif
Metode deteksi 3D yang membangkitkan proposal dari fusi fitur BEV LiDAR dan citra RGB pada resolusi tinggi, efisien memori dan akurat pada objek kecil.

## Abstrak (Parafrase)
AVOD (Aggregate View Object Detection) memfusikan fitur BEV LiDAR dan citra RGB pada tahap proposal (bukan hanya deteksi akhir), memakai feature map beresolusi tinggi dan crop-and-resize agar objek kecil (pejalan/pesepeda) terdeteksi baik. Desainnya efisien memori dan akurat pada KITTI.

## Latar Belakang & Konteks
Proposal 3D berkualitas untuk objek kecil membutuhkan fitur beresolusi tinggi; MV3D memfusikan terlalu belakangan dan boros untuk objek kecil.

## Permasalahan yang Diangkat
- Proposal objek kecil butuh fitur resolusi tinggi.
- Fusi hanya di deteksi akhir kurang optimal.
- MV3D boros memori untuk objek kecil.
- Penyelarasan BEV-RGB pada proposal sulit.
- Efisiensi memori diperlukan.

## Tujuan & Pertanyaan Penelitian
- Memfusikan fitur BEV+RGB pada tahap proposal.
- Memakai fitur resolusi tinggi untuk objek kecil.
- Meningkatkan efisiensi memori.

## Tinjauan Terdahulu / Posisi Literatur
AVOD menyempurnakan MV3D dengan fusi pada tahap proposal.

Karya/konsep pembanding yang relevan:

- MV3D — pendahulu fusi multi-view.
- BEV LiDAR + RGB — modalitas.
- Crop-and-resize — penyelarasan fitur.
- RPN 3D — proposal.

## Metodologi & Arsitektur
Fitur BEV LiDAR dan RGB (beresolusi tinggi) difusikan pada RPN untuk menghasilkan proposal 3D; crop-and-resize menyelaraskan fitur; head kedua menyempurnakan box 3D. Fusi awal (proposal) meningkatkan objek kecil dan efisiensi.

Komponen / langkah metodologis utama:

- Fusi fitur multimodal pada RPN 3D.
- Fitur beresolusi tinggi (objek kecil).
- Crop-and-resize penyelarasan fitur.
- Head penyempurnaan box 3D.
- Efisiensi memori.
- BEV LiDAR + RGB.

## Kontribusi Utama
1. Fusi pada tahap proposal (bukan hanya akhir).
2. Akurat pada objek kecil (pejalan/pesepeda).
3. Efisien memori.
4. Memperkuat fusi LiDAR-kamera.

## Rincian Eksperimen
Diuji pada KITTI 3D (mobil/pejalan/pesepeda) dengan metrik AP 3D/BEV, dibandingkan MV3D.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D (mobil) | AP 3D | kompetitif/unggul |
| KITTI (pejalan/pesepeda) | AP 3D | akurat untuk objek kecil |
| Efisiensi | memori | lebih hemat dari MV3D |

## Temuan Kunci
- Fusi pada proposal meningkatkan objek kecil.
- Fitur resolusi tinggi penting.
- Crop-and-resize menyelaraskan fitur.
- Efisiensi memori tercapai.

## Keunggulan
- Akurat objek kecil.
- Efisien memori.
- Fusi pada proposal.

## Keterbatasan
- Bergantung kalibrasi LiDAR-kamera.
- Dua-tahap relatif lambat.
- Fusi BEV kehilangan detail vertikal.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
AVOD memperkuat fusi LiDAR-kamera pada tahap proposal dalam klaster Deteksi 3D; prinsip fusi awal relevan bagi desain fusi RGB+Depth.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
- [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)
- [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md)
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
AVOD membangkitkan proposal 3D dari fusi fitur BEV LiDAR dan RGB beresolusi tinggi, meningkatkan deteksi objek kecil dan efisiensi memori dibanding MV3D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ku2018avod` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 092/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
