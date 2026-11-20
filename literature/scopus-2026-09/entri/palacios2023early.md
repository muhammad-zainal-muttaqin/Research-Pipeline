# Early yield prediction in different grapevine varieties using computer vision and machine learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `palacios2023early` |
| Judul asli | Early yield prediction in different grapevine varieties using computer vision and machine learning |
| Penulis | Palacios, Fernando; Diago, Maria P.; Melo-Pinto, Pedro; Tardaguila, Javier |
| Tahun | 2023 |
| Venue | Precision Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [palacios2023early.pdf](../pdf/palacios2023early.pdf)
- DOI resmi: https://doi.org/10.1007/s11119-022-09950-y

## Gambaran Umum

Kajian ini bertujuan mengembangkan algoritma prakiraan hasil awal untuk beberapa varietas anggur memakai penglihatan komputer dan pembelajaran mesin. Cara konvensional bersifat destruktif, memerlukan banyak tenaga, dan memakan waktu, sehingga diperlukan penaksiran yang objektif dan cepat. Penulis menguji pula perbedaan kinerja antara model yang dibuat untuk setiap varietas secara terpisah dan model umum yang mencakup semua varietas.

Tanaman yang digunakan adalah enam varietas *Vitis vinifera* L., yaitu tiga varietas merah (Cabernet Sauvignon, Syrah, Tempranillo) dan tiga varietas putih (Malvasia, Muscat of Alexandria, Verdejo), di kebun komersial Vergalijo, Navarra, Spanyol, musim 2018. Sebanyak 96 pohon dipilih, 16 per varietas, dengan satu baris untuk setiap varietas, sistem VSP, jarak baris 2 m, dan jarak pohon 1 m. Defoliasi parsial dengan membuang tiga daun per sulur dilakukan pada tahap pembentukan buah. Citra RGB diambil pada 3 Juli 2018, 66 hari sebelum panen, pada tahap buah seukuran kacang dengan diameter sekitar 7 mm, memakai platform bergerak berbasis kendaraan segala medan yang membawa kamera Canon EOS 5D Mark IV 30,4 MP dengan lensa 35 mm. Kamera ditempatkan 1,80 m dari kanopi, tegak lurus, pada ketinggian 1 m, dengan pengaturan 1/1600 s, ISO 2000, f/5,6, resolusi 6720 × 4480, dan pencahayaan buatan dua panel LED untuk pengambilan pada malam hari. Pada panen, tandan dikumpulkan, ditimbang, dibatang, dan buah dihitung manual untuk memperoleh hasil, jumlah buah, dan berat buah per pohon.

Mekanismenya terdiri atas segmentasi dan regresi. Arsitektur SegNet dengan encoder VGG16 dan decoder cermin digunakan untuk segmentasi semantik. Pelatihan memakai 1.646 potongan citra dari 18 citra resolusi penuh pada pohon lain di kebun dan varietas yang sama; potongan 1120 × 1120 piksel diubah menjadi 560 × 560. Segmentasi berlangsung bertahap: tandan, lalu buah dengan kelas latar, kontur, dan pusat, kemudian unsur kanopi dalam enam kelas, yaitu celah, permukaan bawah daun, permukaan atas daun, sulur, batang, dan tandan. Pelabelan unsur kanopi memakai regresi logistik multinomial dari enam fitur warna RGB dan CIELAB. Enam fitur yang dihitung per pohon adalah jumlah buah tampak hasil segmentasi (F1), nisbah piksel permukaan bawah daun dalam kotak tandan (F2), jumlah piksel sulur di zona buah (F3), jumlah piksel permukaan atas daun (F4), nisbah F4 terhadap luas zona buah (F5), dan luas zona buah (F6). Untuk prakiraan hasil, ditambahkan berat buah rata-rata per varietas. Regresi memakai support vector regression dengan fungsi kernel linear dan fitur distandardisasi. Validasi deteksi buah memakai 60 citra resolusi penuh, sepuluh per varietas, dengan pusat buah dicek manual. Model regresi diuji dengan leave-one-out, eightfold yang diulang 30 kali, dan leave-one-variety-out, serta model lokal per varietas dengan leave-one-out.

Hasil deteksi buah tampak menunjukkan presisi rata-rata 0,626, recall 0,860, dan F1 0,722. Presisi melebihi 0,60 pada semua varietas kecuali Verdejo (0,520), sedangkan F1 di atas 0,70 kecuali Verdejo (0,648). Hubungan antara jumlah buah tampak hasil estimasi dan jumlah buah tampak nyata per citra memiliki R² di atas 0,92 untuk semua varietas. Untuk jumlah buah aktual per pohon, model global dengan leave-one-out menghasilkan RMSE 195 buah, NRMSE 23,83%, dan R² 0,79; eightfold memberi R² 0,77 dan NRMSE 24,67%; leave-one-variety-out memberi R² 0,76 dan NRMSE 31,44%. Model lokal menghasilkan RMSE 204, NRMSE 25,19%, dan R² 0,72. F1 merupakan fitur paling berpengaruh; menghilangkannya menurunkan R² dari kisaran 0,77–0,79 menjadi 0,49–0,51. Untuk prakiraan hasil, model global mencapai R² 0,83 dengan RMSE 0,45 kg dan NRMSE 30% pada leave-one-out, R² 0,82 pada eightfold, serta R² 0,76 dengan RMSE 0,54 kg dan NRMSE 35,89% pada leave-one-variety-out. Per varietas, R² hasil di atas 0,70 kecuali Syrah (0,65) dan Tempranillo (0,54), dengan NRMSE 16,47% pada Verdejo dan 39,17% pada Muscat of Alexandria.

Batasan yang dinyatakan penulis adalah hasil Verdejo lebih rendah karena tandannya lebih besar, sehingga lebih banyak artefak yang salah dikenali sebagai buah. Syrah berbeda dari varietas lain karena kanopinya lebih berongga dan lebih banyak piksel sulur, sehingga NRMSE naik menjadi 55,96% saat varietas itu tidak ikut dilatih. Model lokal tidak lebih akurat daripada model global, terutama untuk Cabernet Sauvignon dan Tempranillo, karena hanya 16 pohon per varietas. Penulis juga mencatat warna hijau buah pada tahap tersebut mirip daun dan sulur, sehingga menimbulkan positif palsu, serta menyatakan bahwa galat 10–15% masih belum tercapai dan penelitian lanjutan memerlukan lebih banyak data, varietas, dan kondisi vigor kanopi.
