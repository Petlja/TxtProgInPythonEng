# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "Fence")
# -*- acsection: main -*-
canvas.fill(pg.Color("skyblue"))
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass

pg.draw.line(canvas, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(canvas, pg.Color('brown'), ( 10, 250), (290, 250), 10)
for x in range(20, 300, 40):
    pg.draw.polygon(canvas, pg.Color('brown'), [(x, 80), (x + 10, 70), (x + 20, 80), (x + 20, 270), (x, 270)])

# -*- acsection: after-main -*-
pygamebg.wait_loop()
