# -*- acsection: general-init -*-
import pygame as pg, petljapg
sirina, visina = 300, 300
prozor = petljapg.open_window(sirina, visina, "Коцке")
# -*- acsection: main -*-

def crtaj_mnogougao(temena, boja, x0, y0):
    pomerena_temena = []
    for x, y in temena:
        pomerena_temena.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerena_temena, 1)

sestougao = [(20, 0), (60, 0), (80, 34), (60, 68), (20, 68), (0, 34)]
prozor.fill(pg.Color("goldenrod"))
for y0 in range(-34, visina, 34):
    for x0 in range(-20, sirina, 60):
        crtaj_mnogougao(sestougao, pg.Color("brown"), x0, y0)
        crtaj_mnogougao(sestougao, pg.Color("brown"), x0 + 30, y0 + 17)

# -*- acsection: after-main -*-
petljapg.wait_loop()
