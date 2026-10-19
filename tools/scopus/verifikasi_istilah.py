"""Arti kode korpus main6 untuk lembar verifikasi yang dibaca manusia.

Lembar menulis kode bersama artinya, misalnya "M3 (pelacakan video)", agar dapat
dibaca tanpa berkas lain. Skrip yang membaca lembar memakai kode() untuk
mengembalikan sel ke kode mentahnya.
"""
import re

KEL = {'C1': 'C1 (hitung dari banyak pengamatan buah yang sama)', 'C2': 'C2 (hitung dari satu foto)',
       'C3': 'C3 (sawit)', 'C4': 'C4 (hitung per kelas dari satu foto)',
       'C5': 'C5 (kamera depth/3D atau sensor lain)', 'R': 'R (tinjauan pustaka)',
       'T': 'T (metode dari luar pertanian)'}
EKS = {'E1': 'bukan buah di tanaman', 'E2': 'hanya pascapanen/laboratorium',
       'E3': 'hasil panen tanpa deteksi buah', 'E4': 'hanya robot pemetik',
       'E5': 'deteksi tanpa hitung atau evaluasi', 'E6': 'sensor bukan kamera', 'E7': 'tidak berbahasa Inggris'}
MEK = {'M0': 'tanpa penghubungan buah', 'M1': 'koreksi statistik', 'M2': 'pencocokan penampilan',
       'M3': 'pelacakan video', 'M4': 'pencocokan posisi 3D', 'M5': 'pencocokan yang dipelajari',
       'DATA': 'dataset'}
AKU = {'V': 'video sepanjang lintasan', 'D': 'beberapa foto dari posisi terpisah', 'S': 'model 3D/awan titik',
       'T': 'kunjungan ulang antarwaktu', '1': 'satu foto'}
TUGAS = {'KLS': 'kematangan', 'DET': 'deteksi tandan', 'HIT': 'menghitung', 'LF': 'brondolan',
         'MUTU': 'mutu/massa/volume', 'SENSOR': 'sensor non-RGB', 'DATA': 'dataset', '?': 'tidak jelas'}
LOK = {'POHON': 'di pohon', 'TANAH': 'di tanah/TPH', 'PABRIK': 'pabrik/laboratorium', 'UAV': 'dari drone',
       '?': 'tidak disebut'}
REF = {'pohon': 'hitungan tangan di pohon', 'panen': 'hasil panen', 'packhouse': 'hitungan di packhouse',
       'anotasi': 'foto/video beranotasi', 'tidak ada': 'tidak ada pembanding'}
MET = {'hitung': 'galat hitungan', 'identitas': 'metrik identitas (MOTA/IDF1/HOTA)', 'deteksi': 'metrik deteksi',
       'tidak ada': 'tidak ada'}
MOD = {'RGB': 'kamera warna (RGB)', 'MSI': 'multispektral', 'HSI': 'hiperspektral', 'TERMAL': 'termal',
       'DEPTH': 'kedalaman (depth)', 'LASER': 'laser', 'NIR': 'inframerah dekat', 'LIDAR': 'LiDAR',
       'STEREO': 'kamera stereo', 'RADAR': 'radar'}
KLS = {'-': 'tidak berlaku (tidak dihitung per kelas)'}
YN = {'Y': 'ya', 'N': 'tidak'}
JUDUL = {'Yes': 'lanjut ke tahap abstrak', 'Yes-C1': 'lanjut ke tahap abstrak, calon C1',
         'Yes-C3': 'lanjut ke tahap abstrak, calon C3', 'No': 'dikeluarkan',
         'lanjut': 'lanjut ke tahap abstrak', 'eksklusi': 'dikeluarkan'}


def kelompok(v):
    """'C1' -> 'C1 (hitung ...)'; 'X-E5' -> 'dikeluarkan, E5 (deteksi ...)'."""
    v = v.strip().replace('-', ' ')
    if not v:
        return ''
    if v.startswith('X'):
        e = v.split()[-1]
        return f'dikeluarkan, {e} ({EKS[e]})' if e in EKS else 'dikeluarkan'
    return KEL.get(v.split()[0], v)


def arti(v, peta, sep='+'):
    """Kode tunggal atau gabungan ('M2+M3') ditulis bersama artinya."""
    v = v.strip()
    if not v:
        return ''
    if peta is MEK or peta is AKU:
        return ' + '.join(f'{p} ({peta[p]})' if p in peta else p for p in (s.strip() for s in v.split(sep)))
    return ' + '.join(peta.get(p.strip(), p.strip()) for p in v.split(sep))


def kode(sel, peta=None):
    """Kebalikan kelompok()/arti(): sel lembar -> kode mentah."""
    sel = sel.strip()
    if not sel:
        return ''
    m = re.match(r'dikeluarkan, (E[1-7])', sel)
    if m:
        return 'X-' + m.group(1)
    if peta:
        balik = {b: a for a, b in peta.items()}
        if sel in balik:
            return balik[sel]
    return '+'.join(p.split(' (')[0].strip() for p in sel.split(' + '))
