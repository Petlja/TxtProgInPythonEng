# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Cubes")
# -*- acsection: main -*-

def draw_polygon(points, color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points, 1)

hexagon = [(20, 0), (60, 0), (80, 34), (60, 68), (20, 68), (0, 34)]
canvas.fill(pg.Color("goldenrod"))
for y0 in range(-34, height, 34):
    for x0 in range(-20, width, 60):
        draw_polygon(hexagon, pg.Color("brown"), x0, y0)
        draw_polygon(hexagon, pg.Color("brown"), x0 + 30, y0 + 17)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
