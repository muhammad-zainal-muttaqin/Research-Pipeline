#!/usr/bin/env python3
"""Create readable review reports for unresolved deduplication groups."""

from __future__ import annotations

import argparse
import csv
import html
from datetime import date
from pathlib import Path
from typing import Iterable


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def md(value: object) -> str:
    text = clean(value).replace("\r", " ").replace("\n", " ")
    return text.replace("|", "\\|")


def html_text(value: object) -> str:
    return html.escape(clean(value).replace("\r", " ").replace("\n", " "))


def component_for(record_id: str, components: str) -> str:
    for component in components.split(" | "):
        ids = [item for item in component.split("+") if item]
        if record_id in ids:
            if len(ids) > 1:
                return "merge saat ini dengan " + ", ".join(item for item in ids if item != record_id)
            return "keep separate saat ini"
    return "review"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--force", action="store_true", help="replace existing reports")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    resolution_path = derived / f"dedup-resolution-{args.run_date}.csv"
    exact_master_path = derived / f"master-screening-exact-key-{args.run_date}.csv"
    report_csv = derived / f"dedup-resolution-review-{args.run_date}.csv"
    report_md = derived / f"dedup-resolution-review-{args.run_date}.md"
    report_html = derived / f"dedup-resolution-review-{args.run_date}.html"

    for path in (resolution_path, exact_master_path):
        if not path.exists():
            raise FileNotFoundError(f"Missing input: {path}")
    outputs = (report_csv, report_md, report_html)
    if any(path.exists() for path in outputs) and not args.force:
        names = ", ".join(str(path.relative_to(root)) for path in outputs if path.exists())
        raise FileExistsError(f"Reports already exist: {names}")

    _, resolution_rows = read_csv(resolution_path)
    _, master_rows = read_csv(exact_master_path)
    master_by_id = {row["record_id"]: row for row in master_rows}
    unresolved = [
        row
        for row in resolution_rows
        if row["decision"] in {"keep_separate_conservative", "partial_merge_author_match"}
    ]
    unresolved.sort(key=lambda row: row["review_id"])

    review_fields = [
        "review_id",
        "current_decision",
        "candidate_record_id",
        "doi",
        "title",
        "year",
        "authors",
        "venue",
        "source_databases",
        "query_ids",
        "abstract_available",
        "raw_files",
        "current_component_action",
        "resolution_basis",
        "user_decision",
        "user_notes",
    ]
    review_rows: list[dict[str, str]] = []
    for resolution in unresolved:
        for record_id in resolution["candidate_record_ids"].split(";"):
            candidate = master_by_id[record_id]
            review_rows.append(
                {
                    "review_id": resolution["review_id"],
                    "current_decision": resolution["decision"],
                    "candidate_record_id": record_id,
                    "doi": candidate.get("doi", ""),
                    "title": candidate.get("title", ""),
                    "year": candidate.get("year", ""),
                    "authors": candidate.get("authors", ""),
                    "venue": candidate.get("venue", ""),
                    "source_databases": candidate.get("source_databases", ""),
                    "query_ids": candidate.get("query_ids", ""),
                    "abstract_available": candidate.get("abstract_available", ""),
                    "raw_files": candidate.get("raw_files", ""),
                    "current_component_action": component_for(
                        record_id, resolution["resolved_components"]
                    ),
                    "resolution_basis": resolution["resolution_basis"],
                    "user_decision": "",
                    "user_notes": "",
                }
            )

    write_csv(report_csv, review_fields, review_rows)

    lines = [
        f"# Deduplication review, {args.run_date}",
        "",
        "Laporan ini hanya memuat kelompok residual yang belum dapat diputuskan sepenuhnya secara otomatis. Laporan ini untuk spot-check dan tidak menghalangi screening judul-abstrak.",
        "",
        f"- Kelompok residual untuk spot-check: **{len(unresolved)}**",
        f"- Kandidat yang ditampilkan: **{len(review_rows)}**",
        "- Pilihan keputusan: `merge` atau `keep_separate`.",
        "- CSV ringkas di sebelah file ini bersifat opsional dan dapat dipakai untuk mengisi keputusan serta catatan.",
        "",
        "## Cara membaca",
        "",
        "`keep_separate_conservative` berarti record tidak digabung karena bukti penulis, venue, DOI, atau metadata belum cukup. `partial_merge_author_match` berarti sebagian kandidat sudah cocok, tetapi ada kandidat lain yang tetap dipisahkan.",
        "",
    ]
    for resolution in unresolved:
        ids = resolution["candidate_record_ids"].split(";")
        group_raw_files = sorted(
            {
                raw_file
                for record_id in ids
                for raw_file in master_by_id[record_id].get("raw_files", "").split(" || ")
                if raw_file.strip()
            }
        )
        lines.extend(
            [
                f"## {resolution['review_id']}",
                "",
                f"**Keputusan saat ini:** `{resolution['decision']}`",
                f"**Dasar:** {md(resolution['resolution_basis'])}",
                f"**Komponen:** `{md(resolution['resolved_components'])}`",
                "",
                "| ID | DOI | Judul | Tahun | Penulis | Venue | Sumber | Tindakan saat ini | Keputusan Anda | Catatan |",
                "|---|---|---|---:|---|---|---|---|---|---|",
            ]
        )
        for record_id in ids:
            candidate = master_by_id[record_id]
            lines.append(
                "| "
                + " | ".join(
                    [
                        md(record_id),
                        md(candidate.get("doi", "")),
                        md(candidate.get("title", "")),
                        md(candidate.get("year", "")),
                        md(candidate.get("authors", "")),
                        md(candidate.get("venue", "")),
                        md(candidate.get("source_databases", "")),
                        md(component_for(record_id, resolution["resolved_components"])),
                        "",
                        "",
                    ]
                )
                + "|"
            )
        lines.extend(["", "Raw files:"])
        lines.extend(f"- `{md(raw_file)}`" for raw_file in group_raw_files)
        lines.append("")
    report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    html_parts = [
        "<!doctype html>",
        '<html lang="id"><head><meta charset="utf-8">',
        f"<title>Deduplication review {html_text(args.run_date)}</title>",
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:2rem;line-height:1.4;color:#202124}h1{margin-bottom:.3rem}h2{margin-top:2.5rem;border-bottom:1px solid #ddd;padding-bottom:.3rem}table{border-collapse:collapse;width:100%;margin:1rem 0 2rem;font-size:.9rem}th,td{border:1px solid #d9d9d9;padding:.45rem;text-align:left;vertical-align:top}th{background:#f3f5f7}td{max-width:28rem}code{background:#f1f3f4;padding:.1rem .25rem;border-radius:3px}.muted{color:#5f6368}</style>",
        "</head><body>",
        f"<h1>Deduplication review, {html_text(args.run_date)}</h1>",
        f"<p class=\"muted\">{len(unresolved)} kelompok, {len(review_rows)} kandidat. Isi keputusan di CSV ringkas.</p>",
    ]
    for resolution in unresolved:
        html_parts.append(f"<h2>{html_text(resolution['review_id'])}</h2>")
        html_parts.append(
            f"<p><strong>Keputusan saat ini:</strong> <code>{html_text(resolution['decision'])}</code><br>"
            f"<strong>Dasar:</strong> {html_text(resolution['resolution_basis'])}<br>"
            f"<strong>Komponen:</strong> <code>{html_text(resolution['resolved_components'])}</code></p>"
        )
        html_parts.append("<table><thead><tr><th>ID</th><th>DOI</th><th>Judul</th><th>Tahun</th><th>Penulis</th><th>Venue</th><th>Sumber</th><th>Tindakan saat ini</th><th>Keputusan Anda</th><th>Catatan</th></tr></thead><tbody>")
        for record_id in resolution["candidate_record_ids"].split(";"):
            candidate = master_by_id[record_id]
            html_parts.append(
                "<tr>"
                + "".join(
                    f"<td>{html_text(value)}</td>"
                    for value in (
                        record_id,
                        candidate.get("doi", ""),
                        candidate.get("title", ""),
                        candidate.get("year", ""),
                        candidate.get("authors", ""),
                        candidate.get("venue", ""),
                        candidate.get("source_databases", ""),
                        component_for(record_id, resolution["resolved_components"]),
                        "",
                        "",
                    )
                )
                + "</tr>"
            )
        html_parts.append("</tbody></table>")
    html_parts.append("</body></html>")
    report_html.write_text("\n".join(html_parts), encoding="utf-8")

    print(f"unresolved_groups={len(unresolved)}")
    print(f"candidate_rows={len(review_rows)}")
    print(f"output_csv={report_csv.relative_to(root).as_posix()}")
    print(f"output_markdown={report_md.relative_to(root).as_posix()}")
    print(f"output_html={report_html.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, FileExistsError, ValueError) as error:
        raise SystemExit(f"ERROR: {error}")
