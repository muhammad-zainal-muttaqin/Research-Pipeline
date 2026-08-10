#!/usr/bin/env python3
"""Audit verified local PDFs against the current literature-search master.

This pass does not claim that every search candidate has full text. It maps the
verified local PDF corpus to the current master and extracts full text only for
records that match by DOI or normalized title.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader


AUDIT_FIELDS = [
    "local_number",
    "pdf_file",
    "entry_file",
    "entry_title",
    "entry_year",
    "entry_doi",
    "pdf_pages",
    "pdf_extraction_status",
    "master_match_type",
    "master_record_ids",
    "master_titles",
    "title_abstract_screen",
    "fulltext_document_type_signal",
    "fulltext_per_instance_signal",
    "fulltext_quantitative_signal",
    "fulltext_dataset_protocol_signal",
    "fulltext_global_output_signal",
    "local_fulltext_assessment",
    "assessment_basis",
]

SUMMARY_FIELDS = [
    "date_run",
    "local_pdf_count",
    "entry_count",
    "pdf_entry_pairs",
    "matched_current_master_records",
    "matched_by_doi",
    "matched_by_title",
    "unmatched_local_pdfs",
    "fulltext_extracted_for_matches",
    "candidate_local_fulltext_eligible",
    "candidate_local_EC1",
    "candidate_local_EC5",
    "needs_manual_local_review",
]


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def normalize(value: object) -> str:
    text = html.unescape(clean(value))
    text = re.sub(r"<[^>]*>", " ", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def normalize_doi(value: object) -> str:
    text = clean(value).lower()
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text)
    text = re.sub(r"^doi:\s*", "", text)
    return text.strip(" .;,()[]").replace(" ", "")


def write_csv(path: Path, fieldnames: Iterable[str], rows: Iterable[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in writer.fieldnames})


def first_metadata(markdown: str, label: str) -> str:
    match = re.search(rf"\|\s*{re.escape(label)}\s*\|\s*([^|]+?)\s*\|", markdown, re.I)
    return clean(match.group(1)) if match else ""


def entry_doi(markdown: str) -> str:
    for line in markdown.splitlines():
        if "doi" not in line.lower():
            continue
        match = re.search(
            r"(?:https?://(?:dx\.)?doi\.org/|\bdoi:\s*)(10\.\d{4,9}/[-._;()/:a-z0-9]+)",
            line,
            re.I,
        )
        if match:
            return normalize_doi(match.group(1))
    return ""


def excerpt(text: str, pattern: re.Pattern[str], limit: int = 180) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    start = max(0, match.start() - 60)
    end = min(len(text), match.end() + limit)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def extract_pdf(path: Path) -> tuple[int, str, str]:
    try:
        reader = PdfReader(str(path))
        pages: list[str] = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        text = re.sub(r"\s+", " ", " ".join(pages)).strip()
        return len(reader.pages), text, "ok" if text else "no_extractable_text"
    except Exception as exc:  # pragma: no cover - depends on individual PDF files
        return 0, "", f"error: {exc}"


def assess_fulltext(entry_title: str, text: str) -> dict[str, str]:
    title_and_lead = f"{entry_title} {text[:4000]}".lower()
    fulltext = text.lower()
    document_type = re.compile(
        r"\b(?:systematic\s+review|literature\s+review|comprehensive\s+review|"
        r"survey|editorial|author\s+response|conference\s+abstract|poster)\b",
        re.I,
    )
    per_instance = re.compile(
        r"\b(?:object\s+detection|instance\s+segmentation|tracking|multi[-\s]?view|"
        r"cross[-\s]?view|re[-\s]?identification|bounding\s+box|fruit\s+detection|"
        r"individual\s+(?:fruit|object|plant|tree))\b",
        re.I,
    )
    quantitative = re.compile(
        r"\b(?:mAP(?:50)?|AP(?:50)?|accuracy|precision|recall|F1|RMSE|MAE|IoU|"
        r"FPS|AUC|R2|R²|mean\s+average\s+precision|\d+(?:\.\d+)?\s*%)\b",
        re.I,
    )
    dataset_protocol = re.compile(
        r"\b(?:dataset|benchmark|training|validation|test\s+(?:set|dataset)|"
        r"experiment|evaluation|results?)\b",
        re.I,
    )
    global_output = re.compile(
        r"\b(?:yield|production|productivity|biomass|harvest|crop\s+load)\b"
        r".{0,80}\b(?:estimat\w*|predict\w*|forecast\w*|regress\w*)\b",
        re.I,
    )

    doc_match = document_type.search(entry_title) or document_type.search(text[:4000])
    per_match = per_instance.search(fulltext)
    quant_match = quantitative.search(fulltext)
    data_match = dataset_protocol.search(fulltext)
    global_match = global_output.search(fulltext)
    signals = {
        "fulltext_document_type_signal": excerpt(title_and_lead, document_type),
        "fulltext_per_instance_signal": excerpt(fulltext, per_instance),
        "fulltext_quantitative_signal": excerpt(fulltext, quantitative),
        "fulltext_dataset_protocol_signal": excerpt(fulltext, dataset_protocol),
        "fulltext_global_output_signal": excerpt(fulltext, global_output),
    }
    if doc_match:
        assessment = "needs_manual_local_review"
        basis = "review or non-primary document signal; verify IC1, EC2, and EC5 from full text"
    elif global_match and not per_match:
        assessment = "candidate_EC1"
        basis = "global output signal without a per-instance or cross-observation signal"
    elif per_match and quant_match and data_match:
        assessment = "candidate_fulltext_eligible"
        basis = "per-instance or cross-observation signal plus quantitative and evaluation evidence"
    else:
        assessment = "needs_manual_local_review"
        basis = "local full text exists but automated evidence is incomplete"
    return {
        **signals,
        "local_fulltext_assessment": assessment,
        "assessment_basis": basis,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    master_path = derived / "master-screening-2026-08-09.csv"
    pdf_dir = root / "literature" / "pdf" / "benar"
    entries_dir = root / "literature" / "entries"
    audit_path = derived / f"local-fulltext-audit-{args.run_date}.csv"
    summary_path = derived / f"local-fulltext-summary-{args.run_date}.csv"
    if not master_path.exists() or not pdf_dir.exists():
        raise FileNotFoundError("Current master and verified local PDF directory are required")
    if any(path.exists() for path in (audit_path, summary_path)) and not args.force:
        raise FileExistsError("Local full-text audit outputs already exist; use --force")

    with master_path.open("r", encoding="utf-8-sig", newline="") as handle:
        master_rows = list(csv.DictReader(handle))
    master_by_doi: dict[str, list[dict[str, str]]] = {}
    master_by_title: dict[str, list[dict[str, str]]] = {}
    for row in master_rows:
        if row.get("doi"):
            master_by_doi.setdefault(normalize_doi(row["doi"]), []).append(row)
        if row.get("title"):
            master_by_title.setdefault(normalize(row["title"]), []).append(row)

    entry_by_number: dict[int, tuple[Path, str, str, str]] = {}
    entry_files = list(entries_dir.glob("*.md"))
    for entry in entry_files:
        match = re.match(r"(\d+)\s+-", entry.name)
        if not match:
            continue
        markdown = entry.read_text(encoding="utf-8")
        entry_by_number[int(match.group(1))] = (
            entry,
            first_metadata(markdown, "Judul asli") or entry.stem,
            first_metadata(markdown, "Tahun"),
            entry_doi(markdown),
        )

    audit_rows: list[dict[str, str]] = []
    matched_ids: set[str] = set()
    matched_by_doi = 0
    matched_by_title = 0
    pdf_entry_pairs = 0
    for pdf in sorted(pdf_dir.glob("*.pdf"), key=lambda path: path.name.lower()):
        number_match = re.match(r"(\d+)_", pdf.name)
        number = int(number_match.group(1)) if number_match else 0
        entry_info = entry_by_number.get(number)
        entry_file = entry_info[0] if entry_info else None
        entry_title = entry_info[1] if entry_info else ""
        entry_year = entry_info[2] if entry_info else ""
        entry_doi_value = entry_info[3] if entry_info else ""
        if entry_info:
            pdf_entry_pairs += 1

        matches: list[dict[str, str]] = []
        match_type = "none"
        if entry_doi_value and entry_doi_value in master_by_doi:
            matches = master_by_doi[entry_doi_value]
            match_type = "doi"
            matched_by_doi += 1
        elif entry_title and normalize(entry_title) in master_by_title:
            matches = master_by_title[normalize(entry_title)]
            match_type = "title"
            matched_by_title += 1
        matched_ids.update(row["record_id"] for row in matches)

        pdf_pages = 0
        pdf_status = "not_extracted_unmatched"
        fulltext_assessment = {
            "fulltext_document_type_signal": "",
            "fulltext_per_instance_signal": "",
            "fulltext_quantitative_signal": "",
            "fulltext_dataset_protocol_signal": "",
            "fulltext_global_output_signal": "",
            "local_fulltext_assessment": "unmatched_local_pdf",
            "assessment_basis": "verified local PDF does not match the current search master by DOI or normalized title",
        }
        if matches:
            pdf_pages, text, pdf_status = extract_pdf(pdf)
            if pdf_status == "ok":
                fulltext_assessment = assess_fulltext(entry_title, text)
            else:
                fulltext_assessment = {
                    **fulltext_assessment,
                    "local_fulltext_assessment": "needs_manual_local_review",
                    "assessment_basis": f"PDF extraction status: {pdf_status}",
                }

        audit_rows.append(
            {
                "local_number": f"{number:03d}" if number else "",
                "pdf_file": pdf.name,
                "entry_file": entry_file.name if entry_file else "",
                "entry_title": entry_title,
                "entry_year": entry_year,
                "entry_doi": entry_doi_value,
                "pdf_pages": str(pdf_pages),
                "pdf_extraction_status": pdf_status,
                "master_match_type": match_type,
                "master_record_ids": ";".join(row["record_id"] for row in matches),
                "master_titles": " | ".join(row.get("title", "") for row in matches),
                "title_abstract_screen": ";".join(row.get("title_abstract_screen", "") for row in matches),
                **fulltext_assessment,
            }
        )

    counts = Counter(row["local_fulltext_assessment"] for row in audit_rows)
    write_csv(audit_path, AUDIT_FIELDS, audit_rows)
    write_csv(
        summary_path,
        SUMMARY_FIELDS,
        [
            {
                "date_run": args.run_date,
                "local_pdf_count": str(len(audit_rows)),
                "entry_count": str(len(entry_files)),
                "pdf_entry_pairs": str(pdf_entry_pairs),
                "matched_current_master_records": str(len(matched_ids)),
                "matched_by_doi": str(matched_by_doi),
                "matched_by_title": str(matched_by_title),
                "unmatched_local_pdfs": str(sum(row["master_match_type"] == "none" for row in audit_rows)),
                "fulltext_extracted_for_matches": str(sum(row["pdf_extraction_status"] == "ok" for row in audit_rows)),
                "candidate_local_fulltext_eligible": str(counts["candidate_fulltext_eligible"]),
                "candidate_local_EC1": str(counts["candidate_EC1"]),
                "candidate_local_EC5": str(counts["candidate_EC5"]),
                "needs_manual_local_review": str(counts["needs_manual_local_review"]),
            }
        ],
    )
    print(f"local_pdfs={len(audit_rows)}")
    print(f"entries={len(entry_files)}")
    print(f"pdf_entry_pairs={pdf_entry_pairs}")
    print(f"matched_current_master_records={len(matched_ids)}")
    print(f"matched_by_doi={matched_by_doi}")
    print(f"matched_by_title={matched_by_title}")
    print(f"fulltext_extracted_for_matches={sum(row['pdf_extraction_status'] == 'ok' for row in audit_rows)}")
    print(f"candidate_fulltext_eligible={counts['candidate_fulltext_eligible']}")
    print(f"candidate_EC1={counts['candidate_EC1']}")
    print(f"candidate_EC5={counts['candidate_EC5']}")
    print(f"needs_manual_local_review={counts['needs_manual_local_review']}")
    print(f"output_audit={audit_path.relative_to(root).as_posix()}")
    print(f"output_summary={summary_path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
