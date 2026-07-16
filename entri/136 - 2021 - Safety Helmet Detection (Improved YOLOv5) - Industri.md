# 136 - Safety Helmet Wearing Detection Based on Improved YOLOv5

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 136 dari 154 |
| Kunci BibTeX | `zhou2021helmet` |
| Judul | Safety Helmet Wearing Detection Based on Improved YOLOv5 |
| Penulis | Zhou, Fang; Zhao, Huailin; Nie, Zhen |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Computer Vision, Image and Deep Learning (CVIDL) |
| Tema klaster | Industri |
| Kata kunci | industri, helm keselamatan, YOLOv5, K3, real-time |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Safety%20Helmet%20Wearing%20Detection%20Based%20on%20Improved%20YOLOv5
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Safety%20Helmet%20Wearing%20Detection%20Based%20on%20Improved%20YOLOv5&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 611--614 |

## Ringkasan Eksekutif
YOLOv5 termodifikasi untuk deteksi pemakaian helm keselamatan di lokasi kerja guna pemantauan K3.

## Abstrak (Parafrase)
Zhou dkk. memodifikasi YOLOv5 untuk mendeteksi pemakaian helm keselamatan (safety helmet) pekerja di lokasi konstruksi secara real-time. Peningkatan arsitektur menargetkan objek kecil (kepala/helm dari jauh), mendukung pemantauan kepatuhan keselamatan kerja (K3).

## Latar Belakang & Konteks
Kepatuhan pemakaian helm perlu dipantau otomatis untuk keselamatan kerja; deteksi manual tidak praktis dan objek (helm dari jauh) kecil.

## Permasalahan yang Diangkat
- Kepatuhan helm perlu pemantauan otomatis.
- Deteksi manual tidak praktis.
- Helm dari jauh berukuran kecil.
- Real-time diperlukan untuk pemantauan.
- Lokasi kerja ramai/kompleks.

## Tujuan & Pertanyaan Penelitian
- Memodifikasi YOLOv5 untuk deteksi helm.
- Menargetkan objek kecil (helm jauh).
- Mendukung pemantauan K3 real-time.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menyempurnakan YOLOv5 untuk deteksi helm.

Karya/konsep pembanding yang relevan:

- YOLOv5 — detektor dasar.
- Peningkatan objek kecil.
- Deteksi helm keselamatan.
- Pemantauan K3.

## Metodologi & Arsitektur
YOLOv5 dimodifikasi (mis. attention/skala tambahan) untuk memperkuat deteksi helm kecil; dilatih pada dataset helm konstruksi; dievaluasi real-time untuk pemantauan kepatuhan; cocok untuk CCTV lokasi kerja.

Komponen / langkah metodologis utama:

- Modifikasi YOLOv5 untuk objek kecil.
- Deteksi pemakaian helm.
- Real-time (CCTV lokasi kerja).
- Pelatihan pada dataset helm.
- Pemantauan kepatuhan K3.
- Evaluasi akurasi-kecepatan.

## Kontribusi Utama
1. Deteksi helm real-time berbasis YOLOv5.
2. Peningkatan untuk objek kecil.
3. Dukungan pemantauan K3.
4. Aplikasi keselamatan kerja.

## Rincian Eksperimen
Diuji pada dataset helm konstruksi dengan metrik deteksi dan kecepatan (CVIDL 2021).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Helm konstruksi | mAP | tinggi real-time |
| Objek kecil | akurasi | helm jauh ditingkatkan |
| Pemantauan | K3 | kepatuhan otomatis |

## Temuan Kunci
- YOLOv5 dapat diadaptasi untuk deteksi helm.
- Objek kecil menuntut peningkatan arsitektur.
- Real-time penting untuk pemantauan.
- Aplikasi keselamatan bermanfaat.

## Keunggulan
- Real-time.
- Objek kecil.
- Aplikasi K3.

## Keterbatasan
- Fokus deteksi helm.
- RGB saja.
- Lingkungan ramai menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini mencontohkan aplikasi YOLO untuk pemantauan keselamatan kerja dalam klaster Industri tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Industri** yang baik dibaca berdampingan:

- [133 - 2023 - EFC-YOLO (Steel Strip Defects) - Industri](./133%20-%202023%20-%20EFC-YOLO%20%28Steel%20Strip%20Defects%29%20-%20Industri.md)
- [134 - 2024 - PCB-YOLO (PCB Defects) - Industri](./134%20-%202024%20-%20PCB-YOLO%20%28PCB%20Defects%29%20-%20Industri.md)
- [135 - 2021 - Review Defect Detection (Bhatt dkk.) - Industri](./135%20-%202021%20-%20Review%20Defect%20Detection%20%28Bhatt%20dkk.%29%20-%20Industri.md)

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
Zhou dkk. memodifikasi YOLOv5 untuk deteksi pemakaian helm keselamatan real-time di lokasi kerja, menargetkan objek kecil untuk mendukung pemantauan kepatuhan K3.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhou2021helmet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 136/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
