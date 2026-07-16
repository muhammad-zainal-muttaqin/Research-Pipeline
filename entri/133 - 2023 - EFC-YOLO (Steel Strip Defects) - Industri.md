# 133 - EFC-YOLO: An Efficient Surface-Defect-Detection Algorithm for Steel Strips

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 133 dari 154 |
| Kunci BibTeX | `yang2023efcyolo` |
| Judul | EFC-YOLO: An Efficient Surface-Defect-Detection Algorithm for Steel Strips |
| Penulis | Yang, Yize; Li, Fengyi; Wang, Bao |
| Tahun | 2023 |
| Venue / Jurnal | Sensors |
| Tema klaster | Industri |
| Kata kunci | industri, cacat, baja, YOLO, real-time |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-industri)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=EFC-YOLO%3A%20An%20Efficient%20Surface-Defect-Detection%20Algorithm%20for%20Steel%20Strips
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=EFC-YOLO%3A%20An%20Efficient%20Surface-Defect-Detection%20Algorithm%20for%20Steel%20Strips&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 23 |
| Nomor | 17 |
| Halaman | 7619 |

## Ringkasan Eksekutif
Algoritma deteksi cacat permukaan efisien untuk strip baja berbasis YOLO dengan modul fitur yang disempurnakan.

## Abstrak (Parafrase)
Yang dkk. mengembangkan EFC-YOLO, detektor cacat permukaan strip baja berbasis YOLO dengan modul ekstraksi fitur yang efisien dan dioptimalkan untuk cacat kecil. Model mencapai akurasi tinggi secara real-time pada inspeksi cacat baja, cocok untuk lini produksi.

## Latar Belakang & Konteks
Deteksi cacat strip baja membutuhkan akurasi tinggi pada cacat kecil sekaligus kecepatan real-time untuk inspeksi inline.

## Permasalahan yang Diangkat
- Cacat strip baja sering berukuran kecil.
- Inspeksi inline butuh real-time.
- Akurasi tinggi diperlukan.
- Variasi cacat beragam.
- Model perlu efisien.

## Tujuan & Pertanyaan Penelitian
- Merancang modul fitur efisien untuk cacat.
- Mengoptimalkan deteksi cacat kecil.
- Mencapai deteksi cacat real-time akurat.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menyempurnakan YOLO untuk inspeksi cacat.

Karya/konsep pembanding yang relevan:

- YOLO — detektor dasar.
- Modul fitur efisien.
- Deteksi cacat baja.
- Dataset cacat (NEU).

## Metodologi & Arsitektur
EFC-YOLO menambahkan modul ekstraksi fitur efisien pada YOLO untuk memperkuat deteksi cacat kecil; dilatih pada dataset cacat baja; dioptimalkan untuk akurasi-kecepatan real-time; cocok untuk lini produksi.

Komponen / langkah metodologis utama:

- Modul ekstraksi fitur efisien.
- Optimasi untuk cacat kecil.
- Basis YOLO (real-time).
- Pelatihan pada cacat baja.
- Inspeksi inline.
- Evaluasi dataset cacat.

## Kontribusi Utama
1. Detektor cacat baja berbasis YOLO efisien.
2. Akurasi tinggi pada cacat kecil.
3. Real-time untuk inspeksi inline.
4. Contoh kustomisasi YOLO industri.

## Rincian Eksperimen
Diuji pada dataset cacat baja (mis. NEU) dengan metrik deteksi (mAP) dan kecepatan (Sensors 2023).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Cacat baja (NEU) | mAP | tinggi |
| Cacat kecil | akurasi | dioptimalkan |
| Kecepatan | real-time | cocok inline |

## Temuan Kunci
- Modul fitur efisien memperkuat deteksi cacat kecil.
- Real-time penting untuk inspeksi inline.
- Kustomisasi domain bermanfaat.
- YOLO cocok untuk inspeksi industri.

## Keunggulan
- Efisien & real-time.
- Akurat cacat kecil.
- Cocok industri.

## Keterbatasan
- Fokus cacat baja.
- RGB saja.
- Generalisasi antar-cacat bervariasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini mencontohkan kustomisasi YOLO untuk inspeksi cacat industri dalam klaster Industri tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Industri** yang baik dibaca berdampingan:

- [134 - 2024 - PCB-YOLO (PCB Defects) - Industri](./134%20-%202024%20-%20PCB-YOLO%20%28PCB%20Defects%29%20-%20Industri.md)
- [135 - 2021 - Review Defect Detection (Bhatt dkk.) - Industri](./135%20-%202021%20-%20Review%20Defect%20Detection%20%28Bhatt%20dkk.%29%20-%20Industri.md)
- [136 - 2021 - Safety Helmet Detection (Improved YOLOv5) - Industri](./136%20-%202021%20-%20Safety%20Helmet%20Detection%20%28Improved%20YOLOv5%29%20-%20Industri.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Industri** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Industri)
Istilah penting untuk memahami makalah ini:

- **Deteksi cacat** — Menemukan defect pada permukaan produk.
- **Inspeksi visual** — Pemeriksaan kualitas berbasis kamera.
- **Cacat kecil** — Defect mikro yang sulit dideteksi.
- **Coordinate attention** — Attention menyandikan posisi.
- **Multi-scale fusion** — Penggabungan fitur lintas skala.
- **NEU/PCB dataset** — Benchmark cacat baja / PCB.
- **mAP/recall** — Metrik deteksi cacat.
- **Real-time inline** — Inspeksi pada laju produksi.
- **K3/helm** — Pemantauan keselamatan kerja.
- **Industry 4.0** — Manufaktur cerdas terintegrasi AI.

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
EFC-YOLO adalah detektor cacat permukaan strip baja berbasis YOLO dengan modul fitur efisien, mencapai akurasi tinggi pada cacat kecil secara real-time untuk inspeksi inline.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yang2023efcyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 133/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
