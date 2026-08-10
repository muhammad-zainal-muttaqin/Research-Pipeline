# Deduplication review, 2026-08-09

Laporan ini hanya memuat kelompok residual yang belum dapat diputuskan sepenuhnya secara otomatis. Laporan ini untuk spot-check dan tidak menghalangi screening judul-abstrak.

- Kelompok residual untuk spot-check: **22**
- Kandidat yang ditampilkan: **55**
- Pilihan keputusan: `merge` atau `keep_separate`.
- CSV ringkas di sebelah file ini bersifat opsional dan dapat dipakai untuk mengisi keputusan serta catatan.

## Cara membaca

`keep_separate_conservative` berarti record tidak digabung karena bukti penulis, venue, DOI, atau metadata belum cukup. `partial_merge_author_match` berarti sebagian kandidat sudah cocok, tetapi ada kandidat lain yang tetap dipisahkan.

## MR-0237

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-8ce1723c9f2b0cea \| R-f074da0fc75e5f3c`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-8ce1723c9f2b0cea | 10.5194/egusphere-2025-3919-rc1 | Comment on egusphere-2025-3919 | 2025 | Bates, Jordan; Montzka, Carsten; Vereecken, Harry; Jonard, François |  | OpenAlex | keep separate saat ini |  | |
| R-f074da0fc75e5f3c | 10.5194/egusphere-2025-3919-rc2 | Comment on egusphere-2025-3919 | 2025 | William Kustas |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0312

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-46e45c933ccac073 \| R-a09e40f2bb89f151`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-46e45c933ccac073 | 10.1109/tgrs.2025.3542685/v1/decision1 | Decision letter for "Integrating Sparse LiDAR and Multisensor Time-Series Imagery From Spaceborne Platforms for Deriving Localized Canopy Height Model" | 2024 |  |  | OpenAlex | keep separate saat ini |  | |
| R-a09e40f2bb89f151 | 10.1109/tgrs.2025.3542685/v2/decision1 | Decision letter for "Integrating Sparse LiDAR and Multisensor Time-Series Imagery From Spaceborne Platforms for Deriving Localized Canopy Height Model" | 2024 |  |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0373

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-396842f6fff1d39f \| R-70b49ea0143a5a6b`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-396842f6fff1d39f | 10.1109/jstars.2024.3410515 | Edge-Cloud Remote Sensing Data-Based Plant Disease Detection Using Deep Neural Networks with Transfer Learning | 2024 | Mohammed, Mazin Abed (57192089894); Lakhan, Abdullah (57209259574); Abdulkareem, Karrar Hameed (57197854295); Almujally, Nouf Abdullah (57193325656); Al-Attar, Bourair (57224767048); Memon, Sajida (58882277200); Marhoon, Haydar Abdulameer (56532476900); Martinek, Radek (36537543900) | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing | Scopus;OpenAlex | keep separate saat ini |  | |
| R-70b49ea0143a5a6b | 10.15680/ijircce.2024.1210061 | Edge-Cloud Remote Sensing Data-Based Plant Disease Detection Using Deep Neural Networks with Transfer Learning. | 2024 | K. Mala; N Kavya | International Journal of Innovative Research in Computer and Communication Engineering | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`
- `literature/search/raw/scopus_Q3_2026-08-09.csv`

## MR-0545

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-8191a7bb05d4be2b \| R-c4f5e077cc4ece52 \| R-e5f061a2703a3919`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-8191a7bb05d4be2b | 10.1108/978-1-78714-619-820181026 | Index | 2018 |  |  | OpenAlex | keep separate saat ini |  | |
| R-c4f5e077cc4ece52 | 10.1108/s1745-886220180000013018 | Index | 2018 |  |  | OpenAlex | keep separate saat ini |  | |
| R-e5f061a2703a3919 | 10.1108/978-1-78743-289-520181015 | Index | 2018 |  |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0546

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-047d086615c6833b \| R-88b3575fb306dd7e \| R-f46b9793dedae3e6`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-047d086615c6833b | 10.1108/978-1-78756-983-620191020 | Index | 2019 |  |  | OpenAlex | keep separate saat ini |  | |
| R-88b3575fb306dd7e | 10.1108/s0733-558x20190000062024 | Index | 2019 |  | Research in the sociology of organizations | OpenAlex | keep separate saat ini |  | |
| R-f46b9793dedae3e6 | 10.1108/978-1-78973-073-920191017 | Index | 2019 |  |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`

## MR-0547

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-74d96cf8063f525d \| R-83497cabd6fd4768 \| R-a86b9ef7fe8301e1 \| R-dec0bffa0e2f109e`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-74d96cf8063f525d | 10.1108/978-1-80117-686-620221034 | Index | 2022 |  |  | OpenAlex | keep separate saat ini |  | |
| R-83497cabd6fd4768 | 10.1108/s1877-636120220000027015 | Index | 2022 |  |  | OpenAlex | keep separate saat ini |  | |
| R-a86b9ef7fe8301e1 | 10.1108/978-1-80071-597-420221045 | Index | 2022 |  |  | OpenAlex | keep separate saat ini |  | |
| R-dec0bffa0e2f109e | 10.1108/978-1-83982-544-620221020 | Index | 2022 |  |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q5_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q6_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q7_2026-07-23.csv`

## MR-0548

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-641b6ad494aa1254 \| R-a5e6610a9b870817 \| R-bc15ff55daa3f645 \| R-d880f31afa441125`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-641b6ad494aa1254 | 10.1108/978-1-80262-277-520231024 | Index | 2023 |  |  | OpenAlex | keep separate saat ini |  | |
| R-a5e6610a9b870817 | 10.1002/9781394171538.index | Index | 2023 | Lawrence R. Griffing |  | OpenAlex | keep separate saat ini |  | |
| R-bc15ff55daa3f645 | 10.1108/978-1-80455-562-020231021 | Index | 2023 |  |  | OpenAlex | keep separate saat ini |  | |
| R-d880f31afa441125 | 10.1108/s1479-355520230000021008 | Index | 2023 |  | Research in occupational stress and well being | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q5_2026-07-23.csv`
- `literature/search-data/raw/openalex_Q7_2026-07-23.csv`

## MR-0562

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-303ecf15f4fa0348 \| R-67c8c3f01d0ba848 \| R-d673c7a14ea320dd`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-303ecf15f4fa0348 | 10.4103/jasi.jasi_101_24 | Instructions to Author | 2024 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |
| R-67c8c3f01d0ba848 | 10.4103/jasi.jasi_155_24 | Instructions to Author | 2024 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |
| R-d673c7a14ea320dd | 10.4103/jasi.jasi_203_24 | Instructions to Author | 2024 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`

## MR-0563

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-20bd39c8221cd83b \| R-4137d30e3daeb6a5 \| R-acebb1e35b19dc6d`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-20bd39c8221cd83b | 10.4103/jasi.jasi_110_25 | Instructions to Author | 2025 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |
| R-4137d30e3daeb6a5 | 10.4103/jasi.jasi_69_25 | Instructions to Author | 2025 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |
| R-acebb1e35b19dc6d | 10.4103/jasi.jasi_152_25 | Instructions to Author | 2025 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`

## MR-0564

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-5e6dd8fb9206f1a2 \| R-c4cc16ffa08ae4e3`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-5e6dd8fb9206f1a2 | 10.4103/jasi.jasi_62_26 | Instructions to Author | 2026 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |
| R-c4cc16ffa08ae4e3 | 10.4103/jasi.jasi_132_26 | Instructions to Author | 2026 |  | Journal of Anatomical Society of India | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`

## MR-0571

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-77e592a05413d558 \| R-cec478561abaf218`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-77e592a05413d558 | 10.14733/cadconfp.2015.389-394 | Interactive Collision Detection for Engineering Plants based on Large-Scale Point-Clouds | 2015 |  |  | OpenAlex | keep separate saat ini |  | |
| R-cec478561abaf218 | 10.14733/cadconfp.2015.338-342 | Interactive Collision Detection for Engineering Plants based on Large-Scale Point-Clouds | 2015 | Takeru Niwa; Hiroshi Masuda |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0614

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-13da2cfa6f9fd4fb \| R-424dedd96638e065`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-13da2cfa6f9fd4fb | 10.1016/j.compag.2025.110524 | MangoSense: A time-series vision sensing dataset for mango tree segmentation and detection toward yield prediction | 2025 | Ven, Janaksinh (58942219400); Sharma, Charu (59724779500); Syed, Azeemuddin (7801623099) | Computers and Electronics in Agriculture | Scopus;OpenAlex | keep separate saat ini |  | |
| R-424dedd96638e065 | 10.2139/ssrn.5195283 | Mangosense: A Time-Series Vision Sensing Dataset for Mango Tree Segmentation and Detection Toward Yield Prediction | 2025 | Joop van de Ven | SSRN Electronic Journal | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q7_2026-07-23.csv`
- `literature/search/raw/scopus_Q1_2026-08-09.csv`
- `literature/search/raw/scopus_Q7_2026-08-09.csv`

## MR-0676

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-60f66e9ef5819a4e \| R-a8fb9d2e25f6d71b`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-60f66e9ef5819a4e | 10.5281/zenodo.10041907 | NEON Tree Species Predictions | 2023 | Ben Weinstein; Ethan P. White | Zenodo (CERN European Organization for Nuclear Research) | OpenAlex | keep separate saat ini |  | |
| R-a8fb9d2e25f6d71b | 10.5281/zenodo.10067302 | NEON Tree Species Predictions | 2023 | Ben Weinstein; Sergio Marconi; Alina Zare; Stephanie Bohlman | Zenodo (CERN European Organization for Nuclear Research) | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0729

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-1740dc9a39f20878 \| R-4b72e9321aae1f5f`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-1740dc9a39f20878 | 10.5256/f1000research.190779.r433710 | Peer Review Report For: First photographic evidence of the Egyptian fruit bat, Rousettus aegyptiacus (Pteropodidae) in the King Salman Bin Abdulaziz Royal Nature Reserve, Hail Region, Saudi Arabia [version 2; peer review: 1 approved, 1 not approved] | 2025 | Maya M Juman |  | OpenAlex | keep separate saat ini |  | |
| R-4b72e9321aae1f5f | 10.5256/f1000research.190779.r433709 | Peer Review Report For: First photographic evidence of the Egyptian fruit bat, Rousettus aegyptiacus (Pteropodidae) in the King Salman Bin Abdulaziz Royal Nature Reserve, Hail Region, Saudi Arabia [version 2; peer review: 1 approved, 1 not approved] | 2025 | Barry W. Brook | University of Tasmania | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`

## MR-0763

**Keputusan saat ini:** `partial_merge_author_match`
**Dasar:** merge only author-matched components; retain other candidates separately
**Komponen:** `R-25dab8c6024f15f8+R-e62e031e21bda53e \| R-93693b2915de0edd`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-25dab8c6024f15f8 | 10.22323/1.397.0261 | Precision Luminosity Measurement with the CMS detector at HL-LHC | 2021 | C. Oropeza Barrera | Proceedings of The Ninth Annual Conference on Large Hadron Collider Physics — PoS(LHCP2021) | OpenAlex | merge saat ini dengan R-e62e031e21bda53e |  | |
| R-93693b2915de0edd | 10.22323/1.390.0864 | Precision luminosity measurement with the CMS detector at HL-LHC | 2021 | Pásztor, Gabriella (34572244600) | Proceedings of Science | Scopus;OpenAlex | keep separate saat ini |  | |
| R-e62e031e21bda53e |  | Precision luminosity measurement with the CMS detector at HL-LHC | 2021 | Barrera, Cristina Oropeza (58524304100) | Proceedings of Science | Scopus | merge saat ini dengan R-25dab8c6024f15f8 |  | |

Raw files:
- `literature/search-data/raw/openalex_Q1_2026-07-23.csv`
- `literature/search/raw/scopus_Q1_2026-08-09.csv`

## MR-0814

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-00ada2bd61b0685d \| R-ecece0eab7bb7bab`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-00ada2bd61b0685d | 10.5194/essd-2024-157-ac2 | Reply on RC1 | 2024 | Adrià Descals |  | OpenAlex | keep separate saat ini |  | |
| R-ecece0eab7bb7bab | 10.5194/egusphere-2024-378-ac1 | Reply on RC1 | 2024 | Ruiying Zhao |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q6_2026-07-23.csv`

## MR-0815

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-1f6961385de453ad \| R-5f2902df41b80c5a`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-1f6961385de453ad | 10.5194/egusphere-2024-4094-ac1 | Reply on RC1 | 2025 | Sofie Van Winckel |  | OpenAlex | keep separate saat ini |  | |
| R-5f2902df41b80c5a | 10.5194/egusphere-2025-2347-ac1 | Reply on RC1 | 2025 | Esteban Alonso‐González |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0816

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-0163b5570e8c180e \| R-b5bf7e5f3829dabd`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-0163b5570e8c180e | 10.5194/essd-2024-157-ac3 | Reply on RC2 | 2024 | Adrià Descals |  | OpenAlex | keep separate saat ini |  | |
| R-b5bf7e5f3829dabd | 10.5194/egusphere-2024-378-ac2 | Reply on RC2 | 2024 | Ruiying Zhao |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q6_2026-07-23.csv`

## MR-0817

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-5e73eb871be79935 \| R-7ef805bc2946b4a8`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-5e73eb871be79935 | 10.5194/egusphere-2024-4094-ac2 | Reply on RC2 | 2025 | Sofie Van Winckel |  | OpenAlex | keep separate saat ini |  | |
| R-7ef805bc2946b4a8 | 10.5194/egusphere-2025-2347-ac2 | Reply on RC2 | 2025 | Esteban Alonso‐González |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0825

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** insufficient author metadata; retained separately
**Komponen:** `R-0acb743dd0d5235e \| R-3741525fc2dfc978 \| R-6cd7b791654138f9 \| R-b2e3667be9478f93`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-0acb743dd0d5235e | 10.1109/tgrs.2025.3542685/v1/review2 | Review for "Integrating Sparse LiDAR and Multisensor Time-Series Imagery From Spaceborne Platforms for Deriving Localized Canopy Height Model" | 2024 |  |  | OpenAlex | keep separate saat ini |  | |
| R-3741525fc2dfc978 | 10.1109/tgrs.2025.3542685/v3/review1 | Review for "Integrating Sparse LiDAR and Multisensor Time-Series Imagery From Spaceborne Platforms for Deriving Localized Canopy Height Model" | 2024 |  |  | OpenAlex | keep separate saat ini |  | |
| R-6cd7b791654138f9 | 10.1109/tgrs.2025.3542685/v1/review1 | Review for "Integrating Sparse LiDAR and Multisensor Time-Series Imagery From Spaceborne Platforms for Deriving Localized Canopy Height Model" | 2024 |  |  | OpenAlex | keep separate saat ini |  | |
| R-b2e3667be9478f93 | 10.1109/tgrs.2025.3542685/v2/review1 | Review for "Integrating Sparse LiDAR and Multisensor Time-Series Imagery From Spaceborne Platforms for Deriving Localized Canopy Height Model" | 2024 |  |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q3_2026-07-23.csv`

## MR-0827

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-2d488ce4912e21a2 \| R-f83383124ed914ed`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-2d488ce4912e21a2 | 10.32388/s1p1ei | Review of: "Comparing YOLOv8 and Mask RCNN for object segmentation in complex orchard environments" | 2023 | Jyoti Snehi |  | OpenAlex | keep separate saat ini |  | |
| R-f83383124ed914ed | 10.32388/tv1hr6 | Review of: "Comparing YOLOv8 and Mask RCNN for object segmentation in complex orchard environments" | 2023 | Aayushi Gautam |  | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q5_2026-07-23.csv`

## MR-0921

**Keputusan saat ini:** `keep_separate_conservative`
**Dasar:** author or publication metadata differs below the merge threshold
**Komponen:** `R-7affa167a97b4f44 \| R-8d4e351299ef4487`

| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |
|---|---|---|---:|---|---|---|---|---|---|
| R-7affa167a97b4f44 | 10.37934/araset.53.1.237248 | Synthetic Image Data Generation via Rendering Techniques for Training AI-Based Instance Segmentation | 2024 | Dickson Yik Cheng Kho; Norazlianie Sazali; Ismayuzri Ishak; Saiful Anwar Che Ghani | Journal of Advanced Research in Applied Sciences and Engineering Technology | OpenAlex | keep separate saat ini |  | |
| R-8d4e351299ef4487 | 10.37934/araset.62.1.158169 | Synthetic Image Data Generation via Rendering Techniques for Training AI-Based Instance Segmentation | 2024 | Dickson Yik Cheng Kho; Norazlianie Sazali; Maurice Kettner; Christian Friedrich | Journal of Advanced Research in Applied Sciences and Engineering Technology | OpenAlex | keep separate saat ini |  | |

Raw files:
- `literature/search-data/raw/openalex_Q4_2026-07-23.csv`
