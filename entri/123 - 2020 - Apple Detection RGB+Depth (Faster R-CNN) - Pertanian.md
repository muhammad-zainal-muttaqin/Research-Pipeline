# 123 - Faster R-CNN-Based Apple Detection in Dense-Foliage Fruiting-Wall Trees Using RGB and Depth Features for Robotic Harvesting

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 123 dari 154 |
| Kunci BibTeX | `fu2020apple` |
| Judul | Faster R-CNN-Based Apple Detection in Dense-Foliage Fruiting-Wall Trees Using RGB and Depth Features for Robotic Harvesting |
| Penulis | Fu, Longsheng; Majeed, Yaqoob; Zhang, Xin; Karkee, Manoj; Zhang, Qin |
| Tahun | 2020 |
| Venue / Jurnal | Biosystems Engineering |
| Tema klaster | Pertanian |
| Kata kunci | pertanian, apel, RGB+Depth, Faster R-CNN, oklusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Faster%20R-CNN-Based%20Apple%20Detection%20in%20Dense-Foliage%20Fruiting-Wall%20Trees%20Using%20RGB%20and%20Depth%20Features%20for%20Robotic%20Harvesting
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Faster%20R-CNN-Based%20Apple%20Detection%20in%20Dense-Foliage%20Fruiting-Wall%20Trees%20Using%20RGB%20and%20Depth%20Features%20for%20Robotic%20Harvesting&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 197 |
| Halaman | 245--256 |

## Ringkasan Eksekutif
Deteksi apel pada pohon dinding-buah berdaun lebat memakai Faster R-CNN dengan fitur RGB dan kedalaman untuk pemanenan robotik.

## Abstrak (Parafrase)
Fu dkk. memakai Faster R-CNN dengan fitur RGB dan kedalaman untuk mendeteksi apel pada pohon fruiting-wall berdaun lebat, di mana oklusi berat. Kanal kedalaman membantu memisahkan buah dari daun/latar, meningkatkan deteksi untuk pemanenan robotik. Ini adalah bukti langsung manfaat depth pada deteksi buah.

## Latar Belakang & Konteks
Oklusi dedaunan lebat pada fruiting-wall menyulitkan deteksi apel dari RGB saja; kedalaman dapat membantu memisahkan buah dari daun.

## Permasalahan yang Diangkat
- Oklusi dedaunan lebat menyulitkan deteksi RGB.
- Buah sulit dipisah dari daun/latar.
- Pemanenan robotik butuh deteksi andal.
- Kedalaman belum banyak dimanfaatkan untuk buah.
- Fruiting-wall padat menantang.

## Tujuan & Pertanyaan Penelitian
- Menambahkan fitur kedalaman ke Faster R-CNN.
- Memisahkan buah dari daun via kedalaman.
- Meningkatkan deteksi untuk panen robotik.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan detektor dua-tahap dan fitur kedalaman.

Karya/konsep pembanding yang relevan:

- Faster R-CNN — detektor dasar.
- RGB+Depth features — fusi.
- Deteksi apel fruiting-wall.
- Pemanenan robotik.

## Metodologi & Arsitektur
Faster R-CNN dimodifikasi untuk menerima fitur RGB dan kedalaman; kedalaman membantu segmentasi buah dari dedaunan pada fruiting-wall; dievaluasi untuk deteksi apel pada oklusi berat; analisis kontribusi kedalaman.

Komponen / langkah metodologis utama:

- Kanal kedalaman ditambahkan ke Faster R-CNN.
- Fusi fitur RGB + kedalaman.
- Pemisahan buah dari daun (kedalaman).
- Deteksi apel pada fruiting-wall padat.
- Analisis kontribusi kedalaman.
- Orientasi panen robotik.

## Kontribusi Utama
1. Bukti langsung kedalaman memperbaiki deteksi buah.
2. Kedalaman memisahkan buah dari daun.
3. Deteksi membaik pada oklusi berat.
4. Aplikasi panen robotik fruiting-wall.

## Rincian Eksperimen
Diuji pada kebun fruiting-wall dengan metrik deteksi apel, membandingkan RGB saja vs RGB+depth (Biosystems Engineering 2020).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Fruiting-wall | akurasi deteksi | RGB+depth > RGB saja |
| Oklusi berat | robustness | kedalaman membantu |
| Kontribusi depth | analisis | memisahkan buah-daun |

## Temuan Kunci
- Kedalaman memperbaiki deteksi buah pada oklusi.
- Buah dapat dipisah dari daun via depth.
- Fusi RGB-D bermanfaat untuk panen.
- Bukti empiris manfaat kedalaman.

## Keunggulan
- Bukti manfaat depth langsung.
- Menangani oklusi.
- Panen robotik.

## Keterbatasan
- Dua-tahap relatif lambat.
- Bergantung kualitas kedalaman.
- Fokus spesies apel/fruiting-wall.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini adalah bukti empiris kunci bahwa depth memperbaiki deteksi buah pada oklusi — inti argumen RGB+Depth dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pertanian** yang baik dibaca berdampingan:

- [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)
- [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md)
- [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md)
- [124 - 2020 - Fruit Detection & 3D Location (Gene-Mola dkk.) - Pertanian](./124%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Location%20%28Gene-Mola%20dkk.%29%20-%20Pertanian.md)
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
Fu dkk. memakai Faster R-CNN dengan fitur RGB dan kedalaman untuk mendeteksi apel pada fruiting-wall berdaun lebat, membuktikan kedalaman memisahkan buah dari daun dan meningkatkan deteksi untuk panen.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `fu2020apple` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 123/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
