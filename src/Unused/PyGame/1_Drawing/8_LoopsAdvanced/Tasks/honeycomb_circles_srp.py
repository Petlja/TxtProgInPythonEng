# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-

prozor.fill((255,255,128))
for y0 in range(-17, visina, 34):
    for x0 in range(-10, sirina, 60):
        pg.draw.circle(prozor, pg.Color("goldenrod"), (x0, y0), 16)
        pg.draw.circle(prozor, pg.Color("goldenrod"), (x0 + 30, y0 + 17), 16)

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
