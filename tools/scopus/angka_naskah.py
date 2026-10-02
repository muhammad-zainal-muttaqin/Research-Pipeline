#!/usr/bin/env python3
"""Menghitung semua angka korpus yang dikutip naskah main6.

  python tools/scopus/angka_naskah.py            # cetak ke layar
  python tools/scopus/angka_naskah.py --simpan   # tulis juga dua berkas keluaran

Keluaran (jangan disunting tangan):
  literature/scopus-2026-09/ANGKA-NASKAH.md   daftar angka, berurutan menurut seksi naskah
  manuscript/source/main6-angka.tex           makro LaTeX (\\nIncluded, \\pTrack, ...) yang dipakai teks naskah

Angka dihitung dari berkas yang sama dengan gambar (matriks_bukti.csv, keputusan
penyaringan, kode_C3.txt), sehingga teks naskah selalu mengikuti data. Skrip ini
tidak mengubah berkas data. Jalankan sesudah kode_bukti.py.
"""
import csv
import glob
import json
import re
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature/scopus-2026-09"
TOPIK = KORPUS / "topik"
AI2 = KORPUS / "verifikasi/ai2"
TEX = ROOT / "manuscript/source/main6-angka.tex"
MEK = ["M0", "M1", "M2", "M3", "M4", "M5"]
NAMA = {"M0": "no association", "M1": "statistical correction", "M2": "appearance matching",
        "M3": "temporal tracking", "M4": "geometric or 3D association", "M5": "learned association"}
MAKRO_MEK = {"M0": "None", "M1": "Stat", "M2": "App", "M3": "Track", "M4": "Geom", "M5": "Learn"}
METRIK = {"hitung": {"MAE", "RMSE", "R2", "MAPE/rel. error", "count accuracy"},
          "identitas": {"MOTA", "IDF1", "HOTA", "ID switch"},
          "deteksi": {"mAP/AP", "F1"}}
out = []
makro = {}


def tulis(s=""):
    out.append(s)


def m(nama, nilai):
    """Daftarkan makro \\<nama>. Bilangan bulat diberi pemisah ribuan LaTeX."""
    assert re.fullmatch(r"[A-Za-z]+", nama) and nama not in makro, nama
    if isinstance(nilai, int):
        nilai = f"{nilai:,}".replace(",", "{,}")
    makro[nama] = str(nilai)


def persen(a, b):
    return round(100 * a / b) if b else 0


def pct(a, b):
    return f"{a} dari {b} ({persen(a, b)}%)"


def baca(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def utama(r):
    return r["tanaman"].split(";")[0] if r["tanaman"] else "(tanaman tidak disebut)"


def eks(r):
    return "+".join(sorted(set(r["mekanisme"].split("+"))))


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
            mm = re.match(r"^(\d+)\s+(C[1-5]|T|R|M|X)(?:\s+(E\d))?", line)
            if mm:
                dec[int(mm.group(1))] = (mm.group(2), mm.group(3) or "")
                if "T00" in fn or "(judul)" in line:
                    judul_saja += 1
    xa = Counter(d[1] for d in dec.values() if d[0] == "X")
    inc = Counter(d[0] for d in dec.values() if d[0] != "X")
    p_lain = TOPIK / "tambahan_metode_lain.csv"
    lain = baca(p_lain) if p_lain.exists() else []
    n_scopus = sum(inc.values())
    tulis("## Seksi 2: alur rekaman\n")
    tulis(f"- Rekaman diambil {diambil:,}; unik {unik:,}; duplikat {diambil - unik:,}")
    tulis(f"- Dibuang menurut tipe dokumen {x0}; judul disaring {unik - x0:,}; dikeluarkan di tahap judul {xj:,}")
    tulis(f"- Dinilai kelayakannya {len(dec):,} (dengan abstrak {len(dec) - judul_saja}; judul dan sumber saja {judul_saja})")
    tulis(f"- Dikeluarkan di tahap kelayakan {sum(xa.values())}: " + ", ".join(f"{k} {xa[k]}" for k in sorted(xa)))
    tulis(f"- Masuk peta dari Scopus {n_scopus}: " + ", ".join(f"{k} {inc[k]}" for k in ["C1", "C2", "C3", "C4", "C5", "R", "T"]))
    tulis(f"- Metode lain {len(lain)}: " + ", ".join(f"{r['key']} ({r['kode']})" for r in lain))
    tulis(f"- Total kajian masuk {n_scopus + len(lain)}")
    m("nRetrieved", diambil)
    m("nUnique", unik)
    m("nDocType", x0)
    m("nTitles", unik - x0)
    m("nTitleExcl", xj)
    m("nAssessed", len(dec))
    m("nNoAbstract", judul_saja)
    m("nEligExcl", sum(xa.values()))
    for i, nama in enumerate(["One", "Two", "Three", "Four", "Five", "Six", "Seven"], 1):
        m(f"nExcl{nama}", xa[f"E{i}"])
    m("nScopusIncl", n_scopus)
    m("nOther", len(lain))
    m("nIncluded", n_scopus + len(lain))
    lain_k = Counter(r["kode"] for r in lain)
    for kode, nama in [("C1", "Multi"), ("C2", "Single"), ("C3", "Palm"), ("C4", "ClassSingle"), ("C5", "Depth"),
                       ("R", "Reviews"), ("T", "Outside")]:
        m(f"n{nama}", inc[kode] + lain_k[kode])
    th = Counter(int(r["year"]) for r in mat)
    tulis("- Kajian per tahun: " + ", ".join(f"{t}: {th[t]}" for t in sorted(th)))
    c1_th = Counter(int(r["year"]) for r in mat if r["kode"] == "C1")
    tulis("- Multi-pengamatan per tahun: " + ", ".join(f"{t}: {c1_th[t]}" for t in sorted(c1_th)))
    n_abs = sum(1 for r in mat if r["ada_abstrak"] == "ya")
    n_teks = sum(1 for r in mat if (KORPUS / "teks" / (r["key"] + ".txt")).exists())
    tulis(f"- Dengan abstrak {n_abs} dari {len(mat)}; teks lengkap lokal {n_teks}")
    m("nYearFirst", th[2012])
    m("nYearPeak", th[2025])
    m("nMultiEarlyMax", max(c1_th[t] for t in range(2012, 2020)))
    m("nMultiPeak", c1_th[2025])
    m("nWithAbstract", n_abs)
    m("nFullText", n_teks)

    # peta istilah (aturan sama dengan gambar_istilah di gambar_tinjauan.py)
    from gambar_tinjauan import ISTILAH
    abstrak = {}
    for line in open(TOPIK / "enrich.jsonl", encoding="utf-8"):
        d = json.loads(line)
        abstrak[d["eid"]] = d.get("abstract") or ""
    frek, pasangan = Counter(), Counter()
    for r in mat:
        teks = (r["title"] + " " + abstrak.get(r["eid"], "")).lower()
        ada = sorted(lab for lab, pola in ISTILAH if re.search(pola, teks))
        frek.update(ada)
        pasangan.update(combinations(ada, 2))
    simpul = {lab for lab, _ in ISTILAH if frek[lab] >= 20}
    sisi = sum(1 for (a, b), w in pasangan.items() if w >= 12 and a in simpul and b in simpul)
    ident = [frek[k] for k in ("data association", "re-identification", "double counting", "multi-view")]
    tulis(f"- Peta istilah: {len(simpul)} istilah, {sisi} tautan; istilah identitas {min(ident)}-{max(ident)} kajian; "
          f"detection {frek['detection']}; counting {frek['counting']}")
    m("nTerms", len(simpul))
    m("nLinks", sisi)
    m("nIdentTermMin", min(ident))
    m("nIdentTermMax", max(ident))
    m("nTermDetection", frek["detection"])
    m("nTermCounting", frek["counting"])

    # ---------------------------------------------------------------- C1
    c1 = [r for r in mat if r["kode"] == "C1"]
    met = [r for r in c1 if r["mekanisme"] != "DATA"]
    n = len(met)
    tulis("\n## Seksi 3: kajian multi-pengamatan\n")
    tulis(f"- Multi-pengamatan {len(c1)}; makalah dataset {len(c1) - n}; kajian metode {n}")
    m("nMultiData", len(c1) - n)
    m("nMethod", n)
    occ = Counter(k for r in met for k in set(r["mekanisme"].split("+")))
    tulis("- Kemunculan mekanisme: " + "; ".join(f"{NAMA[k]} {pct(occ[k], n)}" for k in ["M3", "M4", "M2", "M1", "M0", "M5"]))
    for k in MEK:
        m(f"n{MAKRO_MEK[k]}", occ[k])
        m(f"p{MAKRO_MEK[k]}", persen(occ[k], n))
    n_gab = sum(1 for r in met if "+" in r["mekanisme"])
    tulis(f"- Kajian yang menggabungkan mekanisme: {n_gab}")
    m("nCombined", n_gab)
    e = Counter(eks(r) for r in met)
    tulis("- Kategori eksklusif: " + ", ".join(f"{k} {v}" for k, v in e.most_common()))
    for k, nama in [("M3", "TrackOnly"), ("M4", "GeomOnly"), ("M2+M3", "AppTrack"), ("M3+M4", "TrackGeom"),
                    ("M1", "StatOnly"), ("M0", "NoneOnly"), ("M2", "AppOnly"), ("M5", "LearnOnly")]:
        m(f"n{nama}", e[k])
    m("nOtherComb", n - sum(e[k] for k in ("M0", "M1", "M2", "M3", "M4", "M5", "M2+M3", "M3+M4")))
    m("nAppWith", occ["M2"] - e["M2"])
    ak = Counter(r["akuisisi_manual"] for r in met)
    tulis("- Akuisisi (V video, D diskret, S pindaian 3D, T kunjungan ulang, 1 satu pandang): "
          + ", ".join(f"{k} {ak[k]}" for k in ["V", "D", "S", "T", "1"]))
    for k, nama in [("V", "Video"), ("D", "Discrete"), ("S", "Scan"), ("T", "Revisit"), ("1", "SingleView")]:
        m(f"n{nama}", ak[k])
    for nama, a, b in [("2012-2017", 2012, 2017), ("2018-2020", 2018, 2020), ("2021-2022", 2021, 2022),
                       ("2023-2024", 2023, 2024), ("2025-2026", 2025, 2026), ("sejak 2023", 2023, 2026)]:
        s = [r for r in met if a <= int(r["year"]) <= b]
        o = Counter(k for r in s for k in set(r["mekanisme"].split("+")))
        tulis(f"- Periode {nama} (n = {len(s)}): " + ", ".join(f"{k} {o[k]} ({persen(o[k], len(s))}%)" for k in MEK if o[k]))
        if nama == "2012-2017":
            m("nEarly", len(s))
            m("nEarlyStat", o["M1"])
            m("nEarlyGeom", o["M4"])
            m("nEarlyTrack", o["M3"])
        if nama == "sejak 2023":
            m("nRecent", len(s))
            m("pTrackRecent", persen(o["M3"], len(s)))
            m("pAppRecent", persen(o["M2"], len(s)))
    tan = Counter(utama(r) for r in met)
    tulis("- Tanaman: " + ", ".join(f"{k} {v}" for k, v in tan.most_common(12)))
    for k, nama in [("apple", "Apple"), ("citrus", "Citrus"), ("grape", "Grape"), ("tomato", "Tomato"),
                    ("strawberry", "Strawberry"), ("mango", "Mango")]:
        m(f"nCrop{nama}", tan[k])
    n_kelas = sum(1 for r in met if r["per_kelas"] == "Y")
    tulis(f"- Melaporkan hitungan per kelas: {n_kelas} dari {n}")
    m("nPerClass", n_kelas)
    tulis("- Akuisisi x kategori mekanisme: " + "; ".join(
        f"{a}: " + ", ".join(f"{k} {v}" for k, v in Counter(eks(r) for r in met if r["akuisisi_manual"] == a).most_common(5))
        for a in ["V", "D", "S", "T", "1"] if ak[a]))
    d_geo = sum(1 for r in met if r["akuisisi_manual"] == "D" and "M4" in r["mekanisme"].split("+"))
    d_stat = sum(1 for r in met if r["akuisisi_manual"] == "D" and "M1" in r["mekanisme"].split("+"))
    tulis(f"- Pandangan diskret: dengan asosiasi geometris {d_geo}, dengan koreksi statistik {d_stat}")
    m("nDiscreteGeom", d_geo)
    m("nDiscreteStat", d_stat)
    plat = Counter()
    for r in met:
        p = [x for x in r["platform"].split(";") if x]
        plat["tidak disebut" if not p else ("lebih dari satu" if len(p) > 1 else p[0])] += 1
    tulis("- Platform (satu kategori per kajian): " + ", ".join(f"{k} {v}" for k, v in plat.most_common()))
    for k, nama in [("tidak disebut", "PlatNone"), ("ground vehicle/robot", "PlatGround"), ("UAV", "PlatUav"),
                    ("handheld/smartphone", "PlatHand"), ("lebih dari satu", "PlatSeveral"), ("conveyor/lab", "PlatLab")]:
        m(f"n{nama}", plat[k])
    mod = Counter(k for r in met for k in r["modalitas"].split(";"))
    tulis("- Modalitas (kemunculan): " + ", ".join(f"{k} {v}" for k, v in mod.most_common()))
    for k, nama in [("RGB", "ModRgb"), ("RGB-D", "ModRgbd"), ("stereo", "ModStereo"), ("LiDAR", "ModLidar"),
                    ("multispectral", "ModMulti")]:
        m(f"n{nama}", mod[k])
    tulis(f"- Pencocokan penampilan: satu-satunya mekanisme pada {e['M2']}, digabung pada {occ['M2'] - e['M2']}")
    for k in ["M0", "M5"]:
        tulis(f"- Kajian {NAMA[k]}: " + ", ".join(sorted(r["key"] for r in met if k in r["mekanisme"].split("+"))))
    tulis("- Makalah dataset: " + ", ".join(sorted(r["key"] for r in c1 if r["mekanisme"] == "DATA")))
    dasar = Counter((r.get("sumber_kode") or "").strip() or r["dasar_keputusan"] for r in c1)
    tulis("- Dasar pengodean kajian multi-pengamatan: " + ", ".join(f"{k} {v}" for k, v in dasar.most_common()))
    m("nCodedFull", dasar["teks lengkap"])
    m("nCodedAbs", dasar["abstrak"])
    m("nCodedTitle", dasar["judul"])
    if "sumber_kode" in mat[0]:
        rh = Counter(x for r in met for x in r["referensi_hitung"].split(";") if x)
        tulis("- Referensi hitung (kemunculan): " + ", ".join(f"{k} {v}" for k, v in rh.most_common()))
        tm = Counter(x for r in met for x in r["tingkat_metrik"].split(";") if x)
        tulis("- Tingkat metrik menurut pengodean kajian (kemunculan): " + ", ".join(f"{k} {v}" for k, v in tm.most_common()))
        ck = Counter(r["cara_kelas"] or "(kosong)" for r in met if r["per_kelas"] == "Y")
        tulis("- Cara pemberian kelas pada kajian per kelas: " + ", ".join(f"{k} {v}" for k, v in ck.most_common()))
        for k, nama in [("pohon", "RefTree"), ("panen", "RefHarvest"), ("packhouse", "RefPack"), ("anotasi", "RefAnnot"),
                        ("tidak ada", "RefNone")]:
            m(f"n{nama}", rh[k])
        m("nClassDuring", ck["saat pelacakan"])
        m("nClassAfter", ck["sesudah pelacakan"])
        m("nClassVote", ck["voting antarpandang"])
        m("nClassUnstated", ck["tidak dinyatakan"] + ck["(kosong)"])

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
    m("nMethodAbs", len(ada))
    for k, nama in [("hitung", "MetCount"), ("deteksi", "MetDet"), ("identitas", "MetIdent"), ("tanpa metrik", "MetNone")]:
        m(f"n{nama}", hit[k])
        m(f"p{nama}", persen(hit[k], len(ada)))

    # ---------------------------------------------------------------- C4, C5
    c4 = [r for r in mat if r["kode"] == "C4"]
    t4 = Counter(utama(r) for r in c4)
    n_mat = sum(1 for r in c4 if "maturity" in r["atribut_kelas"].split(";"))
    tulis("\n## Seksi 6: pencacahan per kelas pada citra tunggal\n")
    tulis(f"- Kajian {len(c4)}; tanaman: " + ", ".join(f"{k} {v}" for k, v in t4.most_common(6)))
    tulis(f"- Atribut kelas kematangan: {n_mat}")
    m("nClassSingleTomato", t4["tomato"])
    m("nClassSingleBlueberry", t4["blueberry"])
    m("nClassSingleMaturity", n_mat)
    c5 = [r for r in mat if r["kode"] == "C5"]
    m5 = Counter(k for r in c5 for k in r["modalitas"].split(";"))
    t5 = Counter(utama(r) for r in c5)
    tulis("\n## Seksi 7: kedalaman dan sensor lain\n")
    tulis(f"- Kajian {len(c5)}; modalitas (kemunculan): " + ", ".join(f"{k} {v}" for k, v in m5.most_common()))
    tulis("- Tanaman: " + ", ".join(f"{k} {v}" for k, v in t5.most_common(5)))
    m("nDepthRgbd", m5["RGB-D"])
    m("nDepthStereo", m5["stereo"])
    m("nDepthLidar", m5["LiDAR"])
    m("nDepthApple", t5["apple"])

    # ---------------------------------------------------------------- C3
    c3 = {}
    for line in open(TOPIK / "bukti/kode_C3.txt", encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("\t")
        c3[int(p[0])] = p[1:6]
    tg, lk = Counter(v[0] for v in c3.values()), Counter(v[1] for v in c3.values())
    tulis("\n## Seksi 8: kelapa sawit\n")
    tulis(f"- Kajian {len(c3)} (matriks: {sum(1 for r in mat if r['kode'] == 'C3')})")
    tulis("- Tugas: " + ", ".join(f"{k} {v}" for k, v in tg.most_common()))
    tulis("- Lokasi: " + ", ".join(f"{k} {v}" for k, v in lk.most_common()))
    tulis("- Modalitas: " + ", ".join(f"{k} {v}" for k, v in Counter(v[2] for v in c3.values()).most_common()))
    n_mv, n_pk = sum(1 for v in c3.values() if v[3] == "Y"), sum(1 for v in c3.values() if v[4] == "Y")
    tulis(f"- Multipandang Y: {n_mv}; kelas per instans Y: {n_pk}")
    key = {int(r["idx"]): r["key"] for r in mat}
    tulis("- Kajian pencacahan (HIT): " + ", ".join(sorted(key.get(i, str(i)) for i, v in c3.items() if v[0] == "HIT")))
    tulis("- Kajian multipandang: " + ", ".join(sorted(key.get(i, str(i)) for i, v in c3.items() if v[3] == "Y")))
    for k, nama in [("KLS", "PalmCls"), ("DET", "PalmDet"), ("SENSOR", "PalmSensor"), ("MUTU", "PalmQual"),
                    ("LF", "PalmLoose"), ("HIT", "PalmCount"), ("DATA", "PalmData")]:
        m(f"n{nama}", tg[k])
    for k, nama in [("POHON", "PalmOnTree"), ("PABRIK", "PalmMill"), ("TANAH", "PalmGround"), ("UAV", "PalmUav"),
                    ("?", "PalmUnstated")]:
        m(f"n{nama}", lk[k])
    m("nPalmViews", n_mv)
    m("nPalmInstClass", n_pk)

    tulis("\n## Seksi 9: tinjauan terdahulu dan metode luar pertanian\n")
    tulis(f"- Tinjauan terdahulu {inc['R']} (+ {lain_k['R']} metode lain); metode luar pertanian {inc['T']}")

    # ---------------------------------------------------------------- verifikasi putaran kedua
    p_final = AI2 / "keputusan_final.csv"
    if p_final.exists():
        fin = baca(p_final)
        st = Counter(r["status"] for r in fin)
        bk = baca(AI2 / "banding_kelayakan.csv")
        sama = sum(1 for r in bk if r["status_grup"] in ("sama", "lunak"))
        tulis("\n## Verifikasi putaran kedua (model bahasa besar; bukan peninjau manusia)\n")
        tulis(f"- Rekaman kunci dinilai ulang {len(bk)}; kelompok sama atau juga cocok {pct(sama, len(bk))}; "
              f"ada perbedaan kode apa pun {sum(1 for r in bk if r['beda'])}")
        tulis(f"- Status akhir ({len(fin)} rekaman termasuk tambahan): " + ", ".join(f"{k} {v}" for k, v in st.most_common()))
        m("nSecondPass", len(bk))
        m("pSecondAgree", persen(sama, len(bk)))
        m("nAdjudicated", sum(1 for r in bk if r["beda"]))
        m("nGroupChanged", st["kelompok berubah"])
        m("nGroupNotUpheld", st["sengketa"])
        m("nNeedsHuman", st["perlu manusia"])
        bs = baca(AI2 / "banding_sampel.csv")
        sj = [r for r in bs if r["tahap"] == "judul"]
        sa = [r for r in bs if r["tahap"] == "kelayakan"]
        j_sama = sum(1 for r in sj if r["sama"] == "ya")
        j_lanjut = sum(1 for r in sj if r["ai1"].startswith("X") and r["ai2"].startswith("L"))
        a_sama = sum(1 for r in sa if r["sama"] in ("ya", "kelompok sama"))
        tulis(f"- Sampel judul {len(sj)}: sama {pct(j_sama, len(sj))}; putaran 1 eksklusi tetapi putaran 2 lanjut {j_lanjut}")
        tulis(f"- Sampel kelayakan {len(sa)}: kelompok sama {pct(a_sama, len(sa))}")
        m("nSampleTitles", len(sj))
        m("pSampleTitles", persen(j_sama, len(sj)))
        m("nSampleTitlesFlagged", j_lanjut)
        m("nSampleElig", len(sa))
        m("pSampleElig", persen(a_sama, len(sa)))
        t_hasil = [x for fn in sorted(glob.glob(str(AI2 / "hasil/t_*.json"))) for x in json.load(open(fn, encoding="utf-8"))]
        t_masuk = Counter(x["kode"] for x in t_hasil if x["kode"] != "X")
        tulis(f"- Dari {len(t_hasil)} judul sampel yang dilanjutkan putaran 2, layak menurut abstrak: {sum(t_masuk.values())} "
              f"({dict(t_masuk)})")
        m("nSampleTitlesEligible", sum(t_masuk.values()))
        cf = baca(AI2 / "cek_fakta_ai2.csv")
        cfc = Counter(r["benar_ai2"] for r in cf)
        vf = [k for fn in sorted(glob.glob(str(AI2 / "hasil/vf_*.json"))) for s in json.load(open(fn, encoding="utf-8")) for k in s["klaim"]]
        vfc = Counter(k["putusan"] for k in vf)
        tulis(f"- Cek fakta: {len(cf)} pasangan klaim-kajian; Y {cfc['Y']}, SEBAGIAN {cfc['SEBAGIAN']}, N {cfc['N']}, "
              f"tak terperiksa {cfc['TAK-TERPERIKSA']}; verifikasi kedua atas {len(vf)}: {dict(vfc)}")
        m("nClaims", len(cf))
        m("nClaimsOk", cfc["Y"])
        m("nClaimsFlagged", cfc["SEBAGIAN"] + cfc["N"])
        m("nClaimsUnchecked", cfc["TAK-TERPERIKSA"])
        m("nClaimsCorrected", vfc["SEBAGIAN"] + vfc["N"])
    p_u = sorted(glob.glob(str(AI2 / "hasil/u_[0-9]*.json")))
    if p_u:
        u = [x for fn in p_u for x in json.load(open(fn, encoding="utf-8"))]
        ref = {x["idx"]: x for fn in sorted(glob.glob(str(AI2 / "hasil/ref_ru_[0-9]*.json")))
               for x in json.load(open(fn, encoding="utf-8"))}
        masuk = Counter(x["kode"] for x in u if x["kode"] != "X" and ref.get(x["idx"], {}).get("bertahan") is True)
        tulis(f"- Pemeriksaan ulang eksklusi tahap judul (Q1, Q3): {len(u)} rekaman; dimasukkan kembali {sum(masuk.values())} "
              f"({dict(masuk)})")
        m("nTitleRecheck", len(u))
        m("nTitleReinstated", sum(masuk.values()))
        m("nTitleReinstatedMulti", masuk["C1"])
        m("nTitleReinstatedPalm", masuk["C3"])

    teks = "\n".join(out) + "\n"
    print(teks)
    if "--simpan" in sys.argv:
        kepala = ("# Angka Naskah `main6`\n\nDibuat `tools/scopus/angka_naskah.py`; jangan disunting tangan. "
                  "Teks naskah memakai angka ini melalui makro di `manuscript/source/main6-angka.tex`.\n\n")
        (KORPUS / "ANGKA-NASKAH.md").write_text(kepala + teks, encoding="utf-8", newline="\n")
        baris = ["%% Dibuat otomatis oleh tools/scopus/angka_naskah.py; jangan disunting manual.",
                 "%% Setiap makro adalah satu angka korpus yang dihitung dari literature/scopus-2026-09."]
        # Makro persentase (awalan p) selalu diikuti \% di naskah, jadi tanpa \xspace.
        baris += [f"\\newcommand{{\\{k}}}{{{v}{'' if k.startswith('p') else chr(92) + 'xspace'}}}"
                  for k, v in sorted(makro.items())]
        TEX.write_text("\n".join(baris) + "\n", encoding="utf-8", newline="\n")
        print(f"{len(makro)} makro -> {TEX}")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
