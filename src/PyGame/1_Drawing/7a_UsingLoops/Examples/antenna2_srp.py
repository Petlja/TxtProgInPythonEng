# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Антена")

# -*- acsection: main -*-
prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo

pg.draw.line(prozor, pg.Color('black'), (150,  50), (150, 250), 4)
for i in range(6):
    pg.draw.line(prozor, pg.Color('black'), (120 - 10 * i,  75 + 25 * i), (180 +  10 * i,  75 + 25 * i), 1 + i//2)

# -*- acsection: after-main -*-
petljapg.wait_loop()
