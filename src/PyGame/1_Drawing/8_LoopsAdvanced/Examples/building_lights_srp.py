# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Зграда - светла")

# -*- acsection: main -*-
prozor.fill(pg.Color("lightgray")) # bojimo pozadinu ekrana u svetlo sivo

pg.draw.rect(prozor, pg.Color("darkgray"), (120, 50, 60, 140))    # zgrada

y = pg.Color('yellow')
b = pg.Color('black')
boja = [y, y, y, b, b, y, y, y, b, b]
for i in range(5):
    pg.draw.rect(prozor, boja[2*i],   (130, 60 + 20 * i, 15, 15)) # levi prozor
    pg.draw.rect(prozor, boja[2*i+1], (155, 60 + 20 * i, 15, 15)) # desni prozor

pg.draw.rect(prozor, pg.Color("black"),  (140, 160, 20, 30))      # kapija

# -*- acsection: after-main -*-
petljapg.wait_loop()
