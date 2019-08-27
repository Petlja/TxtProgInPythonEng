# -*- acsection: general-init -*-
import pygame as pg

# uključivanje rada biblioteke PyGame
pg.init()

# podešavamo naslov prozora
pg.display.set_caption("Ноћно небо")
# ukljucujemo prozor dimenzije 400x400 piksela
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
# -*- acsection: main -*-

def zvezdica(x, y):
    r = 10
    d = 2
    pg.draw.line(prozor, pg.Color("white"), (x-r, y), (x+r, y), d)
    pg.draw.line(prozor, pg.Color("white"), (x, y-r), (x, y+r), d)
    pg.draw.line(prozor, pg.Color("white"), (x-r/2, y-r/2), (x+r/2, y+r/2), d)
    pg.draw.line(prozor, pg.Color("white"), (x+r/2, y-r/2), (x-r/2, y+r/2), d)

prozor.fill(pg.Color("black"))
brojZvezdica = 10
razmak_x = sirina // (brojZvezdica + 1)
razmak_y = visina // (brojZvezdica + 1)
for i in range(brojZvezdica):
    for j in range(brojZvezdica):
        x = (i + 1) * razmak_x
        y = (j + 1) * razmak_y
        zvezdica(x, y)

# -*- acsection: after-main -*-
# prikazujemo crtez na ekranu
pg.display.update()

# program radi sve dok ne nastupi dogadjaj pg.QUIT
while pg.event.wait().type != pg.QUIT:
    pass

# iskljucivanje rada biblioteke PyGame
pg.quit()

