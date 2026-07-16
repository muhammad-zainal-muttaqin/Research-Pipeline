# 187 - BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 187 dari 191 |
| Kunci BibTeX | `li2022bevformer` |
| Judul | BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers |
| Penulis | Li, Zhiqi; Wang, Wenhai; Li, Hongyang; Xie, Enze; Sima, Chonghao; Lu, Tong; Qiao, Yu; Dai, Jifeng |
| Tahun | 2022 |
| Venue / Jurnal | European Conference on Computer Vision (ECCV) |
| Tema klaster | Deteksi 3D |
| Kata kunci | multi-camera 3D, BEV, spatiotemporal transformer, autonomous driving |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2203.17270
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=BEVFormer%3A%20Learning%20Bird%27s-Eye-View%20Representation%20from%20Multi-Camera%20Images
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=BEVFormer%3A%20Learning%20Bird%27s-Eye-View%20Representation%20from%20Multi-Camera%20Images%20via%20Spatiotemporal%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2203.17270 |

## Ringkasan Eksekutif
BEVFormer membangun representasi Bird's-Eye-View terpadu dari banyak kamera lewat Transformer spatiotemporal, memungkinkan deteksi 3D dan segmentasi map hanya dari kamera (tanpa LiDAR) dengan memanfaatkan konteks temporal.

## Abstrak (Parafrase)
Penulis merancang kueri BEV grid yang, melalui spatial cross-attention, mengambil fitur dari banyak kamera pada lokasi 3D terkait, dan melalui temporal self-attention menggabungkan informasi dari frame sebelumnya. Representasi BEV terpadu ini mendukung deteksi 3D dan segmentasi peta, mencapai kinerja kamera-saja yang kuat pada nuScenes dan mendekati metode LiDAR pada beberapa metrik.

## Latar Belakang & Konteks
Persepsi 3D kamera-saja menarik karena murah, tetapi menyatukan banyak pandangan dan waktu ke ruang BEV sulit.

## Permasalahan yang Diangkat
- Menyatukan multi-kamera ke BEV sulit.
- Informasi temporal kurang dimanfaatkan.
- Kamera-saja tertinggal dari LiDAR.

## Tujuan & Pertanyaan Penelitian
- Membangun BEV terpadu dari multi-kamera.
- Memanfaatkan konteks temporal.
- Mendukung deteksi 3D + map segmentation.

## Tinjauan Terdahulu / Posisi Literatur
Berdialog dengan LSS/BEVDet (proyeksi BEV) dan DETR3D (kueri 3D); kebaruan pada attention spatiotemporal BEV.

Karya/konsep pembanding yang relevan:

- DETR3D - kueri 3D-to-2D.
- LSS/BEVDet - lift-splat ke BEV.
- PETR - position embedding 3D.
- Transformer multi-view.

## Metodologi & Arsitektur
Kueri BEV grid; spatial cross-attention menyorot fitur multi-kamera pada titik 3D terproyeksi; temporal self-attention menggabungkan BEV historis; kepala deteksi/segmentasi memakai fitur BEV.

Komponen / langkah metodologis utama:

- Kueri grid BEV terpadu.
- Spatial cross-attention multi-kamera.
- Temporal self-attention (frame lampau).
- Kepala deteksi 3D + map segmentation.

## Kontribusi Utama
1. Representasi BEV spatiotemporal dari kamera.
2. Pemanfaatan temporal eksplisit.
3. Kamera-saja mendekati LiDAR.
4. Multitugas (deteksi + map).

## Rincian Eksperimen
nuScenes untuk deteksi 3D (NDS/mAP) dan segmentasi peta BEV; ablation temporal.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| nuScenes deteksi | NDS/mAP | SOTA kamera-saja saat rilis |
| Map segmentation | IoU | kuat |
| Ablation temporal | NDS | temporal menaikkan hasil |

## Temuan Kunci
- Attention spatiotemporal menyatukan multi-kamera+waktu.
- Temporal penting untuk kecepatan/oklusi.
- Kamera-saja bisa mendekati LiDAR.

## Keunggulan
- Kamera-saja (murah).
- Memanfaatkan waktu.
- Multitugas BEV.

## Keterbatasan
- Komputasi Transformer besar.
- Bergantung kalibrasi kamera.
- Masih di bawah LiDAR pada kasus tertentu.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Persepsi 3D berbasis kamera + BEV relevan untuk sistem otonom dan menjembatani depth/kamera ke deteksi 3D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [185 - 2021 - CenterPoint - Deteksi 3D](./185%20-%202021%20-%20CenterPoint%20-%20Deteksi%203D.md)
- [186 - 2020 - PV-RCNN - Deteksi 3D](./186%20-%202020%20-%20PV-RCNN%20-%20Deteksi%203D.md)
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
BEVFormer menyatukan multi-kamera dan waktu ke BEV via Transformer, memajukan persepsi 3D kamera-saja.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `li2022bevformer` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 187/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
