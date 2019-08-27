# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Honeycomb")

# -*- acsection: main -*-
def draw_polygon(points, color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points, 1)

hexagon = [(10, 0), (30, 0), (40, 17), (30, 34), (10, 34), (0, 17)]
canvas.fill(pg.Color("goldenrod"))
for y0 in range(-17, height, 34):
    for x0 in range(-10, width, 60):
        draw_polygon(hexagon, pg.Color("brown"), x0, y0)
        draw_polygon(hexagon, pg.Color("brown"), x0 + 30, y0 + 17)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
