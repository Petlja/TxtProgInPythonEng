# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба 4")  # podešavamo naslov prozora
(sirina, visina) = (300, 300)      # otvaramo prozor dimenzije 300x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

for i in range(3):
    pg.draw.rect(prozor, pg.Color("brown"), (100*i + 40, 180, 20, 100))        # stablo
    pg.draw.ellipse(prozor, pg.Color("darkgreen"), (100*i + 10, 50, 80, 150))  # krosnja

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
