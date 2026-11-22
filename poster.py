"""Render the 22 November 2026 poster (round 3) with PIL.

Layout (1024 x 1024, deterministic): masthead + red date band, a
four-box stat strip, one full-width lead story with a big headline,
two rows of two stories each, one row of two shorter stories, a red
DATE CHECK box, and a footer. Every story gets a small illustration
drawn with PIL primitives. No randomness, no system date.

Revision 2: certainty chips moved onto the kicker line and the
source line flows right after the tagline, so nothing can overlap;
icons are drawn on a small canvas and scaled to fit their strip.
Revision 3 (fix): row 4 runs tight (shorter icon strip, tighter gaps)
so the source line sits ~13 px higher, clear of the panel border.
"""

import os

from PIL import Image, ImageDraw, ImageFont

import stories

W = 1024
H = 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
GREY = (120, 116, 108)
LINE = (200, 194, 182)
SKY = (214, 230, 240)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
OUT = "poster-20261122.png"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731
REG = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731


def wrap(text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if fnt.getlength(trial) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, text, fnt, x, y, width, fill, spacing=4):
    lines = wrap(text, fnt, width)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def draw_center(draw, text, fnt, cx, y, fill):
    w = fnt.getlength(text)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def chip_width(label):
    return BOLD(11).getlength(label) + 12


def draw_chip(draw, x, y, label, fill):
    """Small certainty chip: coloured box + white bold label."""
    fnt = BOLD(11)
    w = chip_width(label)
    h = 17
    draw.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=fill)
    draw.text((x + 6, y + 3), label, font=fnt, fill=(255, 255, 255))
    return x + w


# ---------------------------------------------------------------- icons
def _icon_canvas(kind):
    """Draw one icon on a 120x76 sky canvas; returns the image."""
    cv = Image.new("RGB", (120, 76), SKY)
    d = ImageDraw.Draw(cv)
    x0, y0, x1, y1 = 0, 0, 120, 76
    cx, cy = 60, 38
    if kind == "radar":
        d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], outline=NAVY, width=3)
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], outline=NAVY, width=2)
        d.line([cx, cy, cx + 26, cy - 16], fill=RED, width=3)
        d.line([cx - 30, cy, cx + 30, cy], fill=NAVY, width=1)
        d.line([cx, cy - 30, cx, cy + 30], fill=NAVY, width=1)
        for bx, by in [(cx - 11, cy + 7), (cx + 12, cy - 5), (cx + 3, cy + 14)]:
            d.ellipse([bx - 3, by - 3, bx + 3, by + 3], fill=RED)
        for i in range(3):
            yy = y1 - 8 - i * 6
            d.arc([x0 + 6, yy - 6, x1 - 6, yy + 10], 180, 360, fill=NAVY, width=2)
    elif kind == "missile":
        d.polygon([(cx - 40, cy + 12), (cx + 26, cy - 22), (cx + 35, cy - 14),
                   (cx - 31, cy + 21)], fill=NAVY)
        d.polygon([(cx - 40, cy + 12), (cx - 50, cy + 3), (cx - 35, cy + 1)],
                  fill=RED)
        d.polygon([(cx + 26, cy - 22), (cx + 38, cy - 26), (cx + 35, cy - 14)],
                  fill=RED)
        for i in range(3):
            d.line([cx - 45 - i * 7, cy + 17 + i * 4, cx - 50 - i * 7,
                    cy + 22 + i * 4], fill=(255, 150, 40), width=3)
        d.line([x0 + 8, y1 - 12, x1 - 8, y1 - 12], fill=GREY, width=2)
    elif kind == "globe":
        d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], outline=NAVY, width=3)
        d.ellipse([cx - 11, cy - 30, cx + 11, cy + 30], outline=NAVY, width=2)
        d.line([x0 + 4, cy, x1 - 4, cy], fill=NAVY, width=2)
        d.arc([x0 + 4, cy - 18, x1 - 4, cy + 18], 0, 180, fill=NAVY, width=2)
        d.arc([x0 + 4, cy - 18, x1 - 4, cy + 18], 180, 360, fill=NAVY, width=2)
        d.line([cx + 16, cy - 26, cx + 30, cy - 38], fill=(60, 140, 70), width=3)
        d.ellipse([cx + 26, cy - 42, cx + 40, cy - 30], fill=(60, 140, 70))
    elif kind == "chart":
        d.line([x0 + 10, y0 + 8, x0 + 10, y1 - 10], fill=INK, width=2)
        d.line([x0 + 10, y1 - 10, x1 - 8, y1 - 10], fill=INK, width=2)
        pts = [(x0 + 14, y0 + 14), (x0 + 30, y0 + 22), (x0 + 44, y0 + 18),
               (x0 + 58, y0 + 38), (x0 + 72, y0 + 52), (x0 + 86, y0 + 58)]
        d.line(pts, fill=RED, width=4, joint="curve")
        d.polygon([(x0 + 86, y0 + 58), (x0 + 78, y0 + 52), (x0 + 88, y0 + 48)],
                  fill=RED)
    elif kind == "trade":
        d.rectangle([x0 + 10, y0 + 10, x0 + 44, y0 + 32], fill=NAVY)
        for sx, sy in [(x0 + 27, y0 + 14), (x0 + 19, y0 + 21), (x0 + 35, y0 + 21),
                       (x0 + 23, y0 + 27), (x0 + 31, y0 + 27)]:
            d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 215, 0))
        d.rectangle([x0 + 52, y0 + 10, x0 + 86, y0 + 21], fill=RED)
        d.rectangle([x0 + 52, y0 + 21, x0 + 86, y0 + 32], fill=(255, 255, 255))
        d.rectangle([x0 + 16, y0 + 40, x1 - 16, y1 - 8], outline=INK, width=2)
        for i in range(3):
            d.line([x0 + 22, y0 + 47 + i * 7, x1 - 24, y0 + 47 + i * 7],
                   fill=GREY, width=2)
    elif kind == "cuffs":
        d.ellipse([cx - 34, cy - 12, cx - 9, cy + 12], outline=NAVY, width=4)
        d.ellipse([cx + 9, cy - 12, cx + 34, cy + 12], outline=NAVY, width=4)
        d.line([cx - 9, cy, cx + 9, cy], fill=NAVY, width=3)
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=NAVY)
        d.polygon([(cx, cy - 30), (cx + 4, cy - 23), (cx + 11, cy - 23),
                   (cx + 5, cy - 18), (cx + 7, cy - 11), (cx, cy - 15),
                   (cx - 7, cy - 11), (cx - 5, cy - 18), (cx - 11, cy - 23),
                   (cx - 4, cy - 23)], fill=RED)
    elif kind == "quake":
        d.polygon([(x0 + 8, y1 - 12), (x0 + 26, y0 + 24), (x0 + 40, y1 - 12),
                   (x0 + 58, y0 + 14), (x0 + 76, y1 - 12)], outline=NAVY, width=2)
        pts = [(x0 + 6, cy), (x0 + 20, cy), (x0 + 26, cy - 14), (x0 + 32, cy + 12),
               (x0 + 38, cy - 5), (x0 + 46, cy), (x0 + 58, cy), (x0 + 64, cy - 18),
               (x0 + 70, cy + 14), (x0 + 78, cy), (x0 + 92, cy)]
        d.line(pts, fill=RED, width=3, joint="curve")
    return cv


def draw_icon(img, kind, box):
    """Paste the icon at its natural aspect, centred in `box`."""
    x0, y0, x1, y1 = box
    h = y1 - y0
    w = h * 120 // 76
    icon = _icon_canvas(kind).resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    d.rectangle(box, fill=SKY)
    img.paste(icon, (x0 + (x1 - x0 - w) // 2, y0))
    d.rectangle(box, outline=LINE, width=1)


# ---------------------------------------------------------------- layout
def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead
    draw_center(d, stories.MASTHEAD, BOLD(52), W // 2, 6, INK)
    d.rectangle([0, 60, W, 96], fill=RED)
    draw_center(d, stories.DATE_LINE, BOLD(30), W // 2, 64, (255, 255, 255))

    # --- stat strip
    y0, y1 = 100, 146
    bw = (W - 32) // 4
    for i, (num, lab) in enumerate(stories.STATS):
        x0 = 16 + i * bw
        x1 = x0 + bw - 8
        d.rectangle([x0, y0, x1, y1], outline=LINE, width=1)
        draw_center(d, num, BOLD(29), (x0 + x1) // 2, y0 + 2, NAVY if i % 2 == 0 else RED)
        draw_center(d, lab, REG(11), (x0 + x1) // 2, y0 + 31, GREY)

    # --- lead story (full width)
    lead = stories.STORIES[0]
    ly0, ly1 = 150, 336
    d.rectangle([16, ly0, W - 16, ly1], outline=LINE, width=1)
    d.rectangle([16, ly0, W - 16, ly0 + 4], fill=RED)
    draw_icon(img, lead["icon"], (24, ly0 + 14, 300, ly1 - 12))
    d.text((316, ly0 + 6), "1  " + lead["kicker"], font=BOLD(13), fill=RED)
    y = draw_wrapped(d, lead["headline"], BOLD(44), 316, ly0 + 26, W - 16 - 316 - 16,
                     INK, spacing=2)
    y = draw_wrapped(d, lead["tagline"], REG(16), 316, y + 4, W - 16 - 316 - 16,
                     INK, spacing=3)
    x = draw_chip(d, 316, y + 6, lead["label"], RED if lead["label"] == "CLAIM" else NAVY)
    d.text((x + 10, y + 9), lead["source"], font=REG(12), fill=GREY)

    # --- two-story rows (chip on the kicker line, source flows after tagline)
    # Row 4 (stories 6-7) is 26 px shorter than rows 2-3 but holds the same
    # text, so it runs `tight`: a shorter icon strip and tighter gaps, which
    # pulls the source line ~13 px up so its ink ends well clear of the
    # panel's bottom border (fix: "AP / FBI" / "USGS" were half-clipped).
    def row_panel(s, x0, x1, y0, y1, head_size, strip_h, tight=False):
        d.rectangle([x0, y0, x1, y1], outline=LINE, width=1)
        d.rectangle([x0, y0, x1, y0 + 3], fill=RED)
        sh = strip_h - 4 if tight else strip_h
        draw_icon(img, s["icon"], (x0 + 8, y0 + 10, x1 - 8, y0 + 10 + sh))
        tx = x0 + 12
        tw = x1 - 12 - tx
        ty = y0 + 10 + sh + 6
        d.text((tx, ty), "%d  %s" % (s["num"], s["kicker"]), font=BOLD(12), fill=RED)
        fill = RED if s["label"] == "CLAIM" else NAVY
        draw_chip(d, x1 - 12 - chip_width(s["label"]), ty - 1, s["label"], fill)
        ty += 14 if tight else 17
        ty = draw_wrapped(d, s["headline"], BOLD(head_size), tx, ty, tw, INK,
                          spacing=1 if tight else 2)
        ty = draw_wrapped(d, s["tagline"], REG(14), tx, ty + (1 if tight else 2),
                          tw, INK, spacing=2 if tight else 3)
        d.text((tx, ty + (2 if tight else 3)), s["source"], font=REG(11), fill=GREY)

    row_panel(stories.STORIES[1], 16, 504, 340, 534, 28, 46)
    row_panel(stories.STORIES[2], 520, 1008, 340, 534, 28, 46)
    row_panel(stories.STORIES[3], 16, 504, 538, 732, 28, 46)
    row_panel(stories.STORIES[4], 520, 1008, 538, 732, 28, 46)
    row_panel(stories.STORIES[5], 16, 504, 736, 904, 23, 36, tight=True)
    row_panel(stories.STORIES[6], 520, 1008, 736, 904, 23, 36, tight=True)

    # --- DATE CHECK
    dy0, dy1 = 908, 960
    d.rectangle([16, dy0, W - 16, dy1], outline=RED, width=3)
    d.text((28, dy0 + 5), stories.DATE_CHECK_TITLE, font=BOLD(14), fill=RED)
    pw = REG(11).getlength(stories.PRESS_TIME)
    d.text((W - 28 - pw, dy0 + 6), stories.PRESS_TIME, font=REG(11), fill=GREY)
    draw_wrapped(d, stories.DATE_CHECK_BODY, REG(12), 28, dy0 + 24, W - 56, INK,
                 spacing=2)

    # --- footer
    d.line([16, 968, W - 16, 968], fill=RED, width=3)
    draw_center(d, stories.FOOTER_DATE, BOLD(12), W // 2, 974, INK)
    draw_center(d, stories.ALSO, REG(11), W // 2, 989, INK)
    draw_center(d, stories.FOOTER_SOURCES, REG(10), W // 2, 1003, GREY)

    img.save(OUT)
    print("wrote %s" % OUT)


if __name__ == "__main__":
    render()
