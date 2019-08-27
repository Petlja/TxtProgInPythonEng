# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (500, 300)
prozor = petljapg.open_window(sirina, visina, "Медведић")
# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))
zuta = pg.Color("yellow")
crna = pg.Color("black")

def crtaj_medu(cx, cy):
    meda = (
        #boja, (  x,   y),  r
        (zuta, (-60, -60),  45), # levo uvo
        (zuta, ( 60, -60),  45), # desno uvo
        (zuta, (  0,   0), 100), # glava
        (zuta, (  0,  50),  50), # njuska
        (crna, (-50, -30),  15), # levo oko
        (crna, ( 50, -30),  15), # desno oko
        (crna, (  0,  20),  15), # vrh njuske
    )
    for boja, (dx, dy), poluprecnik in meda:
        centar = (cx + dx, cy + dy)
        pg.draw.circle(prozor, boja, centar, poluprecnik)
        pg.draw.circle(prozor, crna, centar, poluprecnik, 1)

crtaj_medu(sirina // 2, visina // 2)

# -*- acsection: after-main -*-
petljapg.wait_loop()
