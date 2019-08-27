# -*- acsection: general-init -*-
import pygame as pg, pygamebg
(width, height) = (300, 300)
canvas = pygamebg.open_window(width, height, "Triangles")

# -*- acsection: main -*-
def draw_polygon(points, boja, x0, y0, thickness):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, boja, shifted_points, thickness)

triangle = [(10, 0), (0, 17), (20, 17)]
canvas.fill(pg.Color("goldenrod"))
for y0 in range(0, height, 17):
    for x0 in range(0, width, 20):
        draw_polygon(triangle, pg.Color("brown"), x0, y0, 0)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
