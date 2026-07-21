# SR-013 — RT-DETR: apakah NMS yang membatasi deteksi?

**Ide I-14** · **Eksperimen:** E-020 · **Putusan: SEDANG BERJALAN** · 2026-07-21

---

## 1. Masalah

E-014 menunjukkan deteksi bukan hambatan utama (agnostik 0,7191–0,7730). Tetapi
"bukan hambatan utama" tidak berarti "sempurna": E-018 mengukur bahwa 11,7%
kotak GT tidak tercapai pada IoU 0,5 oleh detektor mana pun, dan median IoU
terbaik hanya 0,73. Sebagian dari kotak yang hilang itu bisa jadi bukan soal
model gagal *melihat* tandan, melainkan soal **satu kotak benar ditekan oleh
kotak lain di sebelahnya**.

Tandan di mahkota sawit rapat dan saling menutup sebagian. Setiap detektor
keluarga YOLO — termasuk yolo26m baseline — memakai **Non-Maximum Suppression
(NMS)**: bila dua kotak tumpang tindih melebihi ambang IoU, yang skornya lebih
rendah dibuang. Pada objek yang memang berdekatan, NMS greedy dapat membuang
kotak yang sebenarnya benar. Ini plafon **struktural** — tidak bisa dihapus
dengan menambah data, kapasitas, atau resolusi, karena letaknya di
pasca-pemrosesan, bukan di model.

`deep-research-report.md` menempatkan ini sebagai **prioritas 1**: "NMS sering
menjadi plafon struktural pada objek rapat/bertumpuk."

## 2. Ide

RT-DETR (Real-Time DEtection TRansformer) tidak memakai NMS sama sekali. Ia
memakai **pencocokan Hungarian satu-ke-satu** saat pelatihan: tiap objek nyata
dipasangkan tepat dengan satu prediksi, sehingga model belajar mengeluarkan
satu kotak per objek tanpa perlu penindasan pasca-pemrosesan.

Kalau sebagian plafon deteksi kita berasal dari NMS, mengganti detektor dengan
yang NMS-free akan menaikkan recall pada tandan yang bertumpuk — dan itu terbaca
langsung pada mAP.

Ini menguji hipotesis yang **berbeda** dari yolo26x (kapasitas): di sana
pertanyaannya "apakah model kurang besar?"; di sini "apakah mekanisme penindasan
kotaknya yang membatasi?". Keduanya jalur bebas.

**Yang akan memalsukan:** RT-DETR tidak melampaui baseline YOLO pada mAP maupun
pada recall untuk tandan yang bertumpuk — artinya NMS bukan penyebab plafon, dan
prioritas-1 laporan itu tidak berlaku untuk kasus ini.

## 3. Solusi

`experiments/train_rtdetr.py`. RT-DETR-L (33,0 juta parameter — sebanding
yolo26m 21,9 juta, jadi selisih bukan sekadar kapasitas), dilatih dari bobot
COCO pada resolusi asli 1280, augmentasi aman-warna (`hsv_s=0.15`; kematangan
adalah warna, lihat E-019), 60 epoch dengan jadwal kosinus. Split, seed, dan
data.yaml identik dengan baseline.

**Integritas** — split per pohon 716/96/141, irisan nol (diverifikasi di
E-017). Konfigurasi dipilih pada val; test dilaporkan terpisah. Evaluasi memakai
`val()` ultralytics bawaan (definisi mAP sama dengan baseline).

## 4. Hasil

*(diisi saat E-020 selesai — pelatihan ~8–10 jam pada L4)*

Rencana angka yang dilaporkan:

| Sistem | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|
| Baseline yolo26m (640) | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| RT-DETR-L (1280, NMS-free) | — | — | — | — | — | — |

Selain mAP, satu diagnosis khusus yang membedakan hipotesis ini dari sekadar
"detektor lain": **recall pada tandan yang bertumpuk** (pasangan GT dengan
IoU antar-GT > 0,3). Kalau RT-DETR menang justru di sanalah, penyebabnya
memang NMS.

## 5. Putusan

*(diisi saat E-020 selesai)*

## 6. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python train_rtdetr.py --weights rtdetr-l.pt --imgsz 1280 --epochs 60
# keluaran: runs/rtdetr_l_e60_i1280/
```
