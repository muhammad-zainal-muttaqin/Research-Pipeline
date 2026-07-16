# 008 - YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 008 dari 154 |
| Kunci BibTeX | `wang2024yolov9` |
| Judul | YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information |
| Penulis | Wang, Chien-Yao; Yeh, I-Hau; Liao, Hong-Yuan Mark |
| Tahun | 2024 |
| Venue / Jurnal | Proceedings of the European Conference on Computer Vision (ECCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv9, PGI, GELAN, information bottleneck, reversible |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv9%3A%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv9%3A%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Menghubungkan teori aliran informasi dengan arsitektur YOLO melalui Programmable Gradient Information (PGI) dan Generalized ELAN (GELAN) untuk mengatasi kehilangan informasi pada jaringan dalam.

## Abstrak (Parafrase)
YOLOv9 menyoroti masalah information bottleneck: informasi input tergerus saat melewati banyak lapisan, sehingga gradien yang dihasilkan menjadi kurang andal. Solusinya adalah PGI (Programmable Gradient Information) yang menyediakan informasi gradien lengkap dan andal melalui cabang reversibel bantu, serta GELAN (Generalized ELAN) yang menggeneralisasi ELAN dan CSPNet untuk efisiensi parameter. Hasilnya, YOLOv9 mengungguli YOLOv7/YOLOv8 pada jumlah parameter setara dengan komputasi lebih rendah.

## Latar Belakang & Konteks
Semakin dalam jaringan, semakin besar risiko kehilangan informasi penting (information bottleneck), yang menyebabkan gradien tak merepresentasikan tujuan dengan baik. Fungsi reversibel dapat mempertahankan informasi, tetapi mahal bila diterapkan naif.

## Permasalahan yang Diangkat
- Information bottleneck menggerus informasi di lapisan dalam.
- Gradien menjadi kurang andal untuk pembelajaran.
- Fungsi reversibel penuh mahal secara komputasi.
- Arsitektur perlu efisien parameter sekaligus akurat.
- Deep supervision klasik dapat menimbulkan bias informasi.

## Tujuan & Pertanyaan Penelitian
- Menyediakan informasi gradien andal tanpa biaya inferensi.
- Menggeneralisasi agregasi fitur (ELAN/CSP) menjadi efisien.
- Meningkatkan akurasi pada anggaran parameter tetap.

## Tinjauan Terdahulu / Posisi Literatur
YOLOv9 bertumpu pada teori information bottleneck dan reversible functions, serta mengembangkan ELAN/CSPNet menjadi GELAN.

Karya/konsep pembanding yang relevan:

- Information bottleneck principle — landasan teori.
- Reversible functions — pelestarian informasi.
- ELAN/CSPNet — dasar GELAN.
- Deep supervision — pembanding PGI.

## Metodologi & Arsitektur
PGI terdiri dari main branch (inferensi), auxiliary reversible branch (menyediakan gradien andal saat pelatihan, dibuang saat inferensi), dan multi-level auxiliary information. GELAN menggabungkan keunggulan ELAN (jalur gradien) dan CSPNet (partisi) untuk blok agregasi ringan.

Komponen / langkah metodologis utama:

- PGI: main + auxiliary reversible branch + multi-level aux info.
- Auxiliary branch hanya aktif saat pelatihan (bebas biaya inferensi).
- GELAN: generalisasi ELAN + CSPNet.
- Efisiensi parameter tinggi.
- Kompatibel dengan head deteksi YOLO modern.
- Skalabilitas model beragam.

## Kontribusi Utama
1. PGI mengatasi information bottleneck secara praktis.
2. GELAN sebagai blok agregasi efisien parameter.
3. Akurasi lebih tinggi pada parameter/komputasi lebih rendah.
4. Menghubungkan teori aliran informasi dengan desain YOLO.

## Rincian Eksperimen
Diuji di COCO dengan perbandingan parameter/FLOPs terhadap YOLOv7, YOLOv8, RT-DETR, dan ablation atas PGI dan GELAN.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP / parameter | unggul atas YOLOv8/v7 pada parameter setara |
| COCO | FLOPs | akurasi lebih tinggi dengan komputasi lebih rendah |
| Ablation | PGI/GELAN | keduanya menyumbang gain terukur |

## Temuan Kunci
- Information bottleneck adalah faktor nyata pada detektor dalam.
- PGI memberi gradien andal tanpa biaya inferensi.
- GELAN efisien parameter dan akurat.
- Teori aliran informasi bermanfaat memandu arsitektur.

## Keunggulan
- Akurasi-efisiensi parameter terbaik pada kelasnya.
- Landasan teori yang kuat.
- Bebas biaya inferensi (aux branch dibuang).

## Keterbatasan
- Konsep PGI relatif kompleks dipahami/diimplementasi.
- Manfaat bergantung kedalaman/skala model.
- Pelatihan dengan aux branch menambah beban memori.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv9 mewakili arah mutakhir desain YOLO yang lebih efisien; relevansinya bagi RGB-D adalah menyediakan backbone deteksi 2D yang lebih akurat-efisien untuk pipeline fusi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
- [007 - 2023 - YOLOv7 - Fondasi RGB](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)
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
YOLOv9 menautkan teori information bottleneck dengan arsitektur nyata via PGI dan GELAN, menghasilkan detektor yang lebih akurat dan efisien pada anggaran parameter tetap.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2024yolov9` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 008/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
