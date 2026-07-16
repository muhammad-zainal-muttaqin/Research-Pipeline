# 003 - YOLOv3: An Incremental Improvement

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 003 dari 154 |
| Kunci BibTeX | `redmon2018yolov3` |
| Judul | YOLOv3: An Incremental Improvement |
| Penulis | Redmon, Joseph; Farhadi, Ali |
| Tahun | 2018 |
| Venue / Jurnal | arXiv preprint arXiv:1804.02767 |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv3, Darknet-53, multi-skala, residual, multi-label |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1804.02767
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv3%3A%20An%20Incremental%20Improvement
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv3%3A%20An%20Incremental%20Improvement&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 1804.02767 |

## Ringkasan Eksekutif
Versi ketiga YOLO yang memperkenalkan backbone Darknet-53 residual dan prediksi pada tiga skala berbeda, menjadikannya baseline YOLO paling banyak diadopsi karena keseimbangan kecepatan-akurasi yang matang.

## Abstrak (Parafrase)
YOLOv3 melakukan sejumlah peningkatan inkremental namun berdampak: backbone Darknet-53 dengan koneksi residual yang jauh lebih kuat dari Darknet-19, prediksi pada tiga skala fitur (mirip FPN) untuk menangani objek besar hingga kecil, serta klasifikasi multi-label memakai logistic regression independen alih-alih softmax. Kombinasi ini membuat YOLOv3 sangat kompetitif pada ambang IoU longgar dengan kecepatan tinggi, dan unggul mendeteksi objek kecil dibanding pendahulunya.

## Latar Belakang & Konteks
YOLOv2 masih lemah pada objek kecil dan representasi fiturnya terbatas. Kebutuhan mendeteksi objek pada rentang skala lebar sekaligus mempertahankan kecepatan mendorong desain multi-skala dengan backbone yang lebih dalam namun tetap efisien.

## Permasalahan yang Diangkat
- Deteksi objek kecil masih lemah pada YOLOv2.
- Representasi fitur perlu diperkuat tanpa mengorbankan kecepatan.
- Softmax tak ideal untuk label yang tumpang tindih/multi-label.
- Rentang skala objek yang lebar sulit ditangani satu skala.
- Kedalaman jaringan membutuhkan mekanisme anti-degradasi.

## Tujuan & Pertanyaan Penelitian
- Meningkatkan deteksi multi-skala, khususnya objek kecil.
- Memperkuat backbone dengan koneksi residual.
- Mendukung klasifikasi multi-label.

## Tinjauan Terdahulu / Posisi Literatur
YOLOv3 memadukan gagasan residual (ResNet) dan piramida fitur (FPN) ke dalam kerangka YOLO, mempertahankan filosofi satu-tahap real-time.

Karya/konsep pembanding yang relevan:

- ResNet — koneksi residual pada Darknet-53.
- FPN — prediksi multi-skala top-down.
- YOLOv2 — anchor dan direct location prediction.
- Logistic classifiers — klasifikasi multi-label.

## Metodologi & Arsitektur
Darknet-53 (53 lapis, blok residual) mengekstrak fitur; prediksi dilakukan pada tiga skala dengan anchor berbeda per skala (total 9 anchor). Setiap prediksi mencakup objectness (logistic), offset box, dan skor kelas independen. Upsampling + konkatenasi menyatukan fitur antar-skala.

Komponen / langkah metodologis utama:

- Backbone Darknet-53 dengan blok residual.
- Prediksi pada 3 skala (mirip FPN) dengan 3 anchor per skala.
- Objectness score via logistic regression.
- Klasifikasi independen per-kelas (multi-label, tanpa softmax).
- Upsample + concat untuk menyatukan fitur multi-skala.
- NMS akhir per kelas.

## Kontribusi Utama
1. Darknet-53 residual yang dalam namun efisien.
2. Prediksi tiga-skala meningkatkan deteksi objek kecil.
3. Klasifikasi multi-label yang lebih fleksibel.
4. Baseline stabil yang sangat banyak diadopsi & dimodifikasi.

## Rincian Eksperimen
Dievaluasi pada COCO dengan penekanan pada trade-off kecepatan-akurasi dan performa lintas ukuran objek (AP-small/medium/large), dibandingkan RetinaNet dan SSD.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP / AP50 | kuat pada AP50, cepat; AP ketat lebih rendah dari RetinaNet |
| COCO (objek kecil) | AP-S | membaik dibanding YOLOv2 |
| Kecepatan | FPS | jauh lebih cepat dari RetinaNet pada akurasi setara |

## Temuan Kunci
- Prediksi multi-skala krusial untuk objek kecil.
- Backbone residual meningkatkan kualitas fitur signifikan.
- Unggul pada IoU longgar, sedikit tertinggal pada IoU ketat.
- Sangat praktis: cepat, stabil, mudah dimodifikasi.

## Keunggulan
- Keseimbangan kecepatan-akurasi yang matang.
- Deteksi multi-skala efektif.
- Menjadi fondasi rekayasa banyak turunan.

## Keterbatasan
- AP pada IoU ketat kalah dari detektor fokus-akurasi.
- Masih memakai anchor (butuh penyetelan).
- Objek sangat kecil/berhimpitan tetap menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv3 adalah baseline yang paling sering dipakai/dimodifikasi dalam aplikasi RGB-D dan pertanian pada tinjauan ini (mis. deteksi apel), sehingga memahaminya penting untuk menilai turunan-turunannya.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
- [007 - 2023 - YOLOv7 - Fondasi RGB](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)
- [008 - 2024 - YOLOv9 - Fondasi RGB](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md)
- [009 - 2024 - YOLOv10 - Fondasi RGB](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md)

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
YOLOv3 memantapkan desain backbone residual + prediksi multi-skala pada YOLO, memberi keseimbangan kecepatan-akurasi yang menjadikannya baseline de-facto bagi banyak sistem deteksi termasuk integrasi RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `redmon2018yolov3` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 003/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
