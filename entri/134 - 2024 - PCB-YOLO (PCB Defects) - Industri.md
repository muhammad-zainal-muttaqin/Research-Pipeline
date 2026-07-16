# 134 - PCB-YOLO: Enhancing PCB Surface Defect Detection with Coordinate Attention and Multi-Scale Feature Fusion

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 134 dari 154 |
| Kunci BibTeX | `tang2024pcbyolo` |
| Judul | PCB-YOLO: Enhancing PCB Surface Defect Detection with Coordinate Attention and Multi-Scale Feature Fusion |
| Penulis | Tang, Junyan; others |
| Tahun | 2024 |
| Venue / Jurnal | PLOS ONE |
| Tema klaster | Industri |
| Kata kunci | industri, PCB, cacat, coordinate attention, multi-skala |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PCB-YOLO%3A%20Enhancing%20PCB%20Surface%20Defect%20Detection%20with%20Coordinate%20Attention%20and%20Multi-Scale%20Feature%20Fusion
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PCB-YOLO%3A%20Enhancing%20PCB%20Surface%20Defect%20Detection%20with%20Coordinate%20Attention%20and%20Multi-Scale%20Feature%20Fusion&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 19 |
| Nomor | 5 |
| Halaman | e0323684 |

## Ringkasan Eksekutif
Detektor cacat permukaan PCB berbasis YOLO yang diperkuat coordinate attention dan fusi fitur multi-skala.

## Abstrak (Parafrase)
Tang dkk. mengusulkan PCB-YOLO untuk deteksi cacat permukaan papan sirkuit (PCB) dengan menambahkan coordinate attention (menyandikan posisi) dan multi-scale feature fusion untuk menangani cacat kecil dan padat. Model meningkatkan mAP atas baseline pada dataset cacat PCB.

## Latar Belakang & Konteks
Cacat PCB sering sangat kecil dan padat sehingga sulit dideteksi detektor umum; attention dan fusi multi-skala dapat membantu.

## Permasalahan yang Diangkat
- Cacat PCB sangat kecil dan padat.
- Detektor umum sulit mendeteksi cacat kecil.
- Posisi cacat penting (coordinate attention).
- Fitur multi-skala diperlukan.
- Inspeksi PCB menuntut akurasi tinggi.

## Tujuan & Pertanyaan Penelitian
- Menambahkan coordinate attention.
- Memfusikan fitur multi-skala.
- Meningkatkan deteksi cacat PCB kecil.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menyempurnakan YOLO dengan attention & multi-skala.

Karya/konsep pembanding yang relevan:

- YOLO — detektor dasar.
- Coordinate attention.
- Multi-scale feature fusion.
- Dataset cacat PCB.

## Metodologi & Arsitektur
PCB-YOLO menambahkan coordinate attention (menyandikan informasi posisi ke fitur) dan multi-scale feature fusion pada YOLO untuk memperkuat deteksi cacat kecil; dilatih pada dataset cacat PCB; dievaluasi terhadap baseline.

Komponen / langkah metodologis utama:

- Coordinate attention (posisi ke fitur).
- Multi-scale feature fusion.
- Optimasi cacat kecil/padat.
- Basis YOLO.
- Pelatihan pada cacat PCB.
- Perbandingan dengan baseline.

## Kontribusi Utama
1. Attention + multi-skala untuk cacat PCB.
2. Peningkatan mAP atas baseline.
3. Menangani cacat kecil & padat.
4. Contoh kustomisasi YOLO industri.

## Rincian Eksperimen
Diuji pada dataset cacat PCB dengan metrik deteksi (mAP), dibandingkan baseline (PLOS ONE 2024).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Cacat PCB | mAP | peningkatan atas baseline |
| Cacat kecil | akurasi | attention+multi-skala membantu |
| vs baseline | perbandingan | modifikasi menyumbang gain |

## Temuan Kunci
- Coordinate attention penting untuk cacat kecil.
- Multi-skala membantu objek kecil/padat.
- Kustomisasi domain bermanfaat.
- YOLO cocok untuk inspeksi PCB.

## Keunggulan
- Attention + multi-skala.
- Cacat kecil.
- Peningkatan mAP.

## Keterbatasan
- Fokus cacat PCB.
- RGB saja.
- Generalisasi bervariasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menegaskan pentingnya attention dan multi-skala untuk cacat kecil dalam klaster Industri tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Industri** yang baik dibaca berdampingan:

- [133 - 2023 - EFC-YOLO (Steel Strip Defects) - Industri](./133%20-%202023%20-%20EFC-YOLO%20%28Steel%20Strip%20Defects%29%20-%20Industri.md)
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
PCB-YOLO memperkuat deteksi cacat PCB dengan coordinate attention dan multi-scale feature fusion, meningkatkan mAP untuk cacat kecil dan padat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `tang2024pcbyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 134/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
