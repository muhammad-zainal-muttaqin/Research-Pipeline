# 113 - FusionVision: A Comprehensive Approach of 3D Object Reconstruction and Segmentation from RGB-D Cameras Using YOLO and Fast Segment Anything

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 113 dari 154 |
| Kunci BibTeX | `elamraoui2024fusionvision` |
| Judul | FusionVision: A Comprehensive Approach of 3D Object Reconstruction and Segmentation from RGB-D Cameras Using YOLO and Fast Segment Anything |
| Penulis | El Amraoui, Safouane; others |
| Tahun | 2024 |
| Venue / Jurnal | arXiv preprint arXiv:2403.00175 |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, YOLOv8, FastSAM, rekonstruksi 3D, point cloud |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-yolo-plus-rgb-d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2403.00175
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=FusionVision%3A%20A%20Comprehensive%20Approach%20of%203D%20Object%20Reconstruction%20and%20Segmentation%20from%20RGB-D%20Cameras%20Using%20YOLO%20and%20Fast%20Segment%20Anything
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=FusionVision%3A%20A%20Comprehensive%20Approach%20of%203D%20Object%20Reconstruction%20and%20Segmentation%20from%20RGB-D%20Cameras%20Using%20YOLO%20and%20Fast%20Segment%20Anything&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2403.00175 |

## Ringkasan Eksekutif
Pendekatan yang memadukan YOLOv8 (deteksi) dan FastSAM (segmentasi) pada citra RGB-D untuk rekonstruksi dan segmentasi objek 3D dari kamera kedalaman.

## Abstrak (Parafrase)
FusionVision membangun pipeline end-to-end untuk rekonstruksi dan segmentasi objek 3D dari kamera RGB-D (mis. RealSense): YOLOv8 melokalisasi objek, FastSAM mensegmentasinya secara cepat, lalu mask diproyeksikan ke point cloud (via kedalaman) untuk menghasilkan objek 3D yang bersih. [Detail dari abstrak arXiv 2024 — verifikasi ke naskah.]

## Latar Belakang & Konteks
Rekonstruksi 3D objek yang bersih dari RGB-D membutuhkan deteksi dan segmentasi yang terintegrasi dan cepat, sekaligus proyeksi ke geometri 3D.

## Permasalahan yang Diangkat
- Rekonstruksi 3D objek bersih butuh deteksi+segmentasi.
- Segmentasi umum (SAM) bisa lambat.
- Proyeksi mask ke point cloud perlu kedalaman.
- Pipeline end-to-end RGB-D diinginkan.
- Objek perlu dipisah dari latar 3D.

## Tujuan & Pertanyaan Penelitian
- Melokalisasi objek via YOLOv8.
- Mensegmentasi cepat via FastSAM.
- Merekonstruksi/segmentasi objek 3D dari RGB-D.

## Tinjauan Terdahulu / Posisi Literatur
FusionVision menggabungkan YOLO dan Segment Anything cepat pada RGB-D.

Karya/konsep pembanding yang relevan:

- YOLOv8 — deteksi objek.
- FastSAM — segmentasi cepat (SAM).
- Kamera RGB-D (RealSense) — kedalaman.
- Point cloud projection — 3D.

## Metodologi & Arsitektur
YOLOv8 mendeteksi objek pada citra RGB; FastSAM mensegmentasi objek berdasarkan prompt kotak; mask diproyeksikan ke point cloud memakai kedalaman untuk mengisolasi objek 3D; menghasilkan rekonstruksi/segmentasi 3D objek. [Rincian teknis perlu konfirmasi ke naskah asli.]

Komponen / langkah metodologis utama:

- YOLOv8 melokalisasi objek (prompt kotak).
- FastSAM segmentasi cepat per-objek.
- Proyeksi mask ke point cloud (kedalaman).
- Isolasi & rekonstruksi objek 3D.
- Pipeline end-to-end RGB-D.
- Kamera depth (mis. RealSense).

## Kontribusi Utama
1. Pipeline YOLO+SAM pada RGB-D untuk 3D.
2. Rekonstruksi & segmentasi objek 3D.
3. Integrasi deteksi-segmentasi-geometri.
4. Contoh mutakhir YOLO+RGB-D (2024).

## Rincian Eksperimen
Diuji pada kamera kedalaman (RealSense) untuk rekonstruksi/segmentasi 3D objek. [Metrik/hasil spesifik perlu diverifikasi ke naskah arXiv asli.]

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Kamera RGB-D | rekonstruksi/seg 3D | objek 3D bersih (per abstrak) |
| Integrasi | YOLOv8+FastSAM | deteksi + segmentasi cepat |
| Catatan | verifikasi | angka/detail dari abstrak daring |

## Temuan Kunci
- YOLO+SAM+kedalaman menghasilkan objek 3D bersih.
- FastSAM menjaga kecepatan segmentasi.
- Proyeksi kedalaman kunci isolasi 3D.
- Pipeline modular praktis.

## Keunggulan
- Integrasi deteksi-segmentasi-3D.
- Memakai model mutakhir (YOLOv8/FastSAM).
- Pipeline RGB-D praktis.

## Keterbatasan
- Detail dari abstrak daring — belum diverifikasi penuh.
- Bergantung kualitas kedalaman & segmentasi.
- Kinerja bergantung kamera/skenario.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
FusionVision adalah contoh mutakhir pipeline YOLO+RGB-D untuk 3D dalam tinjauan; namun detailnya berasal dari abstrak daring dan perlu diverifikasi ke naskah asli sebelum dikutip formal.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
- [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [117 - 2024 - Onboard Dynamic-Object Detection (Xu dkk.) - YOLO plus RGB-D](./117%20-%202024%20-%20Onboard%20Dynamic-Object%20Detection%20%28Xu%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [119 - 2023 - Distance Measurement via YOLO + Depth (Chen dkk.) - YOLO plus RGB-D](./119%20-%202023%20-%20Distance%20Measurement%20via%20YOLO%20+%20Depth%20%28Chen%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **YOLO plus RGB-D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema YOLO plus RGB-D)
Istilah penting untuk memahami makalah ini:

- **YOLO** — Detektor satu-tahap real-time regresi tunggal.
- **Kanal depth** — Peta kedalaman sebagai masukan tambahan.
- **Fusi RGB-D** — Penggabungan warna dan kedalaman pada deteksi.
- **Lokalisasi 3D** — Posisi objek dalam koordinat 3D via depth.
- **Point cloud** — Titik 3D dari depth untuk grasp/rekonstruksi.
- **Pick-and-place** — Tugas robot mengambil dan menempatkan objek.
- **RealSense/Kinect** — Kamera RGB-D konsumen umum.
- **Early/mid/late fusion** — Titik penggabungan depth pada arsitektur.
- **Segment Anything (SAM)** — Model segmentasi umum; FastSAM=versi cepat.
- **Real-time deployment** — Penerapan dengan kendala latensi.

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
FusionVision memadukan YOLOv8 dan FastSAM pada citra RGB-D untuk rekonstruksi dan segmentasi objek 3D dari kamera kedalaman; rinciannya perlu diverifikasi ke naskah arXiv asli.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `elamraoui2024fusionvision` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 113/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
