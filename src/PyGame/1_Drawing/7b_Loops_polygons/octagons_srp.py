# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Осмоуглови")
# -*- acsection: main -*-

def crtaj_uokviren_mnogougao(temena, boja, boja_okvir, x0, y0):
    pomerena_temena = []
    for x, y in temena:
        pomerena_temena.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerena_temena)
    pg.draw.polygon(prozor, boja_okvir, pomerena_temena, 2)

osmougao = [(14, 0), (34, 0), (48, 14), (48, 34), (34, 48), (14, 48), (0, 34), (0, 14)]
prozor.fill(pg.Color("yellow"))
for y0 in range(0, visina, 48):
    for x0 in range(0, sirina, 48):
        crtaj_uokviren_mnogougao(osmougao, pg.Color("lightgreen"), pg.Color("red"), x0, y0)

# -*- acsection: after-main -*-
petljapg.wait_loop()
