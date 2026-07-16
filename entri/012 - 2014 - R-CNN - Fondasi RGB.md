# 012 - Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 012 dari 154 |
| Kunci BibTeX | `girshick2014rcnn` |
| Judul | Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation |
| Penulis | Girshick, Ross; Donahue, Jeff; Darrell, Trevor; Malik, Jitendra |
| Tahun | 2014 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | R-CNN, region proposal, selective search, CNN features, deteksi objek |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Rich%20Feature%20Hierarchies%20for%20Accurate%20Object%20Detection%20and%20Semantic%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Rich%20Feature%20Hierarchies%20for%20Accurate%20Object%20Detection%20and%20Semantic%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 580--587 |

## Ringkasan Eksekutif
Makalah pelopor yang membawa fitur CNN ke deteksi objek melalui region proposal, memicu lompatan besar akurasi dan membuka era deteksi berbasis deep learning.

## Abstrak (Parafrase)
R-CNN (Regions with CNN features) menggabungkan region proposal (selective search) dengan fitur CNN yang dipra-latih pada ImageNet lalu di-fine-tune untuk deteksi. Setiap region diproyeksikan ke ukuran tetap, diekstrak fiturnya oleh CNN, lalu diklasifikasikan oleh SVM per kelas dan diperhalus oleh bounding-box regression. Pendekatan ini menaikkan mAP secara dramatis dibanding metode fitur-tangan.

## Latar Belakang & Konteks
Sebelum R-CNN, deteksi bergantung pada fitur buatan tangan (HOG, SIFT) yang telah mencapai plateau. Keberhasilan CNN pada klasifikasi ImageNet menimbulkan pertanyaan apakah fitur CNN dapat mengangkat akurasi deteksi.

## Permasalahan yang Diangkat
- Fitur buatan tangan membatasi akurasi deteksi (plateau).
- Menjalankan CNN pada sliding window sangat mahal.
- Data deteksi berlabel terbatas untuk melatih CNN besar.
- Perlu cara memetakan region ke fitur CNN berukuran tetap.
- Lokalisasi presisi memerlukan penyempurnaan box.

## Tujuan & Pertanyaan Penelitian
- Membuktikan fitur CNN meningkatkan akurasi deteksi drastis.
- Memanfaatkan pra-pelatihan ImageNet untuk data deteksi terbatas.
- Menyediakan pipeline deteksi berbasis proposal yang efektif.

## Tinjauan Terdahulu / Posisi Literatur
R-CNN menggantikan fitur klasik pada pipeline DPM/sliding-window dengan fitur CNN, memakai selective search sebagai penghasil proposal.

Karya/konsep pembanding yang relevan:

- DPM — detektor fitur-tangan sebelumnya.
- Selective search — penghasil region proposal.
- AlexNet — CNN pra-latih ImageNet.
- OverFeat — deteksi berbasis CNN sezaman.

## Metodologi & Arsitektur
Selective search menghasilkan ~2000 region per citra; tiap region diwarp ke 227x227 dan diekstrak fiturnya oleh CNN (AlexNet); fitur diklasifikasikan SVM linear per kelas; bounding-box regression memperhalus lokalisasi. Fine-tuning CNN pada data deteksi meningkatkan akurasi.

Komponen / langkah metodologis utama:

- Region proposal via selective search (~2000/citra).
- Warp region ke ukuran tetap untuk CNN.
- Ekstraksi fitur CNN pra-latih + fine-tune.
- Klasifikasi SVM linear per kelas.
- Bounding-box regression untuk lokalisasi.
- Supervised pre-training + domain-specific fine-tuning.

## Kontribusi Utama
1. Membawa fitur CNN ke deteksi objek pertama kali secara efektif.
2. Menaikkan mAP VOC secara dramatis (~30% relatif).
3. Menetapkan paradigma pra-latih + fine-tune untuk deteksi.
4. Leluhur seluruh keluarga R-CNN.

## Rincian Eksperimen
Diuji pada PASCAL VOC dan ILSVRC2013 detection, dengan analisis kontribusi fine-tuning dan bounding-box regression.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| PASCAL VOC 2012 | mAP | ~53.3% (lompatan besar dari fitur-tangan) |
| ILSVRC2013 det | mAP | kompetitif/unggul saat itu |
| Ablation | fine-tuning | peningkatan besar dari fine-tuning |

## Temuan Kunci
- Fitur CNN jauh mengungguli fitur-tangan untuk deteksi.
- Pra-latih + fine-tune efektif untuk data terbatas.
- Bounding-box regression penting untuk lokalisasi.
- Pipeline lambat (CNN per-region) menjadi motivasi Fast R-CNN.

## Keunggulan
- Lompatan akurasi historis.
- Memanfaatkan transfer learning.
- Membuka era deteksi deep learning.

## Keterbatasan
- Sangat lambat (CNN dijalankan per-region).
- Pelatihan bertingkat yang rumit (CNN, SVM, regressor terpisah).
- Butuh penyimpanan fitur besar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sebagai leluhur detektor dua-tahap, R-CNN adalah pembanding historis penting bagi YOLO dan dasar memahami mengapa detektor satu-tahap real-time dibutuhkan pada aplikasi RGB-D.

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
R-CNN membuktikan fitur CNN mengangkat akurasi deteksi secara dramatis dan menetapkan paradigma pra-latih+fine-tune, membuka era deteksi berbasis deep learning meski dengan biaya komputasi tinggi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `girshick2014rcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 012/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
