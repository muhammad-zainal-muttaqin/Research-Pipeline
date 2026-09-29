#!/usr/bin/env python3
"""Daftar kerja teks lengkap (Pemeriksaan 4, bagian 1: permintaan PDF).

Menyusun satu baris per kajian dalam empat kelompok prioritas rencana
verifikasi teks lengkap, lalu menurunkan daftar permintaan PDF darinya.

  1  kajian di Tabel 2 dan 3 naskah (tab:acq + tab:assoc)
  2  kajian inti C1 yang dikodekan dari judul saja (dasar_keputusan = judul)
  3  sisa kajian C1
  4  kajian sawit C3 yang dibahas rinci: pencacahan (tugas HIT) dan
     multipandang (kolom multipandang = Y) di topik/bukti/kode_C3.txt

Keluaran (literature/scopus-2026-09/verifikasi/ dan unduhan/):
  verifikasi/teks_lengkap.csv       daftar kerja (dibaca dan ditulis ulang)
  verifikasi/PERMINTAAN-PDF.md      daftar permintaan + templat surel
  unduhan/PRIORITAS-UNDUH-MANUAL.md daftar centang unduh manual

Aman dijalankan ulang: kolom pdf_ada dihitung ulang dari folder pdf/,
sedangkan kolom isian tangan (status, tanggal_minta, sumber_pdf, catatan,
email_penulis_korespondensi) yang sudah berisi dipertahankan dari
teks_lengkap.csv yang ada (sel kosong diisi catatan otomatis, bila ada).
Kolom jalur_disarankan dihitung ulang, kecuali bila isinya diawali
"manual:" (isian tangan yang dikunci).

Tautan akses terbuka (OA) diambil dari topik/enrich.jsonl (OpenAlex,
Semantic Scholar, Unpaywall; 28 September 2026), dari log unduhan
(unduhan/log_unduh.csv), dan dari daftar OA_MANUAL di bawah (salinan legal
yang ditemukan lewat penelusuran web, 29 September 2026: arXiv, CVF Open
Access, repositori penulis/institusi, jurnal akses terbuka). Skrip ini tidak
mengunduh apa pun dan tidak memakai jaringan.

    python3 tools/scopus/verifikasi_teks_lengkap.py
"""
import csv
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature" / "scopus-2026-09"
MATRIKS = KORPUS / "topik" / "bukti" / "matriks_bukti.csv"
KODE_C3 = KORPUS / "topik" / "bukti" / "kode_C3.txt"
ENRICH = KORPUS / "topik" / "enrich.jsonl"
LOG_UNDUH = KORPUS / "unduhan" / "log_unduh.csv"
PDF_DIR = KORPUS / "pdf"
BODY = ROOT / "manuscript" / "source" / "main6-body.tex"
OUT_CSV = KORPUS / "verifikasi" / "teks_lengkap.csv"
OUT_MINTA = KORPUS / "verifikasi" / "PERMINTAAN-PDF.md"
OUT_PRIOR = KORPUS / "unduhan" / "PRIORITAS-UNDUH-MANUAL.md"

KOLOM = ["prioritas", "kelompok", "key", "kode", "tahun", "penulis_pertama",
         "judul", "sumber", "doi", "penerbit", "pdf_ada", "jalur_disarankan",
         "email_penulis_korespondensi", "status", "tanggal_minta",
         "sumber_pdf", "catatan"]
KOLOM_TANGAN = ["email_penulis_korespondensi", "status", "tanggal_minta",
                "sumber_pdf", "catatan"]

# Angka rencana supervisor (total, dengan PDF). Selisih dilaporkan, tidak dipaksa.
RENCANA = {1: (21, 4), 2: (42, 1), 3: (124, 52), 4: (18, 6)}

TENGGAT_MINTA = "6 Oktober 2026"
TENGGAT_FATMA = "23 Oktober 2026"

# Salinan akses terbuka legal yang tidak tercatat di enrich.jsonl,
# ditemukan lewat penelusuran web 29 September 2026. Hanya arXiv, CVF Open
# Access, repositori penulis/institusi, dan jurnal akses terbuka.
OA_MANUAL = {
    "liu2018robust": "https://arxiv.org/abs/1804.00307",
    "qureshi2023seeing": "https://arxiv.org/abs/2308.07512",
    "lei2025spatio": "https://arxiv.org/abs/2409.19786",
    "meyer2024fruitnerf": "https://arxiv.org/abs/2408.06190",
    "meyer2025fruitnerf": "https://arxiv.org/abs/2505.19863",
    "zaenker2023graph": "https://arxiv.org/abs/2303.03048",
    "yang2025safe": "https://arxiv.org/abs/2409.18293",
    "santos2024multiple": "https://arxiv.org/abs/2312.16724",
    "nellithimaru2019rols": ("https://openaccess.thecvf.com/content_CVPRW_2019/papers/CVPPP/"
                             "Nellithimaru_ROLS__Robust_Object-Level_SLAM_for_Grape_Counting_CVPRW_2019_paper.pdf"),
    "matos2024tracking": ("https://openaccess.thecvf.com/content/CVPR2024W/Vision4Ag/papers/"
                          "Matos_Tracking_and_Counting_Apples_in_Orchards_Under_Intermittent_Occlusions_and_CVPRW_2024_paper.pdf"),
    "nuske2014automated": "https://www.ri.cmu.edu/pub_files/2014/9/rob21541.pdf",
    "prasetyo2020automatic": "https://gigvvy.com/journals/ijase/articles/ijase-202005-17-2-121",
}
# Catatan versi untuk OA_MANUAL yang bukan versi terbit.
OA_CATATAN = {
    "liu2018robust": "OA = pracetak arXiv; periksa selisih dengan versi IROS",
    "qureshi2023seeing": "OA = pracetak arXiv; periksa selisih dengan versi IROS",
    "lei2025spatio": "OA = pracetak arXiv; periksa selisih dengan versi RA-L",
    "meyer2024fruitnerf": "OA = pracetak arXiv; periksa selisih dengan versi IROS",
    "meyer2025fruitnerf": "OA = pracetak arXiv; periksa selisih dengan versi IROS",
    "zaenker2023graph": "OA = pracetak arXiv; periksa selisih dengan versi IROS",
    "yang2025safe": "OA = pracetak arXiv; periksa selisih dengan versi ICRA",
    "santos2024multiple": "OA = pracetak arXiv; periksa selisih dengan versi COMPAG",
    "nellithimaru2019rols": "OA = versi CVF Open Access (setara versi terbit)",
    "matos2024tracking": "OA = versi CVF Open Access (setara versi terbit)",
    "nuske2014automated": "OA = salinan di situs Robotics Institute CMU",
}

PENERBIT = {
    "10.1016": "Elsevier", "10.1109": "IEEE", "10.23919": "IEEE",
    "10.1007": "Springer", "10.1038": "Springer Nature", "10.1002": "Wiley",
    "10.1145": "ACM", "10.1063": "AIP Publishing", "10.1088": "IOP Publishing",
    "10.1093": "Oxford University Press", "10.1017": "Cambridge University Press",
    "10.1117": "SPIE", "10.1080": "Taylor & Francis",
    "10.1051": "EDP Sciences", "10.11591": "IAES", "10.32985": "IJECES (Univ. Osijek)",
    "10.11975": "CSAE (Tiongkok)", "10.3969": "CSAE (Tiongkok)",
    "10.6041": "CSAM (Tiongkok)", "10.13925": "Journal of Fruit Science (Tiongkok)",
    "10.13031": "ASABE", "10.1364": "Optica", "10.1371": "PLOS",
    "10.15586": "Codon Publications", "10.17660": "ISHS", "10.20965": "Fuji Technology Press",
    "10.21894": "MPOB", "10.22456": "UFRGS", "10.3389": "Frontiers", "10.3390": "MDPI",
    "10.34133": "AAAS (Science Partner Journals)", "10.3920": "Wageningen Academic",
    "10.6703": "IJASE (Chaoyang Univ.)",
}
# Jurnal akses terbuka penuh: halaman DOI penerbit lebih andal daripada repositori.
JURNAL_OA = {"IEEE Access", "Data in Brief", "Heliyon", "Smart Agricultural Technology",
             "Plant Phenomics", "OSA Continuum", "Information Processing in Agriculture",
             "E3s Web of Conferences", "Journal of Robotics and Mechatronics"}
TIONGKOK = {"10.11975", "10.3969", "10.6041", "10.13925"}
BESAR = {"Elsevier", "IEEE", "Springer", "Springer Nature", "Wiley", "ACM",
         "AIP Publishing", "IOP Publishing", "Oxford University Press",
         "Cambridge University Press", "SPIE", "Taylor & Francis"}

JALUR_ADA = "- (PDF sudah ada)"
JALUR_LIB = "perpustakaan ULM"
JALUR_FATMA = "Bu Fatma"
JALUR_PENULIS = "penulis"


def cites(teks):
    return [k.strip() for m in re.findall(r"\\cite\{([^}]*)\}", teks)
            for k in m.split(",") if k.strip()]


def potong(body, awal, akhir):
    i = body.index(awal)
    return body[i:body.index(akhir, i)]


def baca_c3():
    c3 = {}
    for baris in KODE_C3.read_text(encoding="utf-8").splitlines():
        if not baris.strip() or baris.startswith("#"):
            continue
        p = baris.split("\t")
        c3[p[0]] = {"tugas": p[1], "multipandang": p[4]}
    return c3


def url_oa(key, rec, en, log):
    """Pilih satu tautan OA terbaik, atau '' bila tidak ada."""
    if key in OA_MANUAL:
        return OA_MANUAL[key]
    kand = list(en.get("pdf_urls") or []) + list(en.get("oa_landing") or [])
    note = log.get("note", "") if log else ""
    for u in re.findall(r"(https?://\S+?):\s", note + " "):
        if not u.startswith("https://doi.org/"):
            kand.append(u)
    if log and log.get("source_url"):
        kand.append(log["source_url"])
    kand = [u for u in kand if "doaj.org" not in u]
    oa_status = en.get("oa_status") or ""
    ada_oa = oa_status in ("gold", "hybrid", "bronze", "green") or bool(en.get("pdf_urls"))
    if not kand:
        return ""
    if not ada_oa and all(u.startswith("https://doi.org/") for u in kand):
        return ""

    def norm(u):
        m = re.match(r"https?://www\.ncbi\.nlm\.nih\.gov/pmc/articles/(?:PMC)?(\d+)", u)
        if m:
            return f"https://pmc.ncbi.nlm.nih.gov/articles/PMC{m.group(1)}/"
        return u

    jurnal_oa = rec.get("source", "") in JURNAL_OA

    def peringkat(u):
        if "ncbi.nlm.nih.gov" in u:
            return 0
        if "arxiv.org" in u or "thecvf.com" in u:
            return 1
        if u.startswith("https://doi.org/"):
            return 1.5 if jurnal_oa else 4
        if any(h in u for h in ("hdl.handle.net", "upcommons", "figshare", "research.wur.nl",
                                "publica.fraunhofer", "digitalcommons", "kerwa.ucr",
                                "psasir.upm", "ri.cmu.edu", "seer.ufrgs")):
            return 2
        return 3
    kand = sorted(dict.fromkeys(norm(u) for u in kand), key=peringkat)
    return kand[0]


def penerbit_dari(doi, sumber):
    if not doi:
        return "ASABE" if "Agricultural and Biological Engineers" in sumber else "?"
    return PENERBIT.get(doi.split("/")[0], sumber or "?")


def jalur_untuk(r, oa):
    if r["pdf_ada"] == "Y":
        return JALUR_ADA
    if oa:
        return "OA: " + oa
    pre = r["doi"].split("/")[0] if r["doi"] else ""
    jenis = r["_doc_type"]
    prosiding = jenis in ("Conference Paper", "Book Chapter") or not r["doi"]
    if r["kode"] == "C3" and prosiding:
        return JALUR_PENULIS          # penulis Indonesia/Malaysia, mudah dihubungi
    if pre in TIONGKOK or prosiding:
        return JALUR_FATMA
    if r["penerbit"] in BESAR:
        return JALUR_LIB
    return JALUR_PENULIS


def susun():
    rows = list(csv.DictReader(MATRIKS.open(encoding="utf-8")))
    bykey = {r["key"]: r for r in rows}
    byidx = {r["idx"]: r for r in rows}
    pdfs = {p.stem for p in PDF_DIR.glob("*.pdf")}
    en = {}
    for baris in ENRICH.open(encoding="utf-8"):
        d = json.loads(baris)
        en[d.get("eid")] = d
    log = {r["key"]: r for r in csv.DictReader(LOG_UNDUH.open(encoding="utf-8"))}
    body = BODY.read_text(encoding="utf-8")
    acq = list(dict.fromkeys(cites(potong(body, r"\label{tab:acq}", r"\end{table*}"))))
    assoc = list(dict.fromkeys(cites(potong(body, r"\label{tab:assoc}", r"\end{table*}"))))
    palm = set(cites(potong(body, r"\label{sec:palm}", r"\label{sec:position}")))
    c3 = baca_c3()

    daftar = OrderedDict()   # key -> (prioritas, kelompok, catatan_awal)
    for k in acq:
        daftar[k] = (1, "Tabel 2 (tab:acq)", "")
    for k in assoc:
        if k not in daftar:
            daftar[k] = (1, "Tabel 3 (tab:assoc)", "")
    for r in rows:
        if r["kode"] == "C1" and r["dasar_keputusan"] == "judul" and r["key"] not in daftar:
            daftar[r["key"]] = (2, "C1 dikode dari judul", "")
    for r in rows:
        if r["kode"] == "C1" and r["key"] not in daftar:
            daftar[r["key"]] = (3, "C1 lainnya", "")
    for idx, c in c3.items():
        hit, mv = c["tugas"] == "HIT", c["multipandang"] == "Y"
        if not (hit or mv):
            continue
        r = byidx[idx]
        kel = "C3 " + "+".join(x for x, y in (("pencacahan", hit), ("multipandang", mv)) if y)
        cat = ("dikutip di seksi Oil palm" if r["key"] in palm
               else "tidak dikutip di seksi Oil palm (hanya masuk hitungan 11 multipandang)")
        if r["key"] not in daftar:
            daftar[r["key"]] = (4, kel, cat)

    peringatan = []
    for k in acq + assoc:
        if k not in bykey:
            peringatan.append(f"kunci tabel {k} tidak ada di matriks_bukti.csv")
        elif bykey[k]["kode"] != "C1":
            peringatan.append(f"kunci tabel {k} berkode {bykey[k]['kode']}, bukan C1")

    lama = {}
    if OUT_CSV.exists():
        lama = {r["key"]: r for r in csv.DictReader(OUT_CSV.open(encoding="utf-8"))}

    keluar = []
    for key, (pr, kel, cat) in daftar.items():
        m = bykey[key]
        r = {
            "prioritas": str(pr), "kelompok": kel, "key": key, "kode": m["kode"],
            "tahun": m["year"], "penulis_pertama": m["first_author"], "judul": m["title"],
            "sumber": m["source"], "doi": m["doi"],
            "penerbit": penerbit_dari(m["doi"], m["source"]),
            "pdf_ada": "Y" if key in pdfs else "N",
            "_doc_type": m["doc_type"],
        }
        oa = url_oa(key, m, en.get(m["eid"], {}), log.get(key))
        r["_oa"] = oa
        r["jalur_disarankan"] = jalur_untuk(r, oa)
        catatan = [c for c in (cat, OA_CATATAN.get(key, "") if oa else "") if c]
        if r["pdf_ada"] == "N" and oa.startswith("https://doi.org/"):
            catatan.append("OA menurut OpenAlex/Unpaywall; bila halaman terkunci, "
                           "pakai perpustakaan ULM")
        if m["dasar_keputusan"] == "judul":
            catatan.append("dikode dari judul")
        r["catatan"] = "; ".join(catatan)
        for kol in ("email_penulis_korespondensi", "status", "tanggal_minta", "sumber_pdf"):
            r[kol] = ""
        if key in lama:
            for kol in KOLOM_TANGAN:
                if lama[key].get(kol, "").strip():
                    r[kol] = lama[key][kol]
            if lama[key].get("jalur_disarankan", "").startswith("manual:"):
                r["jalur_disarankan"] = lama[key]["jalur_disarankan"]
        keluar.append(r)

    urut_jalur = {"OA": 0, JALUR_LIB: 1, JALUR_FATMA: 2, JALUR_PENULIS: 3}

    def kunci(r):
        j = r["jalur_disarankan"]
        jj = 0 if j.startswith("OA") else urut_jalur.get(j, 4)
        tab = 0 if r["prioritas"] == "1" else 1   # prioritas 1 tetap urut tabel naskah
        return (int(r["prioritas"]), r["pdf_ada"] == "Y",
                0 if tab == 0 else jj, 0 if tab == 0 else -int(r["tahun"] or 0))
    keluar.sort(key=kunci)
    return keluar, peringatan


def tulis_csv(keluar):
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLOM, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(keluar)


def md_sel(t):
    return (t or "").replace("|", "\\|").replace("\n", " ")


def doi_link(doi):
    return f"[{doi}](https://doi.org/{doi})" if doi else "(tanpa DOI)"


def rekap(keluar):
    out = {}
    for p in (1, 2, 3, 4):
        g = [r for r in keluar if r["prioritas"] == str(p)]
        out[p] = (len(g), sum(r["pdf_ada"] == "Y" for r in g),
                  sum(r["pdf_ada"] == "N" and r["jalur_disarankan"].startswith("OA") for r in g))
    return out


NAMA_P = {1: "Tabel 2 dan 3 naskah", 2: "C1 dikode dari judul", 3: "C1 lainnya",
          4: "C3 sawit: pencacahan dan multipandang"}

EMAIL_EN = """Subject: Request for a copy of your paper "[TITLE]" for a systematic review

Dear Dr. [SURNAME],

I am conducting a systematic review of image-based fruit counting, focusing on how
studies avoid double counting the same fruit across several images (tracking,
3D association, and related methods). Your paper

  [AUTHORS] ([YEAR]). [TITLE]. [SOURCE]. https://doi.org/[DOI]

is one of the studies included in the review, and I would like to read the full
text to code its methods and results accurately. Our institution does not have
access to it. Would you be willing to send me a copy (the accepted manuscript is
fine) for private research use?

Thank you very much for your time. I will cite the paper in the review.

Kind regards,

Muhammad Zainal Muttaqin
Universitas Lambung Mangkurat
[Department/Faculty]
[email address]
"""

RG_TEXT = """Dear Dr. [SURNAME], I am preparing a systematic review of image-based fruit
counting (how studies avoid counting the same fruit twice across images), and your
paper "[TITLE]" is one of the included studies. Could you kindly share the full text
for private research use? I will cite it in the review. Thank you very much.
Muhammad Zainal Muttaqin, Universitas Lambung Mangkurat"""


def tulis_permintaan(keluar):
    belum = [r for r in keluar if r["pdf_ada"] == "N"]
    oa = [r for r in belum if r["jalur_disarankan"].startswith("OA")]
    lib = [r for r in belum if r["jalur_disarankan"] == JALUR_LIB]
    fat = [r for r in belum if r["jalur_disarankan"] == JALUR_FATMA]
    pen = [r for r in belum if r["jalur_disarankan"] == JALUR_PENULIS]
    paralel = [r for r in belum if r["prioritas"] == "1"
               and r["jalur_disarankan"] in (JALUR_LIB, JALUR_FATMA)]
    rk = rekap(keluar)
    L = []
    a = L.append
    a("# Permintaan PDF teks lengkap (Pemeriksaan 4, bagian 1)")
    a("")
    a("Berkas ini dibuat oleh `tools/scopus/verifikasi_teks_lengkap.py` dari "
      "`verifikasi/teks_lengkap.csv`. Jangan disunting tangan; ubah CSV-nya "
      "(kolom `status`, `tanggal_minta`, `sumber_pdf`, `catatan`) lalu jalankan ulang skrip.")
    a("")
    a("## Tenggat")
    a("")
    a(f"- Semua permintaan (perpustakaan, Bu Fatma, penulis) **terkirim sebelum {TENGGAT_MINTA}**.")
    a(f"- Daftar kajian C1 yang masih belum ber-PDF diserahkan ke Bu Fatma **paling lambat {TENGGAT_FATMA}**.")
    a("- Setiap PDF yang diterima disimpan sebagai `literature/scopus-2026-09/pdf/<key>.pdf`; "
      "isi `status`, `tanggal_minta`, dan `sumber_pdf` di CSV, lalu jalankan ulang skrip.")
    a("")
    a("## Ringkasan")
    a("")
    a("| Prioritas | Kelompok | Kajian | PDF ada | Belum | OA ditemukan |")
    a("|---|---|---|---|---|---|")
    for p in (1, 2, 3, 4):
        t, y, o = rk[p]
        a(f"| {p} | {NAMA_P[p]} | {t} | {y} | {t - y} | {o} |")
    a("")
    a(f"Belum ber-PDF: {len(belum)} kajian. Jalur: OA {len(oa)} · perpustakaan ULM {len(lib)} · "
      f"Bu Fatma {len(fat)} · penulis {len(pen)} (+{len(paralel)} permintaan paralel ke penulis "
      "untuk prioritas 1).")
    a("")
    a("Aturan jalur: salinan OA legal (arXiv, CVF, PMC, repositori institusi, jurnal akses "
      "terbuka) diunduh sendiri; artikel jurnal penerbit besar (Elsevier, IEEE, Springer, "
      "Wiley, ACM, AIP, IOP, OUP) ke perpustakaan ULM; prosiding, bab buku, dan jurnal "
      "Tiongkok ke Bu Fatma; prosiding sawit (penulis Indonesia/Malaysia) dan jurnal "
      "penerbit kecil langsung ke penulis.")
    a("")
    a("## 0. Unduh sendiri: salinan akses terbuka legal")
    a("")
    a("Buka tautan di peramban, unduh PDF, simpan dengan nama `<key>.pdf`. "
      "Bila tautannya pracetak (arXiv), catat di kolom `sumber_pdf`.")
    a("")
    a("| Prioritas | Key | Tahun | Judul | Tautan OA |")
    a("|---|---|---|---|---|")
    for r in oa:
        u = r["jalur_disarankan"][4:]
        a(f"| {r['prioritas']} | `{r['key']}` | {r['tahun']} | {md_sel(r['judul'])} | <{u}> |")
    a("")
    a("## (a) Untuk perpustakaan ULM (dikelompokkan per penerbit)")
    a("")
    per = OrderedDict()
    for r in sorted(lib, key=lambda r: (r["penerbit"], int(r["prioritas"]), r["key"])):
        per.setdefault(r["penerbit"], []).append(r)
    for pen_nama, g in per.items():
        a(f"### {pen_nama} ({len(g)})")
        a("")
        a("| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | DOI |")
        a("|---|---|---|---|---|---|---|")
        for r in g:
            a(f"| {r['prioritas']} | `{r['key']}` | {r['tahun']} | {md_sel(r['penulis_pertama'])} | "
              f"{md_sel(r['judul'])} | {md_sel(r['sumber'])} | {doi_link(r['doi'])} |")
        a("")
    a("## (b) Untuk Bu Fatma (kemungkinan tidak ada di perpustakaan)")
    a("")
    a("Prosiding konferensi, bab buku, dan jurnal Tiongkok.")
    a("")
    a("| Prioritas | Key | Tahun | Penulis pertama | Judul | Sumber | Penerbit | DOI |")
    a("|---|---|---|---|---|---|---|---|")
    for r in sorted(fat, key=lambda r: (int(r["prioritas"]), r["penerbit"], r["key"])):
        a(f"| {r['prioritas']} | `{r['key']}` | {r['tahun']} | {md_sel(r['penulis_pertama'])} | "
          f"{md_sel(r['judul'])} | {md_sel(r['sumber'])} | {r['penerbit']} | {doi_link(r['doi'])} |")
    a("")
    a("## (c) Diminta ke penulis")
    a("")
    a("Jalur utama `penulis`, ditambah kajian prioritas 1 yang jalur utamanya perpustakaan atau "
      "Bu Fatma (permintaan paralel, karena kajian ini menopang Tabel 2 dan 3). Kirim lewat "
      "surel penulis korespondensi bila tercantum; bila tidak, lewat tombol *Request full-text* "
      "di ResearchGate. Surel diisi di kolom `email_penulis_korespondensi` hanya bila ditemukan "
      "terbuka di halaman makalah atau ORCID.")
    a("")
    a("| Prioritas | Key | Tahun | Penulis pertama | Judul | DOI | Surel | Keterangan |")
    a("|---|---|---|---|---|---|---|---|")
    for r in sorted(pen + paralel, key=lambda r: (int(r["prioritas"]), r["key"])):
        ket = "paralel" if r in paralel else "utama"
        a(f"| {r['prioritas']} | `{r['key']}` | {r['tahun']} | {md_sel(r['penulis_pertama'])} | "
          f"{md_sel(r['judul'])} | {doi_link(r['doi'])} | {r['email_penulis_korespondensi']} | {ket} |")
    a("")
    a("## Templat surel ke penulis (bahasa Inggris)")
    a("")
    a("```text")
    a(EMAIL_EN.rstrip())
    a("```")
    a("")
    a("## Templat permintaan ResearchGate")
    a("")
    a("```text")
    a(RG_TEXT)
    a("```")
    a("")
    OUT_MINTA.write_text("\n".join(L), encoding="utf-8")


def tulis_prioritas(keluar):
    belum = [r for r in keluar if r["pdf_ada"] == "N"]
    rk = rekap(keluar)
    L = []
    a = L.append
    a("# Prioritas unduh manual PDF `main6`")
    a("")
    a("Dibuat oleh `tools/scopus/verifikasi_teks_lengkap.py` dari "
      "`literature/scopus-2026-09/verifikasi/teks_lengkap.csv`; jalankan ulang skrip setelah "
      "menambah PDF (baris yang PDF-nya sudah ada akan hilang dari tabel).")
    a("")
    a("Urutan mengikuti rencana verifikasi teks lengkap: (1) kajian Tabel 2 dan 3 naskah, "
      "(2) kajian C1 yang dikode dari judul, (3) sisa kajian C1, (4) kajian sawit C3 "
      "pencacahan dan multipandang. Di dalam prioritas 2–4: OA dulu, lalu perpustakaan, "
      "Bu Fatma, penulis; tahun terbaru dulu.")
    a("")
    a("Simpan setiap PDF sebagai `literature/scopus-2026-09/pdf/<key>.pdf` (nama persis kolom "
      "*key*). Centang kotak setelah selesai. Daftar permintaan dan templat surel: "
      "`literature/scopus-2026-09/verifikasi/PERMINTAAN-PDF.md`.")
    a("")
    a("| Prioritas | Kelompok | Kajian | PDF ada | Belum | OA ditemukan |")
    a("|---|---|---|---|---|---|")
    for p in (1, 2, 3, 4):
        t, y, o = rk[p]
        a(f"| {p} | {NAMA_P[p]} | {t} | {y} | {t - y} | {o} |")
    a("")
    a("| ✓ | # | Prioritas | Kode | Key (nama berkas) | Tahun | Judul | Penerbit | DOI | Jalur disarankan |")
    a("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(belum, 1):
        j = r["jalur_disarankan"]
        if j.startswith("OA: "):
            j = f"OA: <{j[4:]}>"
        a(f"| ☐ | {i} | {r['prioritas']} | {r['kode']} | `{r['key']}` | {r['tahun']} | "
          f"{md_sel(r['judul'])} | {r['penerbit']} | {doi_link(r['doi'])} | {j} |")
    a("")
    OUT_PRIOR.write_text("\n".join(L), encoding="utf-8")


def main():
    keluar, peringatan = susun()
    tulis_csv(keluar)
    tulis_permintaan(keluar)
    tulis_prioritas(keluar)
    rk = rekap(keluar)
    print(f"{OUT_CSV.relative_to(ROOT)}: {len(keluar)} baris")
    for p in (1, 2, 3, 4):
        t, y, o = rk[p]
        rt, ry = RENCANA[p]
        tanda = "" if (t, y) == (rt, ry) else f"  <-- rencana {rt}/{ry}"
        print(f"  prioritas {p} ({NAMA_P[p]}): {t} kajian, {y} ber-PDF, {o} OA ditemukan{tanda}")
    for w in peringatan:
        print("PERINGATAN:", w, file=sys.stderr)


if __name__ == "__main__":
    main()
