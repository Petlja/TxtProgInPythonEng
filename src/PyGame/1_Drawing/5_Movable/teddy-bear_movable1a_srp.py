# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (500, 300)
prozor = petljapg.open_window(sirina, visina, "Медведић")
# -*- acsection: main -*-

# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

def uokviren_krug(prozor, boja, centar, poluprecnik):
    pg.draw.circle(prozor, boja, centar, poluprecnik)
    pg.draw.circle(prozor, pg.Color("black"), centar, poluprecnik, 1)

def crtaj_medu(cx, cy):
    uokviren_krug(prozor, pg.Color("yellow"), (cx - 60,  cy - 70),  45) # levo uvo
    uokviren_krug(prozor, pg.Color("yellow"), (cx + 60,  cy - 70),  45) # desno uvo
    uokviren_krug(prozor, pg.Color("yellow"), (cx,       cy),      100) # glava
    uokviren_krug(prozor, pg.Color("yellow"), (cx,       cy + 50),  50) # njuska
    uokviren_krug(prozor, pg.Color("black"),  (cx - 50,  cy - 30),  15) # levo oko
    uokviren_krug(prozor, pg.Color("black"),  (cx + 50,  cy - 30),  15) # desno oko
    uokviren_krug(prozor, pg.Color("black"),  (cx,       cy + 20),  15) # vrh njuske

crtaj_medu(sirina // 2, visina // 2)

# -*- acsection: after-main -*-
petljapg.wait_loop()
