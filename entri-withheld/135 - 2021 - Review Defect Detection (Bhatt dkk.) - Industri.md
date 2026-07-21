# 135 - A Review of Deep Learning-Based Approaches for Attention-Guided Defect Detection in Smart Manufacturing

## Metadata Ringkas

| Atribut | Nilai |
| --- | --- |
| Kunci BibTeX | `jha2023defectreview` |
| Judul asli | A Review of Deep Learning-Based Approaches for Attention-Guided Defect Detection in Smart Manufacturing |
| Penulis | Bhatt, Prahar M.; Malhan, Rishi K.; Rajendran, Pradeep; Shah, Brual C.; Thakar, Shantanu; Yoon, Yeo Jung; Gupta, Satyandra K. |
| Tahun | 2021 |
| Venue | Journal of Intelligent Manufacturing |
| Tema | Industri |

## Tautan Akses

- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20Review%20of%20Deep%20Learning-Based%20Approaches%20for%20Attention-Guided%20Defect%20Detection%20in%20Smart%20Manufacturing
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20Review%20of%20Deep%20Learning-Based%20Approaches%20for%20Attention-Guided%20Defect%20Detection%20in%20Smart%20Manufacturing&sort=relevance

## Gambaran Umum
Makalah oleh Bhatt dkk. (2021) ini merupakan studi survei komprehensif yang mengulas penerapan pembelajaran mendalam (*deep learning*) untuk deteksi cacat permukaan berbasis citra dalam manufaktur cerdas (*smart manufacturing*). Fokus utama ulasan ini adalah mengklasifikasikan berbagai penelitian deteksi cacat ke dalam taksonomi terstruktur, guna mempermudah pemahaman mengenai perkembangan metodologi serta mengidentifikasi kesenjangan teknologi antara penelitian akademis dan kebutuhan praktis industri.

Melalui analisis ratusan publikasi, penulis merangkum tren perkembangan algoritma dari klasifikasi citra sederhana hingga lokalisasi tingkat piksel (segmentasi semantik) serta deteksi anomali nir-diawasi (*unsupervised anomaly detection*). Hasil utama survei ini adalah perumusan taksonomi tiga dimensi (konteks deteksi, teknik pembelajaran, dan metode lokalisasi/klasifikasi) serta pemetaan tantangan kritis seperti ketidakseimbangan data (*data imbalance*), variabilitas skala cacat, performa waktu nyata (*real-time*), dan generalisasi model pada permukaan bertekstur kompleks.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum publikasi survei ini, penerapan pembelajaran mendalam dalam inspeksi cacat industri berkembang pesat namun terfragmentasi. Peneliti umumnya mengembangkan model ad-hoc untuk satu jenis cacat permukaan saja, seperti cacat lembaran baja atau papan sirkuit cetak (*printed circuit board* atau PCB). Ketiadaan taksonomi terpadu menyulitkan praktisi menentukan arsitektur yang optimal untuk karakteristik fisik permukaan material tertentu.

Kekurangan dari tinjauan pustaka terdahulu adalah kurangnya penekanan pada aspek kepraktisan industri. Sebagian besar survei berfokus pada akurasi teoritis di dataset publik tanpa mempertimbangkan batasan perangkat keras, performa waktu nyata (*real-time inline inspection*), serta kendala kelangkaan data cacat di dunia nyata. Di lantai produksi, cacat adalah kejadian langka sehingga pengumpulan ribuan citra cacat terlabeli untuk pelatihan terawasi (*supervised learning*) sangat sulit dan mahal. Hambatan ini membatasi adopsi kecerdasan buatan (*artificial intelligence*) secara luas pada manufaktur cerdas, sehingga sintesis literatur mengenai solusi kelangkaan data dan taksonomi yang terstruktur menjadi krusial.

## Ide Utama
Ide utama makalah ini adalah membangun taksonomi tiga dimensi untuk memetakan lanskap teknologi deteksi cacat permukaan berbasis pembelajaran mendalam secara sistematis. Kerangka taksonomi ini memproses ratusan publikasi ilmiah terkait inspeksi visual industri berdasarkan tiga variabel klasifikasi utama guna memetakan hubungan antara karakteristik fisik cacat di industri dengan arsitektur jaringan saraf tiruan (*artificial neural network*) yang optimal.

Secara mekanis, taksonomi ini membagi literatur ke dalam tiga dimensi utama:
1. Konteks Deteksi Cacat (*Defect Detection Context*): Menganalisis sifat material (homogen/spekular vs bertekstur) dan kondisi lingkungan (variasi cahaya, derau).
2. Teknik Pembelajaran (*Learning Techniques*): Mengklasifikasikan metode berdasarkan ketersediaan label data, mulai dari pembelajaran terawasi (*supervised*), nir-terawasi (*unsupervised*), semi-terawasi (*semi-supervised*), hingga pembelajaran transfer (*transfer learning*).
3. Metode Lokalisasi/Klasifikasi (*Defect Localization and Classification Method*): Memetakan resolusi spasial dari luaran model, mulai dari klasifikasi global tingkat citra, lokalisasi kotak pembatas (*bounding box*), hingga segmentasi tingkat piksel.

## Cara Kerja Langkah demi Langkah
Bagian ini menguraikan metodologi survei dan struktur taksonomi tiga dimensi yang dirumuskan oleh Bhatt dkk. untuk menganalisis literatur deteksi cacat visual.

```
           TAKSONOMI SURVEI DETEKSI CACAT PERMUKAAN (BHATT DKK.)
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
 ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
 │   KONTEKS    │           │    TEKNIK    │           │ METODE LOKAL/│
 │   DETEKSI    │           │ PEMBELAJARAN │           │  KLASIFIKASI │
 └──────┬───────┘           └──────┬───────┘           └──────┬───────┘
        │                          │                          │
  ┌─────┴────────┐           ┌─────┴────────┐           ┌─────┴────────┐
  ▼              ▼           ▼              ▼           ▼              ▼
┌─────────┐   ┌─────────┐  ┌─────────┐   ┌─────────┐  ┌─────────┐   ┌─────────┐
│Tekstur  │   │Kondisi  │  │Terawasi │   │Nir-     │  │Klasifi- │   │Lokali-  │
│Permukaan│   │Lingkungan│  │(Super-  │   │awasi    │  │kasi     │   │sasi     │
│(Logam/  │   │(Cahaya,  │  │vised)   │   │(Unsuper-│  │Citra    │   │(Deteksi/│
│PCB/Kain)│   │Derau)    │  │         │   │vised)   │  │(Global) │   │Segmen)  │
└─────────┘   └─────────┘  └─────────┘   └─────────┘  └─────────┘   └─────────┘
```

### Metodologi Pengumpulan dan Penyaringan Literatur
Penulis mengumpulkan publikasi ilmiah dari basis data global seperti IEEE Xplore, ScienceDirect, dan SpringerLink. Penyaringan dibatasi pada penerapan metode pembelajaran mendalam untuk inspeksi visual otomatis pada manufaktur. Artikel terpilih dipilah menggunakan kriteria eksklusi untuk membuang makalah tanpa kontribusi arsitektur yang jelas atau tanpa validasi eksperimental pada dataset riil atau dataset tolok ukur (*benchmark dataset*).

### Dimensi 1: Konteks Deteksi Cacat
Dimensi ini membagi literatur berdasarkan jenis permukaan yang diperiksa:
- **Permukaan Homogen atau Spekular:** Material seperti kaca dan cermin memiliki reflektivitas tinggi. Deteksi cacat di sini sangat dipengaruhi oleh sudut pencahayaan eksternal untuk memunculkan kontras retakan mikro.
- **Permukaan Bertekstur dan Non-homogen:** Material seperti lembaran baja, kayu, tekstil, dan PCB memiliki pola visual latar belakang yang kompleks. Cacat pada kelompok ini sering kali berukuran sangat kecil dan menyatu dengan pola tekstur alami material tersebut. Sebagai contoh, pada pelat baja dengan area inspeksi 200×200 mm, cacat berupa *pitting* (lubang mikro) berukuran kurang dari 1 mm² sangat mudah tersamarkan oleh derau tekstur pelat baja jika model tidak dilengkapi ekstraksi fitur multi-skala.

### Dimensi 2: Teknik Pembelajaran
Dimensi ini mengelompokkan literatur berdasarkan strategi pelatihan model:
- **Pembelajaran Terawasi (*Supervised Learning*):** Model dilatih menggunakan citra yang dianotasi secara manual oleh operator ahli. Metode ini memberikan akurasi tertinggi tetapi membutuhkan ribuan sampel berlabel.
- **Pembelajaran Nir-terawasi (*Unsupervised Learning*):** Model dilatih hanya menggunakan data normal untuk merekonstruksi pola permukaan menggunakan arsitektur *Autoencoder* atau GAN. Selisih rekonstruksi (*reconstruction error*) antara citra asli dan hasil rekonstruksi digunakan untuk mengidentifikasi letak anomali tanpa membutuhkan data cacat saat pelatihan.
- **Pembelajaran Semi-terawasi (*Semi-supervised Learning*):** Menggabungkan sedikit data berlabel dengan banyak data tanpa label untuk mengurangi biaya anotasi manual.
- **Pembelajaran Transfer (*Transfer Learning*):** Memanfaatkan bobot pra-latih (*pre-trained weights*) dari model yang telah dilatih pada dataset raksasa seperti ImageNet untuk melakukan penyesuaian (*fine-tuning*) secara cepat dengan sampel cacat yang sangat terbatas (kurang dari 100 citra per kelas).

### Dimensi 3: Metode Lokalisasi dan Klasifikasi Cacat
Dimensi ini mengklasifikasikan literatur berdasarkan kedalaman informasi spasial luaran algoritma:
- **Klasifikasi Citra (*Image-level Classification*):** Mengeluarkan prediksi global (cacat atau normal) tanpa memberikan lokasi spesifik.
- **Deteksi Objek (*Object Detection*):** Memprediksi lokasi cacat dengan membungkusnya dalam kotak pembatas (*bounding box*) koordinat $(x, y, w, h)$ beserta probabilitas keyakinan (*confidence score*).
- **Segmentasi Semantik (*Semantic Segmentation*):** Melakukan klasifikasi tingkat piksel untuk mendelineasi batas fisik cacat secara presisi, sangat cocok untuk cacat berbentuk tidak teratur.
- **Pendeteksian Anomali (*Anomaly Detection*):** Menemukan deviasi dari pola normal tanpa mengategorikan tipe cacat secara spesifik.

### Pemetaan Tantangan Operasional Industri
Bhatt dkk. menyintesis empat tantangan utama dalam implementasi industri:
1. **Ketidakseimbangan Kelas (*Class Imbalance*):** Pabrik modern dengan kontrol kualitas yang baik menghasilkan cacat di bawah 0,5% dari total produksi. Algoritma harus dimodifikasi agar tidak bias terhadap kelas normal.
2. **Keterbatasan Data Latih (*Data Scarcity*):** Sulitnya mengumpulkan sampel cacat dalam jumlah besar untuk melatih model terawasi.
3. **Variabilitas Kondisi Operasional:** Getaran ban berjalan (*conveyor belt*), perubahan intensitas lampu pabrik, dan debu lingkungan mengubah distribusi visual citra masukan secara dinamis.
4. **Batasan Waktu Nyata (*Real-Time Constraints*):** Kecepatan ban berjalan yang tinggi menuntut waktu pemrosesan inferensi di bawah 30 milidetik per bingkai citra pada resolusi tinggi.

## Eksperimen dan Hasil
Sebagai survei, penulis tidak melakukan eksperimen laboratorium mandiri melainkan melakukan analisis komparatif meta-data terhadap kinerja berbagai arsitektur pembelajaran mendalam di berbagai dataset tolok ukur populer.

Bhatt dkk. menyajikan perbandingan kinerja arsitektur utama pada beberapa dataset standar seperti DAGM (cacat tekstur buatan), NEU-CLS/NEU-DET (cacat permukaan baja), dan KolektorSDD (cacat retakan pada komutator). Berdasarkan kompilasi data survei tersebut:
1. Pada dataset **NEU-DET** (6 jenis cacat permukaan baja), model berbasis deteksi objek seperti Faster R-CNN mencapai rata-rata presisi mAP (*mean Average Precision*) sekitar 75,0% hingga 82,0% tetapi dengan kecepatan inferensi rendah (di bawah 15 FPS). Sebaliknya, model satu-tahap (*single-stage detector*) seperti YOLOv3 dan SSD mampu mencapai kecepatan inferensi di atas 45 FPS (memenuhi batas waktu nyata industri) dengan mAP berkisar antara 68,0% hingga 76,0%.
2. Pada dataset **KolektorSDD**, pendekatan segmentasi semantik berbasis U-Net terbukti sangat efektif untuk mendeteksi cacat retakan mikro yang sangat tipis (lebar hanya beberapa piksel), dengan nilai sensitivitas (*recall*) mencapai lebih dari 95,0%. Namun, biaya anotasi piksel untuk melatih model segmentasi ini tercatat 10 kali lipat lebih tinggi dibandingkan anotasi kotak pembatas untuk deteksi objek.
3. Pada skenario nir-terawasi menggunakan dataset **DAGM**, model berbasis *Deep Autoencoder* (DAE) dan GAN menunjukkan sensitivitas deteksi anomali sebesar 85,0% hingga 90,0%. Meskipun bebas dari kebutuhan label cacat, model nir-terawasi ini memiliki tingkat alarm palsu (*false positive rate*) yang relatif tinggi (sekitar 5,0% hingga 8,0%) akibat sensitivitas berlebih terhadap variasi pencahayaan latar belakang.

## Kelebihan dan Keterbatasan
**Kelebihan:**
Survei ini memberikan panduan terstruktur bagi peneliti dan praktisi untuk memahami cara memilih model pembelajaran mendalam berdasarkan karakteristik material fisik. Taksonomi tiga dimensi yang dirumuskan membantu menyederhanakan klasifikasi literatur yang luas. Selain itu, ulasan ini secara jujur menyoroti kesenjangan antara dunia akademis dan industri, terutama terkait kendala ketersediaan data dan performa komputasi waktu nyata di lini produksi sesungguhnya.

**Keterbatasan:**
Dari sisi rekayasa, salah satu keterbatasan survei ini adalah minimnya panduan praktis mengenai integrasi sistem visi komputer (*computer vision system*) dengan sistem otomasi pabrik seperti PLC (*Programmable Logic Controller*) atau protokol komunikasi industri. Survei ini murni membahas aspek algoritma tingkat perangkat lunak tanpa mengulas desain pencahayaan (*lighting design*) and pemilihan lensa kamera yang sebenarnya menentukan keberhasilan inspeksi visual industri sebesar 50%. Secara konseptual, karena diterbitkan pada tahun 2021, survei ini belum sempat mengulas perkembangan arsitektur *Vision Transformer* (ViT) skala besar dan model segmentasi universal seperti SAM (*Segment Anything Model*) yang saat ini mendominasi riset deteksi anomali modern.

## Kaitan dengan Bab Lain
Tinjauan pustaka ini bertindak sebagai payung teoretis dan taksonomik yang menaungi implementasi praktis di bidang industri yang dibahas pada bab-bab lainnya.

Secara khusus, taksonomi yang dirumuskan Bhatt dkk. mengenai deteksi cacat pada material bertekstur non-homogen sangat relevan dengan metode [133 - 2023 - EFC-YOLO (Steel Strip Defects) - Industri](./133%20-%202023%20-%20EFC-YOLO%20%28Steel%20Strip%20Defects%29%20-%20Industri.md). EFC-YOLO menerapkan rekomendasi penting dari survei Bhatt dkk., yaitu penggabungan fitur multi-skala dan mekanisme perhatian (*attention mechanism*) untuk mengatasi variabilitas ukuran cacat pada permukaan baja (dataset NEU).

Sementara itu, tantangan komputasi waktu nyata (*real-time constraints*) dan kompleksitas latar belakang sirkuit elektronik dibahas secara mendalam oleh [134 - 2024 - PCB-YOLO (PCB Defects) - Industri](./134%20-%202024%20-%20PCB-YOLO%20%28PCB%20Defects%29%20-%20Industri.md). PCB-YOLO mengadopsi mekanisme *Coordinate Attention* (CA) untuk memfokuskan ekstraksi fitur pada area sirkuit yang rawan cacat, sejalan dengan taksonomi *attention-guided* yang menjadi sorotan utama dalam ulasan ini.

Terakhir, perluasan domain inspeksi ke pemantauan keselamatan personel di lingkungan manufaktur cerdas diwakili oleh [136 - 2021 - Safety Helmet Detection (Improved YOLOv5) - Industri](./136%20-%202021%20-%20Safety%20Helmet%20Detection%20%28Improved%20YOLOv5%29%20-%20Industri.md). Bab tersebut mengilustrasikan bagaimana modifikasi model YOLOv5 disesuaikan untuk mendeteksi penggunaan alat pelindung diri secara waktu nyata, bentuk aplikasi deteksi objek yang memenuhi batasan operasional industri yang dipetakan oleh Bhatt dkk.

## Poin untuk Sitasi

- **Kunci BibTeX:** `jha2023defectreview`
- **Ringkasan untuk Sitasi:** Bhatt dkk. (2021) menyajikan survei komprehensif mengenai penerapan pembelajaran mendalam untuk deteksi cacat permukaan dalam manufaktur cerdas dengan merumuskan taksonomi tiga dimensi (konteks deteksi, teknik pembelajaran, dan metode lokalisasi). Tinjauan ini memetakan tantangan utama seperti ketidakseimbangan kelas, keterbatasan data latih, dan kebutuhan inferensi waktu nyata di industri.
- **Catatan Verifikasi:** Angka performa mAP untuk Faster R-CNN (75,0%--82,0%) dan YOLOv3 (68,0%--76,0%) pada dataset NEU-DET yang dicantumkan dalam bab ini merupakan hasil kompilasi dari berbagai literatur sekunder yang disintesis oleh penulis survei, sehingga perlu diverifikasi langsung ke naskah asli masing-masing model untuk kepastian absolut.
