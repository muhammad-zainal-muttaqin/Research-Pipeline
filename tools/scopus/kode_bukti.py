#!/usr/bin/env python3
"""Pengodean awal matriks bukti dari judul dan abstrak kajian yang lolos.

Aturan kata kunci di bawah hanya menghasilkan kode awal. Kode mekanisme
identitas untuk kajian C1 diperiksa ulang secara manual dan disimpan di
bukti/mekanisme_C1.txt; berkas itu menimpa kode otomatis.

Keluaran: bukti/matriks_bukti.csv (satu baris per kajian yang lolos).

Kolom verifikasi teks lengkap (Pemeriksaan 5, lihat
literature/scopus-2026-09/verifikasi/KODE-ULANG.md): mekanisme_C1.txt boleh
memuat enam kolom TAB tambahan yang opsional sesudah hasil_ringkas, yaitu
sumber_kode, halaman, referensi_hitung, tingkat_metrik, cara_kelas, berubah.
Keenam kolom itu ditambahkan di ujung kanan matriks_bukti.csv hanya bila
sedikitnya satu baris mekanisme_C1.txt mengisinya (atau bila diminta dengan
--kolom-verifikasi); tanpa isian, matriks_bukti.csv identik byte demi byte
dengan keluaran versi sebelumnya. Sel kosong berarti belum diverifikasi.
"""
import argparse
import csv
import glob
import json
import re
from pathlib import Path

KODE = re.compile(r"^(\d+)\s+(C[1-5]|T|R|M|X)(?:\s+(E\d))?(.*)$")

TANAMAN = [
    ("oil palm", r"oil[- ]palm|palm oil|fresh fruit bunch|\bffbs?\b|palm fruit|loose fruit"),
    ("apple", r"\bapples?\b"),
    ("citrus", r"citrus|orange|mandarin|tangerine|lemon|pomelo|kumquat|navel"),
    ("mango", r"\bmangoe?s?\b"),
    ("grape", r"grape|vineyard|vitis|berry clusters"),
    ("tomato", r"tomato"),
    ("strawberry", r"strawberr"),
    ("kiwifruit", r"kiwi"),
    ("peach/nectarine", r"peach|nectarine"),
    ("pear", r"\bpears?\b"),
    ("cherry", r"cherr(y|ies)"),
    ("blueberry", r"blueberr"),
    ("sweet pepper", r"pepper|capsicum"),
    ("coconut", r"coconut"),
    ("date palm", r"date palm|date fruit"),
    ("banana", r"banana"),
    ("pineapple", r"pineapple"),
    ("pomegranate", r"pomegranate"),
    ("passion fruit", r"passion fruit"),
    ("camellia", r"camellia"),
    ("coffee", r"coffee"),
    ("olive", r"\bolives?\b"),
    ("avocado", r"avocado"),
    ("melon", r"melon"),
    ("cucumber", r"cucumber"),
    ("jujube", r"jujube"),
    ("litchi/longan", r"litchi|lychee|longan"),
    ("pitaya", r"pitaya|dragon fruit"),
    ("plum/apricot", r"\bplums?\b|apricot"),
    ("nut crops", r"walnut|almond|macadamia|pecan|hazelnut"),
    ("papaya", r"papaya"),
    ("other berries", r"raspberr|blackberr|cranberr"),
    ("persimmon/guava", r"persimmon|guava"),
    ("pumpkin/squash", r"pumpkin|squash"),
    ("cotton", r"cotton"),
]

MODALITAS = [
    ("RGB-D", r"rgb-?d\b|depth camera|realsense|kinect|time[- ]of[- ]flight|\btof\b|zed (mini|camera|2)|azure kinect|depth (image|map|sensor|information)"),
    ("stereo", r"stereo|binocular"),
    ("LiDAR", r"lidar|laser scann|terrestrial laser|\btls\b"),
    ("thermal", r"thermal"),
    ("multispectral", r"multispectral|multi-spectral"),
    ("hyperspectral", r"hyperspectral"),
    ("NIR", r"\bnir\b|near[- ]infrared"),
    ("monocular depth", r"monocular (metric )?depth|depth anything|depth estimation network|estimated depth"),
    ("radar", r"\bradar\b"),
]

PLATFORM = [
    ("UAV", r"\buav|drone|unmanned aerial|aerial imag"),
    ("ground vehicle/robot", r"robot|vehicle|tractor|\bugv\b|mobile platform|ground platform|rover|harvester|trolley|cart"),
    ("handheld/smartphone", r"smartphone|mobile phone|handheld|hand-held|android|mobile device"),
    ("fixed camera", r"fixed camera|stationary camera|surveillance camera|time-lapse"),
    ("conveyor/lab", r"conveyor|laborator|\blab\b|grading machine|sorting machine|loading ramp|mill"),
]

AKUISISI = [
    ("video", r"video|frames?\b|image sequence|sequence of images"),
    ("multi-view", r"multi-?view|multiple views|multiple viewpoints|dual[- ]side|both sides|two sides|opposite sides|four sides|multi-?camera|multiple cameras|multi-perspective|bilateral"),
    ("3D scan/reconstruction", r"point cloud|3d reconstruction|structure[- ]from[- ]motion|\bsfm\b|photogrammetr|nerf|radiance field|gaussian splatting|\bslam\b"),
]

MEKANISME = [
    ("M1", r"correction factor|calibration factor|visibility factor|occlusion (factor|ratio)|regression (to|against) (harvest|manual)|linear regression|calibrated (against|to) (harvest|manual)|scaling factor"),
    ("M2", r"re-?identification|\breid\b|appearance (feature|descriptor|embedding)|deep ?sort|feature matching|descriptor match"),
    ("M3", r"track|\bsort\b|bytetrack|kalman|optical flow|hungarian|counting line|counting region|virtual line"),
    ("M4", r"point cloud|structure[- ]from[- ]motion|\bsfm\b|\bslam\b|3d (map|mapping|reconstruction|localization|localisation|position)|triangulat|epipolar|gnss|\bgps\b|\brtk\b|registration|nerf|radiance field|gaussian splatting|odometry|global coordinate"),
    ("M5", r"learned (association|matching)|graph neural|matching network|association network|attention-based matching|transformer[- ]based (association|tracking|matching)|end-to-end tracking"),
]

METRIK = [
    ("MAE", r"\bmae\b|mean absolute error"),
    ("RMSE", r"\brmse\b|root mean square"),
    ("R2", r"\br2\b|r²|r\^2|coefficient of determination|\br ?= ?0\.\d"),
    ("MAPE/rel. error", r"mape|relative error|percentage error|counting error|count error|error rate"),
    ("count accuracy", r"counting accuracy|count accuracy|counting precision"),
    ("MOTA", r"\bmota\b"),
    ("IDF1", r"idf1"),
    ("HOTA", r"\bhota\b"),
    ("ID switch", r"id switch|identity switch|idsw"),
    ("mAP/AP", r"\bmap\b|\bap\b|average precision|map50|map@"),
    ("F1", r"\bf1\b|f-score|f-measure"),
]

ATRIBUT = [
    ("maturity", r"ripe|maturit|ripening|growth stage|colou?r grade|harvest stage|immature|mature"),
    ("size", r"\bsize\b|sizing|diameter|volume"),
    ("mass", r"weight|mass estimation|\bmass\b"),
    ("defect/disease", r"defect|disease|damage|rotten|bruise"),
    ("variety/type", r"variety|cultivar|bunch type|fruit type"),
]


def cocok(daftar, teks):
    return [nama for nama, pola in daftar if re.search(pola, teks, re.I)]


def muat_keputusan(folder):
    dec, catatan = {}, {}
    for fn in sorted(glob.glob(str(folder / "abstrak_*.txt"))):
        for line in open(fn):
            m = KODE.match(line.strip())
            if m:
                i = int(m.group(1))
                dec[i] = (m.group(2), m.group(3) or "")
                catatan[i] = "judul" if "(judul)" in line or Path(fn).name == "abstrak_T00.txt" else "abstrak"
    return dec, catatan


# Kolom opsional hasil verifikasi teks lengkap (kolom ke-6 s.d. ke-11 berkas
# mekanisme_C1.txt), dalam urutan tetap.
KOLOM_VERIFIKASI = ["sumber_kode", "halaman", "referensi_hitung",
                    "tingkat_metrik", "cara_kelas", "berubah"]


def muat_manual(path, lengkap=False):
    """Baris: idx, mekanisme, akuisisi, per_kelas, hasil (dipisah TAB),
    lalu enam kolom verifikasi opsional (KOLOM_VERIFIKASI).
    Mekanisme gabungan ditulis dengan '+', misalnya M3+M4.

    lengkap=False mengembalikan tuple 4 kolom lama (perilaku semula);
    lengkap=True mengembalikan tuple 4 + len(KOLOM_VERIFIKASI) kolom."""
    n = 4 + (len(KOLOM_VERIFIKASI) if lengkap else 0)
    out = {}
    if path.exists():
        for line in open(path, encoding="utf-8"):
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\r\n").split("\t")
            parts += [""] * (1 + n - len(parts))
            out[int(parts[0])] = tuple(p.strip() if j >= 4 else p
                                       for j, p in enumerate(parts[1:1 + n]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topik", default="literature/scopus-2026-09/topik")
    ap.add_argument("--kolom-verifikasi", action="store_true",
                    help="selalu tulis enam kolom verifikasi walau belum ada isian")
    args = ap.parse_args()
    topik = Path(args.topik)
    pen = topik / "penyaringan"
    bukti = topik / "bukti"
    bukti.mkdir(exist_ok=True)

    dec, sumber_kep = muat_keputusan(pen)
    manual = muat_manual(bukti / "mekanisme_C1.txt", lengkap=True)
    ada_verif = args.kolom_verifikasi or any(any(v[4:]) for v in manual.values())
    rec = {r["eid"]: r for r in csv.DictReader(open(topik / "records_all.csv"))}
    enr = {}
    for line in open(topik / "enrich.jsonl"):
        e = json.loads(line)
        enr[e["eid"]] = e

    kolom = ["idx", "key", "eid", "doi", "year", "first_author", "title", "source",
             "doc_type", "cited_by", "kode", "dasar_keputusan", "tanaman",
             "modalitas", "platform", "akuisisi", "mekanisme_otomatis",
             "mekanisme", "akuisisi_manual", "per_kelas", "hasil_ringkas",
             "atribut_kelas", "metrik",
             "ada_abstrak"]
    if ada_verif:
        kolom += KOLOM_VERIFIKASI
    baris = []
    for r in csv.DictReader(open(pen / "kandidat_abstrak.csv")):
        i = int(r["idx"])
        kode, _ = dec.get(i, ("?", ""))
        if kode == "X":
            continue
        e = enr.get(r["eid"], {})
        abstrak = e.get("abstract") or ""
        teks = f"{r['title']} {abstrak}"
        mod = cocok(MODALITAS, teks) or ["RGB"]
        mek_auto = cocok(MEKANISME, teks) if kode == "C1" else []
        kode_manual = manual.get(i, ("",) * (4 + len(KOLOM_VERIFIKASI)))
        mek, akm, kelas, hasil = kode_manual[:4]
        b = {
            "idx": i, "key": r["key"], "eid": r["eid"], "doi": r["doi"],
            "year": r["year"], "first_author": r["first_author"],
            "title": r["title"], "source": r["source"],
            "doc_type": r["doc_type"], "cited_by": r["cited_by"],
            "kode": kode, "dasar_keputusan": sumber_kep.get(i, ""),
            "tanaman": ";".join(cocok(TANAMAN, teks)),
            "modalitas": ";".join(mod),
            "platform": ";".join(cocok(PLATFORM, teks)),
            "akuisisi": ";".join(cocok(AKUISISI, teks)),
            "mekanisme_otomatis": "+".join(mek_auto),
            "mekanisme": mek, "akuisisi_manual": akm, "per_kelas": kelas,
            "hasil_ringkas": hasil,
            "atribut_kelas": ";".join(cocok(ATRIBUT, teks)),
            "metrik": ";".join(cocok(METRIK, teks)),
            "ada_abstrak": "ya" if abstrak else "tidak",
        }
        if ada_verif:
            b.update(zip(KOLOM_VERIFIKASI, kode_manual[4:]))
        baris.append(b)
    baris.sort(key=lambda b: (b["kode"], -int(b["year"]), b["key"]))
    with open(bukti / "matriks_bukti.csv", "w", newline="", encoding="utf-8") as f:
        # Akhir baris LF, sesuai .gitattributes (eol=lf) dan berkas di Git.
        w = csv.DictWriter(f, fieldnames=kolom, lineterminator="\n")
        w.writeheader()
        w.writerows(baris)
    print(len(baris), "baris ->", bukti / "matriks_bukti.csv",
          "(dengan kolom verifikasi)" if ada_verif else "")


if __name__ == "__main__":
    main()
