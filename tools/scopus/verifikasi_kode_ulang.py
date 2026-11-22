#!/usr/bin/env python3
"""Cek 5: tulis verifikasi/cek-5-kode-ulang/kode_ulang_C1.csv dari
topik/bukti/mekanisme_C1.txt dan matriks_bukti.csv.

Label C1 diubah langsung di mekanisme_C1.txt dan setiap perubahan dicatat di
verifikasi/.teknis/log_perubahan.csv (lihat verifikasi_log_manusia.py).

  python3 tools/scopus/verifikasi_kode_ulang.py
"""
import csv
import re
import sys
from pathlib import Path

from verifikasi_istilah import AKU, MEK, MET, REF, YN, arti, kode

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature/scopus-2026-09"
MAT = KORPUS / "topik/bukti/matriks_bukti.csv"
MANUAL = KORPUS / "topik/bukti/mekanisme_C1.txt"
CEK5 = KORPUS / "verifikasi/cek-5-kode-ulang"
LEMBAR = CEK5 / "kode_ulang_C1.csv"
LOG = KORPUS / "verifikasi/.teknis/log_perubahan.csv"
CEK5_DISETUJUI = "2026-10-19"

KOLOM_MANUAL = ["mekanisme", "akuisisi", "per_kelas", "hasil_ringkas", "sumber_kode", "halaman",
                "referensi_hitung", "tingkat_metrik", "cara_kelas", "berubah"]
NAMA_KOLOM = {"mekanisme": "cara penghubungan", "akuisisi": "cara foto diambil", "per_kelas": "per kelas"}
KELAS = {"-": "tidak berlaku", "saat pelacakan": "kelas ditetapkan saat pelacakan",
         "sesudah pelacakan": "kelas ditetapkan sesudah pelacakan",
         "voting antarpandang": "kelas digabung antarbingkai dengan suara atau rata-rata",
         "tidak dinyatakan": "tidak dinyatakan"}


def baca(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def muat_manual():
    kode_c1 = {}
    for line in MANUAL.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        p = line.split("\t")
        p += [""] * (11 - len(p))
        kode_c1[p[0]] = dict(zip(KOLOM_MANUAL, p[1:11]))
    return kode_c1


def jamak(v, peta):
    return "; ".join(peta.get(p.strip(), p.strip()) for p in v.split(";") if p.strip())


def perubahan(v):
    """'ya (lama: mekanisme=M3; per_kelas=N)' -> 'ya; sebelumnya cara penghubungan = M3 (pelacakan video); ...'."""
    m = re.match(r"ya \(lama: (.*)\)$", v.strip())
    if not m:
        return {"tidak": "tidak", "": ""}.get(v.strip(), v)
    bag = []
    for b in m.group(1).split(";"):
        k, _, x = b.strip().partition("=")
        peta = {"mekanisme": MEK, "akuisisi": AKU, "per_kelas": YN}.get(k)
        bag.append(f"{NAMA_KOLOM.get(k, k)} = {arti(x, peta) if peta else x}")
    return "ya; sebelumnya " + "; ".join(bag)


PROSES = re.compile(r"isian model|pembaca buta|diserahkan peninjau|^Diisi \d+ Oktober|Kode ulang (Sonnet|Haiku|Opus)|"
                    r"Hasil ringkas tidak diubah|Belum dibaca peninjau|kode tidak berubah|^$")


def bersih(c):
    """Buang keterangan proses (pembaca model, tanggal isian); sisakan isi catatan."""
    bag = [b.strip() for b in re.split(r";\s+|\.\s+(?=[A-Z])|\.;\s*", c)]
    bag = [re.sub(r"^label buta dikoreksi agen utama setelah membaca teks lengkap: ",
                  "dikoreksi setelah membaca teks lengkap: ", b) for b in bag if not PROSES.search(b)]
    teks = "; ".join(re.sub(r"\s*\((agen utama|diperiksa agen utama)[^)]*\)", "", b) for b in bag).strip(" ;.")
    teks = re.sub(r"\s*\(\d+ Oktober 2026\)", "", teks).replace("dibaca agen utama", "dibaca")
    teks = teks.replace("cara_kelas", "cara kelas")
    return re.sub(r"\b(M[0-5])\b(?! \()", lambda m: f"{m.group(1)} ({MEK[m.group(1)]})", teks)


def isian_sesudah_cek5():
    """idx -> isi diisi_oleh untuk baris mekanisme_C1.txt yang disunting sesudah Cek 5 disetujui.

    Baris yang ditambahkan sesudah persetujuan belum diperiksa peninjau. Suntingan
    yang dicatat dengan pengubah berawalan "AI, " memakai keterangan itu.
    """
    isian = {}
    for r in baca(LOG):
        if r["berkas"] != "topik/bukti/mekanisme_C1.txt" or r["tanggal"] <= CEK5_DISETUJUI:
            continue
        idx = r["idx_atau_key"].split()[0]
        if r["oleh"].startswith("AI, disetujui peninjau"):
            isian[idx] = f"AI dari teks lengkap, {r['oleh'][4:]}"
        elif r["kolom"] == "baris":
            isian[idx] = "AI dari teks lengkap, belum diperiksa peninjau"
        elif r["oleh"].startswith("AI, "):
            isian[idx] = f"AI dari teks lengkap, {r['oleh'][4:]} ({r['tanggal']})"
    return isian


def bangun_lembar():
    lama = {r["idx"]: r for r in baca(LEMBAR)} if LEMBAR.exists() else {}
    sesudah = isian_sesudah_cek5()
    manual = muat_manual()
    mat = {r["idx"]: r for r in baca(MAT) if r["kode"] == "C1"}
    baris = []
    for idx in sorted(set(manual) & set(mat), key=lambda i: (not i.isdigit(), int(i.lstrip("L")))):
        k, r, l = manual[idx], mat.get(idx, {}), lama.get(idx, {})
        baris.append({
            "idx": idx, "key": r.get("key", ""), "tahun": r.get("year", ""), "judul": r.get("title", ""),
            "dibaca_dari": k["sumber_kode"],
            "cara_penghubungan": arti(k["mekanisme"], MEK),
            "cara_foto_diambil": arti(k["akuisisi"], AKU),
            "hitung_per_kelas_kematangan": YN.get(k["per_kelas"], k["per_kelas"]),
            "cara_kelas": KELAS.get(k["cara_kelas"], k["cara_kelas"]),
            "acuan_hitungan": jamak(k["referensi_hitung"], REF),
            "metrik_evaluasi": jamak(k["tingkat_metrik"], MET),
            "hasil_ringkas": k["hasil_ringkas"],
            "halaman_bukti": k["halaman"],
            "bukti": l.get("bukti", l.get("draf_ai_bukti", "")),
            "berubah_saat_cek_5": perubahan(k["berubah"]),
            "diisi_oleh": (sesudah[idx] if idx in sesudah
                           else "AI dari teks lengkap, disetujui peninjau 19 Oktober 2026" if l
                           else "AI dari teks lengkap, belum diperiksa peninjau"),
            "catatan": bersih(l.get("catatan", l.get("catatan_peninjau", ""))),
        })
    for n, b in enumerate(baris, 1):
        b["no"] = n
    kolom = ["no"] + [c for c in baris[0] if c != "no"]
    with open(LEMBAR, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=kolom)
        w.writeheader()
        w.writerows(baris)
    print(f"{len(baris)} kajian C1 -> {LEMBAR.relative_to(ROOT)}")


def main():
    bangun_lembar()


if __name__ == "__main__":
    main()
