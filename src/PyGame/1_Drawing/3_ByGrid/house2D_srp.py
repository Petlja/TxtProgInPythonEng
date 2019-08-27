# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Кућа")

# -*- acsection: main -*-
prozor.fill(pg.Color("lightblue")) # bojimo pozadinu ekrana u svetlo plavo

pg.draw.circle(prozor, pg.Color("orange"), (250, 180), 30)   # sunce
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 300, 100))  # trava
pg.draw.rect(prozor, pg.Color("brown"), (50, 150, 150, 100)) # kuca
pg.draw.polygon(prozor, pg.Color("red"), [(50, 150), (125, 100), (200, 150)]) # krov

# -*- acsection: after-main -*-
petljapg.wait_loop()
