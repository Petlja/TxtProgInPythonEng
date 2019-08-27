# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Octagons")
# -*- acsection: main -*-

def draw_framed_polygon(points, color, frame_color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points)
    pg.draw.polygon(canvas, frame_color, shifted_points, 2)

octagon = [(14, 0), (34, 0), (48, 14), (48, 34), (34, 48), (14, 48), (0, 34), (0, 14)]
canvas.fill(pg.Color("yellow"))
for y0 in range(0, height, 48):
    for x0 in range(0, width, 48):
        draw_framed_polygon(octagon, pg.Color("lightgreen"), pg.Color("red"), x0, y0)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
