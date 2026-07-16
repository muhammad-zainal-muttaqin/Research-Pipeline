# 090 - Frustum PointNets for 3D Object Detection from RGB-D Data

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 090 dari 154 |
| Kunci BibTeX | `qi2018frustum` |
| Judul | Frustum PointNets for 3D Object Detection from RGB-D Data |
| Penulis | Qi, Charles R.; Liu, Wei; Wu, Chenxia; Su, Hao; Guibas, Leonidas J. |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, RGB-D, frustum, PointNet, fusi kaskade |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Frustum%20PointNets%20for%203D%20Object%20Detection%20from%20RGB-D%20Data
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Frustum%20PointNets%20for%203D%20Object%20Detection%20from%20RGB-D%20Data&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 918--927 |

## Ringkasan Eksekutif
Metode deteksi 3D yang memakai deteksi 2D RGB untuk membangkitkan frustum 3D lalu PointNet mensegmentasi dan meregresi box di dalam frustum — contoh kanonik fusi RGB (2D) + kedalaman (3D).

## Abstrak (Parafrase)
Frustum PointNets memanfaatkan detektor 2D matang pada citra RGB untuk menghasilkan proposal 2D, lalu memproyeksikannya menjadi frustum 3D pada point cloud. Di dalam frustum, PointNet melakukan instance segmentation (memisahkan objek dari latar) dan meregresi box 3D beorientasi. Pendekatan kaskade ini efisien dan SOTA pada KITTI serta SUN RGB-D saat rilis.

## Latar Belakang & Konteks
Mencari objek di seluruh ruang 3D mahal; deteksi 2D RGB yang matang dapat mempersempit pencarian secara efisien, memadukan tekstur dan geometri.

## Permasalahan yang Diangkat
- Pencarian objek di seluruh ruang 3D mahal.
- Point cloud jarang menyulitkan lokalisasi langsung.
- Tekstur RGB & geometri 3D perlu dipadukan.
- Deteksi 3D real-time sulit.
- Objek dalam frustum perlu dipisah dari latar.

## Tujuan & Pertanyaan Penelitian
- Membangkitkan frustum 3D dari deteksi 2D RGB.
- Mensegmentasi & meregresi box dalam frustum (PointNet).
- Memadukan tekstur RGB dan geometri kedalaman.

## Tinjauan Terdahulu / Posisi Literatur
Frustum PointNets menggabungkan deteksi 2D matang dan PointNet.

Karya/konsep pembanding yang relevan:

- Detektor 2D (Faster R-CNN) — proposal.
- PointNet — segmentasi/regresi 3D.
- Frustum proposal — dari 2D ke 3D.
- Dataset KITTI/SUN RGB-D.

## Metodologi & Arsitektur
Detektor 2D menghasilkan box pada citra RGB; box diproyeksikan menjadi frustum 3D (memakai kalibrasi/kedalaman); PointNet mensegmentasi instance dalam frustum; T-Net + PointNet meregresi box 3D beorientasi. Kaskade RGB->3D.

Komponen / langkah metodologis utama:

- Deteksi 2D RGB menghasilkan proposal.
- Proyeksi ke frustum 3D (point cloud).
- Instance segmentation dalam frustum (PointNet).
- T-Net untuk normalisasi & estimasi box 3D.
- Regresi box 3D beorientasi.
- Fusi kaskade RGB + kedalaman.

## Kontribusi Utama
1. Fusi kaskade RGB (2D) + point cloud (3D).
2. Frustum mempersempit pencarian 3D efisien.
3. PointNet memisahkan objek dalam frustum.
4. SOTA KITTI & SUN RGB-D saat rilis.

## Rincian Eksperimen
Diuji pada KITTI (outdoor LiDAR) dan SUN RGB-D (indoor RGB-D) dengan metrik AP 3D, dibandingkan metode 3D lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D | AP 3D | SOTA saat rilis |
| SUN RGB-D | AP 3D | SOTA indoor saat rilis |
| Efisiensi | frustum | mempersempit pencarian 3D |

## Temuan Kunci
- Deteksi 2D matang mempercepat deteksi 3D.
- Frustum efektif mempersempit ruang cari.
- PointNet baik untuk segmentasi frustum.
- Fusi RGB+kedalaman kaskade efektif.

## Keunggulan
- Contoh kanonik fusi RGB-D.
- Efisien (frustum).
- SOTA indoor & outdoor.

## Keterbatasan
- Bergantung kualitas deteksi 2D.
- Error 2D merambat ke 3D.
- Kaskade (bukan end-to-end penuh).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Frustum PointNets adalah contoh kanonik fusi RGB (2D) + kedalaman (3D) yang secara konseptual paralel dengan pipeline YOLO+RGB-D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
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
Frustum PointNets memakai deteksi 2D RGB untuk membangkitkan frustum 3D lalu PointNet mensegmentasi dan meregresi box, menjadi contoh kanonik fusi kaskade RGB + kedalaman untuk deteksi 3D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `qi2018frustum` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 090/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
