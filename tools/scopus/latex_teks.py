"""Mengubah karakter non-ASCII menjadi perintah LaTeX.

Tectonic memakai XeTeX, dan fon Times Type 1 (ptmr8t) yang dipakai IEEEtran tidak
memuat banyak karakter Unicode (misalnya č, ř, tanda pisah Unicode). Karena itu
metadata dari Crossref dan nama penulis diubah ke perintah aksen LaTeX.
"""
import unicodedata

KHUSUS = {
    "‐": "-", "‑": "-", "‒": "--", "–": "--", "—": "---",
    "―": "---", "−": "$-$", "‘": "`", "’": "'", "“": "``",
    "”": "''", " ": "~", " ": "\\,", " ": "\\,", "×": "$\\times$",
    "µ": "$\\mu$", "μ": "$\\mu$", "°": "$^\\circ$", "±": "$\\pm$",
    "≤": "$\\le$", "≥": "$\\ge$", "…": "\\dots{}", "®": "\\textregistered{}",
    "™": "\\texttrademark{}", "©": "\\textcopyright{}", "ß": "{\\ss}",
    "ø": "{\\o}", "Ø": "{\\O}", "ł": "{\\l}", "Ł": "{\\L}",
    "æ": "{\\ae}", "Æ": "{\\AE}", "œ": "{\\oe}", "Œ": "{\\OE}",
    "ı": "{\\i}", "đ": "d", "Đ": "D", "ð": "d", "þ": "th",
    "²": "$^2$", "³": "$^3$", "½": "1/2", "→": "$\\rightarrow$",
    "α": "$\\alpha$", "β": "$\\beta$", "γ": "$\\gamma$", "δ": "$\\delta$",
    "λ": "$\\lambda$", "σ": "$\\sigma$", "′": "'", "ﬁ": "fi", "ﬂ": "fl",
}
AKSEN = {
    "́": "'", "̀": "`", "̂": "^", "̈": '"', "̃": "~",
    "̌": "v", "̆": "u", "̧": "c", "̊": "r", "̄": "=",
    "̇": ".", "̨": "k", "̋": "H", "̣": "d",
}


def ke_latex(teks):
    out = []
    for ch in teks:
        if ord(ch) < 128:
            out.append(ch)
            continue
        if ch in KHUSUS:
            out.append(KHUSUS[ch])
            continue
        d = unicodedata.normalize("NFD", ch)
        if len(d) >= 2 and ord(d[0]) < 128 and all(c in AKSEN for c in d[1:]):
            s = d[0]
            if s in "ij" and d[1] != "̧":
                s = "\\" + s
            for c in d[1:]:
                cmd = AKSEN[c]
                s = f"\\{cmd}{{{s}}}" if cmd.isalpha() else f"\\{cmd}{{{s}}}"
            out.append("{" + s + "}")
            continue
        if unicodedata.combining(ch):
            continue
        out.append("")
    return "".join(out)
