# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Вага")

# -*- acsection: main -*-
prozor.fill(pg.Color("green")) # bojimo pozadinu ekrana u zeleno

pg.draw.line(prozor, pg.Color("brown"), (60, 100), (240,  100), 2)                              # letva
pg.draw.polygon(prozor, pg.Color("brown"), [(100, 120), (150, 100), (200, 120), (100, 120)])   # oslonac
pg.draw.polygon(prozor, pg.Color("brown"), [( 30, 200), ( 60, 100), ( 90, 200), ( 30, 200)], 2)  # levi tas
pg.draw.polygon(prozor, pg.Color("brown"), [(210, 200), (240, 100), (270, 200), (210, 200)], 2) # desni tas

# -*- acsection: after-main -*-
petljapg.wait_loop()
