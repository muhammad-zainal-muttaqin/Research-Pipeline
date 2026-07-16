# 146 - Microsoft COCO: Common Objects in Context

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 146 dari 154 |
| Kunci BibTeX | `lin2014coco` |
| Judul | Microsoft COCO: Common Objects in Context |
| Penulis | Lin, Tsung-Yi; Maire, Michael; Belongie, Serge; Hays, James; Perona, Pietro; Ramanan, Deva; Doll{\'a |
| Tahun | 2014 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Dataset |
| Kata kunci | dataset, deteksi, segmentasi, konteks, metrik AP |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-dataset)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Microsoft%20COCO%3A%20Common%20Objects%20in%20Context
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Microsoft%20COCO%3A%20Common%20Objects%20in%20Context&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 740--755 |

## Ringkasan Eksekutif
Dataset deteksi/segmentasi/captioning berskala dengan objek dalam konteks dan anotasi instance padat, mendefinisikan evaluasi deteksi modern (metrik AP).

## Abstrak (Parafrase)
COCO (Lin dkk.) menyediakan ~330 ribu citra dengan 80 kategori dan ~1.5 juta instance objek beranotasi (kotak + mask), menampilkan objek dalam konteks natural dan banyak objek kecil. Metrik AP-nya (rata-rata AP pada IoU 0.5:0.95) menjadi standar de-facto evaluasi hampir semua detektor, termasuk YOLO.

## Latar Belakang & Konteks
Dataset deteksi sebelumnya terbatas skala/konteks; diperlukan benchmark besar dengan objek dalam konteks natural dan banyak objek kecil untuk mendorong deteksi robust.

## Permasalahan yang Diangkat
- Dataset deteksi sebelumnya terbatas skala/konteks.
- Objek dalam konteks natural kurang tercakup.
- Objek kecil beragam diperlukan.
- Metrik evaluasi belum seragam.
- Anotasi instance padat mahal.

## Tujuan & Pertanyaan Penelitian
- Menyediakan dataset deteksi/segmentasi berskala.
- Menampilkan objek dalam konteks + banyak objek kecil.
- Mendefinisikan metrik AP standar.

## Tinjauan Terdahulu / Posisi Literatur
COCO menyediakan benchmark deteksi/segmentasi standar.

Karya/konsep pembanding yang relevan:

- Deteksi/segmentasi/captioning — tugas.
- 80 kategori objek.
- Anotasi instance (kotak + mask).
- Metrik AP (IoU 0.5:0.95).

## Metodologi & Arsitektur
~330k citra dianotasi dengan kotak dan mask instance untuk 80 kategori, menampilkan objek dalam konteks natural; metrik AP (rata-rata pada IoU 0.5:0.95) dan AP per ukuran objek (S/M/L) didefinisikan sebagai standar evaluasi.

Komponen / langkah metodologis utama:

- ~330k citra, 80 kategori, ~1.5M instance.
- Anotasi kotak + mask instance.
- Objek dalam konteks natural.
- Banyak objek kecil.
- Metrik AP (IoU 0.5:0.95) standar.
- AP per ukuran objek (S/M/L).

## Kontribusi Utama
1. Dataset deteksi/segmentasi berskala & kontekstual.
2. Anotasi instance padat (kotak + mask).
3. Metrik AP standar de-facto.
4. Mendefinisikan evaluasi deteksi modern.

## Rincian Eksperimen
Menyediakan benchmark COCO; hampir semua detektor (termasuk YOLO) dievaluasi dengan metrik AP-nya.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO deteksi | AP | standar evaluasi de-facto |
| COCO segmentasi | AP mask | benchmark instance seg |
| Objek kecil | AP-S | tantangan kunci |

## Temuan Kunci
- Skala & konteks mendorong deteksi robust.
- Metrik AP menyeragamkan evaluasi.
- Objek kecil menjadi tantangan sentral.
- Benchmark de-facto memacu kemajuan.

## Keunggulan
- Benchmark deteksi de-facto.
- Anotasi kaya.
- Metrik AP standar.

## Keterbatasan
- Anotasi mahal.
- Domain objek umum (bukan RGB-D).
- Bias distribusi kelas.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
COCO mendefinisikan metrik dan benchmark yang dipakai semua entri YOLO dan detektor RGB dalam tinjauan; fundamental untuk perbandingan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Dataset** yang baik dibaca berdampingan:

- [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)
- [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)
- [143 - 2017 - ScanNet - Dataset](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)
- [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)
- [145 - 2020 - nuScenes - Dataset](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Dataset** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Dataset)
Istilah penting untuk memahami makalah ini:

- **Benchmark** — Dataset+metrik standar untuk evaluasi adil.
- **Anotasi** — Label ground-truth (box, mask, pose, depth).
- **RGB-D** — Data warna berpasangan kedalaman.
- **Split train/val/test** — Pembagian data pelatihan/evaluasi.
- **Metrik** — Ukuran kinerja (mAP, mIoU, AbsRel).
- **Sensor** — Perangkat akuisisi (Kinect, LiDAR, stereo).
- **Skala** — Jumlah citra/instance.
- **Kelas/kategori** — Jenis objek yang dilabeli.
- **Kalibrasi** — Parameter intrinsik/ekstrinsik sensor.
- **Generalisasi** — Kemampuan lintas domain.

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
COCO menyediakan dataset deteksi/segmentasi berskala dengan objek dalam konteks dan metrik AP standar, mendefinisikan evaluasi deteksi modern yang dipakai hampir semua detektor termasuk YOLO.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lin2014coco` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 146/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
