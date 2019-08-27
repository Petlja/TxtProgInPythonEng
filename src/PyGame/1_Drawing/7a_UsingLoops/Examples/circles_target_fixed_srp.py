# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Концентрични кругови")
# -*- acsection: main -*-

# bojimo pozadinu prozora u belu
prozor.fill(pg.Color("white"))

# centar kruga je u centru prozora
centar = (sirina // 2, visina // 2)

# crtamo krugove
# poluprecnik se menja od 25 do 150, sa korakom 25
pg.draw.circle(prozor, pg.Color("red"), centar,  25, 2)
pg.draw.circle(prozor, pg.Color("red"), centar,  50, 2)
pg.draw.circle(prozor, pg.Color("red"), centar,  75, 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 100, 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 125, 2)
pg.draw.circle(prozor, pg.Color("red"), centar, 150, 2)
# -*- acsection: after-main -*-
petljapg.wait_loop()
