# 195 - RiO-DETR: DETR for Real-time Oriented Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 195 dari 202 |
| Kunci BibTeX | `hu2026riodetr` |
| Judul | RiO-DETR: DETR for Real-time Oriented Object Detection |
| Penulis | Hu, Zhangchi; others |
| Tahun | 2026 |
| Venue / Jurnal | arXiv preprint arXiv:2603.09411 |
| Tema klaster | Remote Sensing |
| Kata kunci | RiO-DETR, oriented detection, real-time, OBB, remote sensing |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-remote-sensing)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2603.09411
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RiO-DETR%3A%20DETR%20for%20Real-time%20Oriented%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RiO-DETR%3A%20DETR%20for%20Real-time%20Oriented%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2603.09411 |

## Ringkasan Eksekutif
RiO-DETR (arXiv, Maret 2026) mengklaim sebagai transformer deteksi berorientasi real-time pertama, membawa paradigma DETR end-to-end ke tugas oriented bounding box yang lazim pada citra udara/penginderaan jauh.

## Abstrak (Parafrase)
RiO-DETR memperluas kerangka DETR untuk deteksi objek berorientasi (oriented bounding box) secara real-time, tugas penting pada penginderaan jauh dan citra udara di mana objek muncul dalam sudut arbitrer. Sebagai detektor berorientasi real-time end-to-end pertama berbasis transformer, ia menghapus komponen bergantung-anchor dan pasca-proses rumit, menghadirkan prediksi kotak berorientasi langsung dengan latensi rendah.

## Latar Belakang & Konteks
Deteksi berorientasi (OBB) krusial untuk objek berputar pada citra udara. Metode arus utama masih bergantung pada anchor berorientasi dan pasca-proses; belum ada DETR berorientasi yang benar-benar real-time.

## Permasalahan yang Diangkat
- Objek pada citra udara muncul dalam orientasi arbitrer sehingga box aksis-sejajar tidak memadai.
- Metode OBB berbasis anchor rumit dan lambat.
- Belum ada DETR berorientasi end-to-end real-time.
- Representasi sudut rentan diskontinuitas.

## Tujuan & Pertanyaan Penelitian
- Menghadirkan DETR berorientasi real-time pertama.
- Menghapus anchor dan pasca-proses untuk OBB.
- Menangani diskontinuitas sudut secara stabil.
- Menjaga latensi rendah pada citra udara.

## Tinjauan Terdahulu / Posisi Literatur
RiO-DETR memadukan garis DETR (end-to-end, query) dengan literatur oriented detection (mis. keluarga di DOTA), menargetkan real-time yang belum tersentuh metode OBB sebelumnya.

Karya/konsep pembanding yang relevan:

- Oriented R-CNN / S2A-Net - OBB berbasis anchor.
- RT-DETR - DETR real-time (basis kecepatan).
- DINO/DN-DETR - denoising query untuk konvergensi.
- DOTA - benchmark deteksi udara berorientasi.

## Metodologi & Arsitektur
Kerangka DETR diperluas dengan representasi dan kepala prediksi kotak berorientasi, penugasan set-based end-to-end, tanpa anchor berorientasi maupun NMS, dioptimalkan untuk latensi.

Komponen / langkah metodologis utama:

- Kepala prediksi oriented bounding box (sudut + geometri).
- Pencocokan set-based end-to-end (tanpa NMS).
- Penanganan diskontinuitas representasi sudut.
- Desain sadar-latensi untuk real-time.

## Kontribusi Utama
1. Detektor berorientasi real-time end-to-end pertama berbasis DETR.
2. Penghapusan anchor/pasca-proses untuk OBB.
3. Strategi representasi sudut yang stabil.
4. Kinerja real-time pada benchmark citra udara.

## Rincian Eksperimen
Dievaluasi pada benchmark deteksi berorientasi (mis. DOTA dan sejenis) untuk akurasi OBB dan latensi real-time; detail lengkap pada naskah.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| DOTA (dan sejenis) | mAP (OBB) | Kompetitif; lihat naskah untuk angka pasti |
| Latensi | Real-time | Diklaim real-time end-to-end |
| Anchor/NMS | Kebutuhan | Dihilangkan |

## Temuan Kunci
- DETR dapat diperluas ke OBB tanpa mengorbankan real-time.
- Menghapus anchor menyederhanakan pipeline OBB.
- Representasi sudut yang tepat penting untuk stabilitas.

## Keunggulan
- OBB end-to-end tanpa anchor/NMS.
- Real-time pada citra udara.
- Menyederhanakan pipeline deteksi berorientasi.

## Keterbatasan
- Karya 2026 sangat baru; validasi independen minim.
- Angka perlu dikonfirmasi via naskah.
- Kinerja objek sangat kecil/padat perlu diperiksa.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Relevan untuk klaster remote sensing/citra udara dan sebagai perluasan DETR ke OBB; melengkapi bab detektor transformer dengan tugas berorientasi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Remote Sensing** yang baik dibaca berdampingan:

- (tidak ada entri lain pada tema ini)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Remote Sensing** dalam peta tinjauan (17 klaster, 202 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Remote Sensing)
Istilah penting untuk memahami makalah ini:

- **Remote sensing** — Penginderaan jauh satelit/UAV.
- **UAV/drone** — Wahana udara citra resolusi tinggi.
- **Objek kecil** — Objek sangat kecil khas citra udara.
- **Tiling** — Pemecahan citra besar menjadi ubin.
- **Oriented bounding box** — Kotak beorientasi untuk objek berputar.
- **Transformer head** — Kepala prediksi attention untuk objek kecil.
- **VisDrone/DOTA** — Benchmark deteksi udara/remote sensing.
- **mAP** — Metrik deteksi remote sensing.
- **Skala bervariasi** — Rentang ukuran objek sangat lebar.
- **Latar kompleks** — Latar beragam dan padat.

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
RiO-DETR membawa DETR ke ranah deteksi berorientasi real-time, menutup celah OBB end-to-end. Sebagai karya 2026, verifikasi metrik dan protokol via arXiv sebelum dikutip.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `hu2026riodetr` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 195/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
