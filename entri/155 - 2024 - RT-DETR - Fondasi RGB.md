# 155 - DETRs Beat YOLOs on Real-Time Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 155 dari 191 |
| Kunci BibTeX | `zhao2024rtdetr` |
| Judul | DETRs Beat YOLOs on Real-Time Object Detection |
| Penulis | Zhao, Yian; Lv, Wenyu; Xu, Shangliang; Wei, Jinman; Wang, Guanzhong; Dang, Qingqing; Liu, Yi; Chen, Jie |
| Tahun | 2024 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | DETR real-time, hybrid encoder, object detection, end-to-end |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2304.08069
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DETRs%20Beat%20YOLOs%20on%20Real-Time%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DETRs%20Beat%20YOLOs%20on%20Real-Time%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2304.08069 |

## Ringkasan Eksekutif
RT-DETR adalah detektor berbasis Transformer (DETR) pertama yang benar-benar real-time dan, pada anggaran latensi setara, mengungguli seri YOLO tanpa memerlukan Non-Maximum Suppression (NMS). Kuncinya adalah efficient hybrid encoder dan seleksi kueri berbasis ketidakpastian minimum.

## Abstrak (Parafrase)
Makalah ini berargumen bahwa detektor end-to-end berbasis DETR sebenarnya dapat bersaing dengan YOLO dalam kecepatan bila hambatan komputasinya diatasi. Penulis merancang hybrid encoder yang memisahkan interaksi intra-skala dan fusi lintas-skala sehingga biaya attention pada peta fitur beresolusi tinggi ditekan. Ditambah pemilihan kueri objek berbasis skor ketidakpastian (uncertainty-minimal query selection), RT-DETR mencapai akurasi tinggi pada COCO sambil menghapus NMS yang menjadi sumber latensi variabel pada detektor konvensional.

## Latar Belakang & Konteks
Seri YOLO mendominasi deteksi real-time namun bergantung pada NMS yang menambah latensi tak stabil dan hyperparameter tambahan. DETR menghapus NMS tetapi lambat konvergen dan berat komputasinya, sehingga jarang dipakai untuk aplikasi real-time hingga munculnya varian efisien seperti RT-DETR.

## Permasalahan yang Diangkat
- NMS pada YOLO menambah latensi yang bergantung jumlah deteksi dan sulit dioptimasi seragam.
- Encoder Transformer DETR mahal pada fitur multiskala beresolusi tinggi.
- Inisialisasi kueri objek yang buruk memperlambat konvergensi dan menurunkan akurasi.

## Tujuan & Pertanyaan Penelitian
- Membangun detektor end-to-end tanpa NMS yang real-time.
- Menekan biaya encoder Transformer pada fitur multiskala.
- Menyediakan skema penskalaan kecepatan-akurasi yang fleksibel.

## Tinjauan Terdahulu / Posisi Literatur
Menempatkan diri sebagai penerus DETR (Carion 2020) dan Deformable DETR yang mempercepat konvergensi, sekaligus pembanding langsung terhadap YOLOv5/YOLOv8. Berbeda dari keduanya, RT-DETR menggabungkan efisiensi CNN backbone dengan decoder Transformer bebas-NMS.

Karya/konsep pembanding yang relevan:

- DETR - fondasi deteksi berbasis kueri Transformer.
- Deformable DETR - attention terdeformasi untuk konvergensi lebih cepat.
- YOLOv5/YOLOv8 - baseline real-time berbasis anchor/anchor-free.

## Metodologi & Arsitektur
Backbone CNN mengekstrak fitur multiskala; hybrid encoder melakukan Attention-based Intra-scale Feature Interaction (AIFI) hanya pada level tertinggi lalu CNN-based Cross-scale Feature Fusion (CCFF) untuk menggabungkan skala. Decoder DETR memakai kueri terpilih dan menghasilkan prediksi langsung tanpa NMS.

Komponen / langkah metodologis utama:

- Hybrid encoder (AIFI + CCFF) memangkas biaya attention resolusi tinggi.
- Uncertainty-minimal query selection memilih kueri awal berkualitas.
- Decoder bebas-NMS dengan jumlah query tetap.
- Penskalaan model (R18/R34/R50/R101) untuk trade-off kecepatan-akurasi.

## Kontribusi Utama
1. Detektor DETR real-time pertama yang mengalahkan YOLO pada latensi setara.
2. Hybrid encoder efisien untuk fitur multiskala.
3. Skema seleksi kueri berbasis ketidakpastian.
4. Bebas-NMS sehingga latensi lebih stabil.

## Rincian Eksperimen
Dievaluasi pada MS COCO dengan pengukuran mAP dan latensi/FPS pada GPU T4/TensorRT, dibandingkan langsung dengan seri YOLO pada anggaran kecepatan setara.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| MS COCO val | AP | RT-DETR-R50 ~53 AP, mengungguli YOLO sebanding pada FPS setara |
| Latensi (T4/TensorRT) | ms/FPS | real-time tanpa NMS, latensi lebih stabil |
| Ablation encoder | AP/latensi | hybrid encoder menaikkan efisiensi vs encoder DETR penuh |

## Temuan Kunci
- DETR dapat real-time bila encoder multiskala dirancang efisien.
- Menghapus NMS menstabilkan latensi inferensi.
- Seleksi kueri berkualitas mempercepat konvergensi.

## Keunggulan
- Bebas-NMS, end-to-end.
- Akurasi/kecepatan kompetitif terhadap YOLO.
- Mudah diskalakan lewat backbone berbeda.

## Keterbatasan
- Memori pelatihan lebih besar dari YOLO ringan.
- Manfaat penuh perlu optimasi TensorRT.
- Tetap butuh backbone CNN besar untuk akurasi puncak.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sebagai pembanding modern terhadap YOLO, entri ini penting untuk memposisikan pilihan detektor real-time pada pipeline RGB/RGB-D dan mempertimbangkan alternatif bebas-NMS.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [156 - 2024 - YOLO-World - Fondasi RGB](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)
- [157 - 2023 - Gold-YOLO - Fondasi RGB](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md)
- [158 - 2023 - DINO detector - Fondasi RGB](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)
- [159 - 2022 - DN-DETR - Fondasi RGB](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md)
- [160 - 2021 - Conditional DETR - Fondasi RGB](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md)
- [161 - 2021 - Sparse R-CNN - Fondasi RGB](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md)
- [162 - 2022 - ConvNeXt - Fondasi RGB](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)
- [163 - 2022 - Swin Transformer V2 - Fondasi RGB](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fondasi RGB** dalam peta tinjauan (17 klaster, 191 entri total).
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
RT-DETR menunjukkan detektor Transformer bisa real-time dan mengungguli YOLO tanpa NMS, menjadikannya rujukan penting untuk keputusan arsitektur deteksi mutakhir.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhao2024rtdetr` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 155/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
