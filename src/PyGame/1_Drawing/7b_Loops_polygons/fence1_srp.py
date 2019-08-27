# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Ограда")

# -*- acsection: main -*-
prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 300, 100))  # trava

pg.draw.line(prozor, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(prozor, pg.Color('brown'), ( 10, 250), (290, 250), 10)
temena = [(20, 80), (30, 70), (40, 80), (40, 270), (20, 270)]
for i in range(7):
    pg.draw.polygon(prozor, pg.Color('brown'), [(x + 40*i, y) for (x,y) in temena])

# -*- acsection: after-main -*-
petljapg.wait_loop()
