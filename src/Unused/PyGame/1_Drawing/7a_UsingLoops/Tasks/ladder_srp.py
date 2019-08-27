# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба 2")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

pg.draw.line(prozor, pg.Color("brown"), (100, 10), (100, visina - 10), 10)    # leva strana
pg.draw.line(prozor, pg.Color("brown"), (200, 10), (200, visina - 10), 10)    # desna strana

for i in range(1, 6):
    pg.draw.line(prozor, pg.Color("brown"), (100, i * 50), (200, i * 50), 10) # precaga

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
