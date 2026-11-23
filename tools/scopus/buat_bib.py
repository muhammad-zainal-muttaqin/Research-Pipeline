#!/usr/bin/env python3
"""Membuat berkas BibTeX dari rekaman Scopus yang lolos penyaringan.

Scopus (tampilan STANDARD) hanya memberi penulis pertama, jadi daftar penulis
lengkap, volume, nomor, dan halaman diambil dari Crossref berdasarkan DOI.
Bila Crossref tidak memberi penulis, DOI, atau halaman, OpenAlex dipakai (lewat
DOI, atau lewat judul yang sama persis dengan tahun yang sama). Daftar penulis yang
dibaca dari PDF (--penulis-pdf) menggantikan daftar dari kedua layanan itu. Respons kedua
layanan disimpan di berkas cache agar skrip dapat diulang tanpa memanggil API lagi.

Contoh:
  python3 tools/scopus/buat_bib.py --rekaman literature/scopus-2026-09/topik/records_all.csv \
      --kunci literature/scopus-2026-09/topik/bukti/matriks_bukti.csv \
      --cache literature/scopus-2026-09/crossref.jsonl --cache-openalex literature/scopus-2026-09/openalex.jsonl \
      --penulis-pdf literature/scopus-2026-09/penulis_pdf.tsv \
      --keluar manuscript/source/references6.bib
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

from latex_teks import ke_latex, tanpa_em_dash

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


def ambil_openalex(rec):
    doi = rec.get("doi", "")
    if doi:
        url, params = f"https://api.openalex.org/works/doi:{doi}", {}
    else:
        url, params = "https://api.openalex.org/works", {"filter": "title.search:" + re.sub(r"[,:|]", " ", rec["title"])[:200], "per-page": 5}
    params["mailto"] = MAILTO
    for _ in range(3):
        try:
            r = requests.get(url, params=params, timeout=40)
        except requests.RequestException:
            time.sleep(2)
            continue
        if r.status_code == 404:
            return {}
        if r.status_code == 200:
            hasil = r.json()
            if doi:
                return hasil
            for w in hasil.get("results", []):
                if judul_normal(w.get("title")) == judul_normal(rec["title"]) and str(w.get("publication_year")) == rec.get("year"):
                    return w
            return {}
        time.sleep(2)
    return None


def judul_normal(teks):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", teks or "").lower())


def penulis_openalex(w):
    out = []
    for a in (w or {}).get("authorships") or []:
        nama = (a.get("author") or {}).get("display_name") or a.get("raw_author_name") or ""
        bagian = nama.split()
        if len(bagian) >= 2:
            out.append(f"{bersihkan(bagian[-1])}, {bersihkan(' '.join(bagian[:-1]))}")
        elif bagian:
            out.append(bersihkan(bagian[0]))
    return out


LATEX_KHUSUS = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_"}


def bersihkan(teks):
    teks = teks or ""
    while html.unescape(teks) != teks:
        teks = html.unescape(teks)
    teks = re.sub(r"<[^>]+>", "", teks)
    teks = re.sub(r"\s+", " ", teks).strip()
    return "".join(LATEX_KHUSUS.get(c, c) for c in teks)


NAMA_DIRI = ["Kalman", "Gaussian", "Hungarian", "Hough", "Fuji", "Kinect", "Azure", "Raspberry Pi", "Mamba",
             "Egyptian", "Australian", "Brazilian", "Chinese", "Indian", "Peruvian", "Indonesia", "Florida",
             "America", "Latin", "Tacna", "Medan", "Sumatera", "Batu", "Boolean", "Elaeis", "Gossypium",
             "Lycopersicon", "Malus", "Pyrus", "Solanum", "Prunoideae", "Xanthoceras", "Jacq", "Blanco"]


def judul_terlindung(teks):
    """Lindungi singkatan huruf besar, angka-huruf (3D), dan nama diri agar tidak diubah gaya bibliografi."""
    teks = re.sub(r"\b([A-Za-z]*[A-Z][A-Za-z]*[A-Z0-9][A-Za-z0-9-]*|\d+[A-Z][A-Za-z0-9-]*)\b", r"{\1}", bersihkan(teks))
    for nama in NAMA_DIRI:
        teks = re.sub(rf"(?<![{{\w])({re.escape(nama)})\b", r"{\1}", teks)
    return teks


# Singkatan yang dipulihkan setelah judul berhuruf kapital semua diturunkan.
SINGKATAN = [(r"\bfaster r-cnn\b", "Faster R-CNN"), (r"\byolov(\d+)\b", r"YOLOv\1"), (r"\bcnn\b", "CNN"),
             (r"\bcmle-yolo\b", "CMLE-YOLO"), (r"\befficientdet-lite\b", "EfficientDet-Lite"),
             (r"^Sam 2: segment", "SAM 2: Segment")]


def huruf_wajar(teks):
    """Nama atau judul yang seluruhnya kapital diubah ke kapital awal kata."""
    if teks and teks == teks.upper() and re.search(r"[A-Z]{3}", teks):
        return " ".join(w.capitalize() if len(w) > 2 else w for w in teks.split(" "))
    return teks


DIAKRITIK = {"Hani": "Häni", "Braso": "Brasó", "Leal-Taixe": "Leal-Taixé"}


def rapikan_nama(fam, giv):
    """Perbaiki nama dari Crossref: kapital semua, titik tersisa, inisial di kolom marga, diakritik hilang."""
    fam, giv = huruf_wajar(fam.strip()), huruf_wajar((giv or "").strip())
    fam = DIAKRITIK.get(fam, fam)
    if re.fullmatch(r"[A-Z]{2}", fam):  # marga dua huruf (XU, LV), bukan inisial
        fam = fam.capitalize()
    giv = re.sub(r"(?<=[a-z]{2})\.$", "", giv)
    if giv and re.fullmatch(r"[A-Z](?:[. ]+[A-Z])*\.?", fam) and re.fullmatch(r"[A-Z][a-z]{2,}", giv):
        fam, giv = giv, fam
    return fam, giv


def penulis_crossref(msg):
    out = []
    for a in msg.get("author", []) or []:
        fam, giv = a.get("family"), a.get("given")
        if fam:
            fam, giv = rapikan_nama(fam, giv)
        if fam and giv:
            out.append(f"{bersihkan(fam)}, {bersihkan(giv)}")
        elif fam:
            out.append(bersihkan(fam))
        elif a.get("name") and not re.search(r"Department|Faculty|Universit|Institute|School of",
                                              a["name"]):
            out.append("{" + bersihkan(a["name"]) + "}")
    return out


def entri(rec, msg, oa=None, penulis_pdf=None):
    key = rec["key"]
    doi = rec.get("doi", "")
    tipe_scopus = rec.get("source_type", "")
    ct = (msg or {}).get("type", "")
    konf = ct in ("proceedings-article",) or tipe_scopus == "Conference Proceeding"
    buku = ct in ("book-chapter", "book") or tipe_scopus in ("Book", "Book Series")
    jenis = "inproceedings" if konf else ("incollection" if buku else "article")
    f = {}
    judul = ((msg or {}).get("title") or [rec["title"]])[0]
    if judul == judul.upper() and re.search(r"[A-Z]{3}", judul):
        judul = judul.capitalize()
        for pola, ganti in SINGKATAN:
            judul = re.sub(pola, ganti, judul)
    f["title"] = judul_terlindung(tanpa_em_dash(judul))
    aut = penulis_pdf or penulis_crossref(msg or {}) or penulis_openalex(oa)
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
    if not hal and oa:
        b = oa.get("biblio") or {}
        hal = "-".join(x for x in (b.get("first_page"), b.get("last_page")) if x)
    if vol:
        f["volume"] = bersihkan(vol)
    if num and jenis == "article":
        f["number"] = bersihkan(num)
    if hal:
        f["pages"] = bersihkan(hal).replace("-", "--")
    if not doi and oa and oa.get("doi"):
        doi = oa["doi"].replace("https://doi.org/", "")
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
    ap.add_argument("--cache-openalex", required=True)
    ap.add_argument("--penulis-pdf", required=True,
                    help="TSV kunci, penulis (format BibTeX), tempat dibaca di PDF")
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
    def kurang(d):
        msg = cache.get(d.get("doi", "")) or {}
        return not msg.get("author") or not d.get("doi") or not (msg.get("page") or d.get("pages") or d.get("article_number"))
    oa = {}
    op = Path(args.cache_openalex)
    if op.exists():
        for line in op.read_text().splitlines():
            c = json.loads(line)
            oa[c["key"]] = c["work"]
    butuh = [d for k, d in sorted(pilih.items()) if kurang(d) and k not in oa]
    print("ambil OpenAlex:", len(butuh))
    with open(op, "a") as fo:
        for d in butuh:
            w = ambil_openalex(d)
            if w is None:
                continue
            keep = {k: w.get(k) for k in ("doi", "title", "publication_year", "authorships", "biblio")}
            oa[d["key"]] = keep
            fo.write(json.dumps({"key": d["key"], "work": keep}) + "\n")
            time.sleep(0.2)
    pdf_aut = {}
    for line in open(args.penulis_pdf, encoding="utf-8"):
        if line.strip() and not line.startswith("#"):
            k, aut, _ = line.rstrip("\n").split("\t")
            pdf_aut[k] = aut.split(" and ")
    assert set(pdf_aut) <= set(pilih), f"kunci penulis_pdf tanpa rekaman: {sorted(set(pdf_aut) - set(pilih))}"
    with open(args.keluar, "w", newline="\n") as f:
        f.write("% Dibuat oleh tools/scopus/buat_bib.py dari rekaman Scopus, Crossref, dan OpenAlex.\n\n")
        for key in sorted(pilih):
            d = pilih[key]
            f.write(entri(d, cache.get(d.get("doi", "")), oa.get(key), pdf_aut.get(key)) + "\n")
    print(len(pilih), "entri ->", args.keluar)


if __name__ == "__main__":
    main()
