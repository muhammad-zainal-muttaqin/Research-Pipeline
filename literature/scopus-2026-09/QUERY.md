# Query Scopus yang dijalankan

Semua query di bawah ditulis persis seperti yang dikirim ke Scopus Search API
(`https://api.elsevier.com/content/search/scopus`, view `STANDARD`). String yang
sama dapat ditempel langsung ke **Advanced document search** di scopus.com.

Berkas pendukung untuk tiap folder:

| Berkas | Isi |
|---|---|
| `queries.json` | String query verbatim, urutan, dan batas pengambilan |
| `counts.csv` | Waktu eksekusi (UTC), jumlah hasil total, jumlah rekaman yang diambil |
| `raw/<QID>/page_NNN.json` | Respons mentah API per halaman (25 rekaman) |
| `records_<QID>.csv` | Satu baris per rekaman: EID, DOI, judul, penulis pertama, tahun, sumber, tipe dokumen, jumlah sitasi |

Cara menjalankan ulang (kunci API Elsevier disimpan di luar repo):

```bash
export ELSEVIER_API_KEY_FILE=/path/ke/kunci.txt
python3 tools/scopus/scopus_search.py --queries literature/scopus-2026-09/topik/queries.json \
    --out literature/scopus-2026-09/topik
```

Jumlah hasil dapat bertambah bila query dijalankan ulang di kemudian hari karena
Scopus terus mengindeks terbitan baru, terutama tahun 2025–2026. Angka pada
`counts.csv` adalah angka pada tanggal eksekusi.

## Kajian metodologi tinjauan pustaka (MA1–MA7)

Dipakai untuk menemukan panduan penulisan tinjauan pustaka dan contoh review yang banyak disitasi (fase A).

### MA1

Dijalankan 2026-09-28T12:47:58+00:00 (UTC). Total hasil Scopus: 2592; diurutkan menurut jumlah sitasi, diambil 150 teratas.

```
TITLE(("literature review*" OR "review article*" OR "integrative review*") AND (methodolog* OR guideline* OR "how to" OR writing OR typolog* OR "research method*" OR framework)) AND DOCTYPE(ar OR re)
```

### MA2

Dijalankan 2026-09-28T12:48:02+00:00 (UTC). Total hasil Scopus: 859; diurutkan menurut jumlah sitasi, diambil 100 teratas.

```
TITLE(("systematic literature review*" OR "systematic review*" OR "systematic mapping" OR "scoping review*") AND (guideline* OR procedure* OR "how to" OR methodolog* OR snowballing)) AND (SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(BUSI) OR SUBJAREA(DECI))
```

### MA3

Dijalankan 2026-09-28T12:48:13+00:00 (UTC). Total hasil Scopus: 2470; diurutkan menurut jumlah sitasi, diambil 75 teratas.

```
TITLE("PRISMA" OR "preferred reporting items") AND DOCTYPE(ar OR re)
```

### MA4

Dijalankan 2026-09-28T12:48:18+00:00 (UTC). Total hasil Scopus: 1052; diurutkan menurut jumlah sitasi, diambil 125 teratas.

```
TITLE-ABS-KEY((fruit* OR orchard* OR crop* OR agricultur*) AND ("deep learning" OR "computer vision" OR "machine vision" OR "image processing") AND (detection OR counting OR "yield estimation" OR "yield prediction" OR localization)) AND DOCTYPE(re) AND PUBYEAR > 2011 AND PUBYEAR < 2027
```

### MA5

Dijalankan 2026-09-28T12:48:21+00:00 (UTC). Total hasil Scopus: 373; diurutkan menurut jumlah sitasi, diambil 100 teratas.

```
TITLE("RGB-D" OR "multi-view" OR "multiple object tracking" OR "multi-object tracking" OR "re-identification" OR "object detection" OR "depth estimation" OR "structure from motion") AND DOCTYPE(re) AND SUBJAREA(COMP) AND PUBYEAR > 2011 AND PUBYEAR < 2027
```

### MA6

Dijalankan 2026-09-28T12:48:23+00:00 (UTC). Total hasil Scopus: 50; diurutkan menurut jumlah sitasi, diambil 50 teratas.

```
TITLE-ABS-KEY("oil palm" AND (image* OR vision OR "remote sensing" OR "machine learning" OR "deep learning" OR detection OR ripeness OR grading)) AND DOCTYPE(re) AND PUBYEAR > 2011 AND PUBYEAR < 2027
```

### MA7

Dijalankan 2026-09-28T12:52:23+00:00 (UTC). Total hasil Scopus: 37; diurutkan menurut jumlah sitasi, diambil 37 teratas.

```
TITLE("analyzing the past to prepare for the future") OR TITLE("systematic literature reviews in software engineering") OR TITLE("guidelines for snowballing in systematic literature studies") OR TITLE("a typology of reviews") OR TITLE("generating research questions through problematization") OR TITLE("advancing theory with review articles") OR TITLE("what literature review is not") OR TITLE("creating high-impact literature reviews") OR TITLE("theorizing through literature reviews") OR TITLE("review research as scientific inquiry") OR TITLE("conducting systematic literature reviews and bibliometric analyses") OR TITLE("scoping studies: towards a methodological framework")
```

## Topik naskah (Q1–Q9)

Dipakai untuk korpus tinjauan: penghitungan buah dari banyak pengamatan, penghitungan satu pandang, persepsi TBS sawit, atribut kelas, depth/3D, bukti lintas ranah, dan review terdahulu (fase B).

### Q1

Dijalankan 2026-09-28T13:06:24+00:00 (UTC). Total hasil Scopus: 871.

```
TITLE-ABS-KEY((fruit* OR orchard* OR "tree crop*" OR "fresh fruit bunch*" OR "oil palm" OR "Elaeis guineensis" OR apple* OR citrus OR orange* OR mango* OR grape* OR vineyard* OR strawberr* OR tomato* OR kiwifruit* OR pear OR pears OR peach* OR cherr* OR blueberr* OR "sweet pepper*" OR capsicum OR banana* OR pineapple* OR "date palm*" OR coconut* OR pomegranate* OR avocado* OR lemon* OR plum OR plums OR almond* OR walnut* OR olive*) AND (count* OR "yield estimat*" OR "yield predict*" OR "yield forecast*" OR "load estimat*" OR "fruit load" OR "crop load" OR inventor* OR enumerat* OR "fruit number") AND ("multi-view" OR multiview OR "multiple view*" OR "multi-camera" OR "multiple camera*" OR video* OR "image sequence*" OR track* OR "structure from motion" OR "structure-from-motion" OR SfM OR SLAM OR "3D reconstruct*" OR "point cloud*" OR "double count*" OR duplicat* OR "re-identification" OR "data association" OR "cross-view" OR "both sides" OR "two sides") AND (image* OR camera* OR vision OR "deep learning" OR "neural network*" OR detect* OR segment* OR YOLO OR "R-CNN" OR photograph*)) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT) OR SUBJAREA(PHYS) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MATH) OR SUBJAREA(DECI) OR SUBJAREA(BIOC)) AND NOT TITLE-ABS-KEY("fruit fl*" OR drosophila OR "blood count*")
```

### Q2

Dijalankan 2026-09-28T13:07:16+00:00 (UTC). Total hasil Scopus: 757.

```
TITLE((fruit* OR orchard* OR "tree crop*" OR "fresh fruit bunch*" OR "oil palm" OR "Elaeis guineensis" OR apple* OR citrus OR orange* OR mango* OR grape* OR vineyard* OR strawberr* OR tomato* OR kiwifruit* OR pear OR pears OR peach* OR cherr* OR blueberr* OR "sweet pepper*" OR capsicum OR banana* OR pineapple* OR "date palm*" OR coconut* OR pomegranate* OR avocado* OR lemon* OR plum OR plums OR almond* OR walnut* OR olive*) AND (count* OR "yield estimat*" OR "yield predict*" OR "load estimat*" OR "fruit load" OR "crop load" OR "fruit number")) AND TITLE-ABS-KEY((image* OR camera* OR vision OR "deep learning" OR "neural network*" OR detect* OR segment* OR YOLO OR "R-CNN" OR photograph*)) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT) OR SUBJAREA(PHYS) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MATH) OR SUBJAREA(DECI) OR SUBJAREA(BIOC)) AND NOT TITLE-ABS-KEY("fruit fl*" OR drosophila OR "blood count*")
```

### Q3

Dijalankan 2026-09-28T13:07:55+00:00 (UTC). Total hasil Scopus: 1079.

```
TITLE-ABS-KEY(("oil palm" OR "Elaeis guineensis" OR "fresh fruit bunch*" OR "palm oil fruit*") AND (image* OR vision OR camera* OR "deep learning" OR "machine learning" OR detect* OR convolutional OR YOLO OR segment* OR classif* OR ripeness OR maturity OR count*) AND (bunch* OR fruit* OR ripeness OR maturity OR harvest*)) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT) OR SUBJAREA(PHYS) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MATH) OR SUBJAREA(DECI) OR SUBJAREA(BIOC))
```

### Q4

Dijalankan 2026-09-28T13:08:21+00:00 (UTC). Total hasil Scopus: 361.

```
TITLE-ABS-KEY((fruit* OR orchard* OR "tree crop*" OR "fresh fruit bunch*" OR "oil palm" OR "Elaeis guineensis" OR apple* OR citrus OR orange* OR mango* OR grape* OR vineyard* OR strawberr* OR tomato* OR kiwifruit* OR pear OR pears OR peach* OR cherr* OR blueberr* OR "sweet pepper*" OR capsicum OR banana* OR pineapple* OR "date palm*" OR coconut* OR pomegranate* OR avocado* OR lemon* OR plum OR plums OR almond* OR walnut* OR olive*) AND (ripeness OR maturity OR "ripening stage*" OR "maturity stage*" OR "size class*" OR grade* OR grading OR defect* OR "multi-class" OR "per class" OR "class-wise") AND (count* OR "yield estimat*" OR inventor* OR "load estimat*") AND (detect* OR track* OR segment*) AND (image* OR camera* OR video* OR vision)) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT) OR SUBJAREA(PHYS) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MATH) OR SUBJAREA(DECI) OR SUBJAREA(BIOC)) AND NOT TITLE-ABS-KEY("fruit fl*" OR drosophila OR "blood count*")
```

### Q5

Dijalankan 2026-09-28T13:10:52+00:00 (UTC). Total hasil Scopus: 1988.

```
TITLE-ABS-KEY((fruit* OR orchard* OR "tree crop*" OR "fresh fruit bunch*" OR "oil palm" OR "Elaeis guineensis" OR apple* OR citrus OR orange* OR mango* OR grape* OR vineyard* OR strawberr* OR tomato* OR kiwifruit* OR pear OR pears OR peach* OR cherr* OR blueberr* OR "sweet pepper*" OR capsicum OR banana* OR pineapple* OR "date palm*" OR coconut* OR pomegranate* OR avocado* OR lemon* OR plum OR plums OR almond* OR walnut* OR olive*) AND ("RGB-D" OR RGBD OR "depth camera*" OR "depth image*" OR "depth map*" OR "depth sensor*" OR "depth information" OR "stereo camera*" OR "stereo vision" OR binocular OR LiDAR OR "time-of-flight" OR "point cloud*" OR Kinect OR RealSense OR "3D camera*") AND (detect* OR count* OR locali* OR "yield estimat*" OR "size estimat*") AND (orchard* OR field* OR tree* OR canopy OR plant* OR greenhouse* OR vineyard*)) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT) OR SUBJAREA(PHYS) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MATH) OR SUBJAREA(DECI) OR SUBJAREA(BIOC)) AND NOT TITLE-ABS-KEY("fruit fl*" OR drosophila OR "blood count*")
```

### Q6

Dijalankan 2026-09-28T13:11:02+00:00 (UTC). Total hasil Scopus: 236.

```
TITLE-ABS-KEY(("multi-object tracking" OR "multiple object tracking" OR "multi-target tracking" OR "multiple target tracking" OR "re-identification" OR "multi-camera tracking" OR "multi-camera multi-object" OR "multi-view detection" OR "multiview detection" OR "cross-view association" OR "multi-view association" OR "cross-camera association" OR "object counting" OR "structure from motion" OR "visual SLAM" OR "instance association") AND (review OR survey OR benchmark)) AND DOCTYPE(re) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI))
```

### Q7

Dijalankan 2026-09-28T13:12:23+00:00 (UTC). Total hasil Scopus: 1049.

```
TITLE-ABS-KEY((fruit* OR orchard* OR "tree crop*" OR "fresh fruit bunch*" OR "oil palm" OR "Elaeis guineensis" OR apple* OR citrus OR orange* OR mango* OR grape* OR vineyard* OR strawberr* OR tomato* OR kiwifruit* OR pear OR pears OR peach* OR cherr* OR blueberr* OR "sweet pepper*" OR capsicum OR banana* OR pineapple* OR "date palm*" OR coconut* OR pomegranate* OR avocado* OR lemon* OR plum OR plums OR almond* OR walnut* OR olive*) AND (count* OR "yield estimat*" OR "yield predict*" OR "load estimat*" OR detect* OR ripeness OR maturity OR harvest* OR locali*) AND (image* OR vision OR camera* OR sensor* OR "deep learning" OR "machine learning")) AND DOCTYPE(re) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(AGRI) OR SUBJAREA(COMP) OR SUBJAREA(ENGI) OR SUBJAREA(MULT) OR SUBJAREA(PHYS) OR SUBJAREA(EART) OR SUBJAREA(ENVI) OR SUBJAREA(MATH) OR SUBJAREA(DECI) OR SUBJAREA(BIOC)) AND NOT TITLE-ABS-KEY("fruit fl*" OR drosophila OR "blood count*")
```

### Q8a

Dijalankan 2026-09-28T13:12:23+00:00 (UTC). Total hasil Scopus: 3604; diurutkan menurut jumlah sitasi, diambil 25 teratas.

```
TITLE("multi-object tracking" OR "multiple object tracking" OR "multi-target tracking" OR "tracking-by-detection" OR "tracking by detection") AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI)) AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

### Q8b

Dijalankan 2026-09-28T13:12:24+00:00 (UTC). Total hasil Scopus: 2243; diurutkan menurut jumlah sitasi, diambil 25 teratas.

```
TITLE("multi-view" OR multiview OR "multi-camera" OR "multiple cameras" OR "cross-view") AND TITLE(detection OR tracking OR association OR counting OR "re-identification") AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI)) AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

### Q8c

Dijalankan 2026-09-28T13:12:25+00:00 (UTC). Total hasil Scopus: 9696; diurutkan menurut jumlah sitasi, diambil 25 teratas.

```
TITLE("structure from motion" OR "structure-from-motion" OR SLAM OR "bundle adjustment" OR "multi-view stereo") AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI)) AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

### Q8d

Dijalankan 2026-09-28T13:12:26+00:00 (UTC). Total hasil Scopus: 1554; diurutkan menurut jumlah sitasi, diambil 25 teratas.

```
TITLE("object counting" OR "crowd counting" OR "counting objects" OR "class-agnostic counting") AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI)) AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

### Q8e

Dijalankan 2026-09-28T13:12:27+00:00 (UTC). Total hasil Scopus: 6435; diurutkan menurut jumlah sitasi, diambil 25 teratas.

```
TITLE("re-identification" OR "reidentification") AND TITLE(object OR vehicle OR person OR instance) AND PUBYEAR > 2011 AND PUBYEAR < 2027 AND (SUBJAREA(COMP) OR SUBJAREA(ENGI)) AND (DOCTYPE(ar) OR DOCTYPE(cp))
```

### Q9

Dijalankan 2026-09-28T13:18:29+00:00 (UTC). Total hasil Scopus: 1082; diurutkan menurut jumlah sitasi, diambil 25 teratas.

```
(TITLE("simple online and realtime tracking") OR TITLE("deep association metric") OR TITLE("BoT-SORT") OR TITLE("StrongSORT") OR TITLE("multiview detection with feature perspective transformation") OR TITLE("representing scenes as neural radiance fields") OR TITLE("3D Gaussian splatting for real-time radiance field rendering") OR TITLE("depth anything") OR TITLE("segment anything") OR TITLE("vision transformers for dense prediction") OR TITLE("end-to-end object detection with transformers") OR TITLE("DETRs beat YOLOs")) AND PUBYEAR > 2011 AND PUBYEAR < 2027
```
