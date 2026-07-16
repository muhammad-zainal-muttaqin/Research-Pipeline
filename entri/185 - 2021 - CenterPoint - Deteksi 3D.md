# 185 - Center-Based 3D Object Detection and Tracking

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 185 dari 191 |
| Kunci BibTeX | `yin2021centerpoint` |
| Judul | Center-Based 3D Object Detection and Tracking |
| Penulis | Yin, Tianwei; Zhou, Xingyi; Kr{\"a |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | 3D detection, center-based, LiDAR, tracking |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2006.11275
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Center-Based%203D%20Object%20Detection%20and%20Tracking
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Center-Based%203D%20Object%20Detection%20and%20Tracking&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2006.11275 |

## Ringkasan Eksekutif
CenterPoint mendeteksi dan melacak objek 3D dengan merepresentasikan objek sebagai titik pusat pada Bird's-Eye View, menyederhanakan deteksi 3D anchor-free dan memungkinkan pelacakan berbasis kecepatan yang sederhana namun kuat.

## Abstrak (Parafrase)
Penulis mengangkat paradigma CenterNet ke 3D: dari fitur BEV point cloud, jaringan memprediksi heatmap pusat objek lalu meregresi atribut 3D (ukuran, orientasi, kecepatan). Tahap kedua menyempurnakan box. Representasi berbasis pusat menghindari anchor beorientasi yang rumit dan memberi pelacakan sederhana via perpindahan pusat, mencapai SOTA pada nuScenes dan Waymo.

## Latar Belakang & Konteks
Deteksi 3D berbasis anchor menuntut banyak anchor beorientasi dan penyetelan. Pendekatan berbasis pusat menyederhanakannya.

## Permasalahan yang Diangkat
- Anchor 3D beorientasi rumit.
- Objek berputar sulit dengan box sumbu-selaras.
- Pelacakan 3D perlu disederhanakan.

## Tujuan & Pertanyaan Penelitian
- Deteksi 3D anchor-free berbasis pusat.
- Meregresi atribut 3D dari pusat.
- Menyediakan tracking sederhana.

## Tinjauan Terdahulu / Posisi Literatur
Mengangkat CenterNet (2D) ke 3D; berdialog dengan VoxelNet/PointPillars/SECOND sebagai backbone BEV.

Karya/konsep pembanding yang relevan:

- CenterNet - deteksi 2D berbasis pusat.
- PointPillars - encoder pillar BEV.
- VoxelNet - voxelisasi 3D.
- SECOND - konvolusi jarang 3D.

## Metodologi & Arsitektur
Backbone 3D/pillar menghasilkan fitur BEV; head memprediksi heatmap pusat + regresi (ukuran, yaw, kecepatan, tinggi); tahap refinement kedua memakai fitur titik pada box; tracking via asosiasi pusat + kecepatan.

Komponen / langkah metodologis utama:

- Heatmap pusat objek pada BEV.
- Regresi atribut 3D dari pusat.
- Refinement dua-tahap.
- Tracking berbasis perpindahan pusat.

## Kontribusi Utama
1. Deteksi 3D berbasis pusat (anchor-free).
2. Prediksi kecepatan untuk tracking sederhana.
3. SOTA nuScenes/Waymo saat rilis.
4. Kerangka backbone-agnostik.

## Rincian Eksperimen
nuScenes dan Waymo Open Dataset untuk deteksi (mAP/NDS) dan tracking (AMOTA).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| nuScenes | mAP/NDS | SOTA saat rilis |
| Waymo | mAP | kompetitif/unggul |
| Tracking | AMOTA | sederhana namun kuat |

## Temuan Kunci
- Representasi pusat menyederhanakan deteksi 3D.
- Prediksi kecepatan memudahkan tracking.
- Backbone-agnostik dan skalabel.

## Keunggulan
- Anchor-free sederhana.
- Deteksi+tracking terpadu.
- SOTA.

## Keterbatasan
- Fokus LiDAR (butuh point cloud).
- Refinement menambah biaya.
- Objek sangat kecil/jauh menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Paradigma berbasis pusat relevan untuk deteksi 3D dari point cloud (termasuk pseudo-LiDAR dari depth) pada persepsi RGB-D/otonom.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [186 - 2020 - PV-RCNN - Deteksi 3D](./186%20-%202020%20-%20PV-RCNN%20-%20Deteksi%203D.md)
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
CenterPoint menyederhanakan deteksi dan pelacakan 3D lewat representasi berbasis pusat, menjadi baseline kuat untuk persepsi 3D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yin2021centerpoint` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 185/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
