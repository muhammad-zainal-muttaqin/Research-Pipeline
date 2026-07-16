# 022 - End-to-End Object Detection with Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 022 dari 154 |
| Kunci BibTeX | `carion2020detr` |
| Judul | End-to-End Object Detection with Transformers |
| Penulis | Carion, Nicolas; Massa, Francisco; Synnaeve, Gabriel; Usunier, Nicolas; Kirillov, Alexander; Zagoruyko, Sergey |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | DETR, Transformer, set prediction, bipartite matching, end-to-end |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=End-to-End%20Object%20Detection%20with%20Transformers
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=End-to-End%20Object%20Detection%20with%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 213--229 |

## Ringkasan Eksekutif
Merumuskan deteksi sebagai prediksi himpunan langsung memakai Transformer encoder-decoder dan bipartite matching loss, menghapus anchor dan NMS.

## Abstrak (Parafrase)
DETR (DEtection TRansformer) memandang deteksi sebagai prediksi himpunan tetap: sejumlah object query diproses Transformer decoder untuk langsung mengeluarkan himpunan (kelas, box). Pelatihan memakai Hungarian bipartite matching yang memasangkan prediksi dengan ground truth secara unik, sehingga tidak butuh anchor maupun NMS. Self-attention encoder menangkap konteks global antar-fitur.

## Latar Belakang & Konteks
Pipeline deteksi konvensional bergantung pada komponen manual (anchor, NMS, penetapan sampel) yang rumit dan memerlukan tuning. DETR menawarkan formulasi end-to-end yang benar-benar menghapus komponen tersebut.

## Permasalahan yang Diangkat
- Anchor dan NMS adalah komponen manual yang rumit.
- Penetapan sampel heuristik memerlukan tuning.
- Duplikasi prediksi memerlukan pasca-proses.
- Konteks global antar-objek kurang dimanfaatkan.
- Deteksi belum benar-benar end-to-end.

## Tujuan & Pertanyaan Penelitian
- Merumuskan deteksi sebagai prediksi himpunan langsung.
- Menghapus anchor dan NMS.
- Memanfaatkan attention global untuk konteks.

## Tinjauan Terdahulu / Posisi Literatur
DETR membawa Transformer dari NLP ke deteksi sebagai alternatif end-to-end terhadap Faster R-CNN.

Karya/konsep pembanding yang relevan:

- Transformer — arsitektur attention dari NLP.
- Faster R-CNN — pembanding dua-tahap.
- Hungarian algorithm — bipartite matching.
- Set prediction — formulasi tujuan.

## Metodologi & Arsitektur
Backbone CNN mengekstrak fitur; Transformer encoder (self-attention) memperkaya konteks; decoder memproses N object query (paralel) menjadi prediksi (kelas, box); Hungarian matching memasangkan prediksi-GT untuk loss; query belajar menspesialisasi wilayah/ukuran.

Komponen / langkah metodologis utama:

- Backbone CNN + positional encoding.
- Transformer encoder (self-attention global).
- Decoder dengan N object query paralel.
- Prediksi himpunan (kelas + box) langsung.
- Hungarian bipartite matching loss.
- Tanpa anchor & NMS.

## Kontribusi Utama
1. Deteksi end-to-end tanpa anchor/NMS pertama berbasis Transformer.
2. Bipartite matching menghilangkan duplikasi.
3. Attention global menangkap relasi antar-objek.
4. Memicu gelombang detektor berbasis Transformer.

## Rincian Eksperimen
Diuji di COCO dengan perbandingan terhadap Faster R-CNN, analisis konvergensi lambat dan performa per ukuran objek.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | setara Faster R-CNN (baseline kuat) |
| COCO (objek besar) | AP-L | unggul berkat konteks global |
| COCO (objek kecil) | AP-S | lebih lemah; konvergensi lambat |

## Temuan Kunci
- Deteksi dapat dirumuskan sebagai set prediction murni.
- Anchor/NMS tidak wajib.
- Konvergensi lambat & objek kecil jadi kelemahan awal.
- Attention global unggul untuk objek besar.

## Keunggulan
- End-to-end sejati (tanpa anchor/NMS).
- Konsep elegan dan berpengaruh.
- Kuat pada objek besar.

## Keterbatasan
- Konvergensi pelatihan lambat (ratusan epoch).
- Lemah pada objek kecil.
- Butuh komputasi attention besar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DETR membuka paradigma deteksi Transformer end-to-end yang memengaruhi RT-DETR dan YOLOv10 (ide bebas-NMS); relevan untuk memahami arah detektor pada tinjauan ini.

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
DETR merumuskan deteksi sebagai prediksi himpunan berbasis Transformer dengan bipartite matching, menghapus anchor/NMS dan memicu keluarga detektor Transformer end-to-end.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `carion2020detr` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 022/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
