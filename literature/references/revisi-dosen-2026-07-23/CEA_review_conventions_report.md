# Reverse-Engineering CEA Review-Article Conventions
### A methodology analysis of 8 review articles in *Computers and Electronics in Agriculture* (2026)

*Sample size: 8 papers. This is a small, indicative sample, not a statistically representative one. Treat every "always/never" statement below as "in this sample of 8." Ranges, medians, and modes are reported throughout; a trait seen in 7-8/8 papers is flagged as a likely must-have, a trait seen in 1-3/8 as optional/stylistic.*

---

## 1. Executive summary

All 8 papers are 2026 "articles in press" in CEA, each an applied engineering/technology review (AI, sensors, robotics, DEM) rather than a biological or agronomic review. The modal template is: **Introduction (with embedded background, gaps, and a literature-search methodology subsection) → 2-4 thematic synthesis sections organized around a proposed taxonomy → a combined Challenges/Limitations section → a Future-directions/roadmap section (often folded into the same section as Challenges) → a short Conclusion.** A separate, clearly-labeled "Discussion" section is uncommon (only 2/8); most papers fold discussion into the challenges/future-directions section instead.

**Likely must-haves (7-8/8 papers):** a named literature-search method citing specific databases; a proposed taxonomy or classification framework for the topic; a dedicated Challenges/Limitations section immediately followed by a Future-directions section, then a short Conclusion; a single unstructured (non-IMRaD-labeled) abstract; no Elsevier "Highlights" bullets; no numbered equations; explicit positioning against prior reviews (framed as a gap statement, not necessarily a labeled "Contributions" section).

**Variable/optional (roughly a 50/50 or minority split):** PRISMA/PRISMA-ScR branding of the search (5/8 cite PRISMA by name, 2/8 use "systematic literature review" without PRISMA, 1/8 neither); a standalone numbered "Methods" section (7/8 yes, 1/8 folds it into the intro with no numbering); a dedicated "Contributions of this review" statement (3/8 explicit, others implicit); open-access status (2/8 OA); first-person "we" voice (roughly half); a dedicated nomenclature/abbreviation table (1/8 has one as a real section).

Figures range 4-17 (median 12), tables 2-12 (median 6), references 59-286 (median ~190), and body length 19-33 pages (median 24).

---
## 2. Sample overview

| ID | Title (short) | Year | Declared/functional review type | Pages | References |
|---|---|---|---|---|---|
| P1 | Global wheat disease identification via AI technologies: An in-depth survey... | 2026 | "Global comprehensive survey" (PRISMA-style screening, not branded) | 27 | ~179 |
| P2 | Autonomous navigation path planning for agricultural ground machinery: a review | 2026 | Scoping review (PRISMA 2020 + PRISMA-ScR) | 33 | ~201 |
| P3 | Automated insect behavioral phenotyping with computer vision and DL | 2026 | Systematic search, framed via 4 research questions | 19 | ~159 |
| P4 | A comprehensive review of wearable sensors for animal information acquisition | 2026 | Self-labeled "systematic literature review" (PRISMA-guided), but caveats it's a narrative synthesis | 21 | ~177 |
| P5 | Intelligent integration in agricultural insect management equipment | 2026 | Narrative review, systematic dual-database search | 30 | ~236 |
| P6 | Multi-sensor integration and cloud-native AI for climate-smart agricultural monitoring | 2026 | Structured literature analysis (PRISMA 2020 search only; thematic synthesis, no meta-analysis) | 19 | ~216 |
| P7 | Plant wearables in smart agriculture for VOC detection | 2026 | Narrative review, PRISMA-screened single-database search | 21 | ~59 |
| P8 | Modelling the shapes of agricultural materials in DEM | 2026 | Self-labeled "systematic literature review (SLR)", no PRISMA branding | 29 | ~286 |

Reference counts are automated approximations (regex-based parsing of the bibliography), accurate to within roughly ±5-10 entries; treat them as good-enough for ranking and central-tendency purposes, not as exact citation counts.

---
## 3. Cross-paper synthesis

### 3.A Bibliographic / metadata

- **Authors:** 2-10 per paper (median 5.5, mode 6). Single-institution papers: 3/8 (P1, P2, P7). Multi-institution: 5/8, and 3 of those are also multi-*country* (P3: China+Australia; P4: China+Serbia+Malaysia; P6: Czech Republic+Hungary+Türkiye).
- **Open access:** only 2/8 (P6, P7) are OA (CC BY and CC BY-NC respectively); the other 6/8 are standard-subscription Elsevier articles.
- **Keywords:** tightly clustered, 4-6 per paper (median 5).
- **Title structure:** 7/8 titles use a colon ("Topic: sub-description") — the one exception (P4) instead opens with "A comprehensive review of...". Only 2/8 titles contain an explicit "review" or "survey" noun (P1 "survey", P4 "comprehensive review"); the other 6/8 signal review-ness through phrasing like "...challenges and future directions" or "...a systems framework" rather than the word itself. None use "systematic review," "scoping review," or "bibliometric" in the title.
- **Title scope:** 1/8 is single-crop (P1, wheat); the remaining 7/8 are task-general or technology-general, applied across crops/species/materials generally — consistent with CEA's engineering/technology orientation.

**Takeaway:** a colon-structured title is near-universal; explicitly branding the piece as a "review" or "survey" in the title itself is not — CEA reviews more often signal their nature through a descriptive subtitle ("...challenges and future directions," "...a systems framework").

### 3.B Review type and search methodology (the reproducibility axis)

- **PRISMA/PRISMA-ScR cited by name:** 5/8 (P2, P3, P4, P6, P7 use or reference PRISMA-style flow diagrams; P2 is the only one citing both PRISMA 2020 and PRISMA-ScR explicitly with sources). 2/8 (P5, P8) run an equally rigorous staged screening but never invoke the PRISMA name. 1/8 (P1) uses a PRISMA-style flow figure without citing the PRISMA standard itself.
- **Dedicated, numbered methodology section:** 7/8. The exception is P7, which describes its (single-database) search inside the Introduction with no standalone "Methods" heading.
- **Databases named:** 8/8 name at least one database. Web of Science and/or Scopus anchor most searches; ScienceDirect, IEEE Xplore, SpringerLink, Google Scholar, PubMed, and Wiley appear as secondary sources. One paper (P7) searches only a single database (Scopus).
- **Search strings/Boolean queries given:** 7/8 give at least a partial Boolean string; most give it verbatim (P2, P3, P5, P6, P7 all reproduce an actual query).
- **Inclusion/exclusion criteria:** stated in some form in 8/8, but only 6/8 use that literal phrase — P3 and P7 give equivalent numbered screening rules without labeling them "inclusion/exclusion criteria."
- **Numeric funnel (identified → screened → included):** given in 6/8 (P1, P2, P4, P5, P6, and partially P8); P3 and P7 give a flow diagram but less complete numeric detail in the prose.
- **PRISMA flow diagram (an actual figure):** 7/8. Only P8 has no dedicated flow-diagram figure.
- **Protocol registration:** 0/8 mention pre-registering a review protocol.
- **Reproducibility verdict:** roughly half (P2, P4, P6) are fully reproducible — exact queries, criteria, and a complete numeric funnel are all given. The rest (P1, P3, P5, P7, P8) are partly documented: databases and criteria are named, but some combination of the exact query, exclusion-reason breakdown, or final numeric total is missing or incomplete.

**Takeaway:** naming databases and giving some form of inclusion/exclusion logic is essentially required; formally branding the process as PRISMA/PRISMA-ScR and hitting every reporting box (protocol registration, full numeric funnel) is not — the journal's real bar sits at "transparent and mostly reproducible," not "formally systematic" in the Cochrane sense.

### 3.C Length and structure

- **Pages:** 19-33 (median 24, mode 19).
- **Body word count (excluding references):** ~11,500-19,850 words (median ~13,700).
- **Abstract:** unstructured single paragraph in 7/8; only P1 uses labeled Context/Objective/Method/Results/Conclusion sub-fields. Length 185-290 words (median ~233) — notably longer than a typical research-article abstract.
- **Elsevier "Highlights" bullets:** 0/8. None of the 8 sampled papers carry the separate 3-5-bullet Highlights block that Elsevier surfaces on some articles.
- **Sections:** 6-8 top-level numbered sections (median 7), with 13-33 total (sub)sections (median 22) — P2 is the most finely subdivided, P3/P7 the least.
- **Standard components:** Introduction (8/8), background/context folded into the introduction rather than a separate heading (common pattern), a dedicated Methodology/Methods section (7/8), a Challenges/Limitations section (8/8), a Future-directions section (8/8, though in 5/8 it's merged into the same section as Challenges rather than split out), a standalone "Discussion" heading (only 2/8: P2, and arguably P3 which merges it with future directions), Nomenclature/Acronym table as a real section (1/8: P8), formal Declarations (CRediT, competing interest, data availability) — present in essentially all (8/8, standard Elsevier back-matter).
- **Ends with future directions/open challenges:** 8/8 — every paper's second-to-last major section is Challenges/Future-directions/Roadmap, immediately followed by a short Conclusion.
- **Explicit "contributions of this review" statement:** 3/8 have it as a clearly labeled element (P2 as a paragraph, P6 as subsection 1.5, P7 as a numbered list); the other 5/8 make the novelty case less formally (a "gaps and contributions" subsection in P1, an "unlike previous reviews" sentence in P4/P5/P8, or nothing explicit in P3).

**Takeaway:** the skeleton is extremely consistent — Introduction → synthesis → Challenges → Future directions → short Conclusion — even though the labels and granularity of subsections vary a lot; a standalone "Discussion" section and a formal "Highlights" block are both the exception rather than the rule.

### 3.D Figures and tables

- **Figures:** 4-17 (median 12, mode 17). Figure counts correlate loosely with page count and with how hardware/device-photo-heavy the topic is.
- **Tables:** 2-12 (median 6, mode 4), counting appendix tables. Two papers (P2, P8) push their large synthesis tables into an Appendix (A1-A10 for P2; A.1-A.2 for P8) rather than the main body.
- **Recurring figure types**, roughly in order of prevalence: conceptual/framework diagrams (about 7/8), a literature-search/PRISMA-style flow diagram (7/8 — every paper except P8), bibliometric/scientometric plots — keyword co-occurrence networks, publication-trend bar charts, VOSviewer-style maps (6-7/8), taxonomy/classification diagrams (about half), device/example/sample photographs (5/8, concentrated in the more hardware-centric papers: P3, P4, P5, P7, P8), and comparison/performance charts (about half).
- **Recurring table types:** method/approach comparison tables (near-universal), at least one large multi-row synthesis table cataloguing many individual studies (present in some form in 7/8 — P7 is the exception, with only 2 modest tables), dataset-summary tables (common in the CV/AI-heavy papers), and taxonomy-adjacent tables.
- **Large synthesis table (many rows, one per study/method):** yes in 7/8, ranging from a couple of large in-body tables (P1, P5) to whole appendices of coded studies (P2's 10 appendix tables, P8's Table A.1 comparing prior reviews).
- **Graphics origin:** a genuine mix in every paper — conceptual/schematic figures and bibliometric plots are original/synthesized, while device photos and material-shape images are frequently reproduced (with attribution) from the underlying primary studies, especially in the more hardware-focused reviews (P4, P5, P7, P8).

**Takeaway:** a literature-flow figure and at least one large, many-row synthesis table are close to mandatory; the *mix* of figure types (how bibliometric- vs. hardware-photo-heavy the figure set is) tracks the sub-domain more than the journal's house style.

### 3.E References / corpus

- **Reference count:** 59-286 (median ~190, mean ~189). P7 is a clear outlier on the low end (59) — it draws on a narrower, more specialized VOC-sensor literature searched in a single database; P8 is the high end (286), reflecting the breadth of DEM/agricultural-engineering literature it surveys.
- **Recency (share published in last 5 years, ~2021-2026):** ranges enormously, from 9.3% (P6) to 83.1% (P5, P7). This is the single most heterogeneous quantitative feature in the sample. P6 is a genuine outlier, not a parsing artifact: it reviews long-running satellite/remote-sensing programs (Landsat, MODIS, Sentinel) and necessarily cites decades of foundational literature alongside recent work.
- **Recency (last 3 years, ~2023-2026):** 6.9%-75.4% (median ~45%).
- **Source mix:** overwhelmingly journal articles in every paper; conference proceedings are a small minority (roughly 0-7% by rough count) except where a paper explicitly draws on IEEE conference venues (P3, P5); preprints/arXiv appear only in P5 (a handful) and are otherwise essentially absent; books/theses are rare (a few theses in P2 only).
- **Bibliometric analysis of the corpus itself** (publication trend by year, keyword co-occurrence, country/author contribution): present in some form in 6/8 (P1, P2, P3, P4, P5 partially, P7, P8 partially); absent in P6, which is the only paper with no keyword-network or trend-over-time figure despite following PRISMA 2020 for its search.

**Takeaway:** journal-dominated reference lists and *some* corpus-level bibliometric figure (trend line or keyword map) are the norm; overall reference count and recency both vary by an order of magnitude depending on whether the sub-field is fast-moving (AI/CV: high recency) or has a long instrumental history (remote sensing: low recency).

### 3.F Content and framing

- **Scope breadth:** 7/8 are technology- or task-general (applicable across crops/species/materials); only 1/8 (P1) is single-crop.
- **Taxonomy/classification framework proposed:** 6-7/8 propose an explicit classification scheme (disease ontology in P1; information-type × operation-mode framework in P2; research-purpose taxonomy in P3; sensor-modality × function taxonomy in P4; equipment-development-stage × function taxonomy in P5; material-type × shape-model taxonomy in P8). P6 and P7 offer looser conceptual frameworks/thematic clusters rather than a formal taxonomy.
- **Gap analysis / research agenda:** 8/8.
- **Positions explicitly against prior reviews:** 6/8 do this with clear "unlike previous reviews..." language or a dedicated gap subsection (P1, P2, P4, P5, P6, P8); P3 does it implicitly via its research-question framing; P7's novelty case is a numbered contributions list rather than a direct contrast with prior reviews.
- **Quantitative synthesis depth:** ranges from strong (P1, P2, P5 tabulate reported accuracies/metrics across many individual studies) to moderate (P3, P4, P6, P7, P8 favor qualitative strengths/limitations comparison, with some quantitative tables but no large pooled-accuracy table).
- **Voice/person:** a near-even split — P2, P3, P4, P7 use first-person "we" at least occasionally (P7 most heavily); P1, P5, P6, P8 stay in third-person/passive voice throughout.
- **Equations:** essentially none — 0 numbered equations detected in 8/8 papers (even P8, on a numerically-flavored DEM topic, describes shape descriptors in prose/figures rather than numbered formulas). This is a genuine and slightly surprising near-universal trait for the sample.
- **Nomenclature/abbreviation table:** only 1/8 (P8) has a dedicated Nomenclature section; P1 instead front-loads a long abbreviation list inside the abstract block; the other 6/8 have no dedicated list at all (abbreviations are just expanded on first use in the text).

**Takeaway:** proposing some kind of classification framework and closing with a gap/future-research agenda are essentially required; how quantitatively the synthesis is done (pooled-accuracy tables vs. qualitative comparison) and whether the prose uses "we" are stylistic choices that vary by author group, not by journal convention.

---
## 4. The common outline

The modal section structure a new CEA review would be expected to follow, synthesized across the 8 papers:

- **1. Introduction**
  - Background / context for the problem (often unnumbered or a short subsection)
  - Research gaps and positioning against prior reviews (a sentence, a paragraph, or its own subsection)
  - Review methodology (search databases, Boolean query, inclusion/exclusion criteria, PRISMA-style flow diagram) — either as its own numbered top-level section ("2. Methods" / "2. Literature analysis methodology") or as a late subsection of the Introduction
- **2-3 (or up to 5). Thematic synthesis body**, organized around a proposed taxonomy or classification framework, typically one top-level section per major category of the taxonomy, each with 2-5 subsections going one or two levels deep (e.g., by sensor modality, by algorithm family, by material type, by operation mode)
  - At least one large, many-row synthesis table cataloguing individual studies (method, dataset, metric, reference)
  - A bibliometric or scientometric figure (publication-year trend and/or keyword co-occurrence map)
  - Device/example photographs where the topic is hardware-centric
- **Second-to-last section: Challenges / Limitations**, frequently combined with...
- **...Future directions / research agenda / roadmap** (sometimes its own section, sometimes a subsection of the same "Challenges and Future Directions" section)
- **Final section: Conclusion(s)** — short, often under a page, restating scope and key findings
- **Back matter:** CRediT authorship statement, competing-interest declaration, data-availability statement, references

A standalone "Discussion" section, a Nomenclature table, and Elsevier Highlights bullets are all optional extras layered onto this skeleton rather than part of the core template.

---

## 5. Near-universal vs. variable traits

**Likely required (present in 7-8/8 papers — treat as load-bearing conventions):**
- Colon-structured title (7/8)
- A named-database literature search with at least a partial Boolean string and some form of inclusion/exclusion logic (8/8)
- A literature-search flow diagram, PRISMA-branded or not (7/8)
- A dedicated, numbered Methods/Methodology section (7/8)
- Unstructured, single-paragraph abstract 185-290 words long (7/8)
- No Elsevier Highlights block (8/8)
- A proposed taxonomy or classification framework for the topic (6-7/8)
- A Challenges/Limitations section immediately followed by a Future-directions section, then a short Conclusion (8/8)
- Explicit gap analysis / research agenda (8/8)
- Journal-dominated reference list with minimal conference/preprint content (8/8)
- At least one large, many-row synthesis table (7/8)
- Zero or near-zero numbered equations (8/8)
- No dedicated Nomenclature/Acronym table (7/8 lack one)

**Optional / stylistic (present in roughly 1-5/8 papers — match to your own preference, not a journal requirement):**
- Explicit PRISMA/PRISMA-ScR branding by name (5/8)
- A complete numeric identified→screened→included funnel in the prose (6/8)
- A protocol-registration statement (0/8 — essentially never done in this sample)
- A standalone "Discussion" heading separate from Challenges/Future directions (2/8)
- A formally labeled "Contributions of this review" statement (3/8)
- Open-access publication (2/8)
- First-person "we" voice (4/8, and only one paper — P7 — uses it heavily)
- Single-crop/single-species scope (1/8; almost everything else is technology- or task-general)
- Structured (Context/Objective/Method/Results) abstract (1/8)
- A dedicated Nomenclature section (1/8)

---

## 6. Practical checklist / recommendations for matching CEA norms

1. **Title:** use a colon-structured title ("Topic: descriptive subtitle"). You don't need the literal word "review" or "survey" in the title — a phrase like "...challenges and future directions" or "...a systems framework" reads as equally review-like in this venue.
2. **Abstract:** write one unstructured paragraph, 200-290 words. Structured (Context/Objective/Method/Results) abstracts are rare here — only do this if you have a strong reason to.
3. **Search methodology:** name at least 2-3 databases (Web of Science and/or Scopus as the anchor, plus 1-2 secondary sources), give at least a partial Boolean query verbatim, state inclusion/exclusion rules (numbered rules are fine even without the literal words "inclusion criteria"), and include a literature-flow figure. Citing PRISMA/PRISMA-ScR by name is a nice-to-have, not required — roughly 5/8 papers do, 3/8 don't and are still functionally rigorous.
4. **Structure:** aim for 6-8 top-level sections and roughly 15-30 total (sub)sections. Put your search methodology either as a standalone numbered section or as the last subsection of the Introduction — both are common.
5. **Propose a taxonomy:** organize your synthesis body around an explicit classification scheme (by sensor type, by algorithm family, by material type, by operation mode, etc.) rather than a flat chronological or alphabetical survey.
6. **Figures/tables:** target roughly 10-15 figures and 4-8 tables (median observed: 12 figures, 6 tables). Include at minimum: (a) a literature-search flow diagram, (b) at least one large synthesis table (or an appendix of them) cataloguing individual studies with method/dataset/metric/reference columns, and (c) if feasible, a bibliometric figure (publication-year trend and/or keyword co-occurrence map) — this appeared in 6-7/8 papers.
7. **Close with a two-part ending:** a Challenges/Limitations section immediately followed by (or merged with) a Future-directions/research-agenda section, then a short (well under a page) Conclusion. Every paper in the sample ends this way.
8. **References:** expect somewhere in the 150-250 range for a comprehensive technology review (median ~190); a narrower sub-topic (like P7's plant-wearable VOC sensors) can be well-supported with as few as ~60. Keep the source mix journal-dominated; conference papers and preprints should be a small minority unless your sub-field is genuinely conference-driven.
9. **Skip:** the Elsevier Highlights block, numbered equations (unless your topic is genuinely equation-derivation-heavy), and a dedicated Nomenclature table — none of these are expected by default in this venue/genre.
10. **State your novelty explicitly** somewhere near the end of the Introduction — as a labeled "Contributions" statement, a "Research gaps and contributions" subsection, or simply an "unlike previous reviews..." sentence. Some form of this appeared in every paper that engaged with prior reviews at all (6-7/8).

---

## 7. Caveats

- **N = 8.** Every percentage and "X/8" figure above describes this specific sample, not CEA review articles as a whole. Do not treat any single-paper trait (e.g., "only P1 uses a structured abstract") as evidence that the trait is rare or common in the broader journal — with 8 data points, one paper is 12.5% of the "vote."
- All 8 sampled papers happen to be very recent (2026, still carrying "article in press" article numbers rather than assigned volume/issue numbers) and are all applied-engineering/technology reviews (AI, sensors, robotics, DEM) rather than biological, agronomic, or purely bibliometric reviews. Conventions for other CEA review sub-genres (e.g., a purely agronomic or economics-focused review) may differ.
- **Reference counts and recency percentages are automated approximations.** They were derived by regex-parsing the bibliography (splitting on "Surname, I., ... year." patterns) rather than by manually counting every entry. Cross-checks on two papers (the shortest, P7, and a mid-length one) confirmed the method produces an accurate count, but expect ±5-10 entries of noise on any individual paper, and treat the recency percentages as indicative rather than exact.
- **Page counts** are physical page-image counts (one JPEG per typeset page as delivered), which should match the published PDF pagination but were not cross-checked against an independently paginated copy.
- **Figure/table counts** were derived from the highest caption number found per paper (e.g., "Fig. 17" implies 17 main-body figures) plus a separate count of appendix tables (Table A.1, A.2, ...). This is reliable when captions are sequential and complete, which they were in all 8 papers on inspection, but a genuinely missing or renumbered caption could cause a small undercount.
- **No papers were unparsed.** All 8 source files were text-extractable in full (the "PDF" files were archives containing per-page text and images with a clean, non-OCR text layer), so no paper had to be excluded or flagged as unreadable.
- Several qualitative judgments (figure/table "type" categorization, the background/synthesis/future percentage split, quantitative-synthesis-depth ratings, voice/person characterization) are impressions formed from reading captions, headings, and representative passages rather than a sentence-by-sentence classification of every page. Where a synthesis claim rests on this kind of judgment rather than a hard count, it is described in qualitative language ("moderate," "strong," "roughly") rather than given a false-precision number.

---
## Appendix A — Per-paper feature matrix

The full matrix (67 features × 8 papers) is transposed below for readability (features as rows, papers as columns) and is also provided as a separate, fully machine-readable file, `review_features.csv`, with one row per paper and one column per feature. Numeric approximations (reference counts, recency percentages, section/subsection counts) were obtained by automated parsing of the extracted text as described in the Caveats section, not by exhaustive manual counting of every entry.

| Feature | P1 (Wheat disease AI survey) | P2 (Ag navigation path-planning review) | P3 (Insect behavior phenotyping survey) | P4 (Wearable sensors for livestock review) | P5 (Insect management equipment review) | P6 (Climate-smart ag monitoring framework) | P7 (Plant wearables for VOC detection) | P8 (DEM shape modelling review) |
|---|---|---|---|---|---|---|---|---|
| **A. Bibliographic / metadata** |  |  |  |  |  |  |  |  |
| full_title | Global wheat disease identification via AI technologies: An in-depth survey with sustainability and future projections | Research progress of autonomous navigation path planning methods for agricultural ground machinery: a review | Automated insect behavioral phenotyping with computer vision and deep learning: Current knowledge and future directions | A comprehensive review of wearable sensors for animal information acquisition in precision livestock farming | Intelligent integration in agricultural insect management equipment: applications, challenges, and future directions | Multi-sensor integration and cloud-native AI for climate-smart agricultural monitoring: A systems framework | Plant wearables in smart agriculture: advancements, technical challenges, opportunities, and a cyber-physical roadmap in volatile organic compound detection | Modelling the shapes of agricultural materials in DEM: methods, advances, and challenges |
| authors_n | 3 | 4 | 5 | 7 | 10 | 6 | 2 | 6 |
| countries | China | China | China; Australia | China; Serbia; Malaysia | China | Czech Republic; Hungary; Turkiye | Philippines | China |
| institutions_n | 1 | 1 | 4 | 5 | 3 | 4 | 1 | 2 |
| single_or_multi_institution | single | single | multi | multi | multi | multi | single | multi (same country) |
| year | 2026 | 2026 | 2026 | 2026 | 2026 | 2026 | 2026 | 2026 |
| article_no | 112042 | 112078 | 112110 | 112175 | 112178 | 112182 | 112188 | 112215 |
| open_access | No (subscription) | No (subscription) | No (subscription) | No (subscription) | No (subscription) | Yes (CC BY) | Yes (CC BY-NC) | No (subscription) |
| keywords_n | 5 | 6 | 5 | 5 | 4 | 5 | 4 | 4 |
| keywords | Wheat diseases; Artificial intelligence; Vision system; Robotic; Sustainable development goals | Agricultural ground machinery; Autonomous navigation; Path planning; Multi-vehicle cooperation; Sensor fusion; Static-real-time-hybrid information | Insect behavior; Computer vision; Deep learning; Object tracking; Behavior quantification | Wearable sensor; Animal information acquisition; Precision livestock farming; Systematic literature review; Sensor fusion | Intelligence integration; Insect management; Edge device; Pest monitoring | Machine learning; Multi-sensor data fusion; Cloud-native computing; Google earth engine; Agricultural monitoring | Conducting polymer; Plant wearable sensor; Smart agriculture; Volatile organic compound | Discrete Element Method; Agricultural Materials; Particle Shape Modelling; Non-spherical Particles |
| title_has_review_survey_word | survey | review | none (title uses 'Current knowledge and future directions') | review (comprehensive review of) | none (title uses 'applications, challenges, and future directions') | none (title uses 'A systems framework') | none (title uses 'advancements, technical challenges, opportunities... roadmap') | none (title uses 'methods, advances, and challenges') |
| title_has_colon | Y | Y | Y | No | Y | Y | Y | Y |
| title_scope | single-crop (wheat) | task-general (navigation/path planning), crop-general | task-general (insect behavior), organism-general | technology-general (wearable sensors), animal/livestock-general | task-general (insect management equipment) | technology-general (multi-sensor/cloud AI), crop-general | technology-general (plant wearables/VOC), crop-general | technology-general (DEM shape modelling), material-general (not crop-specific) |
| **B. Review type & search methodology** |  |  |  |  |  |  |  |  |
| declared_review_type | Self-styled 'Global Comprehensive Survey (GCS)'; PRISMA-style screening but not branded systematic/scoping | Scoping review (PRISMA-ScR) | Systematic literature review framed around 4 research questions (RQ1-RQ4), not explicitly PRISMA-branded as 'systematic review' | Self-labeled 'Systematic literature review' (keyword) but explicitly caveats it is a narrative synthesis, not formal quality-appraised systematic review | Narrative review with a systematic (Boolean, dual-database) search protocol; not PRISMA-branded | Structured literature analysis following PRISMA 2020 (search/selection only); explicitly NOT a formal meta-analysis; synthesized thematically | Narrative review with PRISMA-screened literature survey (search described in intro, no standalone Methods section) | Self-labeled 'systematic literature review (SLR)' explicitly contrasted with 'traditional narrative reviews' |
| cites_reporting_standard | PRISMA (used for flow diagram only, not named as PRISMA-2020/ScR) | PRISMA 2020 + PRISMA-ScR (explicitly named and cited) | PRISMA (flowchart used, not explicitly 'PRISMA 2020' cited) | PRISMA (guidelines followed for flow/reporting) | No (no PRISMA/PRISMA-ScR citation found) | PRISMA 2020 (explicitly cited, Page et al. 2021) | PRISMA (PRISMA2020 flow diagram cited/used) | No (no PRISMA/PRISMA-ScR citation; generic 3-stage SLR screening only) |
| dedicated_methodology_section | Yes - 1.4 Review methodology (+1.4.1-1.4.3) | Yes - Section 2 'Methods' with 7 subsections (2.1-2.7) | Yes - Section 3 'Research methodology' (3.1-3.2) | Yes - Section 2 'Materials and methods' (2.1-2.2) | Yes - embedded in Section 2 'Development of Insect Management Equipment and Review Methodology' (2.2 Review Methods and Summary) | Yes - 1.4 'Literature search and review methodology' (embedded in Introduction, not a standalone numbered section) | No standalone numbered Methods section - search described within Introduction/Highlights | Yes - Section 2 'Literature analysis methodology' |
| databases_named | Web of Science; ScienceDirect; IEEE Xplore; SpringerLink; Google Scholar | Web of Science Core Collection (primary) + backward/forward snowballing | ScienceDirect; SpringerLink; Wiley Online Library; Web of Science | Scopus; ScienceDirect; IEEE Xplore; PubMed; Web of Science | Scopus; Web of Science; supplemented by IEEE Xplore; SpringerLink | Web of Science; Scopus; Google Scholar | Scopus (only) | Scopus (primary); Google Scholar (supplementary); ScienceDirect/Elsevier & MDPI (publisher-specific) |
| search_string_given | Partial (Boolean fragment: identification OR Vision system OR Robotics) | Yes, full Boolean WoS query given verbatim | Yes (S1 AND S2 AND S3 AND S4 Boolean structure given) | Yes, per-database search terms given (e.g., 'Wearable sensors AND farm animals') | Yes (WoS Boolean example given: (target OR trajectory OR image) AND (detection OR classification OR tracking OR phenotype) AND (pest OR insect)) | Yes (Table 1 lists exact per-database queries) | Yes (full search syntax with quoted terms given verbatim) | Yes (keywords/logic described, partial Boolean detail) |
| date_range_coverage | 1960-2025 (bibliometric corpus); AI era focus 2018-2025 | Jan 2019 - Sep 2025 | 2015-2025 (primary studies) | 2015-2025 | Jan 2021 - May 2026 (screening); cited work mostly 2020-2026 | 2000-2025 (search completed Dec 2025) | 2019-2026 | Not fully specified as a date range in prose (implied recent + foundational DEM literature back to 1979 Cundall) |
| inclusion_exclusion_stated | Yes (dedicated 1.4.3 subsection) | Yes (2.3 Inclusion and exclusion criteria) | Functionally yes - 5 numbered refinement rules, though not literally labeled 'inclusion/exclusion criteria' | Yes (predefined inclusion/exclusion criteria applied in Rayyan screening) | Yes (3 numbered inclusion standards under 'Literature Inclusion') | Yes (explicit inclusion/exclusion criteria listed) | Functionally yes (screening exclusion conditions listed), not literally labeled 'inclusion/exclusion criteria' | Yes (explicit inclusion/exclusion criteria defined) |
| records_at_each_stage | 1543 identified -> 575 after dedup/auto-exclude -> 382 after title/keyword screen -> 315 sought -> 191 assessed -> 175 included | 564 records screened -> 210 studies included (3-stage: title/abstract/full-text) | Not fully quantified at each PRISMA stage in text (flowchart carries numbers; not repeated in prose) | 1984 identified -> 738 after type restriction -> 683 after dedup -> screened in Rayyan -> 98 studies included | 1773 identified (757 Scopus + 672 WoS + others) -> 817 after dedup -> 486 after title/abstract screen -> 330 full texts assessed | 230 identified -> 160 after dedup/date-lang filter -> 135 full-text eligible -> +4 supplementary -> 160 total cited | 17 excluded at initial screening -> 76 reports sought -> 24 unretrievable -> final included set not explicitly totalled in prose | 2126 identified across sources -> 3-step screening (dedup, title/abstract, full-text) -> final N not explicitly stated as single number in prose |
| prisma_flow_diagram | Yes (Fig. 5) | Yes (Fig. 1, PRISMA-ScR flow diagram) | Yes (Fig. 1) | Yes (Fig. 2) | No formal PRISMA-labeled diagram, but an equivalent screening flow figure (Fig. 2) | Yes (Fig. 2, 4-stage PRISMA 2020 workflow) | Yes (Fig. 1a) | No (no PRISMA-branded flow diagram figure) |
| protocol_registration | No | No | No | No | No | No | No | No |
| reproducibility_verdict | Partly documented (databases + numeric flow given; full Boolean string and exclusion reasons not fully itemized) | Reproducible - full query, criteria, coding scheme, and PRISMA-ScR flow all given | Partly documented (databases + Boolean logic given; stage-by-stage counts less explicit in prose than P2) | Reproducible - per-database queries, restriction rules, and full numeric flow given | Reproducible - full numeric flow and Boolean query given, though not PRISMA-branded | Reproducible - exact queries (Table 1), dates, and PRISMA flow all given | Partly documented (single database only, full query given, but final N and per-stage totals less complete than P2/P4/P6) | Partly documented (sources and criteria described; no visual flow diagram or exact final count given) |
| **C. Length & structure** |  |  |  |  |  |  |  |  |
| page_count | 27 | 33 | 19 | 21 | 30 | 19 | 21 | 29 |
| body_word_count_excl_refs | 16146 | 19847 | 11903 | 13164 | 15627 | 12761 | 11472 | 14313 |
| total_word_count_incl_refs | 21209 | 25651 | 16218 | 17950 | 22427 | 18183 | 13298 | 22777 |
| highlights_present | No | No | No | No | No | No | No | No |
| abstract_word_count | 286 | 290 | 199 | 185 | 211 | 255 | 219 | 246 |
| abstract_structured | Yes (Context/Objective/Method/Results labels) | No (single unstructured paragraph) | No | No | No | No | No | No |
| top_level_sections_n | 7 | 7 | 7 | 8 | 6 | 6 | 6 | 8 |
| subsections_approx_n | 26 | 33 | 16 | 22 | 13 | 26 | 13 | 22 |
| heading_outline | 1 Introduction>1.1 Background>1.2 Wheat disease taxonomy>1.3 Research gaps & contributions>1.4 Review methodology(1.4.1-1.4.3) / 2 WD discovery technologies(2.1-2.4) / 3 Wheat machinery innovation(3.1-3.2, 3.2.1-3.2.5) / 4 Accession of WD resource data / 5 Bibliometric analysis pattern(5.1-5.2) / 6 Limitations & future directions(6.1-6.2) / 7 Conclusion | 1 Intro / 2 Methods(2.1-2.7) / 3 Navigation problems & scenarios(3.1-3.5) / 4 Single-vehicle navigation(4.1-4.4, w/ 4.1.1-4.4.2) / 5 Multi-vehicle navigation(5.1-5.2, w/ subsubsections) / 6 Discussion(6.1-6.5) / 7 Conclusions | 1 Intro / 2 Motivation & problems(2.1) / 3 Research methodology(3.1-3.2) / 4 Methodological framework(4.1-4.2, 4.2.1-4.2.5) / 5 Public datasets & platforms / 6 Discussion & future directions / 7 Conclusion | 1 Intro / 2 Materials & methods(2.1-2.2) / 3 Results(3.1-3.2) / 4 Research settings / 5 Research subject: Farm animals / 6 Wearable sensors by modality(6.1-6.5, many sub-subsections) / 7 Challenges, Prospects, future roadmap(7.1-7.3) / 8 Conclusions | 1 Intro / 2 Development of equipment & review methodology(2.1-2.2) / 3 Intelligent function integration(3.1-3.3) / 4 Intelligent hardware integration(4.1-4.2) / 5 Challenges & future directions(5.1-5.2) / 6 Conclusion | 1 Intro(1.1-1.5 incl. methodology & contribution) / 2 RS platforms(2.1-2.3) / 3 Key applications(3.1-3.4, w/ sub-subsections) / 4 Integration approaches(4.1-4.2) / 5 Limitations/emerging tech/priorities(5.1-5.5, w/ 5.5.1-5.5.3) / 6 Conclusions | 1 Intro / 2 Plant wearable sensors for VOCs(2.1-2.4) / 3 AI for data processing(3.1-3.2) / 4 Global trends & gaps(4.1-4.2, w/ sub-subsections) / 5 Plant wearable VOC-sensing roadmap / 6 Conclusion and recommendation | 1 Intro / 2 Literature analysis methodology / 3 Shape modelling approaches(3.1-3.3) / 4 Shape measurement & characterisation(4.1-4.3) / 5 Shape modelling by material type(5.1-5.4, w/ 5.4.1-5.4.2 & deeper) / 6 Practical considerations(6.1) / 7 Challenges & outlook(7.1-7.4) / 8 Conclusions |
| has_intro | Y | Y | Y | Y | Y | Y | Y | Y |
| has_background | Y | Y (in intro) | Y (sec 2) | Y | Y (sec 2.1 developmental stages) | Y (1.1-1.3) | Y (in intro & sec2) | Y |
| has_methodology_section | Y | Y | Y | Y | Y (2.2) | Y (1.4, within intro) | No (search embedded in intro, no numbered section) | Y (sec 2) |
| has_challenges_section | Y | Y (6.4 cross-cutting gaps) | Y (embedded in sec2/6) | Y (sec 7.1) | Y (sec 5.1) | Y (5.1) | Y (4.2) | Y (sec 7) |
| has_future_directions_section | Y | Y (6.5) | Y (sec 6, in title) | Y (sec 7.2-7.3) | Y (sec 5.2) | Y (5.5, w/ short/med/long-term subsections) | Y (sec 5, framed as roadmap) | Y (sec 7, 'outlook') |
| has_discussion_section | No (merged into 6) | Y (separate sec 6) | Y (merged w/ future dir., sec 6) | No separate Discussion (folded into sec 7) | No separate Discussion | No separate Discussion | No separate Discussion | No separate Discussion (sec 6 practical considerations serves similar role) |
| has_nomenclature_table | Partial (abstract-level abbreviation list, not a separate section) | No | No | No | No | No | No | Yes - dedicated Nomenclature/Abbreviations section |
| has_declarations | Y (Data availability, refs) | Y | Y | Y | Y | Y | Y (CRediT, competing interest) | Y |
| ends_with_future_directions | Yes (sec 6, followed by short sec 7 conclusion) | Yes (future directions embedded as 6.5, then sec 7 conclusion) | Yes (sec 6 combines discussion+future, then short sec 7 conclusion) | Yes (sec 7, then short sec 8 conclusion) | Yes (sec 5, then short sec 6 conclusion) | Yes (sec 5, then short sec 6 conclusion) | Yes (sec 5 roadmap, then sec 6 conclusion+recommendation) | Yes (sec 7 Challenges & outlook, then sec 8 conclusion) |
| contributions_statement | Yes - dedicated subsection 1.3 'Research gaps and contributions' | Yes - explicit paragraph 'This review makes three main contributions...' | No explicit labeled 'contributions' statement (uses RQ framing instead) | No labeled 'contributions' section, but explicit 'Unlike earlier reviews...' novelty claim in abstract | No dedicated labeled section, novelty claim inline ('Unlike previous...') | Yes - dedicated subsection 1.5 'Contribution of this review compared to existing literature' | Yes - explicit 'The key contributions of this study are the following:' (3 numbered items) | No explicitly labeled 'contributions' section, but explicit gap statement vs. prior DEM reviews in intro |
| **D. Figures & tables** |  |  |  |  |  |  |  |  |
| figures_n | 17 | 11 | 13 | 8 | 14 | 4 | 9 | 15 |
| tables_n | 8 | 12 | 4 | 4 | 11 | 7 | 2 | 5 |
| figs_per_page | 0.63 | 0.33 | 0.68 | 0.38 | 0.47 | 0.21 | 0.43 | 0.52 |
| tabs_per_page | 0.3 | 0.36 | 0.21 | 0.19 | 0.37 | 0.37 | 0.1 | 0.17 |
| figure_types | Conceptual/framework(1); taxonomy(1); PRISMA flow(1); bibliometric/trend plots(6+); sample/device images(1); comparison charts(4) | PRISMA-ScR flow(1); bibliometric VOSviewer keyword maps(2); trend bar charts(2); conceptual framework(1); comparison chart(1); commercial systems photo montage(1); sensor/algorithm config diagrams(2-3) | PRISMA flow(1); bibliometric trend(1); conceptual framework(3); method/architecture diagrams(4); taxonomy(1); sample/data-acquisition images(1); annotation-type diagram(1); overview/summary(1) | Conceptual/research framework(1); PRISMA-like flow(1); bibliometric trend+keyword network(2); sensor hardware/example photos(4) | Conceptual/stagewise framework(2); screening-process flow(1); performance/comparison charts(3); taxonomy/classification(2); device/example photos(4); hardware comparison(1); roadmap(1) | Conceptual/integration framework(2); PRISMA flow(1); time-series/data plot(1); NO bibliometric keyword-network figure | PRISMA flow + keyword network combo(1); device/sensor photos & schematics(5); validation/performance plots(2); roadmap diagram(1) | Bibliometric keyword network(1); classification/taxonomy diagrams(2); shape-descriptor diagrams(1); method/workflow diagrams(2); material example photos(6); comparison plot(1); selection flowchart(1) |
| table_types | Dataset tables; method/performance comparison tables; large multi-row synthesis tables (disease-model-outcome-reference) | Main synthesis table(s) + 10 appendix tables (A1-A10) of coded studies - dataset/method/scenario summary tables | Method comparison (Transformer algorithms); dataset/platform summary; taxonomy-adjacent table | Sensor/method comparison; performance-metric tables | Large multi-row comparison tables (algorithms, devices, advantages/limitations); performance tables | Search-query table; platform/sensor comparison tables; framework comparison table | Comparison tables only (plant wearables vs conventional methods; sensor summary) | Large appendix comparison tables (A.1 prior-reviews comparison; A.2 software list) + main-text method/application tables |
| large_synthesis_table | Yes, 2 large multi-row tables (disease/model/accuracy/reference, ~30+ rows combined) | Yes - 10 appendix tables cataloguing all 210 coded studies | Moderate - largest table (Transformer methods) is comparison-style, not exhaustive study-by-study | Moderate (tables are comparison-style, not one giant 98-study table in main text) | Yes - several large tables (e.g., Transformer algorithms; device advantages/limitations) with many rows | Moderate - comparison tables (e.g., platform specs) rather than one-row-per-study catalogue | No (only 2 tables, modest size) | Yes - Table A.1 compares representative prior DEM reviews; application tables list many material/process examples |
| graphics_origin_split | Mostly original/synthesized (bibliometric + schematic); few reproduced device photos | Mostly original except commercial-system photos (Fig.10, reproduced/promotional) | Mostly original, several 'modified from' cited prior figures (explicitly attributed) | Mix - hardware photos largely reproduced from cited device papers; frameworks original | Mix of original schematics and reproduced device/detection-result photos (attributed) | Mostly original conceptual diagrams; time-series plot appears illustrative/synthesized | Mix - several sensor photos reproduced from cited device papers, roadmap original | Mix - material/shape photos mostly reproduced (attributed) from cited studies; diagrams original |
| **E. References / corpus** |  |  |  |  |  |  |  |  |
| references_n_approx | 179 | 201 | 159 | 177 | 236 | 216 | 59 | 286 |
| ref_last5y_pct | 62.6 | 74.1 | 73.0 | 54.2 | 83.1 | 9.3 | 83.1 | 62.2 |
| ref_last3y_pct | 43.6 | 42.8 | 55.3 | 33.3 | 75.4 | 6.9 | 72.9 | 46.5 |
| ref_source_mix | ~overwhelmingly journal articles; conference ~2%; ~0% preprints/books | Predominantly journal articles; conference ~0% detected; a few theses | Mostly journals; conference ~4-5%; a couple preprints | Mostly journals; some conference (IEEE Access etc.) | Mostly journals; conference ~4%; several preprints/arXiv (8) | Mostly journals; some conference; notably many older (pre-2015) foundational remote-sensing/satellite-program citations | Mostly journals; conference ~2%; no preprints detected | Predominantly journals; conference ~2%; no preprints detected |
| bibliometric_analysis_of_corpus | Yes (Fig.8-9,15-16: publication trends, keyword co-occurrence, author/country contribution) | Yes (keyword co-occurrence/density maps, studies-per-year by category) | Yes (Fig.2 yearly/topic-wise spread) | Yes (Fig.3 pubs/year, Fig.4 keyword co-occurrence) | Partial (trend commentary, no dedicated VOSviewer-style figure) | No (no keyword co-occurrence/VOSviewer-style figure; only Table 1 query yields) | Partial (keyword association network only, Fig.1b, no publication-year trend chart) | Partial (keyword co-occurrence network, Fig.1, no publication-year trend chart) |
| **F. Content & framing** |  |  |  |  |  |  |  |  |
| scope_breadth | single-crop, technology-general within it | task-general, crop/machinery-general | task-general, organism-general (all insects), cross-crop | technology-general, cross-species (livestock) | task-general (pest/insect management equipment), cross-crop | technology-general, crop-general | technology-general, crop-general | technology-general, material-general (grains/stems/leaves/composites) |
| taxonomy_proposed | Yes - wheat disease ontology (awn/spike/stem/root x symptom/yield/quality) | Yes - 2D framework: information type (static/real-time/hybrid) x operation mode (single/multi-vehicle) | Yes - taxonomy of research purposes on insect behavior quantification (Fig.11) | Yes - sensor modality taxonomy (motion/acoustic/optical/thermistor/other) x monitoring function | Yes - 4-stage equipment-development taxonomy + function-based classification (detection/tracking/phenotyping) | Partial - conceptual integration framework rather than a formal taxonomy | No formal taxonomy, but thematic clustering of literature (3 clusters in Fig.1b) | Yes - materials classified into granular/rod/shell/mixture-composite types x single/multi-element shape models |
| gap_analysis_present | Yes (sec 1.3, sec 6.1) | Yes (6.4 Cross-cutting research gaps) | Yes (sec 2.1 Limitations in studying insect behaviors; sec 6) | Yes (sec 7.1 Challenges) | Yes (sec 5.1) | Yes (sec 5.1, 5.3) | Yes (sec 4.2 Technological gaps and challenges) | Yes (sec 7, and explicit gap statement in intro re: prior DEM reviews) |
| positions_against_prior_reviews | Yes (via 'Research gaps and contributions' subsection) | Yes (explicit 'Existing reviews have provided...' + 4 stated limitations of prior reviews) | Implicit via RQ framing and motivation section rather than explicit 'unlike previous reviews' language | Yes (abstract: 'Unlike earlier reviews that focus mainly on single species...') | Yes ('Unlike previous... existing reviews have not effectively categorized...') | Yes (dedicated 1.5 + 'Unlike previous reviews...' language later) | Weak/implicit (no explicit 'unlike previous reviews' phrase found; novelty framed via contributions list) | Yes ('In contrast, existing reviews of DEM... emphasise parameter calibration... A systematic review focusing specifically on shape modelling... remains lacking') |
| pct_background_vs_synthesis_vs_future | ~15% background / ~65% synthesis / ~20% future (approx, qualitative) | ~10% background / ~75% synthesis / ~15% future (approx) | ~15% background / ~70% synthesis / ~15% future (approx) | ~10% background / ~75% synthesis / ~15% future (approx) | ~15% background / ~70% synthesis / ~15% future (approx) | ~20% background / ~60% synthesis / ~20% future (approx) | ~15% background / ~65% synthesis / ~20% future (approx) | ~10% background / ~75% synthesis / ~15% future (approx) |
| quantitative_synthesis_depth | Strong - tabulates per-study accuracy/model/dataset across many studies | Strong - converts heterogeneous accuracy/error metrics to comparable units (Fig.7) | Moderate - qualitative strengths/limitations comparison more than pooled accuracy tables | Moderate - performance descriptors more than pooled accuracy tables; self-acknowledged lack of formal quality appraisal | Strong - many per-study accuracy/dataset entries tabulated | Moderate - platform/technique comparison tables, not pooled accuracy synthesis | Moderate - some quantitative performance data (sensitivity, response) in tables/figures | Moderate-strong - accuracy/efficiency trade-off comparisons (Fig.14) and structured decision framework |
| voice_person | Third-person/passive (minimal 'we') | Mixed, moderate 'we' usage | Mixed, some 'we' | Mixed, low-moderate 'we' | Third-person/passive (no 'we' detected) | Third-person/passive (no 'we' detected) | Frequent 'we' - most first-person of the sample | Third-person/passive (no 'we' detected) |
| equations_n | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| nomenclature_table | No dedicated table (abbreviation list embedded in abstract only) | No | No | No | No | No | No | Yes (dedicated section) |

---

## Appendix B — Per-paper profiles

### P1 — Global wheat disease identification via AI technologies: An in-depth survey with sustainability and future projections

**Heading outline:**
1. Introduction (1.1 Background, 1.2 Wheat disease standardized taxonomy, 1.3 Research gaps and contributions, 1.4 Review methodology [1.4.1 Screening process, 1.4.2 Search strategy, 1.4.3 Inclusion & exclusion criteria])
2. Wheat disease discovery technologies (2.1 Image processing system advancement [2.1.1-2.1.4], 2.2 Classification algorithm schemes, 2.3 Progress of detecting systems, 2.4 Advances of segmentation applications)
3. Wheat machinery innovation (3.1 UAV revolution, 3.2 Robotic innovation [3.2.1-3.2.5 by sensor type])
4. Accession of WD resource data
5. Bibliometric analysis pattern (5.1 Performance analysis, 5.2 Science mapping and thematic evolution)
6. Limitations and future directions (6.1 Limitations, 6.2 Future perspective)
7. Conclusion

**Notable traits:** Only paper with a structured (Context/Objective/Method/Results) abstract. Uses PRISMA-style screening (1,543 → 175 included) without ever citing PRISMA by name. Massive inline abbreviation glossary embedded directly in the abstract block (60+ terms) rather than a separate Nomenclature section. Single-crop scope (the only one in the sample). Strong quantitative synthesis — tabulates per-study accuracy/model/dataset across ~2 large tables.

### P2 — Research progress of autonomous navigation path planning methods for agricultural ground machinery: a review

**Heading outline:**
1. Introduction
2. Methods (2.1 Data sources, 2.2 Data search strategy, 2.3 Inclusion and exclusion criteria, 2.4 Study selection and screening [PRISMA-ScR], 2.5 Data extraction and coding, 2.6 Analytical framework, 2.7 Evidence synthesis and descriptive statistical analysis)
3. Navigation problems, application scenarios and analytical framework (3.1-3.5)
4. Single-vehicle navigation (4.1-4.4, with 4.1.1-4.4.2 sub-subsections)
5. Multi-vehicle cooperative navigation and path planning (5.1-5.2, with sub-subsections)
6. Discussion (6.1-6.5)
7. Conclusions

**Notable traits:** The most methodologically rigorous paper in the sample — explicitly follows both PRISMA 2020 and PRISMA-ScR, gives a full verbatim Boolean query, and reports a complete numeric funnel (564 screened → 210 included). The only paper with a standalone, clearly-labeled "Discussion" section distinct from its conclusion. Pushes its large synthesis tables into a 10-part appendix (Table A1-A10) rather than the main body. Most finely subdivided outline in the sample (33 total sections/subsections).

### P3 — Automated insect behavioral phenotyping with computer vision and deep learning: Current knowledge and future directions

**Heading outline:**
1. Introduction
2. Motivation and problems (2.1 Limitations in studying insect behaviors)
3. Research methodology (3.1 Search and selection strategies, 3.2 Comprehensive science mapping analysis)
4. Methodological framework in the literature (4.1 Literature overview, 4.2 Framework overview [4.2.1-4.2.5])
5. Public datasets and available platforms
6. Discussion and future directions
7. Conclusion

**Notable traits:** Structures its motivation around four explicit research questions (RQ1-RQ4) rather than a conventional "gaps and contributions" narrative — an alternative way of positioning the review that still functions as a gap statement. Uses numbered screening rules without ever using the phrase "inclusion/exclusion criteria." Several figures are explicitly labeled "modified from" a cited source rather than fully original. Shortest top-level section count tied with P7 (6-7 sections) but a moderately fine subsection breakdown.

### P4 — A comprehensive review of wearable sensors for animal information acquisition in precision livestock farming

**Heading outline:**
1. Introduction
2. Materials and methods (2.1 Literature search strategy, 2.2 Literature screening and selection)
3. Results (3.1 Literature search results, 3.2 Literature analysis)
4. Research settings
5. Research subject: Farm animals
6. Animal information acquisition: Role of wearable sensors (6.1-6.5, many sub-subsections by sensor type)
7. Challenges, Prospects, and future roadmap (7.1-7.3)
8. Conclusions

**Notable traits:** The only paper in the sample to self-label as a "Systematic literature review" in its own keywords, yet its limitations section explicitly walks that back, describing the result as "a narrative synthesis of the current technical evidence base rather than... a systematic assessment of evidence quality" — a candid, unusually self-aware methodological caveat. Fully reproducible search (five databases, per-database query strings, full numeric funnel to 98 included studies). Most authors' countries of any paper in the sample (China, Serbia, Malaysia).

### P5 — Intelligent integration in agricultural insect management equipment: applications, challenges, and future directions

**Heading outline:**
1. Introduction
2. Development of Insect Management Equipment and Review Methodology (2.1 Stages of Equipment Development, 2.2 Review Methods and Summary)
3. Intelligent Function Integration in Insect Management (3.1-3.3)
4. Intelligent Hardware Integration in Insect Management (4.1-4.2)
5. Challenges and future directions (5.1-5.2)
6. Conclusion

**Notable traits:** Largest author team in the sample (10 authors). Highest reference count relative to its length and highest last-5-year recency (83.1%) alongside P7. Dual-database (Scopus + Web of Science) search with an identical Boolean query applied to both — a nice reproducibility touch even without PRISMA branding. Rich synthesis tables (algorithm comparisons, device advantages/limitations) with many rows. No first-person "we" detected anywhere in the text.

### P6 — Multi-sensor integration and cloud-native AI for climate-smart agricultural monitoring: A systems framework

**Heading outline:**
1. Introduction (1.1 Climate change impacts, 1.2 Need for technology-driven solutions, 1.3 Role of remote sensing, 1.4 Literature search and review methodology, 1.5 Contribution of this review compared to existing literature)
2. Remote sensing platforms for agricultural monitoring (2.1-2.3)
3. Key applications of remote sensing for climate-smart agriculture (3.1-3.4, with sub-subsections)
4. Integration approaches and enabling technologies (4.1-4.2)
5. Limitations, emerging technologies, and research priorities (5.1-5.5, including short/medium/long-term future-research subsections)
6. Conclusions

**Notable traits:** One of only two open-access papers in the sample (CC BY). The only paper with an explicitly labeled "Contribution of this review" subsection (1.5) placed inside the Introduction. Fewest figures in the sample (4) but a healthy 7 tables. Reference list skews dramatically older than any other paper (~9% published in the last 5 years) because it must cite decades of foundational satellite/remote-sensing-program literature (Landsat, MODIS, Sentinel) — a genuine domain-driven outlier, not a data artifact. No bibliometric/keyword-network figure, unusual for the sample.

### P7 — Plant wearables in smart agriculture: advancements, technical challenges, opportunities, and a cyber-physical roadmap in volatile organic compound detection

**Heading outline:**
1. Introduction
2. Plant wearable sensors for volatile organic compound... (2.1-2.4)
3. Artificial intelligence for data processing, stress... (3.1-3.2)
4. Global trends and technological gaps (4.1-4.2, with sub-subsections)
5. Plant wearable VOC-sensing roadmap
6. Conclusion and recommendation

**Notable traits:** Smallest reference list by far (~59) — reflecting a narrower, single-database (Scopus-only) search on a more specialized sub-topic. Heaviest use of first-person "we" in the sample. Only paper with an explicit numbered "key contributions of this study" list. No standalone Methods section — the (single-database, PRISMA-screened) search is described within the Introduction. The other open-access paper in the sample (CC BY-NC). Fewest tables (2) of any paper.

### P8 — Modelling the shapes of agricultural materials in DEM: methods, advances, and challenges

**Heading outline:**
1. Introduction
2. Literature analysis methodology
3. Shape modelling approaches in DEM (3.1-3.3)
4. Shape measurement and characterisation methods (4.1-4.3)
5. Shape modelling of agricultural materials in DEM (5.1-5.4, with deep sub-subsections down to 5.4.2.3)
6. Practical considerations for shape model selection (6.1 Case study)
7. Challenges and outlook (7.1-7.4)
8. Conclusions

**Notable traits:** Largest reference list in the sample (~286) and most figures (15). The only paper with a genuine, dedicated Nomenclature/Abbreviations section as its own heading. Self-labels explicitly as a "systematic literature review (SLR)" and contrasts this with "traditional narrative reviews," yet — unlike P2, P4, or P6 — never cites PRISMA or PRISMA-ScR by name and has no dedicated flow-diagram figure, relying instead on a prose description of a three-stage screening process. Pushes a comparison of prior DEM reviews (Table A.1) and a DEM-software list (Table A.2) into an appendix.

---

*Data file: `review_features.csv` (67 columns × 8 rows) contains the complete raw per-paper feature matrix underlying this report.*
