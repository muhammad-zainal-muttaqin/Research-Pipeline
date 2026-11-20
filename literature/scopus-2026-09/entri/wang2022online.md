# Online recognition and yield estimation of tomato in plant factory based on YOLOv3

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2022online` |
| Judul asli | Online recognition and yield estimation of tomato in plant factory based on YOLOv3 |
| Penulis | Wang, Xinfa; Vladislav, Zubko; Viktor, Onychko; Wu, Zhenwei; Zhao, Mingfu |
| Tahun | 2022 |
| Venue | Scientific Reports |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [wang2022online.pdf](../pdf/wang2022online.pdf)
- DOI resmi: https://doi.org/10.1038/s41598-022-12732-1

## Gambaran Umum

Kajian ini bertujuan mewujudkan estimasi hasil panen tomat secara daring di pabrik tanaman dengan pencahayaan buatan. Di lingkungan tersebut, tanaman tumbuh rapat dan tidak teratur serta batang, daun, dan buah saling menutupi, sehingga pengenalan ciri citra menjadi faktor pembatas estimasi hasil. Penulis mengusulkan metode pengenalan buah merah dan buah hijau berbasis YOLOv3 yang diperbaiki untuk menghitung buah dan mengestimasi hasil pada kondisi pertumbuhan alami.

Eksperimen berlangsung di laboratorium pabrik tanaman Institut Sains dan Teknologi Henan dari Januari hingga Agustus 2021 dengan tomat kerdil Micro-Tom. Sistem akuisisi memakai kamera RGB-D Intel RealSense D455 dan kamera industri iDS-TCV441-CF pada jarak 800 mm dari tanaman, dilengkapi rel, pan-tilt, dan modul 5G yang tidak dipakai dalam percobaan ini. Citra tanaman dalam pot diambil dari tiga arah, yaitu bidang horizontal setiap 60°, bidang miring 45° setiap 60°, dan satu bidang tegak lurus, sehingga setiap tanaman menghasilkan 13 citra. Dari 120 tanaman diperoleh 1.560 citra tanaman tunggal dan 780 citra rumpun tiga tanaman. Pengambilan pada tanaman hidroponik berpencahayaan buatan dilakukan secara acak pada berbagai waktu dan sudut; 2.600 citra dipilih dan 4.000 buah diberi label. Augmentasi mencakup rotasi, pembalikan, pencerminan, dan blur. Secara keseluruhan, 3.680 citra asli dan 18.400 citra hasil augmentasi dianotasi dengan LabelImg; dari 4.680 sampel, 1.000 dijadikan himpunan uji dan 3.680 himpunan latih. Pelatihan berjalan pada server Sugon Tiankuo I620-G30 dengan prosesor Xeon E5-2680v4, memori 128 GB, dan RTX 1080Ti, memakai PyTorch 1.39, CUDA 10.1, CUDNN 7.6, dan OpenCV 4.0.0. Parameter pelatihan adalah 700 iterasi, ukuran batch 8, momentum 0,9, learning rate 0,001, ambang keyakinan 0,5, dan ambang non-maximum suppression 0,3.

Mekanisme deteksi memakai DarkNet53 untuk mengekstrak fitur multiskala. Citra diubah ke ukuran 416 × 416 piksel, lalu diturunkan 32 kali, 16 kali, dan 8 kali menghasilkan peta fitur 13 × 13, 26 × 26, dan 52 × 52 yang digabungkan kembali melalui upsampling dan konkatenasi. K-means clustering dengan indeks 1-IOU menghasilkan sembilan kotak prior yang dibagi menurut tingkat peta fitur, sehingga diperlukan 10.647 prediksi per citra. Karena jarak antara kamera dan buah berubah terus, fungsi rugi posisi berbasis jarak Euclidean yang tidak invarian skala diganti dengan GIoU, yaitu jumlah seluruh sel dan kotak prior dari 1 dikurangi GIoU. Penulis menyatakan perubahan ini membuat nilai rugi bergantung pada jarak kotak prediksi terhadap kotak sebenarnya dan membantu mengurangi kegagalan deteksi pada buah kecil.

Metrik yang dipakai adalah mAP dan akurasi estimasi hasil, dengan akurasi dihitung sebagai rasio jumlah buah yang terdeteksi terhadap hitungan manual. Model YOLOv3 dasar mencatat mAP 96,5%, sedangkan model perbaikan mencatat 99,3%, atau naik 2,8% menurut Tabel 3 dan simpulan; abstrak menyebut kenaikan 2,7%. Waktu deteksi rata-rata per citra adalah 15 ms untuk kedua model. Pada uji lapang yang mencakup 200 bidang pandang, akurasi estimasi model perbaikan untuk buah merah, buah hijau, dan seluruh buah berturut-turut adalah 99,4%, 99,3%, dan 99,3%, naik 2,5%, 4,3%, dan 3,3% dibanding YOLOv3 yang mencatat 97,0%, 95,2%, dan 96,1%. Pengujian pada 30 citra per kategori menunjukkan kenaikan 2,9% dan 2,8% untuk buah jarang, 5,9% dan 7,1% untuk buah rapat, serta 9,2% dan 9,4% untuk buah tertutup, masing-masing untuk buah merah dan hijau. Simpulan mencatat akurasi 99,5% dan 99,4% pada buah rapat serta 98,9% dan 98,7% pada buah tertutup.

Batasan yang dinyatakan penulis mencakup rendahnya akurasi buah hijau dibanding buah merah karena kemiripan warna dengan latar tanaman dan kerumitan pencahayaan pabrik tanaman; area hijau pada citra kadang terdeteksi sebagai tomat, sementara buah yang menyatu dengan latar tidak terdeteksi. Periode perubahan warna buah sangat singkat sehingga datanya sedikit dan timpang dibanding data buah merah dan hijau. Penulis tidak melakukan pelabelan maupun klasifikasi terpisah untuk buah pada masa transisi warna, melainkan hanya dua kelas. Kerumitan lingkungan pabrik tanaman dan kekhususan aplikasinya juga menyulitkan deteksi dan estimasi hasil, sehingga diperlukan penelitian lanjutan. Dataset tersedia dari penulis sesuai permintaan.
