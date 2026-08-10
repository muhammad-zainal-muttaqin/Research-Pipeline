#!/usr/bin/env python3
"""Run a conservative title-only screening pass.

Only high-confidence title signals are excluded here. All other records advance
to abstract screening because EC1 cannot be decided reliably from a title alone.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Iterable


TITLE_FIELDS = [
    "record_id",
    "doi",
    "title",
    "year",
    "source_databases",
    "query_ids",
    "title_screen_decision",
    "title_screen_exclusion_code",
    "title_screen_confidence",
    "title_screen_basis",
    "abstract_screen_status",
    "abstract_screen_priority",
]

SUMMARY_FIELDS = [
    "date_run",
    "n_master",
    "n_titles_reviewed",
    "n_exclude_EC5",
    "n_exclude_EC6",
    "n_advance_to_abstract",
    "n_missing_title",
    "rule_version",
]

EDITORIAL_PATTERNS = [
    (re.compile(r"^editorial\b", re.I), "editorial"),
    (re.compile(r"^comment\s+on\b", re.I), "comment on another work"),
    (re.compile(r"^reply\s+(on|to)\b", re.I), "reply to review/comment"),
    (re.compile(r"^decision\s+letter\b", re.I), "decision letter"),
    (re.compile(r"^review\s+for\b", re.I), "peer review record"),
    (re.compile(r"^peer\s+review\s+report\b", re.I), "peer review report"),
    (re.compile(r"^review\s+of:\s*", re.I), "peer review record"),
    (re.compile(r"^instructions?\s+to\s+author", re.I), "instructions to author"),
    (re.compile(r"^index\s*$", re.I), "index"),
    (re.compile(r"^preface\b", re.I), "preface"),
    (re.compile(r"^foreword\b", re.I), "foreword"),
    (re.compile(r"^erratum\b", re.I), "erratum"),
    (re.compile(r"^corrigendum\b", re.I), "corrigendum"),
    (re.compile(r"^correction\s+(to|for)\b|^correction\s*:", re.I), "correction notice"),
    (re.compile(r"^retraction\b", re.I), "retraction notice"),
    (re.compile(r"^commentary\b", re.I), "commentary"),
    (re.compile(r"^poster\b", re.I), "poster"),
    (re.compile(r"\bconference\s+abstract\b", re.I), "conference abstract"),
    (re.compile(r"\bposter\s+abstract\b", re.I), "poster abstract"),
    (re.compile(r"^patent\b|\bpatent\s+application\b", re.I), "patent record"),
]

CORE_TERMS = re.compile(
    r"\b(fruit|mango|apple|citrus|grape|berry|bunch|crop|orchard|vineyard|"
    r"oil\s+palm|fresh\s+fruit\s+bunch|plant|tree|agriculture|agricultural|"
    r"yield|harvest|phenotyp|leaf|canopy)\b",
    re.I,
)

MECHANISM_TERMS = re.compile(
    r"\b(count|counting|enumerat|detect|detection|segment|segmentation|"
    r"tracking|track|re-identification|reidentification|multi-view|multiview|"
    r"cross-view|multi-camera|association|correspondence|instance|object|"
    r"point cloud|3d|three-dimensional|computer vision|image|lidar|remote sensing)\b",
    re.I,
)


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


def title_decision(row: dict[str, str]) -> dict[str, str]:
    title = clean(row.get("title", ""))
    year = clean(row.get("year", ""))
    if year and year.isdigit() and not 2015 <= int(year) <= 2026:
        return {
            "title_screen_decision": "exclude_title",
            "title_screen_exclusion_code": "EC6",
            "title_screen_confidence": "high",
            "title_screen_basis": f"publication year {year} is outside 2015-2026",
            "abstract_screen_status": "not_needed",
            "abstract_screen_priority": "none",
        }
    for pattern, label in EDITORIAL_PATTERNS:
        if pattern.search(title):
            return {
                "title_screen_decision": "exclude_title",
                "title_screen_exclusion_code": "EC5",
                "title_screen_confidence": "high",
                "title_screen_basis": f"title signal: {label}",
                "abstract_screen_status": "not_needed",
                "abstract_screen_priority": "none",
            }
    if not title:
        priority = "high_missing_title"
        basis = "title is missing; use abstract and source metadata"
    elif CORE_TERMS.search(title) and MECHANISM_TERMS.search(title):
        priority = "high_relevance_signal"
        basis = "title contains domain and visual/mechanism terms; retain for abstract screening"
    elif CORE_TERMS.search(title) or MECHANISM_TERMS.search(title):
        priority = "normal_relevance_signal"
        basis = "title contains one target signal; retain for abstract screening"
    else:
        priority = "low_relevance_signal"
        basis = "no decisive title-level exclusion; retain to protect recall"
    return {
        "title_screen_decision": "advance_to_abstract",
        "title_screen_exclusion_code": "",
        "title_screen_confidence": "high" if title else "medium",
        "title_screen_basis": basis,
        "abstract_screen_status": "pending",
        "abstract_screen_priority": priority,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--force", action="store_true", help="replace title-screening outputs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    source_master = derived / f"master-screening-resolved-{args.run_date}.csv"
    primary_master = derived / f"master-screening-{args.run_date}.csv"
    pre_title_master = derived / f"master-screening-pre-title-{args.run_date}.csv"
    title_path = derived / f"title-screening-{args.run_date}.csv"
    summary_path = derived / f"title-screening-summary-{args.run_date}.csv"
    prisma_path = root / "literature" / "search" / "prisma-counts.csv"

    if not source_master.exists() or not prisma_path.exists():
        raise FileNotFoundError("Resolved master and PRISMA files are required")
    if not pre_title_master.exists():
        shutil.copyfile(source_master, pre_title_master)
    if any(path.exists() for path in (title_path, summary_path)) and not args.force:
        raise FileExistsError("Title screening outputs already exist; use --force to rebuild")

    master_fields, source_rows = read_csv(pre_title_master)
    title_rows: list[dict[str, str]] = []
    updated_master: list[dict[str, str]] = []
    for source_row in source_rows:
        decision = title_decision(source_row)
        title_rows.append(
            {
                "record_id": source_row.get("record_id", ""),
                "doi": source_row.get("doi", ""),
                "title": source_row.get("title", ""),
                "year": source_row.get("year", ""),
                "source_databases": source_row.get("source_databases", ""),
                "query_ids": source_row.get("query_ids", ""),
                **decision,
            }
        )
        updated = dict(source_row)
        for field, value in decision.items():
            updated[field] = value
        if decision["title_screen_decision"] == "exclude_title":
            updated["title_abstract_screen"] = "excluded_title"
            updated["screen_exclusion_code"] = decision["title_screen_exclusion_code"]
            updated["screening_notes"] = decision["title_screen_basis"]
        else:
            updated["title_abstract_screen"] = "pending"
        updated_master.append(updated)

    output_fields = list(master_fields)
    for field in (
        "title_screen_decision",
        "title_screen_exclusion_code",
        "title_screen_confidence",
        "title_screen_basis",
        "abstract_screen_status",
        "abstract_screen_priority",
    ):
        if field not in output_fields:
            output_fields.append(field)
    write_csv(title_path, TITLE_FIELDS, title_rows)
    write_csv(
        summary_path,
        SUMMARY_FIELDS,
        [
            {
                "date_run": args.run_date,
                "n_master": str(len(source_rows)),
                "n_titles_reviewed": str(len(source_rows)),
                "n_exclude_EC5": str(sum(row["title_screen_exclusion_code"] == "EC5" for row in title_rows)),
                "n_exclude_EC6": str(sum(row["title_screen_exclusion_code"] == "EC6" for row in title_rows)),
                "n_advance_to_abstract": str(sum(row["title_screen_decision"] == "advance_to_abstract" for row in title_rows)),
                "n_missing_title": str(sum(not clean(row["title"]) for row in title_rows)),
                "rule_version": "title-high-confidence-v1",
            }
        ],
    )
    write_csv(primary_master, output_fields, updated_master)

    prisma_fields, prisma_rows = read_csv(prisma_path)
    summary = title_rows
    for row in prisma_rows:
        if row.get("query_id") == "ALL":
            row["notes"] = "Title-only high-confidence triage complete; title-abstract screening remains pending. See derived/title-screening-summary-2026-08-09.csv."
    write_csv(prisma_path, prisma_fields, prisma_rows)

    n_ec5 = sum(row["title_screen_exclusion_code"] == "EC5" for row in summary)
    n_ec6 = sum(row["title_screen_exclusion_code"] == "EC6" for row in summary)
    print(f"titles_reviewed={len(summary)}")
    print(f"exclude_EC5={n_ec5}")
    print(f"exclude_EC6={n_ec6}")
    print(f"advance_to_abstract={len(summary) - n_ec5 - n_ec6}")
    print(f"output_title_screening={title_path.relative_to(root).as_posix()}")
    print(f"output_summary={summary_path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
