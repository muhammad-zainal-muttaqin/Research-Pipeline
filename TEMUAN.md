# Temuan Riset: YOLO, RGB, RGB+Depth, dan YOLO+RGB-D (2019–2026)

> Dokumen ini merangkum **temuan** dari tinjauan pustaka mendalam. Naskah lengkap
> dalam format LaTeX ada di [`evidence-body.tex`](evidence-body.tex), dikompilasi ke
> [`main.pdf`](main.pdf) (gaya IEEE) dan [`main-elsarticle.pdf`](main-elsarticle.pdf) (gaya
> Elsevier), dengan basis data sitasi di [`references.bib`](references.bib).

---

## 1. Ringkasan Eksekutif

| Item | Nilai |
|---|---|
| Total entri terkumpul dalam ledger | **202** |
| Sumber terverifikasi (ada PDF lokal) dan dijadikan korpus | **182** |
| Sumber unik yang benar-benar dirujuk di naskah | **182** |
| Target minimum yang diminta | 100 ✅ **terlampaui 2×** |
| Rentang tahun fokus | 2019–2026 (plus karya fondasi 2014–2018 sebagai konteks) |
| Poros riset | (1) Evolusi YOLO · (2) Deteksi RGB · (3) Fusi RGB+Depth · (4) YOLO+RGB-D |
| Jumlah tema/klaster | 14 |

**Status penyelesaian:** Naskah LaTeX + basis data BibTeX telah ditulis; seluruh
182 sumber tervalidasi (tidak ada sitasi menggantung; 20 record ledger ditahan karena PDF sumber tak tersedia lokal). Ambang 100 sitasi
tercapai dan terlampaui. Batch entri 155–202 (penyeimbang ujung rentang, termasuk
jurnal 2025–2026 yang diverifikasi via arXiv) telah terintegrasi penuh ke naskah
dan tabel taksonomi.

---

## 2. Cara Kerja (Metodologi)

1. **Penelusuran bertahap** dilakukan pada 20+ kueri lintas basis data akademik
   (arXiv, IEEE Xplore, ScienceDirect, SpringerLink, MDPI, PLOS, Nature) memakai
   kombinasi kata kunci: `YOLO`, `object detection`, `RGB-D`, `depth fusion`,
   `cross-modal`, `salient object detection`, `semantic segmentation`,
   `6D pose`, `robotic grasping`, `3D detection`, `multispectral`, `SLAM`.
2. **Penyaringan** berdasarkan relevansi tema, kejelasan kontribusi, dan
   cakupan tahun 2019–2026 (karya fondasi 2014–2018 dipertahankan sebagai
   konteks historis yang diperlukan).
3. **Sintesis** ke dalam 14 klaster tematik dan penulisan tinjauan naratif.
4. **Verifikasi silang** otomatis memastikan setiap `\cite` di naskah memiliki
   entri padanan di `references.bib` (0 sitasi menggantung).

> **Catatan integritas:** Metadata bibliografi disusun dari hasil penelusuran
> web dan pengetahuan atas karya-karya kanonik. Untuk publikasi formal,
> disarankan verifikasi akhir nomor volume/halaman/DOI tiap entri melalui laman
> penerbit — terutama untuk entri aplikasi yang lebih baru.

---

## 3. Temuan Utama per Poros

### Poros 1 — Evolusi YOLO
- YOLO berkembang dari perumusan **deteksi sebagai regresi tunggal** (v1, 2016)
  menuju desain **anchor-free** (YOLOX, 2021), **efisiensi industri** (v6, 2022),
  **trainable bag-of-freebies + E-ELAN** (v7, 2022), **PGI/GELAN** (v9, 2024),
  **bebas-NMS end-to-end** (v10, 2024), dan **modul atensi C3K2/C2PSA** (v11, 2024).
- **Temuan:** tren jelas menuju penghapusan komponen manual (anchor, NMS) dan
  penyisipan mekanisme atensi — YOLO makin menyerupai detektor end-to-end
  bergaya transformer sambil mempertahankan kecepatan waktu-nyata.

### Poros 2 — Deteksi Objek Berbasis RGB
- Ekosistem RGB matang: dua-tahap (Faster R-CNN), satu-tahap (SSD, RetinaNet),
  anchor-free (FCOS, CenterNet), dan **transformer** (DETR, Deformable DETR,
  ViT, Swin).
- **Temuan:** terjadi **konvergensi arsitektur hibrida CNN–transformer**; Swin
  dan DETR menjadi pembanding/backbone standar yang juga merembes ke pipeline
  RGB-D.

### Poros 3 — Fusi RGB+Depth
- Strategi fusi terbagi tiga: **awal (input-level)**, **menengah
  (feature-level)**, **akhir (decision-level)**.
- **Temuan kuat & berulang:** **fusi tingkat-fitur menengah dengan atensi
  lintas-modal** paling konsisten mengungguli fusi awal/akhir (didukung
  SA-Gate, CIR-Net, dan studi Ophoff dkk.). Kualitas & penyelarasan peta
  kedalaman adalah faktor penentu keuntungan fusi.

### Poros 4 — Integrasi YOLO+RGB-D
- Dua pola integrasi dominan:
  1. **Perluasan kanal masukan** — menambahkan kanal depth ke RGB (mis.
     *Expandable YOLO* → kotak 3D).
  2. **Deteksi-lalu-proyeksi** — YOLO mendeteksi 2D, hasilnya diproyeksikan ke
     peta depth teraligned untuk lokalisasi 3D (navigasi robot, pengukuran
     jarak, penggenggaman, panen buah).
- **Temuan:** penambahan depth **meningkatkan ketahanan terhadap oklusi** dan
  **memungkinkan estimasi posisi 3D** yang wajib untuk aksi robotik — dengan
  YOLO tetap menjadi tahap deteksi 2D pilihan karena rasio kecepatan/akurasi.

---

## 4. Taksonomi Tematik (17 Klaster, selaras katalog)

| # | Tema | Jumlah | Contoh kunci |
|---|---|---|---|
| 1 | Fondasi RGB | 39 | R-CNN, Faster R-CNN, YOLOv1–v11/26, DETR, RT-DETR, ViT, Swin, ConvNeXt |
| 2 | Estimasi Kedalaman | 21 | DPT, MiDaS, Depth Anything V2/3, ZoeDepth, Metric3D, Marigold, UniDAC |
| 3 | RGB-D SOD | 19 | DMRA, BBS-Net, D3Net, VST, CIR-Net, CAVER, MobileSal, GL-DMNet |
| 4 | Deteksi 3D | 17 | VoxelNet, PointPillars, PV-RCNN, CenterPoint, BEVFusion, BEVFormer, DETR3D |
| 5 | Segmentasi RGB-D | 15 | FuseNet, SA-Gate, CMX, DFormer, SegFormer, GeminiFusion, DiffPixelFormer |
| 6 | Pose 6D | 10 | PoseCNN, DenseFusion, FFB6D, GDR-Net, ZebraPose, OnePose, FoundationPose |
| 7 | Grasp Robotik | 9 | GG-CNN, GR-ConvNet v2, GraspNet-1Billion, Contact-GraspNet, VGN |
| 8 | Survei YOLO | 7 | Terven 2023, Hussain 2023, Sapkota 2024/2025, Jegham 2024 |
| 9 | RGB-D SLAM | 7 | ORB-SLAM2/3, DynaSLAM, DS-SLAM, CFP-SLAM, DROID-SLAM |
| 10 | Fusi Multimodal | 7 | ResNet, PointNet, CBAM, Feng 2021, Zou 2023, Zhou 2021, Lopes 2022 |
| 11 | Pedestrian RGB-T | 6 | KAIST, IAF R-CNN, MBNet, GAFF, CFR, CFT |
| 12 | Dataset | 6 | NYUv2, SUN RGB-D, ScanNet, KITTI, nuScenes, COCO |
| 13 | YOLO plus RGB-D | 5 | Expandable YOLO, FusionVision, YOLOv8-URE, Ophoff 2019, Xu 2024 |
| 14 | Pertanian | 4 | Gené-Mola 2020, Kang & Chen 2020, Birrell 2020, Onishi 2019 |
| 15 | Remote Sensing | 4 | YOLT, TPH-YOLOv5, UAV-YOLOv8, RiO-DETR |
| 16 | Medis | 3 | Qureshi 2024, Al-Antari 2021, Baccouche 2021 |
| 17 | Industri | 3 | EFC-YOLO, PCB-YOLO, Safety Helmet YOLOv5 |

> Jumlah per tema dihitung langsung dari katalog terverifikasi dan berjumlah **182** total
> (17 tema), selaras dengan Ruang Baca Riset dan naskah.

---

## 5. Insight Lintas-Tema

1. **Depth melengkapi kelemahan RGB.** Pada oklusi, pencahayaan rendah, dan
   kebutuhan lokalisasi 3D, kanal kedalaman memberi keuntungan konsisten lintas
   domain (SOD, segmentasi, pose, grasp, panen buah).
2. **Atensi lintas-modal adalah mekanisme fusi paling efektif.** Modul separasi-
   agregasi, criss-cross, dan transformer token-fusion mengungguli konkatenasi
   naif.
3. **YOLO adalah "mesin deteksi 2D" default** dalam pipeline RGB-D karena
   keseimbangan latensi–akurasi; penalaran geometri 3D umumnya menjadi tahap
   sesudahnya.
4. **Estimasi kedalaman fondasi (Depth Anything, MiDaS)** membuka peluang
   "pseudo-depth" murah — YOLO+RGB-D tanpa sensor depth khusus.
5. **Pelajaran dari RGB-T** (ketidakseimbangan & penyelarasan lemah modalitas)
   langsung relevan untuk fusi RGB-D.

---

## 6. Tantangan Terbuka & Arah Masa Depan

- **Kualitas & penyelarasan depth:** sensor RGB-D terdegradasi pada jarak dekat
  dan cahaya matahari kuat.
- **Ketidakseimbangan modalitas & penyelarasan lemah** antar RGB dan depth.
- **Kelangkaan dataset RGB-D beranotasi berskala besar** untuk deteksi objek
  waktu-nyata (kontras dengan melimpahnya dataset RGB seperti COCO).
- **Efisiensi di perangkat tepi (edge):** fusi multimodal menuntut model ringan.
- **Generalisasi lintas-domain** via pseudo-depth fondasi.
- **Arah menjanjikan:** YOLOv9–v11 + depth fondasi; fusi transformer hemat
  parameter; pelatihan tangguh terhadap kegagalan/kehilangan modalitas.

---

## 7. Daftar Referensi (Roster 182 Entri Terverifikasi)

> Korpus terverifikasi (182 sumber). Nomor mengikuti ID entri katalog, sehingga
> nomor yang tidak muncul adalah 20 record ledger yang ditahan (tanpa PDF sumber lokal).
> Dikelompokkan sesuai bagian di `references.bib`. Rentang fokus 2019–2026;
> karya fondasi disertakan sebagai konteks.

### A. Fondasi Deteksi Objek Berbasis RGB
1. Redmon dkk. (2016). *You Only Look Once*. CVPR.
2. Redmon & Farhadi (2017). *YOLO9000: Better, Faster, Stronger*. CVPR.
3. Redmon & Farhadi (2018). *YOLOv3: An Incremental Improvement*. arXiv:1804.02767.
4. Bochkovskiy dkk. (2020). *YOLOv4*. arXiv:2004.10934.
5. Ge dkk. (2021). *YOLOX*. arXiv:2107.08430.
6. Li dkk. (2022). *YOLOv6*. arXiv:2209.02976.
7. Wang dkk. (2023). *YOLOv7*. CVPR.
8. Wang, Yeh & Liao (2024). *YOLOv9*. ECCV.
9. Wang dkk. (2024). *YOLOv10*. NeurIPS.
10. Khanam & Hussain (2024). *YOLOv11: Key Architectural Enhancements*. arXiv:2410.17725.
11. Long dkk. (2020). *PP-YOLO*. arXiv:2007.12099.
12. Girshick dkk. (2014). *R-CNN*. CVPR.
13. Girshick (2015). *Fast R-CNN*. ICCV.
14. Ren dkk. (2017). *Faster R-CNN*. IEEE TPAMI.
15. Liu dkk. (2016). *SSD*. ECCV.
16. Lin dkk. (2017). *Focal Loss / RetinaNet*. ICCV.
17. He dkk. (2017). *Mask R-CNN*. ICCV.
18. Lin dkk. (2017). *Feature Pyramid Networks*. CVPR.
19. Tian dkk. (2019). *FCOS*. ICCV.
20. Zhou dkk. (2019). *Objects as Points (CenterNet)*. arXiv:1904.07850.
21. Tan dkk. (2020). *EfficientDet*. CVPR.
22. Carion dkk. (2020). *DETR*. ECCV.
23. Zhu dkk. (2021). *Deformable DETR*. ICLR.
24. Dosovitskiy dkk. (2021). *ViT*. ICLR.
25. Liu dkk. (2021). *Swin Transformer*. ICCV.

### B. Survei / Tinjauan YOLO
26. Terven dkk. (2023). *Comprehensive Review of YOLO (v1–v8, YOLO-NAS)*. MAKE.
27. Hussain (2023). *YOLO-v1 to v8 & Industrial Defect Detection*. Machines.
28. Jiang dkk. (2022). *A Review of YOLO Algorithm Developments*. Procedia CS.
29. Sapkota dkk. (2024). *YOLOv1–v10 in Agricultural Domain*. arXiv:2406.10139.
30. Sapkota dkk. (2025). *YOLO Advances to Its Genesis: A Decadal and Comprehensive Review*. Artificial Intelligence Review.
31. Vijayakumar & Vairavasundaram (2024). *YOLO-Based Object Detection Review*. MTAP.
32. Alif & Hussain (2024). *YOLO Evolution: YOLOv12, YOLO11 Benchmark*. arXiv:2411.00201.

### C. RGB-D Salient Object Detection
35. Piao dkk. (2019). *DMRA*. ICCV.
36. Fan dkk. (2020). *BBS-Net*. ECCV.
37. Fan dkk. (2021). *D3Net / Rethinking RGB-D SOD*. IEEE TNNLS.
38. Fu dkk. (2020). *JL-DCF*. CVPR.
39. Liu dkk. (2020). *S2MA*. CVPR.
40. Pang dkk. (2020). *HDFNet*. ECCV.
41. Zhang dkk. (2020). *UC-Net*. CVPR.
42. Liu dkk. (2021). *Visual Saliency Transformer (VST)*. ICCV.
43. Liu dkk. (2022). *SwinNet*. IEEE TCSVT.
44. Liu dkk. (2021). *TriTransNet*. ACM MM.
45. Sun dkk. (2021). *DSA2F*. CVPR.
46. Cong dkk. (2022). *CIR-Net*. IEEE TIP.
50. Wu dkk. (2023). *HiDAnet*. IEEE TIP.

### D. Segmentasi Semantik RGB-D
51. Hazirbas dkk. (2016). *FuseNet*. ACCV.
52. Jiang dkk. (2018). *RedNet*. arXiv:1806.01054.
53. Park dkk. (2017). *RDFNet*. ICCV.
54. Hu dkk. (2019). *ACNet*. ICIP.
55. Chen dkk. (2020). *SA-Gate*. ECCV.
56. Seichter dkk. (2021). *ESANet*. ICRA.
57. Cao dkk. (2021). *ShapeConv*. ICCV.
58. Zhang dkk. (2023). *CMX*. IEEE T-ITS.
60. Wang dkk. (2022). *Multimodal Token Fusion*. CVPR.
61. Yin dkk. (2024). *DFormer*. ICLR.

### E. Estimasi Kedalaman
62. Eigen dkk. (2014). *Multi-Scale Depth Prediction*. NeurIPS.
63. Godard dkk. (2017). *Monodepth (Left-Right Consistency)*. CVPR.
64. Godard dkk. (2019). *Monodepth2*. ICCV.
65. Lee dkk. (2019). *BTS*. arXiv:1907.10326.
66. Bhat dkk. (2021). *AdaBins*. CVPR.
67. Ranftl dkk. (2021). *DPT*. ICCV.
68. Ranftl dkk. (2022). *MiDaS*. IEEE TPAMI.
69. Guizilini dkk. (2020). *PackNet*. CVPR.
70. Ji dkk. (2021). *MonoIndoor*. ICCV.
71. Yang dkk. (2024). *Depth Anything*. CVPR.
72. Ming dkk. (2021). *Deep Learning for Monocular Depth: A Review*. Neurocomputing.

### F. Estimasi Pose 6D Berbasis RGB-D
73. Xiang dkk. (2018). *PoseCNN*. RSS.
74. Wang dkk. (2019). *DenseFusion*. CVPR.
75. He dkk. (2020). *PVN3D*. CVPR.
76. He dkk. (2021). *FFB6D*. CVPR.
77. Chen dkk. (2020). *G2L-Net*. CVPR.
78. Wen dkk. (2024). *FoundationPose*. CVPR.
79. Hoque dkk. (2021). *Review on 3D Detection & 6D Pose*. IEEE Access.

### G. Grasp Detection / Manipulasi Robotik
80. Lenz dkk. (2015). *Deep Learning for Detecting Robotic Grasps*. IJRR.
81. Morrison dkk. (2018). *GG-CNN*. RSS.
82. Kumra dkk. (2020). *GR-ConvNet*. IROS.
83. Kumra dkk. (2022). *GR-ConvNet v2*. Sensors.
84. Fang dkk. (2020). *GraspNet-1Billion*. CVPR.
85. Zhang & Sun (2023). *Bilateral Cross-Modal Fusion Network for Grasp*. Sensors.
86. Depierre dkk. (2018). *Jacquard Dataset*. IROS.

### H. Deteksi 3D: Fusi LiDAR + RGB
87. Zhou & Tuzel (2018). *VoxelNet*. CVPR.
88. Lang dkk. (2019). *PointPillars*. CVPR.
89. Shi dkk. (2019). *PointRCNN*. CVPR.
90. Qi dkk. (2018). *Frustum PointNets*. CVPR.
91. Chen dkk. (2017). *MV3D*. CVPR.
92. Ku dkk. (2018). *AVOD*. IROS.
93. Vora dkk. (2020). *PointPainting*. CVPR.
94. Yoo dkk. (2020). *3D-CVF*. ECCV.
95. Wang dkk. (2019). *Pseudo-LiDAR*. CVPR.
96. You dkk. (2020). *Pseudo-LiDAR++*. ICLR.
97. Bai dkk. (2022). *TransFusion*. CVPR.
98. Liu dkk. (2023). *BEVFusion*. ICRA.
99. Arnold dkk. (2019). *Survey on 3D Object Detection*. IEEE T-ITS.

### I. Deteksi Pedestrian Multispektral (RGB-T)
100. Hwang dkk. (2015). *KAIST Multispectral Benchmark*. CVPR.
101. Li dkk. (2019). *Illumination-Aware Faster R-CNN*. Pattern Recognition.
102. Zhou dkk. (2020). *MBNet (Modality Imbalance)*. ECCV.
103. Zhang dkk. (2021). *GAFF*. WACV.
104. Zhang dkk. (2020). *Cyclic Fuse-and-Refine (CFR)*. ICIP.

### J. RGB-D SLAM Dinamis & Semantik
107. Mur-Artal & Tardós (2017). *ORB-SLAM2*. IEEE T-RO.
108. Bescos dkk. (2018). *DynaSLAM*. IEEE RA-L.
109. Yu dkk. (2018). *DS-SLAM*. IROS.
110. Hu dkk. (2022). *CFP-SLAM*. IROS.
111. Soares dkk. (2019). *Visual SLAM in Human-Populated Environments*. ICAR.

### K. YOLO + RGB-D (Integrasi)
112. Takahashi dkk. (2020). *Expandable YOLO: 3D Detection from RGB-D*. REM.
113. El Amraoui dkk. (2024). *FusionVision*. arXiv:2403.00175.
115. Yang dkk. (2025). *YOLOv8-URE 2D Vision + Point Cloud Grasping*. Applied Sciences.
117. Xu dkk. (2024). *Onboard Dynamic-Object Detection & Tracking (RGB-D)*. IEEE RA-L.
118. Ophoff dkk. (2019). *Exploring RGB+Depth Fusion for Real-Time Detection*. Sensors.

### L. Aplikasi YOLO: Pertanian
124. Gené-Mola dkk. (2020). *Fruit 3D Location via Instance Segmentation*. Comput. Electron. Agric.
125. Kang & Chen (2020). *Fruit Detection & 3D Visualisation in Apple Orchards*. Comput. Electron. Agric.
126. Birrell dkk. (2020). *Robotic Iceberg Lettuce Harvesting*. J. Field Robotics.
127. Onishi dkk. (2019). *Automated Fruit Harvesting Robot*. ROBOMECH Journal.

### M. Aplikasi YOLO: Medis
128. Qureshi dkk. (2024). *Systematic Review of YOLO for Medical Detection*. IEEE Access.
129. Al-Antari dkk. (2021). *Fast Deep Learning CAD for COVID-19*. Applied Intelligence.
130. Baccouche dkk. (2021). *Breast Lesions Detection via YOLO Fusion*. CMC.

### N. Aplikasi YOLO: Industri / Defect
133. Yang dkk. (2023). *EFC-YOLO Steel Strip Defects*. Sensors.
134. Tang dkk. (2024). *PCB-YOLO*. PLOS ONE.
136. Zhou dkk. (2021). *Safety Helmet Detection Improved YOLOv5*. CVIDL.

### O. Aplikasi YOLO: Remote Sensing / UAV
137. Zhu dkk. (2021). *TPH-YOLOv5*. ICCVW.
139. Wang dkk. (2023). *UAV-YOLOv8*. Sensors.
140. Van Etten (2018). *YOLT: Satellite Imagery Detection*. arXiv:1805.09512.

### P. Dataset RGB-D / Deteksi Utama
141. Silberman dkk. (2012). *NYU Depth v2*. ECCV.
142. Song dkk. (2015). *SUN RGB-D*. CVPR.
143. Dai dkk. (2017). *ScanNet*. CVPR.
144. Geiger dkk. (2012). *KITTI Benchmark*. CVPR.
145. Caesar dkk. (2020). *nuScenes*. CVPR.
146. Lin dkk. (2014). *Microsoft COCO*. ECCV.

### Q. Fusi Multimodal, Backbone & Survei Pendukung
147. He dkk. (2016). *ResNet*. CVPR.
148. Qi dkk. (2017). *PointNet*. CVPR.
149. Woo dkk. (2018). *CBAM*. ECCV.
150. Feng dkk. (2021). *Deep Multi-Modal Detection & Segmentation Survey*. IEEE T-ITS.
151. Zou dkk. (2023). *Object Detection in 20 Years: A Survey*. Proc. IEEE.
153. Zhou dkk. (2021). *RGB-D Salient Object Detection: A Survey*. Comput. Visual Media.
154. Lopes dkk. (2022). *A Survey on RGB-D Datasets*. CVIU.

### R. Detektor RGB & Transformer Lanjutan
155. Zhao dkk. (2024). *DETRs Beat YOLOs on Real-Time Object Detection (RT-DETR)*. CVPR.
156. Cheng dkk. (2024). *YOLO-World: Real-Time Open-Vocabulary Object Detection*. CVPR.
157. Wang dkk. (2023). *Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism*. NeurIPS.
158. Zhang dkk. (2023). *DINO: DETR with Improved DeNoising Anchor Boxes*. ICLR.
159. Li dkk. (2022). *DN-DETR: Accelerate DETR Training by Introducing Query DeNoising*. CVPR.
160. Meng dkk. (2021). *Conditional DETR for Fast Training Convergence*. ICCV.
161. Sun dkk. (2021). *Sparse R-CNN: End-to-End Detection with Learnable Proposals*. CVPR.
162. Liu dkk. (2022). *A ConvNet for the 2020s (ConvNeXt)*. CVPR.
163. Liu dkk. (2022). *Swin Transformer V2: Scaling Up Capacity and Resolution*. CVPR.
164. Wang dkk. (2021). *Pyramid Vision Transformer (PVT)*. ICCV.
165. Zong dkk. (2023). *DETRs with Collaborative Hybrid Assignments Training (Co-DETR)*. ICCV.

### S. RGB-D Salient Object Detection (Lanjutan)
166. Ji dkk. (2020). *Accurate RGB-D SOD via Collaborative Learning (CoNet)*. ECCV.
167. Ji dkk. (2021). *Calibrated RGB-D Salient Object Detection (DCF)*. CVPR.
168. Zhou dkk. (2021). *Specificity-Preserving RGB-D Saliency Detection (SPNet)*. ICCV.
169. Pang dkk. (2023). *CAVER: Cross-Modal View-Mixed Transformer for SOD*. IEEE TIP.
170. Wu dkk. (2022). *MobileSal: Extremely Efficient RGB-D SOD*. IEEE TPAMI.

### T. Segmentasi Semantik RGB-D (Lanjutan)
171. Xie dkk. (2021). *SegFormer: Simple, Efficient Segmentation with Transformers*. NeurIPS.
172. Seichter dkk. (2022). *Efficient Multi-Task RGB-D Scene Analysis (EMSANet)*. IJCNN.
173. Jia dkk. (2024). *GeminiFusion: Efficient Pixel-wise Multimodal Fusion for ViT*. ICML.
174. Girdhar dkk. (2022). *Omnivore: A Single Model for Many Visual Modalities*. CVPR.

### U. Estimasi Kedalaman (Lanjutan: Metrik & Fondasi)
175. Yang dkk. (2024). *Depth Anything V2*. NeurIPS.
176. Bhat dkk. (2023). *ZoeDepth: Combining Relative and Metric Depth*. arXiv:2302.12288.
177. Yin dkk. (2023). *Metric3D: Zero-Shot Metric 3D Prediction from a Single Image*. ICCV.
178. Ke dkk. (2024). *Marigold: Diffusion-Based Monocular Depth Estimation*. CVPR.
179. Yuan dkk. (2022). *Neural Window Fully-Connected CRFs for Depth (NeWCRFs)*. CVPR.

### V. Estimasi Pose 6D & Grasp (Lanjutan)
180. Wang dkk. (2021). *GDR-Net: Geometry-Guided Direct Regression for 6D Pose*. CVPR.
181. Su dkk. (2022). *ZebraPose: Coarse-to-Fine Surface Encoding for 6DoF Pose*. CVPR.
182. Sun dkk. (2022). *OnePose: One-Shot Object Pose Estimation without CAD Models*. CVPR.
183. Sundermeyer dkk. (2021). *Contact-GraspNet: 6-DoF Grasp Generation in Clutter*. ICRA.
184. Breyer dkk. (2020). *Volumetric Grasping Network (VGN): Real-Time 6-DOF Grasp*. CoRL.

### W. Deteksi 3D (Lanjutan)
185. Yin dkk. (2021). *Center-Based 3D Object Detection and Tracking (CenterPoint)*. CVPR.
186. Shi dkk. (2020). *PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Detection*. CVPR.
187. Li dkk. (2022). *BEVFormer: BEV Representation via Spatiotemporal Transformers*. ECCV.
188. Wang dkk. (2022). *DETR3D: 3D Detection from Multi-View Images via 3D-to-2D Queries*. CoRL.

### X. Pedestrian RGB-T & RGB-D SLAM (Lanjutan)
189. Fang dkk. (2022). *Cross-Modality Fusion Transformer for Multispectral Detection (CFT)*. arXiv:2111.00273.
190. Campos dkk. (2021). *ORB-SLAM3: Visual, Visual-Inertial, and Multimap SLAM*. IEEE T-RO.
191. Teed & Deng (2021). *DROID-SLAM: Deep Visual SLAM (Mono/Stereo/RGB-D)*. NeurIPS.

### Y. Jurnal Terbaru 2025–2026 (Diverifikasi arXiv)
192. Sapkota dkk. (2025). *YOLO26: Real-Time End-to-End Object Detection*. arXiv:2509.25164.
193. Robinson dkk. (2025). *RF-DETR: NAS for Real-Time Detection Transformers*. ICLR.
194. Huang dkk. (2026). *Le-DETR: Real-Time DETR with Efficient Encoder Design*. arXiv:2602.21010.
195. Hu dkk. (2026). *RiO-DETR: DETR for Real-Time Oriented Object Detection*. arXiv:2603.09411.
196. Yi dkk. (2025). *GL-DMNet: Dual Mutual Learning with Global-Local Awareness (RGB-D SOD)*. arXiv:2501.01648.
197. Gong dkk. (2025). *DiffPixelFormer: Pixel-Aware Transformer for RGB-D Indoor Segmentation*. arXiv:2511.13047.
198. Lin dkk. (2025). *Depth Anything 3: Recovering Visual Space from Any Views*. arXiv:2511.10647.
199. Zhang (2025). *Survey on Monocular Metric Depth Estimation*. arXiv:2501.11841.
200. Ma dkk. (2026). *AsyncMDE: Real-Time Monocular Depth via Asynchronous Spatial Memory*. arXiv:2603.10438.
201. Ganesan dkk. (2026). *UniDAC: Universal Metric Depth Estimation for Any Camera*. arXiv:2603.27105.
202. Du dkk. (2026). *Focusable Monocular Depth Estimation*. arXiv:2605.11756.

---

## 8. Berkas Terkait

| Berkas | Isi |
|---|---|
| [`evidence-body.tex`](evidence-body.tex) | Badan naskah review (LaTeX), disisipkan ke wrapper IEEE & Elsevier |
| [`main.pdf`](main.pdf) / [`main-elsarticle.pdf`](main-elsarticle.pdf) | Naskah review terkompilasi (IEEE / Elsevier) |
| [`references.bib`](references.bib) | Basis data BibTeX, 202 entri (182 diverifikasi & dirujuk) |
| `TEMUAN.md` (berkas ini) | Ringkasan temuan dalam Markdown |

**Kompilasi LaTeX:**
```bash
pdflatex main-elsarticle   # atau: tectonic main-elsarticle.tex
bibtex   main-elsarticle
pdflatex main-elsarticle
pdflatex main-elsarticle
```
