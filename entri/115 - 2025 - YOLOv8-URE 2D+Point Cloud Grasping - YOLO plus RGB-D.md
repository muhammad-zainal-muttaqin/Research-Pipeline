# 115 - Research on a Fusion Technique of YOLOv8-URE-Based 2D Vision and Point Cloud for Robotic Grasping in Stacked Scenarios

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 115 dari 154 |
| Kunci BibTeX | `yang2025yolov8ure` |
| Judul | Research on a Fusion Technique of YOLOv8-URE-Based 2D Vision and Point Cloud for Robotic Grasping in Stacked Scenarios |
| Penulis | Yang, Wen; others |
| Tahun | 2025 |
| Venue / Jurnal | Applied Sciences |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, YOLOv8, point cloud, grasp, tumpukan |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Research%20on%20a%20Fusion%20Technique%20of%20YOLOv8-URE-Based%202D%20Vision%20and%20Point%20Cloud%20for%20Robotic%20Grasping%20in%20Stacked%20Scenarios
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Research%20on%20a%20Fusion%20Technique%20of%20YOLOv8-URE-Based%202D%20Vision%20and%20Point%20Cloud%20for%20Robotic%20Grasping%20in%20Stacked%20Scenarios&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 15 |
| Nomor | 12 |
| Halaman | 6583 |

## Ringkasan Eksekutif
Teknik fusi visi 2D berbasis YOLOv8-URE dengan point cloud untuk grasp robotik pada skenario objek bertumpuk.

## Abstrak (Parafrase)
Makalah ini mengusulkan fusi antara deteksi 2D berbasis YOLOv8-URE (varian YOLOv8 dengan modul peningkatan) dan point cloud untuk memperkirakan pose grasp objek pada tumpukan (stacked scenarios). Deteksi 2D mempersempit wilayah lalu geometri point cloud memberi pose grasp 3D, meningkatkan keberhasilan grasp. [Detail dari metadata daring 2025 — verifikasi.]

## Latar Belakang & Konteks
Grasp pada tumpukan objek menuntut integrasi deteksi 2D (identifikasi objek) dan geometri 3D (pose grasp), karena kotak 2D saja tak cukup untuk cengkeraman di tumpukan.

## Permasalahan yang Diangkat
- Grasp pada tumpukan objek sangat menantang.
- Kotak 2D saja tak cukup untuk pose grasp.
- Geometri 3D (point cloud) diperlukan.
- Oklusi/tumpang tindih pada tumpukan.
- Integrasi 2D-3D belum optimal.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi objek via YOLOv8-URE (2D).
- Memperkirakan pose grasp via point cloud (3D).
- Meningkatkan keberhasilan grasp pada tumpukan.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan YOLOv8 termodifikasi dan point cloud untuk grasp.

Karya/konsep pembanding yang relevan:

- YOLOv8 — detektor 2D dasar.
- Modul URE — peningkatan YOLOv8.
- Point cloud (RGB-D) — geometri 3D.
- Grasp pada tumpukan.

## Metodologi & Arsitektur
YOLOv8-URE mendeteksi objek pada citra 2D untuk mempersempit wilayah; point cloud (dari RGB-D) di wilayah tersebut dipakai memperkirakan pose grasp 3D; sistem memilih grasp untuk objek pada tumpukan. [Rincian perlu konfirmasi ke naskah.]

Komponen / langkah metodologis utama:

- Deteksi 2D via YOLOv8-URE.
- Modul URE meningkatkan deteksi.
- Fusi dengan point cloud untuk pose 3D.
- Estimasi grasp pada tumpukan.
- Pipeline 2D-3D terintegrasi.
- Evaluasi skenario stacked.

## Kontribusi Utama
1. Fusi YOLOv8-URE (2D) + point cloud (3D).
2. Peningkatan keberhasilan grasp pada tumpukan.
3. Modul URE menyempurnakan deteksi.
4. Contoh YOLO+point cloud untuk grasp (2025).

## Rincian Eksperimen
Diuji pada skenario objek bertumpuk dengan metrik keberhasilan grasp. [Angka spesifik perlu diverifikasi ke naskah asli.]

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Skenario tumpukan | success rate | peningkatan grasp (per makalah) |
| Fusi | 2D+point cloud | deteksi + pose 3D |
| Catatan | verifikasi | detail dari metadata daring |

## Temuan Kunci
- Fusi 2D-3D meningkatkan grasp pada tumpukan.
- YOLOv8-URE menyempurnakan deteksi.
- Point cloud kunci pose grasp 3D.
- Tumpukan menuntut geometri 3D.

## Keunggulan
- Fusi 2D+point cloud.
- Fokus skenario tumpukan.
- Memakai YOLOv8 mutakhir.

## Keterbatasan
- Detail dari metadata daring — verifikasi.
- Bergantung kualitas point cloud.
- Kinerja spesifik-skenario.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menghubungkan YOLO+RGB-D dan grasp robotik dalam tinjauan; rinciannya perlu diverifikasi ke naskah asli sebelum dikutip formal.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
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
YOLOv8-URE memadukan deteksi 2D dan point cloud untuk grasp robotik pada tumpukan objek; rinciannya perlu diverifikasi ke naskah asli.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yang2025yolov8ure` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 115/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
