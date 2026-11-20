# Complete and accurate holly fruits counting using YOLOX object detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022complete` |
| Judul asli | Complete and accurate holly fruits counting using YOLOX object detection |
| Penulis | Zhang, Yanchao; Zhang, Wenbo; Yu, Jiya; He, Leiying; Chen, Jianneng; He, Yong |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [zhang2022complete.pdf](../pdf/zhang2022complete.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107062

## Gambaran Umum

Pencacahan buah pada seluruh tajuk pohon sulit dilakukan dengan satu foto. Buah sering tertutup daun, tersembunyi di balik cabang, berada dalam bayangan, atau menempel satu sama lain. Pencacahan dari satu sisi pohon juga melewatkan buah di sisi lain. Kajian ini mengusulkan metode pencacahan buah lengkap pada satu pohon dengan cara menyusun panorama 360 derajat dari citra drone, lalu mendeteksi buah pada panorama tersebut menggunakan jaringan deteksi objek *YOLOX*. Metode ini diuji pada pohon *holly* yang berbuah lebat.

Citra diambil dengan drone DJI Mavic 2 Pro yang dilengkapi kamera RGB beresolusi 4000 × 3000 piksel. Drone terbang mengelilingi pohon dengan sudut elevasi 30 derajat dan memotret satu foto untuk setiap rotasi 30 derajat. Jari-jari pengambilan (R) diuji pada rentang 0,6 m sampai 2,0 m. Citra dijahit menjadi panorama menggunakan fitur *SIFT*. Jumlah buah aktual pada setiap jarak berkisar antara 614 dan 753 buah. Data latih dibuat dari tiga kelompok jarak, yaitu R 1,0 m, 1,5 m, dan 2,0 m, dengan sampel yang juga mencakup bayangan dan oklusi. Data dibagi 75% untuk latih dan 25% untuk validasi. Anotasi dibuat dengan program Labelimg. Penulis menambah sampel dengan augmentasi *Gaussian kernel*, penyesuaian komponen gamma, dan teknik *mosaic* serta *MixUp*.

Model YOLOX dilatih dengan PyTorch 1.11 pada ukuran masukan 640 × 640 piksel. Hasil pencacahan pada panorama dilaporkan dengan dua metrik. *Detection Rate* (DR) membandingkan jumlah buah yang dihitung jaringan dengan jumlah buah yang tertangkap di panorama. *Statistical Rate* (SR) membandingkan jumlah buah yang dihitung dengan jumlah buah aktual. Pada R 0,6 m sampai 1,2 m, DR berada di atas 99%, yaitu 99,343%, 99,147%, 99,128%, dan 99,519%. Pada R 2,0 m, DR sebesar 97,671%. SR tertinggi tercatat 98,534% pada R 0,6 m dan turun menjadi 90,374% pada R 2,0 m. SR masih di atas 95% hingga R 1,4 m, yaitu 95,618%, dan turun di bawah 95% pada R 1,6 m dengan nilai 95,549%. Tingkat penangkapan buah pada panorama (CR) berada di atas 96% untuk R hingga 1,6 m. Nilai CR terendah tercatat 92,53% pada R 2,0 m. Penulis juga mencatat bahwa metode ini lebih unggul daripada penelitian terdahulu yang dikutip, yaitu deteksi stroberi dengan 91% dan deteksi jeruk dengan 92%. Penulis menyatakan bahwa penambahan kernel Gaussian dan kompensasi gamma berdampak positif pada laju deteksi, terutama pada sampel yang gelap dan buram. Dalam penelitian ini, metode lain yang diuji tidak mencapai laju deteksi lebih tinggi daripada YOLOX.

Penulis menyatakan beberapa batasan. Sebagian buah tetap tidak terdeteksi pada ambang kepercayaan 0,5. Buah yang hilang umumnya memiliki kontur tidak lengkap, bayangan berat, piksel yang tidak cukup, atau bentuk mirip dengan objek lain. Buah yang jauh dari kamera dan berukuran sangat kecil juga sering tidak dikenali sebagai buah. Penulis menyatakan bahwa bayangan dan buram tidak dapat dihilangkan sepenuhnya walaupun komposisi sampel sudah dioptimalkan. Penurunan ambang kepercayaan dapat meningkatkan deteksi, tetapi penulis tidak menyajikan angka hasil untuk pengaturan tersebut. Panorama juga mengalami sedikit kabur dan distorsi akibat peregangan tajuk dan penjahitan, meskipun penulis menyatakan hal ini tidak memengaruhi deteksi. Pengujian hanya dilakukan pada satu jenis pohon. Penulis berpendapat bahwa metode ini dapat diperluas ke buah lain, seperti apel dan leci, tetapi klaim tersebut belum diuji dalam penelitian ini.
