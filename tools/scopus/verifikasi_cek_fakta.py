#!/usr/bin/env python3
"""Lembar cek fakta naskah main6 (Pemeriksaan 6).

Memecah naskah menjadi klaim, satu baris per pasangan (klaim, kajian yang
dikutip), dan mengurutkannya menurut rencana verifikasi:

  1  baris Tabel 2 dan 3 (tab:acq, tab:assoc)
  2  abstrak dan Pendahuluan
  3  kalimat berkutipan di seksi akuisisi, mekanisme, atribut kelas, depth,
     dan sawit
  4  baris tabel tinjauan terdahulu (tab:position): cakupan dan metode
  5  kalimat berkutipan di seksi lain (kerangka, agenda, keterbatasan, simpulan)
  S  angka tanpa kutipan (hitungan korpus dari skrip): cukup dicocokkan
     dengan keluaran kode_bukti.py setelah dijalankan ulang, tidak dicek ke
     makalah

Kolom isian tangan (halaman, benar, perbaikan, catatan, oleh, tanggal) hanya
diisi manusia. Skrip tidak pernah mengisinya. Saat dijalankan ulang, isian
yang sudah ada dipertahankan menurut pasangan (kalimat, key); baris lama yang
kalimatnya sudah berubah di naskah tetap disimpan di bawah dengan prioritas
"lama" agar tidak ada isian yang hilang.

    python tools/scopus/verifikasi_cek_fakta.py
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature" / "scopus-2026-09"
SRC = ROOT / "manuscript" / "source"
BODY = SRC / "main6-body.tex"
MAIN = SRC / "main6.tex"
BIB = SRC / "references6.bib"
PDF_DIR = KORPUS / "pdf"
TEKS_DIR = KORPUS / "teks"
OUT = KORPUS / "verifikasi" / "cek_fakta.csv"

KOLOM = ["id", "prioritas", "bagian", "jenis", "kalimat", "key", "kajian",
         "pdf_ada", "teks_lokal", "halaman", "benar", "perbaikan", "catatan",
         "oleh", "tanggal"]
KOLOM_TANGAN = ["halaman", "benar", "perbaikan", "catatan", "oleh", "tanggal"]

TABEL_P1 = {"tab:acq", "tab:assoc"}
TABEL_P4 = {"tab:position"}
SEKSI_P3 = {"sec:acq", "sec:mech", "sec:class", "sec:depth", "sec:palm"}
URUT_PRIORITAS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "S": 6, "lama": 7}


def cites(teks):
    return [k.strip() for m in re.findall(r"\\cite[tp]?\{([^}]*)\}", teks)
            for k in m.split(",") if k.strip()]


def marga(penulis):
    penulis = penulis.strip()
    return (penulis.split(",")[0] if "," in penulis else penulis.split()[-1]).strip("{} ")


def baca_bib():
    kajian = {}
    for blok in re.split(r"\n@", BIB.read_text(encoding="utf-8")):
        m = re.match(r"@?\w+\{([^,]+),", blok)
        if not m:
            continue
        au = re.search(r"\bauthor\s*=\s*\{(.+?)\},?\s*\n", blok, re.S)
        th = re.search(r"\byear\s*=\s*\{?(\d{4})", blok)
        nama = "?"
        if au:
            penulis = [marga(p) for p in au.group(1).split(" and ")]
            nama = penulis[0] if len(penulis) == 1 else \
                f"{penulis[0]} & {penulis[1]}" if len(penulis) == 2 else f"{penulis[0]} dkk."
        kajian[m.group(1).strip()] = f"{nama} ({th.group(1) if th else '?'})"
    return kajian


AKSEN = {r"{\'{\i}}": "í", r"{\'{e}}": "é", r"{\'{a}}": "á", r"{\'{o}}": "ó",
         r"{\'{u}}": "ú", r"{\"{o}}": "ö", r"{\"{u}}": "ü", r"{\"{a}}": "ä",
         r"{\~{n}}": "ñ", r"{\c{c}}": "ç"}


def bersih(t):
    for a, b in AKSEN.items():
        t = t.replace(a, b)
    t = re.sub(r"\\cite[tp]?\{([^}]*)\}", lambda m: "[" + m.group(1).replace(",", ", ") + "]", t)
    t = re.sub(r"(?:Sections?|Figures?|Figs?\.|Tables?|Appendix)~\\ref\{[^}]*\}", lambda m: m.group(0).split("~")[0] + " (ref)", t)
    t = re.sub(r"\\(?:textit|textbf|emph|mathrm|text)\{([^}]*)\}", r"\1", t)
    t = t.replace("\\%", "%").replace("{,}", ",").replace("~", " ").replace("\\ ", " ")
    t = t.replace("\\dots", "...").replace("--", "–").replace("$", "")
    t = re.sub(r"\\IEEEPARstart\{(\w)\}\{\}", r"\1", t)
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    return re.sub(r"\s+", " ", t).strip()


def kalimat_dari(paragraf):
    # "et al.}\ " tidak terpotong karena karakter sebelum spasi adalah "\".
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\\])", paragraf) if s.strip()]


def ada_angka(t):
    t = re.sub(r"\\(?:cite[tp]?|ref|label)\{[^}]*\}", "", t)
    t = re.sub(r"\b(?:RQ|M|Q|G|C|E)\d\b|\bQ\d[a-e]?\b|\b(?:YOLO|v)\S*\d\S*", "", t)
    return bool(re.search(r"\d", t))


def klaim_tabel(blok, label):
    isi = blok.split("\\midrule", 1)[1].split("\\bottomrule")[0]
    for baris in isi.split("\\\\"):
        baris = baris.replace("\\midrule", "").strip()
        if not baris or baris.startswith("This review"):
            continue
        yield " | ".join(bersih(sel) for sel in baris.split("&")), cites(baris)


def susun():
    teks = BODY.read_text(encoding="utf-8")
    klaim = []  # (prioritas, bagian, jenis, kalimat_bersih, keys)

    abstrak = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}",
                        MAIN.read_text(encoding="utf-8"), re.S).group(1)
    for s in kalimat_dari(abstrak.strip()):
        klaim.append(("2", "Abstract", "abstrak", bersih(s), []))

    seksi, judul = "", ""
    for bagian in re.split(r"(\\section\{[^}]*\}\\label\{[^}]*\})", teks):
        m = re.match(r"\\section\{([^}]*)\}\\label\{([^}]*)\}", bagian)
        if m:
            judul, seksi = m.group(1), m.group(2)
            continue
        # Tabel dan gambar dipisah dari prosa.
        for blok in re.findall(r"\\begin\{table\*?\}.*?\\end\{table\*?\}", bagian, re.S):
            lab = re.search(r"\\label\{(tab:[^}]*)\}", blok)
            lab = lab.group(1) if lab else ""
            if lab in TABEL_P1 or lab in TABEL_P4:
                p = "1" if lab in TABEL_P1 else "4"
                for k, keys in klaim_tabel(blok, lab):
                    klaim.append((p, f"{judul} ({lab})", "baris_tabel", k, keys))
        prosa = re.sub(r"\\begin\{(table\*?|figure\*?|enumerate)\}.*?\\end\{\1\}", "", bagian, flags=re.S)
        for par in re.split(r"\n\s*\n", prosa):
            par = par.strip()
            if not par or par.startswith("\\subsection") and "\n" not in par:
                continue
            par = re.sub(r"^\\subsection\{[^}]*\}\s*", "", par)
            for s in kalimat_dari(par):
                keys = cites(s)
                if keys:
                    p = "2" if seksi == "sec:intro" else "3" if seksi in SEKSI_P3 else "5"
                    klaim.append((p, judul, "kalimat", bersih(s), keys))
                elif ada_angka(s):
                    p = "2" if seksi == "sec:intro" else "S"
                    klaim.append((p, judul, "angka_korpus", bersih(s), []))
    return klaim


def main():
    kajian = baca_bib()
    lama = {}
    if OUT.exists():
        with OUT.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                lama[(r["kalimat"], r["key"])] = r

    baris, dipakai = [], set()
    klaim = susun()
    klaim.sort(key=lambda k: URUT_PRIORITAS[k[0]])
    tak_dikenal = set()
    for i, (p, bagian, jenis, kal, keys) in enumerate(klaim, 1):
        for j, key in enumerate(keys or [""]):
            if key and key not in kajian:
                tak_dikenal.add(key)
            r = {"id": f"K{i:03d}" + (f"-{j + 1}" if len(keys) > 1 else ""),
                 "prioritas": p, "bagian": bagian, "jenis": jenis, "kalimat": kal,
                 "key": key, "kajian": kajian.get(key, "") if key else "",
                 "pdf_ada": ("Y" if (PDF_DIR / f"{key}.pdf").exists() else "N") if key else "",
                 "teks_lokal": (f"teks/{key}.txt" if (TEKS_DIR / f"{key}.txt").exists() else "") if key else ""}
            sebelum = lama.get((kal, key), {})
            for k in KOLOM_TANGAN:
                r[k] = sebelum.get(k, "")
            dipakai.add((kal, key))
            baris.append(r)

    yatim = [r for kk, r in lama.items() if kk not in dipakai and any(r.get(k) for k in KOLOM_TANGAN)]
    for r in yatim:
        r["prioritas"] = "lama"
        baris.append({k: r.get(k, "") for k in KOLOM})

    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLOM)
        w.writeheader()
        w.writerows(baris)

    hit = Counter(r["prioritas"] for r in baris)
    klaim_n = Counter(k[0] for k in klaim)
    print(f"{OUT.relative_to(ROOT)}: {len(baris)} baris dari {len(klaim)} klaim")
    for p in sorted(hit, key=URUT_PRIORITAS.get):
        print(f"  prioritas {p}: {klaim_n.get(p, 0)} klaim, {hit[p]} baris")
    kunci = {r["key"] for r in baris if r["key"]}
    ada_pdf = sum((PDF_DIR / f"{k}.pdf").exists() for k in kunci)
    print(f"  kajian unik dikutip: {len(kunci)}, PDF lokal: {ada_pdf}")
    if tak_dikenal:
        print("  PERINGATAN key tidak ada di references6.bib: " + ", ".join(sorted(tak_dikenal)), file=sys.stderr)
    if yatim:
        print(f"  {len(yatim)} baris berisi isian yang kalimatnya sudah berubah disimpan sebagai 'lama'")


if __name__ == "__main__":
    main()
