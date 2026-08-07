# Complete Research Results Report Plan

## 1. Purpose and acceptance criteria

This plan defines the evidence, narrative order, file set, visual set, and
verification gates for the complete English results report. The report is
designed as the results companion to "manuscript/source/main.tex". The
manuscript maps the literature; this report explains what was actually tried,
what was measured, why a result moved the research branch, and what remains
open.

The finished deliverable must satisfy all of the following:

1. Use Elsevier `elsarticle` formatting in "reports.tex" so the layout stays
   readable while the evidence and discussion remain the acceptance criteria.
2. Give a dedicated discussion section to every numbered slot E-001 through
   E-032.
3. State explicitly that E-008 was not run and that E-023 was executed under
   the redesigned E-032 protocol.
4. Cover the physical-depth gate register G0 through G8 and retain the open
   follow-up G7b.
5. For every experiment, state objective, hypothesis, data, configuration,
   controls, metrics, evidence, interpretation, verdict, consequence, and
   reproduction route.
6. Keep RGB pilot results and physical-depth results in separate evidence
   boundaries. Do not compare their absolute mAP values as one leaderboard.
7. Use GPT Image 2 for explanatory raster figures and deterministic charts for
   exact metric comparisons.
8. Compile to a PDF and render representative pages for visual inspection.
   Page count is descriptive, not a pass/fail criterion; the current snapshot
   is allowed to grow when additional evidence is added.
9. Give each executed experiment a substantive, evidence-rich discussion.
   A section may combine prose, a table, and a phase figure, but it must not be
   padded with forced page breaks or unsupported filler. E-008 remains a
   transparent not-run exception.
10. Make the causal transition from one experiment to the next explicit. A
    figure is useful only when its caption and surrounding prose explain what
    changed, what was held fixed, and why the next branch followed.
11. Keep every claim traceable to a repository document, script, metric table,
   JSON artifact, commit, or explicitly marked historical audit.

## 2. Repository evidence hierarchy

The report follows this precedence when sources disagree:

1. Current raw result JSON, metric manifests, and checksum manifests.
2. "experiments/METRICS.md" for the definitive E-021 comparison.
3. "experiments/AUDIT-E022.md" for corrections to the first physical-depth
   result.
4. "experiments/LAPORAN-EKSPERIMEN.md" for the curated experiment register
   and current verdicts.
5. "experiments/EKSPERIMEN.md" for the append-only chronology.
6. SR notes, reproduction READMEs, and scripts for method detail.
7. Literature and generated figures for motivation or explanation only.

The report never turns an unverified historical number into a current claim.
The report also preserves withdrawn claims so that a reader can understand
why the branch changed.

## 3. Report architecture

### Part I. Scope and evidence boundary

- Define the operational target: detect, classify, count, and support RGB-only
  fallback for fresh-fruit bunches.
- Explain the difference between the 953-tree RGB pilot and the 352-tree
  physical-depth branch.
- Freeze the repository cutoff at commit "5b63297".
- Summarize the 202 BibTeX records and 182 verified local PDFs.
- Define verdict vocabulary: confirmed, partial, falsified, inconclusive,
  withdrawn, null, delivered, and open.

### Part II. Evidence base and design translation

- Connect detector, depth, fusion, geometry, and identity literature to
  falsifiable hypotheses.
- Explain why pseudo-depth and physical sensor depth are different modalities.
- Describe the planned visual taxonomy and the complete roadmap.

### Part III. RGB pilot, E-001 through E-021

The RGB branch is narrated as a diagnostic funnel:

1. E-001 to E-005: invalidate the first ambiguity statistic and establish the
   tree-level geometry boundary.
2. E-006 to E-007: test pseudo-depth and geometric counting at the bunch level.
3. E-009 to E-012: diagnose B4 visibility, texture, and ordinal maturity.
4. E-013 to E-017: specify the production contract and decompose the mAP
   bottleneck.
5. E-018 to E-021: measure the localization envelope, test safe high
   resolution, compare RT-DETR-L, and select RF-DETR-L.

### Part IV. Physical-depth branch, E-022 through E-032

The physical-depth branch is narrated as an audit and replication funnel:

1. E-022: audit sidecar semantics, calibration, reprojection, range, and the
   first early-fusion result.
2. E-023: preserve the redesigned middle/late-fusion plan as an execution
   alias under E-032.
3. E-024 to E-026: create and test an annotation-derived cross-side identity measure.
4. E-025: bind every inter-arm comparison to one evaluator.
5. E-027 and E-029: replace seed-42 claims with corrected multi-seed matrices.
6. E-028: repeat identity measurement on the larger RGB dataset.
7. E-030 and E-031: isolate capacity and split variance.
8. E-032: test early, middle, late, and noise controls from scratch.

### Part V. Synthesis and appendices

- State the best observed RGB development benchmark with its external boundary.
- State the bounded negative physical-depth result.
- Explain exactly which hypotheses were closed and which remain open.
- Provide the full configuration ledger, script map, derived metric rules,
  complete experiment register, visual provenance, and gate register.

## 4. Per-experiment writing contract

Every "experiment" section must contain the following subsections or
equivalent paragraphs:

| Field | Required content |
|---|---|
| Objective | The scientific question in one sentence |
| Hypothesis | What would count as support and what would falsify it |
| Configuration | Dataset, split, architecture, input size, epochs, seed, batch, optimizer, augmentation, initialization, evaluator |
| Controls | Negative controls, swapped controls, same-seed pairing, or why no control was valid |
| Evidence | Exact counts, metric values, confidence intervals, and class-level results |
| Interpretation | Mechanistic explanation constrained by the measurement |
| Verdict | Confirmed, partial, falsified, inconclusive, withdrawn, null, or delivered |
| Consequence | Which next experiment or gate was opened or closed |
| Reproducibility | Script, manifest, JSON, README, or commit path |

Special provenance rules:

- A missing run is not a null result.
- A withdrawn metric remains visible but cannot be cited as current evidence.
- A cross-dataset comparison must be labeled invalid when dataset, split, or
  protocol differs.
- A CI containing zero is inconclusive for that contrast; it is not proof of
  no effect.
- A one-seed capacity pattern is a hypothesis generator until G7b is closed.

## 5. Experiment traceability matrix

| Experiment | Scientific focus | Primary evidence | Report treatment |
|---|---|---|---|
| E-001 | "class_mismatch" as ambiguity | SR-001 and E-001 log | Falsified as an ambiguity measure |
| E-002 | Reuse master annotations | SR-002 and inventory probe | Inconclusive, motivates E-015 |
| E-003 | DA3 on one orbit video | SR-003 | Partial, tree geometry only |
| E-004 | DA3 on six videos | SR-003 | Confirmed at tree level |
| E-005 | DA3 four/eight-side order | SR-004 | Confirmed for side ordering |
| E-006 | Pseudo-depth bunch signal | SR-005 and result JSON | Falsified |
| E-007 | Geometric linking and counting | SR-006 and ablation table | Falsified |
| E-008 | Reserved slot | Append-only log | Not run |
| E-009 | Ground-truth box size | SR-007 | Partial |
| E-010 | B4 contrast, texture, density | SR-007 | Contrast confirmed, density falsified |
| E-011 | Texture preprocessing | SR-008 | Texture confirmed, contrast boost falsified |
| E-012 | Ordinal maturity confusion | SR-009 | Confirmed |
| E-013 | Production RGB-D contract | "pipeline/README.md" | Delivered contract, no accuracy claim |
| E-014 | Detection versus classification bottleneck | SR-010 and diagnostic JSON | Diagnostic pending JSON identity check |
| E-015 | Master-image content mapping | SR-002 and mapping manifest | Unblocked |
| E-016 | Proposed maturity ceiling | SR-011 | Withdrawn as a hard ceiling |
| E-017 | Two-stage detector | SR-012 and evaluator outputs | Falsified |
| E-018 | Localization envelope | E-018 analysis and IoU envelope | Descriptive oracle reachability, not AP/mAP |
| E-019 | High-resolution safe-color baseline | RGB run manifest | Single-run descriptive result; no population-null claim |
| E-020 | RT-DETR-L direction | SR-013 and metrics | Multi-factor shortlist direction |
| E-021 | RF-DETR-L fair comparison | "METRICS.md" and paired bootstrap | Best observed RGB development benchmark; repeated test exposure |
| E-022 | Sensor audit and early fusion | "AUDIT-E022.md" and audit JSON | Historical metrics retracted |
| E-023 | Redesigned fusion study | E-032 manifest | Execution alias |
| E-024 | Cross-side identity measure | SR-016 and consistency JSON | Annotation-derived measure with power limits |
| E-025 | Evaluator gap | evaluator diagnostic JSON | pycocotools protocol bound |
| E-026 | Depth identity stabilization | paired consistency JSON | Inconclusive within measured subset; unequal denominators |
| E-027 | YOLO26n multi-seed matrix | 12 paired JSON files | Benefit criterion falsified; harmful in two of three seeds, not universal |
| E-028 | SawitMVC identity power | G8 consistency JSON | RGB identity power/context study; no physical-depth treatment test |
| E-029 | RT-DETR-L multi-seed matrix | 9 paired JSON files | Capacity rescue retracted |
| E-030 | YOLO26 capacity sweep | capacity metrics manifest | Partial, one seed |
| E-031 | Split versus seed variance | split manifests and paired JSON | Observed split sensitivity |
| E-032 | Early/mid/late fusion | 15-run manifest and 12 contrasts | Inconclusive within tested regime; all CIs include zero; G4/G6 not universal |

## 6. Gate traceability matrix

| Gate | Question | Closing evidence | Current status |
|---|---|---|---|
| G0 | Are all runs and links accounted for? | Run inventory and link audit | Open; manifest repair required |
| G1 | Why do trainer and pycocotools scores differ? | E-025 | Protocol bound; asymmetry characterized |
| G2 | Does a single seed generalize? | E-027 and E-029 | Closed |
| G3 | Is the E-022 decision aligned with the audit? | E-022 audit corrections | Closed |
| G4 | Does middle fusion help? | E-032 | Inconclusive within tested regime |
| G5 | Does the split change the result? | E-031 | Closed within tested split conditions; observed split sensitivity |
| G6 | Does late fusion help? | E-032 | Inconclusive within tested regime |
| G7 | Does capacity explain the channel cost? | E-030 | Exploratory, one seed |
| G8 | Is identity power sufficient on SawitMVC? | E-028 | Limited power boundary |
| G7b | Does the capacity pattern hold across seeds? | Five runs and paired evaluation still required | Open |

## 7. Visual production plan

### GPT Image 2 conceptual assets

Use GPT Image 2 for explanatory figures where exact numerical geometry is not
the claim:

| Asset | Intended role |
|---|---|
| F01 | Evidence taxonomy |
| F02 | YOLO and detector timeline |
| F03 | RGB detector lineage |
| F04 | Early, middle, and late fusion strategy |
| F05 | YOLO RGB-D input and projection patterns |
| F06 | Cross-modal attention and feature fusion |
| F07 | FFB detection-to-counting funnel |
| F08 | Production RGB-D pipeline |
| R01 | Complete roadmap from evidence to G7b |
| R02 | Physical-depth audit and training-arm logic |
| R07 | RGB-D experiment architecture and evaluator boundary |
| C01 | Literature corpus by year |
| C02 | Literature corpus by theme |
| H01 | Why RGB-D is a hypothesis for FFB perception |
| H02 | Hypothesis to control and decision-gate translation |
| H03 | Five-phase chronology from E-001 through E-032 |
| H04 | Error attribution for a negative RGB-D result |
| H05 | YOLO26, RT-DETR-L, and RF-DETR-L architecture comparison |
| H06 | Physical-depth audit and replication timeline |
| H07 | Early, middle, late, and noise fusion variants |
| H08 | E-001--E-008 RGB-D diagnostic phase |
| H09 | E-009--E-012 RGB bottleneck phase |
| H10 | E-013--E-021 production and final RGB phase |
| N19 | E-002 provenance before identity |
| N20 | E-003--E-007 geometry transfer and bunch-identity boundary |
| N21 | E-009--E-012 RGB bottleneck chain |
| N22 | E-014 detection versus maturity decomposition |
| N23 | E-015--E-019 mapping to a bounded RGB baseline |
| N24 | E-018--E-021 one RGB protocol and detector directions |
| N25 | E-022--E-032 physical-depth audit, alias, and fusion controls |
| N26 | E-024--E-026 identity denominator and evaluator binding |
| N27 | E-027--E-030 replication and capacity boundary |
| N28 | E-031 split, seed, and paired-delta variance |
| N29 | End-to-end conditional depth claim boundary |

GPT Image 2 figures are labeled conceptual. They must never be used as the
source of a metric, confidence interval, or count.

### Deterministic figures

Use code-native charts for exact data:

| Asset | Exact data shown |
|---|---|
| R03 | E-021 model comparison |
| R04 | E-027 multi-seed deltas |
| R05 | E-032 fusion contrasts |
| R06 | E-014 bottleneck gap |
| "fig-corpus-year.png" | Corpus year distribution |
| "fig-corpus-theme.png" | Corpus theme distribution |

## 8. Configuration ledger

### RGB pilot

- Dataset: SawitMVC RGB, 953 trees, 18,540 boxes, 9,823 unique bunches.
- Images: 3,000/404/588 train/validation/test, 960 by 1280 portrait.
- Tree split: 716/96/141 with zero tree intersection.
- Classes: ordered B1, B2, B3, B4.
- Baseline: YOLO26m, seed 42, 640 pixels, 60 epochs.
- E-021 comparison: YOLO26m, YOLO26l, RT-DETR-L, RF-DETR-L, 1280 pixels,
  safe-color augmentation, one pycocotools protocol.

### Physical-depth branch

- Dataset: SawitMVC-Depth, 352 trees, 1,408 RGB images, 2,299 boxes.
- RGB image geometry: 1280 by 800 landscape.
- Depth: Orbbec Y16, 848 by 480, unsigned 16-bit millimeters.
- Tree split: 245/35/72, with device and dominant-class stratification.
- Reprojection: per-file intrinsics, extrinsics, Brown-Conrady distortion,
  forward z-buffer, median hole fill.
- Raw sidecar range: 0.8 to 15.0 m selected from train only.
- Input order: [B,G,R,D], zero invalid, one to 255 inverse depth.
- Evaluation: paired tree bootstrap, 2,000 resamples, pycocotools.

### Fusion matrix

- Five arms: RGB, early, middle, late, and noise.
- Three seeds: 42, 1337, 2024.
- Fifteen runs, 150 epochs, 640 pixels, YOLO26n, from scratch.
- Twelve paired contrasts.
- Decision rule: all three seeds agree and every CI excludes zero for a
  confirmed difference; sign agreement with a CI containing zero is only an
  indication.

## 9. Build and verification plan

### Source checks

~~~powershell
rg -c '^\\experiment' reports.tex
rg -n '^\\experiment' reports.tex
Select-String -Path reports.tex -Pattern ([char]0x2014)
git diff --check
~~~

Expected experiment count is 32 and the em dash/backtick check must be zero.

### PDF build

~~~powershell
New-Item -ItemType Directory -Force output/pdf | Out-Null
& C:\Users\Zainal\bin\tectonic.exe --outdir output/pdf reports.tex
~~~

### PDF evidence

~~~powershell
& C:\Users\Zainal\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe output/pdf/reports.pdf
~~~

The page count is descriptive, not a minimum. Render the title page, roadmap
page, representative early experiment, representative detector experiment,
representative depth experiment, E-032, configuration ledger, and references.
Inspect for clipped tables, missing figures, unreadable labels, and accidental
blank pages.

## 10. Update protocol

When a new experiment or commit is added:

1. Add the raw artifact and source path first.
2. Update "experiments/EKSPERIMEN.md" and
   "experiments/LAPORAN-EKSPERIMEN.md".
3. Update the experiment and gate matrices in this plan.
4. Add or revise the dedicated experiment section in "reports.tex".
5. Add exact metric charts only from machine-readable data.
6. Rebuild and render the PDF.
7. Recheck the dataset boundary and the open-gate wording.

The report is complete only when the source, plan, figures, compiled PDF, and
verification evidence agree.
