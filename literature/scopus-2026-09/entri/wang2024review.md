# A Review of Perception Technologies for Berry Fruit-Picking Robots: Advantages, Disadvantages, Challenges, and Prospects

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024review` |
| Judul asli | A Review of Perception Technologies for Berry Fruit-Picking Robots: Advantages, Disadvantages, Challenges, and Prospects |
| Penulis | Wang, Chenglin; Pan, Weiyu; Zou, Tianlong; Li, Chunjiang; Han, Qiyu; Wang, Haoming; Yang, Jing; Zou, Xiangjun |
| Tahun | 2024 |
| Venue | Agriculture Switzerland |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [wang2024review.pdf](../pdf/wang2024review.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture14081346

## Gambaran Umum

Tinjauan ini membahas kesulitan memanen buah beri. Buah beri berkulit tipis, berdaging lunak, dan mudah rusak, sehingga pemanenan manual mahal dan berisiko merusak buah. Mesin pemanen konvensional yang bekerja dengan getaran atau cengkeraman mekanis meningkatkan kecepatan, tetapi masih menimbulkan kerusakan, buah tertinggal, dan salah panen. Penulis mengajukan robot pemanen yang dilengkapi teknologi persepsi sebagai alternatif, lalu meninjau prinsip kerja, mekanisme mencengkeram, dan rancangan struktur robot tersebut.

Data tinjauan berasal dari literatur, bukan percobaan baru; pernyataan ketersediaan data menyatakan tidak ada data baru yang dibuat atau dianalisis. Penulis mencari artikel dalam lima basis data, yaitu Web of Science, Google Scholar, Wiley Online Library, IEEE Xplore, dan ScienceDirect, dengan kata kunci yang mencakup robot pemanen buah beri, teknologi persepsi, sensor, pembelajaran mesin, dan pertanian presisi. Pencarian awal di Web of Science menghasilkan sekitar 500 artikel; setelah pengecualian kajian buah non-beri tersisa lebih dari 200 artikel, dan sekitar 200 artikel akhirnya dikeluarkan karena tidak memenuhi kriteria. Buah yang dibahas mencakup raspberry, anggur, blueberry, kiwi, dan stroberi, dengan tomat dan ceri sebagai studi perbandingan.

Mekanisme pemanenan terdiri atas pendekatan, kontak, penambahan gaya cengkeram, penguncian objek, pengangkatan, pelepasan, dan pemantauan cengkeraman. Cara mencengkeram dibedakan menjadi mencengkeram tangkai, mengisap buah, dan mencengkeram buah langsung. Persepsi dibagi menjadi empat teknologi, yaitu persepsi visual, persepsi taktil, pengukuran jarak, dan sensor sakelar. Persepsi visual memakai klasifikasi citra, deteksi objek, segmentasi semantik, dan segmentasi instance; segmentasi instance memisahkan tiap objek dengan topeng tingkat piksel. Persepsi taktil memakai sensor piezoresistif, kapasitif, piezoelektrik, dan triboelektrik untuk mengukur tekanan, kekerasan, tekstur, dan slip. Pengukuran jarak memakai sensor inframerah, ultrasonik, LiDAR, kamera stereo, dan kamera kedalaman. Sensor sakelar memakai sakelar fotoelektrik, proksimiti, dan tekanan. Asosiasi lintas pandang atau penghitungan buah unik lintas sudut pandang tidak dinyatakan.

Angka hasil yang dikutip berasal dari kajian primer yang ditinjau dan dihitung dengan metrik masing-masing, karena tinjauan ini tidak menghasilkan data baru. Deteksi objek tomat ceri dengan YOLOv3 yang ditingkatkan melaporkan presisi 94,29%; jaringan YOLOv5 untuk blueberry meningkatkan akurasi 2,4% dibandingkan YOLOv5 awal. Segmentasi semantik tomat melaporkan intersection over union 82,5% dan akurasi piksel 89,79%, sedangkan penilaian kematangan stroberi melaporkan akurasi 93,7%. Segmentasi anggur melaporkan akurasi 41,7% untuk kelas tepi. Tabel sensor taktil mencantumkan batas deteksi, sensitivitas, rentang, waktu respons, dan stabilitas, misalnya sensor graphene/PDMS berpola dengan batas deteksi 5 Pa, sensitivitas 1,2 kPa⁻¹, dan rentang 0–25 kPa.

Penulis mencatat sejumlah batasan. Akurasi terganggu oleh pencahayaan, oklusi, angin, dan latar belakang, yang menyebabkan kelalaian dan deteksi salah. Adaptabilitas dibatasi oleh perubahan cuaca, kelembapan, suhu, dan tata letak tanaman. Daya tahan dibatasi oleh aus, korosi, debu, dan getaran. Pemrosesan data menghadapi derau, bias internal, dan kebutuhan integrasi banyak sensor. Biaya sensor berkualitas tinggi masih mahal. Penulis menyimpulkan bahwa segmentasi semantik lebih cocok untuk budidaya rumah kaca, sedangkan sensor taktil piezoresistif dan LiDAR lebih sesuai untuk lahan terbuka.

