#!/usr/bin/env python3
"""Cek 5: pengodean ulang kajian inti C1 dari teks lengkap.

Membuat dan memelihara lembar kerja peninjau
literature/scopus-2026-09/verifikasi/kode_ulang_C1.csv. Prosedur lengkap ada di
literature/scopus-2026-09/verifikasi/KODE-ULANG.md.

Mode:
  (tanpa opsi)        buat atau segarkan lembar. Kolom final_* dan
                      catatan_peninjau (milik peninjau) serta draf_ai_* (draf
                      model) dipertahankan; kolom lain dihitung ulang dari
                      matriks_bukti.csv, mekanisme_C1.txt, main6-body.tex, dan
                      folder pdf/ + teks/.
  --draf BERKAS.csv   impor draf model (kolom idx + draf_ai_*) ke lembar. Hanya
                      kolom draf_ai_* yang ditimpa; kolom final_* tidak pernah
                      disentuh.
  --terapkan --oleh INISIAL [--kering]
                      salin nilai final_* yang sudah dikonfirmasi ke
                      topik/bukti/mekanisme_C1.txt dan catat setiap sel yang
                      berubah di verifikasi/log_perubahan.csv. --kering hanya
                      menampilkan rencana perubahan.
  --sampel-fatma      tarik 20 kajian C1 acak (benih tetap) ke
                      verifikasi/sampel_fatma_C1.csv tanpa kode peninjau/model.
  --banding-fatma     bandingkan isian Fatma dengan final_* peninjau.

  python3 tools/scopus/verifikasi_kode_ulang.py
"""
import argparse
import csv
import datetime
import io
import os
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature/scopus-2026-09"
MAT = KORPUS / "topik/bukti/matriks_bukti.csv"
MANUAL = KORPUS / "topik/bukti/mekanisme_C1.txt"
BODY = ROOT / "manuscript/source/main6-body.tex"
VER = KORPUS / "verifikasi"
LEMBAR = VER / "kode_ulang_C1.csv"
LOG = VER / "log_perubahan.csv"
SAMPEL = VER / "sampel_fatma_C1.csv"
LOG_KEPALA = ["tanggal", "berkas", "idx_atau_key", "kolom", "nilai_lama",
              "nilai_baru", "alasan", "oleh"]

LAMA = ["mekanisme", "akuisisi", "per_kelas", "hasil_ringkas"]
BARU = ["sumber_kode", "halaman", "referensi_hitung", "tingkat_metrik",
        "cara_kelas", "berubah"]
SEPULUH = LAMA + BARU
TABEL_PRIORITAS = ["tab:acq", "tab:assoc"]
BENIH_FATMA = 20261106
N_FATMA = 20

# Kosakata terkendali (huruf kecil; gabungan dipisah ';').
SUMBER = {"teks lengkap", "abstrak", "judul"}
REFERENSI = {"pohon", "panen", "packhouse", "anotasi", "tidak ada"}
TINGKAT = {"hitung", "identitas", "deteksi", "tidak ada"}
CARA = {"saat pelacakan", "sesudah pelacakan", "voting antarpandang",
        "tidak dinyatakan", "-"}
AKUISISI = {"V", "D", "S", "T", "1"}
POLA_MEK = re.compile(r"^(M[0-5]|DATA)(\+(M[0-5]|DATA))*$")


def kolom_lembar():
    k = ["no", "prioritas", "alasan_prioritas", "idx", "key", "tahun", "judul",
         "doi", "dasar_keputusan", "pdf_ada", "path_pdf", "teks_ada"]
    k += [f"kode_ai_{c}" for c in LAMA]
    for c in SEPULUH:
        k.append(f"draf_ai_{c}")
        if c == "halaman":
            k.append("draf_ai_bukti")
        k.append(f"final_{c}")
    k += ["draf_ai_catatan", "catatan_peninjau", "catatan_skrip"]
    return k


KOLOM = kolom_lembar()
MILIK_PENINJAU = [f"final_{c}" for c in SEPULUH] + ["catatan_peninjau"]
MILIK_DRAF = [k for k in KOLOM if k.startswith("draf_ai_")]


# ------------------------------------------------------------------ baca/tulis
def baca_csv(path):
    """Baca CSV yang mungkin sudah disimpan ulang Excel (BOM, ';' atau TAB)."""
    teks = path.read_text(encoding="utf-8-sig")
    kepala = teks.split("\n", 1)[0]
    pemisah = max([",", ";", "\t"], key=kepala.count)
    return list(csv.DictReader(io.StringIO(teks), delimiter=pemisah))


def tulis_csv(path, kolom, baris):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=kolom, lineterminator="\n",
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(baris)
    os.replace(tmp, path)


def muat_manual():
    """idx -> daftar 10 nilai (4 lama + 6 verifikasi), plus urutan baris."""
    baris = MANUAL.read_text(encoding="utf-8").split("\n")
    kode = {}
    for n, line in enumerate(baris):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\r").split("\t")
        p += [""] * (11 - len(p))
        kode[int(p[0])] = {"_baris": n, **dict(zip(SEPULUH, p[1:11]))}
    return baris, kode


def kunci_tabel(label):
    s = BODY.read_text(encoding="utf-8")
    for env in re.findall(r"\\begin\{table\*?\}.*?\\end\{table\*?\}", s, re.S):
        if f"\\label{{{label}}}" in env:
            out = []
            for c in re.findall(r"\\cite[a-z]*\{([^}]*)\}", env):
                out += [k.strip() for k in c.split(",") if k.strip() not in out]
            return out
    return []


# ------------------------------------------------------------------ lembar
def bangun_lembar(impor_draf=None):
    mat = [r for r in csv.DictReader(open(MAT, encoding="utf-8")) if r["kode"] == "C1"]
    _, manual = muat_manual()
    tab = {lab: kunci_tabel(lab) for lab in TABEL_PRIORITAS}
    lama = {}
    if LEMBAR.exists():
        for r in baca_csv(LEMBAR):
            if r.get("idx", "").strip():
                lama[int(r["idx"])] = r
    draf = {}
    if impor_draf:
        for r in baca_csv(Path(impor_draf)):
            asing = [k for k in r if k and k.startswith("final_") and r[k]]
            if asing:
                print(f"PERINGATAN: kolom {asing} di berkas draf diabaikan", file=sys.stderr)
            draf[int(r["idx"])] = {k: (v or "").strip() for k, v in r.items()
                                   if k in MILIK_DRAF}

    baris = []
    for r in mat:
        i = int(r["idx"])
        key = r["key"]
        alasan = [lab for lab in TABEL_PRIORITAS if key in tab[lab]]
        if alasan:
            prio = 1
        elif r["dasar_keputusan"] == "judul":
            prio, alasan = 2, ["judul saja"]
        else:
            prio, alasan = 3, []
        pdf = KORPUS / "pdf" / f"{key}.pdf"
        teks = KORPUS / "teks" / f"{key}.txt"
        m = manual.get(i, {})
        b = {
            "prioritas": prio, "alasan_prioritas": "; ".join(alasan), "idx": i,
            "key": key, "tahun": r["year"], "judul": r["title"], "doi": r["doi"],
            "dasar_keputusan": r["dasar_keputusan"],
            "pdf_ada": "Y" if pdf.exists() else "N",
            "path_pdf": str(pdf.relative_to(ROOT)).replace("\\", "/") if pdf.exists() else "",
            "teks_ada": "Y" if teks.exists() else "N",
        }
        for c in LAMA:
            b[f"kode_ai_{c}"] = m.get(c, "")
        catatan = []
        if not m:
            catatan.append("tidak ada baris di mekanisme_C1.txt")
        sebelum = lama.pop(i, None)
        if sebelum:
            if sebelum.get("key") and sebelum["key"] != key:
                catatan.append(f"key berubah dari {sebelum['key']}")
            for c in LAMA:
                v0 = (sebelum.get(f"kode_ai_{c}") or "").strip()
                if v0 and v0 != b[f"kode_ai_{c}"] and c != "hasil_ringkas":
                    catatan.append(f"kode_ai_{c} kini {b[f'kode_ai_{c}']} (sebelumnya {v0})")
            for k in MILIK_PENINJAU + MILIK_DRAF:
                b[k] = sebelum.get(k) or ""
        if i in draf:
            b.update(draf[i])
        b["catatan_skrip"] = "; ".join(catatan)
        baris.append(b)

    # Baris lama yang tidak lagi C1 disimpan bila sudah ada isian peninjau.
    for i, r in lama.items():
        if any((r.get(k) or "").strip() for k in MILIK_PENINJAU):
            r = dict(r)
            r["prioritas"] = 9
            r["catatan_skrip"] = "bukan C1 lagi di matriks_bukti.csv; tidak diterapkan"
            baris.append(r)

    baris.sort(key=lambda b: (int(b["prioritas"]), b.get("pdf_ada") != "Y",
                              -int(b.get("tahun") or 0), b["key"]))
    for n, b in enumerate(baris, 1):
        b["no"] = n
    VER.mkdir(parents=True, exist_ok=True)
    tulis_csv(LEMBAR, KOLOM, baris)
    from collections import Counter
    hit = Counter(int(b["prioritas"]) for b in baris)
    ada_draf = sum(1 for b in baris if any(b.get(k) for k in MILIK_DRAF))
    ada_final = sum(1 for b in baris if any((b.get(k) or "").strip() for k in MILIK_PENINJAU))
    print(f"{len(baris)} baris -> {LEMBAR.relative_to(ROOT)}; prioritas {dict(sorted(hit.items()))}; "
          f"berdraf {ada_draf}; berisian peninjau {ada_final}")


# ------------------------------------------------------------------ terapkan
def normal(kolom, v):
    v = " ".join((v or "").replace("\t", " ").split())
    if kolom in ("mekanisme", "akuisisi", "per_kelas"):
        return v.upper().replace(" ", "")
    if kolom in ("sumber_kode", "referensi_hitung", "tingkat_metrik", "cara_kelas"):
        return ";".join(x.strip() for x in v.lower().split(";") if x.strip())
    return v


def periksa(kolom, v, per_kelas):
    """Kembalikan pesan galat atau None."""
    if v == "":
        return None
    if kolom == "mekanisme" and not POLA_MEK.match(v):
        return f"mekanisme '{v}' tidak sah (contoh: M3, M3+M4, DATA)"
    if kolom == "akuisisi" and v not in AKUISISI:
        return f"akuisisi '{v}' tidak sah ({'/'.join(sorted(AKUISISI))})"
    if kolom == "per_kelas" and v not in ("Y", "N"):
        return f"per_kelas '{v}' tidak sah (Y/N)"
    if kolom == "sumber_kode" and v not in SUMBER:
        return f"sumber_kode '{v}' tidak sah ({' / '.join(sorted(SUMBER))})"
    for k, himp in (("referensi_hitung", REFERENSI), ("tingkat_metrik", TINGKAT)):
        if kolom == k:
            salah = [x for x in v.split(";") if x not in himp]
            if salah:
                return f"{k} {salah} tidak sah ({' / '.join(sorted(himp))})"
    if kolom == "cara_kelas":
        if v not in CARA:
            return f"cara_kelas '{v}' tidak sah ({' / '.join(sorted(CARA))})"
        if per_kelas == "N" and v != "-":
            return "cara_kelas diisi padahal per_kelas N (isi '-' atau kosongkan)"
    if kolom == "berubah" and not (v == "tidak" or v.startswith("ya")):
        return f"berubah '{v}' tidak sah (tidak / ya (lama: ...))"
    return None


def urai_berubah(v):
    m = re.match(r"^ya\s*\(lama:\s*(.*)\)\s*$", v or "")
    out = {}
    if m:
        for bag in m.group(1).split(";"):
            if "=" in bag:
                k, x = bag.split("=", 1)
                out[k.strip()] = x.strip()
    return out


def terapkan(oleh, kering):
    if not LEMBAR.exists():
        sys.exit("Lembar belum ada; jalankan skrip tanpa opsi dahulu.")
    teks_baris, manual = muat_manual()
    lembar = baca_csv(LEMBAR)
    rencana, galat, lewati = [], [], []
    for r in lembar:
        if not (r.get("idx") or "").strip():
            continue
        i = int(r["idx"])
        final = {c: normal(c, r.get(f"final_{c}")) for c in SEPULUH}
        if not any(final.values()):
            continue
        if not final["sumber_kode"]:
            lewati.append(f"idx {i}: final_sumber_kode kosong; baris belum dianggap selesai")
            continue
        if str(r.get("prioritas")) == "9" or i not in manual:
            lewati.append(f"idx {i}: bukan C1 atau tidak ada di mekanisme_C1.txt")
            continue
        kini = manual[i]
        # Lembar kedaluwarsa: kode sumber berubah sejak lembar dibuat.
        basi = [c for c in LAMA[:3] if (r.get(f"kode_ai_{c}") or "").strip()
                and r[f"kode_ai_{c}"].strip() != kini[c] and final[c] != kini[c]]
        if basi:
            galat.append(f"idx {i}: {basi} di mekanisme_C1.txt berubah sejak lembar dibuat; "
                         "jalankan ulang skrip tanpa opsi, periksa, lalu terapkan lagi")
            continue
        # '=' berarti menyetujui nilai yang ada (kode_ai) atau draf model.
        for c in SEPULUH:
            if final[c] == "=":
                final[c] = normal(c, kini[c] if c in LAMA else r.get(f"draf_ai_{c}"))
        baru = {c: (final[c] if final[c] != "" else kini[c]) for c in SEPULUH}
        berubah_lama = {c: kini[c] for c in LAMA if baru[c] != kini[c]}
        if baru["berubah"] == "" or final["berubah"] == "":
            tercatat = urai_berubah(kini["berubah"])
            for c, v in berubah_lama.items():
                tercatat.setdefault(c, v)
            baru["berubah"] = ("ya (lama: " + "; ".join(f"{c}={v}" for c, v in tercatat.items()) + ")"
                               if tercatat else "tidak")
        elif baru["berubah"] == "tidak" and berubah_lama:
            galat.append(f"idx {i}: final_berubah 'tidak' padahal {list(berubah_lama)} berubah")
            continue
        elif baru["berubah"].startswith("ya") and "(lama:" not in baru["berubah"]:
            baru["berubah"] = "ya (lama: " + "; ".join(f"{c}={v}" for c, v in berubah_lama.items()) + ")"
        pesan = [p for c in SEPULUH if (p := periksa(c, baru[c], baru["per_kelas"]))]
        if baru["per_kelas"] == "Y" and not baru["cara_kelas"]:
            pesan.append("per_kelas Y tetapi cara_kelas kosong")
        if pesan:
            galat += [f"idx {i}: {p}" for p in pesan]
            continue
        ubah = [(c, kini[c], baru[c]) for c in SEPULUH if baru[c] != kini[c]]
        alasan = (r.get("catatan_peninjau") or "").strip() or "verifikasi teks lengkap (Cek 5)"
        rencana.append((i, kini, baru, ubah, alasan))

    for p in lewati:
        print("LEWATI", p)
    if galat:
        for p in galat:
            print("GALAT ", p, file=sys.stderr)
        sys.exit(f"{len(galat)} galat; tidak ada yang ditulis. Perbaiki lembar lalu ulangi.")
    n_sel = sum(len(u) for *_, u, _ in rencana)
    for i, _, _, ubah, _ in rencana:
        for c, a, b in ubah:
            print(f"idx {i:>5} {c:16} {a!r:>30} -> {b!r}")
    print(f"{len(rencana)} baris siap, {n_sel} sel berubah")
    if kering or n_sel == 0:
        print("(mode kering: tidak ada yang ditulis)" if kering else "Tidak ada perubahan.")
        return
    if not oleh:
        sys.exit("--oleh INISIAL wajib untuk --terapkan")

    for i, kini, baru, ubah, _ in rencana:
        if not ubah:
            continue
        nilai = [baru[c] for c in SEPULUH]
        if not any(nilai[4:]):
            nilai = nilai[:4]
        teks_baris[kini["_baris"]] = "\t".join([str(i)] + nilai)
    tmp = MANUAL.with_suffix(".txt.tmp")
    tmp.write_text("\n".join(teks_baris), encoding="utf-8")
    os.replace(tmp, MANUAL)

    baru_log = not LOG.exists()
    if not baru_log and not LOG.read_bytes().endswith(b"\n"):
        with open(LOG, "ab") as f:
            f.write(b"\n")
    tanggal = datetime.date.today().isoformat()
    berkas = str(MANUAL.relative_to(KORPUS)).replace("\\", "/")
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        if baru_log:
            w.writerow(LOG_KEPALA)
        for i, _, _, ubah, alasan in rencana:
            for c, a, b in ubah:
                w.writerow([tanggal, berkas, i, c, a, b, alasan, oleh])
    print(f"Ditulis: {MANUAL.relative_to(ROOT)} dan {n_sel} baris log di {LOG.relative_to(ROOT)}")
    bangun_lembar()  # segarkan kode_ai_* di lembar; isian peninjau tetap
    print("Berikutnya: python3 tools/scopus/kode_bukti.py && python3 tools/scopus/gambar_tinjauan.py "
          "&& python3 tools/scopus/tabel_lampiran.py")


# ------------------------------------------------------------------ Fatma
KOLOM_FATMA_KODE = ["mekanisme", "akuisisi", "per_kelas", "sumber_kode", "halaman",
                    "referensi_hitung", "tingkat_metrik", "cara_kelas"]
BANDING = ["mekanisme", "akuisisi", "per_kelas", "referensi_hitung",
           "tingkat_metrik", "cara_kelas"]


def sampel_fatma(timpa):
    if SAMPEL.exists() and not timpa:
        sys.exit(f"{SAMPEL.relative_to(ROOT)} sudah ada; pakai --timpa untuk menarik ulang "
                 "(isian Fatma akan hilang).")
    mat = [r for r in csv.DictReader(open(MAT, encoding="utf-8")) if r["kode"] == "C1"]
    mat.sort(key=lambda r: int(r["idx"]))
    pilih = random.Random(BENIH_FATMA).sample(mat, N_FATMA)
    pilih.sort(key=lambda r: int(r["idx"]))
    kolom = ["no", "idx", "key", "tahun", "judul", "doi", "pdf_ada", "path_pdf"]
    kolom += [f"fatma_{c}" for c in KOLOM_FATMA_KODE] + ["catatan_fatma"]
    baris = []
    for n, r in enumerate(pilih, 1):
        pdf = KORPUS / "pdf" / f"{r['key']}.pdf"
        baris.append({"no": n, "idx": r["idx"], "key": r["key"], "tahun": r["year"],
                      "judul": r["title"], "doi": r["doi"],
                      "pdf_ada": "Y" if pdf.exists() else "N",
                      "path_pdf": str(pdf.relative_to(ROOT)).replace("\\", "/") if pdf.exists() else ""})
    VER.mkdir(parents=True, exist_ok=True)
    tulis_csv(SAMPEL, kolom, baris)
    print(f"{len(baris)} kajian (benih {BENIH_FATMA}) -> {SAMPEL.relative_to(ROOT)}")


def sama(c, a, b):
    if c == "mekanisme":
        return set(a.split("+")) == set(b.split("+"))
    if c in ("referensi_hitung", "tingkat_metrik"):
        return set(a.split(";")) == set(b.split(";"))
    if c == "cara_kelas":
        return (a or "-") == (b or "-")
    return a == b


def banding_fatma():
    fatma = baca_csv(SAMPEL)
    lembar = {int(r["idx"]): r for r in baca_csv(LEMBAR) if (r.get("idx") or "").strip()}
    _, manual = muat_manual()
    beda, belum, belum_p = [], [], []
    for r in fatma:
        i = int(r["idx"])
        if not (r.get("fatma_mekanisme") or "").strip():
            belum.append(i)
            continue
        baris_p = lembar.get(i) or {}
        if not (normal("sumber_kode", baris_p.get("final_sumber_kode"))
                or manual.get(i, {}).get("sumber_kode")):
            belum_p.append(i)
            continue
        acuan = {}
        for c in BANDING:
            f = normal(c, (lembar.get(i) or {}).get(f"final_{c}"))
            if f == "=":
                f = ""
            acuan[c] = f or manual.get(i, {}).get(c, "")
        d = [f"{c}: Fatma={normal(c, r.get(f'fatma_{c}'))!r} peninjau={acuan[c]!r}"
             for c in BANDING if not sama(c, normal(c, r.get(f"fatma_{c}")), acuan[c])]
        if d:
            beda.append((i, r["key"], d))
    for i, k, d in beda:
        print(f"BEDA idx {i} {k}: " + " | ".join(d))
    n = len(fatma) - len(belum) - len(belum_p)
    print(f"{len(beda)} dari {n} kajian yang sudah diisi Fatma dan peninjau berbeda "
          f"(ambang: >3 dari 20 -> cari penyebab dan periksa ulang baris terdampak)")
    if belum:
        print(f"belum diisi Fatma: {len(belum)} kajian")
    if belum_p:
        print(f"belum diverifikasi peninjau (final_sumber_kode kosong): idx {belum_p}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--draf", help="CSV draf model (idx + draf_ai_*) untuk diimpor ke lembar")
    ap.add_argument("--terapkan", action="store_true")
    ap.add_argument("--kering", action="store_true", help="dengan --terapkan: tampilkan saja")
    ap.add_argument("--oleh", help="inisial peninjau untuk kolom 'oleh' di log")
    ap.add_argument("--sampel-fatma", action="store_true")
    ap.add_argument("--timpa", action="store_true", help="dengan --sampel-fatma: tarik ulang")
    ap.add_argument("--banding-fatma", action="store_true")
    a = ap.parse_args()
    if a.terapkan:
        terapkan(a.oleh, a.kering)
    elif a.sampel_fatma:
        sampel_fatma(a.timpa)
    elif a.banding_fatma:
        banding_fatma()
    else:
        bangun_lembar(a.draf)


if __name__ == "__main__":
    main()
