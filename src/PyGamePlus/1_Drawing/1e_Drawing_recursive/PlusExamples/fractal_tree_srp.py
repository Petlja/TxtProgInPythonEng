# -*- acsection: general-init -*-
import pygame as pg
import math

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Фрактал - дрво")
# otvaramo prozor dimenzije 800x600
(sirina, visina) = (800, 600)
prozor = pg.display.set_mode((sirina,visina))

def crtaj_drvo(x, y, d, pravac):
    if  d > 2:
        x1 = x + d * math.cos(pravac)
        y1 = y - d * math.sin(pravac)
        pg.draw.line(prozor, pg.Color("yellow"), (x, y), (x1, y1) )
        crtaj_drvo(x1, y1, d * 0.7, pravac - 0.5)
        crtaj_drvo(x1, y1, d * 0.7, pravac + 0.5)
  
prozor.fill(pg.Color("black")) # bojimo pozadinu u crno
crtaj_drvo(0.5 * sirina, 0.8 * visina, 100, 0.5 * math.pi)

# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass
    
# isključivanje rada biblioteke PyGame
pg.quit()
