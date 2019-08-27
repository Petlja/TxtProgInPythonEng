# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Кућа")

# -*- acsection: main -*-
prozor.fill(pg.Color("darkgreen")) # bojimo pozadinu ekrana u tamno zeleno

pg.draw.polygon(prozor, pg.Color("red"), [(50, 150), (120, 100), (190, 150)]) # krov
pg.draw.rect(prozor, pg.Color("khaki"), ( 50, 150, 140, 100))  # kuca
pg.draw.rect(prozor, pg.Color("brown"), ( 60, 170,  30,  30))  # levi prozor
pg.draw.rect(prozor, pg.Color("brown"), (150, 170,  30,  30))  # desni prozor
pg.draw.rect(prozor, pg.Color("brown"), (100, 180,  40,  70))  # vrata

# -*- acsection: after-main -*-
petljapg.wait_loop()
