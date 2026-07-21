"""Turunkan peta kedalaman 16-bit ke 8-bit.

Pemuat pelatihan 4-kanal toh mengonversi ke 8-bit, jadi presisi 16-bit tidak
terpakai di jalur mana pun yang masih aktif -- tetapi memakan 4x ruang disk.
"""
import sys, cv2, numpy as np
from pathlib import Path
sh, n = int(sys.argv[1]), int(sys.argv[2])
files = sorted(Path("depth_da3/depth").glob("*.png"))
files = [f for i, f in enumerate(files) if i % n == sh]
c = 0
for f in files:
    im = cv2.imread(str(f), cv2.IMREAD_UNCHANGED)
    if im is None or im.dtype == np.uint8:
        continue
    cv2.imwrite(str(f), (im.astype(np.float32) / 65535.0 * 255).astype(np.uint8))
    c += 1
print(f"shard {sh}: {c} dikonversi")
