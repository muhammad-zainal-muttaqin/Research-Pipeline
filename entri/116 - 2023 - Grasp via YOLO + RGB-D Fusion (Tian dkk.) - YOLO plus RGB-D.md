# 116 - A Robot Grasp Detection Method Based on YOLO and RGB-D Feature Fusion

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 116 dari 154 |
| Kunci BibTeX | `tian2023grasp` |
| Judul | A Robot Grasp Detection Method Based on YOLO and RGB-D Feature Fusion |
| Penulis | Tian, Hao; Song, Kechen; Li, Song; Ma, Shaoning; Yan, Yunhui |
| Tahun | 2023 |
| Venue / Jurnal | Journal of Intelligent \& Robotic Systems |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, grasp, fusi fitur, deteksi, robotik |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20Robot%20Grasp%20Detection%20Method%20Based%20on%20YOLO%20and%20RGB-D%20Feature%20Fusion
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20Robot%20Grasp%20Detection%20Method%20Based%20on%20YOLO%20and%20RGB-D%20Feature%20Fusion&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 107 |
| Nomor | 3 |
| Halaman | 38 |

## Ringkasan Eksekutif
Metode deteksi grasp robotik yang memfusikan fitur RGB dan kedalaman dalam kerangka berbasis YOLO untuk memprediksi grasp.

## Abstrak (Parafrase)
Tian dkk. mengusulkan deteksi grasp robotik yang menggabungkan kecepatan detektor gaya YOLO dengan fusi fitur RGB-D: fitur warna (tekstur) dan kedalaman (geometri) difusikan untuk memprediksi konfigurasi grasp. Pendekatan ini memanfaatkan komplementaritas RGB-D dalam kerangka deteksi cepat, mencapai akurasi grasp kompetitif.

## Latar Belakang & Konteks
Deteksi grasp perlu cepat (seperti YOLO) sekaligus memanfaatkan geometri kedalaman; menggabungkan keduanya dalam satu kerangka belum banyak dieksplorasi.

## Permasalahan yang Diangkat
- Grasp perlu cepat dan akurat.
- Geometri kedalaman penting untuk grasp.
- Detektor cepat (YOLO) belum banyak difusikan dengan depth untuk grasp.
- Komplementaritas RGB-D kurang dimanfaatkan.
- Real-time diinginkan untuk robotika.

## Tujuan & Pertanyaan Penelitian
- Membangun detektor grasp gaya YOLO.
- Memfusikan fitur RGB dan kedalaman.
- Memprediksi grasp secara cepat & akurat.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan detektor YOLO dan fusi fitur RGB-D untuk grasp.

Karya/konsep pembanding yang relevan:

- YOLO — detektor cepat.
- RGB-D feature fusion.
- Grasp detection (Cornell/Jacquard).
- Robotik manipulasi.

## Metodologi & Arsitektur
Backbone gaya YOLO mengekstrak fitur; modul fusi menggabungkan fitur RGB dan kedalaman; head memprediksi konfigurasi grasp (posisi/sudut/lebar); dilatih pada dataset grasp dan/atau divalidasi robot.

Komponen / langkah metodologis utama:

- Backbone gaya YOLO (cepat).
- Modul fusi fitur RGB-D.
- Head prediksi grasp (posisi/sudut/lebar).
- Pemanfaatan komplementaritas warna-geometri.
- Pelatihan pada dataset grasp.
- Orientasi real-time.

## Kontribusi Utama
1. Detektor grasp gaya YOLO dengan fusi RGB-D.
2. Memanfaatkan komplementaritas RGB-D.
3. Akurasi grasp kompetitif.
4. Cepat (basis YOLO).

## Rincian Eksperimen
Diuji pada dataset grasp (Cornell/Jacquard) dan/atau robot dengan metrik akurasi grasp (J. Intelligent & Robotic Systems 2023).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Cornell/Jacquard | akurasi grasp | kompetitif |
| Robot/uji | success rate | validasi grasp |
| Fusi | RGB-D | komplementaritas dimanfaatkan |

## Temuan Kunci
- YOLO dapat diadaptasi untuk grasp cepat.
- Fusi RGB-D meningkatkan akurasi grasp.
- Komplementaritas warna-geometri bermanfaat.
- Real-time terjaga.

## Keunggulan
- Integrasi YOLO + fusi RGB-D eksplisit.
- Cepat.
- Akurasi kompetitif.

## Keterbatasan
- Grasp planar (bukan 6-DoF penuh).
- Bergantung kualitas RGB-D.
- Detail bergantung implementasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini adalah contoh eksplisit integrasi YOLO dan fusi RGB-D untuk grasp dalam tinjauan, menautkan deteksi cepat dengan manipulasi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
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
Tian dkk. mengusulkan deteksi grasp robotik berbasis YOLO dengan fusi fitur RGB-D, memanfaatkan komplementaritas warna dan geometri dalam kerangka deteksi cepat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `tian2023grasp` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 116/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
