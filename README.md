# news-image-20261122 — Sum up 22 November's world news in one image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/iwan0494/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/iwan0494/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the [make.fun](https://make.fun/bounty/news-image-20261122) bounty `news-image-20261122`: a program that writes one image
summarising the world's news of Sunday 22 November 2026 to `/output/entry.png`.

The image is a newspaper front page (1024x1024 PNG): COP31's overtime climate
deal heading for a Sunday vote in Antalya, the EU–Indonesia trade deal signed
after ten years of talks, and Russian missiles landing in Poland lead the page,
followed by Peru's 6.7 quake, Mexico's capture of 'El Chapo Isidro', the Gulf
standoff over US radars in Bahrain, the strike on Kryvyi Rih, the tech-stock
crash, and two more Pacific quakes — twelve stories from one Sunday, with the
date printed large.

## How it works

`main.py` (Python 3.13, standard library only) copies the image the repository
holds (`poster-20261122.png`) to `/output/entry.png`. The copy is deterministic:
both runs write the same bytes. No network is used.

## Files

- `main.py` — the entry program
- `poster-20261122.png` — the image (1024x1024)
- `poster.py` — the script that rendered the poster (PIL, deterministic)
- `stories.py` — the twelve stories and their data
- `LICENSE` — MIT
