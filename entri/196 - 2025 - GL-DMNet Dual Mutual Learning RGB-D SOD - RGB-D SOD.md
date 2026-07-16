# 196 - Dual Mutual Learning Network with Global-local Awareness for RGB-D Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 196 dari 202 |
| Kunci BibTeX | `yi2025gldmnet` |
| Judul | Dual Mutual Learning Network with Global-local Awareness for RGB-D Salient Object Detection |
| Penulis | Yi, Kang; Tang, Haoran; Li, Yumeng; Xu, Jing; Zhang, Jun |
| Tahun | 2025 |
| Venue / Jurnal | arXiv preprint arXiv:2501.01648 |
| Tema klaster | RGB-D SOD |
| Kata kunci | GL-DMNet, RGB-D SOD, mutual learning, global-local, fusion |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2501.01648
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Dual%20Mutual%20Learning%20Network%20with%20Global-local%20Awareness%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Dual%20Mutual%20Learning%20Network%20with%20Global-local%20Awareness%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2501.01648 |

## Ringkasan Eksekutif
GL-DMNet (Yi dkk., arXiv Januari 2025) adalah jaringan RGB-D salient object detection dengan kesadaran global-lokal dan pembelajaran mutual ganda, dilaporkan mengungguli 24 metode pembanding dengan rata-rata perbaikan ~3% lintas metrik.

## Abstrak (Parafrase)
GL-DMNet mengidentifikasi wilayah menonjol dengan memproses citra warna dan kedalaman melalui modul position mutual fusion dan channel mutual fusion, menjembatani informasi global dan lokal antar-modalitas. Alih-alih fusi satu arah, kedua modalitas saling belajar (dual mutual learning) sehingga saling menguatkan. Dilaporkan mengungguli ~24 metode terkini dengan perbaikan rata-rata sekitar 3% pada beberapa metrik saliency standar.

## Latar Belakang & Konteks
RGB-D SOD memanfaatkan geometri kedalaman untuk menyorot objek menonjol, tetapi depth berkualitas rendah dan fusi lintas-modal yang naif dapat merusak hasil. Kesadaran global-lokal dan saling-belajar antar-modal berpotensi memperbaiki keselarasan fitur.

## Permasalahan yang Diangkat
- Fusi RGB-D satu arah kurang memanfaatkan komplementaritas modalitas.
- Depth berderau dapat menyesatkan prediksi saliency.
- Keseimbangan konteks global dan detail lokal sulit dijaga.
- Interaksi posisi dan kanal antar-modal belum optimal.

## Tujuan & Pertanyaan Penelitian
- Merancang fusi mutual posisi dan kanal antar-modal.
- Menyatukan kesadaran global dan lokal.
- Menaikkan akurasi saliency lintas dataset RGB-D.
- Menahan pengaruh depth berkualitas rendah.

## Tinjauan Terdahulu / Posisi Literatur
GL-DMNet berdiri di atas tren transformer RGB-D SOD (SwinNet, CAVER, TriTransNet) dengan penekanan pada pembelajaran mutual dua-arah alih-alih fusi searah.

Karya/konsep pembanding yang relevan:

- CAVER - transformer view-mixed lintas-modal (entri 169).
- SwinNet - Swin transformer sadar-tepi RGB-D/RGB-T.
- SPNet - saliency yang mempertahankan spesifisitas (entri 168).
- TriTransNet - triplet transformer embedding.

## Metodologi & Arsitektur
Dua cabang (RGB dan depth) berinteraksi via position mutual fusion (menyelaraskan konteks spasial) dan channel mutual fusion (menimbang kanal antar-modal), lalu decoder menyatukan isyarat global-lokal untuk peta saliency.

Komponen / langkah metodologis utama:

- Position Mutual Fusion (PMF) untuk keselarasan spasial.
- Channel Mutual Fusion (CMF) untuk penimbangan kanal.
- Kesadaran global-lokal (global-local awareness).
- Dekoder saliency yang menyatukan fitur mutual.

## Kontribusi Utama
1. Kerangka dual mutual learning untuk RGB-D SOD.
2. Modul PMF dan CMF antar-modal.
3. Perbaikan ~3% lintas 24 metode pembanding.
4. Ketahanan lebih baik terhadap depth berkualitas rendah.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar (mis. NJU2K, NLPR, SIP, STERE, DES) menggunakan metrik S-measure, E-measure, F-measure, dan MAE, dibanding ~24 metode SOTA.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Benchmark RGB-D SOD | S/E/F-measure, MAE | Unggul; rata-rata ~+3% vs 24 metode (lihat naskah) |
| Ablation | PMF/CMF | Kedua modul berkontribusi (konfirmasi naskah) |
| Robustness | Depth rendah | Lebih tahan derau depth |

## Temuan Kunci
- Pembelajaran mutual dua-arah mengalahkan fusi searah.
- Fusi posisi+kanal saling melengkapi.
- Kesadaran global-lokal menstabilkan saliency.

## Keunggulan
- Akurasi SOTA pada banyak benchmark RGB-D SOD.
- Modul fusi mutual yang eksplisit.
- Lebih tahan depth berkualitas rendah.

## Keterbatasan
- Biaya komputasi fusi ganda perlu ditelaah.
- Angka bergantung protokol; verifikasi via naskah.
- Generalisasi ke video/real-time belum dibahas.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Rujukan RGB-D SOD terbaru (2025) untuk melengkapi klaster SOD (entri 35-50, 166-170); relevan bagi fusi RGB-D di tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- (tidak ada entri lain pada tema ini)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 202 entri total).
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
GL-DMNet memperlihatkan pembelajaran mutual global-lokal meningkatkan RGB-D SOD melampaui fusi searah. Sebagai karya 2025, angka dan ablation sebaiknya dikonfirmasi via arXiv sebelum sitasi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yi2025gldmnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 196/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
