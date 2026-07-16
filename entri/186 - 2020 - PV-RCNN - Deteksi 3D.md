# 186 - PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 186 dari 191 |
| Kunci BibTeX | `shi2020pvrcnn` |
| Judul | PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection |
| Penulis | Shi, Shaoshuai; Guo, Chaoxu; Jiang, Li; Wang, Zhe; Shi, Jianping; Wang, Xiaogang; Li, Hongsheng |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | 3D detection, point-voxel, set abstraction, LiDAR |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1912.13192
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PV-RCNN%3A%20Point-Voxel%20Feature%20Set%20Abstraction%20for%203D%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PV-RCNN%3A%20Point-Voxel%20Feature%20Set%20Abstraction%20for%203D%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 1912.13192 |

## Ringkasan Eksekutif
PV-RCNN menggabungkan kekuatan representasi voxel (efisien, konteks) dan titik (lokasi presisi) melalui voxel set abstraction, menghasilkan deteksi objek 3D dari point cloud yang sangat akurat.

## Abstrak (Parafrase)
Penulis memadukan konvolusi voxel jarang 3D dengan operasi berbasis titik. Voxel-to-keypoint set abstraction meringkas fitur voxel multiskala ke sejumlah keypoint, lalu RoI-grid pooling mengagregasi fitur keypoint untuk penyempurnaan proposal. Kombinasi point-voxel ini mencapai akurasi SOTA pada KITTI dan Waymo saat rilis.

## Latar Belakang & Konteks
Metode voxel efisien tapi kehilangan presisi lokasi; metode titik presisi tapi mahal. PV-RCNN mengombinasikan keduanya.

## Permasalahan yang Diangkat
- Voxel kehilangan presisi lokasi.
- Point-based mahal/berskala buruk.
- Perlu fitur konteks + presisi.

## Tujuan & Pertanyaan Penelitian
- Menggabungkan fitur voxel dan titik.
- Meringkas konteks ke keypoint.
- Meningkatkan akurasi deteksi 3D.

## Tinjauan Terdahulu / Posisi Literatur
Menyatukan SECOND (voxel jarang) dan PointNet++ (titik); berdialog dengan PointRCNN dan Part-A2.

Karya/konsep pembanding yang relevan:

- SECOND - konvolusi voxel jarang.
- PointRCNN - proposal berbasis titik.
- PointNet++ - set abstraction.
- Part-A2 - bagian objek.

## Metodologi & Arsitektur
Backbone voxel 3D jarang menghasilkan fitur BEV+proposal; voxel set abstraction meringkas fitur multiskala ke keypoint; RoI-grid pooling mengagregasi fitur keypoint untuk refinement box tahap kedua.

Komponen / langkah metodologis utama:

- Konvolusi voxel 3D jarang.
- Voxel-to-keypoint set abstraction.
- RoI-grid pooling pada keypoint.
- Refinement dua-tahap.

## Kontribusi Utama
1. Framework point-voxel terpadu.
2. Voxel set abstraction.
3. RoI-grid pooling.
4. SOTA KITTI/Waymo saat rilis.

## Rincian Eksperimen
KITTI dan Waymo Open Dataset untuk AP 3D (mobil/pejalan/siklus) dan BEV.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI | AP 3D | SOTA saat rilis |
| Waymo | mAP | unggul |
| Ablation | AP | point+voxel > salah satu saja |

## Temuan Kunci
- Kombinasi point-voxel melampaui masing-masing.
- Keypoint meringkas konteks efektif.
- Refinement grid meningkatkan presisi.

## Keunggulan
- Akurasi tinggi.
- Konteks + presisi.
- Backbone kuat.

## Keterbatasan
- Komputasi/memori besar.
- Fokus LiDAR.
- Dua-tahap lebih lambat.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Backbone deteksi 3D presisi untuk point cloud, dapat memproses pseudo-LiDAR dari depth pada pipeline berbasis kamera.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [185 - 2021 - CenterPoint - Deteksi 3D](./185%20-%202021%20-%20CenterPoint%20-%20Deteksi%203D.md)
- [187 - 2022 - BEVFormer - Deteksi 3D](./187%20-%202022%20-%20BEVFormer%20-%20Deteksi%203D.md)
- [188 - 2022 - DETR3D - Deteksi 3D](./188%20-%202022%20-%20DETR3D%20-%20Deteksi%203D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Deteksi 3D** dalam peta tinjauan (17 klaster, 191 entri total).
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
PV-RCNN memadukan fitur point dan voxel untuk deteksi 3D akurat, menjadi arsitektur rujukan pada persepsi LiDAR.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `shi2020pvrcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 186/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
