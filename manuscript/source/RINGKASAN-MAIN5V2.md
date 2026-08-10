# Ringkasan Review Article — main5v2

**Judul:** *Multi-View and Multimodal Perception for Class-Wise Fruit Inventories: A Design-Space Review*

**Total:** 29 halaman, 235 referensi, 8 seksi utama + 3 lampiran.

---

## Masalah Inti (hal. 1)

Menghitung buah sawit per kelas kematangan bukan sekadar deteksi per-gambar. Sistem harus: (1) mendeteksi setiap tandan, (2) memberi label kematangan ke tandan yang benar, (3) **tidak menghitung tandan yang sama dua kali** saat kamera berpindah sisi. Duplikasi lintas-pandangan inilah masalah utama yang belum ditangani review sebelumnya.

## Kontribusi (hal. 1, paragraf 5)

Tiga kontribusi eksplisit:

1. **Taksonomi 6 mekanisme identitas (M0–M5)** — dari deteksi per-gambar tanpa asosiasi (M0), koreksi statistik (M1), pencocokan tampilan/re-ID (M2), tracking temporal (M3), asosiasi geometris/3D (M4), sampai asosiasi multi-view terpelajari (M5). Setiap mekanisme punya asumsi minimum dan mode kegagalan berbeda.
2. **Sintesis komparatif** bukti detektor, geometri, fusi, dan asosiasi menurut keputusan yang didukung tiap mekanisme.
3. **Interpretasi pertanian** — memisahkan bukti langsung dari mekanisme transferable, dan mendefinisikan pengukuran yang dibutuhkan untuk inventaris buah sadar-duplikat.

## Struktur Seksi (hal. 1–25)

| Seksi | Isi | Halaman (kira-kira) |
|---|---|---|
| 1. Introduction | Masalah, scope, kontribusi | 1–2 |
| 2. Review approach | Tiga level bukti: direct, transferable, design hypothesis | 2 |
| 3. Design space | **Taksonomi M0–M5**, asumsi akuisisi A1–A7, atribut kelas di luar kematangan | 2–4 |
| 4. Instance formation | Detektor RGB: R-CNN→YOLO→DETR, backbone, attention, query-based | 4–9 |
| 5. Cross-view identity | Depth monokular, persepsi 3D, pose/grasping, SLAM, **bukti counting multi-view pertanian**, positioning vs 6 review lain | 9–19 |
| 6. Synthesis & Discussion | Tiga kesimpulan terbatas, disagreement fusi, limitasi | 19–21 |
| 7. Conclusion | Identitas lintas-pandangan harus dievaluasi langsung | 21 |
| App. A | **Matriks bukti 44 studi** (longtable) | 22–25 |
| App. B | 7 query string Scopus lengkap (Q1–Q7) | 25–27 |
| App. C | Dokumentasi pencarian: alur, eligibility, screening, angka PRISMA | 27–29 |

## Alur Argumen (jika ditanya "apa inti reviewnya?")

1. **Deteksi saja tidak cukup.** AP tinggi per-gambar tidak menjamin hitungan benar per-pohon — tandan yang sama bisa terdeteksi dari 2–3 sisi (k ≈ 1,89 di SawitMVC).

2. **Ada 6 cara menangani duplikasi** (M0–M5), masing-masing butuh asumsi berbeda. Tidak ada satu mekanisme universal — pilihan tergantung protokol akuisisi (berapa sisi, ada depth atau tidak, kamera bergerak atau diam).

3. **Depth bukan solusi otomatis.** Depth membantu separasi geometris (tandan kecil/tertutup), tetapi pseudo-depth dari RGB berbagi error dengan RGB itu sendiri. Depth sensor bisa gagal di bawah sinar matahari langsung. Prinsipnya: *filter before you fuse* (SA-Gate, D3Net).

4. **Fusi di level fitur/akhir lebih baik dari fusi di input.** Ophoff dkk. menyapu 28 titik fusi di YOLOv2 dua-cabang dan menemukan fusi awal (4-kanal) kalah dari fusi tengah/akhir. Ini temuan transferable paling penting di review (hal. 16–17).

5. **Bukti langsung untuk sawit masih tipis.** Dari 44 studi di matriks, tidak ada satu pun yang mengevaluasi RGB-D + deduplikasi lintas-pandangan + kelas kematangan secara bersamaan untuk FFB. Ini gap yang review serahkan ke eksperimen.

## Figur Kunci (jika ditanya detail visual)

| Figur | Isi | Hal. |
|---|---|---|
| Fig. 1 | Peta konseptual review: 4 sumbu (RGB, depth, fusi, geometri/asosiasi) | 2 |
| Fig. 2 | Timeline komponen desain YOLO | 5 |
| Fig. 3 | Silsilah paradigma detektor RGB | 4 |
| Fig. 4 | Tiga lokasi fusi (early, middle, late) | 12 |
| Fig. 5 | Dua pola integrasi YOLO+depth | 16 |
| Fig. 6 | Mekanisme cross-modal attention/gating | 13 |
| Fig. 7 | Funnel bukti → gap riset FFB | 19 |
| Fig. 8 | Pipeline konseptual (setiap tahap = hipotesis) | 19 |
| Fig. 9 | Distribusi temporal 182 sumber (2012–2026) | 20 |
| Fig. 10 | Distribusi tematik 17 area riset | 20 |

## Tabel Kunci

| Tabel | Isi | Hal. |
|---|---|---|
| Table I | 6 mekanisme identitas M0–M5 + asumsi minimum | 3 |
| Table II | Pertanyaan yang mengubah perbandingan detektor jadi bukti FFB | 8 |
| Table III | Alternatif fusi + failure mode yang harus diuji | 17 |
| Table IV | Hierarki metrik: deteksi → atribut → geometri → counting → deployment | 20 |
| Table V | Positioning vs 6 review sebelumnya | 18 |
| Table VI | Hasil pencarian per query (Scopus + OpenAlex) | 28 |
| Table VII | **Matriks bukti 44 studi** (Appendix A) | 22–25 |

## Positioning vs Review Lain (hal. 18, Table V)

Enam review sebelumnya (Lai, Goh, Naftali, Naghipour, Sapkota, Nordin & Misro) diorganisasi menurut sensor, kematangan, keluarga detektor, atau aplikasi pertanian. **Tidak ada yang menjadikan identitas lintas-pandangan sebagai unit perbandingan utama.** Itulah gap yang diisi review ini.

## Jika Ditanya Pertanyaan Spesifik

| Pertanyaan | Jawab singkat | Baca detail |
|---|---|---|
| "Kenapa bukan systematic review?" | Ini structured evidence-mapping review — memetakan mekanisme, bukan menghitung pooled effect | hal. 27, §C.1 |
| "Kenapa judulnya tidak ada sawit?" | Scope = pertanian umum, sawit kasus utama; mekanisme dari luar pertanian = transferable | hal. 1 par. 3 + poin revisi 5 |
| "Apa bedanya M0 dengan M4?" | M0 = hitung per-gambar tanpa asosiasi; M4 = gunakan geometri 3D/depth untuk menolak duplikat | hal. 3, Table I |
| "Kenapa depth bisa merugikan?" | D3Net: depth buruk menurunkan prediksi kecuali ada quality gate | hal. 13 |
| "Berapa referensi baru dari Scopus?" | 44 studi di matriks bukti + referensi tambahan, total 235 sitasi | App. A + App. C |
| "Bagaimana SawitMVC masuk?" | Dikutip sebagai dataset yang aligned dengan masalah inventaris (punya identity graph lintas-sisi) | hal. 18 |
