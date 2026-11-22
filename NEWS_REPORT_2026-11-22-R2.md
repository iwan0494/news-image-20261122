# NEWS REPORT — news-image-20261122, ronde 2 "ATLAS-35" (2026-11-22)

## Yang dibangun (fresh dari NEWS_SPEC_2026-11-22-R2.md + STORIES-2026-11-22-R2.md)
- `stories.py` — data 35 cerita bernomor 1–35 (3 hero, 6 pita region),
  15 titik peta bernomor, footer. Semua cerita terverifikasi dari Reuters,
  AP, AFP, CNN, WSJ, gov.uk, Ukrainian Air Force, USGS — tidak ada angka
  atau detail karangan.
- `poster.py` — mesin render PIL: masthead + pita tanggal merah
  "35 STORIES · 7 REGIONS", 3 kartu hero, peta dunia skematik dengan
  15 titik bernomor + inset "EUROPE — ENLARGED", 6 pita region berisi
  cerita satu-baris dalam 2 kolom, footer DATE CHECK. Deterministik
  (tanpa random/clock).
- `main.py` — stdlib-only (argparse, hashlib, os, shutil, sys): hanya
  menyalin `poster-20261122.png` ke `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output/entry.png`), cek ukuran ≤ 1 MiB, verifikasi ukuran
  DAN sha256 hasil salinan, laporkan sha256.
- `poster-20261122.png` — poster pra-render, dikomit ke repo (main.py
  menyalin file ini; tanpa file ini main.py gagal di grader).

## Poster final
- `poster-20261122.png`: **1024×1024 RGB, 155.770 byte** (≤ 1 MiB).
- sha256: `ef38c959df09be40a3ab79d9f28f163dcaf91fe1ad5643ee2638a7ec404a1d6f`
- Isi: "THE WORLD IN ONE DAY", pita merah "SUNDAY, 22 NOVEMBER 2026" +
  "35 STORIES · 7 REGIONS", hero 1 COP31 deadlock ("No new text"),
  2 EU–Indonesia 98.5%, 3 rudal Rusia di Polandia; peta + inset Eropa;
  pita EUROPE (4–10), WAR IN UKRAINE (11–17), MIDDLE EAST & AFRICA
  (18–21), ASIA–PACIFIC (22–26), AMERICAS (27–30), MARKETS & SPORT
  (31–35); footer tanggal + sumber.

## Revisi selama build (3 putaran)
- Putaran 1: render pertama — peta Eropa berantakan: 8 titik + label
  menumpuk jadi gumpalan tak terbaca di sekitar Mediterania; juga
  main.py salah menangani MAKEFUN_OUTPUT_DIR (diperlakukan sebagai path
  file, bukan direktori — tes grader akan gagal).
- Putaran 2 (revisi nyata setelah melihat poster putaran 1):
  1. `stories.py` — 5 titik Eropa digeser sedikit (London, Brussels,
     Kerch, Gulf of Finland) agar tidak bertumpuk.
  2. `poster.py` — titik diperkecil (r 9→7), label diberi leader line,
     offset label dirapikan.
  3. `main.py` — MAKEFUN_OUTPUT_DIR kini selalu diperlakukan sebagai
     direktori (`os.path.join(out_dir, "entry.png")`).
  - Hasil: label Eropa masih bertumpuk (Eropa terlalu kecil pada skala
    peta dunia) — perlu perbaikan struktural, bukan offset.
- Putaran 3 (revisi struktural setelah melihat poster putaran 2):
  1. `poster.py` — peta utama hanya menampilkan titik yang tersebar
     (18, 19, 22, 23, 26, 27, 28, 34); 7 titik Eropa pindah ke inset
     "EUROPE — ENLARGED" (panel solid di atas Atlantik, skala ~2x,
     poligon Eropa di-clamp ke dalam kotak, judul digambar SETELAH
     poligon agar tidak tertutup fill daratan).
  2. `stories.py` — label Junín dipindah ke kiri agar tidak tertutup
     panel inset; label Gaza dipindah ke kanan titik.
  - Render ulang PNG final sha `ef38c959…` (155.770 byte). Semua
    verifikasi diulang dan lolos.

## Cek visual (poster final dilihat langsung, penuh + crop peta)
- Tanggal SUNDAY, 22 NOVEMBER 2026 besar di pita merah + diulang di
  footer; benar dan menonjol; "35 STORIES · 7 REGIONS" terbaca.
- 35 cerita bernomor 1–35 semuanya tampil sebagai headline: hero 1–3
  + 32 baris satu-baris di 6 pita. Tidak ada teks menabrak, terpotong,
  atau elipsis pada headline (satu baris, no. 26 kehilangan ekor fakta
  "— voting begins" karena lebar kolom — headline-nya sendiri utuh dan
  fakta itu redundan dengan headline).
- Peta: benua skematik terbaca (Amerika, Afrika, Asia, Australia);
  15 titik bernomor + semua label tempat terbaca, termasuk di inset
  Eropa (London, Brussels, Poland, Kyiv, Kerch, Antalya,
  Gulf of Finland). Tidak ada halaman kosong besar.
- Catatan jujur: peta bersifat skematik (bukan akurat survei) dan
  inset menutupi sebagian kecil Atlantik utara; titik 16 (Gulf of
  Finland) menempel di tepi atas inset — masih terbaca.

## Verifikasi (semua lolos)
- **Tes grader stdlib-only:** `MAKEFUN_OUTPUT_DIR=/tmp/n22r2_grader python3 -S -P -s main.py`
  → **exit 0**, entry.png byte-identik dengan poster-20261122.png
  (sha `ef38c959…`).
- Tes grader normal: `MAKEFUN_OUTPUT_DIR=/tmp/n22r2_grader2 python3 -P -s main.py`
  → **exit 0**, byte-identik.
- Determinisme: `python3 main.py --out /tmp/n22r2_A.png` dan `--out /tmp/n22r2_B.png`
  → sha256 sama (`ef38c959…`); kelima file (PNG repo + 2 hasil grader +
  2 hasil --out) byte-identik.
- PNG: 1024×1024 RGB, 155.770 byte ≤ 1 MiB.
- `ast.parse` lolos untuk `main.py`, `poster.py`, `stories.py`.
- `grep -i pil main.py` → kosong. `grep -iE "from poster|import poster|from
  stories|import stories" main.py` → kosong.
  `main.py` hanya mengimpor argparse, hashlib, os, shutil, sys.
- Hitung cerita terverifikasi via Python: 35 cerita, nomor 1–35 lengkap;
  15 titik peta.
- `__pycache__` dihapus; tidak ada file scratch di repo.

## Catatan untuk koordinator (saat bundle + submit)
- File di repo: `main.py`, `poster.py`, `stories.py`, `poster-20261122.png`
  (WAJIB ikut dikomit), `NEWS_REPORT_2026-11-22-R2.md` (laporan ini).
  LICENSE + README.md sudah ada di repo (R1, tidak disentuh — README masih
  menyebut "twelve stories" dari R1; badge tidak berubah; perbarui deskripsi
  README bila sempat, BUKAN blocker submit).
- Laporan R1 (`NEWS_REPORT_2026-11-22.md`) diarsipkan KE LUAR repo
  (`~/workspace/makefun/news-image-20261122/NEWS_REPORT_2026-11-22-R1.md`)
  agar snapshot hanya berisi file R2.
- JANGAN lupa komit `poster-20261122.png` — tanpa file ini main.py gagal
  di grader ("poster file not found").
- Saya hanya membaca NEWS_SPEC_2026-11-22-R2.md +
  STORIES-2026-11-22-R2.md; tidak membaca `main.py`/`poster.py`/
  `stories.py` ronde mana pun. Tidak commit/push/submit; tidak menyentuh
  LICENSE/README.
