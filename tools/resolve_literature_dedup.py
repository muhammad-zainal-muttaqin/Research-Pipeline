#!/usr/bin/env python3
"""Resolve the exact-key deduplication review conservatively.

The first deduplication pass deliberately does not merge records whose DOI
keys differ but whose normalized title and year collide. This script applies a
reproducible second pass to that review register:

* pairs with a high author-overlap score are merged;
* a small, explicit set of metadata-variant groups is merged because their
  DOI, venue, or repository evidence shows the same publication;
* all remaining candidates are retained separately with a documented reason.

The exact-key master is preserved as an immutable derived snapshot before the
resolved working master is written.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import sys
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Iterable, Sequence


AUTHOR_MATCH_THRESHOLD = 0.75

# These groups have exact normalized title and year matches, but abbreviated,
# transliterated, repository, preprint, or URL-form DOI metadata prevents the
# generic author rule from reaching the conservative threshold.
CURATED_MERGE_GROUPS = {
    "MR-0023": "same article; DOI spelling variant and matching title/authors",
    "MR-0037": "same article; DOI PDF URL variant and matching title/authors",
    "MR-0343": "same article; DOI spelling variant and matching title/authors",
    "MR-0348": "same article; transliterated author names and repository metadata",
    "MR-0407": "same article; repository record has incomplete author metadata",
    "MR-0404": "same article; exact title/year and Scopus/OpenAlex metadata variant",
    "MR-0565": "same study version; journal and SSRN records share exact title/year",
    "MR-0594": "same article; abbreviated author names in repository metadata",
    "MR-0697": "same study version; conference and Open MIND records share exact title/year",
    "MR-0808": "same book; Scopus and open-book catalog records share exact title/year",
    "MR-0942": "same article; DOI and author-name metadata variants",
}


def clean(value: object) -> str:
    return "" if value is None else str(value).strip()


def distinct(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        value = clean(value)
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def normalize_name(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", clean(value)).casefold()
    normalized = "".join(
        char for char in normalized if not unicodedata.combining(char)
    )
    return re.sub(r"[^a-z0-9]+", "", normalized)


def author_variants(segment: str) -> set[str]:
    segment = re.sub(r"\([^)]*\)", "", clean(segment)).strip()
    if not segment:
        return set()
    if "," in segment:
        left, right = [part.strip() for part in segment.split(",", 1)]
        variants = {
            normalize_name(left),
            normalize_name(right),
            normalize_name(left + right),
            normalize_name(right + left),
        }
    else:
        tokens = [
            normalize_name(token)
            for token in re.findall(r"[A-Za-zÀ-ÿ]+", segment)
        ]
        variants = {normalize_name(segment), normalize_name("".join(tokens))}
        variants.update(token for token in tokens if len(token) >= 4)
    return {variant for variant in variants if variant}


def author_list(value: str) -> list[set[str]]:
    return [author_variants(part) for part in clean(value).split(";") if part.strip()]


def author_names_match(left: set[str], right: set[str]) -> bool:
    return any(
        value_left == value_right
        or (
            len(value_left) >= 6
            and len(value_right) >= 6
            and (value_left in value_right or value_right in value_left)
        )
        for value_left in left
        for value_right in right
    )


def pair_author_score(left: dict[str, str], right: dict[str, str]) -> float | None:
    left_authors = author_list(left.get("authors", ""))
    right_authors = author_list(right.get("authors", ""))
    if not left_authors or not right_authors:
        return None
    matched = sum(
        1
        for left_author in left_authors
        if any(author_names_match(left_author, right_author) for right_author in right_authors)
    )
    return matched / max(1, min(len(left_authors), len(right_authors)))


def union_find_components(
    ids: Sequence[str], rows_by_id: dict[str, dict[str, str]], force_all: bool
) -> list[list[str]]:
    parent = {record_id: record_id for record_id in ids}

    def find(record_id: str) -> str:
        while parent[record_id] != record_id:
            parent[record_id] = parent[parent[record_id]]
            record_id = parent[record_id]
        return record_id

    def union(left: str, right: str) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for index, left_id in enumerate(ids):
        for right_id in ids[index + 1 :]:
            score = pair_author_score(rows_by_id[left_id], rows_by_id[right_id])
            if force_all or (score is not None and score >= AUTHOR_MATCH_THRESHOLD):
                union(left_id, right_id)

    components: dict[str, list[str]] = defaultdict(list)
    for record_id in ids:
        components[find(record_id)].append(record_id)
    return sorted((sorted(component) for component in components.values()), key=lambda item: item[0])


def query_sort_key(value: str) -> tuple[int, str]:
    match = re.search(r"(\d+)$", value)
    return (int(match.group(1)) if match else 999999, value)


def source_sort_key(value: str) -> tuple[int, str]:
    return (0 if value == "Scopus" else 1, value)


def split_values(row: dict[str, str], field: str, separator: str) -> list[str]:
    return [part.strip() for part in clean(row.get(field, "")).split(separator) if part.strip()]


def choose_row(rows: Sequence[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(
        rows,
        key=lambda row: (
            0 if "Scopus" in split_values(row, "source_databases", ";") else 1,
            0 if clean(row.get("doi", "")) else 1,
            0 if clean(row.get("title", "")) else 1,
            row.get("record_id", ""),
        ),
    )


def choose_field(rows: Sequence[dict[str, str]], field: str) -> str:
    for row in choose_row(rows):
        value = clean(row.get(field, ""))
        if value:
            return value
    return ""


def combine_delimited(
    rows: Sequence[dict[str, str]], field: str, separator: str
) -> str:
    values: list[str] = []
    for row in rows:
        values.extend(split_values(row, field, separator))
    values = distinct(values)
    if field in {"source_databases"}:
        values.sort(key=source_sort_key)
    elif field in {"query_ids"}:
        values.sort(key=query_sort_key)
    elif field in {"source_query_ids"}:
        values.sort(
            key=lambda value: (
                source_sort_key(value.split(":", 1)[0]),
                query_sort_key(value.split(":", 1)[1]),
            )
        )
    else:
        values.sort()
    return separator.join(values)


def stable_merge_id(record_ids: Sequence[str]) -> str:
    material = "manual-merge|" + "|".join(sorted(record_ids))
    return "M-" + hashlib.sha1(material.encode("utf-8")).hexdigest()[:16]


def merge_screening_value(rows: Sequence[dict[str, str]], field: str) -> str:
    values = distinct(row.get(field, "") for row in rows)
    if field in {"screening_notes", "full_text_notes"}:
        return " || ".join(values)
    if len(values) == 1:
        return values[0]
    if not values:
        return ""
    return "review_required"


def merge_master_rows(
    rows: Sequence[dict[str, str]], record_ids: Sequence[str], basis: str
) -> dict[str, str]:
    ordered = choose_row(rows)
    merged = dict(ordered[0])
    merged["record_id"] = stable_merge_id(record_ids)
    merged["dedup_key"] = "manual-merge:" + merged["record_id"]
    merged["dedup_key_type"] = "manual-merge"
    merged["doi"] = choose_field(ordered, "doi")
    merged["doi_variants"] = combine_delimited(ordered, "doi_variants", ";")
    merged["title"] = choose_field(ordered, "title")
    merged["title_variants"] = combine_delimited(ordered, "title_variants", " || ")
    merged["year"] = choose_field(ordered, "year")
    merged["year_variants"] = combine_delimited(ordered, "year_variants", ";")
    merged["venue"] = choose_field(ordered, "venue")
    merged["venue_variants"] = combine_delimited(ordered, "venue_variants", " || ")
    merged["authors"] = choose_field(ordered, "authors")
    merged["author_variants"] = combine_delimited(ordered, "author_variants", " || ")

    abstract_rows = sorted(
        ordered,
        key=lambda row: (
            0 if row.get("abstract_source") == "OpenAlex" and row.get("abstract") else 1,
            0 if row.get("abstract") else 1,
        ),
    )
    merged["abstract"] = choose_field(abstract_rows, "abstract")
    merged["abstract_source"] = choose_field(abstract_rows, "abstract_source")
    merged["abstract_available"] = "yes" if merged["abstract"] else "no"
    merged["source_databases"] = combine_delimited(ordered, "source_databases", ";")
    merged["query_ids"] = combine_delimited(ordered, "query_ids", ";")
    merged["source_query_ids"] = combine_delimited(ordered, "source_query_ids", ";")
    merged["raw_files"] = combine_delimited(ordered, "raw_files", " || ")
    merged["source_row_refs"] = combine_delimited(ordered, "source_row_refs", " || ")
    merged["openalex_ids"] = combine_delimited(ordered, "openalex_ids", ";")
    merged["scopus_eids"] = combine_delimited(ordered, "scopus_eids", ";")
    merged["scopus_links"] = combine_delimited(ordered, "scopus_links", " || ")
    merged["raw_row_count"] = str(sum(int(row.get("raw_row_count", "0") or 0) for row in ordered))
    merged["unique_source_query_records"] = str(
        sum(int(row.get("unique_source_query_records", "0") or 0) for row in ordered)
    )
    merged["within_duplicate_rows"] = str(
        sum(int(row.get("within_duplicate_rows", "0") or 0) for row in ordered)
    )
    merged["cross_source_merged"] = (
        "yes" if len(split_values(merged, "source_databases", ";")) > 1 else "no"
    )
    merged["cross_query_merged"] = (
        "yes" if len(split_values(merged, "query_ids", ";")) > 1 else "no"
    )
    merged["manual_review_flag"] = "no"
    flags: list[str] = []
    if not merged["title"]:
        flags.append("missing_title")
    if not merged["abstract"]:
        flags.append("missing_abstract")
    if not merged["year"]:
        flags.append("missing_year")
    if merged.get("year_window_flag"):
        flags.append(merged["year_window_flag"])
    merged["metadata_flags"] = ";".join(distinct(flags))
    for field in (
        "title_abstract_screen",
        "screen_exclusion_code",
        "screening_notes",
        "full_text_status",
        "full_text_exclusion_code",
        "full_text_notes",
        "final_inclusion",
    ):
        merged[field] = merge_screening_value(ordered, field)
    merged["dedup_resolution"] = "merge"
    merged["merged_from_record_ids"] = ";".join(sorted(record_ids))
    merged["resolution_basis"] = basis
    return merged


def write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        return fields, [dict(row) for row in reader]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--force", action="store_true", help="replace resolved outputs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    derived = root / "literature" / "search" / "derived"
    primary_master = derived / f"master-screening-{args.run_date}.csv"
    exact_master = derived / f"master-screening-exact-key-{args.run_date}.csv"
    review_path = derived / f"manual-dedup-review-{args.run_date}.csv"
    exact_prisma = root / "literature" / "search" / f"prisma-counts-exact-key-{args.run_date}.csv"
    primary_prisma = root / "literature" / "search" / "prisma-counts.csv"
    resolved_master = derived / f"master-screening-resolved-{args.run_date}.csv"
    resolved_review_path = derived / f"manual-dedup-review-resolved-{args.run_date}.csv"
    resolution_path = derived / f"dedup-resolution-{args.run_date}.csv"

    if not primary_master.exists() or not review_path.exists() or not primary_prisma.exists():
        raise FileNotFoundError("The exact-key master, review, and PRISMA files are required")
    if exact_master.exists():
        input_master = exact_master
    else:
        shutil.copyfile(primary_master, exact_master)
        input_master = exact_master
    if exact_prisma.exists():
        input_prisma = exact_prisma
    else:
        shutil.copyfile(primary_prisma, exact_prisma)
        input_prisma = exact_prisma

    outputs = [resolved_master, resolved_review_path, resolution_path]
    if any(path.exists() for path in outputs) and not args.force:
        names = ", ".join(str(path.relative_to(root)) for path in outputs if path.exists())
        raise FileExistsError(f"Resolved outputs already exist: {names}")

    master_fields, master_rows = read_csv(input_master)
    review_fields, review_rows = read_csv(review_path)
    prisma_fields, prisma_rows = read_csv(input_prisma)
    rows_by_id = {row["record_id"]: row for row in master_rows}
    if len(rows_by_id) != len(master_rows):
        raise ValueError("Master record_id values are not unique")

    group_for_record: dict[str, str] = {}
    component_records: list[tuple[list[str], str]] = []
    resolution_rows: list[dict[str, str]] = []
    resolved_review_rows: list[dict[str, str]] = []

    for review in review_rows:
        review_id = review["review_id"]
        record_ids = sorted(record_id for record_id in review["candidate_record_ids"].split(";") if record_id)
        if not record_ids or any(record_id not in rows_by_id for record_id in record_ids):
            raise ValueError(f"{review_id}: candidate record id is missing from master")
        if any(record_id in group_for_record for record_id in record_ids):
            raise ValueError(f"Record appears in more than one manual review group: {review_id}")
        for record_id in record_ids:
            group_for_record[record_id] = review_id

        force_all = review_id in CURATED_MERGE_GROUPS
        components = union_find_components(record_ids, rows_by_id, force_all)
        merged_components = [component for component in components if len(component) > 1]
        if force_all:
            decision = "merge_all_curated"
            basis = CURATED_MERGE_GROUPS[review_id]
        elif merged_components and len(merged_components) == 1 and len(components) == 1:
            decision = "merge_all_author_match"
            basis = "same normalized title/year and pairwise author overlap >= 0.75"
        elif merged_components:
            decision = "partial_merge_author_match"
            basis = "merge only author-matched components; retain other candidates separately"
        else:
            decision = "keep_separate_conservative"
            if any(not clean(rows_by_id[record_id].get("authors", "")) for record_id in record_ids):
                basis = "insufficient author metadata; retained separately"
            else:
                basis = "author or publication metadata differs below the merge threshold"

        evidence_scores: list[str] = []
        for index, left_id in enumerate(record_ids):
            for right_id in record_ids[index + 1 :]:
                score = pair_author_score(rows_by_id[left_id], rows_by_id[right_id])
                evidence_scores.append(
                    f"{left_id}:{right_id}=" + ("NA" if score is None else f"{score:.3f}")
                )
        component_text = " | ".join("+".join(component) for component in components)
        resolution_rows.append(
            {
                "review_id": review_id,
                "candidate_record_ids": ";".join(record_ids),
                "decision": decision,
                "resolved_components": component_text,
                "candidate_count": str(len(record_ids)),
                "merged_component_count": str(len(merged_components)),
                "author_pair_scores": ";".join(evidence_scores),
                "resolution_basis": basis,
                "reviewer_notes": "Generated from local title, year, author, venue, DOI, and provenance fields.",
            }
        )
        resolved_review_row = dict(review)
        resolved_review_row["resolution"] = decision
        resolved_review_row["reviewer_notes"] = basis
        resolved_review_rows.append(resolved_review_row)

        for component in merged_components:
            component_records.append((component, basis))

    resolved_rows: list[dict[str, str]] = []
    consumed: set[str] = set()
    for record_ids, basis in component_records:
        resolved_rows.append(
            merge_master_rows(
                [rows_by_id[record_id] for record_id in record_ids], record_ids, basis
            )
        )
        consumed.update(record_ids)

    for row in master_rows:
        record_id = row["record_id"]
        if record_id in consumed:
            continue
        copy = dict(row)
        if record_id in group_for_record:
            review_id = group_for_record[record_id]
            decision_row = next(item for item in resolution_rows if item["review_id"] == review_id)
            copy["dedup_resolution"] = "keep_separate"
            copy["merged_from_record_ids"] = record_id
            copy["resolution_basis"] = decision_row["resolution_basis"]
            copy["manual_review_flag"] = "no"
            copy["metadata_flags"] = ";".join(
                value
                for value in distinct(copy.get("metadata_flags", "").split(";"))
                if value != "manual_dedup_review"
            )
        else:
            copy["dedup_resolution"] = "not_applicable"
            copy["merged_from_record_ids"] = record_id
            copy["resolution_basis"] = "no exact normalized title/year collision across distinct DOI keys"
        resolved_rows.append(copy)

    master_output_fields = list(master_fields)
    for field in ("dedup_resolution", "merged_from_record_ids", "resolution_basis"):
        if field not in master_output_fields:
            master_output_fields.append(field)
    resolved_rows.sort(key=lambda row: (row.get("title", "").casefold(), row.get("year", ""), row["record_id"]))

    membership: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in resolved_rows:
        for source_query in split_values(row, "source_query_ids", ";"):
            database, query_id = source_query.split(":", 1)
            membership[(database, query_id)].add(row["record_id"])

    for row in prisma_rows:
        query_id = row.get("query_id", "")
        database = row.get("database", "")
        if query_id == "ALL":
            row["n_dedup_across"] = str(len(resolved_rows))
            row["notes"] = "Union after exact-key deduplication plus conservative manual conflict resolution; screening fields are pending."
        else:
            row["n_dedup_across"] = str(len(membership[(database, query_id)]))
            row["notes"] = "Distinct resolved master records represented by this query; per-query values are not additive because queries overlap."

    write_csv(resolution_path, [
        "review_id",
        "candidate_record_ids",
        "decision",
        "resolved_components",
        "candidate_count",
        "merged_component_count",
        "author_pair_scores",
        "resolution_basis",
        "reviewer_notes",
    ], resolution_rows)
    write_csv(resolved_review_path, review_fields, resolved_review_rows)
    write_csv(resolved_master, master_output_fields, resolved_rows)
    shutil.copyfile(resolved_master, primary_master)
    write_csv(primary_prisma, prisma_fields, prisma_rows)

    merged_components_count = len(component_records)
    merged_reduction = sum(len(record_ids) - 1 for record_ids, _ in component_records)
    kept_groups = sum(1 for row in resolution_rows if row["decision"] == "keep_separate_conservative")
    partial_groups = sum(1 for row in resolution_rows if row["decision"] == "partial_merge_author_match")
    curated_groups = sum(1 for row in resolution_rows if row["decision"] == "merge_all_curated")
    print(f"exact_master_records={len(master_rows)}")
    print(f"resolved_master_records={len(resolved_rows)}")
    print(f"merged_components={merged_components_count}")
    print(f"merged_reduction={merged_reduction}")
    print(f"curated_merge_groups={curated_groups}")
    print(f"partial_merge_groups={partial_groups}")
    print(f"kept_separate_groups={kept_groups}")
    print(f"resolution_output={resolution_path.relative_to(root).as_posix()}")
    print(f"resolved_master_output={resolved_master.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, FileExistsError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
