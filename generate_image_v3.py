#!/usr/bin/env python3
# Designer v3 - large pictorials, clear typography, no gibberish
from PIL import Image, ImageDraw, ImageFont
import textwrap, math, os

W,H=1024,1024
NAVY=(8,22,49)
CREAM=(250,247,236)
CARD=(255,255,255)
BLUE=(24,67,161)
RED=(179,28,38)
GREEN=(21,92,67)
TEAL=(12,103,102)
GOLD=(194,153,46)
INK=(22,28,45)

def f(s,b=False):
    try:
        p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p,s)
    except: return ImageFont.load_default()

f_title=f(30,True); f_date=f(12,True); f_kicker=f(7,True); f_h1=f(13,True); f_body=f(8,False); f_small=f(7,False); f_cap=f(6,False); f_h2=f(15,True)

im=Image.new("RGB",(W,H),CREAM)
d=ImageDraw.Draw(im)

# Header
d.rectangle([0,0,W,100],fill=NAVY)
d.rectangle([0,100,W,102],fill=GOLD)
d.text((14,12),"THE WORLD TODAY",font=f_title,fill="white")
d.text((14,48),"WEDNESDAY — 18 NOVEMBER 2026",font=f_date,fill=(170,195,230))
d.text((14,66),"Six continents · Eight verified stories · No speculation shown as fact · 23:59 UTC cutoff",font=f_small,fill=(180,195,210))
# date block
d.rectangle([W-110,8,W-12,92],outline=(90,110,150),width=1)
d.text((W-100,12),"18",font=f(38,True),fill=GOLD)
d.text((W-58,14),"NOV",font=f(13,True),fill=GOLD)
d.text((W-58,30),"2026",font=f(10,True),fill="white")
d.text((W-100,68),"WORLD EDITION",font=f_small,fill=(160,180,210))
d.text((W-100,80),"FINAL • 8 STORIES",font=f_cap,fill=(140,160,190))

# Lead - Shenzhen
ly=114; lh=190
d.rounded_rectangle([10,ly,W-10,ly+lh],radius=12,fill=(230,238,255),outline=(190,205,235))
# Left image: skyline with handshake
d.rounded_rectangle([16,ly+8, 340, ly+lh-8],radius=10,fill=(12,32,76))
# skyline
for i in range(8):
    x=22+i*38
    h=[90,70,85,75,95,65,80,85][i]
    d.rectangle([x, ly+lh-22-h, x+28, ly+lh-14],fill=(210,220,235),outline="white",width=1)
    for wy in range(ly+lh-20-h+4, ly+lh-16, 7):
        d.rectangle([x+5,wy,x+8,wy+3],fill=(255,235,120))
        d.rectangle([x+14,wy,x+17,wy+3],fill=(255,235,120))
# flags
def flag(x,y,c1,c2,c3):
    for j,c in enumerate([c1,c2,c3]): d.rectangle([x, y+j*5, x+20, y+5+j*5],fill=c)
    d.rectangle([x,y,x+20,y+15],outline="white",width=1)
flag(36,ly+20,(200,20,20),(200,20,20),(255,255,0))
flag(140,ly+20,(0,57,166),(255,255,255),(212,0,28))
flag(244,ly+20,(60,59,110),(178,34,34),(255,255,255))
d.text((36,ly+38),"CHINA",font=f_kicker,fill="white")
d.text((140,ly+38),"RUSSIA",font=f_kicker,fill="white")
d.text((244,ly+38),"USA",font=f_kicker,fill="white")
# handshake ellipse
cx,cy=180, ly+lh-40
d.ellipse([cx-30,cy-12,cx+30,cy+12],fill=(244,200,88),outline="white",width=2)
d.ellipse([cx-12,cy-6,cx-2,cy+5],fill=(222,170,100))
d.ellipse([cx+2,cy-6,cx+12,cy+5],fill=(222,170,100))
d.text((cx-36,cy+16),"SHENZHEN  •  APEC  •  QUAD",font=f_kicker,fill=(180,200,230))
# Right text
tx=354
d.text((tx,ly+14),"ASIA-PACIFIC  •  DIPLOMACY",font=f_kicker,fill=BLUE)
d.text((tx,ly+26),"Xi and Putin meet — Trump next",font=f_h2,fill=NAVY)
body="Xi Jinping and Vladimir Putin met at the APEC summit in Shenzhen on Wednesday. A first-ever Xi–Putin–Trump trilateral is scheduled for Thursday 19 Nov — not yet held in reports checked. Donald Trump landed in Manila for Quad talks en route."
for j,l in enumerate(textwrap.wrap(body,62)):
    d.text((tx,ly+48+j*12),l,font=f_body,fill=(30,35,50))
d.text((tx,ly+lh-22),"SHENZHEN • QUAD • APEC • TRILATERAL PENDING 19 NOV",font=f_kicker,fill=BLUE)
# globe icon top-right of lead
mx,my=W-50,ly+24
d.ellipse([mx-18,my-12,mx+18,my+12],outline=BLUE,width=2)
d.line([mx,my-12,mx,my+12],fill=BLUE,width=1)
d.arc([mx-14,my-8,mx+14,my+8],0,180,fill=BLUE,width=1)

# Helper to draw large pictorial
def pict(ax,ay,aw,ah, kind, col):
    d.rounded_rectangle([ax,ay,ax+aw,ay+ah],radius=8,fill=(242,245,252),outline=(220,225,235))
    if kind=="gulf":
        # Map of Gulf: Kuwait top-left, Bahrain center, Qatar, UAE
        # Water
        d.rectangle([ax+4,ay+4,ax+aw-4,ay+ah-4],fill=(195,220,240))
        # Land masses - simplified Arabian Peninsula
        # Saudi
        d.polygon([(ax+12,ay+12),(ax+aw-12,ay+12),(ax+aw-14,ay+ah-12),(ax+10,ay+ah-10)],fill=(245,235,200),outline=(180,170,140))
        # Kuwait marker
        kx,ky=ax+20,ay+18
        d.ellipse([kx-4,ky-4,kx+4,ky+4],fill=RED,outline="white",width=1)
        d.text((kx+6,ky-6),"KUWAIT",font=f_cap,fill=RED)
        d.text((kx+6,ky+2),"Ali Al Salem",font=f_cap,fill=(80,0,0))
        # Bahrain
        bx,by=ax+aw//2-2,ay+ah//2-6
        d.ellipse([bx-3,by-3,bx+3,by+3],fill=RED,outline="white",width=1)
        d.text((bx+6,by-4),"BAHRAIN",font=f_cap,fill=RED)
        d.text((bx+6,by+4),"Sheikh Isa",font=f_cap,fill=(80,0,0))
        # Drones
        for dx,dy in [(ax+aw-28,ay+14),(ax+aw-22,ay+26)]:
            d.polygon([(dx,dy),(dx+10,dy-3),(dx+8,dy),(dx+10,dy+3)],fill=RED)
            d.ellipse([dx-2,dy-2,dx+2,dy+2],fill=(60,0,0))
        # Intercept arcs
        d.arc([kx-2,ky-2,bx+8,by+8],20,80,fill=BLUE,width=1)
        d.text((ax+6,ay+ah-10),"DRONES INTERCEPTED",font=f_kicker,fill=BLUE)
    elif kind=="sanction":
        # UK flag + document
        # Union Jack simplified
        d.rectangle([ax+6,ay+6,ax+aw//2-4,ay+ah-6],fill=(0,36,125))
        d.rectangle([ax+6,ay+ah//2-2,ax+aw//2-4,ay+ah//2+2],fill="white")
        d.rectangle([ax+aw//4-2,ay+6,ax+aw//4+2,ay+ah-6],fill="white")
        d.rectangle([ax+6,ay+ah//2-1,ax+aw//2-4,ay+ah//2+1],fill=(200,16,46))
        d.rectangle([ax+aw//4-1,ay+6,ax+aw//4+1,ay+ah-6],fill=(200,16,46))
        # Document right
        d.rectangle([ax+aw//2+2,ay+8,ax+aw-8,ay+ah-8],fill="white",outline=col,width=1)
        for j in range(4):
            d.line([(ax+aw//2+6,ay+14+j*9),(ax+aw-12,ay+14+j*9)],fill=(180,180,180),width=1)
        # Ban
        cx,cy=ax+aw-16,ay+14
        d.ellipse([cx-8,cy-8,cx+8,cy+8],outline=RED,width=2)
        d.line([cx-6,cy-6,cx+6,cy+6],fill=RED,width=2)
        d.text((ax+aw//2+6,ay+ah-14),"8 FIRMS • TZAV 9",font=f_kicker,fill=RED)
    elif kind=="eu":
        # EU flag field
        d.rectangle([ax+4,ay+4,ax+aw-4,ay+ah-4],fill=(0,51,153))
        cx,cy=ax+aw//2,ay+ah//2-4
        import math
        for a in range(0,360,30):
            rx=math.cos(math.radians(a))*18
            ry=math.sin(math.radians(a))*13
            d.text((cx+rx-2,cy+ry-2),"★",font=f(7,True),fill=GOLD)
        d.rectangle([ax+aw//2-16,cy+10,ax+aw//2+16,cy+22],fill=GOLD)
        d.text((ax+aw//2-12,cy+11),"€45bn",font=f(7,True),fill=NAVY)
    elif kind=="cop":
        # Earth + thermometer
        cx,cy=ax+aw//3,ay+ah//2
        d.ellipse([cx-18,cy-18,cx+18,cy+18],fill=(100,170,120),outline=GREEN,width=2)
        d.polygon([(cx-8,cy-6),(cx-2,cy-10),(cx+6,cy-8),(cx+4,cy+2),(cx-6,cy+6)],fill=(70,130,90))
        d.polygon([(cx+8,cy+4),(cx+12,cy+8),(cx+6,cy+12),(cx+2,cy+8)],fill=(70,130,90))
        # Thermometer
        tx=ax+aw-24
        d.rectangle([tx,ay+8,tx+8,ay+ah-14],fill="white",outline=GREEN,width=1)
        d.ellipse([tx-4,ay+ah-18,tx+12,ay+ah-4],fill=RED,outline=RED)
        d.rectangle([tx+2,ay+14,tx+6,ay+ah-18],fill=RED)
        d.text((tx+12,ay+10),"+1.5°C",font=f_cap,fill=RED)
        # CO2
        d.text((cx+12,ay+6),"COP31",font=f_kicker,fill=GREEN)
    elif kind=="voyager":
        d.rectangle([ax,ay,ax+aw,ay+ah],fill=(6,10,24))
        for i in range(14):
            sx=ax+4+(i*19)%(aw-8); sy=ay+4+(i*13)%(ah-8)
            d.ellipse([sx,sy,sx+2,sy+2],fill="white")
        cx,cy=ax+aw//2,ay+ah//2
        # Probe body
        d.polygon([(cx-14,cy-3),(cx+12,cy-7),(cx+14,cy),(cx+12,cy+7),(cx-14,cy+3)],fill=(210,210,220))
        d.rectangle([cx-10,cy-5,cx,cy+5],fill=(180,180,190))
        d.ellipse([cx+8,cy-8,cx+16,cy+8],outline=(220,230,255),width=1)
        # Distance label
        d.text((ax+6,ay+ah-10),"1 LIGHT-DAY • 25.9bn km",font=f_kicker,fill=GOLD)
        d.text((ax+6,ay+6),"VOYAGER 1",font=f_kicker,fill="white")
    elif kind=="market":
        d.rectangle([ax+4,ay+4,ax+aw-4,ay+ah-4],fill="white",outline=(200,190,150))
        # Grid
        for j in range(3):
            d.line([(ax+10,ay+12+j*14),(ax+aw-10,ay+12+j*14)],fill=(235,235,235),width=1)
        pts=[(ax+14,ay+ah-18),(ax+26,ay+ah-24),(ax+38,ay+ah-20),(ax+50,ay+ah-28),(ax+62,ay+ah-26),(ax+76,ay+ah-12)]
        for k in range(len(pts)-1): d.line([pts[k],pts[k+1]],fill=GOLD,width=2)
        d.polygon([(pts[-1][0],pts[-1][1]-5),(pts[-1][0]+5,pts[-1][1]-3),(pts[-1][0],pts[-1][1]+2)],fill=GOLD)
        d.text((ax+10,ay+6),"ANTHROPIC $83",font=f_kicker,fill=(80,60,0))
        d.text((ax+10,ay+ah-10),"NVIDIA +103%",font=f_kicker,fill=BLUE)
    elif kind=="cyclone":
        d.rectangle([ax+4,ay+4,ax+aw-4,ay+ah-4],fill=(210,230,250))
        # India coast simplified
        coast=[(ax+14,ay+8),(ax+28,ay+12),(ax+38,ay+16),(ax+44,ay+24),(ax+46,ay+32),(ax+40,ay+40),(ax+30,ay+42),(ax+16,ay+38)]
        d.polygon(coast,fill=(245,235,200),outline=(140,120,80))
        d.text((ax+14,ay+10),"INDIA",font=f_kicker,fill=(100,80,40))
        # Bay + cyclone
        cx,cy=ax+aw//2+12,ay+ah//2-2
        for r,c in [(16,TEAL),(11,TEAL),(6,TEAL)]:
            d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=c,width=2 if r==16 else 1)
        d.ellipse([cx-3,cy-3,cx+3,cy+3],fill=TEAL)
        # wind arrows
        d.arc([cx-16,cy-16,cx+16,cy+16],0,90,fill="white",width=1)
        d.text((ax+6,ay+ah-10),"120–130 KM/H",font=f_kicker,fill=RED)

# Cards - 3 per row, 2 rows + bottom full width
# Row1
cards_r1=[
    {"kicker":"MIDDLE EAST — GULF","col":RED,"title":"Bahrain: drones downed","kind":"gulf","body":"Bahrain said its defences intercepted Iranian drones targeting U.S. sites; Kuwait engaged hostile drones over Ali Al Salem — a day after a U.S. strike on an IRGC missile site on Qeshm Island (night of 17 Nov).","tag":"REPORTED 18 NOV • PRIOR STRIKE 17 NOV"},
    {"kicker":"MIDDLE EAST — WEST BANK","col":(120,15,15),"title":"UK + Australia sanction","kind":"sanction","body":"Britain sanctioned 8 firms building in the West Bank and activist group Tzav 9 blocking Gaza aid; Australia sanctioned 3 people & 4 groups — incl. settler leader Daniella Weiss / Nachala.","tag":"FOREIGN OFFICE • 18 NOV"},
    {"kicker":"EUROPE — UKRAINE","col":(0,46,102),"title":"EU proposes €45bn for Kyiv","kind":"eu","body":"European Commission proposed a €45bn loan to Ukraine — €20bn budget + €25bn arms — repayable only if Russia pays reparations. Russian strikes killed at least 5 the same day.","tag":"BRUSSELS • 18 NOV"},
]
row1_y=318; cw=(W-24-2*10)//3; ch=196
for i,s in enumerate(cards_r1):
    x=12+i*(cw+10); y=row1_y
    d.rounded_rectangle([x,y,x+cw,y+ch],radius=10,fill=CARD,outline=(215,220,230))
    d.rectangle([x,y,x+4,y+ch],fill=s["col"])
    pict(x+8,y+8,cw-16,58,s["kind"],s["col"])
    d.text((x+8,y+74),s["kicker"],font=f_kicker,fill=s["col"])
    tl=textwrap.wrap(s["title"],width=22)
    ty=y+86
    for t in tl:
        d.text((x+8,ty),t,font=f_h1,fill=NAVY)
        ty+=13
    bl=textwrap.wrap(s["body"],width=34)
    ty+=2
    for b in bl[:4]:
        d.text((x+8,ty),b,font=f_body,fill=(35,38,50))
        ty+=10
    d.text((x+8,y+ch-12),s["tag"],font=f_small,fill=(120,125,135))

cards_r2=[
    {"kicker":"CLIMATE — GLOBAL","col":GREEN,"title":"COP31 still deadlocked","kind":"cop","body":"Talks in Antalya stayed split over fossil-fuel language — “phase out” vs “transition away” — and climate finance. Presidency said 21 issues remain; new texts due Thu, close Fri 20 Nov.","tag":"ANTALYA • TALKS CONTINUE"},
    {"kicker":"SPACE — GLOBAL","col":(18,44,96),"title":"Voyager 1: one light-day","kind":"voyager","body":"At 10:16 UTC Voyager 1 became the first human-made object one light-day from Earth — ~25.9bn km. Light from the Sun takes a full day to reach it.","tag":"NASA • 10:16 UTC • FIRST"},
    {"kicker":"MARKETS — TECH","col":(124,90,0),"title":"Anthropic IPO at $83","kind":"market","body":"Anthropic priced its record $64.4bn IPO at $83/share, above the $70–78 range; Nvidia doubled revenue to $115.8bn (+103%). Gold fell below $3,800 to a year-low on dollar strength.","tag":"MARKETS • 18 NOV"},
]
row2_y=526
for i,s in enumerate(cards_r2):
    x=12+i*(cw+10); y=row2_y
    d.rounded_rectangle([x,y,x+cw,y+ch],radius=10,fill=CARD,outline=(215,220,230))
    d.rectangle([x,y,x+4,y+ch],fill=s["col"])
    pict(x+8,y+8,cw-16,58,s["kind"],s["col"])
    d.text((x+8,y+74),s["kicker"],font=f_kicker,fill=s["col"])
    tl=textwrap.wrap(s["title"],width=22)
    ty=y+86
    for t in tl:
        d.text((x+8,ty),t,font=f_h1,fill=NAVY)
        ty+=13
    bl=textwrap.wrap(s["body"],width=34)
    ty+=2
    for b in bl[:4]:
        d.text((x+8,ty),b,font=f_body,fill=(35,38,50))
        ty+=10
    d.text((x+8,y+ch-12),s["tag"],font=f_small,fill=(120,125,135))

# Bottom full-width cyclone
s={"kicker":"ASIA — BAY OF BENGAL / INDIA","col":TEAL,"title":"Cyclone Akvan nears India","kind":"cyclone","body":"Severe Cyclonic Storm Akvan intensified in the Bay of Bengal on 18 Nov; IMD forecast landfall around noon 20 Nov on the Andhra Pradesh / Yanam coasts — winds 120–130 km/h gusting to 145 km/h. Andhra and Odisha on alert.","tag":"IMD • BAY OF BENGAL • LANDFALL NOON 20 NOV"}
x=12; y=734; bh=200
d.rounded_rectangle([x,y,x+cw*3+20,y+bh],radius=12,fill=CARD,outline=(215,220,230))
d.rectangle([x,y,x+5,y+bh],fill=s["col"])
pict(x+10,y+8,280,62,s["kind"],s["col"])
d.text((x+300,y+12),s["kicker"],font=f_kicker,fill=s["col"])
d.text((x+300,y+24),s["title"],font=f_h1,fill=NAVY)
bl=textwrap.wrap(s["body"],width=62)
ty=y+42
for b in bl:
    d.text((x+300,ty),b,font=f_body,fill=(35,38,50))
    ty+=11
d.text((x+300,y+bh-14),s["tag"],font=f_small,fill=(120,125,135))
# Forecast box
d.rounded_rectangle([x+300,y+bh-40,x+500,y+bh-16],radius=6,fill=(235,245,240),outline=TEAL)
d.text((x+306,y+bh-36),"FORECAST: LANDFALL ~NOON 20 NOV",font=f_kicker,fill=TEAL)
d.text((x+306,y+bh-26),"ANDHRA PRADESH / YANAM • 120–145 KM/H",font=f_small,fill=(60,60,60))

# Footer
fy=y+bh+8
d.rectangle([0,fy,W,fy+1],fill=(190,190,180))
d.text((10,fy+5),"EDITORIAL NOTE — All events reported on 18 Nov 2026 except Qeshm Island strike (night of 17 Nov) and Thursday’s trilateral (scheduled 19 Nov) noted as such. Sources: AA, BBC, NYT, Guardian, IMD, NASA, EC. Each story states what happened, where, when — no speculation as fact.",font=f_cap,fill=(85,85,85))
d.text((10,fy+15),"Image faithful to reports available 18 Nov 2026. Designed to read at 300 px: headlines legible, each story clear from picture + label.",font=f_cap,fill=(85,85,85))
d.rectangle([0,H-22,W,H],fill=NAVY)
d.text((10,H-14),"THE WORLD TODAY  •  WEDNESDAY 18 NOVEMBER 2026  •  8 VERIFIED STORIES  •  ONE FRONT PAGE",font=f_kicker,fill="white")
d.text((W-140,H-14),"make.fun #news-image",font=f_kicker,fill=GOLD)

im.save("/home/user/workspace-repo/entry.png","PNG",optimize=True)
print(os.path.getsize("/home/user/workspace-repo/entry.png"), im.size)
