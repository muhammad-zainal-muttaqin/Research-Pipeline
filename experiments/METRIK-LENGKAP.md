# Metrik lengkap seluruh run E-022/G7/G8 — protokol tunggal

Tabel rujukan untuk **semua** run pada SawitMVC-Depth, split test 72 pohon /
288 citra / 504 kotak. Seluruh angka lewat **pycocotools**, protokol yang
dibekukan [E-025] setelah terbukti bahwa evaluator internal trainer tidak boleh
dipakai membandingkan antar lengan.

Sumber: [`experiments/results/E-022/metrics_lengkap.json`](results/E-022/metrics_lengkap.json)
(berisi pula AP per kelas pada kedua ambang dan provenans tiap checkpoint).
Skrip: [`experiments/code/eval/metrics_lengkap.py`](code/eval/metrics_lengkap.py).

**Angka di sini bukan hasil final yang boleh dikutip.** Seluruh klaim positif
E-022 dicabut ([E-027], [E-029]); tabel ini adalah rekam terukur, bukan capaian.
Hasil final yang boleh dikutip tetap [METRICS.md](METRICS.md) (E-021, dataset
lain).

## Konvensi

- **P / R / F1** pada conf 0,25 dan IoU 0,5, pencocokan serakah, tiap kotak GT
  hanya boleh dipakai sekali. Ini angka **operasional** pada satu ambang, bukan
  integral kurva — jadi tidak sebanding dengan mAP.
- **mAP50 / mAP50-95** dari matriks presisi COCOeval, seluruh kelas.
- Prediksi: conf 0,001, NMS IoU 0,7, `max_det` 300, imgsz 640.

## RT-DETR-L (33,0 jt parameter)

| Run | mAP50 | mAP50-95 | P | R | F1 | TP |
|---|---:|---:|---:|---:|---:|---:|
| rgb seed42 | 0,4282 | 0,1450 | 0,312 | 0,744 | 0,440 | 375 |
| rgb seed1337 | 0,4142 | 0,1467 | 0,317 | 0,754 | 0,446 | 380 |
| rgb seed2024 | 0,3523 | 0,1168 | 0,303 | 0,673 | 0,418 | 339 |
| rgbd seed42 | 0,3932 | 0,1371 | 0,291 | 0,762 | 0,421 | 384 |
| rgbd seed1337 | 0,4233 | 0,1451 | 0,343 | 0,758 | 0,472 | 382 |
| rgbd seed2024 | 0,4225 | 0,1472 | 0,376 | 0,728 | 0,496 | 367 |
| derau seed42 | 0,3749 | 0,1227 | 0,287 | 0,734 | 0,412 | 370 |
| derau seed1337 | 0,4066 | 0,1390 | 0,240 | 0,750 | 0,363 | 378 |
| derau seed2024 | 0,4171 | 0,1453 | 0,355 | 0,693 | 0,469 | 349 |

## YOLO26n (2,57 jt parameter)

| Run | mAP50 | mAP50-95 | P | R | F1 | TP |
|---|---:|---:|---:|---:|---:|---:|
| rgb seed42 | 0,3479 | 0,1208 | 0,548 | 0,468 | 0,505 | 236 |
| rgb seed1337 | 0,3428 | 0,1212 | 0,571 | 0,439 | 0,496 | 221 |
| rgb seed2024 | 0,3749 | 0,1354 | 0,567 | 0,456 | 0,505 | 230 |
| rgbd seed42 | 0,3583 | 0,1225 | 0,585 | 0,490 | 0,533 | 247 |
| rgbd seed1337 | 0,3014 | 0,1006 | 0,531 | 0,468 | 0,498 | 236 |
| rgbd seed2024 | 0,3371 | 0,1286 | 0,558 | 0,411 | 0,473 | 207 |
| derau seed42 | 0,3511 | 0,1323 | 0,523 | 0,434 | 0,474 | 219 |
| derau seed1337 | 0,3443 | 0,1181 | 0,564 | 0,508 | 0,534 | 256 |
| derau seed2024 | 0,3318 | 0,1143 | 0,564 | 0,454 | 0,503 | 229 |
| tukar seed42 | 0,3393 | 0,1172 | 0,539 | 0,484 | 0,510 | 244 |
| tukar seed1337 | 0,3286 | 0,1196 | 0,526 | 0,427 | 0,471 | 215 |
| tukar seed2024 | 0,3412 | 0,1194 | 0,547 | 0,484 | 0,514 | 244 |

## Sapuan kapasitas G7 (seed 42)

| Run | Param | mAP50 | mAP50-95 | P | R | F1 |
|---|---:|---:|---:|---:|---:|---:|
| yolo26m rgb | 21,9 jt | 0,3346 | 0,1088 | 0,553 | 0,484 | 0,516 |
| yolo26m rgbd | 21,9 jt | 0,3260 | 0,1135 | 0,516 | 0,480 | 0,497 |
| yolo26m derau | 21,9 jt | 0,3530 | 0,1134 | 0,573 | 0,530 | 0,550 |
| yolo26l rgb | 26,3 jt | 0,3557 | 0,1207 | 0,569 | 0,482 | 0,522 |

Lengan `yolo26l` rgbd dan derau masih berjalan.

## Satu pengamatan yang hanya terlihat dari P/R

**RT-DETR-L dan YOLO26 beroperasi pada titik kerja yang berlawanan.** RT-DETR-L
mencapai recall 0,67–0,76 dengan precision 0,24–0,38; keluarga YOLO26 kebalikannya,
precision 0,52–0,59 dengan recall 0,41–0,53. mAP50 keduanya berdekatan (0,35–0,43),
jadi perbedaan perilaku ini **tidak terlihat sama sekali** dari mAP.

Konsekuensinya praktis: untuk penghitungan tandan, detektor ber-recall tinggi
lebih berguna karena kotak berlebih dapat disaring tahap berikutnya sementara
tandan yang terlewat hilang selamanya. Itu argumen memilih RT-DETR-L yang tidak
bersandar pada mAP — dan tidak pernah muncul di catatan mana pun sebelum tabel
ini dibuat.

## Provenans, karena bobot tidak diarsipkan

Kebijakan repo tidak menyimpan checkpoint, jadi angka ini tidak dapat
diverifikasi dengan membuka bobotnya. JSON sumber mencatat **SHA-256 dan ukuran
byte** tiap `best.pt`, jumlah epoch tercatat, dan modalitas kanal ke-4. Gunanya:
bila hasil latih-ulang berbeda, hash memberi tahu apakah checkpoint-nya memang
lain atau resepnya yang tidak tereproduksi — dua kemungkinan yang tanpa ini
tidak dapat dibedakan.
