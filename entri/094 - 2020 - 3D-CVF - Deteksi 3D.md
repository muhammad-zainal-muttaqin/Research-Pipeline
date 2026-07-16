# 094 - 3D-CVF: Generating Joint Camera and LiDAR Features Using Cross-View Spatial Feature Fusion for 3D Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 094 dari 154 |
| Kunci BibTeX | `yoo20203dcvf` |
| Judul | 3D-CVF: Generating Joint Camera and LiDAR Features Using Cross-View Spatial Feature Fusion for 3D Object Detection |
| Penulis | Yoo, Jin Hyeok; Kim, Yecheol; Kim, Jisong; Choi, Jun Won |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, cross-view fusion, gated, LiDAR-kamera, spasial |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=3D-CVF%3A%20Generating%20Joint%20Camera%20and%20LiDAR%20Features%20Using%20Cross-View%20Spatial%20Feature%20Fusion%20for%203D%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=3D-CVF%3A%20Generating%20Joint%20Camera%20and%20LiDAR%20Features%20Using%20Cross-View%20Spatial%20Feature%20Fusion%20for%203D%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 720--736 |

## Ringkasan Eksekutif
Metode deteksi 3D yang menggabungkan fitur kamera dan LiDAR via cross-view spatial feature fusion dengan skema gated untuk penyelarasan spasial.

## Abstrak (Parafrase)
3D-CVF (Cross-View Feature Fusion) menyelaraskan fitur kamera 2D dan LiDAR 3D secara spasial melalui auto-calibrated projection ke ruang BEV, lalu menggabungkannya dengan gated feature fusion yang menimbang kontribusi tiap modal per-lokasi. Pendekatan ini mengatasi kesulitan penyelarasan cross-view dan SOTA fusi saat rilis.

## Latar Belakang & Konteks
Menyelaraskan fitur kamera (2D perspektif) dan LiDAR (3D) secara spasial sulit karena perbedaan ruang representasi; fusi tanpa penyelarasan yang baik kurang optimal.

## Permasalahan yang Diangkat
- Penyelarasan fitur kamera 2D dan LiDAR 3D sulit.
- Perbedaan ruang representasi (perspektif vs 3D).
- Fusi tanpa penyelarasan kurang optimal.
- Kontribusi modal bervariasi per-lokasi.
- Kalibrasi memengaruhi kualitas fusi.

## Tujuan & Pertanyaan Penelitian
- Menyelaraskan fitur kamera-LiDAR secara spasial.
- Menggabungkan modal via gated fusion.
- Meningkatkan akurasi deteksi 3D.

## Tinjauan Terdahulu / Posisi Literatur
3D-CVF mengembangkan fusi spasial cross-view untuk deteksi 3D.

Karya/konsep pembanding yang relevan:

- MV3D/AVOD — fusi multi-view (pembanding).
- BEV projection — penyelarasan.
- Gated fusion — pembobotan adaptif.
- Dataset KITTI/nuScenes.

## Metodologi & Arsitektur
Auto-calibrated projection memetakan fitur kamera ke ruang BEV untuk selaras dengan fitur LiDAR; gated feature fusion menimbang kontribusi kamera vs LiDAR per-lokasi; fitur tergabung diproses head deteksi 3D.

Komponen / langkah metodologis utama:

- Auto-calibrated projection kamera ke BEV.
- Penyelarasan spasial cross-view.
- Gated feature fusion (pembobotan per-lokasi).
- Fitur BEV tergabung.
- Head deteksi 3D.
- LiDAR + kamera.

## Kontribusi Utama
1. Penyelarasan spasial cross-view efektif.
2. Gated fusion menimbang modal adaptif.
3. SOTA fusi saat rilis.
4. Mengatasi perbedaan ruang representasi.

## Rincian Eksperimen
Diuji pada KITTI dan nuScenes dengan metrik AP 3D/NDS, dibandingkan metode fusi lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D | AP 3D | SOTA fusi saat rilis |
| nuScenes | NDS | kuat |
| Ablation | gated fusion | penyelarasan+gating menyumbang gain |

## Temuan Kunci
- Penyelarasan spasial krusial untuk fusi 3D.
- Gated fusion adaptif per-lokasi bermanfaat.
- Proyeksi ke BEV menyatukan ruang.
- Kalibrasi memengaruhi hasil.

## Keunggulan
- Penyelarasan cross-view.
- Gated fusion adaptif.
- SOTA fusi.

## Keterbatasan
- Bergantung kalibrasi sensor.
- Fusi BEV kehilangan detail vertikal.
- Kompleksitas penyelarasan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
3D-CVF menegaskan pentingnya penyelarasan spasial pada fusi multi-sensor — prinsip yang berlaku juga untuk penyelarasan RGB-Depth dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
- [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)
- [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md)
- [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md)
- [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md)
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
3D-CVF menggabungkan fitur kamera dan LiDAR via cross-view spatial fusion dengan gating adaptif, mengatasi kesulitan penyelarasan cross-view untuk deteksi 3D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yoo20203dcvf` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 094/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
