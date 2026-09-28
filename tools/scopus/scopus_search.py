#!/usr/bin/env python3
"""Menjalankan query Scopus Search API dan menyimpan respons mentah.

Kunci API dibaca dari variabel lingkungan ELSEVIER_API_KEY atau dari berkas
yang ditunjuk ELSEVIER_API_KEY_FILE. Kunci tidak pernah ditulis ke repo.

Contoh:
    python3 tools/scopus/scopus_search.py \
        --queries literature/scopus-2026-09/topik/queries.json \
        --out literature/scopus-2026-09/topik

Keluaran per query:
    raw/<QID>/page_NNN.json   respons mentah Scopus (view STANDARD)
    records_<QID>.csv         satu baris per rekaman
Keluaran gabungan:
    counts.csv                jumlah hasil per query dan tanggal eksekusi
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

import requests

API_URL = "https://api.elsevier.com/content/search/scopus"
PAGE_SIZE = 25
FIELDS = [
    "qid", "eid", "doi", "title", "first_author", "year", "cover_date",
    "source", "source_type", "doc_type", "volume", "issue", "pages",
    "article_number", "cited_by", "open_access", "issn", "eissn",
    "affil_country",
]


def load_key():
    key = os.environ.get("ELSEVIER_API_KEY", "").strip()
    if not key and os.environ.get("ELSEVIER_API_KEY_FILE"):
        key = Path(os.environ["ELSEVIER_API_KEY_FILE"]).read_text().strip()
    if not key:
        sys.exit("ELSEVIER_API_KEY atau ELSEVIER_API_KEY_FILE belum diisi")
    return key


def get_page(session, query, start, sort):
    # Kunci non-langganan tidak boleh memakai parameter cursor, jadi paginasi
    # memakai start. Scopus membatasi start + count <= 5000 per query.
    params = {
        "query": query,
        "count": PAGE_SIZE,
        "view": "STANDARD",
        "start": start,
    }
    if sort:
        params["sort"] = sort
    for attempt in range(6):
        resp = session.get(API_URL, params=params, timeout=90)
        if resp.status_code == 429 or resp.status_code >= 500:
            time.sleep(2 ** attempt)
            continue
        resp.raise_for_status()
        return resp.json()
    resp.raise_for_status()


def entry_to_row(qid, e):
    affil = e.get("affiliation") or []
    countries = sorted({a.get("affiliation-country") or "" for a in affil} - {""})
    date = e.get("prism:coverDate") or ""
    return {
        "qid": qid,
        "eid": e.get("eid", ""),
        "doi": (e.get("prism:doi") or "").lower(),
        "title": e.get("dc:title", ""),
        "first_author": e.get("dc:creator", ""),
        "year": date[:4],
        "cover_date": date,
        "source": e.get("prism:publicationName", ""),
        "source_type": e.get("prism:aggregationType", ""),
        "doc_type": e.get("subtypeDescription", ""),
        "volume": e.get("prism:volume", "") or "",
        "issue": e.get("prism:issueIdentifier", "") or "",
        "pages": e.get("prism:pageRange", "") or "",
        "article_number": e.get("article-number", "") or "",
        "cited_by": e.get("citedby-count", ""),
        "open_access": e.get("openaccessFlag", ""),
        "issn": e.get("prism:issn", "") or "",
        "eissn": e.get("prism:eIssn", "") or "",
        "affil_country": "; ".join(countries),
    }


MAX_OFFSET = 5000


def fetch_all(session, qid, query, raw_dir, sort, limit, tag=""):
    rows, start, page, total = [], 0, 0, None
    while True:
        data = get_page(session, query, start, sort)
        res = data["search-results"]
        if total is None:
            total = int(res.get("opensearch:totalResults", 0))
        (raw_dir / f"page_{tag}{page:03d}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=1))
        entries = [e for e in res.get("entry", []) if "error" not in e]
        rows.extend(entry_to_row(qid, e) for e in entries)
        page += 1
        start += PAGE_SIZE
        if (not entries or len(rows) >= min(total, limit)
                or start >= MAX_OFFSET):
            break
        time.sleep(0.15)
    return total, rows


def run_query(session, qid, query, out_dir, sort, limit):
    raw_dir = out_dir / "raw" / qid
    raw_dir.mkdir(parents=True, exist_ok=True)
    total, rows = fetch_all(session, qid, query, raw_dir, sort, limit)
    if total > MAX_OFFSET and limit > MAX_OFFSET:
        # Hasil di atas 5000 diambil per tahun terbit agar tidak terpotong.
        rows = []
        for year in range(2012, dt.date.today().year + 1):
            sub = f"({query}) AND PUBYEAR = {year}"
            sub_total, sub_rows = fetch_all(session, qid, sub, raw_dir, sort,
                                            limit, tag=f"y{year}_")
            if sub_total > MAX_OFFSET:
                print(f"PERINGATAN {qid} {year}: {sub_total} > {MAX_OFFSET}")
            rows.extend(sub_rows)
    with open(out_dir / f"records_{qid}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    return total, len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queries", required=True,
                    help="JSON: daftar objek {qid, query, sort?, limit?}")
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", nargs="*", help="jalankan hanya QID ini")
    ap.add_argument("--count-only", action="store_true",
                    help="cetak jumlah hasil tanpa menyimpan apa pun")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    queries = json.loads(Path(args.queries).read_text())
    session = requests.Session()
    session.headers.update({"X-ELS-APIKey": load_key(),
                            "Accept": "application/json"})

    if args.count_only:
        for q in queries:
            if args.only and q["qid"] not in args.only:
                continue
            res = get_page(session, q["query"], 0, "")["search-results"]
            print(f"{q['qid']}: {res.get('opensearch:totalResults')}")
        return

    counts_path = out_dir / "counts.csv"
    new_file = not counts_path.exists()
    with open(counts_path, "a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["qid", "executed_utc", "total_results", "retrieved",
                        "query"])
        for q in queries:
            if args.only and q["qid"] not in args.only:
                continue
            total, got = run_query(session, q["qid"], q["query"], out_dir,
                                   q.get("sort", ""), q.get("limit", 10 ** 6))
            stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
            w.writerow([q["qid"], stamp, total, got, q["query"]])
            f.flush()
            print(f"{q['qid']}: total={total} diambil={got}")


if __name__ == "__main__":
    main()
