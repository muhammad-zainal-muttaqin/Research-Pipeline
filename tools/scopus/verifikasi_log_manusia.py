"""Buat verifikasi/log_perubahan.csv (bahasa biasa) dari verifikasi/.teknis/log_perubahan.csv.

Log teknis dipakai skrip penerap untuk mencegah pencatatan ganda. Log manusia dapat dibaca
tanpa berkas lain: artikel disebut dengan penulis dan judul, kode diterjemahkan, dan
alasan memuat alasan sebenarnya, bukan nama proses.

    python3 tools/scopus/verifikasi_log_manusia.py
"""
import csv, re
from pathlib import Path

from verifikasi_istilah import AKU, EKS, KEL, KLS, LOK, MEK, MET, REF, TUGAS, YN, kelompok

ROOT = Path(__file__).resolve().parents[2]
B = ROOT / 'literature/scopus-2026-09'
VER = B / 'verifikasi'
TEK = VER / '.teknis'
SRC = TEK / 'log_perubahan.csv'
OUT = VER / 'log_perubahan.csv'


def baca(p, enc='utf-8'):
    return list(csv.DictReader(open(p, encoding=enc)))


rec = {r['idx']: r for r in baca(B / 'topik/records_all.csv')}
tamb = {r['key']: r for r in baca(B / 'topik/tambahan_metode_lain.csv')}
adj = {r['idx']: r['alasan'] for r in baca(TEK / 'ajudikasi_cek1.csv', 'utf-8-sig')}
c1 = {r['idx']: r['alasan'] for r in baca(TEK / 'label_c1.csv')}
c3 = {r['idx']: r['alasan'] for r in baca(TEK / 'label_c3.csv')}

W = r'\b'
OLEH = {'AI-2': 'AI, disetujui peninjau', 'AI-Tugas': 'AI, disetujui peninjau', 'AI-Cek1': 'AI, disetujui peninjau',
        'peninjau': 'peninjau', 'Fatma': 'Bu Fatma'}


def gabung(peta, sep='+'):
    return lambda v: ' + '.join(peta.get(p.strip(), p.strip()) for p in v.split(sep))


def terjemah(a):
    a = re.sub(r'\bX[ -](E[1-7])\b', lambda m: f'dikeluarkan ({EKS[m.group(1)]})', a)
    a = re.sub(r'[Dd]ikeluarkan dikeluarkan', 'dikeluarkan', a)
    a = re.sub(W + r'(E[1-7])' + W, lambda m: f'{m.group(1)} ({EKS[m.group(1)]})', a)
    a = re.sub(W + r'(M[0-5])' + W, lambda m: f'{m.group(1)} ({MEK[m.group(1)]})', a)
    a = re.sub(W + r'(C[1-5])' + W, lambda m: KEL[m.group(1)], a, count=1)
    a = re.sub(W + r'(KLS|DET|HIT|LF|MUTU|SENSOR)' + W, lambda m: TUGAS[m.group(1)], a)
    a = re.sub(W + r'(POHON|TANAH|PABRIK)' + W, lambda m: LOK[m.group(1)], a)
    a = re.sub(r'(PER[ _]KELAS|[Pp]er_kelas|[Pp]er kelas|MULTIPANDANG|[Mm]ultipandang)( diisi |[ =])([YN])' + W,
               lambda m: ('per kelas' if 'kelas' in m.group(1).lower() else 'difoto lebih dari sekali')
               + ' = ' + YN[m.group(3)], a)
    a = re.sub(r'([Aa]kuisisi)( diisi |[ =])([VDST1])' + W, lambda m: 'cara foto diambil = ' + AKU[m.group(3)], a)
    a = re.sub(W + r'(multipandang|MULTIPANDANG)' + W, 'banyak pandang', a)
    a = re.sub(r'aturan \d\.\d[a-z]?(, )?', '', a)
    a = re.sub(r'\s*\(\)', '', a)
    a = a.replace('mekanisme=', 'cara penghubungan = ').replace('akuisisi=', 'cara foto diambil = ')
    a = a.replace('per_kelas=', 'per kelas = ').replace('teks_lengkap', 'teks lengkap')
    a = re.sub(r'= ([VDST1])\b', lambda m: '= ' + AKU[m.group(1)], a)
    a = re.sub(r'(per kelas) = ([YN])\b', lambda m: m.group(1) + ' = ' + YN[m.group(2)], a)
    return a


def bersih(a, utama=()):
    a = a.strip()
    for pola in (r'ajudikasi_cek1\.csv; (.*)', r'diperiksa (?:ulang )?agen utama\)[^:]*: (.*)',
                 r'^baris dihapus: rekaman keluar dari C\d \((.*)\)$', r'usul_kode_ulang_C1\.csv\)\. (.*)'):
        m = re.search(pola, a, re.S)
        if m:
            a = m.group(1)
    m = re.search(r'dasar: [^;]+; (.*?)(?: Penyanggah:.*)?$', a, re.S)
    if m:
        a = m.group(1)
    a = re.sub(r'^(Putaran (kedua|2|pertama|1)|Kedua putaran|Tidak ada putaran)[^.:]*[.:]\s*', '', a)
    a = re.sub(r'diputuskan model atas butir [^;]*; ', '', a)
    a = re.sub(r'Kode ulang (Sonnet|Haiku|Opus) [\d.]+', 'Dibaca ulang', a)
    a = re.sub(r'\s*\(aturan [a-z]\)', '', a)
    a = re.sub(r' (pada|menurut) aturan( operasional)? [a-z]' + W, '', a)
    a = re.sub(W + r'aturan [a-z]' + W, 'aturan', a)
    for l, b in (('putaran pertama', 'keputusan awal'), ('Putaran pertama', 'Keputusan awal'),
                 ('putaran 1', 'keputusan awal'), ('Putaran 1', 'Keputusan awal'),
                 ('putaran kedua', 'pemeriksaan ulang'), ('Putaran kedua', 'Pemeriksaan ulang'),
                 ('putaran 2', 'pemeriksaan ulang'), ('Putaran 2', 'Pemeriksaan ulang')):
        a = a.replace(l, b)
    a = re.sub(r'\b(hlm|h|hal|Gbr|No|dkk)\. ', lambda m: m.group(1) + '.§', a)
    kal = [k.replace('§', ' ') for k in re.split(r'(?<=[.!?])\s+', a)
           if k and not re.search(r'[Pp]aket|verbatim|[Kk]utipan|sepakat|penengah|Label C3|[Pp]engode|'
                                  r'[Pp]embaca [AB]|Haiku|Sonnet|Opus|Belum dibaca peninjau|tidak diubah\.$|'
                                  r'putaran|pdftoppm|Read tanpa|null|teks_lengkap|dikutip|[Kk]eyakinan (sedang|rendah) karena', k)]
    if not kal:  # semua kalimat bermuatan proses: pakai yang paling sedikit memuatnya
        a = re.sub(r'( (dari|oleh|yang diusulkan))?\s*\(?(kedua )?[Pp]engode( [AB])?\)?', '', a)
        a = re.sub(r'\s*verbatim', '', a)
        kal = [k.replace('§', ' ') for k in re.split(r'(?<=[.!?])\s+', a)
               if k and not re.search(r'[Pp]aket|pdftoppm|Haiku|Sonnet|Opus|Read tanpa|null|hanya membaca judul', k)]
    if utama:
        kal.sort(key=lambda k: not any(u in k.lower() for u in utama))
    a = ' '.join(kal[:2])
    a = re.sub(r'\S+/\S+\.(csv|txt|md|json)\S*', '', a)
    a = re.sub(r'\s*\(?(paket|Paket) K\d+\)?', '', a)
    return terjemah(a).strip(' ;')


KUNCI = {'mekanisme': ['mekanisme', 'lacak', 'asosiasi', 'pelacak'], 'akuisisi': ['akuisisi', 'video', 'pandang', 'foto'],
         'per_kelas': ['kelas'], 'tugas': ['tugas'], 'lokasi': ['lokasi', 'tempat'], 'modalitas': ['modalitas', 'sensor', 'kamera'],
         'multipandang': ['multipandang', 'sudut', 'sisi', 'kali', 'frame'], 'referensi_hitung': ['acuan', 'dibandingkan', 'hitungan'],
         'tingkat_metrik': ['metrik', 'mota', 'idf1', 'galat'], 'halaman': ['tabel', 'bagian', 'hal'],
         'cara_kelas': ['kelas'], 'sumber_kode': ['teks lengkap', 'abstrak']}

# kolom teknis -> (yang diubah, penerjemah nilai)
NAMA = {
    'kode': ('Kelompok artikel', kelompok),
    'keputusan_judul': ('Keputusan di tahap judul', lambda v: {'X': 'dikeluarkan', 'I': 'lolos ke tahap abstrak'}.get(v, v)),
    'keputusan_manusia': ('Keputusan peninjau pada sampel acak',
                          lambda v: {'Yes': 'masuk', 'No': 'keluar'}.get(v) or kelompok(v)),
    'alasan': ('Alasan dikeluarkan', lambda v: f'{v} ({EKS[v]})' if v in EKS else v),
    'dasar_keputusan': ('Dasar keputusan', lambda v: v),
    'mekanisme': ('Cara memastikan buah tidak terhitung dua kali', gabung(MEK)),
    'akuisisi': ('Cara foto diambil', gabung(AKU)),
    'per_kelas': ('Hitungan per kelas', lambda v: YN.get(v, v)),
    'hasil_ringkas': ('Ringkasan hasil artikel', lambda v: v),
    'sumber_kode': ('Keterangan artikel dibaca dari', lambda v: v),
    'halaman': ('Letak bukti di artikel', lambda v: 'hanya judul; abstrak dan teks lengkap tidak dapat dibaca'
                if re.search(r'pdftoppm|null', v) and not v.startswith('Abstrak') else '; '.join(
        p.strip() for p in re.sub(r'\s*\([^)]*paket[^)]*\)', '', v.replace('Judul paket', 'Judul')).split(';')
        if not re.search(r'paket|Paket|sumber:|/', p))),
    'referensi_hitung': ('Hitungan artikel dibandingkan dengan', gabung(REF, ';')),
    'tingkat_metrik': ('Jenis angka yang dilaporkan artikel', gabung(MET, ';')),
    'cara_kelas': ('Cara kelas tiap buah ditetapkan', lambda v: KLS.get(v, v)),
    'berubah': ('Label berubah setelah dibaca ulang',
                lambda v: 'ya, sebelumnya ' + terjemah(re.search(r'lama: (.*)\)', v).group(1))
                if v.startswith('ya (') else v),
    'tugas': ('Tugas artikel sawit', lambda v: TUGAS.get(v, v)),
    'lokasi': ('Tempat foto tandan diambil', lambda v: LOK.get(v, v)),
    'modalitas': ('Jenis kamera/sensor', lambda v: {'?': 'tidak disebut'}.get(v, v)),
    'multipandang': ('Tandan difoto lebih dari sekali', lambda v: YN.get(v, v)),
    'berkas': ('Berkas PDF artikel', lambda v: v),
}


def ubah(x):
    """Kembalikan (yang diubah, sebelum, sesudah)."""
    k, lama, baru, f = x['kolom'], x['nilai_lama'].strip(), x['nilai_baru'].strip(), x['berkas']
    if k == 'baris':
        if 'tambahan_metode_lain' in f:
            return 'Kelompok artikel', 'tidak ada di hasil pencarian Scopus', \
                KEL[baru.split()[-1]] + ', ditemukan di daftar pustaka'
        daftar = KEL['C1' if 'mekanisme_C1' in f else 'C3']
        if baru.startswith('(dihapus'):
            return f'Keberadaan di daftar {daftar}', 'ada di daftar', 'dihapus dari daftar'
        return f'Keberadaan di daftar {daftar}', 'tidak ada di daftar', 'ditambahkan ke daftar'
    nama, tr = NAMA[k]
    if k == 'kode' and lama == '' and f.endswith('abstrak_U00.txt'):
        lama = 'X (judul)'
    s = 'belum diisi' if lama == '' else tr(lama)
    if baru == '' and ('mekanisme_C1' in f or 'kode_C3' in f):
        t = 'dihapus karena artikel keluar dari daftar'
    elif baru == '' and k == 'alasan':
        t = 'tidak ada (artikel kini masuk)'
    else:
        t = 'belum diisi' if baru == '' else tr(baru)
    if k == 'kode' and lama == 'X (judul)':
        s = 'dikeluarkan di tahap judul'
    return nama, s, t


def alasan(x):
    a, key, k = x['alasan'], x['idx_atau_key'], x['kolom']
    utama = tuple(KUNCI.get(k, []))
    if a == 'putaran kedua (AI-2)':
        return 'Keterangan baru yang diisi saat artikel dibaca ulang.' if x['nilai_lama'] == '' \
            else 'Diperbarui saat artikel dibaca ulang.'
    if a.startswith('putaran kedua menemukan abstrak'):
        return 'Abstrak atau teks lengkap ditemukan kemudian; keputusan tidak berubah.'
    if a.startswith('isian model, bukan bacaan peninjau: dua pembaca') and key in c1:
        return bersih(c1[key], utama)
    if a.startswith('label C3 dikode ulang') and key in c3:
        return bersih(c3[key], utama)
    if a.startswith('ajudikasi ketidaksepakatan') and not re.search(r'ajudikasi_cek1\.csv; ', a) and key in adj:
        return bersih(adj[key])
    if k == 'baris' and key in ALASAN_KODE:
        m = re.search(r'\(dihapus; (.*?)\)?$', x['nilai_baru'])
        awal = terjemah(m.group(1)) + '. ' if m and ':' not in m.group(1) else ''
        return awal + ALASAN_KODE[key]
    if a.startswith('keputusan butir verifikasi diserahkan') and k == 'baris':
        m = re.search(r'\(dihapus; (.*)\)$', x['nilai_baru'])
        return terjemah(m.group(1)) if m else ''
    if key in tamb and k == 'baris':
        return bersih(tamb[key].get('catatan', ''))
    if a == 'butir 4.4':
        return 'Berkas PDF sebelumnya berisi artikel lain; diganti dengan artikel yang benar dan teksnya diekstrak ulang.'
    return bersih(a, utama)


def artikel(key):
    if key == 'kang2022accurate':
        return 'Kang H. (2022). Accurate Fruit Localisation for Robotic Harvesting using High Resolution LiDAR-Camera Fusion'
    r = rec.get(key) or tamb.get(key)
    return f"{r['first_author'].strip()} ({r['year']}). {r['title']}" if r else key


def kalimat(s):
    s = s.strip()
    return s[0].upper() + s[1:] + ('' if s.endswith('.') else '.') if s else ''


matriks = baca(B / 'topik/bukti/matriks_bukti.csv')
KINI = {r['idx']: r['kode'] for r in matriks} | {r['key']: r['kode'] for r in matriks} \
    | {k: r['kode'] for k, r in tamb.items()}


def kelompok_sekarang(key):
    k = KINI.get(key)
    return KEL[k] if k else 'dikeluarkan'


# Baris yang menentukan masuk-tidaknya artikel atau kelompoknya; ditaruh paling atas.
KEANGGOTAAN = ('Kelompok artikel', 'Alasan dikeluarkan', 'Keputusan di tahap judul',
               'Keputusan peninjau pada sampel acak', 'Keberadaan di daftar')

KOLOM = ['tanggal', 'artikel', 'kelompok_sekarang', 'yang_diubah', 'sebelum', 'sesudah', 'alasan', 'diubah_oleh']
log = baca(SRC)
ALASAN_KODE = {}  # alasan perubahan kelompok, dipakai juga untuk baris daftar C1/C3 artikel yang sama
for x in log:
    if x['kolom'] == 'kode':
        ALASAN_KODE[x['idx_atau_key']] = alasan(x)
baris = []
for i, x in enumerate(log):
    nama, s, t = ubah(x)
    a = artikel(x['idx_atau_key'])
    atas = nama.startswith(KEANGGOTAAN)
    urut = (0, a.lower(), x['tanggal'], i) if atas else (1, i)
    baris.append((urut, [x['tanggal'], a, kelompok_sekarang(x['idx_atau_key']), nama, s, t,
                         kalimat(alasan(x)), OLEH.get(x['oleh'], x['oleh'])]))
baris.sort(key=lambda b: b[0])
with open(OUT, 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(KOLOM)
    w.writerows(b[1] for b in baris)
n_atas = sum(1 for b in baris if b[0][0] == 0)
print(f'{len(log)} baris ditulis ke {OUT.relative_to(ROOT)}; {n_atas} baris keanggotaan di atas')
