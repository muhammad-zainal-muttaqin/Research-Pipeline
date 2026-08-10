#!/usr/bin/env python3
"""Record one full-text review decision in the resumable ledger.

Retrieval, screening, and synthesis are deliberately separate. This script
updates one candidate at a time and preserves every field belonging to all
other candidates.
"""

from __future__ import annotations

import argparse
import csv
import tempfile
import time
from datetime import date, datetime, timezone
from pathlib import Path


ALLOWED = {
    "decision": {"include", "exclude", "uncertain"},
    "review_status": {"reviewed", "needs_manual_retrieval", "ready_for_review"},
    "retrieval_status": {"pending", "local_available", "retrieved", "not_found_or_restricted"},
    "ic1": {"yes", "no", "uncertain"},
    "ic2": {"yes", "no", "uncertain"},
    "ic3": {"yes", "no", "uncertain"},
    "ic4": {"yes", "no", "uncertain"},
    "ic5": {"yes", "no", "uncertain"},
    "ec2": {"yes", "no", "uncertain"},
    "ec3": {"yes", "no", "uncertain"},
    "ec4": {"yes", "no", "uncertain"},
}

NEW_FIELDS = [
    "evidence_type",
    "study_design",
    "modality",
    "task_scope",
    "identity_mechanism",
    "class_attribute",
    "evaluation",
    "key_finding",
    "limitations",
]


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    return fields, rows


def write_csv_atomic(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", dir=path.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    last_error: PermissionError | None = None
    for attempt in range(8):
        try:
            temporary.replace(path)
            return
        except PermissionError as exc:
            last_error = exc
            if attempt == 7:
                break
            time.sleep(0.5)
    raise last_error or PermissionError(f"could not replace {path}")


def find_index(rows: list[dict[str, str]], record_id: str, order: str) -> int:
    for index, row in enumerate(rows):
        if record_id and clean(row.get("record_id")) == record_id:
            return index
        if order and clean(row.get("review_order")) == order:
            return index
    raise KeyError(f"candidate not found: record_id={record_id!r}, order={order!r}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--record-id")
    group.add_argument("--order")
    parser.add_argument("--decision", choices=sorted(ALLOWED["decision"]), required=True)
    parser.add_argument("--review-status", default="reviewed", choices=sorted(ALLOWED["review_status"]))
    parser.add_argument("--retrieval-status", choices=sorted(ALLOWED["retrieval_status"]))
    parser.add_argument("--retrieval-source")
    parser.add_argument("--fulltext-path")
    parser.add_argument("--extraction-status")
    parser.add_argument("--document-type")
    for field in ("ic1", "ic2", "ic3", "ic4", "ic5", "ec2", "ec3", "ec4"):
        parser.add_argument(f"--{field}", choices=sorted(ALLOWED[field]), required=True)
    parser.add_argument("--exclusion-code", default="")
    parser.add_argument("--evidence-pages", required=True)
    parser.add_argument("--evidence-quote", required=True)
    for field in NEW_FIELDS:
        option = f"--{field.replace('_', '-')}"
        legacy_option = f"--{field}"
        parser.add_argument(option, legacy_option, dest=field, default="")
    parser.add_argument("--reviewer", default="agent")
    parser.add_argument("--review-date", default=date.today().isoformat())
    parser.add_argument("--review-notes", required=True)
    parser.add_argument("--ledger-date", default="2026-08-10")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    ledger_path = root / "literature" / "search" / "derived" / f"fulltext-review-ledger-{args.ledger_date}.csv"
    fields, rows = read_csv(ledger_path)

    missing = [field for field in NEW_FIELDS if field not in fields]
    if missing:
        fields.extend(missing)
        for row in rows:
            for field in missing:
                row.setdefault(field, "")

    index = find_index(rows, args.record_id or "", args.order or "")
    row = rows[index]
    if clean(row.get("decision")) not in {"", "pending"}:
        raise ValueError(
            f"candidate already has decision={row['decision']!r}; use the ledger history before changing it"
        )
    if args.decision == "exclude" and not clean(args.exclusion_code):
        raise ValueError("--exclusion-code is required for an excluded candidate")
    if args.decision != "exclude" and clean(args.exclusion_code):
        raise ValueError("--exclusion-code must be empty unless --decision exclude is used")

    updates = {
        "review_status": args.review_status,
        "retrieval_status": args.retrieval_status or clean(row.get("retrieval_status")),
        "retrieval_source": args.retrieval_source if args.retrieval_source is not None else clean(row.get("retrieval_source")),
        "fulltext_path": args.fulltext_path if args.fulltext_path is not None else clean(row.get("fulltext_path")),
        "extraction_status": args.extraction_status if args.extraction_status is not None else clean(row.get("extraction_status")),
        "document_type": args.document_type or "",
        "ic1": args.ic1,
        "ic2": args.ic2,
        "ic3": args.ic3,
        "ic4": args.ic4,
        "ic5": args.ic5,
        "ec2": args.ec2,
        "ec3": args.ec3,
        "ec4": args.ec4,
        "decision": args.decision,
        "exclusion_code": args.exclusion_code,
        "evidence_pages": args.evidence_pages,
        "evidence_quote": args.evidence_quote,
        "evidence_type": args.evidence_type,
        "study_design": args.study_design,
        "modality": args.modality,
        "task_scope": args.task_scope,
        "identity_mechanism": args.identity_mechanism,
        "class_attribute": args.class_attribute,
        "evaluation": args.evaluation,
        "key_finding": args.key_finding,
        "limitations": args.limitations,
        "reviewer": args.reviewer,
        "review_date": args.review_date,
        "review_notes": args.review_notes,
        "updated_at": now_iso(),
    }
    row.update(updates)
    write_csv_atomic(ledger_path, fields, rows)
    print(f"record_id={row['record_id']}")
    print(f"review_order={row['review_order']}")
    print(f"decision={row['decision']}")
    print(f"review_status={row['review_status']}")
    print(f"ledger={ledger_path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
