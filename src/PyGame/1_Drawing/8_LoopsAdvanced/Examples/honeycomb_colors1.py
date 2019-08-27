# -*- acsection: general-init -*-
import pygame as pg, pygamebg
width, height = 300, 300
canvas = pygamebg.open_window(width, height, "Colored hexagons")

# -*- acsection: main -*-
def draw_polygon(points, color, x0, y0):
    shifted_points = []
    for x, y in points:
        shifted_points.append((x+x0, y+y0))
    pg.draw.polygon(canvas, color, shifted_points)

hexagon = [(10, 0), (30, 0), (40, 17), (30, 34), (10, 34), (0, 17)]
for y0 in range(-17, height, 102):
    for x0 in range(-10, width, 60):
        draw_polygon(hexagon, pg.Color("blue"),   x0, y0)
        draw_polygon(hexagon, pg.Color("yellow"), x0, y0 + 34)
        draw_polygon(hexagon, pg.Color("green"),  x0, y0 + 68)
        draw_polygon(hexagon, pg.Color("green"),  x0 + 30, y0 + 17)
        draw_polygon(hexagon, pg.Color("blue"),   x0 + 30, y0 + 51)
        draw_polygon(hexagon, pg.Color("yellow"), x0 + 30, y0 + 85)

# -*- acsection: after-main -*-
pygamebg.wait_loop()
