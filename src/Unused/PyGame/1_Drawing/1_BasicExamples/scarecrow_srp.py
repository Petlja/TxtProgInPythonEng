# -*- acsection: general-init -*-
import math
import pygame as pg

pg.init()                             # uključivanje rada biblioteke PyGame
pg.display.set_caption("Страшило")    # podešavamo naslov prozora
(sirina, visina) = (300, 500)         # zadajemo velicinu prozora
prozor = pg.display.set_mode((sirina, visina))  # otvaramo prozor

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.circle(prozor, pg.Color("black"), (150, 70), 50, 6)        # glava
pg.draw.line(prozor, pg.Color("black"), (150, 120), (150, 300), 6) # telo
pg.draw.line(prozor, pg.Color("black"), (80, 170), (220, 170), 6)  # ruke
pg.draw.line(prozor, pg.Color("black"), (150, 300), (90, 480), 6)  # leva noga
pg.draw.line(prozor, pg.Color("black"), (150, 300), (210, 480), 6) # desna noga

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
