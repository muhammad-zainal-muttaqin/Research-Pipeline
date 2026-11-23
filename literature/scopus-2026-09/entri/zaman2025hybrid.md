# A Hybrid Approach for Handling Occlusion in UAV Images of Fresh Oil Palm Fruit Bunches Based on Computer Vision

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zaman2025hybrid` |
| Judul asli | A Hybrid Approach for Handling Occlusion in UAV Images of Fresh Oil Palm Fruit Bunches Based on Computer Vision |
| Penulis | Zaman, Baizul; Indrabayu; Nurtanio, Ingrid |
| Tahun | 2025 |
| Venue | Proceedings International Seminar on Intelligent Technology and Its Applications Isitia |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [zaman2025hybrid.pdf](../pdf/zaman2025hybrid.pdf)
- DOI resmi: https://doi.org/10.1109/isitia66279.2025.11137494

## Gambaran Umum

Penelitian ini bertujuan meningkatkan deteksi dan segmentasi tandan buah segar (TBS) kelapa sawit yang tertutup (oklusi) pada citra UAV. Penulis menyebut penyebab oklusi: pelepah yang saling menutupi, tandan yang bergerombol, dan sudut pandang yang tidak seragam. Penulis menyatakan studi terdahulu masih kesulitan pada tandan yang tertutup vegetasi dan sering memerlukan daya komputasi besar.

Data diambil dari kebun sawit rakyat di Kabupaten Polewali Mandar, Sulawesi Barat, memakai drone DJI Mavic Air pada cuaca cerah pukul 09.00 sampai 13.00, dengan jarak sekitar 2 meter dari tandan. Video berukuran 1920x1080 piksel, 30 fps, berdurasi 5 sampai 8 detik per tandan. Dari tiap video diambil sekitar 25 bingkai (selang delapan bingkai), sehingga totalnya 2.643 citra. Pembagiannya 70% latih (2.313 citra), 15% validasi (165), dan 15% uji (165). Teks tidak menyebut pembagian per tandan atau per pohon. Anotasi dilakukan manual dengan satu kelas, dan pemberi label tidak disebut. Citra diubah ukurannya menjadi 640x360 piksel.

Metode memakai YOLOv11-Seg, yaitu detektor satu tahap yang juga menghasilkan *mask* segmentasi tiap objek. Ditambahkan *Loss Rank Mining* (LRM): sampel dalam satu *batch* diurutkan menurut nilai *loss* (galat latih), lalu 35% dengan *loss* tertinggi dipilih sebagai sampel sulit untuk pembaruan parameter. Sampel dengan *loss* rendah tidak dibuang dan diberi bobot kecil saat *backpropagation*. Ambang 35% dinyatakan dipilih secara empiris. LRM hanya dipakai saat pelatihan sehingga waktu inferensi tidak berubah.

Pada 165 citra dengan 290 instans objek, YOLOv11-LRM mencapai *mask* mAP50 99,2% dan mAP50-95 85,6%, presisi 99,6%, *recall* 98,5%. Pembanding: YOLOv11n-Seg mAP50-95 83,2%, YOLOv11s-Seg 84,2%, YOLOv11m-Seg 84,0%. Selisih mAP50-95 terhadap varian terbaik berikutnya adalah 1,4 poin. Teks menyebut evaluasi pada 165 citra validasi, padahal 165 juga jumlah citra uji, sehingga set yang dipakai tidak jelas.

Keterbatasan yang dapat diperiksa: bingkai dari video yang sama sangat mirip dan pembagian tidak dinyatakan per tandan, sehingga kebocoran data antara latih dan uji mungkin terjadi (belum diperiksa). Hanya satu kelas, tanpa kematangan. Kondisi cuaca seragam, yang diakui penulis sebagai batas generalisasi. Tidak ada pengulangan dengan beberapa *seed* atau interval kepercayaan. Tidak ada pengukuran khusus pada subset tandan tertutup. Penghitungan tandan antarbingkai tidak dilakukan.
