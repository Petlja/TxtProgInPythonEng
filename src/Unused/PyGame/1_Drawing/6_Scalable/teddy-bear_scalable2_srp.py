# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Медведић")
# otvaramo prozor dimenzije 300x300
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-
# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
zuta = pg.Color("yellow")
crna = pg.Color("black")

def crtaj_medu(cx, cy, a):
    meda = (
        #boja, (  x,   y),  r
        (zuta, (-12, -12),  9), # levo uvo
        (zuta, ( 12, -12),  9), # desno uvo
        (zuta, (  0,   0), 20), # glava
        (zuta, (  0,  10), 10), # njuska
        (crna, (-10,  -6),  3), # levo oko
        (crna, ( 10,  -6),  3), # desno oko
        (crna, (  0,   4),  3), # vrh njuske
    )
    for boja, (dx, dy), poluprecnik in meda:
        centar = (cx + dx*a, cy + dy*a)
        pg.draw.circle(prozor, boja, centar, a*poluprecnik)
        pg.draw.circle(prozor, crna, centar, a*poluprecnik, 1)

crtaj_medu(sirina // 2, visina // 2, 6)

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
