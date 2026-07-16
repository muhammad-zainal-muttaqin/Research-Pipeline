# 189 - Cross-Modality Fusion Transformer for Multispectral Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 189 dari 191 |
| Kunci BibTeX | `fang2022cft` |
| Judul | Cross-Modality Fusion Transformer for Multispectral Object Detection |
| Penulis | Fang, Qingyun; Han, Dapeng; Wang, Zhaokui |
| Tahun | 2022 |
| Venue / Jurnal | arXiv preprint arXiv:2111.00273 |
| Tema klaster | Pedestrian RGB-T |
| Kata kunci | multispectral detection, RGB-thermal, fusion transformer, cross-modality |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pedestrian-rgb-t)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2111.00273
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Cross-Modality%20Fusion%20Transformer%20for%20Multispectral%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Cross-Modality%20Fusion%20Transformer%20for%20Multispectral%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2111.00273 |

## Ringkasan Eksekutif
CFT (Cross-Modality Fusion Transformer) memfusikan fitur RGB dan thermal menggunakan Transformer sehingga interaksi intra- dan inter-modal terjadi bersamaan, meningkatkan deteksi objek multispektral pada kondisi cahaya menantang.

## Abstrak (Parafrase)
Penulis menyisipkan modul Transformer fusi lintas-modal ke backbone deteksi dua-aliran (RGB dan thermal). Dengan self-attention atas token gabungan kedua modalitas, CFT menangkap ketergantungan intra-modal dan inter-modal sekaligus, tanpa desain fusi manual bertahap. Diterapkan pada detektor seperti YOLOv5, CFT meningkatkan akurasi pada FLIR, LLVIP, dan VEDAI.

## Latar Belakang & Konteks
Deteksi multispektral RGB-thermal andal siang-malam, tetapi fusi CNN bertahap sering suboptimal. Transformer menawarkan fusi global sekaligus.

## Permasalahan yang Diangkat
- Fusi CNN bertahap suboptimal.
- Interaksi intra+inter-modal perlu simultan.
- Kondisi cahaya bervariasi menyulitkan.

## Tujuan & Pertanyaan Penelitian
- Fusi RGB-thermal berbasis Transformer.
- Menangkap ketergantungan intra+inter-modal.
- Meningkatkan deteksi multispektral.

## Tinjauan Terdahulu / Posisi Literatur
Berdialog dengan MBNet/GAFF (fusi RGB-T) dan detektor YOLO; kebaruan pada modul fusi Transformer.

Karya/konsep pembanding yang relevan:

- MBNet - modality imbalance.
- GAFF - guided attentive feature fusion.
- YOLOv5 - detektor dasar.
- Halfway fusion - baseline fusi.

## Metodologi & Arsitektur
Dua backbone mengekstrak fitur RGB dan thermal; pada beberapa skala, token kedua modalitas digabung dan diproses self-attention (CFT module) untuk fusi; fitur terfusi diteruskan ke kepala deteksi.

Komponen / langkah metodologis utama:

- Backbone dua-aliran RGB + thermal.
- Modul CFT (self-attention token gabungan).
- Fusi multiskala.
- Integrasi ke detektor YOLO.

## Kontribusi Utama
1. Modul fusi Transformer lintas-modal.
2. Interaksi intra+inter-modal simultan.
3. Peningkatan pada beberapa dataset multispektral.
4. Mudah diintegrasi ke detektor umum.

## Rincian Eksperimen
FLIR, LLVIP, dan VEDAI untuk deteksi (mAP) siang/malam; ablation modul fusi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| FLIR/LLVIP | mAP | peningkatan atas fusi CNN |
| VEDAI | mAP | kuat pada citra udara |
| Ablation CFT | mAP | fusi Transformer menyumbang kenaikan |

## Temuan Kunci
- Transformer menangkap fusi intra+inter-modal sekaligus.
- Fusi global mengungguli fusi bertahap manual.
- Manfaat konsisten lintas dataset.

## Keunggulan
- Fusi lintas-modal kuat.
- Mudah diintegrasi.
- Andal siang-malam.

## Keterbatasan
- Attention menambah biaya.
- Butuh pasangan RGB-thermal terkalibrasi.
- Bergantung kualitas registrasi modal.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Fusi RGB-thermal berbasis Transformer melengkapi fusi RGB-D; keduanya contoh persepsi multimodal untuk kondisi menantang.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pedestrian RGB-T** yang baik dibaca berdampingan:

- (tidak ada entri lain pada tema ini)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pedestrian RGB-T** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pedestrian RGB-T)
Istilah penting untuk memahami makalah ini:

- **Multispektral** — Citra beberapa pita (RGB + thermal).
- **RGB-T** — Pasangan citra warna dan termal.
- **Thermal/LWIR** — Inframerah panjang; andal saat gelap.
- **Illumination-aware** — Bobot modal menyesuaikan kondisi cahaya.
- **Modality imbalance** — Ketimpangan keandalan antar-modal.
- **Miss rate (MR)** — Metrik deteksi pejalan (makin kecil makin baik).
- **KAIST** — Dataset pejalan multispektral standar.
- **CVC-14** — Dataset pejalan siang-malam RGB-thermal.
- **Feature alignment** — Penyelarasan spasial fitur antar-modal.
- **Cross-modal attention** — Attention pemandu fusi RGB-thermal.

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
CFT menghadirkan fusi RGB-thermal berbasis Transformer yang menangkap interaksi lintas-modal secara simultan, meningkatkan deteksi multispektral.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `fang2022cft` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 189/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
