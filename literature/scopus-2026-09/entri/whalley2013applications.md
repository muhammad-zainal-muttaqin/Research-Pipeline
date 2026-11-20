# Applications of image processing in viticulture: A review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `whalley2013applications` |
| Judul asli | Applications of image processing in viticulture: A review |
| Penulis | Whalley, J.; others |
| Tahun | 2013 |
| Venue | Proceedings 20th International Congress on Modelling and Simulation Modsim 2013 |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [whalley2013applications.pdf](../pdf/whalley2013applications.pdf)

## Gambaran Umum

Tinjauan ini membahas penerapan pengolahan citra digital untuk pengelolaan kebun anggur (*viticulture*). Industri anggur bernilai ekonomi besar. Hasil panen dapat berbeda jauh antar tahun dan antar bagian kebun. Cara yang dipakai saat ini untuk menaksir hasil dan mutu bersifat merusak, mahal, kurang akurat, dan sangat subjektif. Penulis menilai citra yang diambil di lapangan dapat memberi informasi yang tidak merusak tentang seluruh kebun. Tinjauan ini memusatkan perhatian pada pengambilan dan analisis citra dari dekat, di atas tanaman, pada tingkat permukaan tanah.

Tinjauan ini mencakup studi-studi terbaru di empat bidang. Bidang pertama adalah estimasi hasil. Bidang kedua adalah evaluasi mutu buah, yang dikaitkan dengan ukuran, berat, dan warna buah. Bidang ketiga adalah deteksi penyakit seperti embun tepung, embun bulu, dan botrytis. Bidang keempat adalah fenologi, yaitu tahap perkembangan tanaman. Penulis menyebut bahwa sebagian besar karya sebelumnya berfokus pada pencarian buah untuk panen robotik, penyemprotan cerdas, dan pemangkasan, bukan pada estimasi hasil. Penulis juga mencatat bahwa sebagian besar penelitian mutu dilakukan terhadap buah tunggal di laboratorium, bukan di alam.

Dari sisi metode, tinjauan ini menguraikan beberapa studi. Chamelat dkk. (2006) mendeteksi tandan anggur merah di citra luar ruang dengan momen Zernike dan warna, serta *support vector machine* (SVM). Metode itu mencapai tingkat keberhasilan 99%. Reis dkk. (2011) mendeteksi anggur merah dan putih pada citra malam hari dan melaporkan tingkat deteksi salah 9%. Murillo-Bracamontes dkk. (2012) memakai transformasi Hough lingkaran untuk mencari buah, termasuk buah yang tertutup sebagian. Dunn dan Martin (2004) memotret kanopi Cabernet Sauvignon dengan latar putih dan menghitung piksel buah dengan ambang warna RGB. Battany (2008) menghitung buah Pinot Noir dari pemindai datar, dengan segmentasi *watershed*. Metode itu dinilai cukup akurat, tetapi masih memerlukan panen destruktif dan pengambilan sampel. Nuske dkk. (2011) mengembangkan metode untuk mendeteksi dan menghitung buah anggur. Metode itu memperkirakan hasil dengan selisih 9,8% dari hasil panen sebenarnya.

Untuk deteksi penyakit, Meunkaewjinda dkk. (2008) mengklasifikasikan daun anggur menjadi tiga kelas, yaitu bercak, karat, dan sehat, dengan jaringan saraf dan SVM. Hasilnya dinilai baik, tetapi segmentasi daun masih terganggu oleh piksel latar yang ambigu. Li dkk. (2012) mengenali penyakit embun bulu dan embun tepung dengan 31 fitur warna, tekstur, dan morfologi. Tingkat pengenalan yang dilaporkan adalah 90% untuk embun bulu dan 93% untuk embun tepung. Untuk fenologi, Rodríguez-Pulido dkk. (2012) memperkirakan tingkat kematangan anggur merah dari citra yang diambil sejak *véraison*. Mereka menghitung persentase buah yang melewati ambang kecerahan (R+G+B)/3 ≥ 90 untuk menentukan tahap *véraison* setiap tandan.

Penulis menyatakan bahwa tantangan utama ada pada pengambilan citra di lapangan. Warna buah berubah menurut kondisi cahaya. Pada anggur putih, dan pada semua varietas sebelum *véraison*, warna buah sulit dibedakan dari kanopi. Buah yang tertutup buah lain, daun, dan kanopi juga menyulitkan deteksi. Penulis menilai fitur RGB saja tidak memadai untuk varietas putih atau sistem penopang yang berbeda. Penulis juga menyatakan bahwa sebagian besar karya terbaik belum memakai citra lapangan. Metode yang diharapkan harus tanpa pengawasan manusia, murah, andal, dan berjalan secara real-time. Di akhir, penulis menyimpulkan bahwa belum ada sistem yang dapat melacak dan memprediksi tahap fenologi tanaman dan buah dari musim ke musim. Mereka juga menilai bahwa algoritma yang cepat, akurat, dan umum masih perlu dikembangkan. Tujuannya adalah deteksi penyakit dan lokasi buah secara langsung.
