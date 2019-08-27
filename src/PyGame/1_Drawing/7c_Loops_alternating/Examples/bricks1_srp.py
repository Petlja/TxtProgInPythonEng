# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Цигле")

# -*- acsection: main -*-
prozor.fill(pg.Color("red"))
a_cigle, h_cigle = 80, 40
x_poc = 0
for y0 in range(0, visina, h_cigle):
    for x0 in range(x_poc, sirina, a_cigle):
        pg.draw.rect(prozor, pg.Color("black"), (x0, y0, a_cigle, h_cigle), 1)
        
    if x_poc == 0:
        x_poc = -a_cigle//2
    else:
        x_poc = 0

# -*- acsection: after-main -*-
petljapg.wait_loop()
