# -*- acsection: general-init -*-
import random
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()
# podešavamo naslov prozora
pg.display.set_caption("Фрактал - тепих Сјерпинског")
# otvaramo prozor dimenzije 243x243
a = 3**5
(sirina, visina) = (a, a)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

def kvadrat(x, y, d):
    d3 = d // 3
    if d <= 3:
        pg.draw.rect(prozor, pg.Color('yellow'), (x - d3, y - d3, d-1, d-1), 1)
    else:
        for dx, dy in ((-d3, -d3), (0, -d3), (d3, -d3), (-d3, 0), (d3, 0), (-d3, d3), (0, d3), (d3, d3)):
            kvadrat(x + dx, y + dy, d3)

prozor.fill(pg.Color("black")) # bojimo pozadinu u crno
kvadrat(a // 2, a // 2, a)
# -*- acsection: after-main -*-
# ažuriramo prikaz sadržaja ekrana
pg.display.update()

# čekamo da korisnik isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass
    
# isključivanje rada biblioteke PyGame
pg.quit()
