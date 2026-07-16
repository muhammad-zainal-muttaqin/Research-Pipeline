# 170 - MobileSal: Extremely Efficient RGB-D Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 170 dari 191 |
| Kunci BibTeX | `wu2022mobilesal` |
| Judul | MobileSal: Extremely Efficient RGB-D Salient Object Detection |
| Penulis | Wu, Yu-Huan; Liu, Yun; Xu, Jun; Bian, Jia-Wang; Gu, Yu-Chao; Cheng, Ming-Ming |
| Tahun | 2022 |
| Venue / Jurnal | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| Tema klaster | RGB-D SOD |
| Kata kunci | efficient RGB-D SOD, mobile, implicit depth, real-time |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-sod)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2012.13095
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=MobileSal%3A%20Extremely%20Efficient%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=MobileSal%3A%20Extremely%20Efficient%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 44 |
| Nomor | 12 |
| Halaman | 10261--10269 |
| arXiv | 2012.13095 |

## Ringkasan Eksekutif
MobileSal adalah jaringan RGB-D SOD yang sangat efisien untuk perangkat mobile, memakai implicit depth restoration dan backbone ringan sehingga mencapai kecepatan tinggi dengan akurasi kompetitif.

## Abstrak (Parafrase)
Penulis merancang model RGB-D SOD hemat komputasi berbasis backbone MobileNet. Ide kunci Implicit Depth Restoration (IDR) memanfaatkan depth hanya saat pelatihan untuk memperkuat fitur, sehingga saat inferensi depth tak wajib diproses berat. Dengan compact pyramid refinement, MobileSal berjalan sangat cepat pada parameter kecil sambil menjaga akurasi mendekati model berat.

## Latar Belakang & Konteks
Model RGB-D SOD umumnya berat; penerapan pada perangkat mobile menuntut efisiensi ekstrem tanpa kehilangan akurasi berarti.

## Permasalahan yang Diangkat
- Model RGB-D SOD terlalu berat untuk mobile.
- Pemrosesan depth menambah biaya.
- Menjaga akurasi pada model kecil sulit.

## Tujuan & Pertanyaan Penelitian
- Membuat RGB-D SOD real-time di mobile.
- Mengurangi biaya pemrosesan depth.
- Menjaga akurasi kompetitif.

## Tinjauan Terdahulu / Posisi Literatur
Kontras dengan model berat (BBS-Net, JL-DCF); menekankan efisiensi ala MobileNet dan pemanfaatan depth implisit.

Karya/konsep pembanding yang relevan:

- MobileNet - backbone ringan.
- BBS-Net/JL-DCF - model berat pembanding.
- D3Net - kualitas depth.
- Model efisien SOD lain.

## Metodologi & Arsitektur
Backbone MobileNet untuk RGB; Implicit Depth Restoration menambahkan cabang depth ringan hanya saat latih untuk memandu fitur; compact pyramid refinement menyempurnakan peta saliency dengan biaya rendah.

Komponen / langkah metodologis utama:

- Backbone MobileNet ringan.
- Implicit Depth Restoration (depth saat latih).
- Compact pyramid refinement.
- Optimasi untuk latensi mobile.

## Kontribusi Utama
1. RGB-D SOD ultra-efisien.
2. Pemanfaatan depth implisit.
3. Kecepatan tinggi pada parameter kecil.
4. Akurasi kompetitif.

## Rincian Eksperimen
Benchmark RGB-D SOD standar dengan S/F/E-measure/MAE plus pengukuran FPS/params dan uji kecepatan di perangkat.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Benchmark RGB-D SOD | S/E-measure | mendekati model berat |
| Kecepatan | FPS/params | jauh lebih cepat/ringan |
| Ablation IDR | metrik | IDR menaikkan akurasi tanpa biaya inferensi |

## Temuan Kunci
- Depth implisit memberi manfaat tanpa biaya inferensi.
- Model kecil bisa mendekati akurasi model berat.
- Refinement ringkas efektif.

## Keunggulan
- Sangat cepat/ringan.
- Cocok untuk mobile/edge.
- Akurasi kompetitif.

## Keterbatasan
- Akurasi sedikit di bawah model berat.
- Bergantung depth saat latih.
- Kasus sulit tetap menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Model efisien penting untuk penerapan RGB-D real-time pada robot/edge dengan sumber daya terbatas.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [166 - 2020 - CoNet - RGB-D SOD](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md)
- [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md)
- [168 - 2021 - SPNet - RGB-D SOD](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md)
- [169 - 2023 - CAVER - RGB-D SOD](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SOD)
Istilah penting untuk memahami makalah ini:

- **SOD** — Salient Object Detection; menyorot objek paling menonjol.
- **Peta kedalaman** — Citra yang tiap pikselnya menyatakan jarak ke kamera.
- **Fusi lintas-modal** — Penggabungan fitur RGB dan depth.
- **Early/middle/late fusion** — Fusi di input, fitur tengah, atau keputusan akhir.
- **Attention lintas-modal** — Membobot kontribusi RGB vs depth secara adaptif.
- **S-measure** — Structure-measure; kemiripan struktur peta saliency.
- **E-measure** — Enhanced-alignment measure; kesejajaran piksel-global.
- **F-measure** — Harmonik precision-recall pada peta saliency.
- **MAE** — Mean Absolute Error peta saliency vs ground truth.
- **Depth berkualitas rendah** — Depth berderau yang dapat merusak fusi.
- **Backbone Transformer** — Encoder attention (mis. Swin) untuk konteks global.

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
MobileSal menunjukkan RGB-D SOD dapat dijalankan real-time di perangkat terbatas berkat pemanfaatan depth implisit dan desain ringan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wu2022mobilesal` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 170/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
