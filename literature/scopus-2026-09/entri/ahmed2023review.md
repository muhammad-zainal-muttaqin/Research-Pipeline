# A REVIEW OF NON-DESTRUCTIVE RIPENESS CLASSIFICATION TECHNIQUES FOR OIL PALM FRESH FRUIT BUNCHES

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ahmed2023review` |
| Judul asli | A REVIEW OF NON-DESTRUCTIVE RIPENESS CLASSIFICATION TECHNIQUES FOR OIL PALM FRESH FRUIT BUNCHES |
| Penulis | Mohamed Ahmed Mansour, Mohamed Yasser |
| Tahun | 2023 |
| Venue | Journal of Oil Palm Research |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [ahmed2023review.pdf](../pdf/ahmed2023review.pdf)
- DOI resmi: https://doi.org/10.21894/jopr.2022.0063

## Gambaran Umum

Tinjauan ini mengkaji penentuan tingkat kematangan tandan buah segar kelapa sawit. Cara yang biasa dipakai adalah inspeksi visual oleh pekerja terlatih berdasarkan warna dan jumlah buah lepas di sekitar pohon. Cara ini memakan tenaga dan waktu, serta rawan salah karena ketinggian pohon, penghitungan buah lepas, pandangan yang kurang jelas, dan kondisi pencahayaan. Tandan yang terlalu muda atau terlalu matang menurunkan efisiensi pemurnian minyak, mutu minyak, dan keuntungan. Penulis meninjau teknik non-destruktif untuk menilai apakah tiap teknik dapat dipakai secara langsung di lapangan dengan akurasi tinggi.

Tinjauan ini menyusun hasil kajian sebelumnya, bukan percobaan baru, dan tidak menyatakan strategi pencarian literatur. Teknik yang dibahas mencakup spektroskopi laboratorium dan lapangan, pengolahan citra digital, visi komputer, pencitraan hiperspektral, pencitraan hambur-balik cahaya laser, dan sensor baterai buah. Tanaman yang dikaji adalah kelapa sawit (*Elaeis guineensis*), khususnya varietas tenera yang dominan di Malaysia. Berdasarkan warna buah, dikenal dua tipe, yaitu nigrescens yang berubah dari hitam atau ungu gelap pada tahap mentah menjadi merah gelap pada tahap matang, serta virescens yang berubah dari hijau gelap menjadi jingga tua.

Mekanisme setiap teknik memakai sifat berbeda dari tandan. Spektroskopi inframerah, NIR, dan SWIR mengukur pantulan pada panjang gelombang tertentu untuk mendeteksi klorofil, karotenoid, air, dan minyak, lalu memakai kemometrik seperti regresi *partial least square*, analisis komponen utama, atau jaringan saraf tiruan. Visi komputer dan pengolahan citra digital mengekstraksi ciri warna dari citra RGB, mengubahnya ke ruang L*a*b atau HSI, lalu mengklasifikasikan dengan CNN, ANN, atau SVM. Pencitraan hiperspektral menggabungkan spektroskopi dan pencitraan pada ratusan pita sempit. Hambur-balik laser memakai kamera CCD untuk menangkap citra hamburan cahaya. Sensor baterai buah memasukkan dua elektrode ke buah dan mengukur tegangan yang timbul dari reaksi redoks.

Angka hasil berikut diambil dari kajian primer yang ditinjau dan dihitung dengan metrik masing-masing, karena tinjauan ini tidak menghasilkan data baru. Visi komputer melaporkan akurasi 96% pada data latih dan 97% pada data validasi, dengan AlexNet mencapai 100% pada empat kelas kematangan. Pengolahan citra digital melaporkan akurasi 89% untuk model L*a*b berbanding 66% untuk model RGB, serta 94% untuk model histogram warna dengan ANN. Pencitraan hiperspektral melaporkan koefisien determinasi 99,7% untuk kandungan minyak dan 99,5% untuk asam lemak bebas, dengan laju estimasi kematangan 97,92%. Hambur-balik laser melaporkan koefisien determinasi lebih dari 0,8 dan akurasi klasifikasi rata-rata 85%. Sensor baterai buah menghasilkan tegangan rata-rata 20–30 mV untuk buah matang dan 13 mV untuk buah mentah.

Penulis menyatakan sejumlah batasan. Spektroskopi memerlukan peralatan laboratorium, prosedur pengukuran khusus, dan tenaga ahli; modelnya bersifat lokal untuk kebun tertentu dan hasilnya terganggu oleh cahaya sekitar. Pengolahan citra digital memerlukan pencahayaan khusus dan peralatan yang sulit dipakai di lapangan. Visi komputer memerlukan waktu untuk memilih arsitektur yang tepat dan dataset besar, tetapi tidak memerlukan pencahayaan khusus karena model dilatih pada berbagai kondisi. Pencitraan hiperspektral dan hambur-balik laser memerlukan perlengkapan khusus serta bilik dengan pencahayaan seragam, sehingga tidak cocok untuk perangkat genggam. Sensor baterai hanya dapat dipakai setelah tandan dipanen, bukan saat masih di pohon. Penulis menyimpulkan bahwa visi komputer paling layak untuk klasifikasi kematangan langsung di lapangan dan dapat dijalankan pada telepon seluler atau komputer papan tunggal.

