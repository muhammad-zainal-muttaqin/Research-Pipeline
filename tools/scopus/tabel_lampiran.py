#!/usr/bin/env python3
"""Membuat tabel lampiran LaTeX (matriks bukti C1) dari matriks_bukti.csv.

Kode di bukti/mekanisme_C1.txt (M0-M5, V/D/S/T/1) hanya kunci internal berkas
data. Tabel menuliskannya dengan nama, sama seperti naskah dan gambar, sehingga
pembaca tidak perlu menghafal kode. Keluaran:
manuscript/source/main6-appendix-c1.tex
"""
import csv
import re
from pathlib import Path

from latex_teks import ke_latex  # noqa: F401  (dipakai skrip lain yang mengimpor modul ini)

ROOT = Path(__file__).resolve().parents[2]
MAT = ROOT / "literature/scopus-2026-09/topik/bukti/matriks_bukti.csv"
TEMUAN = ROOT / "literature/scopus-2026-09/topik/bukti/temuan_C1.tsv"
OUT = ROOT / "manuscript/source/main6-appendix-c1.tex"

PLAT = {"UAV": "UAV", "ground vehicle/robot": "Ground vehicle or robot", "handheld/smartphone": "Handheld",
        "fixed camera": "Fixed camera", "conveyor/lab": "Laboratory"}
AKUISISI = {"V": "Video", "D": "Discrete views", "S": "3D scan", "T": "Revisits", "1": "Single view"}
NAMA_MEK = {"M0": "No association", "M1": "Statistical correction", "M2": "Appearance matching",
            "M3": "Temporal tracking", "M4": "Geometric or 3D association", "M5": "Learned association",
            "DATA": "Dataset paper"}
NAMA_PENDEK = {"M0": "no association", "M1": "statistical", "M2": "appearance", "M3": "tracking",
               "M4": "geometric", "M5": "learned"}
TINGKAT = [("hitung", "Count"), ("identitas", "Identity"), ("deteksi", "Detection")]
DASAR = {"teks lengkap": "Full text", "abstrak": "Abstract", "judul": "Title"}
CROP_ABBR = {"peach/nectarine": "peach", "sweet pepper": "pepper", "litchi/longan": "litchi",
             "plum/apricot": "plum", "passion fruit": "passion fruit", "other berries": "berry",
             "persimmon/guava": "persimmon", "pumpkin/squash": "pumpkin", "nut crops": "nut"}


AKRONIM = {
    "AGV": "automated guided vehicle", "AP": "average precision",
    "AP50": "average precision at an intersection-over-union threshold of 0.5",
    "ARIMA": "autoregressive integrated moving average",
    "DBSCAN": "density-based spatial clustering of applications with noise",
    "DIoU": "distance intersection over union", "EKF": "extended Kalman filter",
    "FCN": "fully convolutional network", "FPR": "false positive rate",
    "GIoU": "generalized intersection over union", "GMM": "Gaussian mixture model",
    "GNSS": "global navigation satellite system", "GPS": "global positioning system",
    "HOTA": "higher-order tracking accuracy", "ICP": "iterative closest point", "ID": "identity",
    "IDF1": "identification F1 score", "IDSW": "identity switches", "IoU": "intersection over union",
    "KLT": "Kanade-Lucas-Tomasi feature tracker", "LiDAR": "light detection and ranging",
    "MAE": "mean absolute error", "MAPE": "mean absolute percentage error", "MB": "megabytes",
    "MedAE": "median absolute error", "MHT": "multiple hypothesis tracking",
    "MOT": "multiple-object tracking", "MOTA": "multiple-object tracking accuracy",
    "MOTS": "multi-object tracking and segmentation",
    "MOTSA": "multi-object tracking and segmentation accuracy",
    "sMOTSA": "soft multi-object tracking and segmentation accuracy", "MVS": "multi-view stereo",
    "NeRF": "neural radiance field", "NIR": "near-infrared", "NMS": "non-maximum suppression",
    "NRMSE": "normalized root-mean-square error", "RANSAC": "random sample consensus",
    "re-ID": "re-identification", "RGB": "red-green-blue",
    "RGB-D": "red-green-blue-depth", "RMSE": "root-mean-square error", "ROI": "region of interest",
    "ROS": "Robot Operating System", "RTK": "real-time kinematic positioning",
    "SfM": "structure from motion", "SIFT": "scale-invariant feature transform",
    "SLAM": "simultaneous localization and mapping", "SORT": "simple online and realtime tracking",
    "SURF": "speeded-up robust features", "SVM": "support vector machine",
    "SVR": "support vector regression", "TPR": "true positive rate", "UAV": "unmanned aerial vehicle",
    "WAPE": "weighted absolute percentage error", "YOLO": "You Only Look Once",
    "mAP": "mean average precision",
    "mAP50": "mean average precision at an intersection-over-union threshold of 0.5",
    "mAP50-95": "mean average precision over intersection-over-union thresholds from 0.5 to 0.95",
    "mIoU": "mean intersection over union",
}
NAMA_METODE = {
    "AgriSORT", "ALRM-Track", "BoT-SORT", "BoTSORT", "ByteTrack", "Cascade-SORT", "CloseUp", "ConvNet",
    "CoTracker3", "CottonSense", "DeepSORT", "DeepSort", "DynCount", "FaceNet", "FairMOT", "FlowNet2",
    "FruitNeRF", "Grounded-SAM2", "KinectV2", "KiwiDetector", "KiwiTracker", "LettuceMOT", "LFuji-air",
    "LoFTR", "MAFP", "MinkPanoptic", "MOrangeT", "MR-SORT", "MultiMap", "NTrack", "OC-SORT", "OCSort", "ORB-SLAM3",
    "OrangeSort", "PineSORT", "PointRCNN", "PointTrack", "R-CNN", "SAM2", "SiamFC", "StrongSORT", "TexCot22",
    "XGBoost", "ZED",
}
POLA_NAMA = re.compile(r"^(\w*YOLO\w*|\w*Yolo\w*|YOLOv\w+|ResNet\d*)$")


def akronim_tabel(teks):
    """Jabaran akronim yang muncul di tabel. Berhenti bila ada token berhuruf kapital ganda yang
    bukan akronim terdaftar (AKRONIM) dan bukan nama metode (NAMA_METODE, POLA_NAMA), agar setiap
    akronim di Lampiran A dijabarkan di catatan tabel."""
    teks = re.sub(r"\\cite[pt]?\{[^}]*\}", "", teks)
    dipakai, asing = set(), set()
    for tok in re.findall(r"[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9]", teks):
        if tok in NAMA_METODE or any(POLA_NAMA.match(b) for b in tok.split("-")):
            continue
        if tok in AKRONIM:
            dipakai.add(tok)
            continue
        for bag in tok.split("-"):
            dasar = bag[:-1] if bag.endswith("s") and bag[:-1] in AKRONIM else bag
            if dasar in AKRONIM:
                dipakai.add(dasar)
            elif sum(c.isupper() for c in bag) >= 2 and bag not in NAMA_METODE and not POLA_NAMA.match(bag):
                asing.add(tok)
    if asing:
        raise SystemExit("Akronim tanpa jabaran di tabel_lampiran.py (tambahkan ke AKRONIM atau "
                         "NAMA_METODE): " + ", ".join(sorted(asing)))
    return "; ".join(f"{a}, {AKRONIM[a]}" for a in sorted(dipakai, key=str.lower))


def nama_mekanisme(kode):
    """'M3+M2' -> 'Appearance + tracking'; urutan tetap M0..M5 apa pun urutan di berkas data."""
    bagian = sorted(set(kode.split("+")))
    if len(bagian) == 1:
        return NAMA_MEK.get(bagian[0], kode)
    t = " + ".join(NAMA_PENDEK[b] for b in bagian)
    return t[0].upper() + t[1:]


def sel_metrik(r):
    """Jenis metrik dari kolom tingkat_metrik (kode teks lengkap); "Not coded" bila kolom itu kosong."""
    ms = {x.strip() for x in r["tingkat_metrik"].split(";") if x.strip()}
    if not ms:
        return "Not coded"
    out = [nama for k, nama in TINGKAT if k in ms]
    return ", ".join(out).capitalize() if out else "None"


def sel_dasar(r):
    """Dasar pengodean: kolom verifikasi sumber_kode bila ada, selain itu dasar keputusan penyaringan."""
    v = (r.get("sumber_kode") or "").strip() or r.get("dasar_keputusan", "")
    return DASAR.get(v, "Abstract")


def main():
    rows = [r for r in csv.DictReader(open(MAT, encoding="utf-8")) if r["kode"] == "C1"]
    rows.sort(key=lambda r: (int(r["year"]), r["first_author"]))
    temuan = dict(l.rstrip("\n").split("\t", 1) for l in open(TEMUAN, encoding="utf-8") if "\t" in l)
    baris = []
    for r in rows:
        tan = r["tanaman"].split(";")[0] if r["tanaman"] else "Not stated"
        tan = CROP_ABBR.get(tan, tan).capitalize()
        plat = ", ".join(PLAT[p] for p in r["platform"].split(";") if p in PLAT) or "Not stated"
        kelas = "Yes" if r["per_kelas"] == "Y" else "No"
        baris.append(f"\\citet{{{r['key']}}} & {tan} & {plat} & "
                     f"{AKUISISI.get(r['akuisisi_manual'], 'Not stated')} & {nama_mekanisme(r['mekanisme'])} & "
                     f"{kelas} & {sel_metrik(r)} & {temuan.get(r['key'], '')} \\\\")
    judul = (r"Study & Crop & Platform & Acquisition & Association mechanism & Per-class counts & "
             r"Metric types & Main finding\\")
    kepala = r"""%% Dibuat otomatis oleh tools/scopus/tabel_lampiran.py; jangan disunting manual.
\begin{footnotesize}
\setlength{\tabcolsep}{3pt}
\begin{longtable}{@{}L{2.5cm}L{1.3cm}L{1.6cm}L{1.4cm}L{2.2cm}L{0.9cm}L{1.5cm}L{5.0cm}@{}}
\caption{Detailed coding records of the %d multi-observation studies.}\label{tab:c1matrix}\\
\toprule
%s
\midrule
\endfirsthead
\toprule
%s
\midrule
\endhead
\bottomrule
\endfoot
\bottomrule
\multicolumn{8}{@{}p{\textwidth}@{}}{\rule{0pt}{2.6ex}\textit{Note:} A plus sign joins the mechanisms that a study combines. Crop (the first crop whose fruit the study itself detected, counted, or tracked) and platform (what carried the camera) were read from the full text; Not stated, the text does not say. Metric types were coded from the full text where it was read: Count, agreement between estimated and reference counts; Identity, a tracking metric such as MOTA, IDF1, HOTA, or identity switches; Detection, detection quality; None, no quantitative metric; Not coded, the metric type was not recorded during full-text coding. Main finding: the principal result reported by the study, as coded, with values as reported. %s.}\\
\endlastfoot
""" % (len(rows), judul, judul, akronim_tabel("\n".join(baris)))
    OUT.write_text(kepala + "\n".join(baris) + "\n\\end{longtable}\n\\end{footnotesize}\n", newline="\n")
    print(len(rows), "baris ->", OUT)


if __name__ == "__main__":
    main()
