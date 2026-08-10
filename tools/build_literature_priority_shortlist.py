#!/usr/bin/env python3
"""Rank and diversify the retained literature candidates.

The 20,035 records retained after title and abstract screening are a search
pool, not a promise to read 20,035 papers in full.  This tool assigns a
transparent title/abstract relevance score, creates a complete ranked queue,
and selects a diverse shortlist for targeted full-text review.

The score is a triage aid.  It is not an inclusion decision and must not be
used to silently delete a candidate from the search record.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = ROOT / "literature/search/derived/abstract-screening-2026-08-10.csv"
DEFAULT_MASTER = ROOT / "literature/search/derived/master-screening-2026-08-09.csv"
DEFAULT_LEDGER = ROOT / "literature/search/derived/fulltext-review-ledger-2026-08-10.csv"
DEFAULT_RANKING = ROOT / "literature/search/derived/priority-ranking-2026-08-10.csv"
DEFAULT_SHORTLIST = ROOT / "literature/search/derived/priority-shortlist-2026-08-10.csv"
DEFAULT_SUMMARY = ROOT / "literature/search/derived/priority-selection-summary-2026-08-10.csv"
DEFAULT_REPORT = ROOT / "literature/search/derived/priority-selection-method-2026-08-10.md"
DEFAULT_HTML = ROOT / "literature/search/derived/priority-shortlist-2026-08-10.html"
DEFAULT_WAVE = ROOT / "literature/search/derived/priority-review-wave1-2026-08-10.csv"

RULE_VERSION = "priority-v1.0-title-abstract-scored-diversified"


@dataclass(frozen=True)
class Signal:
    pattern: re.Pattern[str]
    label: str
    weight: int


def signals(items: Iterable[tuple[str, str, int]]) -> tuple[Signal, ...]:
    return tuple(Signal(re.compile(pattern, re.I), label, weight) for pattern, label, weight in items)


# The first group is the central design problem: associating observations so
# that a fruit is counted once.  Individual weak terms are deliberately given
# lower weights than explicit identity or duplicate-resolution language.
CORE_SIGNALS = signals(
    [
        (r"\bunique\s+(?:fruit|count|inventory|instance|item)s?\b", "unique inventory", 42),
        (r"\b(?:duplicate|dedup(?:lication)?|de[-\s]?duplicate|double[-\s]?count)\w*\b", "duplicate resolution", 38),
        (r"\b(?:re[-\s]?identification|reidentification|re[-\s]?id|fruit\s+identity|instance\s+identity)\b", "re-identification", 40),
        (r"\b(?:cross[-\s]?view|cross[-\s]?observation|same\s+fruit|same\s+object|multi[-\s]?view|multiple[-\s]?view|multi[-\s]?camera)\b", "cross-view association", 30),
        (r"\b(?:data\s+association|feature\s+correspondence|correspondence\s+matching|assignment\s+problem)\b", "association", 28),
        (r"\b(?:multi[-\s]?object\s+tracking|object\s+tracking|fruit\s+tracking|visual\s+tracking|persistent\s+id|id[-\s]?switch|hota|mota|idf1|tracklet)\b", "tracking identity", 27),
        (r"\b(?:structure\s+from\s+motion|\bsfm\b|multi[-\s]?view\s+stereo|\bmvs\b|stereo\s+vision|photogrammetr\w*|3d\s+reconstruction|three[-\s]?dimensional\s+reconstruction)\b", "3D reconstruction", 24),
        (r"\b(?:point\s+cloud|rgb[-\s]?d|depth\s+camera|depth\s+map|lidar|gaussian\s+splatting|nerf|nerfacto)\b", "depth or point cloud", 22),
        (r"\b(?:count(?:ing)?|enumerat(?:e|ion|ing)|inventory|census)\b", "counting or inventory", 12),
    ]
)

FRUIT_SIGNALS = signals(
    [
        (r"\b(?:fruit|fruitlet|berry|berries|pod|bunch|cluster|apple|mango|citrus|orange|grape|tomato|strawberr(?:y|ies)|blueberr(?:y|ies)|pineapple|banana|peach|pear|cherry|kiwi|guava|pomegranate)\b", "fruit target", 22),
        (r"\b(?:orchard|vineyard|greenhouse|plantation|horticultur\w*|fruit\s+tree|tree\s+crop)\b", "horticultural setting", 10),
        (r"\b(?:detect\w*|segment\w*|locali[sz]\w*|recogn\w*|count\w*|track\w*)\b.{0,70}\b(?:fruit|fruitlet|berry|bunch|cluster|apple|mango|citrus|orange|grape|tomato|strawberr\w*|oil\s+palm|ffb)\b", "fruit instance operation", 24),
    ]
)

OIL_PALM_SIGNALS = signals(
    [
        (r"\b(?:oil\s+palm|palm\s+oil|fresh\s+fruit\s+bunch(?:es)?|\bffb\b|tandan\s+buah|kelapa\s+sawit|elaeis\s+guineensis)\b", "oil-palm target", 36),
        (r"\b(?:ripeness|matur\w*|ripe|unripe|variet\w*|tenera|dura|pisifera)\b", "ripeness or variety attribute", 10),
    ]
)

INSTANCE_SIGNALS = signals(
    [
        (r"\b(?:instance\s+segmentation|instance[-\s]?level|per[-\s]?instance|object\s+detection|fruit\s+detection|semantic\s+segmentation|mask\s+r[-\s]?cnn|yolo|detector)\b", "instance perception", 18),
        (r"\b(?:precision|recall|f1|mAP|iou|mean\s+absolute\s+error|rmse|r\s*2|hota|mota|idf1)\b", "quantitative evaluation", 5),
    ]
)

REVIEW_SIGNALS = signals(
    [
        (r"\b(?:systematic\s+review|scoping\s+review|literature\s+review|mini\s+review|survey|review\s+of|state[-\s]?of[-\s]?the[-\s]?art)\b", "prior review", 24),
        (r"\b(?:benchmark|dataset|data\s+set|annotated\s+dataset|corpus)\b", "benchmark or dataset", 12),
    ]
)

TRANSFER_SIGNALS = signals(
    [
        (r"\b(?:person\s+re[-\s]?identification|vehicle\s+re[-\s]?identification|pedestrian\s+tracking|multi[-\s]?object\s+tracking|mot\s+benchmark|visual\s+odometry|slam|robot\s+tracking)\b", "transfer identity mechanism", 28),
        (r"\b(?:structure\s+from\s+motion|\bsfm\b|multi[-\s]?view\s+stereo|point\s+cloud|3d\s+reconstruction|stereo\s+vision|lidar)\b", "transfer geometry mechanism", 20),
    ]
)

PENALTY_SIGNALS = signals(
    [
        (r"\b(?:land\s+use|land[-\s]?cover|biomass|carbon\s+stock|production\s+forecast|yield\s+forecast|yield\s+prediction|crop\s+yield\s+regression)\b", "global output", -30),
        (r"\b(?:remote\s+sensing|canopy\s+mapping|tree\s+crown|forest\s+inventory|tree\s+count(?:ing)?)\b", "canopy or remote-sensing focus", -18),
        (r"\b(?:leaf\s+disease|plant\s+disease|disease\s+classification|weed\s+mapping|soil\s+classification)\b", "non-fruit agricultural target", -15),
        (r"\b(?:image[-\s]?level|whole[-\s]?image|global)\s+(?:classification|regression|recognition)\b", "global image output", -22),
    ]
)

TARGET_TERM_PATTERN = re.compile(
    r"\b(?:fruit|fruitlet|berry|berries|apple|mango|citrus|"
    r"orange|grape|tomato|strawberr(?:y|ies)|blueberr(?:y|ies)|pineapple|"
    r"banana|peach|pear|cherry|kiwi|guava|pomegranate)\b",
    re.I,
)
DIRECT_TARGET_OPERATION_PATTERN = re.compile(
    r"(?:\b(?:fruit|fruitlet|berry|berries|apple|mango|citrus|"
    r"orange|grape|tomato|strawberr\w*|blueberr\w*|pineapple|banana|peach|pear|"
    r"cherry|kiwi|guava|pomegranate|ffb)\b.{0,45}\b(?:detect\w*|"
    r"segment\w*|locali[sz]\w*|recogn\w*|count\w*|track\w*|reconstruct\w*)\b|"
    r"\b(?:detect\w*|segment\w*|locali[sz]\w*|recogn\w*|count\w*|track\w*|"
    r"reconstruct\w*)\b.{0,45}\b(?:fruit|fruitlet|berry|berries|apple|mango|citrus|"
    r"orange|grape|tomato|strawberr\w*|blueberr\w*|"
    r"pineapple|banana|peach|pear|cherry|kiwi|guava|pomegranate|ffb)\b)",
    re.I,
)
PALM_FRUIT_PATTERN = re.compile(
    r"\b(?:fresh\s+fruit\s+bunch(?:es)?|oil\s+palm\s+fruit|palm\s+fruit|"
    r"palm\s+oil\s+(?:fruit|ffb|counter)|\bffb\b|tandan\s+buah|kelapa\s+sawit)\b",
    re.I,
)
PRIOR_REVIEW_TITLE_PATTERN = re.compile(
    r"\b(?:systematic\s+review|scoping\s+review|literature\s+review|mini\s+review|"
    r"survey|review\s+of|(?:a\s+)?review\b|state[-\s]?of[-\s]?the[-\s]?art)\b",
    re.I,
)
TITLE_TREE_ONLY_PATTERN = re.compile(
    r"\b(?:tree|canopy|crown|plantation|forest)\b.{0,35}\b(?:detect\w*|count\w*|segment\w*|map\w*|inventory)\b",
    re.I,
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").lower()).strip()


def matched(signal_set: tuple[Signal, ...], text: str) -> tuple[int, list[str]]:
    total = 0
    labels: list[str] = []
    for signal in signal_set:
        if signal.pattern.search(text):
            total += signal.weight
            labels.append(signal.label)
    return total, labels


def compact_reason(labels: list[str], limit: int = 8) -> str:
    seen: list[str] = []
    for label in labels:
        if label not in seen:
            seen.append(label)
    return "; ".join(seen[:limit])


def source_boost(row: dict[str, str]) -> int:
    score = 0
    if normalize(row.get("doi", "")):
        score += 4
    if normalize(row.get("abstract", "")):
        score += 4
    if "scopus" in normalize(row.get("source_databases", "")):
        score += 3
    if normalize(row.get("abstract_screen_confidence", "")) == "high":
        score += 2
    return score


def classify(row: dict[str, str]) -> dict[str, str]:
    title = row.get("title", "")
    abstract = row.get("abstract", "")
    text = normalize(f"{title} {abstract}")
    core_score, core_labels = matched(CORE_SIGNALS, text)
    fruit_score, fruit_labels = matched(FRUIT_SIGNALS, text)
    palm_score, palm_labels = matched(OIL_PALM_SIGNALS, text)
    instance_score, instance_labels = matched(INSTANCE_SIGNALS, text)
    review_score, review_labels = matched(REVIEW_SIGNALS, text)
    transfer_score, transfer_labels = matched(TRANSFER_SIGNALS, text)
    penalty, penalty_labels = matched(PENALTY_SIGNALS, text)

    # Avoid over-ranking global yield and canopy records that happen to use a
    # generic word such as detection or counting.
    if penalty and not (core_score >= 28 or instance_score >= 18):
        penalty *= 1.35
    if palm_score and core_score:
        palm_score += 8
    if fruit_score and core_score:
        fruit_score += 8
    if review_score and not (fruit_score or palm_score or core_score):
        review_score -= 12

    has_direct_target = bool(DIRECT_TARGET_OPERATION_PATTERN.search(text))
    title_has_target = bool(TARGET_TERM_PATTERN.search(title))
    has_fruit = has_direct_target or (title_has_target and instance_score >= 18)
    has_palm_fruit = bool(PALM_FRUIT_PATTERN.search(text)) and (core_score >= 12 or instance_score >= 18)
    has_palm = has_palm_fruit
    title_tree_only = bool(TITLE_TREE_ONLY_PATTERN.search(title)) and not title_has_target and not has_palm_fruit
    if title_tree_only:
        has_direct_target = False
        has_fruit = False
        has_palm = False
        core_score = max(0, core_score - 42)
        fruit_score = max(0, fruit_score - 30)
        palm_score = max(0, palm_score - 30)
        penalty -= 24
        penalty_labels.append("tree or canopy only")
    has_core = core_score >= 22
    has_instance = instance_score >= 18
    has_review = bool(PRIOR_REVIEW_TITLE_PATTERN.search(title))
    has_transfer = bool(transfer_labels)
    review_relevant = has_review and (has_fruit or has_palm_fruit or fruit_score >= 22 or palm_score >= 36 or core_score >= 22)

    total = (
        core_score
        + fruit_score
        + palm_score
        + instance_score
        + review_score
        + transfer_score
        + source_boost(row)
        + penalty
    )

    if review_relevant:
        bucket = "prior_review_or_positioning"
        tier = "D"
    elif has_palm and has_instance:
        bucket = "oil_palm_direct"
        tier = "B"
    elif has_fruit and has_instance and (has_core or "3D reconstruction" in core_labels or "depth or point cloud" in core_labels):
        bucket = "fruit_multiview_or_3d"
        tier = "B"
    elif has_core and (has_fruit or has_palm):
        bucket = "core_identity_or_inventory"
        tier = "A"
    elif has_fruit and has_instance:
        bucket = "fruit_instance_baseline"
        tier = "C"
    elif has_transfer:
        bucket = "transfer_mechanism"
        tier = "D"
    else:
        bucket = "supporting_or_uncertain"
        tier = "E"

    labels = core_labels + palm_labels + fruit_labels + instance_labels + review_labels + transfer_labels
    return {
        "priority_score": str(total),
        "core_score": str(core_score),
        "fruit_score": str(fruit_score),
        "oil_palm_score": str(palm_score),
        "instance_score": str(instance_score),
        "review_score": str(review_score),
        "transfer_score": str(transfer_score),
        "penalty_score": str(penalty),
        "priority_tier": tier,
        "priority_bucket": bucket,
        "priority_reason": compact_reason(labels),
        "priority_penalties": compact_reason(penalty_labels),
        "rule_version": RULE_VERSION,
    }


def choose_shortlist(rows: list[dict[str, str]], limit: int) -> tuple[list[dict[str, str]], dict[str, int]]:
    ordered = sorted(rows, key=lambda row: (-float(row["priority_score"]), row.get("review_order", "999999"), row.get("record_id", "")))
    buckets = [
        ("core_identity_or_inventory", 60),
        ("oil_palm_direct", 45),
        ("fruit_multiview_or_3d", 65),
        ("fruit_instance_baseline", 40),
        ("transfer_mechanism", 30),
        ("prior_review_or_positioning", 20),
    ]
    selected: dict[str, dict[str, str]] = {}
    selection_stage: dict[str, str] = {}
    counts: Counter[str] = Counter()

    for bucket, quota in buckets:
        candidates = [row for row in ordered if row["priority_bucket"] == bucket]
        for row in candidates:
            if len(selected) >= limit or counts[bucket] >= quota:
                break
            record_id = row["record_id"]
            if record_id in selected:
                continue
            selected[record_id] = row
            selection_stage[record_id] = f"quota:{bucket}"
            counts[bucket] += 1

    for row in ordered:
        if len(selected) >= limit:
            break
        record_id = row["record_id"]
        if record_id in selected:
            continue
        selected[record_id] = row
        selection_stage[record_id] = "global_score_fill"

    shortlist = []
    for rank, row in enumerate(sorted(selected.values(), key=lambda item: (-float(item["priority_score"]), item.get("review_order", "999999"))), start=1):
        copy = dict(row)
        copy["shortlist_rank"] = str(rank)
        copy["selection_stage"] = selection_stage[row["record_id"]]
        shortlist.append(copy)
    return shortlist, dict(counts)


def write_report(path: Path, args: argparse.Namespace, ranking: list[dict[str, str]], shortlist: list[dict[str, str]], bucket_counts: dict[str, int]) -> None:
    tier_counts = Counter(row["priority_tier"] for row in shortlist)
    reviewed = Counter(row["review_status"] for row in shortlist)
    lines = [
        "# Prioritas full-text review",
        "",
        f"Tanggal: {args.run_date}",
        f"Rule version: `{RULE_VERSION}`",
        "",
        "## Keputusan metodologis",
        "",
        "20.035 record adalah search pool setelah deduplikasi dan title-abstract screening. Tidak semua record dijanjikan untuk dibaca full text. Ranking ini memilih studi yang paling relevan dengan inventaris buah unik lintas-observasi, studi sawit, studi buah dengan bukti instance atau 3D, review terdahulu, dan mekanisme transfer yang mendukung.",
        "",
        "Skor hanya alat prioritas. Skor tidak mengubah keputusan inklusi, tidak menghapus record, dan tidak menggantikan verifikasi full text.",
        "",
        "## Sinyal yang digunakan",
        "",
        "- Sinyal inti: unique inventory, duplicate resolution, re-identification, cross-view, tracking, association, SfM/MVS/stereo, point cloud, RGB-D, depth, dan 3D reconstruction.",
        "- Sinyal target: fruit, fruitlet, berry, bunch, apple, mango, citrus, grape, tomato, oil palm, dan FFB.",
        "- Sinyal pendukung: instance detection/segmentation, counting, ripeness, benchmark/dataset, prior review, dan mekanisme tracking atau geometry dari domain lain.",
        "- Penalti: global yield/biomass/land-use output, canopy or remote sensing only, non-fruit disease/weed targets, dan image-level output.",
        "",
        "## Diversifikasi shortlist",
        "",
        "Shortlist dipilih dengan kuota bucket agar hasil tidak didominasi satu keluarga YOLO atau satu domain. Angka dalam kurung adalah target maksimum:",
        "",
        f"- {bucket_counts.get('core_identity_or_inventory', 0)} core identity or inventory (target 60)",
        f"- {bucket_counts.get('oil_palm_direct', 0)} oil-palm direct (target 45)",
        f"- {bucket_counts.get('fruit_multiview_or_3d', 0)} fruit multiview or 3D (target 65)",
        f"- {bucket_counts.get('fruit_instance_baseline', 0)} fruit instance baselines (target 40)",
        f"- {bucket_counts.get('transfer_mechanism', 0)} transfer mechanisms (target 30)",
        f"- {bucket_counts.get('prior_review_or_positioning', 0)} prior reviews or positioning (target maximum 20; remaining shortlist capacity after earlier quotas)",
        f"- global score fill sampai {args.limit} record",
        "",
        "## Rekap hasil",
        "",
        f"- Ranking lengkap: {len(ranking)} record",
        f"- Shortlist: {len(shortlist)} record",
        f"- Status shortlist: {reviewed.get('reviewed', 0)} reviewed, {reviewed.get('needs_manual_retrieval', 0)} perlu retrieval manual, {reviewed.get('pending', 0)} pending",
        f"- Tier: {dict(sorted(tier_counts.items()))}",
        f"- Bucket kuota yang terisi: {bucket_counts}",
        "",
        "File ranking menyimpan skor, komponen skor, alasan, penalti, bucket, dan status ledger sehingga keputusan dapat diaudit dan diubah tanpa mengubah data mentah.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_html(path: Path, shortlist: list[dict[str, str]]) -> None:
    rows = []
    for row in shortlist:
        cells = [
            row.get("shortlist_rank", ""),
            row.get("priority_score", ""),
            row.get("priority_tier", ""),
            row.get("priority_bucket", ""),
            row.get("review_status", ""),
            row.get("ledger_decision", ""),
            row.get("year", ""),
            row.get("title", ""),
            row.get("venue", ""),
            row.get("doi", ""),
            row.get("priority_reason", ""),
            row.get("selection_stage", ""),
        ]
        rows.append("<tr>" + "".join(f"<td>{html.escape(value or '')}</td>" for value in cells) + "</tr>")
    headers = [
        "Rank", "Score", "Tier", "Bucket", "Review status", "Decision", "Year",
        "Title", "Venue", "DOI", "Reason", "Selection stage",
    ]
    header_html = "".join(f"<th>{html.escape(label)}</th>" for label in headers)
    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Priority shortlist for targeted full-text review</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #17202a; background: #f7f9fb; }}
h1 {{ margin-bottom: .3rem; }}
p {{ color: #46515c; }}
input {{ width: min(760px, 100%); padding: .7rem; border: 1px solid #aab7c4; border-radius: .5rem; font-size: 1rem; }}
.wrap {{ overflow-x: auto; background: white; border: 1px solid #d7dee5; border-radius: .6rem; margin-top: 1rem; }}
table {{ border-collapse: collapse; width: 100%; min-width: 1500px; }}
th, td {{ border-bottom: 1px solid #e4e9ee; padding: .55rem .65rem; text-align: left; vertical-align: top; }}
th {{ position: sticky; top: 0; background: #e9f1f8; color: #1d3b53; }}
tr:hover {{ background: #f1f7fb; }}
td:nth-child(1), td:nth-child(2), td:nth-child(3), td:nth-child(5), td:nth-child(6), td:nth-child(7) {{ white-space: nowrap; }}
.meta {{ font-size: .9rem; }}
</style>
</head>
<body>
<h1>Priority shortlist for targeted full-text review</h1>
<p class="meta">Generated {html.escape(str(date.today()))}. The score ranks candidates; it is not a final inclusion decision.</p>
<label for="filter">Filter title, venue, DOI, bucket, or reason</label><br>
<input id="filter" type="search" placeholder="type to filter...">
<div class="wrap"><table id="results"><thead><tr>{header_html}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<script>
const input = document.getElementById('filter');
const tableRows = Array.from(document.querySelectorAll('#results tbody tr'));
input.addEventListener('input', () => {{
  const query = input.value.toLowerCase();
  tableRows.forEach(row => {{ row.hidden = query && !row.textContent.toLowerCase().includes(query); }});
}});
</script>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--master", type=Path, default=DEFAULT_MASTER)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--ranking", type=Path, default=DEFAULT_RANKING)
    parser.add_argument("--shortlist", type=Path, default=DEFAULT_SHORTLIST)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--html", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--wave", type=Path, default=DEFAULT_WAVE)
    parser.add_argument("--wave-limit", type=int, default=60)
    parser.add_argument("--limit", type=int, default=250)
    parser.add_argument("--run-date", default=str(date.today()))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidate_rows = read_csv(args.candidates)
    master_by_id = {row["record_id"]: row for row in read_csv(args.master)}
    ledger_by_id = {row["record_id"]: row for row in read_csv(args.ledger)} if args.ledger.exists() else {}

    retained = [
        row for row in candidate_rows
        if row.get("abstract_screen_decision") == "advance_fulltext"
    ]
    scored: list[dict[str, str]] = []
    for candidate in retained:
        master = master_by_id.get(candidate["record_id"], {})
        merged = dict(master)
        merged.update({key: value for key, value in candidate.items() if value != ""})
        merged["record_id"] = candidate["record_id"]
        scored_row = dict(merged)
        scored_row.update(classify(merged))
        ledger = ledger_by_id.get(candidate["record_id"], {})
        scored_row["review_status"] = ledger.get("review_status", "pending")
        scored_row["retrieval_status"] = ledger.get("retrieval_status", "pending")
        scored_row["ledger_decision"] = ledger.get("decision", "pending")
        scored_row["ledger_review_order"] = ledger.get("review_order", "")
        scored.append(scored_row)

    scored.sort(key=lambda row: (-float(row["priority_score"]), row.get("record_id", "")))
    for rank, row in enumerate(scored, start=1):
        row["priority_rank"] = str(rank)

    shortlist, bucket_counts = choose_shortlist(scored, args.limit)
    wave = [
        row for row in shortlist
        if row.get("review_status") in {"pending", "needs_manual_retrieval"}
    ][: args.wave_limit]
    for rank, row in enumerate(wave, start=1):
        row["wave_rank"] = str(rank)
    ranking_fields = [
        "priority_rank", "record_id", "doi", "title", "year", "venue", "authors", "abstract",
        "source_databases", "query_ids", "abstract_available", "abstract_screen_confidence",
        "abstract_screen_basis", "priority_score", "core_score", "fruit_score", "oil_palm_score",
        "instance_score", "review_score", "transfer_score", "penalty_score", "priority_tier",
        "priority_bucket", "priority_reason", "priority_penalties", "rule_version", "review_status",
        "retrieval_status", "ledger_decision", "ledger_review_order",
    ]
    shortlist_fields = ["shortlist_rank", "selection_stage"] + ranking_fields
    wave_fields = ["wave_rank"] + shortlist_fields
    write_csv(args.ranking, scored, ranking_fields)
    write_csv(args.shortlist, shortlist, shortlist_fields)
    write_csv(args.wave, wave, wave_fields)

    summary_rows: list[dict[str, str]] = []
    for label, count in sorted(Counter(row["priority_bucket"] for row in scored).items()):
        summary_rows.append({"scope": "all_ranked", "category": label, "count": str(count), "rule_version": RULE_VERSION})
    for label, count in sorted(Counter(row["priority_tier"] for row in scored).items()):
        summary_rows.append({"scope": "all_ranked", "category": f"tier_{label}", "count": str(count), "rule_version": RULE_VERSION})
    for label, count in sorted(Counter(row["priority_bucket"] for row in shortlist).items()):
        summary_rows.append({"scope": "shortlist", "category": label, "count": str(count), "rule_version": RULE_VERSION})
    for label, count in sorted(Counter(row["review_status"] for row in shortlist).items()):
        summary_rows.append({"scope": "shortlist", "category": f"review_status_{label}", "count": str(count), "rule_version": RULE_VERSION})
    write_csv(args.summary, summary_rows, ["scope", "category", "count", "rule_version"])
    write_report(args.report, args, scored, shortlist, bucket_counts)
    write_html(args.html, shortlist)

    print(f"retained_candidates={len(scored)}")
    print(f"ranking={args.ranking}")
    print(f"shortlist={len(shortlist)}")
    print(f"shortlist_path={args.shortlist}")
    print(f"wave={len(wave)}")
    print(f"wave_path={args.wave}")
    print(f"summary={args.summary}")
    print(f"report={args.report}")
    print(f"html={args.html}")
    print(f"bucket_counts={bucket_counts}")


if __name__ == "__main__":
    main()
