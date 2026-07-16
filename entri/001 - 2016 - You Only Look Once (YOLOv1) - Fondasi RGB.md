# 001 - You Only Look Once: Unified, Real-Time Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 001 dari 154 |
| Kunci BibTeX | `redmon2016yolo` |
| Judul | You Only Look Once: Unified, Real-Time Object Detection |
| Penulis | Redmon, Joseph; Divvala, Santosh; Girshick, Ross; Farhadi, Ali |
| Tahun | 2016 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | deteksi objek, real-time, one-stage, regresi tunggal, PASCAL VOC |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=You%20Only%20Look%20Once%3A%20Unified%2C%20Real-Time%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=You%20Only%20Look%20Once%3A%20Unified%2C%20Real-Time%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 779--788 |

## Ringkasan Eksekutif
Makalah pelopor yang mendefinisikan ulang deteksi objek sebagai satu masalah regresi tunggal, menghasilkan detektor real-time pertama yang benar-benar terpadu dan menjadi cikal bakal seluruh keluarga YOLO.

## Abstrak (Parafrase)
YOLO (You Only Look Once) memandang deteksi objek sebagai regresi langsung dari piksel citra ke koordinat bounding box dan probabilitas kelas. Sebuah jaringan saraf konvolusi tunggal membagi citra menjadi grid S x S; setiap sel bertanggung jawab memprediksi sejumlah bounding box beserta skor confidence dan distribusi kelas. Karena seluruh pipeline adalah satu jaringan yang dievaluasi sekali, YOLO dapat dilatih end-to-end dan dioptimalkan langsung terhadap kinerja deteksi. Sistem berjalan sangat cepat (45 FPS untuk model penuh, 155 FPS untuk Fast YOLO) sambil mempertahankan akurasi yang kompetitif, serta bernalar secara global sehingga membuat lebih sedikit kesalahan latar dibanding metode berbasis region.

## Latar Belakang & Konteks
Sebelum YOLO, detektor terbaik (keluarga R-CNN) memakai pipeline kompleks: menghasilkan ribuan region proposal, mengklasifikasikan tiap region, lalu pasca-pemrosesan. Pipeline itu lambat dan sulit dioptimalkan karena komponennya dilatih terpisah. Kebutuhan aplikasi real-time (robotika, kendaraan otonom) menuntut pendekatan yang jauh lebih sederhana dan cepat.

## Permasalahan yang Diangkat
- Pipeline deteksi dua-tahap sangat lambat sehingga tak layak real-time.
- Komponen yang dilatih terpisah sulit dioptimalkan secara menyeluruh.
- Metode berbasis sliding-window/region banyak menghasilkan false positive latar.
- Kompleksitas sistem menyulitkan penerapan dan pemeliharaan.
- Belum ada kerangka deteksi tunggal yang benar-benar end-to-end dan cepat.

## Tujuan & Pertanyaan Penelitian
- Merumuskan deteksi sebagai regresi tunggal end-to-end.
- Mencapai kecepatan real-time tanpa mengorbankan akurasi secara berlebihan.
- Menyederhanakan arsitektur deteksi menjadi satu jaringan.

## Tinjauan Terdahulu / Posisi Literatur
YOLO diposisikan sebagai antitesis pipeline dua-tahap R-CNN/Fast R-CNN. Ia mewarisi ide CNN untuk fitur namun membuang tahap proposal, dan dibandingkan dengan DPM berbasis sliding window.

Karya/konsep pembanding yang relevan:

- DPM (Deformable Parts Model) — pendekatan sliding-window klasik.
- R-CNN / Fast R-CNN — dua-tahap berbasis region proposal.
- OverFeat — deteksi berbasis konvolusi multi-skala.
- Deep MultiBox — pelopor prediksi box berbasis jaringan.

## Metodologi & Arsitektur
Arsitektur GoogLeNet-termodifikasi (24 lapis konvolusi + 2 fully-connected) memproses citra 448x448 dan mengeluarkan tensor S x S x (B*5 + C). Setiap sel memprediksi B kotak (x,y,w,h,confidence) dan C probabilitas kelas bersyarat. Loss adalah jumlah kuadrat terboboti yang menyeimbangkan lokalisasi, confidence, dan klasifikasi.

Komponen / langkah metodologis utama:

- Grid S x S (7x7) membagi citra; tiap sel memprediksi B=2 kotak.
- Confidence = P(objek) x IoU prediksi-ground truth.
- Prediksi kelas bersyarat per sel, digabung dengan confidence saat inferensi.
- Loss sum-squared dengan bobot lambda_coord dan lambda_noobj.
- Akar kuadrat pada w,h untuk menyeimbangkan objek besar-kecil.
- NMS pada keluaran akhir untuk membuang duplikasi.

## Kontribusi Utama
1. Merumuskan deteksi sebagai regresi tunggal grid — paradigma baru.
2. Detektor real-time terpadu pertama (45-155 FPS).
3. Penalaran global menurunkan kesalahan latar dibanding R-CNN.
4. Generalisasi kuat ke domain di luar foto natural (mis. lukisan).

## Rincian Eksperimen
Dievaluasi pada PASCAL VOC 2007 dan 2012, dibandingkan dengan DPM, R-CNN, dan Fast R-CNN, baik pada akurasi (mAP) maupun kecepatan (FPS), disertai analisis galat lokalisasi vs latar.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| PASCAL VOC 2007 | mAP / FPS | 63.4% mAP @45 FPS; Fast YOLO 52.7% @155 FPS |
| PASCAL VOC 2012 | mAP | kompetitif terhadap detektor sezaman |
| Analisis galat | tipe error | galat lokalisasi tinggi, galat latar rendah |

## Temuan Kunci
- Regresi tunggal grid memungkinkan deteksi real-time terpadu.
- Trade-off: lokalisasi kurang presisi terutama objek kecil berkelompok.
- Penalaran global mengurangi false positive latar.
- Kombinasi YOLO+Fast R-CNN meningkatkan mAP (saling melengkapi).

## Keunggulan
- Sangat cepat dan sederhana (satu jaringan).
- Generalisasi domain yang baik.
- Sedikit kesalahan latar.

## Keterbatasan
- Lokalisasi kurang presisi; lemah pada objek kecil yang berkelompok.
- Batasan jumlah objek per sel grid.
- Recall lebih rendah dari metode dua-tahap.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sebagai akar silsilah YOLO, entri ini adalah fondasi paling penting bagi seluruh tinjauan: setiap varian YOLO+RGB-D yang dibahas mewarisi formulasi regresi-grid dan filosofi real-time dari makalah ini.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
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
YOLOv1 membuktikan deteksi objek dapat dirumuskan sebagai regresi tunggal yang cepat dan end-to-end, membuka era detektor satu-tahap dan menjadi titik awal semua varian YOLO berikutnya yang menjadi tulang punggung pipeline RGB-D modern.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `redmon2016yolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 001/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
