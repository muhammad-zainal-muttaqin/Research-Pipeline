# Artificial intelligence for oil palm tree management using deep structured learning: A systematic review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `farhan2026artificial` |
| Judul asli | Artificial intelligence for oil palm tree management using deep structured learning: A systematic review |
| Penulis | Farhan, Mohammad; Hamad, Qusay Shihab; Akhtar, Mohammad N.; Rajendran, R.; Danish, Mohammed; Bakar, Elmi Abu |
| Tahun | 2026 |
| Venue | Al Qadisiyah Journal for Engineering Sciences |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [farhan2026artificial.pdf](../pdf/farhan2026artificial.pdf)
- DOI resmi: https://doi.org/10.30772/qjes.2026.165663.1755

## Gambaran Umum

Tinjauan sistematik ini mengkaji penerapan pembelajaran mendalam, khususnya
jaringan saraf konvolusional, untuk deteksi dan pencacahan pohon kelapa sawit.
Perkebunan sawit mengelola jutaan pohon di lahan luas dengan nilai ekonomi
sekitar 65 miliar dolar per tahun. Penghitungan manual yang masih lazim
bersifat padat karya dan memiliki tingkat galat 15–25%, yang merambat ke
prediksi hasil, alokasi sumber daya, dan pelaporan keberlanjutan. Tekanan
tambahan datang dari perubahan iklim, kekurangan tenaga kerja, serta
peraturan seperti European Union Deforestation Regulation yang berlaku pada
2024. Penulis menempatkan otomatisasi sebagai kebutuhan untuk pengelolaan
perkebunan yang dapat diskalakan.

Bahan tinjauan berupa publikasi tahun 2016–2025 tentang pengenalan kelapa
sawit memakai pembelajaran mendalam dengan pengukuran kuantitatif. Pencarian
dilakukan pada Scopus, Web of Science, IEEE Xplore, dan Google Scholar dengan
kueri ("oil AND palm") AND ("artificial AND intelligence" OR "machine AND
learning" OR "deep AND learning" OR convolutional neural network). Penyaringan
tiga tahap mencakup pencarian otomatis, pemeriksaan judul dan abstrak, lalu
pembacaan teks lengkap. Kriteria inklusi mensyaratkan deteksi, pencacahan,
atau klasifikasi pohon sawit dengan pembelajaran mesin atau mendalam, data
penginderaan jauh dari UAV, satelit, atau platform udara, metrik kuantitatif,
serta publikasi tinjauan sejawat setelah 2016. Kajian tentang ekonomi atau
kebijakan, metode pencitraan konvensional tanpa pembelajaran mesin, dan
kajian tanpa rincian metode dikeluarkan. Penulis mengekstraksi arsitektur,
karakteristik data, metrik kinerja, serta batasan komputasi, lalu menganalisis
47 kumpulan data.

Mekanisme deteksi bertumpu pada CNN yang mengekstraksi ciri langsung dari
citra tanpa ekstraksi ciri manual seperti SIFT atau LBP, dengan varian R-CNN,
deret YOLO, serta pendekatan transformer dan model fondasi. Penulis
melaporkan sejumlah angka dengan metrik akurasi, presisi, recall, F1, dan mAP.
Arsitektur CNN mutakhir dengan kerangka YOLO mencapai akurasi deteksi lebih
dari 95% pada pohon dewasa, tetapi turun menjadi 87,2% berbanding 96,8% mAP
pada pohon muda. Generalisasi lintas wilayah menyebabkan penurunan 21,9 poin
persentase, yaitu dari 98,3% pada validasi data Malaysia menjadi 76,4% pada
uji data Indonesia dengan ResNet-50. Kebutuhan komputasi berkisar 450–650
milidetik per citra dengan kecepatan 1,5–2,2 FPS untuk Faster R-CNN, sedangkan
YOLOv8-nano mencapai 8–12 FPS dengan pengorbanan 4–7 poin mAP. Model tepi
Tiny-LiteNet pada Raspberry Pi 5 mencatat akurasi 98,6%, ukuran 1,2 MB, dan
waktu inferensi 80 milidetik; YOLOv8 nano pada Raspberry Pi 4B dengan Intel
NCS1 mencapai 97% mAP@0,5 pada 2,4 FPS dan daya puncak 1,6 W. Analisis data
menunjukkan bias geografis 68% Malaysia, 23% Indonesia, dan 9% negara lain
dari 22 negara, dengan komposisi 72% pohon dewasa, 11% muda, dan 17% remaja;
hanya 8% kumpulan data yang tersedia publik. Penulis menyimpulkan pembelajaran
mendalam meningkatkan pengelolaan sawit 15–20% dibanding metode konvensional.

Penulis mengemukakan sejumlah batasan dan hambatan. Ketersediaan data yang
terbatas dan ketiadaan metrik evaluasi yang seragam menyulitkan perbandingan
objektif dan adopsi luas. Model belum tergeneralisasi dengan baik lintas
kondisi perkebunan, musim, dan umur pohon; pada lahan petani kecil dengan
jarak tanam tidak teratur terjadi penurunan akurasi 18–28%. Faktor lingkungan
tropis menambah galat, yaitu tutupan awan 65–72% pada musim hujan, kabut
asal kebakaran menurunkan akurasi 12–18%, dan perubahan sudut matahari
menghasilkan galat 15–22% pada citra pagi atau sore bagi model yang dilatih
pada citra siang. Anotasi manual memakan 15–25 menit per citra; untuk 5.000
citra diperlukan 1.250–2.083 jam kerja dengan biaya 18.750–52.075 dolar.
Kinerja menurun 8–14% dalam 36 bulan tanpa pelatihan ulang, sehingga
diperlukan pembaruan tiap 6–12 bulan, sementara perangkat keras lapang
memiliki tingkat kegagalan 12–18% per tahun. Dari sisi operasional, hanya
9% pekerja perkebunan yang memahami pembelajaran mesin, dan audit RSPO
menemukan sistem otomatis memenuhi toleransi ±5% hanya pada 67% skenario uji.
Penulis juga mencatat keterbatasan integrasi data, kendala biaya bagi
perkebunan skala 50–500 hektare, serta ketidakpastian regulasi data hasil AI.


