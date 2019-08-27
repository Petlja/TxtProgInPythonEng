# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Концентрични кругови")
# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))

centar = (sirina // 2, visina // 2) # centar kruga je u centru prozora
br_krugova = 6
r_korak = sirina / (2*br_krugova)

for i in range(1, br_krugova + 1):
    pg.draw.circle(prozor, pg.Color("red"), centar, round(i * r_korak), 2)

# -*- acsection: after-main -*-
petljapg.wait_loop()
