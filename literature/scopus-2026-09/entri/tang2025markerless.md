# Markerless Feature-Registration-Based Image Processing Framework for Oil Palm Fresh Fruit Bunch Robotic Harvester

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tang2025markerless` |
| Judul asli | Markerless Feature-Registration-Based Image Processing Framework for Oil Palm Fresh Fruit Bunch Robotic Harvester |
| Penulis | Tang, Tiong Yew; Ho, Chian C.; Nadarajan, Geetha |
| Tahun | 2025 |
| Venue | Proceedings of SPIE the International Society for Optical Engineering |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [tang2025markerless.pdf](../pdf/tang2025markerless.pdf)
- DOI resmi: https://doi.org/10.1117/12.3057866

## Gambaran Umum

Kajian ini berangkat dari kebutuhan mekanisasi panen tandan buah segar (TBS) kelapa sawit di Malaysia. Industri perkebunan di sana menghadapi tantangan pekerja, termasuk gangguan muskuloskeletal akibat kerja. Penulis mengusulkan pengolahan citra untuk robot pemanen. Robot harus mengenali kategori kematangan TBS, lalu memperkirakan pose 6D buah agar dapat didekati dan dipanen. Pendekatan yang dipakai adalah *markerless* tanpa penanda, karena penanda sulit dipasang di area perkebunan yang luas.

Data yang digunakan adalah dataset TBS kelapa sawit publik. Dataset ini memuat enam kategori tingkat kematangan. Total terdapat 4160 foto beranotasi dan 14559 sampel berlabel. Citra yang dipakai adalah citra RGB dari kamera di platform robot pemanen. Penulis menerapkan gangguan *view obstruction* pada data uji, dengan persentase 0% hingga 80%, untuk meniru kondisi lapangan yang tertutup daun, cabang, atau kotoran. Teks tidak menyebut pembagian data latih dan data uji. Pelatihan model CNN dilakukan selama 200 *epoch* dengan GPU Nvidia Quadro P5000 dan membutuhkan sekitar 8 jam.

Metode terdiri dari tiga tahap. Tahap pertama adalah klasifikasi kategori TBS dengan CNN. Tahap kedua membangun model 3D TBS menggunakan RGB dengan Spectacular AI atau COLMAP, dilanjutkan NeRF dan Blender. Tahap ketiga adalah estimasi pose 6D dengan *coarse estimator* dan *iterative refiner*, yang kemudian dipakai untuk *visual servoing* robot. Hasil kuantitatif yang dilaporkan terbatas pada klasifikasi. Bobot F1 tertinggi adalah 0,2226 pada 0% obstruksi, dan terendah 0,0438 pada 80% obstruksi. Penurunan belum signifikan hingga 70% obstruksi. Kategori *ripe* memperoleh F1 tertinggi, yaitu 0,44989, pada obstruksi 20%. Penulis mengaitkan hasil ini dengan jumlah sampel latih kategori tersebut yang paling banyak. Penulis tidak melaporkan angka akurasi pose 6D.

Penulis menyatakan beberapa batasan. Dataset publik dinilai tidak menyediakan sampel latih yang cukup. Akibatnya, kinerja klasifikasi buruk pada kategori dengan sampel sedikit. Implementasi pemrosesan waktu nyata di robot belum dilakukan. Alasannya, komputasi membutuhkan laptop GPU kelas tinggi, setidaknya RTX 4080Ti atau yang lebih baik, dan pendanaan penelitian terbatas. Untuk penelitian lanjutan, penulis berencana mengumpulkan dan melabeli lebih banyak sampel TBS. Penulis juga akan menguji mekanisasi robot pemanen di lapangan.
