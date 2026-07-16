# 149 - CBAM: Convolutional Block Attention Module

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 149 dari 154 |
| Kunci BibTeX | `woo2018cbam` |
| Judul | CBAM: Convolutional Block Attention Module |
| Penulis | Woo, Sanghyun; Park, Jongchan; Lee, Joon-Young; Kweon, In So |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Fusi Multimodal |
| Kata kunci | attention, channel, spatial, plug-and-play, CNN |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-fusi-multimodal)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=CBAM%3A%20Convolutional%20Block%20Attention%20Module
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=CBAM%3A%20Convolutional%20Block%20Attention%20Module&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 3--19 |

## Ringkasan Eksekutif
Modul attention ringan yang menerapkan attention kanal lalu spasial secara berurutan, plug-and-play untuk CNN dan banyak dipakai termasuk pada YOLO/RGB-D.

## Abstrak (Parafrase)
CBAM (Convolutional Block Attention Module) menyempurnakan fitur CNN dengan dua sub-modul berurutan: channel attention (menimbang 'apa' yang penting) dan spatial attention (menimbang 'di mana'). Ringan dan plug-and-play, CBAM memberi peningkatan konsisten lintas backbone dan tugas, banyak diadopsi termasuk pada detektor YOLO dan fusi RGB-D.

## Latar Belakang & Konteks
CNN standar memperlakukan semua kanal dan lokasi secara setara, padahal sebagian fitur/lokasi lebih informatif; diperlukan penekanan adaptif yang efisien.

## Permasalahan yang Diangkat
- CNN memperlakukan semua kanal/lokasi setara.
- Fitur/lokasi informatif perlu ditekankan.
- Attention harus ringan (efisien).
- Perlu solusi plug-and-play.
- Penekanan adaptif meningkatkan representasi.

## Tujuan & Pertanyaan Penelitian
- Menimbang kanal penting (channel attention).
- Menimbang lokasi penting (spatial attention).
- Menyediakan modul attention ringan plug-and-play.

## Tinjauan Terdahulu / Posisi Literatur
CBAM mengembangkan attention (setelah SE-Net) untuk fitur konvolusi.

Karya/konsep pembanding yang relevan:

- SE-Net — channel attention (pendahulu).
- Spatial attention — penekanan lokasi.
- CNN backbone — tempat penyisipan.
- ImageNet/deteksi — evaluasi.

## Metodologi & Arsitektur
Channel attention module mengagregasi fitur (avg+max pooling) untuk menghasilkan bobot kanal; spatial attention module menghasilkan peta bobot spasial dari fitur teragregasi kanal; keduanya diterapkan berurutan untuk merekalibrasi fitur; disisipkan ke blok CNN mana pun.

Komponen / langkah metodologis utama:

- Channel attention (avg+max pooling).
- Spatial attention (peta bobot spasial).
- Penerapan berurutan (kanal lalu spasial).
- Modul ringan.
- Plug-and-play ke blok CNN.
- Rekalibrasi fitur adaptif.

## Kontribusi Utama
1. Attention kanal + spasial berurutan.
2. Ringan dan plug-and-play.
3. Peningkatan konsisten lintas backbone/tugas.
4. Banyak diadopsi (YOLO/RGB-D).

## Rincian Eksperimen
Diuji pada ImageNet (klasifikasi) dan deteksi (mis. MS-COCO/VOC) dengan berbagai backbone, menunjukkan peningkatan konsisten.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ImageNet | top-1 | peningkatan konsisten lintas backbone |
| Deteksi | mAP | peningkatan dengan CBAM |
| Ablation | channel+spatial | keduanya menyumbang gain |

## Temuan Kunci
- Attention kanal + spasial saling melengkapi.
- Plug-and-play memudahkan adopsi.
- Ringan namun berdampak.
- Konsisten lintas tugas/backbone.

## Keunggulan
- Ringan & plug-and-play.
- Peningkatan konsisten.
- Banyak diadopsi.

## Keterbatasan
- Menambah sedikit komputasi.
- Bukan spesifik RGB-D.
- Manfaat bervariasi antar-arsitektur.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
CBAM adalah modul attention fundamental yang dipakai pada banyak varian YOLO (mis. TPH-YOLOv5) dan fusi RGB-D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fusi Multimodal** yang baik dibaca berdampingan:

- [147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)
- [148 - 2017 - PointNet - Fusi Multimodal](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)
- [150 - 2021 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)
- [153 - 2021 - Survei RGB-D SOD (Zhou dkk.) - Fusi Multimodal](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [154 - 2022 - Survei Dataset RGB-D (Lopes dkk.) - Fusi Multimodal](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fusi Multimodal** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Fusi Multimodal)
Istilah penting untuk memahami makalah ini:

- **Multimodal** — Menggabungkan >1 modalitas data.
- **Backbone** — Jaringan ekstraksi fitur fundamental.
- **Residual/skip** — Jalan pintas memudahkan pelatihan jaringan dalam.
- **Attention (CBAM/SE)** — Modul penimbang fitur kanal-spasial.
- **PointNet** — Jaringan pemroses point cloud mentah.
- **Early/late/deep fusion** — Tingkat penggabungan modalitas.
- **Survei** — Sintesis literatur lintas metode.
- **Generalisasi lintas-sensor** — Ketahanan terhadap kombinasi sensor.
- **Kalibrasi/penyelarasan** — Penyelarasan spasial-temporal antar-modal.
- **Representasi bersama** — Ruang fitur gabungan lintas-modal.

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
CBAM menerapkan attention kanal lalu spasial secara berurutan sebagai modul ringan plug-and-play, memberi peningkatan konsisten lintas backbone dan banyak diadopsi termasuk pada YOLO dan fusi RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `woo2018cbam` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 149/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
