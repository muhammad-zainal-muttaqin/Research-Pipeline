#!/usr/bin/env python3
"""Run a conservative abstract-screening pass after title triage.

Only high-confidence EC1, EC5, and EC6 signals are excluded. Records with a
missing or ambiguous abstract are retained for full-text review.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Iterable


ABSTRACT_FIELDS = [
    "record_id",
    "doi",
    "title",
    "year",
    "source_databases",
    "query_ids",
    "abstract_available",
    "abstract_screen_decision",
    "abstract_screen_exclusion_code",
    "abstract_screen_confidence",
    "abstract_screen_basis",
    "mechanism_evidence",
    "global_output_evidence",
    "full_text_status",
]

SUMMARY_FIELDS = [
    "date_run",
    "source_date",
    "n_master",
    "n_title_abstract_candidates",
    "n_abstracts_available",
    "n_abstracts_missing",
    "n_exclude_EC1",
    "n_exclude_EC5",
    "n_exclude_EC6",
    "n_advance_fulltext",
    "n_advance_with_strong_mechanism_signal",
    "n_advance_abstract_uncertain",
    "rule_version",
]


# These patterns describe document metadata, not ordinary research prose.
TITLE_METADATA_PATTERNS = [
    (re.compile(r"^author\s+response\b", re.I), "author response"),
    (re.compile(r"^reviewer\s+response\b", re.I), "reviewer response"),
    (re.compile(r"^reviewer\s*#?\s*\d+\b", re.I), "public reviewer report"),
    (re.compile(r"^public\s+review\b", re.I), "public reviewer report"),
    (re.compile(r"^elife\s+assessment\b", re.I), "journal assessment"),
    (re.compile(r"^response\s+to\s+(?:the\s+)?reviewers?\b", re.I), "response to reviewers"),
    (re.compile(r"^decision\s+letter\b", re.I), "decision letter"),
    (re.compile(r"^cover\s+(?:image|picture)\b", re.I), "cover image or picture"),
    (
        re.compile(
            r"\b(?:123movies|putlockers|worldmovieshd|freemovies|filmzilla|"
            r"goodreads|filmywap)\b|\bfull\s+movie\s+(?:online|free|download)\b|"
            r"\bwatch\s+.+?\bfull\s+movie\b",
            re.I,
        ),
        "non-research movie or spam record",
    ),
]

ABSTRACT_METADATA_PATTERNS = [
    (
        re.compile(
            r"^\s*(?:this\s+(?:special\s+)?issue(?:['’]s)?\s+cover\s+image|"
            r"cover\s+image\s*:|cover\s+picture\s+and\s+issue\s+information)\b",
            re.I,
        ),
        "cover or issue information",
    ),
    (
        re.compile(r"^\s*(?:table\s+of\s+contents|contents\s+of\s+this\s+issue)\b", re.I),
        "table of contents",
    ),
    (
        re.compile(
            r"^.{0,180}volume[-\s]?\d+\s+issue[-\s]?\d+\b"
            r".{0,220}volume[-\s]?\d+\s+issue[-\s]?\d+\b",
            re.I,
        ),
        "repeated issue listing",
    ),
    (
        re.compile(
            r"^\s*(?:erratum|corrigendum|retraction(?:\s+notice)?|"
            r"correction\s+notice)\b",
            re.I,
        ),
        "publication correction or retraction notice",
    ),
    (
        re.compile(
            r"^\s*(?:\[[^\]]*\]\s*)?(?:putlockers|freemovies|worldmovieshd)\b",
            re.I,
        ),
        "non-research spam artifact",
    ),
    (
        re.compile(
            r"\b(?:123movies|putlockers|worldmovieshd|freemovies|filmzilla|"
            r"goodreads|filmywap)\b|\bfull\s+movie\s+(?:online|free|download)\b|"
            r"\bhow\s+to\s+watch\s+.+?\bfull\s+movie\b",
            re.I,
        ),
        "non-research movie or spam artifact",
    ),
]


# Strong signals for a per-instance or cross-observation visual mechanism.
# Generic words such as image, detection, remote sensing, or classification are
# intentionally not sufficient on their own.
MECHANISM_PATTERNS = [
    (
        re.compile(
            r"\b(?:instance[-\s]?(?:detection|segmentation|recognition|level)|"
            r"object\s+(?:detection|tracking|recognition|locali[sz]ation)|"
            r"multi[-\s]?object\s+tracking)\b",
            re.I,
        ),
        "object or instance perception",
    ),
    (
        re.compile(
            r"\b(?:fruit|fruitlet|berry|pod|bunch|boll|flower|bud|shoot|"
            r"plant|tree|leaf|stem|canopy|crown|spikelet|silique|seed|"
            r"apple|mango|tomato|citrus|grape|strawberr(?:y|ies)|litchi|"
            r"kiwi|pepper|cucumber|maize|corn|wheat|soybean|cotton|rice|"
            r"object|target|animal|person|vehicle)s?"
            r"(?:\s+[a-z0-9-]+){0,3}\s+"
            r"(?:detection|detector|locali[sz]ation|segmentation|tracking|"
            r"counting|enumeration|recognition)\b",
            re.I,
        ),
        "target-specific detection, segmentation, tracking, or counting",
    ),
    (
        re.compile(
            r"\b(?:detect(?:ion|ing)?|locali[sz](?:e|ation|ing)|segment(?:ation|ing)?|"
            r"track(?:ing)?|count(?:ing)?|enumerat(?:e|ion|ing)|reconstruct(?:ion|ing)?)\s+"
            r"(?:of\s+)?(?:the\s+|a\s+|an\s+)?"
            r"(?:[a-z0-9-]+\s+){0,3}(?:individual\s+)?"
            r"(?:fruit|fruitlet|berry|pod|bunch|boll|flower|bud|shoot|plant|tree|"
            r"leaf|stem|canopy|crown|spikelet|silique|seed|apple|mango|tomato|"
            r"citrus|grape|strawberr(?:y|ies)|litchi|kiwi|pepper|cucumber|maize|"
            r"corn|wheat|soybean|cotton|rice|object|target|animal|person|vehicle)s?\b",
            re.I,
        ),
        "operation on a named target",
    ),
    (
        re.compile(
            r"(?:\b(?:detect\w*|segment\w*|track\w*|count\w*|locali[sz]\w*|"
            r"reconstruct\w*|correspond\w*)\b.{0,100}\b(?:fruit|fruitlet|berry|"
            r"berries|pod|pods|bunch|bunches|cluster|clusters|crown|crowns|"
            r"inflorescence|inflorescences|spikelet|spikelets|seedpod|seedpods|"
            r"lesion|lesions|spot|spots|weed|weeds|disease|diseases|pest|pests|"
            r"plant|tree|leaf|stem|branch|crop|cabbage|"
            r"object|target|apple|pear|peach|"
            r"plum|cherry|banana|pineapple|watermelon|longan|guava|pomegranate|"
            r"blueberr(?:y|ies)|cranberr(?:y|ies)|oil\s+palm|fresh\s+fruit\s+"
            r"bunch|ffb|[a-z0-9-]+(?:fruit|berry|berries|bunch|pod|cluster|"
            r"crown|inflorescence|spikelet|seedpod))\b|\b(?:fruit|fruitlet|berry|berries|pod|pods|bunch|"
            r"cluster|crown|inflorescence|spikelet|seedpod|lesion|lesions|spot|spots|"
            r"weed|weeds|disease|diseases|pest|pests|"
            r"plant|tree|leaf|stem|branch|crop|cabbage|object|target|apple|pear|peach|plum|cherry|banana|"
            r"pineapple|watermelon|longan|guava|pomegranate|blueberr(?:y|ies)|"
            r"cranberr(?:y|ies)|oil\s+palm|fresh\s+fruit\s+bunch|ffb|"
            r"[a-z0-9-]+(?:fruit|berry|berries|bunch|pod|cluster|crown|"
            r"inflorescence|spikelet|seedpod))\b.{0,100}"
            r"\b(?:detect\w*|segment\w*|track\w*|count\w*|locali[sz]\w*|"
            r"reconstruct\w*|correspond\w*)\b)",
            re.I,
        ),
        "broad visual target-operation evidence",
    ),
    (
        re.compile(
            r"\b(?:individual|each|per[-\s]?instance|instance[-\s]?level|"
            r"instance[-\s]?aware)\s+"
            r"(?:fruit|fruitlet|berry|pod|bunch|flower|bud|shoot|plant|tree|leaf|"
            r"stem|crown|spikelet|silique|seed|object|target)s?\b",
            re.I,
        ),
        "individual-target evidence",
    ),
    (
        re.compile(
            r"\b(?:multi[-\s]?view|cross[-\s]?view|multi[-\s]?camera|"
            r"re[-\s]?identification|reidentification|data\s+association|"
            r"feature\s+correspondence|structure\s+from\s+motion|"
            r"3d(?:\s+[a-z0-9-]+){0,3}\s+reconstruction|"
            r"three[-\s]?dimensional(?:\s+[a-z0-9-]+){0,3}\s+reconstruction|"
            r"point\s+cloud)\b",
            re.I,
        ),
        "cross-view, association, reconstruction, or point-cloud evidence",
    ),
]


# These patterns indicate a global output that is outside the per-instance
# target. They are used only when no strong mechanism signal is present.
GLOBAL_OUTPUT_PATTERNS = [
    (
        re.compile(
            r"\b(?:yield|production|productivity|biomass|harvest|crop\s+load|"
            r"fruit\s+load|soil\s+health|land\s+use|carbon\s+(?:stock|emission)s?)\b"
            r".{0,100}\b(?:predict\w*|forecast\w*|estim\w*|regress\w*|"
            r"assess\w*|quantif\w*|mapp?ing|mapp?ed)\b",
            re.I,
        ),
        "global production, yield, biomass, or land-use output",
    ),
    (
        re.compile(
            r"\b(?:predict\w*|forecast\w*|estim\w*|regress\w*|assess\w*|"
            r"quantif\w*|mapp?ing|mapp?ed)\b"
            r".{0,100}\b(?:yield|production|productivity|biomass|harvest|"
            r"crop\s+load|fruit\s+load|soil\s+health|land\s+use|"
            r"carbon\s+(?:stock|emission)s?)\b",
            re.I,
        ),
        "global production, yield, biomass, or land-use output",
    ),
    (
        re.compile(
            r"\b(?:total|global|field[-\s]?level|plot[-\s]?level|"
            r"canopy[-\s]?level|whole[-\s]?image)\b.{0,80}\b"
            r"(?:number|count|counting|classification|prediction|regression)\b",
            re.I,
        ),
        "explicit global or image-level output",
    ),
    (
        re.compile(
            r"\b(?:image[-\s]?level|whole[-\s]?image|scene|global)\s+"
            r"(?:classification|recognition|prediction|regression)\b",
            re.I,
        ),
        "explicit image-level classification or regression",
    ),
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def write_csv(path: Path, fieldnames: Iterable[str], rows: Iterable[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in writer.fieldnames})


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def normalize(value: object) -> str:
    text = html.unescape(clean(value))
    text = re.sub(r"<[^>]*>", " ", text)
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", text).strip()


def evidence_excerpt(text: str, match: re.Match[str] | None) -> str:
    if match is None:
        return ""
    start = max(0, match.start() - 90)
    end = min(len(text), match.end() + 150)
    return text[start:end].strip()


def first_match(
    patterns: list[tuple[re.Pattern[str], str]], text: str
) -> tuple[str, str] | None:
    for pattern, label in patterns:
        match = pattern.search(text)
        if match:
            return label, evidence_excerpt(text, match)
    return None


def abstract_available(row: dict[str, str], abstract: str) -> bool:
    flag = clean(row.get("abstract_available", "")).lower()
    if flag in {"false", "0", "no", "n", "missing", "unavailable"}:
        return False
    return bool(abstract)


def screen_row(row: dict[str, str]) -> dict[str, str]:
    title = normalize(row.get("title", ""))
    abstract = normalize(row.get("abstract", ""))
    combined = ". ".join(part for part in (title, abstract) if part)
    available = abstract_available(row, abstract)

    year = clean(row.get("year", ""))
    if year.isdigit() and not 2015 <= int(year) <= 2026:
        return {
            "abstract_screen_decision": "exclude_abstract",
            "abstract_screen_exclusion_code": "EC6",
            "abstract_screen_confidence": "high",
            "abstract_screen_basis": f"publication year {year} is outside 2015-2026",
            "mechanism_evidence": "",
            "global_output_evidence": "",
            "full_text_status": "not_needed",
        }

    title_metadata = first_match(TITLE_METADATA_PATTERNS, title)
    abstract_metadata = first_match(ABSTRACT_METADATA_PATTERNS, abstract)
    metadata = title_metadata or abstract_metadata
    if metadata:
        label, excerpt = metadata
        source = "title" if title_metadata else "abstract"
        return {
            "abstract_screen_decision": "exclude_abstract",
            "abstract_screen_exclusion_code": "EC5",
            "abstract_screen_confidence": "high",
            "abstract_screen_basis": f"{source} signal: {label}; evidence: {excerpt}",
            "mechanism_evidence": "",
            "global_output_evidence": "",
            "full_text_status": "not_needed",
        }

    if not available:
        return {
            "abstract_screen_decision": "advance_fulltext",
            "abstract_screen_exclusion_code": "",
            "abstract_screen_confidence": "not_assessed",
            "abstract_screen_basis": "abstract unavailable; do not exclude automatically",
            "mechanism_evidence": "",
            "global_output_evidence": "",
            "full_text_status": "pending",
        }

    mechanism = first_match(MECHANISM_PATTERNS, combined)
    global_output = first_match(GLOBAL_OUTPUT_PATTERNS, combined)
    if global_output and not mechanism:
        label, excerpt = global_output
        return {
            "abstract_screen_decision": "exclude_abstract",
            "abstract_screen_exclusion_code": "EC1",
            "abstract_screen_confidence": "high",
            "abstract_screen_basis": f"{label}; evidence: {excerpt}",
            "mechanism_evidence": "",
            "global_output_evidence": f"{label}: {excerpt}",
            "full_text_status": "not_needed",
        }

    mechanism_text = ""
    if mechanism:
        mechanism_text = f"{mechanism[0]}: {mechanism[1]}"
    global_text = ""
    if global_output:
        global_text = f"{global_output[0]}: {global_output[1]}"
    confidence = "medium" if mechanism else "low"
    basis = "no high-confidence EC1, EC5, or EC6 exclusion; full-text review required"
    if mechanism:
        basis = f"retain because of mechanism signal: {mechanism[0]}; full-text review required"
    return {
        "abstract_screen_decision": "advance_fulltext",
        "abstract_screen_exclusion_code": "",
        "abstract_screen_confidence": confidence,
        "abstract_screen_basis": basis,
        "mechanism_evidence": mechanism_text,
        "global_output_evidence": global_text,
        "full_text_status": "pending",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-date", default="2026-08-09")
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--force", action="store_true", help="replace abstract-screening outputs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    source_master = derived / f"master-screening-{args.source_date}.csv"
    pre_abstract_master = derived / f"master-screening-pre-abstract-{args.run_date}.csv"
    primary_master = derived / f"master-screening-{args.source_date}.csv"
    abstract_path = derived / f"abstract-screening-{args.run_date}.csv"
    summary_path = derived / f"abstract-screening-summary-{args.run_date}.csv"
    prisma_path = root / "literature" / "search" / "prisma-counts.csv"

    if not source_master.exists() or not prisma_path.exists():
        raise FileNotFoundError("Title-screened master and PRISMA files are required")
    if not pre_abstract_master.exists():
        shutil.copyfile(source_master, pre_abstract_master)
    if any(path.exists() for path in (abstract_path, summary_path)) and not args.force:
        raise FileExistsError("Abstract screening outputs already exist; use --force to rebuild")

    master_fields, source_rows = read_csv(pre_abstract_master)
    candidate_rows = [
        row for row in source_rows if row.get("title_screen_decision") == "advance_to_abstract"
    ]
    if not candidate_rows:
        raise ValueError("No title-abstract candidates found")

    abstract_rows: list[dict[str, str]] = []
    updated_master: list[dict[str, str]] = []
    for source_row in source_rows:
        updated = dict(source_row)
        if source_row.get("title_screen_decision") == "advance_to_abstract":
            decision = screen_row(source_row)
            abstract_rows.append(
                {
                    "record_id": source_row.get("record_id", ""),
                    "doi": source_row.get("doi", ""),
                    "title": source_row.get("title", ""),
                    "year": source_row.get("year", ""),
                    "source_databases": source_row.get("source_databases", ""),
                    "query_ids": source_row.get("query_ids", ""),
                    "abstract_available": "yes" if abstract_available(
                        source_row, normalize(source_row.get("abstract", ""))
                    ) else "no",
                    **decision,
                }
            )
            for field, value in decision.items():
                updated[field] = value
            if decision["abstract_screen_decision"] == "exclude_abstract":
                updated["title_abstract_screen"] = "excluded_abstract"
                updated["screen_exclusion_code"] = decision["abstract_screen_exclusion_code"]
                updated["screening_notes"] = decision["abstract_screen_basis"]
            else:
                updated["title_abstract_screen"] = "advance_fulltext"
                updated["screen_exclusion_code"] = ""
                updated["screening_notes"] = decision["abstract_screen_basis"]
        updated_master.append(updated)

    output_fields = list(master_fields)
    for field in (
        "abstract_screen_decision",
        "abstract_screen_exclusion_code",
        "abstract_screen_confidence",
        "abstract_screen_basis",
        "mechanism_evidence",
        "global_output_evidence",
    ):
        if field not in output_fields:
            output_fields.append(field)
    write_csv(abstract_path, ABSTRACT_FIELDS, abstract_rows)

    n_available = sum(row["abstract_available"] == "yes" for row in abstract_rows)
    n_missing = len(abstract_rows) - n_available
    n_ec1 = sum(row["abstract_screen_exclusion_code"] == "EC1" for row in abstract_rows)
    n_ec5 = sum(row["abstract_screen_exclusion_code"] == "EC5" for row in abstract_rows)
    n_ec6 = sum(row["abstract_screen_exclusion_code"] == "EC6" for row in abstract_rows)
    n_advance = sum(row["abstract_screen_decision"] == "advance_fulltext" for row in abstract_rows)
    n_strong = sum(
        row["abstract_screen_decision"] == "advance_fulltext"
        and row["abstract_screen_confidence"] == "medium"
        for row in abstract_rows
    )
    n_uncertain = sum(
        row["abstract_screen_decision"] == "advance_fulltext"
        and row["abstract_screen_confidence"] in {"low", "not_assessed"}
        for row in abstract_rows
    )
    write_csv(
        summary_path,
        SUMMARY_FIELDS,
        [
            {
                "date_run": args.run_date,
                "source_date": args.source_date,
                "n_master": str(len(source_rows)),
                "n_title_abstract_candidates": str(len(candidate_rows)),
                "n_abstracts_available": str(n_available),
                "n_abstracts_missing": str(n_missing),
                "n_exclude_EC1": str(n_ec1),
                "n_exclude_EC5": str(n_ec5),
                "n_exclude_EC6": str(n_ec6),
                "n_advance_fulltext": str(n_advance),
                "n_advance_with_strong_mechanism_signal": str(n_strong),
                "n_advance_abstract_uncertain": str(n_uncertain),
                "rule_version": "abstract-high-confidence-v6",
            }
        ],
    )
    write_csv(primary_master, output_fields, updated_master)

    prisma_fields, prisma_rows = read_csv(prisma_path)
    for row in prisma_rows:
        if row.get("query_id") == "ALL":
            row["notes"] = (
                "Title triage and conservative abstract triage complete; "
                "final title-abstract disposition is retained in derived/abstract-screening-"
                f"summary-{args.run_date}.csv. High-confidence exclusions only; full-text review pending."
            )
    write_csv(prisma_path, prisma_fields, prisma_rows)

    print(f"master={len(source_rows)}")
    print(f"title_abstract_candidates={len(candidate_rows)}")
    print(f"abstracts_available={n_available}")
    print(f"abstracts_missing={n_missing}")
    print(f"exclude_EC1={n_ec1}")
    print(f"exclude_EC5={n_ec5}")
    print(f"exclude_EC6={n_ec6}")
    print(f"advance_fulltext={n_advance}")
    print(f"advance_with_strong_mechanism_signal={n_strong}")
    print(f"advance_abstract_uncertain={n_uncertain}")
    print(f"output_abstract_screening={abstract_path.relative_to(root).as_posix()}")
    print(f"output_summary={summary_path.relative_to(root).as_posix()}")
    print(f"output_pre_abstract_master={pre_abstract_master.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
