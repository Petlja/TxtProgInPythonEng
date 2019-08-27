# -*- acsection: general-init -*-
import pygame as pg

pg.init()                          # uključivanje rada biblioteke PyGame
pg.display.set_caption("Вежба")  # podešavamo naslov prozora
(sirina, visina) = (500, 300)      # otvaramo prozor dimenzije 500x300
prozor = pg.display.set_mode((sirina, visina))

# -*- acsection: main -*-
prozor.fill(pg.Color("gray"))

for x in range(10, sirina, 20):
    pg.draw.line(prozor, pg.Color("black"), (x, 10), (x, visina - 10), 1)

print()
for y in range(10, visina, 20):
    pg.draw.line(prozor, pg.Color("black"), (10, y), (sirina - 10, y), 1)

# -*- acsection: after-main -*-
pg.display.update()   # prikazujemo nacrtano na ekranu

# petlja obrade događaja - čekamo dok korisnik ne isključi prozor
while pg.event.wait().type != pg.QUIT:
    pass

# isključivanje rada biblioteke PyGame
pg.quit()
