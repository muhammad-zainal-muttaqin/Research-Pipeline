# A review of key techniques of vision-based control for harvesting robot

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2016review` |
| Judul asli | A review of key techniques of vision-based control for harvesting robot |
| Penulis | Zhao, Yuanshen; Gong, Liang; Huang, Yixiang; Liu, Chengliang |
| Tahun | 2016 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [zhao2016review.pdf](../pdf/zhao2016review.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2016.06.022

## Gambaran Umum

Kajian ini adalah tinjauan pustaka tentang teknik kendali berbasis citra untuk robot pemanen buah. Penulis menyatakan bahwa rendahnya tingkat keberhasilan pengenalan buah dan tidak efisiennya koordinasi tangan-mata membatasi kinerja robot pemanen. Akibatnya, robot pemanen belum mampu bersaing dengan pemanenan manual. Tinjauan ini bertujuan memberi gambaran terkini tentang metode dalam literatur untuk dua persoalan utama, yaitu pengenalan buah sasaran dan kendali koordinasi tangan-mata.

Cakupan tinjauan meliputi buah dan sayuran yang tumbuh di kanopi tanaman. Penulis membahas lima skema pencitraan, yaitu kamera monokular, *stereovision* binokular, sensor aktif laser, pencitraan termal, dan pencitraan spektral. Untuk pengenalan buah, penulis membahas pendekatan fitur tunggal, penggabungan beberapa fitur, dan pendekatan pengenalan pola. Penulis juga meninjau koordinasi tangan-mata yang dibagi menjadi kendali visual *open-loop* dan *visual servo*. Bagian akhir membahas contoh robot pemanen buah serta tantangan dan arah pengembangan, termasuk peningkatan kendali berbasis citra, kolaborasi manusia dan mesin, kerja sama beberapa lengan robot, dan penyesuaian lingkungan kebun agar lebih sesuai bagi robot.

Tinjauan ini tidak menyajikan hasil eksperimen baru atau metrik kuantitatif baru. Kesimpulannya bersifat kualitatif. Citra dua dimensi dapat diperoleh dari kamera monokular, pencitraan hiperspektral, dan pencitraan termal. Rekonstruksi permukaan tiga dimensi buah memerlukan data dari stereoskop binokular atau sensor *structured light*. Algoritma pengolahan citra untuk kedua kelompok ini sangat berbeda. Penulis juga menjelaskan bahwa kendali *open-loop* sangat bergantung pada kalibrasi kamera dan manipulator yang presisi. Sebaliknya, *visual servo* dapat mencapai presisi tertentu tanpa kalibrasi, tetapi laju bingkai video harus sesuai dengan lebar pita loop tertutup pengendali visual.

Penulis menyebutkan sejumlah faktor yang membatasi keandalan sistem pengenalan. Kinerja sistem dipengaruhi oleh cahaya yang berubah-ubah, oklusi, dan spesies buah yang dipanen. Oleh sebab itu, keandalan metode pengenalan harus mempertimbangkan lingkungan kerja robot, dan pemilihan sensor harus dilakukan dengan tepat. Penulis juga menegaskan bahwa kemajuan teknologi pencitraan dan algoritma kendali baru diharapkan memberi lebih banyak informasi untuk mengenali buah sasaran dan mempercepat proses pemetikan.
