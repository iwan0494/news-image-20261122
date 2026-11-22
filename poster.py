"""Render the 22 November 2026 world-news poster (1024x1024 RGB).

Deterministic: no randomness, no system clock, no time metadata.
Run: python3 poster.py  -> writes poster-20261122.png next to this file.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

import stories

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "poster-20261122.png")

PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
GREY = (110, 108, 100)
LINE = (190, 186, 174)
SOFT = (238, 233, 220)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 46)
F_DATE = font("DejaVuSans-Bold.ttf", 30)
F_SUB = font("DejaVuSans.ttf", 15)
F_STAT_NUM = font("DejaVuSans-Bold.ttf", 30)
F_STAT_LBL = font("DejaVuSans-Bold.ttf", 14)
F_STAT_SUB = font("DejaVuSans.ttf", 12)
F_NUM = font("DejaVuSans-Bold.ttf", 40)
F_KICK = font("DejaVuSans-Bold.ttf", 13)
F_HEAD = font("DejaVuSans-Bold.ttf", 21)
F_BODY = font("DejaVuSans.ttf", 14)
F_FACT = font("DejaVuSans-Bold.ttf", 14)
F_PLACE = font("DejaVuSans.ttf", 12)
F_TNUM = font("DejaVuSans-Bold.ttf", 17)
F_THEAD = font("DejaVuSans-Bold.ttf", 16)
F_TBODY = font("DejaVuSans.ttf", 13)
F_TPLACE = font("DejaVuSans.ttf", 11)
F_SECT = font("DejaVuSans-Bold.ttf", 15)
F_BULLET = font("DejaVuSans.ttf", 13)
F_BRIEF_H = font("DejaVuSans-Bold.ttf", 14)
F_BRIEF_B = font("DejaVuSans.ttf", 12)
F_FOOT = font("DejaVuSans-Bold.ttf", 13)
F_SRC = font("DejaVuSans.ttf", 11)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to the given pixel width."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, step, fill=INK):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


# ---------------------------------------------------------------- icons

def icon(draw, kind, cx, cy, s, col=NAVY):
    """Small primitive icon centred at (cx, cy), size s."""
    r = s / 2.0
    if kind == "globe":
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=3)
        draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
                     outline=col, width=2)
        draw.line([cx - r, cy, cx + r, cy], fill=col, width=2)
    elif kind == "trade":
        draw.rectangle([cx - r, cy - r * 0.5, cx - r * 0.1, cy + r * 0.5],
                       outline=col, width=3)
        draw.rectangle([cx + r * 0.1, cy - r * 0.5, cx + r, cy + r * 0.5],
                       outline=RED, width=3)
        draw.line([cx - r, cy + r * 0.8, cx + r, cy + r * 0.8],
                  fill=col, width=3)
        draw.polygon([(cx + r, cy + r * 0.8), (cx + r * 0.6, cy + r * 0.5),
                      (cx + r * 0.6, cy + r * 1.1)], fill=col)
    elif kind == "missile":
        draw.polygon([(cx - r * 0.7, cy + r * 0.3), (cx + r * 0.8, cy - r * 0.8),
                      (cx + r * 0.3, cy + r * 0.7)], fill=col)
        draw.polygon([(cx - r * 0.7, cy + r * 0.3), (cx - r, cy + r * 0.9),
                      (cx - r * 0.3, cy + r * 0.7)], fill=RED)
        draw.line([cx - r * 0.9, cy + r * 0.9, cx - r * 0.2, cy + r * 0.2],
                  fill=GREY, width=2)
    elif kind == "quake":
        pts = [(cx - r, cy - r * 0.2), (cx - r * 0.5, cy + r * 0.4),
               (cx, cy - r * 0.4), (cx + r * 0.5, cy + r * 0.3),
               (cx + r, cy - r * 0.3)]
        draw.line(pts, fill=col, width=3, joint="curve")
        draw.line([cx - r, cy - r * 0.7, cx + r, cy - r * 0.7],
                  fill=RED, width=2)
    elif kind == "cuffs":
        draw.ellipse([cx - r, cy - r * 0.55, cx - r * 0.1, cy + r * 0.55],
                     outline=col, width=3)
        draw.ellipse([cx + r * 0.1, cy - r * 0.55, cx + r, cy + r * 0.55],
                     outline=col, width=3)
        draw.line([cx - r * 0.1, cy, cx + r * 0.1, cy], fill=col, width=3)
    elif kind == "radar":
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=3)
        draw.pieslice([cx - r, cy - r, cx + r, cy + r], -90, 0, fill=RED)
        draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=col)
    elif kind == "blast":
        for ang in range(0, 360, 45):
            import math
            a = math.radians(ang)
            x1 = cx + math.cos(a) * r * 0.35
            y1 = cy + math.sin(a) * r * 0.35
            x2 = cx + math.cos(a) * r
            y2 = cy + math.sin(a) * r
            draw.line([x1, y1, x2, y2], fill=RED, width=3)
        draw.ellipse([cx - r * 0.3, cy - r * 0.3, cx + r * 0.3, cy + r * 0.3],
                     fill=col)
    elif kind == "chart":
        draw.line([cx - r, cy + r, cx + r, cy + r], fill=col, width=2)
        draw.line([cx - r, cy + r, cx - r, cy - r], fill=col, width=2)
        pts = [(cx - r * 0.8, cy - r * 0.6), (cx - r * 0.3, cy - r * 0.1),
               (cx + r * 0.2, cy + r * 0.1), (cx + r * 0.8, cy + r * 0.7)]
        draw.line(pts, fill=RED, width=3, joint="curve")
    elif kind == "chip":
        draw.rectangle([cx - r * 0.7, cy - r * 0.7, cx + r * 0.7, cy + r * 0.7],
                       outline=col, width=3)
        draw.rectangle([cx - r * 0.3, cy - r * 0.3, cx + r * 0.3, cy + r * 0.3],
                       fill=RED)
        for dx in (-1, 0, 1):
            draw.line([cx + dx * r * 0.4, cy - r, cx + dx * r * 0.4,
                       cy - r * 0.7], fill=col, width=2)
            draw.line([cx + dx * r * 0.4, cy + r * 0.7, cx + dx * r * 0.4,
                       cy + r], fill=col, width=2)


# ---------------------------------------------------------------- layout

def masthead(draw):
    draw.text((W / 2, 12), stories.MASTHEAD, font=F_TITLE, fill=INK,
              anchor="ma")
    draw.rectangle([0, 64, W, 102], fill=RED)
    draw.text((W / 2, 70), stories.DATE_LINE, font=F_DATE, fill=(255, 255, 255),
              anchor="ma")
    draw.text((W / 2, 103), stories.SUBHEAD, font=F_SUB, fill=INK, anchor="ma")
    draw.line([24, 120, W - 24, 120], fill=LINE, width=1)


def stats(draw):
    cell = W / 4.0
    for i, (num, label, sub) in enumerate(stories.STATS):
        cx = cell * i + cell / 2.0
        draw.text((cx, 126), num, font=F_STAT_NUM, fill=NAVY, anchor="ma")
        draw.text((cx, 158), label, font=F_STAT_LBL, fill=RED, anchor="ma")
        draw.text((cx, 175), sub, font=F_STAT_SUB, fill=GREY, anchor="ma")
        if i:
            draw.line([cell * i, 128, cell * i, 188], fill=LINE, width=1)
    draw.line([24, 194, W - 24, 194], fill=LINE, width=1)


def features(draw):
    y0, y1 = 198, 470
    colw = (W - 48 - 20) / 3.0
    for i, feat in enumerate(stories.FEATURES):
        x0 = 24 + i * (colw + 10)
        x1 = x0 + colw
        draw.rectangle([x0, y0, x1, y1], outline=LINE, width=1)
        draw.rectangle([x0, y0, x1, y0 + 4], fill=RED)
        px = x0 + 14
        py = y0 + 16
        draw.text((px, py), str(feat["num"]), font=F_NUM, fill=RED)
        draw.text((px + 52, py + 6), feat["kicker"], font=F_KICK, fill=NAVY)
        draw.text((px + 52, py + 24), feat["place"], font=F_PLACE, fill=GREY)
        icon(draw, feat["icon"], (x0 + x1) / 2, y0 + 102, 50)
        hy = y0 + 132
        lines = wrap(draw, feat["headline"], F_HEAD, colw - 28)
        hy = draw_lines(draw, lines[:2], F_HEAD, px, hy, 25)
        by = hy + 6
        blines = wrap(draw, feat["body"], F_BODY, colw - 28)
        by = draw_lines(draw, blines[:3], F_BODY, px, by, 19)
        draw.text((px, y1 - 26), feat["fact"], font=F_FACT, fill=RED)


def tiles(draw):
    y0 = 482
    rowh = 156
    colw = (W - 48 - 30) / 4.0
    for idx, tile in enumerate(stories.TILES):
        row, col = divmod(idx, 4)
        x0 = 24 + col * (colw + 10)
        y = y0 + row * (rowh + 6)
        x1 = x0 + colw
        y1 = y + rowh
        draw.rectangle([x0, y, x1, y1], outline=LINE, width=1)
        draw.text((x0 + 10, y + 8), str(tile["num"]), font=F_TNUM, fill=RED)
        icon(draw, tile["icon"], x1 - 24, y + 24, 30)
        lines = wrap(draw, tile["headline"], F_THEAD, colw - 20)
        ty = draw_lines(draw, lines[:2], F_THEAD, x0 + 10, y + 40, 20)
        blines = wrap(draw, tile["body"], F_TBODY, colw - 20)
        draw_lines(draw, blines[:2], F_TBODY, x0 + 10, ty + 4, 17)
        draw.text((x0 + 10, y1 - 20), tile["place"], font=F_TPLACE, fill=GREY)


def bottom(draw):
    y0 = 810
    draw.line([24, 804, W - 24, 804], fill=LINE, width=1)
    # Left: ALSO ON + story 12
    lx = 24
    lw = 470
    draw.text((lx, y0), "ALSO ON 22 NOVEMBER", font=F_SECT, fill=RED)
    by = y0 + 26
    for item in stories.ALSO_ON:
        draw.text((lx, by), "\u2022", font=F_BULLET, fill=RED)
        draw.text((lx + 16, by), item, font=F_BULLET, fill=INK)
        by += 18
    by += 6
    draw.line([lx, by - 4, lx + lw, by - 4], fill=LINE, width=1)
    b = stories.BRIEF
    head = "12. " + b["headline"]
    lines = wrap(draw, head, F_BRIEF_H, lw)
    by = draw_lines(draw, lines[:2], F_BRIEF_H, lx, by, 17)
    blines = wrap(draw, b["body"], F_BRIEF_B, lw)
    draw_lines(draw, blines[:1], F_BRIEF_B, lx, by + 2, 15)
    # Right: WHERE IT HAPPENED
    rx = 524
    draw.text((rx, y0), "WHERE IT HAPPENED", font=F_SECT, fill=NAVY)
    py = y0 + 26
    for col in range(2):
        for row in range(6):
            n, place = stories.PLACES[col * 6 + row]
            draw.text((rx + col * 230, py + row * 19),
                      "%d. %s" % (n, place), font=F_BULLET, fill=INK)


def footer(draw):
    draw.rectangle([0, 962, W, 968], fill=RED)
    draw.text((W / 2, 974), stories.FOOTER, font=F_FOOT, fill=INK, anchor="ma")
    draw.text((W / 2, 996), stories.SOURCES, font=F_SRC, fill=GREY, anchor="ma")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    stats(draw)
    features(draw)
    tiles(draw)
    bottom(draw)
    footer(draw)
    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
