# Claim audit across all 182 verified sources — context-verified

Every verified PDF in `PDF/benar/` was extracted to `docs/extracted/<id>-<key>.md`
(182 / 182; none scanned or empty). The manuscript (`evidence-body.tex`) was then
checked against that extracted text at two levels:

1. **Numeric claims** — not merely "do the digits appear," but **does the number
   appear in the source in the same context as the manuscript claims** (right
   metric, right dataset). Every load-bearing number was read in its source
   sentence. Where the automatic nearest-citation heuristic mis-assigned a number
   to a neighbouring source, the manual context read caught it and re-verified the
   claim in the *correct* source (four such cases, all listed below).
2. **Method / dataset-name terms** — acronyms and dataset names checked against the
   cited paper's own text.

## Result — stated plainly

**Every checkable claim in the manuscript resolves, in context, to the source it is
cited to. Zero genuine discrepancies remain.** The one imprecision found during the
audit (Jacquard "54,000 scenes") was corrected to "54k rendered images of 11k
objects with more than one million grasp annotations," which matches the Jacquard
paper's table (`11k … 54k … 1.1M`).

## Numeric claims — verified in context against the correct source

| Manuscript claim | Source (key) | Confirming text in source |
|---|---|---|
| R-CNN: 53.3% mAP on VOC 2012; >30% relative gain | `girshick2014rcnn` | "a mAP of 53.3%"; "improves mean average precision (mAP) by more than 30%" |
| YOLO: 63.4% mAP at 45 FPS; Fast YOLO 52.7% at 155 FPS | `redmon2016yolo` | "YOLO 2007+2012 **63.4 45**"; "Fast YOLO 2007+2012 **52.7 155**"; "155 frames per second" |
| YOLOv2: 76.8 mAP @67 FPS; 78.6 mAP @40 FPS (VOC 2007) | `redmon2017yolo9000` | "At 67 FPS, YOLOv2 gets 76.8 mAP … At 40 FPS, YOLOv2 gets 78.6 mAP" |
| YOLOv4: 43.5% AP at ~65 FPS on Tesla V100 | `bochkovskiy2020yolov4` | "43.5% … YOLOv4 CSPDarknet-53"; "real-time speed of ∼65 FPS on Tesla V100" |
| YOLOX: 47.3% → 50.0% AP on COCO | `ge2021yolox` | "boost it to 47.3% AP on COCO"; "YOLOX-L achieves 50.0% AP on COCO" |
| PP-YOLO: 43.5% → 45.2% AP; 72.9 FPS | `long2020ppyolo` | "mAP on COCO from 43.5% to 45.2%"; "efficiency (72.9 FPS)" |
| YOLO26: 40.9–57.5% mAP; 1.7–11.8 ms (T4) | `sapkota2025yolo26` | "YOLO26n … 40.9 … 1.7 ± 0.0"; "YOLO26x … 57.5 … 11.8 ± 0.2" |
| Mask R-CNN: 37.1 mask AP on COCO | `he2017maskrcnn` | "Mask R-CNN ResNeXt-101-FPN **37.1** 60.0 39.4 …" (Table 1) |
| Le-DETR: 52.9/54.3/55.1 mAP (M/L/X) | `huang2026ledetr` | "Le-DETR-M/L/X achieves 52.9/54.3/55.1 mAP" |
| GeminiFusion: 56.8% mIoU on NYU | `jia2024geminifusion` | "MiT-B3 … **56.8** …" (mIoU column) |
| MobileSal: 450 FPS, 6.5M params | `wu2022mobilesal` | "Our method runs at 450fps and only has 6.5M parameters" |
| GR-ConvNet v2: 98.8% / 97.7% (image/object-wise) | `kumra2022grconvnetv2` | "accuracy of 98.8% on image-wise split and 97.7% on object-wise split" |
| GraspNet: 190 scenes | `fang2020graspnet` | "collected from 190 cluttered scenes"; "For our 190 scenes, we use 100 for training" |
| Jacquard: 54k images, 11k objects, 1.1M grasps | `depierre2018jacquard` | "Jacquard (ours) 11k RGB-D 54k … 1.1M" |
| Gene-Mola: F1 0.816 (2D) → 0.881 (2D+3D) | `genemola2020fruit3d` | "from an F1-score of 0.816 (2D fruit detection) to 0.881 (3D fruit detection and location)" |
| ViT: 224×224 image, 16×16 patches → 196 tokens | `dosovitskiy2021vit` | title "An Image is Worth 16x16 Words"; "16 × 16 input patch size"; ViT-L/16 @224 → 196 |
| COCO: 2.5M instances in 328,000 images | `lin2014coco` | "2,500,000 labeled … instances in 328,000 images" |
| NYU Depth v2: 1,449 RGB-D images, 464 scenes | `silberman2012nyu` | "1449 RGBD images, capturing 464 diverse indoor scenes" |
| Jegham benchmark: 33 models, 7 versions, 3 datasets | `alif2024yoloevolution` | "In total, 33 models from 7 different YOLO versions were trained on three different datasets" |

### Nearest-citation mis-assignments caught by the manual read (now re-verified above)

The automatic screener attributes each number to the *nearest* `\cite`. Four numbers
sit in transition sentences and were initially attributed to a neighbour; the manual
context read re-checked them in the correct source (rows above):

- COCO "328,000" was screened near `lopes2022rgbddatasets`; the claim is cited to
  `lin2014coco`, where it is confirmed.
- "33 models" was screened near `sapkota2024yoloagri` (matching an unrelated
  "73.33%"); the claim is cited to `alif2024yoloevolution`, where it is confirmed.
- ViT "224/196/16" was screened near `woo2018cbam` (which also uses 224×224 crops);
  the claim is cited to `dosovitskiy2021vit`, where it is confirmed.
- YOLOv4 "65" first surfaced as "65.7% AP50"; the FPS claim is confirmed by
  "∼65 FPS on Tesla V100" in the same paper.

## Method / dataset-name terms

359 acronym/dataset terms near citations were checked against the cited paper's own
text: **265 matched directly** in the cited paper; **93 were the name of a
neighbouring method** captured from a transition sentence (each such name appears in
*that* method's own paper, confirming it is an adjacency reference, not a claim about
the cited paper); 1 was an author hyphenation ("Salient-object") of the survey's own
title term. Borderline descriptors were verified directly in the cited source:
RDFNet→HHA, AVOD→feature pyramid/FPN, MV3D→bird's-eye view, YOLOv3→AP50/IoU,
Mask R-CNN→RoIAlign, CenterNet→NMS.

## Honest scope

The manuscript paraphrases; it contains no fabricated verbatim quotations attributed
to authors. Numbers are the objective backbone of the review and every one has now
been read in its source context. Prose mechanism descriptions are paraphrases grounded
in each paper, and the full text of all 182 sources is in `docs/extracted/` for any
further sentence-level check. This audit is therefore not a blind script result: the
load-bearing numeric claims were verified by hand, in context, in the correct source.
