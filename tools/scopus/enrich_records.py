#!/usr/bin/env python3
"""Melengkapi rekaman Scopus dengan abstrak dan tautan PDF akses terbuka.

View STANDARD pada Scopus Search API tidak memuat abstrak. Abstrak untuk
penyaringan judul-abstrak diambil berdasarkan DOI dari OpenAlex, lalu Semantic
Scholar, lalu Crossref. Rekaman tanpa DOI dicocokkan dengan judul dan tahun di
OpenAlex. Sumber abstrak dicatat per rekaman agar dapat diaudit.

Keluaran: berkas JSONL cache (satu baris per EID), diperbarui secara bertahap.
"""
import argparse
import csv
import json
import re
import time
from pathlib import Path

import requests

MAILTO = "research-pipeline@users.noreply.github.com"
OA_URL = "https://api.openalex.org/works"
S2_URL = "https://api.semanticscholar.org/graph/v1/paper/batch"
CR_URL = "https://api.crossref.org/works/"


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def inverted_to_text(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def openalex_fields(w):
    urls = []
    for loc in [w.get("best_oa_location")] + (w.get("locations") or []):
        if loc and loc.get("pdf_url") and loc["pdf_url"] not in urls:
            urls.append(loc["pdf_url"])
    landing = []
    for loc in w.get("locations") or []:
        if loc and loc.get("landing_page_url") and loc.get("is_oa"):
            landing.append(loc["landing_page_url"])
    arxiv = ""
    for loc in w.get("locations") or []:
        src = (loc or {}).get("source") or {}
        lp = (loc or {}).get("landing_page_url") or ""
        if "arxiv" in (src.get("display_name") or "").lower() or "arxiv.org" in lp:
            m = re.search(r"(\d{4}\.\d{4,5})", lp)
            if m:
                arxiv = m.group(1)
    return {
        "openalex_id": w.get("id", ""),
        "abstract": inverted_to_text(w.get("abstract_inverted_index")),
        "abstract_source": "openalex" if w.get("abstract_inverted_index") else "",
        "oa_status": (w.get("open_access") or {}).get("oa_status", ""),
        "pdf_urls": urls,
        "oa_landing": landing,
        "arxiv_id": arxiv,
        "keywords": [k.get("display_name") for k in (w.get("keywords") or [])],
        "referenced_works": len(w.get("referenced_works") or []),
    }


OA_SELECT = ("id,doi,abstract_inverted_index,open_access,best_oa_location,"
             "locations,keywords,referenced_works")


def openalex_by_doi(session, dois):
    # Pencarian entitas tunggal (/works/doi:...) tidak memakai kuota harian
    # OpenAlex, sedangkan pencarian daftar (filter=doi:a|b) memakainya. Karena
    # kuota per IP sering habis, dipakai pencarian tunggal satu per satu.
    out = {}
    for doi in dois:
        r = session.get(f"{OA_URL}/doi:{doi}",
                        params={"select": OA_SELECT, "mailto": MAILTO},
                        timeout=60)
        if r.status_code == 200:
            out[doi] = openalex_fields(r.json())
        elif r.status_code == 429:
            time.sleep(5)
        time.sleep(0.12)
    return out


def openalex_by_title(session, title, year):
    q = norm_title(title)[:200]
    if not q:
        return None
    params = {"search": q, "per-page": 5, "mailto": MAILTO}
    if year:
        params["filter"] = f"publication_year:{int(year) - 1}-{int(year) + 1}"
    r = session.get(OA_URL, params=params, timeout=90)
    if r.status_code != 200:
        return None
    for w in r.json().get("results", []):
        if norm_title(w.get("title")) == norm_title(title):
            return openalex_fields(w)
    return None


def s2_by_doi(session, dois):
    out = {}
    for i in range(0, len(dois), 100):
        chunk = dois[i:i + 100]
        for attempt in range(5):
            r = session.post(S2_URL, params={
                "fields": "abstract,openAccessPdf,externalIds"},
                json={"ids": [f"DOI:{d}" for d in chunk]}, timeout=90)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            break
        if r.status_code != 200:
            continue
        for doi, p in zip(chunk, r.json()):
            if not p:
                continue
            pdf = (p.get("openAccessPdf") or {}).get("url") or ""
            out[doi] = {"abstract": p.get("abstract") or "",
                        "pdf": pdf,
                        "arxiv_id": (p.get("externalIds") or {}).get("ArXiv", "")}
        time.sleep(1.2)
    return out


def europepmc_abstract(session, doi):
    # Europe PMC juga mengindeks AGRICOLA, sehingga sebagian artikel pertanian
    # dan rekayasa punya abstrak di sini walau tidak ada di Semantic Scholar.
    r = session.get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                    params={"query": f'DOI:"{doi}"', "format": "json",
                            "resultType": "core"}, timeout=60)
    if r.status_code != 200:
        return ""
    res = r.json().get("resultList", {}).get("result", [])
    ab = res[0].get("abstractText", "") if res else ""
    return re.sub(r"<[^>]+>", " ", ab).strip()


def crossref_abstract(session, doi):
    r = session.get(CR_URL + doi, params={"mailto": MAILTO}, timeout=60)
    if r.status_code != 200:
        return ""
    ab = r.json().get("message", {}).get("abstract", "")
    return re.sub(r"<[^>]+>", " ", ab).strip()


def fill_missing(cache_path):
    session = requests.Session()
    session.headers["User-Agent"] = f"research-pipeline (mailto:{MAILTO})"
    recs = [json.loads(l) for l in cache_path.read_text().splitlines()]
    empty = [r for r in recs if not r["abstract"] and r["doi"]]
    oa = openalex_by_doi(session, [r["doi"] for r in empty])
    filled = 0
    for r in empty:
        info = oa.get(r["doi"])
        if info:
            for k, v in info.items():
                if k == "pdf_urls":
                    r[k] = list(dict.fromkeys(r[k] + v))
                elif not r.get(k):
                    r[k] = v
        if not r["abstract"]:
            ab = europepmc_abstract(session, r["doi"])
            if ab:
                r["abstract"], r["abstract_source"] = ab, "europepmc"
        filled += bool(r["abstract"])
        time.sleep(0.1)
    cache_path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs))
    print(f"kosong={len(empty)} terisi={filled}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", required=True, help="CSV dengan eid, doi, title, year")
    ap.add_argument("--cache", required=True, help="JSONL cache keluaran")
    ap.add_argument("--fill-missing", action="store_true",
                    help="ulangi pencarian abstrak untuk entri cache yang kosong")
    args = ap.parse_args()

    if args.fill_missing:
        fill_missing(Path(args.cache))
        return

    rows = list(csv.DictReader(open(args.records)))
    cache_path = Path(args.cache)
    cache = {}
    if cache_path.exists():
        for line in cache_path.read_text().splitlines():
            rec = json.loads(line)
            cache[rec["eid"]] = rec
    todo = [r for r in rows if r["eid"] not in cache]
    print(f"rekaman={len(rows)} sudah di-cache={len(rows) - len(todo)}")

    session = requests.Session()
    session.headers["User-Agent"] = f"research-pipeline (mailto:{MAILTO})"

    dois = sorted({r["doi"] for r in todo if r["doi"]})
    oa = openalex_by_doi(session, dois)
    # Semantic Scholar dipanggil untuk semua DOI: selain abstrak, ia memberi
    # tautan PDF terbuka dan ID arXiv yang tidak selalu ada di OpenAlex.
    s2 = s2_by_doi(session, dois) if dois else {}

    with open(cache_path, "a") as f:
        for r in todo:
            doi = r["doi"]
            rec = {"eid": r["eid"], "doi": doi}
            info = oa.get(doi) if doi else openalex_by_title(session, r["title"], r["year"])
            rec.update(info or {"openalex_id": "", "abstract": "",
                                "abstract_source": "", "oa_status": "",
                                "pdf_urls": [], "oa_landing": [],
                                "arxiv_id": "", "keywords": [],
                                "referenced_works": 0})
            extra = s2.get(doi) if doi else None
            if extra:
                if not rec["abstract"] and extra["abstract"]:
                    rec["abstract"] = extra["abstract"]
                    rec["abstract_source"] = "semanticscholar"
                if extra["pdf"] and extra["pdf"] not in rec["pdf_urls"]:
                    rec["pdf_urls"].append(extra["pdf"])
                rec["arxiv_id"] = rec["arxiv_id"] or extra["arxiv_id"]
            if not rec["abstract"] and doi:
                ab = crossref_abstract(session, doi)
                if ab:
                    rec["abstract"], rec["abstract_source"] = ab, "crossref"
            if not rec["abstract"] and doi:
                ab = europepmc_abstract(session, doi)
                if ab:
                    rec["abstract"], rec["abstract_source"] = ab, "europepmc"
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("selesai")


if __name__ == "__main__":
    main()
