# Permintaan PDF teks lengkap (Pemeriksaan 4, bagian 1)

Berkas ini dibuat oleh `tools/scopus/verifikasi_teks_lengkap.py` dari `verifikasi/teks_lengkap.csv`. Jangan disunting tangan; ubah CSV-nya (kolom `status`, `tanggal_minta`, `sumber_pdf`, `catatan`) lalu jalankan ulang skrip.

## Tenggat

- Semua permintaan (perpustakaan, Bu Fatma, penulis) **terkirim sebelum 6 Oktober 2026**.
- Daftar kajian C1 yang masih belum ber-PDF diserahkan ke Bu Fatma **paling lambat 23 Oktober 2026**.
- Setiap PDF yang diterima disimpan sebagai `literature/scopus-2026-09/pdf/<key>.pdf`; isi `status`, `tanggal_minta`, dan `sumber_pdf` di CSV, lalu jalankan ulang skrip.

## Ringkasan

| Prioritas | Kelompok | Kajian | PDF ada | Belum | OA ditemukan |
|---|---|---|---|---|---|
| 1 | Tabel 2 dan 3 naskah | 22 | 11 | 11 | 7 |
| 2 | C1 dikode dari judul | 43 | 2 | 41 | 2 |
| 3 | C1 lainnya | 130 | 67 | 63 | 23 |
| 4 | C3 sawit: pencacahan dan multipandang | 19 | 10 | 9 | 2 |

Belum ber-PDF: 124 kajian. Jalur: OA 34 · perpustakaan ULM 28 · Bu Fatma 53 · penulis 9 (+4 permintaan paralel ke penulis untuk prioritas 1).

Aturan jalur: salinan OA legal (arXiv, CVF, PMC, repositori institusi, jurnal akses terbuka) diunduh sendiri; artikel jurnal penerbit besar (Elsevier, IEEE, Springer, Wiley, ACM, AIP, IOP, OUP) ke perpustakaan ULM; prosiding, bab buku, dan jurnal Tiongkok ke Bu Fatma; prosiding sawit (penulis Indonesia/Malaysia) dan jurnal penerbit kecil langsung ke penulis.

## 0. Unduh sendiri: salinan akses terbuka legal

Buka tautan di peramban, unduh PDF, simpan dengan nama `<key>.pdf`. Bila tautannya pracetak (arXiv), catat di kolom `sumber_pdf`.

| Prioritas | Key | Tahun | Judul | Tautan OA |
|---|---|---|---|---|
| 1 | `felippomes2026video` | 2026 | Video-based fruit detection and tracking: effects of scanning conditions on fruit load estimation | <https://doi.org/10.1016/j.compag.2026.112330> |
| 1 | `vijayakumar2023tree` | 2023 | Tree-level citrus yield prediction utilizing ground and aerial machine vision and machine learning | <https://doi.org/10.1016/j.atech.2022.100077> |
| 1 | `genemola2023video` | 2023 | Video-Based Fruit Detection and Tracking for Apple Counting and Mapping | <https://upcommons.upc.edu/bitstream/2117/407100/1/Gene%20_Mola%20et%20al.pdf> |
| 1 | `piazolo2026enhanced` | 2026 | Enhanced grape tracking (using deep neural networks) with an extended matching algorithm for SORT and DeepSORT | <https://publica.fraunhofer.de/handle/publica/507891> |
| 1 | `qi2025assessment` | 2025 | Assessment of the tomato cluster yield estimation algorithms via tracking-by-detection approaches | <https://doi.org/10.1016/j.inpa.2025.02.005> |
| 1 | `xing2026lightweight` | 2026 | A lightweight multi-view detection and counting method for real-time cherry tomato yield estimation using greenhouse inspection robots | <https://doi.org/10.1016/j.atech.2026.102260> |
| 1 | `mollineda2025estimation` | 2025 | Estimation of orange tree production by regression from video segments under uncontrolled conditions | <https://link.springer.com/content/pdf/10.1007/s00521-024-10772-4.pdf> |
| 2 | `hernandez2024multi` | 2024 | Multi-Object Tracking in Agricultural Applications using a Vision Transformer for Spatial Association | <https://doi.org/10.1016/j.compag.2024.109379> |
| 2 | `villacres2024assessing` | 2024 | Assessing a multi-camera system to enhance fruit visibility for robotic harvesting in a V-trellised apple orchard | <https://doi.org/10.1016/j.compag.2024.109164> |
| 3 | `awal2026development` | 2026 | Development of a plant sensing robot using virtual space and evaluation of its accuracy | <https://doi.org/10.1016/j.atech.2026.102429> |
| 3 | `farhoud2026instance` | 2026 | Instance segmentation and multi-object tracking for fruit quality grading and dynamic yield estimation in Egyptian citrus orchards | <https://doi.org/10.1016/j.atech.2026.102529> |
| 3 | `nguyen2026modular` | 2026 | A Modular UAV-Based Framework for Apple Detection and Yield Extrapolation from 3D Point Clouds | <https://doi.org/10.1145/3748522.3779768> |
| 3 | `pardobeainy2026maturity` | 2026 | Maturity and size estimation with yield mapping for hydroponic strawberries using machine vision | <https://doi.org/10.1016/j.atech.2026.102416> |
| 3 | `woo2026geometry` | 2026 | Geometry-Driven Triangulation and Differentiable Semantic Gaussian Refinement for 3D Grape Bunch Model Reconstruction in the Field | <https://doi.org/10.1145/3803291.3803356> |
| 3 | `yang2026real` | 2026 | A real-time semantic 3D vineyard mapping and fruit localization system for yield estimation in dynamic vineyards | <https://doi.org/10.1016/j.atech.2026.101784> |
| 3 | `yoshida2026cross` | 2026 | Cross-Day Grape Cluster Tracking Using Branch-Based 3D Alignment in Vineyards | <https://doi.org/10.20965/jrm.2026.p0953> |
| 3 | `zhao2026adapting` | 2026 | Adapting SAM3 for 3D fruit counting with cross-view contrastive learning and Hough voting | <https://doi.org/10.1016/j.compag.2026.112325> |
| 3 | `zhao2026two` | 2026 | A two-stage fine-tuning strategy for 3D object segmentation from multi-view images | <https://doi.org/10.1016/j.atech.2026.102443> |
| 3 | `dong2025fruit` | 2025 | Fruit detection and yield estimation in Camellia oleifera based on improved YOLOv8 and ByteTrack algorithm | <https://doi.org/10.1016/j.atech.2025.101435> |
| 3 | `isobe2025mandarin` | 2025 | Mandarin count estimation with 360-degree tree video and transformer-based deep learning | <https://doi.org/10.1016/j.atech.2025.100874> |
| 3 | `kutyrev2025uav` | 2025 | UAV-based sustainable orchard management: deep learning for apple detection and yield estimation | <https://www.e3s-conferences.org/articles/e3sconf/pdf/2025/14/e3sconf_icaw2024_03021.pdf> |
| 3 | `xieli2025pinesort` | 2025 | PineSORT: A Simple Online Real-Time Tracking Framework for Drone Videos in Agriculture | <https://www.kerwa.ucr.ac.cr/bitstreams/e6886bd8-7ed9-4f46-b574-9d066006527c/download> |
| 3 | `zhang2025robust` | 2025 | Robust real-time blueberry counting in greenhouses using small-object detection and mamba-driven multi-step trajectory completion | <https://doi.org/10.1016/j.atech.2025.101402> |
| 3 | `huang2024automatic` | 2024 | An automatic tracking method for fruit abscission of litchi using convolutional networks | <https://doi.org/10.1016/j.compag.2024.109213> |
| 3 | `zhou2024advancing` | 2024 | Advancing tracking-by-detection with MultiMap: Towards occlusion-resilient online multiclass strawberry counting | <https://doi.org/10.1016/j.eswa.2024.124587> |
| 3 | `zhu2024citrus` | 2024 | Citrus yield estimation for individual trees integrating pruning intensity and image views | <https://doi.org/10.1016/j.eja.2024.127349> |
| 3 | `zheng2023object` | 2023 | Object-Detection from Multi-View remote sensing Images: A case study of fruit and flower detection and counting on a central Florida strawberry farm | <https://digitalcommons.mtu.edu/michigantech-p2/18> |
| 3 | `itakura2021automatic` | 2021 | Automatic pear and apple detection by videos using deep learning and a Kalman filter | <https://doi.org/10.1364/osac.424583> |
| 3 | `sun2020three` | 2020 | Three-dimensional photogrammetric mapping of cotton bolls in situ based on point cloud segmentation and clustering | <https://doi.org/10.1016/j.isprsjprs.2019.12.011> |
| 3 | `nuske2014modeling` | 2014 | Modeling and calibrating visual yield estimates in vineyards | <https://figshare.com/articles/Modeling_and_Calibrating_Visual_Yield_Estimates_in_Vineyards/6555602> |
| 3 | `song2014automatic` | 2014 | Automatic fruit recognition and counting from multiple images | <https://research.wur.nl/en/publications/automatic-fruit-recognition-and-counting-from-multiple-images> |
| 3 | `wang2013automated` | 2013 | Automated Crop Yield Estimation for Apple Orchards | <https://figshare.com/articles/Automated_Crop_Yield_Estimation_for_Apple_Orchards/6551996> |
| 4 | `hamdani2026automated` | 2026 | Automated oil palm fruit counting using deep learning for reliable yield estimation in natural background | <https://doi.org/10.1016/j.atech.2026.102376> |
| 4 | `prasetyo2020automatic` | 2020 | Automatic detection and calculation of palm oil fresh fruit bunches using faster R-CNN | <https://gigvvy.com/journals/ijase/articles/ijase-202005-17-2-121> |

## (a) Untuk perpustakaan ULM (dikelompokkan per penerbit)

### Elsevier (21)

| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | DOI |
|---|---|---|---|---|---|---|
| 1 | `gongal2016apple` | 2016 | Gongal A. | Apple crop-load estimation with over-the-row machine vision system | Computers and Electronics in Agriculture | [10.1016/j.compag.2015.10.022](https://doi.org/10.1016/j.compag.2015.10.022) |
| 2 | `an2024stratracker` | 2024 | An Q. | StraTracker: A dynamic counting method for growing strawberries based on multi-target tracking | Computers and Electronics in Agriculture | [10.1016/j.compag.2024.109564](https://doi.org/10.1016/j.compag.2024.109564) |
| 2 | `gao2022novel` | 2022 | Gao F. | A novel apple fruit detection and counting methodology based on deep learning and trunk tracking in modern orchard | Computers and Electronics in Agriculture | [10.1016/j.compag.2022.107000](https://doi.org/10.1016/j.compag.2022.107000) |
| 2 | `he2022cascade` | 2022 | He L. | Cascade-SORT: A robust fruit counting approach using multiple features cascade matching | Computers and Electronics in Agriculture | [10.1016/j.compag.2022.107223](https://doi.org/10.1016/j.compag.2022.107223) |
| 2 | `hu2026calibration` | 2026 | Hu S. | Calibration-enhanced multi-view RGB-D vision for robust recognition and 3D localization of strawberries under occlusions | Computers and Electronics in Agriculture | [10.1016/j.compag.2025.111221](https://doi.org/10.1016/j.compag.2025.111221) |
| 2 | `huang2026mfft` | 2026 | Huang W. | MFFT: an improved method for stable ID tracking and counting of multi-class mango segmentation with multi-feature fusion in complex occlusion scenarios | Computers and Electronics in Agriculture | [10.1016/j.compag.2026.112149](https://doi.org/10.1016/j.compag.2026.112149) |
| 2 | `jiang2026robot` | 2026 | Jiang L. | Robot-assisted Neural Radiance fields for plot-level cotton crop 3D reconstruction and yield estimation | Computers and Electronics in Agriculture | [10.1016/j.compag.2026.112063](https://doi.org/10.1016/j.compag.2026.112063) |
| 2 | `qi2024improved` | 2024 | Qi Z. | An improved framework based on tracking-by-detection for simultaneous estimation of yield and maturity level in cherry tomatoes | Measurement Journal of the International Measurement Confederation | [10.1016/j.measurement.2024.114117](https://doi.org/10.1016/j.measurement.2024.114117) |
| 2 | `scalisi2021reliability` | 2021 | Scalisi A. | Reliability of a commercial platform for estimating flower cluster and fruit number, yield, tree geometry and light interception in apple trees under different rootstocks and row orientations | Computers and Electronics in Agriculture | [10.1016/j.compag.2021.106519](https://doi.org/10.1016/j.compag.2021.106519) |
| 2 | `scalisi2024detecting` | 2024 | Scalisi A. | Detecting, mapping and digitising canopy geometry, fruit number and peel colour in pear trees with different architecture | Scientia Horticulturae | [10.1016/j.scienta.2023.112737](https://doi.org/10.1016/j.scienta.2023.112737) |
| 2 | `shen2023real` | 2023 | Shen L. | Real-time tracking and counting of grape clusters in the field based on channel pruning with YOLOv5s | Computers and Electronics in Agriculture | [10.1016/j.compag.2023.107662](https://doi.org/10.1016/j.compag.2023.107662) |
| 2 | `tu2025estimation` | 2025 | Tu S. | Estimation of passion fruit yield based on YOLOv8n + OC-SORT + CRCM algorithm | Computers and Electronics in Agriculture | [10.1016/j.compag.2024.109727](https://doi.org/10.1016/j.compag.2024.109727) |
| 2 | `villacres2023apple` | 2023 | Villacrés J. | Apple orchard production estimation using deep learning strategies: A comparison of tracking-by-detection algorithms | Computers and Electronics in Agriculture | [10.1016/j.compag.2022.107513](https://doi.org/10.1016/j.compag.2022.107513) |
| 2 | `vulpi2022rgb` | 2022 | Vulpi F. | An RGB-D multi-view perspective for autonomous agricultural robots | Computers and Electronics in Agriculture | [10.1016/j.compag.2022.107419](https://doi.org/10.1016/j.compag.2022.107419) |
| 2 | `wang2024slam` | 2024 | Wang H. | SLAM-PYE: Tightly coupled GNSS-binocular-inertial fusion for pitaya positioning, counting, and yield estimation | Computers and Electronics in Agriculture | [10.1016/j.compag.2024.109177](https://doi.org/10.1016/j.compag.2024.109177) |
| 2 | `zhang2025row` | 2025 | Zhang J. | Row-based kiwifruit counting pipeline for smartphone-captured videos using fruit tracking and detection region adaptation guided by support-post | Computers and Electronics in Agriculture | [10.1016/j.compag.2025.110476](https://doi.org/10.1016/j.compag.2025.110476) |
| 2 | `zheng2024robust` | 2024 | Zheng Z. | A robust and efficient citrus counting approach for large-scale unstructured orchards | Agricultural Systems | [10.1016/j.agsy.2024.103867](https://doi.org/10.1016/j.agsy.2024.103867) |
| 3 | `tan2025appleyolo` | 2025 | Tan S. | AppleYOLO: Apple yield estimation method using improved YOLOv8 based on Deep OC-SORT | Expert Systems with Applications | [10.1016/j.eswa.2025.126764](https://doi.org/10.1016/j.eswa.2025.126764) |
| 3 | `wu2023twice` | 2023 | Wu Z. | Twice matched fruit counting system: An automatic fruit counting pipeline in modern apple orchard using mutual and secondary matches | Biosystems Engineering | [10.1016/j.biosystemseng.2023.09.005](https://doi.org/10.1016/j.biosystemseng.2023.09.005) |
| 3 | `xiao20243d` | 2024 | Xiao S. | 3D reconstruction and characterization of cotton bolls in situ based on UVA technology | ISPRS Journal of Photogrammetry and Remote Sensing | [10.1016/j.isprsjprs.2024.01.027](https://doi.org/10.1016/j.isprsjprs.2024.01.027) |
| 3 | `zhang2021method` | 2021 | Zhang C. | A method for organs classification and fruit counting on pomegranate trees based on multi-features fusion and support vector machine by 3D point cloud | Scientia Horticulturae | [10.1016/j.scienta.2020.109791](https://doi.org/10.1016/j.scienta.2020.109791) |

### IEEE (4)

| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | DOI |
|---|---|---|---|---|---|---|
| 2 | `park2026incremental` | 2026 | Park D. | Incremental 3D Crop Model Association for Real-Time Counting in Dense Orchards | IEEE Robotics and Automation Letters | [10.1109/lra.2026.3662648](https://doi.org/10.1109/lra.2026.3662648) |
| 3 | `lu2025iot` | 2025 | Lu J. | IoT-Based Precision Litchi Tracking and Counting Method Using Gated Metrics | IEEE Internet of Things Journal | [10.1109/jiot.2025.3561130](https://doi.org/10.1109/jiot.2025.3561130) |
| 3 | `wang2026semantic` | 2026 | Wang Y. | Semantic NeRF-Oriented 3-D Object Counting for Industrial Fruit Harvesting | IEEE Transactions on Automation Science and Engineering | [10.1109/tase.2026.3700861](https://doi.org/10.1109/tase.2026.3700861) |
| 3 | `yang2025hierarchical` | 2025 | Yang W. | Hierarchical 3D Scene Graph based Semantic-Metric SLAM for Plant Inspection and Fruit Counting in Intelligent Hydroponics System | IEEE Internet of Things Journal | [10.1109/jiot.2025.3600531](https://doi.org/10.1109/jiot.2025.3600531) |

### Springer (2)

| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | DOI |
|---|---|---|---|---|---|---|
| 2 | `pichhika2025enhanced` | 2025 | Pichhika H.C. | Enhanced YOLO-Based Mango Detection and Centroid Tracking for Precise Yield Estimation | Applied Fruit Science | [10.1007/s10341-025-01385-9](https://doi.org/10.1007/s10341-025-01385-9) |
| 2 | `tu2024passion` | 2024 | Tu S. | A passion fruit counting method based on the lightweight YOLOv5s and improved DeepSORT | Precision Agriculture | [10.1007/s11119-024-10132-1](https://doi.org/10.1007/s11119-024-10132-1) |

### Wiley (1)

| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | DOI |
|---|---|---|---|---|---|---|
| 3 | `zheng2023efficient` | 2023 | Zheng Z. | An efficient online citrus counting system for large-scale unstructured orchards based on the unmanned aerial vehicle | Journal of Field Robotics | [10.1002/rob.22147](https://doi.org/10.1002/rob.22147) |

## (b) Untuk Bu Fatma (kemungkinan tidak ada di perpustakaan)

Prosiding konferensi, bab buku, dan jurnal Tiongkok.

| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | Penerbit | DOI |
|---|---|---|---|---|---|---|---|
| 1 | `hong2025fruitgaussian` | 2025 | Hong X. | Fruitgaussian: 3D Gaussian Splatting for Automated Fruit Counting in Natural Orchard | Chinese Control Conference Ccc | IEEE | [10.23919/ccc64809.2025.11179457](https://doi.org/10.23919/ccc64809.2025.11179457) |
| 1 | `poncemachete2025optimizing` | 2025 | Ponce-Machete R.A. | Optimizing Fruit Yield Prediction: Evaluating Multiobject Tracking Algorithms for Calamansi Fruit Detection Using Yolov8m | 2025 17th International Conference on Computer and Automation Engineering Iccae 2025 | IEEE | [10.1109/iccae64891.2025.10980575](https://doi.org/10.1109/iccae64891.2025.10980575) |
| 1 | `wei2025multi` | 2025 | Wei J. | Multi-Object Tracking for Apple Counting in Orchards Using Stereo Vision | Conference Proceedings 2025 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2025 | IEEE | [10.1109/metroagrifor66923.2025.11512512](https://doi.org/10.1109/metroagrifor66923.2025.11512512) |
| 2 | `gongal2014identification` | 2014 | Gongal A. | Identification of repetitive apples for improved crop-load estimation with dual-side imaging | American Society of Agricultural and Biological Engineers Annual International Meeting 2014 Asabe 2014 | ASABE | (tanpa DOI) |
| 2 | `gao2021apple` | 2021 | Gao F. | Apple detection and counting using real-time video based on deep learning and object tracking | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering | CSAE (Tiongkok) | [10.11975/j.issn.1002-6819.2021.21.025](https://doi.org/10.11975/j.issn.1002-6819.2021.21.025) |
| 2 | `lyu2023method` | 2023 | Lyu J. | Method for estimation of bagged grape yield using a self-correcting NMS-ByteTrack | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering | CSAE (Tiongkok) | [10.11975/j.issn.1002-6819.202304116](https://doi.org/10.11975/j.issn.1002-6819.202304116) |
| 2 | `lyu2025counting` | 2025 | Lyu J. | Counting bagging grape using improved YOLOv9s and adaptive Kalman filter | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering | CSAE (Tiongkok) | [10.11975/j.issn.1002-6819.202412026](https://doi.org/10.11975/j.issn.1002-6819.202412026) |
| 2 | `lyu2025real` | 2025 | Lyu J. | Real-time detecting and counting dual-association bagged grape clusters using EMO-YOLOv5s | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering | CSAE (Tiongkok) | [10.11975/j.issn.1002-6819.202412150](https://doi.org/10.11975/j.issn.1002-6819.202412150) |
| 2 | `qian2013yield` | 2013 | Qian J. | Yield estimation model of single tree of Fuji apples based on bilateral image identification | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering | CSAE (Tiongkok) | [10.3969/j.issn.1002-6819.2013.11.017](https://doi.org/10.3969/j.issn.1002-6819.2013.11.017) |
| 2 | `weng2026citrus` | 2026 | Weng H. | Citrus tracking and counting using UAV remote sensing video imagery with improved YOLO11 | Nongye Gongcheng Xuebao Transactions of the Chinese Society of Agricultural Engineering | CSAE (Tiongkok) | [10.11975/j.issn.1002-6819.202508166](https://doi.org/10.11975/j.issn.1002-6819.202508166) |
| 2 | `feng2026greenhouse` | 2026 | Feng Q. | Greenhouse Tomato Fruit Inspection and Counting Method Based on Improved YOLO v8n ByteTrack | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery | CSAM (Tiongkok) | [10.6041/j.issn.1000-1298.2026.05.011](https://doi.org/10.6041/j.issn.1000-1298.2026.05.011) |
| 2 | `guo2023real` | 2023 | Guo M. | Real-time Production Prediction of Kiwifruit in Orchard Based on Video Tracking Algorithm | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery | CSAM (Tiongkok) | [10.6041/j.issn.1000-1298.2023.06.018](https://doi.org/10.6041/j.issn.1000-1298.2023.06.018) |
| 2 | `tu2026passion` | 2026 | Tu S. | Passion Fruit Counting Method Based on Lightweight YOLO lln CLL and BoT SORT | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery | CSAM (Tiongkok) | [10.6041/j.issn.1000-1298.2026.10.021](https://doi.org/10.6041/j.issn.1000-1298.2026.10.021) |
| 2 | `wang2024camellia` | 2024 | Wang J. | Camellia oleifera Fruit Static and Dynamic Detection Counting Based on Improved COF-YOLO v8n | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery | CSAM (Tiongkok) | [10.6041/j.issn.1000-1298.2024.04.019](https://doi.org/10.6041/j.issn.1000-1298.2024.04.019) |
| 2 | `zhu2022identification` | 2022 | Zhu Q. | Identification and Counting Method of Potted Kumquat Fruits Based on Point Cloud Registration | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery | CSAM (Tiongkok) | [10.6041/j.issn.1000-1298.2022.05.021](https://doi.org/10.6041/j.issn.1000-1298.2022.05.021) |
| 2 | `blondet2026counting` | 2026 | Blondet D.A. | Counting Avocados in Orchard Videos Using a YOLO and BoT-SORT-Based Architecture | Communications in Computer and Information Science | Springer | [10.1007/978-3-032-20322-9_36](https://doi.org/10.1007/978-3-032-20322-9_36) |
| 2 | `dai2022tracking` | 2022 | Dai G. | Tracking and Counting Method for Tomato Fruits Scouting Robot in Greenhouse | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics | Springer | [10.1007/978-3-031-13844-7_6](https://doi.org/10.1007/978-3-031-13844-7_6) |
| 2 | `kirk2021robust` | 2021 | Kirk R. | Robust Counting of Soft Fruit Through Occlusions with Re-identification | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics | Springer | [10.1007/978-3-030-87156-7_17](https://doi.org/10.1007/978-3-030-87156-7_17) |
| 2 | `matos2025apple` | 2025 | Matos G.P. | An Apple Counting System Robust to Multiple Intermittent Occlusions | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics | Springer | [10.1007/978-3-031-73497-7_15](https://doi.org/10.1007/978-3-031-73497-7_15) |
| 2 | `parico2023real` | 2023 | Parico A.I.B. | Real-Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT | Iot and AI in Agriculture Self Sufficiency in Food Production to Achieve Society 5 0 and Sdgs Globally | Springer | [10.1007/978-981-19-8113-5_11](https://doi.org/10.1007/978-981-19-8113-5_11) |
| 2 | `roy2017vision` | 2017 | Roy P. | Vision-Based Apple Counting and Yield Estimation | Springer Proceedings in Advanced Robotics | Springer | [10.1007/978-3-319-50115-4_42](https://doi.org/10.1007/978-3-319-50115-4_42) |
| 2 | `xia2024kiwifruit` | 2024 | Xia Y. | Kiwifruit Counting Using Kiwidetector and Kiwitracker | Lecture Notes in Networks and Systems | Springer | [10.1007/978-3-031-47724-9_41](https://doi.org/10.1007/978-3-031-47724-9_41) |
| 3 | `ashokan2024fruit` | 2024 | Ashokan A. | Fruit yield estimation and forecasting for precision agriculture | Aip Conference Proceedings | AIP Publishing | [10.1063/5.0196960](https://doi.org/10.1063/5.0196960) |
| 3 | `gao2021appleb` | 2021 | Gao F. | Apple fruit detection and counting based on deep learning and trunk tracking | American Society of Agricultural and Biological Engineers Annual International Meeting Asabe 2021 | ASABE | [10.13031/aim.202100193](https://doi.org/10.13031/aim.202100193) |
| 3 | `huang2019high` | 2019 | Huang Y.H. | High-throughput image analysis framework for fruit detection, localization and measurement from video streams | 2019 Asabe Annual International Meeting | ASABE | [10.13031/aim.201900487](https://doi.org/10.13031/aim.201900487) |
| 3 | `jiang2025neural` | 2025 | Jiang L. | Neural Radiance Fields for Plot-level Cotton Crop Three-dimensional Reconstruction and Yield Estimation | 2025 Asabe Annual International Meeting | ASABE | [10.13031/aim.202500502](https://doi.org/10.13031/aim.202500502) |
| 3 | `li2023blueberry` | 2023 | Li Z. | Blueberry Yield Estimation Through Multi-View Imagery with YOLOv8 Object Detection | 2023 Asabe Annual International Meeting | ASABE | [10.13031/aim.202300883](https://doi.org/10.13031/aim.202300883) |
| 3 | `zhou2023dynamic` | 2023 | Zhou X. | A Dynamic Object Counting Method for Strawberry Fruits using Vision Transformer Networks and Kalman Filter Tracking | 2023 Asabe Annual International Meeting | ASABE | [10.13031/aim.202301450](https://doi.org/10.13031/aim.202301450) |
| 3 | `ahmad2024enabling` | 2024 | Ahmad J. | Enabling Consumer UAVs for Precision Agriculture Applications: A Case Study of Yield Estimation | Digest of Technical Papers IEEE International Conference on Consumer Electronics | IEEE | [10.1109/icce59016.2024.10444191](https://doi.org/10.1109/icce59016.2024.10444191) |
| 3 | `akella2025deep` | 2025 | Akella A. | Deep Learning-Based Coconut Ripeness Classification and Yield Estimation using YOLO and Kalman Filtering | 2025 International Conference on Sensors and Related Networks Sennet 2025 Special Focus on Digital Healthcare 64220 | IEEE | [10.1109/sennet64220.2025.11136053](https://doi.org/10.1109/sennet64220.2025.11136053) |
| 3 | `arlotta2023ekf` | 2023 | Arlotta A. | An EKF-Based Multi-Object Tracking Framework for a Mobile Robot in a Precision Agriculture Scenario | Proceedings of the 11th European Conference on Mobile Robots Ecmr 2023 | IEEE | [10.1109/ecmr59166.2023.10256338](https://doi.org/10.1109/ecmr59166.2023.10256338) |
| 3 | `gao2026vision` | 2026 | Gao Z. | Vision-Based 3D Fruit Localization for Robotic Harvesting Using Recursive State Estimation | 2026 7th International Conference on Artificial Intelligence and Electromechanical Automation Aiea 2026 | IEEE | [10.1109/aiea70743.2026.11633088](https://doi.org/10.1109/aiea70743.2026.11633088) |
| 3 | `garderes2024apple` | 2024 | Garderes R. | Apple Detection and Counting Using Neural Networks | Proceedings 2024 50th Latin American Computing Conference Clei 2024 | IEEE | [10.1109/clei64178.2024.10700174](https://doi.org/10.1109/clei64178.2024.10700174) |
| 3 | `garg2025autonomous` | 2025 | Garg K. | Autonomous UAV Navigation and Mapping for Accurate Fruit Detection and Counting in Controlled Environments: Simulation and Real-World Validation | 2025 International Conference on Unmanned Aircraft Systems Icuas 2025 | IEEE | [10.1109/icuas65942.2025.11007888](https://doi.org/10.1109/icuas65942.2025.11007888) |
| 3 | `ishizuka2024eggplant` | 2024 | Ishizuka T. | Eggplant Detection and Counting Across the Entire Greenhouse Using Deep Learning and Motion Parallax | 10th IEEE International Smart Cities Conference Smart Cities Revolution for Mankind Isc2 2024 Proceedings | IEEE | [10.1109/isc260477.2024.11004199](https://doi.org/10.1109/isc260477.2024.11004199) |
| 3 | `issad2025real` | 2025 | Issad H.A. | Real-Time Fruit Detection and Counting | Icrami 2025 2025 International Conference on Recent Advances in Mathematics and Informatics | IEEE | [10.1109/icrami64946.2025.11472714](https://doi.org/10.1109/icrami64946.2025.11472714) |
| 3 | `kemper2025performance` | 2025 | Kemper R.J.H. | Performance Evaluation of Detection and Tracking Algorithms for Automated Grape Cluster Counting | C3 2025 IEEE Colombian Caribbean Conference | IEEE | [10.1109/c366505.2025.11340275](https://doi.org/10.1109/c366505.2025.11340275) |
| 3 | `louis2025automated` | 2025 | Louis F. | Automated Muskmelon Counting in Real Farm Environment using YOLOv11n | Proceeding of the IEEE International Conference on Smart Instrumentation Measurement and Applications Icsima | IEEE | [10.1109/icsima66552.2025.11233648](https://doi.org/10.1109/icsima66552.2025.11233648) |
| 3 | `majdalawieh2025optimizing` | 2025 | Majdalawieh M. | Optimizing Fruit Harvesting Through a High-Performance Deep Learning Framework for Detection, Tracking, and Automated Counting. | Proceedings 2025 27th IEEE International Conference on High Performance Computing and Communications 11th IEEE International Conference on Data Science and Systems 23rd IEEE International Conference on Smart City 11th IEEE International Conference on Dependability in Sensor Cloud and Big Data Systems and Applications and 21st IEEE International Conference on Embedded Software and Systems Hpcc Dss Smartcity Dependsys Icess 2025 | IEEE | [10.1109/hpcc67675.2025.00132](https://doi.org/10.1109/hpcc67675.2025.00132) |
| 3 | `osman2021yieldb` | 2021 | Osman Y. | Yield Estimation using Deep Learning for Precision Agriculture | 7th IEEE World Forum on Internet of Things Wf Iot 2021 | IEEE | [10.1109/wf-iot51360.2021.9595143](https://doi.org/10.1109/wf-iot51360.2021.9595143) |
| 3 | `pai2024maturity` | 2024 | Pai C.A. | Maturity and Yield Estimation of Tomatoes Using RGB and Multispectral Images | Proceedings of the IEEE International Conference on Industrial Technology | IEEE | [10.1109/icit58233.2024.10540838](https://doi.org/10.1109/icit58233.2024.10540838) |
| 3 | `roy2016surveying` | 2016 | Roy P. | Surveying apple orchards with a monocular vision system | IEEE International Conference on Automation Science and Engineering | IEEE | [10.1109/coase.2016.7743500](https://doi.org/10.1109/coase.2016.7743500) |
| 3 | `roy2017active` | 2017 | Roy P. | Active view planning for counting apples in orchards | IEEE International Conference on Intelligent Robots and Systems | IEEE | [10.1109/iros.2017.8206500](https://doi.org/10.1109/iros.2017.8206500) |
| 3 | `sasse2025object` | 2025 | Sasse A.M. | An Object-Tracking Technique for Counting Grape Clusters in Brazilian Northeast's Pergola Vineyards | Proceedings of the 2025 28th International Conference on Information Fusion Fusion 2025 | IEEE | [10.23919/fusion65864.2025.11124157](https://doi.org/10.23919/fusion65864.2025.11124157) |
| 3 | `serafino2020detection` | 2020 | Serafino S.E. | Detection and Counting of Lemons using Artificial Vision and Tracking Techniques for Real Time Harvest Estimation | Proceedings 2020 46th Latin American Computing Conference Clei 2020 | IEEE | [10.1109/clei52000.2020.00064](https://doi.org/10.1109/clei52000.2020.00064) |
| 3 | `vaishnavi2025fruit` | 2025 | Vaishnavi M. | Fruit Detection and Yield Estimation using Path Aggregation Feature Pyramid Network and Deep SORT Algorithm: A Case Study on Orange Fruit | Proceedings of the 9th International Conference on Electronics Communication and Aerospace Technology Iceca 2025 | IEEE | [10.1109/iceca66444.2025.11383116](https://doi.org/10.1109/iceca66444.2025.11383116) |
| 3 | `wang2022research` | 2022 | Wang S. | Research on UAV Online Visual Tracking Algorithm based on YOLOv5 and FlowNet2 for Apple Yield Inspection | Proceedings of the 4th Wrc Symposium on Advanced Robotics and Automation 2022 Wrc Sara 2022 | IEEE | [10.1109/wrcsara57040.2022.9903925](https://doi.org/10.1109/wrcsara57040.2022.9903925) |
| 3 | `xie2023fruit` | 2023 | Xie F. | Fruit Distribution Acquisition with Multi-Vision for Multi-Arm Harvesting Robots | 2023 8th International Conference on Control Robotics and Cybernetics CRC 2023 | IEEE | [10.1109/crc60659.2023.10488608](https://doi.org/10.1109/crc60659.2023.10488608) |
| 3 | `xing2025cb` | 2025 | Xing Y. | CB-YOLO-DeepSORT: Real-Time Yield Estimation for Tomatoes in Greenhouses | 15th IEEE International Conference on Cyber Technology in Automation Control and Intelligent Systems Cyber 2025 | IEEE | [10.1109/cyber67662.2025.11168194](https://doi.org/10.1109/cyber67662.2025.11168194) |
| 3 | `zhang2024stablesort` | 2024 | Zhang W. | StableSort-CMC: a tracking algorithm for robot dog based orchard fruit counting | Proceedings 2024 China Automation Congress Cac 2024 | IEEE | [10.1109/cac63892.2024.10865478](https://doi.org/10.1109/cac63892.2024.10865478) |
| 3 | `zhou2024utilizing` | 2024 | Zhou C. | Utilizing NeRF-Based Rays for Spatial Perception in Fruit Counting Deduplication | Proceedings 2024 International Symposium on Internet of Things and Smart Cities Isitsc 2024 | IEEE | [10.1109/isitsc64373.2024.00013](https://doi.org/10.1109/isitsc64373.2024.00013) |
| 3 | `si2026citrus` | 2026 | Si N. | Citrus yield estimation based on multi- object tracking in video streams using an improved YOLOv8n model | Journal of Fruit Science | Journal of Fruit Science (Tiongkok) | [10.13925/j.cnki.gsxb.20250487](https://doi.org/10.13925/j.cnki.gsxb.20250487) |
| 3 | `cho2025case` | 2025 | Cho S.H. | A case study on the integration of a snapshot hyperspectral field-portable imager solving fruit quality assessment | Proceedings of SPIE the International Society for Optical Engineering | SPIE | [10.1117/12.3042114](https://doi.org/10.1117/12.3042114) |

## (c) Diminta ke penulis

Jalur utama `penulis`, ditambah kajian prioritas 1 yang jalur utamanya perpustakaan atau Bu Fatma (permintaan paralel, karena kajian ini menopang Tabel 2 dan 3). Kirim lewat surel penulis korespondensi bila tercantum; bila tidak, lewat tombol *Request full-text* di ResearchGate. Surel diisi di kolom `email_penulis_korespondensi` hanya bila ditemukan terbuka di halaman makalah atau ORCID.

| Prioritas | Key | Tahun | Penulis pertama | Judul | DOI | Surel | Keterangan |
|---|---|---|---|---|---|---|---|
| 1 | `gongal2016apple` | 2016 | Gongal A. | Apple crop-load estimation with over-the-row machine vision system | [10.1016/j.compag.2015.10.022](https://doi.org/10.1016/j.compag.2015.10.022) |  | paralel |
| 1 | `hong2025fruitgaussian` | 2025 | Hong X. | Fruitgaussian: 3D Gaussian Splatting for Automated Fruit Counting in Natural Orchard | [10.23919/ccc64809.2025.11179457](https://doi.org/10.23919/ccc64809.2025.11179457) |  | paralel |
| 1 | `poncemachete2025optimizing` | 2025 | Ponce-Machete R.A. | Optimizing Fruit Yield Prediction: Evaluating Multiobject Tracking Algorithms for Calamansi Fruit Detection Using Yolov8m | [10.1109/iccae64891.2025.10980575](https://doi.org/10.1109/iccae64891.2025.10980575) |  | paralel |
| 1 | `wei2025multi` | 2025 | Wei J. | Multi-Object Tracking for Apple Counting in Orchards Using Stereo Vision | [10.1109/metroagrifor66923.2025.11512512](https://doi.org/10.1109/metroagrifor66923.2025.11512512) |  | paralel |
| 2 | `safre2024advanced` | 2024 | Safre A. | Advanced methods for yield mapping in tart cherries: tank change tracking and YOLO-DeepSort fruit counting | [10.17660/actahortic.2024.1395.38](https://doi.org/10.17660/actahortic.2024.1395.38) |  | utama |
| 3 | `singh2025robust` | 2025 | Singh R. | Robust real-time strawberry maturity detection using UAV-mounted deep learning for precision agriculture | [10.1186/s12870-025-07246-7](https://doi.org/10.1186/s12870-025-07246-7) |  | utama |
| 4 | `aji2021automatic` | 2021 | Aji W.S. | Automatic Oil Palm Unstripped Bunch (USB) Counting System based on Faster RCNN and Object Tracking | [10.1109/ic2se52832.2021.9792068](https://doi.org/10.1109/ic2se52832.2021.9792068) |  | utama |
| 4 | `daud2022loose` | 2022 | Daud M.M. | Loose Fruitlet and Fresh Fruit Bunch Detection for Palm Oil Harvest Management | [10.1109/iotais56727.2022.9975972](https://doi.org/10.1109/iotais56727.2022.9975972) |  | utama |
| 4 | `daud2023detection` | 2023 | Daud M.M. | Detection of Oil Palm Tree and Loose Fruitlets for Fresh Fruit Bunch's Ready-to-Harvest Prediction via Deep Learning Approach | (tanpa DOI) |  | utama |
| 4 | `hidayat2024establishing` | 2024 | Hidayat M.R. | Establishing a Standard Operating Procedure (SOP) for Palm Oil Plantation FFB Image Capture: Utilizing YOLOv8 for Counting and Ripeness Classification | [10.1109/icoris63540.2024.10903724](https://doi.org/10.1109/icoris63540.2024.10903724) |  | utama |
| 4 | `hutapea2024palm` | 2024 | Hutapea R.R. | Palm Fruit Ripeness Detection and Counting Using YOLOv8 Algorithm in PTPN IV Medan North Sumatera Indonesia | [10.1109/icoris63540.2024.10903790](https://doi.org/10.1109/icoris63540.2024.10903790) |  | utama |
| 4 | `kassim2012oil` | 2012 | Kassim M.S.M. | Oil palm fresh fruit bunches (FFB) growth determination system to support harvesting operation | (tanpa DOI) |  | utama |
| 4 | `narendran2024palm` | 2024 | Narendran R. | Palm fruit harvesting using IoT-based fruit counting system | [10.1063/5.0229292](https://doi.org/10.1063/5.0229292) |  | utama |

## Templat surel ke penulis (bahasa Inggris)

```text
Subject: Request for a copy of your paper "[TITLE]" for a systematic review

Dear Dr. [SURNAME],

I am conducting a systematic review of image-based fruit counting, focusing on how
studies avoid double counting the same fruit across several images (tracking,
3D association, and related methods). Your paper

  [AUTHORS] ([YEAR]). [TITLE]. [SOURCE]. https://doi.org/[DOI]

is one of the studies included in the review, and I would like to read the full
text to code its methods and results accurately. Our institution does not have
access to it. Would you be willing to send me a copy (the accepted manuscript is
fine) for private research use?

Thank you very much for your time. I will cite the paper in the review.

Kind regards,

Muhammad Zainal Muttaqin
Universitas Lambung Mangkurat
[Department/Faculty]
[email address]
```

## Templat permintaan ResearchGate

```text
Dear Dr. [SURNAME], I am preparing a systematic review of image-based fruit
counting (how studies avoid counting the same fruit twice across images), and your
paper "[TITLE]" is one of the included studies. Could you kindly share the full text
for private research use? I will cite it in the review. Thank you very much.
Muhammad Zainal Muttaqin, Universitas Lambung Mangkurat
```
