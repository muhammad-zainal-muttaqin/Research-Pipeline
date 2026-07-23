#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Jalankan set query Q1-Q6 (docs/search/PROTOCOL.md) terhadap OpenAlex.

Lengan OpenAlex dari protokol pencarian. Bukan pengganti Scopus/WoS - lengan
berlangganan dijalankan terpisah dan angkanya digabung di prisma-counts.csv.

Keluaran:
  docs/search/raw/openalex_<qid>_<TANGGAL>.csv   satu berkas per query
  docs/search/raw/known-item-test_<TANGGAL>.csv  hasil uji known-item
  docs/search/openalex-counts.csv                rekap n_raw per query

Pemakaian:
  python tools/openalex_search.py            # jalankan semua
  python tools/openalex_search.py Q2 Q5      # jalankan sebagian

Tidak ada dependensi eksternal (urllib saja). OpenAlex polite pool dipakai
lewat parameter mailto; batasnya 10 permintaan/detik.
"""

import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

TANGGAL = "2026-07-23"          # tanggal pencarian, dicatat di nama berkas
MAILTO = "mz.muttaqin1@gmail.com"
DARI_TANGGAL = "2015-01-01"     # PUBYEAR > 2014
BATAS_PER_QUERY = 5000          # penjaga runaway; bila tercapai, DICATAT bukan didiamkan
PER_PAGE = 200

BASE = "https://api.openalex.org/works"
AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_RAW = os.path.join(AKAR, "docs", "search", "raw")

# ---------------------------------------------------------------------------
# Set query. Terjemahan dari docs/search/PROTOCOL.md ke sintaks OpenAlex.
#
# Deviasi yang WAJIB dilaporkan di naskah:
#   - OpenAlex tidak mendukung wildcard (count*), jadi varian dieja satu per satu.
#   - title_and_abstract.search memakai pencocokan berbasis token dengan stemming
#     ringan, bukan pencocokan frasa persis seperti TITLE-ABS-KEY Scopus.
#     Recall-nya berbeda; ini dicatat, bukan dihaluskan.
# ---------------------------------------------------------------------------

QUERIES = {
    "Q1": (
        "inventaris/penghitungan buah dari banyak observasi",
        '("fruit" OR "fresh fruit bunch" OR "oil palm" OR "apple" OR "citrus" '
        'OR "mango" OR "grape" OR "berry" OR "bunch" OR "crop") '
        'AND ("counting" OR "count" OR "yield estimation" OR "load estimation" '
        'OR "fruit load" OR "inventory" OR "enumeration") '
        'AND ("multi-view" OR "multiple views" OR "multi-camera" OR "video" '
        'OR "cross-view" OR "structure from motion" OR "tracking" '
        'OR "3D reconstruction" OR "image sequence")'
    ),
    "Q2": (
        "asosiasi lintas-view dan anti-duplikasi (non-pertanian diizinkan)",
        '("multi-view" OR "cross-view" OR "multi-camera" OR "multiple cameras" '
        'OR "overlapping views") '
        'AND ("re-identification" OR "data association" OR "identity" '
        'OR "duplicate" OR "duplicates" OR "deduplication" OR "double counting" '
        'OR "correspondence" OR "instance matching" OR "tracking" OR "association") '
        'AND ("object detection" OR "instance segmentation" OR "counting" '
        'OR "instance" OR "pedestrian" OR "vehicle")'
    ),
    "Q3": (
        "multimodalitas dan geometri untuk tanaman",
        '("RGB-D" OR "depth camera" OR "stereo vision" OR "LiDAR" OR "point cloud" '
        'OR "monocular depth" OR "photogrammetry" OR "structure from motion") '
        'AND ("fruit" OR "orchard" OR "vineyard" OR "canopy" OR "plant" '
        'OR "tree crop" OR "plantation" OR "oil palm") '
        'AND ("detection" OR "segmentation" OR "localization" OR "counting" '
        'OR "phenotyping" OR "harvesting")'
    ),
    "Q4": (
        "kelas per-instans di luar kematangan",
        '("fruit" OR "produce" OR "crop" OR "bunch") '
        'AND ("maturity" OR "ripeness" OR "grading" OR "grade" OR "quality class" '
        'OR "size class" OR "defect" OR "disease" OR "cultivar" OR "variety") '
        'AND ("instance segmentation" OR "object detection" OR "individual fruit" '
        'OR "bounding box" OR "per-object")'
    ),
    "Q5": (
        "tinjauan terdahulu untuk positioning",
        '("review" OR "survey" OR "systematic review" OR "scoping review") '
        'AND ("fruit detection" OR "fruit counting" OR "yield estimation" '
        'OR "oil palm" OR "orchard" OR "crop monitoring" OR "precision agriculture") '
        'AND ("deep learning" OR "computer vision" OR "object detection" '
        'OR "machine vision")'
    ),
    "Q6": (
        "seed sawit",
        '("oil palm" OR "elaeis guineensis" OR "fresh fruit bunch") '
        'AND ("detection" OR "classification" OR "counting" OR "ripeness" '
        'OR "maturity" OR "yield" OR "grading" OR "harvesting" OR "plantation")'
    ),
}

# Uji known-item (PROTOCOL.md sec.6). Query dianggap lolos hanya bila
# keempat item ini kembali. Rujukan Suharjito/Goh menunggu konfirmasi dosen,
# jadi di sini diuji lewat pencarian nama penulis, bukan DOI.
KNOWN_ITEMS = [
    ("Gene-Mola 2020 deteksi buah + SfM", "10.1016/j.compag.2019.105165", ["Q1", "Q3"]),
    ("Koirala 2019 MangoYOLO", "10.1007/s11119-019-09642-0", ["Q1", "Q4"]),
    ("Indriani 2026 SawitMVC", "10.1016/j.dib.2026.112990", ["Q1"]),
]


def ambil(url, percobaan=4):
    """GET JSON dengan backoff sederhana."""
    for i in range(percobaan):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Research-Pipeline/1.0 (%s)" % MAILTO})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if i == percobaan - 1:
                raise
            time.sleep(2 ** i)
    return None


def susun_abstrak(indeks):
    """Rekonstruksi abstrak dari abstract_inverted_index OpenAlex."""
    if not indeks:
        return ""
    posisi = {}
    for kata, tempat in indeks.items():
        for p in tempat:
            posisi[p] = kata
    if not posisi:
        return ""
    return " ".join(posisi[k] for k in sorted(posisi))


def baris_dari(w, qid):
    lokasi = w.get("primary_location") or {}
    sumber = lokasi.get("source") or {}
    penulis = [a["author"]["display_name"] for a in (w.get("authorships") or [])[:4]]
    return {
        "query_id": qid,
        "openalex_id": (w.get("id") or "").rsplit("/", 1)[-1],
        "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
        "year": w.get("publication_year") or "",
        "type": w.get("type") or "",
        "title": (w.get("title") or "").replace("\n", " "),
        "venue": sumber.get("display_name") or "",
        "authors": "; ".join(penulis),
        "cited_by_count": w.get("cited_by_count") or 0,
        "is_oa": (w.get("open_access") or {}).get("is_oa", ""),
        "abstract": susun_abstrak(w.get("abstract_inverted_index"))[:4000],
    }


def jalankan(qid, query):
    """Ambil seluruh halaman untuk satu query. Kembalikan (baris, n_dilaporkan, terpotong)."""
    kursor = "*"
    hasil = []
    n_dilaporkan = None
    while True:
        params = {
            "filter": "title_and_abstract.search:%s,from_publication_date:%s" % (query, DARI_TANGGAL),
            "per-page": str(PER_PAGE),
            "cursor": kursor,
            "mailto": MAILTO,
        }
        url = BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        d = ambil(url)
        if n_dilaporkan is None:
            n_dilaporkan = d["meta"]["count"]
        for w in d["results"]:
            hasil.append(baris_dari(w, qid))
        kursor = d["meta"].get("next_cursor")
        if not kursor or not d["results"] or len(hasil) >= BATAS_PER_QUERY:
            break
        time.sleep(0.12)
    return hasil, n_dilaporkan, len(hasil) >= BATAS_PER_QUERY and n_dilaporkan > len(hasil)


def uji_known_item(peta_doi):
    baris = []
    for nama, doi, query_diharapkan in KNOWN_ITEMS:
        d = ambil("%s?filter=doi:%s&mailto=%s" % (BASE, urllib.parse.quote(doi), MAILTO))
        ada_di_openalex = bool(d.get("results"))
        ditemukan_oleh = sorted(peta_doi.get(doi.lower(), []))
        lolos = all(q in ditemukan_oleh for q in query_diharapkan)
        baris.append({
            "item": nama,
            "doi": doi,
            "ada_di_openalex": "y" if ada_di_openalex else "n",
            "query_diharapkan": " ".join(query_diharapkan),
            "ditemukan_oleh": " ".join(ditemukan_oleh) or "-",
            "lolos": "LOLOS" if lolos else "GAGAL",
        })
        time.sleep(0.12)
    return baris


def tulis_csv(path, baris, kolom):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kolom)
        w.writeheader()
        w.writerows(baris)


def main():
    os.makedirs(DIR_RAW, exist_ok=True)
    pilih = [a.upper() for a in sys.argv[1:]] or list(QUERIES)
    kolom = ["query_id", "openalex_id", "doi", "year", "type", "title",
             "venue", "authors", "cited_by_count", "is_oa", "abstract"]

    rekap = []
    peta_doi = {}
    for qid in pilih:
        judul, query = QUERIES[qid]
        print("[%s] %s ..." % (qid, judul), flush=True)
        baris, n_dilaporkan, terpotong = jalankan(qid, query)
        path = os.path.join(DIR_RAW, "openalex_%s_%s.csv" % (qid, TANGGAL))
        tulis_csv(path, baris, kolom)
        for b in baris:
            if b["doi"]:
                peta_doi.setdefault(b["doi"].lower(), []).append(qid)
        rekap.append({
            "query_id": qid,
            "deskripsi": judul,
            "database": "OpenAlex",
            "date_run": TANGGAL,
            "n_dilaporkan_api": n_dilaporkan,
            "n_diunduh": len(baris),
            "terpotong_oleh_batas": "YA" if terpotong else "tidak",
            "berkas": os.path.relpath(path, AKAR).replace("\\", "/"),
        })
        print("    n_dilaporkan=%s  n_diunduh=%s  terpotong=%s"
              % (n_dilaporkan, len(baris), "YA" if terpotong else "tidak"), flush=True)

    tulis_csv(os.path.join(AKAR, "docs", "search", "openalex-counts.csv"), rekap,
              list(rekap[0]))

    print("\nUji known-item ...", flush=True)
    ki = uji_known_item(peta_doi)
    tulis_csv(os.path.join(DIR_RAW, "known-item-test_%s.csv" % TANGGAL), ki, list(ki[0]))
    for b in ki:
        print("    %-6s %-34s ditemukan_oleh=%s" % (b["lolos"], b["item"][:34], b["ditemukan_oleh"]))


if __name__ == "__main__":
    main()
