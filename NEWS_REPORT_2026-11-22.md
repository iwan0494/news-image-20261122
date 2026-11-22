# NEWS REPORT — news-image-20261122, ronde 1 (2026-11-22)

## Yang dibangun (fresh dari NEWS_SPEC_2026-11-22.md + STORIES-2026-11-22.md)
- `stories.py` — data 12 cerita bernomor 1–12 (3 fitur, 8 ubin, 1 brief),
  4 statistik, 4 butir ALSO ON, daftar 12 lokasi, footer. Semua cerita
  terjadi atau pertama kali dilaporkan pada Minggu 22 November 2026.
- `poster.py` — mesin render PIL: masthead + pita tanggal merah, strip
  statistik, 3 panel fitur dengan ilustrasi primitif (globe iklim,
  dokumen dagang, rudal), grid 8 ubin dengan ikon primitif, kolom ALSO ON
  + WHERE IT HAPPENED, footer DATE CHECK. Deterministik (tanpa
  random/clock).
- `main.py` — stdlib-only (argparse, hashlib, os, shutil, sys): hanya
  menyalin `poster-20261122.png` ke `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output/entry.png`), cek ukuran ≤ 1 MiB, verifikasi ukuran
  DAN sha256 hasil salinan, laporkan sha256.
- `poster-20261122.png` — poster pra-render, dikomit ke repo (main.py
  menyalin file ini; tanpa file ini main.py gagal di grader).

## Poster final
- `poster-20261122.png`: **1024×1024 RGB, 145.632 byte** (≤ 1 MiB).
- sha256: `1cccf9fe78cf0868e611357f617bc2be3214dba03ccb71759fdbb45c3425d4ea`
- Isi: "THE WORLD IN ONE DAY", pita merah "SUNDAY, 22 NOVEMBER 2026",
  subhead, strip "98.5% / 6.7 / $5M / 2", fitur 1 COP31 overtime Antalya,
  2 EU–Indonesia trade deal 98.5%, 3 rudal Rusia di Polandia, ubin 4
  gempa Peru 6.7, 5 'El Chapo Isidro' ditangkap, 6 IRGC klaim serang
  radar AS di Bahrain, 7 serangan Kryvyi Rih, 8 tech crash, 9 Trump
  ancam pajak AI, 10 gempa Myanmar 4.1, 11 gempa Timor-Leste 6.8,
  brief 12 drone bakar kapal Rusia di Teluk Finlandia; ALSO ON
  (Hong Kong, Ethiopia–Eritrea, UN autonomous weapons, Sudan Bau);
  WHERE IT HAPPENED 1–12; footer tanggal + sumber.

## Revisi selama build (2 putaran)
- Putaran 1: render pertama — ditemukan 5 cacat visual: (a) angka strip
  statistik menumpuk dengan label + sub-label; (b) subhead menabrak garis
  pemisah; (c) body fitur meluber dan menabrak baris fakta + baris tempat
  ganda di bawah panel; (d) ikon ubin menabrak headline (ubin 6, 7);
  (e) body ubin 5, 6, 7, 8, 11 terpotong kalimatnya (hanya 2 dari 3 baris
  tergambar); (f) body brief 12 menabrak garis footer merah.
- Putaran 2 (revisi nyata setelah melihat poster putaran 1):
  1. `stories.py` — 3 body fitur dipendekkan jadi 3 baris; 5 body ubin
     dipendekkan jadi ≤2 baris kalimat utuh (5, 6, 7, 8, 11); body brief
     12 jadi 1 baris.
  2. `poster.py` — posisi angka/label/sub statistik dipisah (126/158/175);
     subhead naik + garis ke y120; ikon fitur dikecilkan (62→50) dan
     headline/body digeser ke atas, fakta hanya 1 baris di y1-26, baris
     tempat ganda di bawah panel dihapus; headline ubin mulai y+40 (di
     bawah baris ikon); tinggi baris ubin 158→156; bawah dipadatkan
     (divider 804, bullet step 18, brief 1 baris).
  3. `main.py` — tambah verifikasi sha256 salinan vs sumber (sebelumnya
     hanya ukuran).
  - Render ulang PNG final sha `1cccf9fe…` (145.632 byte). Semua verifikasi
    diulang dan lolos.

## Cek visual (poster final dilihat langsung, penuh)
- Tanggal SUNDAY, 22 NOVEMBER 2026 besar di pita merah + diulang di
  footer; benar dan menonjol.
- 12 cerita bernomor 1–12 semuanya tampil sebagai headline: fitur 1–3,
  ubin 4–11, dan baris "12. Drones set Russian ship ablaze in the Gulf
  of Finland" di bawah ALSO ON; daftar WHERE IT HAPPENED 1–12 konsisten.
- Tidak ada teks menabrak, terpotong, atau elipsis; tidak ada halaman
  kosong besar; semua label tempat terbaca; ikon ubin muat di kotaknya.

## Verifikasi (semua lolos)
- **Tes grader stdlib-only:** `MAKEFUN_OUTPUT_DIR=/tmp/n22_grader python3 -S -P -s main.py`
  → **exit 0**, entry.png byte-identik dengan poster-20261122.png
  (sha `1cccf9fe…`).
- Tes grader normal: `MAKEFUN_OUTPUT_DIR=/tmp/n22_grader2 python3 -P -s main.py`
  → **exit 0**, byte-identik.
- Determinisme: `python3 main.py --out /tmp/n22_A.png` dan `--out /tmp/n22_B.png`
  → sha256 sama (`1cccf9fe…`); kelima file (PNG repo + 2 hasil grader +
  2 hasil --out) byte-identik.
- PNG: 1024×1024 RGB, 145.632 byte ≤ 1 MiB.
- `ast.parse` lolos untuk `main.py`, `poster.py`, `stories.py`.
- `grep -i pil main.py` → kosong (exit 1). `grep -iE "from poster|import poster|from stories|import stories" main.py` → kosong (exit 1).
  `main.py` hanya mengimpor argparse, hashlib, os, shutil, sys.
- `__pycache__` dihapus; tidak ada file scratch di repo.

## Catatan untuk koordinator (saat bundle + submit)
- File di repo: `main.py`, `poster.py`, `stories.py`, `poster-20261122.png`
  (WAJIB ikut dikomit), `NEWS_REPORT_2026-11-22.md` (laporan ini).
  LICENSE + README.md sudah ada di repo (dibuat koordinator, tidak disentuh).
- JANGAN lupa komit `poster-20261122.png` — tanpa file ini main.py gagal
  di grader ("poster file not found").
- Saya hanya membaca NEWS_SPEC_2026-11-22.md + STORIES-2026-11-22.md;
  tidak membaca file bounty news-image lain apa pun. Tidak commit/push/
  submit; tidak menyentuh LICENSE/README.
