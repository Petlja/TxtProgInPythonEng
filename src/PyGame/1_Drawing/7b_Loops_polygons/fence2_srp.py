# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Ограда")

# -*- acsection: main -*-
prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 300, 100))  # trava

pg.draw.line(prozor, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(prozor, pg.Color('brown'), ( 10, 250), (290, 250), 10)
for x in range(20, 300, 40):
    pg.draw.polygon(prozor, pg.Color('brown'), [(x, 80), (x + 10, 70), (x + 20, 80), (x + 20, 270), (x, 270)])

# -*- acsection: after-main -*-
petljapg.wait_loop()
