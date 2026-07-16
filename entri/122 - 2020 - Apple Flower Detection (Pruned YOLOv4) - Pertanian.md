# 122 - Using Channel Pruning-Based YOLO v4 Deep Learning Algorithm for the Real-Time and Accurate Detection of Apple Flowers in Natural Environments

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 122 dari 154 |
| Kunci BibTeX | `wu2020flower` |
| Judul | Using Channel Pruning-Based YOLO v4 Deep Learning Algorithm for the Real-Time and Accurate Detection of Apple Flowers in Natural Environments |
| Penulis | Wu, Dihua; Lv, Shuqin; Jiang, Mei; Song, Huaibo |
| Tahun | 2020 |
| Venue / Jurnal | Computers and Electronics in Agriculture |
| Tema klaster | Pertanian |
| Kata kunci | pertanian, bunga apel, YOLOv4, channel pruning, real-time |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Using%20Channel%20Pruning-Based%20YOLO%20v4%20Deep%20Learning%20Algorithm%20for%20the%20Real-Time%20and%20Accurate%20Detection%20of%20Apple%20Flowers%20in%20Natural%20Environments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Using%20Channel%20Pruning-Based%20YOLO%20v4%20Deep%20Learning%20Algorithm%20for%20the%20Real-Time%20and%20Accurate%20Detection%20of%20Apple%20Flowers%20in%20Natural%20Environments&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 178 |
| Halaman | 105742 |

## Ringkasan Eksekutif
YOLOv4 dengan channel pruning untuk deteksi bunga apel real-time dan akurat di lingkungan alami (untuk penjarangan/estimasi hasil).

## Abstrak (Parafrase)
Wu dkk. menerapkan channel pruning pada YOLOv4 untuk menghasilkan model deteksi bunga apel yang ringan dan real-time namun tetap akurat di lingkungan alami. Deteksi bunga berguna untuk penjarangan (thinning) dan estimasi hasil awal. Pruning menekan ukuran/latensi tanpa kehilangan akurasi berarti.

## Latar Belakang & Konteks
Deteksi bunga apel real-time di lapangan membutuhkan model ringan yang dapat berjalan pada perangkat terbatas namun tetap akurat.

## Permasalahan yang Diangkat
- Deteksi bunga real-time butuh model ringan.
- Perangkat lapangan terbatas komputasi.
- Bunga kecil dan padat sulit dideteksi.
- Lingkungan alami bervariasi.
- Akurasi tak boleh dikorbankan berlebihan.

## Tujuan & Pertanyaan Penelitian
- Menerapkan channel pruning pada YOLOv4.
- Menghasilkan model bunga apel ringan real-time.
- Menjaga akurasi deteksi.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menerapkan pruning pada YOLOv4 untuk efisiensi.

Karya/konsep pembanding yang relevan:

- YOLOv4 — detektor dasar.
- Channel pruning — kompresi model.
- Deteksi bunga apel.
- Aplikasi penjarangan/estimasi.

## Metodologi & Arsitektur
YOLOv4 dilatih untuk deteksi bunga apel lalu dipangkas (channel pruning) untuk mengurangi kanal/parameter; model ringan hasil pruning dievaluasi untuk akurasi-kecepatan di lingkungan alami; cocok untuk deployment lapangan.

Komponen / langkah metodologis utama:

- Pelatihan YOLOv4 untuk bunga apel.
- Channel pruning (kompresi kanal).
- Model ringan real-time.
- Deteksi bunga di lingkungan alami.
- Deployment lapangan.
- Evaluasi akurasi-kecepatan.

## Kontribusi Utama
1. Kompresi YOLOv4 via channel pruning.
2. Model bunga apel ringan & real-time.
3. Akurasi terjaga pasca-pruning.
4. Contoh deployment pertanian efisien.

## Rincian Eksperimen
Diuji pada dataset bunga apel dengan metrik deteksi dan ukuran/kecepatan model, dibandingkan YOLOv4 penuh.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Bunga apel | akurasi | terjaga pasca-pruning |
| Model | ukuran/kecepatan | jauh lebih ringan/cepat |
| vs YOLOv4 | perbandingan | efisiensi meningkat |

## Temuan Kunci
- Pruning menekan ukuran/latensi efektif.
- Akurasi dapat dipertahankan pasca-pruning.
- Model ringan cocok untuk lapangan.
- Deteksi bunga berguna untuk penjarangan.

## Keunggulan
- Ringan & real-time.
- Akurasi terjaga.
- Cocok lapangan.

## Keterbatasan
- Fokus bunga apel.
- RGB saja (tanpa depth).
- Bunga padat/kecil menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini mencontohkan kompresi model YOLO untuk deployment pertanian dalam tinjauan; relevan bagi efisiensi yang juga penting pada RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pertanian** yang baik dibaca berdampingan:

- [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)
- [121 - 2019 - Apple Detection (Improved YOLOv3) - Pertanian](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md)
- [123 - 2020 - Apple Detection RGB+Depth (Faster R-CNN) - Pertanian](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md)
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
Wu dkk. menerapkan channel pruning pada YOLOv4 untuk deteksi bunga apel real-time yang ringan namun akurat, cocok untuk penjarangan dan estimasi hasil di lapangan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wu2020flower` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 122/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
