#!/usr/bin/env python3
"""Create a resumable, one-record-per-candidate full-text review ledger.

The ledger is deliberately separate from the search and abstract-screening
exports. Those files remain immutable evidence of earlier stages. A later
review pass can update only the full-text decision fields in this ledger.
"""

from __future__ import annotations

import argparse
import csv
import re
from datetime import date, datetime, timezone
from pathlib import Path


FIELDS = [
    "review_order",
    "record_id",
    "doi",
    "title",
    "year",
    "venue",
    "authors",
    "source_databases",
    "query_ids",
    "openalex_ids",
    "scopus_eids",
    "scopus_links",
    "abstract_available",
    "abstract_screen_confidence",
    "abstract_screen_basis",
    "mechanism_evidence",
    "review_status",
    "retrieval_status",
    "retrieval_source",
    "fulltext_path",
    "extraction_status",
    "document_type",
    "ic1",
    "ic2",
    "ic3",
    "ic4",
    "ic5",
    "ec2",
    "ec3",
    "ec4",
    "decision",
    "exclusion_code",
    "evidence_pages",
    "evidence_quote",
    "evidence_type",
    "study_design",
    "modality",
    "task_scope",
    "identity_mechanism",
    "class_attribute",
    "evaluation",
    "key_finding",
    "limitations",
    "reviewer",
    "review_date",
    "review_notes",
    "updated_at",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def query_tokens(value: str) -> set[str]:
    return {token for token in re.split(r"[;|,\s]+", value.upper()) if token}


def relevance_score(row: dict[str, str]) -> int:
    """Rank likely direct or transferable mechanism evidence first.

    This is a queue order only. It is never a full-text decision and it is
    preserved once written to the ledger.
    """

    title = clean(row.get("title", "")).lower()
    basis = clean(row.get("abstract_screen_basis", "")).lower()
    query_ids = query_tokens(row.get("query_ids", ""))
    score = 0
    if row.get("abstract_screen_confidence") == "medium":
        score += 100
    if row.get("abstract_available") == "yes":
        score += 10
    if clean(row.get("doi")):
        score += 5
    if query_ids & {"Q1", "Q2", "Q3", "Q4", "Q6", "Q7"}:
        score += 10
    if "Q1" in query_ids or "Q6" in query_ids or "Q7" in query_ids:
        score += 8
    mechanism_terms = (
        "multi-view",
        "cross-view",
        "multi-camera",
        "re-identification",
        "data association",
        "structure from motion",
        "point cloud",
        "3d",
        "fruit detection",
        "fruit counting",
        "oil palm",
        "fresh fruit bunch",
        "apple",
        "citrus",
        "mango",
        "grape",
    )
    score += min(30, sum(3 for term in mechanism_terms if term in title or term in basis))
    if not title or title.startswith("#"):
        score -= 20
    return score


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--force", action="store_true", help="replace an existing ledger")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    abstract_path = derived / "abstract-screening-2026-08-10.csv"
    master_path = derived / "master-screening-2026-08-09.csv"
    local_audit_path = derived / "local-fulltext-audit-2026-08-10.csv"
    ledger_path = derived / f"fulltext-review-ledger-{args.run_date}.csv"

    if ledger_path.exists() and not args.force:
        raise FileExistsError(f"{ledger_path} already exists; use --force only for a deliberate rebuild")

    _, abstract_rows = read_csv(abstract_path)
    _, master_rows = read_csv(master_path)
    master_by_id = {clean(row.get("record_id")): row for row in master_rows}

    local_pdf_by_id: dict[str, str] = {}
    if local_audit_path.exists():
        _, local_rows = read_csv(local_audit_path)
        for row in local_rows:
            if row.get("master_match_type") == "none":
                continue
            for record_id in clean(row.get("master_record_ids")).split(";"):
                if record_id:
                    local_pdf_by_id[record_id] = clean(row.get("pdf_file"))

    candidates = [
        row
        for row in abstract_rows
        if clean(row.get("abstract_screen_decision")) == "advance_fulltext"
    ]
    candidates.sort(
        key=lambda row: (
            -relevance_score(row),
            0 if clean(row.get("doi")) else 1,
            clean(row.get("year")),
            clean(row.get("record_id")),
        )
    )

    timestamp = now_iso()
    ledger_rows: list[dict[str, str]] = []
    for order, abstract_row in enumerate(candidates, start=1):
        record_id = clean(abstract_row.get("record_id"))
        master = master_by_id.get(record_id, {})
        local_pdf = local_pdf_by_id.get(record_id, "")
        row = {field: "" for field in FIELDS}
        row.update(
            {
                "review_order": str(order),
                "record_id": record_id,
                "doi": clean(abstract_row.get("doi")) or clean(master.get("doi")),
                "title": clean(abstract_row.get("title")) or clean(master.get("title")),
                "year": clean(abstract_row.get("year")) or clean(master.get("year")),
                "venue": clean(master.get("venue")),
                "authors": clean(master.get("authors")),
                "source_databases": clean(abstract_row.get("source_databases"))
                or clean(master.get("source_databases")),
                "query_ids": clean(abstract_row.get("query_ids")) or clean(master.get("query_ids")),
                "openalex_ids": clean(master.get("openalex_ids")),
                "scopus_eids": clean(master.get("scopus_eids")),
                "scopus_links": clean(master.get("scopus_links")),
                "abstract_available": clean(abstract_row.get("abstract_available")),
                "abstract_screen_confidence": clean(abstract_row.get("abstract_screen_confidence")),
                "abstract_screen_basis": clean(abstract_row.get("abstract_screen_basis")),
                "mechanism_evidence": clean(abstract_row.get("mechanism_evidence")),
                "review_status": "pending",
                "retrieval_status": "local_available" if local_pdf else "pending",
                "retrieval_source": "local_verified_pdf" if local_pdf else "",
                "fulltext_path": f"literature/pdf/benar/{local_pdf}" if local_pdf else "",
                "extraction_status": "extracted_by_local_audit" if local_pdf else "",
                "decision": "pending",
                "updated_at": timestamp,
            }
        )
        ledger_rows.append(row)

    write_csv(ledger_path, ledger_rows)
    print(f"candidates={len(ledger_rows)}")
    print(f"doi_candidates={sum(bool(row['doi']) for row in ledger_rows)}")
    print(f"local_pdf_matches={sum(row['retrieval_status'] == 'local_available' for row in ledger_rows)}")
    print(f"output={ledger_path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
