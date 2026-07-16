# 158 - DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 158 dari 191 |
| Kunci BibTeX | `zhang2023dino` |
| Judul | DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection |
| Penulis | Zhang, Hao; Li, Feng; Liu, Shilong; Zhang, Lei; Su, Hang; Zhu, Jun; Ni, Lionel M.; Shum, Heung-Yeung |
| Tahun | 2023 |
| Venue / Jurnal | International Conference on Learning Representations (ICLR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | DETR, denoising, contrastive queries, end-to-end detection |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2203.03605
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DINO%3A%20DETR%20with%20Improved%20DeNoising%20Anchor%20Boxes%20for%20End-to-End%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DINO%3A%20DETR%20with%20Improved%20DeNoising%20Anchor%20Boxes%20for%20End-to-End%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2203.03605 |

## Ringkasan Eksekutif
DINO (DETR with Improved deNoising anchOr boxes) mempercepat konvergensi dan menaikkan akurasi DETR lewat contrastive denoising training, mixed query selection, dan skema look-forward-twice, menjadi salah satu detektor SOTA pada COCO.

## Abstrak (Parafrase)
Penulis memperbaiki tiga aspek DETR: (1) contrastive denoising untuk memisahkan kueri positif/negatif dekat ground truth agar mengurangi duplikat; (2) mixed query selection yang menginisialisasi posisi kueri dari fitur encoder; (3) look-forward-twice yang memperbaiki estimasi box antar-layer decoder. Hasilnya konvergensi jauh lebih cepat dan akurasi tinggi, termasuk saat diskalakan ke backbone besar.

## Latar Belakang & Konteks
DETR menghapus komponen buatan-tangan tetapi lambat konvergen dan kalah akurat dari detektor klasik pada awalnya. Rangkaian perbaikan (DN-DETR, DAB-DETR) mengarah ke DINO.

## Permasalahan yang Diangkat
- Konvergensi DETR lambat (ratusan epoch).
- Kueri duplikat menurunkan presisi.
- Inisialisasi kueri dan refinement box belum optimal.

## Tujuan & Pertanyaan Penelitian
- Mempercepat pelatihan DETR.
- Meningkatkan akurasi deteksi end-to-end.
- Menyediakan denoising kontrastif yang stabil.

## Tinjauan Terdahulu / Posisi Literatur
Melanjutkan DAB-DETR (anchor box sebagai kueri) dan DN-DETR (query denoising); DINO menambah versi kontrastif dan seleksi kueri campuran.

Karya/konsep pembanding yang relevan:

- DAB-DETR - kueri sebagai kotak anchor dinamis.
- DN-DETR - denoising kueri untuk stabilisasi.
- Deformable DETR - attention terdeformasi.
- DETR - dasar deteksi berbasis kueri.

## Metodologi & Arsitektur
Menambahkan kueri denoising positif dan negatif (kontrastif) selama pelatihan; memilih kueri posisi dari fitur encoder (mixed selection) sambil menjaga konten kueri dapat dilatih; memperbaiki box dua kali antar-layer (look-forward-twice).

Komponen / langkah metodologis utama:

- Contrastive denoising (pasangan positif-negatif).
- Mixed query selection dari encoder.
- Look-forward-twice untuk refinement box.
- Kompatibel dengan backbone besar (Swin-L).

## Kontribusi Utama
1. Denoising kontrastif untuk mengurangi duplikat.
2. Konvergensi jauh lebih cepat.
3. SOTA COCO dengan backbone besar.
4. Dasar bagi banyak detektor DETR berikutnya.

## Rincian Eksperimen
COCO dengan ResNet-50 (epoch sedikit) dan Swin-L (skala besar), melaporkan AP dan kurva konvergensi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO (R50, 12/24 ep) | AP | akurasi tinggi dengan epoch sedikit |
| COCO (Swin-L) | AP | SOTA saat rilis (>63 AP) |
| Ablation | AP | tiap komponen menyumbang kenaikan |

## Temuan Kunci
- Denoising kontrastif menstabilkan pencocokan kueri.
- Inisialisasi kueri dari encoder mempercepat konvergensi.
- DETR dapat memimpin benchmark deteksi.

## Keunggulan
- Akurasi puncak.
- Konvergensi cepat.
- Skalabel ke model besar.

## Keterbatasan
- Komputasi besar pada backbone besar.
- Kompleksitas pelatihan bertambah.
- Kurang cocok untuk perangkat edge langsung.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sebagai tonggak DETR modern, penting untuk memahami arah deteksi end-to-end yang dapat menggantikan pipeline berbasis anchor pada persepsi RGB/RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [155 - 2024 - RT-DETR - Fondasi RGB](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)
- [156 - 2024 - YOLO-World - Fondasi RGB](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)
- [157 - 2023 - Gold-YOLO - Fondasi RGB](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md)
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
DINO menjadikan DETR akurat sekaligus cepat-berlatih, referensi kunci untuk deteksi end-to-end mutakhir.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2023dino` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 158/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
