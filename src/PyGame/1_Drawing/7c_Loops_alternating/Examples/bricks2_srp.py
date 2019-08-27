# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Цигле")

# -*- acsection: main -*-
prozor.fill(pg.Color("red"))
a_cigle, h_cigle = 80, 40
for y0 in range(0, visina, 2 * h_cigle):
    for x0 in range(0, sirina, a_cigle):
        #crtamo prvu ciglu
        pg.draw.rect(prozor, pg.Color("black"), (x0, y0, a_cigle, h_cigle), 1)
        
        # druga cigla je u sledecem redu, pomerena za pola sirine
        x1, y1 = x0 - a_cigle//2, y0 + h_cigle 
        pg.draw.rect(prozor, pg.Color("black"), (x1, y1, a_cigle, h_cigle), 1)

# -*- acsection: after-main -*-
petljapg.wait_loop()
