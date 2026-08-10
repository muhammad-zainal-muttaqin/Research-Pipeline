# Prioritas full-text review

Tanggal: 2026-08-10
Rule version: `priority-v1.0-title-abstract-scored-diversified`

## Keputusan metodologis

20.035 record adalah search pool setelah deduplikasi dan title-abstract screening. Tidak semua record dijanjikan untuk dibaca full text. Ranking ini memilih studi yang paling relevan dengan inventaris buah unik lintas-observasi, studi sawit, studi buah dengan bukti instance atau 3D, review terdahulu, dan mekanisme transfer yang mendukung.

Skor hanya alat prioritas. Skor tidak mengubah keputusan inklusi, tidak menghapus record, dan tidak menggantikan verifikasi full text.

## Sinyal yang digunakan

- Sinyal inti: unique inventory, duplicate resolution, re-identification, cross-view, tracking, association, SfM/MVS/stereo, point cloud, RGB-D, depth, dan 3D reconstruction.
- Sinyal target: fruit, fruitlet, berry, bunch, apple, mango, citrus, grape, tomato, oil palm, dan FFB.
- Sinyal pendukung: instance detection/segmentation, counting, ripeness, benchmark/dataset, prior review, dan mekanisme tracking atau geometry dari domain lain.
- Penalti: global yield/biomass/land-use output, canopy or remote sensing only, non-fruit disease/weed targets, dan image-level output.

## Diversifikasi shortlist

Shortlist dipilih dengan kuota bucket agar hasil tidak didominasi satu keluarga YOLO atau satu domain. Angka dalam kurung adalah target maksimum:

- 60 core identity or inventory (target 60)
- 45 oil-palm direct (target 45)
- 65 fruit multiview or 3D (target 65)
- 40 fruit instance baselines (target 40)
- 30 transfer mechanisms (target 30)
- 10 prior reviews or positioning (target maximum 20; remaining shortlist capacity after earlier quotas)
- global score fill sampai 250 record

## Rekap hasil

- Ranking lengkap: 20035 record
- Shortlist: 250 record
- Status shortlist: 26 reviewed, 11 perlu retrieval manual, 213 pending
- Tier: {'A': 60, 'B': 110, 'C': 40, 'D': 40}
- Bucket kuota yang terisi: {'core_identity_or_inventory': 60, 'oil_palm_direct': 45, 'fruit_multiview_or_3d': 65, 'fruit_instance_baseline': 40, 'transfer_mechanism': 30, 'prior_review_or_positioning': 10}

File ranking menyimpan skor, komponen skor, alasan, penalti, bucket, dan status ledger sehingga keputusan dapat diaudit dan diubah tanpa mengubah data mentah.
