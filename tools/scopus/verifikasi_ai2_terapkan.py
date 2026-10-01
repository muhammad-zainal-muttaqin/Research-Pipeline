#!/usr/bin/env python3
"""Menerapkan keputusan putaran kedua (AI-2) yang sudah diajudikasi ke berkas sumber.

  python tools/scopus/verifikasi_ai2_terapkan.py --kering   # tampilkan ringkasan, tidak menulis
  python tools/scopus/verifikasi_ai2_terapkan.py            # tulis berkas sumber + log + laporan

Aturan penerapan:
  1. Rekaman tanpa perbedaan antarputaran: keputusan putaran pertama tetap. Untuk C1, enam kolom
     verifikasi (sumber_kode, halaman, referensi_hitung, tingkat_metrik, cara_kelas, berubah)
     diisi dari putaran kedua.
  2. Rekaman yang berbeda: nilai final diambil dari ajudikator (paket adj). Bila ajudikator
     menandai `perlu_manusia`, nilai putaran pertama dipertahankan.
  3. Perubahan KELOMPOK (masuk/keluar korpus, atau pindah kelompok) hanya diterapkan bila
     pemeriksa penyanggah (paket ref) menyatakan perubahan itu bertahan. Selain itu rekaman
     dicatat sebagai sengketa dan nilai putaran pertama dipertahankan.
  4. Setiap sel yang berubah dicatat di verifikasi/log_perubahan.csv dengan `oleh = AI-2`
     (model bahasa besar, putaran kedua; belum diperiksa manusia).

Berkas yang ditulis: topik/penyaringan/abstrak_*.txt, topik/bukti/mekanisme_C1.txt,
topik/bukti/kode_C3.txt, verifikasi/log_perubahan.csv, verifikasi/ai2/PERUBAHAN-AI2.md,
verifikasi/ai2/keputusan_final.csv. Skrip idempoten: menjalankannya dua kali tidak menulis
perubahan untuk kedua kalinya.
"""
import csv
import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

import shutil

from verifikasi_ai2 import AI2, BERKAS, HASIL, KODE, KORPUS, SNAP, TOPIK, VER, baca_csv, muat_keputusan
from verifikasi_ai2_gabung import himp_mek, himp_mod, muat_tab

TANGGAL = "2026-10-01"
OLEH = "AI-2"
LOG = VER / "log_perubahan.csv"
KOLOM_LOG = ["tanggal", "berkas", "idx_atau_key", "kolom", "nilai_lama", "nilai_baru", "alasan", "oleh"]
KUAT = ("teks lengkap", "teks lengkap (web)")


def muat(awalan):
    out = {}
    for h in sorted(HASIL.glob(f"{awalan}_[0-9]*.json")):
        for x in json.loads(h.read_text(encoding="utf-8")):
            out[x["idx"]] = x
    return out


def sumber_kode(dasar):
    return "teks lengkap" if dasar.startswith("teks lengkap") else ("abstrak" if dasar.startswith("abstrak") else "judul")


def bersih(v):
    return re.sub(r"\s+", " ", str(v or "")).strip()


def main():
    kering = "--kering" in sys.argv
    if not SNAP.exists():  # salinan putaran pertama, sekali saja, sebelum penerapan pertama
        SNAP.mkdir(parents=True)
        for fn in sorted(glob.glob(str(TOPIK / "penyaringan/abstrak_*.txt"))):
            shutil.copy2(fn, SNAP / Path(fn).name)
        shutil.copy2(TOPIK / "bukti/mekanisme_C1.txt", SNAP / "mekanisme_C1.txt")
        shutil.copy2(TOPIK / "bukti/kode_C3.txt", SNAP / "kode_C3.txt")
    dec = muat_keputusan(SNAP)
    c1_lama = muat_tab(SNAP / "mekanisme_C1.txt")
    c3_lama = muat_tab(SNAP / "kode_C3.txt")
    kand = {int(r["idx"]): r for r in baca_csv(TOPIK / "penyaringan/kandidat_abstrak.csv")}
    s = muat("s")
    adj = muat("adj")
    ref = {}
    for h in sorted(HASIL.glob("ref_adj_*.json")):
        for x in json.loads(h.read_text(encoding="utf-8")):
            ref[x["idx"]] = x
    tambahan = []
    p_tambah = HASIL / "tambahan.json"
    if p_tambah.exists():
        tambahan = json.loads(p_tambah.read_text(encoding="utf-8"))
    for t in tambahan:  # rekaman di luar 510 (mis. Häni 2020): diperlakukan seperti hasil ajudikasi
        adj[t["idx"]] = t
        s.setdefault(t["idx"], t)
        if "ref" in t:
            ref[t["idx"]] = t["ref"]

    log, final, laporan = [], [], {"grup": [], "sengketa": [], "manusia": [], "alasan": [], "c1": [], "c3": []}

    def catat(berkas, idx, kolom, lama, baru, alasan):
        if bersih(lama) != bersih(baru):
            log.append({"tanggal": TANGGAL, "berkas": berkas, "idx_atau_key": idx, "kolom": kolom,
                        "nilai_lama": bersih(lama), "nilai_baru": bersih(baru), "alasan": bersih(alasan), "oleh": OLEH})

    c1_baru, c3_baru, kode_baru = {}, {}, {}
    for idx in sorted(s):
        d = dec[idx]
        h, a, r = s[idx], adj.get(idx), ref.get(idx)
        key = kand[idx]["key"]
        sumber = a if (a and not a.get("perlu_manusia")) else h
        kode, alasan = d["kode"], d["alasan"]
        status = "tetap"
        dasar_alasan = bersih((a or {}).get("alasan_ajudikasi") or h.get("catatan") or "")
        bukti = " || ".join((a or h).get("bukti", [])[:2])
        if a and a.get("perlu_manusia"):
            status = "perlu manusia"
            laporan["manusia"].append((idx, key, d, a, bukti))
        elif a and a["kode"] != d["kode"]:
            if d["kode"] in a.get("juga_cocok", []):
                status = "tetap (kode lama juga cocok)"
            elif r and r.get("bertahan") is True:
                kode, alasan, status = a["kode"], a.get("alasan", ""), "kelompok berubah"
                laporan["grup"].append((idx, key, d, a, r, bukti))
            else:
                status = "sengketa"
                laporan["sengketa"].append((idx, key, d, a, r, bukti))
        elif a and d["kode"] == "X" and a.get("alasan", "") != d["alasan"]:
            alasan, status = a.get("alasan", ""), "alasan berubah"
            laporan["alasan"].append((idx, key, d, a, bukti))
        if (kode, alasan) != (d["kode"], d["alasan"]):
            kode_baru[idx] = (kode, alasan)
            berkas = f"topik/penyaringan/{d['berkas']}"
            catat(berkas, idx, "kode", d["kode"], kode, dasar_alasan)
            if d["alasan"] != alasan:
                catat(berkas, idx, "alasan", d["alasan"], alasan, dasar_alasan)
        if d["dasar"] == "judul" and not sumber["dasar_bukti"].startswith("judul") and idx in dec:
            catat(f"topik/penyaringan/{d['berkas']}", idx, "dasar_keputusan", "judul",
                  sumber["dasar_bukti"], "putaran kedua menemukan abstrak atau teks; baris tidak dipindah")

        # ---- kode C1
        if kode == "C1":
            lama = (c1_lama.get(idx) or []) + [""] * 10
            k = sumber.get("c1") if isinstance(sumber.get("c1"), dict) else (h.get("c1") if isinstance(h.get("c1"), dict) else None)
            baru = lama[:4]
            ubah = []
            if k:
                if idx not in c1_lama or (a and not a.get("perlu_manusia")):
                    if himp_mek(lama[0]) != himp_mek(k["mekanisme"]):
                        baru[0] = k["mekanisme"]
                    if lama[1] != k["akuisisi"]:
                        baru[1] = k["akuisisi"]
                    if lama[2] != k["per_kelas"]:
                        baru[2] = k["per_kelas"]
                if idx not in c1_lama or sumber["dasar_bukti"] in KUAT or \
                        (d["dasar"] == "judul" and sumber["dasar_bukti"].startswith("abstrak")):
                    baru[3] = bersih(k["hasil_ringkas"])
                for i, nama in enumerate(["mekanisme", "akuisisi", "per_kelas"]):
                    if idx in c1_lama and bersih(lama[i]) != bersih(baru[i]):
                        ubah.append(f"{nama}={lama[i]}")
                ver = [sumber_kode(sumber["dasar_bukti"]), bersih(k.get("halaman", "")),
                       bersih(k.get("referensi_hitung", "")), bersih(k.get("tingkat_metrik", "")),
                       bersih(k.get("cara_kelas", "")) if baru[2] == "Y" else "",
                       f"ya (lama: {'; '.join(ubah)})" if ubah else "tidak"]
            else:
                ver = lama[4:10]
            c1_baru[idx] = baru + ver
            for i, nama in enumerate(["mekanisme", "akuisisi", "per_kelas", "hasil_ringkas", "sumber_kode", "halaman",
                                      "referensi_hitung", "tingkat_metrik", "cara_kelas", "berubah"]):
                catat("topik/bukti/mekanisme_C1.txt", idx, nama, lama[i] if idx in c1_lama else "", c1_baru[idx][i],
                      dasar_alasan if i < 3 else "putaran kedua (AI-2)")
            if ubah:
                laporan["c1"].append((idx, key, lama[:3], baru[:3], sumber["dasar_bukti"], dasar_alasan, bukti))
        elif idx in c1_lama:
            for i, nama in enumerate(["mekanisme", "akuisisi", "per_kelas", "hasil_ringkas"]):
                catat("topik/bukti/mekanisme_C1.txt", idx, nama, c1_lama[idx][i] if i < len(c1_lama[idx]) else "", "",
                      f"baris dihapus: rekaman keluar dari C1 ({dasar_alasan})")

        # ---- kode C3
        if kode == "C3":
            lama = (c3_lama.get(idx) or []) + [""] * 5
            k = sumber.get("c3") if isinstance(sumber.get("c3"), dict) else None
            baru = lama[:5]
            if k and (idx not in c3_lama or (a and not a.get("perlu_manusia"))):
                kand_baru = [k["tugas"], k["lokasi"], k["modalitas"].upper().replace(" ", ""), k["multipandang"], k["per_kelas"]]
                for i in range(5):
                    if i == 2:
                        if himp_mod(lama[2]) != himp_mod(kand_baru[2]):
                            baru[2] = kand_baru[2]
                    elif lama[i] != kand_baru[i]:
                        baru[i] = kand_baru[i]
            c3_baru[idx] = baru
            ubah = []
            for i, nama in enumerate(["tugas", "lokasi", "modalitas", "multipandang", "per_kelas"]):
                catat("topik/bukti/kode_C3.txt", idx, nama, lama[i] if idx in c3_lama else "", baru[i], dasar_alasan)
                if idx in c3_lama and lama[i] != baru[i]:
                    ubah.append(f"{nama}: {lama[i]} -> {baru[i]}")
            if ubah:
                laporan["c3"].append((idx, key, ubah, sumber["dasar_bukti"], dasar_alasan, bukti))
        elif idx in c3_lama:
            for i, nama in enumerate(["tugas", "lokasi", "modalitas", "multipandang", "per_kelas"]):
                catat("topik/bukti/kode_C3.txt", idx, nama, c3_lama[idx][i] if i < len(c3_lama[idx]) else "", "",
                      f"baris dihapus: rekaman keluar dari C3 ({dasar_alasan})")

        final.append({"idx": idx, "key": key, "kode_putaran_1": d["kode"] + (" " + d["alasan"] if d["alasan"] else ""),
                      "kode_putaran_2": h["kode"] + (" " + h.get("alasan", "") if h.get("alasan") else ""),
                      "kode_ajudikasi": (a["kode"] + (" " + a.get("alasan", "") if a.get("alasan") else "")) if a else "",
                      "penyanggah": ("bertahan" if r.get("bertahan") else "disanggah") if r else "",
                      "kode_final": kode + (" " + alasan if alasan else ""), "status": status,
                      "dasar_bukti": sumber["dasar_bukti"], "alasan": dasar_alasan, "bukti": bukti})

    # Baris yang sudah ada di log (dari eksekusi sebelumnya) tidak dicatat dua kali.
    if LOG.exists() and LOG.stat().st_size > 0:
        sudah = {(r["berkas"], str(r["idx_atau_key"]), r["kolom"], r["nilai_lama"], r["nilai_baru"])
                 for r in baca_csv(LOG)}
        log = [l for l in log if (l["berkas"], str(l["idx_atau_key"]), l["kolom"], l["nilai_lama"], l["nilai_baru"]) not in sudah]

    hit = Counter(f["status"] for f in final)
    print("status:", dict(hit))
    print("baris log baru:", len(log), "| per kolom:", dict(Counter(l["kolom"] for l in log)))
    print("C1 final:", len(c1_baru), "(lama", len(c1_lama), ") | C3 final:", len(c3_baru), "(lama", len(c3_lama), ")")
    if kering:
        return

    # ---- tulis berkas sumber
    for fn in sorted(glob.glob(str(SNAP / "abstrak_*.txt"))):
        baris = []
        tujuan = TOPIK / "penyaringan" / Path(fn).name
        for line in open(fn, encoding="utf-8"):
            m = KODE.match(line.rstrip("\n").strip())
            if m and int(m.group(1)) in kode_baru:
                kode, alasan = kode_baru[int(m.group(1))]
                ekor = m.group(4) or ""
                line = f"{m.group(1)} {kode}{' ' + alasan if alasan else ''}{ekor}\n"
            baris.append(line)
        if tujuan.read_text(encoding="utf-8") != "".join(baris):
            tujuan.write_text("".join(baris), encoding="utf-8", newline="\n")

    def tulis_tab(path, lama, baru):
        kepala = [l for l in open(path, encoding="utf-8") if l.startswith("#") or not l.strip()]
        urut = [i for i in lama if i in baru] + sorted(i for i in baru if i not in lama)
        isi = []
        for i in urut:
            v = [bersih(x) for x in baru[i]]
            while len(v) > (4 if "mekanisme" in path.name else 5) and not v[-1]:
                v.pop()
            isi.append("\t".join([str(i)] + v) + "\n")
        path.write_text("".join(kepala + isi), encoding="utf-8", newline="\n")

    # rekaman C1/C3 di luar cakupan putaran kedua tidak disentuh
    for i, v in c1_lama.items():
        if i not in s:
            c1_baru[i] = v
    for i, v in c3_lama.items():
        if i not in s:
            c3_baru[i] = v
    tulis_tab(TOPIK / "bukti/mekanisme_C1.txt", c1_lama, c1_baru)
    tulis_tab(TOPIK / "bukti/kode_C3.txt", c3_lama, c3_baru)

    ada = LOG.exists() and LOG.stat().st_size > 0
    with open(LOG, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLOM_LOG)
        if not ada:
            w.writeheader()
        w.writerows(log)

    with open(AI2 / "keputusan_final.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(final[0].keys()))
        w.writeheader()
        w.writerows(final)

    md = ["# Perubahan dari Putaran Kedua (AI-2)\n",
          f"Dibuat `tools/scopus/verifikasi_ai2_terapkan.py` pada {TANGGAL}. Semua keputusan di bawah dibuat model "
          "bahasa besar (putaran kedua buta, lalu ajudikasi, lalu penyanggahan untuk perubahan kelompok). "
          "**Belum ada yang diperiksa manusia.** Setiap sel yang berubah tercatat di `../log_perubahan.csv` "
          "dengan `oleh = AI-2`.\n",
          f"Ringkasan status 510 rekaman (+ tambahan): {dict(hit)}.\n"]

    def kd(d):
        return d["kode"] + (" " + d.get("alasan", "") if d.get("alasan") else "")

    md.append(f"## A. Kelompok berubah dan diterapkan ({len(laporan['grup'])})\n")
    for idx, key, d, a, r, bukti in laporan["grup"]:
        md.append(f"- **{idx} `{key}`**: {kd(d)} -> **{kd(a)}** (dasar: {a['dasar_bukti']}). "
                  f"{bersih(a.get('alasan_ajudikasi'))} Penyanggah: {bersih(r.get('alasan'))} Bukti: {bukti}")
    md.append(f"\n## B. Usul perubahan kelompok yang TIDAK diterapkan: sengketa ({len(laporan['sengketa'])})\n")
    for idx, key, d, a, r, bukti in laporan["sengketa"]:
        md.append(f"- **{idx} `{key}`**: putaran 1 {kd(d)}; ajudikator mengusulkan {kd(a)} (dasar: {a['dasar_bukti']}). "
                  f"{bersih(a.get('alasan_ajudikasi'))} Penyanggah: {bersih((r or {}).get('alasan', 'tidak ada hasil'))}")
    md.append(f"\n## C. Diserahkan kepada manusia oleh ajudikator ({len(laporan['manusia'])})\n")
    for idx, key, d, a, bukti in laporan["manusia"]:
        md.append(f"- **{idx} `{key}`**: putaran 1 {kd(d)}; putaran 2 {kd(s[idx])}. {bersih(a.get('alasan_ajudikasi'))}")
    md.append(f"\n## D. Alasan eksklusi berubah ({len(laporan['alasan'])})\n")
    for idx, key, d, a, bukti in laporan["alasan"]:
        md.append(f"- **{idx} `{key}`**: {kd(d)} -> {kd(a)}. {bersih(a.get('alasan_ajudikasi'))}")
    md.append(f"\n## E. Kode C1 berubah ({len(laporan['c1'])})\n")
    md.append("| idx | key | mekanisme | akuisisi | per kelas | dasar | alasan |")
    md.append("|---|---|---|---|---|---|---|")
    for idx, key, lama, baru, dasar, alasan, bukti in laporan["c1"]:
        sel = [f"{l} -> **{b}**" if bersih(l) != bersih(b) else l for l, b in zip(lama, baru)]
        md.append(f"| {idx} | `{key}` | {sel[0]} | {sel[1]} | {sel[2]} | {dasar} | {alasan.replace('|', '/')} |")
    md.append(f"\n## F. Kode C3 berubah ({len(laporan['c3'])})\n")
    md.append("| idx | key | perubahan | dasar | alasan |")
    md.append("|---|---|---|---|---|")
    for idx, key, ubah, dasar, alasan, bukti in laporan["c3"]:
        md.append(f"| {idx} | `{key}` | {'; '.join(ubah)} | {dasar} | {alasan.replace('|', '/')} |")
    (AI2 / "PERUBAHAN-AI2.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    print("ditulis: berkas sumber, log, keputusan_final.csv, PERUBAHAN-AI2.md")


if __name__ == "__main__":
    main()
