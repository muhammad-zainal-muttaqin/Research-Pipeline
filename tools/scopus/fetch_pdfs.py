#!/usr/bin/env python3
"""Mengunduh PDF akses terbuka untuk rekaman Scopus terpilih.

Urutan kandidat per rekaman:
  1. tautan PDF dari OpenAlex, Semantic Scholar, dan Unpaywall;
  2. aturan per penerbit (CDN MDPI, bingkai PDF IEEE, Frontiers);
  3. meta citation_pdf_url pada halaman arahan DOI;
  4. versi arXiv bila tercatat di OpenAlex atau Semantic Scholar.

Hanya berkas yang diawali '%PDF' yang disimpan. Rekaman yang gagal dicatat
beserta alasannya di log agar dapat dilengkapi lewat akses institusi.

Masukan CSV minimal berkolom: key, doi, title. Nama berkas = <key>.pdf.
"""
import argparse
import csv
import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin

import requests

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/140.0 Safari/537.36")
MAILTO = "research-pipeline@users.noreply.github.com"

# Kode jurnal pada DOI MDPI -> nama folder di mdpi-res.com.
MDPI_JOURNALS = {
    "s": "sensors", "rs": "remotesensing", "app": "applsci",
    "agronomy": "agronomy", "agriculture": "agriculture",
    "horticulturae": "horticulturae", "electronics": "electronics",
    "plants": "plants", "foods": "foods", "drones": "drones",
    "jimaging": "jimaging", "ai": "ai", "computers": "computers",
    "agriengineering": "agriengineering", "forests": "forests",
    "ijgi": "ijgi", "robotics": "robotics", "machines": "machines",
    "mathematics": "mathematics", "symmetry": "symmetry", "su": "sustainability",
    "info": "information", "make": "make", "technologies": "technologies",
    "bdcc": "BDCC", "asi": "asi", "futureinternet": "futureinternet",
    "biology": "biology", "entropy": "entropy", "algorithms": "algorithms",
    "systems": "systems", "land": "land", "fire": "fire", "ani": "animals",
    "insects": "insects", "processes": "processes", "photonics": "photonics",
    "micromachines": "micromachines", "smartcities": "smartcities",
    "vision": "vision", "jsan": "jsan", "iot": "iot", "digital": "digital",
    "applbiosci": "applbiosci", "geomatics": "geomatics", "data": "data",
}


def mdpi_cdn(doi):
    """DOI MDPI = kode jurnal + volume + nomor (2 digit) + artikel (4-5 digit)."""
    m = re.match(r"10\.3390/([a-z]+)(\d{7,9})$", doi)
    if not m or m.group(1) not in MDPI_JOURNALS:
        return None
    d = m.group(2)
    vol, art = {7: (d[:1], d[3:]), 8: (d[:2], d[4:]), 9: (d[:2], d[4:])}[len(d)]
    j = MDPI_JOURNALS[m.group(1)]
    stem = f"{j}-{int(vol):02d}-{int(art):05d}"
    return f"https://mdpi-res.com/d_attachment/{j}/{stem}/article_deploy/{stem}.pdf"


def is_pdf(content):
    return content[:4] == b"%PDF"


class Hasil:
    """Respons ringkas: isi sudah dibaca penuh dalam batas waktu dan ukuran."""

    def __init__(self, url, content, encoding):
        self.url = url
        self.content = content
        self.encoding = encoding or "utf-8"

    @property
    def text(self):
        return self.content.decode(self.encoding, errors="replace")

    def json(self):
        return json.loads(self.content)


def try_get(session, url, timeout=25, deadline=90, max_bytes=80_000_000):
    """GET dengan batas waktu total; server yang mengirim data sangat lambat
    tidak boleh menahan satu pekerja tanpa batas."""
    start = time.monotonic()
    try:
        with session.get(url, timeout=timeout, allow_redirects=True,
                         stream=True) as r:
            if r.status_code != 200:
                return None, f"HTTP {r.status_code}"
            chunks, size = [], 0
            for chunk in r.iter_content(65536):
                chunks.append(chunk)
                size += len(chunk)
                if size > max_bytes:
                    return None, "berkas terlalu besar"
                if time.monotonic() - start > deadline:
                    return None, "melewati batas waktu total"
            return Hasil(r.url, b"".join(chunks), r.encoding), ""
    except requests.RequestException as exc:
        return None, f"galat jaringan: {exc.__class__.__name__}"


def resolve_pdf(session, url):
    """Mengikuti URL; bila HTML, cari bingkai PDF IEEE atau citation_pdf_url."""
    r, err = try_get(session, url)
    if r is None:
        return None, err
    if is_pdf(r.content):
        return r.content, ""
    html = r.text[:400000]
    m = re.search(r'src="(https://ieeexplore\.ieee\.org/ielx?\d*/[^"]+\.pdf[^"]*)"', html)
    if not m:
        m = re.search(r'name="citation_pdf_url"\s+content="([^"]+)"', html) or \
            re.search(r'content="([^"]+)"\s+name="citation_pdf_url"', html)
    if not m and "doi.org" not in url:
        # Halaman repositori institusi (DSpace, EPrints, Pure): tautan berkas
        # utama biasanya berupa bitstream atau berakhiran .pdf.
        m = re.search(r'href="([^"]*(?:/bitstream/|/files/|/download/)[^"]*\.pdf[^"]*)"',
                      html, re.I) or re.search(r'href="([^"]+\.pdf)"', html, re.I)
    if m:
        pdf_url = urljoin(r.url, m.group(1).replace("&amp;", "&"))
        r2, err2 = try_get(session, pdf_url)
        if r2 is not None and is_pdf(r2.content):
            return r2.content, ""
        return None, f"citation_pdf_url gagal ({err2 or 'bukan PDF'})"
    return None, "HTML tanpa tautan PDF"


def unpaywall_urls(session, doi):
    r, _ = try_get(session, f"https://api.unpaywall.org/v2/{doi}?email={MAILTO}", 60)
    if r is None:
        return []
    try:
        locs = r.json().get("oa_locations") or []
    except ValueError:
        return []
    out = []
    for loc in locs:
        for k in ("url_for_pdf", "url"):
            if loc.get(k) and loc[k] not in out:
                out.append(loc[k])
    return out


def ieee_stamp(doi, urls):
    for u in urls:
        m = re.search(r"arnumber=(\d+)|document/(\d+)", u)
        if m and "ieee" in u:
            num = m.group(1) or m.group(2)
            return f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={num}"
    return None


def candidates(session, rec, enrich):
    doi = rec.get("doi", "")
    urls = list(enrich.get("pdf_urls") or [])
    if doi:
        urls += [u for u in unpaywall_urls(session, doi) if u not in urls]
        cdn = mdpi_cdn(doi)
        if cdn:
            urls.insert(0, cdn)
        if doi.startswith("10.3389/"):
            urls.insert(0, f"https://www.frontiersin.org/articles/{doi}/pdf")
        if doi.startswith("10.1109/"):
            stamp = ieee_stamp(doi, urls + list(enrich.get("oa_landing") or []))
            if stamp:
                urls.insert(0, stamp)
    urls += list(enrich.get("oa_landing") or [])
    # Halaman arahan DOI penerbit berikut selalu menolak klien non-peramban
    # (403 atau tantangan JavaScript), jadi tidak dicoba.
    blocked = ("10.1016/", "10.1111/", "10.1002/", "10.1080/", "10.1177/",
               "10.1007/", "10.1145/", "10.1049/", "10.1142/", "10.1108/")
    if doi and not doi.startswith(blocked):
        urls.append(f"https://doi.org/{doi}")
    arxiv = enrich.get("arxiv_id")
    if arxiv:
        urls.append(f"https://arxiv.org/pdf/{arxiv}")
    seen, out = set(), []
    for u in urls:
        # Halaman berikut selalu memblokir klien non-peramban; lewati.
        if any(h in u for h in ("sciencedirect.com", "onlinelibrary.wiley.com",
                                "tandfonline.com", "journals.sagepub.com",
                                "www.mdpi.com", "link.springer.com")):
            continue
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", required=True, help="CSV: key, doi, title, eid")
    ap.add_argument("--enrich", help="JSONL keluaran enrich_records.py")
    ap.add_argument("--out", required=True, help="folder PDF")
    ap.add_argument("--log", required=True, help="CSV log hasil unduh")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    enrich = {}
    if args.enrich and Path(args.enrich).exists():
        for line in Path(args.enrich).read_text().splitlines():
            e = json.loads(line)
            enrich[e["eid"]] = e
    done = {}
    log_path = Path(args.log)
    if log_path.exists():
        for row in csv.DictReader(open(log_path)):
            done[row["key"]] = row
    rows = [r for r in csv.DictReader(open(args.records))
            if not (out_dir / f"{r['key']}.pdf").exists()
            and done.get(r["key"], {}).get("status") != "ok"]
    lock = threading.Lock()
    new_log = not log_path.exists()
    f = open(log_path, "a", newline="")
    w = csv.writer(f)
    if new_log:
        w.writerow(["key", "doi", "status", "source_url", "bytes", "note"])
    local = threading.local()

    def work(rec):
        if not hasattr(local, "session"):
            local.session = requests.Session()
            local.session.headers["User-Agent"] = UA
        session = local.session
        key = rec["key"]
        notes = []
        for url in candidates(session, rec, enrich.get(rec.get("eid", ""), {})):
            content, err = resolve_pdf(session, url)
            if content:
                (out_dir / f"{key}.pdf").write_bytes(content)
                with lock:
                    w.writerow([key, rec.get("doi", ""), "ok", url, len(content), ""])
                    f.flush()
                return key, True
            notes.append(f"{url[:80]}: {err}")
        with lock:
            w.writerow([key, rec.get("doi", ""), "gagal", "", 0,
                        " | ".join(notes)[:900]])
            f.flush()
        return key, False

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for key, ok in pool.map(work, rows):
            print(key, "ok" if ok else "gagal", flush=True)
    f.close()


if __name__ == "__main__":
    main()
