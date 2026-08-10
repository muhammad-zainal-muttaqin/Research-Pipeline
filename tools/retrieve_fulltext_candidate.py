#!/usr/bin/env python3
"""Retrieve one candidate's legally accessible full text and update the ledger.

The script is intentionally one-record-at-a-time. It never marks a candidate
included or excluded; retrieval and scientific review remain separate steps.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


MAX_BYTES = 75 * 1024 * 1024


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


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


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def slug(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return text[:90] or "candidate"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def is_trusted_html(payload: bytes) -> bool:
    """Reject bot challenges and redirect shells masquerading as full text."""
    sample = payload[:65536].lower()
    blocked_markers = (
        b"awswaf",
        b"challenge.js",
        b"are you a robot",
        b"javascript is disabled",
        b"verify that you're not a robot",
    )
    if any(marker in sample for marker in blocked_markers):
        return False
    return b"<html" in sample and len(payload) >= 4096


def fetch_bytes(url: str, allow_html: bool = False) -> tuple[bytes, str, str]:
    request = Request(
        url,
        headers={
            "User-Agent": "Research-Pipeline full-text retrieval/1.0",
            "Accept": "application/pdf,application/octet-stream;q=0.8,text/html;q=0.2",
        },
    )
    with urlopen(request, timeout=45) as response:
        content_type = clean(response.headers.get("Content-Type")).lower()
        content_length = clean(response.headers.get("Content-Length"))
        if content_length.isdigit() and int(content_length) > MAX_BYTES:
            raise ValueError(f"response exceeds {MAX_BYTES} bytes")
        data = bytearray()
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            data.extend(chunk)
            if len(data) > MAX_BYTES:
                raise ValueError(f"response exceeds {MAX_BYTES} bytes")
        payload = bytes(data)
        if payload.startswith(b"%PDF-"):
            return payload, content_type, "pdf"
        if allow_html and "text/html" in content_type and is_trusted_html(payload):
            return payload, content_type, "html"
        raise ValueError(f"response is not an accepted full-text artifact; content_type={content_type or 'unknown'}")


def openalex_urls(doi: str) -> list[str]:
    if not doi:
        return []
    api_url = "https://api.openalex.org/works/https://doi.org/" + quote(doi, safe="")
    request = Request(api_url, headers={"User-Agent": "Research-Pipeline full-text retrieval/1.0"})
    with urlopen(request, timeout=30) as response:
        record = json.loads(response.read().decode("utf-8"))
    urls: list[str] = []
    best = record.get("best_oa_location") or {}
    for location in [best, *(record.get("locations") or [])]:
        for key in ("pdf_url", "landing_page_url"):
            value = clean(location.get(key))
            if value and value not in urls:
                urls.append(value)
    return urls


def candidate_index(rows: list[dict[str, str]], record_id: str, order: str) -> int:
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
    parser.add_argument("--url", action="append", default=[], help="explicit OA PDF or landing URL")
    parser.add_argument("--allow-html", action="store_true", help="accept a trusted full-text HTML page")
    parser.add_argument("--force", action="store_true", help="retry and replace an existing downloaded file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    ledger_path = derived / "fulltext-review-ledger-2026-08-10.csv"
    fulltext_dir = root / "literature" / "search" / "fulltext"
    fields, rows = read_csv(ledger_path)
    index = candidate_index(rows, args.record_id or "", args.order or "")
    row = rows[index]

    urls = list(args.url)
    doi = clean(row.get("doi"))
    if doi:
        doi_url = f"https://doi.org/{doi}"
        if doi_url not in urls:
            urls.append(doi_url)
        try:
            for url in openalex_urls(doi):
                if url not in urls:
                    urls.append(url)
        except Exception as exc:
            print(f"openalex_lookup=failed: {exc}")

    attempted: list[str] = []
    errors: list[str] = []
    for url in urls:
        if not url or url in attempted:
            continue
        attempted.append(url)
        try:
            payload, content_type, artifact_type = fetch_bytes(url, allow_html=args.allow_html)
        except (HTTPError, URLError, ValueError, TimeoutError) as exc:
            errors.append(f"{url}: {exc}")
            continue
        fulltext_dir.mkdir(parents=True, exist_ok=True)
        extension = "pdf" if artifact_type == "pdf" else "html"
        filename = f"{int(row['review_order']):05d}_{slug(row['record_id'])}_{slug(row['title'])}.{extension}"
        output_path = fulltext_dir / filename
        if output_path.exists() and not args.force:
            print(f"existing_file={output_path.relative_to(root).as_posix()}")
        else:
            output_path.write_bytes(payload)
        row.update(
            {
                "review_status": "ready_for_review",
                "retrieval_status": "retrieved",
                "retrieval_source": url,
                "fulltext_path": output_path.relative_to(root).as_posix(),
                "extraction_status": "pending" if artifact_type == "pdf" else "html_fulltext_pending",
                "review_notes": f"retrieved {artifact_type} ({len(payload)} bytes; {content_type or 'content type unavailable'})",
                "updated_at": now_iso(),
            }
        )
        write_csv_atomic(ledger_path, fields, rows)
        print(f"record_id={row['record_id']}")
        print(f"retrieval_status=retrieved")
        print(f"source={url}")
        print(f"path={output_path.relative_to(root).as_posix()}")
        print(f"bytes={len(payload)}")
        return 0

    row.update(
        {
            "review_status": "needs_manual_retrieval",
            "retrieval_status": "not_found_or_restricted",
            "retrieval_source": " | ".join(attempted),
            "review_notes": "No legally accessible PDF retrieved automatically. " + " | ".join(errors),
            "updated_at": now_iso(),
        }
    )
    write_csv_atomic(ledger_path, fields, rows)
    print(f"record_id={row['record_id']}")
    print("retrieval_status=not_found_or_restricted")
    print(f"attempts={len(attempted)}")
    print(f"errors={len(errors)}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
