#!/usr/bin/env python3
"""Bangun tabel sintesis LaTeX (satu baris per studi) dari matriks bukti.

Masukan : docs/audit/evidence-matrix-182.csv
Keluaran: docs/manuscript/source/appendix-synthesis.tex

Tabel ini memenuhi butir 8 revisi dosen (2026-07-23): matriks bukti harus masuk
ke dalam makalah sebagai tabel sintesis, bukan hanya sebagai berkas CSV terpisah.

Kolom prosa panjang (method_or_contribution, dataset_or_evaluation_context,
limitations; rerata 460 karakter) tidak dimuat di tabel karena akan menjadi
puluhan halaman. Kolom-kolom itu tetap tersedia di CSV suplemen.

Jalankan ulang setiap kali matriks berubah:
    python reproduce/tools/build_synthesis_table.py
"""

import csv
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "docs" / "audit" / "evidence-matrix-182.csv"
OUT = ROOT / "docs" / "manuscript" / "source" / "appendix-synthesis.tex"

# domain_theme di CSV ditulis dalam Bahasa Indonesia; naskah berbahasa Inggris
# memakai tujuh belas kode tema yang disebut di evidence-body.tex Seksi 2.
THEME_EN = {
    "Fondasi RGB": "General RGB detection",
    "Estimasi Kedalaman": "Monocular depth",
    "RGB-D SOD": "RGB-D salient obj.",
    "Deteksi 3D": "3D detection",
    "Segmentasi RGB-D": "RGB-D segmentation",
    "Pose 6D": "6D pose",
    "Grasp Robotik": "Robotic grasping",
    "Survei YOLO": "YOLO surveys/variants",
    "RGB-D SLAM": "RGB-D SLAM",
    "Pedestrian RGB-T": "Pedestrian RGB-T",
    "Dataset": "Benchmark datasets",
    "YOLO plus RGB-D": "YOLO with RGB-D",
    "Remote Sensing": "Remote sensing",
    "Fusi Multimodal": "Multimodal fusion",
    "Pertanian": "Agriculture",
    "Medis": "Medical",
    "Industri": "Industrial",
    "Uncoded": "Uncoded",
}

TASK_SHORT = {
    "Computer-vision method or application": "CV method",
    "Segmentation / salient-object perception": "Segmentation",
    "2D object detection / real-time detection": "2D detection",
    "Depth estimation or depth-aware perception": "Depth",
    "6D pose estimation or robotic grasping": "Pose, grasp",
    "3D detection or localization": "3D detection",
    "Visual localization / mapping": "SLAM",
}

# tbs_relevance adalah tiga kalimat baku; dipendekkan menjadi label tingkat bukti
# yang sama dengan aturan interpretasi di evidence-body.tex Seksi 2.2.
EVIDENCE_SHORT = {
    "Direct agricultural or fruit-transfer evidence; not automatically TBS evidence.": "Direct",
    "Transferable evidence for depth reliability, fusion, geometry, or de-duplication; requires TBS field validation.": "Transferable",
    "Baseline or methodological evidence; requires TBS-specific validation.": "Baseline",
}

TITLE_MAXLEN = 62

LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def esc(text):
    """Lolos-kan karakter khusus LaTeX."""
    return "".join(LATEX_ESCAPES.get(ch, ch) for ch in text)


def shorten(text, limit):
    """Potong pada batas kata, tambahkan elipsis bila terpotong."""
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "\\,\\ldots"


def lookup(mapping, key, unknown):
    """Ambil nilai peta; catat kunci tak dikenal alih-alih diam-diam melewatinya."""
    if key not in mapping:
        unknown.add(key)
        return esc(key)
    return mapping[key]


def main():
    if not SRC.exists():
        sys.exit(f"Matriks bukti tidak ditemukan: {SRC}")

    with SRC.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    unknown = set()
    lines = []
    for r in rows:
        title = shorten(esc(r["title"]), TITLE_MAXLEN)
        theme = lookup(THEME_EN, r["domain_theme"], unknown)
        task = lookup(TASK_SHORT, r["task"], unknown)
        evidence = lookup(EVIDENCE_SHORT, r["tbs_relevance"].strip(), unknown)
        lines.append(
            "{id} & {title} & {yr} & {theme} & {task} & {mod} & {ev} & \\cite{{{key}}} \\\\".format(
                id=esc(r["source_id"]),
                title=title,
                yr=esc(r["year"]),
                theme=theme,
                task=task,
                mod=esc(r["modality"]),
                ev=evidence,
                key=r["bibtex_key"].strip(),
            )
        )

    if unknown:
        print("PERINGATAN: nilai tanpa pemetaan (dipakai apa adanya):", file=sys.stderr)
        for value in sorted(unknown):
            print("  -", value, file=sys.stderr)

    uncoded = sum(1 for r in rows if r["domain_theme"] == "Uncoded")
    # Kalimat tidak boleh diawali angka.
    numerals = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
    uncoded_word = numerals.get(uncoded, str(uncoded))

    header = (
        "ID & Study (short title) & Yr & Thematic domain & Task & Modality & "
        "Evidence level & Ref. \\\\"
    )

    body = "\n".join(lines)
    OUT.write_text(
        f"""% DIBANGKITKAN OTOMATIS oleh reproduce/tools/build_synthesis_table.py --- jangan disunting tangan.
% Sumber: docs/audit/evidence-matrix-182.csv ({len(rows)} baris)
% Tabel ini butuh lebar penuh. Simpan dulu status kolom dokumen agar daftar
% pustaka setelahnya kembali dua kolom pada IEEEtran, dan tetap satu kolom pada
% elsarticle.
\\makeatletter
\\newif\\ifrestoretwocol
\\if@twocolumn\\restoretwocoltrue\\fi
\\makeatother
\\clearpage
\\onecolumn
\\section*{{Appendix A. Evidence synthesis matrix}}
\\label{{app:matrix}}

Table~\\ref{{tab:matrix}} lists every one of the {len(rows)} verified primary sources
with the coding used throughout this review: thematic domain, task, input modality,
and the evidence level defined in Section~\\ref{{sec:rules}}. Each row corresponds to
one source, and each source was read from its full text. {uncoded_word} sources carry
no thematic code and are shown as \\textit{{Uncoded}}. The longer prose fields recorded
during coding (method or contribution, evaluation context, reported finding, stated
limitations, and transfer boundary) are omitted here for length and are supplied in
the accompanying machine-readable supplement.

{{\\small
\\sloppy
\\setlength{{\\tabcolsep}}{{3pt}}
\\renewcommand{{\\arraystretch}}{{1.12}}
\\begin{{longtable}}{{@{{}}>{{\\raggedright\\arraybackslash}}p{{0.030\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.170\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.045\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.165\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.115\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.105\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.120\\textwidth}}>{{\\raggedright\\arraybackslash}}p{{0.045\\textwidth}}@{{}}}}
\\caption{{Evidence synthesis matrix: one row per verified primary source.}}
\\label{{tab:matrix}} \\\\
\\toprule
{header}
\\midrule
\\endfirsthead
\\multicolumn{{8}}{{@{{}}l}}{{\\textit{{Table~\\ref{{tab:matrix}} continued from previous page.}}}} \\\\
\\toprule
{header}
\\midrule
\\endhead
\\midrule
\\multicolumn{{8}}{{r@{{}}}}{{\\textit{{Continued on next page.}}}} \\\\
\\endfoot
\\bottomrule
\\endlastfoot
{body}
\\end{{longtable}}
}}
\\ifrestoretwocol\\twocolumn\\fi
""",
        encoding="utf-8",
    )
    print(f"Ditulis: {OUT} ({len(rows)} baris, {uncoded} tanpa kode tema)")


if __name__ == "__main__":
    main()
