#!/usr/bin/env python3
"""Pemeriksaan ulang eksklusi tahap judul dari dua kueri inti (putaran kedua, AI-2).

Sampel buta Cek 1 (300 judul) memuat satu kajian multi-pengamatan (C1) dan satu
kajian kelapa sawit (C3) yang dikeluarkan putaran pertama dari judul saja. Rencana
verifikasi meminta, bila hal itu terjadi, semua rekaman sejenis diperiksa ulang.
"Sejenis" di sini berarti: dikeluarkan di tahap judul dan diambil oleh kueri
multi-pengamatan (Q1) atau kueri kelapa sawit (Q3).

  python tools/scopus/verifikasi_ai2_judul.py daftar     # ai2/ulang_judul.csv (masukan enrich_records.py)
  python tools/scopus/verifikasi_ai2_judul.py siapkan    # paket ai2/berkas/u_NNN.json (judul + abstrak)
  python tools/scopus/verifikasi_ai2_judul.py sanggah    # paket ai2/berkas/ru_NNN.json dari usul masuk
  python tools/scopus/verifikasi_ai2_judul.py terapkan [--kering]

Abstrak diambil dengan:
  python tools/scopus/enrich_records.py --records literature/scopus-2026-09/verifikasi/ai2/ulang_judul.csv \
      --cache literature/scopus-2026-09/verifikasi/ai2/enrich_ulang_judul.jsonl

`terapkan` memasukkan rekaman yang usul masuknya bertahan terhadap penyanggah:
tahap_judul.csv (X -> I), kandidat_abstrak.csv, enrich.jsonl, penyaringan/abstrak_U00.txt,
mekanisme_C1.txt, kode_C3.txt, dan log_perubahan.csv (oleh = AI-2). Perintah ini idempoten.
"""
import csv
import json
import re
import sys
import unicodedata
from collections import Counter

from verifikasi_ai2 import AI2, BERKAS, HASIL, TOPIK, VER, baca_csv, tulis_json

DAFTAR = AI2 / "ulang_judul.csv"
CACHE = AI2 / "enrich_ulang_judul.jsonl"
KUERI_INTI = {"Q1", "Q3"}
ISI_PAKET = 30
TANGGAL = "2026-10-02"
KATA_TUGAS = {"a", "an", "the", "of", "on", "in", "for", "and", "to", "with", "using", "based", "by", "from", "towards", "toward"}


def muat_cache():
    out = {}
    if CACHE.exists():
        for line in open(CACHE, encoding="utf-8"):
            d = json.loads(line)
            out[d["eid"]] = d
    return out


def sasaran():
    rec = {int(r["idx"]): r for r in baca_csv(TOPIK / "records_all.csv")}
    tj = baca_csv(TOPIK / "penyaringan/tahap_judul.csv")
    # Rekaman yang sudah dimasukkan kembali tetap menjadi sasaran agar paket tidak berubah.
    asal = {int(r["idx"]) for r in baca_csv(DAFTAR)} if DAFTAR.exists() else None
    out = []
    for r in tj:
        i = int(r["idx"])
        if asal is not None:
            if i in asal:
                out.append(rec[i])
        elif r["keputusan_judul"] == "X" and set(rec[i]["qids"].split(";")) & KUERI_INTI:
            out.append(rec[i])
    return out


def daftar():
    rows = sasaran()
    with open(DAFTAR, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["idx", "eid", "doi", "title", "year", "qids"], extrasaction="ignore",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    c = Counter(q for r in rows for q in r["qids"].split(";") if q in KUERI_INTI)
    print(f"{len(rows)} rekaman -> {DAFTAR} ({dict(c)})")


def siapkan():
    rows = sasaran()
    ab = muat_cache()
    for lama in BERKAS.glob("u_*.json"):
        lama.unlink()
    items = []
    for r in sorted(rows, key=lambda r: int(r["idx"])):
        e = ab.get(r["eid"], {})
        items.append({"idx": int(r["idx"]), "judul": r["title"], "tahun": r["year"],
                      "penulis_pertama": r["first_author"], "sumber": r["source"],
                      "tipe_dokumen": r["doc_type"], "doi": r["doi"],
                      "abstrak": e.get("abstract") or "", "sumber_abstrak": e.get("abstract_source") or ""})
    for i in range(0, len(items), ISI_PAKET):
        tulis_json(BERKAS / f"u_{i // ISI_PAKET:03d}.json", items[i:i + ISI_PAKET])
    n = sum(1 for x in items if x["abstrak"])
    print(f"paket u: {len(items)} rekaman dalam {(len(items) + ISI_PAKET - 1) // ISI_PAKET} paket; dengan abstrak {n}")


def muat_hasil(awalan):
    out = {}
    for h in sorted(HASIL.glob(f"{awalan}_[0-9]*.json")):
        for x in json.loads(h.read_text(encoding="utf-8")):
            x["_paket"] = h.name
            out[x["idx"]] = x
    return out


def sanggah():
    """Paket penyanggahan: setiap rekaman yang dinilai layak masuk, bersama abstraknya."""
    asal = {}
    for b in sorted(BERKAS.glob("u_[0-9]*.json")):
        for x in json.loads(b.read_text(encoding="utf-8")):
            asal[x["idx"]] = x
    usul = [dict(asal[i], usul={k: v for k, v in x.items() if not k.startswith("_") and k != "idx"})
            for i, x in sorted(muat_hasil("u").items()) if x["kode"] != "X"]
    for lama in BERKAS.glob("ru_*.json"):
        lama.unlink()
    for i in range(0, len(usul), 12):
        tulis_json(BERKAS / f"ru_{i // 12:03d}.json", usul[i:i + 12])
    print(f"usul masuk: {len(usul)} dari {len(muat_hasil('u'))} dinilai; {dict(Counter(u['usul']['kode'] for u in usul))}; "
          f"{(len(usul) + 11) // 12} paket ru")


def buat_key(r, terpakai):
    nama = unicodedata.normalize("NFD", r["first_author"].rsplit(" ", 1)[0])
    nama = re.sub(r"[^a-z]", "", "".join(c for c in nama if not unicodedata.combining(c)).lower())
    kata = [w for w in re.findall(r"[a-z0-9]+", r["title"].lower()) if w not in KATA_TUGAS]
    dasar = f"{nama}{r['year']}{kata[0] if kata else 'x'}"
    key, akhiran = dasar, "b"
    while key in terpakai:
        key, akhiran = dasar + akhiran, chr(ord(akhiran) + 1)
    terpakai.add(key)
    return key


def terapkan():
    kering = "--kering" in sys.argv
    rec = {int(r["idx"]): r for r in baca_csv(TOPIK / "records_all.csv")}
    hasil = muat_hasil("u")
    ref = {}
    for h in sorted(HASIL.glob("ref_ru_[0-9]*.json")):
        for x in json.loads(h.read_text(encoding="utf-8")):
            ref[x["idx"]] = x
    masuk = {i: x for i, x in hasil.items() if x["kode"] != "X" and ref.get(i, {}).get("bertahan") is True}
    gugur = {i: x for i, x in hasil.items() if x["kode"] != "X" and i not in masuk}
    print(f"dinilai {len(hasil)}; usul masuk {len(masuk) + len(gugur)}; bertahan {len(masuk)} "
          f"{dict(Counter(x['kode'] for x in masuk.values()))}; tidak bertahan atau belum disanggah {len(gugur)}")
    if kering:
        return

    kand_path = TOPIK / "penyaringan/kandidat_abstrak.csv"
    kand = baca_csv(kand_path)
    ada = {int(r["idx"]) for r in kand}
    terpakai = {r["key"] for r in kand}
    baru = []
    for i in sorted(masuk):
        if i in ada:
            continue
        r = rec[i]
        baru.append({"idx": i, "eid": r["eid"], "doi": r["doi"], "title": r["title"], "year": r["year"],
                     "first_author": r["first_author"], "source": r["source"], "doc_type": r["doc_type"],
                     "cited_by": r["cited_by"], "keputusan_judul": "I", "key": buat_key(r, terpakai)})
    if baru:
        with open(kand_path, "a", encoding="utf-8", newline="") as f:
            csv.DictWriter(f, fieldnames=list(kand[0].keys()), lineterminator="\n").writerows(baru)
    key = {int(r["idx"]): r["key"] for r in baca_csv(kand_path)}

    # tahap judul: X -> I
    tj_path = TOPIK / "penyaringan/tahap_judul.csv"
    tj = baca_csv(tj_path)
    for r in tj:
        if int(r["idx"]) in masuk and r["keputusan_judul"] == "X":
            r["keputusan_judul"], r["alasan"] = "I", "dilanjutkan oleh pemeriksaan ulang putaran kedua (AI-2)"
    with open(tj_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(tj[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(tj)

    # abstrak ke enrich.jsonl (hanya yang belum ada)
    ab = muat_cache()
    sudah = {json.loads(l)["eid"] for l in open(TOPIK / "enrich.jsonl", encoding="utf-8")}
    with open(TOPIK / "enrich.jsonl", "a", encoding="utf-8", newline="\n") as f:
        for i in sorted(masuk):
            e = ab.get(rec[i]["eid"])
            if e and e["eid"] not in sudah:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")

    # keputusan tahap kelayakan
    kepala = ("# Rekaman yang dikeluarkan putaran pertama di tahap judul dan dimasukkan kembali oleh pemeriksaan ulang\n"
              "# putaran kedua (AI-2) atas semua eksklusi tahap judul dari kueri Q1 dan Q3. Keputusan dari judul dan abstrak;\n"
              "# setiap usul masuk diuji penyanggah. Dibuat tools/scopus/verifikasi_ai2_judul.py; jangan disunting tangan.\n")
    baris = []
    for i in sorted(masuk):
        x = masuk[i]
        tanda = " (judul)" if x["dasar_bukti"] == "judul" else ""
        baris.append(f"{i} {x['kode']}  {rec[i]['title'][:110]}{tanda}\n")
    (TOPIK / "penyaringan/abstrak_U00.txt").write_text(kepala + "".join(baris), encoding="utf-8", newline="\n")

    # kode C1 dan C3
    def tambah_tab(path, isi):
        teks = path.read_text(encoding="utf-8")
        punya = {int(l.split("\t")[0]) for l in teks.splitlines() if l and not l.startswith("#")}
        tambahan = "".join("\t".join([str(i)] + v) + "\n" for i, v in sorted(isi.items()) if i not in punya)
        if tambahan:
            path.write_text(teks + ("" if teks.endswith("\n") else "\n") + tambahan, encoding="utf-8", newline="\n")
        return [i for i in isi if i not in punya]

    def bersih(v):
        return re.sub(r"\s+", " ", str(v or "")).strip()

    c1, c3 = {}, {}
    for i, x in masuk.items():
        if x["kode"] == "C1" and isinstance(x.get("c1"), dict):
            k = x["c1"]
            sumber = "teks lengkap" if x["dasar_bukti"].startswith("teks") else ("abstrak" if x["dasar_bukti"].startswith("abstrak") else "judul")
            c1[i] = [k["mekanisme"], k["akuisisi"], k["per_kelas"], bersih(k["hasil_ringkas"]), sumber, bersih(k.get("halaman")),
                     bersih(k.get("referensi_hitung")), bersih(k.get("tingkat_metrik")),
                     bersih(k.get("cara_kelas")) if k["per_kelas"] == "Y" else "", "tidak"]
        if x["kode"] == "C3" and isinstance(x.get("c3"), dict):
            k = x["c3"]
            c3[i] = [k["tugas"], k["lokasi"], k["modalitas"].upper().replace(" ", ""), k["multipandang"], k["per_kelas"]]
    c1_baru = tambah_tab(TOPIK / "bukti/mekanisme_C1.txt", c1)
    c3_baru = tambah_tab(TOPIK / "bukti/kode_C3.txt", c3)

    # log
    log_path = VER / "log_perubahan.csv"
    sudah_log = {(r["berkas"], str(r["idx_atau_key"]), r["kolom"]) for r in baca_csv(log_path)}
    with open(log_path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        for i in sorted(masuk):
            x, r = masuk[i], ref[i]
            for berkas, kolom, lama, nilai in [
                ("topik/penyaringan/tahap_judul.csv", "keputusan_judul", "X", "I"),
                ("topik/penyaringan/abstrak_U00.txt", "kode", "", x["kode"]),
            ]:
                if (berkas, str(i), kolom) not in sudah_log:
                    w.writerow([TANGGAL, berkas, i, kolom, lama, nilai,
                                bersih(f"pemeriksaan ulang eksklusi tahap judul (Q1, Q3); dasar: {x['dasar_bukti']}; "
                                       f"{x.get('catatan', '')} Penyanggah: {r.get('alasan', '')}"), "AI-2"])

    # laporan
    md = ["# Pemeriksaan Ulang Eksklusi Tahap Judul dari Kueri Q1 dan Q3 (AI-2)\n",
          "Dibuat `tools/scopus/verifikasi_ai2_judul.py`; jangan disunting tangan. Semua keputusan dibuat model bahasa "
          "besar dan **belum diperiksa manusia**.\n",
          f"- Rekaman yang diperiksa ulang: {len(hasil)} (dikeluarkan putaran pertama dari judul saja; kueri Q1 atau Q3).",
          f"- Dasar bukti: {dict(Counter(x['dasar_bukti'] for x in hasil.values()))}.",
          f"- Tetap dikeluarkan: {sum(1 for x in hasil.values() if x['kode'] == 'X')} "
          f"({dict(Counter(x.get('alasan', '') for x in hasil.values() if x['kode'] == 'X'))}).",
          f"- Diusulkan masuk: {len(masuk) + len(gugur)}; bertahan terhadap penyanggah dan dimasukkan: **{len(masuk)}** "
          f"({dict(Counter(x['kode'] for x in masuk.values()))}); tidak bertahan: {len(gugur)}.\n",
          "## Dimasukkan ke korpus\n", "| idx | key | kode | dasar | judul |", "|---|---|---|---|---|"]
    for i in sorted(masuk, key=lambda i: (masuk[i]["kode"], i)):
        md.append(f"| {i} | `{key.get(i, '')}` | {masuk[i]['kode']} | {masuk[i]['dasar_bukti']} | {rec[i]['title'][:120]} |")
    md += ["\n## Diusulkan masuk tetapi tidak bertahan (tetap dikeluarkan)\n", "| idx | usul | alasan penyanggah | judul |", "|---|---|---|---|"]
    for i in sorted(gugur):
        md.append(f"| {i} | {gugur[i]['kode']} | {bersih(ref.get(i, {}).get('alasan', 'belum disanggah')).replace('|', '/')} | {rec[i]['title'][:100]} |")
    (AI2 / "ULANG-JUDUL.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    print(f"dimasukkan {len(masuk)} (kandidat baru {len(baru)}; baris C1 baru {len(c1_baru)}; baris C3 baru {len(c3_baru)})")


if __name__ == "__main__":
    perintah = sys.argv[1] if len(sys.argv) > 1 else ""
    {"daftar": daftar, "siapkan": siapkan, "sanggah": sanggah, "terapkan": terapkan}.get(perintah, lambda: sys.exit(__doc__))()
