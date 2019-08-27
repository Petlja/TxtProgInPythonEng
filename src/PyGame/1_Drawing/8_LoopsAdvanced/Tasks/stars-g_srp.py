# -*- acsection: general-init -*-
import pygame as pg, petljapg
sirina, visina = 400, 400
prozor = petljapg.open_window(sirina, visina, "Ноћно небо")
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
petljapg.wait_loop()
