# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Стрелице")
# -*- acsection: main -*-
def draw_polygon(points, color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points)

arrow = [(0, 10), (40, 10), (40, 0), (60, 20), (40, 40), (40, 30), (0, 30)]
arrow_length, arrow_height = 60, 40
canvas.fill(pg.Color("white"))
for y0 in range(0, height, arrow_height):
    for x0 in range(0, width, arrow_length):
        draw_polygon(arrow, pg.Color("black"), x0, y0)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
