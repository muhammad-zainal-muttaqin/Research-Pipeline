# Brief: coding rules for a systematic mapping review

You are an independent methodologist. A systematic mapping review has a written
protocol with gaps. Decide six open coding rules. Base every answer only on the
protocol text below, the review questions, and the example records in
`contoh.json` (same folder as this brief). Do not open any other file in the
repository: other files contain earlier decisions you must not see.

## Review topic and questions

Image-based fruit counting, with focus on cross-view identity: how a method
decides that observations of a fruit in different images belong to the same
fruit, so it is counted once.

1. Which mechanisms decide that observations in different images come from the
   same fruit, and which acquisition conditions does each mechanism assume?
2. What evidence shows how well each mechanism controls double counting and
   missed fruit, and how is that evidence measured?
3. How are class attributes, especially ripeness, attached to unique fruit
   rather than to each detection?
4. What does oil-palm imaging literature cover, and what is missing for a
   per-class bunch census from images?

## Inclusion codes (one code per record)

| Code | Meaning |
|---|---|
| C1 | Method that combines several observations of the same fruit (video, several views, repeated scans). Core group |
| C2 | Counting or yield estimation from a single view |
| C3 | Oil-palm fresh-fruit-bunch imaging, including mill grading and loose fruit |
| C4 | Class attribute (e.g. ripeness) together with counting from a single image |
| C5 | Detection, localization, or measurement of fruit with depth, 3D, or non-RGB modality |
| R | Earlier review |
| T | Transferable method from outside agriculture |

Fixed rules already decided:
- Stereo: one stereo pair counts as one observation, so a study that detects,
  localizes or measures fruit from one stereo pair is C5. A stereo study is C1
  only if fruit are linked across frames or across camera positions.
- Priority: if several codes fit, C1 takes precedence for a study that combines
  several observations of the same fruit.

Exclusion reasons: E1 not fruit on the plant; E2 only postharvest or
laboratory; E3 yield model without fruit-level detection; E4 only picking or
manipulation; E5 detection without counting or other evaluation; E6 non-imaging
sensor; E7 language other than English.

## Labels for C1 records

Mechanism (how the same fruit is prevented from being counted twice), combined
with "+" when several apply:
M0 no association across images; M1 statistical correction (e.g. multiplier
factor or regression); M2 appearance matching or re-identification; M3 temporal
tracking frame to frame; M4 geometric or 3D association (matching positions in
3D space); M5 learned association; DATA the paper releases a dataset.

Acquisition: V video along a path; D several images from separate positions;
S 3D scan or point cloud; T revisits at different times; 1 single image.

Per class: Y if counts are reported per class.

## Questions

1.1 Two kinds of record were coded C1 although the protocol has no explicit
rule for them. (a) RECONSTRUCTION: images from many positions are fused into a
3D model (structure-from-motion, photogrammetric point cloud, SLAM map, NeRF or
Gaussian splatting, 360-degree panorama) and fruit are detected or counted in
or via that fused model. (b) STATISTICAL: counts from several images of the
same tree (e.g. two sides, several angles) are combined by a statistical rule
(sum with correction factor, regression, learned regression) without linking
individual fruit. Are (a) and (b) C1? If not, what code do they get? State any
conditions.
Examples: `contoh.json` key "1.1".

1.2 Dataset papers that release multi-view or 3D fruit data (annotated images
and point clouds) but present no counting method of their own. Are they C1
(mechanism DATA), or another code? Examples: key "1.2".

1.3 A study tracks fruit across video frames (identity is linked across
frames) but the count it reports comes from a single frame or no count is
reported. Is it C1? Example: key "1.3".

1.4 A calibration regression converts the number of fruit visible in images to
the true number on the tree (to correct occlusion). In a C1 record, is this
labelled M1 (added to the other mechanisms), or not a mechanism? Examples:
key "1.4".

1.5 Images are taken from many positions and fused into a 3D point cloud
(photogrammetry/SfM, or a moving scanner). Which acquisition label applies:
D (several images from separate positions), S (3D scan or point cloud), or V
(video along a path)? Give a rule that decides between them. Examples: key "1.5".

1.6 Two Chinese-language agricultural engineering journals (Transactions of the
Chinese Society of Agricultural Engineering; Transactions of the Chinese
Society for Agricultural Machinery) publish full texts in Chinese with an
English title and abstract indexed in Scopus. Facts: 27 records from these two
journals are already included in the map (11 C1, 7 C2, 7 C5, 1 C4, 1 R), coded
from their English abstracts and, for C1, the Chinese full text. E7 has so far
been applied to one record whose abstract is only in Chinese. Ten further
records from these journals are pending: should they be excluded as E7, or
assessed on content like the 27? State the rule.

## Output

For each question give: the answer, one operational rule sentence that a
screener can apply without judgement calls, the reasoning (tie it to the
protocol definitions and review questions), and your confidence (high, medium,
low).
