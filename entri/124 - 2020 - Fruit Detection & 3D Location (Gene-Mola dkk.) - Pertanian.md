# 124 - Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 124 dari 154 |
| Kunci BibTeX | `genemola2020fruit3d` |
| Judul | Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry |
| Penulis | Gen{\'e |
| Tahun | 2020 |
| Venue / Jurnal | Computers and Electronics in Agriculture |
| Tema klaster | Pertanian |
| Kata kunci | pertanian, instance segmentation, SfM, lokasi 3D, Mask R-CNN |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pertanian)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Fruit%20Detection%20and%203D%20Location%20Using%20Instance%20Segmentation%20Neural%20Networks%20and%20Structure-from-Motion%20Photogrammetry
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Fruit%20Detection%20and%203D%20Location%20Using%20Instance%20Segmentation%20Neural%20Networks%20and%20Structure-from-Motion%20Photogrammetry&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 169 |
| Halaman | 105165 |

## Ringkasan Eksekutif
Menggabungkan instance segmentation (Mask R-CNN) dan fotogrametri Structure-from-Motion untuk deteksi buah dan lokasi 3D-nya di kebun.

## Abstrak (Parafrase)
Gene-Mola dkk. mendeteksi dan mensegmentasi buah dengan Mask R-CNN pada banyak citra, lalu memakai Structure-from-Motion (SfM) photogrammetry untuk merekonstruksi posisi 3D tiap buah di kebun. Ini menyediakan lokasi 3D buah (bukan hanya deteksi 2D) untuk pemetaan/panen, sebagai jalur alternatif lokalisasi 3D tanpa sensor depth aktif.

## Latar Belakang & Konteks
Lokasi 3D buah diperlukan untuk panen/pemetaan, bukan hanya deteksi 2D; sensor depth aktif tidak selalu tersedia, sehingga SfM menjadi alternatif.

## Permasalahan yang Diangkat
- Lokasi 3D buah diperlukan (bukan hanya 2D).
- Sensor depth aktif tak selalu tersedia.
- Rekonstruksi 3D kebun menantang.
- Buah perlu disegmentasi per-instance.
- Pemetaan/panen butuh koordinat 3D.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi & mensegmentasi buah (Mask R-CNN).
- Merekonstruksi lokasi 3D via SfM.
- Menyediakan lokasi 3D untuk pemetaan/panen.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan segmentasi instan dan rekonstruksi 3D.

Karya/konsep pembanding yang relevan:

- Mask R-CNN — instance segmentation.
- Structure-from-Motion (SfM) — rekonstruksi 3D.
- Deteksi buah kebun.
- Lokalisasi 3D.

## Metodologi & Arsitektur
Mask R-CNN mendeteksi dan mensegmentasi buah pada banyak citra kebun; SfM photogrammetry merekonstruksi struktur 3D scene dari citra multi-view; posisi 3D tiap buah dihitung dari segmentasi + rekonstruksi; menghasilkan peta lokasi buah.

Komponen / langkah metodologis utama:

- Instance segmentation buah (Mask R-CNN).
- SfM photogrammetry (multi-view).
- Rekonstruksi 3D scene kebun.
- Estimasi posisi 3D tiap buah.
- Pemetaan lokasi buah.
- Tanpa sensor depth aktif.

## Kontribusi Utama
1. Deteksi/segmentasi + lokalisasi 3D buah.
2. SfM sebagai alternatif sensor depth.
3. Posisi 3D akurat untuk pemetaan/panen.
4. Jalur lokalisasi 3D tanpa depth aktif.

## Rincian Eksperimen
Diuji pada kebun apel dengan metrik deteksi/segmentasi dan akurasi lokasi 3D buah (Computers and Electronics in Agriculture 2020).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Kebun apel | deteksi/seg | akurat (Mask R-CNN) |
| Lokasi 3D | akurasi | posisi buah via SfM |
| Alternatif depth | SfM | tanpa sensor aktif |

## Temuan Kunci
- SfM dapat memberi lokasi 3D buah tanpa depth aktif.
- Segmentasi instan penting untuk lokalisasi.
- Multi-view memungkinkan rekonstruksi 3D.
- Alternatif praktis untuk pemetaan buah.

## Keunggulan
- Lokalisasi 3D tanpa depth aktif.
- Segmentasi + rekonstruksi.
- Pemetaan buah.

## Keterbatasan
- SfM butuh banyak citra multi-view.
- Rekonstruksi sensitif terhadap gerak/tekstur.
- Fokus spesies apel.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menunjukkan jalur alternatif (SfM) menuju lokalisasi 3D buah dalam tinjauan, melengkapi pendekatan berbasis sensor RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pertanian** yang baik dibaca berdampingan:

- [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)
- [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md)
- [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md)
- [123 - 2020 - Apple Detection RGB+Depth (Faster R-CNN) - Pertanian](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md)
- [125 - 2020 - Iceberg Lettuce Harvesting Robot - Pertanian](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md)
- [126 - 2019 - Automated Fruit Harvesting Robot (Onishi dkk.) - Pertanian](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md)
- [127 - 2020 - Fruit Detection & 3D Visualisation (Kang & Chen) - Pertanian](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pertanian** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pertanian)
Istilah penting untuk memahami makalah ini:

- **Deteksi buah** — Melokalisasi buah untuk estimasi/pemanenan.
- **Oklusi dedaunan** — Buah terhalang daun/cabang.
- **Fruit load** — Estimasi jumlah/beban buah.
- **Robotic harvesting** — Panen otomatis (deteksi + manipulasi).
- **RGB-D/stereo** — Penginderaan kedalaman untuk lokalisasi 3D buah.
- **Instance segmentation** — Segmentasi per-objek untuk buah.
- **Model pruning** — Pemangkasan kanal untuk model ringan.
- **SfM** — Structure-from-Motion; rekonstruksi 3D dari banyak citra.
- **mAP/PR** — Metrik deteksi buah.
- **Kondisi lapangan** — Variasi cahaya/angin/latar di kebun.

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
Gene-Mola dkk. menggabungkan Mask R-CNN dan Structure-from-Motion untuk deteksi buah dan lokasi 3D-nya di kebun, menyediakan lokalisasi 3D tanpa sensor depth aktif.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `genemola2020fruit3d` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 124/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
