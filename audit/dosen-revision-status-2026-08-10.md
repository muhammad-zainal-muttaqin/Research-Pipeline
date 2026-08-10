# Status Revisi Dosen

Audit ini mencocokkan delapan butir pada `literature/references/revisi-dosen-2026-07-23/Chat.txt` dengan naskah aktif dan artefak pencarian yang tersedia pada 10 Agustus 2026.

| No. | Permintaan dosen | Bukti keadaan saat ini | Status | Pekerjaan yang diperlukan |
|---:|---|---|---|---|
| 1 | Metodologi pencarian reproduksibel | `main3.tex` memuat sumber Scopus/OpenAlex, rentang 2015-2026, tujuh keluarga query di Appendix, IC/EC, deduplikasi, triage, ranking judul-abstrak, dan angka corong. | Selesai | Batas Web of Science dan batas full-text dilaporkan eksplisit. |
| 2 | Reframe menjadi *design-space review* untuk inventaris buah unik per kelas | `main3.tex` berpusat pada konversi observasi berulang menjadi inventaris instans unik per kelas, bukan sejarah YOLO/RGB-D atau usulan satu arsitektur. | Selesai | Tidak ada tindakan struktural tersisa. |
| 3 | Deduplikasi multiview sebagai kontribusi utama dan positioning terhadap review terdahulu | `main3.tex` memuat taksonomi M0-M5, asumsi A1-A7, pertanyaan kapan deduplikasi layak dibayar, dan positioning terhadap review terdahulu. | Selesai | Klaim kebaruan dibatasi pada korpus yang ditemukan dan diverifikasi. |
| 4 | Sawit sebagai kasus utama, mekanisme non-pertanian sebagai bukti transfer | `main3.tex` memisahkan bukti langsung sawit/buah dari mekanisme transfer non-pertanian pada sintesis dan matriks. | Selesai | Tidak ada tindakan struktural tersisa. |
| 5 | Judul tanpa YOLO, RGB-D, dan kelapa sawit | Judul `Multi-View and Multimodal Perception for Class-Wise Fruit Inventories: A Design-Space Review` dipakai pada `main3.tex` dan `main-elsarticle3.tex`. | Selesai | Tidak ada tindakan struktural tersisa. |
| 6 | Klasifikasi digeneralisasi sebagai atribut instans | `main3.tex` mendefinisikan atribut sebagai properti instans dan memberi contoh kematangan, ukuran, mutu, penyakit, kultivar, serta kesiapan panen. | Selesai | Tidak ada tindakan struktural tersisa. |
| 7 | Tambahkan sawit, Suharjito, Goh, apel, jeruk, anggur | `main3.tex` memuat SawitMVC, Suharjito, Goh, apel, jeruk, anggur, serta bukti full-text baru untuk FruitNeRF, RGB-D SLAM tomat, dan LiDAR-camera pear. | Selesai | Status direct dan transferable dibedakan pada matriks. |
| 8 | Evidence matrix menjadi tabel sintesis di makalah | Appendix pada `main3.tex` memuat satu baris per 44 studi yang diikutkan setelah targeted full-text review, dengan metode, modalitas, evaluasi, mekanisme identitas, atribut, temuan, batas transfer, status, dan sitasi. | Selesai | Matriks CSV juga tersedia untuk audit baris per baris. |

## Batas bukti yang wajib disebut

Pencarian Scopus 7 query menghasilkan 15.722 baris ekspor. Pencarian OpenAlex menghasilkan 16.656 baris. Setelah deduplikasi lintas-query dan lintas-sumber, master kerja berisi 21.066 record. Triage judul-abstrak meneruskan 20.035 record ke tahap full-text.

Full-text lokal belum tersedia untuk seluruh kandidat. Audit awal terhadap folder `literature/pdf/benar/` menemukan 182 PDF dan 6 kecocokan dengan master pencarian baru. Setelah itu dilakukan retrieval targeted dari shortlist, sehingga 44 record memiliki full-text dan evidence row lengkap, sedangkan 16 record telah dikeluarkan setelah review. Sebelas kandidat shortlist masih memerlukan retrieval manual. Karena itu, angka 20.035 tidak boleh ditulis sebagai studi yang sudah termasuk.

Naskah `main3.tex` menyatakan dua register secara terpisah dan menambahkan register prioritas:

1. Register A: hasil pencarian dan penyaringan kandidat baru, dengan status full-text yang belum lengkap.
2. Register B: korpus sumber yang full-text-nya telah diverifikasi dan dipakai untuk sintesis mekanisme.
3. Register prioritas: 20.035 kandidat diranking, 250 dipilih sebagai shortlist, dan 60 ditempatkan pada wave pertama. Tidak ada kandidat yang dihapus dari data pencarian.

Pemisahan ini mencegah corong PRISMA dibuat seolah-olah berakhir pada angka 182 atau 20.035 studi yang sudah direview penuh.
