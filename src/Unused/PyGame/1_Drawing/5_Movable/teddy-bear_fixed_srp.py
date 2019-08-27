# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Медведић")
# otvaramo prozor dimenzije 500x300
(sirina, visina) = (500, 300)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-
# bojimo pozadinu prozora u belo
prozor.fill(pg.Color("white"))

def uokviren_krug(prozor, boja, centar, poluprecnik):
    pg.draw.circle(prozor, boja, centar, poluprecnik)
    pg.draw.circle(prozor, pg.Color("black"), centar, poluprecnik, 1)
   
uokviren_krug(prozor, pg.Color("yellow"), (190,  80),  45) # levo uvo
uokviren_krug(prozor, pg.Color("yellow"), (310,  80),  45) # desno uvo
uokviren_krug(prozor, pg.Color("yellow"), (250, 150), 100) # glava
uokviren_krug(prozor, pg.Color("yellow"), (250, 200),  50) # njuska
uokviren_krug(prozor, pg.Color("black"),  (200, 120),  15) # levo oko
uokviren_krug(prozor, pg.Color("black"),  (300, 120),  15) # desno oko
uokviren_krug(prozor, pg.Color("black"),  (250, 170),  15) # vrh njuske

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()

