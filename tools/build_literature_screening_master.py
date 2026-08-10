#!/usr/bin/env python3
"""Build reproducible deduplication and screening registers from raw exports.

The raw Scopus and OpenAlex CSV files are inputs only. This script creates
derived audit, review, master-screening, and PRISMA count files. It performs
exact DOI matching first and uses normalized title plus year only when a DOI is
absent. Potential collisions where the same normalized title and year map to
more than one deduplication key are reported for manual review and are not
merged automatically.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Sequence


MISSING_VALUES = {"", "-", "na", "n/a", "none", "null", "not available"}
SCOPUS_HEADER = {"Title", "Year", "DOI", "EID"}
OPENALEX_HEADER = {"query_id", "openalex_id", "doi", "year", "title"}
YEAR_MIN = 2015
YEAR_MAX = 2026


@dataclass(frozen=True)
class SourceRecord:
    database: str
    query_id: str
    raw_file: Path
    row_number: int
    doi_raw: str
    doi: str
    title: str
    title_normalized: str
    year_raw: str
    year: str
    venue: str
    authors: str
    abstract: str
    openalex_id: str
    scopus_eid: str
    scopus_link: str
    dedup_key: str
    dedup_key_type: str


@dataclass(frozen=True)
class WithinCluster:
    database: str
    query_id: str
    dedup_key: str
    dedup_key_type: str
    records: tuple[SourceRecord, ...]

    @property
    def canonical(self) -> SourceRecord:
        return sorted(self.records, key=record_preference)[0]


def clean(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def first_value(row: dict[str, str], *names: str) -> str:
    for name in names:
        value = clean(row.get(name, ""))
        if value:
            return value
    return ""


def normalize_doi(value: str) -> str:
    """Return a stable DOI key, or an empty string for a missing DOI."""

    normalized = unicodedata.normalize("NFKC", clean(value)).casefold()
    normalized = normalized.strip().strip("<>\"'")
    normalized = re.sub(r"^https?://(?:www\.)?(?:dx\.)?doi\.org/", "", normalized)
    normalized = re.sub(r"^doi:\s*", "", normalized)
    normalized = normalized.split("?", 1)[0].split("#", 1)[0]
    normalized = re.sub(r"\s+", "", normalized)
    normalized = normalized.rstrip(".,;:]}>'\"")
    if normalized in MISSING_VALUES:
        return ""
    if not normalized.startswith("10.") or "/" not in normalized:
        return ""
    return normalized


def normalize_title(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", clean(value)).casefold()
    return "".join(
        char
        for char in normalized
        if not unicodedata.combining(char) and char.isalnum()
    )


def normalize_year(value: str) -> str:
    match = re.search(r"\b((?:19|20)\d{2})\b", clean(value))
    return match.group(1) if match else ""


def query_sort_key(query_id: str) -> tuple[int, str]:
    match = re.search(r"(\d+)$", query_id)
    return (int(match.group(1)) if match else 999999, query_id)


def database_sort_key(database: str) -> tuple[int, str]:
    return (0 if database == "Scopus" else 1, database)


def record_preference(record: SourceRecord) -> tuple[int, int, int, int, str]:
    """Prefer Scopus metadata, then DOI-bearing and information-rich rows."""

    return (
        database_sort_key(record.database)[0],
        0 if record.doi else 1,
        0 if record.title else 1,
        0 if record.abstract else 1,
        record.row_number,
    )


def distinct(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        value = clean(value)
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def join_distinct(values: Iterable[str], separator: str = "; ") -> str:
    return separator.join(distinct(values))


def relative_path(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def query_id_from_filename(path: Path, database: str) -> str:
    pattern = rf"^{database.lower()}_(Q\d+)_.*\.csv$"
    match = re.match(pattern, path.name, re.IGNORECASE)
    if not match:
        raise ValueError(f"Cannot infer query id from {path.name}")
    return match.group(1).upper()


def read_csv_rows(path: Path, required_header: set[str]) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        header = set(reader.fieldnames or [])
        missing = sorted(required_header - header)
        if missing:
            raise ValueError(f"{path}: missing columns: {', '.join(missing)}")
        return [dict(row) for row in reader]


def build_scopus_record(
    row: dict[str, str], path: Path, query_id: str, row_number: int
) -> SourceRecord:
    doi_raw = first_value(row, "DOI")
    doi = normalize_doi(doi_raw)
    title = first_value(row, "Title")
    title_normalized = normalize_title(title)
    year_raw = first_value(row, "Year")
    year = normalize_year(year_raw)
    key, key_type = make_dedup_key(
        "Scopus", query_id, row_number, doi, title_normalized, year
    )
    return SourceRecord(
        database="Scopus",
        query_id=query_id,
        raw_file=path,
        row_number=row_number,
        doi_raw=doi_raw,
        doi=doi,
        title=title,
        title_normalized=title_normalized,
        year_raw=year_raw,
        year=year,
        venue=first_value(row, "Source title"),
        authors=first_value(row, "Author full names", "Authors"),
        abstract="",
        openalex_id="",
        scopus_eid=first_value(row, "EID"),
        scopus_link=first_value(row, "Link"),
        dedup_key=key,
        dedup_key_type=key_type,
    )


def build_openalex_record(
    row: dict[str, str], path: Path, query_id: str, row_number: int
) -> SourceRecord:
    doi_raw = first_value(row, "doi")
    doi = normalize_doi(doi_raw)
    title = first_value(row, "title")
    title_normalized = normalize_title(title)
    year_raw = first_value(row, "year")
    year = normalize_year(year_raw)
    key, key_type = make_dedup_key(
        "OpenAlex", query_id, row_number, doi, title_normalized, year
    )
    return SourceRecord(
        database="OpenAlex",
        query_id=query_id,
        raw_file=path,
        row_number=row_number,
        doi_raw=doi_raw,
        doi=doi,
        title=title,
        title_normalized=title_normalized,
        year_raw=year_raw,
        year=year,
        venue=first_value(row, "venue"),
        authors=first_value(row, "authors"),
        abstract=first_value(row, "abstract"),
        openalex_id=first_value(row, "openalex_id"),
        scopus_eid="",
        scopus_link="",
        dedup_key=key,
        dedup_key_type=key_type,
    )


def make_dedup_key(
    database: str,
    query_id: str,
    row_number: int,
    doi: str,
    title_normalized: str,
    year: str,
) -> tuple[str, str]:
    if doi:
        return f"doi:{doi}", "doi"
    if title_normalized and year:
        return f"titleyear:{title_normalized}|{year}", "titleyear"
    return f"source-row:{database}:{query_id}:{row_number}", "source-row"


def source_records_from_files(
    root: Path, database: str, paths: Sequence[Path]
) -> tuple[dict[tuple[str, str], list[SourceRecord]], dict[tuple[str, str], Path]]:
    records_by_arm: dict[tuple[str, str], list[SourceRecord]] = defaultdict(list)
    file_by_arm: dict[tuple[str, str], Path] = {}
    required_header = SCOPUS_HEADER if database == "Scopus" else OPENALEX_HEADER
    builder = build_scopus_record if database == "Scopus" else build_openalex_record
    for path in paths:
        query_id = query_id_from_filename(path, database)
        arm = (database, query_id)
        if arm in file_by_arm:
            raise ValueError(f"More than one {database} file found for {query_id}")
        file_by_arm[arm] = path
        rows = read_csv_rows(path, required_header)
        if database == "OpenAlex":
            row_query_ids = {
                first_value(row, "query_id")
                for row in rows
                if first_value(row, "query_id")
            }
            if row_query_ids and row_query_ids != {query_id}:
                raise ValueError(
                    f"{path}: query_id column does not match filename: {sorted(row_query_ids)}"
                )
        records_by_arm[arm].extend(
            builder(row, path, query_id, row_number)
            for row_number, row in enumerate(rows, start=1)
        )
    return records_by_arm, file_by_arm


def make_within_clusters(
    records_by_arm: dict[tuple[str, str], list[SourceRecord]]
) -> tuple[list[WithinCluster], dict[tuple[str, str], list[WithinCluster]]]:
    all_clusters: list[WithinCluster] = []
    clusters_by_arm: dict[tuple[str, str], list[WithinCluster]] = defaultdict(list)
    for arm in sorted(
        records_by_arm, key=lambda item: (database_sort_key(item[0]), query_sort_key(item[1]))
    ):
        grouped: dict[str, list[SourceRecord]] = defaultdict(list)
        for record in records_by_arm[arm]:
            grouped[record.dedup_key].append(record)
        for dedup_key in sorted(grouped):
            records = tuple(sorted(grouped[dedup_key], key=lambda item: item.row_number))
            cluster = WithinCluster(
                database=arm[0],
                query_id=arm[1],
                dedup_key=dedup_key,
                dedup_key_type=records[0].dedup_key_type,
                records=records,
            )
            all_clusters.append(cluster)
            clusters_by_arm[arm].append(cluster)
    return all_clusters, clusters_by_arm


def record_id_for_key(dedup_key: str) -> str:
    digest = hashlib.sha1(dedup_key.encode("utf-8")).hexdigest()[:16]
    return f"R-{digest}"


def year_window_flag(year: str) -> str:
    if not year:
        return "missing_year"
    numeric_year = int(year)
    if numeric_year < YEAR_MIN or numeric_year > YEAR_MAX:
        return f"outside_{YEAR_MIN}_{YEAR_MAX}"
    return ""


def choose_field(records: Sequence[SourceRecord], field_name: str) -> str:
    for record in sorted(records, key=record_preference):
        value = clean(getattr(record, field_name))
        if value:
            return value
    return ""


def choose_abstract(records: Sequence[SourceRecord]) -> tuple[str, str]:
    ranked = sorted(
        records,
        key=lambda record: (
            0 if record.database == "OpenAlex" and record.abstract else 1,
            *record_preference(record),
        ),
    )
    for record in ranked:
        if record.abstract:
            return record.abstract, record.database
    return "", ""


def make_conflict_reviews(
    all_records: Sequence[SourceRecord],
    root: Path,
) -> tuple[list[dict[str, str]], set[str]]:
    title_year_keys: dict[tuple[str, str], set[str]] = defaultdict(set)
    for record in all_records:
        if record.title_normalized and record.year:
            title_year_keys[(record.title_normalized, record.year)].add(record.dedup_key)

    conflict_keys: set[str] = set()
    review_rows: list[dict[str, str]] = []
    review_number = 0
    by_key: dict[str, list[SourceRecord]] = defaultdict(list)
    for record in all_records:
        by_key[record.dedup_key].append(record)

    for (title_normalized, year), keys in sorted(title_year_keys.items()):
        if len(keys) < 2:
            continue
        review_number += 1
        ordered_keys = sorted(keys)
        conflict_keys.update(ordered_keys)
        candidate_records = [by_key[key] for key in ordered_keys]
        flattened = [record for records in candidate_records for record in records]
        titles = distinct(record.title for record in flattened)
        dois = distinct(record.doi for record in flattened)
        refs = sorted(
            source_ref(record, root)
            for record in flattened
        )
        candidate_ids = [record_id_for_key(key) for key in ordered_keys]
        review_rows.append(
            {
                "review_id": f"MR-{review_number:04d}",
                "normalized_title": title_normalized,
                "year": year,
                "candidate_record_ids": ";".join(candidate_ids),
                "candidate_dedup_keys": " || ".join(ordered_keys),
                "candidate_dois": ";".join(dois),
                "candidate_titles": " || ".join(titles),
                "source_row_refs": " || ".join(refs),
                "reason": "same normalized title and year mapped to multiple dedup keys",
                "resolution": "",
                "reviewer_notes": "",
            }
        )
    return review_rows, conflict_keys


def source_ref(record: SourceRecord, root: Path) -> str:
    return f"{record.database}|{record.query_id}|{relative_path(record.raw_file, root)}|row={record.row_number}"


def make_master_row(
    dedup_key: str,
    clusters: Sequence[WithinCluster],
    conflict_keys: set[str],
    root: Path,
) -> dict[str, str]:
    records = [record for cluster in clusters for record in cluster.records]
    canonical = sorted(records, key=record_preference)[0]
    abstract, abstract_source = choose_abstract(records)
    databases = distinct(
        database
        for database in sorted(
            {record.database for record in records}, key=database_sort_key
        )
    )
    query_ids = sorted({record.query_id for record in records}, key=query_sort_key)
    source_query_ids = sorted(
        {f"{record.database}:{record.query_id}" for record in records},
        key=lambda value: (database_sort_key(value.split(":", 1)[0]), query_sort_key(value.split(":", 1)[1])),
    )
    raw_files = sorted(
        distinct(relative_path(record.raw_file, root) for record in records)
    )
    source_refs = sorted(source_ref(record, root) for record in records)
    years = distinct(record.year_raw or record.year for record in records)
    title_variants = distinct(record.title for record in records)
    venue_variants = distinct(record.venue for record in records)
    author_variants = distinct(record.authors for record in records)
    dois = distinct(record.doi for record in records)
    openalex_ids = distinct(record.openalex_id for record in records)
    scopus_eids = distinct(record.scopus_eid for record in records)
    scopus_links = distinct(record.scopus_link for record in records)
    within_duplicate_rows = sum(len(cluster.records) - 1 for cluster in clusters)
    title = choose_field(records, "title")
    year = choose_field(records, "year")
    flags: list[str] = []
    if not title:
        flags.append("missing_title")
    if not abstract:
        flags.append("missing_abstract")
    if not year:
        flags.append("missing_year")
    if year_window_flag(year):
        flags.append(year_window_flag(year))
    if dedup_key in conflict_keys:
        flags.append("manual_dedup_review")
    return {
        "record_id": record_id_for_key(dedup_key),
        "dedup_key": dedup_key,
        "dedup_key_type": canonical.dedup_key_type,
        "doi": choose_field(records, "doi"),
        "doi_variants": ";".join(dois),
        "title": title,
        "title_variants": " || ".join(title_variants),
        "year": year,
        "year_variants": ";".join(years),
        "year_window_flag": year_window_flag(choose_field(records, "year")),
        "venue": choose_field(records, "venue"),
        "venue_variants": " || ".join(venue_variants),
        "authors": choose_field(records, "authors"),
        "author_variants": " || ".join(author_variants),
        "abstract": abstract,
        "abstract_source": abstract_source,
        "abstract_available": "yes" if abstract else "no",
        "source_databases": ";".join(databases),
        "query_ids": ";".join(query_ids),
        "source_query_ids": ";".join(source_query_ids),
        "raw_files": " || ".join(raw_files),
        "source_row_refs": " || ".join(source_refs),
        "openalex_ids": ";".join(openalex_ids),
        "scopus_eids": ";".join(scopus_eids),
        "scopus_links": " || ".join(scopus_links),
        "raw_row_count": str(len(records)),
        "unique_source_query_records": str(len(clusters)),
        "within_duplicate_rows": str(within_duplicate_rows),
        "cross_source_merged": "yes" if len(databases) > 1 else "no",
        "cross_query_merged": "yes" if len(query_ids) > 1 else "no",
        "manual_review_flag": "yes" if dedup_key in conflict_keys else "no",
        "metadata_flags": ";".join(flags),
        "title_abstract_screen": "pending",
        "screen_exclusion_code": "",
        "screening_notes": "",
        "full_text_status": "pending",
        "full_text_exclusion_code": "",
        "full_text_notes": "",
        "final_inclusion": "pending",
    }


MASTER_FIELDS = [
    "record_id",
    "dedup_key",
    "dedup_key_type",
    "doi",
    "doi_variants",
    "title",
    "title_variants",
    "year",
    "year_variants",
    "year_window_flag",
    "venue",
    "venue_variants",
    "authors",
    "author_variants",
    "abstract",
    "abstract_source",
    "abstract_available",
    "source_databases",
    "query_ids",
    "source_query_ids",
    "raw_files",
    "source_row_refs",
    "openalex_ids",
    "scopus_eids",
    "scopus_links",
    "raw_row_count",
    "unique_source_query_records",
    "within_duplicate_rows",
    "cross_source_merged",
    "cross_query_merged",
    "manual_review_flag",
    "metadata_flags",
    "title_abstract_screen",
    "screen_exclusion_code",
    "screening_notes",
    "full_text_status",
    "full_text_exclusion_code",
    "full_text_notes",
    "final_inclusion",
]


AUDIT_FIELDS = [
    "database",
    "query_id",
    "date_run",
    "raw_file",
    "raw_sha256",
    "n_raw",
    "n_unique_after_within_dedup",
    "n_duplicates_within_query",
    "n_missing_doi",
    "n_missing_title_or_year",
    "n_year_outside_2015_2026",
    "n_global_records_present",
    "n_cross_source_records_present",
]


PRISMA_FIELDS = [
    "query_id",
    "database",
    "date_run",
    "n_raw",
    "n_dedup_within",
    "n_dedup_across",
    "n_screened",
    "n_excl_EC1",
    "n_excl_EC2",
    "n_excl_EC3",
    "n_excl_EC4",
    "n_excl_EC5",
    "n_excl_EC6",
    "n_fulltext_sought",
    "n_retrieved",
    "n_included",
    "notes",
]


REVIEW_FIELDS = [
    "review_id",
    "normalized_title",
    "year",
    "candidate_record_ids",
    "candidate_dedup_keys",
    "candidate_dois",
    "candidate_titles",
    "source_row_refs",
    "reason",
    "resolution",
    "reviewer_notes",
]


def write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=date.today().isoformat())
    parser.add_argument("--scopus-date", default="2026-08-09")
    parser.add_argument("--openalex-date", default="2026-07-23")
    parser.add_argument("--force", action="store_true", help="replace existing derived files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    scopus_dir = root / "literature" / "search" / "raw"
    openalex_dir = root / "literature" / "search-data" / "raw"
    derived_dir = root / "literature" / "search" / "derived"
    prisma_path = root / "literature" / "search" / "prisma-counts.csv"

    scopus_paths = sorted(scopus_dir.glob(f"scopus_Q*_{args.scopus_date}.csv"))
    openalex_paths = sorted(openalex_dir.glob(f"openalex_Q*_{args.openalex_date}.csv"))
    if not scopus_paths or not openalex_paths:
        raise FileNotFoundError("Expected Scopus and OpenAlex raw exports were not found")

    outputs = [
        derived_dir / f"dedup-audit-{args.run_date}.csv",
        derived_dir / f"manual-dedup-review-{args.run_date}.csv",
        derived_dir / f"master-screening-{args.run_date}.csv",
        prisma_path,
    ]
    existing = [path for path in outputs if path.exists()]
    if existing and not args.force:
        names = ", ".join(str(path.relative_to(root)) for path in existing)
        raise FileExistsError(
            f"Derived outputs already exist: {names}. Use --force only after reviewing them."
        )

    scopus_records, scopus_files = source_records_from_files(root, "Scopus", scopus_paths)
    openalex_records, openalex_files = source_records_from_files(root, "OpenAlex", openalex_paths)
    records_by_arm: dict[tuple[str, str], list[SourceRecord]] = {}
    records_by_arm.update(scopus_records)
    records_by_arm.update(openalex_records)
    file_by_arm = {}
    file_by_arm.update(scopus_files)
    file_by_arm.update(openalex_files)

    all_records = [record for records in records_by_arm.values() for record in records]
    all_clusters, clusters_by_arm = make_within_clusters(records_by_arm)
    global_clusters: dict[str, list[WithinCluster]] = defaultdict(list)
    for cluster in all_clusters:
        global_clusters[cluster.dedup_key].append(cluster)

    review_rows, conflict_keys = make_conflict_reviews(all_records, root)
    master_rows = [
        make_master_row(key, global_clusters[key], conflict_keys, root)
        for key in sorted(global_clusters)
    ]
    master_rows.sort(key=lambda row: (row["title"].casefold(), row["year"], row["record_id"]))

    audit_rows: list[dict[str, str]] = []
    prisma_rows: list[dict[str, str]] = []
    global_membership: dict[tuple[str, str], set[str]] = defaultdict(set)
    cross_source_membership: dict[tuple[str, str], set[str]] = defaultdict(set)
    for key, clusters in global_clusters.items():
        databases = {cluster.database for cluster in clusters}
        for cluster in clusters:
            arm = (cluster.database, cluster.query_id)
            global_membership[arm].add(key)
            if len(databases) > 1:
                cross_source_membership[arm].add(key)

    for arm in sorted(
        records_by_arm, key=lambda item: (database_sort_key(item[0]), query_sort_key(item[1]))
    ):
        records = records_by_arm[arm]
        clusters = clusters_by_arm[arm]
        missing_doi = sum(1 for record in records if not record.doi)
        missing_title_or_year = sum(
            1 for record in records if not record.title_normalized or not record.year
        )
        outside_year = sum(
            1
            for record in records
            if record.year and (int(record.year) < YEAR_MIN or int(record.year) > YEAR_MAX)
        )
        n_raw = len(records)
        n_within = len(clusters)
        n_duplicates = n_raw - n_within
        n_global = len(global_membership[arm])
        n_cross_source = len(cross_source_membership[arm])
        raw_file = relative_path(file_by_arm[arm], root)
        audit_rows.append(
            {
                "database": arm[0],
                "query_id": arm[1],
                "date_run": args.run_date,
                "raw_file": raw_file,
                "raw_sha256": sha256_file(file_by_arm[arm]),
                "n_raw": str(n_raw),
                "n_unique_after_within_dedup": str(n_within),
                "n_duplicates_within_query": str(n_duplicates),
                "n_missing_doi": str(missing_doi),
                "n_missing_title_or_year": str(missing_title_or_year),
                "n_year_outside_2015_2026": str(outside_year),
                "n_global_records_present": str(n_global),
                "n_cross_source_records_present": str(n_cross_source),
            }
        )
        prisma_rows.append(
            {
                "query_id": arm[1],
                "database": arm[0],
                "date_run": args.run_date,
                "n_raw": str(n_raw),
                "n_dedup_within": str(n_within),
                "n_dedup_across": str(n_global),
                "n_screened": "",
                "n_excl_EC1": "",
                "n_excl_EC2": "",
                "n_excl_EC3": "",
                "n_excl_EC4": "",
                "n_excl_EC5": "",
                "n_excl_EC6": "",
                "n_fulltext_sought": "",
                "n_retrieved": "",
                "n_included": "",
                "notes": "n_dedup_across is distinct master records represented by this query; per-query values are not additive because queries overlap.",
            }
        )

    total_raw = sum(int(row["n_raw"]) for row in audit_rows)
    total_within = sum(int(row["n_unique_after_within_dedup"]) for row in audit_rows)
    cross_source_count = sum(
        1 for row in master_rows if row["cross_source_merged"] == "yes"
    )
    prisma_rows.append(
        {
            "query_id": "ALL",
            "database": "Scopus+OpenAlex",
            "date_run": args.run_date,
            "n_raw": str(total_raw),
            "n_dedup_within": str(total_within),
            "n_dedup_across": str(len(master_rows)),
            "n_screened": "",
            "n_excl_EC1": "",
            "n_excl_EC2": "",
            "n_excl_EC3": "",
            "n_excl_EC4": "",
            "n_excl_EC5": "",
            "n_excl_EC6": "",
            "n_fulltext_sought": "",
            "n_retrieved": "",
            "n_included": "",
            "notes": "Union across all Scopus/OpenAlex queries after within-query and across-source deduplication; screening fields are pending.",
        }
    )

    write_csv(derived_dir / f"dedup-audit-{args.run_date}.csv", AUDIT_FIELDS, audit_rows)
    write_csv(derived_dir / f"manual-dedup-review-{args.run_date}.csv", REVIEW_FIELDS, review_rows)
    write_csv(derived_dir / f"master-screening-{args.run_date}.csv", MASTER_FIELDS, master_rows)
    write_csv(prisma_path, PRISMA_FIELDS, prisma_rows)

    print(f"raw_rows={total_raw}")
    print(f"within_unique_rows={total_within}")
    print(f"within_duplicate_rows={total_raw - total_within}")
    print(f"master_records={len(master_rows)}")
    print(f"cross_source_merged_records={cross_source_count}")
    print(f"manual_review_groups={len(review_rows)}")
    print(f"master_pending_screening={sum(1 for row in master_rows if row['title_abstract_screen'] == 'pending')}")
    print(f"output_master={relative_path(derived_dir / f'master-screening-{args.run_date}.csv', root)}")
    print(f"output_prisma={relative_path(prisma_path, root)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, FileExistsError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
