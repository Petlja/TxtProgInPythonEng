# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Стрелице")
# -*- acsection: main -*-
def crtaj_mnogougao(temena, boja, x0, y0):
    pomerena_temena = []
    for x, y in temena:
        pomerena_temena.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerena_temena)

strelica = [(0, 10), (40, 10), (40, 0), (60, 20), (40, 40), (40, 30), (0, 30)]
a_strelice, h_strelice = 60, 40
prozor.fill(pg.Color("white"))
for y0 in range(0, visina, h_strelice):
    for x0 in range(0, sirina, a_strelice):
        crtaj_mnogougao(strelica, pg.Color("black"), x0, y0)

# -*- acsection: after-main -*-
petljapg.wait_loop()
