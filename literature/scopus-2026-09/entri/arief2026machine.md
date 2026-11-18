# Machine vision for detection of defective oil palm fresh fruit bunches using YOLO Algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arief2026machine` |
| Judul asli | Machine vision for detection of defective oil palm fresh fruit bunches using YOLO Algorithm |
| Penulis | Arief, Dodi Sofyan; Shiddiq, Minarni; Jahrizal, Jahrizal; Dalil, M; Salambue, Roni; Yuhendra, Ari; Dasta, Vicky Vernando; Hamid, Muhammad Ikhsan; Mahmudah, Dewi Anjarwati; Harmailil, Ihsan Okta |
| Tahun | 2026 |
| Venue | Journal of Physics Conference Series |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [arief2026machine.pdf](../pdf/arief2026machine.pdf)
- DOI resmi: https://doi.org/10.1088/1742-6596/3186/1/012026

## Gambaran Umum

Penelitian ini membangun sistem visi mesin waktu nyata untuk mendeteksi tandan buah segar (TBS) sawit yang cacat pada konveyor rol, sebagai pengganti penyortiran manual di stasiun penerimaan pabrik minyak sawit. Penyortiran manual biasanya dilakukan oleh dua hingga empat pekerja berpengalaman, bersifat membosankan, subjektif, dan rawan salah. Empat kategori cacat mengikuti aturan pabrik, yaitu tangkai panjang, berduri atau tidak berkembang, kosong, dan busuk. Model yang dibangun hanya membedakan dua kelas, yaitu normal dan cacat, karena sistem hanya memiliki satu lengan pemisah.

Datanya adalah citra TBS dari perkebunan PTPN V di Provinsi Riau, Indonesia, yang validasi kelasnya dilakukan oleh tiga grader berpengalaman. Sampel terdiri atas 200 TBS normal dan 200 TBS cacat, dengan 50 TBS per kategori cacat; setiap TBS dipotret 6–8 kali dari bagian depan dan belakang pada empat posisi dalam bidang pandang kamera, sehingga menghasilkan 2.400 citra. Anotasi memakai LabelImg dan menghasilkan berkas .txt berisi indeks kelas serta koordinat xcen, ycen, w, dan h. Data dibagi dengan rasio 80:20 untuk latih dan uji. Perangkat kerasnya berupa kamera CMOS warna DFM 22BUC03-ML (744 × 480 piksel, 0,4 MP, 76 FPS) dengan lensa 16 mm pada jarak 90 cm dari permukaan konveyor, pelindung logam putih, dua lampu neon 5 W, konveyor rol sepanjang 5 m, katup pneumatik dan lengan pemisah, Arduino, serta Intel NUC. Perangkat lunaknya memakai Python 3.8, YOLOv4-tiny, pustaka pelacakan SORT, OpenCV, Arduino IDE, dan Flask.

Mekanisme deteksi memakai YOLOv4-tiny dengan konfigurasi batch 64, subdivisi 16, masukan 416 × 416, dua kelas, 21 filter, dan max_batches 6000 dengan langkah pada 80% dan 90% dari nilai tersebut. Pelatihan memakai bobot awal yolov4-tiny.conv.29 dari repositori AlexeAB yang telah dilatih pada COCO berisi 80 kelas, melalui Darknet dan Google Colab. Kotak deteksi diberikan pada setiap TBS yang muncul dan dilacak hingga garis pemicu; bila kelas abnormal memiliki keyakinan lebih dari 70%, sinyal dikirim ke Arduino, katup pneumatik mendorong TBS cacat keluar dari konveyor, lalu ditarik kembali setelah 500 ms. TBS normal tidak memicu sinyal. Kinerja diukur dengan AP, mAP, IoU, serta matriks konfusi yang menghasilkan presisi, recall, dan F1-score.

Pelatihan menunjukkan rugi minimum 0,04 pada iterasi ke-5900 dengan skor 99,71%. Pada iterasi 5000, model memperoleh mAP 99,08% dan IoU rata-rata 87,79%, lebih baik daripada iterasi 3000 (mAP 96,53%, IoU 78,44%) dan 4000 (mAP 98,05%, IoU 80,90%). Pengujian waktu nyata dengan grader di pabrik menghasilkan presisi rata-rata 99,65% untuk kelas normal dan 99,38% untuk kelas cacat; abstrak menyebut AP 98% dan 96%, serta mAP 99,7% dari matriks konfusi, sedangkan simpulan menyebut mAP validasi 99,6% untuk normal dan 99,7% untuk cacat. Validasi pada 60 sampel TBS, 30 per kelas, menghasilkan untuk kelas normal 27 deteksi benar, 3 positif palsu, presisi 0,90, recall 1,00, dan F1 0,94; untuk kelas cacat 24 deteksi benar, 6 negatif palsu, presisi 0,80, recall 1,00, dan F1 0,88.

Batasan yang dinyatakan penulis adalah model hanya dua kelas agar sesuai dengan satu lengan pemisah. Beberapa TBS terdeteksi salah karena overfitting, kebutuhan data yang lebih besar khususnya untuk TBS cacat, intensitas pencahayaan yang rendah sehingga kedua kelas sulit dibedakan, dan ukuran TBS yang beragam hingga menyebabkan bidang gambar tidak tajam; penulis mengusulkan lensa autofokus. Kinerja kelas cacat lebih rendah karena jumlah citra untuk empat jenis cacat belum memadai. Kriteria lain seperti kotor, basah, spikelet rusak, dan TBS bertumpuk atau tertutup sebagian tidak dimasukkan karena jumlahnya sedikit di area penyortiran. Penulis mengusulkan pengembangan model empat kelas dan model untuk TBS bertumpuk dengan lengan pemisah lain.

