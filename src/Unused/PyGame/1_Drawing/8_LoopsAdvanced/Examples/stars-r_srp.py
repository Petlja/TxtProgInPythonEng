# -*- acsection: general-init -*-
import pygame as pg, random

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Број пи")
# ukljucujemo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

def zvezdica(x, y, r):
    d = 2
    pg.draw.line(prozor, pg.Color("white"), (x-r, y), (x+r, y), d)
    pg.draw.line(prozor, pg.Color("white"), (x, y-r), (x, y+r), d)
    pg.draw.line(prozor, pg.Color("white"), (x-r/2, y-r/2), (x+r/2, y+r/2), d)
    pg.draw.line(prozor, pg.Color("white"), (x+r/2, y-r/2), (x-r/2, y+r/2), d)

# bojimo pozadinu prozora u crno
prozor.fill(pg.Color("black"))

broj_zvezdica = 10
razmak_x = sirina // (broj_zvezdica + 1)
razmak_y = visina // (broj_zvezdica + 1)
for i in range(broj_zvezdica):
    for j in range(broj_zvezdica):
        x = (i + 1) * razmak_x + random.randint(-razmak_x//2, razmak_x//2)
        y = (j + 1) * razmak_y + random.randint(-razmak_y//2, razmak_y//2)
        r = random.randint(10, 16)
        zvezdica(x, y, r)

# -*- acsection: after-main -*-
# prikazujemo crtez na ekranu
pg.display.update()

# program radi sve dok ne nastupi dogadjaj pg.QUIT
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucivanje rada biblioteke PyGame
pg.quit()

