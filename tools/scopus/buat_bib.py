#!/usr/bin/env python3
"""Membuat berkas BibTeX dari rekaman Scopus yang lolos penyaringan.

Scopus (tampilan STANDARD) hanya memberi penulis pertama, jadi daftar penulis
lengkap, volume, nomor, dan halaman diambil dari Crossref berdasarkan DOI.
Rekaman tanpa DOI memakai metadata Scopus apa adanya. Respons Crossref disimpan
di berkas cache agar skrip dapat diulang tanpa memanggil API lagi.

Contoh:
  python3 tools/scopus/buat_bib.py --rekaman literature/scopus-2026-09/topik/records_all.csv \
      --kunci literature/scopus-2026-09/topik/bukti/matriks_bukti.csv \
      --cache literature/scopus-2026-09/topik/crossref.jsonl --keluar manuscript/source/references6.bib
"""
import argparse
import html
import csv
import json
import re
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from latex_teks import ke_latex

MAILTO = "research-pipeline@users.noreply.github.com"


def ambil_crossref(doi):
    url = f"https://api.crossref.org/works/{doi}"
    for _ in range(3):
        try:
            r = requests.get(url, params={"mailto": MAILTO}, timeout=40)
        except requests.RequestException:
            time.sleep(2)
            continue
        if r.status_code == 200:
            return r.json().get("message", {})
        if r.status_code == 404:
            return {}
        time.sleep(2)
    return None


LATEX_KHUSUS = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_"}


def bersihkan(teks):
    teks = teks or ""
    while html.unescape(teks) != teks:
        teks = html.unescape(teks)
    teks = re.sub(r"<[^>]+>", "", teks)
    teks = re.sub(r"\s+", " ", teks).strip()
    return "".join(LATEX_KHUSUS.get(c, c) for c in teks)


def judul_terlindung(teks):
    """Lindungi singkatan huruf besar agar tidak diubah gaya bibliografi."""
    return re.sub(r"\b([A-Za-z]*[A-Z][A-Za-z]*[A-Z0-9][A-Za-z0-9-]*)\b", r"{\1}", bersihkan(teks))


def penulis_crossref(msg):
    out = []
    for a in msg.get("author", []) or []:
        fam, giv = a.get("family"), a.get("given")
        if fam and giv:
            out.append(f"{bersihkan(fam)}, {bersihkan(giv)}")
        elif fam:
            out.append(bersihkan(fam))
        elif a.get("name") and not re.search(r"Department|Faculty|Universit|Institute|School of",
                                              a["name"]):
            out.append("{" + bersihkan(a["name"]) + "}")
    return out


def entri(rec, msg):
    key = rec["key"]
    doi = rec.get("doi", "")
    tipe_scopus = rec.get("source_type", "")
    ct = (msg or {}).get("type", "")
    konf = ct in ("proceedings-article",) or tipe_scopus == "Conference Proceeding"
    buku = ct in ("book-chapter", "book") or tipe_scopus in ("Book", "Book Series")
    jenis = "inproceedings" if konf else ("incollection" if buku else "article")
    f = {}
    judul = ((msg or {}).get("title") or [rec["title"]])[0]
    f["title"] = judul_terlindung(judul)
    aut = penulis_crossref(msg or {})
    if not aut:
        fa = rec.get("first_author", "")
        m = re.match(r"(.+?)\s+([A-Z][A-Za-z.\- ]*)$", fa)
        aut = [f"{bersihkan(m.group(1))}, {m.group(2)}" if m else bersihkan(fa), "others"]
    f["author"] = " and ".join(aut)
    wadah = ((msg or {}).get("container-title") or [rec.get("source", "")])
    wadah = bersihkan(wadah[0] if wadah else rec.get("source", ""))
    if jenis == "article":
        f["journal"] = wadah
    else:
        f["booktitle"] = wadah
    f["year"] = rec.get("year", "")
    vol = (msg or {}).get("volume") or rec.get("volume", "")
    num = (msg or {}).get("issue") or rec.get("issue", "")
    hal = (msg or {}).get("page") or rec.get("pages", "") or rec.get("article_number", "")
    if vol:
        f["volume"] = bersihkan(vol)
    if num and jenis == "article":
        f["number"] = bersihkan(num)
    if hal:
        f["pages"] = bersihkan(hal).replace("-", "--")
    if doi:
        f["doi"] = doi
    f["scopuseid"] = rec["eid"]
    isi = ",\n".join(f"  {k} = {{{v}}}" for k, v in f.items())
    return ke_latex(f"@{jenis}{{{key},\n{isi}\n}}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rekaman", nargs="+", required=True,
                    help="CSV rekaman Scopus (records_all.csv, terpilih.csv, ...)")
    ap.add_argument("--kunci", nargs="+", required=True,
                    help="CSV berkolom key dan eid yang dimasukkan ke BibTeX")
    ap.add_argument("--cache", required=True)
    ap.add_argument("--keluar", required=True)
    args = ap.parse_args()

    rec = {}
    for p in args.rekaman:
        for r in csv.DictReader(open(p)):
            rec[r["eid"]] = r
    pilih = {}
    for p in args.kunci:
        for r in csv.DictReader(open(p)):
            if r.get("eid") in rec:
                d = dict(rec[r["eid"]])
                d["key"] = r["key"]
                pilih[r["key"]] = d
    cache = {}
    cp = Path(args.cache)
    if cp.exists():
        for line in cp.read_text().splitlines():
            c = json.loads(line)
            cache[c["doi"]] = c["msg"]
    butuh = sorted({d["doi"] for d in pilih.values() if d.get("doi") and d["doi"] not in cache})
    print("ambil Crossref:", len(butuh))
    with ThreadPoolExecutor(max_workers=6) as pool, open(cp, "a") as fc:
        for doi, msg in zip(butuh, pool.map(ambil_crossref, butuh)):
            if msg is None:
                continue
            keep = {k: msg.get(k) for k in ("type", "title", "author", "container-title",
                                            "volume", "issue", "page")}
            cache[doi] = keep
            fc.write(json.dumps({"doi": doi, "msg": keep}) + "\n")
    with open(args.keluar, "w") as f:
        f.write("% Dibuat oleh tools/scopus/buat_bib.py dari rekaman Scopus dan metadata Crossref.\n\n")
        for key in sorted(pilih):
            d = pilih[key]
            f.write(entri(d, cache.get(d.get("doi", ""))) + "\n")
    print(len(pilih), "entri ->", args.keluar)


if __name__ == "__main__":
    main()
