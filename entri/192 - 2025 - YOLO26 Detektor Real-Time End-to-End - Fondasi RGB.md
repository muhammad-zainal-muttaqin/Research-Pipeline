# 192 - YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 192 dari 202 |
| Kunci BibTeX | `sapkota2025yolo26` |
| Judul | YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection |
| Penulis | Sapkota, Ranjan; Cheppally, Rahul Harsha; Sharda, Ajay; Karkee, Manoj |
| Tahun | 2025 |
| Venue / Jurnal | arXiv preprint arXiv:2509.25164 |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLO26, NMS-free, edge, real-time, DFL-free |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2509.25164
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLO26%3A%20Key%20Architectural%20Enhancements%20and%20Performance%20Benchmarking%20for%20Real-Time%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLO26%3A%20Key%20Architectural%20Enhancements%20and%20Performance%20Benchmarking%20for%20Real-Time%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2509.25164 |

## Ringkasan Eksekutif
YOLO26 (dirilis Ultralytics, September 2025) adalah anggota terbaru keluarga YOLO yang dirancang end-to-end dan hemat untuk perangkat edge/berdaya rendah. Makalah ini menelaah inovasi arsitekturnya dan membandingkannya lintas versi YOLO serta detektor berbasis transformer.

## Abstrak (Parafrase)
Makalah mengevaluasi YOLO26, detektor objek real-time yang menghapus Distribution Focal Loss (DFL) dan mengadopsi inferensi tanpa NMS (NMS-free) sehingga menghasilkan prediksi deterministik tanpa pasca-proses. Diperkenalkan pula ProgLoss, skema Small-Target-Aware Label Assignment (STAL) untuk objek kecil, serta optimizer MuSGD untuk konvergensi stabil. YOLO26 mendukung lima tugas (deteksi, segmentasi instans, estimasi pose, deteksi berorientasi/OBB, klasifikasi) dan menyasar penempatan pada perangkat seperti NVIDIA Jetson. Dilaporkan capaian sekitar 40.9-57.5 mAP pada COCO dengan latensi 1.7-11.8 ms pada GPU T4, mendorong batas Pareto akurasi-latensi melampaui YOLO real-time sebelumnya.

## Latar Belakang & Konteks
Detektor YOLO umumnya bergantung pada NMS untuk membuang deteksi tumpang tindih, menambah latensi dan menyulitkan penerapan end-to-end. DFL juga menambah kompleksitas kepala regresi. YOLO26 berupaya menyederhanakan pipeline sambil menjaga akurasi objek kecil dan efisiensi pada perangkat tepi.

## Permasalahan yang Diangkat
- Ketergantungan pada NMS menghambat inferensi end-to-end dan menambah latensi variabel.
- Akurasi objek kecil sering turun pada detektor ringan untuk edge.
- Kompleksitas DFL pada kepala regresi menambah beban komputasi.
- Kebutuhan model tunggal untuk banyak tugas visi pada perangkat berdaya rendah.

## Tujuan & Pertanyaan Penelitian
- Menghapus NMS dan DFL tanpa menurunkan akurasi.
- Meningkatkan deteksi objek kecil via STAL dan ProgLoss.
- Menstabilkan pelatihan dengan optimizer MuSGD.
- Menyediakan satu model multi-tugas siap-edge.

## Tinjauan Terdahulu / Posisi Literatur
YOLO26 melanjutkan garis keturunan YOLOv8-v13 dan detektor NMS-free bergaya DETR/YOLOv10, memadukan efisiensi CNN dengan penugasan label satu-ke-satu untuk menghapus pasca-proses.

Karya/konsep pembanding yang relevan:

- YOLOv10 - deteksi NMS-free via penugasan konsisten ganda.
- RT-DETR - detektor transformer real-time end-to-end.
- YOLOv8/v11 - basis keluarga Ultralytics multi-tugas.
- Distribution Focal Loss (GFL) - representasi regresi yang dihapus di sini.

## Metodologi & Arsitektur
Kepala deteksi dirancang ulang untuk menegakkan penugasan label satu-ke-satu saat pelatihan, menghasilkan prediksi non-redundan tanpa NMS. DFL dihilangkan; ProgLoss dan STAL meningkatkan pembelajaran objek kecil; optimizer MuSGD (hibrida bergaya Muon+SGD) menjaga konvergensi.

Komponen / langkah metodologis utama:

- Arsitektur end-to-end NMS-free (penugasan satu-ke-satu).
- Penghapusan Distribution Focal Loss (DFL) pada kepala regresi.
- ProgLoss untuk penyeimbangan pelatihan progresif.
- STAL: penugasan label sadar objek kecil.
- Optimizer MuSGD untuk stabilitas konvergensi.
- Dukungan multi-tugas: deteksi, segmentasi, pose, OBB, klasifikasi.

## Kontribusi Utama
1. Detektor YOLO end-to-end tanpa NMS dan tanpa DFL.
2. Mekanisme STAL+ProgLoss untuk akurasi objek kecil.
3. Optimizer MuSGD baru untuk pelatihan stabil.
4. Benchmark lintas versi YOLO dan perangkat edge (Jetson).

## Rincian Eksperimen
Evaluasi pada COCO untuk akurasi/latensi dan benchmarking pada perangkat edge NVIDIA Jetson, dibandingkan dengan YOLOv8 hingga YOLOv13 serta detektor transformer.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | mAP | ~40.9-57.5 lintas skala model (konfirmasi ke naskah) |
| GPU T4 | Latensi | ~1.7-11.8 ms per citra |
| Jetson (edge) | FPS/latensi | Dioptimalkan untuk CPU/edge; angka pasti lihat naskah |

## Temuan Kunci
- Menghapus NMS memungkinkan inferensi deterministik end-to-end.
- STAL+ProgLoss menaikkan akurasi objek kecil pada model ringan.
- MuSGD memberi konvergensi lebih stabil dibanding baseline.
- Satu model melayani lima tugas visi sekaligus.

## Keunggulan
- Inferensi tanpa NMS: latensi lebih ringkas dan deterministik.
- Fokus objek kecil dan efisiensi edge.
- Multi-tugas dalam satu arsitektur.

## Keterbatasan
- Sebagai rilis 2025, benchmark independen masih terbatas (verifikasi angka).
- Sebagian klaim berasal dari pihak pengembang; perlu reproduksi.
- Detail MuSGD/ProgLoss perlu dibaca dari naskah untuk implementasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sangat relevan sebagai state-of-the-art YOLO terbaru (2025) untuk fokus tinjauan YOLO real-time; menjadi rujukan mutakhir dibanding YOLOv8/RT-DETR pada bab detektor.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [193 - 2025 - RF-DETR NAS untuk Detektor Transformer Real-Time - Fondasi RGB](./193%20-%202025%20-%20RF-DETR%20NAS%20untuk%20Detektor%20Transformer%20Real-Time%20-%20Fondasi%20RGB.md)
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
YOLO26 memindahkan keluarga YOLO ke paradigma end-to-end NMS-free dengan penekanan objek kecil dan efisiensi edge. Sebagai karya 2025 paling mutakhir di klaster ini, ia layak menjadi tolok ukur; angka kinerja spesifik sebaiknya diverifikasi lewat naskah/arXiv sebelum dikutip.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `sapkota2025yolo26` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 192/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
