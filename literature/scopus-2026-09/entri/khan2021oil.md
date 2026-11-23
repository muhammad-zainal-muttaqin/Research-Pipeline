# Oil palm and machine learning: Reviewing one decade of ideas, innovations, applications, and gaps

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `khan2021oil` |
| Judul asli | Oil palm and machine learning: Reviewing one decade of ideas, innovations, applications, and gaps |
| Penulis | Khan, Nuzhat; Kamaruddin, Mohamad Anuar; Sheikh, Usman Ullah; Yusup, Yusri; Bakht, Muhammad Paend |
| Tahun | 2021 |
| Venue | Agriculture Switzerland |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [khan2021oil.pdf](../pdf/khan2021oil.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture11090832

## Gambaran Umum

Tinjauan sistematis ini merangkum aplikasi pembelajaran mesin pada perkebunan kelapa sawit selama dekade 2011–2020. Penulis mengemukakan tiga tantangan utama yang mendorong penggunaan teknologi, yaitu menaikkan hasil rata-rata global 3,5 ton per hektar menuju potensi penuh 11–18 ton per hektar, mengubah arsitektur pohon menjadi rendah tenaga kerja dan tinggi mekanisasi, serta menyesuaikan komposisi minyak dengan kebutuhan industri. Analisis celah hasil dipandang sulit dengan metode konvensional karena faktor penurun hasil saling bergantung, seperti kelembapan tanah dan curah hujan, panjang hari dan radiasi matahari, frekuensi pemupukan, serta pertumbuhan tanaman. Pembelajaran mesin dipandang mampu mengintegrasikan data heterogen tersebut dan menghasilkan model prediktif maupun deskriptif.

Metode tinjauan mengikuti protokol sistematis hibrida kualitatif-kuantitatif dengan tujuh pertanyaan penelitian. Penelusuran memakai string ("machine learning" OR "deep learning" OR "artificial intelligence") AND ("oil palm" OR "Elaeis guineensis") pada Scopus, ScienceDirect, Springer Link, Web of Science, dan Google Scholar, menghasilkan 1.060 kajian awal. Penerapan tujuh kriteria eksklusi (antara lain bahasa selain Inggris, duplikasi, teks lengkap tidak tersedia, artikel tinjauan, serta terbit sebelum 2011 atau sesudah 2020) menyisakan 61 makalah untuk dianalisis mengikuti alur PRISMA. Makalah dibagi menjadi dua kelompok besar berdasarkan jenis analisis, yaitu klasifikasi sekitar 84% dan regresi sekitar 16%, dengan subkategori klasifikasi serbaguna, deteksi penyakit, pemantauan kanopi dengan UAV, prediksi atau estimasi, deteksi lahan dan pohon, serta analisis tandan buah segar.

Mekanisme yang dirangkum meliputi deteksi dan penghitungan pohon dari citra satelit atau UAV dengan SVM, CNN, Faster-CNN, dan DeepLabV3+, penilaian kematangan tandan buah segar melalui warna, fluoresensi merah-biru, sifat dielektrik, dan citra hiperspektral, serta deteksi penyakit busuk pangkal batang akibat Ganoderma boninense memakai SVM, RF, ANN, dan citra WorldView-3 atau QuickBird. Untuk prediksi, penulis mencatat penggunaan ANN, regresi linear, SVR, jaringan Bayesian, serta model simulasi PALMSIM dan ECOPALM guna memperkirakan hasil tandan buah segar, waktu panen, harga minyak sawit mentah, dan variasi musiman. Input yang dipakai mencakup ciri mahkota, pantulan spektral, NDVI, variabel meteorologis, warna tandan, kandungan flavonoid dan antosianin, serta komposisi hara daun.

Berikut temuan kuantitatif tinjauan beserta dasar hitungnya. Sekitar 33% kajian difokuskan pada klasifikasi buah, 30% pada pengamatan lahan dan pohon, dan masing-masing 7% pada deteksi penyakit, pemantauan kanopi dengan UAV, serta klasifikasi serbaguna. Berdasarkan frekuensi penggunaan, SVM merupakan algoritma paling banyak dipakai, diikuti ANN, RF, regresi, CART, dan CNN; untuk klasifikasi buah ANN paling sering, untuk deteksi penyakit SVM dan RF dominan, dan untuk prediksi ANN paling umum disusul regresi linear dan SVM. Secara geografis, Malaysia menyumbang sekitar 62% makalah dan Indonesia 18%, dengan kontribusi dari Britania Raya, Amerika Serikat, Australia, China, Thailand, dan Belanda. Sumber data yang disebut meliputi Google Earth Engine, QuickBird, dan WorldView-3, disamping data lapang yang dikumpulkan sendiri. Metrik evaluasi paling sering adalah overall accuracy, disusul classification accuracy, RMSE, dan F1-score; penulis menegaskan bahwa peringkat algoritma dihitung dari frekuensi pemakaian, bukan dari ketepatan.

Penulis menyatakan sejumlah batasan dan celah. Pembelajaran mesin masih kurang dimanfaatkan untuk analisis prediktif kelapa sawit dan prediksi hasil masih pada tahap awal. Keterbatasan data kuantitatif yang bebas diakses menjadi hambatan utama pertanian presisi, karena pengumpulan data lapang yang konsisten memakan waktu dan sulit dilakukan. Kematangan tandan buah segar mencakup empat tahap (mentah, kurang matang, matang, dan lewat matang) yang memiliki ciri yang mirip pada tahap berurutan sehingga sulit dibedakan dengan klasifikasi konvensional. Belum ada model yang membedakan kelapa sawit dari tanaman serupa seperti kurma dan kelapa, sehingga klasifikasi citra berskala luas berisiko keliru. Tinjauan ini juga mengakui bahwa mesin pencari sulit membedakan "oil palm" dan "palm oil", algoritma pembelajaran mendalam dan pembelajaran mesin tidak dipisahkan secara eksplisit, beberapa kajian tidak menyebut metrik evaluasi atau sama sekali tidak melakukan evaluasi, dan perbandingan ketepatan antaralgoritma tidak dilakukan karena perbedaan tujuan dan data.
