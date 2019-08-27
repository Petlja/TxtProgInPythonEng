# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(20, 40, "Мердевине")

# -*- acsection: main -*-
prozor.fill(pg.Color("white")) # bojimo pozadinu ekrana u belo

pg.draw.line(prozor, pg.Color("black"), ( 5, 3), ( 5, 36), 1)  # leva strana
pg.draw.line(prozor, pg.Color("black"), (14, 3), (14, 36), 1)  # desna strana

pg.draw.line(prozor, pg.Color("black"), (5,  9), (14,  9), 1) # precaga
pg.draw.line(prozor, pg.Color("black"), (5, 16), (14, 16), 1) # precaga
pg.draw.line(prozor, pg.Color("black"), (5, 23), (14, 23), 1) # precaga
pg.draw.line(prozor, pg.Color("black"), (5, 30), (14, 30), 1) # precaga

# -*- acsection: after-main -*-
petljapg.wait_loop()
