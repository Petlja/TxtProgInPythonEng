# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Саће у боји")

# -*- acsection: main -*-
def crtaj_mnogougao(tacke, boja, x0, y0):
    pomerene_tacke = []
    for x, y in tacke:
        pomerene_tacke.append((x+x0, y+y0))
    pg.draw.polygon(prozor, boja, pomerene_tacke)

sestougao = [(10, 0), (30, 0), (40, 17), (30, 34), (10, 34), (0, 17)]
boja = [pg.Color("blue"), pg.Color("yellow"), pg.Color("green"), pg.Color("blue"), pg.Color("yellow")]
i_boja = 0
for y0 in range(-17, visina, 34):
    for x0 in range(-10, sirina, 60):
        crtaj_mnogougao(sestougao, boja[i_boja],   x0, y0)
        crtaj_mnogougao(sestougao, boja[i_boja+2],  x0 + 30, y0 + 17)
    i_boja = (i_boja + 1) % 3

# -*- acsection: after-main -*-
petljapg.wait_loop()
