# -*- acsection: general-init -*-
import pygame as pg, random

pg.init()   # uključujemo rad biblioteke PyGame

pg.display.set_caption("Кућица")

# otvaramo prozor
(sirina, visina) = (300, 300)
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))


# -*- acsection: main -*-
pg.draw.rect(prozor, pg.Color("yellow"), (60, 120, 180, 160))
pg.draw.polygon(prozor, pg.Color("red"), [(60, 120), (150, 20), (240, 120)])
pg.draw.rect(prozor, pg.Color("skyblue"), (80, 140, 50, 50))
pg.draw.line(prozor, pg.Color("black"), (80, 165), (130, 165))
pg.draw.line(prozor, pg.Color("black"), (105, 140), (105, 190))
pg.draw.rect(prozor, pg.Color("skyblue"), (170, 140, 50, 50))
pg.draw.line(prozor, pg.Color("black"), (170, 165), (220, 165))
pg.draw.line(prozor, pg.Color("black"), (195, 140), (195, 190))
pg.draw.rect(prozor, pg.Color("brown"), (120, 200, 60, 80))


# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()

