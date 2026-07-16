# 194 - Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 194 dari 202 |
| Kunci BibTeX | `huang2026ledetr` |
| Judul | Le-DETR: Revisiting Real-Time Detection Transformer with Efficient Encoder Design |
| Penulis | Huang, Jiannan; Kane, Aditya; Zhou, Fengzhe; Wei, Yunchao; Shi, Humphrey |
| Tahun | 2026 |
| Venue / Jurnal | arXiv preprint arXiv:2602.21010 |
| Tema klaster | Fondasi RGB |
| Kata kunci | Le-DETR, efficient encoder, real-time, COCO, DETR |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2602.21010
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Le-DETR%3A%20Revisiting%20Real-Time%20Detection%20Transformer%20with%20Efficient%20Encoder%20Design
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Le-DETR%3A%20Revisiting%20Real-Time%20Detection%20Transformer%20with%20Efficient%20Encoder%20Design&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2602.21010 |

## Ringkasan Eksekutif
Le-DETR (arXiv, Februari 2026) meninjau ulang detektor transformer real-time dengan desain encoder yang efisien, melaporkan 52.9/54.3/55.1 mAP pada COCO val2017 dengan efisiensi pelatihan yang membaik.

## Abstrak (Parafrase)
Le-DETR mengusulkan desain ulang encoder untuk DETR real-time agar lebih efisien secara komputasi tanpa mengorbankan akurasi. Dengan encoder ringan yang menata ulang agregasi fitur multi-skala, model mencapai 52.9/54.3/55.1 mAP pada COCO Val2017 untuk beberapa skala, sekaligus mempercepat konvergensi pelatihan. Karya ini menempatkan diri dalam tren RT-DETR/D-FINE dengan penekanan pada beban encoder yang selama ini menjadi hambatan latensi.

## Latar Belakang & Konteks
Pada DETR real-time, encoder multi-skala kerap menjadi bagian termahal. Menyederhanakannya dapat memangkas latensi dan mempercepat konvergensi, dua isu klasik keluarga DETR.

## Permasalahan yang Diangkat
- Encoder multi-skala DETR mahal secara komputasi.
- Konvergensi pelatihan DETR lambat.
- Trade-off akurasi-latensi belum optimal pada rezim real-time.
- Perlu desain encoder yang ringan namun tetap akurat.

## Tujuan & Pertanyaan Penelitian
- Merancang encoder efisien untuk DETR real-time.
- Mempercepat konvergensi pelatihan.
- Mempertahankan/menaikkan mAP COCO pada latensi rendah.
- Menyediakan beberapa skala model.

## Tinjauan Terdahulu / Posisi Literatur
Le-DETR melanjutkan RT-DETR dan pesaing D-FINE/DEIM, memfokuskan kontribusi pada bagian encoder alih-alih kepala/pencocokan.

Karya/konsep pembanding yang relevan:

- RT-DETR - encoder hibrida efisien pelopor.
- D-FINE - penyempurnaan regresi.
- DEIM - pencocokan lebih baik untuk konvergensi.
- Deformable DETR - attention multi-skala yang mahal.

## Metodologi & Arsitektur
Encoder dirancang ulang agar hemat (efficient encoder design) dengan agregasi fitur yang lebih ringkas, menekan biaya attention multi-skala dan mempercepat pelatihan.

Komponen / langkah metodologis utama:

- Desain encoder efisien pengganti encoder berat.
- Agregasi fitur multi-skala yang ringkas.
- Skema pelatihan yang mempercepat konvergensi.
- Beberapa varian skala model (mAP 52.9/54.3/55.1).

## Kontribusi Utama
1. Encoder efisien untuk DETR real-time.
2. Peningkatan efisiensi pelatihan (konvergensi lebih cepat).
3. Akurasi COCO kompetitif (52.9-55.1 mAP).
4. Analisis biaya encoder pada detektor transformer.

## Rincian Eksperimen
Dievaluasi pada COCO Val2017 untuk mAP lintas skala model, dengan penekanan pada efisiensi pelatihan dan latensi encoder.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO Val2017 | mAP | 52.9 / 54.3 / 55.1 pada varian berbeda |
| Pelatihan | Konvergensi | Lebih cepat dibanding baseline (lihat naskah) |
| Encoder | Biaya | Ditekan vs encoder DETR standar |

## Temuan Kunci
- Encoder adalah titik hemat utama pada DETR real-time.
- Efisiensi encoder mempercepat konvergensi tanpa menurunkan mAP.
- Trade-off akurasi-latensi membaik pada rezim real-time.

## Keunggulan
- Encoder ringan namun akurat.
- Konvergensi pelatihan lebih cepat.
- Kompetitif di COCO.

## Keterbatasan
- Karya 2026 sangat baru; validasi independen minim.
- Angka perlu dikonfirmasi via naskah arXiv.
- Generalisasi lintas domain belum banyak diuji.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Melengkapi bab DETR real-time dengan sudut efisiensi encoder (2026); dibaca berdampingan RF-DETR (193) dan RT-DETR (155).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [192 - 2025 - YOLO26 Detektor Real-Time End-to-End - Fondasi RGB](./192%20-%202025%20-%20YOLO26%20Detektor%20Real-Time%20End-to-End%20-%20Fondasi%20RGB.md)
- [193 - 2025 - RF-DETR NAS untuk Detektor Transformer Real-Time - Fondasi RGB](./193%20-%202025%20-%20RF-DETR%20NAS%20untuk%20Detektor%20Transformer%20Real-Time%20-%20Fondasi%20RGB.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fondasi RGB** dalam peta tinjauan (17 klaster, 202 entri total).
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
Le-DETR menegaskan bahwa merampingkan encoder adalah jalur efektif menuju DETR real-time yang cepat-berlatih dan akurat. Sebagai karya 2026, angka spesifik perlu diverifikasi melalui arXiv sebelum dikutip formal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `huang2026ledetr` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 194/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
