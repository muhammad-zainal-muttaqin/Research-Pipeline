# YOLO11-SBS: leveraging ACE and ORCM to gauge robust and accurate apple counting in complex orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2026yolo11` |
| Judul asli | YOLO11-SBS: leveraging ACE and ORCM to gauge robust and accurate apple counting in complex orchards |
| Penulis | Zhang, Long; Wang, Haochen; Zhang, Jiarui; Su, Ye; Yao, Ruitong; Liu, Jiashu; Jia, Aowei; Liu, Juan; Hu, Jie |
| Tahun | 2026 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [zhang2026yolo11.pdf](../pdf/zhang2026yolo11.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2026.1841916

## Gambaran Umum

Kajian ini mengatasi deteksi dan penghitungan apel hijau pada kebun dengan latar kompleks. Model YOLO konvensional memiliki bobot konvolusi tetap, mekanisme penyaringan fitur yang lemah, serta rentan terhadap bayangan cabang dan daun serta kantong plastik pembungkus buah. Kemampuan memanfaatkan fitur multiskala juga belum memadai, sehingga detail buah kecil dan berkerumun hilang dan penghitungan menjadi tidak tepat. Tujuannya adalah membangun model YOLO11-SBS sekaligus mengukur ketahanan dan mutu penghitungan memakai metrik ACE dan ORCM. ACE menilai ketahanan terhadap gangguan pencahayaan, sedangkan ORCM menyatakan secara bersamaan galat positif palsu dan galat kelewatan pada berbagai tingkat oklusi.

Tanaman yang dikaji adalah apel kultivar Ruixue. Pengambilan citra dilakukan di kebun apel Kabupaten Wanrong, Kota Yuncheng, Provinsi Shanxi, Tiongkok, dari 20 September hingga 10 Oktober 2025 dengan selang 3 hari. Sejumlah 2.210 citra dikumpulkan dari berbagai sudut pandang dan jarak, mencakup adegan banyak buah, sedikit buah, pencahayaan depan, pencahayaan belakang, pandangan dekat, dan pandangan jauh. Anotasi memakai LabelImg dengan satu kelas "apple" dan diekspor ke berkas TXT format YOLO berisi ID kelas serta koordinat dan ukuran kotak ternormalisasi. Pembagian acak 8:1:1 menghasilkan 1.768 citra latih, 221 citra validasi, dan 221 citra uji tanpa tumpang tindih. Pelatihan memakai 300 epoch, batch 24, optimizer SGD, laju pembelajaran awal 0,01, masukan 640 × 640, dan RTX 4090D 24 GB dengan PyTorch 2.0.1.

YOLO11-SBS memodifikasi YOLO11 dengan tiga bagian. Modul C3k2_SAC menggabungkan SAConv untuk kalibrasi bobot konvolusi secara dinamis dan fusi dua cabang adaptif, sehingga menyaring fitur dan menekan gangguan bayangan daun serta kantong buah. Modul C2PSA_BIF, ditempatkan setelah SPPF, memakai bi-level routing attention dan position-sensitive attention untuk mempertajam fitur lokal buah dan menghilangkan gangguan tangkai. Modul ASF2 terdiri atas SSFF dan TFE, yang melakukan agregasi sejajar skala tanpa parameter dan interaksi fitur lintas skala 3D guna meningkatkan penghitungan buah kecil dan rapat. Penghitungan dilakukan dengan mendeteksi kotak buah lalu menghitung jumlah kotak hasil. ACE dihitung sebagai rata-rata perubahan metrik antara pencahayaan normal dan pencahayaan yang diganggu; nilainya lebih kecil berarti lebih stabil. ORCM menggabungkan laju galat pada empat tingkat oklusi dengan bobot tetap λ₀ = 1, λ₁ = 2, λ₂ = 3, dan λ₃ = 4; nilainya berkisar 0 sampai 1 dan lebih tinggi berarti lebih tangguh.

Pada split uji 221 citra, YOLO11-SBS mencapai presisi 86,7%, recall 83,7%, mAP@50 92,0%, dan mAP@50:95 75,2% dengan 2.569.755 parameter dan 128,8 FPS. YOLO11 sebagai acuan menghasilkan 85,5%, 79,8%, 88,9%, dan 67,0%; YOLOv5, YOLOv6, YOLOv8, YOLOv9, YOLOv10, YOLOv12, dan RT-DETR juga dibandingkan. Validasi silang 10 lipat memberi rerata 86,7%, 83,7%, 92,0%, dan 75,2% dengan simpangan baku masing-masing 1,1%, 1,2%, 1,3%, dan 0,7%. Ablasi menunjukkan kombinasi BiFormer, ASF2, dan SAConv menghasilkan recall tertinggi. Pada metrik ORCM, YOLO11-SBS memperoleh 0,878 (tertinggi), dengan laju galat 14,6% tanpa oklusi, 6,7% oklusi ringan, 8,3% oklusi sedang, dan 5,2% oklusi berat, serta MAE 3,86 dan RMSE 5,34. ORCM berkorelasi negatif dengan MAE dan RMSE (Pearson r = −0,962; Spearman r = −0,964; p < 0,001). Di bawah gangguan pencahayaan buatan, ACE model ini 4,30%, terendah di antara model yang dibandingkan, dengan perubahan presisi 4,5%, recall 4,6%, mAP@50 3,1%, dan mAP@50:95 5,0%.

Penulis menyebutkan tiga batasan. Data dikumpulkan dari wilayah geografis yang sempit, satu kultivar, dan satu periode akuisisi, sehingga generalisasi ke kebun, kultivar, tahap pertumbuhan, dan musim lain belum terbukti. Kinerja pada kondisi ekstrem seperti motion blur parah, cuaca buruk, lingkungan malam, dan pergeseran domain antarperangkat masih memerlukan pengujian lanjutan. Penambahan beberapa modul meningkatkan kompleksitas model, yang dapat membatasi penerapan pada perangkat edge dengan sumber daya sangat terbatas.
