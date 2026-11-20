# RGB-D Heterogeneous Image Feature Fusion for YOLOfuse Apple Detection Model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2023rgb` |
| Judul asli | RGB-D Heterogeneous Image Feature Fusion for YOLOfuse Apple Detection Model |
| Penulis | Liu, Liqun; Hao, Pengfei |
| Tahun | 2023 |
| Venue | Agronomy |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [liu2023rgb.pdf](../pdf/liu2023rgb.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy13123080

## Gambaran Umum

Penelitian ini mengatasi deteksi apel untuk robot pemanen. Posisi apel di kebun bersifat acak, sehingga citra yang dikumpulkan sistem penglihatan memuat banyak sasaran tertutup daun, ranting, atau buah lain. Informasi yang hilang pada apel tertutup menyulitkan identifikasi dan penentuan lokasi serta menurunkan ketepatan cengkeraman. Penulis mengusulkan model YOLOfuse berbasis fusi fitur citra heterogen RGB-D yang mampu mengenali apel tertutup dan tetap ringan untuk dipasang pada perangkat tertanam robot pemanen.

Data berasal dari dua himpunan yang keduanya memakai kamera kedalaman prinsip *time of flight* (ToF). Himpunan publik PApple_RGB-D-Size dari Universitat de Lleida memuat 4.017 pasangan citra RGB-D dari enam pohon apel Fuji, terdiri atas 2.407 pasangan apel matang dan 1.610 pasangan apel hijau 75% matang dengan total 16.332 objek apel; banyak di antaranya mengalami penutupan ranting, tumpang tindih antarbuah, dan pemotongan tepi. Kamera Microsoft Kinect v2 memiliki rentang tangkap 0,3–0,8 m, jarak citra sekitar 0,5 m, format PNG, dan resolusi 1024 × 1024. Himpunan buatan sendiri memakai kamera kedalaman Basler yang dipasangi kamera warna, dengan rentang 0,3–1,5 m, jarak citra sekitar 0,8 m, format TIFF, resolusi 640 × 480, serta empat keluaran berupa citra intensitas, keyakinan, kedalaman, dan awan titik tiga dimensi. Data ini dikumpulkan di Basis Eksperimen Apel Institut Penelitian Buah Tianshui, Gansu, Tiongkok, lebih dari 2.000 pasangan RGB-D antara pukul 14.00–17.00 pada bulan Agustus; pengambilan menghindari sinar matahari langsung dan siang hari karena informasi kedalaman melemah. Anotasi memakai LabelImg berformat XML. Transformasi affine acak, balik horizontal, Mosaic, dan perubahan HSV diterapkan berurutan sehingga setiap himpunan menjadi 10.000 citra. Kedua himpunan dibagi secara acak dengan nisbah latih:validasi:uji 8:1:1 dan resolusi masukan diskalakan menjadi 480 × 480.

Mekanisme deteksi membangun *backbone* dua cabang: cabang RGB memakai YOLOv5s, sedangkan cabang kedalaman memakai CSPDarknet53-Tiny. Fitur kedalaman yang bersifat jarang digabungkan dengan keluaran modul SPP melalui strategi Ffuse = FRGB + αFDepth dengan faktor α dalam rentang 0–1; penulis menetapkan α = 0,2 agar fitur RGB tetap dominan dan fitur kedalaman tidak mencair. Modul *coordinate attention* (CA) disisipkan setelah fusi untuk memanfaatkan informasi spasial arah tinggi dan lebar tanpa biaya komputasi besar. Algoritme Soft-NMS menggantikan NMS standar karena NMS menekan kotak apel yang tertutup apel di depannya; Soft-NMS menurunkan skor keyakinan secara bertahap alih-alih langsung menjadi nol. Pelatihan memakai pembelajaran pindah, pengoptimal Adam, ukuran kumpulan 8, 300 epoch, momentum 0,937, peluruhan nol, dan jadwal laju pembelajaran COS dari 10⁻⁵ yang naik menjadi 3 × 10⁻⁴ lalu turun kembali; bobot akhir diambil dari epoch ke-120 dengan AP validasi 94,5%.

Metrik yang dipakai adalah presisi, recall, F1-score, AP sebagai integral kurva presisi terhadap recall, dan FPS dihitung dari waktu pemrosesan 100 citra. Pada himpunan uji publik, YOLOfuse mencapai AP 94,2%, presisi 95,4%, recall 89,1%, F1 92,1%, laju 51,761 FPS, 10,701 juta parameter, dan ukuran model 41,1 MB dibandingkan YOLOv5s yang mencatat AP 93,6%, 54,645 FPS, 7,022 juta parameter, dan 26,9 MB. Model ini mengungguli YOLOv3, YOLOv4, YOLOv4-Tiny, dan Faster RCNN dengan selisih AP berturut-turut 2,4; 2,5; 2,3; dan 2,2 poin persentase, meski kalah dari YOLOv5m, YOLOv5l, dan YOLOv5x. Uji ablasi menunjukkan Soft-NMS menaikkan AP dari 93,7% menjadi 94,2% dibanding NMS; perbandingan modul perhatian memberi AP 94,2% untuk CA, 93,6% untuk SE, dan 94,3% untuk CBAM dengan laju berturut-turut 51,761; 52,482; dan 48,273 FPS, sehingga CA dipilih sebagai keseimbangan antara akurasi dan kecepatan.

Batasan yang dinyatakan penulis mencakup akurasi YOLOfuse yang masih lebih rendah daripada YOLOv5m, YOLOv5l, dan YOLOv5x, sehingga struktur jaringan dan jumlah parameter perlu diperbaiki. Pemrosesan awal citra kedalaman mengonsumsi sumber daya komputasi sehingga kecepatan YOLOfuse turun dibanding YOLOv5s, dan model tidak sebanding dengan YOLOv4-Tiny dalam kecepatan karena cabang tersebut memakai masukan tunggal serta hanya dua skala fitur. Pengambilan data juga dibatasi oleh rentang kamera dan kondisi pencahayaan, karena sinar matahari langsung melemahkan informasi kedalaman. Penulis menyatakan data dapat diperoleh dari penulis korespondensi atas permintaan, bukan disediakan terbuka.
