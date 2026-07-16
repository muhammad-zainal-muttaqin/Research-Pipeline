# 037 - Rethinking RGB-D Salient Object Detection: Models, Data Sets, and Large-Scale Benchmarks

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 037 dari 154 |
| Kunci BibTeX | `fan2020d3net` |
| Judul | Rethinking RGB-D Salient Object Detection: Models, Data Sets, and Large-Scale Benchmarks |
| Penulis | Fan, Deng-Ping; Lin, Zheng; Zhang, Zhao; Zhu, Menglong; Cheng, Ming-Ming |
| Tahun | 2021 |
| Venue / Jurnal | IEEE Transactions on Neural Networks and Learning Systems |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, depth depurator, tiga-aliran, benchmark, dataset SIP |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Rethinking%20RGB-D%20Salient%20Object%20Detection%3A%20Models%2C%20Data%20Sets%2C%20and%20Large-Scale%20Benchmarks
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Rethinking%20RGB-D%20Salient%20Object%20Detection%3A%20Models%2C%20Data%20Sets%2C%20and%20Large-Scale%20Benchmarks&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 32 |
| Nomor | 5 |
| Halaman | 2075--2089 |

## Ringkasan Eksekutif
Studi 'rethinking' RGB-D SOD yang memperkenalkan gerbang penyaring kedalaman (depth depurator), model tiga-aliran, serta benchmark skala besar dan dataset SIP, menekankan pentingnya kualitas kedalaman.

## Abstrak (Parafrase)
D3Net menyoroti bahwa peta kedalaman berkualitas rendah dapat merusak fusi. Solusinya adalah Depth Depurator Unit (DDU) yang menyaring peta kedalaman buruk sebelum digunakan, dipadukan model tiga-aliran (RGB, depth, dan aliran fusi). Makalah juga menyediakan benchmark skala besar dan dataset SIP (person-oriented), menstandarkan evaluasi RGB-D SOD.

## Latar Belakang & Konteks
Banyak metode RGB-D SOD mengasumsikan kedalaman selalu bermanfaat, padahal sensor menghasilkan depth berderau/tidak akurat yang justru menurunkan kinerja fusi; selain itu evaluasi RGB-D SOD belum terstandar.

## Permasalahan yang Diangkat
- Peta kedalaman berkualitas buruk merusak fusi.
- Metode mengasumsikan kedalaman selalu bermanfaat.
- Benchmark RGB-D SOD belum terstandar.
- Dataset person-oriented masih kurang.
- Perbandingan antar-metode tak setara.

## Tujuan & Pertanyaan Penelitian
- Menyaring kedalaman buruk sebelum fusi (DDU).
- Menstandarkan evaluasi RGB-D SOD.
- Menyediakan dataset SIP baru.

## Tinjauan Terdahulu / Posisi Literatur
D3Net meninjau ulang model, dataset, dan protokol evaluasi RGB-D SOD secara menyeluruh.

Karya/konsep pembanding yang relevan:

- RGB-D SOD berbasis fusi — dasar.
- Depth quality gating — gagasan penyaringan.
- Benchmark SOD sebelumnya.
- Dataset RGB-D (NJU2K, NLPR).

## Metodologi & Arsitektur
Depth Depurator Unit menilai kualitas peta kedalaman dan menyaringnya (gating) agar hanya kedalaman andal masuk fusi; jaringan tiga aliran memproses RGB, depth, dan fusi; evaluasi dilakukan pada benchmark besar termasuk dataset SIP.

Komponen / langkah metodologis utama:

- Depth Depurator Unit (DDU) penyaring kualitas depth.
- Jaringan tiga aliran (RGB, depth, fusi).
- Gating kedalaman sebelum fusi.
- Benchmark skala besar terstandar.
- Dataset SIP (person-oriented).
- Protokol evaluasi seragam.

## Kontribusi Utama
1. DDU menyaring kedalaman buruk agar fusi robust.
2. Model tiga-aliran yang efektif.
3. Benchmark besar & dataset SIP menstandarkan bidang.
4. Menekankan peran kualitas kedalaman.

## Rincian Eksperimen
Diuji ekstensif lintas dataset RGB-D SOD (NJU2K, NLPR, STERE, SIP, dll.) dengan metrik S/F/E-measure dan MAE, plus analisis ketahanan terhadap depth buruk.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Benchmark besar | S/F/E, MAE | kokoh terhadap depth berkualitas rendah |
| SIP (baru) | S/F/E, MAE | dataset person-oriented |
| Ablation | DDU | gating meningkatkan ketahanan |

## Temuan Kunci
- Kualitas kedalaman krusial untuk fusi RGB-D.
- Gating depth meningkatkan ketahanan.
- Standarisasi evaluasi penting bagi bidang.
- Dataset SIP memperkaya benchmark.

## Keunggulan
- Menekankan & menangani kualitas kedalaman.
- Menstandarkan evaluasi RGB-D SOD.
- Menyediakan dataset baru.

## Keterbatasan
- Gating menambah komponen/heuristik.
- Bergantung metrik kualitas depth.
- Backbone CNN (konteks global terbatas).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
D3Net menegaskan prinsip penting bagi seluruh tinjauan RGB+Depth: kedalaman tidak selalu bermanfaat dan perlu disaring — pelajaran yang relevan bagi semua fusi RGB-D termasuk YOLO+RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [040 - 2020 - HDFNet - RGB-D SOD](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)
- [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)
- [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)
- [043 - 2022 - SwinNet - RGB-D SOD](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 154 entri total).
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
D3Net memikirkan ulang RGB-D SOD dengan menyaring kedalaman buruk (DDU), model tiga-aliran, dan benchmark/dataset SIP, menegaskan bahwa kualitas kedalaman adalah faktor kunci fusi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `fan2020d3net` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 037/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
