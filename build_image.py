#!/usr/bin/env python3
"""Build the news-image entry: one infographic summing up world news,
Tuesday 17 November 2026. Renders entry.png (1024x1024) with PIL.

Gate limits (RULES.txt): PNG/JPEG, <= 1 MiB, <= 1024x1024 px.

Stories verified against 17 Nov 2026 sources (Reuters, Al Jazeera, AFP, BBC
via search results of 18 Nov 2026):
 1. US-Iran war escalates in the Gulf (4th tanker mined in Hormuz in 24h;
    US strikes IRGC Qeshm launch site; Iranian drones target US base Bahrain)
 2. Ukraine hits Crimean Bridge; Russia hits Kyiv bridges; Zaporizhzhia 40 dead
 3. Gaza winter crisis: UK/AU/CA/IT urge Israel to open aid crossings;
    1.7M displaced (WFP/IOM, 17 Nov)
 4. Gerard Depardieu pleads guilty to sexual assault, drops appeal (Paris)
 5. Japan scrambles jets as Russian aircraft breach its airspace
 6. COP31 draft deal (Antalya): faster fossil-fuel phase-out, $120bn/yr by 2035
Also: US loses measles-elimination status (~30 yrs); Xi-Trump-Putin summit
Thu 19 Nov in Shenzhen; Mongolia's president resigns.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (255, 255, 255)
INK = (12, 12, 12)
RED = (178, 0, 0)
GREY = (90, 90, 90)
LIGHT = (238, 238, 238)
NAVY = (16, 28, 52)

SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
M = 40
x0, x1 = M, W - M

# ---- Masthead ----
y = 30
title = "THE WORLD IN ONE IMAGE"
tf = font(SERIF_B, 52)
tw = d.textlength(title, font=tf)
d.text(((W - tw) / 2, y), title, font=tf, fill=INK)
y += 66
d.rectangle([x0, y, x1, y + 4], fill=INK)
y += 12
bar_h = 50
d.rectangle([x0, y, x1, y + bar_h], fill=NAVY)
bf = font(SANS_B, 24)
bar = "TUESDAY, 17 NOVEMBER 2026"
bw = d.textlength(bar, font=bf)
d.text(((W - bw) / 2, y + 11), bar, font=bf, fill=(255, 255, 255))
y += bar_h + 20

# ---- Lead story (full width) ----
kick = font(SANS_B, 22)
d.text((x0, y), "1  —  WAR IN THE GULF", font=kick, fill=RED)
y += 32
hl = font(SANS_B, 40)
for ln in wrap(d, "U.S.–Iran war escalates in the Strait of Hormuz", hl, x1 - x0):
    d.text((x0, y), ln, font=hl, fill=INK)
    y += 48
sf = font(SANS, 24)
lead = ("A fourth tanker is hit by a mine in 24 hours. U.S. forces strike an IRGC "
        "launch site on Qeshm Island, and Iranian drones target the U.S. base in Bahrain.")
for ln in wrap(d, lead, sf, x1 - x0):
    d.text((x0, y), ln, font=sf, fill=(40, 40, 40))
    y += 32
y += 12
d.rectangle([x0, y, x1, y + 3], fill=INK)
y += 16

# ---- Stories 2-5: two columns x two rows ----
col_w = (x1 - x0 - 32) // 2
stories = [
    ("2  —  UKRAINE",
     "Kyiv strike closes the Crimean Bridge",
     "Russia answers by hitting bridges in Kyiv. A strike on Zaporizhzhia kills 40 people."),
    ("3  —  GAZA",
     "West urges Israel to open aid crossings",
     "Britain, Australia, Canada and Italy call the situation catastrophic. 1.7 million people remain displaced as winter closes in."),
    ("4  —  FRANCE",
     "Depardieu pleads guilty to sexual assault",
     "The French film star drops his appeal and admits the charge in a Paris court."),
    ("5  —  JAPAN",
     "Tokyo scrambles jets as Russian planes breach airspace",
     "Two suspected Russian aircraft enter Japanese airspace. Japan lodges a strong protest."),
]
row_top = y
row_h = 190
for idx, (kicker, headline, summary) in enumerate(stories):
    col = idx % 2
    row = idx // 2
    cx = x0 + col * (col_w + 32)
    cy = row_top + row * row_h
    d.text((cx, cy), kicker, font=kick, fill=RED)
    hf = font(SANS_B, 27)
    ly = cy + 30
    for ln in wrap(d, headline, hf, col_w):
        d.text((cx, ly), ln, font=hf, fill=INK)
        ly += 33
    sf2 = font(SANS, 21)
    for ln in wrap(d, summary, sf2, col_w):
        d.text((cx, ly), ln, font=sf2, fill=(40, 40, 40))
        ly += 27
    if col == 0:
        d.line([cx + col_w + 16, cy + 4, cx + col_w + 16, cy + 172], fill=(200, 200, 200), width=2)
y = row_top + 2 * row_h + 4
d.rectangle([x0, y, x1, y + 3], fill=INK)
y += 14

# ---- Story 6: climate band ----
band_h = 116
d.rectangle([x0, y, x1, y + band_h], fill=LIGHT)
d.text((x0 + 18, y + 8), "6  —  CLIMATE", font=kick, fill=RED)
hf6 = font(SANS_B, 26)
ly6 = y + 40
for ln in wrap(d, "COP31 draft: faster fossil-fuel exit, $120bn a year for developing nations by 2035.",
               hf6, x1 - x0 - 36):
    d.text((x0 + 18, ly6), ln, font=hf6, fill=INK)
    ly6 += 32
y += band_h + 14

# ---- Also line ----
af = font(SANS_B, 20)
also = ("ALSO:  U.S. loses measles-elimination status after ~30 years  •  "
        "Xi, Trump and Putin to meet Thursday in Shenzhen  •  "
        "Mongolia's president resigns")
for ln in wrap(d, also, af, x1 - x0):
    d.text((x0, y), ln, font=af, fill=(40, 40, 40))
    y += 27
y += 10
d.rectangle([x0, y, x1, y + 2], fill=(180, 180, 180))
y += 10
ff = font(SANS, 17)
d.text((x0, y), "Sources: Reuters, Al Jazeera, AFP, BBC — 17 November 2026",
       font=ff, fill=GREY)

img.save("entry.png")
print("saved entry.png", img.size)
