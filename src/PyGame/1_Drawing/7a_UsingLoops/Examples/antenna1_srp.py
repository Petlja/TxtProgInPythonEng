# -*- acsection: general-init -*-
import pygame as pg, petljapg
prozor = petljapg.open_window(300, 300, "Антена")

# -*- acsection: main -*-
prozor.fill(pg.Color("skyblue")) # bojimo pozadinu ekrana u nebo-plavo

pg.draw.line(prozor, pg.Color('black'), (150,  50), (150, 250), 4)
x1, x2, y, debljina = 120, 180, 75, 1.0
for i in range(6):
    pg.draw.line(prozor, pg.Color('black'), (x1, y), (x2, y), int(debljina))
    x1 -= 10
    x2 += 10
    y += 25
    debljina += 0.5

# -*- acsection: after-main -*-
petljapg.wait_loop()
