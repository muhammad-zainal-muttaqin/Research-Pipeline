# 015 - SSD: Single Shot MultiBox Detector

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 015 dari 154 |
| Kunci BibTeX | `liu2016ssd` |
| Judul | SSD: Single Shot MultiBox Detector |
| Penulis | Liu, Wei; Anguelov, Dragomir; Erhan, Dumitru; Szegedy, Christian; Reed, Scott; Fu, Cheng-Yang; Berg, Alexander C. |
| Tahun | 2016 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | SSD, single-shot, default box, multi-skala, satu-tahap |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=SSD%3A%20Single%20Shot%20MultiBox%20Detector
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=SSD%3A%20Single%20Shot%20MultiBox%20Detector&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 21--37 |

## Ringkasan Eksekutif
Detektor satu-tahap yang memprediksi box dari feature map multi-skala memakai default box beragam rasio, menyeimbangkan kecepatan dan akurasi sebagai pembanding langsung YOLO.

## Abstrak (Parafrase)
SSD (Single Shot MultiBox Detector) melakukan deteksi dalam satu lintasan jaringan dengan memprediksi kelas dan offset box dari beberapa feature map pada resolusi berbeda. Setiap lokasi memiliki default box dengan beragam skala dan rasio aspek, memungkinkan penanganan objek multi-skala tanpa tahap proposal. Hard negative mining dan augmentasi menstabilkan pelatihan.

## Latar Belakang & Konteks
Detektor dua-tahap akurat tetapi lambat, sementara deteksi satu-tahap perlu mekanisme untuk menangani objek multi-skala secara efektif dalam satu lintasan.

## Permasalahan yang Diangkat
- Detektor dua-tahap lambat untuk aplikasi real-time.
- Deteksi satu-tahap sulit menangani objek multi-skala.
- Ketidakseimbangan foreground-background besar.
- Objek kecil sulit pada feature map dalam beresolusi rendah.
- Perlu default box yang mencakup beragam bentuk.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi dalam satu lintasan tanpa proposal.
- Menangani objek multi-skala via feature map berjenjang.
- Menyeimbangkan kecepatan dan akurasi.

## Tinjauan Terdahulu / Posisi Literatur
SSD menggabungkan ide anchor (Faster R-CNN) dengan prediksi dari beberapa feature map dalam satu jaringan (VGG backbone).

Karya/konsep pembanding yang relevan:

- Faster R-CNN — konsep anchor/default box.
- YOLO — deteksi satu-tahap.
- VGG16 — backbone dasar.
- Hard negative mining — penyeimbang kelas.

## Metodologi & Arsitektur
Backbone VGG16 ditambah lapisan konvolusi ekstra beresolusi menurun; prediksi kelas+offset dilakukan pada beberapa feature map (skala berbeda); default box multi rasio di tiap lokasi; hard negative mining menjaga rasio positif:negatif; NMS akhir.

Komponen / langkah metodologis utama:

- Prediksi dari beberapa feature map (multi-skala).
- Default box beragam skala & rasio aspek.
- Konvolusi ekstra beresolusi menurun.
- Hard negative mining (rasio ~3:1).
- Augmentasi data ekstensif.
- NMS pada keluaran akhir.

## Kontribusi Utama
1. Deteksi satu-tahap multi-skala tanpa proposal.
2. Trade-off kecepatan-akurasi kuat saat rilis.
3. Default box multi-rasio efektif menangani bentuk.
4. Menjadi pembanding langsung YOLO.

## Rincian Eksperimen
Diuji pada PASCAL VOC dan COCO dengan dua resolusi (SSD300, SSD512), dibandingkan YOLO dan Faster R-CNN pada akurasi dan kecepatan.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| PASCAL VOC 2007 | mAP | SSD512 ~76.8%, SSD300 ~74.3% |
| COCO | mAP | kompetitif; objek kecil lebih lemah |
| Kecepatan | FPS | real-time (SSD300 ~59 FPS) |

## Temuan Kunci
- Prediksi multi-feature-map efektif untuk multi-skala.
- Objek kecil tetap menantang (feature dangkal minim semantik).
- Hard negative mining penting untuk stabilitas.
- Trade-off kecepatan-akurasi menarik untuk real-time.

## Keunggulan
- Cepat dan akurat (satu-tahap).
- Menangani multi-skala secara elegan.
- Sederhana tanpa proposal.

## Keterbatasan
- Objek kecil relatif lemah.
- Banyak default box perlu penyetelan.
- Feature dangkal kurang semantik.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
SSD adalah pelopor detektor satu-tahap multi-skala dan pembanding klasik YOLO; konsep prediksi multi-skala relevan untuk memahami neck pada YOLO+RGB-D.

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
SSD menetapkan deteksi satu-tahap multi-skala dengan default box, menjadi salah satu pembanding utama YOLO dalam kurva kecepatan-akurasi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `liu2016ssd` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 015/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
