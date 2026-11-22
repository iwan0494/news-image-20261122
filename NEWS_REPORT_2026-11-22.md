# NEWS REPORT — news-image-20261122, ronde 3 + perbaikan (2026-11-22)

## Entri
- Bounty: make.fun `news-image-20261122` — "Sum up 22 November's world
  news in one image". Deadline 24 Nov 2026 07:00 WIB.
- Konsep R3 (perintah Iwan 21:19 WIB): 7 berita PALING HIT, tiap berita
  HEADLINE BESAR + TAGLINE satu kalimat yang menjelaskan headline.
- Repo: https://github.com/iwan0494/news-image-20261122 (HEAD saat ini
  commit R2 533486c; perbaikan ini belum di-commit — koordinator yang
  commit/push/submit).

## Isi poster (7 cerita, sesuai STORIES-R3-2026-11-22.md)
1. LEAD — IRAN STRIKES US BASES IN BAHRAIN (CLAIM, Reuters / Bahrain
   officials) — 2 radar Patriot.
2. NATO VOWS TO DEFEND EVERY INCH OF POLAND (CONFIRMED, Polish
   prosecutors / NATO) — Kh-101.
3. COP31 IN OVERTIME — THE FIGHT IS OVER TWO WORDS (CONFIRMED,
   Reuters / AP) — 35% listrik 2035.
4. STOCKS IN CORRECTION AS TECH ROUT DEEPENS (CONFIRMED, Market
   wires) — S&P 500 -3,7%.
5. EU AND INDONESIA SIGN LANDMARK TRADE DEAL (CONFIRMED, European
   Commission / DW) — 98,5% tarif hilang.
6. MEXICO CAPTURES FBI MOST-WANTED 'EL CHAPO ISIDRO' (CONFIRMED,
   AP / FBI) — hadiah $5 juta.
7. PERU QUAKE 6.7 SHAKES THE ANDES (CONFIRMED, USGS) — 15 luka,
   127 rumah rusak.
- Stat strip: 2 RADARS | KH-101 | -3,7% | 98,5%. Kotak merah DATE CHECK
  (press time Minggu 22 Nov 2026 sore UTC + yang sengaja dibuang).
  Footer: tanggal + "Also Sunday" + sumber.

## Perbaikan (fix) — satu-satunya perubahan ronde ini
- CACAT: di poster R3, baris sumber panel 6 ("AP / FBI") dan panel 7
  ("USGS") duduk tepat di garis bawah panel — tinta huruf (y 897-906)
  menyeberangi garis batas panel (y 904), sehingga huruf terlihat
  terpotong setengah. Penyebab: baris 4 (y 736-904, tinggi 168px)
  26px lebih pendek dari baris 2-3 tapi memuat teks yang sama banyak.
  Terkonfirmasi visual: crop 4x sebelum perbaikan menunjukkan garis
  panel memotong bagian bawah huruf "AP / FBI" dan "USGS".
- PERBAIKAN (hanya poster.py, fungsi row_panel; isi cerita/headline/
  tagline/sumber TIDAK diubah): row 4 kini memakai mode `tight` —
  strip ikon 36->32px, celah kicker-ke-headline 17->14px, spasi
  headline 2->1px, jeda tagline 2->1px, spasi tagline 3->2px, jeda
  sumber 3->2px. Baris sumber naik ~13px (y 894 -> 881); tinta huruf
  berakhir y 893, 11px di atas garis bawah panel (y 904). Baris 2-3
  dan lead TIDAK disentuh (metrik default dipertahankan).
- Juga dicatat di docstring poster.py sebagai "Revision 3 (fix)".

## Poster final
- `poster-20261122.png`: 1024x1024 RGB, 201.643 byte (<= 1 MiB)
- sha256: d6113ac4a1299eaa537ee7bf6055343639ceee09f0d6df28c6e3b1a7dcb0515b

## Verifikasi — semua lolos
- Tes grader stdlib-only
  `MAKEFUN_OUTPUT_DIR=/tmp/n22r3f_grader python3 -S -P -s main.py`:
  exit 0, entry.png byte-identik dengan poster repo.
- Tes grader normal
  `MAKEFUN_OUTPUT_DIR=/tmp/n22r3f_grader2 python3 -P -s main.py`:
  exit 0, byte-identik.
- Determinisme: 2 run `--out` berbeda + 2 run grader + PNG repo =
  5 file, semua sha256 d6113ac4… (sama).
- PNG: 1024x1024 RGB, 201.643 byte <= 1.048.576.
- `grep -i pil main.py` = 0; `grep -iE "from poster|import poster|
  from stories|import stories" main.py` = 0.
- `ast.parse` lolos untuk main.py, poster.py, stories.py.
- Tidak ada `__pycache__` / file scratch di repo.

## Cek visual (poster dilihat langsung + zoom 4x panel 6 dan 7)
- Panel 6: "AP / FBI" utuh, duduk penuh di dalam panel dengan ruang
  kertas jelas di bawahnya sebelum garis batas — TIDAK terpotong lagi.
- Panel 7: "USGS" utuh, sama bersihnya.
- Panel lain sekilas: sumber cerita 2 ("Polish prosecutors / NATO"),
  3 ("Reuters / AP"), 4 ("Market wires"), 5 ("European Commission /
  DW") dan sumber lead ("Reuters / Bahrain officials") semuanya di
  dalam panel; 7 cerita bernomor 1-7; headline besar terbaca; DATE
  CHECK terbaca; tanggal "SUNDAY, 22 NOVEMBER 2026" besar dan benar;
  tidak ada teks menabrak/terpotong; tidak ada halaman kosong besar.

## Yang belum dilakukan (koordinator)
- Commit + push + submit (bukan tugas fix ini).
