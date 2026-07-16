# 126 - An Automated Fruit Harvesting Robot by Using Deep Learning

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 126 dari 154 |
| Kunci BibTeX | `onishi2019harvest` |
| Judul | An Automated Fruit Harvesting Robot by Using Deep Learning |
| Penulis | Onishi, Yuki; Yoshida, Takeshi; Kurita, Hiroki; Fukao, Takanori; Arihara, Hiromu; Iwai, Ayako |
| Tahun | 2019 |
| Venue / Jurnal | ROBOMECH Journal |
| Tema klaster | Pertanian |
| Kata kunci | pertanian, panen robotik, deep learning, SSD/YOLO, pemetikan |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=An%20Automated%20Fruit%20Harvesting%20Robot%20by%20Using%20Deep%20Learning
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=An%20Automated%20Fruit%20Harvesting%20Robot%20by%20Using%20Deep%20Learning&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 6 |
| Nomor | 1 |
| Halaman | 13 |

## Ringkasan Eksekutif
Robot panen buah otomatis memakai deteksi berbasis deep learning dan penginderaan untuk melokalisasi dan memetik buah.

## Abstrak (Parafrase)
Onishi dkk. mengembangkan robot panen buah otomatis yang memakai detektor berbasis deep learning (mis. SSD/YOLO) untuk melokalisasi buah pada citra, lalu penginderaan (stereo/depth) memberi posisi 3D untuk pemetikan oleh lengan robot. Sistem mendemonstrasikan pemetikan buah yang cepat dan andal. (ROBOMECH Journal 2019.)

## Latar Belakang & Konteks
Kekurangan tenaga panen mendorong otomasi; robot perlu mendeteksi dan melokalisasi buah dalam 3D lalu memetiknya secara andal.

## Permasalahan yang Diangkat
- Kekurangan tenaga panen mendorong otomasi.
- Buah perlu dideteksi & dilokalisasi 3D.
- Pemetikan butuh posisi akurat.
- Kondisi kebun bervariasi.
- Deteksi + manipulasi harus terintegrasi.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi buah via deep learning.
- Melokalisasi buah dalam 3D.
- Memetik buah via lengan robot.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan detektor deep learning dan lengan robot.

Karya/konsep pembanding yang relevan:

- Detektor DL (SSD/YOLO).
- Penginderaan stereo/depth.
- Lengan robot pemetik.
- Panen buah.

## Metodologi & Arsitektur
Detektor deep learning mendeteksi buah pada citra; penginderaan (stereo/depth) mengestimasi posisi 3D buah; lengan robot bergerak ke posisi dan memetik; sistem diuji untuk kecepatan dan keberhasilan pemetikan.

Komponen / langkah metodologis utama:

- Deteksi buah via deep learning (SSD/YOLO).
- Estimasi posisi 3D (stereo/depth).
- Lengan robot pemetik.
- Integrasi persepsi-manipulasi.
- Uji pemetikan.
- Sistem robot panen.

## Kontribusi Utama
1. Robot panen buah otomatis berbasis DL.
2. Lokalisasi 3D untuk pemetikan.
3. Integrasi deteksi + manipulasi.
4. Demonstrasi pemetikan cepat & andal.

## Rincian Eksperimen
Diuji pada skenario panen dengan metrik keberhasilan dan kecepatan pemetikan (ROBOMECH Journal 2019).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Panen | success rate | pemetikan andal dilaporkan |
| Lokalisasi | 3D | posisi buah via penginderaan |
| Integrasi | DL+robot | persepsi-manipulasi |

## Temuan Kunci
- DL memungkinkan deteksi buah untuk panen otomatis.
- Penginderaan 3D penting untuk pemetikan.
- Integrasi deteksi-manipulasi kunci.
- Otomasi panen buah demonstratif.

## Keunggulan
- Panen otomatis berbasis DL.
- Lokalisasi 3D.
- Integrasi sistem.

## Keterbatasan
- Fokus jenis buah tertentu.
- Kondisi kebun memengaruhi kinerja.
- Kecepatan/keberhasilan masih terbatas.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini mencontohkan panen buah otomatis berbasis deteksi DL + penginderaan 3D dalam tinjauan, paralel dengan sistem YOLO+RGB-D panen.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pertanian** yang baik dibaca berdampingan:

- [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)
- [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md)
- [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md)
- [123 - 2020 - Apple Detection RGB+Depth (Faster R-CNN) - Pertanian](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md)
- [124 - 2020 - Fruit Detection & 3D Location (Gene-Mola dkk.) - Pertanian](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md)
- [125 - 2020 - Iceberg Lettuce Harvesting Robot - Pertanian](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md)
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
Onishi dkk. mengembangkan robot panen buah otomatis dengan deteksi deep learning dan penginderaan 3D untuk melokalisasi dan memetik buah, mendemonstrasikan pemetikan cepat dan andal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `onishi2019harvest` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 126/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
