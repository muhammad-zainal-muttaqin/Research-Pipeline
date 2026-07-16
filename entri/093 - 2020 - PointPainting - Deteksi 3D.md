# 093 - PointPainting: Sequential Fusion for 3D Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 093 dari 154 |
| Kunci BibTeX | `vora2020pointpainting` |
| Judul | PointPainting: Sequential Fusion for 3D Object Detection |
| Penulis | Vora, Sourabh; Lang, Alex H.; Helou, Bassam; Beijbom, Oscar |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Deteksi 3D |
| Kata kunci | deteksi 3D, fusi sekuensial, segmentasi, LiDAR-kamera, plug-in |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PointPainting%3A%20Sequential%20Fusion%20for%203D%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PointPainting%3A%20Sequential%20Fusion%20for%203D%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4604--4612 |

## Ringkasan Eksekutif
Metode fusi sekuensial yang 'mengecat' titik LiDAR dengan skor segmentasi semantik dari citra RGB sebelum masuk detektor 3D — sederhana namun efektif dan plug-in.

## Abstrak (Parafrase)
PointPainting memproyeksikan skor segmentasi semantik dari citra RGB ke titik-titik LiDAR (setiap titik 'dicat' dengan vektor skor kelas), lalu detektor 3D berbasis LiDAR (mis. PointPillars) memproses point cloud yang telah diperkaya. Fusi sekuensial sederhana ini meningkatkan berbagai detektor 3D pada KITTI dan nuScenes tanpa mengubah arsitektur detektor.

## Latar Belakang & Konteks
Fusi LiDAR-kamera sering rumit dan terikat arsitektur; dibutuhkan cara sederhana, general, dan plug-in untuk menambahkan informasi semantik RGB ke detektor LiDAR.

## Permasalahan yang Diangkat
- Fusi LiDAR-kamera sering rumit & terikat arsitektur.
- Informasi semantik RGB kurang dimanfaatkan.
- Perlu metode fusi general & plug-in.
- Detektor LiDAR-only mengabaikan tekstur.
- Penyelarasan citra-titik diperlukan.

## Tujuan & Pertanyaan Penelitian
- Memperkaya titik LiDAR dengan skor semantik RGB.
- Menyediakan fusi sekuensial plug-in.
- Meningkatkan berbagai detektor 3D.

## Tinjauan Terdahulu / Posisi Literatur
PointPainting menggabungkan segmentasi citra dan detektor LiDAR secara sekuensial.

Karya/konsep pembanding yang relevan:

- Segmentasi semantik citra — sumber skor.
- PointPillars/detektor LiDAR — hilir.
- Proyeksi citra-ke-titik (kalibrasi).
- Fusi sekuensial (sequential fusion).

## Metodologi & Arsitektur
Jaringan segmentasi memberi skor kelas per-piksel pada citra RGB; skor diproyeksikan ke titik LiDAR memakai kalibrasi (painting); titik yang telah 'dicat' (koordinat + skor semantik) diproses detektor 3D LiDAR standar; plug-in ke berbagai detektor.

Komponen / langkah metodologis utama:

- Segmentasi semantik citra (skor per-piksel).
- Proyeksi skor ke titik LiDAR (painting).
- Titik diperkaya (geometri + semantik).
- Detektor 3D LiDAR standar hilir.
- Fusi sekuensial plug-in.
- Evaluasi KITTI & nuScenes.

## Kontribusi Utama
1. Fusi sekuensial sederhana & efektif.
2. Plug-in ke berbagai detektor 3D.
3. Meningkatkan akurasi tanpa ubah arsitektur.
4. Memanfaatkan semantik RGB untuk LiDAR.

## Rincian Eksperimen
Diuji dengan beberapa detektor 3D (PointPillars, PointRCNN, dll.) pada KITTI dan nuScenes dengan metrik AP 3D/NDS.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI 3D | AP 3D | peningkatan lintas detektor |
| nuScenes | NDS | peningkatan konsisten |
| Plug-in | generalisasi | bekerja lintas detektor |

## Temuan Kunci
- Semantik RGB memperkaya titik LiDAR efektif.
- Fusi sekuensial sederhana bisa sangat efektif.
- Plug-in memudahkan adopsi.
- Kalibrasi akurat penting untuk painting.

## Keunggulan
- Sederhana & plug-in.
- Efektif lintas detektor.
- Memanfaatkan semantik RGB.

## Keterbatasan
- Bergantung kualitas segmentasi & kalibrasi.
- Sekuensial (bukan end-to-end).
- Error segmentasi merambat.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PointPainting adalah contoh fusi sekuensial RGB->geometri yang paralel dengan gagasan menyuntikkan kedalaman/semantik ke pipeline deteksi dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Deteksi 3D** yang baik dibaca berdampingan:

- [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md)
- [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md)
- [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md)
- [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md)
- [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md)
- [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md)
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
PointPainting 'mengecat' titik LiDAR dengan skor segmentasi RGB sebelum detektor 3D, menyediakan fusi sekuensial sederhana, plug-in, dan efektif lintas berbagai detektor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `vora2020pointpainting` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 093/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
