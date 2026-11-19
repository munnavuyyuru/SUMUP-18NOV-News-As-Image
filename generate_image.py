#!/usr/bin/env python3
# Generates a 1024x1024 editorial front page for 18 Nov 2026
# No external deps beyond Pillow (installed) and standard library
import textwrap
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
# Colors
NAVY = (10, 27, 58)
NAVY2 = (18, 42, 84)
CREAM = (248, 244, 235)
LIGHT_BG = (236, 238, 242)
CARD_BG = (255, 255, 255)
BLUE = (29, 78, 176)
RED = (178, 34, 34)
GREEN = (26, 95, 63)
GOLD = (182, 138, 28)
ORANGE = (197, 88, 26)
TEAL = (15, 118, 110)
PURPLE = (84, 51, 123)

def load_font(size, bold=False):
    # Try DejaVu, fallback to default
    try:
        if bold:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        else:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", size)
        except:
            return ImageFont.load_default()

# Fonts
font_title = load_font(36, True)
font_date = load_font(16, True)
font_big18 = load_font(52, True)
font_h1 = load_font(17, True)
font_h2 = load_font(13, True)
font_body = load_font(10, False)
font_body_bold = load_font(10, True)
font_kicker = load_font(8, True)
font_small = load_font(7, False)
font_footer = load_font(7, False)

im = Image.new("RGB", (W, H), CREAM)
draw = ImageDraw.Draw(im)

# Header band
HEADER_H = 132
draw.rectangle([0,0,W,HEADER_H], fill=NAVY)
# subtle line
draw.rectangle([0,HEADER_H-2,W,HEADER_H], fill=(242, 185, 64))

# Header text
draw.text((24, 16), "THE WORLD TODAY", font=font_title, fill=(255,255,255))
draw.text((24, 62), "WEDNESDAY 18 NOVEMBER 2026", font=font_date, fill=(180, 205, 255))
draw.text((24, 86), "Eight verified developments  ·  six continents  ·  one front page", font=font_small, fill=(196, 207, 227))

# Big 18 on right
draw.text((W-110, 12), "18", font=font_big18, fill=(242, 185, 64))
# NOV label
font_nov = load_font(12, True)
draw.text((W-84, 66), "NOV", font=font_nov, fill=(242, 185, 64))
draw.text((W-108, 92), "2026 • WORLD EDITION", font=font_small, fill=(180,205,255))

# Top feature: Xi + Putin at APEC — full width card
top_y = HEADER_H + 12
top_h = 210
card_pad = 12
draw.rounded_rectangle([12, top_y, W-12, top_y+top_h], radius=14, fill=(224, 235, 255), outline=(190,210,240))
# kicker pill
draw.rounded_rectangle([24, top_y+12, 230, top_y+28], radius=8, fill=BLUE)
draw.text((34, top_y+15), "ASIA-PACIFIC  ·  DIPLOMACY", font=font_kicker, fill=(255,255,255))
draw.text((24, top_y+38), "Xi + Putin meet in Shenzhen", font=load_font(20, True), fill=NAVY)
draw.text((24, top_y+66), "Xi Jinping and Vladimir Putin met at the APEC summit in", font=font_body, fill=(30,30,50))
draw.text((24, top_y+82), "Shenzhen on Wednesday; a first Xi–Putin–Trump trilateral is", font=font_body, fill=(30,30,50))
draw.text((24, top_y+98), "scheduled for Thursday 19 Nov — not yet held in reports", font=font_body, fill=(30,30,50))
draw.text((24, top_y+114), "checked. Trump landed in Manila for Quad talks en route.", font=font_body, fill=(30,30,50))
draw.text((24, top_y+138), "APEC  ·  SHENZHEN  ·  QUAD  ·  XI • PUTIN • TRUMP", font=font_kicker, fill=BLUE)
# Simple globe/vectors on right
# Draw stylized APEC circle
cx, cy = W-140, top_y+95
draw.ellipse([cx-78, cy-62, cx+78, cy+62], outline=BLUE, width=3)
draw.arc([cx-70, cy-52, cx+60, cy+42],  -40, 40, fill=BLUE, width=2)
draw.line([cx, cy-60, cx, cy+60], fill=BLUE, width=2)
draw.polygon([(cx-78, cy+48), (cx-62, cy+32), (cx-44, cy+48)], fill=BLUE)
draw.polygon([(cx-44, cy+38), (cx-28, cy+22), (cx-12, cy+38)], fill=BLUE)
draw.text((cx-48, cy+68), "SHENZHEN  ·  APEC", font=font_kicker, fill=NAVY)
draw.line([W-240, top_y+top_h-18, W-24, top_y+top_h-18], fill=BLUE, width=1)

# Grid of 7 remaining stories: 3 columns, rows
# We have 8 total, 1 used on top, so 7 left -> but we want 7? Actually we promised 8, so top + 7 = 8. We'll add 7 cards.
# Better to have 3 cols x 3 rows = 9 spots, but we have 7 -> last row 1 card spanning? We'll make 3 cols, 3 rows, last row has 2 cards + 1 empty with footer? Let's make 3 cols x 2 rows (6) + 1 spanning bottom row?
# Simpler: 3 cols x 3 rows = 8 cards with one empty filled with legend
GRID_TOP = top_y + top_h + 12
GAP = 10
COL_W = (W - 24 - 2*GAP)//3
ROW_H = 180

stories = [
    {
        "kicker": "MIDDLE EAST / GULF",
        "color": RED,
        "title": "Gulf drones intercepted",
        "icon": "drone",
        "body": "Bahrain said its defences intercepted Iranian drones aimed at U.S. sites; Kuwait engaged hostile drones over Ali Al Salem. Came a day after a U.S. strike on an IRGC missile site on Qeshm Island (night of 17 Nov). No casualties confirmed.",
        "tag": "REPORTED 18 NOV · PRIOR STRIKE 17 NOV"
    },
    {
        "kicker": "MIDDLE EAST / WEST BANK",
        "color": (139, 0, 0),
        "title": "UK & Australia sanction",
        "body": "Britain sanctioned 8 firms building settlements in the occupied West Bank + activist group Tzav 9 blocking Gaza aid; Australia sanctioned 3 people & 4 groups incl. settler leader Daniella Weiss / Nachala.",
        "tag": "FOREIGN OFFICE · 18 NOV",
        "icon": "sanction"
    },
    {
        "kicker": "EUROPE / UKRAINE",
        "color": (0, 51, 102),
        "title": "EU proposes €45bn for Kyiv",
        "body": "European Commission proposed a €45bn loan to Ukraine (€20bn budget + €25bn arms), repayable only if Russia pays reparations. Russian strikes killed at least 5 the same day.",
        "tag": "BRUSSELS · 18 NOV",
        "icon": "eu"
    },
    {
        "kicker": "CLIMATE / GLOBAL",
        "color": GREEN,
        "title": "COP31 deadlocked",
        "body": "Talks in Antalya remained split over “phase out” vs “transition away” for fossil fuels and climate finance. Presidency said 21 issues left; new texts due Thu, close Fri 20 Nov.",
        "tag": "ANTALYA · TALKS CONTINUE",
        "icon": "cop"
    },
    {
        "kicker": "SPACE / GLOBAL",
        "color": (30, 60, 120),
        "title": "Voyager 1: one light-day",
        "body": "At 10:16 UTC Voyager 1 became the first human-made object one light-day from Earth (~25.9B km). Light takes a full day to reach it.",
        "tag": "NASA · 10:16 UTC · FIRST",
        "icon": "space"
    },
    {
        "kicker": "MARKETS / TECH",
        "color": (90, 60, 0),
        "title": "Anthropic IPO at $83",
        "body": "Anthropic priced its record $64.4bn IPO at $83/share, above $70–78 range; Nvidia doubled revenue to $115.8bn (+103%). Gold fell below $3,800 to a year-low.",
        "tag": "MARKETS · 18 NOV",
        "icon": "market"
    },
    {
        "kicker": "ASIA / INDIA",
        "color": TEAL,
        "title": "Cyclone Akvan nears",
        "body": "Severe Cyclonic Storm Akvan intensified in the Bay of Bengal on 18 Nov; IMD forecast landfall ~noon 20 Nov on Andhra Pradesh/Yanam coasts, winds 120–130 km/h gusting 145.",
        "tag": "IMD · BAY OF BENGAL",
        "icon": "cyclone"
    },
]

# Draw grid
for idx, s in enumerate(stories):
    col = idx % 3
    row = idx // 3
    x0 = 12 + col*(COL_W+GAP)
    y0 = GRID_TOP + row*(ROW_H+GAP)
    x1 = x0 + COL_W
    y1 = y0 + ROW_H
    # card
    draw.rounded_rectangle([x0,y0,x1,y1], radius=10, fill=CARD_BG, outline=(210,215,225))
    # left color bar
    draw.rounded_rectangle([x0,y0,x0+5,y1], radius=5, fill=s["color"])
    # kicker
    draw.text((x0+14, y0+10), s["kicker"], font=font_kicker, fill=s["color"])
    # title
    draw.text((x0+14, y0+24), s["title"], font=font_h1, fill=NAVY)
    # icon area top-right small shape
    ix, iy = x1-28, y0+20
    if s["icon"] == "drone":
        # red missile
        draw.polygon([(ix,iy),(ix+18,iy-7),(ix+16,iy-2),(ix+10,iy+4)], fill=RED)
        draw.ellipse([ix-2,iy-2,ix+4,iy+4], fill=RED)
    elif s["icon"] == "sanction":
        draw.rectangle([ix-6,iy-6,ix+10,iy+6], outline=(139,0,0), width=2)
        draw.line([ix-6,iy-6,ix+10,iy+6], fill=(139,0,0), width=2)
    elif s["icon"] == "eu":
        draw.ellipse([ix-8,iy-4,ix+8,iy+4], outline=(0,51,102), width=2)
        # stars
        for a in range(0,360,45):
            import math
            rx = math.cos(math.radians(a))*5
            ry = math.sin(math.radians(a))*3
            draw.ellipse([ix+rx-1,iy+ry-1,ix+rx+1,iy+ry+1], fill=GOLD)
    elif s["icon"] == "cop":
        draw.arc([ix-8,iy-8,ix+8,iy+8], 0, 270, fill=GREEN, width=2)
        draw.line([ix,iy,ix+6,iy-8], fill=GREEN, width=2)
    elif s["icon"] == "space":
        draw.ellipse([ix-9,iy-9,ix+9,iy+9], outline=(30,60,120), width=2)
        draw.ellipse([ix-5,iy-5,ix+5,iy+5], fill=(30,60,120))
        draw.line([ix+9,iy-9,ix+16,iy-16], fill=(30,60,120), width=2)
    elif s["icon"] == "market":
        # upward chart
        draw.line([ix-8,iy+4,ix-4,iy-2,ix,iy+2,ix+4,iy-6,ix+10,iy-8], fill=GOLD, width=2)
        draw.polygon([(ix+10,iy-8),(ix+7,iy-6),(ix+10,iy-3)], fill=GOLD)
    elif s["icon"] == "cyclone":
        draw.arc([ix-8,iy-8,ix+8,iy+8], 20, 300, fill=TEAL, width=3)
        draw.arc([ix-5,iy-5,ix+5,iy+5], 40, 280, fill=TEAL, width=2)
    
    # body text wrapped
    # wrap to ~34 chars per line
    body = s["body"]
    # simple wrapping
    max_w = COL_W - 28
    # use textwrap with width approx 38
    lines = textwrap.wrap(body, width=38)
    # ensure max 6 lines
    lines = lines[:6]
    ty = y0+46
    for line in lines:
        draw.text((x0+14, ty), line, font=font_body, fill=(40,40,55))
        ty += 13
    # tag at bottom
    draw.text((x0+14, y1-16), s["tag"], font=font_small, fill=(120,125,135))

# Footer strip
footer_y = GRID_TOP + 3*(ROW_H+GAP) + 4
draw.rectangle([0, footer_y, W, footer_y+1], fill=(190,190,180))
draw.text((12, footer_y+6), "EDITORIAL NOTE  ·  All events reported on 18 Nov 2026, except the Qeshm Island strike (night of 17 Nov) and Thursday’s trilateral (scheduled 19 Nov) noted as such. Sources: AA, BBC, NYT, Guardian, IMD, NASA, Commission.", font=font_footer, fill=(90,90,90))
draw.text((12, footer_y+18), "Each story cites what happened, where, and when — no speculation shown as fact. Image is faithful to reports available 18 Nov 2026.", font=font_footer, fill=(90,90,90))
# bottom bar
draw.rectangle([0, H-22, W, H], fill=NAVY)
draw.text((12, H-18), "THE WORLD TODAY  ·  WEDNESDAY 18 NOVEMBER 2026  ·  ONE DAY  ·  ONE FRONT PAGE", font=font_kicker, fill=(255,255,255))
draw.text((W-140, H-18), "make.fun #news-image", font=font_kicker, fill=(242,185,64))

im.save("/home/user/workspace-repo/entry.png", "PNG", optimize=True)
print(f"Saved {os.path.getsize('/home/user/workspace-repo/entry.png')} bytes")
# check size
from PIL import Image as PILImage
i = PILImage.open("/home/user/workspace-repo/entry.png")
print(i.size)
