#!/usr/bin/env python3
"""Putaran kedua penyaringan dan pengodean oleh model (AI-2), terpisah dari isian manusia.

Rencana verifikasi (literature/scopus-2026-09/verifikasi/rencana/index.html)
meminta pemeriksaan manusia. Skrip ini menyiapkan dan menggabungkan pemeriksaan
putaran kedua yang dikerjakan model bahasa besar atas permintaan penulis pertama
(1 Oktober 2026), supaya penulis kemudian memeriksa hasilnya. Hasil AI-2 TIDAK
PERNAH ditulis ke kolom manusia (`keputusan_manusia`, `konfirmasi_*`, `final_*`,
`benar`, `oleh`) di lembar Cek 1-6; semuanya disimpan di verifikasi/hasil-kerja-ai/.

  python tools/scopus/verifikasi_ai2.py siapkan     # paket rekaman buta di ai2/berkas/
  python tools/scopus/verifikasi_ai2.py periksa s_000.json   # validasi satu berkas hasil
  python tools/scopus/verifikasi_ai2.py status      # paket mana yang hasilnya sudah ada dan sah

Paket:
  s_NNN.json   rekaman tahap kelayakan yang oleh putaran pertama diberi kode C1, C3,
               atau X, dicampur dan TANPA keputusan putaran pertama (buta)
  j_NN.json    sampel buta tahap judul (Cek 1), tanpa keputusan putaran pertama
  a_NN.json    sampel buta tahap kelayakan (Cek 1), tanpa keputusan putaran pertama
  f_NNN.json   klaim naskah per kajian yang dikutip (Cek 6)
"""
import csv
import glob
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KORPUS = ROOT / "literature/scopus-2026-09"
TOPIK = KORPUS / "topik"
VER = KORPUS / "verifikasi"
AI2 = VER / "hasil-kerja-ai"
BERKAS = AI2 / "berkas"
HASIL = AI2 / "hasil"
BENIH = 20261001
# Salinan keputusan dan kode putaran pertama, dibuat sebelum hasil putaran kedua diterapkan.
# Banding dan penerapan selalu membaca putaran pertama dari sini, sehingga keduanya dapat
# dijalankan ulang setiap kali ada paket hasil baru tanpa kehilangan nilai awal.
SNAP = AI2 / "putaran_1"
KODE = re.compile(r"^(\d+)\s+(C[1-5]|T|R|M|X)(?:\s+(E\d))?(.*)$")


def baca_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def muat_keputusan(folder=None):
    """Keputusan tahap kelayakan. `folder` = salinan putaran pertama (SNAP) atau berkas aktif."""
    dec = {}
    for fn in sorted(glob.glob(str((folder or TOPIK / "penyaringan") / "abstrak_*.txt"))):
        nama = Path(fn).name
        for line in open(fn, encoding="utf-8"):
            m = KODE.match(line.strip())
            if m:
                dasar = "judul" if ("T00" in nama or "(judul)" in line) else "abstrak"
                dec[int(m.group(1))] = {"kode": m.group(2), "alasan": m.group(3) or "",
                                        "dasar": dasar, "berkas": nama}
    return dec


def muat_abstrak():
    ab = {}
    for line in open(TOPIK / "enrich.jsonl", encoding="utf-8"):
        d = json.loads(line)
        ab[d["eid"]] = d
    return ab


def tulis_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def kemas(items, bobot, kapasitas, rng):
    items = list(items)
    rng.shuffle(items)
    paket, kini, isi = [], [], 0
    for it in items:
        b = bobot(it)
        if kini and isi + b > kapasitas:
            paket.append(kini)
            kini, isi = [], 0
        kini.append(it)
        isi += b
    if kini:
        paket.append(kini)
    return paket


def siapkan():
    rng = random.Random(BENIH)
    rec = {int(r["idx"]): r for r in baca_csv(TOPIK / "records_all.csv")}
    kand = {int(r["idx"]): r for r in baca_csv(TOPIK / "penyaringan/kandidat_abstrak.csv")}
    dec = muat_keputusan()
    ab = muat_abstrak()
    for lama in BERKAS.glob("*.json"):
        lama.unlink()

    # --- paket s: C1, C3, X dari tahap kelayakan, buta
    rekaman = []
    for idx, d in sorted(dec.items()):
        if d["kode"] not in ("C1", "C3", "X"):
            continue
        r, k = rec[idx], kand[idx]
        key = k["key"]
        e = ab.get(r["eid"], {})
        teks = KORPUS / "teks" / f"{key}.txt"
        rekaman.append({
            "idx": idx, "key": key, "judul": r["title"], "tahun": r["year"],
            "penulis_pertama": r["first_author"], "sumber": r["source"],
            "tipe_dokumen": r["doc_type"], "doi": r["doi"],
            "abstrak": e.get("abstract") or "",
            "sumber_abstrak": e.get("abstract_source") or "",
            "teks_lengkap": f"literature/scopus-2026-09/teks/{key}.txt" if teks.exists() else "",
            "pdf": f"literature/scopus-2026-09/pdf/{key}.pdf" if teks.exists() else "",
        })

    def bobot(x):
        return 3 if x["teks_lengkap"] else (1 if x["abstrak"] else 2)

    paket = kemas(rekaman, bobot, 12, rng)
    for i, p in enumerate(paket):
        tulis_json(BERKAS / f"s_{i:03d}.json", p)
    c = Counter("teks" if x["teks_lengkap"] else ("abstrak" if x["abstrak"] else "judul") for x in rekaman)
    print(f"paket s: {len(rekaman)} rekaman dalam {len(paket)} paket; dasar bukti {dict(c)}")

    # --- paket j dan a: sampel buta Cek 1
    sj = baca_csv(VER / "cek-1-sampel-buta" / "sampel_judul.csv")
    for i in range(0, len(sj), 50):
        tulis_json(BERKAS / f"j_{i // 50:02d}.json",
                   [{"idx": int(r["idx"]), "judul": r["judul"], "tahun": r["tahun"], "sumber": r["sumber"]}
                    for r in sj[i:i + 50]])
    sa = baca_csv(VER / "cek-1-sampel-buta" / "sampel_abstrak.csv")
    for i in range(0, len(sa), 20):
        tulis_json(BERKAS / f"a_{i // 20:02d}.json",
                   [{"idx": int(r["idx"]), "judul": r["judul"], "tahun": r["tahun"], "sumber": r["sumber"],
                     "abstrak": r["abstrak"]} for r in sa[i:i + 20]])
    print(f"paket j: {len(sj)} judul; paket a: {len(sa)} abstrak")

    # --- paket f: cek fakta per kajian
    key2rec = {}
    for idx, k in kand.items():
        key2rec[k["key"]] = rec[idx]
    met = {}
    p_met = KORPUS / "metodologi/terpilih.csv"
    if p_met.exists():
        for r in baca_csv(p_met):
            met[r.get("key", "")] = r
    klaim = defaultdict(list)
    for r in baca_csv(VER / "cek-6-cek-fakta" / "cek_fakta.csv"):
        if r["key"] and r["prioritas"] not in ("S", "lama"):
            klaim[r["key"]].append({"id": r["id"], "bagian": r["bagian"], "jenis": r["jenis"],
                                    "kalimat": r["kalimat"]})
    kajian = []
    for key, ks in sorted(klaim.items()):
        r = key2rec.get(key) or met.get(key) or {}
        e = ab.get(r.get("eid", ""), {})
        teks = KORPUS / "teks" / f"{key}.txt"
        kajian.append({
            "key": key, "judul": r.get("title", ""), "tahun": r.get("year", ""),
            "doi": r.get("doi", ""), "abstrak": e.get("abstract") or "",
            "teks_lengkap": f"literature/scopus-2026-09/teks/{key}.txt" if teks.exists() else "",
            "klaim": ks,
        })

    def bobot_f(x):
        return (3 if x["teks_lengkap"] else 1.5) + 0.5 * (len(x["klaim"]) - 1)

    paket = kemas(kajian, bobot_f, 12, rng)
    for i, p in enumerate(paket):
        tulis_json(BERKAS / f"f_{i:03d}.json", p)
    print(f"paket f: {len(kajian)} kajian, {sum(len(x['klaim']) for x in kajian)} baris klaim, "
          f"{len(paket)} paket; tanpa metadata: {sum(1 for x in kajian if not x['judul'])}")
    HASIL.mkdir(parents=True, exist_ok=True)


def status():
    for awalan in ("s", "j", "a", "f", "adj", "vf", "t", "u", "ru"):
        ber = sorted(BERKAS.glob(f"{awalan}_[0-9]*.json"))
        ada, rusak = 0, []
        for b in ber:
            h = HASIL / b.name
            if not h.exists():
                continue
            try:
                isi = json.loads(h.read_text(encoding="utf-8"))
                kunci = "key" if awalan in ("f", "vf") else "idx"
                mau = {str(x[kunci]) for x in json.loads(b.read_text(encoding="utf-8"))}
                dapat = {str(x[kunci]) for x in isi}
                if mau - dapat:
                    rusak.append(f"{b.name}: kurang {sorted(mau - dapat)[:5]}")
                else:
                    ada += 1
            except Exception as e:  # noqa: BLE001
                rusak.append(f"{b.name}: {e}")
        print(f"paket {awalan}: {len(ber)} paket, {ada} selesai, {len(rusak)} bermasalah")
        for r in rusak:
            print("   ", r)


GRUP = {"C1", "C2", "C3", "C4", "C5", "R", "T", "X"}
DASAR = {"teks lengkap", "teks lengkap (web)", "abstrak", "abstrak (web)", "judul"}
YAKIN = {"tinggi", "sedang", "rendah"}
MEK = re.compile(r"^(DATA|M[0-5](\+M[0-5])*)$")
REF = {"pohon", "panen", "packhouse", "anotasi", "tidak ada"}
MET = {"hitung", "identitas", "deteksi", "tidak ada"}
CARA = {"saat pelacakan", "sesudah pelacakan", "voting antarpandang", "tidak dinyatakan", "", "-"}
TUGAS = {"KLS", "DET", "HIT", "LF", "MUTU", "SENSOR", "DATA"}
LOKASI = {"POHON", "TANAH", "PABRIK", "UAV", "?"}


def periksa_isi(nama, isi, paket):
    """Mengembalikan daftar galat untuk satu berkas hasil."""
    g = []
    awalan = nama.split("_")[0]
    kunci = "key" if awalan in ("f", "vf") else "idx"
    if awalan == "ref":
        if not isinstance(isi, list):
            return ["akar JSON harus berupa daftar"]
        for x in isi:
            if not isinstance(x, dict) or "idx" not in x:
                g.append("butir harus objek dengan idx")
            elif x.get("bertahan") not in (True, False):
                g.append(f"idx {x.get('idx')}: bertahan harus true/false")
            elif not str(x.get("alasan", "")).strip():
                g.append(f"idx {x.get('idx')}: alasan kosong")
        return g
    if not isinstance(isi, list):
        return ["akar JSON harus berupa daftar"]
    mau = [str(x[kunci]) for x in paket]
    dapat = [str(x.get(kunci)) for x in isi if isinstance(x, dict)]
    for k in mau:
        if k not in dapat:
            g.append(f"{kunci} {k}: tidak ada di hasil")
    for k in dapat:
        if k not in mau:
            g.append(f"{kunci} {k}: bukan anggota paket ini")
    for x in isi:
        if not isinstance(x, dict):
            g.append("butir bukan objek")
            continue
        t = f"{kunci} {x.get(kunci)}"
        if awalan == "adj":
            if not isinstance(x.get("ubah_dari_putaran_1"), list):
                g.append(f"{t}: ubah_dari_putaran_1 harus daftar nama kolom (boleh kosong)")
            if not str(x.get("alasan_ajudikasi", "")).strip():
                g.append(f"{t}: alasan_ajudikasi kosong")
            if x.get("perlu_manusia") not in (True, False):
                g.append(f"{t}: perlu_manusia harus true/false")
        if awalan in ("s", "adj", "t", "u"):
            if x.get("dasar_bukti") not in DASAR:
                g.append(f"{t}: dasar_bukti harus salah satu {sorted(DASAR)}")
            if x.get("kode") not in GRUP:
                g.append(f"{t}: kode harus salah satu {sorted(GRUP)}")
            if x.get("kode") == "X" and not re.fullmatch(r"E[1-7]", str(x.get("alasan", ""))):
                g.append(f"{t}: kode X perlu alasan E1..E7")
            if x.get("kode") != "X" and x.get("alasan"):
                g.append(f"{t}: alasan hanya untuk kode X")
            if not isinstance(x.get("juga_cocok", []), list) or set(x.get("juga_cocok", [])) - GRUP:
                g.append(f"{t}: juga_cocok harus daftar kode grup")
            if x.get("keyakinan") not in YAKIN:
                g.append(f"{t}: keyakinan harus tinggi/sedang/rendah")
            if not isinstance(x.get("bukti"), list):
                g.append(f"{t}: bukti harus daftar kutipan (boleh kosong bila hanya judul)")
            c1, c3 = x.get("c1"), x.get("c3")
            if x.get("kode") == "C1" or "C1" in x.get("juga_cocok", []):
                if not isinstance(c1, dict):
                    g.append(f"{t}: kode C1 (utama atau juga_cocok) perlu objek c1")
                else:
                    if not MEK.match(str(c1.get("mekanisme", ""))):
                        g.append(f"{t}: c1.mekanisme tidak sah ({c1.get('mekanisme')!r})")
                    if c1.get("akuisisi") not in {"V", "D", "S", "T", "1"}:
                        g.append(f"{t}: c1.akuisisi harus V/D/S/T/1")
                    if c1.get("per_kelas") not in {"Y", "N"}:
                        g.append(f"{t}: c1.per_kelas harus Y/N")
                    if c1.get("cara_kelas", "") not in CARA:
                        g.append(f"{t}: c1.cara_kelas tidak sah")
                    for kol, sah in (("referensi_hitung", REF), ("tingkat_metrik", MET)):
                        v = [a.strip() for a in str(c1.get(kol, "")).split(";") if a.strip()]
                        if not v or set(v) - sah:
                            g.append(f"{t}: c1.{kol} harus dari {sorted(sah)} (gabungan dengan ';')")
                    if not str(c1.get("hasil_ringkas", "")).strip():
                        g.append(f"{t}: c1.hasil_ringkas kosong")
                    if "\t" in str(c1.get("hasil_ringkas", "")):
                        g.append(f"{t}: c1.hasil_ringkas tidak boleh memuat TAB")
            if x.get("kode") == "C3" or "C3" in x.get("juga_cocok", []):
                if not isinstance(c3, dict):
                    g.append(f"{t}: kode C3 (utama atau juga_cocok) perlu objek c3")
                else:
                    if c3.get("tugas") not in TUGAS:
                        g.append(f"{t}: c3.tugas harus salah satu {sorted(TUGAS)}")
                    if c3.get("lokasi") not in LOKASI:
                        g.append(f"{t}: c3.lokasi harus salah satu {sorted(LOKASI)}")
                    if not str(c3.get("modalitas", "")).strip():
                        g.append(f"{t}: c3.modalitas kosong")
                    if c3.get("multipandang") not in {"Y", "N"} or c3.get("per_kelas") not in {"Y", "N"}:
                        g.append(f"{t}: c3.multipandang dan c3.per_kelas harus Y/N")
        elif awalan == "j":
            if x.get("keputusan") not in {"L", "L-C1", "L-C3", "X"}:
                g.append(f"{t}: keputusan harus L, L-C1, L-C3, atau X")
        elif awalan == "a":
            if not re.fullmatch(r"C[1-5]|T|R|X-E[1-7]", str(x.get("keputusan", ""))):
                g.append(f"{t}: keputusan harus C1..C5, T, R, atau X-E1..X-E7")
        elif awalan == "vf":
            mauid = {k["id"] for p in paket if p["key"] == x.get("key") for k in p["klaim"]}
            ada = set()
            for k in x.get("klaim", []) if isinstance(x.get("klaim"), list) else []:
                ada.add(k.get("id"))
                if k.get("putusan") not in {"Y", "N", "SEBAGIAN", "TAK-TERPERIKSA"}:
                    g.append(f"{t} {k.get('id')}: putusan harus Y, N, SEBAGIAN, atau TAK-TERPERIKSA")
                if k.get("putusan") in {"N", "SEBAGIAN"} and not str(k.get("perbaikan_final", "")).strip():
                    g.append(f"{t} {k.get('id')}: N/SEBAGIAN perlu perbaikan_final")
                if not str(k.get("alasan", "")).strip():
                    g.append(f"{t} {k.get('id')}: alasan kosong")
            if mauid - ada:
                g.append(f"{t}: klaim belum diverifikasi {sorted(mauid - ada)}")
        elif awalan == "f":
            if x.get("dasar_bukti") not in DASAR:
                g.append(f"{t}: dasar_bukti harus salah satu {sorted(DASAR)}")
            mauid = {k["id"] for p in paket if p["key"] == x.get("key") for k in p["klaim"]}
            ada = set()
            for k in x.get("klaim", []) if isinstance(x.get("klaim"), list) else []:
                ada.add(k.get("id"))
                if k.get("benar") not in {"Y", "N", "SEBAGIAN", "TAK-TERPERIKSA"}:
                    g.append(f"{t} {k.get('id')}: benar harus Y, N, SEBAGIAN, atau TAK-TERPERIKSA")
                if k.get("benar") in {"N", "SEBAGIAN"} and not str(k.get("perbaikan", "")).strip():
                    g.append(f"{t} {k.get('id')}: N/SEBAGIAN perlu perbaikan")
                if k.get("benar") in {"Y", "N", "SEBAGIAN"} and not str(k.get("bukti", "")).strip():
                    g.append(f"{t} {k.get('id')}: perlu bukti (kutipan verbatim dari sumber)")
            if mauid - ada:
                g.append(f"{t}: klaim belum dinilai {sorted(mauid - ada)}")
    return g


def periksa(nama):
    b = BERKAS / (nama[4:] if nama.startswith("ref_") else nama)
    h = HASIL / nama
    if not b.exists():
        sys.exit(f"paket tidak dikenal: {nama}")
    if not h.exists():
        sys.exit(f"GALAT: hasil belum ditulis: {h}")
    try:
        isi = json.loads(h.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        sys.exit(f"GALAT: JSON tidak sah: {e}")
    g = periksa_isi(nama, isi, json.loads(b.read_text(encoding="utf-8")))
    if g:
        print(f"GALAT ({len(g)}):")
        for x in g:
            print(" -", x)
        sys.exit(1)
    print(f"OK {nama}: {len(isi)} butir sah")


def siapkan_t():
    """Paket t: judul sampel yang dikeluarkan putaran 1 tetapi ingin dilanjutkan putaran 2."""
    rec = {int(r["idx"]): r for r in baca_csv(TOPIK / "records_all.csv")}
    baris = [r for r in baca_csv(AI2 / "banding_sampel.csv")
             if r["tahap"] == "judul" and r["ai1"].startswith("X") and r["ai2"].startswith("L")]
    items = []
    for b in baris:
        r = rec[int(b["idx"])]
        items.append({"idx": int(b["idx"]), "key": "", "judul": r["title"], "tahun": r["year"],
                      "penulis_pertama": r["first_author"], "sumber": r["source"],
                      "tipe_dokumen": r["doc_type"], "doi": r["doi"], "abstrak": "", "sumber_abstrak": "",
                      "teks_lengkap": "", "pdf": "", "tanda_putaran_2": b["ai2"]})
    for lama in BERKAS.glob("t_*.json"):
        lama.unlink()
    for i in range(0, len(items), 11):
        tulis_json(BERKAS / f"t_{i // 11:02d}.json", items[i:i + 11])
    print(f"paket t: {len(items)} judul dalam {(len(items) + 10) // 11} paket")


if __name__ == "__main__":
    perintah = sys.argv[1] if len(sys.argv) > 1 else ""
    if perintah == "siapkan":
        siapkan()
    elif perintah == "siapkan-t":
        siapkan_t()
    elif perintah == "status":
        status()
    elif perintah == "periksa" and len(sys.argv) > 2:
        periksa(sys.argv[2])
    else:
        sys.exit(__doc__)
