# 188 - DETR3D: 3D Object Detection from Multi-View Images via 3D-to-2D Queries

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 188 dari 191 |
| Kunci BibTeX | `wang2022detr3d` |
| Judul | DETR3D: 3D Object Detection from Multi-View Images via 3D-to-2D Queries |
| Penulis | Wang, Yue; Guizilini, Vitor; Zhang, Tianyuan; Wang, Yilun; Zhao, Hang; Solomon, Justin |
| Tahun | 2022 |
| Venue / Jurnal | Conference on Robot Learning (CoRL) |
| Tema klaster | Deteksi 3D |
| Kata kunci | multi-view 3D, 3D-to-2D queries, camera-only, set prediction |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2110.06922
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DETR3D%3A%203D%20Object%20Detection%20from%20Multi-View%20Images%20via%203D-to-2D%20Queries
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DETR3D%3A%203D%20Object%20Detection%20from%20Multi-View%20Images%20via%203D-to-2D%20Queries&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2110.06922 |

## Ringkasan Eksekutif
DETR3D melakukan deteksi objek 3D dari banyak kamera secara end-to-end dengan kueri objek 3D yang memproyeksikan titik referensi ke citra (3D-to-2D) untuk mengambil fitur, menghapus post-processing NMS dan penggabungan BEV eksplisit.

## Abstrak (Parafrase)
Penulis memperluas DETR ke 3D multi-kamera: tiap kueri objek memprediksi titik referensi 3D yang diproyeksikan ke seluruh citra untuk sampling fitur, lalu disempurnakan lintas-layer. Prediksi himpunan 3D dilakukan langsung tanpa NMS dan tanpa membangun BEV padat, mencapai deteksi 3D kamera-saja yang kompetitif pada nuScenes.

## Latar Belakang & Konteks
Metode kamera-saja awal membangun BEV eksplisit atau depth per-piksel. DETR3D menawarkan alternatif berbasis kueri sparse.

## Permasalahan yang Diangkat
- BEV padat/depth eksplisit mahal & rawan galat.
- Butuh deteksi 3D end-to-end multi-kamera.
- Menghapus NMS antar-view.

## Tujuan & Pertanyaan Penelitian
- Deteksi 3D multi-kamera berbasis kueri.
- Sampling fitur via proyeksi 3D-to-2D.
- End-to-end tanpa NMS/BEV eksplisit.

## Tinjauan Terdahulu / Posisi Literatur
Mengadaptasi DETR/Deformable DETR ke 3D; mendahului/berdialog dengan BEVFormer dan PETR.

Karya/konsep pembanding yang relevan:

- DETR - set prediction 2D.
- Deformable DETR - sampling fitur terdeformasi.
- BEVFormer - BEV spatiotemporal.
- FCOS3D - deteksi 3D mono.

## Metodologi & Arsitektur
Kueri objek memprediksi titik referensi 3D; titik diproyeksikan ke tiap kamera memakai matriks kalibrasi untuk sampling fitur; fitur teragregasi menyempurnakan kueri lintas-layer; kepala memprediksi box 3D + kelas.

Komponen / langkah metodologis utama:

- Kueri objek 3D + titik referensi.
- Proyeksi 3D-to-2D untuk sampling fitur.
- Refinement kueri lintas-layer.
- Set prediction tanpa NMS.

## Kontribusi Utama
1. Deteksi 3D multi-kamera berbasis kueri.
2. Sampling fitur geometris (3D-to-2D).
3. End-to-end tanpa BEV eksplisit/NMS.
4. Baseline berpengaruh kamera-saja.

## Rincian Eksperimen
nuScenes untuk deteksi 3D (NDS/mAP), pembandingan dengan FCOS3D dan metode BEV.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| nuScenes | NDS/mAP | kompetitif kamera-saja |
| End-to-end | - | tanpa NMS/BEV padat |
| Ablation sampling | mAP | proyeksi geometris penting |

## Temuan Kunci
- Kueri sparse + proyeksi geometris efektif untuk 3D.
- BEV padat tak wajib.
- Kalibrasi kamera dimanfaatkan langsung.

## Keunggulan
- End-to-end, tanpa NMS.
- Kamera-saja.
- Sparse & elegan.

## Keterbatasan
- Bergantung kalibrasi akurat.
- Tanpa temporal (versi dasar).
- Di bawah LiDAR pada kasus tertentu.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Pendekatan deteksi 3D berbasis kueri geometris relevan untuk menyatukan kamera/depth ke persepsi 3D pada pipeline RGB-D/otonom.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [185 - 2021 - CenterPoint - Deteksi 3D](./185%20-%202021%20-%20CenterPoint%20-%20Deteksi%203D.md)
- [186 - 2020 - PV-RCNN - Deteksi 3D](./186%20-%202020%20-%20PV-RCNN%20-%20Deteksi%203D.md)
- [187 - 2022 - BEVFormer - Deteksi 3D](./187%20-%202022%20-%20BEVFormer%20-%20Deteksi%203D.md)

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
DETR3D menghadirkan deteksi 3D multi-kamera end-to-end berbasis kueri dengan sampling 3D-to-2D, fondasi banyak metode kamera-saja berikutnya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2022detr3d` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 188/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
