# 114 - Development of a Pumpkin Fruits Pick-and-Place Robot Using an RGB-D Camera and a YOLO Based Object Detection AI Model

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 114 dari 154 |
| Kunci BibTeX | `ito2024pumpkin` |
| Judul | Development of a Pumpkin Fruits Pick-and-Place Robot Using an RGB-D Camera and a YOLO Based Object Detection AI Model |
| Penulis | Ito, Nakaguchi; others |
| Tahun | 2024 |
| Venue / Jurnal | Computers and Electronics in Agriculture |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, pertanian, pick-and-place, panen robotik, lokalisasi 3D |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Development%20of%20a%20Pumpkin%20Fruits%20Pick-and-Place%20Robot%20Using%20an%20RGB-D%20Camera%20and%20a%20YOLO%20Based%20Object%20Detection%20AI%20Model
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Development%20of%20a%20Pumpkin%20Fruits%20Pick-and-Place%20Robot%20Using%20an%20RGB-D%20Camera%20and%20a%20YOLO%20Based%20Object%20Detection%20AI%20Model&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 227 |
| Halaman | 109625 |

## Ringkasan Eksekutif
Pengembangan robot pick-and-place buah labu memakai kamera RGB-D dan deteksi berbasis YOLO untuk melokalisasi dan mengambil buah.

## Abstrak (Parafrase)
Makalah ini mengembangkan sistem robot pick-and-place untuk memanen buah labu: model deteksi berbasis YOLO melokalisasi buah pada citra RGB, dan kamera RGB-D memberikan koordinat 3D untuk perencanaan pengambilan (grasp). Sistem robot terintegrasi diuji untuk pemanenan. [Detail penulis/halaman dari metadata daring — verifikasi.]

## Latar Belakang & Konteks
Pemanenan labu padat karya dan membutuhkan deteksi serta lokalisasi 3D buah yang andal di lapangan untuk otomasi pick-and-place.

## Permasalahan yang Diangkat
- Pemanenan labu padat karya.
- Deteksi & lokalisasi 3D buah di lapangan sulit.
- Kondisi lapangan bervariasi (cahaya/oklusi).
- Manipulasi butuh koordinat 3D akurat.
- Otomasi pick-and-place diperlukan.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi buah labu via YOLO.
- Melokalisasi buah dalam 3D via RGB-D.
- Mengotomasi pick-and-place pemanenan.

## Tinjauan Terdahulu / Posisi Literatur
Sistem menggabungkan deteksi YOLO dan penginderaan kedalaman untuk manipulasi.

Karya/konsep pembanding yang relevan:

- YOLO — deteksi buah pada RGB.
- Kamera RGB-D — koordinat 3D.
- Robot manipulator — pick-and-place.
- Domain pertanian (panen).

## Metodologi & Arsitektur
Model YOLO mendeteksi buah labu pada citra RGB; kedalaman dari kamera RGB-D memberi posisi 3D buah; sistem perencanaan menggerakkan lengan robot untuk mengambil dan menempatkan buah; diuji pada skenario pemanenan. [Rincian perlu konfirmasi ke naskah.]

Komponen / langkah metodologis utama:

- Deteksi buah labu via YOLO (RGB).
- Estimasi koordinat 3D via kedalaman.
- Perencanaan grasp/pick-and-place.
- Lengan robot manipulator.
- Integrasi sistem panen.
- Uji lapangan/lab.

## Kontribusi Utama
1. Sistem panen labu berbasis YOLO+RGB-D.
2. Lokalisasi 3D buah dari kedalaman.
3. Otomasi pick-and-place terintegrasi.
4. Aplikasi konkret YOLO+RGB-D di pertanian.

## Rincian Eksperimen
Diuji pada skenario pemanenan (lab/lapangan) dengan metrik keberhasilan pick-and-place. [Angka spesifik perlu diverifikasi ke naskah asli.]

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Pemanenan | success rate | keberhasilan pick-and-place (per makalah) |
| Lokalisasi | 3D | koordinat buah dari RGB-D |
| Catatan | verifikasi | detail dari metadata daring |

## Temuan Kunci
- YOLO+RGB-D memungkinkan panen labu otomatis.
- Kedalaman memberi lokalisasi 3D untuk grasp.
- Integrasi deteksi-manipulasi praktis.
- Kondisi lapangan tetap menantang.

## Keunggulan
- Aplikasi konkret pertanian.
- Integrasi YOLO+RGB-D+robot.
- Pick-and-place otomatis.

## Keterbatasan
- Detail penulis/halaman dari metadata daring — verifikasi.
- Bergantung kualitas kedalaman & deteksi.
- Kinerja spesifik-tanaman/lapangan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menghubungkan klaster YOLO+RGB-D dan Pertanian dalam tinjauan; contoh penerapan nyata deteksi+kedalaman untuk panen robotik.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
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
Ito dkk. mengembangkan robot pick-and-place buah labu berbasis deteksi YOLO dan kamera RGB-D untuk lokalisasi 3D; rincian metadata perlu diverifikasi ke naskah asli.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ito2024pumpkin` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 114/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
