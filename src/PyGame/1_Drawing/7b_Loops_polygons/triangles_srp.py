# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Троуглови")

# -*- acsection: main -*-
def crtaj_mnogougao(temena, boja, x0, y0, debljina):
    pomerena_temena = []
    for x, y in temena:
        pomerena_temena.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerena_temena, debljina)

trougao = [(10, 0), (0, 17), (20, 17)]
prozor.fill(pg.Color("goldenrod"))
for y0 in range(0, visina, 17):
    for x0 in range(0, sirina, 20):
        crtaj_mnogougao(trougao, pg.Color("brown"), x0, y0, 0)

# -*- acsection: after-main -*-
petljapg.wait_loop()
