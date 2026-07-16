# 005 - YOLOX: Exceeding YOLO Series in 2021

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 005 dari 154 |
| Kunci BibTeX | `ge2021yolox` |
| Judul | YOLOX: Exceeding YOLO Series in 2021 |
| Penulis | Ge, Zheng; Liu, Songtao; Wang, Feng; Li, Zeming; Sun, Jian |
| Tahun | 2021 |
| Venue / Jurnal | arXiv preprint arXiv:2107.08430 |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOX, anchor-free, decoupled head, SimOTA, label assignment |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2107.08430
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOX%3A%20Exceeding%20YOLO%20Series%20in%202021
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOX%3A%20Exceeding%20YOLO%20Series%20in%202021&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2107.08430 |

## Ringkasan Eksekutif
Mengubah YOLO menjadi anchor-free dengan decoupled head dan penetapan label dinamis SimOTA, memberikan lonjakan akurasi konsisten lintas skala model dan memengaruhi desain YOLO generasi berikutnya.

## Abstrak (Parafrase)
YOLOX merombak YOLO klasik menjadi anchor-free, memisahkan cabang klasifikasi dan regresi (decoupled head), serta memakai SimOTA — penyederhanaan OTA (Optimal Transport Assignment) untuk penetapan label positif secara dinamis. Ditambah augmentasi kuat (Mosaic+MixUp) dan strategi end-to-end opsional, YOLOX konsisten mengungguli YOLOv3-v5 pada skala model setara dan memenangi tantangan Streaming Perception (WAD 2021).

## Latar Belakang & Konteks
Desain berbasis anchor menambah hyperparameter (skala, rasio, jumlah) dan menimbulkan bias domain, sementara head yang terkopel (klasifikasi dan regresi berbagi fitur) diketahui membatasi kinerja. Tren anchor-free (FCOS) menunjukkan penyederhanaan bisa meningkatkan akurasi.

## Permasalahan yang Diangkat
- Anchor menambah hyperparameter dan bias domain.
- Head terkopel membatasi kinerja klasifikasi vs regresi.
- Penetapan label statis (IoU) suboptimal.
- Gap akurasi YOLO terhadap detektor akademik terbaru.
- Kebutuhan detektor kuat namun tetap sederhana.

## Tujuan & Pertanyaan Penelitian
- Menghapus anchor untuk menyederhanakan dan menaikkan akurasi.
- Memisahkan head untuk klasifikasi dan regresi.
- Menetapkan label positif secara dinamis dan optimal.

## Tinjauan Terdahulu / Posisi Literatur
YOLOX mengambil ide anchor-free (FCOS), decoupled head, dan penetapan label berbasis optimal transport (OTA), lalu menyederhanakannya menjadi SimOTA agar efisien.

Karya/konsep pembanding yang relevan:

- FCOS — deteksi anchor-free per-lokasi.
- OTA — penetapan label sebagai optimal transport.
- YOLOv3/DarkNet — basis backbone.
- Decoupled head — pemisahan cabang tugas.

## Metodologi & Arsitektur
Backbone Darknet/CSP; head dipisah menjadi cabang klasifikasi, regresi, dan objectness. Titik grid diperlakukan anchor-free; SimOTA memilih sejumlah k prediksi terbaik per objek berdasarkan biaya klasifikasi+lokalisasi dinamis. Augmentasi Mosaic+MixUp dimatikan menjelang akhir pelatihan.

Komponen / langkah metodologis utama:

- Desain anchor-free (satu prediksi per lokasi grid).
- Decoupled head (klasifikasi/regresi/objectness terpisah).
- SimOTA: penetapan label dinamis berbasis biaya.
- Mosaic + MixUp augmentation kuat.
- Opsi end-to-end (tanpa NMS) yang dieksplorasi.
- Skala model dari Nano hingga X.

## Kontribusi Utama
1. Konversi YOLO ke anchor-free yang meningkatkan akurasi.
2. Decoupled head mempercepat konvergensi & menaikkan AP.
3. SimOTA sebagai penetapan label dinamis yang efisien.
4. Kemenangan Streaming Perception Challenge (WAD 2021).

## Rincian Eksperimen
Diuji di COCO lintas skala (Nano-X) dengan ablation atas decoupled head, anchor-free, dan SimOTA, dibandingkan YOLOv3/v4/v5 pada akurasi dan kecepatan.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | YOLOX-L ~50.0% AP; unggul atas YOLOv5-L setara |
| COCO (Nano/Tiny) | AP | lebih tinggi dari pesaing ringan |
| Streaming Perception | juara | WAD 2021 winner |

## Temuan Kunci
- Anchor-free + label dinamis menaikkan akurasi konsisten.
- Decoupled head penting untuk konvergensi & AP.
- SimOTA memberi gain tanpa biaya besar.
- Skalabilitas baik dari perangkat tepi hingga server.

## Keunggulan
- Akurasi tinggi lintas skala model.
- Desain lebih sederhana (tanpa anchor).
- Berpengaruh pada YOLO generasi berikut.

## Keterbatasan
- Kompleksitas SimOTA dibanding penetapan statis.
- Augmentasi kuat menuntut penjadwalan pelatihan cermat.
- Manfaat end-to-end (tanpa NMS) masih terbatas saat itu.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOX menandai peralihan YOLO ke paradigma anchor-free dan label assignment dinamis yang diwarisi banyak detektor RGB modern, relevan untuk memahami arah desain YOLO+RGB-D terbaru.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
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
YOLOX menunjukkan bahwa anchor-free dengan penetapan label dinamis dan head terdekopel meningkatkan YOLO secara nyata, memengaruhi arah desain generasi YOLO selanjutnya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ge2021yolox` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 005/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
