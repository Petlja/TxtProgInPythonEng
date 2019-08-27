# -*- acsection: general-init -*-
import pygame as pg, petljapg
(sirina, visina) = (300, 300)
prozor = petljapg.open_window(sirina, visina, "Мердевине")

# -*- acsection: main -*-
prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

pg.draw.line(prozor, pg.Color("brown"), (100, 10), (100, visina - 10), 10)    # leva strana
pg.draw.line(prozor, pg.Color("brown"), (200, 10), (200, visina - 10), 10)    # desna strana

for i in range(1, 6):
    pg.draw.line(prozor, pg.Color("brown"), (100, i * 50), (200, i * 50), 10) # precaga

# -*- acsection: after-main -*-
petljapg.wait_loop()
