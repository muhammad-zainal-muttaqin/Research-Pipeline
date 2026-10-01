#!/usr/bin/env python3
"""Mencetak semua angka korpus yang dikutip naskah main6, berurutan menurut seksi.

  python tools/scopus/angka_naskah.py            # ke layar
  python tools/scopus/angka_naskah.py --simpan   # juga ke literature/scopus-2026-09/ANGKA-NASKAH.md

Angka dihitung dari berkas yang sama dengan gambar (matriks_bukti.csv, keputusan
penyaringan, kode_C3.txt), sehingga setiap angka di teks naskah dapat dicocokkan
tanpa membaca gambar. Skrip ini tidak mengubah berkas data.
"""
import csv
import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature/scopus-2026-09"
TOPIK = KORPUS / "topik"
MEK = ["M0", "M1", "M2", "M3", "M4", "M5"]
NAMA = {"M0": "no association", "M1": "statistical correction", "M2": "appearance matching",
        "M3": "temporal tracking", "M4": "geometric or 3D association", "M5": "learned association"}
METRIK = {"hitung": {"MAE", "RMSE", "R2", "MAPE/rel. error", "count accuracy"},
          "identitas": {"MOTA", "IDF1", "HOTA", "ID switch"},
          "deteksi": {"mAP/AP", "F1"}}
out = []


def tulis(s=""):
    out.append(s)


def pct(a, b):
    return f"{a} dari {b} ({100 * a / b:.0f}%)" if b else f"{a} dari 0"


def baca(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def utama(r):
    return r["tanaman"].split(";")[0] if r["tanaman"] else "(tanaman tidak disebut)"


def main():
    mat = baca(TOPIK / "bukti/matriks_bukti.csv")
    # ---------------------------------------------------------------- alur rekaman
    counts = baca(TOPIK / "counts.csv")
    diambil = sum(int(r["retrieved"]) for r in counts)
    unik = len(baca(TOPIK / "records_all.csv"))
    tj = baca(TOPIK / "penyaringan/tahap_judul.csv")
    x0 = sum(1 for r in tj if r["keputusan_judul"] == "X0")
    xj = sum(1 for r in tj if r["keputusan_judul"] == "X")
    dec, judul_saja = {}, 0
    for fn in sorted(glob.glob(str(TOPIK / "penyaringan/abstrak_*.txt"))):
        for line in open(fn, encoding="utf-8"):
            m = re.match(r"^(\d+)\s+(C[1-5]|T|R|M|X)(?:\s+(E\d))?", line)
            if m:
                dec[int(m.group(1))] = (m.group(2), m.group(3) or "")
                if "T00" in fn or "(judul)" in line:
                    judul_saja += 1
    xa = Counter(d[1] for d in dec.values() if d[0] == "X")
    inc = Counter(d[0] for d in dec.values() if d[0] != "X")
    lain = baca(TOPIK / "tambahan_metode_lain.csv") if (TOPIK / "tambahan_metode_lain.csv").exists() else []
    tulis("## Seksi 2: alur rekaman\n")
    tulis(f"- Rekaman diambil {diambil:,}; unik {unik:,}; duplikat {diambil - unik:,}")
    tulis(f"- Dibuang menurut tipe dokumen {x0}; judul disaring {unik - x0:,}; dikeluarkan di tahap judul {xj:,}")
    tulis(f"- Dinilai kelayakannya {len(dec):,} (dengan abstrak {len(dec) - judul_saja}; judul dan sumber saja {judul_saja})")
    tulis(f"- Dikeluarkan di tahap kelayakan {sum(xa.values())}: " + ", ".join(f"{k} {xa[k]}" for k in sorted(xa)))
    tulis(f"- Masuk peta dari Scopus {sum(inc.values())}: " + ", ".join(f"{k} {inc[k]}" for k in ["C1", "C2", "C3", "C4", "C5", "R", "T"]))
    tulis(f"- Metode lain {len(lain)}: " + ", ".join(f"{r['key']} ({r['kode']})" for r in lain))
    tulis(f"- Total kajian masuk {sum(inc.values()) + len(lain)}")
    th = Counter(int(r["year"]) for r in mat)
    tulis("- Kajian per tahun: " + ", ".join(f"{t}: {th[t]}" for t in sorted(th)))
    c1_th = Counter(int(r["year"]) for r in mat if r["kode"] == "C1")
    tulis("- Multi-pengamatan per tahun: " + ", ".join(f"{t}: {c1_th[t]}" for t in sorted(c1_th)))
    tulis(f"- Dengan abstrak {sum(1 for r in mat if r['ada_abstrak'] == 'ya')} dari {len(mat)}; "
          f"teks lengkap lokal {sum(1 for r in mat if (KORPUS / 'teks' / (r['key'] + '.txt')).exists())}")

    # ---------------------------------------------------------------- C1
    c1 = [r for r in mat if r["kode"] == "C1"]
    met = [r for r in c1 if r["mekanisme"] != "DATA"]
    n = len(met)
    tulis("\n## Seksi 3: kajian multi-pengamatan\n")
    tulis(f"- Multi-pengamatan {len(c1)}; makalah dataset {len(c1) - n}; kajian metode {n}")
    occ = Counter(m for r in met for m in set(r["mekanisme"].split("+")))
    tulis("- Kemunculan mekanisme: " + "; ".join(f"{NAMA[m]} {pct(occ[m], n)}" for m in ["M3", "M4", "M2", "M1", "M0", "M5"]))
    tulis(f"- Kajian yang menggabungkan mekanisme: {sum(1 for r in met if '+' in r['mekanisme'])}")
    eks = Counter("+".join(sorted(set(r["mekanisme"].split("+")))) for r in met)
    tulis("- Kategori eksklusif: " + ", ".join(f"{k} {v}" for k, v in eks.most_common()))
    ak = Counter(r["akuisisi_manual"] for r in met)
    tulis("- Akuisisi (V video, D diskret, S pindaian 3D, T kunjungan ulang, 1 satu pandang): "
          + ", ".join(f"{k} {ak[k]}" for k in ["V", "D", "S", "T", "1"]))
    for nama, a, b in [("2012-2017", 2012, 2017), ("2018-2020", 2018, 2020), ("2021-2022", 2021, 2022),
                       ("2023-2024", 2023, 2024), ("2025-2026", 2025, 2026), ("sejak 2023", 2023, 2026)]:
        s = [r for r in met if a <= int(r["year"]) <= b]
        o = Counter(m for r in s for m in set(r["mekanisme"].split("+")))
        tulis(f"- Periode {nama} (n = {len(s)}): " + ", ".join(f"{m} {o[m]} ({100 * o[m] / len(s):.0f}%)" for m in MEK if o[m]))
    tan = Counter(utama(r) for r in met)
    tulis("- Tanaman: " + ", ".join(f"{k} {v}" for k, v in tan.most_common(12)))
    tulis(f"- Melaporkan hitungan per kelas: {sum(1 for r in met if r['per_kelas'] == 'Y')} dari {n}")
    tulis("- Akuisisi x kategori mekanisme: " + "; ".join(
        f"{a}: " + ", ".join(f"{k} {v}" for k, v in Counter(
            "+".join(sorted(set(r['mekanisme'].split('+')))) for r in met if r["akuisisi_manual"] == a).most_common(5))
        for a in ["V", "D", "S", "T", "1"] if ak[a]))
    plat = Counter()
    for r in met:
        p = [x for x in r["platform"].split(";") if x]
        plat["tidak disebut" if not p else ("lebih dari satu" if len(p) > 1 else p[0])] += 1
    tulis("- Platform (satu kategori per kajian): " + ", ".join(f"{k} {v}" for k, v in plat.most_common()))
    mod = Counter(m for r in met for m in r["modalitas"].split(";"))
    tulis("- Modalitas (kemunculan): " + ", ".join(f"{k} {v}" for k, v in mod.most_common()))
    m2 = [r for r in met if "M2" in r["mekanisme"].split("+")]
    tulis(f"- Pencocokan penampilan: satu-satunya mekanisme pada {sum(1 for r in m2 if r['mekanisme'] == 'M2')}, "
          f"digabung pada {sum(1 for r in m2 if r['mekanisme'] != 'M2')}")
    for m in ["M0", "M5"]:
        tulis(f"- Kajian {NAMA[m]}: " + ", ".join(sorted(r["key"] for r in met if m in r["mekanisme"].split("+"))))
    tulis("- Makalah dataset: " + ", ".join(sorted(r["key"] for r in c1 if r["mekanisme"] == "DATA")))
    if "sumber_kode" in mat[0]:
        sk = Counter(r["sumber_kode"] or "(kosong)" for r in c1)
        tulis("- Dasar pengodean (sumber_kode): " + ", ".join(f"{k} {v}" for k, v in sk.most_common()))
        rh = Counter(x for r in met for x in r["referensi_hitung"].split(";") if x)
        tulis("- Referensi hitung (kemunculan): " + ", ".join(f"{k} {v}" for k, v in rh.most_common()))
        tm = Counter(x for r in met for x in r["tingkat_metrik"].split(";") if x)
        tulis("- Tingkat metrik menurut pengodean kajian (kemunculan): " + ", ".join(f"{k} {v}" for k, v in tm.most_common()))
        ck = Counter(r["cara_kelas"] or "(kosong)" for r in met if r["per_kelas"] == "Y")
        tulis("- Cara pemberian kelas pada kajian per kelas: " + ", ".join(f"{k} {v}" for k, v in ck.most_common()))

    ada = [r for r in met if r["ada_abstrak"] == "ya"]
    hit = Counter()
    for r in ada:
        ms = set(r["metrik"].split(";")) if r["metrik"] else set()
        for k, s in METRIK.items():
            if ms & s:
                hit[k] += 1
        if not ms:
            hit["tanpa metrik"] += 1
    tulis("\n## Seksi 5: metrik di abstrak kajian metode multi-pengamatan\n")
    tulis(f"- Dengan abstrak {len(ada)} dari {n}: " + "; ".join(f"{k} {pct(hit[k], len(ada))}" for k in ["hitung", "deteksi", "identitas", "tanpa metrik"]))

    # ---------------------------------------------------------------- C4, C5
    c4 = [r for r in mat if r["kode"] == "C4"]
    tulis("\n## Seksi 6: pencacahan per kelas pada citra tunggal\n")
    tulis(f"- Kajian {len(c4)}; tanaman: " + ", ".join(f"{k} {v}" for k, v in Counter(utama(r) for r in c4).most_common(6)))
    tulis(f"- Atribut kelas kematangan: {sum(1 for r in c4 if 'maturity' in r['atribut_kelas'].split(';'))}")
    c5 = [r for r in mat if r["kode"] == "C5"]
    tulis("\n## Seksi 7: kedalaman dan sensor lain\n")
    tulis(f"- Kajian {len(c5)}; modalitas (kemunculan): " + ", ".join(f"{k} {v}" for k, v in Counter(m for r in c5 for m in r["modalitas"].split(";")).most_common()))
    tulis("- Tanaman: " + ", ".join(f"{k} {v}" for k, v in Counter(utama(r) for r in c5).most_common(5)))

    # ---------------------------------------------------------------- C3
    c3 = {}
    for line in open(TOPIK / "bukti/kode_C3.txt", encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("\t")
        c3[int(p[0])] = p[1:6]
    tulis("\n## Seksi 8: kelapa sawit\n")
    tulis(f"- Kajian {len(c3)} (matriks: {sum(1 for r in mat if r['kode'] == 'C3')})")
    tulis("- Tugas: " + ", ".join(f"{k} {v}" for k, v in Counter(v[0] for v in c3.values()).most_common()))
    tulis("- Lokasi: " + ", ".join(f"{k} {v}" for k, v in Counter(v[1] for v in c3.values()).most_common()))
    tulis("- Modalitas: " + ", ".join(f"{k} {v}" for k, v in Counter(v[2] for v in c3.values()).most_common()))
    tulis(f"- Multipandang Y: {sum(1 for v in c3.values() if v[3] == 'Y')}; kelas per instans Y: {sum(1 for v in c3.values() if v[4] == 'Y')}")
    key = {int(r["idx"]): r["key"] for r in mat}
    tulis("- Kajian pencacahan (HIT): " + ", ".join(sorted(key.get(i, str(i)) for i, v in c3.items() if v[0] == "HIT")))
    tulis("- Kajian multipandang: " + ", ".join(sorted(key.get(i, str(i)) for i, v in c3.items() if v[3] == "Y")))

    tulis("\n## Seksi 9: tinjauan terdahulu dan metode luar pertanian\n")
    tulis(f"- Tinjauan terdahulu {inc['R']} (+ {sum(1 for r in lain if r['kode'] == 'R')} metode lain); metode luar pertanian {inc['T']}")

    teks = "\n".join(out) + "\n"
    print(teks)
    if "--simpan" in sys.argv:
        kepala = ("# Angka Naskah `main6`\n\nDibuat `tools/scopus/angka_naskah.py`; jangan disunting tangan. "
                  "Setiap angka korpus di naskah harus cocok dengan berkas ini.\n\n")
        (KORPUS / "ANGKA-NASKAH.md").write_text(kepala + teks, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
