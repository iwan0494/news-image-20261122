"""Render the ATLAS-35 poster for 22 November 2026 to poster-20261122.png.

Layout (1024x1024, all fixed coordinates, no randomness, no clock):
  masthead -> red date ribbon -> 3 hero cards -> schematic world map
  with numbered dots -> 6 region bands of one-line stories -> footer.
Deterministic: the same input always renders the same bytes.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

import stories

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
NAVY = (30, 58, 95)
RED = (185, 28, 28)
GREY = (110, 110, 105)
RULE = (190, 185, 175)
OCEAN = (220, 232, 242)
LAND = (175, 198, 216)
LAND_EDGE = (140, 168, 190)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 52)
F_DATE = font("DejaVuSans-Bold.ttf", 26)
F_STRAP = font("DejaVuSans-Bold.ttf", 17)
F_HERO_NUM = font("DejaVuSans-Bold.ttf", 46)
F_KICKER = font("DejaVuSans-Bold.ttf", 13)
F_HERO_HEAD = font("DejaVuSans-Bold.ttf", 21)
F_HERO_FACT = font("DejaVuSans-Bold.ttf", 15)
F_MAP_LABEL = font("DejaVuSans-Bold.ttf", 14)
F_PLACE = font("DejaVuSans.ttf", 11)
F_DOT = font("DejaVuSans-Bold.ttf", 10)
F_TAB = font("DejaVuSans-Bold.ttf", 14)
F_STORY = font("DejaVuSans-Bold.ttf", 13)
F_FACT = font("DejaVuSans.ttf", 13)
F_NUM = font("DejaVuSans-Bold.ttf", 13)
F_FOOT1 = font("DejaVuSans-Bold.ttf", 16)
F_FOOT2 = font("DejaVuSans.ttf", 12)

MARGIN = 24


def text_w(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap(draw, text, fnt, max_w):
    """Greedy wrap to at most two lines; returns list of lines."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if text_w(draw, trial, fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines[:2]


# --- schematic continents, rough lon/lat outlines (not to survey scale) ---
NORTH_AMERICA = [
    (-168, 66), (-158, 58), (-152, 60), (-140, 60), (-130, 54),
    (-125, 49), (-124, 42), (-120, 34), (-114, 29), (-108, 23),
    (-97, 16), (-90, 14), (-83, 9), (-79, 9), (-82, 13), (-87, 15),
    (-90, 21), (-97, 26), (-91, 29), (-84, 30), (-81, 26), (-80, 32),
    (-76, 35), (-74, 40), (-70, 42), (-66, 45), (-60, 47), (-56, 50),
    (-64, 56), (-72, 60), (-80, 64), (-90, 66), (-100, 69), (-115, 68),
    (-130, 70), (-145, 70), (-158, 71), (-165, 68),
]
GREENLAND = [
    (-58, 64), (-52, 60), (-43, 60), (-38, 65), (-30, 68), (-22, 70),
    (-20, 74), (-26, 76), (-42, 78), (-55, 76), (-60, 74), (-58, 70),
]
SOUTH_AMERICA = [
    (-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
    (-70, -23), (-70, -30), (-73, -37), (-73, -44), (-74, -50),
    (-70, -54), (-66, -55), (-65, -45), (-62, -40), (-57, -34),
    (-52, -32), (-48, -28), (-41, -23), (-39, -17), (-35, -9),
    (-35, -6), (-40, -3), (-44, -2), (-50, 0), (-55, 5), (-60, 8),
    (-66, 10), (-72, 11), (-76, 10),
]
EUROPE = [
    (-10, 36), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (0, 50), (3, 51),
    (6, 53), (8, 55), (8, 57), (11, 59), (6, 60), (6, 62), (11, 64),
    (15, 67), (20, 70), (26, 71), (31, 70), (33, 67), (38, 65),
    (41, 61), (40, 55), (37, 50), (34, 46), (30, 45), (27, 44),
    (23, 40), (22, 37), (26, 36), (29, 36), (27, 38), (23, 36),
    (19, 42), (15, 44), (12, 44), (8, 44), (3, 42), (0, 40), (-2, 37),
    (-6, 36),
]
AFRICA = [
    (-6, 35), (-10, 31), (-15, 27), (-17, 21), (-17, 15), (-15, 11),
    (-12, 8), (-8, 5), (-4, 5), (2, 6), (6, 4), (9, 4), (13, 3),
    (9, 0), (12, -5), (13, -10), (12, -17), (14, -22), (16, -28),
    (20, -35), (26, -34), (32, -29), (35, -24), (40, -15), (40, -10),
    (42, -5), (46, 0), (51, 2), (51, 10), (48, 11), (43, 12),
    (40, 15), (38, 18), (37, 22), (34, 28), (32, 31), (29, 32),
    (24, 32), (19, 32), (14, 32), (10, 34), (10, 37), (5, 37), (0, 36),
]
ASIA = [
    (32, 36), (36, 36), (40, 38), (44, 39), (48, 38), (52, 37),
    (55, 39), (58, 41), (62, 43), (66, 45), (70, 47), (74, 49),
    (78, 52), (82, 55), (87, 58), (92, 61), (97, 63), (102, 65),
    (107, 67), (112, 69), (117, 71), (122, 72), (127, 71), (132, 72),
    (137, 71), (142, 72), (147, 70), (152, 68), (157, 64), (161, 60),
    (162, 56), (158, 52), (155, 50), (150, 48), (145, 45), (142, 42),
    (140, 38), (137, 34), (133, 31), (130, 28), (127, 25), (124, 22),
    (121, 18), (118, 14), (115, 10), (112, 8), (109, 5), (106, 2),
    (103, 1), (100, 5), (98, 9), (96, 13), (94, 17), (92, 21),
    (89, 22), (86, 20), (83, 17), (80, 14), (78, 10), (76, 8),
    (74, 13), (72, 17), (70, 21), (67, 23), (64, 25), (61, 25),
    (58, 26), (55, 27), (52, 28), (49, 30), (48, 32), (45, 34),
    (42, 37), (39, 37), (36, 36),
]
AUSTRALIA = [
    (114, -22), (114, -30), (115, -35), (119, -35), (124, -33),
    (129, -32), (132, -32), (135, -35), (138, -35), (140, -38),
    (145, -38), (150, -37), (153, -32), (153, -27), (151, -24),
    (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
    (132, -12), (130, -13), (126, -14), (122, -17), (118, -20),
]
CONTINENTS = [
    NORTH_AMERICA, GREENLAND, SOUTH_AMERICA, EUROPE, AFRICA, ASIA,
    AUSTRALIA,
]

# Map frame: lon -180..180 -> x, lat 78..-58 -> y.
MAP_X0, MAP_X1 = 28, 996
MAP_Y0, MAP_Y1 = 282, 448
MAP_LAT_TOP, MAP_LAT_BOT = 78.0, -58.0


def map_xy(lon, lat):
    x = MAP_X0 + (lon + 180.0) / 360.0 * (MAP_X1 - MAP_X0)
    y = MAP_Y0 + (MAP_LAT_TOP - lat) / (MAP_LAT_TOP - MAP_LAT_BOT) * (
        MAP_Y1 - MAP_Y0
    )
    return (x, y)


def draw_masthead(draw):
    title = "THE WORLD IN ONE DAY"
    tw = text_w(draw, title, F_TITLE)
    draw.text(((W - tw) / 2, 2), title, font=F_TITLE, fill=NAVY)
    draw.rectangle([0, 58, W, 100], fill=RED)
    date = "SUNDAY, 22 NOVEMBER 2026"
    draw.text((MARGIN, 66), date, font=F_DATE, fill=(255, 255, 255))
    strap = "35 STORIES \u00b7 7 REGIONS"
    sw = text_w(draw, strap, F_STRAP)
    draw.text((W - MARGIN - sw, 72), strap, font=F_STRAP, fill=(255, 255, 255))


def draw_heroes(draw):
    y0, y1 = 106, 252
    gap = 12
    cw = (W - 2 * MARGIN - 2 * gap) // 3
    for i, hero in enumerate(stories.HEROES):
        x0 = MARGIN + i * (cw + gap)
        x1 = x0 + cw
        draw.rectangle([x0, y0, x1, y0 + 3], fill=RED)
        draw.rectangle([x0, y0, x1, y1], outline=RULE, width=1)
        num = str(hero["num"])
        draw.text((x0 + 12, y0 + 12), num, font=F_HERO_NUM, fill=RED)
        nw = text_w(draw, num, F_HERO_NUM)
        draw.text(
            (x0 + 12 + nw + 12, y0 + 18),
            hero["kicker"],
            font=F_KICKER,
            fill=NAVY,
        )
        head_lines = wrap(draw, hero["headline"], F_HERO_HEAD, cw - 24)
        hy = y0 + 66
        for line in head_lines:
            draw.text((x0 + 12, hy), line, font=F_HERO_HEAD, fill=INK)
            hy += 26
        draw.text(
            (x0 + 12, y1 - 26), hero["fact"], font=F_HERO_FACT, fill=RED
        )


def draw_map(draw):
    y0, y1 = 258, 452
    draw.rectangle([MARGIN, y0, W - MARGIN, y1], fill=OCEAN, outline=RULE)
    label = "WHERE IT HAPPENED \u2014 22 NOVEMBER 2026"
    draw.text((MARGIN + 10, y0 + 6), label, font=F_MAP_LABEL, fill=NAVY)
    for poly in CONTINENTS:
        pts = [map_xy(lon, lat) for lon, lat in poly]
        draw.polygon(pts, fill=LAND, outline=LAND_EDGE)
    # Main-map dots: everything except the Europe cluster, which gets
    # its own enlarged inset (at this scale Europe's dots collide).
    inset_nums = {1, 2, 3, 7, 11, 12, 16}
    main_offsets = {
        18: (12, 4), 19: (12, -4), 22: (12, -4), 23: (12, 8),
        27: (-52, -4), 28: (-64, -4), 34: (12, -6),
    }
    for num, lon, lat, name in stories.MAP_DOTS:
        if num in inset_nums:
            continue
        cx, cy = map_xy(lon, lat)
        draw_dot(draw, cx, cy, num)
        if name:
            dx, dy = main_offsets.get(num, (12, -6))
            lx, ly = cx + dx, cy + dy
            draw.line([cx, cy, lx + 4, ly + 5], fill=(120, 130, 145), width=1)
            draw.text((lx, ly), name, font=F_PLACE, fill=(40, 55, 75))
    draw_europe_inset(draw)


def draw_dot(draw, cx, cy, num):
    r = 7
    draw.ellipse(
        [cx - r, cy - r, cx + r, cy + r], fill=RED, outline=(255, 255, 255)
    )
    tag = str(num)
    tw = text_w(draw, tag, F_DOT)
    draw.text((cx - tw / 2, cy - 7), tag, font=F_DOT, fill=(255, 255, 255))


def draw_europe_inset(draw):
    # Enlarged Europe detail over the empty Atlantic: lon -12..42,
    # lat 35..63, drawn inside a solid panel so it reads as a callout.
    ix0, iy0, ix1, iy1 = 330, 290, 600, 430
    draw.rectangle([ix0, iy0, ix1, iy1], fill=(245, 242, 235), outline=NAVY)

    def inset_xy(lon, lat):
        x = ix0 + (lon + 12.0) / 54.0 * (ix1 - ix0)
        y = iy0 + (63.0 - lat) / 28.0 * (iy1 - iy0)
        return (x, y)

    pts = []
    for lon, lat in EUROPE:
        x, y = inset_xy(lon, lat)
        pts.append((min(max(x, ix0), ix1), min(max(y, iy0), iy1)))
    draw.polygon(pts, fill=LAND, outline=LAND_EDGE)
    draw.text(
        (ix0 + 10, iy0 + 6), "EUROPE \u2014 ENLARGED", font=F_MAP_LABEL,
        fill=NAVY,
    )
    labels = {
        1: ("Antalya", (12, -4)),
        2: ("Brussels", (-8, -20)),
        3: ("Poland", (10, -18)),
        7: ("London", (-46, -4)),
        11: ("Kerch", (-44, 2)),
        12: ("Kyiv", (12, -4)),
        16: ("Gulf of Finland", (-80, 6)),
    }
    by_num = {num: (lon, lat) for num, lon, lat, _ in stories.MAP_DOTS}
    for num in (1, 2, 3, 7, 11, 12, 16):
        lon, lat = by_num[num]
        cx, cy = inset_xy(lon, lat)
        draw_dot(draw, cx, cy, num)
        name, (dx, dy) = labels[num]
        lx, ly = cx + dx, cy + dy
        draw.line([cx, cy, lx + 4, ly + 5], fill=(120, 130, 145), width=1)
        draw.text((lx, ly), name, font=F_PLACE, fill=(40, 55, 75))


def draw_bands(draw):
    y = 458
    col_w = (W - 2 * MARGIN) // 2
    for band in stories.BANDS:
        tab = band["label"]
        tab_w = text_w(draw, tab, F_TAB) + 24
        draw.rectangle([MARGIN, y, MARGIN + tab_w, y + 24], fill=band["color"])
        draw.text((MARGIN + 12, y + 4), tab, font=F_TAB, fill=(255, 255, 255))
        draw.line(
            [MARGIN + tab_w, y + 12, W - MARGIN, y + 12], fill=RULE, width=1
        )
        y += 24
        rows = []
        items = band["stories"]
        for i in range(0, len(items), 2):
            rows.append(items[i:i + 2])
        for row in rows:
            for col, (num, headline, fact) in enumerate(row):
                x = MARGIN + col * col_w
                line = "%d. %s \u2014 %s" % (num, headline, fact)
                # Measure the line; if it overflows, drop the fact tail.
                if text_w(draw, line, F_STORY) > col_w - 8:
                    line = "%d. %s" % (num, headline)
                draw.text((x, y), line, font=F_STORY, fill=INK)
            y += 19
        y += 4
    return y


def draw_footer(draw, band_end):
    y = 962
    draw.rectangle([MARGIN, y, W - MARGIN, y + 4], fill=RED)
    line1 = stories.FOOTER_LINE1
    tw = text_w(draw, line1, F_FOOT1)
    draw.text(((W - tw) / 2, y + 12), line1, font=F_FOOT1, fill=INK)
    line2 = stories.FOOTER_LINE2
    tw = text_w(draw, line2, F_FOOT2)
    draw.text(((W - tw) / 2, y + 36), line2, font=F_FOOT2, fill=GREY)


def render(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)
    draw_heroes(draw)
    draw_map(draw)
    band_end = draw_bands(draw)
    draw_footer(draw, band_end)
    img.save(out_path, format="PNG")
    return out_path


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "poster-20261122.png"
    render(out)
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
