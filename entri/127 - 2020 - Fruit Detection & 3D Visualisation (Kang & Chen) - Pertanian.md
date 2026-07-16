# 127 - Fruit Detection, Segmentation and 3D Visualisation of Environments in Apple Orchards

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 127 dari 154 |
| Kunci BibTeX | `kang2020strawberry` |
| Judul | Fruit Detection, Segmentation and 3D Visualisation of Environments in Apple Orchards |
| Penulis | Kang, Hanwen; Chen, Chao |
| Tahun | 2020 |
| Venue / Jurnal | Computers and Electronics in Agriculture |
| Tema klaster | Pertanian |
| Kata kunci | pertanian, deteksi/segmentasi, 3D visualisasi, panen robotik, apel |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Fruit%20Detection%2C%20Segmentation%20and%203D%20Visualisation%20of%20Environments%20in%20Apple%20Orchards
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Fruit%20Detection%2C%20Segmentation%20and%203D%20Visualisation%20of%20Environments%20in%20Apple%20Orchards&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 171 |
| Halaman | 105302 |

## Ringkasan Eksekutif
Kerangka deteksi, segmentasi, dan visualisasi 3D lingkungan kebun apel untuk pemanenan robotik memakai deep learning dan sensor.

## Abstrak (Parafrase)
Kang & Chen mengembangkan kerangka lengkap untuk panen apel robotik: jaringan deteksi/segmentasi buah (mis. DaSNet) mendeteksi dan mensegmentasi apel, dan sensor 3D dipakai untuk memvisualisasikan/merekonstruksi lingkungan kebun dalam 3D. Ini menyediakan persepsi buah sekaligus pemetaan 3D scene untuk perencanaan panen.

## Latar Belakang & Konteks
Panen apel robotik membutuhkan persepsi buah (deteksi/segmentasi) sekaligus pemahaman 3D lingkungan untuk perencanaan gerak dan pemetikan.

## Permasalahan yang Diangkat
- Panen robotik butuh persepsi buah + 3D scene.
- Deteksi/segmentasi buah menantang di kebun.
- Pemetaan 3D lingkungan diperlukan.
- Perencanaan gerak butuh geometri 3D.
- Kondisi kebun kompleks.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi & mensegmentasi buah apel.
- Memvisualisasikan/merekonstruksi scene 3D.
- Mendukung perencanaan panen robotik.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan deteksi/segmentasi dan rekonstruksi 3D.

Karya/konsep pembanding yang relevan:

- Jaringan deteksi/segmentasi (DaSNet).
- Sensor 3D (RGB-D/stereo).
- Visualisasi/rekonstruksi 3D.
- Panen apel robotik.

## Metodologi & Arsitektur
Jaringan deteksi/segmentasi mengidentifikasi dan memisahkan apel pada citra; sensor 3D (RGB-D/stereo) memberi geometri; scene kebun direkonstruksi/divisualisasikan 3D dengan buah terlokalisasi; mendukung perencanaan panen.

Komponen / langkah metodologis utama:

- Deteksi/segmentasi buah (DaSNet).
- Sensor 3D untuk geometri.
- Rekonstruksi/visualisasi 3D scene.
- Lokalisasi buah dalam 3D.
- Dukungan perencanaan panen.
- Kerangka persepsi lengkap.

## Kontribusi Utama
1. Persepsi buah + pemetaan 3D scene.
2. Deteksi/segmentasi akurat.
3. Visualisasi 3D untuk perencanaan.
4. Kerangka menyeluruh panen robotik.

## Rincian Eksperimen
Diuji pada kebun apel dengan metrik deteksi/segmentasi dan kualitas rekonstruksi 3D (Computers and Electronics in Agriculture 2020).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Kebun apel | deteksi/seg | akurat |
| Scene 3D | rekonstruksi | peta 3D kebun |
| Perencanaan | dukungan | lokalisasi buah 3D |

## Temuan Kunci
- Persepsi buah + 3D scene mendukung panen.
- Segmentasi memisahkan buah dari latar.
- Sensor 3D memberi geometri untuk perencanaan.
- Kerangka menyeluruh bermanfaat.

## Keunggulan
- Persepsi 3D menyeluruh.
- Deteksi/segmentasi + rekonstruksi.
- Dukung panen.

## Keterbatasan
- Fokus spesies apel.
- Bergantung kualitas sensor 3D.
- Kondisi kebun kompleks.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menyediakan persepsi 3D menyeluruh untuk panen robotik dalam tinjauan, menautkan deteksi/segmentasi dengan pemetaan RGB-D/3D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pertanian** yang baik dibaca berdampingan:

- [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)
- [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md)
- [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md)
- [123 - 2020 - Apple Detection RGB+Depth (Faster R-CNN) - Pertanian](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md)
- [124 - 2020 - Fruit Detection & 3D Location (Gene-Mola dkk.) - Pertanian](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md)
- [125 - 2020 - Iceberg Lettuce Harvesting Robot - Pertanian](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md)
- [126 - 2019 - Automated Fruit Harvesting Robot (Onishi dkk.) - Pertanian](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md)

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
Kang & Chen mengembangkan kerangka deteksi, segmentasi, dan visualisasi 3D scene kebun apel untuk panen robotik, menyediakan persepsi buah sekaligus pemetaan 3D untuk perencanaan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `kang2020strawberry` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 127/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
