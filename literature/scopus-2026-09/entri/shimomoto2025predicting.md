# Predicting Sweet Pepper Yield Based on Fruit Counts at Multiple Ripeness Stages Monitored by an AI-Based System Mounted on a Pipe-Rail Trolley †

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shimomoto2025predicting` |
| Judul asli | Predicting Sweet Pepper Yield Based on Fruit Counts at Multiple Ripeness Stages Monitored by an AI-Based System Mounted on a Pipe-Rail Trolley † |
| Penulis | Shimomoto, Kota; Shimazu, Mitsuyoshi; Matsuo, Takafumi; Kato, Syuji; Naito, Hiroki; Kashino, Masakazu; Ohta, Nozomu; Yoshida, Sota; Fukatsu, Tokihiro |
| Tahun | 2025 |
| Venue | Horticulturae |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [shimomoto2025predicting.pdf](../pdf/shimomoto2025predicting.pdf)
- DOI resmi: https://doi.org/10.3390/horticulturae11070718

## Gambaran Umum

Penelitian ini bertujuan menilai hubungan antara jumlah buah paprika pada
berbagai tahap kematangan dan hasil panen, lalu menguji akurasi model prediksi
hasil panen pekan berikutnya di rumah kaca komersial berskala besar. Penulis
mengadaptasi sistem pemantauan buah tomat sebelumnya untuk paprika. Latar
belakangnya adalah produksi paprika berfluktuasi karena fenomena *flush* dan
gugurnya bunga, sehingga pemantauan langsung dan prediksi beberapa pekan ke
depan diperlukan. Berbeda dengan tomat, tanaman paprika memiliki batang kaku,
tidak dapat diturunkan, dan buahnya berwarna tidak merata saat matang.

Percobaan dilakukan di rumah kaca komersial Ai-Sai Farm Kokonoe, Jepang, pada
paprika ‘Nagano’ yang ditanam pada blok rockwool. Rumah kaca seluas 3,0 ha
terbagi menjadi empat ruang masing-masing 0,6 ha; satu ruang dengan 144 baris
tanam menjadi fokus pengujian. Perangkat pemindai berkamera ganda dipasang
pada troli rel pipa yang bergerak sekitar 0,24 m/s saat pemotretan malam hari.
Dua kamera menghadap sisi kiri dan kanan secara bersamaan pada sudut zenit
60° dengan pencahayaan LED 6500 K sebesar 540 lx pada jarak 30 cm. Video
diubah menjadi citra panorama, dipotong menjadi kotak 512 × 512 piksel, lalu
dianalisis. Deteksi memakai Mask R-CNN ber-ResNet101 yang sudah dilatih pada
MS COCO, dengan 1042 citra latih dan 190 citra validasi, 500 epoch, laju
pembelajaran 0,001, momentum 0,9, peluruhan bobot 0,0001, dan ambang IoU di
atas 0,5.

Kematangan ditentukan setelah deteksi dengan mengubah citra tersembunyi ke
model warna HSL dan memetakan nilai hue ke tiga kelas: merah (0–30 dan
345–360), *turning* (30–70), dan hijau (70–160). Laju pewarnaan buah dihitung
dari piksel merah ditambah piksel *turning* dengan faktor 0,25, sementara
piksel dengan kecerahan di atas 210 dikeluarkan. Tahap kematangan dibagi
menjadi 0% (pembesaran), 1–40%, 41–80%, dan 81–100%. Deteksi dilakukan untuk
satu kelas tanpa membedakan buah matang dan muda. Penghitungan memakai rata-rata
jumlah buah dari enam baris di tiga titik, kurang dari 5% dari total 144 baris;
sebagai acuan, seorang petani menghitung manual 20 tanaman di tengah baris
pada pekan 1–11.

Hasil menunjukkan AP pada IoU 0,5 stabil di kisaran 71–77% selama 12 pekan.
Hubungan hitungan manual dan otomatis memberi koefisien korelasi 0,96 untuk
tahap 1–40% (kemiringan 0,80), 0,63 untuk 41–80% (0,19), dan 0,92 untuk
81–100% (0,87). Jumlah buah tahap 1–40% dan 41–80% berkorelasi dengan hasil
panen seluruh area 0,6 ha pada pekan berikutnya, masing-masing r = 0,88 dan
0,94 (p < 0,01); tahap 81–100% tidak signifikan (r = 0,48). Model regresi
linier berganda dengan validasi silang *leave-one-out* memberi WAPE 21,35%
untuk pasangan 1–40% dan 41–80%, 24,06% untuk ketiga tahap, dan 63,18% untuk
tahap 81–100% saja. Acuan hasil panen adalah berat buah terpanen di seluruh
area 0,6 ha yang diukur dari pekan 2 hingga 13.

Batasan yang dinyatakan penulis mencakup AP yang lebih rendah daripada
penelitian tomat sebelumnya karena okklusi daun dan salah deteksi buah hijau
sebagai daun. Sistem meremehkan jumlah buah karena hanya permukaan yang
menghadap kamera yang tampak, dan buah tahap 41–80% sering salah diklasifikasi
sebagai 81–100%. Ukuran buah tidak diukur karena penaksiran dari piksel citra
depan tidak dapat diandalkan saat daun menutupi buah. Pengujian hanya
mencakup enam baris dan dilakukan pada musim dingin, sehingga pengaruh musim
panas serta keragaman hasil di seluruh area perlu dinilai. Penulis juga
menyatakan WAPE 21,35% belum tinggi dan dapat ditingkatkan dengan memasukkan
cuaca, kecepatan pematangan, dan lebih banyak baris pantauan.
