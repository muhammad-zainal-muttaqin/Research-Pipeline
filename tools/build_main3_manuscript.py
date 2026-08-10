#!/usr/bin/env python3
"""Build the third manuscript revision from the targeted evidence ledger.

The script keeps the existing main2 prose as a source-preserving base, updates
the search-pool accounting, replaces the appendix with one row per included
ledger study, and creates a bibliography containing every cited ledger study.
Generated files are derived artifacts and can be rebuilt from the ledger.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "source"
LEDGER = ROOT / "literature" / "search" / "derived" / "fulltext-review-ledger-2026-08-10.csv"
BASE_BODY = SOURCE / "main2-body.tex"
BASE_BIB = SOURCE / "references.bib"
BODY3 = SOURCE / "main3-body.tex"
MAIN3 = SOURCE / "main3.tex"
ELSE3 = SOURCE / "main-elsarticle3.tex"
BIB3 = SOURCE / "references3.bib"
MATRIX_CSV = ROOT / "audit" / "evidence-matrix-v2.csv"
MATRIX_MD = ROOT / "audit" / "evidence-matrix-v2.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def normalize_doi(value: str) -> str:
    text = clean(value).lower()
    text = re.sub(r"^https?://doi.org/", "", text)
    return text.rstrip(".")


def latex_escape(value: object) -> str:
    text = clean(value)
    text = text.replace("\u2013", "-")
    text = text.replace("\\", r"\textbackslash{}")
    replacements = [
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
        ("_", r"\_\allowbreak{}"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def bib_escape(value: object) -> str:
    text = clean(value)
    text = text.replace("\u2013", "-")
    text = text.replace("\\", "")
    for old, new in [
        ("&", r"\&"),
        ("%", r"\%"),
        ("#", r"\#"),
        ("_", r"\_"),
    ]:
        text = text.replace(old, new)
    return text


def existing_bib_maps(text: str) -> tuple[dict[str, str], dict[str, str]]:
    doi_to_key: dict[str, str] = {}
    title_to_key: dict[str, str] = {}
    for block in re.split(r"(?=^@)", text, flags=re.M):
        key_match = re.search(r"^@\w+\{([^,]+),", block, flags=re.M)
        if not key_match:
            continue
        key = key_match.group(1).strip()
        doi_match = re.search(r"\bdoi\s*=\s*\{([^}]+)\}", block, flags=re.I)
        title_match = re.search(r"\btitle\s*=\s*\{([^}]+)\}", block, flags=re.I)
        if doi_match:
            doi_to_key[normalize_doi(doi_match.group(1))] = key
        if title_match:
            title = re.sub(r"[^a-z0-9]+", "", title_match.group(1).lower())
            if title:
                title_to_key[title] = key
    return doi_to_key, title_to_key


def generated_key(row: dict[str, str], doi_to_key: dict[str, str], title_to_key: dict[str, str]) -> str:
    doi = normalize_doi(row.get("doi", ""))
    if doi and doi in doi_to_key:
        return doi_to_key[doi]
    title = re.sub(r"[^a-z0-9]+", "", clean(row.get("title", "")).lower())
    if title and title in title_to_key:
        return title_to_key[title]
    record_id = re.sub(r"[^a-zA-Z0-9]+", "_", clean(row.get("record_id", ""))).strip("_").lower()
    return f"ledger_{record_id or 'study'}"


def bib_entry(row: dict[str, str], key: str) -> str:
    document_type = clean(row.get("document_type", "")).lower()
    if "conference" in document_type or "proceedings" in clean(row.get("venue", "")).lower():
        entry_type = "inproceedings"
        venue_field = "booktitle"
    elif "preprint" in document_type or "arxiv" in clean(row.get("venue", "")).lower():
        entry_type = "misc"
        venue_field = "howpublished"
    else:
        entry_type = "article"
        venue_field = "journal"

    authors = clean(row.get("authors", "")).replace(";", " and ")
    authors = re.sub(r"\s*\(\d{6,}\)", "", authors)
    if not authors:
        authors = "Author metadata unavailable in ledger"
    lines = [
        f"@{entry_type}{{{key},",
        f"  author = {{{bib_escape(authors)}}},",
        f"  title = {{{bib_escape(row.get('title', ''))}}},",
        f"  year = {{{bib_escape(row.get('year', ''))}}},",
        f"  {venue_field} = {{{bib_escape(row.get('venue', ''))}}},",
    ]
    doi = normalize_doi(row.get("doi", ""))
    if doi:
        lines.append(f"  doi = {{{bib_escape(doi)}}},")
    lines.append("}")
    return "\n".join(lines)


def build_bibliography(rows: list[dict[str, str]]) -> dict[str, str]:
    base = BASE_BIB.read_text(encoding="utf-8")
    doi_to_key, title_to_key = existing_bib_maps(base)
    key_by_id: dict[str, str] = {}
    additions: list[str] = []
    existing_keys = set(re.findall(r"^@\w+\{([^,]+),", base, flags=re.M))
    for row in rows:
        key = generated_key(row, doi_to_key, title_to_key)
        key_by_id[row["record_id"]] = key
        if key in existing_keys:
            continue
        additions.append(bib_entry(row, key))
        existing_keys.add(key)
    combined = base.rstrip() + "\n\n" + "\n\n".join(additions) + "\n"
    BIB3.write_text(combined, encoding="utf-8")
    return key_by_id


def first_author(row: dict[str, str]) -> str:
    value = clean(row.get("authors", ""))
    value = value.split(";")[0].strip()
    value = re.sub(r"\s*\([^)]*\)\s*$", "", value)
    return value or "Study"


def observation_regime(row: dict[str, str]) -> str:
    text = " ".join(row.get(key, "") for key in ("title", "modality", "task_scope", "identity_mechanism")).lower()
    if any(token in text for token in ("uav", "drone", "aerial")):
        return "aerial"
    if "multi-camera" in text or "multi_camera" in text or "stereo" in text:
        return "multi-camera-rig"
    if any(token in text for token in ("video", "temporal", "tracking", "sequence")):
        return "video-continuous"
    if any(token in text for token in ("multi-view", "multi_view", "multiview", "unordered", "multiple view")):
        return "multi-view-discrete"
    return "single-view"


def identity_codes(value: str) -> list[str]:
    return [code for code in ("M0", "M1", "M2", "M3", "M4", "M5") if code in clean(value)]


def class_family(value: str) -> str:
    text = clean(value).lower()
    if any(token in text for token in ("maturity", "ripeness", "ripe", "unripe")):
        return "maturity"
    if any(token in text for token in ("size", "volume", "diameter", "height")):
        return "size"
    if any(token in text for token in ("quality", "defect", "disease")):
        return "quality-defect"
    if any(token in text for token in ("cultivar", "variety")):
        return "cultivar"
    return "none"


def evidence_status(row: dict[str, str]) -> str:
    kind = clean(row.get("evidence_type", "")).lower()
    if "transfer_mechanism" in kind or kind == "transfer":
        return "transferable"
    return "direct"


def unique_ground_truth(row: dict[str, str]) -> str:
    text = " ".join(row.get(key, "") for key in ("evaluation", "task_scope", "identity_mechanism", "key_finding")).lower()
    limitations = clean(row.get("limitations", "")).lower()
    positive = (
        "unique" in text
        or "identity-linked" in text
        or "duplicate-aware" in text
        or "cross-view" in text
        or "per-tree total" in text
        or ("manual" in text and "ground truth" in text and "count" in text)
    )
    negative = any(token in limitations for token in ("no persistent", "no cross-view", "no global fruit re-identification", "no unique inventory"))
    return "y" if positive and not negative else "n"


def dedup_status(row: dict[str, str]) -> str:
    kind = clean(row.get("evidence_type", "")).lower()
    if "review" in kind or "transfer_mechanism" in kind:
        return "n-a"
    codes = identity_codes(row.get("identity_mechanism", ""))
    text = " ".join(row.get(key, "") for key in ("task_scope", "identity_mechanism", "key_finding")).lower()
    limitations = clean(row.get("limitations", "")).lower()
    if any(token in limitations for token in ("no persistent", "not evaluated", "no cross-view", "no unique inventory", "not assess", "without cross-view")):
        return "no"
    if codes == ["M0"] or not codes:
        return "no"
    if any(token in text for token in ("duplicate", "dedup", "re-ident", "association", "unique")):
        return "explicit"
    return "implicit"


def assumptions(row: dict[str, str]) -> str:
    text = clean(row.get("identity_mechanism", ""))
    codes = identity_codes(text)
    values: list[str] = []
    mapping = {"M1": "A6", "M2": "A5", "M3": "A3", "M4": "A2,A4", "M5": "A7", "M0": "A1"}
    for code in codes:
        for value in mapping.get(code, "").split(","):
            if value and value not in values:
                values.append(value)
    return ",".join(values)


def violated_conditions(row: dict[str, str]) -> str:
    text = clean(row.get("limitations", "")).lower()
    values: list[str] = []
    rules = [
        (("occlusion", "leaf overlap", "hidden"), "P1"),
        (("illumination", "lighting", "shadow", "sunlight", "depth error"), "P2"),
        (("drift", "motion", "camera stability", "track fragmentation"), "P3"),
        (("calibration", "registration", "metric scale", "sfm cost"), "P4"),
        (("single orchard", "one orchard", "one greenhouse", "transfer", "generalizability", "generalization"), "P5"),
    ]
    for tokens, code in rules:
        if any(token in text for token in tokens):
            values.append(code)
    return ",".join(values)


def build_matrix(rows: list[dict[str, str]], key_by_id: dict[str, str]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for row in sorted(rows, key=lambda item: int(clean(item.get("review_order", "999999")) or "999999")):
        output.append({
            "study_id": row.get("record_id", ""),
            "bibtex_key": key_by_id[row["record_id"]],
            "authors": row.get("authors", ""),
            "authors_year": f"{clean(row.get('authors', ''))} ({clean(row.get('year', ''))})",
            "title": row.get("title", ""),
            "doi": row.get("doi", ""),
            "venue": row.get("venue", ""),
            "crop_or_domain": crop_domain(row),
            "observation_regime": observation_regime(row),
            "modality": row.get("modality", ""),
            "identity_mechanism": "/".join(identity_codes(row.get("identity_mechanism", ""))) or "M0",
            "class_attribute_family": class_family(row.get("class_attribute", "")),
            "evaluation_context": row.get("evaluation", ""),
            "unique_instance_gt": unique_ground_truth(row),
            "metrics_reported": row.get("evaluation", ""),
            "dedup_handled": dedup_status(row),
            "evidence_status": evidence_status(row),
            "assumptions_required": assumptions(row),
            "violated_conditions": violated_conditions(row),
            "evidence_pages": row.get("evidence_pages", ""),
            "key_finding": row.get("key_finding", ""),
            "limitations": row.get("limitations", ""),
            "retrieval_source": row.get("retrieval_source", ""),
            "fulltext_path": row.get("fulltext_path", ""),
            "review_order": row.get("review_order", ""),
        })
    return output


def crop_domain(row: dict[str, str]) -> str:
    text = " ".join(row.get(key, "") for key in ("title", "task_scope", "evidence_type")).lower()
    if "oil palm" in text or "ffb" in text:
        return "oil palm FFB"
    for name in ("apple", "mango", "citrus", "grape", "tomato", "orange", "strawberry", "blueberry", "pear", "pineapple"):
        if name in text:
            return name
    if "vehicle" in text or "pedestrian" in text or "person" in text:
        return "non-agricultural transfer domain"
    return "agricultural fruit or transferable mechanism"


def build_matrix_markdown(matrix: list[dict[str, str]]) -> str:
    counts = Counter(row["evidence_status"] for row in matrix)
    lines = [
        "# Targeted evidence matrix",
        "",
        f"The matrix contains {len(matrix)} included studies from the targeted full-text ledger.",
        "",
        "| Evidence status | Studies |",
        "|---|---:|",
    ]
    lines.extend(f"| {label} | {counts[label]} |" for label in sorted(counts))
    lines.extend([
        "",
        "`assumptions_required` and `violated_conditions` are reviewer inferences required by the protocol; they are not claimed as verbatim statements by every source.",
        "",
        "The machine-readable row-level file is `audit/evidence-matrix-v2.csv`. Each row retains the ledger record ID, DOI, retrieval source, local full-text path when available, evidence pages, finding, and limitations.",
    ])
    return "\n".join(lines) + "\n"


def build_matrix_latex(matrix: list[dict[str, str]], key_by_id: dict[str, str]) -> str:
    lines = [
        "\\section{Focused evidence matrix}",
        "\\label{app:matrix3}",
        "",
        "The matrix contains one row per study included after targeted full-text review. Direct evidence covers agriculture and fruit systems; transferable evidence answers an identity or geometry mechanism question outside agriculture. The assumptions and violated-condition codes are reviewer inferences, not verbatim claims from every source. The machine-readable version is available at \\path{audit/evidence-matrix-v2.csv}.",
        "",
        "\\small",
        "\\setlength{\\LTleft}{0pt}",
        "\\setlength{\\LTright}{0pt}",
        "\\setlength{\\tabcolsep}{2pt}",
        "\\makeatletter",
        "\\@ifclassloaded{IEEEtran}{\\onecolumn}{ }",
        "\\makeatother",
        "\\begin{longtable}{@{}>{\\raggedright\\arraybackslash}p{0.14\\textwidth}>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\raggedright\\arraybackslash}p{0.18\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.25\\textwidth}>{\\raggedright\\arraybackslash}p{0.07\\textwidth}@{}}",
        "\\caption{Targeted row-level evidence matrix. Pages refer to the verified full text recorded in the ledger.}\\label{tab:matrix3}\\\\",
        "\\toprule",
        "Study & Method and modality & Evaluation and pages & Identity and attribute & Finding and limitation & Status\\\\",
        "\\midrule",
        "\\endfirsthead",
        "\\multicolumn{6}{c}{\\tablename\\ \\thetable{} continued}\\\\",
        "\\toprule",
        "Study & Method and modality & Evaluation and pages & Identity and attribute & Finding and limitation & Status\\\\",
        "\\midrule",
        "\\endhead",
        "\\midrule",
        "\\multicolumn{6}{r}{Continued on next page}\\\\",
        "\\endfoot",
        "\\bottomrule",
        "\\endlastfoot",
    ]
    for row in matrix:
        key = key_by_id[row["study_id"]]
        study = f"{latex_escape(first_author(row))} ({latex_escape(row['authors_year'].rsplit('(', 1)[-1].rstrip(')'))}) \\cite{{{key}}}"
        method = f"{row['modality']}; {row['crop_or_domain']}"
        evaluation = f"{row['evaluation_context']} Pages {row['evidence_pages']}."
        identity = f"{row['identity_mechanism']}; {row['class_attribute_family']}; GT {row['unique_instance_gt']}; dedup {row['dedup_handled']}"
        finding = f"{row['key_finding']} Limit: {row['limitations']}"
        status = row["evidence_status"]
        lines.append(" & ".join([
            study,
            latex_escape(method),
            latex_escape(evaluation),
            latex_escape(identity),
            latex_escape(finding),
            latex_escape(status),
        ]) + r"\\")
    lines.append("\\end{longtable}")
    lines.extend([
        "\\makeatletter",
        "\\@ifclassloaded{IEEEtran}{\\twocolumn}{ }",
        "\\makeatother",
    ])
    lines.append("")
    return "\n".join(lines)


def update_body(rows: list[dict[str, str]], key_by_id: dict[str, str]) -> str:
    body = BASE_BODY.read_text(encoding="utf-8")
    body = body.replace("\u2013", "-")
    body = body.replace("matrix2", "matrix3")

    trace_start = body.index("High-confidence title screening removed")
    trace_end = body.index("\n\n\\begin{figure}[t]", trace_start)
    trace = (
        "High-confidence title screening removed 242 EC5 records and one EC6 record, leaving 20,823 records for abstract screening. Abstract screening removed 640 EC1 records and 148 EC5 records, leaving 20,035 search-pool candidates. The 20,035 records were not treated as a requirement to read 20,035 papers one by one. A deterministic title-abstract score ranked core identity and inventory signals, fruit and oil-palm targets, instance perception, geometry, tracking, and prior reviews, while penalizing global-only outputs and non-target domains. A diversified shortlist of 250 records was selected, with a first targeted wave of 60. By the manuscript cutoff, 44 records had complete full-text evidence in the ledger and 16 had been excluded after review."
    )
    body = body[:trace_start] + trace + body[trace_end:]

    figure = r"""\begin{figure}[t]
\centering
\small
\begin{tabular}{c}
\fbox{\parbox{0.78\columnwidth}{\centering 32,378 raw records\\Scopus 15,722 + OpenAlex 16,656}}\\[2pt]
$\downarrow$\\[-1pt]
\fbox{\parbox{0.78\columnwidth}{\centering 22,269 exact-key master records}}\\[2pt]
$\downarrow$\\[-1pt]
\fbox{\parbox{0.78\columnwidth}{\centering 21,066 resolved working-master records}}\\[2pt]
$\downarrow$\\[-1pt]
\fbox{\parbox{0.78\columnwidth}{\centering 20,035 abstract-advanced search-pool records}}\\[2pt]
$\downarrow$\\[-1pt]
\fbox{\parbox{0.78\columnwidth}{\centering 250 targeted shortlist; 60 first wave; 44 included evidence studies}}
\end{tabular}
\caption{Search, prioritization, and targeted full-text trace. The 20,035 record pool is ranked and filtered before full-text review; it is not a promise of 20,035 individual paper reviews.}
\label{fig:flow3}
\end{figure}"""
    body = re.sub(r"\\begin\{figure\}\[t\].*?\\end\{figure\}", lambda _: figure, body, count=1, flags=re.S)

    priority = r"""\subsection{Prioritization before full-text review}

After abstract screening, the 20,035 records were treated as a search pool rather than as a mandatory reading list. The ranking script \path{tools/build\_literature\_priority\_shortlist.py} scored reproducible title and abstract signals. Positive signals covered unique inventory, duplicate resolution, re-identification, cross-view association, tracking, SfM or MVS, point clouds, RGB-D, depth, 3D reconstruction, fruit, FFB, and oil palm. Penalties reduced the priority of global yield or biomass outputs, canopy-only remote sensing, non-fruit targets, and image-level outputs. The score did not decide inclusion.

To prevent one model family from dominating, selection used buckets for core identity or inventory, direct oil palm evidence, fruit multiview or 3D evidence, fruit-instance baselines, transfer mechanisms, and prior reviews or positioning. The resulting 250-record shortlist and 60-record first wave are machine-readable in \path{literature/search/derived/priority-shortlist-2026-08-10.csv} and \path{literature/search/derived/priority-review-wave1-2026-08-10.csv}. This design makes the next review step reproducible without pretending that ambiguous candidates have already been included or excluded."""
    body = body.replace("\\subsection{Two evidence registers}", priority + "\n\n\\subsection{Two evidence registers}", 1)

    body = re.sub(
        r"The manuscript keeps two registers separate\..*?automated abstract triage from being described as a completed full-text decision\.",
        "The manuscript keeps two registers separate. Register A is the new Scopus and OpenAlex search, including all candidate and screening states. Register B is the targeted evidence register: studies whose full text was retrieved and whose dataset, protocol, quantitative evaluation, and mechanism fields were verified in the ledger. The ranking and shortlist are selection aids inside Register A; they are not inclusion decisions. This separation prevents the 20,035 search pool from being presented as 20,035 included studies.",
        body,
        count=1,
        flags=re.S,
    )

    target_rows = {row["record_id"]: row for row in rows}
    additions = []
    direct_text = {
        "M-1210e3ea00486b68": "Semantic NeRF converts unordered posed RGB observations into a 3D fruit field and clustered fruit point cloud, providing a geometric route to consolidate repeated observations before counting",
        "R-b2e0e9aabad17a97": "The tomato RGB-D SLAM study projects fruit masks into a filtered semantic point cloud and fits spheres to estimate fruit counts and volume at plant and row levels",
        "R-d4270ea8ab11f268": "A pear study fuses RGB detections, LiDAR, FAST-LIO2 SLAM, and temporal association for 3D fruit counting; field validation reports 96.2 percent counting accuracy while retaining 53 double-counts linked to association threshold and SLAM drift",
    }
    for record_id, sentence in direct_text.items():
        if record_id in target_rows:
            additions.append(f"{sentence} \\cite{{{key_by_id[record_id]}}}.")
    new_direct = "\n\n".join(additions)
    sawit_anchor = "This makes a tree-level unique-count metric possible. It also exposes the central confounder: the number of visible bounding boxes is not the number of unique bunches."
    if new_direct:
        body = body.replace(sawit_anchor, sawit_anchor + "\n\n" + new_direct, 1)

    body = body.replace(
        "Appendix~\\ref{app:matrix3} contains one row per focused study or review used to define the design space. The table includes direct agricultural evidence, fruit evidence, transferable mechanism evidence, and positioning reviews. A status field distinguishes a source with verified local full text from a source represented at the accessible article-record or abstract level. This distinction is part of the evidence, not an editorial footnote.",
        "Appendix~\\ref{app:matrix3} contains one row per the 44 studies included after targeted full-text review. The table records method, modality, evaluation context, evidence pages, identity mechanism, class attribute, unique-instance ground truth status, duplicate handling, finding, and limitations. The machine-readable matrix is \\path{audit/evidence-matrix-v2.csv}; the assumptions and violated-condition codes are explicitly marked as reviewer inferences.",
    )

    body = body.replace(
        "The search is reproducible from the captured raw exports and scripts, but the full-text stage is incomplete at the current cutoff. Scopus was available and Web of Science was not, so database coverage is not equivalent to a two-subscription search. OpenAlex metadata and abstracts are useful for discovery but do not replace article full text. The local audit found only six matches between the new master and the verified local PDF corpus. Consequently, the 20,035 full-text candidates are reported as a retrieval boundary, not as included studies.",
        "The search is reproducible from the captured raw exports and scripts, but the full-text stage is intentionally targeted rather than exhaustive. Scopus was available and Web of Science was not, so database coverage is not equivalent to a two-subscription search. OpenAlex metadata and abstracts are useful for discovery but do not replace article full text. The local audit found six matches in the legacy PDF corpus; targeted retrieval then produced 44 complete evidence records. Consequently, the 20,035 records remain a ranked search pool, not an included-study count.",
    )

    body = body.replace(
        "The target of agricultural multi-view perception is a unique, class-wise inventory, not a sum of independent detections. The revised protocol makes the search reproducible and exposes an important evidence boundary: a large candidate master has been screened automatically, but most candidate full texts are not yet locally available. The direct evidence includes oil-palm detector studies, multi-angle and RGB-depth datasets, fruit SfM, and orchard load estimation. Together they support a six-mechanism design space spanning intra-view counting, statistical correction, appearance, temporal tracking, geometry, and learned association.",
        "The target of agricultural multi-view perception is a unique, class-wise inventory, not a sum of independent detections. The revised protocol makes the search reproducible and makes the selection boundary explicit: 20,035 candidates were ranked, 250 were shortlisted, and 44 targeted full-text studies supplied the current evidence matrix. The direct evidence includes oil-palm detector and dataset studies, multi-angle and RGB-depth systems, fruit SfM, NeRF, LiDAR-camera fusion, and orchard counting. Together they support a six-mechanism design space spanning intra-view counting, statistical correction, appearance, temporal tracking, geometry, and learned association.",
    )

    matrix_start = body.index("\\section{Focused evidence matrix}")
    matrix_end = body.index("\\section{Exact search strings}", matrix_start)
    matrix = build_matrix_latex(build_matrix(rows, key_by_id), key_by_id)
    body = body[:matrix_start] + matrix + "\n\n" + body[matrix_end:]
    return body


def build_documents(body: str) -> None:
    BODY3.write_text(body, encoding="utf-8")
    ieee = r"""\documentclass[journal]{IEEEtran}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{array}
\usepackage{longtable}
\usepackage{tabularx}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{url}
\graphicspath{{../figures/}}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\begin{document}
\title{Multi-View and Multimodal Perception for Class-Wise Fruit Inventories: A Design-Space Review}
\author{Muhammad~Zainal~Muttaqin and Fatma~Indriani\thanks{Department of Computer Science, Universitas Lambung Mangkurat, Banjarbaru, Indonesia.}\thanks{Search, prioritization, and evidence-ledger audit executed 10 August 2026.}}
\maketitle
\begin{abstract}
Turning repeated observations of one tree into a single inventory of unique fruits grouped by class requires more than per-image detection. This design-space review treats oil-palm fresh fruit bunches as the principal agricultural case and transfers identity mechanisms from fruit, orchard, and non-agricultural multi-view perception. Scopus and OpenAlex searches used seven reproducible query families, explicit years, inclusion and exclusion rules, DOI or title-year deduplication, and title-abstract triage. The search produced 21,066 resolved master records; 20,035 advanced after abstract screening. These records were ranked by deterministic title-abstract signals and diversified into a 250-record shortlist with a 60-record first wave, rather than being read one by one. At the reporting cutoff, 44 targeted full-text studies supplied complete evidence rows. The synthesis distinguishes intra-view detection, statistical correction, appearance matching, temporal tracking, geometric association, and learned multi-view association. It generalizes class attributes beyond maturity to size, quality, disease, cultivar, and harvest readiness, while retaining the requirement that attributes attach to persistent instances. The resulting contribution is a testable design space for duplicate-aware, class-wise fruit inventories and an explicit boundary between search candidates and verified evidence.
\end{abstract}
\begin{IEEEkeywords}
multi-view perception, multimodal fusion, fruit counting, instance identity, oil palm, design-space review
\end{IEEEkeywords}
\input{main3-body}
\bibliographystyle{IEEEtran}
\bibliography{references3}
\end{document}
"""
    els = r"""\documentclass[review]{elsarticle}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{array}
\usepackage{longtable}
\usepackage{tabularx}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{url}
\graphicspath{{../figures/}}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\journal{Computers and Electronics in Agriculture}
\begin{document}
\begin{frontmatter}
\title{Multi-View and Multimodal Perception for Class-Wise Fruit Inventories: A Design-Space Review}
\author[a]{Muhammad Zainal Muttaqin\corref{cor1}}
\ead{mz.muttaqin1@gmail.com}
\author[a]{Fatma Indriani}
\affiliation[a]{organization={Department of Computer Science, Universitas Lambung Mangkurat},city={Banjarbaru},country={Indonesia}}
\cortext[cor1]{Corresponding author}
\begin{abstract}
Turning repeated observations of one tree into a single inventory of unique fruits grouped by class requires more than per-image detection. This design-space review treats oil-palm fresh fruit bunches as the principal agricultural case and transfers identity mechanisms from fruit, orchard, and non-agricultural multi-view perception. Scopus and OpenAlex searches used seven reproducible query families, explicit years, inclusion and exclusion rules, DOI or title-year deduplication, and title-abstract triage. The search produced 21,066 resolved master records; 20,035 advanced after abstract screening. These records were ranked by deterministic title-abstract signals and diversified into a 250-record shortlist with a 60-record first wave, rather than being read one by one. At the reporting cutoff, 44 targeted full-text studies supplied complete evidence rows. The synthesis distinguishes intra-view detection, statistical correction, appearance matching, temporal tracking, geometric association, and learned multi-view association. It generalizes class attributes beyond maturity to size, quality, disease, cultivar, and harvest readiness, while retaining the requirement that attributes attach to persistent instances. The resulting contribution is a testable design space for duplicate-aware, class-wise fruit inventories and an explicit boundary between search candidates and verified evidence.
\end{abstract}
\begin{keyword}
multi-view perception \sep multimodal fusion \sep fruit counting \sep instance identity \sep oil palm \sep design-space review
\end{keyword}
\end{frontmatter}
\input{main3-body}
\bibliographystyle{elsarticle-num}
\bibliography{references3}
\end{document}
"""
    MAIN3.write_text(ieee, encoding="utf-8")
    ELSE3.write_text(els, encoding="utf-8")


def main() -> None:
    included = [row for row in read_csv(LEDGER) if clean(row.get("decision")) == "include"]
    key_by_id = build_bibliography(included)
    matrix = build_matrix(included, key_by_id)
    matrix_fields = list(matrix[0])
    write_csv(MATRIX_CSV, matrix, matrix_fields)
    MATRIX_MD.write_text(build_matrix_markdown(matrix), encoding="utf-8")
    body = update_body(included, key_by_id)
    build_documents(body)
    print(f"included={len(included)}")
    print(f"matrix={MATRIX_CSV}")
    print(f"bibliography={BIB3}")
    print(f"body={BODY3}")
    print(f"ieee={MAIN3}")
    print(f"elsarticle={ELSE3}")


if __name__ == "__main__":
    main()
