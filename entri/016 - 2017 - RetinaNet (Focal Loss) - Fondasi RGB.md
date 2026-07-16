# 016 - Focal Loss for Dense Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 016 dari 154 |
| Kunci BibTeX | `lin2017focal` |
| Judul | Focal Loss for Dense Object Detection |
| Penulis | Lin, Tsung-Yi; Goyal, Priya; Girshick, Ross; He, Kaiming; Doll{\'a |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Computer Vision (ICCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | Focal Loss, RetinaNet, ketidakseimbangan kelas, dense detector, FPN |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-fondasi-rgb)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Focal%20Loss%20for%20Dense%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Focal%20Loss%20for%20Dense%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 2980--2988 |

## Ringkasan Eksekutif
Memperkenalkan Focal Loss yang menekan kontribusi contoh mudah, memungkinkan detektor satu-tahap padat (RetinaNet) mengatasi ketidakseimbangan kelas ekstrem dan menyamai akurasi dua-tahap.

## Abstrak (Parafrase)
Makalah mengidentifikasi ketidakseimbangan foreground-background ekstrem sebagai penyebab utama detektor satu-tahap padat tertinggal akurasinya. Focal Loss memodifikasi cross-entropy dengan faktor (1-p)^gamma yang menurunkan bobot contoh mudah sehingga pelatihan fokus pada contoh sulit. RetinaNet (ResNet+FPN dengan Focal Loss) menyamai/mengungguli detektor dua-tahap sambil mempertahankan kecepatan satu-tahap.

## Latar Belakang & Konteks
Detektor satu-tahap padat mengevaluasi puluhan ribu lokasi, mayoritas latar mudah, yang mendominasi loss dan menenggelamkan sinyal dari contoh sulit sehingga akurasi tertinggal dari dua-tahap.

## Permasalahan yang Diangkat
- Ketidakseimbangan foreground-background masif pada dense detector.
- Contoh mudah mendominasi dan menenggelamkan gradien penting.
- Sampling heuristik (OHEM) tak sepenuhnya menyelesaikan.
- Akurasi satu-tahap tertinggal dari dua-tahap.
- Butuh solusi tanpa mengorbankan kecepatan.

## Tujuan & Pertanyaan Penelitian
- Merumuskan Focal Loss untuk fokus pada contoh sulit.
- Membangun detektor satu-tahap padat yang akurat (RetinaNet).
- Menyamai akurasi dua-tahap pada kecepatan satu-tahap.

## Tinjauan Terdahulu / Posisi Literatur
RetinaNet menganalisis kelemahan SSD/YOLO terhadap dua-tahap dan membangun detektor padat dengan FPN dan Focal Loss.

Karya/konsep pembanding yang relevan:

- SSD/YOLO — dense detector sebelumnya.
- FPN — neck multi-skala.
- OHEM — sampling contoh sulit (pembanding).
- Cross-entropy — basis Focal Loss.

## Metodologi & Arsitektur
Backbone ResNet + FPN menghasilkan fitur multi-skala; dua subnet (klasifikasi & regresi box) diterapkan padat di tiap skala dengan anchor; Focal Loss FL(p)=-(1-p)^gamma log(p) menekan contoh mudah; alpha-balancing menambah penyeimbang kelas.

Komponen / langkah metodologis utama:

- Backbone ResNet + FPN.
- Subnet klasifikasi & regresi padat per skala.
- Anchor multi-skala/rasio.
- Focal Loss (faktor (1-p)^gamma).
- Alpha-balancing kelas.
- NMS akhir.

## Kontribusi Utama
1. Focal Loss mengatasi ketidakseimbangan kelas ekstrem.
2. RetinaNet menyamai/mengungguli dua-tahap saat rilis.
3. Menegaskan penyebab akurasi rendah dense detector.
4. Focal Loss menjadi komponen fundamental yang diadopsi luas.

## Rincian Eksperimen
Diuji di COCO dengan ablation gamma/alpha dan perbandingan terhadap SSD, YOLO, dan detektor dua-tahap (Faster R-CNN/FPN).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | RetinaNet ~39.1% AP (ResNet-101-FPN) |
| Ablation | gamma | gamma=2 optimal; menekan contoh mudah |
| vs dua-tahap | AP | menyamai/mengungguli pada kecepatan satu-tahap |

## Temuan Kunci
- Ketidakseimbangan kelas adalah akar masalah dense detector.
- Focal Loss efektif tanpa sampling heuristik.
- FPN penting untuk multi-skala.
- Satu-tahap dapat menyamai dua-tahap dengan loss tepat.

## Keunggulan
- Akurat dan tetap satu-tahap.
- Focal Loss sederhana dan berdampak besar.
- Berpengaruh luas ke detektor lain.

## Keterbatasan
- Masih berbasis anchor.
- Sedikit lebih lambat dari YOLO/SSD.
- Gamma/alpha perlu penyetelan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Focal Loss diadopsi banyak varian YOLO dan detektor RGB-D untuk menangani ketidakseimbangan; memahaminya penting untuk menilai fungsi loss pada pipeline tinjauan ini.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
- [007 - 2023 - YOLOv7 - Fondasi RGB](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)
- [008 - 2024 - YOLOv9 - Fondasi RGB](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fondasi RGB** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Fondasi RGB)
Istilah penting untuk memahami makalah ini:

- **Bounding box** — Kotak pembatas yang melingkupi objek; (x,y,w,h) atau (x1,y1,x2,y2).
- **Anchor box** — Kotak acuan berukuran/rasio tetap tempat jaringan meregresi offset objek.
- **Anchor-free** — Deteksi tanpa anchor; memprediksi pusat/keypoint atau jarak ke sisi box.
- **mAP** — mean Average Precision; rata-rata AP lintas kelas/ambang IoU.
- **IoU** — Intersection over Union; rasio irisan/gabungan dua box.
- **NMS** — Non-Maximum Suppression; membuang deteksi berlebih yang tumpang tindih.
- **Backbone** — Jaringan ekstraksi fitur (ResNet, CSPDarknet) di awal detektor.
- **Neck** — Modul agregasi fitur multi-skala (FPN, PAN, BiFPN).
- **Head** — Bagian akhir yang menghasilkan prediksi kelas dan box.
- **One-stage vs two-stage** — Satu-tahap (YOLO/SSD) langsung; dua-tahap (Faster R-CNN) pakai proposal.
- **FLOPs** — Floating-point operations; ukuran biaya komputasi.
- **Attention/Transformer** — Mekanisme membobot relasi antar-token/fitur secara global.

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
RetinaNet membuktikan bahwa dengan Focal Loss, detektor satu-tahap padat dapat menyamai akurasi dua-tahap, menjadikan Focal Loss komponen fundamental deteksi modern.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lin2017focal` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 016/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
