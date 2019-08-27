# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "fence")

# -*- acsection: main -*-
canvas.fill(pg.Color("skyblue")) 
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass

pg.draw.line(canvas, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(canvas, pg.Color('brown'), ( 10, 250), (290, 250), 10)
picket = [(20, 80), (30, 70), (40, 80), (40, 270), (20, 270)]
for i in range(7):
    pg.draw.polygon(canvas, pg.Color('brown'), [(x + 40*i, y) for (x,y) in picket])

# -*- acsection: after-main -*-
pygamebg.wait_loop()
