#!/usr/bin/env python3
"""Menggabungkan hasil putaran kedua (AI-2) dan membandingkannya dengan putaran pertama.

  python tools/scopus/verifikasi_ai2_gabung.py

Keluaran di literature/scopus-2026-09/verifikasi/ai2/:
  banding_kelayakan.csv   510 rekaman C1/C3/X: keputusan dan kode kedua putaran, tanda beda
  banding_sampel.csv      sampel buta Cek 1 (tahap judul dan tahap kelayakan)
  cek_fakta_ai2.csv       penilaian klaim naskah terhadap sumbernya
  RINGKASAN-BANDING.md    angka kesepakatan antarputaran
  berkas/adj_NNN.json     paket ajudikasi: rekaman yang berbeda antara dua putaran
  berkas/vf_NNN.json      paket verifikasi: klaim yang dinilai N atau SEBAGIAN

Skrip hanya membaca berkas keputusan sumber; tidak ada yang diubah di topik/.
"""
import csv
import json
import random
import sys
from collections import Counter, defaultdict

from verifikasi_ai2 import (AI2, BENIH, BERKAS, HASIL, KORPUS, SNAP, TOPIK, VER, baca_csv, kemas,
                            muat_abstrak, muat_keputusan, tulis_json)

# --tanpa-paket: paket adj/vf sedang atau sudah dikerjakan, jangan dibuat ulang.
TANPA_PAKET = "--tanpa-paket" in sys.argv

SINONIM_MOD = {"RGB-D": "RGB+DEPTH", "RGBD": "RGB+DEPTH", "THERMAL": "TERMAL", "MULTISPEKTRAL": "MSI",
               "MULTISPECTRAL": "MSI", "HIPERSPEKTRAL": "HSI", "HYPERSPECTRAL": "HSI", "NIR": "NIR",
               "KEDALAMAN": "DEPTH"}


def muat_tab(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("\t")
        out[int(p[0])] = p[1:]
    return out


def muat_hasil(awalan):
    out = []
    for b in sorted(BERKAS.glob(f"{awalan}_[0-9]*.json")):
        h = HASIL / b.name
        if h.exists():
            for x in json.loads(h.read_text(encoding="utf-8")):
                x["_paket"] = b.name
                out.append(x)
    return out


def himp_mek(v):
    return frozenset(str(v).replace(" ", "").split("+")) if v else frozenset()


def himp_mod(v):
    v = str(v).upper().replace(" ", "")
    for a, b in SINONIM_MOD.items():
        v = v.replace(a, b)
    return frozenset(x for x in v.split("+") if x)


def kappa(pasangan):
    n = len(pasangan)
    if not n:
        return None, None
    po = sum(1 for a, b in pasangan if a == b) / n
    ca, cb = Counter(a for a, _ in pasangan), Counter(b for _, b in pasangan)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return po, ((po - pe) / (1 - pe) if pe < 1 else 1.0)


def fmt(x, pct=False):
    if x is None:
        return "-"
    return f"{100 * x:.1f}%".replace(".", ",") if pct else f"{x:.3f}".replace(".", ",")


def tulis_csv(path, kolom, baris):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=kolom, extrasaction="ignore")
        w.writeheader()
        w.writerows(baris)


def banding_kelayakan(md):
    asal = SNAP if SNAP.exists() else None  # putaran pertama dibaca dari salinannya bila sudah ada
    dec = muat_keputusan(asal)
    c1 = muat_tab((asal or TOPIK / "bukti") / "mekanisme_C1.txt")
    c3 = muat_tab((asal or TOPIK / "bukti") / "kode_C3.txt")
    rec = {int(r["idx"]): r for r in baca_csv(TOPIK / "records_all.csv")}
    ab = muat_abstrak()
    paket_asal = {}
    for b in sorted(BERKAS.glob("s_*.json")):
        for x in json.loads(b.read_text(encoding="utf-8")):
            paket_asal[x["idx"]] = x
    hasil = {x["idx"]: x for x in muat_hasil("s")}
    baris, adj = [], []
    for idx, x in sorted(paket_asal.items()):
        d = dec[idx]
        h = hasil.get(idx)
        b = {"idx": idx, "key": x["key"], "tahun": x["tahun"], "judul": x["judul"],
             "dasar_ai1": d["dasar"], "kode_ai1": d["kode"], "alasan_ai1": d["alasan"]}
        if not h:
            b["status_grup"] = "belum"
            baris.append(b)
            continue
        beda = []
        juga = h.get("juga_cocok", [])
        b.update({"dasar_ai2": h["dasar_bukti"], "kode_ai2": h["kode"], "alasan_ai2": h.get("alasan", ""),
                  "juga_cocok_ai2": ";".join(juga), "keyakinan_ai2": h["keyakinan"],
                  "bukti_ai2": " || ".join(h.get("bukti", [])), "catatan_ai2": h.get("catatan", "")})
        if d["kode"] == h["kode"]:
            b["status_grup"] = "sama"
            if d["kode"] == "X" and d["alasan"] != h.get("alasan", ""):
                beda.append("alasan")
        elif d["kode"] in juga:
            b["status_grup"] = "lunak"
            beda.append("grup(lunak)")
        else:
            b["status_grup"] = "beda"
            beda.append("grup")
        ai1 = {"kode": d["kode"], "alasan": d["alasan"], "dasar": d["dasar"]}
        if d["kode"] == "C1" and idx in c1:
            p = c1[idx] + [""] * 4
            ai1["c1"] = {"mekanisme": p[0], "akuisisi": p[1], "per_kelas": p[2], "hasil_ringkas": p[3]}
            b.update({"mek_ai1": p[0], "akuisisi_ai1": p[1], "per_kelas_c1_ai1": p[2]})
            k = h.get("c1")
            if isinstance(k, dict):
                b.update({"mek_ai2": k["mekanisme"], "akuisisi_ai2": k["akuisisi"],
                          "per_kelas_c1_ai2": k["per_kelas"]})
                if himp_mek(p[0]) != himp_mek(k["mekanisme"]):
                    beda.append("mekanisme")
                if p[1] != k["akuisisi"]:
                    beda.append("akuisisi")
                if p[2] != k["per_kelas"]:
                    beda.append("per_kelas")
        if d["kode"] == "C3" and idx in c3:
            p = c3[idx] + [""] * 5
            ai1["c3"] = {"tugas": p[0], "lokasi": p[1], "modalitas": p[2], "multipandang": p[3], "per_kelas": p[4]}
            b.update({"tugas_ai1": p[0], "lokasi_ai1": p[1], "modalitas_ai1": p[2],
                      "multipandang_ai1": p[3], "per_kelas_c3_ai1": p[4]})
            k = h.get("c3")
            if isinstance(k, dict):
                b.update({"tugas_ai2": k["tugas"], "lokasi_ai2": k["lokasi"], "modalitas_ai2": k["modalitas"],
                          "multipandang_ai2": k["multipandang"], "per_kelas_c3_ai2": k["per_kelas"]})
                if p[0] != k["tugas"]:
                    beda.append("tugas")
                if p[1] != k["lokasi"]:
                    if p[1] == "?":
                        beda.append("lokasi(isi)")
                    elif k["lokasi"] == "?":
                        if h["dasar_bukti"].startswith("teks lengkap"):
                            beda.append("lokasi(hilang)")
                    else:
                        beda.append("lokasi")
                if himp_mod(p[2]) != himp_mod(k["modalitas"]) and p[2] != "?":
                    beda.append("modalitas")
                if p[3] != k["multipandang"]:
                    beda.append("multipandang")
                if p[4] != k["per_kelas"]:
                    beda.append("per_kelas")
        b["beda"] = ";".join(beda)
        baris.append(b)
        # Beda lunak (kode putaran 1 juga dinilai cocok oleh putaran 2) bukan sengketa kelompok:
        # kelompok putaran 1 dipertahankan dan hanya beda kode lain yang diajudikasi.
        if [x for x in beda if x != "grup(lunak)"]:
            e = ab.get(rec[idx]["eid"], {})
            adj.append({"idx": idx, "key": x["key"], "judul": x["judul"], "tahun": x["tahun"],
                        "sumber": x["sumber"], "doi": x["doi"], "abstrak": x["abstrak"],
                        "teks_lengkap": x["teks_lengkap"], "pdf": x["pdf"], "beda": beda,
                        "putaran_1": ai1,
                        "putaran_2": {k: v for k, v in h.items() if not k.startswith("_") and k not in ("idx", "key")}})
    kolom = ["idx", "key", "tahun", "judul", "status_grup", "beda", "dasar_ai1", "kode_ai1", "alasan_ai1",
             "dasar_ai2", "kode_ai2", "alasan_ai2", "juga_cocok_ai2", "keyakinan_ai2",
             "mek_ai1", "mek_ai2", "akuisisi_ai1", "akuisisi_ai2", "per_kelas_c1_ai1", "per_kelas_c1_ai2",
             "tugas_ai1", "tugas_ai2", "lokasi_ai1", "lokasi_ai2", "modalitas_ai1", "modalitas_ai2",
             "multipandang_ai1", "multipandang_ai2", "per_kelas_c3_ai1", "per_kelas_c3_ai2",
             "bukti_ai2", "catatan_ai2"]
    tulis_csv(AI2 / "banding_kelayakan.csv", kolom, baris)

    # ringkasan
    ada = [b for b in baris if b["status_grup"] != "belum"]
    md.append("## 1. Rekaman kunci tahap kelayakan (C1, C3, dan eksklusi)\n")
    md.append(f"Putaran kedua menilai {len(ada)} dari {len(baris)} rekaman tanpa melihat keputusan putaran pertama.\n")
    kat = lambda k: k if k in ("C1", "C3", "X") else "lain"  # noqa: E731
    po, kp = kappa([(b["kode_ai1"], kat(b["kode_ai2"])) for b in ada])
    md.append(f"Kesepakatan kelompok (C1, C3, X, lain): {fmt(po, True)}; kappa Cohen {fmt(kp)}.\n")
    md.append("| Putaran 1 | n | sama | AI-2: kode lain, tetapi kode putaran 1 juga cocok | berbeda |")
    md.append("|---|---:|---:|---:|---:|")
    for k in ("C1", "C3", "X"):
        s = [b for b in ada if b["kode_ai1"] == k]
        md.append(f"| {k} | {len(s)} | {sum(1 for b in s if b['status_grup'] == 'sama')} | "
                  f"{sum(1 for b in s if b['status_grup'] == 'lunak')} | "
                  f"{sum(1 for b in s if b['status_grup'] == 'beda')} |")
    md.append("")
    md.append("Arah perbedaan kelompok (putaran 1 -> putaran 2):\n")
    arah = Counter((b["kode_ai1"], b["kode_ai2"]) for b in ada if b["status_grup"] != "sama")
    for (a, c), n in arah.most_common():
        md.append(f"- {a} -> {c}: {n}")
    md.append("")
    md.append("Kesepakatan kode pada rekaman yang kelompoknya sama:\n")
    md.append("| Kolom | n dibandingkan | sama | % |")
    md.append("|---|---:|---:|---:|")
    for nama, a1, a2, sama in [
        ("C1 mekanisme", "mek_ai1", "mek_ai2", lambda a, c: himp_mek(a) == himp_mek(c)),
        ("C1 akuisisi", "akuisisi_ai1", "akuisisi_ai2", lambda a, c: a == c),
        ("C1 per kelas", "per_kelas_c1_ai1", "per_kelas_c1_ai2", lambda a, c: a == c),
        ("C3 tugas", "tugas_ai1", "tugas_ai2", lambda a, c: a == c),
        ("C3 lokasi", "lokasi_ai1", "lokasi_ai2", lambda a, c: a == c),
        ("C3 modalitas", "modalitas_ai1", "modalitas_ai2", lambda a, c: himp_mod(a) == himp_mod(c)),
        ("C3 multipandang", "multipandang_ai1", "multipandang_ai2", lambda a, c: a == c),
        ("C3 per kelas", "per_kelas_c3_ai1", "per_kelas_c3_ai2", lambda a, c: a == c),
        ("X alasan", "alasan_ai1", "alasan_ai2", lambda a, c: a == c),
    ]:
        if nama == "X alasan":
            s = [b for b in ada if b["kode_ai1"] == "X" and b["kode_ai2"] == "X"]
        else:
            s = [b for b in ada if b.get(a1) and b.get(a2)]
        if s:
            k = sum(1 for b in s if sama(b[a1], b[a2]))
            md.append(f"| {nama} | {len(s)} | {k} | {fmt(k / len(s), True)} |")
    md.append("")
    md.append(f"Dasar bukti putaran kedua: {dict(Counter(b['dasar_ai2'] for b in ada))}.\n")
    md.append(f"Rekaman yang masuk ajudikasi (ada perbedaan apa pun): **{len(adj)}**.\n")

    rng = random.Random(BENIH + 1)
    paket = kemas(adj, lambda x: 3 if x["teks_lengkap"] else 1.5, 12, rng)
    if not TANPA_PAKET:
        for lama in BERKAS.glob("adj_*.json"):
            lama.unlink()
        for i, p in enumerate(paket):
            tulis_json(BERKAS / f"adj_{i:03d}.json", p)
    print(f"kelayakan: {len(ada)}/{len(baris)} dinilai; ajudikasi {len(adj)} rekaman dalam {len(paket)} paket")


def banding_sampel(md):
    baris = []
    md.append("## 2. Sampel buta Cek 1 (putaran kedua oleh model, bukan manusia)\n")
    md.append("Angka di bawah adalah kesepakatan antara dua putaran model. Angka ini **bukan** "
              "kesepakatan manusia-model yang diminta Cek 1 dan tidak boleh ditulis di `kesepakatan.md`.\n")
    kj = {int(r["idx"]): r for r in baca_csv(VER / ".kunci/kunci_judul.csv")}
    hj = {x["idx"]: x for x in muat_hasil("j")}
    ps = []
    for idx, h in sorted(hj.items()):
        a1 = "X" if kj[idx]["keputusan_ai"].startswith("X") else "L"
        a2 = "X" if h["keputusan"] == "X" else "L"
        kritis = "ya" if a1 == "X" and h["keputusan"] in ("L-C1", "L-C3") else ""
        ps.append((a1, a2))
        baris.append({"tahap": "judul", "idx": idx, "ai1": kj[idx]["keputusan_ai"], "ai2": h["keputusan"],
                      "sama": "ya" if a1 == a2 else "tidak", "kritis": kritis, "catatan_ai2": h.get("catatan", "")})
    po, kp = kappa(ps)
    md.append(f"Tahap judul: n = {len(ps)}; kesepakatan lanjut/eksklusi {fmt(po, True)}; kappa {fmt(kp)}; "
              f"AI-1 eksklusi tetapi AI-2 lanjut: {sum(1 for a, c in ps if a == 'X' and c == 'L')}; "
              f"AI-1 lanjut tetapi AI-2 eksklusi: {sum(1 for a, c in ps if a == 'L' and c == 'X')}; "
              f"kritis (AI-1 eksklusi, AI-2 menandai C1 atau C3): "
              f"**{sum(1 for b in baris if b['tahap'] == 'judul' and b['kritis'])}**.\n")
    ka = {int(r["idx"]): r for r in baca_csv(VER / ".kunci/kunci_abstrak.csv")}
    ha = {x["idx"]: x for x in muat_hasil("a")}
    pf, p8, pb = [], [], []
    for idx, h in sorted(ha.items()):
        a1 = ka[idx]["keputusan_ai"].replace(" ", "-")
        a2 = h["keputusan"]
        g1, g2 = ("X" if a1.startswith("X") else a1), ("X" if a2.startswith("X") else a2)
        kritis = "ya" if g1 == "X" and g2 in ("C1", "C3") else ""
        pf.append((a1, a2))
        p8.append((g1, g2))
        pb.append((g1 == "X", g2 == "X"))
        baris.append({"tahap": "kelayakan", "idx": idx, "ai1": a1, "ai2": a2,
                      "sama": "ya" if a1 == a2 else ("kelompok sama" if g1 == g2 else "tidak"),
                      "kritis": kritis, "catatan_ai2": h.get("catatan", ""),
                      "juga_cocok_ai2": ";".join(h.get("juga_cocok", []))})
    for nama, p in (("kode penuh", pf), ("kode dengan semua X digabung", p8), ("masuk/eksklusi", pb)):
        po, kp = kappa(p)
        md.append(f"Tahap kelayakan, {nama}: n = {len(p)}; kesepakatan {fmt(po, True)}; kappa {fmt(kp)}.")
    md.append(f"\nKritis tahap kelayakan (AI-1 eksklusi, AI-2 C1 atau C3): "
              f"**{sum(1 for b in baris if b['tahap'] == 'kelayakan' and b['kritis'])}**.\n")
    tulis_csv(AI2 / "banding_sampel.csv", ["tahap", "idx", "ai1", "ai2", "sama", "kritis", "juga_cocok_ai2", "catatan_ai2"], baris)
    print(f"sampel: judul {len(hj)}, kelayakan {len(ha)}")


def gabung_fakta(md):
    asal = {}
    for b in sorted(BERKAS.glob("f_*.json")):
        for x in json.loads(b.read_text(encoding="utf-8")):
            asal[x["key"]] = x
    lembar = {r["id"]: r for r in baca_csv(VER / "cek_fakta.csv")}
    baris, vf = [], defaultdict(list)
    for h in muat_hasil("f"):
        for k in h.get("klaim", []):
            l = lembar.get(k["id"], {})
            baris.append({"id": k["id"], "key": h["key"], "bagian": l.get("bagian", ""), "jenis": l.get("jenis", ""),
                          "kalimat": l.get("kalimat", ""), "dasar_bukti": h["dasar_bukti"], "benar_ai2": k["benar"],
                          "halaman": k.get("halaman", ""), "bukti": k.get("bukti", ""),
                          "perbaikan": k.get("perbaikan", ""), "catatan": k.get("catatan", "")})
            if k["benar"] in ("N", "SEBAGIAN"):
                vf[h["key"]].append({"id": k["id"], "bagian": l.get("bagian", ""), "kalimat": l.get("kalimat", ""),
                                     "temuan": {a: k.get(a, "") for a in ("benar", "halaman", "bukti", "perbaikan", "catatan")},
                                     "dasar_bukti_pemeriksa": h["dasar_bukti"]})
    baris.sort(key=lambda r: r["id"])
    tulis_csv(AI2 / "cek_fakta_ai2.csv", ["id", "key", "bagian", "jenis", "kalimat", "dasar_bukti", "benar_ai2",
                                          "halaman", "bukti", "perbaikan", "catatan"], baris)
    c = Counter(b["benar_ai2"] for b in baris)
    md.append("## 3. Cek fakta naskah (Cek 6, oleh model)\n")
    md.append(f"Baris klaim dinilai: {len(baris)} dari {sum(len(x['klaim']) for x in asal.values())}. "
              f"Y {c['Y']}, SEBAGIAN {c['SEBAGIAN']}, N {c['N']}, TAK-TERPERIKSA {c['TAK-TERPERIKSA']}.\n")
    md.append(f"Dasar bukti: {dict(Counter(b['dasar_bukti'] for b in baris))}.\n")
    items = []
    for key, ks in sorted(vf.items()):
        a = asal[key]
        items.append({"key": key, "judul": a["judul"], "tahun": a["tahun"], "doi": a["doi"],
                      "abstrak": a["abstrak"], "teks_lengkap": a["teks_lengkap"], "klaim": ks})
    paket = kemas(items, lambda x: (3 if x["teks_lengkap"] else 1.5) + 0.5 * (len(x["klaim"]) - 1), 12,
                  random.Random(BENIH + 2))
    if not TANPA_PAKET:
        for lama in BERKAS.glob("vf_*.json"):
            lama.unlink()
        for i, p in enumerate(paket):
            tulis_json(BERKAS / f"vf_{i:03d}.json", p)
    print(f"cek fakta: {len(baris)} baris; N/SEBAGIAN {c['N'] + c['SEBAGIAN']} pada {len(items)} kajian, {len(paket)} paket verifikasi")


def main():
    md = ["# Ringkasan Banding Putaran Kedua (AI-2) terhadap Putaran Pertama\n",
          "Berkas ini dibuat `tools/scopus/verifikasi_ai2_gabung.py`; jangan disunting tangan. "
          "Kedua putaran dikerjakan model bahasa besar. Tidak ada angka di sini yang berasal dari peninjau manusia.\n"]
    banding_kelayakan(md)
    banding_sampel(md)
    gabung_fakta(md)
    (AI2 / "RINGKASAN-BANDING.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
