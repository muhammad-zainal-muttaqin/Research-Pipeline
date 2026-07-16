# 121 - Apple Detection During Different Growth Stages in Orchards Using the Improved YOLO-V3 Model

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 121 dari 154 |
| Kunci BibTeX | `tian2019appleyolo` |
| Judul | Apple Detection During Different Growth Stages in Orchards Using the Improved YOLO-V3 Model |
| Penulis | Tian, Yunong; Yang, Guodong; Wang, Zhe; Wang, Hao; Li, En; Liang, Zize |
| Tahun | 2019 |
| Venue / Jurnal | Computers and Electronics in Agriculture |
| Tema klaster | Pertanian |
| Kata kunci | pertanian, apel, YOLOv3, DenseNet, oklusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Apple%20Detection%20During%20Different%20Growth%20Stages%20in%20Orchards%20Using%20the%20Improved%20YOLO-V3%20Model
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Apple%20Detection%20During%20Different%20Growth%20Stages%20in%20Orchards%20Using%20the%20Improved%20YOLO-V3%20Model&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 157 |
| Halaman | 417--426 |

## Ringkasan Eksekutif
Model YOLOv3 termodifikasi (DenseNet) untuk mendeteksi apel pada berbagai tahap pertumbuhan di kebun pada kondisi cahaya/oklusi beragam.

## Abstrak (Parafrase)
Tian dkk. memodifikasi YOLOv3 dengan densifikasi backbone (DenseNet) untuk mendeteksi apel pada tahap pertumbuhan berbeda (muda hingga matang) di kebun. Model dirancang robust terhadap oklusi daun, variasi warna tahap tumbuh, dan pencahayaan, mencapai akurasi tinggi lintas kondisi.

## Latar Belakang & Konteks
Deteksi apel terkendala oklusi dedaunan, variasi warna antar-tahap tumbuh (hijau muda vs merah matang), dan pencahayaan yang berubah di kebun.

## Permasalahan yang Diangkat
- Oklusi daun/cabang menutupi apel.
- Warna apel bervariasi antar-tahap tumbuh.
- Pencahayaan kebun berubah-ubah.
- Deteksi objek kecil/berhimpitan sulit.
- Model perlu robust lintas kondisi.

## Tujuan & Pertanyaan Penelitian
- Memodifikasi YOLOv3 untuk domain apel.
- Meningkatkan robustness terhadap oklusi/cahaya.
- Mendeteksi apel lintas tahap pertumbuhan.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menyempurnakan YOLOv3 untuk deteksi buah.

Karya/konsep pembanding yang relevan:

- YOLOv3 — detektor dasar.
- DenseNet — densifikasi backbone.
- Deteksi apel kebun.
- Dataset apel multi-tahap.

## Metodologi & Arsitektur
Backbone YOLOv3 didensifikasi (koneksi padat gaya DenseNet) untuk fitur lebih kaya; model dilatih pada citra apel berbagai tahap tumbuh dan kondisi; dievaluasi untuk robustness terhadap oklusi dan pencahayaan.

Komponen / langkah metodologis utama:

- Densifikasi backbone YOLOv3 (DenseNet).
- Fitur lebih kaya untuk objek sulit.
- Robust terhadap oklusi & pencahayaan.
- Deteksi apel multi-tahap tumbuh.
- Pelatihan pada citra kebun.
- Evaluasi lintas kondisi.

## Kontribusi Utama
1. Modifikasi backbone YOLOv3 memperkuat deteksi buah.
2. Robust terhadap oklusi & variasi warna.
3. Akurasi tinggi lintas tahap tumbuh.
4. Aplikasi apel kebun yang praktis.

## Rincian Eksperimen
Diuji pada dataset apel kebun (berbagai tahap tumbuh/kondisi) dengan metrik deteksi, dibandingkan YOLOv3 baseline.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Apel kebun | akurasi/F1 | tinggi lintas kondisi |
| Tahap tumbuh | robustness | muda hingga matang |
| vs YOLOv3 | perbandingan | densifikasi menyumbang gain |

## Temuan Kunci
- Densifikasi backbone memperkuat fitur deteksi buah.
- Robustness lintas tahap tumbuh penting.
- Oklusi tetap tantangan utama.
- Modifikasi domain-spesifik bermanfaat.

## Keunggulan
- Robust lintas kondisi.
- Multi-tahap tumbuh.
- Modifikasi efektif.

## Keterbatasan
- Fokus spesies apel.
- RGB saja (tanpa depth).
- Oklusi berat tetap menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menunjukkan modifikasi backbone YOLO untuk deteksi buah lapangan dalam tinjauan; menegaskan adaptasi domain YOLO untuk pertanian.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pertanian** yang baik dibaca berdampingan:

- [120 - 2019 - MangoYOLO - Pertanian](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md)
- [122 - 2020 - Apple Flower Detection (Pruned YOLOv4) - Pertanian](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md)
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
Tian dkk. memodifikasi YOLOv3 dengan densifikasi backbone untuk mendeteksi apel lintas tahap pertumbuhan di kebun, robust terhadap oklusi dan variasi pencahayaan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `tian2019appleyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 121/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
