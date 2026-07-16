# 112 - Expandable YOLO: 3D Object Detection from RGB-D Images

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 112 dari 154 |
| Kunci BibTeX | `takahashi2020expandableyolo` |
| Judul | Expandable YOLO: 3D Object Detection from RGB-D Images |
| Penulis | Takahashi, Masahiro; Moro, Alessandro; Ji, Yonghoon; Umeda, Kazunori |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the 21st International Conference on Research and Education in Mechatronics (REM) |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, deteksi 3D, input depth, box 3D, indoor |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-yolo-plus-rgb-d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Expandable%20YOLO%3A%203D%20Object%20Detection%20from%20RGB-D%20Images
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Expandable%20YOLO%3A%203D%20Object%20Detection%20from%20RGB-D%20Images&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1--5 |

## Ringkasan Eksekutif
Perluasan YOLO agar menerima input RGB-D dan mengeluarkan kotak 3D, memperluas dimensi prediksi untuk deteksi objek 3D dari citra RGB-D.

## Abstrak (Parafrase)
Expandable YOLO memodifikasi arsitektur YOLO untuk menerima kanal kedalaman sebagai input tambahan dan memperluas head prediksi agar menghasilkan parameter kotak 3D (bukan hanya 2D). Dengan demikian YOLO yang semula detektor 2D dapat melakukan deteksi objek 3D indoor secara real-time dari RGB-D.

## Latar Belakang & Konteks
YOLO standar hanya menghasilkan kotak 2D; deteksi objek 3D indoor dari kamera RGB-D membutuhkan perluasan input (depth) dan output (dimensi 3D).

## Permasalahan yang Diangkat
- YOLO standar hanya menghasilkan kotak 2D.
- Deteksi 3D indoor butuh input kedalaman.
- Head perlu diperluas untuk parameter 3D.
- Real-time diinginkan.
- Geometri kedalaman perlu dimanfaatkan.

## Tujuan & Pertanyaan Penelitian
- Menambahkan kanal kedalaman ke input YOLO.
- Memperluas head untuk parameter box 3D.
- Melakukan deteksi 3D indoor real-time.

## Tinjauan Terdahulu / Posisi Literatur
Expandable YOLO mengembangkan YOLO menjadi detektor 3D RGB-D.

Karya/konsep pembanding yang relevan:

- YOLO — detektor 2D dasar.
- RGB-D input — depth tambahan.
- Deteksi 3D indoor.
- Dataset RGB-D indoor.

## Metodologi & Arsitektur
Input RGB-D (RGB + kedalaman) dimasukkan ke backbone YOLO yang dimodifikasi; head diperluas untuk memprediksi parameter kotak 3D (posisi, dimensi, orientasi) selain kelas; memanfaatkan kedalaman untuk lokalisasi 3D; real-time.

Komponen / langkah metodologis utama:

- Input kanal kedalaman ditambahkan ke YOLO.
- Head diperluas untuk parameter box 3D.
- Prediksi kotak 3D (posisi/dimensi/orientasi).
- Memanfaatkan geometri kedalaman.
- Real-time (basis YOLO).
- Evaluasi dataset RGB-D indoor.

## Kontribusi Utama
1. Perluasan YOLO ke deteksi 3D RGB-D.
2. Input depth + output box 3D.
3. Deteksi 3D indoor real-time.
4. Contoh langsung integrasi depth ke YOLO.

## Rincian Eksperimen
Diuji pada dataset RGB-D indoor dengan metrik deteksi 3D, membandingkan dengan baseline 2D/3D.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Dataset RGB-D indoor | deteksi 3D | box 3D real-time berbasis YOLO |
| Input depth | kontribusi | kedalaman memungkinkan output 3D |
| Kecepatan | real-time | basis YOLO |

## Temuan Kunci
- YOLO dapat diperluas ke output 3D.
- Kanal kedalaman memungkinkan lokalisasi 3D.
- Real-time terjaga.
- Integrasi depth langsung ke YOLO layak.

## Keunggulan
- Integrasi depth langsung.
- Output 3D.
- Real-time.

## Keterbatasan
- Akurasi 3D terbatas dibanding metode 3D khusus.
- Bergantung kualitas kedalaman.
- Fokus domain indoor.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Expandable YOLO adalah entri inti klaster YOLO+RGB-D dalam tinjauan: contoh eksplisit menyuntikkan kedalaman ke pipeline YOLO untuk output 3D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
- [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [117 - 2024 - Onboard Dynamic-Object Detection (Xu dkk.) - YOLO plus RGB-D](./117%20-%202024%20-%20Onboard%20Dynamic-Object%20Detection%20%28Xu%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [119 - 2023 - Distance Measurement via YOLO + Depth (Chen dkk.) - YOLO plus RGB-D](./119%20-%202023%20-%20Distance%20Measurement%20via%20YOLO%20+%20Depth%20%28Chen%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **YOLO plus RGB-D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema YOLO plus RGB-D)
Istilah penting untuk memahami makalah ini:

- **YOLO** — Detektor satu-tahap real-time regresi tunggal.
- **Kanal depth** — Peta kedalaman sebagai masukan tambahan.
- **Fusi RGB-D** — Penggabungan warna dan kedalaman pada deteksi.
- **Lokalisasi 3D** — Posisi objek dalam koordinat 3D via depth.
- **Point cloud** — Titik 3D dari depth untuk grasp/rekonstruksi.
- **Pick-and-place** — Tugas robot mengambil dan menempatkan objek.
- **RealSense/Kinect** — Kamera RGB-D konsumen umum.
- **Early/mid/late fusion** — Titik penggabungan depth pada arsitektur.
- **Segment Anything (SAM)** — Model segmentasi umum; FastSAM=versi cepat.
- **Real-time deployment** — Penerapan dengan kendala latensi.

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
Expandable YOLO memperluas YOLO untuk menerima input RGB-D dan mengeluarkan kotak 3D, memungkinkan deteksi objek 3D indoor real-time sebagai integrasi langsung kedalaman ke pipeline YOLO.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `takahashi2020expandableyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 112/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
