# -*- acsection: general-init -*-
import pygame as pg, pygamebg
canvas = pygamebg.open_window(300, 300, "fence")
# -*- acsection: main -*-

canvas.fill(pg.Color("skyblue")) # paint background
pg.draw.rect(canvas, pg.Color("green"), (0, 200, 300, 100))  # grass

pg.draw.line(canvas, pg.Color('brown'), ( 10, 100), (290, 100), 10)
pg.draw.line(canvas, pg.Color('brown'), ( 10, 250), (290, 250), 10)
def draw_polygon(points, color, x0, y0):
    shifted_points = [(x+x0, y+y0) for x, y in points]
    pg.draw.polygon(canvas, color, shifted_points)

picket = [(0, 80), (10, 70), (20, 80), (20, 270), (0, 270)]
for x0 in range(20, 300, 40):
    draw_polygon(picket, pg.Color('brown'), x0, 0)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
