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
for y0 in range(-17, visina, 102):
    for x0 in range(-10, sirina, 60):
        crtaj_mnogougao(sestougao, pg.Color("blue"),   x0, y0)
        crtaj_mnogougao(sestougao, pg.Color("yellow"), x0, y0 + 34)
        crtaj_mnogougao(sestougao, pg.Color("green"),  x0, y0 + 68)
        crtaj_mnogougao(sestougao, pg.Color("green"),  x0 + 30, y0 + 17)
        crtaj_mnogougao(sestougao, pg.Color("blue"),   x0 + 30, y0 + 51)
        crtaj_mnogougao(sestougao, pg.Color("yellow"), x0 + 30, y0 + 85)

# -*- acsection: after-main -*-
petljapg.wait_loop()
