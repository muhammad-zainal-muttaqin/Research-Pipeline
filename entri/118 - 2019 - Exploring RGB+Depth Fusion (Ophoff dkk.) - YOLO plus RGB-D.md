# 118 - Exploring RGB+Depth Fusion for Real-Time Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 118 dari 154 |
| Kunci BibTeX | `ophoff2019multimodal` |
| Judul | Exploring RGB+Depth Fusion for Real-Time Object Detection |
| Penulis | Ophoff, Tanguy; Van Beeck, Kristof; Goedem{\'e |
| Tahun | 2019 |
| Venue / Jurnal | Sensors |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, fusi, early/mid/late, real-time, Sensors |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Exploring%20RGB%2BDepth%20Fusion%20for%20Real-Time%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Exploring%20RGB%2BDepth%20Fusion%20for%20Real-Time%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 19 |
| Nomor | 4 |
| Halaman | 866 |

## Ringkasan Eksekutif
Studi yang mengeksplorasi fusi RGB+kedalaman untuk deteksi objek real-time, membandingkan titik fusi (early/mid/late) dalam jaringan gaya YOLO.

## Abstrak (Parafrase)
Ophoff dkk. secara sistematis membandingkan di mana menggabungkan RGB dan kedalaman dalam detektor gaya YOLO: early fusion (input), mid-level fusion (fitur tengah), dan late fusion (keputusan). Eksperimen menunjukkan fusi tingkat-menengah (mid-level) memberi peningkatan akurasi terbaik untuk deteksi real-time, menjadi bukti empiris penting bagi desain YOLO+RGB-D.

## Latar Belakang & Konteks
Belum jelas di mana dan bagaimana memfusikan kedalaman untuk deteksi real-time terbaik; posisi fusi (early/mid/late) memiliki trade-off yang perlu diukur.

## Permasalahan yang Diangkat
- Posisi fusi optimal (early/mid/late) belum jelas.
- Trade-off titik fusi perlu diukur empiris.
- Deteksi real-time membatasi kompleksitas fusi.
- Kedalaman perlu diintegrasikan efektif.
- Panduan desain YOLO+RGB-D kurang.

## Tujuan & Pertanyaan Penelitian
- Membandingkan titik fusi early/mid/late.
- Mengukur dampak pada akurasi real-time.
- Memberi panduan desain fusi YOLO+RGB-D.

## Tinjauan Terdahulu / Posisi Literatur
Studi ini membandingkan strategi fusi pada detektor cepat gaya YOLO.

Karya/konsep pembanding yang relevan:

- YOLO — detektor cepat dasar.
- Early/mid/late fusion — titik fusi.
- RGB-D input.
- Deteksi real-time.

## Metodologi & Arsitektur
Arsitektur dua-cabang (RGB & kedalaman) gaya YOLO diuji dengan menggabungkan cabang pada posisi berbeda (input=early, fitur tengah=mid, keputusan=late); akurasi dan kecepatan dibandingkan pada dataset RGB-D untuk menemukan posisi fusi optimal.

Komponen / langkah metodologis utama:

- Arsitektur dua-cabang RGB & kedalaman.
- Eksperimen early fusion (input).
- Eksperimen mid-level fusion (fitur tengah).
- Eksperimen late fusion (keputusan).
- Basis detektor gaya YOLO (real-time).
- Evaluasi dataset RGB-D.

## Kontribusi Utama
1. Perbandingan sistematis titik fusi RGB-D.
2. Bukti fusi mid-level unggul untuk real-time.
3. Panduan empiris desain YOLO+RGB-D.
4. Menegaskan manfaat kedalaman untuk deteksi.

## Rincian Eksperimen
Diuji pada dataset RGB-D (mis. indoor) dengan metrik deteksi (mAP) dan kecepatan, membandingkan posisi fusi (Sensors 2019).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Dataset RGB-D | mAP | fusi mid-level terbaik |
| Early vs mid vs late | perbandingan | mid-level unggul |
| Kecepatan | real-time | terjaga |

## Temuan Kunci
- Fusi tingkat-menengah efektif untuk deteksi real-time.
- Posisi fusi memengaruhi akurasi signifikan.
- Kedalaman meningkatkan deteksi.
- Bukti empiris memandu desain.

## Keunggulan
- Bukti empiris kunci.
- Panduan titik fusi.
- Real-time.

## Keterbatasan
- Cakupan dataset terbatas.
- Bergantung kualitas kedalaman.
- Hasil dapat spesifik-arsitektur.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Studi Ophoff adalah bukti empiris sentral bagi klaster YOLO+RGB-D: fusi tingkat-menengah efektif — temuan yang menopang argumen tinjauan tentang strategi fusi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
- [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [117 - 2024 - Onboard Dynamic-Object Detection (Xu dkk.) - YOLO plus RGB-D](./117%20-%202024%20-%20Onboard%20Dynamic-Object%20Detection%20%28Xu%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
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
Ophoff dkk. membandingkan titik fusi RGB+kedalaman (early/mid/late) pada detektor gaya YOLO, menemukan fusi tingkat-menengah memberi peningkatan akurasi terbaik untuk deteksi real-time.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ophoff2019multimodal` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 118/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
