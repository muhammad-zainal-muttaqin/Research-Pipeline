# 011 - PP-YOLO: An Effective and Efficient Implementation of Object Detector

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 011 dari 154 |
| Kunci BibTeX | `long2020ppyolo` |
| Judul | PP-YOLO: An Effective and Efficient Implementation of Object Detector |
| Penulis | Long, Xiang; Deng, Kaipeng; Wang, Guanzhong; Zhang, Yang; Dang, Qingqing; Gao, Yuan; Shen, Hui; Ren, Jianguo; Han, Shumin; Ding, Errui; Wen, Shilei |
| Tahun | 2020 |
| Venue / Jurnal | arXiv preprint arXiv:2007.12099 |
| Tema klaster | Fondasi RGB |
| Kata kunci | PP-YOLO, ResNet50-vd-dcn, Matrix NMS, trik bebas-biaya, PaddlePaddle |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2007.12099
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PP-YOLO%3A%20An%20Effective%20and%20Efficient%20Implementation%20of%20Object%20Detector
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PP-YOLO%3A%20An%20Effective%20and%20Efficient%20Implementation%20of%20Object%20Detector&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2007.12099 |

## Ringkasan Eksekutif
Detektor berbasis YOLOv3 yang menukar backbone dan menyeleksi trik bebas-biaya inferensi untuk menghasilkan keseimbangan efektivitas-efisiensi yang praktis, tanpa arsitektur baru radikal.

## Abstrak (Parafrase)
PP-YOLO menyusun ulang YOLOv3 dengan mengganti backbone Darknet-53 menjadi ResNet50-vd dengan deformable convolution, lalu menambahkan sekumpulan trik yang tidak menambah beban inferensi: DropBlock, EMA, IoU loss, IoU-aware branch, Grid Sensitive, Matrix NMS, CoordConv, dan SPP. Diimplementasikan pada framework PaddlePaddle, PP-YOLO mencapai trade-off kecepatan-akurasi yang unggul dibanding YOLOv4 pada masanya.

## Latar Belakang & Konteks
Alih-alih mengusulkan arsitektur baru, kebutuhan praktis industri adalah detektor yang efektif dan efisien dengan komponen matang dan mudah direproduksi. Banyak trik peningkatan tersedia namun perlu diseleksi agar tidak menambah biaya inferensi.

## Permasalahan yang Diangkat
- Perlu detektor praktis tanpa merombak arsitektur.
- Banyak trik peningkatan menambah biaya inferensi.
- Backbone Darknet-53 bukan satu-satunya pilihan optimal.
- Trade-off kecepatan-akurasi YOLOv3 dapat ditingkatkan.
- Reproduksibilitas dan dukungan framework penting untuk industri.

## Tujuan & Pertanyaan Penelitian
- Meningkatkan YOLOv3 hanya lewat seleksi trik bebas-biaya.
- Mengganti backbone ke ResNet50-vd-dcn.
- Mencapai trade-off kecepatan-akurasi unggul yang reprodusibel.

## Tinjauan Terdahulu / Posisi Literatur
PP-YOLO berbasis YOLOv3 dan mengambil trik dari berbagai karya (DropBlock, Matrix NMS, CoordConv, SPP) tanpa mengubah kerangka deteksi inti.

Karya/konsep pembanding yang relevan:

- YOLOv3 — kerangka dasar.
- ResNet-vd + Deformable Conv — backbone.
- Matrix NMS (SOLOv2) — pasca-proses cepat.
- DropBlock/CoordConv/SPP — trik pendukung.

## Metodologi & Arsitektur
Backbone ResNet50-vd-dcn menggantikan Darknet-53; head YOLOv3 dipertahankan; ditambah IoU-aware branch, Grid Sensitive, SPP, CoordConv, DropBlock, EMA, dan Matrix NMS. Setiap trik divalidasi agar tak menambah latensi inferensi.

Komponen / langkah metodologis utama:

- Backbone ResNet50-vd dengan deformable convolution.
- IoU loss + IoU-aware prediction branch.
- Grid Sensitive untuk lokalisasi tepi sel.
- SPP dan CoordConv untuk konteks/koordinat.
- DropBlock regularization + EMA bobot.
- Matrix NMS untuk pasca-proses cepat.

## Kontribusi Utama
1. Menunjukkan seleksi trik cermat memberi detektor kompetitif.
2. Membuktikan backbone alternatif (ResNet-vd) efektif untuk YOLO.
3. Trade-off kecepatan-akurasi unggul atas YOLOv4 saat rilis.
4. Basis lini PP-YOLO/PP-YOLOE berikutnya.

## Rincian Eksperimen
Diuji di COCO dengan pengukuran kecepatan pada V100 dan ablation tiap trik, dibandingkan YOLOv3, YOLOv4, dan EfficientDet.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP / FPS | ~45.2% AP @~72 FPS (V100) |
| Ablation | tiap trik | kontribusi terkuantifikasi, bebas-biaya inferensi |
| vs YOLOv4 | trade-off | lebih baik pada kecepatan-akurasi saat rilis |

## Temuan Kunci
- Seleksi trik bebas-biaya efektif menaikkan akurasi.
- Backbone ResNet-vd-dcn kompetitif untuk deteksi satu-tahap.
- Matrix NMS mempercepat pasca-proses.
- Reproduksibilitas tinggi di PaddlePaddle.

## Keunggulan
- Praktis dan reprodusibel.
- Trade-off kecepatan-akurasi baik.
- Tanpa arsitektur baru yang rumit.

## Keterbatasan
- Kontribusi bersifat rekayasa/seleksi, bukan paradigma.
- Terikat ekosistem PaddlePaddle pada implementasi asli.
- Masih berbasis anchor.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PP-YOLO menunjukkan fleksibilitas backbone dan trik pada YOLO; relevan sebagai contoh optimasi praktis yang dapat diadaptasi pada pipeline deteksi RGB/RGB-D industri.

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
PP-YOLO membuktikan bahwa seleksi trik bebas-biaya di atas backbone berbeda menghasilkan detektor kompetitif dan praktis, menjadi basis lini PP-YOLO berikutnya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `long2020ppyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 011/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
