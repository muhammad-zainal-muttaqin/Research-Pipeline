# 193 - RF-DETR: Neural Architecture Search for Real-Time Detection Transformers

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 193 dari 202 |
| Kunci BibTeX | `robinson2025rfdetr` |
| Judul | RF-DETR: Neural Architecture Search for Real-Time Detection Transformers |
| Penulis | Robinson, Isaac; Robicheaux, Peter; Popov, Matvei; Ramanan, Deva; Peri, Neehar |
| Tahun | 2025 |
| Venue / Jurnal | International Conference on Learning Representations (ICLR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | RF-DETR, NAS, DETR, real-time, COCO 60 AP |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2511.09554
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RF-DETR%3A%20Neural%20Architecture%20Search%20for%20Real-Time%20Detection%20Transformers
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RF-DETR%3A%20Neural%20Architecture%20Search%20for%20Real-Time%20Detection%20Transformers&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2511.09554 |

## Ringkasan Eksekutif
RF-DETR (Roboflow, arXiv Nov 2025; diterima ICLR 2026) adalah detektor transformer ringan yang memakai pra-pelatihan skala-internet dan Neural Architecture Search (NAS) berbagi-bobot untuk mengoptimalkan trade-off akurasi-latensi, dan menjadi detektor real-time pertama yang melewati 60 AP di COCO.

## Abstrak (Parafrase)
RF-DETR memperkenalkan keluarga model deteksi dan segmentasi berbasis DETR yang bebas-scheduler dan berbasis NAS berbagi-bobot, mengungguli metode real-time SOTA sebelumnya (latensi <= 40 ms) pada COCO dan benchmark Roboflow100-VL. Varian nano mencapai 48.0 AP di COCO, melampaui D-FINE (nano) sebesar 5.3 AP pada latensi setara; varian 2x-large mengungguli GroundingDINO (tiny) sebesar 1.2 AP di Roboflow100-VL sambil berjalan ~20x lebih cepat, dan menjadi detektor real-time pertama yang melampaui 60 AP di COCO. NAS berbagi-bobot memungkinkan pencarian arsitektur yang menyeimbangkan akurasi dan latensi untuk dataset target.

## Latar Belakang & Konteks
DETR real-time (RT-DETR, D-FINE, DEIM) telah mempersempit jurang terhadap YOLO, namun penyetelan arsitektur untuk domain/latensi tertentu masih mahal. RF-DETR memanfaatkan pra-pelatihan besar dan NAS untuk menghasilkan keluarga model yang mudah difinetune.

## Permasalahan yang Diangkat
- Menyeimbangkan akurasi dan latensi lintas domain memerlukan pencarian arsitektur mahal.
- Detektor real-time sebelumnya belum menembus 60 AP di COCO.
- Transfer ke dataset khusus (fine-tuning) sering menuntut re-desain manual.
- Perbandingan adil lintas latensi sulit tanpa keluarga model terukur.

## Tujuan & Pertanyaan Penelitian
- Merancang keluarga DETR real-time via NAS berbagi-bobot.
- Memanfaatkan pra-pelatihan skala-internet untuk generalisasi.
- Menembus 60 AP di COCO pada rezim real-time.
- Unggul pada benchmark multi-domain Roboflow100-VL.

## Tinjauan Terdahulu / Posisi Literatur
RF-DETR berdiri di atas RT-DETR/LW-DETR dan pesaing D-FINE/DEIM, tetapi menambah dimensi NAS berbagi-bobot dan pra-pelatihan besar untuk transfer yang efisien.

Karya/konsep pembanding yang relevan:

- RT-DETR - DETR real-time pelopor yang mengalahkan YOLO.
- D-FINE - regresi distribusi halus untuk DETR.
- DEIM - pencocokan diperbaiki untuk konvergensi cepat.
- GroundingDINO - detektor open-vocabulary sebagai pembanding transfer.

## Metodologi & Arsitektur
Backbone ringan (mis. DINOv2-pretrained) dipadukan dengan pencarian arsitektur berbagi-bobot yang mengevaluasi banyak konfigurasi tanpa melatih ulang dari nol, menghasilkan titik-titik Pareto akurasi-latensi; model bersifat scheduler-free.

Komponen / langkah metodologis utama:

- NAS berbagi-bobot (weight-sharing) untuk eksplorasi arsitektur.
- Pra-pelatihan skala-internet pada backbone.
- Keluarga model nano-2x-large pada satu ruang pencarian.
- Pelatihan bebas-scheduler (scheduler-free).
- Evaluasi pada COCO dan Roboflow100-VL multi-domain.

## Kontribusi Utama
1. Keluarga DETR real-time berbasis NAS berbagi-bobot.
2. Detektor real-time pertama >60 AP di COCO.
3. Peningkatan besar atas D-FINE/GroundingDINO pada latensi setara.
4. Kemudahan fine-tuning lintas domain (Roboflow100-VL).

## Rincian Eksperimen
Diuji pada COCO (akurasi/latensi) dan Roboflow100-VL (transfer multi-domain), dibandingkan dengan D-FINE, DEIM, dan GroundingDINO pada berbagai anggaran latensi (<= 40 ms).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP (nano) | 48.0 AP; +5.3 AP atas D-FINE nano pada latensi setara |
| COCO | AP (2x-large) | Detektor real-time pertama > 60 AP |
| Roboflow100-VL | AP | +1.2 AP atas GroundingDINO tiny, ~20x lebih cepat |

## Temuan Kunci
- NAS berbagi-bobot menghasilkan Pareto akurasi-latensi lebih baik.
- Pra-pelatihan besar memperkuat transfer ke domain khusus.
- Real-time dapat menembus 60 AP di COCO.
- Keluarga model memudahkan pemilihan sesuai anggaran latensi.

## Keunggulan
- SOTA real-time COCO (>60 AP).
- Transfer domain kuat dan cepat difinetune.
- Keluarga skala fleksibel dari NAS.

## Keterbatasan
- Biaya pra-pelatihan/NAS besar di sisi pengembang.
- Angka bergantung pada protokol; verifikasi lewat naskah ICLR.
- Segmentasi dan deployment edge perlu evaluasi lanjutan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Rujukan mutakhir untuk bab DETR real-time (2025/2026); pelengkap RT-DETR (entri 155) dan pembanding langsung D-FINE/DEIM dalam diskusi akurasi-latensi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [192 - 2025 - YOLO26 Detektor Real-Time End-to-End - Fondasi RGB](./192%20-%202025%20-%20YOLO26%20Detektor%20Real-Time%20End-to-End%20-%20Fondasi%20RGB.md)
- [194 - 2026 - Le-DETR Encoder Efisien untuk DETR Real-Time - Fondasi RGB](./194%20-%202026%20-%20Le-DETR%20Encoder%20Efisien%20untuk%20DETR%20Real-Time%20-%20Fondasi%20RGB.md)

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
RF-DETR menunjukkan NAS berbagi-bobot + pra-pelatihan besar mendorong DETR real-time ke >60 AP COCO dengan transfer domain unggul. Ia menjadi tonggak 2025/2026 pada klaster detektor; verifikasi angka via naskah ICLR 2026 sebelum sitasi formal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `robinson2025rfdetr` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 193/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
