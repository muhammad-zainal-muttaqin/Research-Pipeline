# 117 - Onboard Dynamic-Object Detection and Tracking for Autonomous Robot Navigation with RGB-D Camera

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 117 dari 154 |
| Kunci BibTeX | `xu2024onboard` |
| Judul | Onboard Dynamic-Object Detection and Tracking for Autonomous Robot Navigation with RGB-D Camera |
| Penulis | Xu, Zhefan; Zhan, Xiaoyang; Xiu, Yumeng; Suzuki, Christopher; Shimada, Kenji |
| Tahun | 2024 |
| Venue / Jurnal | IEEE Robotics and Automation Letters |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, navigasi, deteksi dinamis, tracking, RA-L |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Onboard%20Dynamic-Object%20Detection%20and%20Tracking%20for%20Autonomous%20Robot%20Navigation%20with%20RGB-D%20Camera
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Onboard%20Dynamic-Object%20Detection%20and%20Tracking%20for%20Autonomous%20Robot%20Navigation%20with%20RGB-D%20Camera&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 9 |
| Nomor | 1 |
| Halaman | 651--658 |

## Ringkasan Eksekutif
Sistem onboard untuk deteksi dan pelacakan objek dinamis memakai kamera RGB-D guna navigasi robot otonom real-time.

## Abstrak (Parafrase)
Xu dkk. mengembangkan sistem persepsi onboard yang mendeteksi dan melacak objek dinamis dari kamera RGB-D untuk mendukung navigasi robot otonom secara real-time. Deteksi objek dan estimasi kecepatan memungkinkan perencanaan gerak yang aman di lingkungan dengan objek bergerak. (IEEE RA-L 2024.)

## Latar Belakang & Konteks
Navigasi robot yang aman membutuhkan deteksi dan pelacakan objek bergerak secara onboard dan real-time, memakai sensor RGB-D yang memberi geometri sekaligus tekstur.

## Permasalahan yang Diangkat
- Navigasi aman butuh persepsi objek dinamis.
- Deteksi + pelacakan harus onboard & real-time.
- Estimasi kecepatan objek diperlukan.
- Lingkungan dinamis menantang perencanaan.
- Sumber daya robot terbatas.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi objek dinamis dari RGB-D onboard.
- Melacak & mengestimasi kecepatan objek.
- Mendukung navigasi otonom real-time.

## Tinjauan Terdahulu / Posisi Literatur
Sistem menggabungkan deteksi RGB-D dan pelacakan untuk navigasi.

Karya/konsep pembanding yang relevan:

- Deteksi objek (RGB-D) — persepsi.
- Tracking + estimasi kecepatan.
- Navigasi/perencanaan gerak.
- Kamera RGB-D onboard.

## Metodologi & Arsitektur
Kamera RGB-D memberi citra + kedalaman; modul deteksi melokalisasi objek dinamis; tracking mengasosiasikan deteksi antar-frame dan mengestimasi kecepatan; hasil dipakai perencana gerak untuk menghindari objek bergerak; berjalan onboard real-time.

Komponen / langkah metodologis utama:

- Deteksi objek dinamis dari RGB-D.
- Tracking antar-frame + estimasi kecepatan.
- Lokalisasi 3D via kedalaman.
- Integrasi ke perencanaan gerak.
- Onboard real-time.
- Uji robot navigasi.

## Kontribusi Utama
1. Deteksi-pelacakan objek dinamis onboard real-time.
2. Estimasi kecepatan untuk perencanaan aman.
3. Memanfaatkan RGB-D untuk lokalisasi 3D.
4. Aplikasi persepsi dinamis navigasi.

## Rincian Eksperimen
Diuji pada robot dengan skenario navigasi dinamis, metrik deteksi/pelacakan dan keberhasilan navigasi (IEEE RA-L 2024).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Robot navigasi | deteksi/tracking | andal onboard real-time |
| Objek dinamis | kecepatan | estimasi untuk perencanaan |
| Lokalisasi | 3D | via kedalaman RGB-D |

## Temuan Kunci
- RGB-D memungkinkan persepsi dinamis 3D onboard.
- Tracking + kecepatan penting untuk navigasi aman.
- Real-time layak pada robot.
- Deteksi objek kunci navigasi dinamis.

## Keunggulan
- Onboard real-time.
- Persepsi dinamis 3D.
- Terintegrasi navigasi.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Kinerja spesifik-platform.
- Detail bergantung implementasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menautkan RGB-D dengan navigasi robot dinamis dalam tinjauan, melengkapi tema persepsi objek bergerak (bandingkan SLAM dinamis).

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
- [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
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
Xu dkk. mengembangkan sistem onboard deteksi dan pelacakan objek dinamis dari kamera RGB-D untuk navigasi robot otonom real-time dengan estimasi kecepatan untuk perencanaan aman.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `xu2024onboard` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 117/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
