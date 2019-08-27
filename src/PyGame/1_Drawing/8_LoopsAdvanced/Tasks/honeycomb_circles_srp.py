# -*- acsection: general-init -*-
import pygame as pg, petljapg
sirina, visina = 300, 300
prozor = petljapg.open_window(sirina, visina, "Саће - кругови")
# -*- acsection: main -*-

prozor.fill((255,255,128))
for y0 in range(-17, visina, 34):
    for x0 in range(-10, sirina, 60):
        pg.draw.circle(prozor, pg.Color("goldenrod"), (x0, y0), 16)
        pg.draw.circle(prozor, pg.Color("goldenrod"), (x0 + 30, y0 + 17), 16)

# -*- acsection: after-main -*-
petljapg.wait_loop()
