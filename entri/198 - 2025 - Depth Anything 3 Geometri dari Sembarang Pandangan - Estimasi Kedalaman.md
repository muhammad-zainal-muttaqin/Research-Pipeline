# 198 - Depth Anything 3: Recovering the Visual Space from Any Views

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2025depthanything3` |
| Judul asli | Depth Anything 3: Recovering the Visual Space from Any Views |
| Penulis | Haotong Lin, Sili Chen, Jun Hao Liew, Donny Y. Chen, Zhenyu Li, Guang Shi, Jiashi Feng, Bingyi Kang (ByteDance Seed) |
| Tahun | 2025 |
| Venue | arXiv preprint arXiv:2511.10647 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2511.10647
- **Versi HTML naskah:** https://arxiv.org/html/2511.10647v1
- **Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Anything%203%3A%20Recovering%20the%20Visual%20Space%20from%20Any%20Views
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Depth%20Anything%203%3A%20Recovering%20the%20Visual%20Space%20from%20Any%20Views&sort=relevance

## Gambaran Umum

Depth Anything 3 (DA3) memperluas keluarga Depth Anything dari estimasi kedalaman satu citra menjadi model geometri untuk **sembarang jumlah citra masukan**: satu foto, beberapa foto dari sudut berbeda, atau bingkai-bingkai video — dengan atau tanpa posisi kamera yang diketahui. Dari masukan itu model menghasilkan geometri 3D yang konsisten antarcitra, sehingga kedalaman dari semua pandangan dapat dilebur menjadi satu awan titik 3D yang utuh.

Kontribusi konseptualnya adalah **penyederhanaan ekstrem** pada dua sisi. Pertama, arsitektur: alih-alih merancang jaringan khusus multi-pandangan seperti pendahulunya (VGGT), DA3 memakai satu transformer polos — encoder DINOv2 standar — tanpa satu pun modifikasi struktural; satu-satunya penyesuaian adalah cara token ditata saat *forward pass*. Kedua, target pelatihan: alih-alih dilatih multi-tugas dengan banyak keluaran (kedalaman, pose, peta titik, pelacakan), DA3 hanya memprediksi dua peta per citra — peta kedalaman dan peta sinar (*depth-ray*) — yang ternyata cukup untuk menurunkan semua besaran lain, termasuk pose kamera.

Hasilnya: SOTA pada 18 dari 20 konfigurasi tolok ukur geometri visual baru yang dibangun penulis, melampaui VGGT dengan margin rata-rata 44,3% pada akurasi pose kamera dan 25,1% pada akurasi geometri (menurut abstrak versi terbaru), sekaligus mengungguli Depth Anything 2 pada kedalaman monokular.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular (bab 071, 175) menghasilkan peta kedalaman yang tampak meyakinkan per citra, tetapi tidak menjamin **konsistensi lintas pandangan**: dua foto dari sudut berbeda bisa memperoleh kedalaman yang saling bertentangan pada titik 3D yang sama. Padahal robotika, pemetaan, dan realitas tertambah justru menuntut konsistensi itu.

Cara klasik mengatasinya adalah *Structure from Motion* (SfM) dan *Multi-View Stereo* (MVS): deteksi titik kunci, pencocokan antarcitra, estimasi pose, *bundle adjustment*, lalu stereo padat. Pipeline modular ini rapuh pada permukaan polos, reflektif, atau perubahan sudut besar. Generasi terpelajar menggantinya dengan satu jaringan: DUSt3R memprediksi peta titik 3D dari pasangan citra, dan VGGT — pemegang SOTA sebelum DA3 — melangkah lebih jauh dengan pelatihan berskala besar. Tetapi keduanya, terutama VGGT, membayar dengan **kompleksitas**: arsitektur multi-tahap yang dirancang khusus, target prediksi yang redundan (pose + peta titik lokal dan global + kedalaman), dan pelatihan multi-tugas dari nol yang tidak dapat memanfaatkan model pralatih berskala besar. Dua pertanyaan yang dijawab DA3: (1) apakah target prediksi bisa direduksi ke himpunan minimal, dan (2) apakah satu transformer polos sudah cukup.

## Ide Utama

Jawaban DA3 atas kedua pertanyaan itu adalah "ya". Transformernya boleh polos asalkan token lintas pandangan dapat bertukar informasi — dan itu bisa dicapai hanya dengan **menata ulang token** pada sebagian lapis, tanpa mengubah arsitektur. Target prediksinya boleh tunggal asalkan bentuknya tepat — dan bentuk yang tepat adalah **sinar kamera per piksel**: bila untuk setiap piksel diketahui dari titik mana sinar itu berangkat, ke arah mana, dan seberapa jauh ia mengenai permukaan, maka posisi kamera dan struktur 3D seluruhnya sudah ditentukan. Tidak perlu kepala pose, kepala peta titik, atau kepala pelacakan terpisah.

## Cara Kerja Langkah demi Langkah

### Apa yang Disederhanakan

Perbandingan berikut merangkum apa yang dikurangi DA3 dari desain ala VGGT:

```
Desain khusus multi-tugas (mis. VGGT)        Depth Anything 3
─────────────────────────────────────        ─────────────────
N citra                                      N citra (+pose, opsional)
  │                                            │
  ▼                                            ▼
transformer khusus multi-tahap:              SATU transformer polos (DINOv2),
blok atensi bergantian yang                  tanpa modifikasi arsitektur;
dirancang khusus + redundansi                hanya penataan ulang token:
  │                                            lapis awal  : atensi dalam-citra
  ▼                                            lapis akhir : atensi silang/dalam
banyak kepala prediksi:                        │      (bergantian, rasio 1:2)
 ├─ kepala pose                                ▼
 ├─ kepala kedalaman                         Dual-DPT head (reassembly berbagi,
 ├─ kepala peta titik (lokal+global)          ├─ cabang fusi depth -> peta kedalaman
 └─ kepala pelacakan                          └─ cabang fusi ray   -> peta sinar
  │                                            │
  ▼                                            ▼
banyak loss multi-tugas yang                 P = t + D(u,v)·d  →  titik 3D, pose,
harus ditimbang satu per satu                dan awan titik diturunkan dari
                                             dua peta ini saja
```

Yang dikurangi: blok-blok atensi khusus, kepala-kepala prediksi tambahan, dan penimbangan banyak loss multi-tugas. Yang dipertahankan justru aset paling berharga: bobot pralatih DINOv2 berskala besar, sehingga DA3 mewarisi kemampuan ekstraksi fiturnya secara penuh — sesuatu yang hilang bila arsitektur dilatih dari nol.

### Masukan dan Token Kamera

Model menerima N citra (N = 1 berarti monokular biasa). Setiap citra dibagi menjadi *patch* dan diubah menjadi token oleh encoder DINOv2. Di depan token-token setiap citra ditambahkan satu **token kamera**: bila parameter kamera (intrinsik K, rotasi, translasi) diketahui, token itu diisi hasil lewat satu MLP kecil; bila tidak, dipakai token bersama yang dipelajari. Token kamera ikut dalam semua operasi atensi, sehingga informasi pose — bila ada — menyebar ke seluruh fitur. Karena pose bersifat opsional, satu model yang sama melayani masukan berpose maupun tanpa pose.

### Atensi Silang Adaptif-Masukan

L lapis transformer dibagi dua kelompok dengan rasio 2:1. Pada Ls lapis pertama, atensi bekerja **di dalam masing-masing citra** (token satu foto hanya beratensi dengan token foto itu sendiri). Pada Lg lapis terakhir, atensi **bergantian** antara dalam-citra dan lintas-citra — dan di sinilah satu-satunya "penyesuaian" terjadi: token-token dari semua citra ditata ulang (*rearranged*) sehingga operasi atensi standar transformer sekaligus menjangkau pandangan lain. Tidak ada modul baru; yang berubah hanyalah susunan data yang masuk operasi yang sudah ada. Desain ini adaptif terhadap masukan: dengan satu citra, model secara alami merosot menjadi estimator kedalaman monokular tanpa biaya tambahan.

### Representasi Depth-Ray

Ini kunci mengapa satu target cukup. Untuk setiap piksel p = (u, v), kamera memandang dunia melalui sebuah **sinar** yang dinyatakan enam angka: titik asal t (posisi pusat kamera di dunia, 3 angka) dan arah d (3 angka). Secara geometri, arah itu adalah d = R·K⁻¹·p: piksel diproyeksikan-balik ke ruang kamera lalu diputar ke ruang dunia. Model memprediksi, untuk setiap citra, **peta kedalaman** D (satu nilai per piksel) dan **peta sinar** M (enam nilai per piksel). Titik 3D dunia yang dilihat piksel itu kemudian diperoleh dengan satu perkalian dan satu penjumlahan:

```
                     kamera (pusat t)
                        \
                         \   sinar: arah d = R·K⁻¹·p
                          \
   piksel p=(u,v) ────────●────────────────●  P = t + D(u,v) · d
   pada citra             ^                ^
                          sinar kamera     titik 3D di dunia,
                                           jaraknya = kedalaman D(u,v)
```

Mengapa tidak langsung memprediksi pose (matriks rotasi R)? Karena matriks rotasi memiliki kendala ortogonalitas yang sulit dipelajari jaringan secara stabil. Sinar per piksel menyandikan pose yang sama **secara implisit** tanpa kendala itu; bila pose eksplisit diperlukan, ia dapat diturunkan dari peta sinar melalui perhitungan homografi (algoritme DLT dilanjutkan dekomposisi RQ untuk memisahkan K dan R). Untuk kepraktisan, DA3 juga menyediakan **kepala kamera ringan** yang memprediksi FOV, rotasi (kuaternion), dan translasi langsung dari token kamera — biayanya diabaikan karena hanya mengolah satu token per citra. Eksperimen ablation makalah (Tabel 6) menunjukkan target depth-ray ini bukan hanya minimal, tetapi juga **mengungguli** alternatifnya: peta titik saja (ala DUSt3R) tidak menjamin konsistensi, sedangkan target redundan (ala VGGT) justru menimbulkan keterkaitan antar-keluaran yang menurunkan akurasi pose.

### Dual-DPT Head

Kedua peta diproduksi oleh satu kepala prediksi bernama Dual-DPT. Fitur dari backbone mula-mula melewati modul *reassembly* **yang dipakai bersama**, lalu bercabang ke dua set lapis fusi yang berbeda — satu untuk kedalaman, satu untuk sinar — dan ditutup dua lapis keluaran. Berbagi pemrosesan awal membuat kedua tugas saling menguatkan (kedalaman dan sinar adalah dua sisi dari geometri yang sama), sementara pemisahan di ujung mencegah representasi yang redundan.

### Pelatihan Guru–Murid

Data nyata berlabel kedalaman sering kali jarang atau bising (penuh lubang dan derau). Karena itu DA3 memakai paradigma guru–murid: sebuah model **guru** — estimator kedalaman monokular yang juga hanya berupa DINOv2 + decoder DPT — dilatih khusus pada ±20 dataset **sintetik** (yang labelnya sempurna) hingga menghasilkan kedalaman berkualitas tinggi. Untuk setiap citra nyata, kedalaman relatif dari guru diselaraskan ke pengukuran asli yang jarang/bising melalui estimasi skala-geser RANSAC, sehingga diperoleh label yang padat, halus, tetapi tetap setia secara geometris. DA3 (murid) dilatih pada campuran label asli dan label guru ini — supervisi beralih ke label guru setelah langkah ke-120 ribu dari total 200 ribu langkah pada 128 GPU H100. Guru yang sama juga dipakai melatih varian monokular (mengungguli Depth Anything 2) dan varian kedalaman metrik (mengikuti kerangka ruang kanonik Metric3Dv2).

## Eksperimen dan Hasil

Penulis membangun tolok ukur geometri visual dari lima dataset (HiRoom, ETH3D, DTU, 7Scenes, ScanNet++; total ±89 scene, dari level objek hingga luar ruang) dengan tiga kelompok pengujian: akurasi pose (metrik AUC dari galat rotasi/translasi relatif), akurasi rekonstruksi (F1 atas awan titik hasil leburan TSDF), dan kualitas *rendering* (PSNR/SSIM/LPIPS pada sintesis pandangan baru). Hasil utama:

- **SOTA pada 18 dari 20 konfigurasi pengujian** dalam tolok ukur tersebut.
- Melampaui VGGT dengan margin rata-rata **44,3% akurasi pose** dan **25,1% akurasi geometri** (abstrak versi terbaru; versi v1 melaporkan 35,7% dan 23,6% — lihat Poin untuk Sitasi). Pada tabel pose v1, misalnya, AUC@30 DA3 pada ETH3D dan DTU mengungguli VGGT, Pi3, MapAnything, dan DUSt3R/Fast3R dengan jarak lebar.
- Pada tolok ukur monokular standar, varian monokularnya **mengungguli Depth Anything 2** — model guru/basisnya sendiri.
- Sebagai aplikasi hilir, fine-tuning DA3 dengan kepala Gaussian (GS-DPT) untuk sintesis pandangan baru *feed-forward* (FF-NVS) mengungguli model khusus tugas itu (mis. DepthSplat), dan makin baik geometri DA3, makin baik pula hasil NVS — bukti bahwa geometri adalah fondasi tugas-tugas 3D lain.

Interpretasinya: margin diperoleh bukan dari arsitektur yang lebih besar (parameter DA3 justru lebih ramping dari VGGT 1,19B), melainkan dari pemilihan target yang tepat dan pemanfaatan penuh pralatih DINOv2 — persis tesis "pemodelan minimal" yang diusung makalah.

## Kelebihan dan Keterbatasan

Kelebihan: (1) satu model untuk spektrum penuh masukan — monokular, multi-pandangan, video, berpose/tanpa pose; (2) arsitektur sederhana yang mewarisi skala pralatih DINOv2 dan mudah direproduksi konsepnya; (3) target depth-ray yang minimal terbukti mengungguli target yang lebih kaya; (4) fondasi kuat untuk tugas hilir (NVS, varian metrik); (5) seluruh pelatihan memakai dataset akademik publik.

Keterbatasan: (1) biaya pelatihan sangat besar (128 GPU H100, 200 ribu langkah) — reproduksi penuh di luar jangkauan kebanyakan laboratorium; (2) tolok ukur baru dibangun oleh tim yang sama, sehingga validasi independen masih diperlukan; (3) inferensi multi-pandangan pada transformer tetap mahal seiring bertambahnya jumlah citra (pelatihan memakai 2–18 pandangan); (4) karya akhir 2025 — angka dan protokolnya belum lama terbuka untuk pemeriksaan komunitas.

## Kaitan dengan Bab Lain

Bab ini puncak sementara garis kedalaman dalam tinjauan: berawal dari estimasi per-citra (bab 062–068), dimantapkan Depth Anything (bab 071) dan Depth Anything V2 (bab 175) — yang menjadi basis arsitektur guru sekaligus pembanding langsung. Varian metriknya mengikuti kerangka kanonik Metric3Dv2, sejalan dengan bab 177 (Metric3D). Pergeserannya dari "kedalaman per citra" ke "geometri konsisten lintas pandangan" melayani kebutuhan klaster Deteksi 3D (bab 087–098) dan RGB-D SLAM (bab 107–111), dan paling enak dibaca berdampingan dengan survei kedalaman metrik (bab 199) serta varian *real-time* AsyncMDE (bab 200).

## Poin untuk Sitasi

Kutip dengan kunci `lin2025depthanything3`. Ringkasan yang aman dikutip: "Depth Anything 3 menunjukkan satu transformer polos (DINOv2) dengan target prediksi depth-ray tunggal cukup untuk memulihkan geometri konsisten dari sembarang jumlah pandangan, dengan atau tanpa pose kamera, melampaui VGGT pada seluruh tugas tolok ukur geometri visual." **Catatan versi:** abstrak arXiv terbaru melaporkan margin 44,3% (pose) dan 25,1% (geometri), sedangkan teks v1 melaporkan 35,7% dan 23,6% — angka berubah antarversi, maka kutiplah angka sesuai versi yang dirujuk dan sebutkan versinya. Rincian arsitektur pada bab ini (rasio lapis 2:1, Dual-DPT, token kamera, pelatihan guru–murid) diambil dari teks lengkap v1; verifikasi ke naskah sebelum penggunaan formal.
