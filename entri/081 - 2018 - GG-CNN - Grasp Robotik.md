# 081 - Closing the Loop for Robotic Grasping: A Real-Time, Generative Grasp Synthesis Approach

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 081 dari 154 |
| Kunci BibTeX | `morrison2018ggcnn` |
| Judul | Closing the Loop for Robotic Grasping: A Real-Time, Generative Grasp Synthesis Approach |
| Penulis | Morrison, Douglas; Corke, Peter; Leitner, J{\"u |
| Tahun | 2018 |
| Venue / Jurnal | Robotics: Science and Systems (RSS) |
| Tema klaster | Grasp Robotik |
| Kata kunci | grasp, generative, per-pixel, real-time, closed-loop |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-grasp-robotik)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Closing%20the%20Loop%20for%20Robotic%20Grasping%3A%20A%20Real-Time%2C%20Generative%20Grasp%20Synthesis%20Approach
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Closing%20the%20Loop%20for%20Robotic%20Grasping%3A%20A%20Real-Time%2C%20Generative%20Grasp%20Synthesis%20Approach&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Metode grasp yang memprediksi kualitas dan pose grasp secara per-piksel dari citra kedalaman, memungkinkan grasp closed-loop real-time pada objek tak dikenal.

## Abstrak (Parafrase)
GG-CNN (Generative Grasping CNN) memprediksi peta grasp per-piksel: kualitas, sudut, dan lebar grasp untuk setiap piksel citra kedalaman, dalam satu lintasan jaringan yang sangat ringan. Karena cepat, ia memungkinkan kontrol closed-loop (memperbarui grasp real-time saat objek/robot bergerak) dan berhasil pada objek tak dikenal termasuk dinamis.

## Latar Belakang & Konteks
Pendekatan grasp berbasis sampling kandidat (mis. dua-tahap) lambat dan tidak cocok untuk kontrol closed-loop yang membutuhkan pembaruan grasp real-time.

## Permasalahan yang Diangkat
- Grasp berbasis sampling kandidat lambat.
- Tidak cocok untuk kontrol closed-loop.
- Objek dinamis butuh pembaruan real-time.
- Diskretisasi kandidat membuang informasi.
- Model besar sulit di perangkat robot.

## Tujuan & Pertanyaan Penelitian
- Memprediksi grasp per-piksel dalam satu lintasan.
- Memungkinkan kontrol closed-loop real-time.
- Menangani objek tak dikenal & dinamis.

## Tinjauan Terdahulu / Posisi Literatur
GG-CNN adalah alternatif ringan terhadap grasp berbasis CNN besar/sampling.

Karya/konsep pembanding yang relevan:

- Grasp dua-tahap (Lenz) — pembanding.
- Generative per-pixel prediction.
- Depth image input.
- Closed-loop control.

## Metodologi & Arsitektur
Jaringan konvolusi ringan (fully-convolutional) memetakan citra kedalaman ke tiga peta per-piksel: grasp quality, angle (sin/cos), dan width; grasp terbaik dipilih dari peta quality; karena ringan, dapat berjalan real-time untuk closed-loop grasping.

Komponen / langkah metodologis utama:

- Generative grasp map per-pixel (quality/angle/width).
- Jaringan fully-convolutional sangat ringan.
- Input citra kedalaman.
- Prediksi sudut via sin/cos.
- Real-time (closed-loop capable).
- Grasp objek tak dikenal.

## Kontribusi Utama
1. Grasp generatif per-piksel yang cepat.
2. Closed-loop real-time.
3. Ringan (cocok di robot).
4. Berhasil pada objek dinamis/tak dikenal.

## Rincian Eksperimen
Diuji dalam eksperimen fisik (robot) pada objek statis dan dinamis dengan metrik success rate grasp, dibandingkan pendekatan sampling.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Objek statis | success rate | tinggi |
| Objek dinamis | success rate | tinggi (closed-loop) |
| Kecepatan | latensi | real-time, sangat ringan |

## Temuan Kunci
- Grasp per-piksel generatif cepat & andal.
- Closed-loop meningkatkan keberhasilan pada dinamika.
- Model ringan praktis untuk robot.
- Kedalaman cukup untuk grasp banyak objek.

## Keunggulan
- Sangat ringan & real-time.
- Closed-loop capable.
- Andal pada objek tak dikenal.

## Keterbatasan
- Grasp planar (bukan 6-DoF penuh).
- Bergantung kualitas kedalaman.
- Objek sangat kompleks/berhimpitan menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
GG-CNN menegaskan grasp generatif per-piksel dari kedalaman — contoh langsung pemanfaatan depth untuk manipulasi real-time dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [080 - 2015 - Deep Learning Robotic Grasps (Lenz dkk.) - Grasp Robotik](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md)
- [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md)
- [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md)
- [084 - 2020 - GraspNet-1Billion - Grasp Robotik](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md)
- [085 - 2023 - BCMFNet (Bilateral Cross-Modal Fusion) - Grasp Robotik](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md)
- [086 - 2018 - Jacquard Dataset - Grasp Robotik](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Grasp Robotik** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Grasp Robotik)
Istilah penting untuk memahami makalah ini:

- **Grasp detection** — Prediksi cengkeraman stabil untuk objek.
- **Grasp rectangle** — Grasp sebagai kotak beorientasi (posisi, sudut, lebar).
- **Antipodal grasp** — Cengkeraman dua-jari berlawanan.
- **RGB-D** — Warna + kedalaman untuk geometri grasp.
- **6-DoF grasp** — Grasp enam derajat kebebasan di ruang 3D.
- **Cornell dataset** — Dataset grasp kecil klasik.
- **Jacquard** — Dataset grasp sintetis berskala besar.
- **Closed-loop** — Kontrol grasp real-time berbasis umpan-balik.
- **Success rate** — Persentase percobaan grasp berhasil.
- **Point cloud fusion** — Penggabungan geometri titik 3D.

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
GG-CNN memprediksi peta grasp per-piksel dari citra kedalaman dalam jaringan ringan, memungkinkan grasp closed-loop real-time yang andal termasuk pada objek dinamis dan tak dikenal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `morrison2018ggcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 081/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
