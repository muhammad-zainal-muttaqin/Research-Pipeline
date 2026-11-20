# Citrus yield estimation based on images processed by an Android mobile phone

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gong2013citrus` |
| Judul asli | Citrus yield estimation based on images processed by an Android mobile phone |
| Penulis | Gong, Aiping; Yu, Junlin; He, Yong; Qiu, Zhenjun |
| Tahun | 2013 |
| Venue | Biosystems Engineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [gong2013citrus.pdf](../pdf/gong2013citrus.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2013.03.009

## Gambaran Umum

*Gong dkk.* (2013) memperkirakan hasil panen jeruk pada tingkat pohon, dua minggu sebelum panen. Data yang dipakai adalah 40 pohon jeruk Gannan yang tumbuh di Ganzhou, Jiangxi, Tiongkok. Pohon difoto di bawah cahaya matahari alami dengan telepon genggam Android (*android mobile phone*, AMP). Kamera diletakkan pada sudut acak terhadap tanah, sehingga setiap pohon difoto dari satu pandang saja.

Metode segmentasi memakai aturan warna. Piksel dianggap buah jika selisih merah dan biru (R dikurangi B) lebih besar dari N, dengan N berada di antara 90 dan 256, dan nilai merah (R) lebih besar dari nilai hijau (G). Nilai N dapat ditetapkan tetap atau disesuaikan otomatis dari warna yang dipilih pengguna dengan pena sentuh. Area di bawah 50 piksel dibuang sebagai derau. Area yang terlalu besar dihaluskan dengan erosi dan buka (*erosion and open*), lalu jumlah buah dihitung dengan *modified 8-connectedness chain code* (M8CCC). Kode ini mencatat arah dari setiap piksel batas ke piksel berikutnya. Jumlah kode 8 dibagi 4, dan hasilnya dibulatkan ke atas. Perangkat lunak ditulis dengan Java di Android dan menyimpan hasil ke basis data SQLite.

Pada dua dari 40 citra demonstrasi, ambang adaptif menghasilkan lebih sedikit derau dibanding ambang tetap 90 dan 110, dengan area buah yang tetap terjaga. Uji kluster memakai 50 citra, dengan 10 citra untuk setiap ukuran kluster 2 sampai 6 buah. Kluster 2 dan 3 buah dihitung dengan benar. Kluster 4 buah gagal sekali, kluster 5 buah gagal dua kali, dan kluster 6 buah benar kurang dari separuh. Penulis menyimpulkan M8CCC memadai untuk kluster di bawah lima buah. Pada 40 pohon validasi, jumlah buah dari algoritma penghitung buah (FCA) dibandingkan dengan hitungan pengamat manusia. Rerata rasio estimasi 90% dilaporkan, dan galat membesar seiring bertambahnya jumlah buah. Penulis menyebut empat sumber galat: daun yang membelah satu buah menjadi dua bagian, buah dalam bayangan yang tidak terdeteksi, daun mati atau daun berwarna serupa yang salah dianggap buah, dan perbedaan iluminasi antarcitra. Waktu pemrosesan sekitar 3 s per citra pada prosesor 1,4 GHz. Penulis menyimpulkan estimasi per pohon dapat dilakukan secara real time beberapa minggu sebelum panen.

Ada tiga batas yang perlu dicatat. Pertama, angka 90% adalah rasio rata-rata antara hasil estimasi dan hasil aktual per pohon, bukan presisi atau recall per buah, sehingga tidak dapat dibandingkan langsung dengan mAP. Kedua, data berasal dari satu kebun dan satu musim dengan 40 pohon. Ketiga, tidak ada pembanding dengan metode lain dan tidak ada evaluasi deteksi per buah.
