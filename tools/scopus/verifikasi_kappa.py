#!/usr/bin/env python3
"""Menghitung kesepakatan peninjau manusia dan penyaring AI untuk Cek 1.

Skrip membaca dua lembar di ``verifikasi/cek-1-sampel-buta/`` yang sudah memuat
kolom ``keputusan_manusia`` dan ``keputusan_ai``:

- ``sampel_judul.csv``: 300 judul; manusia ``Yes``/``Yes-C1``/``Yes-C3``/``No``,
  AI ``lanjut``/``eksklusi``;
- ``sampel_abstrak.csv``: rekaman tahap abstrak yang dinilai peninjau; kode
  ``C1``..``C5``, ``R``, ``T``, ``X-E1``..``X-E7``; kolom ``subsampel_100``.

Keluaran di folder yang sama:

- ``kesepakatan.md``: kesepakatan, kappa Cohen (implementasi sendiri), PABAK,
  matriks kode, dan rekaman kritis (dieksklusi AI, dinilai peninjau C1 atau C3);
- ``ketidaksepakatan.csv``: semua rekaman yang keputusannya berbeda. Isian
  ``keputusan_final_fatma`` dan ``alasan_fatma`` yang sudah ada dipertahankan.

Pemakaian:
    python3 tools/scopus/verifikasi_kappa.py           # laporan saja
    python3 tools/scopus/verifikasi_kappa.py --tulis   # tulis kedua keluaran
"""
import argparse
import csv
import math
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VER = ROOT / "literature/scopus-2026-09/verifikasi/cek-1-sampel-buta"

# Keterangan penarikan sampel dan penghitungan (dicetak di kesepakatan.md)
TANGGAL_HITUNG = "4 Oktober 2026"
PENINJAU = "Muhammad Zainal Muttaqin"
POPULASI_JUDUL, BENIH_JUDUL = "5.723", 20260929
POPULASI_ABSTRAK, BENIH_ABSTRAK, N_SAMPEL_ABSTRAK = "1.143", 20261004, 300

KODE_8 = ["C1", "C2", "C3", "C4", "C5", "R", "T", "X"]
KODE_ABSTRAK = KODE_8[:-1] + [f"X-E{i}" for i in range(1, 8)]
KODE_JUDUL = ["Yes", "Yes-C1", "Yes-C3", "No"]
KOLOM_TIDAK_SEPAKAT = ["tahap", "kritis", "idx", "tahun", "judul", "sumber", "keputusan_manusia",
                       "keputusan_ai", "keputusan_final_fatma", "alasan_fatma"]


def baca(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def kappa(x, y):
    """Kappa Cohen; selang 95% memakai galat baku pendekatan sederhana (indikatif)."""
    n = len(x)
    sepakat = sum(a == b for a, b in zip(x, y))
    po = sepakat / n
    pe = sum((x.count(c) / n) * (y.count(c) / n) for c in set(x) | set(y))
    k = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    se = math.sqrt(po * (1 - po) / (n * (1 - pe) ** 2)) if pe < 1 else float("nan")
    return {"n": n, "sepakat": sepakat, "po": po, "kappa": k, "bawah": k - 1.96 * se, "atas": k + 1.96 * se}


def angka(x, d=2):
    """Desimal koma dan tanda minus U+2212."""
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def f_sepakat(s):
    return f"{s['sepakat']} dari {s['n']} ({angka(s['po'] * 100, 1)}%)"


def f_kappa(s):
    return f"{angka(s['kappa'])} [{angka(s['bawah'])}; {angka(s['atas'])}]"


def gabung(k):
    return "X" if k.startswith("X") else k


def biner(k):
    return "eksklusi" if k.startswith("X") else "masuk"


def tiga(data):
    m, a = [d["manusia"] for d in data], [d["ai"] for d in data]
    return (kappa(m, a), kappa([gabung(v) for v in m], [gabung(v) for v in a]),
            kappa([biner(v) for v in m], [biner(v) for v in a]))


def muat():
    masalah = []
    judul = []
    for r in baca(VER / "sampel_judul.csv"):
        m, ai = r["keputusan_manusia"].strip(), r["keputusan_ai"].strip()
        if m not in KODE_JUDUL or ai not in ("lanjut", "eksklusi"):
            masalah.append(f"sampel_judul.csv idx {r['idx']}: manusia '{m}', AI '{ai}'")
            continue
        judul.append({**r, "manusia": m, "ai": ai, "hm": "lanjut" if m.startswith("Yes") else "eksklusi"})
    abstrak = []
    for r in baca(VER / "sampel_abstrak.csv"):
        m, ai = r["keputusan_manusia"].strip(), r["keputusan_ai"].strip()
        if m not in KODE_ABSTRAK or ai not in KODE_ABSTRAK:
            masalah.append(f"sampel_abstrak.csv idx {r['idx']}: manusia '{m}', AI '{ai}'")
            continue
        abstrak.append({**r, "manusia": m, "ai": ai, "di100": r["subsampel_100"].strip() == "ya"})
    if masalah:
        sys.exit("Keputusan kosong atau tidak sah:\n" + "\n".join(masalah))
    return judul, abstrak


def tulis_md(judul, abstrak, rj, ra, rs, kritis_j, kritis_a):
    tj = Counter((d["hm"], d["ai"]) for d in judul)
    mk = Counter((gabung(d["manusia"]), gabung(d["ai"])) for d in abstrak)
    n, ns = len(abstrak), rs[0]["n"]
    L = []
    a = L.append
    a("# Cek 1: Kesepakatan Peninjau dan Penyaringan AI")
    a("")
    a(f"Kesepakatan dihitung pada {TANGGAL_HITUNG}. Peninjau adalah {PENINJAU}. Ukuran kesepakatan adalah "
      "kappa Cohen, κ = (*p*_o − *p*_e) / (1 − *p*_e), dengan *p*_o sebagai proporsi kesepakatan teramati dan "
      "*p*_e sebagai proporsi kesepakatan yang diharapkan terjadi secara kebetulan. Selang kepercayaan 95% "
      "ditulis dalam kurung siku dan bersifat indikatif.")
    a("")
    a("## 1. Tahap judul")
    a("")
    a(f"Sampel terdiri atas {rj['n']} judul yang ditarik secara acak dari {POPULASI_JUDUL} judul yang disaring "
      f"(benih acak {BENIH_JUDUL}). Keputusan peninjau dan keputusan AI dibandingkan secara biner, yaitu lanjut "
      "ke tahap abstrak atau eksklusi.")
    a("")
    a("| Ukuran | Nilai |")
    a("|---|---|")
    a(f"| Jumlah judul | {rj['n']} |")
    a(f"| Kesepakatan | {f_sepakat(rj)} |")
    a(f"| Kappa Cohen [selang kepercayaan 95%] | {f_kappa(rj)} |")
    a(f"| PABAK (*prevalence-adjusted bias-adjusted kappa*) | {angka(2 * rj['po'] - 1)} |")
    a(f"| Ketidaksepakatan | {rj['n'] - rj['sepakat']} |")
    a("")
    a("| | AI: lanjut | AI: eksklusi |")
    a("|---|---|---|")
    a(f"| **Peninjau: lanjut** | {tj[('lanjut', 'lanjut')]} | {tj[('lanjut', 'eksklusi')]} |")
    a(f"| **Peninjau: eksklusi** | {tj[('eksklusi', 'lanjut')]} | {tj[('eksklusi', 'eksklusi')]} |")
    a("")
    if kritis_j:
        a(f"**Aturan lulus.** Terdapat {len(kritis_j)} judul yang dieksklusi AI tetapi ditandai peninjau sebagai "
          "C1 atau C3. Kelima judul itu diberi tanda pada kolom `kritis` di `ketidaksepakatan.csv`. Status lulus "
          "tahap judul ditetapkan setelah keputusan akhir atas kelima judul tersebut tersedia."
          if len(kritis_j) == 5 else
          f"**Aturan lulus.** Terdapat {len(kritis_j)} judul yang dieksklusi AI tetapi ditandai peninjau sebagai "
          "C1 atau C3. Judul itu diberi tanda pada kolom `kritis` di `ketidaksepakatan.csv`. Status lulus tahap "
          "judul ditetapkan setelah keputusan akhir atas judul tersebut tersedia.")
        a("")
        a("| idx | Peninjau | Judul |")
        a("|---|---|---|")
        for d in kritis_j:
            a(f"| {d['idx']} | {d['manusia']} | {d['judul']} |")
    else:
        a("**Aturan lulus.** Tidak terdapat judul yang dieksklusi AI tetapi ditandai peninjau sebagai C1 atau C3.")
    a("")
    a("## 2. Tahap abstrak")
    a("")
    a(f"Sampel terdiri atas {N_SAMPEL_ABSTRAK} rekaman yang ditarik secara acak dari {POPULASI_ABSTRAK} rekaman "
      f"tahap abstrak (benih acak {BENIH_ABSTRAK}). Peninjau menilai {n} rekaman dari sampel itu. Sebanyak {ns} "
      f"dari {n} rekaman tersebut termasuk subsampel acak 100 yang ditarik dari rekaman berabstrak. Keputusan AI "
      "yang dibandingkan adalah kode yang dipakai korpus saat ini.")
    a("")
    a(f"| Perbandingan | Kesepakatan (*n* = {n}) | Kappa [selang kepercayaan 95%] |")
    a("|---|---|---|")
    for nama, s in zip(("Kode penuh (C1–C5, R, T, X-E1 sampai X-E7)", "Kode dengan semua eksklusi digabung",
                        "Biner: masuk atau eksklusi"), ra):
        a(f"| {nama} | {f_sepakat(s)} | {f_kappa(s)} |")
    a("")
    a(f"Hasil pada {ns} rekaman yang termasuk subsampel acak 100 adalah sebagai berikut.")
    a("")
    a(f"| Perbandingan | Kesepakatan (*n* = {ns}) | Kappa [selang kepercayaan 95%] |")
    a("|---|---|---|")
    a(f"| Kode penuh | {f_sepakat(rs[0])} | {f_kappa(rs[0])} |")
    a(f"| Biner: masuk atau eksklusi | {f_sepakat(rs[2])} | {f_kappa(rs[2])} |")
    a("")
    a(f"Matriks berikut memuat sebaran kode untuk {n} rekaman. Baris menyatakan kode peninjau, kolom menyatakan "
      "kode AI, dan semua kode eksklusi digabung sebagai X. Tanda titik tengah (·) berarti nol.")
    a("")
    a("| | " + " | ".join(KODE_8) + " | Jumlah |")
    a("|---|" + "---|" * (len(KODE_8) + 1))
    for p in KODE_8:
        a(f"| **{p}** | " + " | ".join(str(mk[(p, q)]) if mk[(p, q)] else "·" for q in KODE_8)
          + f" | {sum(mk[(p, q)] for q in KODE_8)} |")
    a("| **Jumlah** | " + " | ".join(str(sum(mk[(p, q)] for p in KODE_8)) for q in KODE_8) + f" | {n} |")
    a("")
    if kritis_a:
        a(f"**Aturan lulus.** Terdapat {len(kritis_a)} rekaman yang dieksklusi AI tetapi dinilai peninjau sebagai "
          "C1 atau C3: " + ", ".join(f"idx {d['idx']} ({d['manusia']})" for d in kritis_a) + ".")
    else:
        a("**Aturan lulus.** Tidak terdapat rekaman yang dieksklusi AI tetapi dinilai peninjau sebagai C1 atau C3.")
    a("")
    a("## 3. Berkas")
    a("")
    a("| Berkas | Isi |")
    a("|---|---|")
    a(f"| `sampel_judul.csv` | Keputusan peninjau dan keputusan AI untuk {rj['n']} judul, dengan kolom "
      "`keputusan_final_fatma` |")
    a(f"| `sampel_abstrak.csv` | Keputusan peninjau dan keputusan AI untuk {n} rekaman tahap abstrak, dengan kolom "
      "`keputusan_final_fatma` |")
    a("| `sampel_judul_manusia.xlsx` | Lembar isian asli peninjau untuk tahap judul |")
    a("| `ketidaksepakatan.csv` | Semua rekaman yang keputusannya berbeda, dengan kolom `keputusan_final_fatma` "
      "dan `alasan_fatma` |")
    a("| `../log_perubahan.csv` | Koreksi isian peninjau |")
    a("")
    (VER / "kesepakatan.md").write_text("\n".join(L), encoding="utf-8", newline="\n")


def tulis_tidak_sepakat(judul, abstrak, kritis_j, kritis_a):
    path = VER / "ketidaksepakatan.csv"
    lama = {(r["tahap"], r["idx"]): r for r in baca(path)} if path.exists() else {}
    out = []
    for tahap, data, kritis, beda in (("judul", judul, kritis_j, lambda d: d["hm"] != d["ai"]),
                                      ("abstrak", abstrak, kritis_a, lambda d: d["manusia"] != d["ai"])):
        for d in data:
            if beda(d):
                r = lama.get((tahap, d["idx"]), {})
                out.append({"tahap": tahap, "kritis": "ya" if d in kritis else "", "idx": d["idx"],
                            "tahun": d["tahun"], "judul": d["judul"], "sumber": d["sumber"],
                            "keputusan_manusia": d["manusia"], "keputusan_ai": d["ai"],
                            "keputusan_final_fatma": r.get("keputusan_final_fatma", ""),
                            "alasan_fatma": r.get("alasan_fatma", "")})
    hilang = [k for k in set(lama) - {(b["tahap"], b["idx"]) for b in out}
              if lama[k].get("keputusan_final_fatma", "").strip()]
    if hilang:
        sys.exit(f"{len(hilang)} baris ketidaksepakatan.csv berisi keputusan Fatma tetapi tidak lagi berbeda "
                 "pendapat; periksa manual sebelum menimpa: " + str(sorted(hilang)[:10]))
    out.sort(key=lambda b: (b["tahap"] != "judul", b["kritis"] != "ya", int(b["idx"])))
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLOM_TIDAK_SEPAKAT)
        w.writeheader()
        w.writerows(out)
    return len(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tulis", action="store_true", help="tulis kesepakatan.md dan ketidaksepakatan.csv")
    a = ap.parse_args()

    judul, abstrak = muat()
    rj = kappa([d["hm"] for d in judul], [d["ai"] for d in judul])
    ra = tiga(abstrak)
    rs = tiga([d for d in abstrak if d["di100"]])
    kritis_j = [d for d in judul if d["ai"] == "eksklusi" and d["manusia"] in ("Yes-C1", "Yes-C3")]
    kritis_a = [d for d in abstrak if d["ai"].startswith("X") and d["manusia"] in ("C1", "C3")]

    print(f"Judul: {f_sepakat(rj)}, kappa {f_kappa(rj)}, PABAK {angka(2 * rj['po'] - 1)}, kritis {len(kritis_j)}")
    for nama, s in zip(("kode penuh", "eksklusi digabung", "biner"), ra):
        print(f"Abstrak, {nama}: {f_sepakat(s)}, kappa {f_kappa(s)}")
    print(f"Abstrak, subsampel 100, kode penuh: {f_sepakat(rs[0])}, kappa {f_kappa(rs[0])}; kritis {len(kritis_a)}")
    if a.tulis:
        tulis_md(judul, abstrak, rj, ra, rs, kritis_j, kritis_a)
        print("ditulis: kesepakatan.md dan ketidaksepakatan.csv,", tulis_tidak_sepakat(judul, abstrak, kritis_j, kritis_a),
              "ketidaksepakatan")


if __name__ == "__main__":
    main()
